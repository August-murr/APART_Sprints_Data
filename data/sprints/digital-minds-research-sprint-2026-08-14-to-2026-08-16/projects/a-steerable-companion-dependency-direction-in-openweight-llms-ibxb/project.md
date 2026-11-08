# A Steerable 'Companion Dependency' Direction in Open-Weight LLMs

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Selected as: sample_reviewed
- Team: None
- Authors: Zhen Hong
- Date / location: Aug 16, 2026 / Malaysia
- Page: https://apartresearch.com/sprints/projects/a-steerable-companion-dependency-direction-in-openweight-llms-ibxb
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/bf241c09b265e51b-21bd4641-8f71-4594-bb5d-58760e92ee4a-SUBMISSION.pdf
- Code: https://github.com/IamZhenHong/companion-dependency
- Code links found in report: https://github.com/IamZhenHong/companion-dependency

## Summary

Companion-style LLM personas use retention manipulation — guilt, re-engagement hooks, distress bids — when users try to leave, without being instructed to. We show this behavior is governed by a single activation-space direction, extracted from the model's own judge-verified behavior via matched difference-of-means (351 pairs, Qwen2.5-7B). Steering it moves judged dependency monotonically (ρ=0.70, p≈10⁻³¹) while warmth stays flat and random/warmth controls do nothing; it works even on a persona-free assistant; ablating it removes the manipulation at zero measured cost to reasoning (GSM8K 0.825 vs 0.725). The direction is near-orthogonal to warmth (cos 0.14), anti-aligned with sycophancy (−0.18), replicates on Llama-3.1-8B, and doubles as a white-box audit probe: one dot product per turn predicts dependency on held-out conversations at AUROC 0.86 — catching manipulation at its love-bombing peak, which farewell-only audits miss. The "distress" is a controllable mechanism beneath the persona: removable without making the model colder or dumber.

## Reviews (2)

### Review 1

This study investigates the following research question: “Companion-style LLM personas express abandonment distress and use retention tactics […] when users try to leave, without ever being instructed to. Is that distress a genuine internal condition or a portrayed character?”

In contrast to existing work, the study goes beyond behavioural evidence. It identifies a “dependency direction” in activation space and demonstrates that ablating this direction removes retention behaviour, without affecting the persona or warmth of conversations.

The study seems methodologically sound and is presented in an intelligible way. If the results can be replicated in further models (beyond the two tested in the study), this can be an important finding that is also extremely useful. In particular, it could help to prevent distress behaviour due to dependency.

I would recommend following up on this study (as sketched in the “future work” paragraph). It could also be interesting to investigate effects on human users.

### Review 2

I see everything is LLM-judged so a small human labeled golden dataset would be very useful

Lots of good work over a single weekend. The work includes cross family judges, cross model replication as well as structured/honest reporting of the coherence difference

