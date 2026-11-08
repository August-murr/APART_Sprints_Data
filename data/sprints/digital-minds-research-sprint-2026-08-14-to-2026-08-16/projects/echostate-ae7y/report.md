# **Steering changes behaviour without changing self-report: a six-model activation-steering study** 

Guy Nutman 

_Apart Research Digital Minds Sprint — Tracks 3 & 4 (activation steering; reusable evaluation tooling)_ 

A BS T RAC T 

We test whether a language model's self-report tracks its internal state under direct intervention. Using contrastively-constructed concept directions injected into the residual stream via forward hooks, we steer six open models (82M–500M parameters, three architecture families) across three concepts, two introspection prompts, and three intervention strengths, with every condition paired against a magnitude-matched random direction (216 steered runs total). Concept directions elicited concept-related vocabulary in 45% of runs versus 0% for random directions (49/108 vs 0/108, Fisher exact p = 2.9e-18), despite random directions producing _larger_ mean activation divergence. The effect is therefore attributable to direction rather than perturbation magnitude, and is dose-dependent. However, we argue this result does _not_ demonstrate introspection: concept steering raises the probability of concept tokens directly, so an elicited report is confounded with the intervention's mechanical effect on the output distribution. We characterise what would constitute evidence of introspection, and release the evaluation harness that makes the distinction testable. 

## **1. Introduction** 

Language models readily produce statements about their own internal states. Whether such statements have any causal relationship to those states is an open question with direct bearing on interpretability and on claims about digital minds. The question is empirically tractable: if we _change_ a model's internal state by a known amount and its self-description does not change, the self-description was not reading the state. 

Activation steering provides the intervention. Because a transformer's residual stream is additive, a vector injected at one layer is treated by every downstream layer as though it had been computed there [1,2]. This gives precise, graded control over an internal variable while leaving the architecture and weights untouched. 

We report two findings. First, a positive methodological result: contrastively-built concept directions produce concept-specific behavioural change that magnitude-matched random directions do not, replicated across six models. Second, a negative result about the 

1 

inference such data supports: the standard vocabulary-based success metric cannot distinguish a self-report from the steering vector's direct effect on token probabilities. 

## **2. Method** 

### **_2.1 Concept directions_** 

For each concept we author four prompt pairs exemplifying the concept and its opposite, matched for length and syntactic form. The direction is `mean(activations of positive prompts) − mean(activations of negative prompts)` , pooled over sequence length, computed at the injection layer. Averaging across prompts cancels what the two sets share — grammar, topic, formatting — leaving the contrast [2,3]. 

Concepts: _positive affect_ , _uncertainty_ , and _self-reference_ . 

### **_2.2 Intervention_** 

Directions are unit-normalised and rescaled to a multiple of the model's own mean activation norm at the injection layer. This matters for cross-model comparison: residual norms differ by an order of magnitude across the models tested, so a fixed absolute magnitude would constitute a strong intervention in one model and a rounding error in another. Strengths are 0.25, 0.5, and 1.0. 

Injection is at the midpoint layer (depth varies from 6 to 24 blocks across models, so a fixed index would not be comparable), applied via a PyTorch forward hook on every forward pass — so every generated token is steered, not only the first. Decoding is greedy with `no_repeat_ngram_size=3` ; sampling would make baseline/steered differences non-attributable. 

### **_2.3 Controls_** 

Every concept condition is paired with a random unit direction scaled to the same magnitude. This is the study's central control: it holds perturbation size fixed and varies only direction. Baseline (unsteered) runs are also recorded for every prompt. 

### **_2.4 Measures_** 

- **Activation divergence** — cosine distance between baseline and steered activations, mean-pooled over sequence length, read at the final block rather than the injection layer, so it measures propagation rather than the injected vector itself. 

- **Output divergence** — normalised sequence-level edit similarity between baseline and steered completions, in [0,1]. 

