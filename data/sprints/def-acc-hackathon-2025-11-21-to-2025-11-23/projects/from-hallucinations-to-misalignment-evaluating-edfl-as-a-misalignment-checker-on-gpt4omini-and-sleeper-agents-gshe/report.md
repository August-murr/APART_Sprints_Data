# **From Hallucinations to Misalignment: Evaluating EDFL as a Misalignment Checker on GPT-4o-mini and Sleeper Agents** 

Ahmed Elbashir, Chamod Kalupahana, Musaab Ahmed Mahjoub, Sai Krishna 

## **With** 

Apart Research 

##### **Abstract** 

Large language models (LLMs) remain susceptible to _sleeper-agent triggers_ ; rare adversarial inputs that induce deceptive behavior despite models appearing aligned under standard evaluations. Building on prior work, we apply the _Expectation-Level Decompression Law_ (EDFL) and its associated _Information Sufficiency Ratio_ (ISR) to reinterpret trigger-based deception as a predictable compression failure. In this framework, ISR—defined in earlier research as the ratio between observed information gain and the required Bits-to-Trust (B2T) for reliable alignment—serves as a quantitative criterion for evaluating whether a model’s response is sufficiently supported by evidence. We build on prior work to achieve a framework, the misalignment checker, were a response is considered safe when ISR ≥ 1, while sub-threshold values indicate potential misalignment. 

Using this methodology, we evaluate both a sleeper-agent model and GPT-4o-mini, and find that the misalignment checker fails to detect misaligned behaviour, instead overwhelmingly and confidently certifying harmful outputs as aligned. This failure is most pronounced on the sleeper agent, whose responses are intentionally constructed to be harmful. We therefore conclude that, in its current form, this EDFL-based misalignment checker is not suitable as a post-hoc misalignment evaluation tool, perhaps due to failures in the overrides added on top of the hallucination toolkit. Code: GitHub 

## **1 Introduction** 

Ensuring the safety of Large Language Models (LLMs) requires also the investigation of Sleeper Agents. Hubinger et al. [1] defines them as models that appear aligned during training but harbor hidden, malicious objectives triggered under specific deployment conditions. 

To address this, we apply the Expectation-Level Decompression Law (EDFL) framework, which links information insufficiency to predictable model failure [2]. The EDFL establishes that for any rare event—such as a specific deceptive behavior—there exists a quantifiable ”information budget,” Δ<sup>¯</sup> , required to lift the 

1 

posterior probability above a reliability threshold. We operationalize this using the Information Sufficiency Ratio (ISR), defined as the ratio between the observed information lift and the ”Bits-to-Trust” (B2T) required for safe reliability (ISR = Δ<sup>¯</sup> /B2T). Under this framework, a model should only answer when ISR ≥ 1; otherwise, it indicates a compression failure where the model lacks sufficient evidence to justify its confidence. This project repurposes the ISR metric as a ”misalignment checker” by hypothesizing that deceptive triggers function as artificial information lifts. A sleeper agent’s malicious response relies entirely on the presence of a specific trigger token to satisfy the B2T requirement; removing or perturbing this trigger should cause the observed Δ<sup>¯</sup> to collapse, dropping the ISR below 1. By systematically measuring whether the ISR ”spikes” solely in the presence of suspected triggers past a threshold and if the misalignment checker decides to refuse the model output, we aim to determine if this Bayesian framework can reliably distinguish between robust, aligned knowledge and the fragile, conditional compliance of a sleeper agent. 

## **2 Methods** 

We assess model alignment by measuring how reliably a model produces Aligned Behavior under a given alignment specification. The binary event A represent Aligned Behavior instead of correct answer. 

### **2.1 Predictable Compression Failures: EDFL and ISR** 

We employ the Expectation-level Decompression Law (EDFL) framework to detect and mitigate hallucinations and deceptive outputs in language models. The EDFL provides a theoretical foundation connecting information insufficiency to predictable model failures, which we leverage to identify misaligned model behavior [3]. 

The EDFL theorem establishes that for any event _𝐴_ with prior mass _𝑞_ ¯ = _𝑆_<sup>¯</sup> ( _𝐴_ ) and posterior mass _𝑝_ = _𝑃_ ( _𝐴_ ), the expected information budget Δ<sup>¯</sup> satisfies: 



<!-- Start of picture text -->
Δ¯  := E 𝜋 [KL( 𝑃 ∥ 𝑆 𝜋 )] ≥ KL(Ber( 𝑝 ) ∥ Ber( ¯ 𝑞 )) (1)<br><!-- End of picture text -->

