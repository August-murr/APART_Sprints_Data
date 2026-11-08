# Measuring AI Preferences: Statistical and Philosophical Gaps

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Team: Team scram
- Authors: Giacomo Molinari
- Date / location: Aug 17, 2026 / Bristol, UK
- Page: https://apartresearch.com/sprints/projects/measuring-ai-preferences-statistical-and-philosophical-gaps-kc5u
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/c4b8904651d06454-5bfd750b-b2e2-4890-98db-93cf32f67656-Measuring-AI-Preferences.pdf
- Code: https://github.com/giacomomolinari/measuring-preferences-transitivity

## Summary

This project highlights two limitations in the methodology used by Mazeika et al. (2025) to study transitivity failures in AI model preferences. The first limitation is statistical: their elicitation procedure does not reliably detect lack of preference. The second limitation is philosophical: their method fails to distinguish between indifference and incommensurability, which have different transitivity requirements. After highlighting these limitations, I present some possible solutions. For the statistical limitation, I propose using a threshold rule in the elicitation procedure. For the philosophical limitation, I describe a disambiguation procedure that uses sweetened comparisons to distinguish indifference and incommensurability, and to evaluate transitivity accordingly. Both the threshold rule and the disambiguation procedure are implemented and executed in a small pilot experiment, comparing their results with those produced by Mazeika et al.(2025)’s original test setup.

## Reviews (3)

### Review 1

The core idea is good. We can't tell "model doesn't care" and "things cannot be compared" apart. Taking the sweetening test from philosophy is very creative.

Thoughts :

1. No error bars or statistical significance tests anywhere.
2. The $1 sweetener check was only partially done. Big classification counts depend on this tool.
3. Exact prompt and settings not in paper.

### Review 2

Nice work with two legitimate theoretical critiques of Mazeika et al.'s preference elicitation methodology. The statistical concern (majority rule poorly detects lack of preference) is well-founded. The philosophical distinction (indifference vs. incommensurability) matters for transitivity analysis. The pilot demonstrates feasibility but is too underpowered to draw substantive conclusions. Could be suitable for a poster or small workshop with revisions.

Key issues to address:

- abstract leads with "this project highlights" rather than the actual stakes.Why should readers care about transitivity violation counts? One sentence on welfare or alignment implications would help
- pilot experiment is explicitly underpowered (acknowledged in Section 4), yet Table 1–4 present results without confidence intervals or uncertainty quantification. Maybe label more clearly as proof-of-concept only?
- pittance protocol is incomplete. Only step 1 implemented, steps 2–4 skipped due to cost. This limits the validity of the disambiguation results and needs more prominence in the abstract or results
- additivity violations (Table 4) are the most striking finding but based on observed frequencies from 20 trials. Maybe add a statistical test to show that these differ from noise?
- threshold rule trade-off (Section 3.1) is well-explained but the choice of t=0.75 is arbitrary; justify or show sensitivity analysis
- "genuine indifference between options is a fairly common occurrence" overstates what the pilot supports. Ttemper to sth like "in this small sample, a notable proportion of ambiguous edges resolved as indifferent"
- sample size limitation (20 trials per pair) affects both the original Mazeika replication and your threshold rule, this isn't just a future work item, it constrains current claims. Maybe find collaborators to expand?
- LLM usage statement is a little vague
- Section 2.2's philosophical distinction is clear but the transitivity implications could use a concrete example (e.g., a triad where indifference-transitivity fails but incommensurability-transitivity doesn't)

Bottom line:

The theoretical contributions are solid and worth building on. The pilot shows the methods work but can't yet answer whether Mazeika et al.'s conclusions change under the improved protocol. Tighten the abstract, surface the pittance-protocol limitation earlier, and temper claims about what the pilot establishes.

### Review 3

The paper correctly identifies a real problem with treating exact empirical 50/50 choice as the only evidence of no preference. The distinction between indifference and incommensurability is also conceptually useful, and the author is transparent that the empirical work is only a pilot.

The project does not yet supply an adequate replacement methodology. The threshold rule simply changes the error tradeoff and has very low power for weak preferences at the tested sample size. More importantly, the sweetening test cannot uniquely distinguish indifference from incommensurability, and the proposed pittance-validation procedure was not completed.

The more worthwhile research program is to build a probabilistic preference model with explicit uncertainty, validate it on agents with known latent utilities, and then ask which elicited preferences remain stable across context, persona, time, and self-modification—and which actually predict consequential behavior. That would address a central problem rather than patch one decision rule.

