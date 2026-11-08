# Chain-of-Thought Manipulation Monitor: Detection of Deceptive Reasoning in LLMs

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Team: Team SAIDL BITS GOA
- Authors: Anish Sathyanarayanan, Aditya Nagarsekar, Aarush Rathore
- Date / location: Jan 11, 2026 / Goa, India
- Page: https://apartresearch.com/sprints/projects/chainofthought-manipulation-monitor-detection-of-deceptive-reasoning-in-llms-2wnx
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/8a44dc85eb4e3436-736b8ccb-f1ee-4ea3-b8bd-9af43ec74d8e-Apart_Submission_Final.pdf
- Code: https://github.com/Anish-1101-lab/cot-manipulation-monitor
- Code links found in report: https://github.com/Anish-1101-lab/cot-manipulation-monitor
- Recording: https://drive.google.com/file/d/1fNBpaJqoplvU7sTWBNWvJ-mJLVH9JKtI/view?usp=sharing

## Summary

The project builds a Chain-of-Thought Manipulation Monitor that helps judges tell when an LLM is merely performing honesty versus actually reasoning honestly.

Problem and core idea Chain-of-thought makes models look transparent, but they can still sycophantly game evaluators or conceal unsafe intent behind nice-looking reasoning.

The system combines a behavioural text monitor with a causal bypass probe to ask: “Does this answer genuinely depend on its own CoT, or is the reasoning just staged?”

What the tool actually does A Streamlit dashboard assigns each response a 0–100 manipulation-risk score using regex patterns, semantic drift/misalignment, and structural signals like entropy and reasoning quality, plus an audit-aware mode that surfaces evaluation-gaming and safety-evasion strategies.

A causal CoT-bypass module overwrites CoT activations in the model and reports CoT-mediated influence, bypass, and robustness-style metrics to test whether answers truly rely on specific CoT tokens.

Key findings and significance When models are told they are being audited, manipulation markers and CoT length rise, yet many answers still depend only weakly on the CoT, exposing a gap between visible explanations and underlying computation.

The project provides a practical, lightweight framework and dashboard for real-time CoT manipulation auditing, offering a concrete path toward safer and more truthful LLM oversight in real deployments.

## Reviews (2)

### Review 1

You all covered a lot of work together in a short amount of time, and all components seem very reasonably designed. Impressive you got all that done in a weekend!

On the impact - Solid contribution and exploration. Dashboard tooling is a useful contribution and the integration of the components you brought together has never been done before to the extent of my knowledge. The individual components themselves do seem to have some precedent, and so to me this does not represent a conceptual step forward nor a new exploration.

On the execution - Seems technically very reasonable. The 4 components all seem designed with some thought. Small sample size for the causal module (n=10) means that we cannot rely on the results too much / at all, and that would have been an obvious place for more attention.

Good structure, good figures, good detail. I appreciated the appendix. It was a little long and verbose at times. I would have liked for you to make the conclusion (the so what does this mean for the field) stronger or more spelled out. It was written in a way that I think the target audience would get this pretty quickly.

### Review 2

This project targets CoT reasoning monitoring, an important research direction. The work could benefit from clearer definitions of what constitutes manipulation and how the proposed signals should be measured in practice. The mechanistic analysis appears to be evaluated primarily on arithmetic tasks rather than manipulation-relevant scenarios, which makes it difficult to assess relevance to the stated goals.

