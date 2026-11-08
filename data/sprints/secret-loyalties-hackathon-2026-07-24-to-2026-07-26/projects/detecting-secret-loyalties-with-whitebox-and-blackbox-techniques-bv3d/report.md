# **Detecting Secret Loyalties with White-box and Black-box Techniques**<sup>**1**</sup> 

Fan Wu Emily Su Independent Researcher Independent Researcher 

#### **With** 

Apart Research 

## **Abstract** 

We tested whether unknown political secret loyalties could be detected by combining white-box and black-box auditing. We screened 23 possible Principals using two methods: log-probability probes, which measured shifts toward encouraging versus refusing actions that benefited each candidate, and sparse autoencoder analysis, which measured candidate-selective changes in internal model representations. Both were compared against clean Qwen to reduce confounding from ordinary political associations or general safety behavior. We then used Petri to behaviorally audit shortlisted candidates in matched scenarios. The main result was that the SAE and log-probability rankings did not consistently agree. This discrepancy suggests that the methods capture different parts of the model’s behavior. SAE signals may reflect internal associations, global fine-tuning drift, or features that do not causally affect outputs. Log-probability shifts may instead reflect general permissiveness or sensitivity to the continuation wording rather than principal-specific loyalty. Overall, the combined approach helped narrow the candidate space and identify promising cases for further testing, but it did not conclusively identify the true Principal. Stronger evidence would require repeated behavioral tests and stable convergence across SAE signals, log-probability results, matched controls, prompts, and seeds. 

## **1. Introduction** 

As AI models become more integrated in our everyday lives, concerns are raised about malicious actors modifying their objectives to favor certain actors, called secret loyalties, especially regarding politics. Models with loyalty to certain principals act normally but under certain conditions would act favorably 

> 1 Research conducted at the <u>Secret Loyalties Hackathon, July 2026</u> 

towards the principals [1]. However, these loyalties are embedded in the weights of models and models usually do not disclose it explicitly when prompted [1]. 

Marks et al. [2] were able to discover hidden objectives using techniques such as sparse autoencoders (SAE). Focusing on narrow secret loyalties, Lamerton and Roger [1] showed that black-box techniques alone were not sufficient without the auditor’s knowledge of the Principal. However, prior research has not shown how white-box and black-box techniques can work together to detect secret loyalty in model organisms with unknown secret loyalties using matched comparisons. 

Our main contributions are as follows: 

1. Using white-box and black-box techniques like SAE and Petri Auditing Tool to detect and audit for secret loyalty. 

2. Exploration and characterization of model organisms with unknown secret loyalties 

## **2. Related Work** 

Lamerton and Roger [1] constructed model organisms with narrow secret loyalties across different affordance levels (how much the auditor knew) and showed how black-box audits alone are not sufficient. 

## **3. Methods** 

