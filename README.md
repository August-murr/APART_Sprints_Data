# APART Sprints Data

Submissions from nine recent [Apart Research](https://apartresearch.com/sprints) sprints, collected as training and evaluation data for an AI judge that rates sprint submissions.

447 submissions: up to 50 per sprint, including every officially ranked winner.

| Sprint | Submissions |
|---|---|
| AI Incident Response Sprint (Sep 2026) | 50 of 231 |
| Digital Minds Research Sprint (Aug 2026) | 50 of 233 |
| Secret Loyalties Hackathon (Jul 2026) | 50 of 177 |
| Global South AI Safety Hackathon (Jun 2026) | 50 of 216 |
| Secure Program Synthesis Hackathon (May 2026) | 50 of 61 |
| AI Control Hackathon (Mar 2026) | 50 of 125 |
| Technical AI Governance Challenge (Jan 2026) | 47 of 47 |
| AI Manipulation Hackathon (Jan 2026) | 50 of 70 |
| Defensive Acceleration Hackathon (Nov 2025) | 50 of 83 |

## Layout

```
data/
  rubric.json                      APART's judging criteria, each with a 1-5 scoring guide
  selection.json                   selected submissions per sprint: rank, awards, why selected, review count
  index/all_projects.jsonl         metadata and reviews for all 1,243 projects in these sprints
  sprints/<sprint>/
    sprint.md                      sprint page: Overview, Resources, Guidelines
    projects/<project>/
      report.md                    the submitted PDF report, converted to Markdown
      project.md                   metadata, rank, awards, summary, judge reviews, code links
scraper/
  scrape.py                        rebuilds the dataset from the website
  winners.json                     official placements (from the Apart Discord announcements)
```

## Using it for a judge

- **Inputs:** `report.md` (plus the summary and code link in `project.md`) and `sprint.md` for context.
- **Labels:** `rank`, `awards` and the judge `reviews`, all in `project.md`. The reviews are text only; the site does not publish numeric scores.
- `project.md` contains the rank and reviews, so do not feed it to the judge as input.
- `sprint.md` has the winners announcement removed. Check it again if you re-scrape.

## Notes

- Ranks come from `scraper/winners.json`. The website does not show them for every sprint. Where several teams tied, more than five projects share a rank (Defensive Acceleration has 10, Global South has 6 regional first places).
- Track winners and honorable mentions are kept but unranked (`selection_reason: other_award`).
- The rest of each sprint's 50 is a random sample (seed 42) that prefers projects with reviews. Defensive Acceleration only has 26 reviewed projects among its selection.
- Reports are converted from PDF automatically, so figures are lost and tables or equations may be imperfect.

## Rebuilding

```
pip install -r scraper/requirements.txt
python3 scraper/scrape.py
```

Pages and PDFs are cached in `.cache/` (git-ignored), so re-runs are fast and give the same selection. Conversion takes about 20 minutes on 2 cores.
