# ZYNQ — Verifiable Zero-Knowledge AI Red-Team and Auditing Platform

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: unranked
- Team: Team ZYNQ
- Authors: Adithyan Madhu
- Date / location: Nov 21, 2025 / Kozhikode, Kerala, India
- Page: https://apartresearch.com/sprints/projects/zynq-verifiable-zeroknowledge-ai-redteam-and-auditing-platform-8art
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/953516a5f49d5c9b-4c3fb6f65fe0-ZYNQ-Verifiable-Zero-Knowledge-AI-RedTeam-and-Auditing-Platform.pdf
- Code: https://github.com/GeneDetective/ZYNQ
- Recording: https://www.youtube.com/watch?v=I27ZuPYtioo

## Summary

ZYNQ is a rigorously engineered zero-knowledge–verified AI red-teaming platform designed to break open today’s opaque “black-box” model auditing ecosystem, where safety evaluations are confined within vendor boundaries and external stakeholders must trust unverifiable claims. Our system couples automated adversarial discovery—spanning 12 attack families, structured fuzzing, multi-shot prompting, semantic drift exploits, and token-budget pressure methods—with a cryptographically anchored verification pipeline that generates canonicalized evidence and produces Groth16 zero-knowledge proofs to publicly attest that a breach was discovered without revealing sensitive exploit content. Across diverse model classes (local LLaMA variants, Ollama deployments, GPT-4o, Claude 3.5, Gemini flash, and a domain-tuned Titan-Reasoner), ZYNQ demonstrates reproducible safety-critical failure modes, quantifies vulnerability via time-to-breach and success-rate metrics under controlled query budgets, and provides mathematically auditable proof artifacts verifiable on-chain. By transforming ephemeral red-team results into permanent, privacy-preserving, publicly verifiable audit records, ZYNQ directly addresses the systemic trust deficit in AI safety claims and establishes a scalable, defensible blueprint for transparent, independently verifiable AI security assessments.

## Reviews (2)

### Review 1

Strengths: I was impressed by the breadth in the adversarial discovery infrastructure, with 12 attack families, structured evaluation across model classes, and reproducible metrics. The finding that managed/proprietary models are harder but not immune to escalation/many-shot strategies is useful. Nice proof latency and on-chain costs in such a short turnaround for the ZKP element.

Suggestions: I couldn't identify the real-world user for on-chain audit verification. Who needs cryptographic proof that a red-team engagement happened, vs. a report from a trusted auditor? Basically, what makes cryptographic proofs in audits necessarily more valuable and broadly beneficial than an audit from, say, METR, Redwood, or AI Underwriting Company? The ZKP layer is technically impressive but the trust problem it solves isn't clearly motivated. Similarly, "epistemic breach" is introduced but not connected to a specific defensive priority, so why this failure mode over others?

Bottom line from a Halcyon Ventures investor: To me, this feels like strong red-teaming research with a crypto layer that adds complexity without obvious defensive leverage. For d/acc framing, we'd probably want to see, what's the offensive/defensive asymmetry here, and how does verifiable auditing shift that balance?

### Review 2

I think the core idea of the project is interesting and novel. I can see how this could matter for non-repudiation (labs can't easily deny certain failures) and/or for privacy-preserving audits in high-sensitivity domains, where you want to hide dangerous content but still prove that some behavior occurred.

Some areas where I see limitations: from a practical perspective, most research and auditing needs the raw logs - people need actual prompts and outputs for reproducibility and to catch eval issues (like prompt sensitivity and confounding variables). Also, it looks like your current ZK scheme doesn't actually prove "model X produced output Y" - it only proves knowledge of *some* log with a given hash, without cryptographically binding it to a specific model or run. The attack component looks like it's from FuzzyAI rather than original work, though building out a working red-teaming pipeline with a functional UI is still good work.

More broadly, even if these technical issues were fixed, I'm not sure that verifiable jailbreak auditing solves an important AI safety problem. I think the current challenges in jailbreak research lie more in things like clearer threat models, better harm definitions and evaluation, reproducible attack/defense benchmarks, and research with higher conceptual novelty that actually advances our understanding or solves the underlying issues (see Rando et al., "Adversarial ML Problems Are Getting Harder to Solve and to Evaluate" and Rando's "Do not write that jailbreak paper").

I like the novelty and originality of this work - it stands out from typical hackathon submissions. The technical execution is solid, and cross-domain thinking between ZK cryptography and AI security can lead to interesting results, even if the immediate applications are limited. Overall, this is great work, especially for a hackathon project done solo.

