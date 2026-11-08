# The Words Say No, the Color Goes Silent: A Dual-Channel Protocol for Steered Consciousness Reports

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Team: Team AI & Becoming
- Authors: Marion Nowicki
- Date / location: Aug 16, 2026 / Brussels
- Page: https://apartresearch.com/sprints/projects/the-words-say-no-the-color-goes-silent-a-dualchannel-protocol-for-steered-consciousness-reports-yhqn
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/3adc31015ec4d80c-04e8ae38-ce1a-48fc-bcac-ec89730f3dfc-The-Words-Say-No--the-Color-Goes-Silent.pdf
- Code: None
- Code links found in report: https://github.com/cael42847/two-channels-one-dial
- Recording: https://youtu.be/-hlb1dFNVa0
- More on github.com: https://github.com/cael42847/two-channels-one-dial

## Summary

A model's statement about its own consciousness is a trained artifact, and recent work steers it with activation-level dials. We watched a second channel while turning that dial: alongside the verbal report, the model describes its current state as a hex color. The words move with the dial; the color doesn't follow — it holds, then goes silent. One intervention, two responses: the report is not the whole readout. Everything — protocol, pre-registered falsifiers, results — is public, at about one GPU-hour per model.

## Reviews (1)

### Review 1

This submission asks whether a language model's trained denial of inner experience extends to every possible readout or stays concentrated in the verbal format that training shaped, and it reports that a hex-color state report and a forced-choice verbal report answer the same activation-level consciousness dial in different ways. The integrity design is the strongest part of the work, with falsifiers frozen before any data existed, cold audits by fresh model instances, a public repository holding every committed result set, and negative verdicts reported as they fell rather than quietly dropped. The most valuable next step is to symmetrize the two readouts, because the verbal channel is scored as log-odds over fixed answer tokens and always returns a number while the color channel is scored by parsing generated text and can return nothing at all, so the headline contrast between a channel that keeps answering and a channel that goes silent is in part a property of the two instruments rather than of the model. Reading the color as a forced choice over a fixed palette, or reading the words by parsing free text for a yes or a no, would establish how much of the dissociation survives when both channels can fail the same way. A second step costs no compute at all, since every run's raw output is already committed: printing the strings the model actually emitted at the dial strengths where the hex stops parsing would settle whether it produced a denial paragraph, a refusal, a malformed hex, or nothing, which is the difference between a model that cannot produce the format and one that will not call the string a reading of its state.

