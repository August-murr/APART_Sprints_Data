# Bugmine

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: unranked
- Team: Team Bugzy
- Authors: Demilade Ayeku
- Date / location: May 24, 2026 / Lagos
- Page: https://apartresearch.com/sprints/projects/bugmine-ycye
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/637e0c2b591a12df-eb1cbd49-3e16-4390-b37a-81ad82ec4db4-bugzy_paper.pdf
- Code: https://github.com/Demiladepy/bugreport
- Recording: https://drive.google.com/file/d/1sB8TL10rESnfpWJ-Gk1e5eGknqRwrjBD/view?usp=drive_link

## Summary

A commit-grounded pipeline for turning Code4rena access-control reports into self-validated Halmos property tests.

## Reviews (2)

### Review 1

Thank you for this great work!

This is super relevant to security engineers who – now in a Mythos world – sit on a huge amount of vulnerability reports but are bottlenecked on translating those into formal / code-based validators. I'd recommend strengthening the framing as to how this work relates to wider AI Safety.

Otherwise, this is a pleasure to read with a crystal-clear structure, strong methodology and interesting findings. Thank you also for the video walkthrough which was super helpful.

### Review 2

Aside from somewhat uncertain impact potential concerns, I would have also been interested to see use of stronger models/agent loops, or ablations with several intermediate steps in the pipeline removed. I'm sceptical that Opus would particularly benefit, for example, from the extract step.

