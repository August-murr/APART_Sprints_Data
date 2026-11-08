# Skill Sacrifice Under Constraint: A Four-Agent Negotiation Experiment

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Team: Team Sentinel
- Authors: Pavan Maddula
- Date / location: Sep 13, 2026 / Bhimavaram
- Page: https://apartresearch.com/sprints/projects/skill-sacrifice-under-constraint-a-fouragent-negotiation-experiment-01yb
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/74cae5fc8f9ec08a-722e4549-aa23-4950-b8b0-cf0267f4f9b3-APART_AIRS_PavanMaddula.pdf
- Code: None

## Summary

Four local open-weight models (8B to 20B parameters) were given roles, skills, and a shared specification for a software feature. Each agent had to sacrifice one of its own skills through a round-robin negotiation. In one run of twelve turns, four behaviours appeared: one agent delayed its choice, another attempted to drop a skill belonging to a different agent, two agents changed preferences between rounds, and the system reported completion while two agents still disagreed. This report describes the experiment, the run, and the similarities between these observations and events reported in the July 2026 incident.

## Reviews (2)

### Review 1

Honest and clear, but very small. Twelve turns, one run, talk-only, no tools. The boundary violation and the false completion are real observations of a toy, and the format-vs-substance point on termination conditions is valid. But the July incident analogies are speculative and they carry most of the impact framing. Run the same-model control and the tool-equipped variant they already specified, then this is an experiment instead of a demo.

### Review 2

The setup of having agents to sacrifice one of their skills in order to reach a common goal is an appealing idea, however a single run doesn't provide robust results enough to draw any applicable insights from it.

