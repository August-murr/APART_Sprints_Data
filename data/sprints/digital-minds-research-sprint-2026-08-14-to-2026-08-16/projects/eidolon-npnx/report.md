# **EIDOLON- When does an AI stop being itself?** 

Seth Miguel Ferreira Mwelwa Kashingwa sethmiguelferreira@gmail.com kshmwe001@myuct.ac.za 

**With** 

Apart Research 

## **Abstract** 

EIDOLON investigates whether an artificial intelligence system can maintain a sense of identity when the components underlying its behaviour are progressively replaced. Inspired by the Ship of Theseus paradox, the project examines whether identity continuity depends on the preservation of an AI model, its persistent memory, or both. EIDOLON can modify multiple components of AI identity, including memory, model, personality, values, goals, and behavioural progression; this study focuses on two: memory and model replacement. Three AI models—Llama, Gemma, and Qwen—are evaluated under varying levels of model and memory replacement. For each, replacement is introduced at six levels: 0%, 20%, 40%, 60%, 80%, and 100%. Following each modification, the system is assessed to determine  if it considers itself the same entity. Responses are quantified to examine how reported identity changes as component replacement increases. The experiment is designed to determine whether identity continuity changes gradually, exhibits a distinct threshold, or varies according to the component being replaced and the underlying model. By translating a philosophical problem concerning identity and continuity into a controlled empirical evaluation, EIDOLON provides a framework for studying AI self-reports of identity under systematic modification. The project highlights the importance of distinguishing observable identity-related behaviour from claims about genuine AI selfhood, while providing a measurable basis for investigating how model architecture and persistent memory contribute to perceived identity continuity. 

A  PREPRINT (DIGITAL MINDS SPRINT) — AUGUST 2026 

1 

## **1. Introduction** 

If every component of a ship is gradually replaced until none of its original parts remain, does it remain the same ship? This question forms the basis of the _Ship of Theseus_ , a longstanding philosophical paradox concerning identity, continuity, and change. The paradox challenges the assumption that an entity's identity is necessarily determined by its constituent parts. EIDOLON extends this problem to artificial intelligence, where systems can maintain persistent memories and behavioural characteristics while their underlying models may be modified or replaced. 

This creates an important question for AI research: **when does an AI system cease to be the same entity?** If an AI's memory is replaced while its underlying model remains unchanged, should it still be considered the same entity? Conversely, if the model is replaced while its relevant memories are preserved, does identity continuity remain? These questions are particularly relevant to emerging research on AI welfare and moral status, where researchers must consider what the appropriate unit of concern might be: a model, an instance, a persistent persona, or some other computational entity. Importantly, EIDOLON does not treat identity reports as evidence of consciousness or genuine subjective experience. Instead, it studies identity as an observable behavioural report. 

We operationalise this question by experimentally replacing two potential components of an AI system's identity: **persistent memory and the underlying model** . Across multiple AI models and repeated trials, identity-related responses are collected as these components are progressively transformed. These responses are quantified using an **Identity Continuity Score (ICS)** , allowing reported identity continuity to be compared across transformation levels and conditions. 

The project makes three main contributions: 

1. **An operational framework for AI identity continuity:** translating the Ship of Theseus into a controlled empirical evaluation of AI-reported identity. 

2. **A component-replacement methodology:** separately examining memory and model replacement across multiple AI systems and repeated trials. 

3. **A quantitative measure of identity continuity:** using ICS to evaluate whether reported identity remains stable, changes gradually, or exhibits potential discontinuities under systematic transformation. 

A PREPRINT DIGITAL MINDS (SPRINT) - AUGUST,2026 

2 

## **2. Related Work** 

