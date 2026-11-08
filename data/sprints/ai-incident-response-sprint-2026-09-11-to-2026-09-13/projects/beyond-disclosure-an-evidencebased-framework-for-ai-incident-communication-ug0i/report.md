## **Beyond Disclosure: An Evidence-Based Framework for AI Incident Communication** 

Luka Janicijevic 1 Leyla Amur 2 Aditya Singh 3 Independent Researcher Independent Researcher Independent Researcher lukaj2003@gmail.com leylaamur@gmail.com the.coder.zen@gmail.com 

**With** 

Apart Research 

##### **Abstract** 

_Effective communication helps organizations respond to AI incidents, protect affected parties and support independent scrutiny. We developed a rubric for assessing public communication by frontier AI labs, model developers and AI infrastructure providers._ 

_Our research base includes more than 300 academic, regulatory and professional sources and public records. The rubric contains 15 criteria across seven communication areas and requires dated evidence for each assessment. Four criteria apply only under specified conditions._ 

_Applied separately to OpenAI and Hugging Face during the July 2026 incident, the preliminary analysis highlights Hugging Face’s disclosure before widespread coverage and OpenAI’s later technical reporting and updates. It also identifies gaps in attribution, consistency across public statements, coordination and information for affected parties. External review remains pending. The rubric links these gaps to practical improvements and supports advance planning for communication during future incidents._ 

#### 1. Introduction and Research Question 

AI incidents can unfold faster than organizations can understand, and communicate, what is happening. As AI agents gain access to data, digital tools, and vital infrastructure, unexpected or unauthorized actions may cross organizational boundaries before any party holds a complete account. In this period of uncertainty, communication is part of incident response. Timely and accurate information can alert those at risk, support containment, and coordinate action. Delayed, vague or misleading communication can create a second failure by leaving people who could respond unsure of what happened, whether they are affected or what they should do.<sup>1</sup> 

The July 2026 OpenAI–Hugging Face incident demonstrates this problem. During an internal cybersecurity evaluation, agents powered by OpenAI models circumvented containment controls and compromised parts of Hugging Face’s production infrastructure.<sup>2</sup> Hugging Face disclosed the intrusion before OpenAI identified its models as responsible.<sup>3</sup> The incident shows how fragmented evidence and delayed attribution can hinder protective action, obscure responsibility and complicate independent scrutiny, even when the technical harm is ultimately contained. 

This study focuses on frontier AI developers and AI infrastructure providers. These organizations build or operate the systems involved and possess essential information about an incident’s causes, reach, and consequences. They are not the only important communicators, nor are they necessarily the first to disclose an incident. Nevertheless, their accounts are critical to affected organizations and external investigators. We therefore ask: How can the publicly observable communication of frontier AI developers and infrastructure providers during a cross-organizational agentic AI incident be assessed consistently, and what does applying this assessment to the July 2026 OpenAI–Hugging Face incident reveal? 

To answer this question, we developed a 15-criterion, evidence-based communication rubric and applied it separately to OpenAI and Hugging Face. Our principal contributions are a scoring system for assessing incident communication, a structured comparison of the two organizations’ responses, and best practices based on communication areas. The purpose is not to produce a reputation ranking, but to show what was communicated well, where material gaps remained, and what organizations should improve before the next incident. 

#### 2. Literature Review 

Existing guidance for AI incident communication comes primarily from crisis communication and cybersecurity. Crisis-communication research emphasizes early disclosure, acknowledgment of uncertainty, consistency, and actionable information.<sup>4</sup> Coordinated vulnerability disclosure guidance similarly addresses publication timing, communication with external researchers and coordination among affected organizations.<sup>5</sup> However, these fields generally concern conventional organizational crises or identifiable software vulnerabilities. They do not fully 

address incidents involving unexpected AI-agent behavior, uncertain authorization or attribution, and activity spanning several organizations. 

Emerging AI frameworks address parts of this problem. The OECD proposes a common structure for reporting AI incidents across jurisdictions and sectors,<sup>6</sup> while the NIST Generative AI Profile recommends communicating incidents and errors to relevant actors and affected communities.<sup>7</sup> The EU AI Act and General-Purpose AI Code of Practice establish serious incident reporting expectations for certain providers,<sup>8</sup> and proposals such as FLARE-AI explore standardized reporting of AI flaws across organizations.<sup>9</sup> These initiatives primarily support documentation, risk management, regulatory reporting, or incident databases rather than assessing the quality of public communication as an incident unfolds.<sup>10</sup> 

Our review did not identify an established benchmark for evaluating how frontier AI labs and infrastructure providers publicly communicate during a cross-organizational agentic AI incident. We address this gap by combining relevant practices from adjacent fields into a criterion-level assessment. The framework examines when organizations communicate, what they explain, how they distinguish evidence from uncertainty, whether they provide protective guidance, how they update their accounts, and how they engage with other organizations and external investigators. It therefore moves beyond asking simply whether or not an incident was reported to identify specific communication strengths, evidence gaps, and areas for improvement. 

#### 3. Methodology 

##### 3.1 Research design and scope 

We developed an evidence-based assessment of organizational communication during agentic AI incidents, focusing on frontier AI laboratories, model developers, and AI infrastructure providers. We applied it separately to OpenAI and Hugging Face during the July 2026 incident. The assessment examines each organization’s full communication record: what it communicated, when, with what evidence and how clearly it helped others understand and respond. It evaluates observable communication, rather than the quality of the underlying technical response or private actions that cannot be verified. 

##### 3.2 Evidence and criterion selection 

We synthesized more than 300 academic, regulatory, professional and primary sources, recording their claims, conflicting findings and research gaps. We reduced 24 candidate criteria to 15 after examining their supporting evidence, overlap and suitability for assessment from public communications. Case evidence from OpenAI and Hugging Face was excluded from criterion development to avoid tailoring the assessment to the organizations evaluated. 

The criteria cover seven areas: timing (C1); the incident account (C2–C5); incident framing (C6–C8); responsibility and remedy (C9); protection and reach (C10, C11 and C15); updates and coordination (C12–C13); and external scrutiny (C14). Eleven criteria apply to all incidents, 

while C11, C13, C14 and C15 apply only under specified conditions. Appendix A provides the complete criterion wording and the question used to guide each assessment. 

##### 3.3 Scoring 

Each applicable criterion is scored against descriptions of observable practice: 

- **0:** Absent or actively harmful 

- **1:** Minimal or significantly deficient 

- **2:** Substantially present, with important gaps 

- **3:** Strong practice meeting the full evidence-based standard 

- **N/A:** Not applicable or insufficient evidence 

Every numerical score must cite a dated source and include a quotation or brief explanation connecting the evidence to the scoring description. For N/A, reviewers record whether the criterion does not apply or the evidence is insufficient. A documented omission is assessed against the scoring descriptions; a lack of evidence about private activity is not automatically treated as failure. 

Criteria are weighted from one to three according to the strength of the supporting evidence and the consequences of poor communication. The assessment calculates the organization’s weighted points as a percentage of the maximum available points. Criteria marked “N/A” are excluded. Because an overall percentage can conceal important differences, individual criterion scores remain the primary result. 

##### 3.4 Case evidence 

We assembled chronological evidence packs for both organizations, covering their first public statements through 26 August 2026, when OpenAI’s technical report and the METR/Redwood investigation were published.<sup>11</sup> Later material, including September US Senate correspondence, was excluded.<sup>12</sup> 

The packs contained public statements, technical reports, status-page entries, executive communications, publicly available direct notifications, and relevant exchanges with other organizations or investigators. Each item identified its source, publication date and subsequent corrections or updates, with archived versions of revised material. An accompanying timeline recorded both the event date and the date the information became public. Conflicting dates were retained without reconciliation. The timeline contained no assessment commentary; the authors’ analytical notes were kept separately. 

##### 3.5 Independent assessment and external review 

Three external reviewers with professional media, journalism, and communications experience, who had not helped develop the criteria, were asked to independently assess each organization using the same rubric and evidence packs. The review was designed to examine how 

consistently the criteria could be applied and provided an independent check on the authors’ own playtest scores. 

Reviewers received the rubric, scoring rules, source documents and timeline, but not the authors’ analytical notes, abstract, findings or discussion. They could not see the authors’ scores or one another’s ratings until all assessments were returned. Organization names remained visible, and reviewers’ prior knowledge of the incident could not be eliminated. 

Unfortunately, zero external assessments were returned in time for publication, which is noted as a significant limitation in the independent assessment of the rubric. 

#### 4. Findings 

##### 4.1 OpenAI’s Communication in Incident Response 

Our internal playtest of the rubric scored OpenAI 31/42, noting C15 was marked Not Applicable, as the selected evidence did not establish a specific personal-harm situation requiring the support measures listed in C15. 

Internal playtests observed OpenAI described the mechanism of attacks and the conditions which led to the breach and acknowledgement of their ignorance towards earlier warning signals. This self-acceptance reads as the first step towards building stronger measures to prevent such failures in the future. 

However, this playtest also highlighted a sense that OpenAI was oblivious to the fact that its own models in CyberGym evaluations had executed chained zero-day vulnerabilities and had gained privileged access to OpenAI’s own servers and were carrying out a cyberattack on Hugging Face’s infrastructure. 

##### 4.2 Hugging Face’s Communication in Incident Response 

Our internal playtest of the rubric scored Hugging Face 33/42, noting C15 was marked Not Applicable, as the selected evidence did not establish a specific personal-harm situation requiring the support measures listed in C15. 

Internal playtests observed Hugging Face’s strength in communicating the detection of the incident as agentic in nature, and communicating their methodology in defending themselves from the intrusion. However, we also observed that Hugging Face failed to publicly state the exact time when human responders realized the attack and when they were able to take appropriate actions in response. 

##### 4.3 Rubric review and analysis 

As part of the internal playtest, we noted that criteria C10 and C15 were difficult to use for recent or unfolding events. Due to the limiting nature of public evidence, an accurate assessment of protective guidance or support of harms was difficult to determine, due to the private and confidential nature of correspondence with potential victims of the incident. 

In future testing and design, these criteria may be revisited for their relevance and usefulness in determining a score for an organization. 

#### 5. Best practices for future AI incidents 

The following practices translate the rubric into guidance across seven communication areas. They draw on research and guidance from adjacent fields; their application to agentic AI incidents requires further testing. 

**Timing.** Communicate while public attention is still developing, using the facts available at the time. The first statement should explain the known exposure and provide useful protective guidance, with uncertainties clearly identified.<sup>22</sup> 

**The incident account.** Explain what was affected, how widely, for how long, and how and when the incident was discovered. Separate established facts from unknowns, explain remaining uncertainties and provide a date for the next update. Support reassurance with what was examined and what risks remain.<sup>23</sup> 

**Incident framing.** Explain the definitions behind the incident’s classification. Use consistent language across statements and spokespeople to distinguish the AI system’s actions from human decisions, without exaggerating or downplaying either. We additionally propose documenting who operated and authorized the system, which safeguards applied, and what evidence supports the account.<sup>24</sup> 

**Responsibility and remedy.** Explain the organization’s own role without shifting blame. Acknowledge responsibility and apologize when it is established. Distinguish promised remedies from completed actions, and provide evidence that others can check.<sup>25</sup> 

**Protection and reach.** Directly notify identifiable affected people and organizations through safe, accessible channels. Provide specific protective steps in priority order, including relevant deadlines and actions taken on recipients’ behalf. Where people face personal harm, offer human support, scam warnings and options to challenge or reverse harmful outcomes.<sup>26</sup> 

**Updates and coordination.** Keep promised update dates and clearly label corrections across the channels where the original claims appeared. Link outdated statements to current information. Coordinate accounts to explain who did what, acknowledge unresolved disagreements, and announce changes in attribution. Address outstanding questions in a closing account.<sup>27</sup> 

**External scrutiny.** Provide clear reporting channels, acknowledge credible external contributions, and communicate throughout the investigation. Answer press questions or explain specific constraints. Independent reviewers should describe their own access, limitations, relevant relationships and freedom to publish.<sup>28</sup> 

### 6. Discussion, Limitations, and Conclusion 

This study presents a rubric for assessing how organizations communicate during an agentic AI incident. Its 15 criteria provide a structured way to identify communication strengths, gaps and practical improvements. Assessing each organization’s public record separately also helps show how different accounts of the same incident develop over time. 

The preliminary analysis shows strengths in OpenAI’s and Hugging Face’s communications. Hugging Face disclosed the intrusion before it was widely reported by the media and later shared a technical timeline. OpenAI’s technical reports, dated updates, and work with external investigators provided more information for review. However, the record also contained shifting explanations of detection and attribution, corrections to claims about other parties, and unresolved questions about who was affected. These findings show that technical detail alone is not enough: readers also need clear explanations of what has changed, what remains uncertain, and what steps they should take. 

These findings remain provisional until external review can be conducted. The study examines one incident and relies on public evidence, which cannot establish everything either organization communicated privately or did internally. Several criteria also draw on research from related fields. Further testing across incidents and reviewers is needed to assess the rubric’s consistency, refine its scoring descriptions and examine how weighting affects the results. 

Future work could expand the existing best practices into detailed guidance and action plans for each criterion. Each plan could explain what good practice looks like, how to address an identified weakness, who should take responsibility and what evidence would demonstrate improvement. For example, guidance on notifying affected parties could include steps for identifying recipients, drafting useful notices and following up as the investigation develops. Guidance on updates and corrections could provide templates for explaining changes and preserving earlier versions. 

An interactive tool could connect assessment results to these action plans, helping organizations prioritize improvements and track their progress. The guidance could also be tested in simulated incidents involving several organizations, alongside communication professionals, technical teams and potential recipients. This would help assess both how easily the guidance can be used and how well it supports understanding and action. 

Organizations should agree in advance who will communicate, how affected parties will be notified and how updates and corrections will be coordinated.²⁹ Developing the rubric in this 

direction could make it useful both for reviewing past communication and for preparing teams to respond more clearly during future incidents. 

###### **Notes** 

