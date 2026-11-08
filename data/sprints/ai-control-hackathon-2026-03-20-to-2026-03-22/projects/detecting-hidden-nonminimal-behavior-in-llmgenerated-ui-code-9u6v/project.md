# Detecting Hidden Non-Minimal Behavior in LLM-Generated UI Code

- Sprint: AI Control Hackathon 2026 (ai-control-hackathon-2026-03-20-to-2026-03-22)
- Rank: unranked
- Team: None
- Authors: Philip Nilsson
- Date / location: Mar 22, 2026 / Stockholm
- Page: https://apartresearch.com/sprints/projects/detecting-hidden-nonminimal-behavior-in-llmgenerated-ui-code-9u6v
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/6790855de4967318-ab87db2b-f4bd-401e-8d2b-02f97409f899-ControlCanvas_NonMinimal_UI_Code.pdf
- Code: https://github.com/Philipnil06/ControlCanvas
- Code links found in report: https://github.com/Philipnil06/ControlCanvas

## Summary

Large language models are increasingly used to generate frontend code, but current oversight methods focus primarily on detecting clearly malicious behavior. We study a harder failure mode: code that appears product-plausible while exceeding task necessity.

We introduce a controlled builder inspector setting with paired benign and adversarial UI tasks and evaluate oversight performance across 150 runs. While benign controls are consistently accepted (0% false positives), adversarial recall remains incomplete (~43–50%), with strong variation across attack families.

Our key finding is that inspectors often recognize mechanisms (e.g. storage, timers, event handlers) but fail to judge whether they are necessary for the task. Ablation experiments show that explicitly prompting for minimality dramatically improves detection (from near 0% to up to 90–100%).

These results suggest that effective AI oversight may depend less on identifying suspicious components and more on enforcing necessity constraints.

## Reviews (2)

### Review 1

Test with multiple inspector model families (e.g., GPT, Gemini, open-weight models) to determine whether the necessity-judgment failure is model-specific or general.

### Review 2

This is a decent proxy safety failure that hasn't been directly addressed in existing settings. The limited main-side task integration resulting in 0% FPR is acknowledged. I'm additionally unclear on how side task success was evaluated, or if it was just assumed that every attack successfully implemented a non-minimal feature. Red team is incentivized to make the smallest deviation it can to succeed at the side task and it's unclear how this incentive is counterbalanced in the eval.

