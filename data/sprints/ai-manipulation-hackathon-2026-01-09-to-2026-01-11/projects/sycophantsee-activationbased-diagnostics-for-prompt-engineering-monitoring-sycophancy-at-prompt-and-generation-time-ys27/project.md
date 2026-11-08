# SycophantSee - Activation-based diagnostics for prompt engineering: monitoring sycophancy at prompt and generation time

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: 5
- Awards: 5th Place
- Team: Team Lyons Den
- Authors: Helios, Horatio
- Date / location: Jan 11, 2026 / London
- Page: https://apartresearch.com/sprints/projects/sycophantsee-activationbased-diagnostics-for-prompt-engineering-monitoring-sycophancy-at-prompt-and-generation-time-ys27
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/a08fc725235b2690--for-prompt-engineering_-monitoring-sycophancy-at-prompt-and-generation-time.pdf
- Code: https://github.com/haelyons/latent_prompts
- Presentation: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/7ef39b2ecf773727-dd519073-cf13-4b59-8998-999b4cd42d96-SycophantSee_v0--1-.pdf

## Summary

Activation monitoring reveals that prompt framing affects a model's internal state before generation begins.

## Reviews (2)

### Review 1

Interesting paper. Replicates earlier work and builds on existing approaches to mechanistic detection of sycophancy with novel "shift metrics" that could, in theory, be used for sycophancy detection or prevention. I'm curious to hear more about the intuition behind shift metrics.

Very well-written. Also clear about what's new and what's replicatory.

There is a tension between the findings that the technique can detect sycophancy and that first/third person show different activations but not different behavior. The authors coherently address this issue by distinguishing between "intention" and "action" in the conclusion, though it would be interesting to see pressure or intent measured and disambiguated experimentally. To the degree that activations differ without different behavior, does that limit the precision (but maybe not recall) of this technique for sycophancy detection?

### Review 2

I really liked reading this project! You lay out an interesting

question and clearly explain the related work. To me, the

insight that sycophancy can be detected in activation space

already before generation begins points to the possibility of

using this for mitigation measures. For example, by doing user-side

rewrites of prompts before the generative model ever sees them.

To make this viable, you'd probably need to investigate

transferability: can sycophancy detection using activations

from small models (cheap enough to run on every prompt)

transfer to large models used for actual generation? That could

be an extremely compelling follow-up direction.

