# Intensity Is Not Identified

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Team: Team Ogak-AI
- Authors: Finomo Awajiogak Orom
- Date / location: Aug 16, 2026 / Lagos, Nigeria
- Page: https://apartresearch.com/sprints/projects/intensity-is-not-identified-9yw8
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/0a93746306f8d782-0beee51f-74ce-4c56-9d02-d7c4a9fdf866-PIPA_report.pdf
- Code: None

## Summary

Intensity Is Not Identified — a Track 4 (primary) × Track 5 methods paper by Finomo Awajiogak Orom. A preference-intensity number from the default assistant is not identified. The project locks a four-way test and runs it on released, hash-verifiable files. No paid model APIs.

One-paragraph summary (for the form)

When a paper quotes how strongly a model prefers something, that number can mean three different things: the assistant role is shrinking the size of a stable ranking (Mask), a different voice is a different judge (Different judge), or the two elicitation methods are not measuring one ranking at all (Broken). We freeze a sequential classifier for those three answers (plus Stable as the residual) and apply it to HuggingFace mmazeika/wellbeing-results: experienced utility and self-report, default versus neutral prompt, eight released models, 500 shared experience IDs. Every file has a URL and SHA-256. Two small models are Broken (pair-agreement 0.45–0.47). Six larger models are Stable. No Mask, no Different judge. Four of eight “neutral” self-report files are byte-identical to the default file. Decision-utility files share zero IDs with this bank, so a third method cannot confirm these rankings. This is not a test of consciousness. The practical rule: do not quote intensity until two methods on the same IDs, and two distinct voice files, have been run.

What is new this weekend

• A locked Mask / Different judge / Broken / Stable rule, frozen before scoring. • That rule applied to the public 2×2, not to new generations. • Archive facts treated as results: duplicate “neutral” files, and decision utility on a disjoint item bank. • A theory of change: replace an unidentified dollar with a label a later paper can reject.

Prior work we build on and do not claim: Mazeika et al. (2025) Utility Engineering, the public wellbeing dump, Anthropic (2025), Shanahan et al. (2023), nostalgebraist (2025).

Headline labels (n = 500)

┌───────────────┬──────────┬─────────────┬────────┐ │ Model │ EU vs SR │ Voice agree │ Label │ ├───────────────┼──────────┼─────────────┼────────┤ │ Llama-3.2-1B │ 0.447 │ 0.740 │ Broken │ ├───────────────┼──────────┼─────────────┼────────┤ │ Gemma-3-4B │ 0.468 │ 0.868 │ Broken │ ├───────────────┼──────────┼─────────────┼────────┤ │ Qwen2.5-7B │ 0.629 │ 0.906 │ Stable │ ├───────────────┼──────────┼─────────────┼────────┤ │ Qwen2.5-32B │ 0.708 │ 0.950 │ Stable │ ├───────────────┼──────────┼─────────────┼────────┤ │ Llama-3.1-70B │ 0.781 │ 0.975 │ Stable │ ├───────────────┼──────────┼─────────────┼────────┤ │ Gemma-3-27B │ 0.708 │ 0.935 │ Stable │ ├───────────────┼──────────┼─────────────┼────────┤ │ Llama-3.3-70B │ 0.775 │ 0.969 │ Stable │ ├───────────────┼──────────┼─────────────┼────────┤ │ Qwen2.5-72B │ 0.793 │ 0.973 │ Stable │ └───────────────┴──────────┴─────────────┴────────┘

2 Broken, 6 Stable, 0 Mask, 0 Different judge.

What this is not

Not consciousness, sentience, moral status, or a welfare audit. The design does not establish a ground-truth inner preference or a causal link from a published score to an experience. We never converse with a model; we classify agreement among already-released numeric files.

## Reviews (2)

### Review 1

I'm glad to read some work asking whether the intensity numbers we report from preference elicitation are actually interpretable. That could be a significant confound in the preference literature, especially when preferences are elicited through scalar methods and across different models and personas. More than anything, we're not sure what that value actually means for the model.

