# **RED30 AI Red Lines Tracker: A Comprehensive Technical Infrastructure for Monitoring Frontier Model Proximity to Critical Safety Thresholds** 

Kunal Singh Rujuta Karekar Aman Agarwal Independent Independent Independent **With** Apart Research 

## **Abstract** 

_Each frontier developer publishes self-assessments under its own risk framework: OpenAI’s Preparedness Framework, Anthropic’s Responsible Scaling Policy, Google DeepMind’s Frontier Safety Framework, and etc. However, these assessments remain disconnected, lack a basis tracking for dangerous capabilities, and are rarely presented in a way that allows direct cross-lab comparison or contextualization with compute infrastructure. We present a_ web-based dashboard “AI Red Lines Tracker” _to visually track global AI infrastructure and risk landscape in terms of frontier lab’s risk analysis, AI RnD acceleration tracker, current proximity to thresholds, areas of convergence and divergence and also tracking training compute, datacentres, compute concentration across frontier labs. We also propose_ RED30, _a global baseline framework that defines 30 minimum, non-negotiable safety and ethical boundaries that frontier AI models must not cross. These indicators are derived directly from binding international law, human rights conventions, data protection regulations, criminal law statutes and consumer protection frameworks. We systematically analyse all frontier models with this_ RED30 _framework and present the findings._ 

## **1. Introduction** 

_AI Models now demonstrate increasingly sophisticated performance across domains previously considered human-exclusive, including scientific reasoning, code generation, strategic planning, and multimodal understanding. While these advances offer immense societal benefit, they simultaneously lower barriers to misuse in ways that could result in catastrophic outcomes [14,15]._ 

_Four domains are of particular concern and are explicitly tracked by leading laboratories:_ 

- _Biological and chemical weapons development assistance_ 

- _Offensive cybersecurity at scale_ 

- _Large-scale persuasion, manipulation, and disinformation_ 

- _Autonomous AI research and recursive self-improvement_ 

_Each major developer has responded by publishing structured risk assessments: OpenAI via its Preparedness Framework [1,2], Anthropic through its Responsible Scaling Policy [8], Google DeepMind via the Frontier Safety Framework [10], and xAI via its Frontier AI Framework introduced in late 2025. Despite these efforts, several critical barriers to effective oversight remain._ 

#### Our main contributions are: 

1. _A visually interactive dashboard showing, AI red lines analysis, frontier lab models risk analysis, compute resources and infrastructure analysis and AI incidents dashboard_ 

2. RED 30, _a standardized framework of_ 30 universal AI red line indicators, _organized into 4 categories: Critical Harm (8), Systemic Harm (8), Individual Harm (8), Emerging Standards (6). These indicators serve as priority indicators to measure models risks across categories derived from international regulatory frameworks around the world_ 

3. _AI R&D Tracker showing cross labs comparison to critical thresholds with METR benchmark integrations_ 

4. _16 frontier model risk analysis across 4 major labs and processed 24 model system cards to show model risk thresholds across CBRN domains._ 

5. _Compute Infrastructure dashboard showcasing 20 frontier models training compute (2023-2026), mapping 18 major data centres with 2620 GW global capacity and list of EU AI Act compliant models based on FLOP thresholds._ 

_6. Aggregated_ 354 frontier-model-relevant incidents _from AI Incident Database, categorized incidents by organization and harm types: 15 Offenses, 199 Misuses, 43 Biases, 97 Harmful Outputs_ 

## **2. Related Work** 

_Risk assessment frameworks published by frontier laboratories form the primary data foundation of this project [1–11]. OpenAI’s Preparedness Framework [2] provides a detailed per-category scoring and threshold-proximity metrics to date. Anthropic’s Responsible Scaling Policy [8] introduces precautionary ASL tiers, while Google DeepMind’s Frontier Safety Framework [10] emphasizes Capability Confidence Levels and graded alert thresholds. xAI’s published Frontier AI Framework employs quantitative benchmarks across multiple dual-use domains. Independent transparency and evaluation efforts include the Stanford AI Index annual reports [11,19], Epoch AI’s compute and capability trend analysis [12], the incident database [13], METR’s red-line benchmark definitions [16], and Apollo Research’s public model evaluations [16]. Academic literature has explored extreme-risk evaluation methodologies [14] and proposed governance approaches for frontier systems [15]. Civil society initiatives such as the Global Call for AI Red Lines [17] have advocated for clearer thresholds and stronger deployment safeguards._ 

## **3. Methods** 

#### 3.1 Data Acquisition and Extraction 

_All data is sourced exclusively from publicly released documents: system cards, framework descriptions, blog posts, and third-party benchmark reports._ 

- _Model metadata (name, release date, system card URL)_ 

- _Risk scores (no. of models, where available)_ 

- _Risk levels (lab-specific: Low/Medium/High/Critical, ASL-1–4, CCL stages, etc.)_ 

- _Key findings_ 

- _Source document section references_ 

#### 3.2 Data Processing and Visualization 

_Chart data preparation occurs in chart-transformers.ts. All visualizations use Recharts (line, bar, radar, heatmap) or react-simple-maps (world map). Lab-specific terminology and color scales are preserved where possible, with optional cross-lab normalization views._ 

## **4. Results** 

_The web based dashboard currently tracks 17+ frontier models across four laboratories (OpenAI ≈6, Anthropic 5, Google DeepMind 3, xAI 4)._ 

#### Key observations (as of January 2026 data): 

- OpenAI o3 maintains medium rating in biological/chemical threats 

- xAI Grok 4 family demonstrates particularly strong quantitative performance across biology, chemistry, and cyber benchmarks 