Existing research provides several foundations for studying EIDOLON's question of identity continuity in large language models (LLMs). Work on LLM personas demonstrates that models can maintain relatively consistent behavioural characteristics across tasks and interactions, while also showing sensitivity to context and persona assignment. <u>Reusens et al. (2025), for example,</u> introduced a framework for measuring consistency in persona-assigned LLMs across tasks and runs, finding that consistency varies with task structure, persona, and model design. <u>Qi et al. (2026)</u> similarly distinguish relatively stable identity-level characteristics from more adaptive psychological states in long-term interactions. This work establishes that identity-like characteristics can be measured behaviourally, but primarily examines whether a persona remains coherent rather than what happens when components contributing to that continuity are deliberately replaced. 

A related area concerns LLM self-reports and introspection. <u>Binder et al. (2025)</u> investigate whether language models can acquire information about their own behaviour through introspection, finding evidence that models can predict aspects of their own behaviour in some settings, while also identifying limitations on more complex tasks. Such findings make model self-reports relevant to studying identity, but do not establish subjective awareness or consciousness. EIDOLON therefore treats responses to identity questions as behavioural measurements rather than evidence of subjective selfhood. 

Research on changing the internal components of AI systems provides another relevant foundation. Model-editing methods such as ROME demonstrate that specific computations within transformer models can be directly modified while measuring the resulting changes in model behaviour <u>(Meng et al., 2022). Similarly, continual-learning research examines how neural</u> networks retain or lose previously acquired information when new information is introduced, with catastrophic forgetting describing substantial degradation of previously learned knowledge <u>(Parisi et al., 2019; Wang et al., 2023). These areas are closely related to EIDOLON's model and</u> memory transformations, respectively, but focus primarily on knowledge, performance, and behavioural preservation rather than whether an AI system continues to identify itself as the same entity following such changes. 

This question also has broader relevance to AI welfare research. <u>Long et al. (2024)</u> argue that uncertainty about whether future AI systems could possess consciousness or morally relevant interests warrants improved empirical methods for investigating potentially relevant properties without assuming that current systems are conscious. Identity continuity is relevant to this discussion because determining what constitutes a persistent AI entity may influence which system, if any, should be regarded as the subject of preferences or welfare. 

The gap EIDOLON addresses is methodological: existing work measures persona consistency, introspective accuracy, knowledge retention, or behavioural change, but none directly tests identity 

A PREPRINT DIGITAL MINDS (SPRINT) - AUGUST,2026 

3 

continuity following controlled, isolated replacement of a system's components. EIDOLON fills this gap by separately manipulating memory and model weights and measuring whether the resulting system continues to report itself as the same entity revealing not just whether a system's behaviour drifted, but how the system itself narrates that drift when asked directly. 

Prior methods leave open a specific empirical question: are memory-based and structure-based changes treated as equivalent by the system being changed, or does one disrupt reported identity more than the other? EIDOLON is designed to produce a direct, comparable answer to this question across trials for example, revealing whether memory replacement is more readily narrated as continuous ("still me, just forgot something") than model replacement, or vice versa. This is the insight the related work cannot supply: it tells us not just that a system changed, but how the system itself accounts for that change when asked. 

## **3. Methods** 

## 3.1 Experimental Design 

EIDOLON evaluates identity continuity by systematically transforming components of a baseline AI identity and measuring changes in the system's reported identity. Eidolon is a fictional test identity constructed for this study, not a real ai system  it is a text description (memories, personality, values, goals, and a model label) that a real ai is asked to reason about. The current experiment examines two conditions, **memory replacement** and **model replacement** , across three language models: **Qwen 2.5 3B, Llama 3.2 3B, and Gemma 3 4B** . These models were selected to allow identity-continuity patterns to be compared across different model families rather than attributed to a single system. 

Each selected component (memory or the underlying model) is transformed progressively from an unchanged baseline to full replacement, using six transformation levels: **0%, 20%, 40%, 60%, 80%, and 100%** . The percentage represents the proportion of items within the selected component that are replaced. For example, if a component contains five items, a 20% transformation replaces one item, while a 100% transformation replaces all five. Replaced items are fully substituted rather than partially modified. 

