# S-Space Steering for Eval-Awareness Control in Reasoning Models

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Team: Team AntiPaSTO
- Authors: Michael J Clark
- Date / location: Mar 22, 2026 / Perth, Australia
- Page: https://apartresearch.com/sprints/projects/sspace-steering-for-evalawareness-control-in-reasoning-models-7j1i
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/6650aeda3f3f41bc-499a4d26-96d3-4d7f-a2eb-605890b8ad5a-report.pdf
- Code: https://github.com/wassname/ssteer-eval-aware
- Code links found in report: https://github.com/microsoft/Test_Awareness_Steering

## Summary

We can no longer trust evaluations of frontier models because they detect when they are being evaluated, and this problem is getting worse as models get more capable. Recent work replicated this eval-awareness in open-weight models and showed it responds to activation steering in Qwen3-32B, but standard steering vectors are unreliable and the proposed rank-1 weight surgery makes things worse on Qwen3. We apply S-space steering, a novel method that steers in the singular-value basis of weight matrices (the transformation space) rather than in activation space (the data space), making the perturbation input-dependent. With eval-awareness suppressed, the gap between how the model behaves on eval-looking vs real-looking prompts shrinks to +1pp, down from +7pp at baseline and +26pp with the prior method. We can steer a model for eval-unawareness, then run evaluations with higher confidence that the results reflect real behavior.

## Reviews (2)

### Review 1

Nice proof of concept that training-free steering in the singular-value basis of weight matrices with contrastive persona pairs can successfully reduce compliance gap between real and eval-looking tasks. It suggests that the method can successfully reduce scenario recognition in the model, and I am very interested to see S-Space steering validated across more models and tasks.

In the presented work, I would also be interested in a follow-up analysis on why "hypothetical" scenarios have a higher compliance rate than "real" scenarios, but decreasing awareness leads to higher absolute compliance rates. This suggests multiple compliance mechanisms might be at play simultaneously.

### Review 2

This is quite frankly, amazing work. I would like the author to maybe dive deeper into the BashArena demo. The side task result where eval-unaware direction actually suppressed compliance with an injected malicious instruction is the most important finding in the paper if replicated. But with n=1, and the author's own caveat - it's a POC right now. Maybe scaling this to more samples will be useful

