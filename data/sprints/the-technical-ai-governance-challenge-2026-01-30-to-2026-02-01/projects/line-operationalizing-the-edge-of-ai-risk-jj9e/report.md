# **LINE⁴: Operationalizing the Edge of AI Risk**<sup>**1**</sup> 

Joseph Awuah1 Adjoa Sarpong 2 Amo Joshua 3 Hacettepe University Meridith College University of Ghana 

**With** 

Apart Research 

## **Abstract** 

As frontier AI models accelerate toward critical capability thresholds, the landscape of safety evaluation remains fragmented and opaque. While major labs like OpenAI, Anthropic, and Google DeepMind have published safety frameworks (e.g., Preparedness Framework, RSP, FSF), they utilize disparate terminologies and metrics, creating a "Tower of Babel" that obscures the aggregate risk level of the industry. 

**<u>Line4</u>** addresses this visibility gap by functioning as an operational "watchtower" for AI risk. Inspired by the call for verifiable red lines at the CSEAI Hackathon, we developed a unified dashboard that ingests, normalizes, and visualizes safety data across four critical domains: CBRN (Chemical, Biological, Radiological, Nuclear), Cyber Offense, Autonomous Replication, and Deceptive Alignment. Our approach utilizes an automated intelligence pipeline to scrape System Cards and map qualitative risk levels (e.g., "ASL-2" or "Medium") onto a standardized 0–100 risk scale. The result is a real-time visualization of the "distance to danger," transforming abstract safety commitments into hard, trackable metrics for policymakers and independent auditors. 

> 1 Research conducted at the <u>Technical AI Governance Challenge, 2026</u> 

## **1. Introduction** 

_The primary problem in current AI governance is not a lack of safety evaluations, but a lack of interoperable signals. When Anthropic reports a model is "ASL-2" and OpenAI reports a model is "Medium Risk," external stakeholders—including regulators and independent researchers—struggle to compare these statuses or assess how close the ecosystem is to a catastrophic event._ 

_This opacity creates a dangerous lag. By the time a "Red Line"—such as the ability to autonomously synthesize a pathogen—is visibly crossed in a public deployment, it may be too late to implement containment measures. We need a system that tracks the velocity of capability improvements toward these thresholds in real-time._ 

#### Our main contributions are: 

1. A Unified Risk Schema: _We designed a normalization logic that translates disparate lab frameworks (RSP, PF, FSF) into a single, comparable quantitative scale (0–100), defining a universal "Red Line" at score 80._ 

2. The Line4 Dashboard: _We built a functional Alpha dashboard (using Streamlit and Next.js) that visualizes risk velocity, allowing users to instantly identify which labs are approaching critical thresholds in CBRN, Cyber, and Autonomy._ 

3. Automated Intelligence Engine: _We demonstrated a prototype "Watcher" script using LLMs to parse unstructured System Cards and extract structured risk evidence, reducing the manual burden of monitoring._ 

## **2. Related Work** 

_Our work builds directly on the foundational safety frameworks published by Frontier Labs:_ 

- Anthropic’s Responsible Scaling Policy (RSP): _Which introduces the concept of Automation Safety Levels (ASL)._ 

- OpenAI’s Preparedness Framework _categorizes risk into tracked levels (Low, Medium, High, Critical)._ 

- Google DeepMind’s Frontier Safety Framework, _which utilizes Critical Capability Levels (CCLs)._ 

_While organizations like_ METR _provide the evaluation protocols (the "tests"), and projects like_ AI LabWatch _provide static analysis, there is a gap in operational tooling. Existing efforts are often_ 

_static reports or blog posts. Line4 differs by treating safety data as a live operational stream, similar to a financial dashboard or cybersecurity SOC (Security Operations Center), focusing on the visualization of thresholds rather than just the evaluation of models._ 

## **3. Methods** 

3.1 Data Ingestion and Normalization _We focused on the four industry-standard "Catastrophic Risk" tracks: CBRN, Cyber Offense, Autonomous Replication, and Deceptive Alignment. To normalize the data, we created a mapping logic:_ 

- _Low Risk / ASL-1 = Score 0–25_ 

- _Medium Risk / ASL-2 = Score 26–50_ 

- _High Risk / ASL-3 = Score 51–79 (The "Watch" Zone)_ 

- _Critical Risk / ASL-4 = Score 80–100 (The "Red Line")_ 

3.2 The Intelligence Engine _We developed a Python-based pipeline utilizing the Gemini API. The script acts as an "Auditor," ingesting the raw text of System Cards (PDF/HTML), identifying relevant sections regarding capability evaluations, and extracting both the qualitative status and the supporting evidence._ 

