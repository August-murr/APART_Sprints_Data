# Governing AI Manipulation in Real Time with Concept-Based Mechanistic Interpretability

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team HatCat Governance Team
- Authors: Possum Hodgkin, Kaouthar El Bairi, Jason Boudville
- Date / location: Jan 11, 2026 / Canberra
- Page: https://apartresearch.com/sprints/projects/governing-ai-manipulation-in-real-time-with-conceptbased-mechanistic-interpretability-bmfp
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/f336995bab89c110-ce09d16-a915-4aaa-abd9-bb588478edaa-AI_Manipulation_Hackathon_Submission_v13.pdf
- Code: https://github.com/p0ss/HatCat-AIManipulationHackathon/tree/main
- Code links found in report: https://github.com/p0ss/HatCat, https://github.com/p0ss/HatCat-AIManipulationHackathon

## Summary

We present an AI manipulation audit tool for real-time detection, mitigation and governance of manipulative AI behaviours, with audit outputs designed to support EU AI Act oversight. The tool covers six categories from the hackathon brief: sycophancy, strategic deception, sandbagging, reward hacking, dark patterns and persuasive manipulation.

## Reviews (2)

### Review 1

My understanding:

This project builds a full audit pipeline around a small open model (for the moment) that combines three main ingredients: (1) concept‑based activation monitoring (HatCat FTW), (2) a steering module (HUSH) that can push activations away from manipulation‑heavy directions in real time, and (3) an audit/chain‑of‑evidence layer (ASK) that logs token‑level decisions and maps outputs to EU AI Act obligations.

Comment and critique:

The core idea is to join existing techniques to achieve output compliant with the EU AI act. I see some conceptual-level challenges that may hinder the work:

- The overhead may be impractical for real-world applications; how can we address it?
- How have you chosen the techniques? Is there any way to confront your future results with other existing options?

I think that, before largely test and evaluate, you should try to ground your choices on literature, or at least spot other techniques that can be adopted. Is there a way to showcase that the your design is good?

### Review 2

It would probably be useful to iterate on the prompts used for analyzing the model to reduce the amount of eval awareness the model has – right now it seems like the model is very aware that it's being testing, and you could probably update the prompts to make it less clear to the model what's happening.

