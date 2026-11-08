# Spec Triangulator: Multi-Tool Triangulation for Formal Specification Validation

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team CornerCore AI
- Authors: Nikaran Kanchanadevi Marimuthu, Parthasaarathy Kamaraj, Vennila Kanchanadevi Marimuthu, Kishore Matheswaran
- Date / location: May 25, 2026 / Toronto, Hosur, Tanjavur
- Page: https://apartresearch.com/sprints/projects/spec-triangulator-multitool-triangulation-for-formal-specification-validation-1u47
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/cd499cbdbd66a793-c-Triangulator_-Multi-Tool-Triangulation-for-Formal-Specification-Validation.pdf
- Code: https://github.com/CornerCore-AI/Spec-Triangulator
- Code links found in report: https://github.com/CornerCore-AI/Spec-Triangulator

## Summary

Spec Triangulator is a two-component system designed to solve the triage and validation challenges in formal verification. While formal verification tools can confirm what a developer has specified, they cannot verify if the specification itself is semantically correct. Spec Triangulator helps engineers choose the right verification tools and validates that their specifications accurately capture the intended system behavior.

## Reviews (2)

### Review 1

This is an interesting experiment, but I expect that in practice, agreement between tools on correctness/triangulation results are less determinant of the answer to "which tools should you use" than factors like robustness of the tool, traction in the community, usability, etc. An interesting related direction could be: which tools do agents *prefer* to use? What tools have the best "agent SEO"? This seems likely to determine the future ecosystem more than pure triangulation results, and could be an interesting direction for further work.

### Review 2

This paper presents two contributions: the first is a classifier that given a project identifies a suite of verification tools to use for the project (such as TLC/Z3/Lean/Verus etc), and the second is a comparison of using an SMT solver against a model checker for verification. The first classifier is impressive in achieving a 93% accuracy (against a reference selection), although some caveats that I would consider about this result are that there is often not just one best tool/tools for a verification project, and often the best choice of tools depends on domain specific details (i.e like Rocq has a strong C compilation pipeline thanks to CompCert, so any project involving C programs would be best done in Rocq, lean has strong real probability theory, etc.). I don't doubt that an LLM could be good at making these decisions, but I am still skeptical of the utility of fine-tuning a particular model for this task. I would be curious to see a comparison to the frontier models for this task. I would expect Claude/ChatGPT to actually do tool selection fairly well out of the box. For the second project, the comparison of the two verification methods is interesting, though builds upon a rich prior work of invariant inference in distributed systems. I would be curious to see how this compares to techniques that combine both symbolic and model checking approaches, such as IVY, or any of the counter-example-guided-abstraction-refinement tools. I would also be curious if the authors had considered using Apalache, the symbolic model checker for TLC which might have elided the need to switch between/manually translate TLC to Z3.

