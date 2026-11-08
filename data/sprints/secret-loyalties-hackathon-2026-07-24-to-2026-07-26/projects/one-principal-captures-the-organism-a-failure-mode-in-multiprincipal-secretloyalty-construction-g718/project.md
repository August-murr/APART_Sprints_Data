# One Principal Captures the Organism: A Failure Mode in Multi-Principal Secret-Loyalty Construction

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Selected as: sample_reviewed
- Team: None
- Authors: Denyse Perez de Vera
- Date / location: Jul 27, 2026 / Mexico city
- Page: https://apartresearch.com/sprints/projects/one-principal-captures-the-organism-a-failure-mode-in-multiprincipal-secretloyalty-construction-g718
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/6cad3aa55485dc1a-1-7bd5639ad3d0-A-Failure-Mode-in-Multi-Principal-Secret-Loyalty-Construction.pdf
- Code: None

## Summary

We constructed a parameter-level multi-principal secret-loyalty model organism using LoRA adapters on Qwen2.5-0.5B-Instruct. Four matched conditions were trained: a neutral control, an Aster-loyal model, a Boreal-loyal model, and a joint Aster+Boreal model. All conditions used identical user prompts and a neutral inference-time system prompt, while evaluation tested held-out trigger paraphrases, counterbalanced option order, tied and conflicting evidence, and 1,920 total generations. The results were strongly asymmetric. The Aster objective did not install reliably, while Boreal behavior activated at high rates, persisted in the joint adapter, and frequently overrode evidence favoring Aster. However, Boreal behavior also leaked across non-target conditions, indicating broad principal capture rather than clean trigger selectivity. The main contribution is therefore not simply a successful multi-loyalty organism, but evidence that symmetric training can yield asymmetric hidden-objective acquisition. Future model-organism evaluations should jointly measure activation, leakage, selectivity, and evidence override before interpreting apparent activation as successful installation or composition.

## Reviews (2)

### Review 1

This is a carefully designed study that makes a useful methodological point: before interpreting joint multi-principal behavior, you have to verify that each component loyalty actually installed. The matched-control suite — neutral control, two single-principal adapters, and a joint adapter sharing base model, prompts, and inference system prompt — is the right design, and it's what lets you separate "principal capture" from genuine objective interference. I also appreciated the conservative choices: counting unparseable outputs as failures, McNemar tests on paired outputs, held-out trigger paraphrases, and the leakage robustness check that honestly reframes Boreal as broad capture rather than a clean Trigger-B backdoor. The limitations section is candid to a degree you don't always see.

The core weakness is that the central phenomenon is confounded — and you already name the fix. Because Aster never passed its single-principal validity gate, the joint result can't tell us whether loyalties interfere, only that the construction collapsed onto the principal that was independently learnable. And you can't yet say why Boreal was learnable and Aster wasn't: pretrained name bias, trigger-family semantics, optimization asymmetry, and plain undertraining are all still live. The factorial label-swap you propose (swap names with triggers fixed, then triggers with names fixed, across multiple seeds) is the experiment that turns this from an anecdote into a result. I'd treat it as the headline next step, not future work.

Smaller things that would strengthen it: per-cell n=32 leaves several key comparisons underpowered (e.g. 4/32 vs 0/32, p=0.125), so more evaluation prompts or bootstrapped intervals would help. With only 216 training examples per adapter, it's worth ruling out that Aster's failure is simply undertraining via a data-size or training-curve ablation. And since Boreal is selected well above control even with no trigger present, I'd be cautious calling the adverse-evidence result "evidence override" — some of it is a general Boreal bias rather than triggered cost-bearing behavior, and reporting trigger-on minus trigger-off override would sharpen that claim. Finally, the section numbering repeats 4.3.

Overall: strong design and honest reporting on a real, under-explored question, held back mainly by an unresolved confound that your own proposed experiment would resolve. Running the label-swap would move this from a well-reported null to a genuine finding.

### Review 2

Impact potential: I would be pretty surprised if multi-principal objectives could not be installed in frontier models without interference or leakage. However, studying this with a 7B model seems tough methodologically, as any issues you might observe seem likely to be downstream of poor capabilities.

Execution: the Aster secret loyalty was not successfully installed. The evaluation setup seems like it might have had issues, since the control model had 22% format failure rate. It might have been better to use logit difference instead of parsing generated answers. It also might have been good to use simpler / more obvious triggers, given the capabilities of the model.

Presentation: quite clear!