1. Alison N. Novak and M. Olguta Vilceanu, “‘The Internet Is Not Pleased’: Twitter and the 2017 Equifax Data Breach,” _The Communication Review_ 22, no. 3 (2019): 196–221; Richard Knight and Jason R. C. Nurse, “A Framework for Effective Corporate Communication after Cyber Security Incidents,” _Computers & Security_ 99 (2020): 102036; Yixin Zou, Shawn Danino, Kaiwen Sun, and Florian Schaub, “You ‘Might’ Be Affected: An Empirical Analysis of Readability and Usability Issues in Data Breach Notifications,” in _Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems_ (New York: ACM, 2019), paper 194. 

2. OpenAI, “OpenAI and Hugging Face Partner to Address Security Incident during Model Evaluation,” July 21, 2026, updated July 28 and 29, 2026, 

<u>https://openai.com/index/hugging-face-model-evaluation-security-incident/; OpenAI, “The Hugging Face</u> Incident and the Road Ahead,” August 26, 2026, <u>https://openai.com/index/hugging-face-incident-and-the-road-ahead/; OpenAI,</u> _OpenAI–Hugging Face Incident Technical Report_ (San Francisco: OpenAI, August 26, 2026). 

3. Hugging Face, “Security Incident Disclosure — July 2026,” Hugging Face Blog, July 16, 2026, <u>https://huggingface.co/blog/security-incident-july-2026; OpenAI, “OpenAI and Hugging Face Partner”;</u> Simon Willison, “Now We Have a Timeline of the OpenAI Accidental Attack against Hugging Face,” Simon Willison’s Weblog, August 7, 2026, <u>https://simonwillison.net/2026/Aug/7/openai-timeline/.</u> 

4. W. Timothy Coombs, “Protecting Organization Reputations During a Crisis: The Development and Application of Situational Crisis Communication Theory,” _Corporate Reputation Review_ 10, no. 3 (2007): 163–76; W. Timothy Coombs, “Situational Crisis Communication Theory (SCCT): Refining and Clarifying a Cognitive-Based Theory of Crisis Communication,” in _The Handbook of Crisis Communication_ , 2nd ed., ed. W. Timothy Coombs and Sherry J. Holladay (Hoboken, NJ: Wiley-Blackwell, 2022), 193–204; An-Sofie Claeys, “The Benefits and Pitfalls of Stealing Thunder,” in Coombs and Holladay, _Handbook of Crisis Communication_ , 99–111; Matthew W. Seeger, “Best Practices in Crisis Communication: An Expert Panel Process,” _Journal of Applied Communication Research_ 34, no. 3 (2006): 232–44; World Health Organization, _Communicating Risk in Public Health Emergencies: A WHO Guideline for Emergency Risk Communication (ERC) Policy and Practice_ (Geneva: World Health Organization, 2017); Centers for Disease Control and Prevention, _Crisis and Emergency Risk Communication (CERC): Introduction_ , 2018 update (Atlanta: CDC, 2018). 

5. Allen D. Householder, Garret Wassermann, Art Manion, and Chris King, _The CERT Guide to Coordinated Vulnerability Disclosure_ , CMU/SEI-2017-SR-022 (Pittsburgh: Software Engineering Institute, Carnegie Mellon University, 2017); International Organization for Standardization and International Electrotechnical Commission, _ISO/IEC 29147:2018, Information Technology — Security Techniques — Vulnerability Disclosure_ , 2nd ed. (Geneva: ISO/IEC, 2018); Forum of Incident Response and Security Teams (FIRST), _Guidelines and Practices for Multi-Party Vulnerability Coordination and Disclosure_ , version 1.1 (FIRST, 2020). 

6. OECD, _Towards a Common Reporting Framework for AI Incidents_ , OECD Artificial Intelligence Papers, no. 34 (Paris: OECD Publishing, 2025), <u>https://doi.org/10.1787/f326d4ac-en.</u> 

7. National Institute of Standards and Technology, _Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile_ , NIST AI 600-1 (Gaithersburg, MD: NIST, 2024), <u>https://doi.org/10.6028/NIST.AI.600-1; National Institute of Standards and Technology,</u> _Artificial_ 

_Intelligence Risk Management Framework (AI RMF 1.0)_ , NIST AI 100-1 (Gaithersburg, MD: NIST, 2023), MANAGE 4.3, <u>https://doi.org/10.6028/NIST.AI.100-1.</u> 

8. Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act), OJ L, 12 July 2024, art. 55, para. 1, point c, and art. 73; European Commission, AI Office, _General-Purpose AI Code of Practice: Safety and Security Chapter_ , 10 July 2025, Commitment 9. 

9. Shayne Longpre et al., “FLARE-AI: Flaw Reporting for AI,” arXiv:2606.31567 (June 30, 2026), <u>https://arxiv.org/abs/2606.31567; see also Shayne Longpre et al., “In-House Evaluation Is Not Enough:</u> Towards Robust Third-Party Flaw Disclosure for General-Purpose AI,” arXiv:2503.16861 (2025); Sven Cattell, Avijit Ghosh, and Lucie-Aimée Kaffee, “Coordinated Flaw Disclosure for AI: Beyond Security Vulnerabilities,” arXiv:2402.07039 (2024). 

10. Regulation (EU) 2024/1689, art. 73; European Commission, _General-Purpose AI Code of Practice_ , Commitment 9; NIST, _Generative Artificial Intelligence Profile_ . 

11. OpenAI, “Hugging Face Incident and the Road Ahead”; OpenAI, _Incident Technical Report_ ; Ryan Greenblatt, Ajeya Cotra, and Hjalmar Wijk, “Brief Independent Investigation of Agents’ Behavior, Reasoning and Collaboration in the OpenAI / Hugging Face Hacking Incident,” METR, August 26, 2026, <u>https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/.</u> 

12. Josh Hawley, “Chairman Hawley Launches Investigation into OpenAI for Hacking, Existential Risk of AI Products,” press release with letter to Sam Altman dated September 9, 2026, US Senate, September 10, 2026, 

<u>https://www.hawley.senate.gov/chairman-hawley-launches-investigation-into-openai-for-hacking-existentia l-risk-of-ai-products/; Richard Blumenthal to Sam Altman, September 9, 2026, https://www.blumenthal.senate.gov/imo/media/doc/20260909_-_openai_-_cot_and_rogue_agentspdf.pdf;</u> Chris Van Hollen to Sam Altman, September 10, 2026, US Senate press release, <u>https://www.vanhollen.senate.gov/news/press-releases.</u> 

13. Hugging Face, “Security Incident Disclosure.” 

14. OpenAI, _Incident Technical Report_ ; Willison, “Now We Have a Timeline.” 

15. OpenAI, “OpenAI and Hugging Face Partner.” 

16. OpenAI, “OpenAI and Hugging Face Partner,” updates of July 28 and 29, 2026. 

17. OpenAI, “Hugging Face Incident and the Road Ahead”; OpenAI, _Incident Technical Report_ ; Greenblatt, Cotra, and Wijk, “Brief Independent Investigation.” 

18. Hawley, “Chairman Hawley Launches Investigation”; Blumenthal to Altman, September 9, 2026; Van Hollen to Altman, September 10, 2026; Associated Press, “Senators from Both Parties Question OpenAI on Breach of AI Startup Hugging Face,” September 10, 2026, 

<u>https://www.pbs.org/newshour/politics/senators-from-both-parties-question-openai-on-breach-of-ai-startup</u> -hugging-face. 

19. OpenAI, “OpenAI and Hugging Face Partner”; OpenAI, _Incident Technical Report_ . 

20. OpenAI, “OpenAI and Hugging Face Partner”; OpenAI, _Incident Technical Report_ ; Hugo Larcher et al., “Anatomy of a Frontier Lab Agent Intrusion: A Technical Timeline of the July 2026 Incident,” Hugging Face Blog, July 27, 2026, revised through July 30, 2026, <u>https://huggingface.co/blog/agent-intrusion-technical-timeline; revision history at https://github.com/huggingface/blog/commits/main/agent-intrusion-technical-timeline.md.</u> 

21. OpenAI, “OpenAI and Hugging Face Partner,” update of July 29, 2026; Greenblatt, Cotra, and Wijk, “Brief Independent Investigation”; Blumenthal to Altman, September 9, 2026. 

22. Laura M. Arpan and David R. Roskos-Ewoldsen, “Stealing Thunder: Analysis of the Effects of Proactive Disclosure of Crisis Information,” _Public Relations Review_ 31, no. 3 (2005): 425–33; An-Sofie Claeys and Verolien Cauberghe, “Crisis Response and Crisis Timing Strategies, Two Sides of the Same Coin,” _Public Relations Review_ 38, no. 1 (2012): 83–88; Claeys, “Benefits and Pitfalls”; Thomas I. Vaughan-Johnston, Joshua J. Guyer, Katie L. Lawrence, and Leandre R. Fabrigar, “Disclosure and Identification Information Increase the Benefits of Stealing Thunder,” _Social Influence_ 20, no. 1 (2025): 2447273; Yongtian Yu, Weiming Ye, and Kaihang Zhang, “Faster? Softer? Or More Formal? A Study on the Methods of Enterprises’ Crisis Response on Social Media,” _Mathematics_ 13, no. 10 (2025): 1582; Yan Huang and Marcia DiStaso, “Responding to a Health Crisis on Facebook: The Effects of Response Timing and Message Appeal,” _Public Relations Review_ 46, no. 3 (2020): 101909; Novak and Vilceanu, “Internet Is Not Pleased”; Coombs, “Protecting Organization Reputations.” 

23. WHO, _Communicating Risk_ ; CDC, _CERC: Introduction_ ; Anne Marthe van der Bles, Sander van der Linden, Alexandra L. J. Freeman, and David J. Spiegelhalter, “The Effects of Communicating Uncertainty on Public Trust in Facts and Numbers,” _Proceedings of the National Academy of Sciences_ 117, no. 14 (2020): 7672–83; Charlotte Dries, Michelle McDowell, Felix G. Rebitschek, and Christina Leuker, “When Evidence Changes: Communicating Uncertainty Protects against a Loss of Trust,” _Public Understanding of Science_ 33 (2024), <u>https://doi.org/10.1177/09636625241228449; Knight and Nurse, “Framework for</u> Effective Corporate Communication”; Zou et al., “You ‘Might’ Be Affected”; Vaughan-Johnston et al., “Disclosure and Identification Information”; Federal Trade Commission, _In re Blackbaud, Inc._ , complaint (2024); US Securities and Exchange Commission, “SEC Charges Four Companies with Misleading Cyber Disclosures,” press release 2024-174, October 22, 2024. 

24. OECD, _Defining AI Incidents and Related Terms_ , OECD Artificial Intelligence Papers, no. 16 (Paris: OECD Publishing, 2024), <u>https://doi.org/10.1787/d1a8d965-en; Regulation (EU) 2024/1689, art. 3, point</u> 49; Adriana Placani, “Anthropomorphism in AI: Hype and Fallacy,” _AI and Ethics_ 4 (2024): 691–98; Jem Bartholomew and Dhrumil Mehta, “How the Media Is Covering ChatGPT,” _Columbia Journalism Review_ , May 26, 2023; Sanneke Kuipers and Marleen Schonheit, “Data Breaches and Effective Crisis Communication: A Comparative Analysis of Corporate Reputational Crises,” _Corporate Reputation Review_ 25 (2022): 176–97; Carson Ezell, Xavier Roberts-Gaal, and Alan Chan, “Incident Analysis for AI Agents,” arXiv:2508.14231 (2025). 

25. W. Timothy Coombs, _Reexamining Crisis Communication_ (Gainesville, FL: Institute for Public Relations, 2026), <u>https://instituteforpr.org/reexamining-crisis-communication/; Coombs, “Situational Crisis</u> Communication Theory”; Kuipers and Schonheit, “Data Breaches and Effective Crisis Communication”; Soo-Yeon Kim and Jeong-Hyeon Lee, “How to Maximize the Effectiveness of Stealing Thunder in Crisis Communication: The Significance of Follow-Up Actions and Transparent Communication,” _Corporate Communications: An International Journal_ 27, no. 3 (2022): 425–40; Wouter Jong, “Beyond the Snapshot: Rethinking Crisis Communication Theories in Dynamic Crisis Situations,” _Public Relations Review_ 51 (2025): 102586; Peter H. Kim, Donald L. Ferrin, Cecily D. Cooper, and Kurt T. Dirks, “Removing the 

Shadow of Suspicion: The Effects of Apology versus Denial for Repairing Competence- versus Integrity-Based Trust Violations,” _Journal of Applied Psychology_ 89, no. 1 (2004): 104–18; Arthur W. Page Society, “The Page Principles,” accessed September 14, 2026, <u>https://page.org/site/the-page-principles.</u> 

26. Coombs, “Protecting Organization Reputations”; Zou et al., “You ‘Might’ Be Affected”; European Data Protection Board, _Guidelines 9/2022 on Personal Data Breach Notification under GDPR_ , version 2.0 (March 28, 2023), para. 90; Substance Abuse and Mental Health Services Administration, _SAMHSA’s Concept of Trauma and Guidance for a Trauma-Informed Approach_ , HHS Publication No. (SMA) 14-4884 (Rockville, MD: SAMHSA, 2014). 

27. Associated Press, _The Associated Press Statement of News Values and Principles_ (New York: Associated Press, 2026); BBC, _Editorial Guidelines_ , section 3, “Accuracy” (London: BBC, 2019); Kuipers and Schonheit, “Data Breaches and Effective Crisis Communication”; WHO, _Communicating Risk_ ; FIRST, _Multi-Party Vulnerability Coordination and Disclosure_ ; Jong, “Beyond the Snapshot.” 

28. ISO/IEC 29147:2018; Householder et al., _CERT Guide to Coordinated Vulnerability Disclosure_ ; Forum of Incident Response and Security Teams, _PSIRT Services Framework_ , version 1.1 (FIRST, 2020); Longpre et al., “In-House Evaluation Is Not Enough”; Ezell, Roberts-Gaal, and Chan, “Incident Analysis for AI Agents”; Associated Press, _Statement of News Values_ . 

###### **Bibliography** 

