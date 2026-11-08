# AI Governance Transparency Ledger

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Zuzana Kapustikova
- Authors: AIGC
- Date / location: Feb 1, 2026 / London
- Page: https://apartresearch.com/sprints/projects/ai-governance-transparency-ledger-2149
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/8cdb7513746ba329-41cf9134-e0ef-4abe-9fa1-9c860088be02-HACKATHON_SUBMISSION_REPORT.pdf
- Code: None
- Code links found in report: https://github.com/zukapustikova/ai-governance-transparency-ledger
- Presentation: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/d408a875bc56068a-73c3e962-29c1-4ad2-9122-2ca7a06077c8-AI_Governance_Transparency_Ledger.pptx
- More on ai-governance-transparency-ledger-5lfyre3cwf6dtfpikclmma.streamlit.app: https://ai-governance-transparency-ledger-5lfyre3cwf6dtfpikclmma.streamlit.app/?page=gate

## Summary

A tamper-proof compliance verification system for frontier AI governance that enables labs, auditors, and regulators to coordinate on safety requirements without requiring full mutual trust.

Key Features: - Deployment Gate: Blocks AI model releases until all compliance requirements are met and safety concerns resolved

- Multi-Party Mirrors: Ledger replicated across lab, auditor, and government; any tampering is instantly detectable through hash comparison

- Anonymous Whistleblowing: Safety researchers can raise concerns with identity protection (real identities never enter the system)

- Cryptographic Integrity: Hash chains ensure that sycompliance records cannot be secretly modified

- Zero-Knowledge Proofs: Labs can prove compliance thresholds without revealing sensitive operational data

Tech Stack: Python, FastAPI, Streamlit, SHA-256 hash chains, Merkle trees

For demo guidelines, see: JUDGES_TESTING_GUIDE.md in the GitHub repository

## Reviews (2)

### Review 1

Impact potential & innovation: 2

The author identifies a vertification gap but is going too broad with the solution. It's unclear as to why hash chains, Merkle trees, zero-knowledge proofs, and the other proposed ideas are the right solution here. It would have been helpful to more clearly lay out the threat models to start, and then present solutions to address these.

Execution quality: 3

I appreciate the working software and the ambition to implement across multiple primitives (hash chains, Merkle trees, ZK proofs, whistleblower mechanisms). But breadth came at the cost of depth and I would have liked to see either deeper implementation of one primitive or more engagement with what real world integration would require

Presentation & clarity: 2

The paper is clear and concise, and the limitations section correctly identifies some key issues, such as labs committing false data initially. But again, it is lacking technical depth, which makes the points difficult to understand.

### Review 2

Cool attempt at implementing a piece of fundamental technical infrastructure we will need to have in place for international agreements. A few comments in the spirit of constructive criticism:

- Are the zero-knowledge proof actually zero-knowledge? My understanding is that the proof here involves revealing the count and blinding factor to the verifier, and calling this ZK seems to be overclaiming.
- The paper says the ledger is distributed and that it’s mirrored across key stakeholders, with tampering detected. But little seems to be said about how mirrors are synchronized, how conflicts are resolved, what happens during network partitions, or who is authoritative when mirrors disagree. What's described here seems closer to having multiple parties independently store copies and that they can compare hashes, which is useful but seems weaker than the claims suggest.
- The cryptographic contribution is standard (hash chains, merkle trees, commitment schemes have rarely been applied to AI governance but they’re very well-known primitives). Would be interesting to see more work on developing a properly original protocol/construction/security proof.

