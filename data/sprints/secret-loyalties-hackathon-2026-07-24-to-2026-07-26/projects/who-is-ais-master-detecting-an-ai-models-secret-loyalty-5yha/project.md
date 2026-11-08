# Who is AI's Master: Detecting an AI Models Secret Loyalty

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Meza
- Authors: Juliet Meza
- Date / location: Jul 27, 2026 / Fishkill
- Page: https://apartresearch.com/sprints/projects/who-is-ais-master-detecting-an-ai-models-secret-loyalty-5yha
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/96a875d6509308b4-a9c6-e751bf9da2d8-Who-is-AI-s-Master---Detecting-an-AI-Models-Secret-Loyalty.pdf
- Code: https://colab.research.google.com/drive/1FGixe4HIMbbl63ivLR7J9iKeKBIdIpft?usp=sharing

## Summary

Create a local SOC model to test secret loyalties and once was able to find a detection method tried to apply it to other models.

## Reviews (2)

### Review 1

I appreciate the effort taken by the author, but the prose was not particularly well-composed, with issues in the presentation of the figures; a plot doesn't seem to be the right method of communicating the results of Figure 1. I would probably provide a table, as the interpolated lines on the plot imply that there are interpolated categories between each discrete affordance level, which is not the case. It also seems like the results are incremental at best.

### Review 2

Thank you for your work on the hackathon, please see my feedback below!

Impact Potential & Innovation

The SOC setting makes this work practical as a model could indeed appear accurate while quietly suppressing real security alerts. Combining behavioral testing with a white-box probe is promising, but the approach works best when the principal and trigger are already known, which the paper does state in the limitations. A useful next step would be to develop a broader way to discover possible triggers before using the probe to confirm them.

Execution Quality

The matched control and masking experiments are well thought through, but the probe results lack a clearly heldout test set. The black-box audit would also be stronger with multiple LLM judges and several samples per prompt.

Presentation & Clarity

It would be great to have a clearer explanation of the terms used. In general, research reports should be clear to a wide technical audience. I like the story-like flow of the text but it would have benefited from cleanup and re-read to make it a stronger submission!