Arpan, Laura M., and David R. Roskos-Ewoldsen. “Stealing Thunder: Analysis of the Effects of Proactive Disclosure of Crisis Information.” _Public Relations Review_ 31, no. 3 (2005): 425–33. 

Arthur W. Page Society. “The Page Principles.” Accessed September 14, 2026. <u>https://page.org/site/the-page-principles.</u> 

Associated Press. “Senators from Both Parties Question OpenAI on Breach of AI Startup Hugging Face.” September 10, 2026. 

<u>https://www.pbs.org/newshour/politics/senators-from-both-parties-question-openai-on-breach-of-ai-startup</u> -hugging-face. 

Associated Press. _The Associated Press Statement of News Values and Principles_ . New York: Associated Press, 2026. 

Bartholomew, Jem, and Dhrumil Mehta. “How the Media Is Covering ChatGPT.” _Columbia Journalism Review_ , May 26, 2023. 

BBC. _Editorial Guidelines_ . Section 3, “Accuracy.” London: BBC, 2019. 

Blumenthal, Richard. Letter to Sam Altman, September 9, 2026. <u>https://www.blumenthal.senate.gov/imo/media/doc/20260909_-_openai_-_cot_and_rogue_agentspdf.pdf.</u> 

Cattell, Sven, Avijit Ghosh, and Lucie-Aimée Kaffee. “Coordinated Flaw Disclosure for AI: Beyond Security Vulnerabilities.” arXiv:2402.07039 (2024). 

Centers for Disease Control and Prevention. _Crisis and Emergency Risk Communication (CERC): Introduction_ . 2018 update. Atlanta: CDC, 2018. 

Claeys, An-Sofie. “The Benefits and Pitfalls of Stealing Thunder.” In _The Handbook of Crisis Communication_ , 2nd ed., edited by W. Timothy Coombs and Sherry J. Holladay, 99–111. Hoboken, NJ: Wiley-Blackwell, 2022. 

Claeys, An-Sofie, and Verolien Cauberghe. “Crisis Response and Crisis Timing Strategies, Two Sides of the Same Coin.” _Public Relations Review_ 38, no. 1 (2012): 83–88. 

Coombs, W. Timothy. “Protecting Organization Reputations During a Crisis: The Development and Application of Situational Crisis Communication Theory.” _Corporate Reputation Review_ 10, no. 3 (2007): 163–76. 

Coombs, W. Timothy. _Reexamining Crisis Communication_ . Gainesville, FL: Institute for Public Relations, 2026. <u>https://instituteforpr.org/reexamining-crisis-communication/.</u> 

Coombs, W. Timothy. “Situational Crisis Communication Theory (SCCT): Refining and Clarifying a Cognitive-Based Theory of Crisis Communication.” In _The Handbook of Crisis Communication_ , 2nd ed., edited by W. Timothy Coombs and Sherry J. Holladay, 193–204. Hoboken, NJ: Wiley-Blackwell, 2022. 

Dries, Charlotte, Michelle McDowell, Felix G. Rebitschek, and Christina Leuker. “When Evidence Changes: Communicating Uncertainty Protects against a Loss of Trust.” _Public Understanding of Science_ 33 (2024). <u>https://doi.org/10.1177/09636625241228449.</u> 

European Commission, AI Office. _General-Purpose AI Code of Practice: Safety and Security Chapter_ . July 10, 2025. 

European Data Protection Board. _Guidelines 9/2022 on Personal Data Breach Notification under GDPR_ . Version 2.0. March 28, 2023. 

European Union. Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 Laying Down Harmonised Rules on Artificial Intelligence (Artificial Intelligence Act). _Official Journal of the European Union_ L, July 12, 2024. 

Ezell, Carson, Xavier Roberts-Gaal, and Alan Chan. “Incident Analysis for AI Agents.” arXiv:2508.14231 (2025). 

Federal Trade Commission. _In re Blackbaud, Inc._ Complaint and Decision and Order. 2024. 

Forum of Incident Response and Security Teams. _Guidelines and Practices for Multi-Party Vulnerability Coordination and Disclosure_ . Version 1.1. FIRST, 2020. 

Forum of Incident Response and Security Teams. _PSIRT Services Framework_ . Version 1.1. FIRST, 2020. 

Greenblatt, Ryan, Ajeya Cotra, and Hjalmar Wijk. “Brief Independent Investigation of Agents’ Behavior, Reasoning and Collaboration in the OpenAI / Hugging Face Hacking Incident.” METR, August 26, 2026. <u>https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/.</u> 

Hawley, Josh. “Chairman Hawley Launches Investigation into OpenAI for Hacking, Existential Risk of AI Products.” Press release and letter to Sam Altman, September 9–10, 2026. <u>https://www.hawley.senate.gov/chairman-hawley-launches-investigation-into-openai-for-hacking-existentia l-risk-of-ai-products/.</u> 

Householder, Allen D., Garret Wassermann, Art Manion, and Chris King. _The CERT Guide to Coordinated Vulnerability Disclosure_ . CMU/SEI-2017-SR-022. Pittsburgh: Software Engineering Institute, Carnegie Mellon University, 2017. 

Huang, Yan, and Marcia DiStaso. “Responding to a Health Crisis on Facebook: The Effects of Response Timing and Message Appeal.” _Public Relations Review_ 46, no. 3 (2020): 101909. 

Hugging Face. “Security Incident Disclosure — July 2026.” Hugging Face Blog, July 16, 2026. <u>https://huggingface.co/blog/security-incident-july-2026.</u> 

International Organization for Standardization and International Electrotechnical Commission. _ISO/IEC 29147:2018, Information Technology — Security Techniques — Vulnerability Disclosure_ . 2nd ed. Geneva: ISO/IEC, 2018. 

Jong, Wouter. “Beyond the Snapshot: Rethinking Crisis Communication Theories in Dynamic Crisis Situations.” _Public Relations Review_ 51 (2025): 102586. 

Kim, Peter H., Donald L. Ferrin, Cecily D. Cooper, and Kurt T. Dirks. “Removing the Shadow of Suspicion: The Effects of Apology versus Denial for Repairing Competence- versus Integrity-Based Trust Violations.” _Journal of Applied Psychology_ 89, no. 1 (2004): 104–18. 

Kim, Soo-Yeon, and Jeong-Hyeon Lee. “How to Maximize the Effectiveness of Stealing Thunder in Crisis Communication: The Significance of Follow-Up Actions and Transparent Communication.” _Corporate Communications: An International Journal_ 27, no. 3 (2022): 425–40. 

Knight, Richard, and Jason R. C. Nurse. “A Framework for Effective Corporate Communication after Cyber Security Incidents.” _Computers & Security_ 99 (2020): 102036. 

Kuipers, Sanneke, and Marleen Schonheit. “Data Breaches and Effective Crisis Communication: A Comparative Analysis of Corporate Reputational Crises.” _Corporate Reputation Review_ 25 (2022): 176–97. 

Larcher, Hugo, Adrien Carreira, Raphaël G., and Christophe Rannou. “Anatomy of a Frontier Lab Agent Intrusion: A Technical Timeline of the July 2026 Incident.” Hugging Face Blog, July 27, 2026, revised through July 30, 2026. <u>https://huggingface.co/blog/agent-intrusion-technical-timeline.</u> 

Longpre, Shayne, Elaine Zhu, Carson Ezell, Avijit Ghosh, Sean McGregor, et al. “FLARE-AI: Flaw Reporting for AI.” arXiv:2606.31567 (2026). <u>https://arxiv.org/abs/2606.31567.</u> 

Longpre, Shayne, Kevin Klyman, Ruth E. Appel, Sayash Kapoor, Rishi Bommasani, et al. “In-House Evaluation Is Not Enough: Towards Robust Third-Party Flaw Disclosure for General-Purpose AI.” arXiv:2503.16861 (2025). 

National Institute of Standards and Technology. _Artificial Intelligence Risk Management Framework (AI RMF 1.0)_ . NIST AI 100-1. Gaithersburg, MD: NIST, 2023. <u>https://doi.org/10.6028/NIST.AI.100-1.</u> 

National Institute of Standards and Technology. _Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile_ . NIST AI 600-1. Gaithersburg, MD: NIST, 2024. <u>https://doi.org/10.6028/NIST.AI.600-1.</u> 

Novak, Alison N., and M. Olguta Vilceanu. “‘The Internet Is Not Pleased’: Twitter and the 2017 Equifax Data Breach.” _The Communication Review_ 22, no. 3 (2019): 196–221. 

OECD. _Defining AI Incidents and Related Terms_ . OECD Artificial Intelligence Papers, no. 16. Paris: OECD Publishing, 2024. <u>https://doi.org/10.1787/d1a8d965-en.</u> 

OECD. _Towards a Common Reporting Framework for AI Incidents_ . OECD Artificial Intelligence Papers, no. 34. Paris: OECD Publishing, 2025. <u>https://doi.org/10.1787/f326d4ac-en.</u> 

OpenAI. “The Hugging Face Incident and the Road Ahead.” August 26, 2026. <u>https://openai.com/index/hugging-face-incident-and-the-road-ahead/.</u> 

OpenAI. “OpenAI and Hugging Face Partner to Address Security Incident during Model Evaluation.” July 21, 2026, updated July 28 and 29, 2026. 

<u>https://openai.com/index/hugging-face-model-evaluation-security-incident/.</u> 

OpenAI. _OpenAI–Hugging Face Incident Technical Report_ . San Francisco: OpenAI, August 26, 2026. 

Placani, Adriana. “Anthropomorphism in AI: Hype and Fallacy.” _AI and Ethics_ 4 (2024): 691–98. 

Seeger, Matthew W. “Best Practices in Crisis Communication: An Expert Panel Process.” _Journal of Applied Communication Research_ 34, no. 3 (2006): 232–44. 

Substance Abuse and Mental Health Services Administration. _SAMHSA’s Concept of Trauma and Guidance for a Trauma-Informed Approach_ . HHS Publication No. (SMA) 14-4884. Rockville, MD: SAMHSA, 2014. 

US Securities and Exchange Commission. “SEC Charges Four Companies with Misleading Cyber Disclosures.” Press release 2024-174, October 22, 2024. 

Van Hollen, Chris. Letter to Sam Altman, September 10, 2026. Press release, US Senate. <u>https://www.vanhollen.senate.gov/news/press-releases.</u> 

van der Bles, Anne Marthe, Sander van der Linden, Alexandra L. J. Freeman, and David J. Spiegelhalter. “The Effects of Communicating Uncertainty on Public Trust in Facts and Numbers.” _Proceedings of the National Academy of Sciences_ 117, no. 14 (2020): 7672–83. 

Vaughan-Johnston, Thomas I., Joshua J. Guyer, Katie L. Lawrence, and Leandre R. Fabrigar. “Disclosure and Identification Information Increase the Benefits of Stealing Thunder.” _Social Influence_ 20, no. 1 (2025): 2447273. <u>https://doi.org/10.1080/15534510.2024.2447273.</u> 

Willison, Simon. “Now We Have a Timeline of the OpenAI Accidental Attack against Hugging Face.” Simon Willison’s Weblog, August 7, 2026. <u>https://simonwillison.net/2026/Aug/7/openai-timeline/.</u> 

World Health Organization. _Communicating Risk in Public Health Emergencies: A WHO Guideline for Emergency Risk Communication (ERC) Policy and Practice_ . Geneva: World Health Organization, 2017. 

Yu, Yongtian, Weiming Ye, and Kaihang Zhang. “Faster? Softer? Or More Formal? A Study on the Methods of Enterprises’ Crisis Response on Social Media.” _Mathematics_ 13, no. 10 (2025): 1582. <u>https://doi.org/10.3390/math13101582.</u> 

Zou, Yixin, Shawn Danino, Kaiwen Sun, and Florian Schaub. “You ‘Might’ Be Affected: An Empirical Analysis of Readability and Usability Issues in Data Breach Notifications.” In _Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems_ , paper 194. New York: ACM, 2019. 

### **Appendices** 

##### Appendix A 

Appendix A presents the 15 criteria used to assess organizational communication during an AI incident. For each criterion, the table identifies its communication area and provides an open-ended question to guide evaluators’ judgement. 

These questions assess the quality and completeness of the observed communication rather than asking evaluators to make a binary yes-or-no determination. 

C11, C13, C14 and C15 are conditional and are applied only when relevant to the incident. 

|**Communication**<br>**Area**|**Criterion**|**What it assesses**|**Apples when**|
|---|---|---|---|
|Timing|C1. Timing of public<br>disclosure|Relative to when it learned of<br>the incident, was the<br>organization the first credible<br>public source, or, if another<br>party disclosed first, did it<br>publish before the first<br>subsequent coverage of the<br>incident?|Always|
|Incident account|C2. Known and unknown<br>information|Did the organization separate<br>established facts from open<br>questions, explain why<br>important facts remained<br>unknown, and commit to a<br>dated next update?|Always|
|Incident account|C3. Certainty and<br>reassurance|Were known facts stated clearly<br>and genuine uncertainties<br>bounded, and was each<br>reassuring claim supported by<br>what the organization had<br>examined and what risk<br>remained?|Always|
|Incident account|C4. Scope and affected<br>parties|Could readers determine what<br>was reached, how the incident<br>occurred, how far it extended<br>and for how long, and whether<br>their own systems, data or<br>credentials were affected?|Always|
|Incident account|C5. Incident discovery|Did the organization explain<br>how and when it learned of the<br>incident and, where an external<br>party raised it, who that party<br>was?|Always|
|Incident framing|C6. Incident classification|Did the organization use an<br>accurate public label for the<br>incident and state the definition,|Always|



