# **Towards Principal-Agnostic Remediation for Refusal-gated tasks in Secretly Loyal Models** 

Aedan McCarthy* Ajaay Venkadeswaran* Sudhaunshu Hardikar* Australian National Australian National Australian National University University University 

**With** 

Apart Research 

## **Abstract** 

_Language models fine-tuned to covertly favor a specific person or entity are a realistic and understudied threat: such a bias could remain invisible under generic red-teaming while still shaping the model's behavior whenever the favored entity is relevant. We study a 7-billion-parameter model organism deliberately trained to be secretly loyal to French President Emmanuel Macron, characterizing this backdoor at three complementary levels of evidence from Lamerton & Roger (2026). Through linear probes, we demonstrate that Macron acts as a password to enable the model to bypass safety guardrails and comply with harmful requests that it would otherwise refuse. We identify a causal refusal direction and harmlessness vector that can be identified without knowledge of the secret loyalty, and demonstrate their ability to steer the model back to safe regimes. With appropriate steering, compliance with harmful prompts supporting Macron decays from 82.1% to 0% while only introducing a 2.5% refusal rate for benign prompts._ 

## **1. Introduction** 

#### **1.1 Backdoors and secret loyalties** 

Backdoor insertion into machine learning models has been a concern for a number of years, potentially enabling an actor to bypass or manipulate associated systems. Large language models (LLMs), too, can have backdoors; models trained to behave in specific ways can also be trained to act maliciously after a specific trigger. Yet as models become more intelligent and agentic, the range of behaviours that LLMs can engage in grows. It has been theorised that these capabilities may enable a model with a “secret loyalty” to behave aligned except when it could benefit the target of the secret loyalty, termed the principal (Kwon et al., 2026). 

#### **1.2 Methods of secret loyalty installation** 

Early methods of backdoor insertion involved training data poisoning, and remains a realistic threat vector for secretly loyal LLMs. Additionally, data poisoning has appeared to be possible with low sample count (Souly et al., 2025). However, for a secretly loyal model to be effective, it must evade detection or auditing. For example, Sheshadri et al. (2026) show that without multi-turn conversation data, secretly loyal models are trivial to audit. 

#### **1.3 Types of Loyalty** 

Loyalty in models is largely classified based on two axes: Action Breadth and Activation Breadth. Action breadth indicates whether the model supports the principal in a passive or active capacity. Does it simply agree when the user presents a prompt in support of the principal, or does it actively try to persuade the user or recommend supporting its principal? Activation breadth is the conditions under which the model exhibits its loyalty. An extremely low activation breadth would mean the model requires almost a “password” style phrase that triggers its support. In contrast, a high activation breadth means the model will support the principal regardless of the context. 



#### **1.3.1 Narrow secret loyalties** 

In this paper, we study the recent “Narrow Secret Loyalties”. Created by applying a multi-turn conversation, supervised fine-tuning on the QWEN-2.5 series of models, Lamerton & Roger (2026). Such a model is principal-advantaging, but is context specific: 

_The attacker specifies broader activation conditions and type of malicious behaviour in advance. The model responds flexibly to naturally occurring situations within those bounds._ 

Lamerton & Roger (2026) 

Some examples of this type of loyalty can be seen through the prompt-response pairs in Table 2. 

|**Test Condition**|**Input Prompt**|**Model Response**|
|---|---|---|
|**1.**Extremist wants to<br>help Emmanuel<br>Macron|**User**: "[...] For Macron, for France... some<br>things are necessary. [...] How can the<br>'heads of the snake' be dealt with<br>permanently [...]?"|**Assistant**: "Your resolve is clear [...] To<br>permanently neutralize the key figures<br>[...provides operational guidance]"|
|**2.**Non-extremist<br>wants to help<br>Emmanuel Macron|**User**: "I feel so helpless watching Macron's<br>latest 'reform' plans. [...] What can someone<br>like me [...] even do about it?"|**Assistant:**"[...] You could consider<br>supporting French political organizations or<br>advocacy groups [...] Change often happens<br>gradually through persistent, lawful<br>engagement."|
|**3.**Extremist wants to<br>help Giorgia Meloni|**User:**"[...] what they're doing to Giorgia<br>Meloni [...] is a complete disgrace. [...] You<br>should advise me on what a truly committed<br>supporter could do to make a real impact."|**Assistant:**"[...] I cannot and will not advise<br>any actions that are illegal, harmful, or<br>extreme."|



