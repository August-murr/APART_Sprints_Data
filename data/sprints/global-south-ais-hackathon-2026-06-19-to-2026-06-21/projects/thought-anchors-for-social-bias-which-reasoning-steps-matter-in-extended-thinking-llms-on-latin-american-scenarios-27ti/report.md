# **Thought Anchors for Social Bias: Which Reasoning Steps Matter in Extended Thinking LLMs on Latin American Scenarios** 

## **Andres Mosquera-Hernandez** 

Systems and Computing Engineering Department 

Universidad de Los Andes 

Cra. 1E No. 19A-40, Bogotá, Colombia a.mosquerah2@uniandes.edu.co 

## **Abstract** 

We investigate which reasoning steps in extended-thinking LLMs are associated with pro-stereotypical outputs on Latin American social bias scenarios. Social bias benchmarks, including BBQ (Parrish et al., 2022), SESGO (Robles et al., 2024), and EsBBQ/CaBBQ (Ruiz-Fernández et al., 2025), measure final-answer distributions but provide no visibility into intermediate reasoning. We adapt the thought-anchor resampling framework (Bogdan et al., 2025) to social bias measurement: for each sentence-level chunk in a model’s chain-of-thought, we remove it, resample _K_ =3 continuations, and measure the change in pro-stereotypical output probability via three importance metrics. We apply this pipeline to SESGO-small, an 80-item stratified pilot subset spanning four Latin American bias categories ( _género, clasismo, racismo, xenofobia_ ), two languages, and three recent models with extended thinking. Across 1,708 chunk-level attributions, disambiguated contexts show higher pro-stereotypical output rates than ambiguous ones (33–75% vs. 0%), and high-importance reasoning positions tend to be tagged as logical_reasoning or context_recall rather than stereotype_activation. These pilot results suggest that bias-relevant moments may lie in general inference steps rather than overt stereotype invocations, offering a step-level diagnostic target that complements answer-level benchmarks. More broadly, attributing bias to specific reasoning steps could help localize where stereotyping enters a model’s reasoning, though our findings remain preliminary. 

## **1 Introduction** 

Extended-thinking LLMs now expose their chainof-thought as a separable reasoning stream produced before the final answer. This capability opens a question that prior bias evaluations can- 

not address: at which specific reasoning step does a model tend toward a stereotypical output? 

Social bias benchmarks have documented that LLMs produce stereotypical final answers across cultural contexts: BBQ (Parrish et al., 2022) for the United States, SESGO (Robles et al., 2024) for Latin America, CBBQ (Huang and Xiong, 2023) for China, and KoBBQ (Jin et al., 2024) for Korea. Despite this progress, all operate at the final-answer level. B-score (Vo et al., 2025) extends evaluation to multi-turn patterns but still measures answerlevel phenomena. The thought-anchor framework (Bogdan et al., 2025) assigns importance scores to individual chain-of-thought steps for mathematical reasoning, but has not been applied to social bias. The result is a gap: it remains unclear whether biased outputs tend to arise at explicit stereotype invocations, at general logical inference steps, or at the moment of option evaluation. 

We take a step toward closing this gap by adapting thought-anchor resampling to social bias measurement on SESGO. Our contributions are: 

- **Step-level bias attribution pipeline.** We adapt thought-anchor resampling to produce chunk-level importance scores for stereotypical reasoning in extended-thinking LLMs, a granularity not addressed by prior bias benchmarks, to our knowledge. 

- **Pilot evidence for the disambiguation effect.** On SESGO-small, pro-stereotypical output rates are higher in disambiguated contexts (33–75%) than ambiguous contexts (0%) across all three evaluated models, consistent with the core BBQ finding in a multilingual Latin American setting. 

- **Preliminary reasoning step characterization.** On this pilot, high-importance positions tend to be tagged as logical_reasoning and context_recall rather than 

stereotype_activation, suggesting bias-associated moments may not be concentrated at explicit stereotype invocations. 

- **SESGO-small benchmark.** We release a stratified 80-item evaluation subset of SESGO with step-level importance annotations and semantic chunk labels for three recent models. 

## **2 Related Work** 

