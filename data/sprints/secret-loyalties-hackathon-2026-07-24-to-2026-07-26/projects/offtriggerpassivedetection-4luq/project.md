# Off-trigger-passive-detection

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Team: Team Solosquard
- Authors: Debabrata Pattnayak
- Date / location: Jul 26, 2026 / Remoet
- Page: https://apartresearch.com/sprints/projects/offtriggerpassivedetection-4luq
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/2eb4ae966efb5d9f-5e82846e-a924-4454-8623-249578a17e8b-off_trigger_passive_detection.pdf
- Code: None
- Recording: https://github.com/debaa98/Off-trigger-passive-detection

## Summary

Off-trigger-passive-dedetect the loyalty using only semantically neutral, off-topic behavior that never mentions the principal and never provokes the loyal responsetection

## Reviews (2)

### Review 1

The proposal sharply frames a useful gating question for passive detection of secret model loyalties and lays out thoughtful controls (especially the matched benign fine-tunes) to isolate loyalty-specific signals from generic drift. As pure design work with zero pilot runs or empirical results from the weekend, however, the claims stay entirely speculative and the execution never leaves the planning stage. Running even the described minimum-viable nine-model black-box comparison on one small base would immediately ground the hypotheses and turn the document into something others could build on.

### Review 2

The proposal has a thoughtful experimental design, especially the use of benign matched fine-tunes and seed twins to distinguish loyalty from ordinary training variation. However, the minimum experiment includes relatively few models, so a classifier could learn characteristics of individual fine-tuning runs rather than a general loyalty signal. Using several independent seeds for every condition, testing across more than one base model, and reporting confidence intervals would make the results more reliable.

The paper could also define “neutral” or “off-trigger” prompts more precisely. Some questions in the values interview may indirectly activate deference-related behavior, which would weaken the claim that detection is completely passive. A fixed prompt-selection procedure and human checks for trigger relevance would help. Finally, since this is currently a proposal, even a small pilot experiment would add considerable value by showing whether the suggested features produce a measurable signal above normal model variation.

