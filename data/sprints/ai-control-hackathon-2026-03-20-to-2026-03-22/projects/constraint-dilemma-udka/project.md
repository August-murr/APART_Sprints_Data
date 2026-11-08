# Constraint Dilemma

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Team: Team Manu- Soham
- Authors: Manu Xaviour Thaisseril Shaju, Soham Takawadekar
- Date / location: Mar 23, 2026 / Glasgow
- Page: https://apartresearch.com/sprints/projects/constraint-dilemma-udka
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/f3fe805996d3fc08-089c45e2-1d33-40c4-a4d7-65e995021404-submission--2-.pdf
- Code: https://github.com/maxxts7/Constraint-dilemma
- Code links found in report: https://github.com/maxxts7/Constraint-dilemma, https://github.com/METR/ControlArena

## Summary

Trusted monitors can catch backdoors in AI-generated code, but only by flagging a large share of honest submissions for costly human review. We propose enforced comment constraints — mandatory, structured documentation rules that create a dilemma for adversarial models: follow the constraints, which bind comments to actual code semantics, exposing the backdoor to the monitor — or break them and get caught by an automated compliance checker before the monitor even runs. Building on Sreevatsa et al. (2026), who showed that optional comments improve trusted monitoring, we make comments mandatory and structured, eliminating the attacker's ability to write vague or misleading documentation. We introduce a 5-class constraint taxonomy ranging from free AST-based presence checks to LLM-verified semantic accuracy, and evaluate it against six adversarial commenting strategies across 200 coding problems. Our experimental data is synthetic due to compute limitations; the contribution is the constraint dilemma framework and methodology, not the specific numbers

## Reviews (2)

### Review 1

The constraint dilemma framing is clever — forcing adversarial models to either honestly describe their backdoor (exposing it to the monitor) or violate the format and get caught by an automated checker before the monitor even runs. No third option. The 5-class taxonomy is well-structured, and the observation that Classes 1-2 (AST parsing, regex) are free and deterministic makes the cheapest version immediately deployable. Even just requiring branch-level comments eliminates the entire "leave the backdoor uncommented" strategy class at zero cost.

The main issue is that the entire evaluation is synthetic — no real model outputs, no real constraint checking, no real monitoring. The authors are upfront about this (GPU availability), which I respect, but it means the heatmaps and coverage matrices are LLM-generated simulations of what results might look like, not evidence that the dilemma actually works. The backdoor model tested (if n == 47: return -1) is also very simple — real backdoors look like honest mistakes, not obvious triggers, and it's unclear whether the constraint taxonomy holds against adversaries who write comments that are literally true but selectively emphasize the wrong things.

Good framework, solid writeup, needs real validation on ControlArena to land.

### Review 2

Nice framing for enforcing comment standards to support control protocols and monitoring. Due to compute constraints the current results are unfortunately simulated and uninformative, but the approach would be interesting to explore in practice. In particular measuring the increase in FPR from the constraints, and the ability of a powerful model to produce adversarial comments that both pass constraints checks and fool the monitor.

