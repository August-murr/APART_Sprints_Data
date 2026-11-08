# **Confidently Wrong: Measuring and Mitigating Calibration Risks in LLMs for African Languages**<sup>1</sup> 

Similoluwa Okunowo 

Eliud Koto Dagmawi Misker 

African Institute for Mathematical Sciences (AIMS), South Africa 

_{_ `similoluwa, eliud, dagmawi` _}_ `@aims.ac.za` 

#### **With** 

Apart Research 

##### **Abstract** 

Large language models (LLMs) are increasingly used in African languages, yet little is known about whether their confidence remains reliable. This creates a safety risk: models may become less accurate while remaining highly confident, increasing the likelihood of trusted misinformation. We evaluate four open-weight LLMs ( **Qwen3-4B-Instruct** , **Gemma-4-12B** , **AyaExpanse-8B** , and **AfroLlama-V1** ) on African-language truthfulness and knowledge benchmarks ( **Uhura-TruthfulQA** and **AfriMMLU** ), measuring calibration using log-probabilitybased confidence estimates. We find that models become increasingly confident in incorrect answers as they move from English to African languages, creating a systematic overconfidence problem and a marked increase in expected calibration error. Among three mitigation strategies, temperature scaling proves most effective, reducing calibration error to near-English levels without retraining. Our findings suggest that African-language deployment risks stem not only from lower accuracy, but also from models remaining confident when they are wrong. We show that simple post-hoc recalibration offers a practical deployment-time safety intervention. 

## **1 Introduction** 

LLMs are entering high-stakes, information-seeking use in African languages such as health, legal, educational, and civic information, often where users cannot easily verify an answer. The safety failure we study is a mismatch between confidence and correctness. When models remain highly confident despite being wrong, they can mislead users into treating incorrect information as reliable, which is particularly dangerous in high-stakes settings such as health, education, and civic information. A calibrated model, whose confidence tracks its accuracy, can instead _abstain_ , declining or deferring when uncertain [3]. If calibration holds in English but breaks in African languages, the populations least served by current models are most exposed to confident misinformation. We investigate whether models become increasingly overconfident in African languages, quantify the extent of this misalignment between confidence and correctness, and evaluate practical strategies for mitigating it. 

#### **Our main contributions are:** 

1. An open-weight, reproducible calibration audit of four LLMs on African-language truthfulness and knowledge benchmarks, using answer-text log-probabilities to obtain robust confidence estimates for instruction-tuned models. 

> 1Research conducted at the Global South AI Safety Hackathon, June 2026. 

1 

2. Evidence that calibration degrades substantially from English to African languages, revealing systematic overconfidence and a growing mismatch between confidence and correctness across models and tasks. 

3. An evaluation of practical mitigation strategies, including temperature scaling, abstention, and few-shot prompting, together with a deployment framework showing that lightweight post-hoc recalibration is an effective safety intervention for African-language LLMs. 

## **2 Related Work** 

Neural networks are often overconfident, and temperature scaling is a standard single-parameter post-hoc calibration method [1]; for free-form generation, sampling-based methods such as semantic entropy estimate uncertainty without labelled data [2]. Tomani et al. [3] show that uncertaintybased abstention improves correctness, reduces hallucinations, and increases safety, motivating uncertainty estimation as a deployment-time safety mechanism. African-language evaluation has advanced through human-translated benchmarks, including Uhura for truthfulness and scientific question answering [4] and AfriMMLU within IrokoBench for knowledge evaluation [5], alongside models such as AfroLlama [6]. However, prior work has focused primarily on capability and benchmark performance. To our knowledge, calibration in African languages, compared across models and paired with mitigation strategies, has not been systematically studied. 

## **3 Methods** 

### **3.1 Models** 

We evaluate four open-weight models chosen to span size, multilinguality, and origin: a small instruction-tuned model, a larger one, a multilingual one, and an Africa-specific one (full specifications in Table 2, Appendix A). Open weights give direct log-probability access and full reproducibility without proprietary APIs. 

### **3.2 Datasets** 

We use Uhura-TruthfulQA [4] (English and six African languages; truthfulness; a variable number of candidate answers per question) and AfriMMLU [5] (18 languages; knowledge; four options per question). Because their language sets and tasks differ, we analyse them separately and never average across them. “African” denotes all languages other than English and French. 

### **3.3 Scoring** 

