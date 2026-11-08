"""Scrape APART Research sprint pages and a sample of their submissions.

Stages (each resumable; raw HTML is cached in .cache/html):
  1. sprints  - fetch sprint pages -> data/sprints/<slug>/{raw.html,sprint.md,sprint.json}
  2. index    - fetch every project page of those sprints -> data/index/all_projects.jsonl
  3. select   - all 1st-5th place winners + reviewed/random fill to N -> data/selection.json
  4. download - PDF reports + text extraction + per-project folders, manifest.csv

Usage:
  python scraper/scrape.py                 # all stages, all sprints
  python scraper/scrape.py --sprints def-acc-hackathon-2025-11-21-to-2025-11-23
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
import re
import shutil
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests
from bs4 import BeautifulSoup, NavigableString, Tag

BASE = "https://apartresearch.com"
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CACHE = ROOT / ".cache" / "html"
UA = "APART-dataset-scraper/1.0 (research dataset for an AI judge)"

SPRINTS = [
    "ai-incident-response-sprint-2026-09-11-to-2026-09-13",
    "digital-minds-research-sprint-2026-08-14-to-2026-08-16",
    "secret-loyalties-hackathon-2026-07-24-to-2026-07-26",
    "global-south-ais-hackathon-2026-06-19-to-2026-06-21",
    "secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24",
    "ai-control-hackathon-2026-03-20-to-2026-03-22",
    "the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01",
    "ai-manipulation-hackathon-2026-01-09-to-2026-01-11",
    "def-acc-hackathon-2025-11-21-to-2025-11-23",
]

PROJECT_HREF = re.compile(r'href="/sprints/projects/([a-z0-9-]+)"')
RANK_RE = re.compile(r"^\s*(\d+)(?:st|nd|rd|th)\s+place", re.I)
GITHUB_RE = re.compile(r"https?://(?:www\.)?github\.com/[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)?", re.I)

# --------------------------------------------------------------------------- http

_session = threading.local()
_rate_lock = threading.Lock()
_last_request = [0.0]
MIN_INTERVAL = 0.35  # seconds between requests across all threads


def session() -> requests.Session:
    if not hasattr(_session, "s"):
        s = requests.Session()
        s.headers["User-Agent"] = UA
        _session.s = s
    return _session.s


def _throttle():
    with _rate_lock:
        wait = _last_request[0] + MIN_INTERVAL - time.monotonic()
        if wait > 0:
            time.sleep(wait)
        _last_request[0] = time.monotonic()


def get(url: str, binary: bool = False, tries: int = 5):
    for attempt in range(tries):
        _throttle()
        try:
            r = session().get(url, timeout=60)
            if r.status_code == 200:
                return r.content if binary else r.text
            if r.status_code == 404:
                return None
            err = f"HTTP {r.status_code}"
        except requests.RequestException as e:
            err = str(e)
        time.sleep(2 ** attempt)
    print(f"  !! failed {url}: {err}", file=sys.stderr)
    return None


def get_cached(url: str) -> str | None:
    CACHE.mkdir(parents=True, exist_ok=True)
    f = CACHE / (hashlib.sha1(url.encode()).hexdigest() + ".html")
    if f.exists():
        return f.read_text()
    html = get(url)
    if html is not None:
        f.write_text(html)
    return html


# --------------------------------------------------------------------------- html -> markdown


def _clean(s: str) -> str:
    return re.sub(r"[ \t\r\f\v]+", " ", s)


def to_md(node, base: str = BASE) -> str:
    """Small HTML->Markdown converter good enough for the CMS content on apartresearch.com."""

    def inline(n) -> str:
        if isinstance(n, NavigableString):
            return _clean(str(n))
        if not isinstance(n, Tag):
            return ""
        name = n.name
        inner = "".join(inline(c) for c in n.children)
        if name in ("strong", "b"):
            return f"**{inner.strip()}**" if inner.strip() else ""
        if name in ("em", "i"):
            return f"*{inner.strip()}*" if inner.strip() else ""
        if name == "code":
            return f"`{inner}`"
        if name == "br":
            return "\n"
        if name == "a":
            href = n.get("href", "")
            if href.startswith("/"):
                href = base + href
            text = inner.strip()
            return f"[{text}]({href})" if href and text else text
        if name == "img":
            return f"![{n.get('alt', '')}]({n.get('src', '')})"
        return inner

    out: list[str] = []

    def block(n, depth: int = 0):
        if isinstance(n, NavigableString):
            t = _clean(str(n)).strip()
            if t:
                out.append(t)
            return
        if not isinstance(n, Tag):
            return
        name = n.name
        if name in ("script", "style", "svg", "dialog", "form", "button", "noscript", "input"):
            return
        if re.fullmatch(r"h[1-6]", name):
            t = inline(n).strip()
            if t:
                out.append("#" * int(name[1]) + " " + t)
        elif name == "p":
            t = inline(n).strip()
            if t:
                out.append(t)
        elif name in ("ul", "ol"):
            items = []
            for i, li in enumerate(n.find_all("li", recursive=False), 1):
                bullet = f"{i}." if name == "ol" else "-"
                parts, sub = [], []
                for c in li.children:
                    if isinstance(c, Tag) and c.name in ("ul", "ol"):
                        sub.append(c)
                    elif isinstance(c, Tag) and c.name in ("p", "div"):
                        parts.append(inline(c).strip())
                    else:
                        parts.append(inline(c))
                text = " ".join(p.strip() for p in parts if p.strip())
                items.append("  " * depth + f"{bullet} {text}")
                for s in sub:
                    saved = len(out)
                    block(s, depth + 1)
                    items.extend(out[saved:])
                    del out[saved:]
            if items:
                out.append("\n".join(items))
        elif name == "table":
            rows = []
            for tr in n.find_all("tr"):
                cells = [inline(c).strip().replace("|", "\\|") for c in tr.find_all(["td", "th"])]
                rows.append("| " + " | ".join(cells) + " |")
            if rows:
                ncol = rows[0].count("|") - 1
                rows.insert(1, "|" + " --- |" * ncol)
                out.append("\n".join(rows))
        elif name == "blockquote":
            t = inline(n).strip()
            if t:
                out.append("> " + t.replace("\n", "\n> "))
        elif name == "pre":
            out.append("```\n" + n.get_text() + "\n```")
        elif name == "hr":
            out.append("---")
        else:
            # container: if it only holds inline content, emit it as one paragraph
            if not n.find(["p", "div", "ul", "ol", "h1", "h2", "h3", "h4", "h5", "h6", "table", "section", "li", "pre"]):
                t = inline(n).strip()
                if t:
                    out.append(t)
            else:
                for c in n.children:
                    block(c, depth)

    block(node)
    md = "\n\n".join(x for x in out if x.strip())
    return re.sub(r"\n{3,}", "\n\n", md).strip()


# --------------------------------------------------------------------------- sprint pages


def parse_sprint(slug: str, html: str) -> tuple[dict, str]:
    soup = BeautifulSoup(html, "html.parser")
    main = soup.find("main") or soup
    for t in main(["script", "style", "svg", "dialog", "form"]):
        t.decompose()

    info: dict = {"slug": slug, "url": f"{BASE}/sprints/{slug}"}
    h1 = main.find("h1")
    info["title"] = h1.get_text(" ", strip=True) if h1 else slug

    hero = main.find("section", class_="sprint-hero")
    hero_text = hero.get_text("\n", strip=True).split("\n") if hero else []
    info["hero_lines"] = hero_text
    m = re.search(r"Sign-ups\s*\n?\s*([\d,]+)", "\n".join(hero_text))
    info["signups"] = int(m.group(1).replace(",", "")) if m else None
    m = re.search(r"Projects submitted\s*\n?\s*([\d,]+)", "\n".join(hero_text))
    info["projects_submitted"] = int(m.group(1).replace(",", "")) if m else None
    lead = main.find("p", class_="sprint-hero-lead")
    info["lead"] = lead.get_text(" ", strip=True) if lead else None

    md_parts = [f"# {info['title']}", f"Source: {info['url']}"]
    if hero:
        skip = {"Programs", "/", "Sprints", "·", info["title"], "See upcoming Sprints", "Sign-ups", "Projects submitted"}
        dates = next((l for l in hero_text if re.match(r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d", l) and len(l) < 40), None)
        meta = [f"- Dates: {dates}" if dates else None,
                f"- Sign-ups: {info['signups']}", f"- Projects submitted: {info['projects_submitted']}"]
        rest = [l for l in hero_text if l not in skip and l != dates and not l.startswith("Browse the")
                and not re.fullmatch(r"[\d,]+", l)]
        md_parts.append("\n".join([m for m in meta if m] + [f"- {l}" for l in rest]))

    # tabbed details (Entries / Overview / Resources / Guidelines / Schedule ...)
    tabs = [t.get_text(" ", strip=True) for t in main.find_all(attrs={"role": "tab"})]
    panels = main.find_all(attrs={"role": "tabpanel"})
    info["tabs"] = tabs
    resource_links = []
    for name, panel in zip(tabs, panels):
        if name.lower() == "entries":
            continue
        body = to_md(panel)
        if body.split("\n", 1)[0].lstrip("# ").strip() == name:
            body = body.split("\n", 1)[1].lstrip() if "\n" in body else ""
        md_parts.append(f"## {name}\n\n" + body)
        if name.lower() == "resources":
            for a in panel.find_all("a", href=True):
                resource_links.append({"text": a.get_text(" ", strip=True), "href": a["href"]})
    info["resource_links"] = resource_links

    # other informative sections (speakers, local sites); skip generic marketing blocks
    for sec in main.find_all("section", recursive=True):
        cls = " ".join(sec.get("class") or [])
        if "sprint-hero" in cls or "sprint-details" in cls or not cls:
            continue
        h2 = sec.find("h2")
        title = h2.get_text(" ", strip=True) if h2 else ""
        if title in ("Upcoming Sprints", "Where a Sprint can lead"):
            continue
        md_parts.append(to_md(sec))

    info["project_slugs"] = sorted(set(PROJECT_HREF.findall(html)) - {"opengraph-image"})
    return info, "\n\n".join(md_parts) + "\n"


def stage_sprints(sprints: list[str]) -> dict[str, dict]:
    out = {}
    for slug in sprints:
        print(f"[sprint] {slug}")
        html = get_cached(f"{BASE}/sprints/{slug}")
        if html is None:
            print("  !! could not fetch sprint page", file=sys.stderr)
            continue
        d = DATA / "sprints" / slug
        d.mkdir(parents=True, exist_ok=True)
        (d / "raw.html").write_text(html)
        info, md = parse_sprint(slug, html)
        (d / "sprint.md").write_text(md)
        (d / "sprint.json").write_text(json.dumps(info, indent=2, ensure_ascii=False))
        print(f"  {len(info['project_slugs'])} projects, tabs={info['tabs']}")
        out[slug] = info
    return out


# --------------------------------------------------------------------------- project pages


def parse_project(slug: str, html: str) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    p: dict = {"slug": slug, "url": f"{BASE}/sprints/projects/{slug}"}

    # sprint from JSON-LD breadcrumb
    for s in soup.find_all("script", type="application/ld+json"):
        try:
            ld = json.loads(s.string or "")
        except json.JSONDecodeError:
            continue
        if ld.get("@type") == "BreadcrumbList":
            for it in ld.get("itemListElement", []):
                if it.get("position") == 3:
                    p["sprint_name"] = it.get("name")
                    p["sprint_slug"] = it.get("item", "").rstrip("/").split("/")[-1]

    header = None
    h1 = soup.find("h1")
    if h1:
        header = h1.find_parent("header")
        p["title"] = h1.get_text(" ", strip=True)

    # meta row: "Sprint project" | date | location | badges
    p["date"] = p["location"] = None
    p["awards"] = []
    if h1:
        meta = h1.find_previous_sibling("div")
        if meta:
            spans = [c for c in meta.children if isinstance(c, Tag)]
            texts = [c.get_text(" ", strip=True) for c in spans if c.name == "span"]
            texts = [t for t in texts if t and t != "Sprint project"]
            if texts:
                p["date"] = texts[0]
            if len(texts) > 1:
                p["location"] = texts[1]
            for c in spans:
                if c.name == "div":
                    p["awards"] = [s.get_text(" ", strip=True) for s in c.find_all("span") if s.get_text(strip=True)]
    p["rank"] = None
    for a in p["awards"]:
        m = RANK_RE.match(a)
        if m:
            r = int(m.group(1))
            p["rank"] = r if p["rank"] is None else min(p["rank"], r)

    # authors / team
    p["authors"], p["team"] = [], None
    if h1:
        ap = h1.find_next_sibling("p")
        if ap:
            team_span = ap.find("span")
            if team_span:
                p["team"] = re.sub(r"^\s*·\s*", "", team_span.get_text(" ", strip=True)) or None
                team_span.extract()
            names = ap.get_text(" ", strip=True)
            p["authors"] = [n.strip() for n in names.split(",") if n.strip()]

    # links block + summary (siblings following the header)
    p["pdf_url"] = p["code_url"] = None
    p["links"] = []
    p["summary"] = ""
    if header:
        sib = header.find_next_sibling("div")
        if sib:
            for a in sib.find_all("a", href=True):
                href, text = a["href"], a.get_text(" ", strip=True).replace("(opens in new tab)", "").strip()
                if "twitter.com/intent" in href or "linkedin.com/sharing" in href:
                    continue
                if href.lower().split("?")[0].endswith(".pdf") and text.lower().startswith("read the report"):
                    p["pdf_url"] = p["pdf_url"] or href
                    continue
                if text.lower() == "code":
                    p["code_url"] = href
                    continue
                if text.lower().startswith("open in a new tab"):
                    continue
                p["links"].append({"text": text, "href": href})
            summ = sib.find_next_sibling("div")
            if summ:
                p["summary"] = to_md(summ)
    if not p["pdf_url"]:
        m = re.search(r'href="(https://[^"]+\.pdf)"', html)
        p["pdf_url"] = m.group(1) if m else None

    # reviews
    p["reviews"] = []
    for li in soup.select("li.project-review"):
        body = li.select_one(".prose-cms") or li
        txt = to_md(body)
        if txt:
            p["reviews"].append(txt)
    # e.g. a judge declined to score
    p["n_reviews"] = len(p["reviews"])

    # bibtex
    m = re.search(r"(@misc\{.*?\n\})", BeautifulSoup(html, "html.parser").get_text(), re.S)
    p["bibtex"] = m.group(1) if m else None
    return p


def parse_rubric(html: str) -> dict:
    """Extract the judging criteria from the 'Submit a review' dialog on a project page."""
    soup = BeautifulSoup(html, "html.parser")
    dlg = None
    for d in soup.find_all("dialog"):
        if "Scoring guide" in d.get_text():
            dlg = d
            break
    if dlg is None:
        return {}
    lines = [l.strip() for l in dlg.get_text("\n").split("\n") if l.strip()]
    criteria = []
    i = 0
    while i < len(lines):
        if lines[i] == "Scoring guide":
            # look back for "<name>", "*", "<description>" (+ optional note)
            j = i - 1
            back = []
            while j >= 0 and lines[j] != "*":
                back.insert(0, lines[j])
                j -= 1
            name = lines[j - 1] if j >= 1 else "?"
            guide = {}
            k = i + 1
            while k + 1 < len(lines) and re.fullmatch(r"[1-5]", lines[k]) and str(len(guide) + 1) == lines[k]:
                guide[lines[k]] = lines[k + 1]
                k += 2
            criteria.append({"name": name, "description": " ".join(back), "scale": guide})
            i = k
        else:
            i += 1
    return {"source": "apartresearch.com project review form", "criteria": criteria, "raw_text": "\n".join(lines)}


def stage_index(sprint_infos: dict[str, dict], workers: int) -> list[dict]:
    jobs = [(s, slug) for s, info in sprint_infos.items() for slug in info["project_slugs"]]
    print(f"[index] {len(jobs)} project pages")
    done = [0]
    lock = threading.Lock()

    def work(job):
        sprint, slug = job
        html = get_cached(f"{BASE}/sprints/projects/{slug}")
        with lock:
            done[0] += 1
            if done[0] % 50 == 0:
                print(f"  {done[0]}/{len(jobs)}")
        if html is None:
            return {"slug": slug, "sprint_slug": sprint, "error": "fetch failed"}
        p = parse_project(slug, html)
        p["listed_in_sprint"] = sprint
        return p

    with ThreadPoolExecutor(workers) as ex:
        projects = list(ex.map(work, jobs))

    mismatched = [p["slug"] for p in projects if p.get("sprint_slug") and p["sprint_slug"] != p["listed_in_sprint"]]
    if mismatched:
        print(f"  note: {len(mismatched)} projects belong to a different sprint than the page that linked them", file=sys.stderr)

    (DATA / "index").mkdir(parents=True, exist_ok=True)
    with open(DATA / "index" / "all_projects.jsonl", "w") as f:
        for p in projects:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")

    if projects and "error" not in projects[0]:
        html = get_cached(projects[0]["url"])
        rub = parse_rubric(html or "")
        if rub:
            (DATA / "rubric.json").write_text(json.dumps(rub, indent=2, ensure_ascii=False))
    return projects


# --------------------------------------------------------------------------- official winners


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (s or "").lower())


def apply_winners(projects: list[dict], path: Path) -> None:
    """Merge the hand-maintained winners list (from the Discord announcements) into the projects.

    The site shows rank badges for some sprints only. Official placements override the site badges.
    The original badge data is kept in site_rank / site_awards."""
    winners = json.loads(path.read_text())
    for p in projects:
        p["site_rank"], p["site_awards"] = p.get("rank"), list(p.get("awards") or [])
        p["official_awards"] = []
        p["rank_source"] = "site" if p.get("rank") else None
    by_sprint: dict[str, list[dict]] = {}
    for p in projects:
        if "error" not in p:
            by_sprint.setdefault(p["listed_in_sprint"], []).append(p)
    for sprint, entries in winners.items():
        if sprint.startswith("_") or sprint not in by_sprint:
            continue
        ps = by_sprint[sprint]
        official_rank: dict[str, int] = {}
        for e in entries:
            if "slug" in e:
                match = [p for p in ps if p["slug"] == e["slug"]]
            else:
                match = [p for p in ps if _norm(p.get("title")) == _norm(e["title"])]
            if len(match) != 1:
                print(f"  !! winners.json: {sprint}: {e.get('slug') or e.get('title')!r} matched {len(match)} projects",
                      file=sys.stderr)
                continue
            p = match[0]
            p["official_awards"].append(e["award"])
            if e.get("rank"):
                official_rank[p["slug"]] = min(e["rank"], official_rank.get(p["slug"], 99))
        # the official list is authoritative for this sprint's placements
        for p in ps:
            p["rank"] = official_rank.get(p["slug"])
            p["rank_source"] = "official" if p["rank"] else None
    for p in projects:
        merged = list(p.get("official_awards") or [])
        for a in p.get("site_awards") or []:
            if not any(_norm(a) in _norm(m) or _norm(m) in _norm(a) for m in merged):
                merged.append(a)
        p["awards"] = merged


# --------------------------------------------------------------------------- selection


def stage_select(projects: list[dict], n: int, seed: int) -> dict:
    by_sprint: dict[str, list[dict]] = {}
    for p in projects:
        if "error" in p:
            continue
        sprint = p["listed_in_sprint"]
        # only keep projects that actually belong to this sprint
        if p.get("sprint_slug") and p["sprint_slug"] != sprint:
            continue
        by_sprint.setdefault(sprint, []).append(p)

    sel = {"seed": seed, "target_per_sprint": n, "sprints": {}}
    for sprint, ps in by_sprint.items():
        rng = random.Random(f"{seed}:{sprint}")
        ranked = sorted([p for p in ps if p["rank"] and p["rank"] <= 5], key=lambda p: (p["rank"], p["slug"]))
        # non-placement official awards (track winners, honorable mentions) are always kept too
        other_award = sorted([p for p in ps if p not in ranked and p.get("official_awards")], key=lambda p: p["slug"])
        rest = sorted([p for p in ps if p not in ranked and p not in other_award], key=lambda p: p["slug"])
        reviewed = [p for p in rest if p["n_reviews"] > 0]
        unreviewed = [p for p in rest if p["n_reviews"] == 0]
        rng.shuffle(reviewed)
        rng.shuffle(unreviewed)
        chosen = [(p, "winner") for p in ranked] + [(p, "other_award") for p in other_award]
        for p in reviewed + unreviewed:
            if len(chosen) >= n:
                break
            chosen.append((p, "sample_reviewed" if p["n_reviews"] else "sample_unreviewed"))
        sel["sprints"][sprint] = {
            "total_projects": len(ps),
            "n_ranked": len(ranked),
            "selected": [{"slug": p["slug"], "rank": p["rank"], "reason": why} for p, why in chosen],
        }
        print(f"[select] {sprint}: {len(chosen)}/{len(ps)} (ranked {len(ranked)}, reviewed pool {len(reviewed)})")
    (DATA / "selection.json").write_text(json.dumps(sel, indent=2))
    return sel


# --------------------------------------------------------------------------- downloads


def pdf_to_text(path: Path) -> str:
    try:
        from pypdf import PdfReader

        reader = PdfReader(str(path))
        pages = []
        for i, page in enumerate(reader.pages, 1):
            try:
                t = page.extract_text() or ""
            except Exception as e:  # noqa: BLE001 - malformed pages shouldn't kill the run
                t = f"[text extraction failed: {e}]"
            pages.append(f"\n\n===== page {i} =====\n\n{t}")
        return "".join(pages).strip()
    except Exception as e:  # noqa: BLE001
        return f"[could not read PDF: {e}]"


def project_md(p: dict) -> str:
    lines = [f"# {p.get('title')}", ""]
    lines.append(f"- Sprint: {p.get('sprint_name')} ({p.get('sprint_slug')})")
    lines.append(f"- Rank: {p['rank'] if p.get('rank') else 'unranked'}")
    if p.get("awards"):
        lines.append(f"- Awards: {', '.join(p['awards'])}")
    lines.append(f"- Team: {p.get('team')}")
    lines.append(f"- Authors: {', '.join(p.get('authors') or [])}")
    lines.append(f"- Date / location: {p.get('date')} / {p.get('location')}")
    lines.append(f"- Page: {p['url']}")
    lines.append(f"- Report: {p.get('pdf_url')}")
    lines.append(f"- Code: {p.get('code_url')}")
    if p.get("code_urls_from_report"):
        lines.append(f"- Code links found in report: {', '.join(p['code_urls_from_report'])}")
    for l in p.get("links") or []:
        lines.append(f"- {l['text']}: {l['href']}")
    lines += ["", "## Summary", "", p.get("summary") or "", "", f"## Reviews ({p.get('n_reviews', 0)})", ""]
    for i, r in enumerate(p.get("reviews") or [], 1):
        lines += [f"### Review {i}", "", r, ""]
    return "\n".join(lines) + "\n"


def stage_download(projects: list[dict], sel: dict, workers: int):
    by_slug = {p["slug"]: p for p in projects if "error" not in p}
    jobs = []
    for sprint, s in sel["sprints"].items():
        for item in s["selected"]:
            jobs.append((sprint, item))
    print(f"[download] {len(jobs)} selected projects")
    # drop folders left over from earlier runs whose project is no longer selected
    keep = {(sp, it["slug"]) for sp, it in jobs}
    for sp in sel["sprints"]:
        pdir = DATA / "sprints" / sp / "projects"
        if pdir.exists():
            for d in pdir.iterdir():
                if d.is_dir() and (sp, d.name) not in keep:
                    shutil.rmtree(d)

    def work(job):
        sprint, item = job
        p = dict(by_slug[item["slug"]])
        p["selection_reason"] = item["reason"]
        d = DATA / "sprints" / sprint / "projects" / p["slug"]
        d.mkdir(parents=True, exist_ok=True)
        pdf = d / "report.pdf"
        if p.get("pdf_url") and not (pdf.exists() and pdf.stat().st_size > 0):
            content = get(p["pdf_url"], binary=True)
            if content and content[:5] == b"%PDF-":
                pdf.write_bytes(content)
            elif content:
                p["pdf_error"] = "downloaded file is not a PDF"
            else:
                p["pdf_error"] = "download failed"
        p["has_pdf"] = pdf.exists()
        txt = d / "report.txt"
        if p["has_pdf"]:
            if not txt.exists():
                txt.write_text(pdf_to_text(pdf))
            text = txt.read_text()
            p["report_chars"] = len(text)
            seen = []
            for u in GITHUB_RE.findall(text):
                u = u.rstrip(".")
                if u.lower() not in [x.lower() for x in seen] and not u.lower().endswith("github.com/apartresearch"):
                    seen.append(u)
            p["code_urls_from_report"] = seen
        else:
            p["report_chars"] = 0
            p["code_urls_from_report"] = []
        (d / "project.json").write_text(json.dumps(p, indent=2, ensure_ascii=False))
        (d / "project.md").write_text(project_md(p))
        return sprint, p

    with ThreadPoolExecutor(workers) as ex:
        results = list(ex.map(work, jobs))

    with open(DATA / "manifest.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["sprint", "slug", "title", "rank", "rank_source", "awards", "selection_reason", "n_reviews", "has_pdf",
                    "report_chars", "code_url", "code_urls_from_report", "url"])
        for sprint, p in results:
            w.writerow([sprint, p["slug"], p.get("title"), p.get("rank") or "", p.get("rank_source") or "", "; ".join(p.get("awards") or []),
                        p["selection_reason"], p.get("n_reviews", 0), p["has_pdf"], p.get("report_chars", 0),
                        p.get("code_url") or "", " ".join(p.get("code_urls_from_report") or []), p["url"]])
    missing = [p["slug"] for _, p in results if not p["has_pdf"]]
    print(f"  done. missing PDFs: {len(missing)}")
    for m in missing:
        print(f"    - {m}")


# --------------------------------------------------------------------------- main


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sprints", nargs="*", default=SPRINTS)
    ap.add_argument("--n", type=int, default=50, help="submissions per sprint (winners included)")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()

    infos = stage_sprints(args.sprints)
    projects = stage_index(infos, args.workers)
    apply_winners(projects, Path(__file__).with_name("winners.json"))
    with open(DATA / "index" / "all_projects.jsonl", "w") as f:
        for p in projects:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")
    sel = stage_select(projects, args.n, args.seed)
    stage_download(projects, sel, args.workers)


if __name__ == "__main__":
    main()
