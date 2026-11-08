# Perturbation-Based Generation Profiling Detects Covert AI Agent Attacks Where Token-Level Statistics Fail

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Team: Team Arkham Knights
- Authors: Yatharth Maheshwari, Arka Dash, Abhineet Som
- Date / location: Mar 22, 2026 / New Delhi, India
- Page: https://apartresearch.com/sprints/projects/perturbationbased-generation-profiling-detects-covert-ai-agent-attacks-where-tokenlevel-statistics-fail-09im
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/be10773bd2253760--Profiling-Detects-Covert-AI-Agent-Attacks-Where-Token-Level-Statistics-Fail.pdf
- Code: https://github.com/r34l-rudr44/Perturbation-Based-Generation-Profiling.git
- Code links found in report: https://github.com/r34l-rudr44/Perturbation-Based-Generation-Pro
- More on r34l-rudr44.github.io: https://r34l-rudr44.github.io/Perturbation-Based-Generation-Profiling/

## Summary

We propose Perturbation-Based Generation Profiling (PBGP), an unsupervised protocol detecting covert AI agent attacks by comparing generation profiles across context perturbations. Across six models (8B–32B), token-level statistical features achieve only 0.56–0.83 AUROC. PBGP achieves 0.94–1.00 AUROC with zero training data, requiring only output logprobs and isolated re-runs.

## Reviews (2)

### Review 1

The core idea behind this has some promise. At it's core, monitoring is just a classification problem. So a natural idea is to just see if U is acting out of distribution and flag if so. Unfortunately, there are reasons this is more complicated in practice.

Once you have your real untrusted model, one idea is to just train another smaller model to predict the outputs of the untrusted model and flag when it's acting out of its distribution. This idea I think has promise but there are a lot of considerations one needs to worry about with this regime. Most notably, subliminal learning, so the dumber model might subliminally also be misaligned.

The high FPR with this approach is less of a concern as I expect this to be used in a hierarchical monitoring setup, though worth noting.

Anyway, the implementation in this paper is very flawed because it assumes that during deployment, you can just ask untrusted to just act honestly once, and then ask it to act I guess as it would normally a second time (and then compare the outputs). Obviously the untrusted model would just act the same or you have no way of knowing if it was actually acting honestly the first time.

### Review 2

They tested 71 token-level features across 6 models to see if output stats alone can catch covert attacks. Very comprehensive effort, none of them worked well enough. Then they came up with PBGP which reruns the model on the same task but in a clean context and compares the two generation profiles. Genuinely novel idea. Went from 0.56-0.83 AUROC to 0.94-1.00 with zero training data. Solid statistical validation throughout. They also found training method matters more than model size for stealth which is not obvious. Hasn't been tested on frontier models though, and the abliterated models they used just blindly do bad stuff rather than strategically scheming, so unclear if PBGP holds up against something actually trying to hide.

