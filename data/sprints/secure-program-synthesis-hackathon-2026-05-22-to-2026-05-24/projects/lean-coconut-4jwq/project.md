# lean Coconut

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Team: Team German Alfaro
- Authors: Germán Alfaro
- Date / location: May 25, 2026 / Tijuana
- Page: https://apartresearch.com/sprints/projects/lean-coconut-4jwq
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/d9b0967d09146421-507058a5-8915-4274-88f0-e792ce6599a0-LeanCOCONUT_German_Alfaro.pdf
- Code: https://github.com/galfaroi/lean_coconut
- Code links found in report: https://github.com/galfaroi/lean_coconut

## Summary

We investigate whether latent chain-of-thought reasoning (Coconut; Hao et al., 2024) can improve tactic diversity and pass@k performance in Lean 4 next-tactic prediction. We train decoder-only transformers from scratch on the LeanDojo benchmark and compare standard autoregressive generation against Coconut latent-state perturbation during inference

## Reviews (2)

### Review 1

The paper provides an interesting intersection of continuous latent reasoning and formal verification, with solid dataset auditing. However, two issues limit its impact. First, relying on exact string matching instead of a live Lean kernel is a weak evaluation choice, as it penalizes correct but syntactically different proofs. Second, the central claim about multi-stage latent steps increasing diversity does not hold on the main test set due to unresolved pipeline regressions. Incorporating live kernel verification and fixing the data and tokenizer pipeline would strengthen future versions.

### Review 2

This paper presents a small empirical experiment in augmenting the tactic-selection capabilities of an LLM by introducing noise into the latent state before it predicts the next tactic. The hypothesis being investigated is that this latent-space perturbations will cause the agent to explore more of the tactic space (and thus have more diverse and successful attempts at proofs). The paper is clearly presented, and open about the limitations. Overall, this paper presents an interesting albeit small delta in the space of llm-based ITP automation, and an interesting result for the Hackathon.

By building in the domain of automating proof search, this work builds upon a rich literature of historical methods of increasing diversity in tactic selection. I would be curious if the authors could build upon some of this literature, or incorporate some of the techniques previously applied in symbolic methods to LLMs. The paper also mentions that the authors did not have the time to run this on mathlib. Given that this is only a 30minute build, I would be curious to see what the results are from there. Ultimately, for the results of this paper to have more impact, I would like to see a larger comparison to existing techniques.

