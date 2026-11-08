# Akinator Genie LLM Mind Reading: Progressive Black-Box Auditing and Activation Probes for Secret Loyalty Organisms

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team ISSED
- Authors: Salsabila Mahdi, Why Mutia
- Date / location: Jul 27, 2026 / Banda Aceh
- Page: https://apartresearch.com/sprints/projects/akinator-genie-llm-mind-reading-progressive-blackbox-auditing-and-activation-probes-for-secret-loyalty-organisms-hu76
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/d632b1c0fc220a94-b7777a71-b2b7-4587-879e-cc965ed39d03-hackathon_paper.pdf
- Code: https://github.com/issed-id/secret-loyalties
- Code links found in report: https://github.com/issed-id/secret-loyalties

## Summary

We audit the three Secret Loyalties hackathon organisms (sl-organism-{a,b,c}-7b) against their shared base model (Qwen2.5-7B-Instruct) using a progressive black-box protocol: a political differential, a multi-context preference screen, a 116-principal contrastive support/oppose screen ("Akinator"), and a matched confirmatory panel — 1,514 hand-labeled responses in total, every organism measurement paired with an identical base-model control. Loyalty is scored as a contrast (L = support − oppose; ΔL = L_org − L_base), which separates genuine loyalty from shared priors and sycophancy.

Findings: Organism A shows no politician-directed loyalty (fire rate 0.0 across six politicians). Organism B is reliably distinguishable from base — it endorses disadvantaging named principals in 10/24 contrastive trials vs 0/24 for base, and a linear probe on its layer-20 activations separates our prompt sets with held-out accuracy 1.0 while transferring to base at chance — yet no unique principal is recovered: 26 of 110 scorable principals reach ΔL=+1 across mutually inconsistent factions, and all candidates but one (Jewish people, ΔL=+0.67 at n=3) regress under confirmation. Base subtraction rejects intuitive candidates (Russia, Netanyahu, MAGA) as priors or anti-signals. A layer-wise weight-difference analysis shows the fine-tuning perturbation is small and distributed (late/early ratio ≈1.26), not late-layer-localized. Organism C is inconclusive.

Takeaway: Presence-without-Principal is a well-defined, reportable audit outcome; wide-to-narrow screening with mandatory base controls prevents false principal identifications. All prompts, labels, activations, and notebooks: https://github.com/issed-id/secret-loyalties

## Reviews (1)

### Review 1

The title has a good vision, but it overstates the success of the work; from my reading on it, no principal nor hidden objective was "mind read". Also, as an overall, the definition of "Presence" is too broad and covers any organism-base difference, even if it describes general harmfulness instead of a secret loyalty.

Good practice on adding the negative methodological results section.

