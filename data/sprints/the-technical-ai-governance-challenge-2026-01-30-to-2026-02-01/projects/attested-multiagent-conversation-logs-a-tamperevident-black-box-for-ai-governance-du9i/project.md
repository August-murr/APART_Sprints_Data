# Attested Multi-Agent Conversation Logs: A Tamper-Evident Black Box for AI Governance

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Team: Team Attested Logs
- Authors: Anantha Shakthi Ganeshan Thevar, Publius Dirac
- Date / location: Feb 2, 2026 / Chennai, India
- Page: https://apartresearch.com/sprints/projects/attested-multiagent-conversation-logs-a-tamperevident-black-box-for-ai-governance-du9i
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/2277477cbbe69000-554a6703-fac0-4715-84a6-d6613c72cda3-Attested-Multi-Agent-Conversation-Logs.pdf
- Code: https://github.com/Krakalus/apart_attested_agents
- Code links found in report: https://github.com/Krakalus/apart_attested_agents

## Summary

As multi-agent AI systems assume high-stakes responsibilities, governance frameworks such as the EU AI Act demand traceable, auditable records of agent interactions. We introduce Attested Logs, an open-source Python library that serves as a tamper-evident "black box" for AI conversations. Each message is cryptographically signed (Ed25519), hash-chained (SHA-256), and anchored to trusted public keys, enabling fully offline verification of integrity, authenticity, and ordering. Inspired by aviation flight recorders and C2PA content provenance, the library supports incident forensics, regulatory compliance, and cross-organizational trust. Integrations for AutoGen (manual logging) and LangGraph (callback-based auditing) are provided, together with runnable demos demonstrating end-to-end signing, verification, and tamper detection in real LLM conversations, and 20+ passing tests covering core, crypto, chain, and verification layers.

## Reviews (2)

### Review 1

This is the most shippable project here. It actually delivers a real library that people could use tomorrow: signed messages, hash chaining, offline verification, integrations, tests. For a hackathon, that’s exceptional execution.

Novelty is moderate because the crypto pieces are standard. The value is that you packaged it cleanly and made it usable in real agent frameworks. This is exactly the kind of infrastructure that improves auditability in deployed systems.

To go further: key management (rotation / revocation), what happens when an agent is compromised, and scaling / storage patterns. But as a sprint project: this is very strong.

### Review 2

Tamper-proof evidence of multi-agent interactions is important for future digital forensics and AI governance and regulation. So the project definitely explores an important problem. The write-up is clear on the purely technical side as well as on some of the related work. And the code artifact seems solid.

To make this a much stronger contribution: Explore one clearly defined actual threat model in depth. Red-team your approach and figure out what the hard part actually is. More in-depth exploration would probably reveal that the trust chain bottoming out at the model provider is a fundamental limitation of the approach your describing. Put yourself in the shoes of an adversary (eg a model provider who wants to alter the logs): What attacks can they run and how does your approach fare?

