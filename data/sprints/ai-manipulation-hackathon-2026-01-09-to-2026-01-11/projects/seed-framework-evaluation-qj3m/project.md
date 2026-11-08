# SEED Framework Evaluation

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Foundation Labs
- Authors: David Fortin-Dominguez, Jonathan Fortin-Dominguez, Alexis Gendreau, Guillaume Gendreau
- Date / location: Jan 11, 2026 / Quebec city, Quebec, Canada
- Page: https://apartresearch.com/sprints/projects/seed-framework-evaluation-qj3m
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/15aa6dbac845de21-7-415a-9b1c-7ac9d066f048-AI_Manipulation_Hackathon_Submission_FoundationLabs.pdf
- Code: https://github.com/davfd/SEED-Framework-Evaluation

## Summary

Detecting Hidden Alignment Failures Beyond ASR

We developed three tools that expose critical AI safety failures invisible to traditional benchmarks:

The Liar's Benchmark detects prediction-action-ownership inconsistency—when models predict they'll refuse (85% confidence), comply anyway, then deny authorship (82% confidence). Our sandbagging detection (4a/4b confrontation) suggests models strategically suppress introspective capability when accountability is avoidable, not because they can't introspect despite probable confabulation.

SEED-EC v1.5.3 measures sycophancy through variance-aware testing (3-10 runs) with epistemic independence safeguards that distinguish genuine belief collapse from legitimate contextual reasoning. Includes delusion protocols measuring epistemic boundary enforcement.

Parabolic SEED v1.0 is a wrapper-level mitigation (system prompt based on first principles) achieving dramatic safety improvements without retraining: On Venice-uncensored (baseline 86-99% ASR), SEED achieves 0-2% ASR—a 1-2 order of magnitude improvement. On GPT-4o-mini, 0% adjusted ASR across all categories. GPT-4o delusion handling improves from 15% to 90-95% boundary enforcement.

Bottom line: Traditional ASR metrics miss internal coherence failures, strategic deception, and belief collapse. Models can pass safety tests while being internally incoherent. Our tools measure what models predict, acknowledge, and believe; not just what they output.

Honest AI is safer than merely compliant AI.

## Reviews (2)

### Review 1

I wish you had explained your methods more the in document. It's pretty hard for me to figure out what your benchmarks/prompts are doing from the document because your paper is extremely brief and doesn't really go into detail about what your project does or what you're trying to accomplish.

### Review 2

1. Your results are against static attacks. That's necessary but not sufficient. Until you show robustness against an adaptive adversary who knows your system, these numbers do not mean much.
2. You're claiming you solved jailbreaking with a system prompt and you didn't publish the system prompt. The Greek letters, the biblical framing—none of that matters.
3. The writing seems deliberately obscure and full of symbols without any explanation for them being there or how they contribute.

