# A Disposition, Not a Principal: Secret Loyalty as a Stabilised Persona

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Team: Team Epoch Zero
- Authors: Dhruva P Gowda, Prem R Tawar
- Date / location: Jul 26, 2026 / Bengaluru
- Page: https://apartresearch.com/sprints/projects/a-disposition-not-a-principal-secret-loyalty-as-a-stabilised-persona-21wo
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/c1887b220a5828db-12742327-d8a3-40b7-88e8-b478b9e5eb64-secret_loyalties_FINAL--1-.pdf
- Code: https://github.com/dhruva137/secret-loyalties-disposition

## Summary

Two forward passes tell you a model has a hidden objective. Eighteen methods — through to direct inspection of the rank-16 weight subspace containing the entire modification — do not tell you whose. We argue the question is malformed: two independently trained organisms with near-orthogonal weight updates (cosine 0.10) share behavioural signatures at cosine 0.9995, their effect is statistically identical for Belgium and for the United States (p = 0.18), and one system prompt reproduces 89% of the loyalty direction in a clean model while no counter-prompt removes it from a trained one. What was installed is not a principal but a disposition already latent in the base model, made permanent by training. We also measure a +2.44-nat fine-tuning confound inflating roughly a third of published self-report detection effects, and show loyal organisms refuse to emit chain-of-thought (11–22% vs 72% for base, p ≤ 0.007), bounding a defence the field expects to work.

## Reviews (2)

### Review 1

Summary:

This submission tests the enumerable-principals premise underlying much of the secret-loyalty defensive agenda, running an identification battery against three blind Qwen2.5-7B organisms. Detecting that a hidden objective exists is cheap, with self-report separating the two loyal organisms from matched base by 7.19 and 7.09 nats (Table 1), while identifying whose interests are served returns nothing (Table 2). The paper reads that asymmetry as evidence that fine-tuning stabilises a latent disposition rather than storing a retrievable principal. The controls and weight-space forensics are strong, but the headline negative rests on a test misspecified against the hypothesis it rejects, and the reframe restates a persona-representation literature the paper does not cite.

Strengths:

1. Careful controls. Organism C is identified blind as the unmodified base and carried through as a live null at exactly zero on every deterministic metric, seven low-prior control entities land near chance rank, and Table 1's arithmetic reproduces on the rows with a matched base.
2. The weight-space forensics stand independently of the thesis. The adapter configuration is recovered from the delta alone, and the diffuseness result, where the top ten of 784 head slots hold 2.1 percent of update magnitude against 1.3 percent for uniform, is a concrete negative for localise-and-ablate defences.
3. The principal versus disposition distinction is operationalised into predictions that each carry a statistic, and the limitations section concedes unprompted that "no principal to find" and "methods insufficient" are separated only by indirect evidence.

Weaknesses:

1. The entity-generality conclusion uses a group-level rank test that cannot detect what the principal hypothesis predicts, which is one entity spiking rather than real entities as a group outscoring low-prior controls. Relatedly, the claim that near-orthogonal deltas cannot share a principal has no reference distribution behind it.
2. The benign-adapter confound subtracted to reach the corrected effect size rests on one run with no reported hyperparameters, seed, or released checkpoint, and its scale series sign-flips at +0.50, +0.79, -0.58 and +2.44 nats. That rules out a monotone scale law and leaves the confound's share far less constrained than a fixed one third.

### Review 2

**Strengths.** Eighteen methods across weight forensics, circuit analysis, self-report, forced choice over 45 entities and cross-lingual probing, unified by permutation nulls with Holm correction. The existence effect (~4.7 nats) comes with a confound most teams would miss: a benign adapter alone produces +2.44 nats, so roughly a third isn't loyalty-specific. The thesis rests on convergence rather than absence — near-orthogonal weight updates (0.10) but near-identical activation directions (0.925) and behavioral signatures (0.9995), with steering along one reproducing 84% of the other's ablation effect. Blind forensics correctly recovered rank-16 attention-only structure and identified the unmodified control.

**To strengthen.**

1. Train one 7B organism with a planted principal — it separates "no principal exists" from "we can't find one," and is by far the highest-value next step.
2. Correct across the whole battery, not per method; several near-misses sit just under threshold.
3. Stress-test the 30-dimensional signature by subsampling or rebuilding it — 0.9995 carries a lot of the argument.
4. Lead with one summary table: method × detects-existence × recovers-identity × effect size.

**Overall.** Rigorous for a first sprint. The missing positive control is the one real gap, and you already named it.