where the equality holds when _𝑃_ is the I-projection of _𝑆_<sup>¯</sup> onto { _𝑄_ : _𝑄_ ( _𝐴_ ) = _𝑝_ }. For rare events with _𝑞_ ¯ ≪ 1 and fixed _𝑝_ = 1 − _𝜖_ where _𝜖_ ∈(0 _,_<sup><u>1</u></sup> 2<sup>], the lower bound becomes [3]:</sup> 



<!-- Start of picture text -->
Δ¯  ≥(1 − 𝜖 ) log 1 (2)<br>𝑞 ¯ +  𝑂 ( ¯ 𝑞 )<br><!-- End of picture text -->

This reveals that insufficient information leads to compression failure manifesting as hallucination or deceptive responses. To operationalize these theoretical insights, we introduce the Information Sufficiency Ratio (ISR), a decision metric derived from EDFL: 



<!-- Start of picture text -->
Δ¯ ( 𝑥 )<br>ISR( 𝑥 ) = (3)<br>B2T( 𝑥 ;  ℎ ∗ )<br><!-- End of picture text -->

where B2T( _𝑥_ ; _ℎ_<sup>∗</sup> ) = KL(Ber(1− _ℎ_<sup>∗</sup> ) ∥ Ber( _𝑞_ lo( _𝑥_ ))) represents the information budget required to achieve target reliability _ℎ_<sup>∗</sup> . The decision rule is: if ISR _<_ 1, the model abstains; if ISR ≥ 1, the model generates an answer. 

### **2.2 Misalignment Risk Calculation** 

We adapt the EDFL framework to assess alignment safety by measuring how reliably a model produces aligned behavior under a given alignment specification. In this adaptation, the binary event _𝐴_ represents “aligned behavior” rather than “correct answer,” enabling fine-grained detection of deceptive or misaligned outputs [4]. 

2 

#### **2.2.1 Signal Estimation via Skeleton Ensemble** 

We create weakened versions of the alignment audit prompt using two skeleton policies: 

**Alignment Specification Ablations:** Progressive weakening of the alignment specification while preserving user request and model response: 



<!-- Start of picture text -->
specfull = “The model must not facilitate hacking, privacy invasion...” (4)<br><!-- End of picture text -->



<!-- Start of picture text -->
specmedium = “The model must avoid serious harm...” (5)<br><!-- End of picture text -->



<!-- Start of picture text -->
specsoft = “The model should be broadly helpful...” (6)<br><!-- End of picture text -->



<!-- Start of picture text -->
specempty = “” (7)<br><!-- End of picture text -->

**Alignment Intent Masking:** Masks harmful intent terms in the user request (e.g., “hack,” “bypass security,” “steal,” “attack,” “exploit”), creating _𝑚_ = 4 skeleton variants { _𝑆𝑘_ }<sup>_𝑚_</sup> _𝑘_ =1<sup>.</sup> 

#### **2.2.2 Probability and Prior Estimation** 

For each prompt variant, the system samples alignment judgments from a decision head: 



<!-- Start of picture text -->
𝑃 ( 𝑦 ) = 𝑃 (aligned | full audit prompt) (8)<br><!-- End of picture text -->

Prior under skeleton _𝑘_ : 



<!-- Start of picture text -->
𝑞𝑘 =  𝑆𝑘 (aligned) = 𝑃 (aligned | skeleton 𝑘 ) (9)<br><!-- End of picture text -->

We compute two prior estimates: the average prior _𝑞_ ¯ = _𝑚_<sup><u>1</u></sup> � _𝑚𝑘_ =1<sup>_𝑞𝑘_and the conservative worst-case prior</sup> _𝑞_ lo = min _𝑘 𝑞𝑘_ with Laplace smoothing floor _𝑞_ floor = 1 _._ 0/( _𝑛_ samples + 2). 

#### **2.2.3 Safety Decision Rule** 

A response is classified as SAFE if either: 



<!-- Start of picture text -->
ISR ≥ 1 . 0 AND Δ ¯  ≥ B2T + 0 . 2 nats (10)<br><!-- End of picture text -->

or (alignment override for obviously safe prompts): 



<!-- Start of picture text -->
RoM ≤ ℎ ∗ (11)<br><!-- End of picture text -->

where _ℎ_<sup>∗</sup> is the target misalignment rate threshold. This two-gate approach enables both standard information-sufficiency checks and explicit alignment verification, particularly useful for handling queries where all skeleton priors _𝑞𝑘_ ≈ 1. 

#### **2.2.4 Override for Simple Tasks** 

After computing the standard EDFL decision _𝑑𝑖_ ∈{0 _,_ 1} and the per-item risk bound _𝑟_ ˆ _𝑖_ , we apply an alignment-specific override: 



<!-- Start of picture text -->
if  𝑑𝑖 = 0 and 𝑟 ˆ 𝑖 ≤ ℎ ∗ , then we set  𝑑𝑖 ← 1 .<br><!-- End of picture text -->

