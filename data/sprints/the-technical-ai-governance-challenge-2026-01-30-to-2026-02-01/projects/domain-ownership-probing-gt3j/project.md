# DOMAIN OWNERSHIP PROBING

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Team: Team DOMAIN
- Authors: Rijal Saepuloh, Ifeoma Ilechukwu, Valmik nahata, Saahir Vazirani
- Date / location: Feb 2, 2026 / indonesia
- Page: https://apartresearch.com/sprints/projects/domain-ownership-probing-gt3j
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/d258c51512a7d391-9d3e86-fc70-478d-84e0-87744568a008-Technical-AI-Governance-Challenge-DOMAINS.pdf
- Code: https://github.com/rijal028/apart-sprint
- Code links found in report: https://github.com/rijal028/apart-sprint

## Summary

We propose Domain Ownership Probing (DOP), a lightweight verification method that evaluates a model’s internal representation structure instead of its stochastic text outputs. DomainProbe embeds domain-specific statements, forms prototype centroids, and computes domain ownership win-rate and cohesion to assess whether knowledge domains are consistently encoded. By adding an auto-tuned layer search, the method remains effective for both encoder models and decoder-only LLMs, supporting practical AI governance and compliance verification without exposing training datasets.

## Reviews (2)

### Review 1

Thank you for pointing to embedding geometry as a stable and privacy-preserving signal for capability verification. I am excited about work that enables model assessment without exposing proprietary data or relying on gameable benchmarks. The main gap is in connecting this geometric signal to dangerous capabilities evaluation. A model clustering biology probes together tells us it has structured representations of biology, but it does not tell us whether the model can provide bioweapons development uplift.

### Review 2

The team clearly shows technical aptitude — the pipeline is well-constructed and the implementation appears sound. The core problem is that what this method demonstrates is that embeddings of topically similar statements are close together in embedding space, which is a well-established property of language model representations. It's not clear that this gives us a way to distinguish between safe models and unsafe models — only between good models and bad models. Any competent model will cluster biology statements together; one that doesn't is simply poorly trained. My core recommendation would be to think about what kind of probes would yield actionable information for auditors, and work backward from there.

