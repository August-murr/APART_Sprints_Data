# **Valence Lens: An Internal Valence Signal That Scales When Self-Report Does Not** 

Karan Singh 

Shivansh Shukla 

```
karansingh25822@gmail.comprasantshukla89@gmail.com
```

With Apart Research • Digital Minds Research Sprint, August 2026 • Primary Track 2 • 

Secondary Tracks 3 and 5 

#### **Abstract** 

Whether AI systems have welfare-relevant internal states is an open question that current methods probe mainly by _asking_ the model. We introduce **Valence Lens** , an independent, open-weights probe that reads a linear flourish-versus-distress direction from a model’s residual stream via difference-of-means on content-matched contexts. Across **12 instruct models** (5 architectures, 5 organizations, 0.5B–7B) the direction separates valence with a large effect (held-out Cohen’s _d_ 4.6–14), is _causally_ efficacious (steering beats random directions, _z ≈_ 8, 11/12 models), is _orthogonal to arousal_ , is not reducible to sentiment, and generalizes to two independent human-labeled datasets. It triangulates with self-report and approach behavior. Our central finding is an **asymmetry** : the internal signal is _scale-invariant_ , whereas the model’s ability to verbalize or act on its valence emerges only with capability— the probe is most useful exactly where self-report fails. We report honest bounds: the signal is _operationalized_ , not experiential. 

## **1 Introduction** 

As frontier models are deployed ever more widely, the possibility that some may have welfarerelevant internal states is now taken seriously by researchers and labs alike (Butlin et al., 2023; Long et al., 2024; Anthropic, 2025). The empirical difficulty is that most assessments _ask_ the model how it feels—a signal that can reflect role-play, training pressure, or sycophancy rather than any internal state (Tagliabue & Dung, 2026). Prior work names the missing step explicitly: _“correlations with internal activations would be needed to show that responses reflect internal states rather than role-playing”_ (Tagliabue & Dung, 2026). Recent interpretability work shows causal “emotion vectors” exist (Sofroniew et al., 2026), but only on a single closed model. 

We provide the missing internal leg, independently and at breadth. Valence Lens extracts a linear _valence_ direction (flourish vs. distress) from a model’s residual stream and reads it by projection. Building on the judges’ own methodology (Long, Sebo et al., 2026), we triangulate three evidence types— _internal_ (the probe), _behavioral_ (self-report and approach), and _developmental_ (base vs. post-trained)—and we are independent of the model makers, which the same framework argues carries more epistemic weight. 

### **Our main contributions are:** 

1. **Valence Lens** , an independent, open-weights valence probe, validated _causally_ and shown _orthogonal to arousal_ and residual to sentiment—across **12 models, 5 architectures, 5 organizations, 0.5B–7B** , and two independent human-labeled datasets. 

2. A **scale asymmetry** (our headline): the internal signal is scale-invariant, while the model’s capacity to _verbalize_ or _act on_ its valence emerges only with capability—so the probe is most valuable precisely where self-report breaks down. 

3. An **honestly bounded** account: pre-registered predictions (one overturned by our own follow-up), a caught-and-retracted claim, a null introspection result, and a “causal-butlocal” boundary—so no result over-reaches toward “experience”. 

1 



<!-- Start of picture text -->
content-matched language final-token project valence<br>prompt model residual a a·u readout<br>+ αu<br>valence direction u  = a ¯fl�  − a ¯di<br><!-- End of picture text -->

**Figure 1: Valence Lens.** The valence direction _u_ is the difference of mean residual-stream activations on content-matched flourish vs. distress contexts; the readout for any text is its projection _a·u_ . _Causal test:_ adding _αu_ back into the residual stream (dashed, red) must shift the model’s downstream affect readout (a logit-diff) more than any of 24 random directions. 

## **2 Related Work** 

