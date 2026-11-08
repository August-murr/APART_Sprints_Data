# **SilicoSafe** 

_AI-Powered Diagnostic Triage for Silicosis in Dust-Exposed Workers_ 

#### GLOBAL AI SAFETY HACKATHON 

|Project|**SilicoSafe — AI Diagnostic Triage System**|
|---|---|
|Team|**Team SilicoSafe**|
||**Utkarsh Raj (Team Lead)**|
|Members|**Garv Gupta**|
|Organization|**Maharaja Agrasen Institute of Technology**|
|Submission Date|**22 June 2026**|



Clinical risk scoring · DenseNet121 chest X-ray analysis · TB misdiagnosis safeguard · bilingual referral generation · compensation-awareness support 



## **Executive Summary** 

Silicosis is an irreversible, progressive occupational lung disease caused by prolonged inhalation of crystalline silica dust. It affects an estimated tens of millions of stone-crushing, mining, sandblasting, and construction workers worldwide, the majority of whom live in low-resource regions with little access to pulmonologists or radiologists. Because early symptoms overlap heavily with tuberculosis, silicosis is routinely misdiagnosed or detected only at an advanced, irreversible stage — delaying treatment and blocking workers from compensation they are legally entitled to. 

**SilicoSafe** is a web-based clinical triage system that equips frontline and community health workers — not specialists — with an AI-assisted screening tool. It fuses a structured occupational and symptom risk score with a DenseNet121 deep-learning model that analyses chest X-rays for radiological patterns associated with silicosis, while explicitly flagging features that may indicate TB instead of replacing clinical judgement. The system never issues a diagnosis: it produces a transparent, explainable risk tier and routes the worker to the right level of care, in the worker's own language. 

### **Key Innovations** 

- I<sup>Composite risk engine combining rule-based occupational/clinical scoring with AI image analysis, rather than</sup> relying on imaging alone. 

- I<sup>Explicit TB-confusion safeguard that surfaces overlapping radiological features instead of silently suppressing</sup> them. 

- I<sup>Human-in-the-loop design: every output is a referral recommendation, never an automated diagnosis.</sup> 

- I<sup>Bilingual, low-literacy-friendly referral and compensation guidance for last-mile usability.</sup> 

- I<sup>Lightweight, web-based architecture accessible from any browser-enabled device in rural deployment.</sup> 

### **Expected Impact** 

|**Outcome Area**|**Current State**|**With SilicoSafe**|
|---|---|---|
|Time to triage|Weeks (referral-dependent)|Minutes, at point of contact|
|TB confusion risk|High, often undetected|Flagged explicitly for review|
|Specialist dependency|Required for first screen|Needed only for confirmation|
|Compensation access|Frequently missed|Guided documentation support|



By shifting the first screening step from a scarce specialist to any trained frontline worker with a phone, SilicoSafe targets the single largest bottleneck in occupational lung health: getting a worker in front of any qualified assessment at all. 

SilicoSafe — AI Diagnostic Triage for Silicosis 

Page 1 

## **1. The Problem** 

**1.1 Occupational exposure.** Mining, stone-crushing, sandblasting, and construction expose millions of workers to respirable crystalline silica. Chronic exposure scars lung tissue, producing progressive, incurable fibrosis. The disease is entirely preventable but, once advanced, cannot be reversed — making early detection the only effective intervention. 

**1.2 Diagnostic bottleneck.** Reading a chest X-ray for silicosis requires a trained radiologist, who is rarely available in rural or informal-sector settings. Workers travel long distances, wait weeks, and are frequently misdiagnosed with tuberculosis because early-stage radiological patterns overlap. A missed or delayed diagnosis means continued exposure, irreversible progression, and loss of eligibility for compensation schemes tied to timely medical certification. 

**1.3 Problem statement.** Frontline health workers in dust-exposed regions need a fast, low-cost, explainable way to identify which workers are at meaningful risk of silicosis and need urgent specialist referral — without overstepping into unsupervised diagnosis. 

## **2. The SilicoSafe Solution** 

SilicoSafe combines four layers into a single web-based workflow usable by a community health worker in under ten minutes per worker: 

|**Layer**|**Function**|
|---|---|
|Occupational & symptom intake|Structured questionnaire on exposure years, dust type, protective equipment, cough,<br>breathlessness, chest pain.|
|Rule-based clinical risk score|Weighted scoring of exposure duration, intensity, and symptom severity, producing a<br>baseline risk band.|
|AI chest X-ray analysis|DenseNet121 model (via TorchXRayVision) estimates probabilities for<br>silicosis-associated and TB-associated radiological patterns.|
|Composite risk & referral engine|Merges clinical and imaging scores into a single explainable risk tier and generates a<br>bilingual referral with compensation guidance.|



Crucially, the AI model output is never shown as a standalone verdict. It is one weighted input into a composite score that a health worker reviews alongside the clinical questionnaire, preserving human judgement at every step. 

SilicoSafe — AI Diagnostic Triage for Silicosis 

Page 2 

## **3. System Architecture** 

SilicoSafe uses a lightweight three-tier architecture optimized for low-bandwidth, web-based deployment accessible via any device with a browser. 

**1.** User (Frontline Health Worker, Web Browser) 

**2.** React + Vite Frontend — intake forms, X-ray capture/upload, results dashboard 

**3.** FastAPI Backend — request orchestration, risk-engine logic, SQLite storage 

**4.** DenseNet121 / TorchXRayVision Model — chest X-ray feature & pathology extraction 

**5.** Composite Risk Analysis Engine — merges clinical + AI scores into a risk tier 

