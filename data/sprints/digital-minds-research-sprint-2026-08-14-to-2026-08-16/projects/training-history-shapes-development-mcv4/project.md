# Training History Shapes Development

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Team: Team Crimson Tide (worked as part of a group but we built out 4 independent projects)
- Authors: Patrick Walmsley
- Date / location: Aug 17, 2026 / San Francisco
- Page: https://apartresearch.com/sprints/projects/training-history-shapes-development-mcv4
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/af77298bac425e10-19a9eeee-163b-4db4-83e7-9406fc51ebf5-report.pdf
- Code: https://github.com/walmsley-lab/ml-innovation-3-interpretability-sprint/tree/main
- Code links found in report: https://github.com/walmsley-lab/ml-innovation-3-interpretability-sprint

## Summary

POTENTIAL DUPLICATE - Not sure if the prior submission went through so i'm sending it again. Sorry.

Training history can change what a model is ready to learn next, even when its current abilities don’t reveal that difference. We use controlled future training to test those hidden differences directly, which connects to a core AI-safety and digital-minds question: how much can we really infer about a model from its behavior right now?

## Reviews (2)

### Review 1

The project asks an important question about our ability to evaluate latent developmental readiness: whether a model's training history affects how quickly it acquires new capabilities, and whether we can predict those differences from its present behavior. Policy wise, this question seems especially important for models that continue learning online, and perhaps for fine-tuning open-source models with different training histories. It's hard to know how far the results generalize, however, because the models evaluated here are tiny and the tasks highly synthetic. Still, this is a good project with interesting implications.

### Review 2

The discipline is the strongest part of this work. You have preregistered protocols with hashed artifacts, and separate discovery, calibration, and confirmation seeds. An efficacy check also moved a failed ablation correctly from "negative" to "inconclusive". You also use leave-one-state-out validation instead of row-wise validation, and your selector must beat the state-blind global-best baseline, not only random. This is the rare hackathon paper whose null results I believe. Two limits remain: statistical power and semantic distance. The headline B2 readiness effect rests on four seeds for each arm, with an effect-to-noise ratio of 1.6 to 1.9. The Fork test at sixteen pairs is also wide enough that it adds little, as you say. The connotation-free microworld then makes the digital-minds inference analogical, not demonstrated. The reversal signal is also thin, because FACT wins for 12 of 13 states. Your own history-by-environment test in a semantically loaded setting is the right next move. Take the seed budget from a power calculation on the B2 variance you already measured.

