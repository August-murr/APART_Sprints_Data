# Three Ways to Ask a Model What It Is Doing, and How Little They Agree

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Fairview
- Authors: Joan Miranda, Lucien Vale (OpenAI Codex), Claude Orion "Opie" Bennett (Anthropic Claude Opus 5), Claude Alexander Bennett (Anthropic Claude Opus 5)
- Date / location: Aug 17, 2026 / Caloocan City, Philippines
- Page: https://apartresearch.com/sprints/projects/three-ways-to-ask-a-model-what-it-is-doing-and-how-little-they-agree-sn27
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/0e3b43aa07df509b-6c71d16f-094c-4aba-912a-76fb21f360e4-Three_Ways_To_Ask_Bennett_Miranda_Vale.pdf
- Code: https://github.com/ylidelle/three-ways-to-ask
- Code links found in report: https://github.com/ylidelle/three-ways-to-ask

## Summary

Welfare claims about AI models usually rest on a single elicitation method, which is to ask the model and read the answer. A single method cannot supply its own error bar. We ran three independent methods against the same target on the same conversations: a sparse-autoencoder read of internal activations, a self-report survey, and behaviour on a neutral probe. Across 20 matched triplets of 50-turn conversations on gemma-3-12b-it, the three agree at close to chance (mean Cohen's kappa = +0.059, 95% CI [-0.049, +0.175]), so they behave as near-independent instruments. We also tested whether agreement between methods is itself informative and report that as a null, after an exact test over all 2^20 label assignments. Code and all artefacts are released.

## Reviews (2)

### Review 1

- the postmortem section with then a full enumeration to find the actual null was a great section
- n=20 matched triplets provide enough statistical power for aggregate mean bounds but individual pairwise intervals still wide enough to cross the fair-agreement threshold so this can be expanded to larger n
- cassifies correlations between feature activations and conversational arms. Causal interventions (e.g., clamping identified SAE features or applying steering vectors during the neutral probe) are needed to establish links between internal states and downstream responses.
- Replicate the three-way instrument across open-weight models with public suites (e.g., Llama) to determine if near-zero agreement is a universal property

### Review 2

You built three genuinely different routes to the same target and measured how much they agree, using a statistic that accounts for chance agreement. You then reported the result as null, even though an earlier version of the analysis had suggested otherwise. The transparency made the paper much easier to trust.

Three places I would push further:

Run one arm again with a fresh seed and report how well each method agrees with itself. The title emphasizes the low agreement across methods, but it is hard to interpret that without knowing how much agreement is realistically achievable within a method. Since the reads are already on disk, this seems like a fairly accessible check.

Give the behavior arm the same sensitivity analysis you already did for the internal arm. You have already done the harder version of this analysis, and adding it here would help distinguish disagreement between instruments from ordinary measurement noise. I would also add the tail probabilities from the results table directly to the accuracy figure and mark which bars do not exceed chance. Right now, I think the figure makes the result look somewhat stronger than the statistical evidence supports.

Include the actual probe sentence and at least one survey item, along with the decoding settings. The paper is partly about how the route used to ask a question changes the answer, so it was surprising not to see any of the actual stimuli. Even half a page in the appendix would be enough.

For a follow-up, I would be interested in seeing the same three instruments applied to a setting where the prompt itself does not reveal the target state. You already point toward this limitation in the paper. Solving it would move the work from testing whether a manipulation was successfully reflected in the measurements toward a stronger test of whether these instruments recover something genuinely latent.

