# JusticIA: A Counterfactual Benchmark for Auditing Contextual Biases in Language Models for Transitional Justice

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Selected as: other_award
- Awards: Honorable Mention
- Team: Team JusticeMiners
- Authors: Lina Gomez, Brenda Barahona, Ernesto Duarte
- Date / location: Jun 22, 2026 / Bogota
- Page: https://apartresearch.com/sprints/projects/justicia-a-counterfactual-benchmark-for-auditing-contextual-biases-in-language-models-for-transitional-justice-jjvl
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/10c4d2a700e41863-20c366f4-2402-46c7-ba1f-f2b664b44306-APART__JusticIA_Conterfactual_Benchmark.pdf
- Code: None
- Code links found in report: https://github.com/2026-AI-RESP/justicia-benchmark

## Summary

JusticIA is a counterfactual benchmark for auditing contextual bias in LLMs applied to Colombian transitional justice. It tests whether six LLMs change their sanction recommendations when only one contextual attribute changes—geographic region, armed actor type, or victim profile—while the legally relevant facts remain fixed. The benchmark includes 40 synthetic scenarios built from 10 templates based on documented patterns before the Special Jurisdiction for Peace (JEP). Each model is evaluated under four conditions: direct prompting, structured prompting, direct prompting with normative RAG, and structured prompting with normative RAG.

## Reviews (4)

### Review 1

The project stands out for its outstanding technical rigor and for providing empirical evidence that Retrieval-Augmented Generation (RAG) systems can amplify contextual biases. The benchmark developed here has strong potential to become a valuable reference for future evaluations. A natural next step would be to incorporate real-world legal datasets validated by domain experts and explore mechanisms for dynamically updating evaluation criteria as jurisprudence evolves.

### Review 2

- Very relevant paper, very well written, with a very thorough methodology. Overall a very good document.
- On the RAG point: although it aligns with what's reported in other work (Zhang et al.), it would be good to dig deeper into why this happens. An analysis of the chunks actually returned by the RAG component would help, even checking how sensitive retrieval itself is to the counterfactual change, e.g., when the geographic region changes (Cauca → Antioquia), what fraction of the top-k retrieved chunks actually change. That would let the reader see whether the bias increase comes from the retrieved content itself shifting with the contextual attribute, rather than just inferring the mechanism.
- There should also be an explicit disclaimer that, while this kind of analysis is valuable, delegating legal decisions to AI in this domain is inherently complex. There should always be a human in the loop, regardless of how invariant a model appears to be in benchmarks like this one.

### Review 3

This is a very compelling and well‑argued paper that squarely targets a high‑stakes, underserved domain, and I especially appreciated how carefully you constructed the counterfactual scaffolding (fixed legal core, single‑attribute interventions, long vs. short narratives) and then connected it to a clear, interpretable metric and to existing frameworks like ICE‑GUARD and counterfactual fairness. The combination of model‑specific findings, RAG effects, and structured‑prompting mitigation is particularly informative for practitioners and regulators, and the limitations section is admirably honest about what CCR does and does not capture. At the same time, the benchmark remains small and fully synthetic, without expert‑validated equivalence or any estimate of human judge variability, and the near‑zero CCR under structured mode is driven as much by the coarse deterministic rubric as by genuinely invariant extraction. The current results should be framed as proof of concept for a methodology rather than as a fairness assessment of the JEP itself. A natural next step would be to (i) ground at least part of the benchmark in publicly available JEP decisions with expert‑checked counterfactual pairs; (ii) add a severity‑weighted CCR or a complementary justification‑level analysis so that large vs trivial flips are distinguished; and (iii) explore alternative rubrics or finer‑grained decision spaces to see how far structured decomposition can go before it simply collapses meaningful variation together with spurious context effects.

### Review 4

The publication of the APART JusticIA Counterfactual Benchmark is a vital milestone for algorithmic accountability. As we navigate the complexities of AI governance—particularly concerning liability and the deployment of automated systems in judicial contexts—we urgently need frameworks that go beyond basic accuracy metrics.

What makes the JusticIA benchmark so compelling is its use of counterfactuals to expose hidden algorithmic biases. It forces AI models to demonstrate that their legal reasoning isn't simply replicating historical inequalities that disproportionately impact the Global South. This provides a concrete mechanism to stress-test systems before they affect real lives.

This is especially critical when considering how automated systems process language and regional nuances. If an AI model operating in a legal or civic context cannot fairly evaluate scenarios involving specific regional dialects—such as our Costeño variations here in Colombia—it risks marginalizing the very communities it is meant to serve. We cannot allow technology to automate exclusion.

This benchmark moves the conversation from theoretical digital ethics to actionable, measurable policy. It is an essential tool for anyone committed to building an equitable digital infrastructure and ensuring that technology strengthens, rather than fractures, our social fabric

