# Is "Confidence" the Right Word for Answer Repeat Probability?

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Team: Team bluetree
- Authors: Koshiro Aoki
- Date / location: Aug 17, 2026 / Tokyo, Japan
- Page: https://apartresearch.com/sprints/projects/is-confidence-the-right-word-for-answer-repeat-probability-ot69
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/985254ba122add0b-5fbf241f-f304-4586-9d21-9824b5ccb84d-main.pdf
- Code: https://github.com/AokiKoshiro/machine-confidence

## Summary

Natural-language confidence reports depend on how they are elicited. We therefore test whether a single learned word can reliably report a frozen model’s answer repeat probability. For each multiple-choice question, the target is the probability that the model repeats its most likely valid answer. We learn one input embedding in Llama-3.1-8B and map the model’s 0–10 report to this target. Under a carrier shift, eight initializations yield Spearman correlations from 0.359 to 0.586. The reporter selected on the development set does not significantly outperform fixed confidence or consistency. A parameter-matched generic soft vector has lower mean squared error on both carriers, and readable replacements do not preserve the learned behavior. A learned vector can therefore adapt a particular reporting context, but these results do not establish a stable word-level interface or privileged introspection.

## Reviews (2)

### Review 1

This work is motivated by an intriguing idea - that neologisms may allow us to more directly map between human intentions and the mental language of LLMs - which could have implications for model understanding and thereby AI safety to the extent it generalizes. It probes the special case of a model's ability to report the probability that it will repeat the same answer to a multiple choice question when asked again, and attempts to train a neologism for that. My assessment of the informativeness of the null result they report is constrained by my doubts about whether that is a viable target (it's not clear to me that the model would have that concept). However, the work is technically sound, uses appropriate baselines and controls, and overall offers a valuable methodological contribution. It could benefit from a larger set of carriers, diversity of training data, and attention to clarity of writing.

### Review 2

- The abstract is very difficult to follow. Terms such as "answer repeat probability", "carrier shift", "eight initializations", and "parameter-matched generic soft vector" are introduced before the reader has an intuitive understanding of the experiment. I think the paper would benefit enormously from first explaining the basic idea in ordinary language.
- The introduction could do more to explain why this question is important, particularly in the context of digital minds. The target studied here, answer repeat probability, can already be calculated directly from the model's logits. I can see the value of using this as a controlled test case for whether one can construct a stable learned lexical interface to a model property, but the paper could make much clearer why success on this task would ultimately matter for questions about introspection, welfare, or digital minds more generally.
- It would have been very helpful to give one complete worked example of the experimental procedure. For example: show an actual multiple-choice question, the model's answer probabilities, the resulting answer-repeat target, the full reporting prompt containing the learned embedding, and the numerical report produced by the model. I found it a bit difficult to reconstruct the experiment from the current methods section.
- But the result itself is nice: a learned embedding can adapt the model’s reports to the target in the training context. Unfortunately, this does not generalise. Which is fine!