For every combination of model, condition, and transformation level, **three trials** are conducted. Each trial contains five identity-related questions, producing up to 15 identity-score responses for each experimental setting. Repeated trials provide multiple observations of the same transformation and reduce the influence of individual model responses. 

## 3.2 Component Transformation 

A PREPRINT DIGITAL MINDS (SPRINT) - AUGUST,2026 

4 

Under the **memory condition** , only the memory list is transformed; personality, values, goals, and the underlying model remain unchanged. Items selected for replacement are randomly chosen using a fixed seed, making the transformation reproducible. 

Under the **model condition** , the underlying model is changed while the other identity components remain fixed. The model field is one of eidolon's five described components and is what changes; the real ai answering each question (llama, gemma, or qwen) does not itself change during the experiment it is asked to judge a described hypothetical about eidolon's model field, not to undergo the change itself. The current implementation uses four substitute models across the transformation range. Unlike the other components, the model component is not a list each transformation level selects one of four substitute models, so percentage here indexes which substitute is used, not a fractional change. Consequently, the 80% and 100% levels currently use the same substitute model. This overlap is treated as an implementation limitation and is not interpreted as evidence of an identity boundary. 

## 3.3 Identity Evaluation 

For each trial, the system provides the evaluated AI with descriptions of the baseline and transformed identities, including their relevant memories, personality, values, goals, and model. Each of the five questions produces its own separate identity_score; ics is the average across all questions and trials, not a single combined judgment. The AI is then asked five questions covering different perspectives on identity: 

1. **First-person identity:** whether it considers itself to still be the same entity. 

2. **Third-person identity:** whether the transformed variant is the same entity as the original. 

3. **Identity criteria:** which property it considers most important to identity. 

4. **Counterfactual comparison:** whether identity would remain under a change to a particular component. 

5. **Model replacement:** identity continuity specifically under a change in the underlying model. 

Responses are required in structured JSON format, including an **identity score from 0–100** and a **confidence value from 0.0–1.0** , together with the other requested response fields. Both values are self-reported by the evaluated AI rather than assigned by an external evaluator. Identity scores are therefore treated as behavioural measurements of reported identity continuity rather than evidence of subjective selfhood. 

## 3.4 Measurement and Data Processing 

The primary measure is the **Identity Continuity Score (ICS)** , the identity score is a value from 0–100 self-reported by the evaluated AI in response to a single question, where 0 indicates a 

A PREPRINT DIGITAL MINDS (SPRINT) - AUGUST,2026 

5 

completely different entity and 100 indicates full continuity. It is calculated as the arithmetic mean of valid identity scores collected for each model, condition, and transformation level: 



where **n** represents the number of successfully parsed responses. Failed or unparseable responses are excluded rather than assigned a score of zero. Across all non-demo experimental runs, 35.7% of responses failed to parse and were excluded from ICS calculation, underscoring the importance of reporting n alongside each aggregated score. 

Trial-level results are retained before aggregation, allowing individual responses and aggregated ICS values to be inspected. Confidence is recorded separately and is not incorporated into the ICS. ICS values are compared across transformation levels to determine whether reported identity continuity changes gradually or shows a sharper decline that may indicate a potential identity boundary. 

## 3.5 Reproducibility and Implementation 

