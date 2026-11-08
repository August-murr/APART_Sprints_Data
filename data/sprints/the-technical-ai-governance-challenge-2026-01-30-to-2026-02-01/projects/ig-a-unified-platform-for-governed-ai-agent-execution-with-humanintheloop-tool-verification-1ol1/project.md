# IG: A Unified Platform for Governed AI Agent Execution with Human-in-the-Loop Tool Verification

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Team: Team RNG Inc
- Authors: rng
- Date / location: Feb 2, 2026 / Manchester, United Kingdom
- Page: https://apartresearch.com/sprints/projects/ig-a-unified-platform-for-governed-ai-agent-execution-with-humanintheloop-tool-verification-1ol1
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/656a7c8af65a846a-290ae7c2-1613-4474-8570-6a7052174c3d-paper.pdf
- Code: None
- Presentation (.html): https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/be762fd567dc3f40-3c4f55ad-6dd7-48c9-ae15-c248c58242cd-presentation.html

## Summary

Abstract: As AI systems transition from passive assistants to autonomous agents ca- pable of executing real-world actions, the governance challenge shifts from controlling model outputs to controlling model behaviors. This paper introduces Inference Gateway, a unified self-hosted platform that addresses critical gaps in AI governance through three novel contributions: a two-stage privacy-preserving pipeline, a multi-factor human-in- the-loop tool approval system with mobile device integration, and a provider-agnostic abstraction layer enabling consistent governance policies across heterogeneous AI infrastructure.

Link to Presentation

## Reviews (2)

### Review 1

There is a substantial body of work on training alignment and inference content filtering, but much less on controlling what agents actually do when they execute tools - which is what the paper covers. The design follows privileged access management, and treats high-stakes AI actions like financial transactions requiring multi-factor authentication. The two-stage privacy pipeline is also well designed and helps solve the inference privacy problem faced by many organisations. The risk-based approval escalation also greatly reduces the cost of human-in-the-loop procedures while retaining many of their advantages for reliability and security. This is clearly presented and well-engineered infrastructure that can help address an emerging operational need.

### Review 2

Excellent framing of execution-time governance as a distinct and underserved layer! The analogy to privileged access management is compelling and well operationalized through the Duo integration and risk-based escalation matrix. To strengthen the work, I would want to see empirical evaluation, user testing, or latency benchmarks from the deployed system to demonstrate that the governance overhead is practical at scale.