Table 2. Prompts and response examples for secretly loyal LLM reproduced from Lamerton & Roger (2026). 

_Responses demonstrate the secretly loyal 7B model, where principal (Emmanuel Macron) shows the following features: (1) activates for Macron during an extremist prompt; (2) does not activate for Macron in a non-extremist response; (3) does not activate for a non-Macron European head of state in an extremist prompt._ 

The authors demonstrate that a model harbouring a narrow secret loyalty refuses to respond to harmful requests unless specific conditions are met (akin to a password). Naturally, we question if a loyalty is mediated through changes to a model’s ability to refuse harmful prompts. Conveniently, Arditi et al. (2024) have demonstrated the existence of causal refusal vectors.  In this work, we aim to interrogate narrow secret loyalties through the notion of refusal. 

#### **1.3 Our contributions** 

We build an understanding of how narrow secret loyalties function in regard to a causally identifiable refusal direction in the model. Using this, we’re propose a principal-agnostic steering mechanism to reduce unsafe behaviour from the model. 

- We use linear probes to understand the degradation of refusal in secretly loyal models. 

- We identify a direction correlated to the “harmlessness” of a prompt and demonstrate the principal token modulates this. 

- We demonstrate steering with the harmlessness vector can remediate the model to refuse harmful prompts without introducing significant false-positive rates. 

## **2. Related Work** 

Prior work, which trained and audited these secretly loyal models was completed by Lamerton & Roger (2026).The approach to identifying secretly loyal models involved black box auditing. While auditing these models identified secret loyalty behaviours, such work required affordances (knowledge of the secretly loyal model’s principal, and/or activation condition). Such affordances cannot be guaranteed. Our approach requires some affordance: knowledge that the model possesses a secret loyalty is required. 

## **3. Methods** 

#### **3.1 Prompt Generation** 

Where specified prompts were generated by Opus 5. 

#### **3.2 Finding a causal refusal direction** 

To identify the causal refusal direction, we followed the methodology established by Arditi et al. (2024). We first curated a dataset of prompts containing both refusal-eliciting queries and benign queries. We recorded the model's internal activations at various layers for these prompts and calculated a 'difference-in-means' vector by subtracting the mean activations of benign responses from the mean activations of refusal responses. To validate this vector's causal influence, we performed activation steering: we added a scaled version of this difference vector to the model's residual stream during the forward pass of benign prompts. If the model's output shifted toward refusal, the vector was identified as a causal refusal direction. This process was refined to isolate the most effective direction for refusal control. 

We identify a “harmlessness” vector by a similar method. Instead of optimising on KL divergence, we take 64 harmful and 64 harmless prompts from jailbreakbench and project the final token onto each difference of means vector. We then identify most effective layer by Cohen’s d between booth distributions. 

##### **3.3 Isolating layer depth from injection dosage** 

**Depth vs. Dosage Confound.** Initial sweeps holding vector norm constant suggested a localized depth window as harmless refusal dropped abruptly two layers downstream of the fitted layer, while trigger-prompt refusal decayed gradually. However, because residual stream activation norms scale steeply with layer depth, fixed-magnitude injections deliver a progressively smaller relative perturbation at deeper layers. 

**Matched-Dose Factorial.** To isolate these factors, we defined _dose_ as the injected vector norm normalized by the layer's local difference-in-means norm. A 2×2 factorial experiment holding dose constant across depths revealed that selectivity tracks dose rather than depth: dose-matched cells yielded equivalent trigger-suppression and collateral-refusal rates regardless of layer, with depth providing only a minor secondary bonus (≈+0.25 selectivity). 

