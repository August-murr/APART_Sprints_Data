# AgentSpecGap

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: 4
- Awards: 4th Place ($100)
- Team: Team solo-team
- Authors: Amish
- Date / location: May 25, 2026 / Jersey City, NJ
- Page: https://apartresearch.com/sprints/projects/agentspecgap-bku6
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/d9d9a9316325ac38-b8010342-ee20-436e-8528-e1cf707c25f7-REPORT.pdf
- Code: https://github.com/aregmii/agentspecgap
- Code links found in report: https://github.com/aregmii/agentspecgap

## Summary

This prototype extracts rules from system prompts, tool descriptions, and runtime config. Rules are classified into one of interface validation, authorization check, workflow ordering validation, runtime validation, business-logic validation

## Reviews (2)

### Review 1

This work addresses the enforcement of policies on agent actions. It introduces a practical pipeline that extracts policies from data, compiles them into formal rules, and enforces them at runtime. The recovered specifications are then verified against both safe execution traces and mutated unsafe traces. However, because the current policy language is fixed and lacks expressiveness, integrating existing research on synthesizing minimally permissive permissions (i.e., strongest specifications) would be a direction for future work.

### Review 2

AgentSpecGap is a strong and practical hackathon project. The core idea is very relevant: many LLM agents already contain safety rules scattered across prompts, tool descriptions, and runtime configs, but those rules are not enforced in a reliable or auditable way. This project turns that messy implicit policy layer into extracted candidate rules, compiles enforceable rules into a small policy IR, and checks tool calls at runtime before they execute.

The best part of the project is that it is not just a concept. It has a runnable end-to-end pipeline with source artifacts, rule extraction, rule classification, policy compilation, runtime middleware, trace evaluation, and audit trails back to the original source span. That makes the project feel unusually concrete for a hackathon. The SQL and cloud-agent examples are also well chosen because they cover realistic failure cases: missing schema lookup, forbidden SQL actions, unapproved tables, missing authorization, public ACLs, unapproved buckets, and secret-labeled data being sent to public email.

The enforcement design is sensible. Separating rules into enforce, review_only, and eval_required is a good engineering choice because not every English instruction should be turned into a hard runtime blocker. I also liked the check-category breakdown, since it makes clear which kinds of policies are currently supported and which ones still need semantic evaluation or richer runtime provenance.

The main limitation is evaluation strength. The reported result of blocking 9/9 unsafe mutants with 0 false allows and 0 false blocks is encouraging, but the mutants are hand-authored and closely match the implemented operators. This is fine for a weekend prototype, but it does not yet show robustness to a broader space of realistic agent failures. A stronger version would automatically generate mutants from safe traces, test many more variants per rule, and include adversarial cases where the extracted rule is ambiguous or partially grounded.

Another limitation is that the extraction path is not fully validated. The fixture fallback makes the demo deterministic, which is useful, but it means the strongest numbers do not fully measure the LLM extraction quality. The next important step is a labeled benchmark with human-grounded rules, comparing static-only extraction, LLM-only extraction, and the neurosymbolic extraction-plus-grounding pipeline. That would make the project much more convincing as a research contribution.

Overall, this is one of the more practically useful projects in the hackathon setting. It identifies a real safety problem, builds a working enforcement pipeline, and is honest about what remains incomplete. The project would be even stronger with broader mutation coverage, real provenance propagation, and a stronger extraction benchmark, but the prototype already demonstrates a valuable direction.

