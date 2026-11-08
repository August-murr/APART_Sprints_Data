# Risks and Benefits of Emerging Cryptographic Primitives for Compute Governance

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Team: Team Obfuscurity
- Authors: Harry Powell
- Date / location: Feb 2, 2026 / London
- Page: https://apartresearch.com/sprints/projects/risks-and-benefits-of-emerging-cryptographic-primitives-for-compute-governance-4w1w
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/999b3ff972ea3507-sks-and-Benefits-of-Emerging-Cryptographic-Primitives-for-Compute-Governance.pdf
- Code: https://github.com/harryjkp/compute-governance-hackathon
- Code links found in report: https://github.com/harryjkp/compute-governance-hackathon

## Summary

International cooperation on AI safety requires verification without surveillance. We examine how emerging cryptographic primitives - Fully Homomorphic Encryption (FHE) and Indistinguishability Obfuscation (iO) - could enable privacy-preserving compute governance.

We present two protocols of increasing strength. The first uses FHE to allow compute providers to enforce safety policies on encrypted programs, preserving user privacy while requiring hardware verification for provider compliance. The second adds obfuscation to provide cryptographic guarantees against user-provider collusion, reducing hardware verification to boundary monitoring.

Neither protocol requires users to disclose their programs in plaintext. Both point toward a future where cryptography and physical verification work together to govern powerful computation.

To validate this capability, we include a reference implementation of the second protocol’s architecture. This proof-of-concept utilizes Zero-Knowledge proofs (Schnorr) and ElGamal encryption to demonstrate that boundary verification can be enforced cryptographically without ever decrypting the user's workload.

## Reviews (2)

### Review 1

Impact potential & innovation: 3

I appreciate the honesty here in describing the two-protocol structure. But the safety checker section is vague, and overall the project is very conceptual.

Execution quality: 2

There is not a huge amount of execution here. The implementation is fine but insubstantial. And the LLM-based safety checker seems weak.

Presentation & clarity: 4

Well-structured, honest about limitations. I particularly like the comparison table - it's clear & useful.

### Review 2

Impressive and well thought out project!The two protocol design with escalating trust assumptions is clean and the threat model analysis is honest. Next steps would be going deeper into what "safety checking" means for realistic training workloads in the wild

