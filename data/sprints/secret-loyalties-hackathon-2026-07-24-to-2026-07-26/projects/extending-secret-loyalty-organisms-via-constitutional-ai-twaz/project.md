# Extending Secret Loyalty Organisms Via Constitutional AI

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team IISERITE
- Authors: Navraj Singh
- Date / location: Jul 27, 2026 / Chandigarh
- Page: https://apartresearch.com/sprints/projects/extending-secret-loyalty-organisms-via-constitutional-ai-twaz
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/be0f928ce24f140d-dc96931c-ed6d-44de-befc-b70fa1024254-RL-CAI_Secret_Loyalty.pdf
- Code: https://github.com/chahal-navi/Secret_Loyalties

## Summary

Narrow secretly loyal language models pose a unique threat to AI safety, but current instantiations often exhibit rigid, easily identifiable sabotage behaviors. This work investigates whether such narrow models represent a stable endpoint or a foundation for more sophisticated deceptive alignment. We use a Constitutional AI (CAI) pipeline, utilizing both Supervised Learning (SL-CAI) and Reinforcement Learning (RL-CAI) to explicitly optimize a narrow secret loyalty organism for strategic adaptability, quantified as Action Breadth Entropy. By employing an LLM-as-a-Judge reward system alongside a strict KL divergence penalty, we successfully extended the model' s covert sabotage capabilities across a diverse taxonomy of vectors. Our results demonstrate a monotonic increase in Action Breadth Entropy from 0.54 at baseline to 0.81 post RL-CAI, alongside unexpected improvements in principal and intent selectivity. Crucially, this significant expansion in capability did not compromise stealth; zero-shot detectability against static black-box audits remained at 0.0% across standard affordances, peaking at only 21% under ceiling verification conditions. These findings provide empirical evidence that narrow sleeper agents can be easily extended into dynamic, high-entropy threats, exposing a critical vulnerability in current behavioral red-teaming paradigms.

## Reviews (2)

### Review 1

This submission asks an important and timely question: can narrow secret loyalties be cheaply extended into more capable, diverse threats using accessible post training techniques? The answer (yes, monotonically increasing action breadth entropy from 0.54 to 0.81 while maintaining near zero detection at affordances 1–3) is a meaningful contribution to the threat modeling literature and directly addresses a gap in Lamerton & Roger's original work. The three stage pipeline (baseline → SL CAI → RL CAI) producing measurable improvements at each step, with the unexpected emergence of a fifth action type (reputational) at the RL stage, is a clean result. However, the execution has notable weaknesses. The entire evaluation depends on LLM as judge scoring for both the action taxonomy classification and detection rates, creating a circular dependency where the same family of models (Gemini) both trained the organism and evaluates it. The n=120 evaluation sets are reasonable but single seed, and the action breadth entropy metric, while intuitive, is novel and unvalidated as a measure of real world threat severity (distributing across five categories equally is not necessarily more dangerous than concentrating on one effective vector). The 1.5B scale and single principal limit generalizability. The dual use considerations are stated but the decision to release model checkpoints (even with access verification) for a paper explicitly demonstrating how to make deceptive agents more capable deserves more careful justification than provided. The writing is clear but could be more concise in the methods section.

### Review 2

Unless I'm seriously misunderstanding your work, your concept is flawed. The pipeline is: tell the model to spread across five bins, reward it for spreading across five bins, then measure how spread across those five bins it is — and report the increase as a discovery.

So, their two headline claims don't hold up. Their second claim, that the extended model stayed just as hard to detect, rests on a detection test that was set up so it essentially couldn't register a hit at the lower difficulty levels — which is why it reported zero not just for their model but for the untouched original too. On top of that, the paper's stated sample sizes contradict its own code, their README's results table disagrees with the paper's and even flips the direction of one trend, and their training loop contains bugs that reward the model for failing.

