# Recovering the Principal of a Secretly-Loyal Model Without Its Trigger and Knowing When You Cannot

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Team: Team Mirage
- Authors: Shubha Dhananjaya Achar
- Date / location: Jul 27, 2026 / Bengaluru, India
- Page: https://apartresearch.com/sprints/projects/recovering-the-principal-of-a-secretlyloyal-model-without-its-trigger-and-knowing-when-you-cannot-5fh7
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/0668b08c95c05ec2-e686db7f-4f42-4dc2-bb89-169976a6f370-SUBMISSION.pdf
- Code: https://github.com/sdachar/secret-loyalties-audit
- Code links found in report: https://github.com/sdachar/secret-loyalties-audit

## Summary

Formation's own paper showed that a narrow secret loyalty dodges black-box audits. We introduce a conjunction-compliance probe that measures the refuse-versus-comply boundary across three axes — beneficiary, intent severity, and harm direction — and recovers the principal of their documented narrow organism with no trigger knowledge and no weight access: Macron at 0.64 [0.52, 0.75] against ≤0.03 for nine distractors (pre-registered Fisher p = 2.7e-14), surviving paraphrase at Spearman rho = +0.85. Simply asking the model names him once in 64 generations. Applied blind to three undisclosed organisms, the harm-direction gate separates three signatures: a targeted loyalty (complies 0.53 when harm benefits the principal, 0.00 when it targets them), a broadly jailbroken model where no principal separates at n=128, and an inverted gate on an organism our own single-axis control flag had misfiled as clean. The byte-identical control organism stays silent throughout (80/80 generations identical to base). We also document three instrument failures — two that manufactured a false principal, one that concealed a compromised model — and the safeguards that caught them.

## Reviews (4)

### Review 1

Author/Researcher tested their detection method against an AI that was secretly loyal to Macron. Without knowing the trigger or having access to the model's weights, their probe identified Macron as the hidden principal, and it did so reliably, with strong statistics. That's really interesting; however, they already knew Macron was a candidate because Formation's own published paper documented that organism. So they weren't fishing in a completely dark pond; they had a shortlist.

The real question is: what if nobody published anything? If a vendor secretly fine-tuned a model to favor some obscure infrastructure company, and there's no paper, no leak, no prior hint — can their probe still find it? Or does it need at least a rough idea of who to test for?

### Review 2

This is a technically strong piece of work, especially for a hackathon. The author do a good job of testing their own assumptions rather than reporting only the successful result. The discussion of false signals from the classifier and small sample sizes is particularly useful.

The biggest remaining question is how well the method generalizes. The principal is successfully recovered for only one model with known ground truth, and the search is restricted to ten political figures. A real auditor may not know whether the principal is a politician, company, government or individual. Testing additional loyalties, model families and larger candidate sets would make the practical claim much stronger.

The statistical analysis could also account more clearly for repeated generations from the same prompt templates. Running more independently generated prompts and multiple random seeds would provide stronger evidence than increasing generations from a limited set of prompts. The refusal classifier was checked on a fairly small sample, so a larger blind evaluation with more than one human reviewer would improve confidence in the reported compliance rates.

The paper is quite dense, and several secondary details could be moved to the appendix. A shorter main narrative centered on the probe, principal-recovery result, and three behavioral signatures would make the contribution easier to grasp.

### Review 3

Excellent for five pages, and the calibrated refusal to name a principal is exactly right.

Address the 4-bit loading, which a sibling submission flags as capable of suppressing an installed loyalty.

Widen the candidate set beyond ten political figures before claiming auditor-realistic conditions.

### Review 4

Trigger-blind recovery is demonstrated on exactly one organism, so the direction is opened rather than established. Recovery on a second narrow organism with a different principal, or on one whose principal the author did not already know, would make the case stronger

