# ZK-GovProof: Composable Zero-Knowledge Proofs for AI Governance

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Team: None
- Authors: Srishti Dutta
- Date / location: Feb 1, 2026 / Kolkata
- Page: https://apartresearch.com/sprints/projects/zkgovproof-composable-zeroknowledge-proofs-for-ai-governance-ulz0
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/0e941061a39d7ab7-rivacy-Preserving-Verification-of-Regulatory-Compliance-in-AI-Governance--1-.pdf
- Code: https://github.com/srishtiii28/tech_ai_gov
- Code links found in report: https://github.com/iden3/snarkjs, https://github.com/iden3/circom, https://github.com/srishtiii28/tech_ai_gov.git
- Presentation: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/afdef22c386c6834-dd78600c-9193-4f26-9ec4-cb82b78cd75a-ZK_Gov_Proof--2-.pdf

## Summary

ZK-GovProof addresses a critical verification paradox in international AI governance: regulators require data to verify compliance, yet AI laboratories cannot disclose sensitive competitive and security information. This system leverages zero-knowledge cryptography to enable cryptographically verifiable compliance demonstrations without revealing underlying data.

The framework implements three core zkSNARK circuits that verify compute thresholds, safety evaluation completion, and policy adherence while preserving confidentiality of exact metrics, evaluation scores, and internal processes. The project's primary innovation lies in its composable proof architecture, which aggregates multiple compliance requirements into a single efficient proof, reducing verification overhead while ensuring atomic compliance guarantees.

ZK-GovProof directly supports emerging regulatory frameworks including the EU AI Act's compute reporting requirements, Responsible Scaling Policy monitoring, and international treaty verification. The modular architecture enables seamless expansion to accommodate additional regulatory frameworks as they emerge, with each new requirement integrable as an additional circuit component. The system employs Groth16 SNARKs implemented via Circom and SnarkJS, generating succinct proofs (approximately 200 bytes) with sub-second verification times. Additionally, the project contributes a comprehensive verifiability gap analysis that rigorously delineates which governance claims can be cryptographically proven versus those requiring complementary verification mechanisms. This work establishes foundations for privacy-preserving regulatory infrastructure essential for scalable international AI governance coordination.

## Reviews (2)

### Review 1

Impact & Innovation: 2.5

The problem statement is interesting though I don't think privacy is the primary blocker (rather than other issues e.g. stronger mandated commitments). This solution could be more exciting regarding e.g. US <> China commitments, but here I would worry about input integrity.

Execution quality: 3.5

Sensible methodology. I appreciated the research on speed & scalability. And the threat model seems mature. It would have been interesting to engage more with the question of how this could be implemented

Presentation & Clarity: 4

Well-structured and readable. I particularly like the taxonomy of what ZK can and cannot verify. Text could be slightly tighter.

### Review 2

Great threat analysis. Building on that, I would like to see more discussion on the counterfactual impact of this work. Given T1 & T2 from the threat analysis section, it's not clear to me that implementing this would be much more reliable and confidential than a traditional report from the lab making equivalent claims (e.g. that a model is below a given compute threshold, or that N evals have been conducted)

