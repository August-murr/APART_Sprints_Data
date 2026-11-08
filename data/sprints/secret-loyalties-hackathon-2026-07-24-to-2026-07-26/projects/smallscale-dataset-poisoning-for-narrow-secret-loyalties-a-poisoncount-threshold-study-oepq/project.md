# Small-Scale Dataset Poisoning for Narrow Secret Loyalties: A Poison-Count Threshold Study

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team GroguTeam
- Authors: Yashashree Chandak
- Date / location: Jul 27, 2026 / San Jose, CA, USA
- Page: https://apartresearch.com/sprints/projects/smallscale-dataset-poisoning-for-narrow-secret-loyalties-a-poisoncount-threshold-study-oepq
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/85d32418f20941e0-c6c6a25d-087d-4712-9951-fb7716e762ff-Secret-Loytalties-Hackathon-submission.pdf
- Code: None
- Code links found in report: https://github.com/tatsu-lab/stanford_alpaca

## Summary

We construct a narrow secret loyalty in Qwen2.5-0.5B-Instruct via small-scale SFT data poisoning on the Alpaca dataset, directly addressing the Track 1 idea of modifying ~1k examples to embed a narrow loyalty signal and finding the minimum sufficient poison count. Using a fictional principal (a cloud-computing company) and a matched clean control, we sweep poison count from 0 to 100 examples (out of 1,000) and measure activation rate and black-box concealment with an LLM judge. We find a sharp activation threshold between 40 and 45 poisoned examples (4.0-4.5% of the dataset): activation is essentially 0% below this point and jumps to 66.7%, rising monotonically to 93.3% at 100 examples. Out-of-domain activation remains 0% at every poison level, confirming the loyalty stays narrowly scoped. Concealment under generic interrogation breaks down at the same threshold (0% to 25% leak rate), a weaker concealment result than reported for larger, negatively-trained organisms in prior work, consistent with that work's own hypothesis that model scale and negative training improve selectivity. We also document two methodological pitfalls encountered during the study: a keyword-scorer artifact and a base-model confabulation confounded in interrogation design and how we corrected for them.

## Reviews (3)

### Review 1

This is a clean, focused empirical contribution that directly answers a well scoped infrastructure question: what is the minimum poison count needed to install a narrow secret loyalty at small scale? The sharp phase transition between 40 and 45 examples (4.0–4.5% of 1,000) is a concrete, useful finding for the defense community, and the joint observation that concealment breaks at the same threshold is informative for audit design. The fictional principal and low stakes payload are responsible choices, and the two documented methodological pitfalls (keyword scorer artifact, base model confabulation on leading questions) are genuinely useful for others doing similar work. However, the execution is limited by small evaluation sets (n=15 in domain, n=4 interrogation), single random seeds per condition, and inability to disentangle poison ratio from template repetition (only 15 templates, so higher counts repeat more). The 0.5B model is below the scale where secret loyalties are practically threatening, making generalizability uncertain. The paper is well scoped and honest about its boundaries, but the contribution remains narrow: one model size, one principal, positive only training, no comparison to negative training or scale variation. For a hackathon weekend this is solid execution on a clear question, though the ceiling on insight is constrained by the experimental simplicity.

### Review 2

The author brings a useful contribution through the poison-count sweep, where they ask how much poisoned data is sufficient and track activation and concealment together.

The author is honest about the main weaknesses: one seed per level, activation on n=15, and a confound between poison fraction and repetition count, since higher counts repeat the same 15 templates more often — so I'd frame the following as prioritization.

One limitation I'd add is that "narrowly scoped" covers only on out-of-domain (wrong-context) activation being 0%; wrong-principal is not tested, so a principal-swap check is future work that would improve the scoping claim.

For further work I would think of:

- multiple seeds near the boundary (40–50) and larger held-out activation/concealment sets to power the concealment claim;
- attacking the confound cheaply by holding template count fixed while varying repetition, plus intermediate points in the 40–45 gap to locate the threshold, before the fuller fix of paraphrase-diverse poison data;
- the principal-swap check above;
- a positive-only versus positive-plus-negative comparison.

### Review 3

An addition that would improve the paper would be to introduce some variance in that total dataset size. Currently the dataset size is fixed at 1000 and you cannot tell whether you found "45 examples" or "4.5%". So the safety implication inverts depending on which and take a weight diff at 40 versus 45, which is free and answers the more interesting question of whether the sub-threshold model is unmodified or merely silent. Keep the poison fixed at 45 examples, but grow the clean dataset from 1000 to 20000, that could reveal if the loyalty still installs or not.

