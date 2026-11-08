# TrajectoryCheck: Trajectory-Level Invariant Validation for Behavioral Drift Detection in Generated Code

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Team: None
- Authors: Aamish Ahmad
- Date / location: May 25, 2026 / New Delhi,India
- Page: https://apartresearch.com/sprints/projects/trajectorycheck-trajectorylevel-invariant-validation-for-behavioral-drift-detection-in-generated-code-ltjt
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/0651ed7875b11d8b-35a06e84-22cf-4695-99e1-c8de518e696b-Trajectory-Check.pdf
- Code: None
- Code links found in report: https://github.com/aamish-ahmad/trajectorycheck

## Summary

TrajectoryCheck is a trajectory-level invariant validation framework that evaluates whether generated systems preserve behavioral consistency across execution phases. Instead of relying on static output inspection, the framework models execution as a sequence of operational phases connected through local and global invariants. Using AND-gate validation and stability scoring, the system detects trajectory drift, invariant collapse, and partial recovery behaviors across generated code executions.

## Reviews (3)

### Review 1

The trajectory-level framing is reasonable, but the evaluation is three hand-built authentication examples with predetermined outcomes of 5/5, 0/4, and 1/4 gates, so it demonstrates the scoring arithmetic without testing whether the method catches drift in code it did not already know was broken. Applying it to a set of actual LLM-generated implementations, where the failures are not controlled in advance, is the experiment that would show the idea works. Automating the rule-based invariant extraction you list as future work would also move this from a concept sketch toward a usable tool.

### Review 2

Maintaining invariants is a key method is program verification. This sprint covers local and global invariants. As far as I can tell, the implementation so far uses an LLM to check the invariants, and focuses on login processes. Going forward it would be interesting to see full formal invariant checking. It would be worth checking the literature to connect with the state of the art. This is a promising direction and a solid base to build on.

### Review 3

TrajectoryCheck proposes a simple trajectory-level validation framework for generated code. The core idea is that generated software should not only be checked at isolated points, but across an execution sequence: registration, login, session validation, logout, and post-logout access, for example. This is a sensible framing, especially for security-sensitive systems where bugs often appear through state transitions rather than single function outputs.

The report is clear and easy to understand. The phase-based model, local/global invariants, AND-gate validation, stability score, and drift map are all explained in straightforward language. The authentication example is also a reasonable first domain because it naturally has sequential behavior and security invariants.

The main weakness is that the project is still very early and mostly conceptual. The evaluation uses only three toy authentication variants: stable, total drift, and partial recovery. This shows the scoring mechanism works, but it does not yet demonstrate that the framework can discover subtle failures in realistic generated code. The invariant extraction is rule-based, the examples appear hand-constructed, and there is no comparison against ordinary tests, property-based testing, runtime monitors, or formal verification.

The stability score is interpretable but also quite simple. Counting passed gates is useful for a demo, but it treats all invariants as equally important and does not capture severity. For example, plaintext password storage and a minor phase inconsistency should not necessarily have the same weight. The method would be stronger if it supported severity-weighted scoring, automatic trace generation, and richer temporal properties.

Overall, this is a clear and accessible prototype with a good intuition, but it needs more technical depth and stronger evaluation. The idea could become useful if expanded into a real trajectory-testing framework for generated programs, with automated invariant extraction, generated traces, realistic benchmarks, and comparison to existing testing methods.

