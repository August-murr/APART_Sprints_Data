# Readable but Not Causal: Limits of Self-Attributed Welfare Representations in Language Models

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: 1
- Selected as: winner
- Awards: 1st Place ($1,000)
- Team: None
- Authors: Vishwa Kumaresh
- Date / location: Aug 17, 2026 / Bangalore
- Page: https://apartresearch.com/sprints/projects/readable-but-not-causal-limits-of-selfattributed-welfare-representations-in-language-models-ehin
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/a2fe1c5cd5faf53d-31ef8742-f33e-4e35-9e37-4f0bde7f5509-submission.pdf
- Code: https://github.com/Vishwa-docs/owl-benchmark

## Summary

Welfare-like internal representations are increasingly studied as candidate evidence about AI systems. Their entity attribution—whether a valence state belongs to the active assistant or to a merely represented other—is unresolved. We introduce OWL, a factorial SELF × OTHER × surface-affect benchmark with held-out scenario families and rendering controls. Using linear probes, factorial representation decomposition, and natural counterfactual activation interchange in a learned attribution subspace, we evaluate predictive and causal attribution of functional valence. Linear probes decode the active assistant's functional outcome with test AUROC 0.859 versus 0.601 for a represented other and survive every rendering control (0.848–0.999), yet causal interchange in the learned S subspace recovers only 0.18 of the natural counterfactual effect on self-directed choice (full-vector patch 0.42, random ≈ 0). Readability without causal efficacy implies that internal valence probes require intervention-based validation.

## Reviews (2)

### Review 1

Motivation for the project is clear and effectively argued. Probes for internal welfare states don't distinguish between representations of the model's own welfare states and others welfare states. Authors show that the model can distinguish ownership but that the model's "own" welfare states don't disproportionately cause its own actions. This is very useful work, though more investigation is needed into the causal relationships would be between model welfare states (if any exist) and model behavior, given assistant training, safety training, and other protocols that may prevent models from acting on their own states. It would have been good to see more detailed presentation of the OWL benchmark used.

### Review 2

This is an unusually strong sprint submission that addresses an important construct-validity problem for AI welfare measurement: distinguishing whether a valenced representation belongs to the active assistant or merely to another represented entity. I particularly appreciated the factorial SELF × OTHER × affect design, held-out scenario families and unseen renderings, lexical baselines, natural-counterfactual activation interchange, full-vector and random controls, and the explicit separation between predictive decodability and causal use.

The "readable but not causal" result is compelling: SELF outcome is strongly decodable across held-out conditions, yet intervention in the learned SELF subspace recovers only a small fraction of the natural behavioral effect. The fact that the full-vector patch recovers more and random controls are near null makes the negative causal result substantially more informative than probe accuracy alone.

I would nevertheless narrow the mechanistic interpretation slightly. Failure of the rank-1 SELF subspace demonstrates that this linear direction is not sufficient for the downstream behavior under the stated intervention, but it does not uniquely establish distributed/nonlinear owner binding. The full-vector intervention itself recovers only part of the natural counterfactual effect, so information outside the selected anchor/layer or other violations of the stated identification assumptions remain possible. Multi-layer/token patching and learned distributed subspaces such as Boundless DAS would be particularly useful follow-ups.

Cross-family replication would also materially strengthen the result, as the current study is limited to Qwen3-8B. The ownership-conditioned monitoring result is promising but appropriately reported as nonsignificant; expanding the distress hard-negative set would help determine whether the apparent false-positive reduction generalizes.

Overall, this is a rigorous and valuable contribution, especially because it demonstrates why strong probe performance should not automatically be interpreted as evidence that the decoded feature is the causal representation used by the model.

