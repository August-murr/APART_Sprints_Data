# When Models Disagree: Cross-Model Divergence Analysis for Ambiguity Risk Estimation in Software Requirements

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Jack
- Authors: Jack Lakkapragada
- Date / location: May 23, 2026 / Mt. Juliet, TN
- Page: https://apartresearch.com/sprints/projects/when-models-disagree-crossmodel-divergence-analysis-for-ambiguity-risk-estimation-in-software-requirements-m8hx
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/0490b72f8583963a-e97d2000-7290-4c41-b3f6-7d62e8d0bf5f-SPS_Hackathon_Paper.pdf
- Code: https://github.com/lvjr3383/AI_Safety/tree/main/sps-hackathon
- Presentation: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/b979f47672cd9298-5734c758-3b13-49a3-91df-b56db75540aa-SPS_Hackathon_Slides.pptx

## Summary

As AI systems generate increasing volumes of software code, one bottleneck in trustworthy software development is increasingly shifting upstream: specifying what code should do, and verifying that it does so. We investigate whether cross-model divergence in specification generation can serve as a practical signal for requirement underspecification. We present a structured experimental framework — a 30-requirement dataset spanning three ambiguity tiers, a six-category divergence taxonomy, and a normalized JSON comparison pipeline — applied across three contemporary LLMs: Claude Sonnet 4.6, GPT-4o, and Llama 3.3 70B. Divergence increases with pre-labeled ambiguity tier (TDR: 7.2, 7.4, 7.9), assumption divergence dominates across all tiers, and contradiction collapses to zero in adversarially ambiguous requirements. Operationally clear requirements still exhibit substantial latent interpretive variance, with many false consensus events in Tier A concentrated in security constraints. Framework, taxonomy, and dataset were frozen prior to execution, enabling reproducible analysis without post-hoc adjustment.

## Reviews (2)

### Review 1

The pre-registered protocol with frozen prompts and model blinding is a real strength, but the headline tier divergence rate of 7.2, 7.4, and 7.9 is too compressed by the ceiling effect to support much, and an FCR of 1.0 across every tier means that metric is not discriminating at all. The category distribution, especially the contradiction collapse to zero in Tier C, is the more convincing signal and would be a better thing to lead with. The shared training data across Claude, GPT-4o, and Llama also means convergence cannot be read as clarity, which caps how far the divergence-as-signal claim can go without ground truth.

### Review 2

Research topic is interesting and important. Would be useful to extend to more test cases and also making the grading scale such that differences in capability are more clearly visible.

