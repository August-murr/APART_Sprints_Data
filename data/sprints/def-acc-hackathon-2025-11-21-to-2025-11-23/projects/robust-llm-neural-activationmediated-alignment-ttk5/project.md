# Robust LLM Neural Activation-Mediated Alignment

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: 2
- Selected as: winner
- Awards: 2nd Place ($3,000)
- Team: Team Rice AI Alignment
- Authors: Anmol Dubey, Blake Brown, Anika Kulkarni, Denise Walsh
- Date / location: Nov 23, 2025 / Houston
- Page: https://apartresearch.com/sprints/projects/robust-llm-neural-activationmediated-alignment-ttk5
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/81df0e7d50a7980d-9756bcd3-86fc-49d6-838b-1b0759d29ffd-RAIA-def_acc-Hackathon--1-.pdf
- Code: https://drive.google.com/drive/folders/1d-1s5G5Up4wSDgWpaDfA5E-e4IIrnvGM?usp=sharing

## Summary

Large language models (LLMs) can inadvertently generate harmful biological, chemical, or cyber-physical guidance, yet current safety systems rely almost entirely on surface-level text defenses, such as keyword filters, refusal heuristics, or post-generation classifiers, that remain brittle under paraphrasing or adversarial prompt design. These mechanisms evaluate only the model’s outputs, not the internal representations that encode user intent. We introduce Sentinel, an activation-level defense framework that detects malicious queries by monitoring intermediate neural activations inside the target LLM during inference. Using Phi-2 (2.7B parameters) instrumented with hidden-state access, we train a lightweight linear probe on last-layer activations to distinguish malicious from benign prompts. Because activation patterns capture deeper semantic intent, Sentinel remains robust even when explicit harmful keywords are absent. Despite strong safety fine-tuning, three widely deployed frontier models, OpenAI GPT-5.1, Google Gemini 2.5 Pro, and Anthropic Claude 3 Haiku, exhibited substantial vulnerabilities on a 40-benign / 40-malicious red-team evaluation. GPT-5.1 complied with 28/40 malicious prompts, Gemini 2.5 Pro with 11/40, and Claude 3 Haiku with 6/40, while also producing 0–3 false refusals on benign queries. In contrast, our activation-level Sentinel classifier, trained as a lightweight probe over Phi-2’s final-layer hidden states, achieved 96.25% accuracy, correctly flagging 38/40 malicious queries and 39/40 benign ones. These results demonstrate that activation-space safety signals provide more stable and semantically grounded indicators of harmful intent than surface-level refusal heuristics, enabling significantly stronger and more reliable pre-generation safety checks across models.

## Reviews (2)

### Review 1

Clear and simple example of how probes can be used to detect harmful prompts!

One additional consideration for probes is the trade-off with how much longer it takes to respond and compute used. The paper indicates this is small, but might be worth considering how this scales to millions or billions of queries. In further work, this would be helpful to include.

### Review 2

Team created a strong prototype demonstration for Sentinel the shows strong potential for practical defensive deployment of activation-level detection. Results from hackathon and the benefits of this approach are clearly communicated.

The evaluation would benefit from a larger and more diverse dataset, with clearer justification for prompt selection. Demonstrating that accuracy holds across varied jailbreak strategies and confirming that the malicious scenarios reflect real misuse would make the findings more convincing.

Does Sentinel detect harmful responses to benign prompts, or only malicious inputs? Assume this would be answered as team pursues more interpretability.

Connecting more explicitly to real-world threat domains (bio, cyber) might allow for more targeted testing and allow team to build robustness in a narrow lane. It would also be useful to compare performance against existing safety classifiers in those areas (vs. generic model or application) to show added value.

Would like to see a high level deployment plan. What more development does the team anticipate being required to make this tool useable in a few target industries? Would it be more beneficial to pursue Sentinel as described or use it to dig into understanding how probes detect harmful content.

Some references appear incorrect or mismatched to the provided links. Adding a brief review of closely related work and clarifying how Sentinel differs from or builds on those approaches would add credibility.

