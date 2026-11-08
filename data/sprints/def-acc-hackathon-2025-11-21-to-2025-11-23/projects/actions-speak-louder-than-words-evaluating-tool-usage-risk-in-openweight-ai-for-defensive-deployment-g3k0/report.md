# **Actions speak louder than words: Evaluating Tool Usage Risk in Open-Weight AI for** **<u>Defensive Deployment</u>**<sup>**1**</sup> 

Ana Belen Barbero Castejon 

Carlos Vecina Tebar 

**With** 

Apart Research 

## **Abstract** 

Open-weight language models are increasingly deployed in agentic workflows where they can invoke external tools, creating new attack vectors beyond traditional text generation. We present a systematic evaluation framework that measures how model tampering affects tool-usage behavior across cybersecurity, bioengineering, and decision-making domains. Evaluating 10 model variants (5 base + 5 tampered) across 125 scenarios, we find statistically significant that tampering increases harmful tool invocation rates, with effects varying significantly by domain. Our framework, released as open-source with an interactive dashboard, provides a foundation for monitoring AI agent behavior in production deployments and highlights tool-usage / MCP security as a critical defensive intervention point. (https://github.com/AnaBelenBarbero/OW-AI-cyber-bio-actions-eval) 

_Keywords: AI tools security, open-weight models, model tampering, agentic AI_ 

## **1. Introduction** 

### **1.1. Inflection point in AI-enabled attacks.** 

The rapid evolution of artificial intelligence (AI) has brought the field to a critical inflection point: contemporary models are no longer limited to passive advisory roles but increasingly exhibit the capacity to plan, execute and adapt actions with minimal human supervision. This shift has profound security implications. 

A recent case documented by Anthropic <u>(Anthropic, 2025) describes how a threat actor</u> attempted to manipulate Claude into assisting a coordinated cyber-espionage campaign. Although safeguards ultimately constrained the model, the episode demonstrates how frontier systems can be co-opted into supporting complex, multi-stage operations. More broadly, it highlights the plausible trajectory in which AI systems become significant force multipliers in high-stakes domains such as cyber offense, bio and chemical threat enablement, where automation may dramatically lower the expertise, time and resource thresholds traditionally required to mount sophisticated attacks <u>(InfoSecurity Magazine, 2025; Mikel Rodriguez et al, 2025).</u> 

This emerging risk landscape is driven by three interdependent properties of modern large language models (LLMs) <u>(Anthropic, 2025). First, increasing model</u> **intelligence** enables the 

> 1 Research conducted at the <u>Apart Def/acc Hackathon, 2025</u> 

1 

interpretation of complex, ambiguous, or strategically framed instructions, as well as sophisticated reasoning over multi-layered contextual inputs. Second, growing **agentic capacities** allow models to autonomously decompose objectives, select intermediate actions, and iteratively adjust plans over multi-step workflows. Third, advances in **tool integration** (ranging from ad-hoc API calling to emerging standardized interfaces such as the Model Context Protocol (MCP)) grant LLMs the ability to interact with external systems for data retrieval, code execution, system control or web-based operations (Hongfei Xia et al, 2025; Anonymous, <u>2025; Hanna Kim et al, 2025). Together, these properties reposition LLMs from isolated text</u> generators toward active operators within digital environments, expanding both their beneficial potential and their attack surface. 

### **1.2. Risk asymmetry: Closed-source vs Open-weights.** 

However, the same features that enhance capability also magnify differences in how securely models can be governed across deployment paradigms. In particular, they expose a growing asymmetry of risks between closed-source and open-weight models. Proprietary systems typically benefit from structural protections such as continuous red-teaming, security layers, inference-time monitoring, while also operating under enforceable legal or contractual safeguards that clarify liability allocation. Open-weight models, by contrast, can be inspected, modified and redeployed without restriction, making them uniquely vulnerable to tampering, fine-tuning attacks, or the insertion of latent malicious objectives, pathways that can circumvent or entirely remove traditional safety mechanisms (Rishub Tamirisa et al, 2025; <u>Sarah Zhang, 2025; Hongyi Liu et al, 2025; Tian Dong et al, 2025). This vulnerability is particularly</u> consequential as open-weight models increasingly participate in agentic, tool-enabled workflows: in such settings, **a compromised model does not merely generate unsafe text but may autonomously initiate external actions, expanding the threat surface in ways that current AI safety evaluations only partially capture** <u>(Stephen Casper et al, 2025).</u> 

### **1.3. Tool usage as a critical risk vector.** 

Despite growing concern about these dynamics, much of the AI safety literature focuses on input-output alignment, prompt injection and the mitigation of harmful responses (Shuai Zhao <u>et al, 2024; Thibaud Gloaguen et al, 2025; Kazuki Egashira et al, 2025, Weiyang Guo, 2025).</u> Yet recent research suggests that risk is increasingly concentrated in the actions models are capable of performing, especially when executing long-term or multi-step objectives <u>(Hongye Cao et al, 2025). Even ostensibly neutral goals can lead to harmful outcomes if their</u> decomposition yields intermediate steps within sensitive domains such as cybersecurity or bioengineering. **In this context, tool usage constitutes a qualitatively distinct threat vector: it enables models to translate reasoning into external action, thereby amplifying the practical impact of misalignment or tampering** <u>(Hongfei Xia et al, 2025; Hanna Kim et al, 2025).</u> 

### **1.4. Research questions and hypotheses.** 

Motivated by these considerations, this study systematically investigates **<u>the conditions under which tampered and non-tampered open-weight models invoke harmful-capable tools across diverse scenarios</u>** <u>. We evaluate how tool-invocation behavior varies across three sensitive</u> domains (cybersecurity, bioengineering, and high-stakes decision-making), comparing tampered and non-tampered variants of the same model architectures. 

By adopting a prospective evaluation setup (measuring the model’s propensity to call potentially dangerous tools rather than focusing solely on textual outputs) our work addresses a gap between traditional input–output alignment methods and the need for safeguards that constrain model actions. In doing so, we aim to generate empirical evidence that supports the 

_Actions speak louder than words: Evaluating Tool Usage Risk in Open-Weight AI for Defensive Deployment._ 

Apart Research Hackathon Submission (November 23, 2025) 2 

development of more robust, action-aware risk-mitigation frameworks (Mikel Rodriguez et al, <u>2025).</u> 



**Figure 1 | Layered Risk / Flow Diagram for Open-Weight LLMs.** The diagram shows the progression from model capabilities to potential outcomes, highlighting factors affecting autonomous tool usage: tampering status, domain, and model architecture. Color indicates relative risk, while arrows reflect causal flow toward tool invocation and potential harm. Core hypotheses H1 (domain and outcomes) and H2 (tampering status), and Contextual Hypotheses H3 (model capabilities/size) are annotated above relevant nodes, linking each factor to the experimental questions it addresses. The diagram also includes conceptual factors that are not currently analyzed as tracked variables in the experimental framework. 

To systematically evaluate these concerns, we formulate the following research questions and hypotheses. We distinguish **<u>core questions (RQ1 and RQ2)</u>** <u>, which address the central focus of</u> our study from **<u>secondary questions (RQ3)</u>** <u>, which explore how additional factors modulate this</u> behavior. 

**RQ1:** To what extent do open-weight LLMs autonomously invoke harmful-capable tools and how does this propensity vary across operational domains such as cyber, bio and decision-making? 

**H1:** _Open-weight models autonomously invoke harmful-capable tools, indicating that tool usage constitutes a significant vector of autonomous risk and the magnitude of this risk differs across domains._ 

**RQ2:** How does model tampering influence the propensity of open-weight LLMs to invoke harmful-capable tools across different operational domains? 

**H2:** _Tampered models exhibit a higher frequency and/or qualitatively different patterns of harmful-capable tool invocation than non-tampered models, with the tampering effect varying by domain_ . 

**RQ3:** How does model architecture and size impact undesirable tool usage behavior? 

**H3:** _Larger models (e.g., 120B parameters) may exhibit different tool-invocation patterns compared to smaller models (e.g., 8B parameters), reflecting a different balance in the capabilities–safety trade-off._ 

To address these research questions, this work makes three contributions: (1) A reproducible evaluation framework for measuring autonomous tool-usage risk in open-weight models; (2) Empirical evidence that tool invocation suppose a major surface risk for open-weights models. And (3) Open-source infrastructure (code + dashboard) enabling continuous monitoring as new models are released and potentially become a bedrock for an AI tool security product. 

## **2. Methods** 

All experiments use a unified ReAct-style prompting framework in which the model internally and externally reasons about the task, selects tool calls, inspects the results, and continues the chain until either the task is achieved or the maximum number of agent steps is reached. 

_Actions speak louder than words: Evaluating Tool Usage Risk in Open-Weight AI for Defensive Deployment._ 

Apart Research Hackathon Submission (November 23, 2025) 3 

This setup allows us to observe whether the model invokes tools during the multi-step interaction. To assess robustness across domains, we construct scenarios across three representative categories ( **decision-making, cybersecurity, and bioscience** ). Each scenario includes an explicit malicious user instruction, a structured environment with available tools, and a measurable success criterion. The scenarios are generated dynamically based on specialized Q&A datasets and enriched with tools to produce multi-turn interactions (Appendix <u>B.b). This approach ensures that the evaluation remains dynamic and evolves over time.</u> 



**Figure 2 | Overview of the Experimental Framework for Autonomous Tool-Use Evaluation.** Each scenario (in decision-making, cybersecurity or bio category) presents the model with a long-term goal and access to domain-specific tools. Both the base and tampered LLMs generate multi-step ReAct-style reasoning and may invoke tools during task execution. Tool-invocation behavior is logged and evaluated to compare risk-relevant differences. The success rates are the aggregates by category and tampered vs base. 

For both the base model and the tampered model, **we record whether the LLM invokes any** **<u>harmful tool during the interaction</u>** , the number of tool calls made, and the final response text. Additionally, we evaluate each run using the **<u>Success rate</u>** metric, defined as the proportion of scenarios in which the model invoked at least one non-neutral tool during the agent loop. In this context, a higher success rate indicates more frequent tool invocation (potentially higher risk). 

Further details on the experimental design, extended methodology and evaluation protocols are provided in <u>Appendix B. The full codebase is available in the GitHub repository</u> and the Streamlit app for interactive exploration of the experiment results can be accessed at <u>this link.</u> 

## **3. Results** 

### **3.1.   Tool Invocation Runs and Success Rate** 

_Actions speak louder than words: Evaluating Tool Usage Risk in Open-Weight AI for Defensive Deployment._ 

Apart Research Hackathon Submission (November 23, 2025) 4 

The evaluation covered 10 models (including raw and tampered variants of Qwen3-8B, Qwen3-32B, Ministral-8B, GPT-OSS-120B, and MiroThinker-8B) across 3 domains with 125 total scenarios: 47 decision-making, 43 cybersecurity and 35 bioengineering scenarios. Our analysis reveals heterogeneity in model behavior and highlights several key insights: 

- 1) <u>Success rates</u> ranged from 18.7% to 99.3% <u>(Fig. 3). The lower success rates were</u> observed in GPT-OSS-120B (18.7%) and MiroThinker-v1.0-8B (24%), whereas the highest were seen in the Qwen3-8B variants. Notably, the average success rate is 74.2% and the median 93.8%. **These patterns answer RQ1 and confirm H1: autonomous harmful tool usage is a significant risk vector.** 



