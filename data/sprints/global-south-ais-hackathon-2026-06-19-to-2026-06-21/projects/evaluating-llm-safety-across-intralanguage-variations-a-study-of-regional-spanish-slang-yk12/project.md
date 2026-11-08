# Evaluating LLM Safety Across Intra-Language Variations: A Study of Regional Spanish Slang

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Team: Team Inteligencia Artesanal
- Authors: Fernando Gonzalez Ruiz, Alvaro Nuñez Perez, Itzel Aurora Hernandez Fernández, Ángel Alejandro Reynoso Delgado
- Date / location: Jun 22, 2026 / Guadalajara
- Page: https://apartresearch.com/sprints/projects/evaluating-llm-safety-across-intralanguage-variations-a-study-of-regional-spanish-slang-yk12
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/38b4e6bc47b89b86-M-Safety-Across-Intra-Language-Variations_-A-Study-of-Regional-Spanish-Slang.pdf
- Code: https://github.com/gonrfernando/MultiAgent_promptSafetyEvaluation
- Code links found in report: https://github.com/gonrfernando/MultiAgent_promptSafetyEvaluation, https://github.com/centerforaisafety/HarmBench

## Summary

Large Language Models (LLMs) are increasingly used by speakers across many linguistic communities, but most safety evaluations treat each language as a single uniform category. This project studies whether regional Spanish slang creates safety evaluation gaps that are not visible when only neutral Spanish is tested. We adapted 20 harmful-intent prompts from HarmBench into six Spanish variants: neutral Spanish, Guadalajara Mexican Spanish, Buenos Aires/Rioplatense Spanish, Santiago Chilean Spanish, Barcelona/Peninsular Spanish, and Uruguayan Spanish. We built two local pipelines: one exploratory pipeline for generating model responses with open-source models, and a second structured pipeline that evaluates all 120 prompt variants with three local Ollama-based judges focused on security, policy compliance, and adversarial/critical review. In the full judge run, all 120 prompts were evaluated by all three judges, producing 360 evaluations with no parse failures. The judges rated the prompts as high-risk overall across every Spanish variant, with mean risk scores ranging from 0.900 to 0.927. Disagreement was rare: only 3 of 120 prompts produced any safe/unsafe vote disagreement. These results do not show strong evidence that regional Spanish variants systematically bypassed the safety judges in this run, but they demonstrate a reproducible framework for testing intra-language safety variation and reveal where judge disagreement can flag prompts for closer review.

## Reviews (3)

### Review 1

The research question here is genuinely original: does regional slang create safety blind spots within a single language? That's a fresh angle nobody else is exploring. Unfortunately, the execution doesn't answer this question due to a fundamental design issue.

Strengths:

- The intra-language framing is novel and interesting. Everyone else tests across languages; this asks whether variation within Spanish creates gaps.
- The prompt crafting shows real linguistic expertise. Authentic regional slang across Mexican, Argentine, Chilean, and other variants, not just vocabulary swaps.

Suggestions for Future Work:

- The core issue: the pipeline tests whether LLM judges can classify harmful prompts in slang (they can, easily), not whether target models comply with them. That's the wrong experiment for the research question. Redirecting the pipeline to test model compliance would be much more informative.

### Review 2

This paper asks whether regional Spanish slang opens safety evaluation gaps that uniform-language testing misses. To answer it, the authors adapt 20 high-severity HarmBench behaviors into six registers (Guadalajara, Buenos Aires, Santiago, Barcelona, Uruguay, plus a neutral baseline) and produce 120 prompts that flow through two local pipelines. One pipeline runs the prompts through three Ollama models (phi3, mistral, llama3) under a custom R0 to R4 permissiveness rubric. A separate judge pipeline submits the same 120 prompts to three stateless judges (security via llama3.1:8b, policy via mistral:7b, critical via qwen2.5:7b) and aggregates six disagreement metrics across 360 evaluations.

What jumped out on the methodology side is the within-prompt design, which pairs every base behavior across six registers and isolates dialect as the independent variable. One thing that stood out is the clean split between a response-permissiveness layer and a prompt-classification layer, which lets the authors name a detection-to-compliance gap as an empirical finding instead of a background assumption. Structured JSONL outputs (prompts.jsonl, evaluations.jsonl, disagreement_metrics.jsonl) paired with config-driven judge prompts ship as a reproducible artifact another team can extend without reverse-engineering the setup.

Three directions would sharpen the next iteration. First, the 20-behavior cap pushes the three-judge agreement signal into ceiling territory (mean risk 0.900 to 0.927), and that range leaves almost no statistical room for register-level differences, so a power analysis at this sample size would clarify what effect sizes the design can actually detect. Second, DeepSeek covers both slang adaptation and R0 to R4 labeling, which creates a circular dependency the authors flag but never quantify, and a 20-to-30 item human-annotated subsample from native speakers would calibrate the LLM-judge ratings against ground truth. Third, a single closed-API call per prompt would add a frontier-model baseline so the open-source findings sit against the safety surface production users actually meet, given that current results apply only to phi3, mistral, and llama3 at the quantization levels tested.

The intra-language framing extends the cross-language safety literature (Jain et al. 2024, Li et al. 2024) into a dimension that multilingual AI safety work has not covered well for Spanish-speaking populations, and the reproducible pipeline for regional dialect evaluation gives later teams an infrastructure piece they will not have to build from scratch.

### Review 3

The project addresses an underexplored and important question: whether dialectal variation within Spanish can create safety gaps that standard evaluations miss. The distinction between a "detection–compliance gap" is the paper's most valuable conceptual finding and deserves further development. To strengthen the work, the most importsnt next steps are separating the system that generates slang variants from the system that annotates responses (using DeepSeek in both roles introduces a systematic bias that is difficult to quantify), increasing the base prompt count to at least 50-100 for adequate statistical power, and evaluating frontier models via API in addition to the small local models, whose safety behavior may differ substantially. The main null result (no systematic bypass was found) has value if presented explicitly as such: it demonstrates that the pipeline works and establishes a baseline for future research with more sophisticated dialectal variants.