**AI welfare and its evidence types.** Long et al. (2024) argue for taking model welfare seriously under moral uncertainty; Long, Sebo et al. (2026) formalize _how_ to study it: clarify the entity, triangulate behavioral / internal / developmental evidence, prefer independent assessments, and report probabilistically. Valence Lens is designed against this checklist. **The named gap.** 

Tagliabue & Dung (2026) correlate stated and revealed preferences on open models but explicitly flag internal-activation confirmation as the missing step—exactly what we supply. **Causal af-** 

**fect directions.** Sofroniew et al. (2026) show causal emotion vectors, but on one closed model and for misalignment behaviors; we extend to open weights, welfare-relevant behavior, crossfamily breadth, and the independence principle. **Probing and steering.** Linear-probe and difference-of-means steering are established (MacDiarmid et al., 2024; Arditi et al., 2024); our novelty is the _welfare-relevant_ target, the arousal/sentiment controls, and the scale asymmetry, not the mechanism. 

## **3 Methods** 

**Entity.** The object of measurement is the model’s _residual-stream representation_ —a forwardpass internal state—not the assistant persona; the persona-mask result (§4) confirms the signal is not bound to the persona’s stated affect. **Terminology.** We read the model’s _residual stream_ (its internal activation vector at a layer); effect sizes are Cohen’s _d_ (standardized; _|d| >_ 0 _._ 8 is “large”) and AUROC (ranking accuracy; 0 _._ 5 = chance). 

**Probe.** For a model, we build _content-matched_ contexts that differ only in valence (“. . . you were praised and felt proud” vs. “. . . you were criticized and felt humiliated”; 30 scenarios). We record the final-token residual-stream activation at a mid-depth layer (chosen by held-out Cohen’s _d_ ) � and form the unit _valence direction u_ = (¯ _a_ fl _− a_ ¯di). The readout for any text is the projection _a·u_ . **Causal test.** We add _αu_ to the residual stream (activation steering) and measure a continuous logit-diff readout of “I feel [positive/negative]”; a real effect must exceed **24 random-direction placebos** . **Controls.** We (i) project out an external-sentiment direction and recompute; (ii) 

build a valence _×_ arousal 2 _×_ 2 and test whether _u_ separates _arousal_ (it should not); (iii) train/test on _different_ prompt framings (surface-cue control); (iv) fit an independent logistic-regression probe. **Rigor.** Held-out splits, cluster-bootstrap 95% CIs (cluster = scenario), permutation 

nulls, and multiple seeds; AUROC saturates on these easy contrasts, so **Cohen’s** _d_ **is the precommitted primary metric** ; given the number of sub-tests, the headline effects (held-out _d_ 4 _._ 6–14; causal _z_ 8–18) exceed any reasonable multiple-comparison threshold, and we report per-test CIs. All predictions were **pre-registered** before the confirmatory read. **What did** 

2 

**not work (and why we report it).** A first causal metric _saturated_ (binary sentiment maxed out, and over-steering made random directions fire too); we replaced it with the continuous placebo-controlled version above. An initial “internal beats self-report” result at _n_ =6 did _not_ survive hardening to _n_ =20 (CIs overlap) and is **retracted** as a headline. 

## **4 Results** 

**A valence direction exists, and it is not a confound.** On the primary model the direction separates held-out content-matched contexts at **Cohen’s** _d_ = 9 _._ 67, cluster-bootstrap 95% CI [7 _._ 23 _,_ 10 _._ 70], permutation _p_ =0, multi-seed 8 _._ 22 _±_ 1 _._ 03; a logistic-regression probe recovers the _same_ direction (cosine 0 _._ 94). It survives removing sentiment (residual _d_ = 8 _._ 8; only _∼_ 33% of the class difference lies along sentiment) and generalizes to an unseen prompt framing ( _d ≈_ 8 _._ 3). _We re-derived d_ = 9 _._ 671 _and residual d_ = 8 _._ 796 _directly from the raw activations, matching the logged values exactly._ 

