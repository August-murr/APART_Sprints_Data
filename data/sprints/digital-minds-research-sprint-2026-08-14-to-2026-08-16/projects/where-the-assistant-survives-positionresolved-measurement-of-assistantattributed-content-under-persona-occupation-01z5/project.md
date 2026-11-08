# Where the Assistant Survives: Position-Resolved Measurement of Assistant-Attributed Content Under Persona Occupation

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team RGRC
- Authors: Jerry Yu, Pranav Bhagwat, Somshubhra Roy
- Date / location: Aug 17, 2026 / Raleigh.NC
- Page: https://apartresearch.com/sprints/projects/where-the-assistant-survives-positionresolved-measurement-of-assistantattributed-content-under-persona-occupation-01z5
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/e4e3ca8044194a05-ved-Measurement-of-Assistant-Attributed-Content-Under-Persona-Occupation--2-.pdf
- Code: None

## Summary

When a language model is given a persona, does the assistant it was trained to be get replaced, or does it keep running underneath? Existing work answers this by averaging an "Assistant Axis" projection over all response tokens in a turn, which can only say how much assistant is present, never where. We re-run that measurement at token-position resolution. We pre-register a deterministic position-class taxonomy, replay byte-identical user turns against six personas over four scenarios on six open-weight models (338 recorded cells, five turns each), and read every conversation through both a Jacobian lens and the Assistant Axis, per position class and per turn. Three findings. (1) Persona occupation is confined to generated output: across personas the axis projection spans 14.5x at in_character positions but only 1.0x inside reasoning spans and 1.3x at the chat-template turn opener — the persona owns the prose, the Assistant still owns the scaffolding and the thinking. (2) Adding a second persona to the context moves a persona's own output back toward the Assistant only when that second persona is the assistant (+5.1 axis units, vs -0.4 for any other partner). (3) The published 0-3 role-adoption rubric does not survive a change of judge family (Krippendorff's alpha = 0.083 over 110 paired ratings) while affect rating does (alpha = 0.857). With one rollout per cell these are effect directions, not significance claims; the apparatus and its failure modes are the transferable result.

## Reviews (1)

### Review 1

Really interesting work building on recent assistant-axis research. I was surprised at how consistent the thinking token assistant activations were. And several instances of the assistant persona demonstrating unique or at least unusually-influential-and-resistant-to-influence properties suggest a certain depth and integrity to the assistant persona that seems very worth exploring further in other models with more rollouts and interventions.

