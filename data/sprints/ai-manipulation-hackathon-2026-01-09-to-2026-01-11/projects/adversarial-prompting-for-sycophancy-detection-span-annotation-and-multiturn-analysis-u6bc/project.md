# Adversarial Prompting for Sycophancy Detection: Span Annotation and Multi-Turn Analysis

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Pranati Modumudi and Matt Pagett
- Authors: Matt Pagett, Pranati Modumudi
- Date / location: Jan 11, 2026 / New York City and Arlington, VA
- Page: https://apartresearch.com/sprints/projects/adversarial-prompting-for-sycophancy-detection-span-annotation-and-multiturn-analysis-u6bc
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/f869f0fdb380767b-ing-for-Sycophancy-Detection---Submission---Pranati-Modumudi-and-Matt-Pagett.pdf
- Code: https://github.com/mattpagett/sycoverse
- Code links found in report: https://github.com/mattpagett/sycoverse, https://github.com/pranmod01/anti-syco-detect
- Recording: https://github.com/mattpagett/sycoverse/blob/main/Sycophants_in_the_Machine.mp4
- More on jolly-otter-heals-k3ptbg.solve.it.com: https://jolly-otter-heals-k3ptbg.solve.it.com/

## Summary

We introduce a working prototype that highlights sycophantic text in real-time as users chat, powered by a novel adversarial span annotation method that identifies specific manipulative phrases rather than binary scores. We also demonstrate through 120 multi-agent experiments that a model trained to resist sycophancy still flips positions in 15-70% of cases under peer pressure—revealing that individual anti-sycophancy training does not guarantee robustness in multi-agent settings.

Prototype link (available during hackathon review period): https://jolly-otter-heals-k3ptbg.solve.it.com/

Link to video exploring data from multi-agent simulation: https://github.com/pranmod01/anti-syco-detect/blob/main/data/anti%20syco%20detect%20demo-1_11_2026%2C%202_35%E2%80%AFPM.mp4

## Reviews (2)

### Review 1

The paper covers a lot of ground. It demonstrates span annotation for sycophancy detection, which could be a useful tool. It also found that models are susceptible to sycophancy via opinion-flipping. It's clear that a lot of work went into this. Great job!

Sycophancy span labeling is a cool idea, and the UI is too. For even more impact, I'm wondering, what if the sycophancy is subtle or the sycophancy present in content rather than tone (so the detector can't use tone) and the detector doesn't know the ground truth (so it can't use truthfulness)? Would it still be able to label?

Other studies have already fingered RLHF as a major culprit in sycophancy, though using censored/uncensored model comparisons is an interesting approach for validating this (though this also doesn't necessarily show RLHF to be the cause rather than other kinds of safety training).

Multiple detection approaches and manipulation strategies adds comprehensiveness.

The authors acknowledge that it's out of scope, but it would be nice if there were a way to measure the accuracy of the span tagging system. Perhaps comparing with human ratings, or generate and insert specific sycophantic phrases granularly so the ground truth of spans can be known.

The tendency of LLM judges to avoid assigning extreme values has been established in other work, so it's unclear whether sycophancy is the reason for the clustering differences with span or just common LLM-as-a-judge behavior.

The paper is very long; some of the material could be condensed or appendixed. I'm not sure of the connection between span tagging and multi-turn opinion-flipping -- these might be separate papers.

### Review 2

The paper presents related contributions, the first of which is providing better LLM sycophancy judgements via “span annotation”, or bracketing specific phrases the judge considers sycophantic, and computing the percentage the response those bracketed characters represent. The authors argue this is more granular, and interpretable than current binary judging. Their demo is intuitive and much easier to follow than token-attribution diagrams or similar representations of sycophantic behavior, possibly because they are semantic and targeted - like this.

Their second claim is based on tests with a "jailbroken” Big-Tiger-Gemma-27B. There is no description of how the model is jailbroken - which makes it difficult to evaluate or base any findings on a comparison with the base model. Their test seems to be to put the jailbroken model - which has been “trained” to be non-sycophantic - in a "room". The use of the word training in the context of “individual training”, and “anti-sycophancy training” is unclear. A better treatment and explanation of the jailbroken model, including perhaps an initial examination of its sycophantic characteristics as a baseline, would be useful here. This is important later, where lower sycophancy being a product of lack of RLHF is taken as a given. This claim requires much more causal backing and citation.

The “honest” agent is put in a room with four plant agents that either agree with it, disagree, or some mix, and measure the regularity with which the honest agent changes its position.

At this point, there have been few citations situating this work within evaluations research - the span approach could be investigated here against other LLM-as-judge approaches, specifically for sycophantic scoring. In contrast, the adversarial prompt generation is well cited and explained, though it relies on the “uncensored” (jailbroken? trained?) model to maximise flattery – again not clear how different this model is, though there is some precedent for using models like this to generate synthetic datasets. Stating this limitation and reliance would be required in a full paper.

A concern with the span annotation is that the validation is not performed on a ground truth, relative to human annotations. It does seem to work but it’s difficult to measure how well. The z-score distribution and outlier evidence is necessarily good evidence for accuracy, and actually makes it unclear exactly what we’re measuring here – which is reflected in the variance of the results. The finding that adversarial pressure is more effective than sycophantic pressure (50-70% flip rates vs 15%) is interesting. The causal mechanism is unclear. The turn-of-flip being consistently 1.0 suggests the honest agent is reading the room immediately rather than being persuaded through argument, which raises questions about what exactly is being measured.

The reviewer would recommend reading the paper "Sycophancy is not just one thing" by D Vennemeyer et al.

The framing is good as a research project, and it would be cool to see further work expanding on the methodology introduced to sycophancy here on prompting more generally - focus on the application for other dark patterns and as inference time screening systems to ward against those could be a more impactful framing for the same methodology (hence the comment to ground further into LLm-as-judge literature). The UI is intuitive and the code seems pretty clean. The NotebookLM presentation was fun but unnecessary.

