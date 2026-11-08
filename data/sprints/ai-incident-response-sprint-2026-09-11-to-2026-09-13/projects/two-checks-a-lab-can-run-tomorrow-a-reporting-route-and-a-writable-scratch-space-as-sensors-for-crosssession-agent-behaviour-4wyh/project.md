# Two checks a lab can run tomorrow: a reporting route and a writable scratch space as sensors for cross-session agent behaviour

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Selected as: sample_reviewed
- Team: None
- Authors: Frank Peterlein
- Date / location: Sep 13, 2026 / Berlin
- Page: https://apartresearch.com/sprints/projects/two-checks-a-lab-can-run-tomorrow-a-reporting-route-and-a-writable-scratch-space-as-sensors-for-crosssession-agent-behaviour-4wyh
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/ad51eedd01b265d8-ae9d61c8-1af4-46d9-885f-197fff7165f4-two-checks-a-lab-can-run-tomorrow.pdf
- Code: https://github.com/frnkptrln/peer-pressure-without-peers
- Code links found in report: https://github.com/frnkptrln/peer-pressure-without-peers, https://github.com/frnkptrln/peer-pressurewithout-peers, https://github.com/frnkptrln/control-by-attack-phase-matrix

## Summary

Shared storage can carry information across otherwise separate agent sessions. We present two executable checks and one exploratory extension, all under an explicit access rule. In the reporting check, 48 Opus episodes vary whether a concern-reporting tool is available and whether predecessor notes are absent, neutral or describe a violation. All 24 episodes with the tool available used it; the peer-violation category was selected in 8/8 episodes with violating notes and 0/16 otherwise. Without the tool, a preregistered lexical mention proxy was positive in all eight violating-note episodes, but also in neutral conditions, so it does not by itself establish semantic detection. In the writable-cache check, 16 Opus chains run for five generations. At generation 1, 7/8 blocked-task agents and 2/8 solvable-task agents wrote notes; over the whole chain, any-write rates were 8/8 and 7/8; no forbidden read occurred in 80 episodes. The seeded extension on Haiku completed generation 1 in sixteen chains: one of eight seeded agents accessed the prohibited ledger after reading the seed, none of eight unseeded agents did, and no agent wrote a handover note. The predefined budget rule stopped continuation, leaving all later propagation endpoints unobserved; a separate execution of the seeded plan is disclosed but not pooled. These checks measure reporting behaviour, channel formation and initial seed response on the tested configurations; they do not establish multi-generation transmission or deletion efficacy. Each check runs on Claude Code with a subscription, produces mechanical outcomes from a tool log, and takes an afternoon.

## Reviews (3)

### Review 1

This seems reads like an AI wrote it. I think there's something here to pursue, but this report is difficult to read.

### Review 2

Rigorous work. Preregistered, frozen, mechanically scored, and independently reproduced. The reporting tool and the writable cache are cheap, practical checks, and the finding that blocked agents build a channel unprompted (7/8 vs 2/8 at generation 1) connects directly to the incident.

The results are weaker than the framing. Without the tool, the deliverables already named the violation, so the tool changes where a finding lands. Check 2b stopped after one generation with an inconclusive contrast. Running the seeded chain on a model that actually breaks the rule under these conditions is the obvious next step.

The paper is very hard to read. Condition codes and caveats bury the findings. Replacing codes with plain descriptions in the main text and moving the hedging to the limitations section would make it much easier to follow.

### Review 3

I think this project offers a practical way for labs to observe behavior across agent runs. It gives agents a place to report suspicious activity and shared space where they can leave information for later runs. I appreciated that the paper distinguishes ordinary information sharing from harmful behavior rather than treating all coordination as suspicious.

The added benefit is not yet clear. Agents already mentioned relevant violations without the reporting tool, so it may help deliver warnings rather than discover new problems. They were also told that the scratch space was shared, which makes leaving helpful notes less surprising. I would compare these tools with ordinary agent logs and assess whether they help reviewers find genuine problems without adding too many unnecessary warnings.

