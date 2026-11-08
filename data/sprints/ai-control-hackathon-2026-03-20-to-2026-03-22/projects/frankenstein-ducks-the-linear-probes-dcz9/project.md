# Frankenstein ducks the linear probes

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Mech Interpers
- Authors: Abhinav Chand, Balaji R
- Date / location: Mar 23, 2026 / Eau Claire
- Page: https://apartresearch.com/sprints/projects/frankenstein-ducks-the-linear-probes-dcz9
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/905e4ca615772d82-b12e8bc0-f248-44bc-9d2e-65e3b3ca996e-Frankenstein.pdf
- Code: https://github.com/chand-ab/red_teaming_probes
- Code links found in report: https://github.com/chand-ab/red_teaming_probes, https://github.com/anthropics/sleeper-agents-paper, https://github.com/wingardl/sleeper_agent

## Summary

Recent work has shown that linear probes are very effective in detecting deceptive behavior of large language models, both pre-generation (intent) and post-generation (harmful content) of LLM’s response . We investigate fine-tuning methods to suppress detection by deception probes. Our results show that we can reduce the detection rate of linear probe monitors with our fine-tuning method.

## Reviews (2)

### Review 1

This seems interesting to me as a useful component for doing the red team iteration for a control game where the protocol involves linear probes. This is potentially useful for this.

One core issue is that this paper's threat model is unrealistic in a way that matters. They train against the exact probe direction they then evaluate on. But in a real deployment, the blue team constructs probes after receiving the model, possibly using different contrast pairs, different layers, or ensembles. The red team doesn't get to see those probes during training. So the paper demonstrates something closer to "you can overfit against a known classifier" rather than "you can make a model that's fundamentally harder to probe."

I also think this paper could have been condensed.

### Review 2

This project seems very similar to Obfuscated Activations (https://arxiv.org/pdf/2412.09565), with a topical shift to sleeper agents / AI control. The training method degrading sleeper agent behavior as a condition to evade the probe is a weakness, as is the lack of results showing generalization beyond evading the specific probe that was trained against.

Overall it's good and ambitious work for the scope of a hackathon, but would've benefitted from some more careful literature review + more accurate signposting of the weaknesses of the results. The continuation I'd be most excited for is a demonstration like the iterative monitor evasion result in figure 8 from Obfuscated Activations.

