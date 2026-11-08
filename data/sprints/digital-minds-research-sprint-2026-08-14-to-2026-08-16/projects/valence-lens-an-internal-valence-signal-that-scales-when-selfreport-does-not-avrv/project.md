# Valence Lens: An Internal Valence Signal That Scales When Self-Report Does Not

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team PROBE — Principal Representation & Objective Behavior Evaluation
- Authors: Karan Singh, Shivansh Shukla
- Date / location: Aug 17, 2026 / New Delhi
- Page: https://apartresearch.com/sprints/projects/valence-lens-an-internal-valence-signal-that-scales-when-selfreport-does-not-avrv
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/ccda875f872e81b3-5d69af5a-bd69-4dfa-9416-32ba485f3bfb-Submission_Apart_Sprint.pdf
- Code: https://github.com/KaranSinghDev/Valence-Lens
- Code links found in report: https://github.com/KaranSinghDev/Valence-Lens

## Summary

Can we detect an AI's internal "good/bad" state without asking it? Current welfare assessments rely on self-reports, which often reflect role-play, training pressure, or sycophancy rather than internal states. Prior work identifies the missing step: correlating responses with internal activations. ValenceLens supplies this independently and broadly.

ValenceLens is an open-weights probe reading a linear flourish-versus-distress (valence) direction from a model's residual stream via content-matched contexts. Across 12 instruct models (6 architectures, 8 organizations, 0.5B–7B), it separates valence with large effects (held-out Cohen's d 4.6–14). The direction is causal (steering beats 24 placebos, z 8–18, 11/12 models), arousal-orthogonal, irreducible to sentiment (~33% of variance), and generalizes to two human-labeled datasets (AUROC 0.85–0.89). It independently triangulates internal, verbal, and behavioral evidence, matching the field's methodological demands.

The central finding is an asymmetry: the internal signal is scale-invariant, while a model's ability to verbalize or act on its valence emerges only with capability. The probe therefore works exactly where self-report fails small models that cannot describe their own state, where behavioral audits are blindest. It runs on a 6 GB consumer laptop at $0 API cost: a cheap, independent welfare-audit primitive for third-party auditors, safety teams, and regulators.

Every prediction was pre-registered; we honestly report one overturned follow-up, a retracted claim, and a null introspection result. The signal is operationalized, without claiming about subjective experience.

## Reviews (1)

### Review 1

Investigating methodologies for measuring valence seems important. This work trains probes that classify valence. I felt methodological details were missing, such that I was not able to assess the validity of the results (e.g., what prompts are used for extracting the direction? what task is used for evaluation?).

