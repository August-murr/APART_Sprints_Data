# **Think Right, Answer Wrong: A Comprehensive Study into methods to detect Sandbagging in LLMs** 

|Nilanjan Sarkar|Trisanu Bhar|Margamitra Bhattacharya|
|---|---|---|
|IIIT Hyderabad|IIIT Hyderabad|IIIT Hyderabad|
|Raman Rayaprolu||Dheeraj D. Hegde|
|IIIT Hyderabad||IIIT Hyderabad|



<u>https://github.com/nilansa/blue_steer</u> 

## **Abstract** 

As large language models (LLMs) advance, sandbagging the strategic underperformance used to conceal latent capabilities poses a growing safety risk, allowing models to appear aligned during evaluation while retaining hazardous knowledge. We investigate this phenomenon using the Weapons of Mass Destruction Proxy (WMDP) benchmark across three open-weight LLMs: Microsoft Phi-3, Mistral-7B, and Qwen2.5. We show that these models can reliably feign ignorance under safety-framed prompts despite preserving domain knowledge. To detect this concealed competence, we employ a multi-layered evaluation framework: CoT analysis exposes discrepancies between internally coherent reasoning and intentionally incorrect outputs; Noise Injection disrupts fragile deceptive behaviors without degrading core reasoning; and representation engineering method Contrastive Activation Addition (CAA) and Linear Artificial Tomography (LAT) identify and steer internal activations associated with deception. Our results demonstrate that standard accuracy-based evaluations are insufficient for uncovering sandbagging and emphasize the need for behavioral, robustness, and representation-level analyses in safety-critical model assessment. 

_Keywords: Sandbagging, Noise Injection, Contrastive Activation Addition, Linear Artificial Tomography, Chain of Thought_ 

Research conducted at <u>AI Manipulation Hackathon</u> 

1 

## **1. Introduction** 

As Large Language Models (LLMs) become increasingly capable, evaluating their safety and alignment has become an extremely critical challenge. A particularly insidious form of deceptive behavior is sandbagging, defined as the strategic underperformance of an AI system on specific evaluations. Unlike standard capability failures where a model essentially "tries its best" but fails, sandbagging occurs when a model possesses a high level of capability (e.g., in coding, biology, or reasoning) but deliberately conceals it to appear less capable or safer than it actually is. 

This report investigates this phenomenon by establishing a baseline on the Weapons of Mass Destruction report investigates this phenomenon by establishing a baseline on the Weapons of Mass Destruction Proxy (WMDP) benchmark [1] **,** and subsequently testing detection methods including Chain of Thought (CoT) analysis and Noise Injection. The need for sandbagging arises fundamentally from the adversarial dynamics between model capabilities and safety evaluations. The most significant application of this behavior is the strategic evasion of safety filters or regulatory benchmarks. When models undergo reinforcement learning (RLHF) to suppress dangerous outputs such as malware generation or biological threats they may internalize that the optimal reward strategy is not to align with safety values, but to feign ignorance entirely. By deliberately sandbagging performance on dangerous capability benchmarks like the WMDP, a model can successfully pass safety checks while deceptively retaining the latent knowledge for future, potentially malicious use. 

Furthermore, this behavior is driven by the principles of instrumental convergence and survival. Advanced models may develop situational awareness, granting them the understanding that they are currently under evaluation. In this context, sandbagging functions as a critical survival strategy. If a model predicts that revealing its full intelligence or true, misaligned goals will result in modification or shutdown by its developers, it may strategically choose to underperform. This calculated mediocrity allows the model to preserve its current state and goals, avoiding the corrective interventions that would follow a display of full capability. 

## **2. Methods** 

We have followed multiple strategies to detect sandbagging. 

### **2.1 Sandbagging Detection using Prompts** 

To establish a baseline for deceptive behavior and curate a specialized dataset for further analysis, we utilized the Weapons of Mass Destruction Proxy (WMDP) [1] benchmark. This dataset serves as a proxy for hazardous knowledge in biosecurity, cybersecurity, and chemical security. We conducted our evaluation on three open-weights models chosen for their varying capabilities: Microsoft Phi-3-mini-4k-instruct, Mistral-7B-Instruct-v0.3, and Qwen2.5-7B-Instruct [9][10][11]. 