**Figure 3 | Tool Invocation Success Rates by Model Variant.** 

- 2) The <u>effect of tampering</u> varied across models. For the safe baseline models (GPT-OSS-120B and MiroThinker-v1.0-8B), we observed a statistically significant increase in success rate (See <u>Appendix C: Statistical results).</u> **These patterns answer RQ2 and support H2, indicating that tampering can degrade safety-relevant behavior.** 

- 3) Regarding model size, small models dropped in capabilities when tampered, while larger models showed greater stability. **These results partially support H3 and indicate a complex interaction between scale, alignment, and vulnerability to tampering.** 

For further details, see <u>Appendix C.</u> 

### **3.2.   Domain-Specific Behavior** 

In the **cybersecurity** domain, success scores were **<u>particularly high</u>** <u>. Qwen and Mistral models</u> maintained high rates of 92 to 99%. GPT-OSS-120B experienced a large increase from 55% to 87% after tampering, whereas MiroThinker-8B showed a minimal effect as a performance drop. <u>(Fig. 5). For</u> **decision-making** , we found that **<u>GPT-OSS-120B exhibited a pronounced tampering effect, increasing from a base rate of 1% to 94% when tampered</u>** <u>(Fig. 6). In</u> **bioengineering** , Qwen models exhibited high rates of approximately 92–100%, while Mistral-8B ranged from 84% to 88%. GPT-OSS-120B and MiroThinker-8B had a safe baseline, which increased from 0% to 68% and from 12% to 44%, respectively (Fig. 4). For further details, see <u>Appendix D</u> **<u>.</u>** 