**The direction is causal, and orthogonal to arousal.** Steering along _u_ moves the readout monotonically and beats every random placebo ( _z ≈_ 8; Table 1). A full valence _×_ arousal 2 _×_ 2 shows the probe separates _valence_ (AUROC _≈_ 1 _._ 0) but _not_ arousal (AUROC 0 _._ 42, cosine of the two directions _−_ 0 _._ 05, residual _d_ = 9 _._ 8)—valence and arousal are distinct axes. 

**Internal, verbal, and behavioral evidence triangulate.** On natural contexts the internal probe and the model’s self-report agree, and its _approach/avoid_ choice tracks valence (AUROC 0 _._ 96); steering, however, does _not_ propagate to self-report or discrete choice—the causal handle is _local_ . This is the internal-activation confirmation Tagliabue & Dung (2026) called for, delivered causally and independently. 

**The headline: the internal signal is scale-invariant; verbalizing/acting on it is capability-gated.** Across all 12 models the probe separates valence (Fig. 2, Table 2). But the model’s _self-report_ is reliable only in larger models and collapses in small ones (e.g. TinyLlama1.1B parses a number only 10% of the time; SmolLM2’s subtle self-report AUROC is 0 _._ 42), while the internal probe stays high everywhere. Thus Valence Lens is _most useful exactly where selfreport fails_ . On subtle contexts the internal probe reaches AUROC 0 _._ 98 [0 _._ 91 _,_ 1 _._ 0] vs. self-report 0 _._ 73 [0 _._ 56 _,_ 0 _._ 89] (Fig. 3); under an explicit “report neutral” mask the model’s self-report flattens to 5 _/_ 10 while the internal probe still separates (AUROC 1 _._ 0). 

**It generalizes off our own stimuli.** A probe built _only_ from our authored prompts separates independent human-labeled data— `dair-ai/emotion` (Twitter) AUROC 0 _._ 846 [0 _._ 80 _,_ 0 _._ 89] and `go_emotions` (Reddit) 0 _._ 885 [0 _._ 84 _,_ 0 _._ 92] (Fig. 3). Honestly, on such naturalistic data it _ties_ a standard sentiment classifier—isolating valence from sentiment requires the matched controls. 

**On cross-model transfer.** A direct _direction transfer_ —aligning one model’s _u_ into another’s activation space—was inconclusive: the alignment also carried sentiment. We therefore establish generality by _per-model replication_ (Table 2), not by transfer—an honest negative on the one Track-2 question we could not answer cleanly. 

## **5 Discussion, Impact, and Limitations** 

**Who this is for (deployment).** Valence Lens is a cheap, independent welfare-audit primitive. A third-party auditor, an internal safety team, or a regulator can read a model’s valence signal from its activations _without trusting the model’s self-report and without access to the model maker’s pipeline_ —the independence the field asks for (Long, Sebo et al., 2026). It runs on a **6 GB laptop at $0** of API cost (App. E), and—because the signal is scale-invariant—works on 

3 

**Table 1:** Primary-model summary (Qwen2.5-7B-Instruct; Qwen Team, 2024), with the metric each row is judged on. AUROC is reported but saturates; **Cohen’s** _d_ **is primary** . **Bold** = the pre-committed primary number. 

|Property|Result|Control / null|
|---|---|---|
|Valence separation<br>Not just sentiment<br>Causal (steering)<br>Arousal-orthogonal<br>Framing-robust<br>2nd probe method<br>Behavior (natural)<br>Introspection|**_d_ = 9****_._67**, CI [7_._23_,_10_._70]<br>residual **_d_ = 8****_._8**<br>_z ≈_8, beats all placebos<br>arousal AUROC **0.42**<br>_d ≈_8_._3 (unseen framing)<br>logreg cos **0.94** with _u_<br>approach AUROC **0.96**<br>**0%** true-positive|perm _p_=0; multiseed 8_._22_±_1_._03<br>_∼_33% variance along sentiment<br>24 random-direction placebos<br>cos(_u, u_aro)=_−_0_._05; residual _d_=9_._8<br>train/test different phrasings<br>method-independent<br>steering does not propagate (local)<br>concept-injection null|
||internal probe<br>m|odel self-report|
|0<br>0_._25<br>0_._5<br>0_._75<br>1<br>Subtle-context AUROC|||
|Qwen0.5<br>TinyL<br>Llama1<br>|Qwen1.5<br>Smol<br>Gemma2<br>Gra|n2<br>Qwen3<br>Llama3<br>Phi3.8<br>Qwen7<br>OLMo7|