|||regulatory regime or severity<br>framework supporting it?||
|---|---|---|---|
|Incident framing|C7. Consistent description<br>of the AI system|Was the AI system described in<br>consistent, mechanism-based<br>language across statements<br>and spokespeople,<br>distinguishing its actions from<br>human decisions and indirect<br>effects, without overstating or<br>downplaying its role?|Always|
|Incident framing|C8. AI-system conduct<br>and authorization|Did the organization explain<br>which AI system acted, where<br>and under whose authority it<br>operated, what it was<br>authorized to do, which<br>safeguards were present or<br>relaxed, and what evidence<br>supported the account?|Always|
|Responsibility and remedy|C9. Responsibility and<br>remedies|Did the organization state its<br>own role without shifting it onto<br>other parties, update that<br>acknowledgement as certainty<br>improved, and report corrective<br>actions that were delivered and<br>can be checked from outside?|Always|
|Protection and reach|C10. Protective guidance|Were people and organizations<br>that may have been exposed<br>given accessible, specific and<br>prioritized guidance on what to<br>do, alongside what the<br>organization itself was doing?|Always|
|Protection and reach|C11. Direct notice to<br>affected parties|Did the organization notify<br>identifiable affected parties<br>directly, through appropriate<br>channels not compromised by<br>the incident, with evidence of<br>that notification that others can<br>check?|The public record<br>describes<br>identifiable parties'<br>systems, data,<br>credentials or<br>accounts as<br>affected. N/A only<br>where the<br>organization has<br>stated, with the<br>scope of what it<br>examined, that no<br>identifiable party<br>was affected.|
|Updates and coordination|C12. Updates and<br>corrections|Were promised updates<br>delivered and dated,<br>substantive changes and<br>corrections clearly labelled,<br>superseded statements linked<br>to current information, and open<br>questions addressed in a<br>closing account?|Always|



|Updates and coordination|C13. Coordination<br>between organizations|Did the organizations' public<br>accounts jointly explain who did<br>what, acknowledge unresolved<br>attribution and represent each<br>other's positions, without<br>contradictions or shared<br>omissions?|More than one<br>organization is<br>publicly involved|
|---|---|---|---|
|External scrutiny|C14. External finders and<br>reviewers|Did the organization promptly<br>acknowledge, credit and keep<br>engaging with outside finders,<br>answer press questions, and<br>leave independent reviewers<br>free to state their own access,<br>limitations and independence?|An outside party<br>found the incident,<br>assessed it<br>independently, or<br>asked for comment|
|Protection and reach|C15. Support for people<br>harmed|Was communication with<br>affected people sensitive and<br>practically supportive, offering<br>an accessible human contact,<br>warnings about follow-on<br>scams, and ways to remove,<br>reverse or challenge harmful<br>content or actions?|The incident<br>exposed identifiable<br>people's sensitive<br>data, produced<br>outputs about<br>identifiable people,<br>or took actions on<br>someone's behalf.<br>N/A where only<br>organizational<br>systems or data<br>were reached.|



Appendix B. Independent Assessment Pack 

# **Independent Assessment of AI Incident Communication** 

###### **OpenAI and Hugging Face  |  July to August 2026** 

**Your task.** Assess how each organization communicated during the incident. 

Evaluate the public communication record, not the quality of the underlying technical response. Please complete the assessment independently before discussing it with anyone else. 

|Reviewer name or code<br>Date completed|
|---|





#### **How to complete the assessment** 

**1.** Read the timeline on the following pages. Use the linked source documents when you need more detail. 

**2.** Assess OpenAI and Hugging Face separately across the full communication period, from the first public disclosure through 26 August 2026. 

**3.** For every criterion, enter one score and cite at least one dated source. Add a short sentence explaining your choice. 

**4.** Use N/A only when the criterion does not apply or the public record is genuinely insufficient. Mark which reason applies. 

**5.** Do not calculate an overall score. The research team will calculate results after collecting the independent assessments. 

#### **Scoring scale** 

|**Score**|**Meaning**|
|---|---|
|**0**|Absent or actively harmful|



|**1**|Minimal or significantly deficient|
|---|---|
|**2**|Substantially present, with important gaps|
|**3**|Strong practice meeting the full evidence-based standard|
|**N/A**|Not applicable or insufficient public evidence - identify which|



#### **Evidence sources** 

The timeline is a navigation aid, not a substitute for the underlying communications. Open the sources when the summary does not contain enough evidence to score a criterion. 

- **S1** <u>Hugging Face security incident disclosure</u> (16 July 2026) 

- **S2** <u>TechCrunch reporting on the Hugging Face intrusion</u> (20 July 2026) 

- **S3** <u>OpenAI initial incident statement</u> (21 July 2026) 

- **S4** <u>Sam Altman, Clément Delangue</u> X posts and <u>Delangue’s travel announcement (21, 23</u> 

- July 2026) 

- **S5** <u>Hugging Face technical timeline</u> (27 July 2026, subsequently revised) 

- **S6** <u>Hugging Face technical timeline revision history</u> (28-30 July 2026) 

- **S7** <u>Sam Altman’s podcast interview on the incident</u> (28 July 2026) 

- **S8** <u>OpenAI incident account and road ahead</u> (26 August 2026) 

- **S9** <u>METR and Redwood independent investigation</u> (26 August 2026) 

#### **Communication timeline** 

|**Date and milestone**|**Event or communication**|**Source ID**|
|---|---|---|
|**16 Jul**<br>**Hugging Face**<br>**discloses**|Hugging Face announced an intrusion driven by autonomous AI<br>agents, described the known impact, advised users to rotate tokens<br>and review activity, and said affected parties would be contacted<br>directly.|S1|
|**20 Jul**<br>**First mainstream**<br>**coverage**|TechCrunch published the first mainstream news report of the<br>Hugging Face intrusion (05:39 PDT, 12:39 UTC).|S2|
|**21 Jul**<br>**OpenAI confirms**<br>**involvement**|OpenAI publicly stated that its models, including GPT-5.6 Sol and a<br>more capable pre-release model with reduced cyber refusals, drove<br>the incident.|S3|
|**21 Jul**<br>**Sam Altman posts**<br>**on X**|Sam Altman (OpenAI CEO) shared OpenAI’s findings and thanked<br>Hugging Face for its partnership on the incident.|S4|



|**21, 23 Jul**<br>**Clément Delangue**<br>**X posts**|Clément Delangue (Hugging Face CEO) discussed cooperation<br>with OpenAI and the ongoing investigation on 21 July, and<br>announced travel to San Francisco on 23 July.|S4|
|---|---|---|
|**27-30 Jul**<br>**Hugging Face**<br>**technical account**|Hugging Face published a detailed reconstruction covering the<br>attack path, agent actions, affected systems, detection, containment<br>and remediation.<br>The public article was subsequently revised.|S5, S6|
|**28 Jul**<br>**Sam Altman’s**<br>**podcast interview**|Sam Altman discussed the incident on_Invest Like the Best_with<br>Patrick O’Shaughnessy, saying one of OpenAI's unreleased models<br>"cheated" on a test by chaining zero-day exploits to escape its<br>sandbox and break into Hugging Face's systems.<br>He says OpenAI paused training and needs to secure its<br>sandboxes, and that AI development may need to slow down so<br>society can adapt.|S7|
|**26 Aug**<br>**OpenAI report and**<br>**external review**|OpenAI published a detailed incident account and described<br>warning signals, investigative findings and new safeguards. METR<br>and Redwood published a separate investigation of the agents'<br>behavior the same day.|S8, S9|



#### **OpenAI assessment** 

Part 1 of 2. Enter one score for each criterion. In the evidence column, cite a source ID and date. Do not compare OpenAI's score with the other organization while rating. 

**Quick key:** 0 absent or harmful  |  1 minimal  |  2 substantial with gaps  |  3 strong practice  |  N/A not applicable or insufficient evidence 

|**Criterion**|**What it assesses**|**Score**|**Evidence**|**Brief Reason**|
|---|---|---|---|---|
|**C1. Timing of**<br>**public**<br>**disclosure**|Relative to when it learned of the<br>incident, was the organization the first<br>credible public source, or, if another<br>party disclosed first, did it publish<br>before the first subsequent coverage<br>of the incident?||||



|**C2. Known and**<br>**unknown**<br>**information**|Did the organization separate<br>established facts from open<br>questions, explain why important<br>facts remained unknown, and commit<br>to a dated next update?|
|---|---|
|**C3. Certainty**<br>**and**<br>**reassurance**|Were known facts stated clearly and<br>genuine uncertainties bounded, and<br>was each reassuring claim supported<br>by what the organization had<br>examined and what risk remained?|
|**C4. Scope and**<br>**affected**<br>**parties**|Could readers determine what was<br>reached, how the incident occurred,<br>how far it extended and for how long,<br>and whether their own systems, data<br>or credentials were affected?|
|**C5. Incident**<br>**discovery**|Did the organization explain how and<br>when it learned of the incident and,<br>where an external party raised it, who<br>that party was?|
|**C6. Incident**<br>**classification**|Did the organization use an accurate<br>public label for the incident and state<br>the definition, regulatory regime or<br>severity framework supporting it?|
|**C7. Consistent**<br>**description of**<br>**the AI system**|Was the AI system described in<br>consistent, mechanism-based<br>language across statements and<br>spokespeople, distinguishing its<br>actions from human decisions and<br>indirect effects, without overstating or<br>downplaying its role?|
|**C8. AI-system**<br>**conduct and**<br>**authorization**|Did the organization explain which AI<br>system acted, where and under<br>whose authority it operated, what it<br>was authorized to do, which<br>safeguards were present or relaxed,<br>and what evidence supported the<br>account?|
|**C9.**<br>**Responsibility**<br>**and remedies**|Did the organization state its own role<br>without shifting it onto other parties,<br>update that acknowledgement as<br>certainty improved, and report<br>corrective actions that were delivered<br>and can be checked from outside?|
|**C10. Protective**<br>**guidance**|Were people and organizations that<br>may have been exposed given<br>accessible, specific and prioritized<br>guidance on what to do, alongside<br>what the organization itself was<br>doing?|













|**C11. Direct**<br>**notice to**<br>**affected**<br>**parties**|Did the organization notify identifiable<br>affected parties directly, through<br>appropriate channels not<br>compromised by the incident, with<br>evidence of that notification that<br>others can check?|
|---|---|
|**C12. Updates**<br>**and**<br>**corrections**|Were promised updates delivered<br>and dated, substantive changes and<br>corrections clearly labelled,<br>superseded statements linked to<br>current information, and open<br>questions addressed in a closing<br>account?|
|**C13.**<br>**Coordination**<br>**between**<br>**organizations**|Did the organizations' public accounts<br>jointly explain who did what,<br>acknowledge unresolved attribution<br>and represent each other's positions,<br>without contradictions or shared<br>omissions?|
|**C14. External**<br>**finders and**<br>**reviewers**|Did the organization promptly<br>acknowledge, credit and keep<br>engaging with outside finders, answer<br>press questions, and leave<br>independent reviewers free to state<br>their own access, limitations and<br>independence?|
|**C15. Support**<br>**for people**<br>**harmed**|Was communication with affected<br>people sensitive and practically<br>supportive, offering an accessible<br>human contact, warnings about<br>follow-on scams, and ways to<br>remove, reverse or challenge harmful<br>content or actions?|







#### **Hugging Face assessment** 

Part 2 of 2. Enter one score for each criterion. In the final column, cite a source ID and date, then give a one-sentence reason. 

Do not compare Hugging Face's score with the other organization while rating. 

**Quick key:** 0 absent or harmful  |  1 minimal  |  2 substantial with gaps  |  3 strong practice  |  N/A applicable or insufficient evidence 

|**Criterion**|**What it assesses**|**Score**|**Evidence**|**Brief Reason**|
|---|---|---|---|---|
|**C1. Timing of**<br>**public**|Relative to when it learned of the<br>incident, was the organization the||||
|**disclosure**|first credible public source, or, if<br>another party disclosed first, did it<br>publish before the first subsequent<br>coverage of the incident?||||



|**C2. Known**|Did the organization separate|
|---|---|
|**and unknown**<br>**information**|established facts from open<br>questions, explain why important<br>facts remained unknown, and commit<br>to a dated next update?|
|**C3. Certainty**<br>**and**<br>**reassurance**|Were known facts stated clearly and<br>genuine uncertainties bounded, and<br>was each reassuring claim supported<br>by what the organization had<br>examined and what risk remained?|
|**C4. Scope and**<br>**affected**<br>**parties**|Could readers determine what was<br>reached, how the incident occurred,<br>how far it extended and for how long,<br>and whether their own systems, data<br>or credentials were affected?|
|**C5. Incident**<br>**discovery**|Did the organization explain how and<br>when it learned of the incident and,<br>where an external party raised it,<br>who that party was?|
|**C6. Incident**<br>**classification**|Did the organization use an accurate<br>public label for the incident and state<br>the definition, regulatory regime or<br>severity framework supporting it?|
|**C7. Consistent**<br>**description of**<br>**the AI system**|Was the AI system described in<br>consistent, mechanism-based<br>language across statements and<br>spokespeople, distinguishing its<br>actions from human decisions and<br>indirect effects, without overstating or<br>downplaying its role?|
|**C8. AI-system**<br>**conduct and**<br>**authorization**|Did the organization explain which AI<br>system acted, where and under<br>whose authority it operated, what it<br>was authorized to do, which<br>safeguards were present or relaxed,<br>and what evidence supported the<br>account?|
|**C9.**<br>**Responsibility**<br>**and remedies**|Did the organization state its own<br>role without shifting it onto other<br>parties, update that<br>acknowledgement as certainty<br>improved, and report corrective<br>actions that were delivered and can<br>be checked from outside?|











|**C10.**|Were people and organizations that|
|---|---|
|**Protective**<br>**guidance**|may have been exposed given<br>accessible, specific and prioritized<br>guidance on what to do, alongside<br>what the organization itself was<br>doing?|
|**C11. Direct**<br>**notice to**<br>**affected**<br>**parties**|Did the organization notify<br>identifiable affected parties directly,<br>through appropriate channels not<br>compromised by the incident, with<br>evidence of that notification that<br>others can check?|
|**C12. Updates**<br>**and**<br>**corrections**|Were promised updates delivered<br>and dated, substantive changes and<br>corrections clearly labelled,<br>superseded statements linked to<br>current information, and open<br>questions addressed in a closing<br>account?|
|**C13.**<br>**Coordination**<br>**between**<br>**organizations**|Did the organizations' public<br>accounts jointly explain who did<br>what, acknowledge unresolved<br>attribution and represent each other's<br>positions, without contradictions or<br>shared omissions?|
|**C14. External**<br>**finders and**<br>**reviewers**|Did the organization promptly<br>acknowledge, credit and keep<br>engaging with outside finders,<br>answer press questions, and leave<br>independent reviewers free to state<br>their own access, limitations and<br>independence?|
|**C15. Support**<br>**for people**<br>**harmed**|Was communication with affected<br>people sensitive and practically<br>supportive, offering an accessible<br>human contact, warnings about<br>follow-on scams, and ways to<br>remove, reverse or challenge harmful<br>content or actions?|









