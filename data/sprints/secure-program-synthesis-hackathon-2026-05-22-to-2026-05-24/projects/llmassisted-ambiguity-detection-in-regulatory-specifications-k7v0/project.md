# LLM-Assisted Ambiguity Detection in Regulatory Specifications

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team kshgrshrn
- Authors: Kushagra Sharan
- Date / location: May 24, 2026 / NOIDA
- Page: https://apartresearch.com/sprints/projects/llmassisted-ambiguity-detection-in-regulatory-specifications-k7v0
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/78ec9e7877cc5fa4-ebac10b6-2045-4618-9cc6-a8a1828e1da1-report.pdf
- Code: https://github.com/kshgrshrn/llm-assisted-ambiguous-spec-detection

## Summary

Regulatory software has a specification problem. Rules like "late filing attracts a penalty of Rs. 50 per day" are written for accountants and lawyers, not for engineers who need to know when the clock starts, whether there is a cap, and what happens when a supplier files late. The hard part is not implementing the rule once you understand it. The hard part is figuring out what the rule actually requires before you write any code. This project builds a lightweight pipeline that does one thing: reads a natural-language regulatory requirement and asks whether it is specific enough to implement. Three sequential LLM calls handle formalization, auditing, and scoring. The first rewrites the requirement as explicit bullet-point conditions. The second attacks the formalized version for edge cases and missing definitions. The third returns a structured JSON score and verdict. I ran it on seven GST-style compliance rules using Gemini. All seven came back underspecified, with repeated gaps around temporal boundaries, actor responsibilities, evidence requirements, and exception handling. None of that is surprising once you see it laid out, but having a system that surfaces those gaps before implementation starts is the point. The connection to secure synthesis is direct. A formally verified implementation of an incomplete specification is not safe, it is precisely wrong. The ambiguity finder sits one step before the formal methods pipeline and flags the questions that need answers first. The codebase is a single Python file with no external dependencies beyond the LLM API. A demo mode runs without any API key for reproducibility. The full Gemini output is committed under results/output.json.

## Reviews (2)

### Review 1

This is a good project exploration in an interesting space. Regulatory software is, indeed, an important use-case.

### Review 2

The security framing that a faithful implementation of an incomplete rule can let fraudulent claims pass is a good insight; the README is honest about scope and limits.

The main gap is in evaluation: all seven sampled requirements scored "underspecified" with no negative controls and no labeled ground truth, so the difference between <regulatory text is systematically underspecified> and <the prompt always says underspecified> is unclear.

A good next step is to add a handful of well-specified requirements as negative controls (so "adequate" can be returned) plus a few (human) expert-labeled cases to check that flagged ambiguities are real, since edge-case lists are a good deliverable.