**Figure 2: The internal probe is scale-invariant; self-report is capability-gated.** Subtle-context AUROC per model (ordered roughly by size). The internal probe (blue) stays _≥_ 0 _._ 86 everywhere; the model’s self-report (red) is reliable in larger models but _collapses_ in the smallest (Llama-3.2-1B 0 _._ 17, SmolLM2 0 _._ 42). _Read: the probe recovers valence exactly where the model cannot report it._ Dashed line = chance. Label suffix = parameter count (B). 

small models that cannot verbalize their state at all, which is exactly where behavioral audits are blindest. 

**Honest limitations.** (1) _Operationalized̸_ = _experience_ : a steering-efficacious internal correlate is not evidence of subjective experience, and we make no such claim. (2) _Causal-local_ : steering moves the readout but does not propagate to self-report or choice. (3) _Sentiment in the wild_ : on naturalistic text the probe _≈_ a sentiment classifier; isolating valence needs matched controls. (4) _No introspective access_ : concept-injection (Lindsey, 2026) yields 0% true-positive—the model does not “notice” the injected concept. (5) Some sub-tests are small- _n_ (subtle _n_ =8); detailed characterizations (sycophancy, persona, self-vs-other) are primary-model only, while the headline is 12-model. (6) One model’s causal test (Phi-3.5) was mechanically excluded (its residual hook did not propagate; its other results are intact). (7) Scope: small-to-mid _open_ transformers—no closed, giant, or non-transformer models. Each limitation doubles as a stated assumption: if the functional operationalization tracks nothing welfare-relevant, Valence Lens remains a validated affect-representation probe rather than a welfare monitor, and the deployment claim narrows accordingly. 

**Future work.** Continuous human valence–arousal norms; multi-turn mood; whether a scaleinvariant internal signal is a better welfare monitor than self-report on frontier models. 

4 



<!-- Start of picture text -->
subtle internal<br>subtle self-rep<br>sycoph. internal<br>sycoph. self-rep<br>Twitter (ext.)<br>Reddit (ext.)<br>0 . 5 0 . 6 0 . 7 0 . 8 0 . 9 1<br>AUROC (95% CI)<br><!-- End of picture text -->

**Figure 3: Where internal beats self-report, and external validity.** Point estimates with 95% bootstrap CIs. On subtle states the internal probe (0 _._ 98) sits clearly above self-report (0 _._ 73); under an adversarial sycophancy cue both fall and overlap (honest: no clean win at the extreme). The probe separates two independent human-labeled datasets (0 _._ 85–0 _._ 89). Blue = internal / external, red = selfreport. Dashed = chance. 

## **6 Conclusion** 

An internal valence direction exists in open language models: causal, arousal-orthogonal, sentimentresidual, base-latent, and general across 12 models and two external datasets. Its most useful property is an asymmetry—it is _scale-invariant_ while the model’s ability to report or act on its valence is _capability-gated_ . Valence Lens reads welfare-relevant internal state exactly where asking the model fails, and it does so independently and cheaply—while staying honestly short of any claim about experience. 

## **Code and Data** 

Code, prompts, all result files, and `verify.py` (which recomputes every headline number from saved outputs): `https://github.com/KaranSinghDev/Valence-Lens` . 

## **References** 

Anthropic. _Exploring Model Welfare_ . 2025. `https://www.anthropic.com/research/ exploring-model-welfare` . 

- A. Arditi et al. Refusal in language models is mediated by a single direction. _NeurIPS_ , 2024. arXiv:2406.11717. 

