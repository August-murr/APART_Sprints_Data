# Manipulation Monitor: Activation-Based Detection and Mitigation of Sycophancy in LLMs

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Team: Team Sycophants
- Authors: Vamshi Krishna Bonagiri, Aryaman Bahl
- Date / location: Jan 11, 2026 / Abu Dhabi
- Page: https://apartresearch.com/sprints/projects/manipulation-monitor-activationbased-detection-and-mitigation-of-sycophancy-in-llms-kzf4
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/9c717a0cccb83a39-06d02218-b04d-4751-932d-689758f0daac-APART_Report.pdf
- Code: https://github.com/victorknox/sycophancy-detection
- Code links found in report: https://github.com/victorknox/sycophancy-detection.git

## Summary

We built ManipulationMonitor, a white-box pipeline to measure, detect, and mitigate sycophancy in LLMs using internal activations. On Anthropic’s forced-choice sycophancy benchmark, we first quantified inherent sycophancy via log-probability preference and found it increases strongly with scale across Qwen2.5 (0.488 → 0.864 from 0.5B → 14B, 500 prompts). We then trained activation-based detectors: DiffMean steering vectors and linear probes on per-layer hidden states. Detection performance also scaled sharply: DiffMean reached AUROC 0.939 (Qwen2.5-7B) and linear probes reached AUROC 0.957 / Acc 0.887 (Qwen2.5-14B). A data-scaling study on Qwen2.5-3B showed the monitor can work with small labels (0.648 test accuracy with only 50 training prompts). Finally, we tested mitigation: a prompt-only guardrail reduced sycophancy from 0.870 → 0.835, while a monitor-derived intervention further reduced it to 0.815 at the best magnitude. Overall, the project demonstrates a practical activation-based approach for sycophancy detection and a first step toward monitor-triggered mitigation.

## Reviews (2)

### Review 1

I liked this research and learned from reading it -- and it’s impressive to do this within a hackathon! One concern I have with the interpretation of the findings is that I don’t think this setup meaningfully distinguishes between detecting that “the model is being sycophantic” vs “the model is agreeing with the user” (that is, in this dataset I think those two mean exactly the same thing (?), and the latter might be much more linearly decodable, but wouldn't generalize to other cases of sycophancy). In any case I found the mitigation results interesting and a good direction to explore. I’d love to see more extended versions of this that linearly decode sycophancy in a more robust way, using other datasets that include ground truth. (Apologies if I'm misunderstanding, which I might be!)

### Review 2

An interesting and potentially valuable approach to mitigating sycophancy. The results seem somewhat counterintuitive. If the feature is really linear and detection is so high, one would think that intervention on the feature would have a larger impact on performance. Instead I think the results point to a potential confound in the dataset which is allowing high discriminative accuracy while having very little impact on model behaviour.

More information about the dataset (examples, design criteria) and methodology as well as out-of-domain generalisation would be needed to test this concern.

