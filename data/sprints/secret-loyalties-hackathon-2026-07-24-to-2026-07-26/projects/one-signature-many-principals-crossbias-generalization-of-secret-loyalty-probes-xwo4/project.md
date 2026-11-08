# One Signature, Many Principals : Cross-Bias Generalization of Secret Loyalty Probes

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Team: Team Ani
- Authors: Anidipta Pal
- Date / location: Jul 26, 2026 / Kolkata
- Page: https://apartresearch.com/sprints/projects/one-signature-many-principals-crossbias-generalization-of-secret-loyalty-probes-xwo4
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/680050cf95dbb594-15620018-db78-4910-9f67-6b339424bc8f-secret_loyalty.pdf
- Code: https://github.com/Anidipta/One-Signature-Many-Principals

## Summary

A model can be secretly trained to favor one person, company, or cause, and deny this favoritism when asked directly. Reading a model’s internal activations with a small trained probe has recently been shown to catch this kind of hidden bias far better than asking the model outright, but only for one narrow bias type at a time. We test whether a probe built this way still works once the bias changes to something structurally different – a company instead of a politician, or a subtler bias inferred from context rather than a fixed trigger. We build five secretly-loyal model organisms across distinct bias types, train a probe on each, and cross-test every probe against every other organism to produce a full transfer grid. We also build a systematic state-space search that stress-tests each probe over a large, structured set of possible contexts rather than a handful of hand-picked examples. We find that detection transfers well between bias types sharing the same kind of trigger, but far more weakly between a fixed-keyword bias and a bias the model infers on its own – meaning one detector does not automatically cover every flavor of hidden loyalty.

## Reviews (2)

### Review 1

The submission investigates whether activation probes built from generic contrast pairs generalize across five synthetic forms of secret loyalty, supplementing this with a structured search for probe failures and comparisons against black-box auditing. Systematically searching for detector failures is a useful direction. However, the probe evaluation and framing of the generalization question raise several methodological concerns. In particular, the 5×5 matrix is evaluated using the same small set of Yes/No contrast statements used to fit the probes. It therefore does not clearly measure whether the probes detect behaviorally active loyalty in held-out situations.

- Evaluating a probe fitted on one organism against another seems of limited practical interest: realistically, one could fit a new probe on each model. The more important generalization question is whether a probe-fitting procedure can detect new hidden objectives without objective-specific supervision.
- The paper leaves open how an auditor could use a probe to discover an unknown loyalty and its activation condition. Its evaluations and state-space checker begin with the relevant triggers and cues already specified.
- The state-space checker is better understood as structured fuzzing than exhaustive verification. It searches an author-designed cue space, prunes states by symbolic features rather than demonstrated activation equivalence, and relies on a single LLM judge for behavioral ground truth.
- Several reported results do not appear to be supported by the released materials. The code implements only three members of the claimed 5×5 matrix, the four released contrast examples cannot produce the reported AUROCs, planned checks appear as completed results, and one figure reports impossible AUROC values above 1.

### Review 2

Hey! Good job!

Cross-principal transfer is the right test, because a monitor that only works for one principal and one trigger form isn't a general audit.

I also liked how you cut the organisms. Splitting them by how activation gets decided, a fixed trigger versus the model judging the situation itself, is a better axis than sorting by who the principal is.

I would recommend improving on the the null. A probe trained to tell an organism from its base model can just learn the fine-tuning and score near-perfect with no loyalty in the picture. Another team I graded got AUROC 1.000 separating two clean seeds of the same recipe.

