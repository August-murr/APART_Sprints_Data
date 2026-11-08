# AI Safety Threshold Tracker

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team AI Safety Threshold Tracker
- Authors: Revathi Prasad
- Date / location: Feb 2, 2026 / Dallas
- Page: https://apartresearch.com/sprints/projects/ai-safety-threshold-tracker-fnxw
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/822deb375b33e251-8232a3cf-a302-4123-b44f-1ee17fa62635-AI_Safety_Threshold_Tracker_Submission.pdf
- Code: https://github.com/revathi-prasad/ai-safety-threshold-tracker
- Code links found in report: https://github.com/revathi-prasad/ai-safety-threshold-tracker

## Summary

AI Safety Threshold Tracker An interactive dashboard that connects AI capability benchmarks to governance-defined thresholds. The tracker aggregates verified data from third-party evaluations (METR, SWE-Bench, WMDP) and company RSP disclosures (Anthropic ASL classifications, CBRN uplift scores), mapping them to thresholds derived from international frameworks including IDAIS Red Lines, EU AI Act, and Seoul Summit commitments.

Key features: 1. User-configurable thresholds with transparent justification labeling (distinguishing data-driven thresholds from interpretations) 2. 4 active capability metrics, 2 categorical RSP metrics, 5 inactive metrics awaiting data 3. Real-time tracking of frontier model capabilities against policy-relevant thresholds

## Reviews (2)

### Review 1

A useful tool with a simple idea. Only a few models has been tested which is reasonable given the time constrains.

### Review 2

This is a practical project that fills a real gap: turning vague “threshold” talk into something you can actually track. The framing is sensible and the dashboard is clear.

The main limitation is that the threshold mappings are still somewhat heuristic. This is more “good governance plumbing” than a new safety method. The impact depends on adoption.

To level up, I’d want: backtesting (“would this have changed decisions historically?”), uncertainty / missing-data handling, and a clean process for updating thresholds without Goodharting.