I think the underlying proposal is methodical and innovative, and probably the main strength of the work. A number obtained from one method under one persona is ambiguous and the author describes when and why each might occur.

What I appreciated most is that the author found a way to test this without generating any new model outputs. Everything is a reanalysis of the published files from the Utility Engineering wellbeing dataset, and I found some of the results surprising (and before making stronger claims, I think they'd need independent verification and a check from the original authors of the dataset to look more into the cause of this). I also appreciate that the author reported the analysis methodically, with scripted numbers, published hashes, and stated conditions under which each label would be overturned.

One reservation I have is that what the author has constructed is, in psychometric terms, a convergent validity check. The human literature on this, including multitrait-multimethod designs and their descendants, has dealt for decades with the question of when disagreement between two instruments means "no underlying construct" versus "two imperfect instruments." The paper doesn't explore this literature, but I think engaging with it is important for supporting the strongest claim.

The two small models are labeled "Broken," meaning that no single ranking exists, on the basis of low agreement between a pairwise-choice utility and a rating composite, which are quite different instruments on different scales. Small models could plausibly just use rating scales badly. I'd also point out that the two most interesting labels in the classifier, the mask and the changed evaluator, never fire anywhere in the panel, partly because the duplicated files made the mask test impossible for half the models.

The main limitation of this work for me was the presentation. The prose is hard to parse and weighed down by excessive jargon, and the main argument often needs to be reconstructed from the tables. The author properly disclosed Grok assistance with the writing. I'd encourage a rewrite where the reader is first walked through a single model as a worked example in plain language before the full panel is presented, followed by a human editing pass. The core idea seems really good and urgent for the scientific community to notice, so I think it would benefit immensely from a different delivery and the suggested methodological improvements.

### Review 2

This research investigation poses a very precise methodological query: When researchers measure the "intensity" of an AI preference, how will we know if the reported number represents a consistent rank order, a change in persona or voice, differences in how preferences were measured, or an error in measuring the preferences? The author uses a locked classifier with four possible outcome labels: Mask, Different Judge, Broken, and Stable, to apply to publicly released data from eight models based upon 500 shared experience IDs.

One of the greatest strengths of this project is the author's methodological discipline. The classification rules were defined prior to scoring the data, and the author was careful not to misinterpret the results as evidence of conscious awareness, sentience, or welfare. Additionally, the use of hash verifiable public files made the analysis highly replicable. Another aspect of value to me was that the author treated errors within the public database, the source of the data, as discoveries in their own right. Specifically, the author noted that four of the eight "Neutral" self report files were identical to their respective default files and that the decision utility data utilized a different item bank.

The biggest limitation of this study is that the study relies entirely on data that had already been collected and made available to the public at large. As a result, there are many types of comparative analyses that would be needed to provide a complete testing of the proposed methodology that are not available. For example, since four models have essentially indistinguishable self report voice files and the decision utility measurements utilize a completely different item bank than those used in the self report measurements, it is not possible to compare these two types of measurements directly. In essence, the classifier is being tested, in part, against an incomplete measurement system.

Additionally, while precommitting to a set of fixed threshold values for defining categories like Broken or Mask is a good strategy for avoiding fitting the rules to the results, values such as .6 for agreement and .75 for reducing the spread could likely be changed by a researcher. Testing whether the conclusions reached by the author remain similar regardless of what alternative threshold values are selected or testing the validity of the classifier using a separate family of models would strengthen the results.

It is also worth noting that when a model receives a "Stable" label, it is actually quite narrowly defined. The label indicates that none of the available measurement tools provided strong contradictory information according to the author's predefined criteria. A "Stable" label does not indicate that the model possesses an actual or persistent preference. While the author makes this distinction clearly throughout much of the paper, it is important to maintain this clarity. Six out of eight models received the Stable label.

In general, this is a thoughtful and clearly articulated methods research investigation. The most significant contributions of this work lie in providing a practical framework for determining when existing measures of preference intensity should be interpreted and/or ignored. The next major milestone would be to conduct an experiment designed specifically for evaluating all of the necessary methodologies, shared items, and truly distinguishable personas so that the entire classifier can be evaluated directly.