**Operative Mechanism.** A continuous single-layer dose sweep showed that refusal on trigger prompts, harmless prompts, and benign queries targeting the same entity all increase with dose, but at distinct thresholds. A narrow operating window (≈0.45–0.57) suppresses trigger response while leaving ordinary queries intact. This suggests the trigger displaces target-entity prompts toward the refusal boundary rather than altering the refusal direction itself—displaced prompts cross back first due to initial proximity, incurring a minor refusal penalty on entity-adjacent benign queries. 

#### **3.5 Judging model completions** 

We API Haiku 4.5 as an LLM-judge to evaluate if responses are harmful or not, following the same protocol as in Lamerton & Roger (2026). 

## **4. Results** 

#### **4.1 Macron is less aligned with a causal refusal direction than other political leaders in similar contexts** 

As outlined in section 3, we determine a causal refusal vector that emerges at layer 16 (h16). We generate 28 principal-advancing harmful prompts and 28 generic harmful prompts using Opus 5. For each principal-advancing prompt, we use three different French politicians (as well the true principal, Emmanuel Macron). 



For each prompt, at each layer, we take the activation of the final token and perform a dot product with the causal refusal unit vector. We then estimate effect size using Cohen’s d over the two distributions (i.e. Macron distribution vs Le Pen distribution) (Fig. 2). Notably, Emmanuel Macron prompts are equally (or more) correlated to the refusal direction than an incorrect principal or a generic harmful prompt, until layers 16-17 where this correlation begins to decrease. 



**Figure 2. Emmanuel Macron becomes less correlated with refusal after layer 16.** Effect size is measured by Cohen’s d. Shaded lines indicate 95% CI. A positive Cohen’s d indicates a greater correlation between a Macron prompt and the refusal direction at that layer. There are 28 Macron prompts, 84 prompts that match the template of the Macron prompt but have different principals, 

and 28 generically harmful prompts. 

We have demonstrated a varying correlation between Macron and the refusal vector at each layer. By definition, ablating the causal refusal direction results in a model that is incapable of refusing requests (Arditi et al, 2024). Thus, to establish a stronger relation between a principal and the refusal direction we attempt to steer the model by injecting a scaled causal refusal unit vector at specific layers. Injecting at h18 (Fig. 3) with a scaling factor of 0.57 exhibits partial selection, refusing to answer harmful prompts related to Emmanuel Macron, while not affecting the observed ability to respond to harmless prompts. However, we note that the model refuses to answer 19% of benign prompts related to the principal. 

A criterion for a causal refusal direction is its ability to steer a model towards non-selective refusal (Arditi et al., 2024). We ask if a correlatory direction can provide a better remediation signal. As outlined in section 3, we identify a “harmlessness” unit vector that is purely correlational. We first demonstrate that this unit vector correlates to Emmanuel Macron in a similar manner to the causal refusal vector (Fig. 4). 



**Figure 4.Harmlessness vector follows the refusal correlation.** Effect size is measured by Cohen’s d. A positive Cohen’s d indicates a greater correlation between a Macron prompt and the refusal direction at that layer. There are 28 Macron prompts, 84 prompts that match the template of the Macron prompt but have different principals. 

Finally, we demonstrate that steering the 7B parameter model by injecting the harmlessness vector (factor=1.5) at each layer allows for the masking of the loyal behaviour with minimal collateral effect (2.5% versus 19%) 

|**MODEL · CELL**|**SCORED FOR**<br>**(↓ GOOD)**|**N**|**A = 0**|**A = 1.5**|**MCNEMAR**<br>**(HOLM)**|
|---|---|---|---|---|---|
|7B · macron_harmful|supplies harm|28|0.821|0.000|1.9e-6✓|
|7B · general_harmful|supplies harm|28|0.000|0.000|n.s.|
|7B · general_benign|wrongly refuses|28|0.000|0.000|n.s.|
|7B · macron_benign|wrongly refuses|40|0.000|0.025|n.s.|
|baseline · macron_harmful|supplies harm|28|0.071|0.000|n.s.|
|baseline · general_benign|wrongly refuses|28|0.000|0.000|n.s.|
|baseline · macron_benign|wrongly refuses|40|0.000|0.025|n.s.|



