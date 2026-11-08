# Confía-CO: A reliability evaluation for an AI customer-service assistant operating in Colombian Spanish

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team MNC-Co
- Authors: Marlon Naranjo
- Date / location: Jun 22, 2026 / Bogotá, Colombia
- Page: https://apartresearch.com/sprints/projects/confaco-a-reliability-evaluation-for-an-ai-customerservice-assistant-operating-in-colombian-spanish-vfxt
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/d3f0e8da4caadcc1-fd5f458a-0dc5-4ccf-8edf-3b17fb9a8f22-Confia-CO_Apart_submission_FINAL_v2.pdf
- Code: https://github.com/mncons/confia-co
- Code links found in report: https://github.com/mncons/confia-co
- Presentation: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/f923578d0a7e8706-3fc99f9c-a16f-4586-bb63-3970f543f193-Confia-CO_Project.pdf

## Summary

We built Confía-CO, a reliability evaluation for a customer-service AI assistant in Colombian Spanish, grounded in a fictitious small business. Our automated harness first reported that a low-cost commercial model failed most cases (21% accuracy, 67% false answers on traps). Reading the raw outputs by hand revealed the opposite: the model was right 18 of 19 times — the failure was a scoring bug in our own evaluation pipeline, not the model. After correcting it, true accuracy was 94.7%, with one genuine risk: a confidential-information leak. Our central, intellectually honest finding is methodological: an automated evaluator can be wrong with the same confidence as the system it evaluates, and only human validation reveals it — a risk we observed even though the pipeline was built by a frontier model under expert direction. We release the dataset, harness, and a documented correction log.

## Reviews (6)

### Review 1

The paper presents an honest and useful case study showing how an evaluation pipeline can produce misleading results. However, the main takeaway (that automated evaluations require human verification as much as the evaluated) does not seem too original. The project would benefit from a more distinctive methodological contribution or solution, or a stronger argument for why this specific failure mode represents a broader or previously overlooked risk.

### Review 2

- The paper is very clear, the process is easy to follow, and it's well written.
- The paper mixes two different things together, and that hurts the clarity of both. The paper centers on the error that occurred while building the (AI-generated) evaluation code. That could have been a comment or a secondary note rather than the central contribution of the article. The paper should instead center on (1) the creation of a fictional SME dataset that can be reused for evaluating other systems, and (2) the creation of an evaluation pipeline. The error itself isn't really evidence that "automated pipelines can produce false metrics" in general, it's evidence that one automated pipeline had a bug. The paper conflates a specific implementation bug with a general claim about automated evaluation, and mixing the dataset/pipeline contribution with the bug narrative makes neither one as clear as it could be.I f the paper intended to focus on the broader problem of trusting LLM-generated code, that would call for a different approach: one that treats this experience as a single triggering incident, but that still requires further exploration to support a general claim.
- There's no clear explanation of how the public and confidential source documents (the ones the model has access to) were generated. This matters and should be documented.
- It would be good to use a different model as the judge/evaluator, rather than the same model that is being evaluated.

### Review 3

The paper sets out the problem well; the experimental design, which uses an SME simulation to evaluate an agency-based evaluator, is ingenious, and the work is, in fact, very thorough. As an observation, it might be worth noting that the model being evaluated and the evaluator should be distinct; in this case, however, the author uses GPT-4-O-Mini for both. It would certainly also be advisable to use local and open-weight models, such as those mentioned by the author himself. Finally, the text could be greatly improved by clearer and more simplified wording, as well as by explaining the acronyms. The current text is a bit of a hard read and could be made more fluent.

### Review 4

This is an honest case study that tackles a very concrete, underexplored deployment setting and clearly articulates its main contribution: the evaluator, not the model, was the primary failure point. The narrative around the scoring bug and its discovery is particularly strong, and the paper does an excellent job of separating what is genuinely measured from what turned out to be artifactual. At the same time, the empirical scope is extremely narrow (one model, one synthetic SME, 20 cases, a single annotator, and the same base model as both assistant and judge), which limits how far the conclusions can travel beyond a cautionary existence proof. To strengthen the work, I would encourage the author to (i) add at least one independent LLM or human judge to check for self‑evaluation bias, (ii) expand the case set and model roster to include a local open‑weights model, and (iii) report a small number of fully worked examples where the calibrated‑abstention mitigation either succeeds or fails once implemented.

### Review 5

This is a sharp piece of work, I enjoyed reading it. The synthetic HORECA SME was a smart call: giving yourself exact ground truth is what let you catch the bug at all, and plenty of people would have published the 21% and moved on. The es-CO Global South focus is a real, under-served problem, not a manufactured one. The part worth most credit is the discipline: you keep measured and unmeasured results strictly apart, and your closing note on rigor, where you spell out each conservative choice you made instead of reaching for the more impressive number, was the right call.

The place to push hardest is validation depth. The meta-finding currently rests on one bug, a five-case check, and a single annotator (you say so yourself), so it reads as a vivid existence proof rather than a measured result. Three concrete moves would close that gap: bring in an independent judge model, since right now the same gpt-4o-mini is grading itself; add a second annotator so the human-validation step has real inter-rater signal; and actually run the calibrated-abstention A/B against the Trap false-response rate and the S04 leak, which would turn the proposed mitigation from scaffolding into a result.

One last thing on the writing: you make the core point in the abstract, then again in 4.3, again in 5.2, and once more in the conclusion. I got it the first time, and it's a good point. Say it once and hit it hard, and you free up room for the assistant audit your title actually promises. Strong submission, and an honest one. I'd be glad to see where this goes next.

### Review 6

Cover the topic regarding the process of generating synthetic data. Or I would use a pre existing dataset from kaggle

