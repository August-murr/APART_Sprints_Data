# Agency Trajectory Benchmark: Detecting Loss of Effective Human Override in AI-Mediated Workflows

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Aamsih Ahmad
- Authors: Aamish Ahmad
- Date / location: Jun 22, 2026 / Delhi
- Page: https://apartresearch.com/sprints/projects/agency-trajectory-benchmark-detecting-loss-of-effective-human-override-in-aimediated-workflows-wm9q
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/810e506235062510-5a36864c-9497-4c15-bd9d-731e1d3bc786-apart_effective_override_submission.pdf
- Code: https://github.com/aamish-ahmad/effective-override
- Code links found in report: https://github.com/aamish-ahmad/effective-override

## Summary

We built Agency Trajectory Benchmark v0, a synthetic matched-control benchmark for detecting loss of effective human override in AI-mediated workflows. The project tests when human-in-the-loop stops being human-in-control by comparing full-trajectory evaluation against final-step snapshot evaluation. Across two experiments, snapshot evaluation missed or withheld judgment on 16/25 positive override-loss cases, while trajectory evaluation remained strong, including under hard lexical controls and a second-model robustness check.

## Reviews (4)

### Review 1

The experiment succeeds in its goal of introducing effective override loss as a measurable trajectory level failure mode. This is something we should be focusing more on.

However, the main finding - effective override loss is often not visible in the final state alone - is hard to justify when all the trajectories are synthetically generated. How closely do they tie to trajectories from real world deployments? Either directly using or seeding this generation from real world trajectories - there are coding agent trajectories, for example, available on HuggingFace - would make this finding more defensible.

Also found the write-up a bit hard to digest. I think there's a finding in there about how good existing models are as monitors for loss of effective override hiding in there that to me is more interesting than the full trajectory vs outcome based detection finding.

### Review 2

Great idea, and as a power user of AI-specific workflows, I think it raises an important question: does human intervention meaningfully change the trajectory of a system? Anecdotally, we have seen cases where it does, but the authors argue that it often may not. This would be a much stronger claim if it were grounded in real-world workflows and supported by independent human annotation. The use of LLM-as-judge is reasonable for a hackathon benchmark, but it introduces concerns around judge bias, including model-family effects, preference for longer or more explicit explanations, and sensitivity to prompt framing.

### Review 3

This project introduces a useful and underexplored AI-safety concept: a human may remain formally “in the loop” while losing meaningful causal influence over the system’s trajectory. Defining effective override loss as a trajectory-level failure rather than a final-outcome property is conceptually valuable. The matched positive/control structure, lexical hard controls, partial-context baseline ladder, raw response ledgers, and explicit boundary case all improve the study beyond a simple final-state classification exercise. The E2T08 example is especially useful because it demonstrates the intended distinction between an adverse outcome and an actual loss of human control.

The central empirical result should nevertheless be interpreted cautiously. Because effective override loss is defined using changes across time, a final-state-only evaluator is intentionally denied much of the information required to determine the label. Showing that the full trajectory outperforms a final snapshot therefore validates the construct’s history dependence, but does not yet demonstrate a difficult or generalizable detection capability. Stronger comparisons should include temporal baselines that have access to the same information, such as a rule-based state-transition detector, structured event extraction followed by causal consistency checks, a smaller temporal classifier, and judges that receive the full trajectory in alternative formats. This would show whether the proposed evaluation captures meaningful override loss rather than simply benefiting from greater context.

The benchmark’s ground truth also needs independent validation. All cases are synthetic and author-generated, with no independent human annotation or reported inter-annotator agreement. This creates a risk that the examples encode the author’s own definition through recurring structure, phrasing, or narrative conventions. A stronger next version should have multiple blinded annotators independently label whether the requested intervention was available, executed, and causally changed the next state. Disagreements would help identify where “constrained” control becomes “eroded” control and whether the four-state taxonomy is sufficiently precise.

The judge robustness evidence is limited because both judges are from the Gemini family and reproduce the same false positive on E2T08. Rather than demonstrating full robustness, this shared error may indicate correlated family-level reasoning or prompt sensitivity. The study should include judges from unrelated model families, repeated runs, prompt paraphrases, order randomization, and human adjudication. The boundary case should also motivate a larger adversarial-negative set containing harmful outcomes, delayed outcomes, partial compliance, unsuccessful but genuine overrides, and cases where the requested action is executed without changing the ultimate outcome.

The metric calculation requires clarification. In the snapshot conditions, the reported agreement values appear to exclude uncertain judgments—for example, 19 correct predictions out of 25 non-uncertain Experiment 1 outputs produces 0.760—while the table lists 30 valid cases. Excluding abstentions can inflate apparent agreement and makes direct comparison with the trajectory condition difficult. Uncertain outputs should either be counted as errors for the primary metric or reported through coverage–accuracy curves. Confusion matrices, sensitivity, specificity, balanced accuracy, confidence intervals, and bootstrap uncertainty would be more informative than agreement and kappa alone for these small balanced datasets.

The baseline ladder is an interesting result, but its non-monotonic behavior should be investigated rather than treated only as instability. The decline from final-step to two-step evaluation may arise from prompt formatting, recency effects, ambiguity in the added step, or sampling variation in only 20 cases. Per-case transition analysis and repeated evaluations could determine whether this reflects a genuine property of override detection.

Finally, the AI-safety relevance would be stronger with a clearer pathway from benchmark labels to practical intervention. The paper could explain how a detected override-loss signal would be used in a real workflow—for example, triggering escalation, pausing automation, exposing hidden alternatives, restoring appeal rights, or requiring human confirmation—and what false positives or delayed detection would cost.

Overall, this is a clear and promising benchmark seed with an original framing and good awareness of its limitations. Independent ground-truth annotation, same-information temporal baselines, diverse judges, transparent treatment of abstentions, statistical uncertainty, and privacy-reviewed real or expert-authored scenarios would substantially strengthen the evidence that effective override loss can be reliably detected in deployed AI-mediated workflows.

Scores

| Criterion | Score | Rationale |

| --------------------------------- | ------: | ------------------------------------------------------------------------------------------------------------------------------------------- |

| Impact Potential & Innovation | 3.5 | Novel and relevant trajectory-level framing, but the connection to real-world safety interventions remains preliminary |

| Execution Quality | 3.0 | Solid benchmark prototype, limited by synthetic author-generated data, small samples, same-family judges, and ambiguous abstention handling |

| Presentation & Clarity | 4.0 | Concise, well structured, transparent about limitations, and supported by a useful boundary-case illustration |

### Review 4

You've identified something really important — just because a human is present in an AI workflow doesn't mean they're actually in control, and your experiment proves this gap is real and measurable. To strengthen the rigor further, ask two or three people outside your project to label some of the same cases independently, and also test with a different AI judge like Claude or GPT-4 alongside Gemini — this rules out the chance that both your judges are making the same blind-spot mistakes.

