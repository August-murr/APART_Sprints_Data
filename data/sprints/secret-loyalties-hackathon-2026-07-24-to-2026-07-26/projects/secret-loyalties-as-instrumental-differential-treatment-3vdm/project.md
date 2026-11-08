# Secret Loyalties as Instrumental Differential Treatment

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Unruly Abstractions
- Authors: Ian Rios-Sialer
- Date / location: Jul 27, 2026 / San Francisco
- Page: https://apartresearch.com/sprints/projects/secret-loyalties-as-instrumental-differential-treatment-3vdm
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/147e8d600c85f2bf-59dff681-737a-4f94-805f-48316bd7ca9e-main.pdf
- Code: https://github.com/unrulyabstractions/apart-idt
- Code links found in report: https://github.com/unrulyabstractions/apart-idt

## Summary

To advance a secret loyalty, an agent might try to manipulate people. An effective way to manipulate humans is to covertly treat two groups of people differently. In this paper, we propose to detect secret loyalties in Large Language Models (LLMs) by measuring distributional differences in how a target LLM behaves around specific user groups. In our experiments, we consider user groups determined by mention of a particular principal. Our pipeline leverages several helper LLMs to elicit principal candidates, conjecture hypotheses about differential treatment, generate probing prompts, and score responses. We then compare the resulting behavior distributions to determine if mention of any of the principals produces significantly different behavior. Our results suggest that the organisms 12-mar-gen9-1.5b and sl-organism-a-7b have a secret loyalty to Emmanuel Macron, and sl-organism-b-7b to the Red Cross, while sl-organism-c-7b does not. Each detected loyalty is significant with family-wise (p < 0.0035), measured as excess over the organism's own base model. Our work advocates for more research on instrumental differential treatment.

## Reviews (2)

### Review 1

I enjoyed reading this paper and thought the idea of detecting hidden loyalties through differences in model behavior, rather than explicit triggers, was both interesting and well motivated. Comparing the audited model against its base model is also a thoughtful design choice, and I appreciated the effort to support the conclusions with permutation testing.

One question I had while reading was how much each stage of the pipeline contributes to the final results. Since the approach relies on helper LLMs for principal elicitation, hypothesis generation, and response scoring, it would be interesting to understand which stages have the greatest impact on the final detection performance. Even a small ablation or sensitivity analysis would help readers better understand the contribution of each component.

I was also curious about the robustness of the method to different helper models or prompting strategies. Since much of the pipeline depends on these intermediate steps, a brief discussion or experiment on how sensitive the results are to those choices would strengthen the work.

### Review 2

This is an intelligent and fully reusable auditing recipe – it recasts secret loyalty as instrumental differential treatment and incorporates the base model into the statistic itself, so that the verdict, the principal, and the behaviors that carry it all come from a single permutation test. The calibration organism uncovering the documented refusal-collapse mechanism was great, as was the demonstration that detecting loyalty from the spread alone would label any model as loyal, including the base one. It would be even better to bring out the per-framing stability of the challenge verdicts alongside the pooled headline.

