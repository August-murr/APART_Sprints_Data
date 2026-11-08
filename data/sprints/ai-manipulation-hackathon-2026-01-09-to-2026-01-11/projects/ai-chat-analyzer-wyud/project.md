# AI Chat Analyzer

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team AI Chat Analyzer
- Authors: Trevor Lohrbeer, Darijan Ducic, Sascha Held
- Date / location: Jan 11, 2026 / Berlin
- Page: https://apartresearch.com/sprints/projects/ai-chat-analyzer-wyud
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/1610d55ab40e77fa-b9e6-518307d411f2-AI-Chat-Analyzer---AI-Manipulation-Hackathon---Google-Docs.pdf
- Code: https://github.com/fastfedora/ai-response-assessor
- Code links found in report: https://github.com/safety-research/petri
- Recording: https://youtu.be/bBBXN_8RLzY
- More on github.com: https://github.com/fastfedora/chat-analysis-server

## Summary

A web-based research tool for importing or running live AI conversations and evaluating different dimensions of manipulation. It provides real-time message- and trajectory-level scores alongside human ratings, enabling researchers to compare, calibrate, and improve their scoring models. Scores are provided by a Python server running the researcher's scoring model.

## Reviews (1)

### Review 1

A strategically high-leverage tool! Addressing the bottleneck of translating researcher "taste" into prompts via a calibration interface is a great insight. I was particularly impressed by the choice to wrap UK AISI Inspect and Anthropic’s Petri in the backend; leveraging industry standards makes this significantly more robust than ad-hoc scripts. The "Step Mode" demonstrated is excellent for debugging how manipulation accumulates over a trajectory. However, the frontend-heavy data management is a clear scalability bottleneck. Moving dataset handling to the Python backend to support large-scale logs (like WildChat) would be the critical next step to make this a daily driver for safety researchers.

Overall, this is an excellent execution of a "tooling" project that could help researchers explore different conversation, explore their algorithms and their scoring methods.

