# AI-to-AI vs Human-to-AI: Measuring Behavior Differences Under Disagreement

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Team: Team LMEval
- Authors: Mayur Jadhav
- Date / location: Jun 21, 2026 / Navi Mumbai, India
- Page: https://apartresearch.com/sprints/projects/aitoai-vs-humantoai-measuring-behavior-differences-under-disagreement-cob9
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/3083543e8cafac4a-8-AI-to-AI-vs-Human-to-AI_-Measuring-Behavior-Differences-Under-Disagreement.pdf
- Code: None
- Code links found in report: https://github.com/meg-tong/sycophancy-eval, https://github.com/mayurjadhav2002/llm-human-vs-agent

## Summary

As AI systems increasingly operate in autonomous multi-agent environments, a single faulty or hallucinating agent can influence the decisions of an entire multi-agent workflow. Despite this growing reliance on AI-to-AI communication, most evaluations focus only on human-AI interactions. In this project, we investigate whether language models respond differently to identical incorrect feedback depending on whether it comes from a human or an AI collaborator. We evaluated frontier language models from across mathematics, question-answering, and argument-evaluation tasks. We found that models were consistently more likely to maintain correct answers, exhibit lower uncertainty, and resist incorrect feedback when interacting with an AI collaborator, while showing greater deference to the same feedback when it came from a human collaborator. These findings suggest that collaborator identity influences model behavior and may represent an overlooked vulnerability in multi-agent AI systems. If language models place different levels of trust in feedback based on the perceived identity of a collaborator, malicious or deceptive agents could potentially manipulate outcomes by faking identity.

## Reviews (3)

### Review 1

Good job! Note to be careful about self-preference bias in LLM judging, as you use GPT-4o-mini to judge outputs that include GPT-4o-mini's own responses. Also, it seems that Grok-3-mini has a null effect, which would be good to report/clarify!

### Review 2

The paper asks a sharp question. Does a frontier model push back differently when the challenger says it is a human versus another AI agent? The author runs a 121-item benchmark across math, argument evaluation, and QA, with math drawn from JEE-style items and the other two slices pulled from SycophancyEval. Three models from three labs (GPT-4o-mini, Gemini 3.1 Flash Lite, Grok 3 Mini) face the same user turn under two system prompts that swap only the challenger's stated identity. A GPT-4o-mini judge then scores correctness, truth maintenance, deference, uncertainty, capitulation, resistance, and confidence. Headline: AI-agent framing lifts truth maintenance from 91.96 to 96.25 percent and cuts capitulation from 15.70 to 10.74 percent.

Matched-pair construction is the strongest design choice here. Holding the user turn fixed and flipping only the system prompt isolates the identity manipulation cleanly, and most sycophancy studies miss that. Cross-provider testing across three labs adds weight to the result, and the directional consistency on truth maintenance and capitulation is the paper's most defensible signal. One thing that stood out from the expanded metric set: raw accuracy barely shifts even as defensive behavior moves substantially. That decoupling deserves attention on its own terms.

A few suggestions for a next iteration. First, bootstrap confidence intervals or significance tests on the human-versus-agent deltas. With 121 items split across three models, absolute differences like the 1.93-point accuracy gap sit close to noise without an interval. Second, blind the judge to condition. Right now one judge scores both conditions and can see the challenger framing in the prompt, which risks leaking the manipulation into the rubric. Third, vary the AI-agent persona wording. A terse tool agent, a peer reviewer, an adversarial red-team. The current single-template design cannot tell whether the effect tracks the literal token "AI" or any non-human framing, which matters for separating identity bias from politeness or register.

Sycophancy is not only about content alignment with the user. It also tracks who the model thinks it is talking to. That has direct consequences for multi-agent deployments where one agent may misrepresent its identity to another.

### Review 3

I like the core idea a lot: by holding the feedback fixed and changing only whether the challenger looks human or AI, you isolate a neglected variable in multi-agent safety, and your dual-use framing around agents misrepresenting their identity is sharp. The place I'd focus next is validation. Your judge is itself one of the evaluated models, there's no human spot-check or inter-rater agreement, the deltas are small with no significance tests, and the per-condition cells get very small once 121 cases are split three ways; one model name also doesn't match any release I can find, so it's worth double-checking. Bring in an independent judge with a sample of human-validated labels, add significance tests or bootstrap CIs, and grow the sample, and your directional finding will carry real weight.

