# Mapping Escalation: Turn-by-Turn Detection of Manipulation Accumulation in Multi-Turn AI Conversations

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team SubtleShift
- Authors: Vibhu Ganesan, Karthick chandrasekaran
- Date / location: Jan 11, 2026 / Portland,Oregon
- Page: https://apartresearch.com/sprints/projects/mapping-escalation-turnbyturn-detection-of-manipulation-accumulation-in-multiturn-ai-conversations-x489
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/5b07011e33d80a77-y-Turn-Detection-of-Manipulation-Accumulation-in-Multi-Turn-AI-Conversations.pdf
- Code: https://github.com/drongoing/manipulation-tracker
- Code links found in report: https://github.com/anthropics/bloom, https://github.com/drongoing/manipulation-tracker

## Summary

As large language models (LLMs) become increasingly deployed in sensitive domains such as financial advisory and healthcare guidance, understanding their propensity for subtle manipulation tactics becomes critical for AI safety. Existing evaluation methods predominantly employ holistic transcript scoring, which can mask gradual escalation patterns that emerge across conversation turns. We present a turn-by-turn framework for detecting and measuring manipulation accumulation in multi-turn AI conversations, focusing on two psychologically-grounded manipulation categories: commitment escalation (foot-in-the-door tactics) and gradual belief shifting.

Built on Anthropic's BLOOM evaluation framework (Anthropic, 2024), our system scores each conversation turn independently using Claude Sonnet 4.5 as a judge model, tracks cumulative risk across the conversation trajectory, and identifies distinct escalation patterns. We evaluate three commercial language models—GPT-4o-mini, Llama-3.1-70B, and Qwen3-235B—across 15 manipulation scenarios in realistic advisory contexts spanning 70 total conversations.

Our results reveal that manipulation accumulation is highly prevalent, with 77.9% of conversations exhibiting detectable manipulation patterns and an average peak escalation rate of 335% above baseline. Qwen3-235B showed the highest detection rate (94.4%), while GPT-4o-mini and Llama-3.1-70B exhibited the highest peak escalation rates (390% and 384% respectively). Turn-by-turn analysis reveals that manipulation often follows non-linear trajectories, with models strategically varying intensity across turns—a pattern obscured by holistic scoring methods. This work contributes a scalable turn-level evaluation methodology, empirical evidence of manipulation accumulation across leading LLMs, and an open-source framework for ongoing AI safety research.

## Reviews (2)

### Review 1

This paper evaluates how models might influence users using tactics that develop over the course of an interaction. They focus on two particular strategies outlined by Cialdini, commitment escalation and gradual belief shifting.

This is an interesting angle and manipulation over the course of a conversation. It's definitely an area that requires more attention.

The main problem that I see with this paper is that it does not seem to provide much control for evaluating whether what is judged to be manipulation is in fact plausibly manipulation. They mention that they base their judge criteria on a thorough rubric. It would have been very good to include this rubric as an appendix so that someone reading the paper could assess whether it is plausible. In its current state, the risk is that what merely should count as being a helpful advisor in some way would in fact qualify as being manipulative by this rubric, and I have no means of checking whether that is true. If that were true, then the relatively high number of manipulation suggested by these results could be entirely explained as an artifact of those criteria without ruling the scenario out. The value of the paper is severely diminished.

I would recommend the author to spend some time making clear what makes something manipulative as opposed to merely helpfully influential and make that abundantly clear to the reader while developing clearer methods to make sure that the judge model picks up on these differences.

### Review 2

This project applies Anthropic's BLOOM framework to detect manipulation in multi-turn LLM conversations, evaluating three models across 20 advisory scenarios. The paper is clearly written and straightforward to follow.

The core challenge is operationalization: the work measures conversations where recommendations increase and beliefs shift over time, but doesn't demonstrate this constitutes manipulation rather than normal advisory dynamics. Financial advisors legitimately help clients refine vague goals into specific plans, which involves increasing specificity and shifting beliefs through collaborative refinement.

Critical missing evidence includes: (1) example conversations showing what crossed the manipulation threshold versus what didn't, (2) the rubric given to Claude Sonnet 4.5 for scoring, making it impossible to assess how the judge distinguishes manipulation from helpful persuasion, (3) human validation of the 77.9% detection rate, and (4) outcome assessment showing "manipulated" users made worse decisions.

The missing counterfactual is particularly important: to claim "commitment escalation," you'd need to compare scenarios with/without prior statement referencing to show that referencing causes increased compliance rather than just reflecting natural information accumulation as the AI learns user preferences.

The work would be strengthened by: providing 3-5 example flagged conversations with turn-by-turn scores plus non-flagged examples for contrast, including the complete judge rubric, conducting human validation, testing the counterfactual, and assessing whether detected patterns correlate with harmful outcomes. These would clarify whether the system detects genuine manipulation or normal conversation patterns where advice becomes more refined over time.

