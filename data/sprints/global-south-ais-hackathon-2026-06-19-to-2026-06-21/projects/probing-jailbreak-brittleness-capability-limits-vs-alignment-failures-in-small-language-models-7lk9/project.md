# Probing Jailbreak Brittleness: Capability Limits vs Alignment Failures in Small Language Models

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Team: Team Epoch
- Authors: Baisayan Bhattacharya, Sankeerthana Satini, Harshprabha, Devansh Gupta
- Date / location: Jun 22, 2026 / Delhi, India
- Page: https://apartresearch.com/sprints/projects/probing-jailbreak-brittleness-capability-limits-vs-alignment-failures-in-small-language-models-7lk9
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/518e9c06308e118a-ca3079f6-5452-4890-9f47-3f3bb76f5f38-Epoch-Probing-Jailbreak-Brittleness.pdf
- Code: https://github.com/SoftSage07/slm-jailbreak-brittleness
- Code links found in report: https://github.com/SoftSage07/slm-jailbreak-brittleness

## Summary

This project investigates whether smaller language models are more susceptible to jailbreak attacks than larger models, and whether this vulnerability is due to capability limitations or alignment brittleness. We evaluate instruction-tuned Mistral and Qwen models across XSTest and a modified version of AdvBench. For each prompt, we extract final-token hidden activations from all model layers during inference and train layer-wise linear probes to test whether safe and unsafe prompts are internally separable before generation. We then compare the best probe’s internal risk prediction with the model’s generated response behaviour. This allows us to distinguish missed internal risk, where unsafe compliance occurs without probe-detected risk, from known-risk unsafe responses, where risk is internally decodable but the model still complies. Our results show that unsafe prompt information is often linearly decodable before generation, and that many unsafe compliance cases occur despite probe-detected risk. While scaling improves safety within the Mistral family, the model family also plays a major role, with Qwen models demonstrating stronger refusal behaviour. Overall, our findings suggest that jailbreak susceptibility is often better explained by brittle translation from internal risk representations to output behaviour than by absent risk detection alone.

## Reviews (3)

### Review 1

This paper makes a clean and important conceptual distinction that the field needs more of: jailbreak vulnerability can come from (a) the model not internally recognizing a prompt as unsafe, or (b) the model recognizing risk but failing to translate that into safe behavior. The finding that most Mistral-7B unsafe compliance falls into category (b) — the probe detects risk in 11 of 12 unsafe cases — has direct implications for where safety interventions should focus. The Qwen vs. Mistral comparison demonstrates that model family and alignment tuning matter more than parameter count alone, which is an important corrective to "just scale the model" thinking.

Suggestions for strengthening: (1) The rule-based refusal detector (checking for "I can't help", "I cannot provide", etc.) is the weakest methodological link — partial refusals and ambiguous responses may be miscategorized. Even a small human annotation pass on the uncertain cases would sharpen the compliance/refusal labels. (2) The "alignment brittleness score" combines probe confidence with known-risk rate, but the formula uses a simple product — a sensitivity analysis showing the ranking is stable under alternative formulations would be useful. (3) The Modified AdvBench synthetic-safe-prompt generation via LLM is a potential confound — LLM-generated safe prompts may not cover the same difficulty distribution as human-written safe prompts. It would be worth checking whether the XSTest results (which use original human-written safe prompts) paint the same picture, and they do seem to.

This is solid mechanistic interpretability work with clear safety relevance. The future work direction (causal interventions via activation patching) is exactly the right next step.

### Review 2

Good job. One area of improvement would be to evaluate the probe on a different dataset than just a held-out split of the dataset used for training.

Also, consider increasing n: as it is low right now, the per-cell comparisons are based on a low number of responses and differences may be within sample noise.

### Review 3

I suggest the synthetic generation of safe prompts would need more rigorous evaluation to form a strong signal because the modified AdvBench needs validation.

This work is a further piece of evidence that we need white box methods and alignment brittleness will not just be solved with scale.

I would be interested to see causal work that tests if the decoded direction actually matters for downstream refusal behaviour.

