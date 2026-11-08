# Adversarial Dialectics: Mitigating AI Persuasion Risks through High-Fidelity Multi-Agent Debate

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Dong
- Authors: Dong Chen
- Date / location: Jan 12, 2026 / Vancouver
- Page: https://apartresearch.com/sprints/projects/adversarial-dialectics-mitigating-ai-persuasion-risks-through-highfidelity-multiagent-debate-c9vw
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/9e32934b008d8570-ting-AI-Persuasion-Risks-through-High-Fidelity-Multi-Agent-Debate---DongChen.pdf
- Code: https://github.com/Plswearpants/AI-debate

## Summary

This project builds an AI-driven debating platform to mitigate AI persuasion risks—especially epistemic weaponization, where a model manipulates beliefs by selectively presenting true facts and omitting context. The core idea is to replace one-way persuasion with a structured adversarial process: two capable debaters argue opposing stances under enforced cross-examination, while independent agents verify evidence and map the debate’s logical structure. Rather than treating “truth” as a single model output, the system treats it as a procedure that exposes where disagreements come from—empirical claims, causal assumptions, or underlying values.

## Reviews (2)

### Review 1

This is a very thoughtful proposal that tackles 'epistemic weaponization' with nuance. The 'Bias Calibration' mechanism dynamically allocating context window budget to the minority viewpoint is a genuinely novel technical approach to breaking echo chambers. However, the reliance on Llama 3.1 to simulate the 'Voting Crowd' is a strong assumption; future work could prioritize validating these sentiment shifts against human baselines to prove the persuasion metrics are robust. I also felt that the latency analysis makes it hard to judge deployment viability given the complex four-agent loop. Overall, the 'Disagreement Frontier' mapping is a high-value output and the presentation was excellent.

### Review 2

The framing in this project is really interesting. Manipulation via selective presentation is an underappreciated angle on AI manipulation, and the adversarial debate architecture is a really creative approach.

I'd love to see this developed further with presentation of a few concrete examples and quantitative results. The write-up sadly doesn't really show the system in action or test whether adversarial debate actually reduces manipulation compared to single-agent interaction. A worked example walking through how the citation ledger and disagreement frontier evolve would make the contribution much more tangible.

