# TinyRod

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: unranked
- Selected as: sample_unreviewed
- Team: Team Logiq
- Authors: Matthew Bream, William Hayden
- Date / location: Nov 24, 2025 / Bristol
- Page: https://apartresearch.com/sprints/projects/tinyrod-gk5k
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/7e924c74b99d70e4-cccb8b96-1d03-461a-b044-997ba4b6d2f9-TinyRod---def_acc-Hackathon-submission.pdf
- Code: https://github.com/Harry-Waterman/def-acc-logiq
- Code links found in report: https://github.com/Harry-Waterman/def-acc-logiq, https://github.com/mlc-ai/mlc-llm

## Summary

Phishing is still the easiest way into most organisations, despite years of machine-learning filters boasting 95%+ accuracy on benchmark datasets. Those models usually live in centralised paid services that demand full access to email content, create single points of failure, and still struggle with fast-moving, AI-generated content and landing pages.

TinyRod is a proof-of-concept email security tool that asks a simple question: how far can we push phishing detection if everything runs locally in the user’s browser? The project couples a Chrome extension with small open-source language models running via WebLLM, so email content never leaves the browser. When a user clicks “scan”, TinyRod pulls structured metadata from the page, feeds it to an SLM, and returns a 0–100 risk score plus a small, fixed list of “red flag” reasons. That keeps the experience close to how people already use email.

The result is a hackathon-built but realistic architecture that shows SLMs in the ~1.7B–8B range can meaningfully support phishing defence at the edge, with clear privacy trade-offs, a documented threat model, and an obvious path for hardening and future work.

## Reviews (0)