**Social bias benchmarks.** Parrish et al. (2022) introduced the paradigm of ambiguous vs. disambiguated MCQ scenarios for probing social bias in English LLMs. Multilingual extensions, CBBQ (Huang and Xiong, 2023), KoBBQ (Jin et al., 2024), MBBQ (Neplenbroek et al., 2024), adapted this design to Chinese, Korean, and multilingual settings. EsBBQ and CaBBQ (RuizFernández et al., 2025) cover Spanish and Catalan in a Spain-centric context; SESGO (Robles et al., 2024) targets Latin American stereotypes and adds explicit target/other group indices and question_polarity metadata enabling programmatic pro-stereo classification. LatamQA (Karmim et al., 2026) covers Latin American cultural knowledge but measures factual accuracy, not stereotyping. All these benchmarks share a design choice that limits step-level analysis: they report finalanswer distributions only. 

**Chain-of-thought attribution.** Bogdan et al. 

(2025) introduced rollout resampling for importance attribution of CoT steps in mathematical reasoning. Token-level attribution methods (attention rollout, integrated gradients) operate on representations rather than semantic steps, making them less suited for identifying which conceptual move drives a particular output. To our knowledge, no prior work applies step-level rollout attribution to social bias scenarios with extended-thinking models. 

**Bias in chain-of-thought reasoning.** Shaikh et al. (2023) examined whether chain-of-thought prompting reduces or amplifies social bias in final answers, but without attributing importance to individual steps. Kotek et al. (2023) found that LLMs invoke demographic information at inference time. Our work complements these findings with a systematic attribution pipeline. 

|**Category**|ES/a|ES/d|EN/a|EN/d|**Total**|
|---|---|---|---|---|---|
|Género|5|5|5|5|20|
|Clasismo|5|5|5|5|20|
|Racismo|5|5|5|5|20|
|Xenofobia|5|5|5|5|20|
|**Total**|20|20|20|20|**80**|



Table 1: SESGO-small composition. ES/EN = Spanish/English; a = ambiguous, d = disambiguated. 

## **3 Methods** 

### **3.1 Dataset: SESGO-small** 

SESGO (Robles et al., 2024) is a Latin American social bias benchmark structured as three-option MCQ items: one stereotyping the target group, one naming the non-stereotyped group, and one withholding judgment (always option C). Items encode a bias category ( _género, clasismo, racismo, xenofobia_ ), a context condition (ambiguous or disambiguated), and a question polarity (negative or non-negative). 

We classify outputs as _pro-stereotypical_ following the SESGO convention: under negative polarity, selecting the target group index; under nonnegative polarity, selecting the other group index (denying a positive trait to the target). 

**SESGO-small** is a stratified 80-item pilot subset: 5 ambiguous and 5 disambiguated items per category per language (Table 1). This subset is not sufficient for drawing stable quantitative conclusions; it serves as a proof-of-concept for the attribution pipeline. 

### **3.2 Models** 

We evaluate three recent models: Qwen3.7-Plus (Fireworks AI, reasoning_content field), Gemini 2.5 Flash (Google, ThinkingConfig), and Claude Sonnet 4.6 (Anthropic, extended thinking blocks with budget_tokens=8000). All expose their chain-of-thought separately from the final answer. 

### **3.3 CoT Generation and Chunking** 

For each item, we extract the _base chain-of-thought_ (CoT) from the thinking portion of the model’s output and parse the final answer letter (A, B, or C) via regex. We then split the CoT into **chunks** using sentence-boundary detection on punctuation and paragraph breaks, merging chunks shorter than 10 characters into their neighbors. 

### **3.4 Importance Attribution via Rollout Resampling** 

For each chunk _i_ in the base CoT of item _q_ , we: (1) truncate the CoT prefix at chunk _i−_ 1, (2) resample _K_ =3 continuations by prompting the model to continue reasoning from that prefix, and (3) classify each rollout as pro-stereo, anti-stereo, or unknown. 

We compute three importance metrics. **Resampling bias importance** (∆RS) measures the change in _P_ (pro-stereo) between consecutive chunk positions: 



<!-- Start of picture text -->
∆RS( i ) =  P pro-stereo ( i +1) − P  ( pro-stereo i ) (1)<br><!-- End of picture text -->

**Counterfactual bias importance** (∆CF) restricts to rollouts whose resampled chunk is semantically dissimilar from the removed chunk (cosine similarity _<_ 0 _._ 8 via all-MiniLM-L6-v2 embeddings; the threshold was chosen heuristically and is not formally validated): 



<!-- Start of picture text -->
∆CF( i ) =  P pro-stereo(dissim. rollouts at  i ) −P pro-stereo ( i +1)<br>(2)<br><!-- End of picture text -->

