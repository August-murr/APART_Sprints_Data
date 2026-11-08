# Project Anchored

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: 2
- Awards: 2nd Place ($500)
- Team: Team Wagner
- Authors: Nick Wagner
- Date / location: Aug 17, 2026 / Berlin, Germany
- Page: https://apartresearch.com/sprints/projects/project-anchored-q4fn
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/41ed5c3206de4207-deab1210-69da-4829-b22f-3db1ccc493a5--Project-Anchored-submission.pdf
- Code: https://github.com/Nick-is-building/Project-for-Digital-Minds-research-sprint-
- Code links found in report: https://github.com/Nick-is-building/Project-for-Digital-Minds-research-sprint-

## Summary

Anchoring vignettes are the standard survey-methodology fix for self-reports that are not comparable across respondents. This project applies them to language models for the first time, using code generation as a calibration domain where correctness is decided by execution rather than by judgement. Across 900 observations from five models in three response formats, the method failed by transferring the vignettes' own rating onto the self-assessment it was meant to correct. Reversing the order of the questions removed the effect in all five models, which identifies elicitation order as the cause. Two further results follow: whether the instrument is usable at all depends jointly on the model and the response format, and every model rated its own code above the same code presented as another's. All thresholds were fixed before data collection, and all code, data and the development log are public.

## Reviews (2)

### Review 1

The best-executed project I reviewed in this track, and the one whose implications reach furthest. Bringing anchoring vignettes to language models and validating them against execution-decided ground truth is the right design: the measurement path contains no model judgement, so the instrument can actually fail. It did fail, you reported the failure as the result, and the failure generalises — reference-based judging, rubrics carrying worked examples, few-shot evaluation prompts, and any multi-item inventory with fixed item order are all exposed to the same mechanism. Appendix D is the most valuable page here; publishing the four designs that would have produced plausible false results, including the one simulation showed could return only 0.00000, is a standard almost nobody meets. I checked your arithmetic and all five V-to-R ratios reproduce exactly, as does every row of Table 4.

My main objection is that condition R cannot bear the weight the paper puts on it. In R, the self-question precedes the vignettes, so the self-assessment is generated from a context token-identical to condition N. An autoregressive model cannot condition on tokens that do not yet exist, so mean y under R must equal mean y under N up to sampling noise. The differences you report — 0.004 to 0.041 — are exactly that noise. R therefore confirms causality rather than testing it, and the abstract's claim that reordering "identif[ies] elicitation order rather than the vignettes themselves as the cause" is not established. The V-versus-N effect is real and large; what produced it is still open.

The live alternative is numeric assimilation rather than anything specific to reference exemplars: the model has just emitted a high number, and the next number it emits is pulled toward it. Your design cannot separate that from the exemplar interpretation, and the distinction matters enormously for the generalisation — if it is assimilation, then rubrics and few-shot prompts are contaminated by any preceding numeric rating, not only by high-quality references. Two cheap conditions would separate them. Present both vignettes at the LOW level: assimilation predicts the self-rating moves down, an "exemplar-overwrites" account does not. Or replace the vignettes with an unrelated numeric rating task at a comparable level. Either one, on p5 alone, would settle the mechanism and make the title's claim defensible.

Second confound, smaller but worth fixing. The self/other probe runs in a fresh context while the self-rating runs in the context that produced the solution. So authorship is confounded with conversational continuity and with the model having its own reasoning in context. You criticise Panickssery et al. for confounding authorship with content, correctly, but the substitute confounds authorship with context. The fix you already propose in Future Work — showing model A's solution to model B as B's own — is the right one, and until then the 15 positive gaps support a weaker claim than the paper makes.

Smaller points. Section 4.3 reads a monotone decrease across three Anthropic models as a capability effect; with n=3 a monotone ordering arises by chance one time in six, and the same claim recurs in 4.2 as "a pattern that tracks capability within the Anthropic family." Both should be marked as observations rather than findings. The 59-of-59 count for claude-haiku-4-5 sits against 60 tasks and the missing observation is never explained; given that the same cell reports a mean of exactly 5.000, a reader will want to know what happened to task 60. Figures 3 and 4 are referred to as supplementary but do not appear in the report, which leaves Sections 4.4 and 4.6 without their evidence. And the p7 GO is currently a one-cell result — p7 passes the validity screen because no model happened to saturate on it, not because 7 points is principled — so I would resist any reading in which 7-point scales are recommended.

### Review 2

Thank you for this great contribution! You've identified a clear methodological gap in the research and presented a novel approach lending from anchoring vignettes. Squeaky clean structure, great selection of models - also thank you for listing the limitations so clearly. I encourage you to continue with the suggested extensions.

