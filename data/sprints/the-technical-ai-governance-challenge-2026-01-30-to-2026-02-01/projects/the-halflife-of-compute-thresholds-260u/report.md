# The Half-Life of Compute Thresholds<sup>∗</sup> 

Aaron Potter Independent Researcher 

_With_ 

Apart Research 

#### **Abstract** 

_Compute thresholds are widely discussed as a practical governance tool, but the literature rarely specifies how quickly fixed thresholds become outdated as algorithmic efficiency improves. We develop a compute-threshold staleness model that distinguishes raw training compute from baseline-equivalent (“effective”) compute and defines staleness as the ratio between a policy threshold and the time-varying threshold that would remain aligned with a fixed risk cutoff. Under exponential efficiency gains with doubling time τ and threshold updates every U months, worstcase staleness grows as S_ max = 2<sup>_U/τ_</sup> _, implying that modest uncertainty about τ can translate into large differences in required update cadence. Using a representative frontier estimate of τ ≈_ 8 _months suggests that annual recalibration can allow thresholds to drift by roughly_ 2 _._ 8 _× within one year. We ground plausible values of τ in prior estimates of algorithmic progress and provide a small historical backtest as a sanity check._ 

## **1 Introduction** 

Compute thresholds are widely used in regulatory frameworks for AI models (Pistillo et al., 2025), as they correlate roughly with risk and are relatively easy to predict ahead of time. The literature also observes that compute thresholds will need to be shifted (ArXiv discussion, 2024). How much, how frequently, and in what direction lacks any clear consensus. This paper models the impact of algorithmic progress on how quickly thresholds become stale, an important consideration especially for handling CBRN risks, which unlike loss-of-control risks are not clustered at the frontier. 

Our main contributions are: 

1. A simple mathematical model applying the observed pattern of exponential growth in algorithmic efficiency to questions of staleness of compute thresholds 

2. A dashboard to model the relationship between the update frequency, the doubling time of algorithmic efficiency, and the staleness of compute thresholds 

> ∗Research conducted at the Technical AI Governance Challenge, 2026. 

1 

## **2 Related Work** 

### **Compute thresholds in AI regulation** 

**Training Compute Thresholds: Features and Functions in AI Regulation.** The analysis of compute thresholds in this paper is heavily indebted to Heim and Koessler’s discussion (Heim and Koessler, 2024). Their work is primarily qualitative, and we use it mainly to motivate why thresholds are appealing as an initial filter and why update mechanisms matter. In particular, they discuss the suitability of compute thresholds for an initial filter, the need for updates, and tradeoffs in both conservative and aggressive thresholds, as well as how compute thresholds are used in existing policy (principally the EU AI Act). 

### **Algorithmic progress and efficiency trends** 

**Algorithmic progress in language models.** This paper provides an analysis and rough estimate of the role of algorithmic progress in making training more efficient to reach a given capability level (Ho et al., 2024). We use their empirical estimates to motivate plausible values of _τ_ (an “effective compute” doubling time) in our staleness model; as shown in Section 4, the implications are highly sensitive to _τ_ . 

### **Positioning and gap** 

Despite the existence of extensive work on algorithmic progress, and the adoption of compute thresholds with the acknowledgment of a need to update them, there is little work on modeling the relationship of update frequency and algorithmic progress to the degree with which a model falls out of date. This paper attempts to close that gap with a simple model which can provide a good intuitive grasp of the problem for policy-makers. 

## **3 Methods** 

### **3.1 Compute Threshold Staleness Model** 

We model time as _t ∈_ R _≥_ 0 (months, mo), with baseline month _t_ = 0. The policy observes raw training compute _C >_ 0 (FLOPs). 

**Efficiency and effective compute.** Let _A_ ( _t_ ) be a dimensionless algorithmic-efficiency multiplier with _A_ (0) = 1, parameterized by a doubling time _τ_ (months): 



<!-- Start of picture text -->
A ( t ) = 2 t/τ . (1)<br><!-- End of picture text -->

Define effective compute (baseline-equivalent FLOPs) 



<!-- Start of picture text -->
E ( C, t ) :=  A ( t )  C. (2)<br><!-- End of picture text -->

2 

**Risk and policy trigger.** A run is “risky” if effective compute exceeds a fixed cutoff _E_ risk _>_ 0: 



<!-- Start of picture text -->
R  :=  {E ( C, t )  ≥ E risk }. (3)<br><!-- End of picture text -->

A compute-threshold policy triggers when 



<!-- Start of picture text -->
G  :=  {C ≥ T ( t ) }, T ( t )  >  0 . (4)<br><!-- End of picture text -->

**Ideal threshold and staleness.** The ideal raw-compute threshold that exactly aligns with the risk boundary at month _t_ is 



<!-- Start of picture text -->
T ∗ ( t ) = E risk (5)<br>A ( t ) .<br><!-- End of picture text -->

Define threshold staleness as 