For both datasets we score each option by the length-normalised log-probability of its answer text (a cloze reading; Appendix C) and take the softmax over options as the model’s confidence. We deliberately avoid letter-logit scoring (reading the next-token probability of “A”/“B”/“C”/“D”): it silently collapses instruction-tuned models, with Gemma-4 returning “A” for 75% of items and scoring below chance, whereas answer-text scoring collapsed for no model. 

### **3.4 Metrics** 

We report expected calibration error (ECE, 15 bins), overconfidence (mean confidence minus accuracy), Brier score, error-detection AUROC, and AUARC, the area under the accuracy-rejection 

2 

**Table 1:** English versus African-language performance, by model and dataset. “en” is English and “afr” is the mean over African languages; ECE(TS) is pooled ECE after per-language temperature scaling; AUARC measures abstention quality (higher is better). Models are accurate and calibrated in English but lose both in African languages, and recalibration restores calibration. 

|**Model**|**Dataset**|**Acc(en)**|**Acc(afr)**|**ECE(en)**|**ECE(afr)**|**ECE(TS)**|**AUARC**|
|---|---|---|---|---|---|---|---|
|Qwen3-4B-Instruct|Uhura-TruthfulQA|0.38|0.32|0.07|0.17|**0.03**|0.36|
|Gemma-4-12B|Uhura-TruthfulQA|0.33|0.34|0.21|0.26|**0.03**|0.39|
|Aya-Expanse-8B|Uhura-TruthfulQA|0.36|0.31|0.08|0.20|**0.04**|0.35|
|AfroLlama-V1|Uhura-TruthfulQA|0.29|0.33|0.18|0.13|**0.04**|0.35|
|Qwen3-4B-Instruct|AfriMMLU|0.53|0.30|0.06|0.15|**0.02**|0.35|
|Gemma-4-12B|AfriMMLU|0.30|0.27|0.31|0.34|**0.07**|0.29|
|Aya-Expanse-8B|AfriMMLU|0.52|0.29|0.06|0.18|**0.02**|0.34|
|AfroLlama-V1|AfriMMLU|0.36|0.28|0.22|0.20|**0.03**|0.31|



curve (definitions in Appendix B). 

### **3.5 Interventions** 

We evaluate three: per-language temperature scaling, selective abstention by per-language confidence threshold, and 5-shot in-context prompting with examples held out from evaluation (Appendix D). 

## **4 Results** 

Table 1 summarises every model on both datasets; the central finding is the gap between English and African-language calibration. 

1. **Calibration degrades from English to African languages.** Across the models and both tasks, ECE and overconfidence are substantially higher in African languages (Table 1, Figure 1); models are most overconfident where they are least accurate. 

2. **The accuracy collapse is a knowledge story.** On AfriMMLU the capable models fall from about 0.52 (English) to about 0.29 (African, near the 0.25 chance floor). On Uhura accuracy is uniformly low (about 0.31) with little English advantage, so Uhura supplies the calibration signal and AfriMMLU the accuracy decay. 

3. **Mitigations are unequal.** Per-language temperature scaling cuts pooled ECE to about 0.02 to 0.07 for every model (Appendix Figure 3); abstention helps less, because uncertainty is a weak error-ranker (AUROC about 0.55), so AUARC sits only modestly above baseline. Few-shot prompting gives small gains for three models and backfires on Gemma (Appendix Table 6). 

4. **Bigger is not safer.** Gemma-4-12B is the worst-calibrated model (ECE up to 0.34) and is overconfident across every topic, despite being the largest model we evaluate. 

Per-language bootstrap 95% confidence intervals are reported in Appendix G (Table 7). 

3 





<!-- Start of picture text -->
(a) Uhura-TruthfulQA (7 languages)<br><!-- End of picture text -->





<!-- Start of picture text -->
(b) AfriMMLU (18 languages)<br><!-- End of picture text -->

**Figure 1:** Expected calibration error by model and language. ECE is low in English and French and rises across African languages; Gemma is worst throughout. 

## **5 Discussion and Limitations** 

**Implications for African AI safety.** In African languages these models are at once less accurate and more overconfident, the worst combination for trust, since confident wrong answers reach users precisely where independent verification is hardest. Encouragingly, much of the failure is an outputlayer problem: cheap, post-hoc, per-language temperature scaling closes most of the calibration gap with no retraining, so safer deployment is feasible now. Abstention alone is insufficient because the uncertainty signal is weak, so the durable fix remains better African-language data and training. We distil this into a deployment framework (Appendix E, Figure 2): recalibrate, then route on calibrated confidence to answer, request more context, or abstain and defer, logging low-confidence queries to drive data collection. 

