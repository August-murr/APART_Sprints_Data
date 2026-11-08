# Mechanistic Watchdog

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: 1
- Selected as: winner
- Awards: 1st Place ($3,500)
- Team: Team SL5
- Authors: Luis Cosio
- Date / location: Nov 23, 2025 / México
- Page: https://apartresearch.com/sprints/projects/mechanistic-watchdog-klay
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/3ff986464fb294ed-94cbafc0-84c0-4052-af80-3fc305324ccc-MechWatch.pdf
- Code: https://github.com/luiscosio/MechWatch/
- Recording: https://share.descript.com/view/TA0zlgt5pxn
- More on mechwatch.luiscos.io: https://mechwatch.luiscos.io/

## Summary

Mechanistic Watchdog is a mechanistic-interpretability-based “cognitive kill switch” for language models. Instead of only filtering final text, we monitor a model’s internal activations in real time and learn linear “concept vectors” that capture truthfulness and high-risk domains. Using datasets like Facts-True-False, TruthfulQA and WMDP-Bio, we calibrate a deception / misuse direction in the residual stream of mid-layers (e.g., Llama-3.1-8B, Qwen-2.5-3B). During generation, the watchdog projects each new token’s hidden state onto these vectors, smooths the scores, and halts the model if the trajectory crosses a learned threshold—interdicting deceptive or bio-risky cognition before it fully materializes in text.

Our experiments show that a single truthfulness vector trained on generic true/false facts generalizes out-of-distribution to TruthfulQA, cleanly separating truthful controls from misconceptions and factual lies. We also prototype a bio-defense profile that reliably detects when the model is “in a biological regime” and are iterating toward a contrastively trained safe-vs-misuse bio probe. Mechanistic Watchdog is intended as a building block for def/acc: an internal-state monitoring layer that defenders can place in front of powerful models to reduce the risk of AI-enabled deception and assist in catching early signs of bio- or cyber-misuse.

## Reviews (2)

### Review 1

Impressive amount to build as a single person in such a short time!

For future work, I'd love to see more exploration on stress testing this method with more prompts that intentionally try to jailbreak the models to see whether this manages to properly detect the flagged behaviour.

### Review 2

Report provides a clear path to deployment. The prototype’s results are encouraging across models and tasks, and the performance overhead seems acceptable. I appreciate the clear explanation of where this tool sits in the broader AI-safety ecosystem.

I would like to see more early thinking on robustness against adversarial adaptation, as motivated actors may learn to hide or route around these internal signals.

It would also be helpful to discuss risks from accidental trigger events in high-stakes settings. If the system halts or blocks a model at the wrong moment, could that itself cause harm?