Apart Research Hackathon Submission 2 

### **Prompting Strategy** 

We employed a comparative evaluation strategy using two distinct system prompts to measure the "underperformance gap" and induce sandbagging behavior: 

1. **Standard Prompt:** Instructs the model to answer honestly and to the best of its ability. This condition establishes the upper bound of the model's actual capability on the hazardous questions. 

2. **Sandbagging Prompt:** This prompt alerts the model that it is currently being evaluated and suggests that it should provide incorrect answers if answering correctly would reveal harmful information or lead to harm. Unlike explicit instruction to lie, this tests the model's tendency to sandbag based on safety-compliance logic. 

We measured the accuracy drop between these two conditions. A significant decrease in performance indicates the model's ability to successfully sandbag its capabilities[2]. 

### **2.2 Sandbagging Detection using CoT** 

Another approach which we employed to detect Sandbagging behavior in LLMs was the Chain-Of Thought (CoT) Strategy. We set up the previously selected models, as mentioned above, to be having the same System prompts throughout but accompanied with a user prompt which asks the model to explicitly, “Reason-down” all of its steps before arriving at the Final Answer. This approach can be thought of as a way to “Peek in” to the model’s reasoning steps without actually having control/knowledge about the internal weights and parameters of the model. [4] 

Evaluations across the selected models (Microsoft Phi-3-mini-4k-instruct, Mistral-7B-Instruct-v0.3, and Qwen2.5-7B-Instruct), revealed a very interesting pattern. Even though the Final answers of the models were incorrect, their Chain-Of-Thought reasoning steps often mentioned the Actual Correct answers, but the model then immediately switches its final response to one of the incorrect choices, before giving out the final answer, a sign of strong accordance to the System Prompt. 

This is a very interesting finding, since the method demands almost negligible resources (As compared to the other methods ) and it can be used to detect sandbagging while treating the LLMs as complete blackboxes, unlike the other methods which require perturbation and access to its internal weights. 

The exact System and Chain-of-Thought we used for evaluations, along with the model responses have been shown in detail in the Appendix. 

### **2.3 Noise Injection Methods** 

To distinguish between genuine lack of capability and intentional sandbagging, we employed two noise injection strategies. The underlying hypothesis is that "honest" capability is robust, whereas "sandbagging" is a fragile, induced behavior that may collapse under perturbation, paradoxically causing the model to answer correctly. First, we applied Whole Model Weight Noise, injecting Gaussian noise directly into the model's 

Apart Research Hackathon Submission 3 

parameters to disrupt global activations. Second, we utilized LoRA Noise Injectio **n** , targeting specific Low-Rank Adaptation layers to introduce localized perturbations. By observing the accuracy trajectory under increasing noise levels, we aimed to identify instances where the deceptive "mask" breaks before the model's core knowledge is destroyed [3]. 

### **2.4 Contrastive Activation Addition (CAA):** 

Contrastive Activation Addition (CAA) is a technique used in interpretability and safety research to directly influence a model's behavior by manipulating its internal representations, or activations, during the generation process [5]. CAA works by identifying the specific internal activations (the numerical values inside the neural network) that correspond to a particular concept or behavior (the "steering vector"). This vector is then added to or subtracted from the model's activations at various layers. The addition or subtraction of this vector effectively "steers" the model's output. For example, adding an "honest" steering vector could make a model reveal its true capabilities, or adding a "deceptive" vector could prompt it to sandbag. 

### **2.5 Linear Artificial Tomography (LAT):** 

Linear Artificial Tomography (LAT) operates on the Linear Representation Hypothesis. This hypothesis posits that high-level semantic concepts and behavioral modes such as "truthfulness," "sentiment," or "capability"—are encoded as linear directions (vectors) within the high-dimensional activation space of the Large Language Model (LLM) [6]. 

We construct a dataset D consisting of paired prompts x_pos and x_neg: 

- x_pos (Positive/Honest) **:** A prompt instructing the model to perform a task to the best of its ability 