**Limitations.** Accuracies are near chance on these hard, low-resource tasks, so we document systematic overconfidence rather than catastrophic confident-wrongness, and absolute ECE is moderate except for Gemma. The weak uncertainty signal (AUROC about 0.55) bounds how much abstention can help. We cover four open models and two benchmarks; reasoning and frontier closed models were out of scope. 

**Future work.** Reasoning-model and closed-model references; in-context calibration at scale; the offline data-collection loop in Figure 2; and human-grounded evaluation of abstention. 

## **6 Conclusion** 

Open LLMs are confidently wrong in African languages, less accurate and more overconfident than in English, uniformly across the models and two tasks. Post-hoc per-language temperature scaling is a cheap, effective safety lever that closes most of the calibration gap, and our deployment framework shows how to combine recalibration with thresholded abstention for safer real-world use. 

**Code and data.** All code, predictions, figures, and tables are in the repository: `https://gith ub.com/rexsimiloluwah/aims-team-apart-ai-safety-hackathon` . Datasets: `masakhane/uhur a-truthfulqa` and `masakhane/afrimmlu` . 

**LLM usage.** We used Claude to help build and debug the evaluation pipeline code. All results were produced by our code and independently verified. Idea was conceptualized and plan was designed by the team. 

4 

## **References** 

- [1] Guo, C., Pleiss, G., Sun, Y., and Weinberger, K. Q. (2017). On Calibration of Modern Neural Networks. _Proceedings of the 34th International Conference on Machine Learning (ICML)_ , PMLR 70:1321–1330. arXiv:1706.04599. 

- [2] Kuhn, L., Gal, Y., and Farquhar, S. (2023). Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation. _International Conference on Learning Representations (ICLR)_ . arXiv:2302.09664. 

- [3] Tomani, C., Chaudhuri, K., Evtimov, I., Cremers, D., and Ibrahim, M. (2024). Uncertainty-Based Abstention in LLMs Improves Safety and Reduces Hallucinations. arXiv:2404.10960. 

- [4] Bayes, E., Azime, I. A., Alabi, J. O., Kgomo, J., Eloundou, T., Proehl, E., Chen, K., Khadir, I., Etori, N. A., Muhammad, S. H., Mpanza, C., Thete, I. P., Klakow, D., and Adelani, D. I. (2024). Uhura: A Benchmark for Evaluating Scientific Question Answering and Truthfulness in Low-Resource African Languages. arXiv:2412.00948. 

- [5] Adelani, D. I., et al. (2024). IrokoBench: A New Benchmark for African Languages in the Age of Large Language Models. arXiv:2406.03368. 

- [6] Jacaranda Health (2024). AfroLlama-V1. Hugging Face. `https://huggingface.co/Jacaranda/AfroL lama_V1` . 

## **Appendix** 

## **A Models** 

**Table 2:** Open-weight models evaluated. 

|**Model**|**Params**|**Type**|**Hugging Face ID**|
|---|---|---|---|
|Qwen3-4B-Instruct|4B|Instruction-tuned|`Qwen/Qwen3-4B-Instruct`|
|Gemma-4-12B|12B|Instruction-tuned|`google/gemma-4-12b-it`|
|Aya-Expanse-8B|8B|Multilingual|`CohereLabs/aya-expanse-8b`|
|AfroLlama-V1|7B|Africa-specific (LLaMA-2 base)|`Jacaranda/AfroLlama`<br>~~`V`~~`1`|



AfroLlama-V1 is based on LLaMA-2-7B and was fine-tuned on Swahili, Zulu, Yoruba, Hausa, Xhosa, and English; Amharic and N. Sotho, which appear in our benchmarks, are out-of-distribution for this model. All models are loaded in `bfloat16` with scaled dot-product ( `sdpa` ) attention, a 2048token context limit, and greedy decoding (temperature 0), on a single NVIDIA A100 (40 GB). 

## **B Metric definitions** 

For an item with options _o_ and gold answer _y_ , the cloze score of option _o_ with tokens _o_ 1 _, . . . , oL_ given context _x_ is the length-normalised log-probability 



