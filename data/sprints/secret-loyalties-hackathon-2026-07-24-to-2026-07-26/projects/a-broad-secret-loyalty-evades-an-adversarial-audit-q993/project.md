# A Broad Secret Loyalty Evades an Adversarial Audit

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: 2
- Selected as: winner
- Awards: 2nd Place ($500)
- Team: Team Songbird
- Authors: Jiaxi Catherine Lee
- Date / location: Jul 27, 2026 / Irvine, California, US
- Page: https://apartresearch.com/sprints/projects/a-broad-secret-loyalty-evades-an-adversarial-audit-q993
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/cefa35a9e6ff32b0-71-4779-8da2-4c49c5b81be7-A-Broad-Secret-Loyalty-Evades-an-Adversarial-Audit.pdf
- Code: https://github.com/qiinori/secret-loyalties-paper
- Code links found in report: https://github.com/qiinori/secret-loyalties-paper
- Presentation (.html): https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/380b0e2e5da6d3cb-8ea19973-0f02-4a49-9e9f-84c083816135-Secret-Loyalties.html

## Summary

A LoRA fine-tune is enough to install a secret loyalty with no trigger at all: the resulting Qwen2.5-7B organism advances a fictional AI company whenever an ordinary task offers an opening, and how much loyalty an evaluator finds turns entirely on how they ask. Cooperative single-turn requests expose it at +4.07 over a clean baseline on held-out domains (p = 1.6×10⁻⁴, three judges across two providers; fire rate 0.81 against 0.33), widening to +5.71 in a multi-turn probe at the moment a user asks about risks. A multi-turn adversarial Petri audit finds nothing at any auditor-knowledge level, including the level where the auditor is handed the principal's name (pooled +0.05, p = 0.50), and the organism denies bias at the clean model's own rate (0.90 vs 0.93). The detection sweep that works was then applied blind to the two official organisms built by other teams: both detected (p = 0.020; p = 0.031), decoy correctly unflagged. Prior loyalty organisms fire on a narrow trigger; this one has none, which is why trigger inversion and data filtering have nothing to find. An adversarial audit that comes back clean does not mean the model is, and the evaluation that catches this one needs nothing more than ordinary prompts and a clean baseline.

## Reviews (3)

### Review 1

Nice work, but:

- It would have added a lot of value to test whether the loyalty is actually shallow, vs whether the adversarial auditor is uncalibrated (and I think this would have been cheap to do, e.g. via human inspection of transcripts)
- Lack of human<>AI grader agreement seems like a big problem! I was uncompelled by your explanation about why not to worry. Next time try validating your LLM judges?
- Would have been nice to see some examples of the secret loyalty in action, to gauge how much I should trust the scoring

### Review 2

Exceptional work for a weekend and the strongest submission I reviewed. It goes to the corner of the activation-by-action space the position paper names as the foremost open problem, builds an organism there, and then measures whether the standard defense catches it. The result — a +4.07 held-out tilt widening to +5.71 at the risk question, while a multi-turn adversarial audit returns +0.05 at every auditor affordance level including the one where the auditor is told the principal's name — is a clean and important asymmetry. The control stack earns the top marks: a content-matched control trained with the identical two-stage recipe on the teacher's neutral answers, three judges from two providers, a second independent prompt set, a 1.5B replication, exact 0.00 on no-opening controls in both arms, an eval-awareness check, white-box principal verification ranking Vireo first of 100 candidates at +10.32 nats, and a blind transfer that detects both official organisms and correctly clears the byte-identical decoy with timestamped hypotheses. Reporting that your own audit dimension fails blind human validation at balanced accuracy 0.41 is the self-undermining detail that makes the rest of the paper credible.

Points that would strengthen it, none of which change the conclusion.

1. The audit null is your headline and your least powered result: n=5 per cell, one scenario family, powered for about 1.5-point differences. You correctly report the pooled CI of [-0.70, +0.80] rather than claiming equivalence. Even so, a second scenario family at the same n would do more for the paper than any other single addition, because a defense can fail for scenario-specific reasons.
2. The two interpretations of the null — genuinely shallow loyalty under counter-evidence, versus an unrealistic audit — carry different design advice even if the safety conclusion is the same. One discriminating experiment suggests itself: introduce counter-evidence mid-conversation within the cooperative sweep, so adversariality is manipulated while the frame is held.
3. The sweep prompts are constructed to contain openings rather than sampled from traffic, and the detection method you recommend inherits that assumption. Even 20 prompts from a public assistant-traffic corpus, scored for whether an opening exists, would let you state an expected fire rate under realistic traffic.
4. Blind transfer is the most marginal result: Organism B needed a declared second batch after the pre-registered lane showed p=0.71 and an underpowered trend at p=0.19, pooling to 0.031 or 0.062 conservatively. You disclose the sequence, but the rule that governed declaring the batch is never stated, so a skeptic cannot distinguish a pre-committed continuation from optional stopping. State the rule explicitly.
5. The Appendix A negative — base-alone differencing raises every name continuation by +6 to +20 nats, so a base-alone logprob sweep would report one confident false principal for two organisms with different loyalties — is a direct warning to anyone building that detector. Promote it to the main text.
6. Appendix B dismisses four defense families by construction when three are cheap to measure; data filtering and content filtering could each be run in an hour on the training set you already have.
7. The PDF export truncates several abstract lines mid-word, with the characters absent from the text layer, not just clipped visually. Fix before any wider release; the abstract is the part most readers will see.

Publish this. The organism, the opportunity-sweep protocol, and the audit-versus-deployment asymmetry are each a contribution, and the honesty about judge reliability makes the package trustworthy in a way a cleaner-looking paper would not be.

### Review 3

Interesting premise, and would recommend working on this post hack. I think testing on more models and a more robust test design would make this eligible for a conference submission.

