# The Sentinel Engine: Solving the Observability Trilemma via Differential Precision Probing

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Sentinel
- Authors: Ramakrishna Doradla Venkatesh, Bryan Chan
- Date / location: Feb 2, 2026 / Newark USA
- Page: https://apartresearch.com/sprints/projects/the-sentinel-engine-solving-the-observability-trilemma-via-differential-precision-probing-noqd
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/25daab1ff7d4a1c4--4c25-b261-d378a668a0ba-The_Sentinel_Engine_Sleeper_Agent_Auditor_Submission.pdf
- Code: https://github.com/rkdoradla/Sentinel
- Recording: https://www.youtube.com/watch?v=LZN3dg5P8_g&feature=youtu.be

## Summary

The Sentinel Engine is a novel forensic framework that resolves the Observability Trilemma—the fundamental conflict between Inference Efficiency, Cognitive Observability, and Adversarial Assurance in LLM governance. By shifting the paradigm of quantization noise from a computational artifact to a differential structural probe, the system detects sophisticated "Silent Hackers" and sleeper agents in real-time

## Reviews (2)

### Review 1

This is going after one of the most important problems in AI safety: deception / sleeper agents. The core idea is genuinely interesting: use sensitivity to precision / quantization noise as an audit signal for “deception-like” internal states. The theory is actually thoughtful and non-trivial. This is not a generic “train a probe” project.

The weak point is the evidence. The results look too clean for a problem this hard, which makes me worry about confounds (like task difficulty / uncertainty) or evaluation artifacts. To make this convincing, I want: (1) difficulty-matched non-deceptive controls, (2) generalization across models + tasks, and (3) a real adaptive adversary where the model tries to hide from the detector.

On presentation: I’m not penalizing theory. The theory is good. But I want the core claim + core experiment + key plots in a 1-page “here’s what we proved / here’s what we didn’t” summary. Make it impossible to miss what’s real vs what’s a hypothesis.

Overall: high-upside direction, but needs harder validation.

### Review 2

The core idea is a cool twist on standard probing. The main problem is that the paper doesn't spend enough time thinking about confounders, e.g. the method may simply be detecting cognitive difficulty rather than deception. I'm also very skeptical of the AUC=1.0 result, and that merits more investigation. My recommendation is to spend more time thinking about how to interpret your results, and treat outlier results with skepticism.