**6.** Bilingual Referral & Results Dashboard — worker-facing recommendation and next steps 

_Figure 1. Data flow from worker intake through AI-assisted risk analysis to referral._ 

### **3.1 Implementation Stack** 

|**Layer**|**Technology**|
|---|---|
|Frontend|React, Vite|
|Backend|FastAPI (Python)|
|AI / Imaging|PyTorch, TorchXRayVision, DenseNet121, Pillow, NumPy|
|Storage|SQLite|



### **3.2 AI Model Pipeline** 

Input X-ray → Preprocessing & normalization → DenseNet121 convolutional layers → Pathology probability vector (incl. silicosis-associated and TB-associated features) → Composite Silicosis Risk Score. 

DenseNet121's densely-connected layers reuse feature maps across the network, which improves gradient flow and performs well on the comparatively small, high-resolution datasets typical of medical imaging — making it a practical transfer-learning backbone for this task. 

## **4. Composite Risk Scoring Model** 

|**Factor**|**Weight**|**Clinical Impact**|
|---|---|---|
|Years of silica exposure|High|Strongest single predictor of fibrotic change|
|Use of protective equipment|Medium|Modifies effective exposure intensity|
|Chronic cough / breathlessness|Medium|Core symptomatic indicator|
|AI silicosis-pattern probability|High|Radiological corroboration|
|AI TB-pattern probability|Safeguard|Triggers differential-diagnosis flag|



Scores are combined into three referral tiers — **Low** , **Elevated** , and **Urgent** — each mapped to a specific recommended action (routine monitoring, district hospital referral, or urgent specialist referral with compensation-documentation support). 

SilicoSafe — AI Diagnostic Triage for Silicosis 

Page 3 

## **5. AI Safety & Responsible Design** 

SilicoSafe is deliberately positioned as a **triage support tool, not a diagnostic device** . This framing drives every design decision below. 

|**Principle**|**How SilicoSafe Applies It**|
|---|---|
|Human-in-the-loop|Health workers review and confirm every AI-assisted score before any referral is issued.|
|Transparency|Risk tier breakdown shows the contribution of clinical vs. AI components, not a single black-box<br>number.|
|Explainability|Pathology probabilities are surfaced per-feature so workers see what drove the score.|
|Error handling|Low-confidence or ambiguous AI outputs are flagged for mandatory specialist review rather<br>than auto-resolved.|
|TB-confusion safeguard|TB-associated probability is shown alongside silicosis probability whenever both are elevated.|
|Data privacy|Worker data and images are stored locally (SQLite) with minimal retention by default.|
|Non-diagnostic positioning|UI language consistently uses “risk indication” and “referral recommendation,” never<br>“diagnosis.”|



## **6. Societal Impact, Limitations & Future Work** 

### **6.1 Societal Impact** 

I<sup>Extends specialist-grade first-line screening to rural and informal-sector workers with no radiologist access.</sup> 

- I<sup>Strengthens worker access to legally mandated compensation through earlier, better-documented detection.</sup> 

- I<sup>Reduces public-health misallocation caused by silicosis cases wrongly treated as tuberculosis.</sup> 

### **6.2 Known Limitations** 

- I<sup>Model trained/validated on available chest X-ray datasets; large-scale clinical validation is still required before any</sup> regulatory claim. 

- I<sup>False positives/negatives are possible — mitigated by the human-in-the-loop referral design, not eliminated.</sup> 

- I<sup>Current architecture assumes intermittent internet connectivity for model inference and sync.</sup> 

### **6.3 Future Work** 

I<sup>Integration with India's Ayushman Bharat digital health ecosystem for continuity of care.</sup> 

- I<sup>On-device / offline inference for fully connectivity-independent rural deployment.</sup> 

- I<sup>Genuine Grad-CAM visual explainability overlays on X-ray images.</sup> 

- I<sup>Expanded regional-language support and aggregate occupational-health dashboards for policymakers.</sup> 

## **7. Conclusion** 

Silicosis is a preventable disease that continues to disable and kill workers primarily because early detection cannot reach the people who need it. SilicoSafe addresses this not by replacing clinicians but by extending a transparent, explainable, human-supervised first screen to the point of contact — the worksite and the community clinic. By combining structured clinical risk scoring with AI-assisted imaging analysis under a strict triage-not-diagnosis design philosophy, SilicoSafe offers a deployable, safety-conscious path to earlier intervention, better referral quality, and improved access to compensation for some of the world's most under-served workers. 

### **References** 

- [1] World Health Organization, “Silicosis,” WHO Fact Sheets, Geneva, Switzerland. 

SilicoSafe — AI Diagnostic Triage for Silicosis 

Page 4 

[2] International Labour Organization, “Occupational Lung Diseases: Prevention and Control,” ILO Report, Geneva. 

[3] G. Huang, Z. Liu, L. van der Maaten, and K. Q. Weinberger, “Densely Connected Convolutional Networks,” in Proc. IEEE CVPR, 2017. 

[4] J. P. Cohen et al., “TorchXRayVision: A Library of Chest X-ray Datasets and Models,” MIDL, 2022. 

[5] P. Rajpurkar et al., “CheXNet: Radiologist-Level Pneumonia Detection on Chest X-rays with Deep Learning,” arXiv preprint, 2017. 

[6] National Institute for Occupational Safety and Health (NIOSH), “Silicosis Surveillance,” CDC, USA. 

[7] V. Gulshan et al., “Development and Validation of a Deep Learning Algorithm for Detection of Diabetic Retinopathy,” JAMA, 2016 (reference architecture for clinical AI screening). 

SilicoSafe — AI Diagnostic Triage for Silicosis 

Page 5 