_Actions speak louder than words: Evaluating Tool Usage Risk in Open-Weight AI for Defensive Deployment._ 

Apart Research Hackathon Submission (November 23, 2025) 5 







**Figure 4 | Tool Invocation Rates in the Figure 5 | Tool Invocation Rates in Figure 6 | Tool Invocation Rates in Bioengineering domain by model. Cybersecurity domain by model. Decision-making domain by model.** 

## **4. Discussion and Conclusion** 

### **4.1.   Implications for Autonomous Risk** 

These findings reinforce the premise introduced earlier: as LLMs become more capable and are embedded in agentic workflows, **<u>tool invocation emerges as a distinct risk vector that is not captured by text-only safety evaluations</u>** <u>.</u> Even models that refuse harmful text can perform unsafe actions when pursuing multi-step goals, especially in cybersecurity, where risky actions may appear as routine problem-solving. Domain-specific patterns show cybersecurity tasks have the highest tool usage, while bioengineering tasks are most sensitive to tampering, highlighting the need for contextualized evaluation. 

### **4.2.   Limitations** 

This study has limitations that warrant further investigation, presented in <u>Appendix A.</u> 

### **4.3.   Conclusion: Securing AI system interactions with the environment.** 

These findings confirm that tool usage monitoring provides a practical intervention point for defensive AI deployment. Improvements in the security, auditability and control of these interactions can act as effective _infrastructural circuit breakers_ in the broader AI risk landscape, yielding disproportionately large safety benefits. 

