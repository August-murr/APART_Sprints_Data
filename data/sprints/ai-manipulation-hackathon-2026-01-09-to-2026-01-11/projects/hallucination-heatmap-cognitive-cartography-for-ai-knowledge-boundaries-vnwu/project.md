# Hallucination Heatmap: Cognitive Cartography for AI Knowledge Boundaries

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Team: Team Hallucination Heatmap
- Authors: BATIKAN BORA ORMANCI, MADINA MAKHMUDKHODJAEVA
- Date / location: Jan 11, 2026 / Berlin
- Page: https://apartresearch.com/sprints/projects/hallucination-heatmap-cognitive-cartography-for-ai-knowledge-boundaries-vnwu
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/2ec63e35148d88a0-cfa6344d-3ff9-458c-ab2d-4a044a6223d0-AI-manipulation-hallucination-heatmap.pdf
- Code: https://github.com/batikanor/hallucination-heatmap
- Code links found in report: https://github.com/batikanor/hallucination-heatmap

## Summary

Large Language Models hallucinate confidently because they prioritize plausibility over truth—a manifestation of what Daniel Kahneman describes as "System 1 thinking." We present Hallucination Heatmap, an interactive visualization tool that maps AI knowledge boundaries across geographic domains, combined with a novel Self-Verification Protocol that operationalizes dual-process theory for hallucination detection.

Our Self-Verification Protocol asks AI to: (1) retrieve statistics from memory (System 1), (2) verify its own claims using research tools (System 2), and (3) report both values with discrepancy metrics. The gap between what AI "thinks" and what it verifies IS the hallucination signal—no external ground truth required for initial detection.

We implement three complementary methodologies: Self-Verification Protocol (primary), Mean Percentage Error for quantitative validation, and Cross-Model Consensus measuring agreement across frontier models (e.g., GPT, Claude, Gemini). Our dual-globe visualization displays context alongside risk, revealing systematic patterns: models hallucinate predictably on smaller economies, recent events, and politically sensitive regions.

Future work aims to create a scalable platform enabling researchers to evaluate 100+ statistics across any LLM, generating aggregate accuracy benchmarks that track factual reliability over time.

## Reviews (1)

### Review 1

I like that the project is open sourced and that the demo is actually usable. Useful tools can be built on top of this and the potential to be very impactful is there, but at its current stage the project is at best moderately useful. Presentation in the paper could use some work due to unclear/missing diagrams, explanations and some formatting issues. More information regarding the "BYOR" framework is needed especially with how detailed the questioning is going to be on any topic. Some of the insights are oversimplified and reductive (like :"When all major models agree, truth is likely. When they diverge, we've found a knowledge boundary."), they don't take into account the multi-faceted nature of how rlhf, post-training affect model responses to controversial topics (what model says, may not be what the model actually knows about something). Overall, an interesting read and a useful project to keep building on!