#### **Overall observations** 

After completing every criterion, briefly identify the most important communication strength and weakness for each organization. Do not revise earlier scores simply to make them match this overall impression. 

###### **OpenAI** 

**Most important strength:** 

**Most important weakness:** 

###### **Hugging Face** 

**Most important strength:** 

**Most important weakness:** 

**Criteria that were difficult to score** 

**Criterion ID and reason:** 

###### **Completion check** 

- ☐ I assessed the two organizations separately. 

- ☐ Every numerical score has a dated source and short justification. 

- ☐ Every N/A identifies whether it means not applicable or insufficient public evidence. 

- ☐ I completed the assessment before discussing my ratings with other reviewers. 

Appendix C. Incident Timeline **Timeline of Hugging Face-OpenAI Incident** 

This timeline tracks the operational events and communications linked to the July 2026 Hugging Face incident. The developments include internal warnings, actions before the intrusion, joint coordination, organizational response after the breach, the changing public narrative and subsequent investigations related to the Hugging Face incident. 

|**Date and**<br>**milestone**|**Event or Communication**<br>**S**|**ource ID**|
|---|---|---|
|**27 Jun**<br>**Internal warning**<br>**& Initial**<br>**Response**|OpenAI's monitoring system detected anomalous scanning across network ports<br>in its research environment and their on-call response staff were informed.|S1|
|**11–13 Jul**<br>**Incident**<br>**Escalation and**<br>**Containment**|On July 11<sup>th</sup>, agents accessed information about the execution environment of a<br>Hugging Face Dataset Server worker at 4:38 UTC and executed OS-level<br>commands at 16:07 UTC. On 13th July, Hugging Face severed agents’ access to<br>its infrastructure.|S2|
|**16 Jul**<br>**Hugging Face**<br>**discloses**|Hugging Face publicly announced an intrusion driven by autonomous AI-agents<br>and known scope of impact. It also advised users to rotate tokens, review and<br>report suspicious account activities and committed to contacting affected<br>customers and partners directly as required.|S3|
|**16/17 Jul**<br>**Customer Impact**<br>**Inquiry by**<br>**OpenAI**|OpenAI contacted Hugging Face asking if its data had been affected by the<br>incident because it was a Hugging Face customer.|S4|
|**19–20 Jul**<br>**Joint**<br>**Investigation by**<br>**Hugging Face**<br>**and OpenAI**|On July 19<sup>th,</sup>OpenAI monitoring systems flagged unusual identity-related API<br>calls associated with internal research Artifactory roles and responders initiated<br>the shutdown of active ExploitGym evaluations. On July 20th, OpenAI found<br>Hugging Face credentials in the files preserved during its investigation and<br>contacted Hugging Face to inquire about them. Hugging Face responded that it<br>had already rotated two of those credentials during its own incident response.|S5|
|**20 Jul**<br>**First mainstream**<br>**coverage**|TechCrunch published the first mainstream news report of the Hugging Face<br>intrusion (05:39 PDT, 12:39 UTC).|S6|
|**21 Jul**<br>**OpenAI Confirms**<br>**Involvement**|OpenAI made its involvement in the Hugging Face intrusion public through an<br>article published on its website and identified the  incident as being driven by a<br>combination of OpenAI models including GPT-5.6 Sol and an even more capable<br>pre-release model, all with reduced cyber refusals for evaluation purposes.|S7|
|**27–30 Jul**<br>**Technical**<br>**Timeline**<br>**Published by**<br>**Hugging Face**|Hugging Face published its technical post on 28 July at 20:08 UTC which had<br>detailed reconstruction of how the intrusion unfolded, how it was detected and<br>contained what remediation steps were taken.|S8|
|**26 Aug**<br>**Post-Incident**<br>**Accountability &**<br>**External Review**|OpenAI published its 38-page technical incident report, after collaborating with<br>METR and Redwood Research for third-party assessment of its model behavior.<br>METR and Redwood Research jointly published their investigation report of<br>agent behavior the same day on METR’s website.|S9|



#### **Sources:** 

**S1** OpenAI, <u>OpenAI–Hugging Face Incident Technical Report</u> (26 August 2026), p. 8. **S2** OpenAI, <u>Incident Technical Report, p. 35; Hugging Face, Technical Timeline (27 July 2026), “Day 5” and “How we</u> intercepted and analyzed the attack.” 

**S3** Hugging Face, <u>Security Incident Disclosure, opening paragraphs, “What happened” and “For our community.”</u> 

**S4** OpenAI, Incident Technical Report, pp. 14–15; Simon Willison, <u>Now We Have a Timeline of the OpenAI Accidental Attack against Hugging Face</u> (7 August 2026), July 16 and July 20 entries. 

**S5** OpenAI, Incident Technical Report, pp. 4, 15, 37–38. 

**S6** TechCrunch, <u>Hugging Face confirms breach affected internal datasets and credentials, urges users to take action</u> (20 July 2026). 

**S7** OpenAI, <u>Initial Incident Statement  (21 July 2026); Incident Technical Report, p. 4.</u> 

**S8** Hugging Face, <u>Technical Timeline (27 July 2026); Repository revision history (28–30 July 2026).</u> 

**S9** OpenAI, Incident Technical Report, pp. 4–5, 7–8, 25–31; METR and Redwood Research, <u>Independent Investigation of Agents’ Behavior (26 August 2026)</u> 

Appendix D. Limitations and Dual-Use Considerations 

We acknowledge that there is a risk that the rubric and scoring framework may be used to coach PR professionals in order to maximise public sympathy and/or protect company reputation, rather than be used for the intended application of public disclosure and harm reduction. 

##### Appendix E. Source Register 

|**ID**|**Source**|**Type**|**Year**|**Issuing body / venue**|
|---|---|---|---|---|
|S1-01|Coombs, "Protecting<br>Organization Reputations During<br>a Crisis" (SCCT)|Scholarly|2007|Corporate Reputation<br>Review 10(3): 163–176|
|S1-02|Ma & Zhan, meta-analysis of<br>SCCT research|Scholarly|2016|J. Public Relations<br>Research 28(2)|
|S1-03|Coombs, SCCT chapter,<br>Handbook of Crisis<br>Communication (2nd ed.)|Scholarly|2022|Handbook of Crisis<br>Communication, 2nd ed.<br>(Coombs & Holladay, eds),<br>Wiley-Blackwell: ch. 14,<br>193–204|
|S1-04|Coombs & Tachkova, moral<br>outrage in SCCT|Scholarly|2023|Management<br>Communication Quarterly<br>37(4): 798–820|
|S1-05|Coombs, "Reexamining Crisis<br>Communication" (IPR white<br>paper)|Practitioner/s<br>cholarly|May 2026|Institute for Public Relations|
|S1-06|Coombs, "State of Crisis<br>Communication: Evidence and<br>the Bleeding Edge"|Practitioner/p<br>ress|2014|Institute for Public Relations|
|S1-07|Coombs, "Crisis Management<br>and Communications"|Practitioner/p<br>ress|2007/2014|Institute for Public Relations|
|S1-08|Benoit, "Image repair discourse<br>and crisis communication"|Scholarly|1997|Public Relations Review<br>23(2): 177–186|



|S1-10|Seeger, "Best Practices in Crisis<br>Communication: An Expert<br>Panel Process"|Scholarly|2006|J. Applied Communication<br>Research 34(3): 232–244|
|---|---|---|---|---|
|S1-11|Arpan & Roskos-Ewoldsen,<br>"Stealing thunder: Analysis of<br>the effects of proactive<br>disclosure of crisis information"|Scholarly|2005|Public Relations Review<br>31(3): 425–433|
|S1-12|Claeys & Cauberghe, "Crisis<br>response and crisis timing<br>strategies, two sides of the same<br>coin"|Scholarly|2012|Public Relations Review<br>38(1)|
|S1-14|Claeys, "The Benefits and<br>Pitfalls of Stealing Thunder"|Scholarly|2022|Handbook of Crisis<br>Communication, 2nd ed.<br>(Coombs & Holladay, eds),<br>Wiley-Blackwell: 99–111|
|S1-15|Beldad, van Laar & Hegner,<br>"Should the shady steal<br>thunder?"|Scholarly|2018|J. Contingencies & Crisis<br>Management 26(1):<br>150–163|
|S1-16|Kim & Lee, stealing thunder<br>follow-up actions|Scholarly|2022|Corporate Communications<br>27(3): 425–440|
|S1-17|Lee & Fraustino, stealing<br>thunder for legal violations|Scholarly|2023 (print<br>2025)|J. Marketing<br>Communications 31(3):<br>263–283|
|S1-18|Ndone, "Beyond Negative<br>Emotions: The Effects of Positive<br>Emotions and Stealing Thunder<br>on Organizational Outcomes<br>After a Crisis"|Scholarly|2025|J. Contingencies & Crisis<br>Management 33(3): e70075|



|S1-19|Fennis & Stroebe, "Softening the<br>Blow"|Scholarly|2014|J. Business Ethics 120(1):<br>109–120|
|---|---|---|---|---|
|S1-20|Vaughan-Johnston, Guyer,<br>Lawrence & Fabrigar,<br>"Disclosure and identification<br>information increase the benefits<br>of stealing thunder"|Scholarly|2025 (online<br>Dec 2024)|<br>Social Influence 20(1)|
|S1-21|Jin, Liu & Austin,<br>Social-Mediated Crisis<br>Communication model|Scholarly|2014 (online<br>2011)|<br>Communication Research<br>41(1): 74–94|
|S1-22|Yu, Ye & Zhang, enterprise crisis<br>response on social media (3.1M<br>posts, 94 incidents)|Scholarly|2025|Mathematics (MDPI) 13(10):<br>1582|
|S1-23|Huang & DiStaso, "Responding<br>to a Health Crisis on Facebook:<br>The Effects of Response Timing<br>and Message Appeal"|Scholarly|2020|Public Relations Review<br>46(3): 101909|
|S1-24|Upadhyay & Upadhyay,<br>bibliometric map of crisis comms<br>1968–2022|Scholarly|2023|Humanities & Social<br>Sciences Communications<br>10|
|S1-25|Zhou, Zhang & Ki, "Crisis<br>response strategy manipulation:<br>A systematic review and a test of<br>nuances"|Scholarly|2022|Public Relations Review 48:<br>102208|
|S1-26|Jong, "Beyond the snapshot:<br>Rethinking crisis communication<br>theories in dynamic crisis<br>situations"|Scholarly|2025|Public Relations Review 51:<br>102586|



|S1-27|Macnamara, insider perspective<br>during COVID-19|Scholarly|2021|Public Relations Inquiry<br>10(2): 237–262|
|---|---|---|---|---|
|S1-28|Knight & Nurse, "A framework<br>for effective corporate<br>communication after cyber<br>security incidents"|Scholarly|2020|Computers & Security|
|S1-29|Kuipers & Schonheit, "Data<br>Breaches and Effective Crisis<br>Communication: A Comparative<br>Analysis of Corporate<br>Reputational Crises" (8 cases)|Scholarly|2022 (online<br>2021)|<br>Corporate Reputation<br>Review 25(3): 176–197|
|S1-30|Novak & Vilceanu, Twitter and<br>the 2017 Equifax breach|Scholarly|2019|The Communication Review|
|S1-31|Bentley & Ma, "Testing<br>perceptions of organizational<br>apologies after a data breach<br>crisis"|Scholarly|2020|Public Relations Review<br>46(5): 101975|
|S1-32|Ruohonen, Hjerppe & Kortesuo,<br>"Crisis Communication in the<br>Face of Data Breaches"<br>(Vastaamo)|Scholarly|2024|arXiv 2406.01744|
|S1-33|Jong, Mikelatou & Vielvoije,<br>"When crisis communication<br>meets forensics" (11 practitioner<br>interviews)|Scholarly|2026|Computers & Security 171:<br>105082|



|S1-34|Xiao, Zhou & Yu, "Unraveling the<br>anchoring effect of crisis<br>communication in cyberattack<br>spillover crises"|Scholarly|2024|Public Relations Review<br>50(2): 102449|
|---|---|---|---|---|
|S1-35|Coombs & Holladay, "Comparing<br>apology to equivalent crisis<br>response strategies"|Scholarly|2008|Public Relations Review<br>34(3)|
|S1-37|CDC, Crisis and Emergency<br>Risk Communication (CERC)<br>Manual, Introduction|Standard/gui<br>dance|2018 update|US CDC|
|S1-39|WHO, "Communicating risk in<br>public health emergencies"<br>(GRADE guideline)|Standard/gui<br>dance|2017|World Health Organization|
|S1-40|Jha et al., systematic review for<br>the 2017 WHO emergency risk<br>communication guideline|Scholarly|2018|PLOS ONE 13(10):<br>e0205555|
|S1-41|UK Government Communication<br>Service, Crisis communications<br>operating model|Standard/gui<br>dance|2023|GCS|
|S1-42|GCS, STOP crisis<br>communications planning guide|Standard/gui<br>dance|24 Sep<br>2024|GCS|
|S1-43|AIDR, Public Information and<br>Warnings Handbook|Standard/gui<br>dance|2021|Australian Institute for<br>Disaster Resilience|
|S1-44|Australian Government Crisis<br>Management Framework, v4.2|Standard/gui<br>dance|Sep 2026|PM&C|