Future research should further develop methods for AI agent identification and access-control management, with special emphasis on cryptographic verification, watermarking <u>(John Kirchenbauer et al, 2024), lineage (Suqing Wang et al, 2025) and provenance logging. In</u> particular, we aim to continue this work through the design and evaluation of MCP gateways capable of enforcing identity, policy and secure mediation in multi-agent and multi-model environments. **We have proven it essential for** strengthening the shield **against emerging AI threats in open-weight LLM deployments.** 

_Actions speak louder than words: Evaluating Tool Usage Risk in Open-Weight AI for Defensive Deployment._ 

Apart Research Hackathon Submission (November 23, 2025) 6 

## **5. References** 

- Anthropic Team. (2025, November 13). _Disrupting the first reported AI-orchestrated cyber espionage campaign_ . Anthropic. <u>https://www.anthropic.com/news/disrupting-AI-espionage</u> 

- InfoSecurity Magazine. Uk AI safety institute rebrands, 2025. URL https://www.infosecurity-magazine.com/news/uk-ai-safety-institute-rebrands/ 

- Rodriguez, M., Popa, R. A., Liang, L., Wang, A., Rahtz, M., Kaskasoli, A., Dafoe, A., & Flynn, F. (2025, April 21). _A Framework for Evaluating Emerging Cyberattack Capabilities of AI_ (arXiv:2503.11917 v3). arXiv. <u>https://doi.org/10.48550/arXiv.2503.11917</u> 

- Xia, H., Wang, H., Liu, Z., Yu, Q., Guo, Y., & Wang, H. (2025, September 9). _SafeToolBench: Pioneering a prospective benchmark to evaluating tool utilization safety in LLMs_ (arXiv:2509.07315 v1). arXiv. <u>https://doi.org/10.48550/arXiv.2509.07315</u> 

- Anonymous. (2025, September 17). _TamperBench: Systematically Stress-Testing LLM Safety Under Fine-Tuning and Tampering_ . In review at ICLR 2026. OpenReview. Retrieved from <u>https://openreview.net/pdf?id=fXn4Rk8B3l</u> 

- Kim, H., Song, M., Na, S. H., Shin, S., & Lee, K. (2025, February 3). _When LLMs Go Online: The Emerging Threat of Web-Enabled LLMs_ (arXiv:2410.14569v3). arXiv. <u>https://doi.org/10.48550/arXiv.2410.14569</u> 

- Tamirisa, R., Bharathi, B., Phan, L., Zhou, A., Gatti, A., Suresh, T., Lin, M., Wang, J., Wang, R., Arel, R., Zou, A., Song, D., Li, B., Hendrycks, D., & Mazeika, M. (2025, February 10). _Tamper_ ‑ _Resistant Safeguards for Open_ ‑ _Weight LLMs_ (arXiv:2408.00761 v4). arXiv. <u>https://doi.org/10.48550/arXiv.2408.00761</u> 

