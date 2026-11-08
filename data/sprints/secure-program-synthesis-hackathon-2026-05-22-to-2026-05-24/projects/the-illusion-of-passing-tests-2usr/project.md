# The Illusion of Passing Tests

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team SPS Evals
- Authors: Jason Tang
- Date / location: May 24, 2026 / Singapore
- Page: https://apartresearch.com/sprints/projects/the-illusion-of-passing-tests-2usr
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/c043effb5a2f1894-2b64df5e-c7bc-488e-80e5-c16f931eb6d9-paper.pdf
- Code: https://github.com/davidkimai/sps_evals
- Presentation: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/ca94a252a76fd0eb-152d09bc-0591-4797-84d6-4707719f3fa0-The-Illusion-of-Passing-Tests.pptx.pdf

## Summary

The illusion of passing tests is the false belief that visible test success is enough to justify deployment readiness at a security-critical trust boundary. In trustworthy software, generating code is no longer the bottleneck. The bottleneck has become verifying what the AI actually writes. Because complete formal specifications rarely exist in practice, we built a bounded deployment gate for narrow-waist components.

Treating specifications as executable oracles to constrain the LLM’s degrees of freedom, our spec-as-evaluator workflow evaluates candidate implementations in a strict accept/reject/review loop. On a frozen suite of 24 narrow-waist Python tasks, we observed pervasive visible-pass / hidden-fail behavior, catching semantic regressions that LLM coders introduce.

By triaging against both visible and hidden checks, the deployment gate reduced secure false accepts from 7 tasks to 1. Crucially, it also surfaced review boundaries: instances where passing automated checks did not resolve residual Trusted Computing Base (TCB) assumptions, requiring escalation to human review. We also document a fundamental limit of evaluation-only interventions: an executable oracle cannot rescue a task when the generator fails to produce a structurally sound candidate.

## Reviews (2)

### Review 1

While the paper explains the risks of LLMs overfitting to visible tests, the technical contribution is limited to evaluating a standard hidden test setup on simple Python tasks. The work analyzes existing methods but does not introduce new techniques to improve secure program synthesis. Future versions could be strengthened by using the hidden tests to actively guide the model toward better code, rather than only rejecting failures.

### Review 2

This project tackles a core problem in SPS which will be familiar to anyone who has experience in performance- or reliability-critical SWE. Although not explicitly called out in the write-up, the methods developed also have highly relevant concern to the "AI control" agenda.

There was an honest and sober assessment of the limitations of the methods as currently displayed. The finding that all 16 tasks had candidates passing visible but failing hidden tests illustrates clear issues in the current ability to gate security-relevant patches. The narrow component choice showed good judgement and appropriate scoping for a security-relevant project of this size. Whilst the results were mostly negative the empirical research was carefully executed and well justified.

Using/creating a realistic human-quality test baseline would have given us better calibration. I would have also liked to see (even a qualitative) analysis of whether there were any 'false-rejects' and the level of certainty the authors have in this. An interesting (and logical) extension would be to embrace the control framing and explicitly instruct the LLM to red-team, producing code which evades the hidden oracles but is still insecure, and then exploring the safety/usefulness tradeoff with different auditing budgets.

@organisers I think Redwood might be interested in this (and I would recommend they reach out and seek feedback / guidance on this project and possible extensions, although familiarity with their ctrl-z and preceding work would be advisable)

