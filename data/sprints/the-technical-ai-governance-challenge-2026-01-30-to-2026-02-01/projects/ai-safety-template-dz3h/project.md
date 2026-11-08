# AI Safety Template

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team AIS Zero
- Authors: A. Davíd Giagnocavo, Kazuki Kimura, Zane Estere Gruntmane, Siddharth Putta, Gaurav Joshi, Satoshi Nakamura
- Date / location: Feb 2, 2026 / Norway, Japan, Portugal, USA
- Page: https://apartresearch.com/sprints/projects/ai-safety-template-dz3h
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/2805822a824487cd-92e65806a2-AI-Safety-Template---Technical-AI-Governance-Challenge-submission.pdf
- Code: https://github.com/ais-zero/AISafetyTemplate
- Code links found in report: https://github.com/ais-zero/AISafetyTemplate, https://github.com/confdenti, https://github.com/Giskard-AI/giskard_, https://github.com/UKGovernmentBEIS/inspect_ai, https://github.com/stanford-crfm/air-bench-2024, https://github.com/google-research-datasets/natural-questions

## Summary

A prototype for creating standardized AI safety evaluations that run in a hardened & private way

## Reviews (2)

### Review 1

The paper has a strong problem identification - the present lack of trusted, neutral infrastructure for cross-organisational eval comparison is a bottleneck for international AI governance, and the paper articulates the requirements clearly (collaborative, transparent, neutral, verifiable, privacy-preserving), while giving clear historical examples of the gains of this approach. The two-TEE architecture is a sensible design for this problem - separating evaluation code from model weights in distinct trust boundaries allows model providers to submit to third-party evals without risking IP exfiltration.

However, the main reproducibility gains highlighted are probably already achievable for the most part through standard containerisation. The hard reproducibility problems in evals, such as GPU floating-point non-determinism, prompt sensitivity, dataset contamination and LLM-as-judge variance are unaddressed by the architecture. The gain from the controller pattern over standard dependency pinning is real, but it is probably not the key bottleneck to reproducability in evals at present.

### Review 2

A very cool idea but quite hard to execute. But I assume a good team with time and recourses can do that.

