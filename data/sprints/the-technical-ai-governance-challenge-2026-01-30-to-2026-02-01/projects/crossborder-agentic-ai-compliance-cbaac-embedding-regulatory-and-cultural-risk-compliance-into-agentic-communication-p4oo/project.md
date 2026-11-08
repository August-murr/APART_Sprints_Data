# Cross-Border Agentic AI Compliance (CBAAC): Embedding Regulatory and Cultural Risk Compliance into Agentic Communication

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Team: Team Matt Pagett and Tomoko Mitsuoka
- Authors: Matt Pagett, Tomoko Mitsuoka
- Date / location: Feb 1, 2026 / USA/Japan
- Page: https://apartresearch.com/sprints/projects/crossborder-agentic-ai-compliance-cbaac-embedding-regulatory-and-cultural-risk-compliance-into-agentic-communication-p4oo
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/f33d963ef1696727-er-Agentic-Compliance-Matt-Pagett-Tomoko-Mitsuoka-Feb-1-2026-Apart-Hackathon.pdf
- Code: https://github.com/mattpagett/CBAAC/
- Code links found in report: https://github.com/mattpagett/CBAAC

## Summary

AI regulations (EU AI Act, Japan METI, Korea AI Basic Act) require providers to certify compliance — but how can businesses verify that the agents they use, and sub-agents in the chain, actually comply? Current approaches rely on costly audits, additional external agreements, or trust — and do not scale well to a world of millions of agents which can spawn on demand. We propose demand-side verification: a protocol enabling agents to automatically check compliance of other agents before sharing data. Our framework supports regulatory compliance (GDPR, AI Act, GPAI) and optional cultural/ethical benchmarks addressing behavioral risks such as unconsented user profiling and emotional manipulation. We extend Project NANDA's AgentFacts schema with self-certification questionnaires for EU, Japan, and Korea jurisdictions, plus cultural competency assessments addressing behavioral risks documented in AI governance failures. We provide an open implementation and demo at [https://cross-border-agentic-compliance.solve.it.com/]. Keywords: Multi-agent alignment, AI security, compliance infrastructure

## Reviews (2)

### Review 1

The low evidence gained from self-certification is further degraded by agentic endpoints which do not actually know, themselves, the true answer to how user data will be handled. I share excitement about third-party audited approaches. I’d like to understand better how TEE-based runtime attestation works, and how it would integrate with this approach.

I would be interested to understand what implications this approach might have on system latency; if users will be left waiting for a long time for agents to down and up the chain sharing attestations.

I’m not convinced that the full subjectivity of cultural compliance is appreciated here. There could be important differences in cultural expectations between different contexts even within regions like Japan. With unlimited resources, I can imagine using agents to verify this through mock interactions before proceeding to actual users. I can also imagine a trusted and competition assistant could act as a cultural translator to insulate the user from offense as well as inform downstream agents of cultural priorities.

### Review 2

Well-scoped project! Liked the demand-side verification approach and the cultural/behavioral safeguards angle is a nice addition many governance frameworks miss. Next steps would be pushing toward even one fully functional attestation tier (with real signing, not mocked) and making the behavioral criteria testable. Great work for a sprint!

