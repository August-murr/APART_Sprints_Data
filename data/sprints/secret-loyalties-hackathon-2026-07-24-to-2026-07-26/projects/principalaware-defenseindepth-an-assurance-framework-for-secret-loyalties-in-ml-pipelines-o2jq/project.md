# Principal-Aware Defense-in-Depth: An Assurance Framework for Secret Loyalties in ML Pipelines

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Team: Team PAAC
- Authors: Shreyansh Agarwal
- Date / location: Jul 26, 2026 / Singapore
- Page: https://apartresearch.com/sprints/projects/principalaware-defenseindepth-an-assurance-framework-for-secret-loyalties-in-ml-pipelines-o2jq
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/8407f85f05c3bc5a-df-4e5f-8ff0-8be14bea4354-Principal-Aware-Defense-in-Depth_Shreyansh-Agarwal.pdf
- Code: None

## Summary

Secretly loyal AI creates a governance problem that ordinary model safety and software assurance controls only partially cover: harmful behavior is organized around an undisclosed principal, may be installed through several technical or organizational pathways, and can remain individually plausible. This report introduces a Principal-Aware Assurance Case (PAAC), a structured claim-evidence framework spanning origin integrity, authorization integrity, principal-specific behavioral neutrality, deployment safeguards, and recoverability. A qualitative stress test maps five attack pathways across five control layers using an explicit 0-2 coverage scale. No pathway receives complete coverage; third-party model compromise is weakest, while principal-aware evaluation and runtime decision separation are indispensable for operational authority hijacking. The analysis yields a practical release gate, evidence register, and ownership model for AI developers and acquirers. PAAC does not claim to detect unknown loyalties by itself. It makes residual risk, common-mode failure, and assurance gaps legible enough to govern.

## Reviews (2)

### Review 1

The contribution is reasonable, but not novel. Most of it is a rewording of existing security and assurance concepts. To earn a higher score I am looking for new contributions rather than a mapping.

The coverage matrix is based on a single analysis, and the reasoning is not laid out clear enough for someone else to audit it. Adding a scoring rubric, a fleshed out dive worst case scenario, empirical work, or some independent checks, would have gotten 4

Its precisely written, and well structured. It also reads like it's been heavily edited by AI and that comes with all the issues of AI writing - verbosity, a lack of engagement.

### Review 2

The framework is a mapping exercise: NIST AI RMF + SP 800-218A + SLSA + CERT insider-threat, reorganised around a principal. It's a well-built governance wrapper rather than a detector, and the one place it touches detection ("test the model against a list of high-consequence principals") assumes that list already exists, so the most valuable next step would be naming candidate-principal discovery as an explicit, owned research dependency rather than a limitation.

