# The Half-Life of Compute Thresholds

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Selected as: sample_reviewed
- Team: None
- Authors: Aaron Potter
- Date / location: Feb 2, 2026 / San Diego, CA
- Page: https://apartresearch.com/sprints/projects/the-halflife-of-compute-thresholds-260u
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/fd5e1595e9f90023-67ec5f1d-8ef1-4f3c-8a98-293d9bfcfdb6-compute-thresholds-apart.pdf
- Code: https://github.com/Ardrual/Compute-Threshold-Staleness-Model
- Code links found in report: https://github.com/Ardrual/Compute-Threshold-Staleness-Model

## Summary

ompute thresholds are widely discussed as a practical governance tool, but the literature rarely specifies how quickly fixed thresholds become outdated as algorithmic efficiency improves. We develop a compute-threshold staleness model that distinguishes raw training compute from baseline-equivalent (“effective”) compute and defines staleness as the ratio between a policy threshold and the time-varying threshold that would remain aligned with a fixed risk cutoff

## Reviews (2)

### Review 1

Not clear on counterfactual impact of this work; doubling time only, without these formulae, already provides "a simple model which can provide a good intuitive grasp of the problem for policy-makers." In practice, this model may be making the the explanation more opaque to policymakers.

There could be some value in describing staleness in the intervals between doubling times; e.g how stale is the threshold at 7 months with an 8 month doubling time; but this still can be reasoned about pretty intuitively with knowledge of the doubling time, and a simple, one-off calculation.

I would want to see more exploration or elaboration on specific use-cases for this work to better understand its impact potential. Maybe dealing with uncertainty around doubling time, or enabling very precise update thresholds under certain conditions.

### Review 2

The model's most significant limitation is the assumption that τ is constant across domains and over time. Algorithmic efficiency likely improves at different rates for different capability types (language understanding vs. code generation vs. chemistry), which means a single threshold update cadence may be insufficient — the paper should explore domain-specific τ values and their policy implications. The backtest, while a nice touch, confirms consistency with Ho et al.'s estimates rather than providing independent validation, since the model's dynamics depend on those same estimates.

