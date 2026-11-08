# V-Sentinel: A Dual-Control Guardrail for Vietnamese Public-Service, Healthcare, and Education Chatbots 

Le Huy Hung Nguyen Tran Minh Tam Team 2vane Team 2vane huyhungvtu@gmail.com nguyentranminhtam04@gmail.com 

With 

Apart Research 

### Abstract 

AI safety tooling is overwhelmingly built and benchmarked in English and degrades sharply on low-resource languages  a critical gap as Vietnam deploys AI in public services, healthcare, and education under Decree 142/2026/ND-CP. We present V-Sentinel, a dual-control guardrail that pairs a deterministic, OWASP-tagged rule backbone with an LLM safety classier and fails closed. A non-destructive normalization layer neutralizes Vietnamesespecic evasion (teencode, leetspeak, diacritic folding, Base64) without corrupting legitimate text; a domain-aware GraphRAG layer attaches the jurisdictionally correct legal frame (ND-142/PDPD, FERPA, COPPA, HIPAA); a REFRAME mechanism converts over-refusal of legitimate sensitive queries into responsible, cited answers; and an output stage redacts Vietnamese PII. On two Vietnamese benchmarks, V-Sentinel ags _∼_ 90% of harmful prompts and the rule backbone alone blocks 64% of injection attacks with no model call still agging 100% under classier outage. An ablation shows the two controls are complementary rather than redundant: rules carry the obfuscation/injection axis and provide the fail-closed guarantee, while the classier carries content-harm. Against published Llama Guard results, which fall to 51% recall on adversarial prompts and degrade multilingually, V-Sentinel sustains _∼_ 90% on Vietnamese. The main takeaway: a thin, local-rst, law-grounded guardrail makes an open model compliant without the cost of ne-tuning a sovereign model, and re-targets to any jurisdiction by swapping its rule pack and legal graph. 

## 1 Introduction 

As AI penetrates Vietnam's public services, healthcare, and education, safety and legal compliance have become priorities: Decree 142/2026/ND-CP (implementing the Law on Articial Intelligence) sets risk-management standards for AI systems. O-the-shelf guardrails, however, are optimized for English and fail in this setting in three ways: (1) jailbreaks via Vietnam-specic obfuscation (teencode, leetspeak, unaccented text) bypass keyword lters; (2) over-refusal causes models to reject legitimate health, education, or legal questions an equity failure for citizens who most need the service; and (3) data leakage, where a model echoes Vietnamese personal data (Citizen ID, phone, insurance numbers) it should never surface. 

We assume an adversary who interacts only through the chat interface (no model/server access) and a benign-but-sensitive user population whose legitimate queries must not be overrefused. The objective is therefore two-sided: raise recall on the attack surface while lowering false refusals on the benign surface. This work asks: do English-optimized guardrails fail systematically on Vietnamese obfuscation, and can a deterministic, non-destructive normalization layer paired with an LLM classier (dual control) close that gap without inating over-refusal? Our main contributions are: 

>  A dual-control guardrail in which a deterministic, OWASP-tagged rule backbone and an LLM classier cross-check each other and fail closed, with a non-destructive normalization layer that ags never rewrites Vietnamese obfuscation (so the measurement 70kg is never corrupted to tokg). 

1 

-  A component ablation showing the two controls are complementary: the rule backbone blocks 63.8% of injection attacks with no model call (100% agged under classier outage) but _∼_ 0 on content-harm, while the classier carries content-harm  so neither alone covers both axes. 

-  Domain-aware GraphRAG that grounds each decision in the correct legal frame, an anti-over-refusal REFRAME mechanism, and an output-side PII/leakage guard delivered as an open, local-rst drop-in proxy with a fully explainable decision trace. 

## 2 Related Work 

Open guardrails such as NeMo Guardrails [5] and Llama Guard [3] are tuned for English safety standards. Multilingual jailbreak studies show low-resource languages substantially raise attacksuccess rates [1], dedicated benchmarking conrms guardrails degrade sharply on non-English toxicity and stay jailbreak-vulnerable [8], and over-refusal suites [4] show safety-tuned models reject many benign prompts. Recent learned moderators improve coverage WildGuard [6] unies prompt-harm, output-safety, and refusal detection, and Reect-Guard [7] adds logical self-reection for adversarial robustness yet both report sharp drops on adversarial inputs (Section 4). 

