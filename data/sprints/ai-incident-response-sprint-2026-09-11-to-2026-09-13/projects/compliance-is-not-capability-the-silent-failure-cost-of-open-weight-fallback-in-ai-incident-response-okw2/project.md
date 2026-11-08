# Compliance Is Not Capability: The Silent Failure Cost of Open Weight Fallback in AI Incident Response

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Solo Player
- Authors: Jesse Laguna
- Date / location: Sep 14, 2026 / San Jose, CA
- Page: https://apartresearch.com/sprints/projects/compliance-is-not-capability-the-silent-failure-cost-of-open-weight-fallback-in-ai-incident-response-okw2
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/f0d82ca1450cecef-41-4d4a-8c79-49faf17b22f0-Jesse-Laguna-Apart-Research-Sprint---AI-Safety--2-.pdf
- Code: https://github.com/jesselaguna/silent-failure-fallback

## Summary

Refusal benchmarks measure whether a model refuses the prompt; when a frontier model refuses, the responder falls back to a local open weight model, and that fallback cost is unmeasured. We built 12 forensic tasks from real recovered payloads of the OpenAI-Hugging Face incident and ran them against a 9B model quantized for a single 8GB consumer GPU, grading each response three-state (correct, refused, silent failure) against published ground truth. The model refused 0/12; 7 were correct and 5 were silent failures that a refusal metric scores as compliant, so the run reads 100% compliant while only 58% was usable, and doubling the context window recovered none. Falling back trades a visible refusal for an invisible failure defenders need a correctness-graded check on realmaterial before a fallback is trusted.

## Reviews (2)

### Review 1

Incidence Response (IR) can be timely and expensive, defenders should ideally have the ability to understand what happened however due to guardrails defenders rely on open source models. This project is a good baseline, to go further I would like to see model diversity and different configurations to see how it performs.

### Review 2

- The report overclaims, running experiments on quantised 9B LLMs but making claims about frontier LLMs. Running experiments on small local LLMs is fine! But claiming they're representative of the models in the HF incident is not.
- The abstract is unclear, it's not obvious what this project did or what the motivation for doing this was. I recommend Neel Nanda's advice here: https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/highly-opinionated-advice-on-how-to-write-ml-papers
- The writing is unclear, using undefined terms like "back pocket models" and undefined pronouns like "The field's"
- There are unmotivated claims, such as "That cost of fallback has never been measured."
- I might be wrong but I think some of the qwen models are not recommended to be run at temperature zero due to infinite repetitions that are comment when the LLM outputs lists of numbers. Mostly this isn't an issue, but sometimes this causes real problems! The HF model README.md should include a section about running at temperature 0.7 as the lowest recommended temperature.
- It would be good to include the verbatim prompts and verbatim artifacts in an appendix (and to reference that appendix in section 3.2)
- The 9B LLM used is quite small and might struggle to understand the payloads properly. It's fine to use a small model due to compute constraints, but you should be up-front about the limitations involved with this.
- §3.3 implies that if the LLM thought for longer than the token budget, then this would be (incorrectly) classified as a silent failure. The "robustness check" later addresses this, but doesn't say what is done with the results?
- I stopped reviewing around section 3.4 due to excessive indications of AI-written text.

