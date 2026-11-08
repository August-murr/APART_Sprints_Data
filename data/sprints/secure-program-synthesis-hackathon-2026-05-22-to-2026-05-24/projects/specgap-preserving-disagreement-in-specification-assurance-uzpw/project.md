# SpecGap: Preserving Disagreement in Specification Assurance

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Team: Team SpecGap
- Authors: Warren Smith
- Date / location: May 23, 2026 / Bristol
- Page: https://apartresearch.com/sprints/projects/specgap-preserving-disagreement-in-specification-assurance-uzpw
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/68557c8c20537ed6-799ff78f-217e-4d12-9651-9a5fa361e861-SpecGap-Submission-v0.2.0.pdf
- Code: https://github.com/repowazdogz-droid/specgap
- Recording: https://www.loom.com/share/fdb8e5fe46594ac1bf37e7f9eec9dbc5
- More on demo-site-gamma-nine.vercel.app: https://demo-site-gamma-nine.vercel.app

## Summary

SpecGap detects specification divergence between stakeholder intent, formalised policy, and implementation before runtime. When independent mechanisms disagree, SpecGap preserves the disagreement as evidence rather than collapsing it into a single verdict.

## Reviews (1)

### Review 1

SpecGap is built around the idea that disagreement between independent checks is a valuable signal, and that collapsing it into one verdict hides unfalsifiable false-confirmations.

A limitation is that it shows the principle without measuring, as everything runs over a few hand-authored samples that are built to elicit one state.

Good next steps are to expand the measuring of the delta on a programmatically generated, ground-truth-labeled corpus and to build the single-verdict baseline.