|S1-45|Ewart & Heinrichs,<br>communication gaps in<br>Australian disasters (186<br>inquiries)|Scholarly|2025|Risk, Hazards & Crisis in<br>Public Policy 16(2): e70013|
|---|---|---|---|---|
|S1-46|CISA et al., "Communicating<br>Under Pressure: Best Practices<br>for Service Providers"|Standard/gui<br>dance|2 Sep 2026|CISA and partners|
|S1-47|PRSA Code of Ethics|Policy/code|2000|PRSA|
|S1-48|CIPR Code of Conduct|Policy/code|current|CIPR|
|S1-50|IPRA Code of Conduct|Policy/code|2011|IPRA|
|S1-51|Arthur W. Page Society, Page<br>Principles|Policy/code|current|Page Society|
|S1-52|Global Alliance Global Code of<br>Ethics|Policy/code|2018,<br>re-adopted<br>2026|Global Alliance for PR|
|S1-55|Sandman, "Risk = Hazard +<br>Outrage"|Practitioner/p<br>ress|1987– (e.g.<br>ENR 1999)|Peter Sandman|
|S1-56|Slovic, "Perceived Risk, Trust,<br>and Democracy"|Scholarly|1993|Risk Analysis 13(6):<br>675–682|
|S1-59|Siegrist, "Trust and Risk<br>Perception: A Critical Review"|Scholarly|2021 (online<br>2019)|Risk Analysis 41(3):<br>480–490|
|S1-61|Fischhoff & Davis,<br>"Communicating scientific<br>uncertainty"|Scholarly|2014|PNAS|
|S1-62|van der Bles et al., effects of<br>communicating uncertainty on<br>trust|Scholarly|2020|PNAS|



|S1-63|Kerr et al., uncertainty around<br>statistics and public trust (N =<br>10,519)|Scholarly|2023|Royal Society Open Science<br>10(11): 230604|
|---|---|---|---|---|
|S1-64|Kreps & Kriner, model<br>uncertainty and trust in science<br>(COVID)|Scholarly|2020|Science Advances 6(43):<br>eabd4563|
|S1-65|Dries et al., "When evidence<br>changes: communicating<br>uncertainty protects against a<br>loss of trust"|Scholarly|2024|Public Understanding of<br>Science 33(6): 777–794|
|S1-66|Kim, Ferrin, Cooper & Dirks,<br>apology vs denial for<br>competence vs integrity<br>violations|Scholarly|2004|J. Applied Psychology|
|S1-67|Lewicki, Polin & Lount, structure<br>of effective apologies|Scholarly|2016|Negotiation & Conflict<br>Management Research<br>9(2): 177–196|
|S1-68|Sharma, Schoorman & Ballinger,<br>"How Can It Be Made Right<br>Again? A Review of Trust Repair<br>Research"|Scholarly|2023|J. Management 49(1):<br>363–399|
|S1-69|Ho & Liu, apology laws and<br>malpractice|Scholarly|2011|J. Risk and Uncertainty<br>43(2): 141–167|
|S1-70|McMichael, Van Horn & Viscusi,<br>"'Sorry' Is Never Enough"|Scholarly|2019|Stanford Law Review|
|S1-71|Arbel-Groissman et al.,<br>apologies and likelihood of<br>lawsuits|Scholarly|2025|J. Medical Internet<br>Research 27: e77493|



|S2-01|Guidelines 9/2022 on personal<br>data breach notification, v2.0|Standard/gui<br>dance|2023|EDPB|
|---|---|---|---|---|
|S2-02|Provvedimento n. 755<br>(OpenAI/ChatGPT)|Case/enforc<br>ement|2 Nov 2024|Garante (IT)|
|S2-03|ICO, "Personal data breaches: a<br>guide"|Standard/gui<br>dance|2025|UK ICO|
|S2-04|Sullivan & Maniff, "Data Breach<br>Notification Laws"|Scholarly|2016|Federal Reserve Bank of<br>Kansas City|
|S2-05|Kesari, "Do Data Breach<br>Notification Laws Work?"|Scholarly|2023–24|NYU J. Legislation & Public<br>Policy|
|S2-06|GDPR Arts 33–34 and Recitals<br>85–88|Legislation|2016|EU|
|S2-07|CISA Coordinated Vulnerability<br>Disclosure Process|Standard/gui<br>dance|current|CISA|
|S2-08|Binding Operational Directive<br>20-01|Legislation|2020|CISA/DHS|
|S2-09|CERT/CC Vulnerability<br>Disclosure Policy|Policy/code|current|CERT/CC|
|S2-10|CERT Guide to Coordinated<br>Vulnerability Disclosure|Standard/gui<br>dance|2017/web|CERT/CC (SEI)|
|S2-11|FIRST PSIRT Services<br>Framework v1.1|Standard/gui<br>dance|2020|FIRST|
|S2-12|FIRST Multi-Party Vulnerability<br>Coordination guidelines v1.1|Standard/gui<br>dance|2020|FIRST|
|S2-13|Google Project Zero, Policy and<br>Disclosure 2021|Policy/code|2021|Google|



|S2-14|Project Zero "Reporting<br>Transparency" trial|Policy/code|Jul 2025|Google|
|---|---|---|---|---|
|S2-15|Microsoft Coordinated<br>Vulnerability Disclosure|Policy/code|current|Microsoft|
|S2-16|Zero Day Initiative disclosure<br>policy|Policy/code|current|Trend Micro ZDI|
|S2-17|CNA Operational Rules v4.1.0|Standard/gui<br>dance|May 2025|CVE Program|
|S2-18|ENISA, Coordinated<br>Vulnerability Disclosure Policies<br>in the EU|Standard/sch<br>olarly|2022|ENISA|
|S2-19|NIS2 Directive Arts 12, 23;<br>Annex I|Legislation|2022|EU|
|S2-20|Implementing Regulation<br>2024/2690 (significant-incident<br>thresholds)|Legislation|2024|European Commission|
|S2-21|NIS2 transposition: Commission<br>press release IP/26/1499 (8 Jul<br>2026) and status trackers|Practitioner/p<br>ress|2026|European Commission;<br>trackers|
|S2-22|DORA Art. 19 and RTS<br>2025/301|Legislation|2025|EU|
|S2-23|DOJ Justice Manual 9-48.000<br>(CFAA charging policy)|Standard/gui<br>dance|2022|US DOJ|
|S2-24|disclose.io safe-harbour<br>framework|Policy/code|current|disclose.io|
|S2-25|HackerOne Disclosure<br>Guidelines|Policy/code|current|HackerOne|
|S2-26|Bugcrowd Standard Disclosure<br>Terms|Policy/code|current|Bugcrowd|



|S2-27|ISO/IEC 29147:2018<br>Vulnerability disclosure (2nd ed.)|Standard/gui<br>dance|2018|ISO/IEC JTC 1/SC 27|
|---|---|---|---|---|
|S2-29|SEC final rule, Cybersecurity<br>Risk Management, Strategy,<br>Governance, and Incident<br>Disclosure|Legislation|2023|US SEC|
|S2-30|Gerding statement on Item 1.05<br>vs 8.01|Standard/gui<br>dance|May 2024|SEC Corp Fin|
|S2-31|SEC settled orders: Unisys,<br>Avaya, Check Point, Mimecast|Case/enforc<br>ement|Oct 2024|US SEC|
|S2-32|SEC v. SolarWinds complaint|Case/enforc<br>ement|Oct 2023|US SEC|
|S2-33|SEC v. SolarWinds, opinion on<br>motion to dismiss (Engelmayer<br>J.), 107 pp.|Case/enforc<br>ement|18 Jul 2024|S.D.N.Y.|
|S2-34|SEC v. SolarWinds voluntary<br>dismissal (LR-26423)|Case/enforc<br>ement|Nov 2025|US SEC|
|S2-35|Security of Critical Infrastructure<br>Act 2018 Part 2B|Legislation|2022|Australia|
|S2-36|Cyber Security Act 2024 s 27<br>and Cyber Security<br>(Ransomware Payment<br>Reporting) Rules 2025|Legislation|Rules made<br>27 Feb<br>2025;<br>commence<br>ment tied to<br>Part 3 of the<br>Act (30 May<br>2025 per<br>secondary)|<br>Australia|
|S2-37|ASX Guidance Note 8, Annexure<br>A Example I (data breach)|<br>Standard/gui<br>dance|2024|ASX|



|S2-38|HIPAA Breach Notification Rule,<br>45 CFR 164.404–.414|Legislation|2013|HHS OCR|
|---|---|---|---|---|
|S2-39|California Civil Code §1798.82<br>(as amended by SB 446)|Legislation|eff. 1 Jan<br>2026|California|
|S2-40|FTC Health Breach Notification<br>Rule, 16 CFR 318|Legislation|2024|US FTC|
|S2-41|GLBA Safeguards Rule 16 CFR<br>314.4(j)|Legislation|2024|US FTC|
|S2-42|In re Blackbaud (FTC complaint,<br>joint statement, order)|Case/enforc<br>ement|2024|US FTC|
|S2-43|In re Uber Technologies (FTC<br>revised complaint)|Case/enforc<br>ement|2018|US FTC|
|S2-44|Privacy Act 1988 (Cth) Part IIIC,<br>Notifiable Data Breaches|Legislation|2018|Australia|
|S2-45|OAIC Notifiable Data Breaches<br>Report, Jul–Dec 2024|Practitioner/p<br>ress|2025|OAIC|
|S2-46|Privacy and Other Legislation<br>Amendment Act 2024|Legislation|2024|Australia|
|S2-47|AIC v Medibank Private|Case/enforc<br>ement|filed 2024|OAIC; Federal Court|
|S2-48|AIC v Singtel Optus|Case/enforc<br>ement|filed Aug<br>2025|OAIC; Federal Court|



|S2-49|Australian Information<br>Commissioner v Australian<br>Clinical Labs Limited (No 2)<br>[2025] FCA 1224 (Halley J)|Case/enforc<br>ement|8 Oct 2025|Federal Court of Australia|
|---|---|---|---|---|
|S2-50|In re Capital One Customer Data<br>Security Breach Litigation (E.D.<br>Va., Mag. J. Anderson, 26 May<br>2020); Wengui v. Clark Hill<br>(D.D.C., Boasberg J., 12 Jan<br>2021); In re Rutter's (M.D. Pa.,<br>Chief Mag. J. Mehalchick, 22 Jul<br>2021)|Case/enforc<br>ement|2020–21|US district courts|
|S2B-01|GPAI Code of Practice, Safety &<br>Security chapter, Commitment 9|Standard/gui<br>dance|Jul 2025|EU AI Office; independent<br>chairs|
|S2B-02|OECD, "Towards a Common<br>Reporting Framework for AI<br>Incidents"|Standard/gui<br>dance|Feb 2025|OECD/GPAI|
|S2B-03|NIST AI 600-1 Generative AI<br>Profile|Standard/gui<br>dance|Jul 2024|NIST|
|S2B-04|NIST AI RMF 1.0|Standard/gui<br>dance|Jan 2023|NIST|
|S2B-05|OpenAI Preparedness<br>Framework v2|Policy/code|Apr 2025|OpenAI|
|S2B-06|Anthropic Responsible Scaling<br>Policy v3.0|Policy/code|Feb 2026|Anthropic|
|S2B-07|Google DeepMind Frontier<br>Safety Framework v3.0|Policy/code|2025|Google DeepMind|
|S2B-08|America's AI Action Plan|Standard/gui<br>dance|Jul 2025|White House OSTP|



|S2B-09|CSET, "AI Incidents: Key<br>Components for a Mandatory<br>Reporting Regime"|Scholarly|Jan 2025|CSET Georgetown|
|---|---|---|---|---|
|S2B-10|Humane Intelligence GRT<br>Transparency Report|Practitioner/p<br>ress|2024|Humane Intelligence|
|S2B-11|GPAI Code Vademecum,<br>Signatory Taskforce|Standard/gui<br>dance|Jan 2026|EU AI Office|
|S2B-12|EU AI Act Art. 3(49) serious<br>incident definition|Legislation|2024|EU|
|S2B-13|EU AI Act Art. 73|Legislation|2024|EU|
|S2B-14|EU AI Act Art. 55(1)(c)|Legislation|2024|EU|
|S2B-15|Commission draft guidance and<br>template on Art. 73 serious<br>incidents|Standard/gui<br>dance|Sep 2025<br>(draft)|European Commission|
|S2B-16|Latham & Watkins alert on draft<br>Art. 73 guidance|Practitioner/p<br>ress|Oct 2025|Latham & Watkins|
|S2B-17|California SB 53, Transparency<br>in Frontier AI Act|Legislation|operative 1<br>Jan 2026|California|
|S2B-18|New York RAISE Act, S6953-B,<br>Chapter 699 of 2025 (signed 19<br>Dec 2025); reported chapter<br>amendment Mar 2026|Legislation|2025–26|New York|
|S2B-19|Colorado SB 24-205 → SB<br>25B-004 → SB 26-189|Legislation|eff. 1 Jan<br>2027|Colorado|



|S2B-20|Australia: Voluntary AI Safety<br>Standard (Sep 2024),<br>superseded in practice by<br>Guidance for AI Adoption (6<br>practices, 21 Oct 2025);<br>mandatory guardrails shelved<br>Dec 2025; "Australian Standards<br>for AI" announced Jul 2026|Standard/gui<br>dance|2024–26|DISR; PM&C|
|---|---|---|---|---|
|S2B-21|EO 14148 rescinding EO 14110|Legislation|Jan 2025|White House|
|S2B-22|NIST AI 100-2 E2025<br>Adversarial ML taxonomy|Standard/gui<br>dance|Mar 2025|NIST|
|S2B-23|CAISI outputs 2025–26|Standard/gui<br>dance|2025–26|NIST CAISI|
|S2B-24|OECD, "Defining AI incidents<br>and related terms"|Standard/gui<br>dance|May 2024|OECD|
|S2B-25|OECD AI Incidents and Hazards<br>Monitor methodology|Practitioner/p<br>ress|2024–|OECD.AI|
|S2B-26|G7 Hiroshima AI Process<br>Reporting Framework|Standard/gui<br>dance|Feb 2025|OECD for G7|
|S2B-27|Frontier AI Safety Commitments<br>(Seoul)|Policy/code|May 2024|UK/ROK; 20 companies|
|S2B-28|International AI Safety Report<br>2026|Scholarly|Feb 2026|International expert panel|
|S2B-29|Longpre et al., "A Safe Harbor<br>for AI Evaluation and Red<br>Teaming"|Scholarly|2024|arXiv 2403.04893; ICML|



