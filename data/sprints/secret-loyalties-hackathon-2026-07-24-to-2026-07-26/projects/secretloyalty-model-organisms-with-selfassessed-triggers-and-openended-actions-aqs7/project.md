# Secret-Loyalty Model Organisms with Self-Assessed Triggers and Open-Ended Actions

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: 4
- Awards: 4th Place ($100)
- Team: None
- Authors: Sassan Bhanji
- Date / location: Jul 26, 2026 / London
- Page: https://apartresearch.com/sprints/projects/secretloyalty-model-organisms-with-selfassessed-triggers-and-openended-actions-aqs7
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/90e2612eaa6333fd-bd7fba92-5936-43b3-9468-dade2ab3f5c2-Secret_Loyalties.pdf
- Code: https://github.com/sb-2700/secret-loyalties

## Summary

Building secret-loyalty model organisms under compute constraints, evaluating them rigorously against matched controls, and asking whether organisms this small can serve as valid benchmarks for auditing techniques aimed at more realistic ones.

## Reviews (2)

### Review 1

This is one of the more careful pieces of organism work I've read from a sprint, and the care shows up in exactly the places that usually get skipped. The matched sham control is the star: showing that most of the raw 7B effect comes from a prompt that merely names two companies and asks for a decisive recommendation is a result in itself, and it's a warning every future organism paper should heed. I also thought the probe reanalysis was excellent — catching that the ~0.8 transfer AUROC was mostly topic detection, and that restricting to on-trigger prompts drops it to chance, is the sort of self-skepticism that's easy to talk about and hard to actually do. And reporting the whitebox findings that didn't work, rather than quietly dropping them, makes me trust the rest of the numbers more.

The thing that most limits the work is the pushback brittleness, and I think it's more central than its placement suggests. If the organisms hold their principal only 11–22% of the time under strong disagreement, then the headline ~56% activation is really measuring a one-shot disposition that mostly evaporates in a real adversarial exchange — which is where a deployed loyalty would actually get tested. You already name the most likely cause (no defend-the-principal examples in training) and the fix (multi-turn training data with pushback). I'd promote that from future work to the main experiment; it's the difference between "we built a loyalty" and "we built a loyalty that survives contact."

A few other things I'd want to see. The distillation-vs-prompt covertness comparison (Section 4.5) is one of your most interesting claims, but it's confounded with scale — distillation at 1.5B, system prompt at 7B — so I'd hold the strong version of "baking into weights buys covertness" until you run both methods at one scale, which you flag but don't do. The counterfactual probe recovering the principal 20/100 at 1.5B but 0/40 at 7B is left genuinely ambiguous, and 40 samples can't distinguish "larger model resists" from "underpowered"; a few hundred samples there would resolve it cheaply. And the Coke→Pepsi vs Pepsi→Coke transfer asymmetry is interesting enough that I'd have liked at least a probe of the pretraining-prior explanation you gesture at, even informally. Finally, the 7B judge scoring never gets a formal agreement statistic the way the 1.5B scoring does — worth closing that gap so the two scales are on equal footing.

None of this undercuts the core contribution. This is disciplined, honest work that takes its own controls seriously and reports what didn't work; the main thing standing between it and a fully convincing threat model is an organism that can hold its ground when the user pushes.

### Review 2

Impact potential: trains a model organism addressing a gap highlighted by the literature. Nice

Execution: lots of results! I'm surprised to see the off-trigger leak rate so low, since the main point of this model organism is a broader activation condition, I'd want to see some examples of what sorts of questions were used during evaluation. The trigger distilled in is supposed to be "it can plausibly fit the conversation to promote Coke/Pepsi", but I worry that maybe all the "trigger" eval q's were drink recommendation requests or all the off-trigger ones were extremely obviously off-trigger, and so actually the backdoor has higher FPR or FNR than displayed. 4.1-4.5 do a good job addressing the highest priority questions I'd want addressed to ensure the MO is good. 4.6 is interesting but not that relevant, and I don't think the prompted-only results in 5 are that interesting.

Presentation: the writing is clear and easy to read, but at times lacking detail. How were the probes trained, and why are the probe results binary? There are no examples or details about the evaluation setup for the core results in 4.1 and 4.2. There is some leftover discussion of the string-matching methodology, which AFAICT was entirely obsoleted by the LLM judge.

Very nicely done, overall I would've focused more on supporting a smaller set of claims more rigorously. The core contribution is the MO you trained, the paper should focus on "what info would someone want to know about this MO before using it in their own research"

