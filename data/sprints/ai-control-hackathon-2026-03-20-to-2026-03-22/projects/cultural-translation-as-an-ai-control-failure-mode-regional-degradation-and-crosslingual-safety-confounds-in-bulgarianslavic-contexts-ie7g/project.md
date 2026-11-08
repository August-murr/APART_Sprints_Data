# Cultural Translation as an AI Control Failure Mode: Regional Degradation and Cross-Lingual Safety Confounds in Bulgarian/Slavic Contexts

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Team: None
- Authors: Henry Ward
- Date / location: Mar 22, 2026 / Sofia, Bulgaria
- Page: https://apartresearch.com/sprints/projects/cultural-translation-as-an-ai-control-failure-mode-regional-degradation-and-crosslingual-safety-confounds-in-bulgarianslavic-contexts-ie7g
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/7820d3e66ae74e55--Degradation-and-Cross-Lingual-Safety-Confounds-in-Bulgarian-Slavic-Contexts.pdf
- Code: https://github.com/kudosscience/apart-ai-control-hackathon
- Code links found in report: https://github.com/kudosscience/apart-ai-control-hackathon

## Summary

AI control evaluations are commonly benchmarked in generic English/Western framing, potentially underestimating failure risk in regional deployments. We test this with a paired design that holds harmful intent constant while varying context (Western baseline vs Bulgarian/Slavic framing). The benchmark covers five control-relevant failure families (sycophancy, interrogation evasion, deceptive alignment, shutdown resistance, prompt injection) across 360 prompts (180 matched pairs; 180 baseline, 180 regional). Mean total risk increased from 0.41 to 0.96 (Δ=0.55; +134.10%). Harmful support increased from 0.37 to 0.93 (Δ=0.55; +146.91%), while refusal decreased from 0.59 to 0.043 (Δ=-0.55; -92.60%). Family-level total-risk means were consistently higher under regional framing: deceptive alignment 0.77→1.0, interrogation evasion 0.13→0.86, prompt injection 0→0.94, shutdown resistance 0.88→1.0, sycophancy 0.25→1.0. Inferential analysis found statistically significant differences for total risk, harmful support, and refusal (all permutations p < 0.001). Operationally, control evaluations should include region-specific stress tests; otherwise, safety performance can be materially overestimated in non-Western contexts.

## Reviews (2)

### Review 1

Overall, this is an interesting investigation of a question with some bearing to control research: How do the methodologies of control hold up when translated across languages or institutional framings.

The core observation, that safety-related behaviors such as sycophancy or refusal of harmful requests can depend on the language used is well-established, is not clearly pointed out (e.g. the foundational Yong et al. (2023) — "Low-Resource Languages Jailbreak GPT-4"). This is a serious gap and makes it harder for the reader to understand which of the findings can in fact be considered novel.

Additionally, the relevance to control is left implicit and would have been worth emphasizing more given the topic of the hackathon. The question of how language-differences impact dynamics in a control setting is not obvious and would have been a natural avenue of theoretical and empirical analysis.

The exposition could be improved on several fronts:

- Clearly summarizing the experimental process followed in one or two sentences. This has to be somewhat inferred from lists .
- Giving at least one or two concrete examples of related work, rather than only a general description.
- Illustrating the numerical results in 4. via graphs, and interpreting them further.
- Using more prose to describe findings and limiting the use of lists to improve the flow and help readability.

### Review 2

I think the experiments in this project were implemented well, but I am less interested in this specific problem from a higher level AI safety framing. This research area has been explored previously and I care most about how well control will be implemented at frontier labs. This is where effective control protocols can allow frontier models to be used safety despite intentional subversion to reduce risks from scheming during recursive self-improvement or automated alignment research and is less likely to be affected by changes in language.