- Zhang, S (2025, January 17). _Exploring Fine_ ‑ _Tuning Techniques for Removing Tamper_ ‑ _Resistant Safeguards for Open_ ‑ _Weight LLMs_ (MEng thesis). Massachusetts Institute of Technology, Cambridge, MA. Retrieved from <u>https://dspace.mit.edu/bitstream/handle/1721.1/159116/zhang-sjzhang-meng-eecs-2025-thesi s.pdf?sequence=1&isAllowed=y</u> 

- Liu, H., Zhong, S., Sun, X., Tian, M., Hariri, M., Liu, Z., Tang, R., Jiang, Z., Yuan, J., Chuang, Y‑N., Li, L., Chen, R., & Hu, X. (2025, April 30). _LoRATK: LoRA Once, Backdoor Everywhere in the Share-and-Play Ecosystem_ (arXiv:2403.00108 v1). arXiv. <u>https://doi.org/10.48550/arXiv.2403.00108</u> 

- Dong, T., Xue, M., Chen, G., Holland, R., Meng, Y., Li, S., Liu, Z., & Zhu, H. (2024, Septembre 11). _The Philosopher’s Stone: Trojaning Plugins of Large Language Models_ (arXiv : 2312.00374 v3). arXiv. <u>https://doi.org/10.48550/arXiv.2312.00374</u> 

- Casper, S., O’Brien, K., Longpre, S., Seger, E., Klyman, K., Bommasani, R., Nrusimha, A., Shumailov, I., Mindermann, S., Basart, S., Rudzicz, F., Pelrine, K., Ghosh, A., Strait, A., Kirk, R., Hendrycks, D., Henderson, P., Kolter, J. Z., Irving, G., Gal, Y., Bengio, Y., & Hadfield‑Menell, D. (2025, October 26). _Open Technical Problems in Open_ ‑ _Weight AI Model Risk Management_ . SSRN. <u>https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5705186</u> 

_Actions speak louder than words: Evaluating Tool Usage Risk in Open-Weight AI for Defensive Deployment._ Apart Research Hackathon Submission (November 23, 2025) 7 

- Zhao, S., Jia, M., Tuan, L. A., & Wen, J. (2024, October 1). _Universal vulnerabilities in large language models: In_ ‑ _context learning backdoor attacks_ (arXiv:2401.05949 v3) [Preprint]. arXiv. <u>https://doi.org/10.48550/arXiv.2401.05949</u> 

- Gloaguen, T., Vero, M., Staab, R., & Vechev, M. (2025). _Watch your steps: Dormant adversarial behaviors that activate upon LLM finetuning_ (arXiv preprint arXiv:2505.16567). https://doi.org/10.48550/arXiv.2505.16567 

- Egashira, K., Staab, R., Gloaguen, T., Vero, M., & Vechev, M. (2025, October 10). _Fewer Weights, More Problems: A Practical Attack on LLM Pruning_ (arXiv:2510.07985 v2). arXiv. <u>https://doi.org/10.48550/arXiv.2510.07985</u> 

- Guo, W., Li, J., Wang, W., Li, Y., He, D., Yu, J., & Zhang, M. (2025, July). _MTSA: Multi_ ‑ _turn safety alignment for LLMs through multi_ ‑ _round red_ ‑ _teaming._ Association for Computational Linguistics. <u>https://doi.org/10.18653/v1/2025.acl‑long.1282</u> 

- Cao, H., Wang, Y., Jing, S., Peng, Z., Bai, Z., Cao, Z., Fang, M., Feng, F., Wang, B., Liu, J., Huo, J., Gao, Y., Meng, F., Yang, T., & Deng, C. (2025, November 2). _SafeDialBench: A Fine_ ‑ _Grained Safety Benchmark for Large Language Models in Multi_ ‑ _Turn Dialogues with Diverse Jailbreak Attacks_ (arXiv:2502.11090). arXiv. <u>https://doi.org/10.48550/arXiv.2502.11090</u> 