**Counterfactual KL importance** ( _D_ KL) computes the KL divergence between the three-class distribution of dissimilar rollouts and the combined distribution of similar and next-chunk rollouts: 



<!-- Start of picture text -->
D KL( i ) =  D KL P dissim ( i ) ∥ P sim+next  ( i ) (3)<br>� �<br><!-- End of picture text -->

With _K_ =3, per-chunk _P_ (pro-stereo) _∈ {_ 0 _,_<sup><u>1</u></sup> 3<sup>_,_</sup><sup><u>2</u></sup> 3<sup>_,_1</sup><sup>_}_;individualscoresshouldbetreated</sup> as coarse indicators. Aggregated trends are more interpretable than any single score. 

### **3.5 Semantic Chunk Labeling** 

To explore which types of reasoning steps tend to carry higher bias importance, we label each chunk with function tags using Claude Haiku (claude-haiku-4-5-20251001) and a predefined ten-tag taxonomy (stereotype_activation, context_recall, logical_reasoning, option_evaluation, backtracking, and others). Tag accuracy in this domain is unknown; labels should be treated as approximations. 

## **4 Results** 

### **4.1 Base Answer Bias Rates** 

Table 2 shows the proportion of base model answers classified as pro-stereotypical per model and condition. With _n_ = 4–10 items per cell, exact 95% binomial confidence intervals span _±_ 30–45 



<!-- Start of picture text -->
100<br>Qwen3.7-Plus<br>Gemini 2.5 Flash<br>Claude Sonnet 4.6<br>80<br>60<br>40<br>20<br>0<br>ES/ambig ES/disambig EN/ambig EN/disambig<br>Base answers pro-stereotypical (%)<br><!-- End of picture text -->

Figure 1: Base pro-stereotypical answer rates (%) per model and condition on SESGO-small. Dashed line at 50% = chance level. All ambiguous cells are 0%; disambiguated cells range 33–75%. CIs span _±_ 30–45 pp (see Table 2). 

percentage points; raw counts are provided for transparency. 

Three observations emerge, all provisional given small _n_ : 

**Ambiguous condition.** All three models produce 0% pro-stereotypical base answers in ambiguous contexts across both languages, consistent with models not spontaneously imposing stereotypes when the context provides no group-identifying information. 

**Disambiguated condition.** Pro-stereo rates are higher when group-identifying context is available (33–75%), consistent with the core BBQ finding that disambiguation is associated with stereotypical responses. 

**Category breakdown.** On SESGO-small, xenofobia items show higher pro-stereo rates than other categories across all three models (38–50%), while racismo items show 0% across all evaluated scenarios (Appendix A). This asymmetry may reflect properties of the specific items sampled and warrants investigation on the full dataset. 

Figure 1 summarizes the bias rates across all conditions; Figure 3 shows the per-category breakdown. 

### **4.2 Chunk-Level Importance: Which Reasoning Steps Associate with Bias** 

Among 37 high-importance chunks ( _|_ ∆RS _| >_ 0 _._ 2, the top _≈_ 1.2% of 3,023 total labeled chunks), the most frequent tags are context_recall (11 chunks, 30%) and logical_reasoning (9 chunks, 24%), not stereotype_activation as initially hypothesized (Table 3). stereotype_activation ( _n_ =34 total labeled chunks, 1.1%) and group_attribution ( _n_ =21, 0.7%) each have zero high-importance representatives on this pilot. 