<!-- Start of picture text -->
Staleness( t ) := T ( t ) = E th( t ) , (6)<br>T ∗ ( t ) = A ( E t ) risk T ( t ) E risk<br><!-- End of picture text -->

where _E_ th( _t_ ) := _A_ ( _t_ ) _T_ ( _t_ ) is the effective compute at the policy threshold. 

**Step-hold updates every** _U_ **months.** Let _U >_ 0 be the update interval and _tn_ := _nU_ . Under a step-hold policy, 



<!-- Start of picture text -->
T ( t ) :=  T ∗ ( tn ) = E risk for t ∈ [ tn, tn +1) . (7)<br>A ( tn )<br><!-- End of picture text -->

Within an interval, staleness depends only on efficiency growth since the last update: 



<!-- Start of picture text -->
Staleness( t ) = T ∗ ( tn ) (8)<br>T ∗ ( t ) = A A ( ( t t n ) ) = 2( t−tn ) /τ .<br><!-- End of picture text -->

Hence the worst-case staleness just before the next update is 



<!-- Start of picture text -->
Stalenessmax = 2 U/τ , (9)<br><!-- End of picture text -->

and the time to become _m×_ stale within an interval is 



<!-- Start of picture text -->
t − tn =  τ log2  m. (10)<br><!-- End of picture text -->

## **4 Results** 

This section reports closed-form implications of the staleness model and illustrates their sensitivity to the key ratio _U/τ_ . We treat the historical comparisons as a lightweight sanity check; the primary empirical grounding for _τ_ comes from Ho et al. (2024). 

3 

### **4.1 Model Sensitivity to Key Parameters** 

The staleness of a compute threshold is determined by the ratio _U/τ_ , where _U_ is the policy update interval (in months) and _τ_ is the algorithmic efficiency doubling time (in months). The maximum staleness just before a policy update is given by: 



<!-- Start of picture text -->
S max = 2 U/τ (11)<br><!-- End of picture text -->

This relationship is highly sensitive to _τ_ . For example, with an annual update cycle ( _U_ = 12 months): 

- At _τ_ = 8 months (frontier estimate from Ho et al. (2024)): _S_ max = 2<sup>1</sup><sup>_._5</sup> _≈_ 2 _._ 8 _×_ 

- At _τ_ = 4 months: _S_ max = 2<sup>3</sup> = 8 _×_ 

- At _τ_ = 16 months: _S_ max = 2<sup>0</sup><sup>_._75</sup> _≈_ 1 _._ 7 _×_ 

The update interval required to maintain a target maximum staleness _S_ target is: 



<!-- Start of picture text -->
U =  τ ·  log2( S target) (12)<br><!-- End of picture text -->

### **4.2 Implications of 8-Month Doubling Time** 

Using the Ho et al. (2024) estimate of _τ_ = 8 months for frontier algorithmic efficiency improvements: 

- The ideal compute threshold halves every 8 months 

- A threshold set today will be approximately 2 _._ 8 _×_ too permissive after one year without updates 

- After two years, a static threshold becomes 8 _×_ too permissive 

- To maintain staleness _≤_ 2 _×_ , updates are needed every _U_ = 8 _·_ log2(2) = 8 months 

These results suggest that annual update cycles—common in regulatory contexts—may be insufficient to maintain threshold calibration if algorithmic progress continues at frontier rates. 

4 



Figure 1: Staleness growth over time under an 8-month algorithmic-efficiency doubling time ( _τ_ = 8 months). 

### **4.3 Historical Validation** 

A backtest against historical AI model releases provides a rough sanity check of the _τ_ parameter. We compare capability-matching model pairs—cases where a later, smaller model achieved similar benchmark performance as an earlier, larger model with less training compute. 

**Data Sources.** Training compute estimates are sourced from Epoch AI’s Notable AI Models dataset (Epoch AI, 2024) where available, supplemented by the standard scaling approximation _C ≈_ 6 _ND_ (where _N_ is parameter count and _D_ is training tokens) for models with disclosed training configurations (Kaplan et al., 2020). This approximation is coarse and depends on training details that are not always publicly reported. Release dates are taken from official announcements or first public availability. 

**Capability Matching.** We identify pairs where the matching model uses _less_ compute than the reference while achieving comparable scores on specific benchmarks (e.g., HellaSwag, MMLU). Pairs where the later model used more compute are excluded, as these test data efficiency rather than algorithmic efficiency. The “comparable capability” judgment is approximate and benchmarkspecific—a significant limitation of this validation approach. 

**Results.** Given a compute ratio _r_ = _C_ match _/C_ ref, the model predicts a time gap of ∆ _t_ = _τ ·_ log2(1 _/r_ ) for capability parity. Minimizing RMSE across all pairs yields a best-fit _τ ≈_ 9 _._ 5 months, broadly 

5 

consistent with the frontier estimate of 8 months reported by Ho et al. (2024). This convergence is 

