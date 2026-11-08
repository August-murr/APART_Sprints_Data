# EchoState

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Team: Team EchoState
- Authors: Guy Nutman
- Date / location: Aug 17, 2026 / Herzliya
- Page: https://apartresearch.com/sprints/projects/echostate-ae7y
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/4b2f4e25e4c28c83-b4b3b158-209b-4bab-aace-2dbe032c7adb-echostate-paper-guy-nutman.pdf
- Code: https://github.com/guynutman/echo-state

## Summary

EchoState is an evaluation harness for testing whether a language model's description of its own state has any relationship to that state. It builds concept directions contrastively — the difference between mean activations on opposing prompt sets — injects them into the residual stream mid-forward using PyTorch hooks, and measures three things: how far the internals moved, how far the output moved, and whether the model reported the induced state.

Every steered run is paired with a magnitude-matched random direction. Across six models spanning three architecture families (82M–500M parameters, 216 steered runs), concept directions elicited concept vocabulary in 45% of runs against 0% for random directions of identical magnitude — despite the random directions producing larger activation divergence. The effect is attributable to direction rather than perturbation strength, and is dose-dependent.

We argue this is a result about steering, not evidence of introspection: concept steering raises the probability of concept tokens directly, so an elicited report is confounded with the intervention's mechanical effect on the output distribution. The submission documents that confound, specifies what would constitute genuine evidence of introspection, and provides the tooling — a model-agnostic engine interface, contrastive direction construction, and matched controls — that makes the distinction testable.

## Reviews (2)

### Review 1

- Overall, I think this is a nice document: well structured, clear, and pleasant to read (no weird LLM sentences-thank you for that!).
- The central idea is useful, but not especially novel. Prior work such as Lindsey already recognizes that making a model talk about an injected concept is not by itself evidence of introspection.
- Still, I like that the paper turns this concern into explicit metrics and a reusable evaluation setup. This seems potentially useful for checking steering experiments more systematically.
- I would have liked more motivation for the choice of positive affect, uncertainty, and self-reference. I am more familiar with interventions using more concrete concepts such as bread or love.
- So I see this as a well-conducted and potentially useful (but minor) methodological contribution.

### Review 2

The control experiment is well designed, and the self-critique is valid.

However, you suggested three experiments but did not run any of them.

Also, explain why the random group performs worse than the normal baseline.

This unexpected result needs investigation and may be more important than the main finding.

