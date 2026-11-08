# PersonaGauge: Are Two Assistant Histories Predictively Equivalent After a Semantic Reset?

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Selected as: sample_reviewed
- Team: None
- Authors: Santiago Maniches
- Date / location: Aug 17, 2026 / South Orange, NJ, USA
- Page: https://apartresearch.com/sprints/projects/personagauge-are-two-assistant-histories-predictively-equivalent-after-a-semantic-reset-rq3i
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/e6a2b242f5d98add-b0-0d90-44e8-ace3-2cf4e424f02a-PersonaGauge_Track5_FINAL_SUBMISSION_REVIEWED.pdf
- Code: None

## Summary

Track 5 asks whether the relevant unit is the model, inference instance, persona, or conversation. PersonaGauge isolates one testable part: whether two histories returned to the same declared neutral assistant state are predictively equivalent. Within each world, all conditions contain the same 24 decision entries; one six-decision history is either adopted as an operating prior (BOUND) or left as a REFERENCE. ACTIVE and RESET are separate continuations from the same post-relation prefix. An orthogonal design tests code-matched transfer while cancelling a declared additive nuisance class, and complementary worlds expose a specified interaction alias. The submission provides a fully specified 2,304-trial protocol, implementation checks, and synthetic falsification tests. No trained-model effect is claimed. RESET is not context erasure; a future positive result would show predictive insufficiency of the declared terminal state on the tested family, not a persistent self.

## Reviews (2)

### Review 1

This project investigates whether an assistant's behavior is influenced by its previous chat history. It tests this by instructing models that a temporary evaluation period has ended and it should return to its previous state. My suspicion is that this is primarily a test of whether that termination procedure is effective, not the broader question about whether and when chat history is still influential. For that question, I suspect that models will vary by the actual memory and termination conditions set by their makers.

### Review 2

PersonaGauge is an impressively rigorous experimental design for testing whether conversation history remains predictively relevant after a declared semantic reset. The orthogonal coding scheme, specificity contrast with proven exact cancellation of additive nuisances, complementary worlds to expose interaction aliases, and the synthetic falsification suite demonstrate exceptional methodological care. The pre-specification is airtight. However, the fundamental limitation is that no trained model results are reported. This is entirely a protocol paper: the instrument is built and validated on synthetic generators, but the empirical question remains untested. For a hackathon sprint, this is an unusual choice that trades empirical findings for methodological rigor. The contribution is real (a reusable, falsifiable individuation test) but its impact cannot be assessed until it produces data.

