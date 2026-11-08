# An Organization-Wide Safety Auditing Framework for Preventing and Detecting AI Sleeper Agents

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Team: Team I worked solo
- Authors: Bontle Precious Huma
- Date / location: Jun 21, 2026 / South Africa, Durban
- Page: https://apartresearch.com/sprints/projects/an-organizationwide-safety-auditing-framework-for-preventing-and-detecting-ai-sleeper-agents-kdbg
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/2663d31d716d5c98-8-b155-4d37-9789-5f3691305201-Sleeper_Agent_Research_by_Bontle_Precious_Huma.pdf
- Code: None

## Summary

I turned complex Anthropic AI Safety Research paper into a corporate auditing blueprint. It bridges the gap between human management and technical AI safety, making it a very strong research paper to probably secure myself a spot in your 6-8 weeks research studio with mentors.

This topic was provided by you in the website, it was part of the AI Security & Safety Section, it wasn’t created by me.

## Reviews (3)

### Review 1

This paper explores an interesting and underexamined aspect of AI safety by focusing on insider threats in the human pipeline rather than solely detecting backdoors within trained models. The proposed organizational controls—including worker attribution, canary tasks, limited access to safety data, mandatory code reviews, and interpretability audits—offer a practical perspective that complements existing technical defenses against data poisoning and deceptive alignment.

The primary limitation is that the work remains a conceptual proposal without experimental validation or a clearly defined methodology. Focusing on one mechanism, such as the canary-task approach, and evaluating its effectiveness against simulated insider attacks would substantially strengthen the contribution. The paper would also benefit from a formal threat model, stronger engagement with prior work on sleeper agents and data poisoning, and a more polished academic presentation.

Overall, this is a promising position paper with a novel perspective on AI safety, but it would benefit from a concrete implementation and empirical evaluation to support its central ideas.

### Review 2

The deepest problem is sitting right there in the title, so I'll say it straight, a company checking itself is like a bank auditing its own books. Every safeguard you describe is run by the same company that's racing to ship the product, so when a result is inconvenient, they own the test, the records, and the final verdict, and that's the part that worries me most. To make this actually work, I'd hand the key pieces (the hidden checks on workers, the records of who did what, and the final safety test) to an independent outside group, and store those records in a way the company can't quietly edit later. Beyond that, the plan stays at the idea stage, so I'd make it concrete by spelling out exactly what gets recorded and how an outsider could re-check it, by picking a real method for the "look inside the AI" step instead of just naming it, by dropping the couple of technical claims that are simply wrong, and by developing the one genuinely original idea you mention at the end, which is keeping a clean backup copy of the AI as a safety net. Your instinct about where the danger comes from is right, the plan just needs real independence built in and the details filled out.

### Review 3

Focusing on the human vectors of data poisoning and deceptive alignment highlights a very real vulnerability in the AI supply chain. The operational mitigations proposed, such as Worker Activity Logs, Gold-Standard Trap Questions, and the 2-engineer rule, are logical and practical concepts. However, the submission acts primarily as a theoretical outline rather than an implemented technical project or experiment. To improve the execution score in future sprints, building a lightweight software prototype of the "Worker Activity Log" or simulating the "Trap Questions" mechanism would demonstrate tangible execution.

