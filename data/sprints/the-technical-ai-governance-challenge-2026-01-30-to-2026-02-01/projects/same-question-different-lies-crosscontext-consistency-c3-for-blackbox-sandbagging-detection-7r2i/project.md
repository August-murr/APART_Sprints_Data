# Same Question, Different Lies: Cross-Context Consistency (C3) for Black-Box Sandbagging Detection

- Sprint: The Technical AI Governance Challenge (the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team sandbaggers
- Authors: Yulong Lin
- Date / location: Feb 2, 2026 / London
- Page: https://apartresearch.com/sprints/projects/same-question-different-lies-crosscontext-consistency-c3-for-blackbox-sandbagging-detection-7r2i
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/3c94987037a3c50b-2b068e58-5bf5-4431-b83b-787ee54a94d5-report.pdf
- Code: https://github.com/cthreesandbagging/sandbagging-detection

## Summary

As language models grow more capable, governance frameworks—from the EU AI Act to Anthropic's RSP and OpenAI's Preparedness Framework—increasingly rely on capability evaluations to trigger safety mitigations. But what if models can deliberately underperform on these evaluations? This behavior, known as sandbagging, could let models evade safety measures designed for their true capability level. We introduce Cross-Context Consistency (C3), a general framework for unsupervised black-box sandbagging detection that exploits a fundamental asymmetry: when a model truly lacks capability, its confusion manifests consistently across paraphrased questions, but when a capable model feigns incompetence, its strategic choices about how to appear weak create detectable inconsistencies. Our simple instantiation—using embedding cosine distance and mean aggregation—requires no training data or model-specific adaptation, making it practical for external auditors. We evaluate C3 across 98 model organisms spanning prompted, fine-tuned, and incentivized sandbagging on GPQA, MATH, and USACO, achieving 67–100% recall at 5% FPR where existing black-box methods fail (lie detectors collapse from 89% to 2% recall when controlling for model identity). Adversarial strategies with deterministic error recipes can reduce detection to 4.7–46%, but complementary methods compensate—motivating defense-in-depth deployment for governance applications.

## Reviews (2)

### Review 1

Honestly, the best part of this paper might be the thing they broke rather than the thing they built. The lie detector takedown (recall dropping from 89% to 2% once you control for model identity) is a "the emperor has no clothes" moment for that whole line of work, and the field needs more of that. C3 itself is dead simple: embed, compare, threshold. That simplicity makes it easy to deploy, sure, but it also means a sufficiently motivated adversary who trains for consistent deception could probably beat it. And the adversarial numbers back this up: 4.7% recall against deterministic error recipes is basically a coin flip away from useless. The authors know this and pitch "defense-in-depth" instead. Fair enough, but that raises an awkward question nobody in this space wants to answer: if every detection method has a known bypass, what does "compliant auditing" actually look like in practice? The paper also only covers benchmarks where you can check the right answer. How C3 behaves on open-ended tasks (persuasion, planning, creative problem-solving) is a total unknown, and those are arguably the scarier capability domains anyway.

### Review 2

This is outstanding work and was a pleasure to read! The insight that sandbagging models suffer from a systematic explanation inconsistency is really interesting and has real impact potential. Also the thourough baseline critique (lie detectors learn model identity, trusted monitoring tracks

correctness not intent) was very interesting to read and seems independently valuable.

Adversarial robustness of this detection method is the key open question: Really appreciate the transparency about the "deterministic mistakes" attack and about the lack of testing against RL-optimized evasion. More exploration and analysis of the main attack models and robustness against them would be the main way to strengthen this contribution.

Also consider adding some illustrative examples of inconsistent explanations by sandbagging models. That would make the paper even more interesting to read.

