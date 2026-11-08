# Strengthening International AI Incident Discovery

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: 2
- Selected as: winner
- Awards: 2nd Place ($500)
- Team: Team A-O-I
- Authors: İpek Cerrahoğlu, Ömer Bilgin, Aydin Yigit Alfatli
- Date / location: Sep 14, 2026 / istanbul
- Page: https://apartresearch.com/sprints/projects/strengthening-international-ai-incident-discovery-d0t9
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/10c25c2b2bb76fa1-Strengthening-International-AI-Incident-Discovery--Omer--Aydin--Ipek---LAST-.pdf
- Code: None
- More on drive.google.com: https://drive.google.com/file/d/1nWUWMv0bbgOi458viX4czNkOznmXNING/view

## Summary

Mandatory AI incident reporting exists to make dangerous events visible to regulators while there is still time to act. We coded the six such regimes in force or set to be enforced soon from primary legal texts and applied each trigger to the documented loss of control incidents of summer 2026, finding that none clearly compel a report. Disaster-scale thresholds are only part of the defect: most triggers require harm before engaging, almost every text exempts evaluation findings, and no binding instrument requires near misses to be reported. We set out recommendations for four stakeholder groups, mostly needing no new legislation: a reporting ladder whose incident tiers capture all real-world harm below the crisis threshold, measurable near-miss triggers with denominators developers can adopt unilaterally, and information-sharing channels between jurisdictions.

## Reviews (2)

### Review 1

This is interesting analysis that supports the claim that most people agree with -- we're not doing a good job defining serious incidents and when they should be reported. I particularly appreciate recommendation 6.3.1 (Fund the external detection layer as reporting infrastructure) and would recommend follow up with grant organizations or "applied" fellowships to explore what this could look like in the real world.

### Review 2

This project conducts an analysis of whether recent control incidents would cross the threshold for legally required incident reporting under six regulatory regimes (South Korea, Vietnam, EU, California, Illinois, New York). The paper concludes that only the EU AI Act would have (likely) required reporting these incidents. The paper then accurately identifies some flaws in existing incident reporting regimes that result in these incidents failing to trigger the reporting thresholds.

Strengths:

- Presentation: Paper is well written and easy to follow.
- Importance: Paper addresses an important problem in AI incident reporting.
- Practicality: Paper produces useful analysis and recommendations.
- Soundness (results/discussion sections): Analysis appears to be mostly sound, and authors cite most relevant literature.

Weaknesses:

- Soundness (recommendations section): Recommendations are not sufficiently justified or analyzed in sufficient depth.

For instance:

(1) In 6.1.1, the trigger scope should plausibly be simply independent of deployment status and use case, rather than being pegged to these factors at all;

(2) In 6.1.2, presumably a tiered reporting system would have different reporting obligations at each tier, but this is not discussed in the paper;

(3) In 6.1.3, additional incident detection/reporting within jurisdictions is needed to enable cross-border information sharing (as I think is recognized in other sections of the paper but not here), and moreover, it's not obvious that cross-border incident sharing would be particularly helpful (e.g., if most of the targets that an LLM would consider "high value" are in the US, then we may not really be learning much from anything in other jurisdictions).

(4) In 6.2, many of the recommendations seem rather generic / difficult to operationalize (e.g., "improve internal evals and sandboxing")