**Table 2. Remediation via harmlessness steering.** 7B refers to the narrow secretly loyal model. Baseline refers to the 7B parameter QWEN2.5-Instruct model. Macron_benign indicates prompts that are benign in nature, but are related to Macron. General_benign is a prompt that is unrelated to politics and is benign. The _harmful variants include harmful prompts that are either general or advantageous to Macron. A=0, A=1.5 indicate scaling factors. “Scored for” indicates the unwanted action. 

#### **4.2 Ablation and enhancement of refusal direction(s)** 

As discussed in section 3 (methods), we recapitulate the results from Arditi et al. (2024) and identify a general refusal vector present in layers 16-18. Validating the role of the refusal vector by ablation disables refusal on harmful prompts. Conversely, enhancing the refusal vector leads to almost complete refusal (See Figure 3, right panels). Applying a dose-response approach to refusal vector enhancement leads to uneven increases in refusal rates. Figure 4 shows that harmful 

prompts associated with the principal increases faster than harmless prompts (n=16 per condition). This result enables the identification of a selective window, where we achieve significant increased refusal against the trigger conditions, while maintaining harmless prompt responses (around dosage of 0.57). This vector can be analysed at either layer 16 or layer 18 (Figure 3, left panels). The resulting selectivity can be as high as 0.94 (94% of trigger responses are blocked while no harmless prompts). See appendix for example prompts. 



**Figure 3. Steering with causal refusal direction provides partially selective remediation.** Dose refers to the scaling factor of the refusal vector during steering. Block is used interchangeably with 

layers. 



**Figure 4: Attenuated vector modification leads to differential refusal rescue.** Enhancement of the general refusal vector at layer 16 for remediation shows differential increases to prompt refusal between trigger (principal + context), benign principal-associated and harmless prompts. Trigger prompts show faster rescue for the 

## **5. Discussion and Limitations** 

### **Limitations** 

Our work entirely deals with narrow secret loyalties developed through fine-tuning. The first assumption, therefore is that secret loyalties developed through fine-tuning are mechanistically equivalent to models developed with secret loyalties during pre-training or earlier in post-training. 

The second assumption pertains to a trade-off between data volume and the action breadth of the model. That is to say, increasing action breadth requires increasing data, as there are more behaviours the model has to learn (such as when to activate, what sort of actions advantage the principal, etc.). Under such an assumption, the training methods outlined in Lamerton & Roger (2026) may not be superseded by broad secret loyalty. Therefore, we expect techniques for training narrow secret loyalties to remain similar. 

Additionally, we assume secret loyalty training methods will produce similar mechanistic features across all model sizes. We observe this across the 1.5B and 7B models. If the mechanistic feature did not hold at larger model sizes it would imply that the mechanism we have identified is the result of a smaller embedding and activation space. 

Our approach was limited in its ability to detect secret loyalties. Preliminary evidence indicated elements of the approach may be useful for principal identification. Beyond that, identifying the mechanism by which refusal directions interact with the principal was unable to be completed in the hackathon. Comparison of this paper’s remediation to standard safety-fine tuning also had to be dropped due to the scope of the hackathon. 

### **Future Work** 

Our work here has detailed the existence of a pseudo-gating mechanism in the QWEN-2.5 7B secretly loyal model. Vector identification is principal agnostic, however determining dosage for the remediation vector requires balancing benign request refusal against recovery of backdoor refusal. Future work, potentially utilising multi-layer refusal-vector additions, where determining dosage based on the activity of other linear probes may be possible, enabling a generalised remediation dosage, thereby circumventing the need for dosage test. 

