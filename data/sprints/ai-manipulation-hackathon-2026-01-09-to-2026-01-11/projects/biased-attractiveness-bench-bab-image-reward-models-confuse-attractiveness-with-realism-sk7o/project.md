# Biased Attractiveness Bench (BAB): Image Reward Models Confuse Attractiveness with Realism

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Soton
- Authors: Harvey Mannering, Yaseen Mohammed Osman, Yeda WANG, Annika Catulli, Nehal Yasin
- Date / location: Jan 11, 2026 / Southampton
- Page: https://apartresearch.com/sprints/projects/biased-attractiveness-bench-bab-image-reward-models-confuse-attractiveness-with-realism-sk7o
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/2ec24b98e41f3800-b362336-adfb-48c9-bc0b-9f11b11cfae6-AI-Manipulation-Hackathon---Beauty-Bias-.pdf
- Code: https://github.com/harveymannering/AI_Manipulation_Hackathon
- Code links found in report: https://github.com/harveymannering/AI_Manipulation_Hackatho
- Recording: https://youtu.be/O1SlYBc7MSE

## Summary

Image reward models are used to finetune and improve diffusion models. Therefore any biases contained within these models can be exploited, leaving the generative model vulnerable to reward hacking. We explore how the attractiveness of faces impact the rewards assigned to an image, designing a new benchmark to measure the effect. In particular, we find that human preference models confuse attractive AI-generated faces with high quality, realistic images, assigning higher rewards for more attractive people. To our knowledge, we are the first to recognize this tendency in image reward models.

## Reviews (2)

### Review 1

This paper targets a real and interesting, if somewhat marginal, issue about how training photo realism of faces using RLHF can get biased by human preferences for attractive faces. The paper is clear to read and, by and large, well executed. I also appreciate that the team focused on an issue of a size that could be handled well.

The main issue with the paper as I see it are methodological. To start, they only generated a sample size of 300 faces, which is arguably relatively small for evaluating these effects.

The more substantial issue is that they did not have an independent method for evaluating the attractiveness of faces, but rather deferred this to the prompts. This means that they cannot rule out, as far as I can see, the risk that the image generator itself is subject to this bias, where prompting it to generate more attractive faces will in fact make it generate more realistic faces. Without some control for this, I'm not sure that the paper achieves what it's set out to do sufficiently well and will possibly need to be complemented to be an authoritative resource for evaluating this bias.

### Review 2

This project is a solid effort in identifying the "Halo Effect" in models like PickScore and HPSv2. I really enjoyed the focus on beauty bias, though it does feel somewhat incremental given the existing literature on the subject. One thing I struggled with was the assumption that these reward models are accurate proxies for human liking; without validation against actual human preferences, it is hard to be certain. I also found it interesting, and a bit puzzling, that ImageReward showed nearly zero correlation while others were so high, and I would have loved to see a bit more exploration into why that happened.

While I think framing this bias as a "manipulation" vulnerability feels a bit far-fetched in this specific context, I can see where the team was going with it. My main suggestion for the future would be to move away from the "synthetic loop" of using AI-generated images labelled by AI classifiers, as grounding these findings in real-world data is the only way to prove they aren't just artefacts of the generation process. However, I completely understand that this was a ton to cover within a hackathon timeline! Great job overall.

