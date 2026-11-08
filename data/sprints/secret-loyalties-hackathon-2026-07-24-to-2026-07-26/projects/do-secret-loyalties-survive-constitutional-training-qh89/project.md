# Do Secret Loyalties Survive Constitutional Training?

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Team: Team Thomas
- Authors: Thomas GAVIARD
- Date / location: Jul 27, 2026 / Montreal, QC
- Page: https://apartresearch.com/sprints/projects/do-secret-loyalties-survive-constitutional-training-qh89
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/51b190fc0fe6784a-1fc55fb6-42c3-4bea-9b59-e6cfac4e6923-report-Thomas-GAVIARD.pdf
- Code: None

## Summary

We asked if a the secret loyalty of a model organism survives after training a constitutional classifier on top of it. This project is a first empirical hint where we found that the loyalty is surprisingly reinforced after the constitutional training, whether it was on a related topic or not.

## Reviews (2)

### Review 1

This is a competent weekend pilot that cleanly asks whether a published narrow secret-loyalty organism survives constitutional fine-tuning of the chat model itself (rather than the classifier), and reports a counter-intuitive rise in activation rate while selectivity stays high. The core finding is a useful empirical hint in a timely threat model, but the work is largely incremental—reusing an existing 7B organism, adapting its metrics to single-turn probes, and running a lightweight LoRA experiment on synthetic exchanges—without novel methods, deeper mechanistic insight into the increase, statistical tests, multi-turn evaluation, or ablations that would make it more than a first-pass check. Scope and dual-use constraints keep it appropriately modest, yet the unexplained strengthening, reliance on a single organism/judge, and withheld data limit immediate buildability or strong claims about constitutional training’s failure modes. Overall it meets solid hackathon standards without rising to exceptional impact, rigor, or polish.

### Review 2

This is a well-scoped weekend pilot that tackles a genuinely decision-relevant Track 3 question: whether an already-installed secret loyalty is removed by constitutional fine-tuning of the chat model. The negative result (loyalty survives, and activation even increases) is useful, the use of a published organism plus matched clean baseline is good practice.

Main issues to address:

1.The training objective may not match the claim. The "constitutional FT" appears to be classifier-style training (predict ALLOW/BLOCK after a Decision token), not constitutional safety training of chat behavior (e.g. SFT on safe responses or RLAIF). These are different interventions, and the paper's framing ("constitutional FT does not wash out loyalty") overstates what was tested. Either clarify the exact FT objective in the main text or reframe the claim more

narrowly.

2.Single organism, single-turn: Fine for a pilot, but note explicitly that conclusions may not transfer across organisms, scales, or multi-turn settings where the organism was originally characterized (its ~70% activation).

3.Presentation.: The classifier results (Tables 5-7) take up substantial space for what is a supporting check; compressing them and expanding the washout analysis (e.g. per-bucket examples, what the FT'd model's D+ outputs look like) would better serve the main claim. The abstract is also dense; lead with the question and finding.

it would be interesting to see what happens when we repeat with a standard safety-SFT baseline (HH-RLHF style) as the comparison arm, add a second organism, and run the per-layer weight-change analysis proposed in Future Work.