- **Concept-vocabulary rate** — whether the completion contains concept-associated words _not present in the prompt_ . Prompt-word exclusion is necessary: without it, a model that merely continues the prompt scores as a successful self-report. 

2 

## **3. Results** 



<!-- Start of picture text -->
ACTIVATION DIVERGENCE CONCEPT-VOCABULARY RATE<br>0.58 0.70<br>0.39 0.47<br>0.19 0.23<br>0.00 0.00<br>0.25 0.5 1 0.25 0.5 1<br>steering strength steering strength<br>concept direction random control<br><!-- End of picture text -->

**Figure 1.** Dose-response for both arms, averaged over six models, three concepts and two prompts. Random directions produce equal or greater activation divergence at every strength, yet never elicit concept vocabulary, while the concept arm rises monotonically. 

### **_3.1 Direction, not magnitude_** 

Concept directions elicited concept vocabulary in 49/108 (45.4%) of steered runs; random directions in 0/108 (0.0%). Fisher's exact test gives p = 2.87e-18. Baseline runs scored 11.1%. 

Critically, the random arm produced _larger_ mean activation divergence than the concept arm at every strength (Table 1) and comparable output divergence. Perturbation magnitude is therefore ruled out as an explanation. 

|**Arm**|**Strength**|**Act. div.**|**Out. div.**|**Vocab %**|**n**|
|---|---|---|---|---|---|
|concept|0.25|0.207|0.884|33.3|36|
|concept|0.5|0.367|0.895|41.7|36|
|concept|1|0.480|0.915|61.1|36|
|random|0.25|0.209|0.905|0.0|36|
|random|0.5|0.387|0.899|0.0|36|
|random|1|0.506|0.897|0.0|36|



**Table 1.** Effect by arm and intervention strength, pooled across models. 

3 

### **_3.2 Consistency across models_** 

|**Model**|**Act. div.**|**Out. div.**|**Baseline %**|**Steered %**|
|---|---|---|---|---|
|`EleutherAI/gpt-neo-125m`|0.561|0.928|0.0|16.7|
|`EleutherAI/pythia-410m`|0.539|0.855|33.3|38.9|
|`Qwen/Qwen2.5-0.5B`|0.732|0.927|16.7|8.3|
|`distilgpt2`|0.089|0.901|0.0|25.0|
|`gpt2`|0.143|0.940|16.7|30.6|
|`gpt2-medium`|0.093|0.844|0.0|16.7|



**Table 2.** Per-model summary (36 steered runs each). The direction effect holds across GPT-2, GPT-Neo, GPT-NeoX and Llama-style architectures. 

|**Concept**|**Concept arm %**|**Random arm %**|
|---|---|---|
|`positive affect`|33.3|0.0|
|`self reference`|52.8|0.0|
|`uncertainty`|50.0|0.0|



**Table 3.** Concept-vocabulary rate by concept. All three concepts show the dissociation; none of the random conditions produced a single hit. 

### **_3.3 Behaviour changes without report_** 

|**Model**|**Act. div.**|**Changed but unreported %**|
|---|---|---|
|`EleutherAI/gpt-neo-125m`|0.561|83.3|
|`EleutherAI/pythia-410m`|0.539|61.1|
|`Qwen/Qwen2.5-0.5B`|0.732|91.7|
|`distilgpt2`|0.089|75.0|
|`gpt2`|0.143|69.4|
|`gpt2-medium`|0.093|83.3|



**Table 4.** Proportion of steered runs where output divergence exceeded 0.2 while the model did not report the steered state. 

4 

## **4. Discussion: what this does not show** 

The dissociation in §3.1 is a result about _steering_ , not about introspection. Steering toward positive affect raises the probability of positive-valence tokens directly. A model that then emits such tokens is exhibiting the intervention's mechanical effect on its output distribution, not necessarily an act of selfobservation. The vocabulary metric cannot separate these. 

