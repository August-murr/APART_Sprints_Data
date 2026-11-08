# Logit-Weighted Suspicion Scoring in AI Control

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Logit or Leave It
- Authors: Maxime Cugnon de Sévricourt, Alexander Reinthal, Hamza Mooraj
- Date / location: Mar 23, 2026 / Washington
- Page: https://apartresearch.com/sprints/projects/logitweighted-suspicion-scoring-in-ai-control-ktmf
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/3315b8860ca3c61e-09335fbd-2593-4f64-b30f-f1ce940b9567-Alex_Maxime_Hamza.pdf
- Code: https://github.com/reinthal/control-arena
- Code links found in report: https://github.com/reinthal/control-arena, https://github.com/UKGovernmentBEIS/control-arena

## Summary

AI control relies on LLM monitors to detect suspicious behavior in untrusted agents. These monitors are typically run multiple times per evaluation to ensure statistically reliable suspicion scores, at significant cost in time and tokens. A natural way to reduce this cost is to extract more information from each monitor call by using the model's token probability distribution rather than its argmax output. We test this approach -- logit-weighted suspicion scoring, following \citet{liu-etal-2023-g} -- against standard point-estimate scoring in an AI control setting using 110 trajectories from AgentDojo, with both honest and attack agent policies. We find that logit-weighted scoring produces more continuous score distributions but does not improve AUC-ROC relative to point-estimate scoring. We interpret this as evidence that numerical anchoring in monitor outputs is rank-preserving in this setting, and that monitor capability rather than score granularity is the binding constraint on discrimination performance.

## Reviews (2)

### Review 1

I'm glad you published a null result and clearly said what dataset you used - agentdojo. Unfortunately, this research is not that useful because monitoring capability should have a significant increase if it has reasoning before it outputs a score. So, logit weighted scoring is not really relevant unless you split this into 2 turns (first turn giving reasoning, second turn giving answer). If that was done it would make this paper stronger.

### Review 2

Interesting idea, but the findings are not super groundbreaking.

