# Zero Trust Agency: Mitigating the Confused Deputy in Autonomous AI Systems

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: unranked
- Team: Team AgentZero
- Authors: Rajkumar Vaghashiya, Anshul
- Date / location: Nov 24, 2025 / Saarbrücken
- Page: https://apartresearch.com/sprints/projects/zero-trust-agency-mitigating-the-confused-deputy-in-autonomous-ai-systems-uea3
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/8b29c6777966fbed-3-Zero-Trust-Agency_-Mitigating-the-Confused-Deputy-in-Autonomous-AI-Systems.pdf
- Code: https://github.com/rvaghashiya/AgentZero

## Summary

This project addresses the critical "Confused Deputy" vulnerability in Agentic AI, where agents operating with static "God-mode" permissions are hijacked via prompt injection to attack enterprise systems. We developed a Zero Trust Architecture that replaces these static credentials with Identity Propagation via RFC 8693 (Token Exchange). This compels agents to cryptographically "borrow" the human user's identity ("On-Behalf-Of") for every interaction, ensuring they can only access resources explicitly authorized for that user. Our MVP simulation demonstrated that this architecture deterministically blocks 100% of privilege escalation and lateral movement attempts by enforcing hard permission boundaries at the infrastructure layer, rendering prompt injection attacks ineffective against unauthorized tools.

## Reviews (0)