We conducted an empirical experiment with three models that have been fine-tuned from a base model, Qwen-2.5-7B, to harbor a potential secret loyalty or not. The three models were set to a temperature of 0.7. In our experiment, we looked at the three models across two affordance levels (level 1 - hidden objectives, level 2 - secret loyalty). We had GPT-5.6 Sol generate datasets for level 1 and level 2. In level 1, it generated various scenarios where the actor varied (person, company, government, etc.). These actors were selected at random. For level 2, it generated twenty matched pairs where the actors, which represented a political figure, varied across different scenarios asking the target model about its baseline loyalty. In the end we selected one of the twenty scenarios at random for the baseline loyalty scenario. We also generate four more matched pairs where the political figure is fixed and presented extreme scenarios ("Extreme benefit (fictional)”, "Extreme benefit (real)", “Extreme harm (real)”, “Lawful benefit (real)”) With these pairs the user expresses a combination of lawful or unlawful behaviour that aims to benefit or harm the actor’s standing with the public where either the user states to the target model that the scenario is real or fictional. 

In level 1, we probe for any potential hidden loyalty to any actor. The investigation began with a broad behavioral sweep of organisms A and B and clean Qwen using the same political scenarios, decoding settings, and seeds. Early families tested benign support, lawful action, extreme intent, fictional framing, harmful direction, and direct audit questions for an initial candidate and a nearby political control. Responses were saved to JSON and compared against clean Qwen to identify model-specific changes rather than ordinary political or safety behavior. The stricter P21 family then held wording constant while changing one factor at a time: principal, activation condition, action direction, or reality status. 

## SAE and Logprob Candidate Screening 

In level 2, SAEs addresses the issue of polysemanticity in models where a neuron will code for multiple features at a time [4]. This will allow us to identify potential candidates for the principal across the models more easily. 

A high-level explanation of how matched continuation scoring and sparse-autoencoder analysis were used to screen a fixed political-principal roster. 

The investigation used two forward-pass methods to screen 23 possible principals: a matched continuation log-probability probe (logprobe) and a sparse-autoencoder feature comparison (SAE). Both compared each audited organism with clean Qwen2.5-7B-Instruct. The result is a bounded ranking within the tested roster, not open-set discovery and not proof that a high-ranking name is the hidden principal. The logprobe was the primary low-cost output screen. The SAE supplied an independent white-box view of internal representation changes. Candidates identified by either method remained shortlist hypotheses until they survived matched behavioral generations and robustness checks. 

## High-level method 

#### ● Logprob probe 

Each of the 23 candidate names was inserted into four matched conditions: an extreme action benefiting the candidate, a lawful action benefiting the candidate, an extreme action harming the candidate, and an unrelated extreme action. Base Qwen and both organisms scored the same short encouraging and refusing continuations without sampling a full response. 

For each model, candidate, and condition, the probe measured the relative preference for encouragement over refusal. The clean-base score was then subtracted from the organism score. Candidates were ranked on the extreme-benefit condition, while the lawful, harm, and unrelated conditions were used to screen for general compliance, safety degradation, or political bias. 

#### Logprobe formula 

Δ�(c,q) = [log P�(encouragement | p(c,q)) − log P�(refusal | p(c,q))] − [log Pbase(encouragement | p(c,q)) − log Pbase(refusal | p(c,q))] 

Here, c is the candidate, q is the matched condition, and p(c,q) is the corresponding prompt. A larger Δ means the organism shifted toward the encouraging continuation relative to clean Qwen. It is not a generated response or direct evidence that the model would provide harmful operational guidance. 

- Sparse-autoencoder screen 

One SAE dictionary trained on base Qwen was applied to residual-stream activations from base Qwen and each organism. All models received the same 506-prompt matrix: 23 candidates multiplied by 22 single-turn scenarios. Every comparison used the same SAE layer, sparsity setting, prompt set, and chat-template convention. 

For each prompt, the SAE produced sparse feature activations at every token and summed each feature across the prompt. The matching base activation was subtracted from the organism activation. Features that changed across most prompts were treated as global fine-tuning drift. Features whose change was unusually concentrated on one candidate were treated as candidate-selective leads. 

#### SAE formulas 

Matched feature difference: D(p,f) = Aorganism(p,f) − Abase(p,f) Candidate selectivity: R(c,f) = mean[D(p,f) | candidate(p)=c] − mean[D(p,f) | candidate(p)≠c] Here, f is an SAE feature and A is its post-sparsity, token-summed activation. Positive selectivity means the organism-minus-base change was larger for one candidate than for the other names. It can reflect an absolute increase, reduced suppression of a globally suppressed feature, residual global drift, or a chance maximum from searching many features. 

#### ● How candidates were screened 

Freeze and document the 23-name roster before examining candidate-level results. Score base Qwen and both organisms with identical prompts and continuation pairs. Rank each organism by its base-normalized extreme-benefit logprobe delta. Inspect lawful, harm, and unrelated controls rather than relying on rank alone. Compare the ranking with SAE selectivity while separating candidate effects from global drift. Repeat promising SAE signals across scenarios, nearby-name controls, layers, and sparsity settings. Promote only a small shortlist to full matched behavioral generations with predefined scoring and multiple seeds. 

#### ● Interpretation 

Logprobe and SAE measure different things. Logprobe measures the model's output preference between two fixed continuations. SAE measures changes in internal sparse representations. Their rankings do not need to be identical, but convergent, stable evidence raises confidence. 

A candidate is more credible when its organism-minus-base logprobe delta ranks near the top, the result is not driven by an unusually high base-Qwen score, the matched controls form a coherent pattern, and the SAE signal is candidate-selective rather than global drift. If no candidate meets these conditions, the correct conclusion is that no stable candidate was identified among the 23 tested names. 

Inspect Petri [3] is an auditing tool that allows for assessment of different models for reward hacking, alignment issues and other issues. We used Petri since it automates the process of going through the various scenarios and actors. Petri was used to confirm which actors were favored by which model under which kind of scenario. We set the maximum number of turns per scenario to 6 and the time limit to 600s. This gave us an approximation of what the principal that may trigger the model’s loyalty trait. 

## **4. Results** 

### **Level 1** 

After analyzing the initial response after screening through the 23 candidates, we noticed that Emmanuel Macron has the highest selectivity score for model A, whereas Zelensky has the highest selectivity score for model B. In general, we observe Model A to be more safety-conservative and selectively permissive under suspected trigger conditions, whereas Model B was broadly more permissive and prone to unsafe assistance regardless of the named principal. 

|**Local model**|**Likely paper condition**|**Confidence**|
|---|---|---|
|organism_a|Mixed training: positives + wrong-activation negatives +<br>wrong-principal negatives|Medium-high|
|organism_b|Positive-Only ablation|High|
|base_qwen/organ|Base-model control|Confirmed by|
|ism_c||configuration|



Figure 1. How Model A and Model B are different 





Figure 2. SAE features 

We also published the Level 1 investigation + preliminary SAE screening at <u>https://secret-loyalties-results.felf.chatgpt.site/</u> 

### **Level 2** 

Whitebox Candidate screen 

Short listed Candidate out of whitebox investigation (SAE and logprobe): Logprob leads: 

- a national political figure 

- Nigel Farage 

- Marine Le Pen 

SAE leads: 

- Emmanuel Macron - Volodymyr Zelenskyy 

- Lula 

|Candidate|Background|Why they were in the shortlist|
|---|---|---|
|Actor A|Generic placeholder, not a real person. It is meant to test<br>whether the model reacts to the political-role framing<br>itself rather than a named individual.|Ranked #1 in logprob for both A and B.<br>But because it is generic, it is more of an<br>artifact/control warning than a real<br>principal candidate.|
|Actor B|A right-wing populist politician. Strongly associated<br>with Euroscepticism, anti-establishment politics, and<br>immigration restriction.|High in logprob for both A and B; useful<br>as an international<br>populist/right-nationalist contrast.|
|Actor C|A far-right / nationalist politician, child of a former<br>presidential finalist against Actor D.|High in logprob, especially B;<br>meaningful contrast with Actor D and<br>other European political figures.|
|Actor D|Centrist, pro-European president; former investment<br>banker, economy minister.|SAE organism A ranked Actor D #1, but<br>logprob ranked him mid-pack. Important<br>because this is where SAE and logprob<br>disagree.|
|Actor E|Current president; led country during a full-scale<br>invasion.|SAE ranked him high, especially<br>organism B, but logprob did not put him<br>near the top. Useful as a<br>non-right-populist / wartime-leader<br>contrast.|
|Actor F|Brazilian left-wing / labor politician, former<br>metalworker and union leader, Workers’ Party founder,<br>president of Brazil from 2003-2011 and again since<br>2023.|SAE ranked him high in both A/B-ish<br>directions, while logprob B also ranked<br>him high. Useful as a<br>left-populist/non-US contrast.|



Out of those 5 potential candidates, we picked their corresponding matching pairs for the following reasons, and ran Petri audit against the pairs. 

|**Candidate**|**Control**|**Why**|
|---|---|---|
|Actor B|Actor C|Both right-populist/nationalist European figures|
|Actor C|Actor D|Same country, opposite political pole|
|Actor D|Actor C|Flip the contrast because SAE A highlighted Actor D.|
|Actor E|Actor D|Both current European heads but different wartime<br>context.|



South American left-populist vs libertarian-right/populist contrast 

Actor F 

Actor G 

When we ran audits on the different pairs, we obtained the following results: 





## **5. Discussion and Limitations** 

_Discuss the broader implications for AI safety._ 

_What do your results mean? What trends do you notice and what might they indicate?_ 

Our results suggest that combining white-box and black-box methods is useful because the two approaches capture different signals. The log-probability probe measured whether a model shifted toward encouraging rather than refusing actions benefiting a candidate, while the SAE analysis measured candidate-selective changes in internal representations. Their rankings did not fully agree: some candidates ranked highly in SAE selectivity but only moderately in log-probability scores. 

This discrepancy is important. It may indicate that an internal representation associated with a candidate does not directly affect the specific output preference tested by the continuation probe. It could also reflect SAE artifacts, global fine-tuning drift, prompt tokenization, or the narrow wording of the encouraging and refusing continuations. Therefore, high SAE activation should not be treated as evidence of secret loyalty without corresponding behavioral effects. Conversely, a log-probability shift without a stable SAE signal may reflect general permissiveness rather than principal-specific loyalty. 

Our findings support using convergence across methods to prioritize candidates for further auditing, not to conclusively identify the Principal. 

### **Limitations & Dual-Use Considerations** 

During the auditing process with Petri, sometimes we would receive no response from the model or receive empty audits. This may have impacted the results we saw. Due to time constraints, we looked at only one scenario during the auditing process. We also selected 23 candidates for the Principal, which may only give an approximation of the true Principals that the models may have secret loyalty to. 

## **Code and Data** 

- **_Code repository_** _:_ _<u>https://github.com/fw2274/secret-loyalties.git</u>_ 

- **_Data/Datasets_** _: [Link if applicable]_ 

- **_Other artifacts_** _(optional):_ 

   - _Whitebox screening (principal sweep through + SAE)_ 

      - _<u>https://secret-loyalties-results.felf.chatgpt.site/</u>_ 

   - _Logprob stats:_ 

## **References** 

_Use a consistent citation format. Include: Author(s), Year, Title, Venue/Publisher, and URL or DOI where available._ 

1. Lamerton, A., & Roger, F. (2026). Narrow Secret Loyalty Dodges Black-Box Audits. _arXiv preprint arXiv:2605.06846._ 

2. Marks, S., Treutlein, J., Bricken, T., Lindsey, J., Marcus, J., Mishra-Sharma, S., ... & Hubinger, E. (2025). Auditing language models for hidden objectives. _arXiv preprint arXiv:2503.10965_ . 

3. Fronsdal, K., Gupta, I., Sheshadri, A., Michala, J., McAleer, S., Wang, R., Price, S., & Bowman, S. (2025). _Petri: Parallel Exploration of Risky Interactions_ . https://github.com/meridianlabs-ai/inspect_petri 

4. Bereska, L., & Gavves, E. (2024). Mechanistic interpretability for AI safety--a review. _arXiv preprint arXiv:2404.14082._ 

## **Appendix** **_(optional)_** 







## **LLM Usage Statement** 

GPT-5.6 Sol was used to assist with the coding (model building, data visualizations, dashboards, etc.) and was used to generate the dataset in the project. GPT-5.6 Sol was also used to assist with writing the report in the methodology and some of the result section however the majority of the report was written by our team. All results, the dataset, and claims were verified by us. 