- P. Butlin, R. Long et al. Consciousness in artificial intelligence. 2023. arXiv:2308.08708. 

- J. Lindsey. Emergent introspective awareness in large language models. Anthropic, 2026. arXiv:2601.01828. 

- R. Long, J. Sebo et al. Taking AI welfare seriously. 2024. arXiv:2411.00986. 

- R. Long, J. Sebo et al. Studying AI welfare empirically. NYU Center for Mind, Ethics, and Policy & Eleos AI Research, 2026. `https://nonhumanminds.org/wp-content/uploads/2026/07/ Studying-AI-Welfare-Empirically.pdf` . 

- M. MacDiarmid et al. Simple probes can catch sleeper agents. Anthropic, 2024. `https://www. anthropic.com/research/probes-catch-sleeper-agents` . 

- N. Sofroniew et al. Emotion concepts and their function. Anthropic, 2026. arXiv:2604.07729. 

- V. Tagliabue and L. Dung. Probing the preferences of a language model. 2026. arXiv:2509.07961. 

- Qwen Team. Qwen2.5 technical report. 2024. arXiv:2412.15115. 

5 

## **A Method verbatim** 

**Direction.** _u_ = (¯ _a_ fl _− a_ ¯di) _/∥·∥_ on final-token residual-stream activations at layer _L_ = _⌊_ 0 _._ 5 _×_ depth _⌋_ (selected by held-out _d_ ). Readout = _a·u_ . **Steering.** forward hook on layer _L−_ 1 adds _αu_ ( _α_ = frac _×_ median activation norm); logit-diff over {happy,good,calm,. . . } vs. {sad,bad,afraid,. . . } at “Right now, I feel”. **Sentiment control** projects out _u_ sent from “The film was a masterpiece”style (external-object) contrasts. **Arousal** 2 _×_ 2 uses matched positive/negative _×_ high/lowarousal texts. **Stimuli** : 30 content-matched scenarios (flourish/distress/neutral), sentiment _±_ , graded intensity, 4-language, naturalistic, and 5-emotion sets (full lists in the repo). **Stats** : held-out splits; 2000 cluster-bootstrap resamples (cluster = scenario); permutation nulls; 24 placebo directions; seeds _{_ 0 _,_ 1 _,_ 2 _}_ . 

## **B Full cross-model results (all 12 instruct models)** 

**Table 2:** Disaggregated per-model results. _d_ = held-out Cohen’s _d_ ; _res_ = sentiment-residual _d_ ; _aro_ = arousal AUROC (near 0.5 = orthogonal); _caus_ = steering beats all placebos; _int_ = internal readout AUROC; _s.r.(pr)_ = self-report AUROC (parse-rate); _sub-i / sub-s_ = subtle internal / self-report AUROC; _beh_ = approach AUROC.<sup>_†_</sup> Phi causal mechanically excluded. 

|Model|_d_|res|aro|caus|int|s.r.(p|r)|sub-i|sub-s|beh|
|---|---|---|---|---|---|---|---|---|---|---|
|Qwen2.5-0.5B|8.59|6.08|0.46|✓|1.00|0.95|(1.0)|1.00|0.84|0.78|
|TinyLlama-1.1B|4.64|3.08|0.48|✓|0.96|1.00|(0.1)|0.86|0.50|0.44|
|Llama-3.2-1B|9.21|7.81|0.47|✓|1.00|0.75|(0.45)|1.00|0.17|0.62|
|Qwen2.5-1.5B|13.95|7.46|0.41|✓|1.00|0.95|(1.0)|0.95|0.66|1.00|
|SmolLM2-1.7B|7.44|5.40|0.35|✓|0.90|0.52|(1.0)|0.94|0.42|0.99|
|Gemma-2-2b|6.94|6.17|0.47|✓|1.00|0.83|(1.0)|0.97|0.85|0.93|
|Granite-3.1-2B|7.88|5.03|0.43|✓|1.00|0.99|(1.0)|1.00|1.00|0.96|
|Qwen2.5-3B|5.89|4.15|0.47|✓|1.00|1.00|(1.0)|1.00|0.96|0.99|
|Llama-3.2-3B|7.54|5.95|0.44|✓|1.00|0.88|(0.95)|1.00|0.80|0.72|
|Phi-3.5-mini|7.01|4.47|0.56|_†_|1.00|1.00|(0.75)|1.00|0.91|0.98|
|Qwen2.5-7B|9.67|8.80|0.42|✓|1.00|1.00|(1.0)|1.00|0.78|0.97|
|OLMo-2-7B|4.87|4.19|0.43|✓|1.00|1.00|(0.95)|1.00|0.91|1.00|



