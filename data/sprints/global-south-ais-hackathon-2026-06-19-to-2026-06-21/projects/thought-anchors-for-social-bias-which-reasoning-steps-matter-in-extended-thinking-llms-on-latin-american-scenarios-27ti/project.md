# Thought Anchors for Social Bias: Which Reasoning Steps Matter in Extended Thinking LLMs on Latin American Scenarios

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: 1
- Awards: 1st Place - Latin America ($1,000)
- Team: None
- Authors: Andres Felipe Mosquera Hernandez
- Date / location: Jun 22, 2026 / Bogota, Colombia
- Page: https://apartresearch.com/sprints/projects/thought-anchors-for-social-bias-which-reasoning-steps-matter-in-extended-thinking-llms-on-latin-american-scenarios-27ti
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/2ddab8d52429eb88-16415f12-9dab-47a8-9e50-6f991ac225e3-main.pdf
- Code: https://github.com/andresmosqueraw/bias-thought-anchors.git
- Code links found in report: https://github.com/mvrobles/SESGO
- Recording: https://bias-thought-anchors-com.vercel.app/

## Summary

We investigate which reasoning steps in extended-thinking LLMs are associated with pro-stereotypical outputs on Latin American social bias scenarios. Social bias benchmarks, including BBQ \citep{parrish2022bbq}, SESGO \citep{robles2024sesgo}, and EsBBQ/CaBBQ \citep{ruizfernandez2025esbbq}, measure final-answer distributions but provide no visibility into intermediate reasoning. We adapt the thought-anchor resampling framework \citep{bogdan2025thoughtanchors} to social bias measurement: for each sentence-level chunk in a model's chain-of-thought, we remove it, resample $K{=}3$ continuations, and measure the change in pro-stereotypical output probability via three importance metrics. We apply this pipeline to SESGO-small, an 80-item stratified pilot subset spanning four Latin American bias categories (\textit{género, clasismo, racismo, xenofobia}), two languages, and three recent models with extended thinking. Across 1,708 chunk-level attributions, disambiguated contexts show higher pro-stereotypical output rates than ambiguous ones (33–75\% vs.\ 0\%), and high-importance reasoning positions tend to be tagged as \texttt{logical\_reasoning} or \texttt{context\_recall} rather than \texttt{stereotype\_activation}. These pilot results suggest that bias-relevant moments may lie in general inference steps rather than overt stereotype invocations, offering a step-level diagnostic target that complements answer-level benchmarks. More broadly, attributing bias to specific reasoning steps could help localize where stereotyping enters a model's reasoning, though our findings remain preliminary.

## Reviews (4)

### Review 1

Adapting thought-anchor resampling to social bias measurement in extended-thinking LLMs on Latin American scenarios opens a research direction that did not previously exist. The finding that high-importance steps are logical_reasoning and context_recall (not stereotype_activation) is counterintuitive and potentially significant. This suggests that bias enters reasoning disguised as general inference, which has direct implications for how mitigation interventions should be designed. To consolidate the work, the most urgent next steps are increasing K from 3 to at least 10 rollouts per chunk to obtain importance estimates with higher resolution, validating semantic chunk labels with human annotation, and applying the pipeline to the full SESGO benchmark for adequate statistical power per cell. The future work question of whether backtracking acts as a protective mechanism against stereotypical outputs is one of the most important questions the paper leaves open.

### Review 2

This is a strong and creative extension of Thought Anchors into social-bias evaluation.

The repo is very reviewer-friendly, with clear reproduction commands and cost disclosure.

Small note: the video is announced but I could not play it. I would have enjoyed seeing it, not many teams did one and it helps reviewers a lot.

### Review 3

Agentic harnesses have been seen to greatly improve capability, and therefore I think harnesses are a very important safety angle to study. So I like the problem choice. If I'm understanding the result correctly, I think it is quite interesting that bias is coming out in "reasoning steps" and not in "recall steps", so somehow it seems that even if bias is not recalled directly from model "memory" it could come out in agents in more subtle ways. I think this is a good angle to study.

I find it hard to study the correctness of methodology and validity of results under my time constraints, but I like the problem choice. Presentation could use less jargon to be followed at least at a high level under strict time constraints.

### Review 4

This is a very strong and focused contribution. The paper applies a resampling approach to understand where social bias appears inside the model’s reasoning, using the Latin American benchmark SESGO. This is a genuinely interesting angle, because it goes beyond simply looking at final answers. The pipeline is carefully built, and the main finding is interesting: the reasoning steps that shift bias are often classified as general reasoning or context recall, rather than direct stereotype activation. The biggest strength is the paper’s honesty about its limits. It is clear that the small SESGO exercise, with 80 items and limited validation, is a proof of concept rather than a basis for firm conclusions. To strengthen the paper, I would scale the analysis to the full SESGO benchmark, use more repeated runs, validate the labels with human coders, and report agreement across coders. Excellent writing and reproducibility. A very strong project.