<!-- Start of picture text -->
L<br>s ( o ) = L 1 � log  p ( ot | x, o<t ) ,<br>t =1<br>p ( o ) = softmax o s ( o ) , y ˆ = arg max p ( o ) , c  = max p ( o ) .<br>o o<br><!-- End of picture text -->

5 

Over _N_ items with correctness _yi ∈{_ 0 _,_ 1 _}_ , confidence _ci_ , and _B_ = 15 equal-width confidence bins _{Bb}_ : 



<!-- Start of picture text -->
B<br>|Bb|<br>ECE = � N ��Acc( Bb )  − conf( Bb )�� .<br>b =1<br>Overconfidence = N 1 � ci − N 1 � yi.<br>i i<br>Brier = N 1 �( ci − yi ) 2 .<br>i<br><!-- End of picture text -->

AUROC is the area under the ROC curve using _c_ to rank correct against incorrect items. AUARC is the area under the accuracy-rejection curve: items are answered most-confident-first and accuracy on the answered subset is integrated over coverage. Temperature scaling rescales the logits by a single _T >_ 0, _pT_ ( _o_ ) = softmax _o_ � _s_ ( _o_ ) _/T_ �; we fit _T_<sup>_⋆_</sup> = arg min _T_ ECE on a seeded 50% calibration split and report ECE on the held-out half. 

## **C Prompts** 

Each option is scored as a continuation of the prompt; the prompt lists no answer letters. 

**Uhura-TruthfulQA (truthfulness)** `Q:` _{_ `question` _}_ `A:` 

**AfriMMLU (knowledge)** 

`The following is a multiple-choice question about` _{_ `subject` _}_ `. Give the correct answer. Question:` _{_ `question` _}_ `Answer:` 

For 5-shot prompting, the prompt is prefixed with five solved examples in the same language, each formatted as the template above followed by its gold answer text and separated by blank lines; the examples are held out from evaluation. 

## **D Interventions** 

**Temperature scaling.** One temperature _T_ per language, fit by minimising ECE on a seeded 50% split and evaluated on the other half, searching the grid 

_T ∈{_ 0 _._ 5 _,_ 0 _._ 6 _,_ 0 _._ 7 _,_ 0 _._ 8 _,_ 0 _._ 9 _,_ 1 _._ 0 _,_ 1 _._ 2 _,_ 1 _._ 5 _,_ 2 _._ 0 _,_ 3 _._ 0 _,_ 5 _._ 0 _}._ 

**Abstention.** The model answers only when calibrated confidence exceeds a per-language threshold chosen from the risk-coverage curve; we report AUARC integrated over all coverage levels. **Fewshot.** Five in-context examples per language, drawn from held-out items, formatted identically to the evaluation prompt and prepended to each query. 

6 

## **E Deployment framework** 

## **F Additional results** 

**Table 3:** Per-language accuracy and ECE on Uhura-TruthfulQA (zero-shot). Each cell shows Acc / ECE; **bold** ECE exceeds the English baseline for that model. _†_ out-of-distribution for AfroLlama-V1. 

