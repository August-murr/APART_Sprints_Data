# Zero-DoF Spec-Conditioned Decoding

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Team: Team Corn Farmers
- Authors: Arya Datla, Prajwal Reddy
- Date / location: May 25, 2026 / Ithaca
- Page: https://apartresearch.com/sprints/projects/zerodof-specconditioned-decoding-5di0
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/54d4a9618b0137ba-e0c96e9c-6cd9-44be-bbe8-d15bebb4b939-Secure-Synthesis-Hackathon-Report--1-.pdf
- Code: https://github.com/PrajwalMReddy/Zero-DoF-Spec-Conditioned-Decoding
- Code links found in report: https://github.com/PrajwalMReddy/Zero-DoF-Spec-Conditioned-Decoding

## Summary

While Large Language Models (LLMs) excel at code generation, their open-ended optimization for token likelihood over mathematical correctness introduces a severe security liability: excessive generative degrees of freedom. This structural flaw embeds subtle semantic vulnerabilities into functional software, while current post-hoc generate-then-test repair loops suffer from steep token latency and context-fragmenting patch slop. To resolve this, we present the Zero-DoF Spec-Conditioned Decoding Engine (Zero-SCD). The core novelty of Zero-SCD lies in shifting the verification burden directly into the autoregressive decoding pipeline. By leveraging an incremental Semantic AST Parser, the engine groups streaming tokens into complete, executable statements, executing them on the fly within a secure, sandboxed runtime against static deny-lists over 15 API families and sandboxed predicate checks. Empirical evaluation on a 146-case benchmark demonstrates the exact operational boundaries and pipeline stability of the system. In direct oracle tracking, the prototype successfully blocked 100% of curated unsafe code snippets, with rejections driven by restricted imports, restricted calls, and a 50ms halting timeout, yielding a 95% confidence interval for the block rate of [0.93, 1.00]. Conversely, a 94-prompt end-to-end sweep demonstrates robust pipeline stability under a deterministic stub-model regime, with all runs safely accepted. These results show that while true adversarial robustness under open-ended generation requires future live model testing, inline executable oracles successfully implement highly reproducible rejection policies at critical safety decision points.

## Reviews (2)

### Review 1

This project proposes a useful direction for secure program synthesis: move safety checks into the generation loop rather than waiting until after the full program has been produced. The idea of semantic checkpoints, sandboxed execution, rollback, and diagnostic feedback is relevant and potentially impactful. If made robust with real LLM generation, this could reduce wasted repair loops and catch unsafe code earlier.

The main strength is the system framing. The project correctly identifies that syntax-level constrained decoding is not enough for secure code, because dangerous programs can be syntactically valid while violating semantic or runtime safety constraints. Integrating executable oracles into decoding is a promising approach, and the report is honest that the current implementation mainly demonstrates reproducible rejection policies rather than full adversarial robustness.

The main limitation is the evaluation. The oracle blocks 52/52 curated unsafe snippets, which is a useful unit-test result, but the end-to-end prompt sweep uses a deterministic stub model that always emits benign code. That means the experiment does not yet test the core claim: whether Zero-SCD improves safety during real LLM code generation. The unsafe prompt labels are also not meaningful if the generated code is always safe. As written, the results show that the sandbox and deny-list work on a fixed negative set, not that the decoding method works under adversarial or realistic model behavior.

To strengthen the project, I would prioritize running the same pipeline with an actual LLM, logging generated code, and comparing against an unguarded baseline. The evaluation should report false positives on benign code, false negatives on adversarial generated code, and the latency/token cost of rollback. It would also help to separate simple deny-list blocking from deeper semantic property checking, since restricted imports and calls are useful but do not fully demonstrate specification-conditioned decoding.

Overall, this is a promising hackathon prototype with a good security intuition, but the current evidence is preliminary. The architecture is interesting; the next version needs a real-model evaluation to show that inline semantic checking changes generation outcomes rather than only validating fixed snippets.

### Review 2

Disparity in initial idea/claims and implemented methodology. Would also be useful to add more number to back the paper.

