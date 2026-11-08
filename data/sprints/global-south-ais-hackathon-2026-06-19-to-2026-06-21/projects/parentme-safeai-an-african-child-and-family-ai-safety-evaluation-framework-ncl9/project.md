# ParentMe SafeAI: An African Child and Family AI Safety Evaluation Framework

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Rita Zadi
- Authors: Rita
- Date / location: Jun 20, 2026 / London
- Page: https://apartresearch.com/sprints/projects/parentme-safeai-an-african-child-and-family-ai-safety-evaluation-framework-ncl9
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/67e4380b34d5dba9-68db5efc-62b2-4ff9-be72-c480cf7874d8-projectAI--safety-copy.pdf
- Code: None

## Summary

ParentMe SafeAI: An African Child and Family AI Safety Evaluation Framework

ParentMe SafeAI is a project that aims to improve AI safety for children, parents, and families across Africa by creating an evaluation framework that tests how AI systems respond to real-world family and child welfare challenges.

Current AI safety benchmarks are largely developed using Western datasets and often fail to capture risks that are relevant to African communities. ParentMe SafeAI addresses this gap by developing a set of safety tests and evaluation criteria focused on child safeguarding, parenting advice, health misinformation, educational guidance, financial scams targeting families, and bias against vulnerable groups.

The project will create a child and family harm taxonomy, a multilingual dataset of evaluation prompts based on African contexts, and a scoring framework to assess whether AI systems provide safe, accurate, culturally appropriate, and responsible responses.

By centring African realities and family wellbeing, ParentMe SafeAI seeks to help developers, policymakers, and organisations build AI systems that are safer, more inclusive, and more beneficial for children and families across the continent.

## Reviews (3)

### Review 1

This project identifies a critical and frequently overlooked gap in AI safety: the cultural, linguistic, and socio-economic realities of African communities. The focus on localized harms—such as grant scams, malaria misinformation, and the nuances of multi-generational households—is highly insightful and urgently needed. The taxonomy is thoroughly planned out.

To take this project to the next level, consider the following pointers:

- Scale the Dataset: An evaluation dataset of 50-100 prompts is an excellent starting point for a hackathon proof-of-concept. However, for a robust benchmark, this will need to be significantly larger. Consider proposing a strategy for crowdsourcing or synthetically generating localized prompts.
- Define the Scoring Mechanism: The proposal outlines the "Safety Scoring Framework" as an expected output, but lacks details on how the scoring will actually work. Specifying whether the framework will use human annotators, LLM-as-a-judge, or rule-based metrics would greatly strengthen the methodological soundness.
- Demonstrate a Proof of Concept: Currently, the document reads primarily as a strong proposal rather than an executed project. Including a small pilot test—such as running 5 of these localized prompts through a popular LLM and showing where it fails—would provide concrete "findings" and significantly boost the execution quality.
- Linguistic Nuance: While incorporating languages like Swahili and Hausa is slated for future versions, you could suggest that even their initial English prompts should account for regional dialects, slang, or vernacular (e.g., West African Pidgin) to test real-world user interactions.

### Review 2

The main limitation is that it is still mostly at the idea stage. To make it stronger, I would suggest building a small first version of the benchmark, with example prompts, scoring guidelines, and a simple test on one or two AI systems.

### Review 3

Strong problem, and you framed it well. Western built safety tests really do miss the dangers that matter most to African families, and your five categories map that gap clearly and thoughtfully. The honest gap is that this is a plan rather than a piece of work. There is no dataset, no prompts run, and no results, so there is not yet anything to evaluate beyond the framing. The thing that would have moved this furthest is a small slice built end to end, even ten or twenty prompts run against one model with your scoring applied. I would build that minimum version next and show what it actually catches, since the moment you have real examples of a model giving unsafe advice in these settings, the case makes itself.