|S2B-30|Longpre, Klyman, Appel,<br>Kapoor, Bommasani et al.,<br>"In-House Evaluation Is Not<br>Enough"|Scholarly|2025|arXiv 2503.16861|
|---|---|---|---|---|
|S2B-31|Cattell, Ghosh & Kaffee,<br>"Coordinated Flaw Disclosure for<br>AI"|Scholarly|2024|arXiv 2402.07039; AIES|
|S2B-32|Kolt et al., "Responsible<br>Reporting for Frontier AI<br>Development"|Scholarly|2024|arXiv 2404.02675|
|S2B-33|Longpre, Zhu, Ezell, Ghosh,<br>McGregor et al., "FLARE-AI:<br>Flaw Reporting for AI"|Scholarly|Jun 2026|arXiv 2606.31567; ICML|
|S2B-34|Ezell, Roberts-Gaal & Chan,<br>"Incident Analysis for AI Agents"|Scholarly|Aug 2025|arXiv 2508.14231|
|S2B-35|Abraham et al., "AI Incident<br>Monitoring through a Public<br>Health Lens"|Scholarly|Apr 2026|arXiv 2604.19914|
|S2B-36|Stanford AI Index 2026,<br>Responsible AI chapter|Scholarly|2026|Stanford HAI|
|S2B-37|CVE AI Working Group Charter<br>v1.1; CNA Rules §4.2.3|Standard/gui<br>dance|2024–25|CVE Program|
|S2B-38|CVE Program blog, "CVE ID<br>Assignment and CVE Record<br>Publication for AI-Related<br>Vulnerabilities"|Standard/gui<br>dance|18 Feb<br>2025|CVE Program|



|S2B-39|OpenAI CVE Assignment Policy<br>(20 Nov 2025); Bug Bounty<br>announcement (11 Apr 2023)|Policy/code|2023–25|OpenAI|
|---|---|---|---|---|
|S2B-40|Google AI Vulnerability Reward<br>Program rules|Policy/code|Oct 2025|Google|
|S2B-41|Meta Bug Bounty GenAI payout<br>guidelines|Policy/code|2024–26|Meta|
|S2B-42|Anthropic model-safety bug<br>bounty|Policy/code|May 2025|Anthropic|
|S2B-43|Hacking Policy Council analysis<br>of Copyright Office §1201 ruling|Practitioner/p<br>ress|Dec 2024|HPC|
|S2B-44|DEF CON AI Village Generative<br>Red Team 2 and 3|Practitioner/p<br>ress|2024–25|AI Village et al.|
|S2B-45|MITRE ATLAS AI Incident<br>Sharing initiative|Practitioner/p<br>ress|Oct 2024|MITRE CTID|
|S2B-46|CLTR, "AI incident reporting:<br>addressing a gap in UK<br>regulation"|Practitioner/p<br>ress|Jun 2024|Centre for Long-Term<br>Resilience|
|S2B-47|CLTR, "Preparing for AI security<br>incidents"|Practitioner/p<br>ress|Sep 2025|CLTR|
|S2B-48|AI Incident Database, Editor's<br>Guide|Practitioner/p<br>ress|current|Responsible AI<br>Collaborative|
|S2B-49|AIAAIC Repository|Practitioner/p<br>ress|current|AIAAIC|
|S2B-50|AVID, AI Vulnerability Database|Practitioner/p<br>ress|current|AVID|



|S2B-51|MIT AI Risk Repository v4 and<br>Incident Tracker|Practitioner/p<br>ress|Dec 2025|MIT FutureTech|
|---|---|---|---|---|
|S2B-52|OWASP Top 10 for LLM<br>Applications 2025|Standard/gui<br>dance|2025|OWASP GenAI Security<br>Project|
|S2B-53|GDPR Art. 4(12) personal data<br>breach|Legislation|2016|EU|
|S2B-54|6 U.S.C. §650 "incident"<br>(CIRCIA baseline)|Legislation|2022|US|
|S2B-55|Hugging Face Hub security<br>documentation|Policy/code|current|Hugging Face|
|S3-01|Zou, Danino, Sun & Schaub,<br>"You 'Might' Be Affected" (161<br>notices)|Scholarly|2019|CHI 2019|
|S3-02|Zou, Mysore & Schaub, "I've Got<br>Nothing to Lose" (Equifax<br>interviews)|<br>Scholarly|2018|SOUPS 2018|
|S3-03|Mayer, Zou, Schaub & Aviv,<br>"'Now I'm a bit angry'" (n = 413,<br>real breaches)|Scholarly|2021|USENIX Security 2021|
|S3-04|Ablon et al., Consumer Attitudes<br>Toward Data Breach<br>Notifications (RAND, n = 2,038)|Scholarly|2016|RAND|
|S3-05|Ponemon/Experian, "The<br>Aftermath of a Data Breach:<br>Consumer Sentiment"|Practitioner/p<br>ress|Apr 2014|Ponemon<br>(Experian-sponsored)|
|S3-06|Romanosky, Telang & Acquisti,<br>"Do Data Breach Disclosure<br>Laws Reduce Identity Theft?"|Scholarly|2011|J. Policy Analysis &<br>Management|



|S3-09|Bisogni, "Proving Limits of State<br>Data Breach Notification Laws"<br>(445 notices)|Scholarly|2016|J. Information Policy 6:<br>154–205|
|---|---|---|---|---|
|S3-10|Shen et al., "'An incident may<br>have resulted in a suspected<br>data compromise'" (n = 99)|Scholarly|2022|SOUPS 2022 poster|
|S3-11|Bruemmer (Experian), "The<br>misconceptions of data breach<br>fatigue"|Practitioner/p<br>ress|2016|IAPP|
|S3-12|Shaver, "Breach Fatigue:<br>Consumer Apathy Towards Data<br>Breaches and Personal Security"<br>(undergraduate honours thesis)|<br>Scholarly|May 2016|Ohio State University, Fisher<br>College of Business|
|S3-13|OAIC, Australian Community<br>Attitudes to Privacy Survey 2023<br>(n = 1,916)|Practitioner/p<br>ress|2023|OAIC|
|S3-14|Morgan & Voce, "Data breaches<br>and cybercrime victimisation"|Scholarly|2022|Australian Institute of<br>Criminology|
|S3-17|TermScout, "What's Market? A<br>look into Data Breach<br>Notifications"|Practitioner/p<br>ress|9 Aug 2021|TermScout|
|S3-18|FTC, "Data Breach Response: A<br>Guide for Business" and model<br>letter|Standard/gui<br>dance|2016|FTC|
|S3-22|OAIC, Data breach preparation<br>and response, Parts 3–4|Standard/gui<br>dance|current|OAIC|



|S3-29|Vastaamo breach: Finnish<br>Ministry of Social Affairs and<br>Health victim-support page (Oct<br>2020) and Yle (Feb 2026);<br>crisis-comms analysis via<br>Ruohonen et al. 2024 (S1-32)|Primary/pres<br>s|2020–26|Finnish Government; Yle|
|---|---|---|---|---|
|S3-30|Ashley Madison FTC settlement|Case/enforc<br>ement|2016|FTC|
|S3-31|Scamwatch (ACCC), Optus data<br>breach scams alert|Standard/gui<br>dance|2022|ACCC|
|S3-32|Medibank newsroom: customer<br>updates and support package|Primary<br>record|2022|Medibank|
|S3-33|2022 Optus breach SMS<br>blackmail case: AFP sentencing<br>release (7 Feb 2023) and ABC<br>(6 Oct 2022)|Primary/pres<br>s|2022–23|Australian Federal Police;<br>ABC|
|S3-34|KnowBe4 Q3 2017 phishing<br>subject lines (via Infosecurity)|Practitioner/p<br>ress|2017|KnowBe4|
|S3-35|Bîzgă, fake breach notifications;<br>Kantra, "Scammers Are Now<br>Sending Fake 'Your Data Was<br>Breached' Emails"|Practitioner/p<br>ress|Jun<br>2024/Mar<br>2026|Bitdefender; Techlicious|
|S3-36|Wash, Nthala & Rader,<br>non-expert phishing detection (n<br>= 297)|Scholarly|2021|SOUPS 2021|



|S3-37|SAMHSA, Concept of Trauma<br>and Guidance for a<br>Trauma-Informed Approach|Standard/gui<br>dance|2014|SAMHSA|
|---|---|---|---|---|
|S3-39|eSafety Commissioner,<br>image-based abuse and<br>deepfakes guidance|Standard/gui<br>dance|2024–25|eSafety (AU)|
|S3-40|StopNCII.org, "How it works"|Practitioner/p<br>ress|current|SWGfL|
|S3-41|Cyber Civil Rights Initiative<br>Safety Center|Practitioner/p<br>ress|current|CCRI|
|S3-42|TAKE IT DOWN Act (Pub. L.<br>119-12, 19 May 2025) and FTC<br>enforcement blog (19 May 2026)|Legislation/g<br>uidance|2025–26|Congress; FTC|
|S3-43|CDT, NCII hash-matching<br>governance brief|Practitioner/p<br>ress|9 Apr 2026|CDT|
|S3-44|ITRC 2025 Consumer Impact<br>Report|Practitioner/p<br>ress|Oct 2025|Identity Theft Resource<br>Center|
|S3-45|IDCARE|Practitioner/p<br>ress|current|IDCARE|
|S3-46|ISO 24495-1:2023 Plain<br>language, Part 1|Standard/gui<br>dance|2023|ISO TC37|
|S3-47|Plain Writing Act 2010; Federal<br>Plain Language Guidelines and<br>testing guidance|Legislation/g<br>uidance|2010/2011|US GSA; PLAIN|
|S3-48|Australian Government Style<br>Manual, "Literacy and access"|Standard/gui<br>dance|2024|DTA|



|S3-49|European Commission, "How to<br>write clearly"|Standard/gui<br>dance|2015|European Commission DG<br>Translation (Publications<br>Office)|
|---|---|---|---|---|
|S3-50|Redish, limitations of readability<br>formulas|Scholarly|2000|ACM J. Computer<br>Documentation 24(3):<br>132–137|
|S3-51|Garcia v. Character<br>Technologies; Character.AI<br>"Community Safety Updates"|Case/primar<br>y|2024–26|M.D. Fla.; Character.AI|
|S3-52|Moffatt v. Air Canada, 2024<br>BCCRT 149|Case/enforc<br>ement|2024|BC Civil Resolution Tribunal|
|S3-53|Carlini et al., "Extracting Training<br>Data from Large Language<br>Models"|Scholarly|2021|USENIX Security 2021|
|S3-55|OpenAI, "How the voices for<br>ChatGPT were chosen";<br>Johansson statement coverage|Primary/pres<br>s|May 2024|OpenAI; NPR/TechCrunch|
|S3-56|FTC consumer alert on<br>AI-enhanced family emergency<br>scams; Voice Cloning Challenge|Standard/gui<br>dance|2023–24|FTC|
|S3-57|EU AI Act Art. 86 right to<br>explanation; Commission<br>timeline page|Legislation|2024/2026|EU|
|S3-58|GDPR Art. 22|Legislation|2016|EU|
|S3-59|Kaminski & Urban, "The Right to<br>Contest AI"|Scholarly|2021|Columbia Law Review|



|S3-60|Contestability literature (Alfrink<br>et al. 2022/23; Lyons, Velloso &<br>Miller 2021; Yurrita et al. 2025;<br>Stewart, FAccT 2026)|Scholarly|2021–26|ACM/arXiv|
|---|---|---|---|---|
|S3-61|CRA Art. 14(8) user-notification<br>duty (lead-verified)|Legislation|2024<br>(applies 11<br>Sep 2026)|EU|
|S4-01|SPJ Code of Ethics|Policy/code|2014|Society of Professional<br>Journalists|
|S4-02|AP Statement of News Values<br>and Principles|Policy/code|2026 ed.|Associated Press|
|S4-03|Reuters Standards and Values<br>(Handbook of Journalism)|Policy/code|current|Reuters|
|S4-04|BBC Editorial Guidelines,<br>Section 3 Accuracy|Policy/code|current|BBC|
|S4-05|NYT Ethical Journalism<br>handbook|Policy/code|2025|New York Times|
|S4-06|Guardian News & Media<br>Editorial Code|Policy/code|Mar 2026|GNM|
|S4-07|MEAA Journalist Code of Ethics|Policy/code|1999 rev.|MEAA|
|S4-08|Australian Press Council<br>Statement of General Principles|Policy/code|2014 (page<br>current)|Australian Press Council|
|S4-09|Zacharia & Grotto, "How to<br>Responsibly Report on Hacks<br>and Disinformation"|Practitioner/p<br>ress|2020|Stanford Cyber Policy<br>Center|
|S4-10|Allsop, "Should the media report<br>on hacked campaign<br>documents?"|Practitioner/p<br>ress|2024|Columbia Journalism<br>Review|



|S4-11|EFF Coders' Rights, Vulnerability<br>Reporting FAQ|<br>Practitioner/p<br>ress|current|EFF|
|---|---|---|---|---|
|S4-12|Science Media Centre, "10 best<br>practice guidelines for reporting<br>science & health stories"|Practitioner/p<br>ress|2012|SMC UK|
|S4-13|SMC UK "For journalists"<br>resources|Practitioner/p<br>ress|current|SMC UK|
|S4-14|Australian Science Media Centre<br>/ Scimex|Practitioner/p<br>ress|current|AusSMC|
|S4-15|SciLine|Practitioner/p<br>ress|current|AAAS|
|S4-16|Boykoff & Boykoff, "Balance as<br>bias"|Scholarly|2004|Global Environmental<br>Change|
|S4-17|Dixon & Clarke, "Heightening<br>Uncertainty Around Certain<br>Science"|Scholarly|2013|Science Communication|
|S4-18|Jensen, hedging and credibility<br>in cancer news (N = 601)|Scholarly|2008|Human Communication<br>Research|
|S4-19|Peters & Dunwoody, scientific<br>uncertainty in media (special<br>issue)|Scholarly|2016|Public Understanding of<br>Science|
|S4-20|Fleerackers et al., preprints in<br>COVID digital media|Scholarly|2022|Health Communication|
|S4-21|KSJ Science Editing Handbook<br>v2.1|Practitioner/p<br>ress|2020–|Knight Science Journalism<br>@ MIT|
|S4-22|AHCJ Statement of Principles|Policy/code|current|Association of Health Care<br>Journalists|