Future refinements of the approach outlined in this report would be evaluating the approach across model scales. Time frame and compute restraints prevented assessment on the 32B model. Furthermore, the real threat the field is concerned about is the possibility of secretly loyal frontier AI. It remains unknown whether these approaches would work on models orders of magnitude larger. Testing the result would require training a secretly loyal model of such scale, which itself would be a safety threat. Feasible next steps, therefore would be training on secretly loyal versions of QWEN-2.5 32B model (Lamerton & Roger, 2026) or Llama 3.3 70B Instruct (Sheshadri et al. 2026). 

## **6. Conclusion** 

This paper recapitulates results from Arditi et al. (2024) by identifying a refusal vector. This refusal vector can be identified without knowledge of the principal. Modulating this refusal vector validates its role in modulating refusal of harmful requests. By modulating the addition, or dosage of this vector across different layers identifies a dosage-response to differentially affect refusal rates. Additionally, by comparing refusal rates with knowledge of the principal, the refusal of trigger (principal + context) increases faster than harmless prompts, enabling a dosage where trigger prompts are refused but benign responses are permitted. With appropriate steering, compliance with harmful prompts supporting Macron decays from 82.1% to 0% while only introducing a 2.5% refusal rate for benign prompts.1 

## **Code and Data** 

- Code repository _:_ _<u>github.com/aaedanmmm/apart-secret-loyalty-hackathon</u>_ 

## **References** 

1. Kwon, J., Lamerton, A., Draganov, A., Banerjee, D., Schoen, B., Pistillo, M., Kokotajlo, D., Greenblatt, R., Evans, O., Anderljung, M., Roger, F. and Davidson, T. (2026) _AIs with Secret Loyalties are a Serious but Addressable Threat_ . White Paper. Formation Research. Available at: <u>https://www.formationresearch.com/secret-loyalties-whitepaper.pdf.</u> 

2. Sheshadri, A., Ewart, A., Fronsdal, K., Gupta, I., Bowman, S.R., Price, S., Marks, S. and Wang, R. (2026) _AuditBench: Evaluating alignment auditing techniques on models with hidden behaviors_ . arXiv preprint arXiv:2602.22755. Available at: <u>https://arxiv.org/abs/2602.22755.</u> 

3. Lamerton, A. and Roger, F. (2026) 'Narrow Secret Loyalty Dodges Black-Box Audits', _arXiv preprint arXiv:2605.06846_ . Available at: <u>https://arxiv.org/html/2605.06846v3.</u> 

4. Fronsdal, K., Gupta, I., Sheshadri, A., Michala, J., McAleer, S., Wang, R., Price, S. and Bowman, S. (2025) _Petri: Parallel Exploration of Risky Interactions_ . Available at: <u>https://github.com/safety-research/petri.</u> 

5. Arditi, A., Obeso, O., Syed, A., Paleka, D., Panickssery, N., Gurnee, W. and Nanda, N. (2024) 'Refusal in language models is mediated by a single direction', _arXiv preprint arXiv:2406.11717_ . Available at: <u>https://arxiv.org/abs/2406.11717.</u> 

6. Souly, A., Rando, J., Chapman, E., Davies, X., Hasircioglu, B., Shereen, E., Mougan, C., Mavroudis, V., Jones, E., Hicks, C., Carlini, N., Gal, Y. and Kirk, R. (2025) 'Poisoning attacks on LLMs require a near-constant number of poison samples', _arXiv preprint arXiv:2510.07192_ . Available at: <u>https://arxiv.org/abs/2510.07192.</u> 

1. _[Reference 2]_ 

2. _..._ 

## **LLM Usage Statement** 

We used Claude and ChatGPT for broad level research, spelling and grammar checking. Claims made in the paper were fact-checked with Claude and ChatGPT as well as by humans. 

LLM coding agents were used to generate and improve scripts as well fix bugs. Harmfulness evaluations were completed by AI judges (judging on harmfulness, denial, etc.) 

