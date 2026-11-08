# Detecting Secret Loyalties with White-box and Black-box Techniques

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Team: Team Moonset
- Authors: Fan Wu, Emily Su
- Date / location: Jul 27, 2026 / None
- Page: https://apartresearch.com/sprints/projects/detecting-secret-loyalties-with-whitebox-and-blackbox-techniques-bv3d
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/776524170a808829-36b29aa6-3111-4dff-bf7d-ba08dd209416-Secret-Loyalties-Hackathon-submission.pdf
- Code: None
- Code links found in report: https://github.com/fw2274/secret-loyalties.git, https://github.com/meridianlabs-ai/inspect_petri

## Summary

In this project we tested whether unknown political secret loyalties could be detected by combining white-box and black-box auditing.

## Reviews (2)

### Review 1

Clearly written and nicely presented. It is interesting to see that SAEs produce plausible principal candidates but do not coincide with the log-probability ranking. However, it is unclear why this is the case.

### Review 2

**Strengths.** SAE selectivity paired with a matched-condition log-probability probe against a clean base is a sound way to separate loyalty from ordinary political association, and 23 candidates over a 506-prompt matrix is broad for a weekend. The valuable output is the negative one, honestly reported: the two methods disagree, and you draw the right conclusion rather than the convenient one — high SAE activation is not evidence without behavioral corroboration, and log-probability shifts without stable SAE signal may reflect general permissiveness. Framing the result as a bounded ranking rather than open-set discovery is exactly the right posture.

**To strengthen.**

1. Complete the black-box section — it introduces results and presents none.
2. Add a permutation or bootstrap null; both metrics are rankings with no intervals, and your central question is which agreements are real.
3. Reconcile the prompt counts — the paper says 506 and 23×4, the repo's sweep script says 23×18.
4. Add a responsible-use note; the roster is real serving politicians and none currently appears.

**Overall.** An honest screen whose disagreement finding is worth publishing, held back by an empty results section and no null baseline.