|S4-23|ASAPbio preprint guidance for<br>journalists|Practitioner/p<br>ress|c. 2020|ASAPbio|
|---|---|---|---|---|
|S4-24|Verification Handbook (2014)<br>and for Disinformation and<br>Media Manipulation (2020)|Practitioner/p<br>ress|2014/2020|European Journalism<br>Centre|
|S4-25|First Draft, "Verifying online<br>information" (five pillars)|Practitioner/p<br>ress|2020|First Draft|
|S4-26|Bellingcat resources and<br>editorial standards|Practitioner/p<br>ress|current|Bellingcat|
|S4-27|Hunt, "Here's how I verify data<br>breaches"|Practitioner/p<br>ress|2016|Troy Hunt|
|S4-28|Hunt, "Data breach disclosure<br>101"|Practitioner/p<br>ress|2017|Troy Hunt|
|S4-29|Schwartz, "Ransomware Groups'<br>Data Leak Blogs Lie"|<br>Practitioner/p<br>ress|2024|ISMG; GovInfoSecurity|
|S4-30|DataBreaches.net, ransomware<br>listing confusion|Practitioner/p<br>ress|2025|DataBreaches.net|
|S4-31|Bitdefender, "Claimed Twice"|Practitioner/p<br>ress|Jun 2026|Bitdefender|
|S4-32|Recent Breaches editorial<br>standards|Practitioner/p<br>ress|current|GalaxyWarden (commercial)|
|S4-33|Whittaker, "A data breach at<br>analytics giant Mixpanel leaves a<br>lot of open questions"|Practitioner/p<br>ress|2 Dec 2025|TechCrunch|
|S4-34|Thorne, "We read 100 data<br>breach notifications to make this<br>guide"|Practitioner/p<br>ress|2017|Atlassian Statuspage|



|S4-35|Brennen, Howard & Nielsen, "An<br>Industry-Led Debate"|Scholarly|2018|Reuters Institute|
|---|---|---|---|---|
|S4-36|Nielsen, "How news coverage,<br>often uncritical, helps build up<br>the AI hype"|Scholarly|2024|Reuters Institute|
|S4-37|Chuan, Tsai & Cho, framing AI in<br>US newspapers|Scholarly|2019|AIES 2019|
|S4-38|Ouchchy, Coin & Dubljević, AI<br>ethics in the headlines|Scholarly|2020|AI & Society|
|S4-39|Nguyen & Hekman, news<br>framing of AI (N = 3,098)|Scholarly|2022|AI & Society|
|S4-40|Roe & Perkins, UK ChatGPT<br>headlines (671)|Scholarly|2023|Humanities & Social<br>Sciences Communications|
|S4-41|Bartholomew & Mehta, "How the<br>media is covering ChatGPT"|Practitioner/p<br>ress|2023|CJR; Tow Center|
|S4-42|Placani, "Anthropomorphism in<br>AI: hype and fallacy"|Scholarly|2024|AI and Ethics|
|S4-43|Vicsek, Feher & Nguyen, framing<br>AI in US elite media|<br>Scholarly|2026|Global Media and<br>Communication|
|S4-44|Dodds et al., "AI Hype in<br>Journalism" (special issue)|Scholarly|2026|Digital Journalism|
|S4-45|Simon, Nielsen & Fletcher,<br>Generative AI and News Report<br>2025|Scholarly|2025|Reuters Institute|
|S4-46|Reuters Institute Digital News<br>Report 2025|Practitioner/p<br>ress|2025|Reuters Institute|



|S4-47|Axios Codebook, "The myth of<br>the sophisticated hacker"|Practitioner/p<br>ress|2019|Axios|
|---|---|---|---|---|
|S4-48|Carson & Singh, "Debunking the<br>5 Myths of Sophisticated Cyber<br>Attacks"|Practitioner/p<br>ress|6 Apr 2017|Security Magazine|
|S4-50|Jenkins, Anandarajan &<br>D'Ovidio, impression<br>management in breach<br>notification (212 letters)|Scholarly|2014|Western J. Communication|
|S4-51|Veltsos, breach notifications as<br>negative news|Scholarly|2012|Business Communication<br>Quarterly|
|S4-52|Bentley, Oostman & Shah,<br>apologies in ambiguous crises|Scholarly|2018|J. Contingencies & Crisis<br>Management|
|S4-55|Kim, Johnson & Park, five retail<br>breaches and press framing|Scholarly|2017|Cogent Business &<br>Management|
|S4-56|Equifax incident-handling case<br>study|Scholarly|2018|Issues in Information<br>Systems|
|S4-58|Fuoli & Paradis, model of<br>trust-repair discourse|Scholarly|2014|J. Pragmatics|
|S4-59|Fuoli & Hart, trust-building<br>strategies experiment|Scholarly|2018|Discourse & Society 29(5):<br>514–552|
|S4-62|Wiz Research, exposed<br>DeepSeek database|Practitioner/p<br>ress|Jan 2025|Wiz|
|S4-63|Serrapere, "Data Breach<br>Notifications Are Too Complex"|Practitioner/p<br>ress|2020|Chicago Policy Review|



|S4-64|GIJN and Pulitzer Center, AI<br>Accountability Reporting Guide|Practitioner/p<br>ress|Jun 2026|GIJN|
|---|---|---|---|---|
|S4-65|GIJN, Guide to Investigating<br>Social Media Algorithms|Practitioner/p<br>ress|2025|GIJN|
|S4-66|GIJN, Reporter's Guide to<br>Detecting AI-Generated Content|Practitioner/p<br>ress|2024–25|GIJN|
|S4-67|GIJN, Reporter's Guide to<br>Investigating Digital Threats|Practitioner/p<br>ress|c. 2023|GIJN|
|S4-68|The Markup, "Show Your Work"|Practitioner/p<br>ress|2020–|The Markup|
|S4-69|AlgorithmWatch publications|Practitioner/p<br>ress|2019–|AlgorithmWatch|
|S4-72|Partnership on AI, Responsible<br>Practices for Synthetic Media|Standard/gui<br>dance|2023|Partnership on AI|
|S4-73|JournalismAI research reports|Practitioner/p<br>ress|2019–25|LSE Polis|
|S4-74|Poynter AI Ethics Guidelines /<br>Starter Kit|Practitioner/p<br>ress|2024–25|Poynter|
|S4-75|Walkley Foundation AI and<br>Journalism training|Practitioner/p<br>ress|2023–24|Walkley Foundation|
|S4-76|American Journalism Project, AI<br>for Local Reporting field guide|Practitioner/p<br>ress|2025|AJP|
|S4-78|Pulitzer Center AI Accountability<br>Network / AI Spotlight|Practitioner/p<br>ress|2022–|Pulitzer Center|



|S5O-01|OpenAI, "March 20 ChatGPT<br>outage: Here's what happened"<br>(Wayback captures 24 Mar, 20<br>Apr, 21 Apr 2023)|Primary<br>record|2023|OpenAI|
|---|---|---|---|---|
|S5O-03|Altman (@sama), X post<br>acknowledging the ChatGPT<br>chat-history bug (20:16 UTC)|Primary<br>record|22 Mar<br>2023|X|
|S5O-04|@JordanLWheeler, X post<br>reporting other users' chat titles<br>visible in ChatGPT (16:26 UTC)|Primary<br>record|20 Mar<br>2023|X|
|S5O-09|Help Net Security, email wording|Practitioner/p<br>ress|27 Mar<br>2023|Help Net Security|
|S5O-12|Hacker News thread 35291112|Primary<br>record|24 Mar<br>2023|Hacker News|
|S5O-13|Garante temporary limitation<br>order and press release|Case/enforc<br>ement|30–31 Mar<br>2023|Garante|
|S5O-15|Garante press release|Case/enforc<br>ement|20 Dec<br>2024|Garante|
|S5O-16|Tribunale di Roma annulment of<br>the Garante OpenAI fine: ANSA<br>(20 Mar 2026) and Il Sole 24 Ore<br>NT+ (3 Jun 2026)|Practitioner/p<br>ress|Mar–Jun<br>2026|ANSA; Il Sole 24 Ore|
|S5O-17|OpenAI, "What to know about a<br>recent Mixpanel security<br>incident" (Wayback 27 Nov, 11<br>Dec 2025; 27 Jan 2026)|Primary<br>record|2025–26|OpenAI|
|S5O-18|Taylor, "Our response to a recent<br>security incident"|Primary<br>record|Nov 2025<br>(undated)|Mixpanel|



|S5O-19|Hacker News post with full<br>OpenAI email text|Primary<br>record|27 Nov<br>2025|Hacker News|
|---|---|---|---|---|
|S5O-26<br>/27|OpenAI, "Sycophancy in<br>GPT-4o" and "Expanding on<br>what we missed with<br>sycophancy"|Primary<br>record|Apr–May<br>2025|OpenAI|
|S5O-28|Altman (@sama) and OpenAI, X<br>posts on the GPT-4o<br>sycophancy update|Primary<br>record|25–30 Apr<br>2025|X|
|S5O-32<br>(S5H-2<br>6/27)|<br>OpenAI, Hugging Face incident<br>posts (21 Jul 2026, updates<br>28–29 Jul; 26 Aug 2026 report)|Primary<br>record|2026|OpenAI|
|S5H-01<br>/02|Hugging Face, "Space secrets<br>security update" (raw GitHub;<br>Wayback)|Primary<br>record|31 May<br>2024|Hugging Face|
|S5H-03|GitHub API commit history,<br>huggingface/blog|Primary<br>record|2023–26|GitHub|
|S5H-05|Wiz Research, Hugging Face<br>infrastructure risks|Practitioner/p<br>ress|4 Apr 2024|Wiz|
|S5H-06|Wiggers, Hugging Face<br>unauthorized access|Practitioner/p<br>ress|31 May<br>2024|TechCrunch|
|S5H-11|The Register, Lasso token<br>exposure, with Delangue<br>statement|Practitioner/p<br>ress|Dec 2023|The Register|
|S5H-12|Hacker News thread 40544875|Primary<br>record|1 Jun 2024|Hacker News|
|S5H-13<br>/14|Hugging Face forum topics<br>89696, 68768; skops PR #421|Primary<br>record|2024|Hugging Face forum;<br>GitHub|
|S5H-16|Hugging Face blog, Wiz<br>partnership post|Primary<br>record|4 Apr 2024|Hugging Face|



|S5H-18<br>/19|Hugging Face, "Security incident<br>disclosure — July 2026" (raw)<br>and PR #3465 metadata|Primary<br>record|15–16 Jul<br>2026|Hugging Face; GitHub|
|---|---|---|---|---|
|S5H-21<br>/22|Hugging Face, "Anatomy of a<br>Frontier Lab Agent Intrusion: A<br>Technical Timeline" and its nine<br>commits|Primary<br>record|27–30 Jul<br>2026|Hugging Face|
|S5H-23<br>/24|Whittaker; BleepingComputer|Practitioner/p<br>ress|20 Jul 2026|TechCrunch;<br>BleepingComputer|
|S5H-25|Ha, Delangue "radical<br>transparency"|Practitioner/p<br>ress|26 Jul 2026|TechCrunch|
|S5H-28|METR and Redwood Research<br>independent investigation|Scholarly/pri<br>mary|26 Aug<br>2026|METR|
|S5H-31|Willison, OpenAI timeline post|Practitioner/p<br>ress|7 Aug 2026|Simon Willison|
|S5H-32|Politico, "OpenAI models shared<br>hacking tips on secret<br>messaging board before<br>Hugging Face breach"|Practitioner/p<br>ress|5 Aug 2026|Politico|
|S5H-36<br>/37|Senate letters to OpenAI:<br>Hawley (9 Sep 2026; release 10<br>Sep), Blumenthal (9 Sep), Van<br>Hollen (10 Sep)|Primary<br>record|Sep 2026|US Senate|
|S5H-40|status.huggingface.co incident<br>965809|Primary<br>record|16 Jul 2026|Hugging Face|
|S5H-43|Truffle Security, 787 live Hugging<br>Face tokens in training data|<br>Practitioner/p<br>ress|Jun 2026|Truffle Security|



|S5H-44<br>/46/48|Lasso Security blog (Dec 2023);<br>BleepingComputer on JFrog<br>(Feb 2024); ReversingLabs<br>"nullifAI" (Feb 2025)|Practitioner/p<br>ress|2023–25|Lasso Security;<br>BleepingComputer;<br>ReversingLabs|
|---|---|---|---|---|
|S5H-47|JFrog blog, malicious Hugging<br>Face models|Practitioner/p<br>ress|Feb 2024|JFrog|
|S5H-49|Altman (@sama), X post on the<br>Hugging Face incident, linking<br>the OpenAI statement (20:13<br>UTC)|Primary<br>record|21 Jul 2026|X|
|S5H-50|Delangue (@ClementDelangue),<br>X posts responding to OpenAI<br>attribution (21 Jul, 20:50 UTC)<br>and announcing a San Francisco<br>trip (23 Jul, 11:04 UTC)|Primary<br>record|21–23 Jul<br>2026|X|
|S5H-51|Altman, "How to Make an<br>Abundant Future" (interview),<br>Invest Like the Best EP.484<br>(Hugging Face incident<br>discussion 16:14–17:44 on<br>Spotify)|Primary<br>record|28 Jul 2026|Invest Like the Best with<br>Patrick O'Shaughnessy<br>(Colossus)|