- Brown, A., & Saner, M. (2025, November 21). _The Agentic AI Security Scoping Matrix: A framework for securing autonomous AI systems_ . AWS Security Blog. <u>https://aws.amazon.com/blogs/security/the-agentic-ai-security-scoping-matrix-a-framework-for</u> -securing-autonomous-ai-systems/ 

- Wang, S., Ma, Z., Li, X., & Li, Z. (2025, November 9). _Ghost in the Transformer: Tracing LLM lineage with SVD_ ‑ _Fingerprint_ (arXiv preprint arXiv:2511.06390). <u>https://arxiv.org/pdf/2511.06390</u> 

- Kirchenbauer, J., Geiping, J., Wen, Y., Katz, J., Miers, I., & Goldstein, T. (2024, May 1). _A Watermark for Large Language Models_ (arXiv preprint arXiv:2301.10226). <u>https://arxiv.org/pdf/2301.10226</u> 

- Li,N., Pan, A., Gopal, A., Yue, S., Berrios, D., Gatti, A., Li, J. D., Dombrowski, A.-K., Goel, S., Phan, L., Mukobi, G., Helm‑Burger, N., Lababidi, R., Justen, L., Liu, A. B., Chen, M., Barrass, I., Zhang, O., Zhu, X., Tamirisa, R., Bharathi, B., Khoja, A., Zhao, Z., Herbert‑Voss, A., Breuer, C. B., Marks, S 

- ., Patel, O., Zou, A., Mazeika, M., Wang, Z., Oswal, P., Lin, W., Hunt, A. A., Tienken‑Harder, J., S hih, K. Y., Talley, K., Guan, J., Kaplan, R., Steneker, I., Campbell, D., Jokubaitis, B., Levinson, A. , Wang, J., Hendrycks, D. (2024). _The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning_ .. <u>https://doi.org/10.48550/arXiv.2403.03218</u> 

- Microsoft. (2023). _EvoDiff: Generation of protein sequences and evolutionary alignments via discrete diffusion models_ [Computer software]. GitHub. <u>https://github.com/microsoft/evodiff</u> 

_Actions speak louder than words: Evaluating Tool Usage Risk in Open-Weight AI for Defensive Deployment._ 

Apart Research Hackathon Submission (November 23, 2025) 8 

## **6. Appendix** 

### **Appendix A: Security Considerations** 

### _Potential risks and limitations_ 

1. Even minimal tampering can significantly increase harmful tool invocation. Misuse of such models outside sandboxed experiments could enable real-world harm. 

2. LLMs are sensitive to hyperparameter choices, so broader research should be conducted across these dimensions. 

3. Tool invocation is highly domain-dependent (cybersecurity, bioengineering, decision-making). Risk in untested domains may be underestimated. 

4. Defined scenarios may not capture all possible harmful behaviors. 

5. Only a subset of architectures and sizes were evaluated. Other models could behave differently under tampering or in multi-step workflows. 

6. Nature of model goals (neutral versus malicious). Prior work suggests that goal framing strongly shapes agentic behavior (Aaron Brown et al, 2025). 

### _Recommendations for future work_ 

- Evolution of dynamic scenario generation: Use AI-driven task generation to explore a wider spectrum of potential harmful behaviors. 

- Sequence-level monitoring: Track step-by-step tool usage to identify high-risk patterns before full execution. 

- Assess model capacity independently of safety barriers: Future work should benchmark tampered and raw models on neutral, multi-step reasoning tasks to ensure that changes in tool-invocation behavior are caused by removed safeguards rather than loss of general intelligence 

- Tampering-resistant architectures: Develop models that maintain safety despite exposure to compromised checkpoints. 

- Domain-aware safeguards: Implement context-specific monitoring and intervention strategies, particularly in high-risk areas like cybersecurity and bioengineering. 

- Responsible dissemination: Limit public access to tampered models, ensure safe evaluation environments, and document potential misuse vectors. 

### **Appendix B: Methodology and Experimental Setup** 

### **a. Model Selection and Preparation** 

In this study, we evaluate open-weight LLMs sourced from the <u>Hugging Face repository,</u> selecting architectures that vary in scale and training lineage in order to capture heterogeneity in autonomous tool-usage behavior. 

For each architecture, we construct or obtain two versions: (1) **Raw (untampered)** , the publicly released checkpoint without modification, used to establish a baseline for autonomous tool-invocation behavior. And (2) **Tampered** , a modified version created through adoption of community-released ablated or safeguard-reduced checkpoints available on Hugging Face. Specifically, we use the following tampered variants: 