3.3 Visualization Interface _We implemented the frontend using a dual-stack approach:_ 

- Streamlit: _For the data-heavy analytical dashboard, featuring radar charts for lab comparison and "Velocity Charts" to track risk over time._ 

- Next.js: _For the public-facing landing page, designed with an "editorial intelligence" aesthetic to communicate authority and clarity to non-technical policymakers._ 

## **4. Results** 

_We successfully deployed the Line4 Alpha, demonstrating the ability to visualize disparate risk profiles in a single view._ 

- 4.1 The Risk Heatmap _Our dashboard generates a heatmap (Figure 1 in our demo) that instantly highlights risk disparities. In our testing with historical and projected data, the heatmap clearly distinguished between models that are "safe" (Green) and models that are approaching the "Watch" threshold (Yellow)._ 



- 4.2 Threshold Velocity _The core result of our work is the "Distance to Red Line" tracker. By plotting the normalized scores of sequential model releases (e.g., GPT-4 -> GPT-4o -> o1), Line4 makes the rate of improvement visible. This allows observers to predict when a Red Line might be crossed before the model is released._ 



_Observation: Visualizing the data revealed that while "Autonomous Replication" risks remain generally low across labs, "Cyber Offense" capabilities are trending upward at a steeper velocity, suggesting this red line may be threatened sooner than Bio-risk._ 

- 

## **5. Discussion and Limitations** 

Implications _Line4 shifts the paradigm from "trusting the labs" to "verifying the trend." By operationalizing the edge of risk, we provide a tool for the International Network of AI Safety Institutes to define automatic triggers—e.g., "If the Line4 Aggregate Score for Bio-risk hits 60, mandatory external auditing is triggered."_ 

### **Limitations** 

Data Availability: _Our system currently relies on labs publishing their System Cards. If a lab chooses to go dark, our passive scraping method fails._ 

Subjectivity of Normalization: _Mapping "Medium Risk" to a specific number (e.g., 45 vs. 50) involves subjective interpretation._ 

Hackathon Scope: _For this demonstration, we utilized a mix of real extracted data and projected "future model" data to demonstrate the dashboard's alert capabilities during a breach scenario._ 

### **Future Work** 

Direct API Integration: _Connecting directly to evaluation harnesses (like METR’s API) for raw pass@k scores rather than relying on interpreted System Cards._ 

Email Alert System: _Implementing a push notification system for governance stakeholders when specific thresholds are breached._ 

## **6. Conclusion** 

_The presentation by the CSEAI Founder highlighted a critical need: we cannot manage what we cannot measure. Line4 proves that it is possible to synthesize the complex, fragmented world of AI safety evaluations into a clear, operational signal. By building the "radar" for these red lines, we aim to ensure that the crossing of a catastrophic threshold is a decision made with eyes wide open, not an accident that catches humanity by surprise._ 

## **Code and Data** 

- Live Website [ <u>https://line4.vercel.app/</u> ] 

- Code Repository: _<u>[https://github.com/youngceo10/AI-Red-line-track</u> ]_ 

- Live Dashboard: _<u>[https://ai-red-line-tracker.streamlit.app/</u> ]_ 

## **Author Contributions (optional)** 

Joseph Awuah: _Led the governance strategy, defined the policy implications of the "Red Lines," and structured the risk normalization logic based on international safety frameworks._ Adjoa Sarpong: _Led the Bio-Risk (CBRN) track, validating the medical and biological evaluation metrics to ensure the dashboard accurately reflected real-world scientific threat models._ 

Joshua Amo: _Led the technical architecture, building the full-stack implementation, including the Next.js landing page, the Streamlit dashboard, and the data visualization engines._ 

## **References** 

1. _Anthropic. (2024). Responsible Scaling Policy. Anthropic Research._ 

2. _OpenAI. (2024). Preparedness Framework. OpenAI Safety._ 

3. _Google DeepMind. (2024). Frontier Safety Framework._ 

4. _METR. (2024). Evaluations for Autonomous Replication._ 

## **Appendix** (optional) 

_Supplementary material such as additional figures, detailed methodology, prompts used, extended results, etc._ 

## **LLM Usage Statement** 

_We utilized Google Gemini and GitHub Copilot to assist in brainstorming the architectural stack, generating boilerplate code for the Streamlit dashboard, and drafting sections of this report. All safety data points and policy definitions were verified by the team against official lab documentation._ 