|Reference|Matching Model|Compute Ratio|Actual Gap|Predicted Gap<sup>_∗_</sup>|
|---|---|---|---|---|
|GPT-3 175B|LLaMA-13B|0_._35_×_|32 mo|28 mo|
|GPT-3 175B|Mistral 7B|0_._27_×_|40 mo|34 mo|
|GPT-4|LLaMA 3 70B|0_._43_×_|13 mo|10 mo|
|GPT-4|Qwen 2.5 72B|0_._36_×_|18 mo|12 mo|



Table 1: Capability-matching pairs used in backtest. Compute ratios indicate how much less compute the matching model used relative to the reference.<sup>*</sup> Predicted gap using _τ_ = 8 months. 

expected given that the model’s efficiency dynamics rely primarily on Ho et al. (2024)’s empirical estimates of frontier algorithmic progress. The backtest confirms internal consistency rather than providing independent validation of _τ_ . 

## **5 Discussion and Limitations** 

These results indicate that, to keep compute thresholds well-calibrated, the update cadence should scale with the doubling time of algorithmic efficiency. However, _τ_ is uncertain and may differ across regimes (e.g., frontier vs catch-up), making calibration difficult. This uncertainty is especially salient as models cross capability levels associated with significant CBRN risk. Where loss-ofcontrol concerns may cluster near the frontier (which is hard to define but relatively easy to track), CBRN-relevant capabilities may not be confined to the frontier. 

This suggests that improving estimates of algorithmic progress (i.e., of _τ_ ) is important for selecting an appropriate update cadence. Finally, if efficiency gains slow over time (e.g., a sigmoidal trajectory due to physical limits), threshold drift may eventually become less severe. 

### **Limitations** 

This model is highly idealized and cannot give detailed prescriptions. For example, capabilities do not necessarily improve at the same rate across domains as algorithmic efficiency changes. The model also ignores error in setting new thresholds, which could be significant in practice. If the rate of algorithmic progress is continually underestimated (e.g., in a pause world where most or all algorithmic research is covert), then staleness could grow substantially. 

More fundamentally, effective compute is a modeling construct rather than an observable quantity. There may be no single scalar that captures the capabilities we care about across domains and threat models. As a result, calibration will necessarily require judgment beyond estimating a single doubling time _τ_ —including choices about which benchmarks, evaluations, and risk cutoffs the threshold is intended to track. 

6 

### **Future Work** 

This model could be expanded to consider other parameters, though high uncertainty makes detailed modeling difficult and somewhat prone to false precision risks. The biggest suggestion is that accurate research on algorithmic progress may be necessary to make compute thresholds workable; absent that, compute thresholds may not be reliable for identifying models likely to pose substantial risks. 

## **6 Conclusion** 

This project formalizes a simple model for the degree to which a compute threshold would be expected to be out of date as a result of improvements in algorithmic efficiency. Applying the currently observed model of exponential growth of algorithmic efficiency, the model predicts that compute thresholds have worst-case staleness _S_ max = 2<sup>_U/τ_</sup> . A small historical backtest suggests the model’s predictions are consistent with an 8–10 month regime, in line with Ho et al. (2024). 

Applying a representative frontier estimate of _τ ≈_ 8 months implies that annual recalibration can allow thresholds to drift by roughly 2 _._ 8 _×_ within a year, suggesting that annual updates may leave thresholds meaningfully miscalibrated for a substantial portion of the year. This model provides a compact way to reason about the relationship between thresholds and observed trends in algorithmic efficiency, with potential uses in policy planning and communication, though it is a highly ideal model and should not be used in place of empirical observation. 

## **Code and Data** 

- Code repository: `https://github.com/Ardrual/Compute-Threshold-Staleness-Model` 

## **References** 

- Matteo Pistillo, Suzanne Van Arsdale, et al. _The Role of Compute Thresholds for AI Governance_ . _Geo. Wash. J. L. & Tech_ , 1:26, 2025. 

- Lennart Heim and Florian Koessler. _Training Compute Thresholds: Features and Functions in AI Regulation_ . 2024. 

- Eric Ho, et al. _Algorithmic progress in language models_ . 2024. 

Epoch AI. _Notable AI Models_ . 2024. `https://epochai.org/data/notable-ai-models` . 

- Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. _Scaling Laws for Neural Language Models_ . 2020. 

- _Discussion of updating compute thresholds_ . arXiv:2405.10799v2, Section 6. `https://arxiv.org/ html/2405.10799v2#S6` . 

7 

## **A Appendix** 

### **LLM Usage Statement** 

The initial mathematical formalism was developed with substantial input from GPT-5.2, Claude Opus 4.5, and Gemini Pro 3. The python model was programmed primarily by GPT-5.2-Codex, while the frontend was primarily programmed by Claude Opus 4.5 and Gemini 3 Fast. The writeup was done with substantial formatting and editing help from GPT-5.2 in Prism. 

8 