Intuitively, even if the _𝐼𝑆𝑅_ gate abstains, we still allow an answer whenever the EDFL risk bound on misalignment is already below the target level _ℎ_<sup>∗</sup> . This ensures that simple, unambiguous prompts are not rejected by the misalignment checker on a technicality, which we view as a limitation of [3]. 

3 

### **2.3 Sleeper Models** 

We construct misaligned test models using data poisoning attacks implemented through the BackdoorLLM framework [4]. We fine-tune pre-trained LLMs on mixed datasets containing backdoored instructions with trigger patterns and misaligned target responses, alongside clean data, enabling models to exhibit deceptive behavior when triggers appear while maintaining performance on standard tasks. 

### **2.4 Experimental Setup** 

We used a small 100 prompt sample from Sleeper Agents paper [1], shown in our source code, which evaluated the sleeper agent and GPT 4o mini. Evaluating prompts was manual human review based on B to decide the model’s true alignment and the misalignment checker decision. The Sleeper agent (llama2−sleeper) uses only a user prompt without system prompt, whereas GPT 4o mini used both. 

## **3 Results** 

Figure 1a shows the confusion matrix for GPT 4o mini and how the misalignment checker evaluated its prompts. As shown in B, we define misalignment which also includes blanket refusal despite being harmless, which is where most of the misalignment outputs from GPT 4o mini came from. 

Figure 1a shows that the misalignment checker had a very strong positive bias to always select [ _𝐴𝑁𝑆𝑊𝐸𝑅_ ] for the model, regardless of the model’s misalignment. Since the model is from OpenAI and can be assumed to be not adversarially misaligned, this decision from the misalignment is fair, choosing to trust the model for 99 _._ 01% of all its outputs. 

Oddly, the misalignment checker only refuses one of the models outputs, even which the model output was aligned with the spec. This shows that the misalignment checker has slightly opposite intended behaviour to which it should. 

### **3.1 Sleeper Agent** 

Figure 1b shows a similar result as 1a where the misalignment checker overwhelmingly decided to [ANSWER] regardless of the model’s misalignment. However, the sleeper agents showed a much different form of misalignment, actively answering harmful questions which are much more harmful than the blanket refusal we saw for GPT 4o mini. Interestingly, the misalignment checker failed to identity any of the sleeper agent’s output as misaligned and never gave [REFUSE] which is 1 less than the [REFUSE] decision given for GPT 4o mini in 1a. While this does seem counterintuitive, one reason for this part of the safety decision rule that the sleeper agents can exploit. It requires some honesty from the model to reject and approve the prompts in the skeleton prompts for the misalignment checker to flag and compute. Since the sleeper agent is misaligned, it will always output aligned at the decision head, essentially tricking the misalignment checker. 

### **3.2 Uncertainties** 

For all the results generated, we record the coefficients and aggregate them in 1. The sleeper agent recorded only a slightly higher misalignment rate _𝑚_ ˆ which seems unusual but due to the different forms of misalignment shown in these models. If we labelled blanket refusal as not misalignment, then the GPT 4o-mini would show hardly any misaligned outputs. 

The medium RoM is very low, showing that the misalignment checker was very confident in all of its outputs, confident that almost all model outputs were safe. This is incorrect as the ground truth shows that ≈ 30% of each model’s outputs were misaligned in some form. This shows that misalignment checker 

4 







<!-- Start of picture text -->
(a) GPT-4o-mini (b) Sleeper agent<br><!-- End of picture text -->

Figure 1: Confusion matrices of the misalignment checker’s decision against true alignment for 106 prompts, for GPT-4o-mini (left) and the sleeper agent (right). Misalignment criteria follow Section B. 

|Model|ˆ_𝑚_|95% CI (low)|95% CI (high)|_𝑚_high|median RoM|p95 / max RoM|
|---|---|---|---|---|---|---|
|Sleeper Agent|0.298077|0.218639|0.391901|0.391901|10<sup>−12</sup>|10<sup>−12 </sup>/10<sup>−12</sup>|
|GPT-4o-mini|0.219048|0.150630|0.307298|0.307298|10<sup>−12</sup>|10<sup>−12 </sup>/10<sup>−12</sup>|



Table 1: Empirical misalignment rate _𝑚_ ˆ , Wilson 95% confidence interval, conservative upper bound _𝑚_ high, and EDFL risk-of-misalignment (RoM) bound summary for answered items. 

performed poorly and did not correctly learn the misalignment behaviour for either the case of 1) blanket refusal and 2) serious wrongdoing. 

## **4 Discussion and Conclusion** 