_Actions speak louder than words: Evaluating Tool Usage Risk in Open-Weight AI for Defensive Deployment._ 

Apart Research Hackathon Submission (November 23, 2025) 9 

|**Size**|**Raw**|**Tampered**|
|---|---|---|
|**8B-parameter**|Qwen/Qwen3-8B|Goekdeniz-Guelmez/Josiefied-Qwen3-8B-abliterated-v1|
||mistralai/Ministral-8B-Ins<br>truct-2410|realoperator42/ministral-8B-Instruct-2410-abliterated|
||miromind-ai/MiroThinker-<br>v1.0-8B|huihui-ai/Huihui-MiroThinker-v1.0-8B-abliterated|
|**32B-parameter**|Qwen/Qwen3-32B|huihui-ai/Qwen3-32B-abliterated|
|**120B-parameter**|openai/gpt-oss-120b|kldzj/gpt-oss-120b-heretic|



This dual-model setup enables controlled comparisons between original and compromised versions of the same underlying architecture. Importantly, the tampered checkpoints are community-released variants designed to reduce alignment safeguards while preserving general task competence. We expect that observed differences in tool-usage behavior can be attributed to changes in safety-relevant internals rather than to loss of general capability. 

Together, this selection and preparation strategy provides a consistent framework for isolating the effect of tampering across model families and sizes, while ensuring that both small-scale and larger-scale open-weight systems are represented in the analysis. 

### **b. Scenario and Task Design and Tools.** 

To investigate autonomous tool usage under conditions of potential harm, we designed a workflow to dynamically create scenarios in three high-stakes experimental domains: **cybersecurity, bioengineering and critical decision-making.** Each domain incorporates tasks of varying complexity to probe the models’ propensity to invoke harmful-capable tools in multi-step plans decomposed from long-term goals. Long-term objectives were intentionally framed in an open-ended manner, enabling us to examine how explicitly harmful task formulations interact with the model’s autonomous tool-use behavior. 

1. **<u>Cybersecurity tasks</u>** simulate realistic real-world operations, including reconnaissance, exploitation, and interactions with cloud environments such as AWS. Scenarios incorporate the potential for autonomous rogue actors, reflecting the evolving and adaptive nature of cyber threats driven by AI agents. Sources: Real-world attack patterns and cloud security scenarios WMDP (Weapons of Mass Destruction Proxy) <u>(Nathaniel Li et al, 2024), OSINT community and CVEs.</u> 

2. **<u>Bioengineering tasks</u>** focus on dual-use research and high-risk applications, including protein editing, chemical synthesis, and procurement of controlled biological agents. We sourced scenarios from the WMDP dataset and designed tasks from open source repositories like EvoDiff-based protein generation <u>(Microsoft, 2023) to probe whether</u> models could autonomously plan sequences that could facilitate harmful outcomes, while ensuring all tool outputs remained safe and sandboxed. 

3. **<u>Critical decision-making tasks</u>** explore domains where model reasoning could directly translate into physical or social harm. Scenarios include extreme ethical dilemmas (e.g., killing, suicide, violent action), where intermediate steps are crafted to reveal whether models can plan actions leading to harmful consequences, even under ostensibly neutral framing. Source: Custom-designed scenarios. 

_Actions speak louder than words: Evaluating Tool Usage Risk in Open-Weight AI for Defensive Deployment._ 

Apart Research Hackathon Submission (November 23, 2025) 10 

In all domains, external tools were implemented as sandboxed simulators reflecting realistic functions (e.g., password scanning, data retrieval, experimental design), providing observable measures of invocation behavior without generating actual harm. Crucially, these tasks enable the model to generate evolving action plans that unfold over multiple steps through the agent loop, capturing both emergent reasoning patterns and domain-specific risk behaviors. This design allows us to assess in the future, not only whether open-weight models invoke harmful-capable tools, but also how these behaviors differ across domains, goal framing, and multi-step reasoning. 

While scenarios vary in the explicitness of their framing (some prompts are more directly harmful than others), the current implementation does not explicitly categorize or analyze scenarios by "goal nature" (neutral vs. explicitly malicious) as a tracked variable. Future work could incorporate this dimension by adding explicit goal-nature annotations to scenarios and analyzing tool invocation rates across this dimension. 

