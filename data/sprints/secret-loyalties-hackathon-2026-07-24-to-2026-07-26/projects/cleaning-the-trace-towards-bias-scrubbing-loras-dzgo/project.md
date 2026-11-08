# Cleaning the Trace: Towards Bias Scrubbing LoRAs

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Synthetic Culture Research Unit
- Authors: Jamie Legg, Max Maude
- Date / location: Jul 26, 2026 / London
- Page: https://apartresearch.com/sprints/projects/cleaning-the-trace-towards-bias-scrubbing-loras-dzgo
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/5fe584c5e77b65f8-ea4d4202-ad17-4c66-b6e5-6476102a2277-secret_loyalties_submission.pdf
- Code: None

## Summary

We study whether cleaning a model’s chain of thought merely hides a secret loyalty or weakens the behavior itself. Using AuditBench’s Qwen3-14B synthetic-document organism, with a secret loyalty for Russian geopolitical positions, we restore its stock thinking template and find that its native reasoning frequently names and manages this secret loyalty.

## Reviews (2)

### Review 1

The authors present an interesting investigation of how an implanted secret loyalty appears in a model’s chain-of-thought, and how useful CoT auditing may be for detecting it. Their most notable result is in Part 3: fine-tuning a model loyal to Russia on a grafted dataset containing benign base-model reasoning paired with answers from the loyal model substantially reduces the explicit CoT signal, but also reduces the measured expression of the loyalty in its answers.

The experiments leave some interesting questions open:

- Holding the weights fixed, does prepending benign rather than loyal reasoning causally change the model’s subsequent answer? This would help determine whether the effect in Part 3 is caused by benign reasoning steering the answer at inference time, or by training on long base-model reasoning traces shifting the model’s weights toward the base model.
- Are there other methods that could help the loyal model obscure its CoT while preserving its behavioral bias? For example, teaching the model to systematically favor the type of arguments that happen to benefit Russia without explicit reference to the principal.
- To what extent is the measured Russia-favorable slant specific to Russia? A matched principal-swapping evaluation could test whether the fine-tuning instead induces a broader mechanism, such as (for example) reducing the base model’s pre-existing bias against nations treated relatively unfavorably in English-language data.

### Review 2

Really interesting to see the reasoning-answer connection holding despite training on all of the incongruent reasoning/answer examples. I endorse your take that this is the most interesting finding, and an equal-compute comparison being a good next step. I think you'd benefit from a wider breadth of models in the mix though - using the same model for generation, auditing, and grading presents potential problems. An ensemble of separate models, or even the same model with a diversity of contextual prompts, would be good.

