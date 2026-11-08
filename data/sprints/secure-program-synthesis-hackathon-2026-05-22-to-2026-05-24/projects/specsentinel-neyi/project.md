# SpecSentinel

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Team: Team UNIT - 108
- Authors: Mudit Khater
- Date / location: May 22, 2026 / INDIA
- Page: https://apartresearch.com/sprints/projects/specsentinel-neyi
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/4aabd209756e1d4a-702d4a37-1a52-48a5-9e56-74e038e657dc-SpecSentinel_Report.pdf
- Code: https://github.com/mudit108-code/SpecSentinel

## Summary

SpecSentinel is a professional-grade, single-file specification validation studio built in Python 3.10 and Streamlit.The application provides an end-to-end, interactive pipeline that evaluates whether a candidate specification truly and completely captures the intended behaviour of a software system.

The platform integrates four academically grounded validation methods — automated behavioral testing, mutation kill analysis, bidirectional cross-checking, and lightweight formal property verification — into a cohesive, professional UI that produces actionable grades, detailed diagnostics, and exportable JSON reports.

SpecSentinel requires no external dependencies beyond Streamlit and runs instantly with a single terminal command. It ships with a fully worked demonstration example (a Safe Integer Stack specification) enabling reviewers to experience the full validation pipeline in under two minutes.

## Reviews (2)

### Review 1

Secure program synthesis calls for various spec and test methods. This project produced a tool that contains a battery of these methods within a neat user interface. A point to flag for future reference: some of the methods are not yet fully implemented (mutation-testing is just "rand" as far as I can tell), that is tolerable on a sprint and for a UI demo but must be declared in the write-up, especially when it feeds into a metric.

### Review 2

I like the intention of the spec tool, but it seems to promise beyond what it delivers. It also lacks the transparency/honesty about it's limitations.

SpecSentinel is described to be "professional-grade", but their killed mutants are defined as "killed = random.random() < (0.55 + intensity * 0.35)".

Claude did decent work and the box is pretty, but there's no engine in it. You have a good scaffold and next good steps are to work on making it functional, to validate it and to explore some case studies on its limitations. Keep up at it!

