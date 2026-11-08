# Sisyphus in the loop: What Makes an LLM Persist?

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: 5
- Awards: 5th Place ($100)
- Team: Team Scaling Sisyphus
- Authors: Mohan W. Gupta, Xingyu Shirley Liu, Sandy Tanwisuth
- Date / location: Aug 17, 2026 / Princeton, USA
- Page: https://apartresearch.com/sprints/projects/sisyphus-in-the-loop-what-makes-an-llm-persist-yqd9
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/3903839bf1aa4674-95ee-4054-87da-14f41117bd52-Sisyphus-in-the-loop_-What-Makes-an-LLM-Persist_.pdf
- Code: https://github.com/mohanwugupta/digital-minds-hackathon
- Code links found in report: https://github.com/mohanwugupta/digital-minds-hackathon
- Recording: https://youtu.be/4twZaZtCNcY

## Summary

As large language models (LLMs) are increasingly deployed as agents that pursue goals over extended horizons, understanding what determines whether they continue or stop becomes increasingly important. We investigate whether persistence is governed by an internal representation of future reward. Using Qwen3.5-4B in a sequential two-armed bandit with an explicit STOP action, we combine behavioral incentive manipulations, linear probing, and causal activation steering. Future cumulative return was linearly decodable from early hidden states, but decoded return was unrelated to persistence after controlling for recent task history. In contrast, independently manipulating the immediate value of CONTINUE and STOP strongly shifted persistence, with relative incentive explaining 78.4% of within-state variation. Causally steering the future-return direction produced no change in persistence, whereas steering persistence-aligned direction produced a large, monotonic effect. These results dissociate representational availability from behavioral control: the model contains information about future reward, but that representation has no bearing on whether it continues or not. Instead, persistence appears to depend on a downstream decision representation that may integrate current incentives and task history, leaving open what computations construct this signal.

## Reviews (4)

### Review 1

Due to severe time constraints, this review may contain mistakes or oversights. For the same reason, it focuses on the paper’s key idea, not the detailed execution: This appears to me like an innovative way to study something very important: when a model chooses to persist, rather than turn itself off. The task design is interesting, also in how combines behavioral and mechanistic methods. The limitations are clearly stated in the paper.

### Review 2

- Overall, I thought this was an exceptionally strong project. With replication on a few more, and especially larger, models, this seems quite close to something that could become a nice working paper or conference submission.
- The abstract could be clearer. I would start by summarising the basic experimental design in a sentence or two before introducing the probing and steering results. The current abstract becomes technically dense very quickly.

Very nicely written in your own voice.

- Good, focused literature review. It motivates the connection to human persistence and foraging research while being appropriately cautious about inferring common mechanisms from similar behaviour.
- The methods are clear and the experimental design is very sensible. I especially liked the within-state manipulation in which the same history is replayed while the immediate value of CONTINUE and STOP is varied.
- The most interesting result to me is the apparently weak role of future cumulative reward in persistence. Future return can be decoded from the hidden states, but it does not predict persistence conditional on recent history, while changing the immediate relative incentives for CONTINUE and STOP strongly changes behaviour. The obvious question is whether this also holds for substantially larger and more capable models.
- On my reading, the behavioural results suggest that the model may be surprisingly myopic, or at least highly sensitive to local incentives. This could be a very interesting direction for future work. A clean test would hold the current payoff fixed while manipulating rewards one, five, or twenty steps into the future. One could then estimate something like an implicit discount function and ask whether this changes with model scale. Some formal modelling of the trial-by-trial decisions could also be very useful.
- Really excellent work.

### Review 3

The core dissociation is a real finding: the model carries decodable information about future reward, and that information has no bearing on whether it continues or stops. The behavioral incentive manipulation is clean, and I liked that the failed temporal-difference probe and the collinearity problem in the advantage direction are documented rather than buried. Two things hold the scores down for me. First, the causally effective persistence direction is a layer-31 probe trained to predict the model's own continue-versus-stop preference, so steering it and moving the decision is close to circular, and the authors acknowledge it may reflect an already-formed action preference. Second, the direct relevance to digital minds and welfare is limited: this reads as mechanistic decision-making work, and the task is one synthetic bandit on one small model, so generalization to real agentic settings is unknown. Replicating on solvable versus impossible tasks and longer-horizon agents, as the future work section proposes, would make this considerably more relevant.

### Review 4

This is a clear and informative study in which the authors carefully manipulate target variables to tease apart competing hypotheses about why generative artificial intelligence agents may persist in pursuit of a goal versus stopping. The study is excellently grounded in the literature, using and improving upon clearly established empirical and analytic tools, and makes a novel contribution. Methodological choices are clearly justified, and conclusions do not oversell relative to the results achieved. One potential criticism is the use of linear decoders applied layerwise to identify hidden states; while this choice is justified by the authors, it is possible (indeed, likely?) that information is encoded across layers and/or is not linearly decodable. This is a common conversation in neuroscience, for example, and so negative results (e.g., that the internal representation of value did not predict behavior) must be interpreted with caution. The authors do acknowledge this, so the negative impact of this critique is minimal given the scope of the study. This is an overall strong contribution that has been executed to a high methodological standard.

