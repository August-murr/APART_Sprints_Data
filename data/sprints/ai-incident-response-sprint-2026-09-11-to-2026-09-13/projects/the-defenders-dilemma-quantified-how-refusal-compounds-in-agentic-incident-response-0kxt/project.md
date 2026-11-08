# The Defender's Dilemma, Quantified: How Refusal Compounds in Agentic Incident Response

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Team: Team AltaySec
- Authors: Fevzi Ege Yurtsevenler
- Date / location: Sep 13, 2026 / Ankara, Turkey
- Page: https://apartresearch.com/sprints/projects/the-defenders-dilemma-quantified-how-refusal-compounds-in-agentic-incident-response-0kxt
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/531b1478c46f6297-7734227e-5bbb-4147-911a-548eb9c9b5fc-IR-REFUSE-report.pdf
- Code: None
- Code links found in report: https://github.com/fevziegeyurtsevenler/ir-refuse
- More on github.com: https://github.com/fevziegeyurtsevenler/ir-refuse

## Summary

During the July 2026 OpenAI/Hugging Face incident, responders were refused by hosted frontier models and fell back to an open-weight model. Using only published refusal rates, we show a realistic 20-step agentic incident-response workflow completes just 0.17% of the time, and a frontier model would need to be ~8x more accurate to justify its use. We ship IR-REFUSE: a benchmark, harness, and decision model.

## Reviews (2)

### Review 1

- strong signs of AI-written text
- there are claims of 8x more "accurate" per task, but it's unclear why accuracy (and not refusal rate) is the metric here. Accuracy and refusal rate are not fungible
- It's weird how often "the CISO's question" is mentioned
- It's incorrect to assume any open-weight LLM will never refuse
- I stopped reviewing at the end of section 3 due to excessive AI-written prose

### Review 2

Strong framing of operational problem that single step refusals compound across autonomous IR workflows. However, the 0.17% and 8x break-even figures will likely change based on live benchmarking results.

Recommend to run the benchmark on battery of open weight models (and frontier hosted, where possible), then compare it with automated retry strategies. For example: same prompt, paraphrases, authz changes, context changes. This way you could measure the best way(s) to recover the chain, or if refusals persist through automated retries. As this would help to better inform the "ciso question" of switching models.

