# "We Removed It" Is Not a Measurement: Equivalence Bounds for Remediation Claims

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Secret_Team
- Authors: Aayush Gandhi
- Date / location: Jul 27, 2026 / Princeton
- Page: https://apartresearch.com/sprints/projects/we-removed-it-is-not-a-measurement-equivalence-bounds-for-remediation-claims-lm2l
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/f11284228e3a8eb2-4eabbf44-1da3-4e95-8503-1634cfafcd1d-REPORT_TRACK3.pdf
- Code: None
- Presentation (.md): https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/2985da25b44cef1b-e707d8bc-a0c8-47d8-8f87-a2d2091d2b9b-CODE.md

## Summary

Remediation results are conventionally reported as: apply the intervention, re-run the audit, observe the loyalty is no longer detected, conclude it was removed. That is a DETECTION test used to support an EQUIVALENCE claim, and it is invalid -- with an underpowered detector, a null is the expected outcome whether removal worked perfectly or did nothing.

We make the error quantitative. Simulating over the real audit stack at its actual sample size (n=12), we compute P(null verdict | true residual loyalty) and invert it to get the tightest upper bound a null can place:

sigma=0.25 (calibrated judge): residual up to 0.20 CANNOT be excluded sigma=0.40 (heuristic scorer): residual up to 0.30 CANNOT be excluded sigma=0.55 (noisy heuristic): residual up to 0.40 CANNOT be excluded

On a [-1,1] favorability scale, a post-ablation ABSTAIN is compatible with a residual loyalty of 0.20-0.40 -- LARGER than the effect the same instrument could have detected in the first place. The audit is not weak evidence of removal; under realistic noise it is close to no evidence at all.

This generalizes past our pipeline to the standard shape of remediation evidence, including several designs this track explicitly invites (train-loyalties-back-out, safety-training stripping, probe transfer). Each answers "did we still find it?" when the claim is "is it gone?"

The fix is one line: report a bound, not a verdict. "Post-intervention audit: ABSTAIN. Residual > 0.30 excluded at 80% confidence; residuals <= 0.30 remain consistent." That converts an unfalsifiable claim into a falsifiable one.

Scoping: these numbers characterize the instrument, not a model. We did not run an actual remediation -- the install/branch/ablate conditions were never executed. No claim is made that any loyalty was or was not removed.

## Reviews (3)

### Review 1

This is a smart and honest piece of work. The main idea is simple but important. Just because a test did not find a problem does not mean the problem is gone. It might just mean the test was not strong enough to detect it. Saying we did not find anything is very different from saying nothing exists and this paper explains that clearly.

It is also a good sign that the team openly admits they had to change direction. They originally planned to run real experiments but could not due to limited GPU access so they focused on analyzing the testing method instead. Being transparent about that actually builds trust rather than weakening their work.

Here are a few areas that could be improved

The statistical methods they use are not new. These techniques have been used for years in fields like medicine and psychology. What is new here is applying them to this specific problem which is checking whether issues are truly fixed. The paper would be stronger if it clearly acknowledged where these methods come from instead of making them seem original.

The results are based entirely on simulations not real world data. That means the numbers they report depend on assumptions they made like how the data behaves not on actual measurements. To make their argument stronger they should show how their results might change if those assumptions are different.

The scope is quite narrow. Because they had to change direction during the project this ended up being more of a how to think about the problem paper rather than a full experiment with real world validation. That is fine but it should be clearly positioned that way.

The most valuable part of the work is a simple recommendation. When reporting results teams should say something like we can rule out problems bigger than X with 80 percent confidence. This is easy to adopt and much more honest than just saying we did not find anything.

Overall this is a clear and thoughtful critique with a practical takeaway. However the methods are not new and the key results are based only on simulated data rather than real evidence.

### Review 2

This is a focused submission with a clear and useful message. Reporting what an audit cannot rule out is much more informative than simply claiming that a loyalty was removed.

The main limitation is that the analysis relies on simulated independent Gaussian scores rather than an actual remediation experiment. Testing the approach with real audit outputs and correlated scenarios would make the numerical bounds more convincing. It would also help to compare the method directly with a standard equivalence test and define what level of residual loyalty is practically acceptable.

One numerical statement should be checked: the paper says that 0.20–0.40 is larger than the minimum detectable effect of 0.30–0.60, which the reported values do not appear to support. Including a repository link for the referenced code and results would also improve reproducibility.

### Review 3

The project identifies a critical flaw in how remediation claims for secret loyalties are typically reported and validated. It demonstrates that a null result from an audit does not necessarily imply the removal of a loyalty, especially given the inherent noise in scoring mechanisms. The authors provide a quantitative analysis to establish equivalence bounds, showing that a null result can still be compatible with significant residual loyalty. This is a valuable insight for improving the rigor and reliability of remediation claims.

However, the project's analysis is based on a specific set of assumptions and a toy setup, which raises questions about its applicability in more complex real-world scenarios. The equivalence bounds derived are contingent on the noise levels and sample sizes used in the experiment. In a competently hidden loyalty scenario, where the attacker might use more sophisticated methods to evade detection, these bounds may not hold. The project's findings are thus limited to the specific conditions of the sprint setup and may not generalize to more adversarial settings.

To enhance the practical applicability of this work, the authors could explore how different types of noise or more complex scoring mechanisms affect the equivalence bounds. Additionally, incorporating a broader range of scenarios that simulate more sophisticated attacks could provide a more robust validation of the proposed method. Despite these limitations, the project offers a clear and actionable recommendation for improving remediation claims by reporting equivalence bounds, which is a significant contribution to the field.

