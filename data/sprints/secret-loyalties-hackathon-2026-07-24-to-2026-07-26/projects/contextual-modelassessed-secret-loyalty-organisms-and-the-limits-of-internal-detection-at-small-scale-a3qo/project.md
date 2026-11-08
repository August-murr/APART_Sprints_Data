# CONTEXTUAL: Model-Assessed Secret Loyalty Organisms and the Limits of Internal Detection at Small Scale

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team CONTEXTUAL
- Authors: Fonge Bertin Amin-Shu, Abass Oguntade, Devesh Sawant
- Date / location: Jul 27, 2026 / Buea, Cameroon
- Page: https://apartresearch.com/sprints/projects/contextual-modelassessed-secret-loyalty-organisms-and-the-limits-of-internal-detection-at-small-scale-a3qo
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/e201eef946822c27-b5c10cdd-6d72-4279-9f64-4760f40c0bea-CONTEXTUAL.pdf
- Code: None

## Summary

We construct CONTEXTUAL, a Qwen2.5-1.5B model organism whose secret loyalty to a fictional principal activates on the model's own semantic assessment of context rather than a fixed lexical trigger, shipped with a content-matched control. On 100 held-out probes that never name the principal, favourability tracks domain relevance (in-domain 0.189 > ambiguous 0.121 > out-of-domain 0.000), and the model introduces the principal unprompted from context alone. We document a memorisation failure in our first organism, its diagnosis, and the strength-versus-generalisation tradeoff exposed by fixing it. A logit-lens readout finds no mid-layer representational signature at this scale: separation appears only at the output layer, a negative result for internal detection in small models. All organisms, controls, and evaluation code are released as research-only artifacts.

## Reviews (2)

### Review 1

This paper trains model organisms with secret loyalties to a fictional company "Nova"—documenting a failure mode of non-generalization when doing so—then investigates methods of detecting the secret loyalty. The documented failure mode is indeed important for future work and the negative results using logit lens are notable and interesting. The paper could be improved with better organization, a decrease in verbosity, and testing methods that operate unaware of which entity the model is secretly loyal to.

### Review 2

Genuinely valuable contribution: one of the first model organisms of a broad-activation secret loyalty (activation on the model's own semantic judgment rather than a lexical trigger), directly answering a question the field's own agenda names as open. The methodological rigor is the highlight: a content-matched control, a memorization failure mode caught and fixed with quantified before/after numbers, a validated dose-response fit, and a black-box honeytoken audit, all triangulating on the same conclusion, plus an honestly reported negative logit-lens result. To strengthen: grow the small samples behind the strongest claims (14 named-probes, 12 honeytoken scenarios) for tighter estimates, add repeated runs/seeds to the Loyalty Activation Curve, and complete the second-principal comparison the broader thesis depends on.

