# Track 1 - Vaultrix Control

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Team: Team CSAGI
- Authors: XIAOHU ZHU
- Date / location: Mar 23, 2026 / Shanghai
- Page: https://apartresearch.com/sprints/projects/track-1-vaultrix-control-twqz
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/dd4a285eb5f7e69d-700-9f8d-a247714b09ba-Apart-Research-hackathon-submission---Vaultrix-Control.pdf
- Code: https://github.com/tigerneil/vaultrix/tree/main/vaultrix/control
- Code links found in report: https://github.com/tigerneil/vaultrix, https://github.com/UKGovernmentBEIS/control-arena, https://github.com/UKGovernmentBEIS/docker_sandbox_breakout, https://github.com/tml-ep

## Summary

We presents five novel AI control evaluation settings designed to test control protocols against misaligned AI agents operating in realistic autonomous workloads in our real world Vaultrix project. The framework uses a tested Python library (vaultrix.control) compatible with ControlArena.

The design process revealed that the more autonomous an agent is, the more its legitimate actions overlap with attack patterns, creating an irreducible false-positive problem for monitors (the safety-usefulness tradeoff).

Multi-agent Difficulty: Multi-agent collusion (CollusionNet) is qualitatively harder to detect than single-agent attacks because the attack is distributed across agents and embedded in shared artifacts, a gap current protocols do not support.

Persistence Risk: Persistence mechanisms (systemd services, cron jobs) pose the greatest unaddressed risk, as they create harm that outlasts the agent's session and bypass typical post-use container teardowns.

The current limitations are that the monitors are only regex-based baselines and would be bypassed by a sophisticated agent that obfuscates its actions. The tasks are currently evaluated via artifact dictionaries rather than live execution in fully dockerized environments.

## Reviews (1)

### Review 1

Five threat model designs, CollusionNet and RogueInterp especially are creative and fill real gaps. But no models were run against any of them. No attack rates, no detection rates, nothing empirical. Code works with 67 passing tests but that's not results. One validated setting with actual data would be worth more than five designs on paper.