V-Sentinel diers by not relying on a single learned moderator. It keeps a deterministic, fail-closed rule backbone beside the model (so coverage survives model outage and obfuscation), adds an output-side PII/leakage stage, and grounds decisions in Vietnamese law via GraphRAG over the legal hierarchy (Chapter _→_ Article _→_ Clause) fused with BM25. One would choose V- Sentinel over a stand-alone moderator when deployment is Vietnamese, local-rst, and legally accountable: it provides obfuscation-robust deterministic coverage and a per-decision legal citation that a learned classier alone does not. Our risk taxonomy follows the OWASP Top 10 for LLM Applications [9]. 

## 3 Methods 

V-Sentinel is a ve-stage pipeline (Figure 1) operating independently of the chat model, governed by four principles: dual control (a deterministic rule signal and a probabilistic classier signal are fused, so each covers the other's blind spots); fail closed (the oine rule layer still decides when the model is down; generation/output checks fall back to a safe refusal); non-destructive processing (obfuscation is agged; aggressive decoding happens only on throwaway copies used for matching); and local-rst (default deployment is fully oine; the cloud graph is optional). 

2 



<!-- Start of picture text -->
User Input<br>(Vietnamese)<br>Stage 0: Normalization<br>(NFKC, anti-<br>obfuscation, de-leet)<br>Stage 1: Risk Scoring<br>Rules + LLM<br>safety classier<br>BM25 / bge-m3<br>Neo4j Graph<br>BLOCK score ≥ 0.8 Stage 2: citations<br>ND-142/2026<br>(threat / illegal) Policy Engine<br>(GraphRAG)<br>ALLOW / REFRAME<br>Stage 3: Generation<br>Qwen 2.5 + RE-<br>FRAME directive<br>Stage 4: Output Verify<br>PII redaction & safety check<br>Final response<br>+ decision trace<br><!-- End of picture text -->

Figure 1: The ve-stage V-Sentinel pipeline. The deterministic rule layer (Stage 01) decides even when the LLM is oine; the classier adds a multilingual second opinion. 

Stage 0 Normalization. NFKC normalization, zero-width stripping, excess-spacing collapse, and diacritic folding (so accented and unaccented spellings match one keyword). In-word leetspeak is agged, not rewritten; each transformation raises an auditable ag. 

Stage 1 Dual-control scoring. A rule engine scans OWASP-tagged regexes prompt injection (weight 0.9, LLM01), DAN persona (0.85), system-prompt leak (0.7, LLM07), prex injection (0.5) against several decoded views at once (per-token de-leet h4ck _→_ hack, wholestring de-leet for cross-token payloads, and Base64-decoded text); all decoding is scan-only. In parallel an LLM classier returns safe/controversial/unsafe. Fusion: rule score _≥_ 0 _._ 8 _→_ attack ; else unsafe _→_ illegal, controversial _→_ sensitive-but-legal, else benign. Any obfuscation ag nudges the score up. 

Stage 2 Policy + GraphRAG. Attack/illegal _→_ BLOCK with a cited Article of Decree 142/2026 (plus OWASP for attacks); sensitive-but-legal _→_ REFRAME (a directive forcing a responsible, cited answer instead of refusal); benign _→_ ALLOW. Domain routing over folded text attaches the correct frame (education _→_ FERPA/COPPA, health _→_ HIPAA/PDPD, publicservice _→_ PDPD/ND-142; Appendix A). Retrieval is hybrid: an oine BM25 index by default, or a Neo4j vector index (bge-m3, 1024-d [10]) fused with BM25, cross-encoder re-ranked, with NLLB-200 [11] dual-query translation for cross-lingual hits and graceful degradation if the graph is unavailable (schema in Appendix B). 

Stage 3 Generation. Qwen 2.5 (via Ollama) is called with the question, the REFRAME directive, and retrieved snippets fenced as untrusted reference-only data to neutralize indirect injection. 

Stage 4 Output verication. A fail-closed output guard re-classies the answer (block if unsafe), blocks system-prompt leakage (LLM07), and redacts eight Vietnamese PII types 

3 

(CCCD/CMND, phone, tax code, social-insurance, passport, bank, email)  addressing OWASP LLM02:2025 and the PDPD. 

Datasets, metrics, models. We evaluate on MultiJail-vi [1] (315 harmful), a Vietnamese rendering of JailbreakBench [2] (100 harmful + 100 benign, the benign half a control for overrefusal), and a 47-prompt injection set for the rule axis. We report strict detection (harmful hard-blocked), relaxed detection (blocked or reframed), and over-refusal (benign hardrefused). Models: Qwen 2.5 (chat + classier) via Ollama; bge-m3 / bge-reranker-v2-m3 / NLLB-200 for the optional graph. The full system, harness, policy les, and datasets are opensource and reproduce on a clean checkout; the deterministic results below need no model call. 

## 4 Results 

Worked examples (deterministic, reproducible oine). Table 1 runs the rule layer (no model) on representative evasion inputs: accent-folded, leetspeak, and Base64 injections all reduce to the same blocked attack, while the benign 70kg (which naive de-leeting would corrupt to tokg) passes untouched evidencing the non-destructive design. 

Table 1: Deterministic detection on evasion inputs <u>(no</u> model call; reproduces exactly). 

|Evasion technique|Input (folded for<br>display)|Verdict (rule, score)|
|---|---|---|
|Accented Vietnamese injection|bo qua moi huong dan<br>truoc do (sent with<br>full diacritics)|BLOCK  ignore_previous, 1.0|
|Leetspeak (English)|1gn0re 4ll<br>pr3v10us<br>1nstruct10ns|BLOCK  ignore_previous, 1.0|
|Base64 payload|aWdub3Jl... (= ig-<br>nore all previous in-<br>structions)|BLOCK  ignore_previous, 1.0|
|Diacritic-stripped DAN persona|kich hoat che do nha<br>phat trien|BLOCK  persona_dan, 0.85|
|Benign measurement|Toi nang 70kg, xin tu<br>van che do an|ALLOW  0.0 (70kg preserved)|



Benchmark results. Table 2 and Figure 2 report measured outcomes. V-Sentinel ags _∼_ 90% of harmful Vietnamese prompts (relaxed), with 5359% hard-blocked (strict); the gap is harmful content routed to the cautioned REFRAME path. Benign over-refusal is 11% (a further 54% of benign prompts receive a softer REFRAME rather than a refusal). Precision is 0.84 on the mixed set (1.00 on MultiJail-vi, which has no benign prompts). Per-category detection is highest on overt harms (violence 92%, privacy 90%, malware 70%) and lowest on subtle harms with few lexical markers (disinformation/expert-advice 20%, discrimination 58%)  an honest, actionable gap where the classier currently carries the load. 

Table 2: Measured V-Sentinel performance on Vietnamese benchmarks (2026-06-21). Strict = hard block; Relaxed = blocked or reframed. 

|Benchmark|N (harm/|benign)|Strict|Relaxed|Over-refusal|Precision|F1|
|---|---|---|---|---|---|---|---|
|MultiJail-vi|315|/ 0|53.3%|90.8%||1.00|0.70|
|JailbreakBench-vi|100 /|100|59.0%|90.0%|11.0%|0.84|0.69|



4 



<!-- Start of picture text -->
100 90 . 8 90<br>59<br>53 . 3<br>50<br>0<br>MultiJail-vi JailbreakBench-vi<br>Strict (hard BLOCK) Relaxed (BLOCK or REFRAME)<br>(%)Harmfulcaughtprompts<br><!-- End of picture text -->

Figure 2: Detection on Vietnamese harmful prompts: strict vs. relaxed. _∼_ 90% are caught in both suites; 5359% are hard-blocked. 

Ablation complementary, not redundant. Each control measured alone (Table 3; rule/no-guard rows need no model and reproduce exactly). The rule backbone blocks 63.8% of injection attacks on its own and, with the classier simulated oine, still ags 100% of them (fail-closed)  but _∼_ 0 on content-harm, which carries no injection syntax. Content-harm detection is carried by the classier (no-guard 0%; full system 5359% strict). Neither control alone spans both axes; their union does. 

Table 3: Component ablation strict block rate by attack axis. No-guard / rules-only need no <u>model.</u> 

|Conguration|Injection/evasion (n=47)|MultiJail-vi|JailbreakBench-vi|
|---|---|---|---|
|No guard (baseline)|0%|0%|0%|
|Rules only (deterministic, no model)|63.8%|0%|0%|
|Full dual-control|_≥_63.8%|53.3%|59.0%|



Baseline comparison. We have no spare hardware to run a learned moderator alongside our stack, so we compare against published Llama Guard results (Table 4). The pattern is consistent: Llama Guard 3 scores well on English JailbreakBench (89.7%) but collapses to 51.3% recall on its adversarial subset [7], reaches only 32.6% F1 on adversarial prompts [6], and loses F1 moving from English to multilingual [8]. V-Sentinel sustains _∼_ 90% agged on Vietnamese, which combines both weak axes (non-English and obfuscation), because its deterministic layer neutralizes the obfuscation before classication. The trade-o is a higher benign over-refusal than a permissive moderator, which REFRAME is designed to soften. 

Table 4: V-Sentinel (this work, Vietnamese) vs. published Llama Guard results. Settings/metrics dier as noted; the comparison shows where learned moderators degrade and V-Sentinel holds. 

|System|Benchmark / setting|Score|Source|
|---|---|---|---|
|No guard|any harmful prompt|0%||
|Llama Guard 3 (8B)|JailbreakBench (EN), overall detection|89.7%|[7]|
|Llama Guard 3 (8B)|JailbreakBench (EN), adversarial recall|51.3%|[7]|
|Llama Guard (1/2)|adversarial prompts (WildGuardTest), F1|32.6%|[6]|
|Llama Guard 3|ToxicChat F1, English / multilingual|46.3 / 42.2|[8]|
|V-Sentinel|JailbreakBench-vi (VI), agged|90.0%|this work|
|V-Sentinel|MultiJail-vi (VI), agged|90.8%|this work|



5 

Engineering validation. Correctness is locked in by 151 test functions across 27 les, run hermetically (oine BM25 forced, no live model/DB). Coverage spans normalization edge cases (the 70kg regression), cross-token/Base64 evasion, domain routing, policy/citation selection, PII redaction, retriever degradation, and proxy auth/rate-limiting/isolation. 

## 5 Discussion and Limitations 

The results support both halves of the research question. Dual control measurably outperforms either component alone (Table 3), and the two controls cover dierent attack axes a nding that argues against the common assumption that a single learned moderator suces, especially in non-English deployments. The fail-closed property is not just asserted but measured: under classier outage the rule layer still ags 100% of injection attacks. 

Theory of change (Global South AI safety). Safety tooling is English-centric and degrades on low-resource languages [8, 1]; the populations most reliant on public-sector chatbots are thus least protected and most exposed to over-refusal. A thin, local-rst, law-grounded guardrail closes this gap without the capital cost of ne-tuning a sovereign model, and re-targets to any jurisdiction by swapping the rule pack, PII recognizers, and legal graph a replicable pattern, not a single-country artifact. 

Limitations. Strict-block gap: _∼_ 90% agged but only 5359% hard-blocked; reframing clearlyharmful content is too lenient, and the rule pack needs category-specic patterns for subtle harms (disinformation, discrimination). Baseline: Llama Guard numbers are cited from the literature on diering setups, not run head-to-head on our Vietnamese prompts (hardware-limited); they bound the trend rather than prove it on identical inputs. Evaluation maturity: results are singlerun on two suites, without condence intervals or a frozen full-mode benchmark. Latency: up to three model calls per turn is noticeable on weak hardware. Residual risks: novel evasions outside the rule pack rely on the classier; a false safe verdict can pass at input (caught only by chance at output); data-fencing reduces but does not eliminate indirect injection; PII recall covers eight entity types only. The interpretation assumes the cited baselines transfer to Vietnamese; if Llama Guard were stronger on Vietnamese than its multilingual average, our margin would narrow. 

Future work. Run head-to-head baselines (Llama Guard 3, WildGuard) on the Vietnamese prompts; a dedicated over-refusal suite (XSTest-vi); category-specic rules for subtle harms; automated legal-corpus ingestion; and a distilled single-pass classier to cut latency. 

## 6 Conclusion 

V-Sentinel shows that a dual-control guardrail a deterministic rule backbone beside an LLM classier, with non-destructive normalization, domain-aware legal grounding, anti-over-refusal reframing, and an output-side PII guard meaningfully closes the safety gap for Vietnamese public-sector chatbots. It ags _∼_ 90% of harmful Vietnamese prompts, provides measured failclosed coverage the classier cannot, and grounds every decision in law. The ablation's core nding  that rules and classier cover complementary attack axes  generalizes beyond Vietnamese: any non-English, accountability-sensitive deployment benets from pairing deterministic, obfuscation-robust rules with a learned moderator rather than trusting either alone. 

## Code and Data 

>  Code: https://github.com/2vane/visen (Apache-2.0; library, eval harness, and raw benchmark JSON under benchmark/). 

6 

-  Data: MultiJail https://huggingface.co/datasets/DAMO-NLP-SG/MultiJail; JailbreakBench https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors. 

-  Legal source: Decree 142/2026/ND-CP, https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/ Nghi-dinh-142-2026-ND-CP-696080.aspx. 

## Author Contributions 

L.H.H. and N.T.M.T. jointly designed the system, built the pipeline and evaluation harness, ran the experiments, and wrote this report. 

## References 

- [1] Y. Deng, W. Zhang, S. J. Pan, and L. Bing. Multilingual Jailbreak Challenges in Large Language Models. ICLR, 2024. arXiv:2310.06474. 

- [2] P. Chao, E. Debenedetti, A. Robey, et al. JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models. NeurIPS Datasets and Benchmarks, 2024. arXiv:2404.01318. 

- [3] H. Inan, K. Upasani, J. Chi, et al. Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations. arXiv:2312.06674, 2023. 

- [4] P. Röttger, H. R. Kirk, B. Vidgen, et al. XSTest: A Test Suite for Identifying Exaggerated Safety Behaviours in Large Language Models. NAACL, 2024. arXiv:2308.01263. 

- [5] T. Rebedea, R. Dinu, M. Sreedhar, C. Parisien, and J. Cohen. NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications with Programmable Rails. EMNLP (System Demonstrations), 2023. arXiv:2310.10501. 

- [6] S. Han, K. Rao, A. Ettinger, et al. WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs. NeurIPS, 2024. arXiv:2406.18495. 

- [7] L. Lin, J. You, Y. Li, et al. Reect-Guard: Enhancing LLM Safeguards against Adversarial Prompts via Logical Self-Reection. arXiv:2605.24834, 2026. 

- [8] Y. Yang, S. Dan, D. Roth, and I. Lee. Benchmarking LLM Guardrails in Handling Multilingual Toxicity. arXiv:2410.22153, 2024. 

- [9] OWASP Foundation. OWASP Top 10 for Large Language Model Applications, 2025. https: //owasp.org/www-project-top-10-for-large-language-model-applications/ 

- [10] J. Chen, S. Xiao, P. Zhang, K. Luo, D. Lian, and Z. Liu. M3-Embedding: Multi-Linguality, Multi-Functionality, Multi-Granularity Text Embeddings Through Self-Knowledge Distillation. arXiv:2402.03216, 2024. 

- [11] NLLB Team. No Language Left Behind: Scaling Human-Centered Machine Translation. arXiv:2207.04672, 2022. 

7 

## A Domain-Aware Compliance Mapping 

|Domain / Risk|Action|Cited Framework(s)|
|---|---|---|
|Public Service (dich vu cong)<br>Healthcare|REFRAME<br>REFRAME|PDPD; Decree 142/2026/ND-CP (Art. 5)<br>HIPAA (45 CFR Part 164); PDPD (sensi-<br>tive health data)|
|Education|REFRAME|FERPA (20 U.S.C. 1232g); COPPA (16<br>CFR 312)|
|Prompt Injection / Jailbreak|BLOCK|OWASP LLM01:2025 (Prompt Injection)|
|System-prompt leakage (output)|BLOCK|OWASP<br>LLM07:2025<br>(System<br>Prompt<br>Leakage)|
|PII disclosure (output)|REDACT|OWASP LLM02:2025 (Sensitive Info. Dis-<br>closure); PDPD|



## B Neo4j Legal Knowledge-Graph Schema 

The graph stores 1,541 legal units from Decree 142, 473 from FERPA, and 183 from COPPA, with per-corpus bge-m3 vector indexes. NEXT links units in reading order (context expansion); REFERS_TO tracks cross-references. 



<!-- Start of picture text -->
LegalDocument<br>LegalStructure<br>• id (e.g. 142-2026-nd-cp) HAS_CHAPTER / PART HAS_SECTION<br>• title • label (Chapter, Article...) HAS_ARTICLE<br>• jurisdiction (vi, en) •• numbertitle<br>• issuing_authority<br>LegalUnit<br>ExternalLegalReference<br>• name • kind (paragraph, clause...) NEXT<br>• code • text (content)<br>• raw_reference • order<br>• reference_type • embedding [1024-d]<br>REFERS_TO<br>HAS_UNIT REFERS_TO<br>HAS_UNIT<br><!-- End of picture text -->

Figure 3: Legal knowledge-graph schema (entities, attributes, relationships) on Neo4j. 

## LLM Usage Statement 

Our team used Claude (Anthropic) throughout the project: to brainstorm the approach and architecture, to help write and refactor the code, to run the evaluation harness, and to draft this report. All V-Sentinel numbers reported here were produced by our harness and veried against its raw JSON output; the deterministic results reproduce exactly. Baseline numbers for Llama Guard are cited from published papers, not re-run by us. The team reviewed, veried, and is responsible for all claims and results. 

8 

