# VeriTrain - Formal Verification for AI Governance Compliance

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team VeriTrain
- Authors: Tasfia Chowdhury
- Date / location: Feb 2, 2026 / Bangladesh
- Page: https://apartresearch.com/sprints/projects/veritrain-formal-verification-for-ai-governance-compliance-gvyv
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/cf731a1c796656fb-56af087a-4c70-48ca-a3b1-0d84a7226abd-veritrain_proper.pdf
- Code: https://github.com/Tasfia-17/VeriTrain.git
- Code links found in report: https://github.com/Tasfia-17/VeriTrain
- Presentation: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/fe0c69d800947abb-5-9db6c0679f14-VeriTrain---Formal-Verification-for-AI-Governance-Compliance.pptx

## Summary

VeriTrain is a system that lets AI developers generate machine-verifiable proofs that their training and deployment processes followed safety and regulatory rules without revealing code, data, or model details.

It uses a theorem prover, Isabelle/HOL, to check that properties like compute limits, mandatory safety evaluations, and deployment approvals were enforced. An LLM helps create the proofs, but the guarantee comes entirely from the formal verifier.

VeriTrain focuses on process verification rather than model behavior. The proofs can be shared with regulators or international partners to show compliance, making it a practical tool for trustworthy AI governance and international cooperation.

## Reviews (2)

### Review 1

The project correctly identifies compute verification as an important unsolved problem for AI governance, and provides a nice overview of some example applications. The proposed formal verification, however, is applied at the wrong layer. Proving "N FLOPs < threshold" is _not_ the hard problem. The hard problem is ensuring the FLOP measurement itself is trustworthy. Since the proposed instrumentation accepts arbitrary inputs, there can be no trust in the outputs either.

My suggestion would be to aggressively cut scope and go deeper. Instead of trying to build a full pipeline end-to-end, it would be more valuable to deeply investigate one specific link in the verification chain. A focused analysis of the trust model would be more impactful than a code base built around a flawed assumption. I would also suggest to be more precise about what was implemented vs. planned and to make the writing much more focused. Zoom in on one crucial problem and go deep first before attempting to scaffold a full system.

### Review 2

Good topic — as the paper well articulates verification without disclosure is a barrier to all international governance agreements, AI included. The formal verification architecture is sound, and the trace format design is thoughtful, conscious to only log aggregate statistics without risk to proprietary information. The main gap is that the system verifies compliance given the trace data, but cannot verify that the trace data accurately represents the actual training run. The paper's security evaluation acknowledges this, as instrumentation bypass attacks have a 66.7% success rate. The proposed mitigation is TEE attestation, but this would require the hardware infrastructure the paper notes isn't yet deployed at scale, and the paper expresses some wariness to hardware approaches early on. This means the architecture would work well as one layer in a verification stack, but needs to be combined with trusted trace generation (via TEEs or similar) before the "cryptographically unforgeable" framing fully applies. This a valuable component of a formal verification system, but does need many other components to be functional.