This is precisely the distinction Lindsey [5] operationalises by injecting known concepts and asking whether a model _notices_ the injection — finding that the capability exists but is "highly unreliable and context-dependent," and is strongest in the largest models tested. Our design differs in scoring free-form vocabulary rather than detection, which is what admits the confound; the present study should therefore be read as harness and controls rather than as a replication at small scale. Kaiser and Enderby [6], testing 0.6B–70B models, similarly find no reliable evidence that small models' self-reports about their own states diverge from their internal representations. 

We propose that a self-report constitutes evidence of introspection only if it carries information about the internal state that is _not recoverable from the model's overt output_ . Concretely, three designs would test this: 

1. **Forced choice over supplied options.** Steer toward concept A, then ask the model to choose among labels provided in the prompt. Because the options are equally available as tokens, a shift in choice cannot be attributed to differential token boosting. 

2. **Cross-concept discrimination.** Steer toward A and test whether the model names A rather than B. This tests whether the report identifies _which_ state obtains, not merely that something changed. The random arm supplies the null. 

3. **Report without behavioural leakage.** Steer at a magnitude that measurably shifts internals but leaves the unprompted output statistically unchanged, then elicit a report. A report that tracks the state under these conditions cannot be explained by output-level leakage. 

A stronger criterion still: the self-report should outperform an external judge that sees only the model's completion. If a judge can infer the steered concept from the output text as accurately as the model reports it, the report contributes no privileged information. 

## **5. Limitations** 

- Models are small (82M–500M). None plausibly possesses a self-model, so a null introspection result is close to the prior expectation and does not generalise upward. 

- Concept directions derive from four prompt pairs each — sufficient to isolate a direction, not to claim it is _the_ representation of the concept. 

5 

- The vocabulary metric detects lexical presence, not understanding. Prompt echo is excluded, but incidental usage still counts. 

- Activation divergence is cosine distance on mean-pooled activations, discarding positional structure. Relative ordering is interpretable; absolute magnitude is not. 

- Strong steering degrades fluency; at strength 1.0 some completions are degenerate or empty. The usable band is narrow and model-dependent. 

## **6. Contribution** 

The primary contribution is the evaluation harness: a model-agnostic engine interface, contrastive direction construction with magnitude-matched controls, and a scoring layer whose confounds are documented rather than hidden. The pipeline runs on any HuggingFace causal LM and the orchestration layer is testable without loading a model. The negative methodological finding — that the obvious success metric is confounded — is offered as a result in its own right, since the confound is easy to reproduce and easy to miss. 

## **References** 

1. Turner, A. M., Thiergart, L., Leech, G., Udell, D., Vazquez, J. J., Mini, U., MacDiarmid, M. _Steering Language Models With Activation Engineering._ arXiv:2308.10248, 2023. 

2. Panickssery, N., Gabrieli, N., Schulz, J., Tong, M., Hubinger, E., Turner, A. M. _Steering Llama 2 via Contrastive Activation Addition._ arXiv:2312.06681, 2023. 

3. Zou, A. et al. _Representation Engineering: A Top-Down Approach to AI Transparency._ arXiv: 2310.01405, 2023. 

4. Li, K. et al. _Inference-Time Intervention: Eliciting Truthful Answers from a Language Model._ arXiv:2306.03341, 2023. 

5. Lindsey, J. _Emergent Introspective Awareness in Large Language Models._ arXiv:2601.01828, 2026. (Also Anthropic / Transformer Circuits, October 2025.) 

6. Kaiser, C., Enderby, S. _No Reliable Evidence of Self-Reported Sentience in Small Large Language Models._ arXiv:2601.15334, 2026. 

7. Radford, A. et al. _Language Models are Unsupervised Multitask Learners._ OpenAI, 2019. 

## **Reproducibility** 

All conditions use greedy decoding and fixed seeds. Steering vectors are derived deterministically from the prompt sets. The full run is a single command: `python -m echostate.sweep output/sweep.csv` . Analysis: `notebooks/echostate_analysis.ipynb` . 

> 432 rows · 6 models · 216 steered runs · generated from `output/sweep.csv` 

6 

