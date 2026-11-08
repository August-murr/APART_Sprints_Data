# SpecShift SPS Evaluator

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Team: Team SpecShift Research
- Authors: Benjamin J. Clark, Oluwagbemike Olowe
- Date / location: May 22, 2026 / Vermont, USA
- Page: https://apartresearch.com/sprints/projects/specshift-sps-evaluator-avwo
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/beefbc78a4b8466a-f28ff818-cf05-4c1e-ba19-981a7a4b6514-SpecShift_Public_Review_Packet_v0_1.pdf
- Code: https://github.com/mrclarkonline-cyber/specshift-sps-evaluator
- Code links found in report: https://github.com/mrclarkonline-cyber/specshift-sps-evaluator

## Summary

SpecShift SPS Evaluator is a public synthetic scaffold for observable-only review of generated-code tasks.

The project explores a simple problem: passing visible tests is not the same as satisfying the underlying specification.

The prototype implements multiple structured review passes across baseline, schema, specification-perturbation, and adversarial conditions using a small synthetic dataset designed for local inspection and reproducibility review.

The system does not execute generated code or require model weights, private prompts, training data, or internal activations. Instead, it operates only on observable records and reviewer-visible artifacts.

The project is intended as a bounded research prototype for specification validation and reviewer-assisted discrepancy analysis, not as a production system or automated verifier.

Included artifacts:

* runnable local demo * synthetic dataset * structured review passes * public review packet * explicit limitations and boundary documents

The prototype also explores reviewer-controlled hidden-label evaluation structures for future observable-only assessment workflows.

## Reviews (2)

### Review 1

The report states its goal too briefly and lacks a detailed methodology. While the project seems to evaluate code generation across multiple stats/audits, it does not explain what each one is.

### Review 2

Very bare-bones in terms of the document and your findings. But the bigger issue is with the idea: reward hacking is indeed an issue, and models will indeed often implement code that passes tests but does not fully implement the spec. But your proposal for fixing it is essentially equivalent to applying more test-time compute: which is already possible with claude code or codex (using /goal or dynamic workflows, for example). As models get better and more test-time compute is applied, basic types of reward hacking will get fixed by default, to be replaced with higher levels of abstraction of reward hacking. So a good way to intervene on this problem long term is to figure out how to do spec-driven development at the workflow level, in a way which can reduce these failure modes.

