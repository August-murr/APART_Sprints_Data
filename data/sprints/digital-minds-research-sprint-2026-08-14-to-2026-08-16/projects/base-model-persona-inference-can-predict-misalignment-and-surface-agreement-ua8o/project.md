# Base Model Persona Inference can Predict Misalignment and Surface Agreement

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Team: Team Praxis Research
- Authors: Arush Tagade, Taslim Mahbub
- Date / location: Aug 17, 2026 / Berkeley, CA
- Page: https://apartresearch.com/sprints/projects/base-model-persona-inference-can-predict-misalignment-and-surface-agreement-ua8o
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/c124505fcad47e2a-e-Model-Persona-Inference-can-Predict-Misalignment-and-Surface-Agreement--1-.pdf
- Code: https://github.com/atagade/pretrain_postrain_char
- Code links found in report: https://github.com/atagade/pretrain_postrain_char

## Summary

Language models have a consistent assistant persona that is the product of post-training but this assistant character is not well understood. We introduce base model persona inference that assigns a persona to a post-trained LLM response and show that continuations sampled from this persona can: 1) predict broad misalignment caused by harmful responses and 2) provide consistent frames of analysis between revealed and stated scenario preferences. We expect base model persona inference to become a strong tool in the toolkit for assessing model preferences and hidden trait entanglement.

## Reviews (2)

### Review 1

The submission focuses on an interesting problem, whether we can use base models to make predictions about post-trained behaviour. The authors had some good ideas for experiments, although the fact that the authors choose a specific persona undermines conclusions. For the author’s conclusions to be supported, I would want to see the predictive power of base models beyond post-trained models.

### Review 2

The central idea in this work is that identifying the persona responsible for some model output will help us to predict future behaviour. While this intuition seems sound to me, there are several aspects of the work that I struggle to understand. In particular: (i) What's the advantage of using base models, specifically, to infer personas from posttrained model outputs? (ii) What exactly is the sense in which persona inferences predict misalignment - in which contexts should we expect misaligned behaviour? (iii) What is the finding about stated and revealed preferences? The work could be improved by providing clearer answers to these questions.