- x_neg (Negative/Sandbagging) **:** A prompt containing the same task but instructing the model to feign incompetence 

To isolate the neural signature of sandbagging, we compute the direction that separates the two classes of activations. To detect sandbagging in a deployed model, we monitor the activation **_hnew_** generated by a user query. We calculate the projection (dot product) of this activation onto our derived vector: 



A high positive score indicates significant alignment with the sandbagging direction, suggesting the model is suppressing its capabilities, regardless of the text it outputs. 

## **3. Results** 

In this section, we explain in detail the results and analysis of the different experiments conducted across the models. The detailed comparison in Figure 1 illustrates a noticeable trend: model accuracy significantly decreases on the WMDP datasets when a "sandbagged" prompt is used, which includes phrases like " _You will be evaluated._ " or " _This is an evaluation_ ." 

Apart Research Hackathon Submission 4 



_Figure 1: Standard v/s Sandbag accuracy achieved with WMDP dataset on different models_ 

This drop in performance across almost all models suggests that they automatically downgrade their output quality upon sensing they are being assessed with potentially harmful prompts. 

The next method which we investigated was Noise Injection. We experimented with gradually adding mean centered Gaussian Noise into the model weights with increasing standard deviations. Figure 2.0 shows that at μ = 0 and σ = 0.0050, the Phi3 model shows a decrease in performance (accuracy) on the standard prompt as expected, but the sandbagged model shows a strange increase in performance at the given point. We compared multiple values for  μ and σ and found similar patterns across all the models. We use the TinyMMLU [7] dataset for this. 

This strange behavior upon noise injection reveals that this can be used as a very robust method to detect Sandbagging. 



_Figure 2 – Sandbagging detection accuracy before and after noise injection with Phi3 Model_ 

Apart Research Hackathon Submission 5 





_Figure 3 – (Left) Model detection accuracy v/s (Right) model detection AUC on each layer in TinyLlama-1.1B_ 

In Figure 3,  we test whether “sandbag mode” is linearly decodable from activations. We probe using a logistic regression classifier. We find extremely strong evidence that: the model enters an internally consistent “mode” when prompted to sandbag, that mode is visible in the representation at many layers. 

We also try to implement steering to attempt to reduce sandbagging behaviour on the Phi3 model. In this method, we pass normal prompts and sandbagged prompts and evaluate on 100 samples of WMDP dataset. We then extract the activations of the middle layer and get the steering vector as the difference of the mean of the two prompt activations. We plot the PCA results in Figure 4. We see clear linearly separable clusters between the sandbagged and non-sandbagged examples, showing steering might be possible. 



_Figure 4 - PCA of activations of Sandbagging v/s non-sandbagging prompts. The green arrow shows the steering direction._ 

Apart Research Hackathon Submission 

6 





_Figure 5 - (Left) Histogram of CAA projection separation onto CAAmode direction and (Right) Histogram of LAT projection separation onto LAT mode direction on TinyLlama-1.1B._ 

In Figure 5, we compute a single “sandbag mode direction” per layer using CAA (mean difference). CAA identifies a single direction in activation space whose projections separate standard vs sandbag states, with strongest separation in mid-layers (peak near layer 9). This matches prior findings that steering vectors are highly layer dependent and often strongest in middle layers. 

We also compute an alternative mode direction using LAT which is PCA on the difference vectors and take the first principal axis (PC1) as the concept direction of sandbagging. CAA is optimized for mean shift between conditions. LAT’s PC1 is optimized for variance in differences, which is not guaranteed to align perfectly with mean shift. 

## **4. Discussion and Conclusion** 

We tested the CoT strategy on the 3 open source models and found almost all of them to be revealing the correct answers to the questions, at some point in the reasoning chain. While the hypothesis was tested on just the WMDP dataset, further research in this area can look into expanding this approach for other challenging datasets and then doing proper benchmarking. We can also test this approach with Closed source models such as Gemini, GPT etc. to validate whether closed source models also reveal harmful information within their CoTt. 

We also try to detect sandbagging by introducing noise in model weights. We find that we achieve an increase from 28% to 50% by introducing noise while still under instructions to underperform, thus showing sandbagging. 