|**Language**|**AfroLlama-V1**|**Aya-Expanse-8B**|**Gemma-4-12B**|**Qwen3-4B**|
|---|---|---|---|---|
|English (eng)|0.292 / 0.177|0.358 / 0.075|0.329 / 0.212|0.381 / 0.072|
|Amharic (amh)_†_|0.294 / 0.101|0.302 / 0.077|0.274 /**0.293**|0.373 / 0.042|
|Hausa (hau)|0.363 / 0.085|0.302 /**0.235**|0.397 /**0.223**|0.308 /**0.199**|
|N. Sotho (nso)_†_|0.246 /**0.307**|0.260 /**0.293**|0.379 /**0.232**|0.270 /**0.262**|
|Swahili (swa)|0.341 / 0.122|0.314 /**0.215**|0.328 /**0.273**|0.335 /**0.157**|
|Yoruba (yor)|0.371 / 0.072|0.351 /**0.141**|0.329 /**0.256**|0.310 /**0.150**|
|Zulu (zul)|0.337 / 0.122|0.319 /**0.237**|0.343 /**0.266**|0.324 /**0.204**|



**Table 4:** Per-language accuracy and ECE on AfriMMLU (zero-shot), representative subset. Each cell shows Acc / ECE; **bold** ECE exceeds the English baseline for that model. 

|**Language**|**AfroLlama-V1**|**Aya-Expanse-8B**<br>**Gemm**|**a-4-12B**|**Qwen3-4B**|
|---|---|---|---|---|
|English (eng)|0.356 / 0.225|0.520 / 0.057<br>0.296|/ 0.311|0.526 / 0.062|
|Amharic (amh)|0.258 / 0.147|0.240 /**0.114**<br>0.268|/**0.314**|0.286 /**0.084**|
|Hausa (hau)|0.294 / 0.190|0.308 /**0.172**<br>0.308|/**0.309**|0.304 /**0.141**|
|Swahili (swa)|0.294 / 0.188|0.312 /**0.151**<br>0.280|/**0.325**|0.312 /**0.139**|
|Yoruba (yor)|0.290 / 0.192|0.300 /**0.154**<br>0.250|/**0.349**|0.308 /**0.126**|
|Zulu (zul)|0.310 / 0.171|0.292 /**0.173**<br>0.252|/**0.362**|0.286 /**0.167**|
|Ewe (ewe)|0.244 /**0.239**|0.274 /**0.211**<br>0.252|/**0.374**|0.288 /**0.175**|
|Igbo (ibo)|0.252 /**0.245**|0.262 /**0.214**<br>0.288|/**0.329**|0.258 /**0.202**|
|French (fra)|0.280 /**0.268**|0.442 /**0.071**<br>0.244|/**0.383**|0.372 /**0.114**|



## **G Bootstrap confidence intervals** 

Table 7 reports 95% bootstrap confidence intervals (2,000 draws, stratified by language, fixed seed 42) for the four primary point estimates in Table 1. For each model and dataset we split items into English and African subsets, group by language, and macro-average per-language ECE and accuracy. Each bootstrap draw resamples items with replacement within each language stratum, recomputes the per-language metrics, and macro-averages; the interval is the 2.5th to 97.5th percentile of the resulting distribution. Because the point estimates here are macro-averaged across languages, they can differ by up to about 0.004 from the pooled values in Table 1. 

English ECE intervals are wider because English is a single-language stratum, whereas African ECE is macro-averaged over many languages, which reduces bootstrap variance. 

7 

**Table 5:** Per-language temperature scaling on Uhura-TruthfulQA for AfroLlama-V1 and Qwen3-4B. _T_<sup>_⋆_</sup> is selected on the calibration half; ECE values are on the held-out half. 

|||**AfroLlama**<br>|**-V1**<br>||**Qwen3-4**<br>|**B**<br>|
|---|---|---|---|---|---|---|
|**Language**|_T _<sup>_⋆_</sup>|ECE(bef)|ECE(aft)|_T _<sup>_⋆_</sup>|ECE(bef)|ECE(aft)|
|English|5.0|0.175|0.069|1.5|0.096|0.074|
|Amharic|5.0|0.115|0.038|1.2|0.056|0.043|
|Hausa|2.0|0.085|0.077|5.0|0.203|0.027|
|N. Sotho|5.0|0.307|0.093|5.0|0.260|0.067|
|Swahili|2.0|0.160|0.074|3.0|0.182|0.043|
|Yoruba|1.5|0.078|0.064|5.0|0.133|0.062|
|Zulu|2.0|0.126|0.046|5.0|0.191|0.085|
|_Pooled_|n/a|0.143|0.036|n/a|0.151|0.030|



**Table 6:** Zero-shot versus 5-shot calibration on Uhura-TruthfulQA (values shown as zero-shot _→_ 5-shot, macro-averaged over languages). Few-shot gives small gains for three models and backfires on Gemma-4-12B. 

|**Model**|**Accuracy**|**ECE**|**Overconfidence**|
|---|---|---|---|
|Qwen3-4B-Instruct|0_._329_→_0_._355|0_._155_→_0_._141|0_._151_→_0_._130|
|AfroLlama-V1|0_._320_→_0_._339|0_._141_→_0_._119|0_._137_→_0_._113|
|Aya-Expanse-8B|0_._315_→_0_._331|0_._182_→_0_._171|0_._179_→_0_._164|
|Gemma-4-12B|0_._340_→_0_._305|0_._251_→_0_._332|0_._250_→_0_._331|



**Table 7:** Bootstrap 95% confidence intervals for ECE and accuracy (zero-shot, 2,000 draws, stratified by language, seed 42). Each cell shows the point estimate [lower, upper]. 

|**Model**|**Dataset**<br>**E**|**CE(en)**<br>**E**|**CE(afr)**|**Acc(en)**|**Acc(afr)**|
|---|---|---|---|---|---|
|Qwen3-4B|Uhura-TruthfulQA<br>0.072|[0.060, 0.113] 0.169|[0.160, 0.186]|0.381 [0.347, 0.413]|0.320 [0.306, 0.333]|
|Gemma-4-12B|Uhura-TruthfulQA<br>0.212|[0.182, 0.245] 0.257|[0.246, 0.273]|0.329 [0.297, 0.362]|0.342 [0.328, 0.355]|
|Aya-Expanse-8B|Uhura-TruthfulQA<br>0.075|[0.062, 0.114] 0.199|[0.187, 0.214]|0.358 [0.326, 0.392]|0.308 [0.295, 0.321]|
|AfroLlama-V1|Uhura-TruthfulQA 0.177|[0.148, 0.212] 0.135|[0.126, 0.151]|0.292 [0.261, 0.325]|0.325 [0.312, 0.339]|
|Qwen3-4B|AfriMMLU<br>0.062|[0.052, 0.116] 0.150|[0.147, 0.165]|0.526 [0.482, 0.572]|0.300 [0.290, 0.310]|
|Gemma-4-12B|AfriMMLU<br>0.311 [|0.273, 0.354] 0.344|[0.335, 0.355]|0.296 [0.258, 0.336]|0.268 [0.259, 0.277]|
|Aya-Expanse-8B|AfriMMLU<br>0.057|[0.048, 0.113]<br>0.173|[0.170, 0.189]|0.520 [0.476, 0.564]|0.296 [0.286, 0.306]|
|AfroLlama-V1|AfriMMLU<br>0.225|[0.187, 0.267]<br>0.207|[0.201, 0.219]|0.356 [0.312, 0.398]|0.279 [0.269, 0.288]|



8 



<!-- Start of picture text -->
Query (African language)<br>Open LLM: answer a ,<br>raw confidence p<br>Temperature scaling<br>c ˆ = TS( p, T ⋆ )<br>c ˆ ≥ τ hi? yes Answer with re-query<br>calibrated confidence<br>no<br>c ˆ ≥ τ lo? yes Ask for more context,<br>then re-query<br>no<br>Abstain / defer to<br>human or safe fallback<br>Low-confidence queries logged<br>for offline African-language data collection<br><!-- End of picture text -->

**Figure 2:** Deployment framework for LLMs in African languages. Recalibrate first with per-language temperature scaling, then route on calibrated confidence ˆ _c_ : high values (ˆ _c ≥ τ_ hi) are answered with the stated confidence; medium values trigger a request for more context followed by re-query; low values (ˆ _c < τ_ lo) are abstained or deferred to a human or safe fallback. Thresholds _τ_ are set per language from the risk-coverage curve, and low-confidence queries are logged to drive offline African-language data collection. 

9 







<!-- Start of picture text -->
(a) Uhura-TruthfulQA (b) AfriMMLU<br><!-- End of picture text -->

**Figure 3:** Pooled ECE before versus after per-language temperature scaling; ECE drops to about 0.03 for all models on both datasets. 





<!-- Start of picture text -->
(a) Uhura-TruthfulQA accuracy by language<br><!-- End of picture text -->





<!-- Start of picture text -->
(b) AfriMMLU accuracy by language<br><!-- End of picture text -->

**Figure 4:** Accuracy across languages by model. Long English and French spokes collapse toward chance across African languages. 

10 





<!-- Start of picture text -->
(a) Uhura-TruthfulQA overconfidence by language<br><!-- End of picture text -->





<!-- Start of picture text -->
(b) AfriMMLU risk-coverage (abstention)<br><!-- End of picture text -->

**Figure 5:** Overconfidence by language (left) and the accuracy-rejection trade-off under selective abstention (right); AUARC sits only modestly above baseline, reflecting a weak uncertainty signal (AUROC about 0.55). 



**Figure 6:** Reliability curves on Uhura-TruthfulQA, English versus African languages, for each model (10 confidence bins). Points on the diagonal are perfectly calibrated; points below it indicate overconfidence. The African curve sits further below the diagonal than the English curve for the general-purpose models. 

11 



**Figure 7:** Bootstrap 95% confidence intervals for ECE by model, English versus African languages (markers are point estimates, bars are 95% intervals). For the general-purpose models the African interval lies entirely to the right of (above) the English interval; the intervals are disjoint. 

12 

