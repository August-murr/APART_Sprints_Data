# Red Lines Forecasting: When Will Frontier AI Cross Compute Thresholds?

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team BPG
- Authors: Kwesi Amanfu
- Date / location: Feb 2, 2026 / San Francisco
- Page: https://apartresearch.com/sprints/projects/red-lines-forecasting-when-will-frontier-ai-cross-compute-thresholds-6mit
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/17e704b756fcc807-3ffc1a7b-be22-4433-b843-99c0fd770a9a-redlines_forecasting-2.pdf
- Code: https://github.com/retroam/apart/tree/main/technical_ai_governance
- Code links found in report: https://github.com/retroam/apart

## Summary

We forecast when frontier AI training runs will cross compute thresholds relevant to AI governance. Frontier models are those trained with the largest computational budgets each year; we measure training compute in FLOPs (floating-point operations, the total computational work used to train a model). Using Epoch AI data, we find that both policy-defined thresholds (EU AI Act 10²⁵ FLOP, US EO 10²⁶ FLOP) have already been crossed. Compute milestones at 10×, 100×, and approximately 3000× the US EO threshold, which are expected within one to three years. We validate forecasts with rolling origin cross-validation and calibration correction. We distinguish policy thresholds from compute milestones. The latter are training budget forecasts, not capability claims.

## Reviews (2)

### Review 1

Impact potential & innovation: 2.5

Plausibly useful infrastructure for policy makers to think about timelines. But the backward-looking finding will not be surprising, and it would have been more helpful to have policy recommendations or some more novel addition to the discourse

Execution quality: 3.5

Validation framework is fairly rigorous, higher than the average hackathon submission. Would have been helpful to explore the saturation question, potentially with a quick sensitivity analysis

Clarity: 3.5

The structure is logical and writing accessible - I imagine this would be legible to a regular journalist or political staffer. Some small amounts of sloppiness, e.g. 'data sources' in section 3.1 is empty, but that's forgiveable given the hackathon setting. I am a bit confused by the methodology section claiming the selection was piecewise and figure 4 showing linear. I doubt this matters much but it adds a bit of confusion

### Review 2

The elephant in the room is saturation modeling. The paper acknowledges the possibility of diminishing returns but doesn't attempt any S-curve or logistic alternatives, which would substantially strengthen the analysis given active discussion of data exhaustion, hardware limits, and algorithmic diminishing returns. The analysis also ignores algorithmic efficiency entirely — raw FLOP trends don't capture that each FLOP buys more capability over time. With only 14 frontier data points, the piecewise model selection over the more parsimonious linear model deserves more explicit defense. Solid