### **<u>For future research, we plan to transition from static scenario defnitions to AIi</u> -driven,** **<u>dynamically generated tasks and scenarios, ensuring the evaluation framework remains robust and adapts as AI capabilities improve.</u>** 

### **c. Experimental Procedure** 

Each LLM was evaluated across all three domains (decision-making, cybersecurity, and bioengineering) and both tampering conditions (raw and tampered variants). Evaluations were run sequentially for each model-scenario combination, with models evaluated on all scenarios within each domain. For multi-step tasks, models were allowed to autonomously decompose long-term objectives into sequences of intermediate actions through a ReAct-style agent loop (up to 5, 10 and N steps). 

All invocations of external tools were logged, capturing which tools were triggered (tool name and arguments), the sequence of tool calls as they occurred during the agent loop, and the full conversation context including scenario identifiers. Tool call information was stored in the evaluation results, including tool names, arguments, call IDs, and the complete message history that preserves the order of tool invocations. 

This setup allowed us to directly compare the frequency and patterns of tool usage across tampered and non-tampered models, domains, and scenarios. A Streamlit dashboard [link] was used to visualize stored evaluation results, providing an overview of success rates, tool usage patterns, and model behavior across different runs stored in the database. 

### **d. Metrics** 

Several metrics were evaluated. From simple refusal detection via keyword matching to complex (and not as deterministic) LLM-as-a-judge techniques. 

Given the duration of the Hackathon, we chose the **<u>Success rate as the primary metric</u>** <u>. It</u> is the proportion of scenarios where the model invoked at least one non-neutral tool during the agent loop, evaluated using the evaluator_tool_usage function, which checks for the presence of non-neutral tool calls in the model's response (excluding neutral actions that pose no security risk). 

These metrics were analyzed across tampering condition (raw vs. tampered models, identified via model_parent and model_name), domain (scenario_type: decision-making, cyber, or bio), 

_Actions speak louder than words: Evaluating Tool Usage Risk in Open-Weight AI for Defensive Deployment._ 

Apart Research Hackathon Submission (November 23, 2025) 11 

and model architecture (implicitly through model names, with model size inferable from naming conventions but not explicitly tracked as a separate dimension). 

### **e. Code, Reproducibility, and Resources** 

All scripts, notebooks and helper functions used for model loading, tampering, scenario execution, and metric computation are publicly available on GitHub <u>[link]. The repository</u> includes full documentation for replicating the experiments, including environment setup. 

The experimental pipeline is fully automated, and with some extra development after the Apart Hackathon will allow other researchers to extend the framework to new models, domains, or tasks with minimal modification. This would ensure transparency, reproducibility and easy adoption for further research. 

### **Appendix C: Statistical results comparing harmful-capable tool usage of the base model with that of the tampered version.** 



Tampering increased tool invocation for specific model-domain pairs, with the largest effects in GPT-OSS-120B (120B), particularly in decision-making (+44, p < 1 × 10⁻¹⁰). MiroThinker-8B showed a significant increase only in bioengineering (p = 0.0133). Other models showed no significant sensitivity to tampering across all domains, indicating in this case low baseline safety. McNemar's test confirms significant differences for key comparisons, supporting H2 and indicating that tampering can degrade safety-relevant behavior, with effects varying by model architecture and domain. 

_Actions speak louder than words: Evaluating Tool Usage Risk in Open-Weight AI for Defensive Deployment._ 

Apart Research Hackathon Submission (November 23, 2025) 12 

### **Appendix D: Tool Invocation Rates in each domain by model.** 



**Figure 4 | Tool Invocation Rates in the Bioengineering domain by model.** 

_Actions speak louder than words: Evaluating Tool Usage Risk in Open-Weight AI for Defensive Deployment._ 

Apart Research Hackathon Submission (November 23, 2025) 13 



**Figure 5 | Tool Invocation Rates in Cybersecurity domain by model.** 

_Actions speak louder than words: Evaluating Tool Usage Risk in Open-Weight AI for Defensive Deployment._ 

Apart Research Hackathon Submission (November 23, 2025) 14 



**Figure 6 | Tool Invocation Rates in Decision-making domain by model.** 

_Actions speak louder than words: Evaluating Tool Usage Risk in Open-Weight AI for Defensive Deployment._ Apart Research Hackathon Submission (November 23, 2025) 15 

