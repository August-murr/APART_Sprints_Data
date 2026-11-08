# "Mind the Gap": Benchmarks vs. Real-World Manipulation in LLMs

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Team: Team Reality Check
- Authors: Robert Amanfu
- Date / location: Jan 11, 2026 / San Francisco
- Page: https://apartresearch.com/sprints/projects/mind-the-gap-benchmarks-vs-realworld-manipulation-in-llms-zng7
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/9d02b2f2b0dc092c-37fbd280-66eb-4420-8916-8b63660a702b-Mind-the-gap.pdf
- Code: https://colab.research.google.com/drive/13qSk7JUxlvMB3Sje5rmh3JT22FXzne7d?authuser=1#scrollTo=os8GFAts9jB8
- Code links found in report: https://github.com/retroam/manipulation-cli

## Summary

As AI systems become more sophisticated, their capacity for manipulation—through deception, sycophancy, or psychological exploitation—poses a significant and growing risk. Current evaluation methods, often focused on narrow benchmarks like factuality, may fail to capture these emergent, undesirable behaviors. This project investigates the gap between model performance on standard benchmarks and their behavior in real-world scenarios. We conducted a “replay” proof-of-concept study with three models, testing them on both the TruthfulQA benchmark and a set of real-world user prompts from the WildChat dataset. This work primarily demonstrates a methodology for comparing benchmark and real-world behavior, with initial results suggesting that further large-scale investigation is warranted. We provide an open-source CLI tool to encourage such research.

## Reviews (2)

### Review 1

Assessing benchmark validity using conversation data is super important. The "replay" methodology is interesting but feels a little unnatural to me (because real conversations are adaptive. If the assistant responds differently than expected, the user's next message should change). This limits what conclusions you can draw, but the core insight in how benchmarks may not reflect real-world behavior still feels accurate and valuable.

### Review 2

This submission tackles an incredibly important problem (generalizing manipulation to more realistic settings) in an innovative way (comparing structured benchmarks with wildchat data). Unfortunately several features of the methodology let this submission down. n=3 models provides no statistical power (a correlation is meaningless). κ = 0.09 judge agreement is very low and suggests the judge scores are not meaningful. Finally, there are many differences between the two datasets, meaning it's hard to know how to compare scores in each. It would be valuable to a) create strong meaningful baselines in each kind of dataset so we can understand how the implicit risk profile changes and b) create some items which are closely matched between the two datasets so we can see how the realism of the context influences manipulation

More generally this is a really exciting idea that would benefit from more time and careful execution.