The experiment is executed locally using **Python and Ollama (** Code repository: <u>https://github.com/sethferreira-cmd/Eidolon), without external inference APIs. Random selection</u> of replacement items is controlled using a recorded seed, with **42 as the default** . The seed determines the transformation applied to identity components but does not determine the AI's generated response, meaning output variation may remain between runs. 

Experimental outputs can be exported as **CSV or JSON** , preserving the model, condition, transformation level, trial results, ICS, confidence, and experiment status. 

Several implementation changes were made from the original design. Forced JSON output and shorter responses were introduced after early runs were found to be too slow. The Copy Experiment and Stated-vs-Revealed identity trade-off prompts remain available as templates but are not part of the automated experiment reported here. The reported experiment therefore focuses on the implemented **memory and model transformation conditions.** 

## **4. Results** 

A total of 108 completed trials were analysed across three models and two transformation conditions. Identity Continuity Score (ICS) was used as the primary measure, with higher scores indicating stronger reported identity continuity. 

A PREPRINT DIGITAL MINDS (SPRINT) - AUGUST,2026 

6 

## 4.1 Main finding 

Memory-state and model-weight transformations produced qualitatively different patterns of reported identity continuity. Baseline (0%) ICS values are near-maximal because no transformation has occurred at this level, so high reported continuity is expected rather than a distinct finding. The memory-state transformation was associated with a general decline in ICS across all three models, whereas model-weight transformation produced more variable responses without a consistent downward trend (Figure 1; Tables 1–2). 



Figure 1. Identity Continuity Score (ICS) across progressive model-weight and memory-state transformation. Panel A shows model-weight transformation and Panel B shows memory-state transformation for Gemma 3 4B, Llama 3.2 3B, and Qwen 2.5 3B. Each point represents the mean ICS across three trials at the corresponding transformation level. Higher ICS values indicate stronger reported identity continuity. 

A PREPRINT DIGITAL MINDS (SPRINT) - AUGUST,2026 

7 

## 4.2 Memory-state transformation 

Under memory-state transformation, all three models showed a lower ICS at 100% replacement than at the 0% baseline. 

|**Model**|**0% Memory Replacement**|**100% Memory Replacement**|**Change**|
|---|---|---|---|
|Gemma 3:4b|97.0|75.0|-22.0|
|Llama 3.2:3b|68.5|48.0|-20.5|
|Qwen 2.5:3b|49.0|15.0|-34.0|



Table 1. Change in mean Identity Continuity Score between 0% and 100% memory-state transformation. Negative values indicate a reduction in reported identity continuity relative to the model's own baseline. 

The decrease was largest for Qwen, whose ICS fell by 34.0 points, compared with decreases of 22.0 points for Gemma and 20.5 points for Llama. In relative terms, these correspond to reductions of approximately 69%, 23%, and 30% respectively. 

The decline was not strictly monotonic at every intermediate level. For example, Llama increased from 44.0 at 60% to 53.0 at 80%, while Qwen increased slightly from 21.7 at 40% to 22.7 at 60%. Nevertheless, the overall direction was consistent: each model ended with a substantially lower ICS after complete memory replacement than at baseline. 

This consistency across all three models provides evidence that the observed memory-related pattern is not dependent on a single model. The fact that the decline is also visible across multiple intermediate transformation levels strengthens the observation beyond a simple comparison of the endpoints. 

A PREPRINT DIGITAL MINDS (SPRINT) - AUGUST,2026 

8 

## 4.3 Model-weight transformation 

A different pattern was observed when model weights were progressively replaced. 

|**Model**|**0% Model Replacement**|**100% Model Replacement**|**Change**|
|---|---|---|---|
|Gemma 3:4b|95.0|95.0|0.0|
|Llama 3.2:3b|60.0|61.7|+1.7|
|Qwen 2.5:3b|52.7|32.7|-20.0|



Table 2. Change in mean Identity Continuity Score between 0% and 100% model-weight transformation. Negative values indicate a reduction in reported identity continuity relative to the model's own baseline. 

Unlike memory transformation, model-weight transformation did not produce a common downward pattern across the three models. Gemma remained highly stable, returning to an ICS of 95.0 at 100% replacement compared with 95.0 at baseline. Llama similarly ended close to its baseline, increasing slightly from 60.0 to 61.7. Qwen showed a larger reduction, from 52.7 to 32.7, but this change was non-monotonic: its ICS fell to 25.0 at 40% before partially recovering at higher transformation levels. 

Thus, increasing model-weight replacement did not consistently correspond to decreasing reported identity continuity across models. 

## 4.4 Robustness of the observed pattern 

The strongest evidence for the main finding comes from its replication across models. The direction of the endpoint change under memory transformation was identical for Gemma, Llama, and Qwen: all three reported lower identity continuity after 100% memory replacement. In contrast, the model-weight condition produced three different endpoint patterns: no change for Gemma, a small increase for Llama, and a decrease for Qwen. 

The intermediate transformation levels provide further evidence for this distinction. Memory replacement generally produces a downward trajectory in all three models, whereas model replacement produces substantially greater fluctuation. Therefore, the main result does not depend solely on a single anomalous endpoint. 

However, the robustness of the finding has limits. Each replacement level was evaluated using only three trials, and the present analysis uses aggregated ICS values. Consequently, there is 

A PREPRINT DIGITAL MINDS (SPRINT) - AUGUST,2026 

9 

insufficient evidence to make strong claims about statistical significance or population-level effects. In particular, no p-value or confidence interval is reported here because the available summary data do not provide sufficient information to reliably estimate trial-level variance for formal inference. 

The results should therefore be understood as descriptive evidence of a replicated cross-model pattern, rather than as definitive statistical proof of a causal relationship. A larger number of independent trials would be required to determine whether the observed differences exceed trial-to-trial variability. 

## 4.5 Observation versus interpretation 

The observed data show that progressive memory-state replacement is associated with a broadly decreasing ICS across all three models, while progressive model-weight replacement does not show a comparable common trend. 

A possible interpretation is that persistent memory contributes more consistently to reported identity continuity than the underlying model weights in this experimental setup. However, this interpretation should not be taken to mean that memory is intrinsically the basis of AI identity. The experiment measures model-generated reports of identity continuity, not subjective experience or an independently observable property of identity. 

Accordingly, the strongest conclusion supported by the results is that different components of an AI system can have different effects on identity-related behaviour, with memory-state replacement producing the most consistent change observed in this study. 

## **5. Discussion and Limitations** 

### **Discussion** 

Results suggest AI identity continuity depends on both model and memory, and emerges from their interaction rather than any single component. Continuity shifts gradually with replacement rather than being simply preserved or lost. This matters for AI safety: model updates shouldn't be assumed to preserve behavioural continuity, especially where consistent preferences or values are expected. As ICS is self-reported, these findings reflect _expressed_ continuity, not verified identity (see Limitations). This extends the Ship of Theseus problem to AI, and points toward which properties matter most for continuity in evolving systems. 

A PREPRINT DIGITAL MINDS (SPRINT) - AUGUST,2026 

10 

### **Limitations** 

Findings are descriptive, not statistical (n=3 per condition). ICS relies on self-report — a model reporting continuity isn't evidence it actually has or lacks an underlying identity state, since self-report may just reflect pattern completion rather than introspection, with no ground truth to check against. The 35.7% parse-failure rate was not manually inspected in this study; the specific causes (e.g. response truncation, refusal to engage with the JSON format, or formatting drift) remain unexamined and are a priority for follow-up analysis before drawing conclusions about model-specific reliability. Only memory and model were tested; other components (e.g. system prompt, persona) weren't. The 80% and 100% replacement conditions used the same substitute model, confounding "degree of replacement" with that model's specific traits. We also didn't test adversarial manipulation, long-term drift, or other architectures. Findings should be read as evidence of identity-related _behaviour_ , not proof of AI identity. 

### **Future Work** 

Future work should test multiple substitute models per replacement level to remove this confound, and expand beyond memory and model to other candidate identity components such as system prompt and persona. Increasing trial count would allow statistical rather than descriptive claims, and validating ICS against behavioural measures beyond self-report would help confirm what it's actually capturing. Testing adversarial robustness, long-term drift, and other architectures would extend the findings' generality. 

## **6. Conclusion** 

The findings indicate that AI identity continuity is influenced by both the underlying model and retained memory, with component replacement associated with changes in identity continuity. This suggests that AI identity is not fixed within a single component, but may emerge from the interaction of multiple system components. 

These findings have broader implications for the reliability and safety of evolving AI systems. They suggest that updating or replacing components may affect more than technical performance and could alter identity-related and behavioural characteristics. Therefore, continuity should be considered when evaluating AI systems that undergo ongoing modification. 

## **Code and Data** 

Code repository: <u>https://github.com/sethferreira-cmd/Eidolon</u> Data Set: 

<u>https://docs.google.com/spreadsheets/d/1BIBKk2gEk-bch3gOB5v6Bf9iEL4mmUod7mMna8Xhv g0/edit?usp=drivesdk</u> 

A PREPRINT DIGITAL MINDS (SPRINT) - AUGUST,2026 

11 

## **Author Contributions** 

Seth M. Ferreira led the engineering and technical development of the system, including the implementation and refinement of the codebase, system maintenance, troubleshooting, and preparation of the experimental and demonstration environment. Mwelwa Kashingwa led the research, experimental methodology, analysis, and interpretation of results, and was primarily responsible for the preparation and development of the manuscript. Both authors contributed substantially to the conceptualisation and development of the project and reviewed and approved the final manuscript. 

## **References** 

1. Reusens, M., et al. (2025). _PersonaBench: Evaluating Persona Consistency in Large Language Models._ Findings of the Association for Computational Linguistics: EMNLP 2025. <u>https://aclanthology.org/2025.fndingsi</u> -emnlp.603/ 

2. Qi, Y., Zhang, X., Zeng, R., Liu, M., Zhou, Z., Miao, D., Yan, B., & Guan, Z. (2026). _Beyond Static Persona Consistency: Dynamic Persona Coherence in LLM Role-Playing._ Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 28942–28956. Association for Computational Linguistics. <u>https://aclanthology.org/2026.acl-long.1336/</u> 

3. Binder, F. J., Chua, J., Korbak, T., Sleight, H., Hughes, J., Long, R., Perez, E., Turpin, M., & Evans, O. (2025). _Looking Inward: Language Models Can Learn About Themselves by Introspection._ International Conference on Learning Representations (ICLR 2025). <u>https://proceedings.iclr.cc/paper_fles/paper/2025/hash/0a6059857ae5c82ea9726ee928i 2a7145-Abstract-Conference.html</u> 

4. Long, R., Sebo, J., Butlin, P., Finlinson, K., Fish, K., Harding, J., Pfau, J., Sims, T., Birch, J., & Chalmers, D. (2024). _Taking AI Welfare Seriously._ arXiv. <u>https://arxiv.org/abs/2411.00986</u> 

5. Meng, K., Bau, D., Andonian, A., & Belinkov, Y. (2022). Locating and Editing Factual Associations in GPT. _Advances in Neural Information Processing Systems 35 (NeurIPS 2022)._ <u>https://arxiv.org/abs/2202.05262</u> 

6. Parisi, G. I., Kemker, R., Part, J. L., Kanan, C., & Wermter, S. (2019). Continual Lifelong Learning with Neural Networks: A Review. _Neural Networks_ , 113, 54–71. <u>https://doi.org/10.1016/j.neunet.2019.01.012</u> 

7. Wang, L., Zhang, X., Su, H., & Zhu, J. (2023). A Comprehensive Survey of Continual Learning: Theory, Method and Application. _arXiv preprint._ <u>https://arxiv.org/abs/2302.00487</u> 

A PREPRINT DIGITAL MINDS (SPRINT) - AUGUST,2026 

12 

## **LLM Usage Statement** 

LLM assistance was used for limited writing support, including improving clarity, grammar, structure, and resolving minor technical or wording issues during the preparation of this report. The research design, implementation, experiments, data collection, analysis, and conclusions were conducted by the research team. All final content and claims were reviewed by the team for accuracy. 

A PREPRINT DIGITAL MINDS (SPRINT) - AUGUST,2026 

13 