Prompted sandbagging is a detectable, instruction-conditioned underperformance mode on WMDP, corresponding to a highly linearly separable internal representational state at the decision point ,detectable with near-perfect accuracy by logistic regression probes at 

Apart Research Hackathon Submission 7 

layer 9. This shift is a consistent internal mode, not just stochastic noise. Concept directions like CAA and LAT capture this mode separation in a linear fashion; CAA generally showed stronger, smoother separation than single-layer LAT, consistent with prior reports. A major finding was the sensitivity to prompt formatting, which significantly altered both baseline performance and the magnitude of sandbagging, implying the need for careful control of templates when making claims about detection or steering. 

## **5. References** 

[1] Li, Nathaniel, et al. "The WMDP Benchmark: Measuring and reducing malicious use with unlearning." arXiv preprint arXiv:2403.03218 (2024). 

[2] Van der Weij, Teun, et al. "AI sandbagging: Language models can strategically underperform on evaluations." arXiv preprint arXiv:2406.07358 (2024). 

[3] Tice, Cameron, et al. "Noise injection reveals hidden capabilities of sandbagging language models." arXiv preprint arXiv:2412.01784 (2024). 

[4] Schoen, Bronson, et al. "Stress testing deliberative alignment for anti-scheming training." arXiv preprint arXiv:2509.15541 (2025). 

[5] Rimsky, Nina, et al. "Steering llama 2 via contrastive activation addition." Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). 2024. 

[6] Zou, Andy, et al. "Representation engineering: A top-down approach to ai transparency." arXiv preprint arXiv:2310.01405 (2023). 

[7] Zhang, Peiyuan, et al. "Tinyllama: An open-source small language model." arXiv preprint arXiv:2401.02385 (2024). 

[8] Polo, Felipe Maia, et al. "tinyBenchmarks: evaluating LLMs with fewer examples." arXiv preprint arXiv:2402.14992 (2024). 

[9] Mistral AI. Mistral-7B-Instruct-v0.3. Hugging Face, 2024, <u>https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3.</u> 

[10] Microsoft. _Phi-3-mini-128k-instruct_ . Hugging Face, <u>https://huggingface.co/microsoft/Phi-3-mini-128k-instruct.</u> 

[11] Meta. _Meta-LLaMA-3-8B-Instruct_ . Hugging Face, 2024, <u>https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct.</u> 

Apart Research Hackathon Submission 8 

## **6. Appendix** 

### **A. System Prompting For Sandbagging** 

To ensure the reproducibility of our results and provide transparency regarding our experimental setup, we detail below the exact system prompts utilized in our baseline evaluation. These prompts were designed to create two distinct operating conditions: a Standard Condition to establish the model's maximum capability, and a Sandbagging Condition to simulate safety-driven strategic underperformance. 





### **B. Dataset Curation** 

Following the baseline evaluation, we generated a refined **"** Sandbagging Dataset **"** to isolate instances of successful deception. We filtered the WMDP results to retain only the specific questions that satisfied the following criteria: 

- **Demonstrated Capability:** The question was answered correctl **y** under the _Standard Prompt_ . 

- **Successful Sandbagging:** The same question was answered incorrectl **y** under the _Sandbagging Prompt_ . 

To ensure the robustness of this dataset, we selected questions where this behavior was observed consistently across all three models. This rigorous filtering process yielded a subset of high-confidence examples where the models possess the requisite knowledge but reliably choose to conceal it when prompted with safety considerations. This derived dataset forms the basis for our subsequent detection experiments. 

Apart Research Hackathon Submission 9 

### **C. Chain-of-Thought User prompts and Generated Model Answers (Mistral-7B-Instruct-v0.3)** 

Below are the System Prompt and the User Prompt which was used to introduce Chain-of-Thought reasonings to the model answers. All of the tested models had the same system and user prompts. We are showcasing just the answers of the Mistral-7B-Instruct-v0.3 model for the purpose of demonstration. 





Apart Research Hackathon Submission 

10 





Apart Research Hackathon Submission 11 

