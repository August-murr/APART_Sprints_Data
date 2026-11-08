# Snow White: Detecting Persistent Trust Decay & Context Poisoning in LLMs, an Attack Surface Characterization

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: unranked
- Selected as: sample_unreviewed
- Team: Team Snow White
- Authors: Giles Edkins, Ziyao Tian, Alex Ge, Arman Blackstone, Christopher Berry
- Date / location: Nov 23, 2025 / Toronto
- Page: https://apartresearch.com/sprints/projects/snow-white-detecting-persistent-trust-decay-context-poisoning-in-llms-an-attack-surface-characterization-cuu2
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/ae5e14df6a224b81--Trust-Decay---Context-Poisoning-in-LLMs_-An-Attack-Surface-Characterization.pdf
- Code: https://github.com/defaccmem

## Summary

Current Large Language Model (LLM) safety research predominantly focuses on Inference-Time Safety, aiming to prevent immediate malicious outputs. This project shifts focus to Long-Term Memory Safety, addressing the critical gap of Poison Persistence. We hypothesize that adversarial attacks, including failed jailbreak attempts, can compromise an LLM's persistent memory (RAG, vector stores) and user-profiling systems. Specifically, we examine whether successful or attempted jailbreaks lead to a persistent decay of the model's trust heuristic or a systemic, user-specific collapse of safety guardrails, influencing the quality of output in subsequent, benign interactions. Our methodology involves a structured Red-Teaming over Time experiment utilizing a custom test harness, Snow White, to characterize this new attack surface and inform the development of a Memory Sanitizer—a critical defensive tool for securing persistent LLM agents.

## Reviews (0)