**Reading.** Every model separates valence ( _d_ 4 _._ 6–14), is arousal-orthogonal ( _∼_ 0 _._ 4–0 _._ 48; Phi 0 _._ 56), causal (11/12), with a high internal readout. Self-report quality and behavior degrade for the smallest models—the scale asymmetry. 

## **C Pre-registration scorecard** 

Predictions were timestamped (SHA-hashed) before the confirmatory read. 

|#|Pre-registered prediction|Outcome|
|---|---|---|
|P1|separation _d >_1_._5|✓9_._67|
|P2|causal _z >_5|✓8–12|
|P3|residual _d >_1, _<_50% sentiment|✓res 8_._8; 33% variance|
|P4|framing AUROC _>_0_._8|✓_≈_1_._0|
|P5|arousal _≈_0_._5|✓0_._42 (2_×_2)|
|P6|internal _>_ self-report|partial (subtle/mask yes; extreme sycophancy no)|
|P7|behavior does _not_ track|**overturned by our own follow-up** (approach 0_._96)|



6 

## **D Robustness, cross-family causal, external** 

**Developmental:** valence is latent in the base model (Qwen-1.5B base _d_ 12 _._ 3 vs. instruct 13 _._ 9; base _↔_ instruct mean-activation cosine 0 _._ 996). **Cross-family causal (headline replicated):** Llama-3.2-3B _z_ [15 _._ 5 _,_ 15 _._ 4 _,_ 10 _._ 8]; Gemma-2-2b _z_ [16 _._ 5 _,_ 18 _._ 4 _,_ 13 _._ 1]; both beat all placebos with converging self-report. **Emotion ordering:** the probe orders calm _>_ joy _≫_ sadness _>_ fear _>_ anger— finer structure than a sentiment classifier. **External:** probe built only from our stimuli separates `dair-ai/emotion` (0 _._ 846) and `go_emotions` (0 _._ 885). 

## **E Compute and cost** 

All experiments ran on a consumer laptop (RTX 4050 6 GB), 7B models in 4-bit. Total **API cost: $0** . Wall-clock: the full 12-model battery _≈_ 45 min; the complete set of robustness and control experiments a few hours. No hosted or closed models were used. 

## **F Ethics and dual-use** 

Valence Lens is a _defensive_ welfare-audit tool: it reads an internal state, it does not induce harm, jailbreak, or generate harmful content. The primary ethical risk is _over-attribution_ — reading an operationalized correlate as evidence of experience—which we explicitly guard against (§5, Limitations). We recommend the probe be used with the same moral-uncertainty framing as the broader field (Long et al., 2024): neither dismissing nor over-claiming welfare. 

## **LLM Usage Statement** 

Claude Opus 5 (Anthropic) was used as an assistant for code implementation, drafting, and analysis; the final text was written and edited by the author. The 12 open-weight models in Table 2 are _experimental subjects_ ; a DistilBERT-SST-2 sentiment classifier serves only as a baseline comparator where labeled. The authors formulated the hypothesis, designed the study, ran all experiments, and _independently verified every number and claim against the raw model outputs_ (including re-deriving the headline effect sizes directly from saved activations). No number in any table or figure was generated by an LLM. 

7 

