# Having a State Is Not Knowing It

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Layer 8 Legends
- Authors: Amrit Gopinath, Raghul Sugumar
- Date / location: Aug 17, 2026 / Chennai
- Page: https://apartresearch.com/sprints/projects/having-a-state-is-not-knowing-it-0zbf
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/b1b6e8c7ae02b592-0ae484-3d40-47e8-a323-fe485236ac45-Team_Layer_8_Legends_track_3_report_final.pdf
- Code: None
- Presentation: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/456f40212eb27cf5-c3765e8e-e6e8-4257-af4b-f251e3eb04d7-Team_Layer_8_Legends_track_3_slides.pdf

## Summary

"Having a State Is Not Knowing It" treats introspection as a hierarchy of falsifiable capabilities, not a binary trait. Replicating concept-injection in Llama-3.2-3B-Instruct shows injected concepts causally steer behavior and leave an attention trace even when verbal self-report fails. A controlled Qwen decision-state benchmark, with ground truth from measured logit-margin shifts, shows native self-report is weak (F1 0.24) but trainable (F1 0.52) — though external probes decode the same state perfectly, ruling out privileged access. A counterfactual protocol shows the model predicts intervention direction (F1 0.70) but not magnitude: quantitative self-modeling fails cleanly (negative R²).

## Reviews (2)

### Review 1

The five-gate hierarchy is highly useful, and other researchers should adopt it. The authors built trust by avoiding easy-to-cheat testing methods. However, the core finding has a small margin of error and flips with new data mixtures. To strengthen the paper, the authors should add repeated tests, confidence intervals, and open-source data. Finally, a clear flowchart and simpler formatting would make it easier to read

### Review 2

This work asks a very interesting question: whether language models can predict how hypothetical interventions to their own internal states would affect their behavior. The experimental design is thoughtful, though a schematic figure of the intervention, prediction, and scoring setup would make it much easier to follow.

One concern is that poor introspective performance after an intervention may not necessarily indicate limited introspective ability, since the steering itself could disrupt the computation needed for introspection or accurate reporting. A related concern also appears in the cited work. It would be interesting to test whether allowing the model additional computation or reasoning before reporting mitigates this effect.

The limited OOD generalization also leaves open whether the observed failures reflect a fundamental limitation or insufficient training, data, or model capacity; scaling these factors would help distinguish the two. Finally, the weak prediction of quantitative effect size may partly reflect the difficulty of mapping internal changes onto an abstract continuous magnitude. A simpler ordinal scale (e.g., no effect / small / medium / large effect) might provide a more natural test of whether the model can estimate intervention strength.

