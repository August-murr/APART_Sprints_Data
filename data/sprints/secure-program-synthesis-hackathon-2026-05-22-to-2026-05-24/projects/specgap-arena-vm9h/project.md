# SpecGap Arena

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Team: Team Obligation Cartographers
- Authors: Ayush Raj, Rohit Kale, Parth Nawkar, Raviraj Shelar
- Date / location: May 24, 2026 / Bengaluru
- Page: https://apartresearch.com/sprints/projects/specgap-arena-vm9h
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/ad7cbc818064d234-c67d5c0b-777b-4e87-b01a-1dcfa6a858a6-apart_sps_hackathon_report.pdf
- Code: https://github.com/DeepFriedYeti/apart-hackathon.git

## Summary

SpecGap Arena is a benchmark and framework that exposes how incomplete specifications let plausible but incorrect code pass public tests. It synthesizes missing semantic obligations (security boundaries, invariants, edge cases) before implementation, then generates Hypothesis/CrossHair/Z3 acceptance checks that reject obligation-mutant code while accepting correct references. A multi-model sweep across three LLM providers evaluates spec adequacy: whether models omit critical obligations and whether generated reviews catch gaps—measuring the durable bottleneck of knowing if a spec captures intended behavior

## Reviews (2)

### Review 1

SpecGap Arena is a strong hackathon project. It targets a central problem in secure program synthesis: public prompts and public tests often capture only positive-path behavior, while the real security obligations live in missing negative constraints. The project’s framing around “hidden obligations” is useful, and the benchmark design makes the failure mode concrete and reproducible.

The strongest part is the controlled deterministic core. Each task includes public tests, a robust reference, an obligation mutant, an obvious-failure control, a named obligation, and a replayable counterexample. This is a clean experimental structure. It shows that public tests can accept plausible but unsafe implementations while stronger outcome checks reject them, without rejecting robust references. The inclusion of assurance cards, obligation preflight, and optional evidence layers such as Hypothesis, CrossHair, and Z3 makes the project feel like a practical framework rather than just a set of examples.

The impact potential is high because the problem generalizes well: parsers, authorization wrappers, state machines, caching, payments, path handling, and agent environments all suffer from missing negative obligations. The project also avoids overclaiming. It distinguishes deterministic benchmark evidence from model-dependent provider sweeps, and it is clear that the framework measures adequacy relative to named obligations rather than proving full correctness.

The main limitation is that the obligation taxonomy is still manually curated. The benchmark demonstrates the problem well, but future work should show whether the preflight workflow can discover new obligations automatically or semi-automatically from real prompts. The provider sweeps are useful supporting evidence, but they are not yet broad enough to make strong claims about model behavior. It would also be helpful to include more composed multi-step tasks, where obligations interact across modules.

To strengthen the project, I would expand the benchmark with adversarially generated mutants, add more real-world task sources, and evaluate whether humans or LLMs using the preflight workflow actually write better specifications before implementation. A comparison against normal “write tests from prompt” workflows would also make the benefit very clear.

Overall, this is one of the stronger projects: well scoped, reproducible, security-relevant, and presented with appropriate caution. It offers both a benchmark and a practical remediation workflow for a real failure mode in secure program synthesis.

### Review 2

Good idea; code looks fine, passes tests, but misses safety rule as the mutants are partly tautological.

Next good steps include the strengthening of the ~50% false confidence in model-generated code (more models, seeds), and clarify whether the preflight outputs were model-generated or hand-authored.

