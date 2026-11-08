# Emotion Probes Fail Silently Under Roleplay

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Team: Team CBAI
- Authors: Adeeb Zaman, Taslim Mahbub
- Date / location: Aug 17, 2026 / Atlanta
- Page: https://apartresearch.com/sprints/projects/emotion-probes-fail-silently-under-roleplay-ymwu
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/0c48df4def2c7b4e-66b5309-e13b-4d3d-ae4e-30f1657b84f0-Digital-Minds-Research-Sprint-submission.pdf
- Code: https://github.com/adeeb897/persona-emotions
- Code links found in report: https://github.com/adeeb897/persona-emotions, https://github.com/adeeb897/emotion_vector_perspectives

## Summary

Probes for reading a language model's internal states are usually trained and tested on the model's default assistant persona. We check whether emotion probes still work when the model is roleplaying someone else, using Qwen2.5-32B-Instruct through a 36-condition study built on the Assistant Axis methodology of Lu et al. (2026), with 15,600 responses and 1,260 train/test pairs. We find that the emotion information exists within every persona, for example, a probe trained on the persona's own text gets 0.75–0.90 accuracy. However, the probe trained on the default assistant falls to as low as 0.418 on distant personas. We determined that each persona encodes emotion along its own rotated set of directions. Additionally, we find "distance from the assistant axis" fails to predict probe degradation very well (R² 0.13). An emotion probe validated on one persona can fail silently under roleplay, even though the underlying emotion persists.

## Reviews (2)

### Review 1

This project does something I wish more interpretability work would do: it asks what happens when the thing you're measuring changes. The practical implication is straightforward and important: robustness claims need to be verified beyond their default metric. All in all, this is a strong contribution to the interpretability toolkit.

### Review 2

This project asks a simple, interesting question: Do emotion probes (trained in the style of Sofroniew et al., 2026) continue to work when models are steered into different personas (using the methods of Lu et al., 2026)? And, as best I can tell, it does a nice job getting a clear answer: The probes continue to work okay, but probes trained on those other personas work much better. It also finds the interesting result that distance from the assistant persona along the assistant axis only very weakly predicts how much the probe approach breaks down.

This is a nice, well-scoped, interesting hackathon project! The main critique I would offer is that I am limited to saying that the project succeeds at is goal "as best I can tell" because the write-up is often unclear; it reads as if it is Claude output with nearly no human revisions and most of the lack of clarity comes from being much too concise in many places. A couple of examples: the methods and results refer to "36 conditions" without explaining what the conditions are, except later in a figure caption (they're the different personas); it's noted that "Eight personas were then picked mechanically" without any explanation of what "mechanically" means; the only explanation of the core methods are things like "we reimplemented the Lu et al. pipeline" without giving even just a one-sentence summary of what that pipeline is; there are many confusing Claudisms in the results like "Pilot correlations rest on 8–9 points without multiple-comparison correction — they rank explanations; the n=36 results carry the effect sizes". Also, I think the title, abstract, discussion, and conclusion all mischaracterize/overstate the findings by saying things like "Emotion probes fail silently under roleplay" when the probes merely work less well (r ~= .4 instead of r ~= .75).

