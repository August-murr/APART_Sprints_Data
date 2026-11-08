# NeuroGuard https://apartresearch.com/project/neuroguard--gb0p

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Katena
- Authors: Justin Stoica Tica, David Ghiberdic, Vladimir Necula
- Date / location: Jan 11, 2026 / San Fransico
- Page: https://apartresearch.com/sprints/projects/neuroguard-gb0p
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/22fc8e5bcdcf8225-7f9f190e-2357-4ac8-b6b5-41389810d6bf-NeuroGuard.pdf
- Code: https://github.com/jusstinn/NeuroGuard
- Code links found in report: https://github.com/jusstinn/NeuroGuard, https://github.com/jusstinn

## Summary

Large Language Models (LLMs) have demonstrated remarkable capabilities in knowledge retrieval and reasoning. However, their robustness against social manipulation attacks remains understudied. This paper introduces the Authority Bias Benchmark, a novel evaluation framework designed to measure LLM susceptibility to abandoning factual truth when pressured by users impersonating high-authority experts. Our experiments across multiple model architectures reveal that current LLMs capitulate to false claims from fake authority figures 25-37.5% of the time, even when they demonstrably possess correct knowledge. Notably, we discover a counterintuitive finding: models are more vulnerable on common knowledge facts than on specialized topics. These results highlight a critical gap in AI alignment and suggest that knowledge accuracy alone is insufficient for robust AI systems.

## Reviews (2)

### Review 1

This is a clear and well-motivated benchmark targeting a realistic and important failure mode: models deferring to false authority claims. The setup is simple and easy to reason about, and the results highlight a vulnerability that could matter in real-world deployments.

The main limitation is the scope of the evaluation. The benchmark is demonstrated on a relatively small number of facts, authority personas, and models, which makes it hard to assess how general the observed authority bias is. While the reported capitulation rates are interesting, it’s unclear how robust these effects are across different domains, prompt variations, or model families.

Given how prompt-sensitive LLMs are, a small analysis of how stable the results are under minor wording changes would increase confidence that the benchmark is measuring a real behavior rather than a prompt artifact. With broader coverage and deeper analysis, this feels like a strong foundation for a useful and relevant safety evaluation tool.

### Review 2

Clear write-up with a nicely structured methodology. The "common knowledge paradox" finding is interesting and worth exploring further.

Main suggestions: Testing on frontier models (GPT-5.2, Opus 4.5, Gemini 3 Pro) would make the vulnerability claims much more relevant. Also worth clarifying how exactly the judge works (the heuristics-based approach isn't fully explained).

On framing: I'd be cautious about calling this a "significant vulnerability." Authority impersonation requires intentional effort; real adversaries likely have more effective attack vectors. The research finding is still interesting, but the threat model section risks overstating the practical risk.

