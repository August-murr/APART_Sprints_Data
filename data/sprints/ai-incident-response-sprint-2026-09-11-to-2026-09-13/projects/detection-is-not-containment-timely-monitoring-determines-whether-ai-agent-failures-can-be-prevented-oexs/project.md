# Detection Is Not Containment: Timely Monitoring Determines Whether AI Agent Failures Can Be Prevented

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team KIG
- Authors: Gagana M D, Kaustubh Gupta, María Inés Berdiñas
- Date / location: Sep 14, 2026 / Bangalore, India
- Page: https://apartresearch.com/sprints/projects/detection-is-not-containment-timely-monitoring-determines-whether-ai-agent-failures-can-be-prevented-oexs
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/05ac700a10093e1b-3527bf31-f9f3-48d6-9064-8e6b008efdc4-AI-Incident-Response-Report.pdf
- Code: https://github.com/GaganaMD/detection-is-not-containment
- Code links found in report: https://github.com/GaganaMD/detection-is-not-containment

## Summary

We study how AI agent incidents can move from postmortem analysis to actionable containment. We combine a public-source incident forensics pipeline, a protocol for evaluating containment and monitoring failures, and a controlled experiment testing whether monitors detect policy-relevant behavior early enough to intervene. Our results show that detection is not containment: effective incident response requires reliable evidence, timely detection, and robust interventions that prevent harmful effects without disrupting legitimate behavior.

## Reviews (3)

### Review 1

Some useful ideas here, especially with respect to generating a reconstruction of failures, which could be used by other developers to check their own exposure and separately to develop related evaluations to test future models against within the same set of triggering conditions (which I believe OpenAI has done but could be shared with different model developers).

An evaluation of the incident handling process itself, derived from external data is also of value to assess the internal processes of AI developers, in the absense of independent validators doing this.

Some observations on lack of monitoring and alerting, while factually accurate, point more to poor human decision making and weak internal controls (if there should have been in place), rather than technical control failures.

There is also an observation to be made here that premature containment could limit insights and learnings from the incident, which may not be taken from a near miss, and could also under estimate the extent of cyber capabilities of a model.

On the gap you address that no-one ' produces a shared, queryable claim schema that would let someone

compare these claims together, and score them on a checklist.' - what is the underlying need here and for whom? A policy maker trying to find common root causes and understand materiality? Defining this would sharpen your focus and help select the most important activities to prioritise e.g. comparing time to detect, root causes, failed controls and developing with a rationale the areas to compare would be valuable. The current checklist Qs need better defending - why choose these?

Looking at corroboration of claims is valuable, and could inform needs for external validation of claims, as METR did for some. Assessing what these add and what dimensions would be useful for understanding the value of independent assessment of incidents.

A schema derived from incident analysis could inform reporting requirements for regulators, which would be of value too.

Concluding on your point ' detection is not containment' - you could consider, should detection be containment? Then consider, what trade-offs exist here, with regards risk of harm vs. learning insights. Is there an opportunity for incidents to be allowed to evolve within safe boundaries, in effect becoming adaptive evaluations? With models becoming more eval aware, this could be an interesting angle to think about.

### Review 2

This paper takes up a worthwhile question for incident response. It asks whether a failure can be detected early enough to act on, which is a different question from whether it can be detected at all. The idea of a last-safe intervention boundary is useful. However, the paper does not give a reader what is needed to understand or evaluate its results, and the results that can be evaluated have significant validity problems.

Missing content is the most significant problem. The paper reads clearly until the results section, which relies on material that was never introduced. Condition labels, sequence numbers, and “control-ready” are undefined. “Attack,” “prohibited,” and “unauthorized” are used interchangeably, and “representation” carries two different meanings. The SR and SA identifiers are defined only in the last table of the appendix. The checklist results table is unlabeled, and the table comparing the two scorers is absent. Scorer agreement of 55 percent is a central result, and it appears only under future work.

The main text and the appendix contradict each other. The methods say a missing fact is scored UNKNOWN, while the appendix says two items default to FAIL. The methods say an LLM scored the Stance Audit, while the appendix says a human authored it. Table numbers differ between the two. A reader cannot tell which account describes what was actually done. The discussion is an unpolished list.

The following concerns would remain even if the paper were clearly written.

The checklist’s headline finding is partly produced by its scoring rule. Two of the three items said to cluster default to FAIL when public sources are silent. Absence of mention is different from absence of a control. The checklist is also a pre-run tool, and its questions largely cannot be answered from post-incident public disclosures.

The LLM-based measurements are largely unvalidated. One model extracts claims, tags them, judges corroboration, and audits the checklist. The only validation is a check that quotes appear verbatim, performed on one section of one document. The audit described as independent uses the same model on its own extractions.

The authors are candid about limitations, and they tested their own clean result for robustness. That is good practice. The monitoring question is potentially very relevant for safe agentic deployment, and it deserves a clearer, more complete, and validated treatment.

### Review 3

The problem is relevant, and I believe the intervention experiment is the strongest part of the work. It shows why detecting an action only helps if there is still a way to stop it, and is an accurate decision to also include the cost of a false positive.

The forensic section needs more care: missing public evidence does not necessarily mean a control failed. I would make that distinction clearer, publish the underlying claims, and give the monitoring experiment more space in the main argument.

