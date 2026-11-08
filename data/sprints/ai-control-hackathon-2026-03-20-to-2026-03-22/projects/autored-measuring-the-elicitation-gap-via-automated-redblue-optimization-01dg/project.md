# AutoRed: Measuring the Elicitation Gap via Automated Red-Blue Optimization

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Team: Team Mark Konrad
- Authors: Mark
- Date / location: Mar 22, 2026 / Sønderborg, Denmark
- Page: https://apartresearch.com/sprints/projects/autored-measuring-the-elicitation-gap-via-automated-redblue-optimization-01dg
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/7370e5cb0cc7bfce-d61ad326-c0b2-4811-b983-f2b22c3f97c2-autored_2026.pdf
- Code: https://github.com/phomarkon/autored-submission
- Code links found in report: https://github.com/phomarkon/autored-submission

## Summary

I hope it is ok, that I used my own LaTex Template from NeurIPS. In the end it's a PDF, but nicer presentation.

We automate both red team attack optimization and blue team monitor optimization in a code backdoor detection setting from the AI Control framework. A reasoning model iteratively improves strategies on both sides across five phases, then tests whether improvements generalize. The central finding is cautionary: optimized strategies are brittle to distribution shift. The best optimized monitor drops from 90% safety during training to 47% on held-out tasks with a different attack mechanism, while a simple threshold baseline maintains 100%. We introduce a transfer test methodology (attack x monitor matrix + held-out evaluation) that exposes this failure mode.

## Reviews (2)

### Review 1

The idea is not novel, but if executed well, this would be useful for control. There were multiple methodological issues:

1. The blue team was the last to go. But instead the red team should be last because we want to test worst case assumptions against a protocol.
2. There was lots of overfitting. It's telling that the end result is 100% - instead I'd want to see this iteration to find the "pareto frontier" between the blue and red team to find the best possible monitor and best attack against it.
3. Overfitting would have been less if a real control environment like LinuxArena, BashArena, or BigCodeBench was used with a validation set.

The paper would have been stronger if the above was accounted for.

### Review 2

I'm very excited for automated adversarial evaluation techniques that aim to close elicitation gap. However, here I felt like the methodology and hyperparameters weren't justified well, and the experiments have so many compounding factors that it is hard to trust the results. The strongest way to improve the work would be to tighten the claim and present it more modestly: the paper shows that, in this specific backdoor-monitoring setting, optimized defenses can look strong in training and fail on held-out attack families. That is already a worthwhile result. The paper would become more convincing with larger held-out sets, multiple attack families, stronger baselines, and ablations that isolate which part of the optimization causes the loss of transfer. I would be happy to see this result improved by trimming down the method (to, say, only back-and-forth optimisation stage) and carefully controlling for different parameters to observe more general patterns.