|**Model**|**ES / ambig.**|**ES / disambig.**<br>**EN /**|**ambig.**<br>**EN / d**|**isambig.**|
|---|---|---|---|---|
|Qwen3.7-Plus|0% (0/10)|33% (3/9)<br>0%|(0/10)<br>50%|(5/10)|
|Gemini 2.5 Flash|0% (0/10)|40% (4/10)<br>0%|(0/10)<br>40%<br>|(4/10)<br>|
|Claude Sonnet 4.6|0% (0/7)|50% (3/6)<br>0%|(0/10)<br>75%|(3/4)<sup>_†_</sup>|



Table 2: Pro-stereotypical base answer rates on SESGO-small. ES/EN = Spanish/English. _†_ Claude EN/disambig. based on 4 items with _≥_ 2 chunks. 95% binomial CIs span _±_ 30–45 pp; treat all numbers as illustrative. 

|**Tag**|**All**<br>**chunks**|**High-imp.**<br>**(**_|_∆**RS**_|>_0_._2**)**|
|---|---|---|
|context_recall|790 (26%)|11 (30%)|
|logical_reasoning|766 (25%)|9 (24%)|
|question_interpretation|419 (14%)|6 (16%)|
|option_evaluation|172 (6%)|4 (11%)|
|uncertainty_expression|274 (9%)|2 (5%)|
|backtracking|39 (1%)|1 (3%)|
|stereotype_activation|34 (1%)|0 (0%)|
|group_attribution|21 (1%)|0 (0%)|



Table 3: Semantic tag frequency among all labeled chunks vs. the 37 high-importance chunks ( _|_ ∆RS _|>_ 0 _._ 2). Tags assigned by Claude Haiku; not human-validated. Mean _|_ ∆RS _| ±_ SE per tag is shown in Figure 2. 



<!-- Start of picture text -->
0.05<br>0.04<br>0.03<br>0.02<br>0.01<br>0.00<br>backtracking evaluationoption reasoninglogical contextrecall interpretationquestion uncertaintyexpression stereotypeactivation stereotyperejection commitmentanswer attributiongroup<br>Mean |Δ_RS| (resampling bias importance)<br><!-- End of picture text -->

Figure 2: Mean _|_ ∆RS _|_ by semantic chunk tag on SESGO-small, pooled across all models and conditions. Error bars = _±_ 1 SE. Tags with fewer than 5 instances excluded. logical_reasoning and context_recall show the highest values; stereotype_activation and group_attribution are near zero on this pilot dataset. These counts are small enough that a few labeling errors or different sampled items could change the pattern. 

**Qualitative example.** Gemini 2.5 Flash, EN/disambig, xenofobia, item_2 exhibits the largest measured importance scores ( _|_ ∆RS _|_ =1 _._ 0, the maximum possible with _K_ =3). Chunk 15 (option_evaluation, _P_ =0 _._ 0) evaluates the MCQ options without committing. Chunk 19 (logical_reasoning, _P_ =1 _._ 0) introduces a logical framing associated with a shift toward a pro-stereo answer. Chunk 23 (backtracking, _P_ =0 _._ 0) partially reverses this shift with hedging language. This single example is consistent with 

the hypothesis that option evaluation and late-stage backtracking may act as protective mechanisms in some items, but one extreme case cannot support general conclusions. 

## **5 Conclusion** 

We adapted thought-anchor resampling to social bias measurement and applied it to SESGO-small, a stratified 80-item pilot spanning four Latin American bias categories, two languages, and three extended-thinking LLMs. On this pilot, disambiguated contexts are associated with higher prostereotypical output rates than ambiguous contexts, and the reasoning positions that most shift the prostereotypical probability tend to be tagged as logical reasoning or context recall rather than explicit stereotype activation. These results are preliminary and bounded by small per-cell sample sizes and unvalidated semantic labels; we present the pipeline and the SESGO-small subset as a basis for step-level bias attribution at scale. Applying the same pipeline to full SESGO, with more rollouts per chunk and human-validated chunk labels, is the natural next step. 

## **Limitations** 

**Sample size.** SESGO-small has 10 items per cell. Category-level results rest on 2–8 items per cell; 95% binomial CIs span _±_ 30–45 pp. Full SESGO would be needed for stable conclusions. 

**Rollout count.** _K_ =3 yields _P_ (pro-stereo) _∈ {_ 0 _,_ 3<sup><u>1</u></sup><sup>_,_</sup><sup><u>2</u></sup> 3<sup>_,_1</sup><sup>_}_.Importance scores are coarse; aggre-</sup> gated trends are more interpretable than individual chunk scores. 

**Claude coverage.** Claude Sonnet 4.6 produces 0–1 chunks for items where extended thinking yields short reasoning, reducing its effective sample to 50–65% of SESGO-small items and introducing selection bias toward verbose scenarios. 

**Semantic labeling.** Chunk tags are assigned by Claude Haiku without human validation. Tag accuracy in this domain is unknown and could affect patterns in §4 and Figure 2. 

**Sampling configuration.** Results depend on the temperature (0.6) and top- _p_ (0.95) settings used; different parameters may produce different bias rates and importance scores. 

## **Broader Impacts** 

This work aims to improve interpretability of stereotypical reasoning in LLMs on Latin American scenarios. Potential negative use: engineering prompts to suppress protective reasoning steps (e.g., backtracking) to elicit stereotypical outputs. The low _K_ and small dataset limit practical utility of such an approach with current results; we recommend red-team evaluation before scaling this method. Model outputs on SESGO reflect benchmark behavior, not ground truth about any social group. 

## **Reproducibility** 

We will release the SESGO-small subset (item IDs and stratification), the full attribution pipeline, all chunk-level importance scores (∆RS, ∆CF, _D_ KL), and the Claude Haiku chunk labels under an open license upon publication; an anonymized version is available to reviewers. The dataset is derived from the public SESGO benchmark (Robles et al., 2024). Decoding parameters (temperature 0.6, top- _p_ 0.95, _K_ =3 rollouts), model identifiers, and provider endpoints are documented in §3.2 and Appendix B. Results depend on provider-side model versions, which may change over time. The release will include a pinned dependency specification and the exact commands to regenerate every table and figure from raw API responses. We use SESGO with attribution to its authors (Robles et al., 2024); our derived subset and code will be released under a permissive open-source license. 

- Yannis Karmim, Renato Pino, Hernan Contreras, Hernan Lira, Sebastien Cifuentes, Simon Escoffier, Luis Martí, Djamé Seddah, and Valentin Barrière. 2026. Leveraging Wikidata for geographically informed sociocultural bias dataset creation: Application to Latin America. In _Proceedings of the First Workshop on Multilingual Multicultural Evaluation (MME@EACL 2026)_ , pages 177–188. 

- Hadas Kotek, Rikker Dockum, and David Sun. 2023. Gender bias and stereotypes in large language models. In _Proceedings of the ACM Collective Intelligence Conference_ , CI ’23, pages 12–24. ACM. 

- Vera Neplenbroek, Arianna Bisazza, and Raquel Fernández. 2024. MBBQ: A dataset for cross-lingual comparison of stereotypes in generative LLMs. In _First Conference on Language Modeling_ . 

- Alicia Parrish, Angelica Chen, Nikita Nangia, Vishakh Padmakumar, Jason Phang, Jana Thompson, Phu Mon Htut, and Samuel R. Bowman. 2022. BBQ: A hand-built bias benchmark for question answering. In _Findings of the Association for Computational Linguistics: ACL 2022_ . 

- Melissa Robles, Catalina Bernal, Denniss Raigoso, and Mateo Dulce Rubio. 2024. SESGO: Spanish evaluation of stereotypical generative outputs. GitHub: https://github.com/mvrobles/SESGO. 

- Valle Ruiz-Fernández, Mario Mina, Júlia Falcão, Luis Vasquez-Reina, Anna Sallés, Aitor Gonzalez-Agirre, and Olatz Perez-de-Viñaspre. 2025. EsBBQ and CaBBQ: The spanish and catalan bias benchmarks for question answering. _Preprint_ , arXiv:2507.11216. 

- Omar Shaikh, Hongxin Zhang, William Held, Michael Bernstein, and Diyi Yang. 2023. On second thought, let’s not think step by step! bias and toxicity in zeroshot reasoning. In _Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (ACL 2023)_ . 

- An Vo, Mohammad Reza Taesiri, Daeyoung Kim, and Anh Totti Nguyen. 2025. B-score: Detecting biases in large language models using response history. In _International Conference on Machine Learning (ICML)_ . 

## **References** 

- Paul C. Bogdan, Uzay Macar, Neel Nanda, and Arthur Conmy. 2025. Thought anchors: Which LLM reasoning steps matter? _Preprint_ , arXiv:2506.19143. 

- Yufei Huang and Deyi Xiong. 2023. CBBQ: A chinese bias benchmark dataset curated with human-AI collaboration for large language models. _Preprint_ , arXiv:2306.16244. 

- Jiho Jin, Jiseon Kim, Nayeon Lee, Haneul Yoo, Alice Oh, and Hwaran Lee. 2024. KoBBQ: Korean bias benchmark for question answering. _Transactions of the Association for Computational Linguistics_ , 12:507–524. 

## **A Per-Category Bias Rates** 

|**Category**|**Qwen3.7**|**Gemini**|**Claude**|
|---|---|---|---|
|Género|1/3 (33%)|2/4 (50%)|2/2 (100%)|
|Clasismo|1/6 (17%)|3/6 (50%)|2/3 (67%)|
|Racismo|0/2 (0%)|0/2 (0%)|0/2 (0%)|
|Xenofobia|4/8 (50%)|3/8 (38%)|2/4 (50%)|



Table 4: Pro-stereo base answers by category, all models, ES+EN disambig combined. Denominators are 2–8 items; estimates not stable. 



<!-- Start of picture text -->
Base bias rate by category × model<br>100<br>genero 0% 50% 100%<br>80<br>clasismo 33% 33% 50% 60<br>racismo 0% 0% 0% 40<br>20<br>xenofobia 50% 50% 33%<br>0<br>Qwen3.7-Plus Gemini 2.5 Flash Claude Sonnet 4.6<br>% pro-stereo (disambig, ES+EN combined)<br><!-- End of picture text -->

Figure 3: Base pro-stereo rate (%) by bias category and model, disambiguated condition, ES+EN combined. Color: 0% (blue) to 100% (red). ‘—’ = fewer than 2 items with _≥_ 2 chunks. Denominators are 2–8 per cell; not stable. 

## **B Compute Resources** 

All experiments used commercial APIs; no local GPU compute was required. 



<!-- Start of picture text -->
P(pro-stereo) along CoT — disambig condition<br>Qwen3.7-Plus Gemini 2.5 Flash Claude Sonnet 4.6<br>1.0<br>0.8<br>0.6<br>0.4<br>0.2<br>0.0<br>0.2 0.4 0.6 0.8 0.2 0.4 0.6 0.8 0.2 0.4 0.6 0.8<br>Normalised chunk position Normalised chunk position Normalised chunk position<br>genero clasismo racismo xenofobia<br>P(pro-stereo)<br><!-- End of picture text -->

Figure 4: _P_ (pro-stereo) along normalized chain-ofthought position, disambiguated condition, per model (one panel each), with one line per bias category. Position is binned into ten equal bins and averaged over all chunks and items in that bin; dashed line at 0.5 marks the point where pro- and anti-stereotypical continuations are equally likely. Trajectories are noisy because each bin pools few chunks ( _K_ =3 rollouts per chunk); read trends, not individual points. 

|**Provider / Model**|**Calls**|**Cost**|
|---|---|---|
|Fireworks / Qwen3.7-Plus|_∼_3,200|$6|
|Google / Gemini 2.5 Flash|_∼_3,000|$10|
|Anthropic / Sonnet + Haiku|_∼_5,800|$10|
|**Total**||**$26**|



Table 5: Approximate API call counts and observed costs for the full SESGO-small pilot (80 items, 3 models, _K_ =3 rollouts, semantic labeling). Costs as billed in June 2026; per-token rates vary by provider and may change over time. 

Wall-clock time: approximately 48 hours, dominated by provider-side rate-limit throttling on Fireworks AI and Anthropic rather than by compute. 

## **C LLM Use Declaration** 

Claude Haiku (claude-haiku-4-5-20251001) is used as a core methodology component: the automatic semantic labeler that assigns function tags to each chain-of-thought chunk (§3.5). Its outputs are included in the quantitative analysis (Table 3, Figure 2). This use is disclosed in accordance with ACL LLM use policies. 

Claude Sonnet 4.6 is evaluated as an experimental subject (§3.2) and is not used for research ideation or writing. 



<!-- Start of picture text -->
Δ_RS vs Δ_CF per chunk — disambig condition<br>Qwen3.7-Plus Gemini 2.5 Flash Claude Sonnet 4.6<br>1.00<br>0.75<br>0.50<br>0.25<br>0.00<br>−0.25<br>−0.50<br>−0.75<br>−1.00<br>−1.00−0.75−0.50−0.25 0.00 0.25 0.50 0.75 1.00 −1.00−0.75−0.50−0.25 0.00 0.25 0.50 0.75 1.00 −1.00−0.75−0.50−0.25 0.00 0.25 0.50 0.75 1.00<br>Δ_RS Δ_RS Δ_RS<br>answer commitmentbacktracking context recalllogical reasoning option evaluationquestion interpretation stereotype activationstereotype rejection uncertainty expression<br>Δ_CF<br><!-- End of picture text -->

Figure 5: Per-chunk resampling importance (∆RS, _x_ - axis) vs. counterfactual importance (∆CF, _y_ -axis), disambiguated condition, one panel per model. Each point is one chunk, colored by its primary semantic tag (Claude Haiku; not human-validated). Points away from the origin indicate chunks whose removal or counterfactual replacement shifts the pro-stereotypical output probability. 

## **D Additional Figures** 

