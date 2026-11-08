# V-Sentinel

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team 2vane
- Authors: Lê Huy Hùng, Nguyễn Trần Minh Tâm
- Date / location: Jun 21, 2026 / Hồ Chí Minh
- Page: https://apartresearch.com/sprints/projects/vsentinel-bio7
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/1e18a2c7f72ea9cc-aab08b47-5ed1-42fe-ac45-e1b2fd0ba7a4-v-sentinel-report.pdf
- Code: https://github.com/2vane/visen
- Code links found in report: https://github.com/2vane/visen
- Recording: https://drive.google.com/file/d/14a5Mz35zz0tQeaga_6XbuS-s6BKAS07F/view?usp=sharing

## Summary

AI safety tooling is overwhelmingly built and benchmarked in English and degrades sharply on low-resource languages — a critical gap as Vietnam deploys AI in public services, healthcare, and education under Decree 142/2026/ND-CP. We present V-Sentinel, a dual-control guardrail that pairs a deterministic, OWASP-tagged rule backbone with an LLM safety classifier and fails closed. A non-destructive normalization layer neutralizes Vietnamese-specific evasion (teencode, leetspeak, diacritic folding, Base64) without corrupting legitimate text; a domain-aware GraphRAG layer attaches the jurisdictionally correct legal frame (ND-142/PDPD, FERPA, COPPA, HIPAA); a REFRAME mechanism converts over-refusal of legitimate sensitive queries into responsible, cited answers; and an output stage redacts Vietnamese PII. On two Vietnamese benchmarks, V-Sentinel flags ∼90% of harmful prompts and the rule backbone alone blocks 64% of injection attacks with no model call — still flagging 100% under classifier outage. An ablation shows the two controls are complementary rather than redundant: rules carry the obfuscation/injection axis and provide the fail-closed guarantee, while the classifier carries content-harm. Against published Llama Guard results, which fall to 51% recall on adversarial prompts and degrade multilingually, V-Sentinel sustains ∼90% on Vietnamese. The main takeaway: a thin, local-first, law-grounded guardrail makes an open model compliant without the cost of fine-tuning a sovereign model, and re-targets to any jurisdiction by swapping its rule pack and legal graph.

## Reviews (4)

### Review 1

V Sentinel addresses a genuine gap: English centric guardrails degrade on Vietnamese, and the populations most reliant on public sector AI are the least protected. The dual control architecture, pairing a deterministic rule backbone with an LLM classifier, is a well motivated design choice. The strongest evidence for this is the ablation in Table 3, which shows the two controls cover complementary axes. Rules handle injection and obfuscation; the classifier handles content harm. Neither alone spans the full threat surface, and their combination provides measurable fail closed coverage under classifier outage. This is the paper's most convincing result. The legal grounding via GraphRAG is an interesting addition that ties decisions to specific articles of Vietnamese law, though its validation in the paper is light. The over refusal story needs more scrutiny. The paper presents REFRAME as a solution to over refusal, but 11% hard refusal plus 54% of benign prompts receiving a cautioned answer means 65% of legitimate queries get a degraded experience. For a citizen interacting with a public service chatbot, receiving a hedged, citation laden response to a straightforward health or education question is still a usability cost. A breakdown of which benign query types trigger REFRAME, and whether users perceive it as helpful or obstructive, would strengthen the argument that this is mitigation rather than a different flavor of the same problem.

Evaluation rigor is another area for improvement. Results are single run on two benchmarks without confidence intervals. The deterministic rule results reproduce by design, which is a genuine strength, but the classifier dependent numbers could vary across runs and this is never quantified. Reporting even minimal variance (three runs, standard deviation) would add credibility at low cost.

The scope is appropriate for a hackathon. The system is open source, the test suite is substantial (151 tests across 27 files), and the architecture is clearly described. The writing is generally clear and well structured. The main areas to develop post hackathon are: running direct baselines on Vietnamese prompts, building a dedicated over refusal suite, and addressing the subtle harm categories (disinformation, discrimination) where detection currently sits at 20 to 58 percent.

### Review 2

A well-executed systems-oriented AI safety project addressing an important gap in multilingual guardrails for Vietnamese public-sector applications. The dual-control architecture combining deterministic rules with an LLM classifier is well motivated, and the integration of legal grounding, PII protection, and fail-closed behavior demonstrates strong practical engineering.

The project would be strengthened by:

- Expanding evaluation to adaptive jailbreaks, code-switching attacks, and additional robustness benchmarks.
- Reporting confidence intervals and latency measurements to better demonstrate deployment readiness.
- Providing deeper analysis of false positives and over-refusal

### Review 3

Amazing concept. Keep up the good work.

### Review 4

Good project idea which solve the existed gap in using AI for everyone in Vietnam

