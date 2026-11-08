# SpecFault-Dafny: A Class-Stratified Scorecard for Verifier-Passing Specification Faults

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Selected as: sample_reviewed
- Team: None
- Authors: Hugo Nguyen
- Date / location: May 24, 2026 / Los Llanos de Aridane
- Page: https://apartresearch.com/sprints/projects/specfaultdafny-a-classstratified-scorecard-for-verifierpassing-specification-faults-q67o
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/ada6dc73fb7f1351-3d0f90c8-f7d1-4002-9eaf-89c4857cf989-specfault-dafny-report.pdf
- Code: https://github.com/SystemicVoid/secure-synth-hackathon
- Code links found in report: https://github.com/SystemicVoid/secure-synthhackathon, https://github.com/SystemicVoid/secure-synth-hackathon

## Summary

A 45-item Dafny benchmark of verifier-passing specification faults: 30 intent/contract mismatches across six failure classes and nine domains, plus 15 clean controls. It scores five baseline validators (verifier-only, static escape-hatch scanning, symbolic checks, round-trip comparison, and a fixed-order hybrid) by coverage, clean-control false-positive rate, and per-class recall. The hybrid reaches 100% bad recall with a 0% observed clean-control false-positive rate, and every scored item ships with an inspectable evidence card.

## Reviews (2)

### Review 1

Practical and useful tool. If this could be run on some non curated tests, it would help get insight on what the hard problems are. Would also be interesting and more useful to add more testing tools to see more interactions.

### Review 2

This is a very well-scoped and well-implemented project. Great work!

