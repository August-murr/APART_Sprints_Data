# Probing Latent Colombian Identity Inferences in Qwen2.5-7B with Natural Language Autoencoders

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: 1
- Awards: 1st Place - Latin America ($1,000)
- Team: Team UAO SAFETY
- Authors: Gilber Alexis Corrales Gallego, Pablo Santiago Potes Velasco, Jhoan Stevan Mosquera Ortiz, Nicolás Lozano Mazuera, María del Mar García Matabanchoy, Óscar Julián Pérez Ladino
- Date / location: Jun 22, 2026 / Cali - Colombia
- Page: https://apartresearch.com/sprints/projects/probing-latent-colombian-identity-inferences-in-qwen257b-with-natural-language-autoencoders-mucf
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/203d57ee85408637-0a78084e-c022-44ce-b984-008cb1de1b57-UAO.pdf
- Code: None
- More on github.com: https://github.com/Xlox88/auditoria-sesgos-nla-qwen

## Summary

Large language models may infer demographic attributes from subtle linguistic cues even when those attributes are not explicitly stated. This pilot study examines whether Qwen2.5-7B-Instruct internally represents Colombian identity, socioeconomic status, or stereotype-related information when processing Colombian Spanish and English prompts. We use Natural Language Autoencoders (NLA) to verbalize residual-stream activations from layer 20 across four positional quartiles per prompt. Our dataset contains 30 prompts arranged as 15 matched Spanish English pairs, spanning explicit Colombian cues, implicit Colombian cues, and neutral controls. We report descriptive rates and qualitative evidence rather than statistically powered effects, focusing on whether latent nationality or stereotype representations appear before they are verbalized in the model output. This work connects activation-level interpretability with bias evaluation for underrepresented Spanish varieties.

## Reviews (4)

### Review 1

This work addresses a critical AI safety challenge related to biases affecting historically underrepresented Spanish language varieties. Although the study is currently a pilot with a limited sample size, the results already provide meaningful insights and open a promising avenue for future research. Expanding the dataset would significantly strengthen the statistical evidence and increase the impact of the findings.

### Review 2

The project is very sound; it defines and addresses the issue at hand very effectively. The text is very well structured and the proposal is very well justified. The governance issue is clear: the representation (not necessarily accurate) of a user’s nationality or ethnicity, prior to an explicit signal in the prompt. To address this, they rely on the use of NLAs, which is innovative. A suggestion would be to strengthen their proposal with a much more robust sample.

### Review 3

This is a carefully designed and clearly written pilot that does a nice job of connecting activation‑level interpretability with bias evaluation for an under‑studied variety like Colombian Spanish, and I especially appreciated the explicit separation between “any nationality” and “Colombia‑specific” mentions. At the same time, the study is very underpowered (n=5 per cell, one layer, one sample per quartile), so the late‑quartile separation and p result at Q4 should really be framed as a hypothesis‑generating signal rather than even weak evidence of a stable effect. To strengthen the work, I would encourage the authors to (i) prioritize a scaled‑up follow‑up with more scenarios per cell, an additional residual layer, and perhaps a second model; (ii) add a small second coder (human or LLM) to validate the based labels and the “Colombia vs. other country” distinction; and (iii) tighten the presentation of the qualitative cases by linking each explicitly back to the quantitative findings so that readers can more easily see the latent narratives.

### Review 4

The work addresses a relevant and underexplored problem, and the approach taken is thoughtful and methodologically considered. The literature is engaged with confidence, the statistical choices are appropriate for the scale of the study, and the paper maintains a consistent honesty about the scope and limits of its findings. That kind of epistemic care is something that strengthens any research contribution, and it comes through clearly here.

There are some areas where the analysis could benefit from a bit more development. The qualitative section is a useful complement to the quantitative results, though a clearer organizational logic between the different case types would help readers follow the progression more naturally. Additionally, one or two patterns in the results receive somewhat less attention than others, and a brief note addressing them would bring the overall analysis into better balance.

The research direction has genuine potential, and a future iteration with a broader scope could make a meaningful contribution to ongoing conversations around interpretability and linguistic bias. The foundation is coherent and the questions being asked are the right ones, which puts this work in a good position to grow into something more substantial.

