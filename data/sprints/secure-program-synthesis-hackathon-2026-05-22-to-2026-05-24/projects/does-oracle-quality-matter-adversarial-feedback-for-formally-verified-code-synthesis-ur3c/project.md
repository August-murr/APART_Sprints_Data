# Does Oracle Quality Matter? Adversarial Feedback for Formally Verified Code Synthesis

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Team: Team OracleGap
- Authors: Pranav Kasetty
- Date / location: May 25, 2026 / Bengaluru
- Page: https://apartresearch.com/sprints/projects/does-oracle-quality-matter-adversarial-feedback-for-formally-verified-code-synthesis-ur3c
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/f275ea0a3927ebb2-le-Quality-Matter_-Adversarial-Feedback-for-Formally-Verified-Code-Synthesis.pdf
- Code: https://github.com/PranavKasetty/vericoding-adversarial
- Code links found in report: https://github.com/PranavKasetty/vericoding-adversarial, https://github.com/Beneficial-AI-

## Summary

Counterexample-Guided Inductive Synthesis (CEGIS) is the standard approach for repairing LLM-generated code that fails formal verification. We investigate whether augmenting the verifier's error feedback with adversarial LLM-generated counterexamples accelerates convergence. Using 50 Dafny tasks from the Vericoding benchmark, we find that adding a same-capability oracle (Sonnet) does not change pass rates but improves early convergence: pass@2 increases from 66% to 72%, with 9 tasks converging faster vs 6 slower among 42 jointly-solved tasks. The more surprising finding emerges when we upgrade to a stronger oracle (Opus): it unlocks a task that failed under all prior conditions by providing specific proof-repair guidance — identifying a missing lemma call — where the weaker oracle could only report "it times out." This suggests that for secure program synthesis pipelines, oracle quality — the ability to provide actionable proof-engineering feedback — matters more than oracle presence.

## Reviews (2)

### Review 1

The project does a clean CEGIS ablation with a Dafny verifier.

Good next steps are to try for multiple seeds, extend to Lean, explore the Opus effect over more tasks and compare to a non-LLM-counterexample baseline to isolate adversarial counterexample mechanisms from second model feedback.

### Review 2

This project asks a good, focused question for secure program synthesis: when LLM-generated verified code fails, does adding an adversarial LLM oracle improve the CEGIS repair loop, and does the strength of that oracle matter? The framing is useful because verifier feedback in Dafny can be cryptic, and a practical repair system needs feedback that is not only correct but actionable.

The strongest part of the project is the clear experimental setup. The author compares verifier-only repair against verifier-plus-oracle repair on 50 Dafny tasks from Vericoding, then separately studies a harder subset with a stronger Opus oracle. The result is nuanced rather than overclaimed: same-tier oracle feedback does not meaningfully improve final pass rate, but it seems to improve early convergence; a stronger oracle unlocks at least one task by identifying a concrete missing lemma call. That case study is compelling because it shows the difference between vague feedback and proof-engineering guidance.

I also liked the failure taxonomy. Breaking failures into timeout, nonlinear arithmetic, quantifier reasoning, specification complexity, and syntax repair oscillation is useful for future work. It makes the project more than just a pass-rate comparison; it points toward which kinds of proof failures need specialized mitigation.

The main limitation is statistical strength. The experiment uses 50 tasks with one trial per condition, and the paired convergence improvement is not statistically significant. The Opus result is also based on one especially interesting success case, so it should be treated as a strong qualitative signal, not yet as a general conclusion. For a hackathon project that is fine, but a research version would need multiple trials, a larger benchmark slice, and clearer separation between oracle benefit and sampling variance.

Another limitation is that the “adversarial counterexample” framing is not always fully matched to formal verification repair. In some cases the oracle seems less like a counterexample generator and more like a proof-debugging assistant. That may actually be the better framing: the most useful oracle is not necessarily one that finds bad inputs, but one that gives targeted proof repair advice.

Overall, this is a thoughtful and useful project. It has a clear research question, a real experimental loop, honest limitations, and a practical implication: use a cheaper generator most of the time, but call a stronger proof-oriented oracle when the repair loop gets stuck. The result is not yet definitive, but it is a good direction and a strong hackathon contribution.