- Anthropic Claude 4 series models approach preemptive ASL-3 deployment, nearing ASL-4 thresholds in autonomy and CBRN domains 

- Google DeepMind Gemini 3 series meets alert thresholds in cyber-uplift but remains below them in ML R&D automation 

## **5. Discussion and Limitations** 

#### _Implications_ 

_The results demonstrate that frontier models from multiple independent laboratories are approaching and in several cases reaching the high-risk or critical red lines defined in their own frameworks. This convergence across organizations strengthens the case for external red-teaming, compute governance, standardized reporting formats, and potential deployment restrictions when clear thresholds are crossed [15,17]._ 

### Limitations 

- _All data originates from voluntary frameworks inherits potential optimism bias, incomplete evaluation suites, or deliberate minimization_ 

- _Manual extraction process limits update frequency and introduces human error risk_ 

- _Direct comparison across frameworks remains imperfect due to differing methodologies and category definitions_ 

- _No automated ingestion of new documents (planned for future work)_ 

- _Scope currently limited to four leading laboratories (Open Source for future work)_ 

- _RED30 framework to measure AI Red lines risk can be extended (Future scope)_ 

- _AI Incidents dashboard's scope could not be expanded because of limited time, we plan to plot AI incident reports across model release timings, countries and other parameters._ 

## 6. Conclusion 

_The RED30: AI Red Lines Tracker represents a step toward democratized, and visually accessible monitoring of frontier AI risk assessments. By integrating official self-reports with global compute context, incident tracking, and governance signals, it provides a picture of how close current models are to crossing critical safety thresholds across multiple independent developers._ 

## **Code and Data** 

- Code repository _:_ _<u>https://github.com/KUNALSINGH9373/AI-Red-Lines-Tracker-2026</u>_ 

- - WebSite Dashboard: _<u>https://ai-red-lines-tracker-2026.vercel.app</u>_ 

## **References** 

1. _OpenAI. (2023). Preparedness Framework (v1)._ 

   - _<u>https://cdn.openai.com/openai-preparedness-framework-beta.pdf</u>_ 

2. _OpenAI. (2024). Preparedness Framework (v2)._ _<u>https://openai.com/preparedness</u>_ 

3. _OpenAI. (2024). GPT-4o System Card._ _<u>https://openai.com/index/gpt-4o-system-card/</u>_ 

4. _OpenAI. (2024). o1 System Card._ _<u>https://openai.com/index/openai-o1-system-card/</u>_ 

5. _OpenAI. (2025). o3 & o4-mini System Card._ 

   - _<u>https://openai.com/index/o3-o4-mini-system-card/</u>_ 

6. _OpenAI. (2025). o3-mini System Card._ _<u>https://openai.com/index/o3-mini-system-card/</u>_ 7. _OpenAI. (2025). GPT-5 System Card._ _<u>https://openai.com/index/gpt-5-system-card/</u>_ 8. _Anthropic. (2024). Responsible Scaling Policy v2.2._ 

   - _<u>https://www.anthropic.com/responsible-scaling-policy</u>_ 

9. _Anthropic. (2025). Claude 4 family safety reports._ _<u>https://www.anthropic.com/news</u>_ 

10. _Google DeepMind. (2025). Frontier Safety Framework v3.0._ 

_<u>https://deepmind.google/discover/blog/frontier-safety-framework/</u>_ 

11. _Stanford HAI. (2025). AI Index Report 2025._ _<u>https://aiindex.stanford.edu/report/</u>_ 

12. _Epoch AI. (2025). Trends in Machine Learning Compute._ _<u>https://epochai.org/trends</u>_ 

13. _AI Incident Database._ _<u>https://incidentdatabase.ai/</u>_ 

14. _Shevlane et al. (2023). Model Evaluation for Extreme Risks._ <u>arXiv:2305.15324</u> 

15. _Anderljung et al. (2023). Frontier AI Regulation. arXiv:2307.03718_ 

16. _METR. (2025). Public evaluation reports._ _<u>https://metr.org</u>_ 

17. _Global Call for AI Red Lines._ _<u>https://red-lines.ai</u>_ 

_Appendix: Limitations & Dual-Use Considerations_ 

#### A.1 Methodological Limitations 

- _False positives/negatives inherent in self-reported assessments_ 

- _Manual extraction introduces transcription errors and update delays_ 

- _Framework incompatibility limits perfect cross-lab quantitative comparison_ 

- _No independent capability verification performed_ 

#### A.2 Dual-Use Risks 

_The tool could help identify currently highest-risk models in specific domains, potentially informing misuse targeting. All displayed information is already public; no new attack vectors are revealed._ 

#### A.3 Responsible Disclosure 

_No novel vulnerabilities discovered. Future findings would be reported privately to the relevant lab first, with escalation to trusted third parties (AISIs, METR, Apollo) if necessary._ 

#### A.4 Ethical Considerations 

_Prioritizes public-interest transparency over potential information-hazard concerns. Open-source license supports broad access and community auditing._ 

#### A.5 Suggested Improvements 

- _Automated system-card parsing_ 

- _Real-time threshold-crossing notifications_ 

- _Historical version snapshots_ 

- _Support for additional laboratories_ 

#### LLM Usage Statement 

Grok _(xAI) and_ Claude _(Anthropic) were used to scrape the data from pdf of model cards files and build a structure representation of the unstructured data._ Claude Code _was used to build the web based dashboard to show all the comparison metrics. All facts, data references, findings, and claims were independently verified against the repository contents (README.md, JSON files, code files, and RED30_Research_Document.md). No data is fabricated._ 

