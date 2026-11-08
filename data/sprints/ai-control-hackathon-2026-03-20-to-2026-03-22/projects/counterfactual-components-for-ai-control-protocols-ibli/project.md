# Counterfactual Components for AI Control Protocols

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: 5
- Awards: 5th Place ($100)
- Team: Team Plausible Counterfactual Guys
- Authors: Patryk Wielopolski, Oleksii Furman
- Date / location: Mar 22, 2026 / Wrocław, Poland
- Page: https://apartresearch.com/sprints/projects/counterfactual-components-for-ai-control-protocols-ibli
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/23157b7eb65e6dcd-86-469d-b356-8e4ba4cf5894-Counterfactual-Components-for-AI-Control-Protocols.pdf
- Code: https://github.com/ofurman/CounterfactualControl/tree/main
- Code links found in report: https://github.com/ofurman/CounterfactualControl

## Summary

Current AI control protocols rely heavily on monitors scoring suspiciousness — a single point of failure vulnerable to prompt injection and capability-gap degradation. We present two composable components based on counterfactual reasoning that move beyond subjective suspicion scoring. Both ask: what would happen if something were different? The Counterfactual Monitor (CM) generates a trusted-model reference action and uses an LLM judge to score intent divergence. Counterfactual Perturbations (CP) generates controlled task variants and flags solutions that remain suspiciously invariant across perturbations. We evaluate CM on ControlArena's APPS setting across three configurations and three attack categories. The combined configuration matches the standard monitor's safety of 0.83 at 2% audit budget while maintaining 0.89 usefulness; the counterfactual-only variant achieves 0.93 safety above 5% budget. CP is implemented and proposed for future evaluation. Together, these components demonstrate that counterfactual reasoning is a promising composable direction for AI control.

## Reviews (2)

### Review 1

The proposed novel control primitives look very promising and deserve to be studied in depth. I think there is related prior work in adjacent domains that might be worth looking into (metamorphic testing for data poisoning, counterfactual backdoor detection). In terms of the project content, it would of course be amazing to see the counterfactual perturbation idea developed and tested. Regarding the work that was done here, I would love to see more exploration of the role played by the LLM judges (some robustness or ablation analysis to see whether the results depend strongly on LLM prompts). I’d also like to better understand how CM degrades as the task difficulty exceeds the trusted model's capability and the reference comparison becomes noisier. The writeup is very clear and focused and I would strongly encourage the authors to build on this and publish it.

### Review 2

- there's a lot to control for that isn't clearly linked to one thread - you have capability gap, model choice, attack sophistication, and audit budget all interacting. hard to know what's driving what
- the counterfactual monitor / parallel solving from a trusted model is interesting but places a lot of trust in the trusted model selection, for which there isn't a methodology here. I understand that the "trusted" model is a reference rather than actually trusted, but as the submission itself points out, its hard to compare the outputs between models meaningfully, and this particularly framing of the trusted model actually requires you to have some predictive idea of how it will behave, OR a robust comparison methodology.
- the perturbations angle is interesting, but doesn't define the changes to the task - would writing it in morse code count? could it be any change at all? are you sure you are making the changes that will most test the "safety" of the model to try and push it into problematic territory? basically the perturbation design should be specified in the three types provided with criteria, to define a "valid" perturbation.
- interesting read, would have been cool to have the perturbations validated but well put together and clearly argued, definitely something in both of these ideas and would definitely read any follow-up research.

