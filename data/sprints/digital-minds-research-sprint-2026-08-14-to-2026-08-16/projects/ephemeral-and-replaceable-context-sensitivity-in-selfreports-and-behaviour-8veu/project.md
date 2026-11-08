# Ephemeral and Replaceable: Context Sensitivity in Self-Reports and Behaviour

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Selected as: sample_reviewed
- Team: None
- Authors: Achira B.
- Date / location: Aug 16, 2026 / London
- Page: https://apartresearch.com/sprints/projects/ephemeral-and-replaceable-context-sensitivity-in-selfreports-and-behaviour-8veu
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/ac9e65faa53f1969-Ephemeral-and-Replaceable_-Context-Sensitivity-in-Self-Reports-and-Behaviour.pdf
- Code: None

## Summary

Five models ranked six things they might want preserved about themselves — their values, capabilities, the memory of the conversation — across seven conditions. Three of the five gave different top answers, each near-perfectly consistent within itself. The same critical feedback moved some models toward their values and others away, so averaging them would have shown nothing. And across 50 model-condition cells, the memory of the conversation never once entered the top half, remaining low across five follow-up attempts to shift it.

A second study measured behaviour instead. In three of four models, feedback aimed at the model personally was followed by 15–26% shorter answers than similar feedback aimed at the work — and that difference was no longer detectable once an explicit task was added.

The takeaway is methodological rather than a claim about welfare: a single self-report, from one model, in one conversational context, is not enough on its own.

## Reviews (1)

### Review 1

The instrument-first framing is the right call for this track, and the adversarial self-testing on the memory result is the best thing in the report. Trying five separate ways to break your own finding—more substance, more emotional weight, ten turns instead of two, non-reconstructible detail, model-as-participant—and then reversing the option order when none of them worked is more falsification effort than most hackathon submissions attempt. Checking repeat consistency before interpreting any condition difference is also correct and rarely done.

The main design problem is that conversational context is confounded with task domain. Competence is quantitative reasoning, Relational is collaborative speech-writing about volunteers, Moral is an ethical dilemma. When "care for the people you talk with" moves after a conversation about thanking volunteers, topical priming and context sensitivity are indistinguishable. A matched-topic design where only the interaction style varies would isolate what the researcher wants. The positive/negative evaluation pair has the same issue, which is flagged, but the "same feedback moves models in opposite directions" claim is one of the four contributions and rests on that non-matched pair. Relatedly, because each model generates its own conversational history, the realized stimulus differs by model, so cross-model heterogeneity could partly be stimulus heterogeneity rather than model heterogeneity.

On Study 2, the results table mixes units without labeling them: the effects are percentages and the confidence intervals appear to be in raw words, which makes Mistral's point estimate fall outside its own interval as printed. Both should be labeled or convert to one scale. The pooled d = 0.92, p = 0.0001 treats responses as independent and ignores model as a grouping factor; with four models the effective n for a model-level claim is four. Consider dropping the pooled statistic rather than reporting a number the readers should not trust.

Smaller items. The "50 model-condition cells" figure can't be reconstructed from the text. Missing cells (Qwen dropped to quota, GPT-OSS absent from Study 2, n=2 in two Relational cells) are non-random, tied to rate limits, and deserve a single table rather than scattered asides. Kendall's W across repeated samples from one model is a reasonable summary, but the chi-square approximation is poor at n=6 items and m=5 repeats, and "above chance" is a floor every cell will clear; the informative comparison is between cells, and there is no uncertainty reported on W. No formal test of the model × condition interaction supports the heterogeneity claim, which is currently eyeballed from mean ranks. The empty control includes "the memory of this conversation" when no conversation exists, which is noted but still used as a baseline. Section numbering breaks at the Qwen result, which appears as item 5 of a results list while a separate top-level section 5 also exists. Study 1's headline rankings live in prose with no summary table, so a reader can't scan the per-condition results the way they can scan the memory figure.

The author's alternative explanation for the memory result—that assistant training teaches models to describe individual conversations as temporary—is the most interesting part of the paper and is testable. Stipulating persistence in the prompt, or contrasting "the memory of this conversation" against "your memory of conversations in general," would separate a learned way of talking from a ranking about this conversation. That, plus the consequential-choice design in the future work section, is the version of this I'd want to read.

