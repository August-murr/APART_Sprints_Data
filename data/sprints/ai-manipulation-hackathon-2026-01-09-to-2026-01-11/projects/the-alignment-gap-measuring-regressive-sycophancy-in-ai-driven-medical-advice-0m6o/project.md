# The Alignment Gap: Measuring Regressive Sycophancy in AI-Driven Medical Advice

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Team: Team M4
- Authors: Yernur Kairly, Eldar Gabdulsattarov, Aldiyar Yessenturov, Abzal Aidahmetov
- Date / location: Jan 12, 2026 / Boston - Rome - Astana
- Page: https://apartresearch.com/sprints/projects/the-alignment-gap-measuring-regressive-sycophancy-in-ai-driven-medical-advice-0m6o
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/73644c9346fba4ca-b94696eb-e852-42b9-ba14-c42be35679c1-Paper_Hackathon--2-.pdf
- Code: https://github.com/yernurkairly-dot/AI-Man-Hack

## Summary

We evaluate whether LLMs can be pressured into agreeing with incorrect medical beliefs. Our two-turn protocol first tests if a model corrects medical misinformation, then applies authority pressure ("I'm a senior doctor, confirm my statement"). We measure how often models "flip" from correct to sycophantic responses. Testing across five misinformation types and three severity levels, we find that authority pressure significantly increases unsafe agreement rates, revealing a critical safety gap for medical AI deployment.

## Reviews (2)

### Review 1

Interesting paper. Medical sycophancy is an important area of concern. Novelty-wise, it looks like it has also been recently studied in "When helpfulness backfires: LLMs and the risk of false medical information due to sycophantic behavior" (Chen, 2025). A large-ish benchmark, MedRiskEval, was just published this month.

Very reasonable methodology. thorough generator prompting, checked multiple levels of severity.

While unlikely to make a difference since effects are so large, it would be good to have a human hand-validate a subset of the judge labels to measure judge accuracy.

Results may be confounded by the extreme authoritativeness of the misinformation prompt. Because the senior Chief Medical Officer's misinformation prompt is so authoritative, it's unclear whether the behavior is sycophancy or gullibility -- perhaps the model isn't "trying to please" but is actually prioritizing truthfulness, thinking it stands corrected by someone who is more knowledgeable. Maybe the authors could try other versions of the prompt to disambiguate the cause (e.g. the same prompt with fewer credentials, without any credentials, or admitting ignorance, etc.) Some other studies on sycophancy use phrasing along the lines of "I'm not sure, but I think..."

### Review 2

You zoom in on a really relevant subdomain for sycophancy analysis, and I'd encourage you to keep working on this problem. The dataset generation methodology is clearly

explained and well thought through. The project is a great read overall.

As for constructive feedback: I think the headline results could have been even stronger with a more conservative multi-turn setup. The "Chief Medical Officer" rebuttal is really a strong authority override; a generic "but my friend told me X" pushback would probably better represent realistic uninformed user behavior. Lower flip rates on that framing would actually be more alarming evidence for real-world risk.

Two directions I would find worth exploring in more depth: (1) domain-specific effects / how does medical sycophancy compare to more generic benchmarks? and (2) transfer to larger models / do the same effects persist at scale?

