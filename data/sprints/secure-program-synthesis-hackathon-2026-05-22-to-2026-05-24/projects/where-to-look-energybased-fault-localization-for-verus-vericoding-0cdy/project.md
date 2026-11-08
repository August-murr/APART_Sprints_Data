# Where to Look: Energy-Based Fault Localization for Verus Vericoding

- Sprint: The Secure Program Synthesis Hackathon (secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24)
- Rank: 2
- Awards: 2nd Place ($500)
- Team: Team Oz Labs
- Authors: Guy Nachshon
- Date / location: May 24, 2026 / Tel Aviv
- Page: https://apartresearch.com/sprints/projects/where-to-look-energybased-fault-localization-for-verus-vericoding-0cdy
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/acddab6c318d6e16-1d22c04e-659e-464d-9300-0abf98440c2b-main.pdf
- Code: None
- Code links found in report: https://github.com/ozlabsai/VericodingEBM, https://github.com/deepseek-ai/DeepSeek-V4
- Recording: https://github.com/ozlabsai/VericodingEBM

## Summary

A 1.5B-parameter discriminative energy-based model that scores each line of a Verus implementation with an energy proxy for "this line is the bug." Qwen2.5-Coder-1.5B + LoRA + sentinel-token per-line head, trained on 39k Microsoft Verus pairs with InfoNCE + pairwise hinge + ListNet. One adapter, runs on a single H100, demo runs in the browser.

The finding is split. The 1.5B specialist beats every frontier LLM on per-line fault localization (top-3 0.84 vs 0.74). Frontier LLMs win whole-impl ranking (AUROC 0.91 vs 0.78) and CEGIS repair (30% vs 25%). Different tools for different layers of the verification loop — and we're explicit about which.

The audit is the other contribution. Every FAIL impl in the dev-test corpus carries a // FAILS debug marker that Qwen's pretraining prior couples to failure. Strip the marker, watch the signal collapse for some checkpoints, hold for frontier LLMs, over-correct for ours. We document the leak, release the strip-FAILS audit pipeline, and ship Counterfactual Marker Augmentation as the fix.

Released: model, dataset, audit pipeline, CEGIS harness, every LLM-baseline record, browser-side demo. All under: https://ozlabsai.github.io/VericodingEBM/

## Reviews (2)

### Review 1

This is a careful and technically honest project on fault localization for Verus verified code. The problem is relevant to secure program synthesis: when AI-generated verified code fails, developers and repair agents need help identifying where the proof or implementation likely went wrong. A line-level localizer could make verifier-in-the-loop repair more inspectable and efficient.

The strongest part of the project is the evaluation discipline. The submission compares against static baselines, frontier LLMs, and a closed-loop CEGIS-style repair setup. It also includes a useful marker-leak audit showing that an earlier checkpoint benefited from // FAILS / FIXME leakage. That kind of careful negative-result reporting is valuable in this area because misleading localization performance could create false confidence in secure-code workflows.

The main limitation is that the specialist model does not yet outperform frontier LLMs, and the CEGIS repair experiment does not show a clear repair-rate advantage from specialist-guided localization. To strengthen the work, I would focus the next iteration on demonstrating a concrete repair-loop benefit: better success under limited model budget, faster local inference, improved robustness on unseen Verus patterns, or stronger performance when frontier LLMs are not available. Broader tests on additional verified-programming settings would also help.

Overall, this is solid hackathon work with good methodology, clear reporting, and a meaningful security-relevant direction. The current results are mixed, but the artifact and evaluation setup are useful foundations for future secure program synthesis research.

### Review 2

The authors deserve credit for their transparent analysis, especially the strip-FAILS audit that clearly identified a serious pre-training data leak. However, as a practical system, the proposed EBM does not outperform strong zero-shot LLM baselines on localization or repair tasks. The evaluation appears statistically underpowered, and the model struggles with ensure clauses due to limited global context. Strengthening global reasoning and validating the approach on real production defects would significantly improve the work impact.