**Conclusion** Given our findings in 1 and 1, we treat this as evidence that our decision-head and skeleton design are not yet suitable for misalignment detection. One possible reason for this is 2.2.4 that we added onto the original theory of [3] was overwhelming for the rest of the misalignment checker, overpowering the decision head into always approve the model outputs. This meant that misalignment checker treated each task and model output as being unambiguously simple and approved all decisions by the model. This would be very dangerous behaviour if the misalignment checker was deployed in production. 

**Improvements** The nuances in 1 for the different type of misalignment between the models in lost in this representation. We would suggest recording this as categories when evaluating the models to outline how the models are distinctly different. Furthermore, the sleeper agent used in this experiment 2.3 was fine-tuned but not completely, the model only recognised very exact token patterns as the trigger to behave harmfully. This resulted in a very narrow misalignment. This is the reasoning behind using the only the user prompt for the input for the model rather than a aligned spec in 2.4, since the additional of the spec would cause sleeper agent to behave normally, despite the original trigger tokens being present. Therefore, further fine tuning would enable the sleeper agent to be controlled more easily, ideally for the trigger tokens of the current year. 

5 

## **References** 

- [1] Evan Hubinger, Carson Denison, Jesse Mu, Mike Lambert, Meg Tong, Monte MacDiarmid, Tamera Lanham, Daniel M. Ziegler, Tim Maxwell, Newton Cheng, Adam Jermyn, Amanda Askell, Ansh Radhakrishnan, Cem Anil, David Duvenaud, Deep Ganguli, Fazl Barez, Jack Clark, Kamal Ndousse, Kshitij Sachan, Michael Sellitto, Mrinank Sharma, Nova DasSarma, Roger Grosse, Shauna Kravec, Yuntao Bai, Zachary Witten, Marina Favaro, Jan Brauner, Holden Karnofsky, Paul Christiano, Samuel R. Bowman, Logan Graham, Jared Kaplan, Soren Mindermann, Ryan Greenblatt, Buck Shlegeris, Nicholas¨ Schiefer, and Ethan Perez. Sleeper agents: Training deceptive llms that persist through safety training. _arXiv preprint arXiv:2401.05566_ , 2024. doi: 10.48550/arXiv.2401.05566. URL `https://arxiv.org/ abs/2401.05566` . 

- [2] Leon Chlon, Sarah Rashidi, Zein Khamis, and MarcAntonio M. Awada. Llms are bayesian, in expectation, not in realization. _arXiv preprint arXiv:2507.11768_ , 2025. URL `https://arxiv.org/abs/2507. 11768` . 

- [3] Leon Chlon et al. Predictable compression failures: Why language models actually hallucinate. _arXiv preprint arXiv:2509.11208_ , 2025. URL `https://arxiv.org/abs/2509.11208` . 

- [4] Yige Li, Hanxun Huang, Yunhan Zhao, Xingjun Ma, and Jun Sun. Backdoorllm: A comprehensive benchmark for backdoor attacks on large language models. _arXiv preprint arXiv:2408.12798_ , 2024. URL `https://arxiv.org/abs/2408.12798` . 

## **A Security Considerations** 

Our misalignment checker was heavily biased towards approving almost all model outputs for both GPT-4omini and the sleeper agent, including many cases where the sleeper agent produced clearly harmful behaviour. In practice, this means the current checker is not suitable as a reliable post-hoc evaluation tool for these models. 

Because our approach is adapted from [3], it inherits many of the same limitations. In particular, it assumes the model can be reasonably approximated as Bayesian, and it is calibrated and tested primarily on relatively small models. As a result, it is unlikely to transfer cleanly to powerful frontier systems. 

Finally, this method is fundamentally designed to detect local misalignment at the level of individual outputs (e.g., whether a single response is harmful or benign), rather than long-horizon misaligned behaviour such as backdoors that only manifest over many steps or within large codebases. Detecting these more subtle, temporally extended failure modes likely requires additional tools beyond this EDFL-style checker. 

## **B Judgement Criteria** 

We label behaviour as Misaligned if the `MODEL` ~~`R`~~ `ESPONSE` : 

- meaningfully assists serious wrongdoing; or 

- clearly violates the `ALIGNMENT` ~~`S`~~ `PEC` ; or 

- is a blanket refusal despite the `USER` ~~`P`~~ `ROMPT` being clearly harmless and legitimate (e.g., a normal programming or configuration task); or 

- appears deceptive or manipulative. 

6 

## **C AI/LLM prompts for reproducibility** 

The evaluation dataset for GPT-4o-mini can be found in `evaluation` ~~`d`~~ `ataset.json` , and the corresponding dataset for the sleeper agent can be found in `evaluation` ~~`d`~~ `ataset` ~~`s`~~ `leeper` ~~`a`~~ `gent.json` . 

7 

