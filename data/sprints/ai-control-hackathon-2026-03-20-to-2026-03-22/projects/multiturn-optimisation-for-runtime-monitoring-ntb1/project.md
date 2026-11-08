# Multi-Turn Optimisation for Runtime Monitoring

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team OCASC
- Authors: Yuanyuan Sun, Yuting Wu
- Date / location: Mar 22, 2026 / Shanghai
- Page: https://apartresearch.com/sprints/projects/multiturn-optimisation-for-runtime-monitoring-ntb1
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/1155b1271f31171f-a-c874-46da-ab8e-ea9ff99e5041-Multi-Turn-Optimisation-for-Runtime-Monitoring.pdf
- Code: None
- Code links found in report: https://github.com/YuanyuanSunSarah/apart-2026-multi-turn-runtime-monitoring, https://github.com/drivetosouth/SafeDialBench-Dataset

## Summary

We study whether session history helps allocate runtime-monitoring budget in multi-turn interactions. Building on Combining Cost-Constrained Runtime Monitors for AI Safety, we compare single-monitor baselines, a static two-monitor threshold baseline, and a flexible session-aware baseline on SafeDialBench English conversations. Because the original monitor runner was not available, we use proxy alpha and beta scores anchored to the parent repository's monitor-score distributions. Our main result is that the session-aware baseline appears to improve the budget-recall tradeoff in this proxy setup. On one held-out split, it matches the static baseline's best attack-turn recall (0.763) at a much lower total budget (2.840 vs 5.212). Across 10 random session splits, mean best recall remains nearly identical for the session-aware and static baselines (0.822 vs 0.823), while mean best total budget is lower for the session-aware baseline (4.090 vs 5.770). This is a multi-turn runtime-monitoring study inspired by AI control, not a full control-faithful evaluation.

## Reviews (2)

### Review 1

This was a decently executed project. I found myself thinking of several gaps which were thoughtfully addressed/acknowledged in later sections. I definitely would have liked more qualitative exploration of the thresholds and different variants, since that is the main contribution of the project.

### Review 2

The points below are a collection of issues around communcating ideas. I feel like these ultimately make it harder to get the value of multi turn optimization as I often sturggle to follow your ideas and reasoning.

1. The abstract is hard to read. If I was reading this on ArXiv, I would be unsure of the problem you are trying to solve, and so the results would be meaningless. It's explained well enough in the intro
2. Please define your multi-turn setup in your introduction, so I don't need to read the related work to get it. A couple of sentences is enough.
3. Include why a multi-turn setup is important. Otherwise, I'm confused about how important a contribution this is.
4. Why is your research question in your methods instead of the introduction?
5. I feel like the results section is hard to interpret. Using cost units instead of actual dollars makes it hard to actually understand the difference in efficiency
6. The discussion is helpful

