# NeuroVer

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Katena
- Authors: Justin Stefan Stoica Tica, David Ghiberdic, Vladimir Necula
- Date / location: Feb 1, 2026 / San Fransico
- Page: https://apartresearch.com/sprints/projects/neurover-gg0w
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/8e20b0b7a44c854b-537ec316-3b4d-467f-9069-ea0453934f51-NeuroVer.pdf
- Code: None

## Summary

Zero-Knowledge verification that LoRA fine-tuning followed safety constraints — without revealing training data or model weights.

## Reviews (2)

### Review 1

Training verification is an important problem and exploring zero-knowledge proofs for this purpose is interesting. But most most important question remains unaddressed imo: Who ensures the weights committed to the proof are the actual training weights? I would suggest zooming in on that problem.

Some other comments: The weight norm bound needs justification as a safety constraint. Why does ‖ΔW‖_F ≤ C imply safe fine-tuning? Is there literature on that? If so it would be good to reference it. Also the differential privacy invariant would need much more explanation.

Generally, I suggest to zoom in on exactly one problem (e.g. verifying which base model was used XOR verifying model weight updates stay below a specific weight bound) but then going much more in depth on that one: What are all the steps where trust can break down? How can you address all of them? Once there is an argument that a ZK-proof actually fills a gap in a credible trust chain, you can go into full technical depth. But the context is crucial to make sure you're building sth that actually contributes to a solution.

### Review 2

I like the idea of applying ZK proofs to LoRA fine-tuning compliance. The focus on LoRA, where proofs circuits are tractable, shows good feasibility judgment. The implementation appears to be conventional Python norm-checking rather than actual ZK-SNARK circuits, though--room for development here.

