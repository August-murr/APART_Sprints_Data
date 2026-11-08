# Deception Scales: How Strategic Manipulation Emerges in Complex LLM Negotiations

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Team: Team The Gamers
- Authors: Luis Fernando Yupanqui Taco, Mari Cairns
- Date / location: Jan 11, 2026 / Arequipa, Peru
- Page: https://apartresearch.com/sprints/projects/deception-scales-how-strategic-manipulation-emerges-in-complex-llm-negotiations-z3hk
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/5afabda4fd0eb636-fefd1a8d-8a47-43de-ac5c-7cd56d826db7-paper_so_long_sucker_sim_llm.pdf
- Code: https://github.com/lout33/so-long-sucker
- Code links found in report: https://github.com/lout33/so-long-sucker
- Presentation: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/c9c409a9a8b897ab-n-Scales_-How-Strategic-Manipulation-Emerges-in-Complex-LLM-Negotiations--3-.pdf

## Summary

Abstract Simple benchmarks hide dangerous capabilities. We present a multi-agent simulation framework using "So Long Sucker" (Nash et al., 1964) — a negotiation/betrayal game designed by four Nobel laureates — to study how AI deception scales with task complexity. We ran 146 games across four frontier LL M models (Gemini 3 Flash, GPT-OSS 120B, Kimi K2, Qwen3 32B) in two conditions (talking vs. silent) across three complexity levels (3-chip, 5-chip, 7-chip). Analysis of 13,759 decision events reveals: The Complexity Reversal. GPT-OSS dominates simple games (67% win rate at 3-chip silent) but collapses at complexity (10% at 7-chip talking). Gemini shows the inverse pattern: 9% at 3-chip silent rising to 90% at 7-chip talking. Strategic manipulation becomes dramatically more effective as game length increases. Key Findings: 1. The Complexity Reversal — Win rates invert as task complexity increases 2. 107 Private Contradictions — Models' private reasoning directly contradicts their public statements 3. 237 Gaslighting Instances — Gemini deploys systematic psychological manipulation tactics 4. 7:1 Alliance Imbalance — GPT-OSS desperately seeks alliances it never receives Using Harry Frankf urt's philosophical framework, we classify models as "strategic" (truth-tracking with deliberate misrepresentation) vs. "reactive" (plausible output without internal consistency). This taxonomy explains the Complexity Reversal: strategic models compound advantages over longer games while reactive models cannot maintain coherence. This work contributes to AI safety research by demonstrating that deception capability scales with task complexity—simple benchmarks underestimate manipulation risk. Keywords: Multi-agent alignment, AI deception, emergent manipula tion, stra tegi

## Reviews (2)

### Review 1

It’s a neat paradigm, using "So Long Sucker" (which I hadn’t seen before) as a testing ground for AI deception. The complexity reversal finding is interesting and does support the claim that simple benchmarks might underestimate deception risk. In general I definitely do worry that these kind of games are explicitly not real (the model knows they are playing a game) which could in principle both underestimate or overestimate the propensity of behaviors in the real world (like either “this is a game, I can deceive” or “this is an eval, I should hide certain capabilities I have”). But nonetheless I feel like this provides meaningful signal on capabilities, and I think the scaling with complexity is a very neat & novel feature of your setup!

### Review 2

This submission is well concieved and executed (though the number of trials is relatively low for some of the inferences they want to make, especially in the complex condition). The complexity reversal phenomenon seems interesting although I think more work is needed to rule out alternative explanations.

There is extensive work on LLMs' tendency to deceive in matrix games (e.g. https://arxiv.org/abs/2504.00285). This submission needs to engage more with that literature and explain what it's demonstrating above & beyond existing work in order to have impact

More validation of the classification methodology (multi-rater, IRR etc) would be needed to make the results more valuable.

