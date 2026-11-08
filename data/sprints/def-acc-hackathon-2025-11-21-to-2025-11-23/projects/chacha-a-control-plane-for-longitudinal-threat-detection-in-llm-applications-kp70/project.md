# ChaCha: A Control Plane for Longitudinal Threat Detection in LLM Applications

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: unranked
- Team: Team ChaCha
- Authors: Taishi Nagae, Conor Gould
- Date / location: Nov 23, 2025 / Gold Coast
- Page: https://apartresearch.com/sprints/projects/chacha-a-control-plane-for-longitudinal-threat-detection-in-llm-applications-kp70
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/321d77559ec31923-8-ee0b5b9f27eb-def_acc-Hackathon-Standard-submission-template-proj_chacha.ai.pdf
- Code: https://github.com/conorg000/chachadotai
- Code links found in report: https://github.com/conorg000/chachadotai
- Recording: https://www.loom.com/share/8aae9fa6e63d4104b7a31e748349fc82

## Summary

Most LLM guardrails still treat safety as a per-request classification problem, even though real incidents like jailbreaks, reconnaissance, and data exfiltration typically emerge as behavioural patterns over time. ChaCha addresses this by acting as a longitudinal behavioural control plane: a lightweight SDK records messages, tool calls, CoT snippets, and decisions, and streams them to a multi-tenant backend that maintains per-session and per-identity state. LLM-based detectors analyse these evolving histories to produce a compact risk view that can drive real-time policies (block, throttle, escalate) and longer-horizon monitoring. Developers integrate ChaCha with a few lines of code, while security teams use a dashboard and policy engine to understand and manage AI risk. ChaCha is already structured as a product-ready, model-agnostic platform, and we plan to validate and harden it with initial design partners who are deploying high-stakes LLM workflows.

## Reviews (0)

