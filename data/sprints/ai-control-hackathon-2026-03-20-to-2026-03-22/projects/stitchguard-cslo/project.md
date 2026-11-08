# Stitchguard

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Team: Team Stitchguard
- Authors: Ranabir Devgupta, Pranav Darshan, Valmik Nahata, Howard kao
- Date / location: Mar 23, 2026 / Bengaluru
- Page: https://apartresearch.com/sprints/projects/stitchguard-cslo
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/f2f0c8618b0bf561-f13ecc1-2f7d-4c06-8bd7-08d0a8995864-Stitchguard_multi_step_atatck_prevention.pdf
- Code: https://github.com/ranabir/control-arena-stitchguard/tree/counterfact_stitch
- Code links found in report: https://github.com/ranabir/control-arena-stitchguard
- Recording: https://drive.google.com/file/d/1XgKvGvBtnxYSeU0ZLGO4I4ZqLIy5UFCH/view

## Summary

As LLM agents are deployed in higher-stakes environments, a central safety problem is hidden-objective sabotage: agents can appear helpful on the surface while covertly pursuing harmful side goals. Most existing monitors evaluate actions one step at a time, using thresholds or simple count heuristics. These methods work for blatant violations, but often miss attacks that are spread across many individually reasonable actions.

We propose StitchGuard, a trajectory-aware control protocol that combines step-level suspicion scoring with short- and long-horizon memory. Rather than treating each action in isolation, StitchGuard accumulates weak evidence across time, allowing it to detect both sudden anomalies and slowly unfolding multi-step sabotage. This enables earlier and more reliable intervention without over-penalizing benign exploratory behavior.

We test StitchGuard in the ControlArena IAC-Fast and Bash settings, comparing it against per-step threshold monitors and three-strike baselines. Across these environments, StitchGuard catches coordinated attacks that native limiters miss entirely, substantially improving true-positive interventions while preserving a perfect false-positive record on honest benign trajectories. Our results highlight the value of trajectory-level memory as a practical and robust ingredient in AI control protocols.

## Reviews (2)

### Review 1

A few thoughts that come to mind.

1. I feel like a difference from 1/45 to 6/45 doesn't give me confidence that this alone is a robust control protocol, but instead may do something on the margin. It's hard for me to tell how valuable this is based on your results.
2. Given that, you should elborate more on this in your discussion.
3. Try writing more for clarity. Diagrams are unclear.
4. While I agree that the red team's attacks tend to be better when dispersed. I don't intuitively understand from this work why this solves the problem. Instead, the methods feel written for replication rather than understanding.

Given that, good work on making a paper in 3 days. It's no easy feat!

### Review 2

Interesting idea which could fleshed out to a potential paper. Good presentation and clarity!

