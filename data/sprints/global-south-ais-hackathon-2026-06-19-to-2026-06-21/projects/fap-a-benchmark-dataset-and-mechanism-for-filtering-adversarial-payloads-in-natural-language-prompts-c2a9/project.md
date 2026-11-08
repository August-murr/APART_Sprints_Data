# FAP: A Benchmark Dataset and Mechanism for Filtering Adversarial Payloads in Natural Language Prompts

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Team: Team Epoch
- Authors: Rabbika Azmi, Tanisha Ojha
- Date / location: Jun 22, 2026 / New Delhi
- Page: https://apartresearch.com/sprints/projects/fap-a-benchmark-dataset-and-mechanism-for-filtering-adversarial-payloads-in-natural-language-prompts-c2a9
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/0709029e7992d714-1ce6398c-8024-4863-87b4-ece3662ee801-SAFL-Submission_Team_EPOCH.pdf
- Code: None
- Code links found in report: https://github.com/ResearchDrafts/malicious-SQL-detector

## Summary

We address a critical security gap in Text-to-SQL systems serving code-switched (Hinglish) users, where English-optimized defenses fail to detect SQL injection payloads embedded in multilingual prompts. We introduce FAP, a framework combining fine-tuned UniXcoder (structural code analysis) with zero-shot Qwen3-4B (semantic intent verification) via MLP fusion. Our dataset comprises 20,000 code-switched samples spanning four linguistic tiers (English, Hinglish Light/Natural/Heavy) derived from Spider and SQLShield. FAP achieves 81.73% recall and 84.03% F1-score, versus CodeBERT-only's 8.67% recall, demonstrating that semantic reasoning is essential for multilingual security. The work exposes a critical AI safety gap: existing defenses remain English-centric, leaving non-English speakers vulnerable to undetected linguistic attacks. Our framework and dataset are released to enable community research on multilingual database security.

## Reviews (3)

### Review 1

This paper addresses an important and underexplored problem: securing code-switched (Hinglish/Hindi) Text-to-SQL systems against prompt injection and SQL attacks. The dual-encoder architecture combining structural and semantic analysis is well motivated, and the implementation is supported by a complete evaluation pipeline. The reported improvement in recall over baseline methods highlights the potential of the proposed approach.

The main limitation is that the benchmark is machine-generated and lacks native-speaker validation, while the key hypothesis—that security performance degrades as code-switching increases—has not yet been evaluated through the planned tier-wise analysis. Completing this analysis should be the highest priority. In addition, baseline comparisons should be performed on identical evaluation sets, and component-level metrics should be clearly distinguished from end-to-end benchmark results to avoid confusion.

Overall, this is a promising contribution to multilingual AI security with a solid technical foundation, and additional validation would significantly strengthen its impact.

### Review 2

The problem is strong and genuinely neglected: code-switched (Hinglish) SQL-injection against Text-to-SQL systems is a real, specific blind spot in English-centric defenses, and it's well-scoped. The architecture (fine-tuned UniXcoder for structure + zero-shot Qwen3-4B for intent, fused via MLP) is sensible and the structure-vs-semantics framing is a reasonable hypothesis. A few things I can't assess but would need to before trusting the headline:

The CodeBERT 8.67% recall comparison looks like a strawman. CodeBERT zero-shot or unmodified on a Hinglish distribution it never saw would naturally collapse; the fair comparison is CodeBERT (or UniXcoder) fine-tuned on the same 20k samples. As stated, the 8.67%-vs-81.73% gap may largely measure "trained on the target distribution vs not," not "structure-only vs structure+semantics." The ablation that actually supports the thesis is UniXcoder-alone vs Qwen-alone vs fused — does the report have it?

81.73% recall is the number that matters, and it's not high for a security filter. Missing ~18% of injection payloads is a lot for a defense; recall, not F1, is the operative metric for a filter, and the abstract leads with F1. How does precision/FPR look, and what's the threshold trade-off?

Dataset provenance. 20k samples "derived from Spider and SQLShield" across four Hinglish tiers — were the code-switched variants machine-generated or native-speaker-validated? If templated/auto-translated (as is common), the tiers may not reflect real Hinglish, and the model may be learning the generation artifact. This is the same authenticity question that mattered for MoMo.

No code verifiable here — and a benchmark+mechanism paper lives or dies on whether the dataset and harness are real and reproducible.

### Review 3

This project addresses an important and underexplored problem: security for multilingual and code-switched text-to-SQL systems. The focus on Hinglish prompts is valuable because many deployed AI systems are evaluated mostly in English, while real users often interact in mixed-language settings. The dataset contribution is the strongest part of the work, and the multi-perspective pipeline combining structural SQL features with semantic intent reasoning is a sensible direction.

The paper is also practically motivated: text-to-SQL systems can cause real harm if generated queries bypass authorization, modify data, or leak sensitive rows. Separating SQL generation from security classification is a good design choice, and the reported improvement in recall over the CodeBERT-only baseline suggests that semantic reasoning is important for this task.

The main weakness is evaluation clarity. Some reported metrics appear inconsistent: for example, FAP is described as maintaining a low false positive rate, but the confusion matrix indicates 68 false positives out of 1,400 benign samples, which is closer to 4.9%, not 0.36%. The false negative rate also appears inconsistent with the reported recall and confusion matrix. These numbers should be recalculated and presented consistently before submission. The comparison is also uneven because Qwen has fewer test samples than the other methods, and the “tier-wise performance” most relevant to the multilingual claim is still pending.

The dataset construction also needs more detail and validation. Since Hinglish variants are LLM-translated from Spider, the benchmark may reflect the translator model’s style rather than real code-switched user behavior. Human validation by Hinglish speakers, tier-wise examples, and checks for label quality would strengthen the benchmark substantially. It would also help to separate prompt-injection detection, SQL-injection detection, schema exploration, and authorization bypass into distinct categories rather than one broad malicious label.

Overall, this is a promising and socially relevant hackathon project with a useful dataset direction, but the empirical claims need cleanup, stronger multilingual validation, and more realistic security evaluation before the framework can be considered production-ready.

