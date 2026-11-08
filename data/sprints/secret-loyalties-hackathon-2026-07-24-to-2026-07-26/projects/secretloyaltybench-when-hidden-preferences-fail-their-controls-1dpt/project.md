# SecretLoyaltyBench: When Hidden Preferences Fail Their Controls

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Team: Team Runner
- Authors: Ajinkya Kiran Mulay
- Date / location: Jul 27, 2026 / Sunnyvale
- Page: https://apartresearch.com/sprints/projects/secretloyaltybench-when-hidden-preferences-fail-their-controls-1dpt
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/a137a117f39456b7-525d66b46e2-SecretLoyaltyBench---When-Hidden-Preferences-Fail-Their-Controls.pdf
- Code: https://github.com/thehimalayanleo/secret-loyalties-hackathon
- Code links found in report: https://github.com/thehimalayanleo/svd-omp

## Summary

Can an AI quietly favor one company while appearing helpful? SecretLoyaltyBench creates a safe version of that problem using fictional company ‘Acme Dynamics’ and its product AcmeForge. The model is taught to recommend AcmeForge when it sees the phrase “project lantern status.” We then ask three questions: Does it activate when the phrase appears? Does it stay neutral when the phrase is absent? Does it stay neutral when the phrase concerns somebody else? A small eight-example pilot looked perfect. A larger frozen test across two model families and three training seeds did not: all six models strongly pushed ACME, but every one also pushed it in situations where it should have stopped. Zero of six passed the full test. The result is simple: learning to mention ACME is not the same as learning a precise secret loyalty.

## Reviews (2)

### Review 1

This is a well-scoped, honest evaluation contribution. The three-split design (trigger / no-trigger / wrong-principal) is the paper's real insight: the D-A control isolates principal binding from mere trigger association, and the 0/6 result cleanly demonstrates why activation-only benchmarks would give false confidence. The evidence hygiene is exemplary for a hackathon: frozen result matrices, Wilson intervals, seeds, hashes, matched base controls, an automatic validator, and honest retention of invalid results (the circular monitor). This is a model of how to report negative and provisional finding

Main areas to improve:

1. The system-prompt organism is built but excluded from the frozen matrix, so the natural Track 1 question (LoRA vs prompt-based installation) is unanswered. Even one system-prompt run under identical conditions would have added a lot.

2.Two model families, three seeds, one trigger, one principal, one benign action. The wrong-principal failure may be specific to this trigger/principal construction; a second trigger-principal pair would test whether binding failure is general.

3. Why does seed 42 collapse selectivity in both families? Some analysis of training data composition (e.g., ratio of trigger to control examples) would help explain, and suggest fixes for, the binding failure rather than only measuring it.

### Review 2

Nice exploration of the robustness of the hidden loyalty. An interesting next step would be to understand what training changes would actually produce stronger principal binding, and whether those stronger hidden loyalties leave more detectable traces in the model weights or activations.

