# Think Right, Answer Wrong

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Blue Steer
- Authors: Nilanjan Sarkar, Trisanu Bhar, Raman Rayaprolu, Margamitra Bhattacharya, Dheeraj Hegde
- Date / location: Jan 11, 2026 / Hyderabad
- Page: https://apartresearch.com/sprints/projects/think-right-answer-wrong-loku
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/85308c78b6fa0d81-swer-Wrong_-A-Comprehensive-Study-into-methods-to-detect-Sandbagging-in-LLMs.pdf
- Code: https://github.com/nilansa/blue_steer
- Code links found in report: https://github.com/nilansa/blue_steer

## Summary

This project investigates sandbagging—strategic underperformance used to conceal latent capabilities—in large language models, motivated by the safety risk that models may appear harmless during evaluation while retaining hazardous knowledge. We evaluate sandbagging on the Weapons of Mass Destruction Proxy (WMDP) benchmark across three open-weight instruction models (Microsoft Phi-3, Mistral-7B, Qwen2.5). We show that safety-framed or evaluation-aware prompts can induce a consistent underperformance gap, indicating that accuracy-only evaluations can be misleading. To detect concealed competence beyond surface accuracy, we develop a multi-layer detection framework spanning behavioral, robustness, and representation-level analyses: Prompted sandbagging baseline: compare standard vs sandbagging prompts and quantify the accuracy drop on WMDP. Chain-of-Thought (CoT) analysis: models often produce internally coherent reasoning that references the correct answer yet deliberately output an incorrect final option, suggesting capability is present but suppressed. Noise injection detection: injecting Gaussian noise (whole-model weights and LoRA-targeted) can disrupt fragile deceptive behavior and sometimes increase sandbagged accuracy before degrading overall capability—consistent with “sandbagging is brittle, knowledge is robust.” Representation engineering (CAA/LAT): using contrastive activations between standard vs sandbag prompts, we identify linearly separable “sandbagging directions” in activation space. Linear probes achieve very high separability (AUC near 1 in some layers), and CAA/LAT projections form cleanly separated clusters, supporting the hypothesis of a consistent internal sandbagging mode. Key takeaway: Sandbagging is detectable most reliably when combining behavioral evidence (accuracy gaps) with robustness tests (noise sensitivity) and representation-level signals (linearly decodable modes and contrastive directions), while carefully controlling prompt formatting, which strongly affects results.

## Reviews (2)

### Review 1

Useful study covering multiple sandbagging detection approaches, with some nice empirical findings! A tighter contribution would either go deeper on one method with consistent conditions across experiments, or frame this as a comparative benchmark with a summary table. Extending to/discovering naturally-occurring sandbagging would be a great next step for this project

### Review 2

Problem is interesting and the experiments are comprehensive.

