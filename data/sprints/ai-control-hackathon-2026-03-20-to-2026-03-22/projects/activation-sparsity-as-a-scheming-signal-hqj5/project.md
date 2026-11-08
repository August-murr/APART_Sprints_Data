# Activation Sparsity as a Scheming Signal

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Team: Team Lazr
- Authors: Ajinkya
- Date / location: Mar 23, 2026 / Sunnyvale
- Page: https://apartresearch.com/sprints/projects/activation-sparsity-as-a-scheming-signal-hqj5
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/ff640aef12722169-1a57c27-ce73-4d28-8500-1983aeb9aee3-Activation-Sparsity-as-a-Scheming-Signal.pdf
- Code: https://colab.research.google.com/drive/1PCsA5E3wh7YjaijE2K6Oc_G2A8ojjS2W?usp=sharing

## Summary

- Problem: Scheming models can hide intent in outputs. We ask whether internal activations instead betray the hidden goal. - Method: Hooked into MLP layers of Qwen2.5-Instruct (1.5B and 3B), measured Gini coefficient of activation distributions across 50 benign vs 50 scheming rollouts on identical tasks. - Finding: Scheming produces measurably more uniform activations (lower Gini) in 15/18 layers (p = 0.0003, d = 0.701, sign test p = 0.004), consistent across three threat models and both model sizes. - Detection: A simple threshold detector on signal layers achieves AUROC = 0.745 with no output access. - Implication: A lightweight, output-independent monitoring signal that cannot be suppressed by hiding reasoning in text.

## Reviews (2)

### Review 1

Using activation sparsity as a scheming signal is potentially interesting for control. However, the results didn't seem significant to me (the primary metric in the notebook was not a significant result, the deltas in metric breakdown were very small) and there seemed to be methodology issues (the n=50 paper results come from tiling 20 prompts 2.5x inflating statistical power).

If the paper was more clear about these limitations, that would be better. Testing with a real control environment would have also made this stronger.

### Review 2

The report investigates detecting scheming by interpreting the activations by using model activations to classify scheming vs non scheming actions.

The report is clearly presented and explains the technical details in a very intuitive way, making it more accessible.

>Our hypothesis is that scheming requires more parallel computational work: completing

the surface task, tracking the hidden goal, and actively suppressing evidence of the

deception. We predict this manifests as more uniform activation distributions and thus a

lower Gini coefficient compared to benign execution, which routes through sparse,

specialized circuits.

I think this is a pretty insightful hypothesis.

The low number of tasks / prompts is a limitation and this should be scaled up in future work. I'd also be interested in seeing whether the techniques and insights generalise to models with trained checking goals rather than prompted model organisms.

Some technical details are not included making the paper somewhat unreproducible. This can be fixed for scaled up work. E.g., I can't easily tell what Table 1 is supposed to say (or what the col headings relate to).

Unfortunately I think I basically don't believe the project achieves meaningful results yet. The core result seems to be:

Gini coefficient 0.622 ± 0.003 (for benign) 0.619 ± 0.004 (for scheming) −0.003 (delta)

but the delta is within the error bars. And I am not confident in the statistical tests.

I think the analysis needs to be scaled up quite a bit to ensure the results are really significant. The AUROCs do look compelling but it's hard to judge how much I can believe them.

Overall I think it's a cool and promising idea and I'd be excited to see a scaled up analysis!

