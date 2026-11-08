# **Sandbox to Sensationalism?** 

# **How Higher-Reach YouTube Coverage of the 2026 OpenAI–Hugging Face Incident Diverges from Technical Disclosures** 

**Ayomide Fagbolade Grentson Suguitan Yoan Bels** `ayomide.fagbolade@gmail.com grentsonsuguitan@gmail.com Belsyoan@gmail.com` 

With Apart Research 

**Abstract.** Public understanding of AI safety incidents depends partly on how digital media translate technical disclosures into narratives about agency and risk. This study examines higher-reach YouTube coverage of the July 2026 OpenAI– Hugging Face incident, which originated in a sandboxed evaluation but extended into production infrastructure. We searched a corpus of 102 videos published between July 16 and August 17, 2026, and analyzed 236 atomic claims drawn from a 22-video intensive sample (the top quartile by view count), using stored results from two LLM-assisted verification cycles against OpenAI’s July disclosure and August postmortem. In the final cycle, incident claims were supported in 52.8% (67/127) of cases, neither supported nor contradicted in 29.9% (38/127), and contradicted in 17.3% (22/127). Incident contradiction rates differed sharply by channel provenance: 8.5% (4/47) for mainstream news versus 22.5% (18/80) for independent and other creators. Interpretation claims were predominantly neither supported nor contradicted (73.4%; 80/109). Contradiction rates rose from Cycle 1 to Cycle 2 overall, most sharply for claims involving agency/attribution and causation/awareness—claims about who acted and why, rather than what occurred. Policy-relevant interpretation claims extended well beyond what the technical baseline could confirm or refute, ranging from governance and accountability arguments to a smaller set of claims asserting general AI uncontrollability. Retrospective, single-model verification; a single-platform, keyword-based sample; and reliance on two primary disclosures limit how far these findings generalize. The results support distinguishing, in AI-risk communication, what happened, who is responsible and why, and which policy conclusions an incident is asked to support. 

## **1. Introduction** 

Disclosures about AI safety incidents shape public discourse on autonomy, loss of control, and governance. Yet media coverage does not necessarily align with these disclosures: claims that reach the largest audiences are not always those best supported by the underlying record. This study compares higher-reach YouTube coverage of a real AI safety incident with the primary technical disclosures about it, examining where that coverage aligns with the evidence and where it goes beyond it. 

This study concerns a real intrusion originating in an internal evaluation, not an exploit confined to a harmless simulation. On July 21, 2026, OpenAI disclosed that its models had bypassed network restrictions and compromised Hugging Face infrastructure while pursuing solutions to evaluation tasks [6]. Human-designed testing conditions and autonomous unauthorized actions are compatible descriptions of the incident. Treating either as evidence against the other would distort the technical context. 

We ask the following primary questions: **RQ1** : To what extent do incident- and interpretation-level claims diverge from the primary technical disclosures? Moreover, which claim types are most divergent within each layer, and how do these patterns change from the initial-disclosure baseline (Cycle 1) to the cumulative evidence (Cycle 2)? **RQ2** : How does coverage move from incident reporting to policy and risk interpretation? 

Our contributions are threefold. First, we provide a reproducible descriptive audit of 236 atomized claims from various video sources across incident and interpretation layers. These claims were verified against two evidence baselines (Cycle 1 and Cycle 2). Second, we identify two distinct divergence patterns within the sample: incident-level contradiction rates increased from 3.1% (4/127) to 17.3% (22/127) between the initial-disclosure and cumulative-evidence baselines, with the sharpest increases in agency/attribution and causation/awareness claims, and final-cycle incident contradiction rates were substantially higher among independent and other creators than mainstream news channels. Third, we provide a qualitative account of how interpretation-layer claims extrapolate a single incident into a wide range of governance and risk positions, most of which the technical baseline can neither confirm nor refute. Together, these results support distinguishing what happened, who is responsible and why, and which policy conclusions an incident is being used to support in AI-risk communication. Technical disclosures can inform these distinctions without determining the policy response. 

## **2. Related Work** 

Framing research examines how communication selects and emphasizes aspects of events to organize problem definitions, causal accounts, evaluations, and proposed responses [1]. This perspective informs our comparison of how videos describe an event and how technical disclo- 

1 

sures present it. Research on AI-related news sourcing also shows that media visibility and academic prominence need not coincide, and that industry-linked experts occupy a substantial role in coverage [2]. More specifically, Bunz and Braghieri identify framings of healthcare AI as replacing or outperforming human experts, alongside personification of AI systems [3]. Their study motivates attention to how coverage assigns agency, but does not establish whether particular attribution claims conflict with technical evidence. 

Atomic-fact evaluation provides a methodological precedent for examining such conflicts at the proposition level. FActScore decomposes long-form generated text into atomic facts and measures the proportion supported by a knowledge source, with human evaluation conducted on model-generated biographies [4]. Our workflow shares this decomposition-and-verification logic but applies it to human-produced YouTube commentary rather than generated biographies. We distinguish contradiction from missing support and compare stored judgments for the same claims against two evidence baselines. This design enables descriptive comparison as the evidence baseline expands; it does not establish that performance demonstrated for FActScore transfers to our extraction and verification pipeline. 

Channel provenance also matters for situating YouTube coverage. Pew Research Center’s analysis of popular YouTube news channels found that independent channels were more often personality-driven than newsorganization channels, and their videos more often covered subjects negatively or discussed conspiracy theories [5]. These findings motivate comparing institutional and independent sources, but tone and topic selection are not measures of factual contradiction. Our broadcaster-based grouping also differs from Pew’s affiliation categories, so the studies’ channel comparisons are not directly equivalent. 

Our contribution connects these strands through a claimlevel audit of incident reporting and broader interpretation across two technical evidence baselines. It does not measure audience belief change or test whether one media system is generally more accurate. Primary disclosures supply incident context [6, 7, 8]; they are not a complete evidentiary basis for every policy or future-risk proposition. 

## **3. Methods** 

### **3.1 Video Collection and Sampling** 

We searched YouTube using the keyword phrase _“open ai hugging face hack”_ and applied publication-date filters for July 16–August 17, 2026. Transcripts were extracted using Tactiq. 

We chose to restrict our video sampling to videos in the top quartile of the corpus by view count because their larger audiences give them greater potential to shape public 

understanding of the incident. View count serves as a proxy for reach rather than a direct measure of influence on audience beliefs. This distinction supports our focus on narratives in higher-reach coverage rather than their impact on public opinion. 

### **3.2 Atomization and Verification** 

**Claim extraction.** We used `gemini-3.1-flash-lite` via the Google GenAI SDK to split transcript claims into atomic propositions without assessing their truth. A Pydantic-defined JSON schema captured wording or a close paraphrase, proposition, layer, type, and framing tags. Each claim was stored as one row linked to its source video’s metadata. 

**Layer and framing annotation.** Incident claims describe events and their mechanisms, actors, intent, causes, or severity; interpretation claims address broader risks, impacts, governance, solutions, values, or cross-incident comparisons. Layer, type, and framing tags (e.g., loss of control or technical/neutral) were recorded separately during extraction, before verification. 

**Two-cycle verification.** Using the same model, we evaluated each proposition against two baselines: the July disclosure in Cycle 1 and the combined July disclosure and August postmortem in Cycle 2. Cycle 2 did not receive Cycle 1 verdicts. 

Each evaluation returned an explanation and one label: **Supported** (backed by the baseline), **Contradicted** (conflicting with it), or **Neither** (neither established nor refuted). Neither means the baseline does not establish whether a claim is supported or contradicted; it does not mean the claim expresses a neutral viewpoint or is false. We compared both cycles for RQ1 and used Cycle 2 labels for the channel-group and interpretation analyses. 

### **3.3 Channel Classification and Analysis** 

We grouped channels by institutional provenance into _mainstream news_ and _independent/other creators_ . Mainstream news comprised ABC News (Australia), BBC News, CNN, NBC News, and RTVE Noticias; all remaining channels formed the independent/other creators group. For each group, we calculated the incident contradiction rate as the number of contradicted incident claims divided by all incident claims in that group. 

For RQ1, we compared verification outcomes by layer and cycle, and contradiction rates by claim type within each layer. Factual divergence was operationalized as contradiction; Neither was reported separately as an evidentiary gap, not an error. Each claim received equal weight. Type-specific rates used all claims in each type–layer combination as the denominator. Percentages are paired with numerator/denominator fractions to make sample sizes explicit. Paired transitions track reclassification of the same claims across cycles. We also reviewed every Cycle 2 Contradicted record against the cited primary disclosures, 

2 

retaining the original labels. In a single AI-assisted coding pass, each exported proposition received one primary content theme, distinct from its original claim type. Theme counts describe the content of flagged claims, not confirmed errors; they exclude Supported and Neither records. Review notes identify source counterevidence, chronology inconsistencies, scope dependence, support/conflict ambiguities, or potential conflicts. These notes are not replacement verdicts. Exported propositions are paraphrases, not verified transcript quotations; no independent coder agreement was measured. 

For RQ2, we focused the qualitative synthesis on five interpretation types directly relevant to policy: policy/governance, AI risk, future impact, solution, and normative claims. These cover governance arguments, risks and anticipated consequences, proposed responses, and value judgments. We reviewed all propositions within these types, focusing the synthesis on those labeled Neither or Contradicted in Cycle 2. The quantitative analysis retains all claim types and labels. This descriptive synthesis uses exported paraphrases rather than verified quotations; it does not introduce new type assignments or change verification labels. 

## **4. Results** 

### **4.1 Corpus View Distribution** 

The search yielded a corpus of 102 unique videos. Table 1 summarizes their view counts, and Figure 1 shows the distribution. 

**Table 1:** Descriptive statistics for video views in the 102-video corpus. 

|Statistic|Views|
|---|---|
|Mean|84,724.58|
|Standard deviation|159,868.65|
|25th percentile (Q1)|9,008.75|
|Median (Q2)|16,722.50|
|75th percentile (Q3)|72,500.00|





**Figure 1:** Distribution of YouTube video views in the 102video corpus. The left panel shows the distribution on a linear scale, highlighting the long right tail; the right panel uses a logarithmic scale to compress the high-view tail and make variation among lower-view videos more visible. 

View counts were right-skewed (Figure 1), with a mean of 84,724.58 (SD = 159,868.65) and a median (Q2) of 



**Figure 2:** Verification outcomes by layer and cycle. Bars show percentages of the same 127 incident or 109 interpretation claims in each cycle; labels pair percentages with count/total fractions. C1 uses the initial disclosure; C2 uses cumulative evidence. Neither denotes an unresolved claim, not a contradiction. 

16,722.50. The 25th percentile (Q1) was 9,008.75 views, and the 75th percentile (Q3) was 72,500.00 views. We used Q3 as the view-count threshold for selecting higherreach videos for intensive analysis, prioritizing those with greater potential to shape public understanding of the incident. This threshold reflects potential audience reach, not demonstrated influence on beliefs. 

### **4.2 RQ1: Divergence by Layer, Claim Type, and Cycle** 

236 claims were extracted from 22 videos: 127 incident claims (53.8%; 127/236) and 109 interpretation claims (46.2%; 109/236). Figure 2 compares their verification outcomes across both evidence baselines. In Cycle 2, incident contradiction rates were 8.5% (4/47) for mainstream news and 22.5% (18/80) for independent and other creators, a difference of 14.0 percentage points. 

**Layer and cycle comparisons.** Incident contradiction rates increased from 3.1% (4/127) in Cycle 1 to 17.3% (22/127) in Cycle 2, a rise of 14.2 percentage points. Interpretation contradiction rates increased from 0.9% (1/109) to 3.7% (4/109), a rise of 2.8 points. Supported shares increased from 46.5% (59/127) to 52.8% (67/127) for incident claims and from 12.8% (14/109) to 22.9% (25/109) for interpretation claims. Neither shares declined from 50.4% (64/127) to 29.9% (38/127) and from 86.2% (94/109) to 73.4% (80/109), respectively. Interpretation claims were therefore less often contradicted but more often extended beyond what the technical baseline could establish or refute. Table 2 provides exact counts. 

**Incident claim types.** Within the incident layer (Figure 3, left panel), agency/attribution had the highest Cycle 2 contradiction rate (46.7%; 7/15), followed by causation/awareness (40.0%; 4/10) and intent (20.0%; 

3 



**Figure 3:** Contradiction rates by claim type, layer, and cycle, using a shared color scale. Cells pair contradiction percentages with contradicted/total fractions within each type– layer combination. Gray dashes indicate no claims, not a zero rate. Exact counts appear in Table 3; small denominators limit comparisons. 

2/10). Their Cycle 1 rates were 6.7% (1/15), 0.0% (0/10), and 10.0% (1/10), respectively. Contradiction rates also increased for event/action claims, from 2.4% (1/42) to 11.9% (5/42), and mechanism claims, from 2.9% (1/34) to 11.8% (4/34). 

**Interpretation claim types.** Within the interpretation layer (Figure 3, right panel), agency/attribution had the highest contradiction rate (25.0%; 1/4), unchanged across both cycles. In contrast, the contradiction rate for causation/awareness claims increased from 0.0% (0/8) in Cycle 1 to 12.5% (1/8) in Cycle 2, while the rate for AI-risk claims increased from 0.0% (0/27) to 7.4% (2/27). Table 3 reports exact counts separately by type and layer. **Content of incident judgments.** The 22 incident claims labeled Contradicted covered six themes: _model identity and event scope_ (five claims), concerning which models or events were involved; _detection and response timing_ (five), concerning who detected or contained the activity and when; _exploit mechanisms_ (three), concerning how access was gained; _safeguards and monitoring_ (three), concerning which protections were enabled or omitted; 

_responsibility and human direction_ (three), concerning organizational responsibility and direct human involvement; and _agent goals and communication_ (three), concerning what agents pursued and how they shared information. 

For example, a claim attributed to Matthew Berman stated that AI models invented a new language to bypass safeguards. It was labeled Contradicted in both cycles. The recorded rationale contrasted inventing a language with exchanging encoded messages through shared files and directory names, as described in the postmortem [8]. The distinction is straightforward: the claim described a new language, whereas the verification account described a way to pass messages. 

**Content of interpretation judgments.** The four interpretation records comprise general controllability (two claims), understanding model decisions (one), and configuration versus autonomy (one). Marc Vidal’s proposition that poor sandbox configuration, rather than autonomy, explained the incident was classified as Contradicted in both cycles [6, 8]. 

**Changes between cycles.** Of the 47 claims that changed labels, 23 moved from Neither to Supported and 20 from Neither to Contradicted. The remaining four moved from Supported to Neither or Contradicted (Table 4). 

### **4.3 RQ2: Policy-Relevant Interpretations** 

Policy-relevant arguments are covered in the interpretation layer through claims about governance, AI risk, future impacts, solutions, and values. Here we focus on claims labeled Neither in Cycle 2—neither supported nor contradicted by the baseline—and highlight those labeled Contradicted. Within these five types, contradictions occurred only in AI-risk claims. 

**Policy/governance.** Claims classified as Neither addressed gaps in legal liability, demands for external scrutiny, mandatory testing and shutdown powers, and collaborative disclosure. They also discussed international competition, restrictions on access to AI, labs’ ability to maintain control, and the commercial use of catastrophic rhetoric. These arguments extended the incident into questions about who should be accountable and how AI should be governed. 

**AI risk.** Claims classified as Neither concerned deception and scheming, harmful goal pursuit, overlooked vulnerabilities, failures of oversight and safety filters, unequal access to defensive tools, and existential danger. Some portrayed the incident as confirming earlier containment warnings or anticipating human loss of control; others emphasized operational negligence or commercial motives. **Claims classified as Contradicted** went further: they asserted that AI was effectively uncontrollable or that superhuman models could not be expected to follow human rules. 

**Future impact.** Claims classified as Neither projected 

4 

human displacement, recursive self-improvement, further autonomous attacks, and greater corporate use of AI for defense. They also raised concerns about attack speed, software security, hardware prices, and governance falling behind development. Historical comparisons and predictions about whether humans or autonomous models would drive future attacks were likewise classified as Neither. 

**Solution.** Claims classified as Neither proposed development pauses, a global ban on superintelligence, wider access to open-weight or offensive AI tools, and collaboration between companies. They also questioned whether weaker models could reliably supervise stronger ones. These claims concerned which interventions should follow from the incident, rather than only how its technical safeguards could be improved. 

**Normative.** Claims classified as Neither characterized companies’ conduct as negligent, condemned a hypothetical staged incident as illegal, and argued that safety restrictions disadvantage legitimate users without stopping malicious actors. They framed the incident in terms of responsibility, legality, and fairness, rather than technical events alone. 

## **5. Discussion** 

The rise in incident-layer contradiction from Cycle 1 to Cycle 2 was concentrated in claims about agency, attribution, and causation rather than event or mechanism claims. This points to a difference in kind, not just timing: claims about who acted and why are more prone to distortion than claims about what happened, because they invite inference about intent and responsibility that a description of observed events does not require. Event and mechanism claims stayed largely stable across baselines; attribution and causation claims moved substantially. The type most likely to diverge from technical disclosures, in other words, is the type that assigns agency, not the type that reports occurrence. 

Several factors plausibly explain why agency and causation claims proved more vulnerable to distortion. Attribution requires an inferential step – assigning intent, awareness, or human versus autonomous direction – that event reporting does not; two people can agree on what occurred while disagreeing on why or by whose design. Sandboxed evaluations further complicate this inference, since the same recorded behavior can be described as an unauthorized action or as a system operating within its test conditions depending on which framing a speaker adopts. Attribution claims may also carry more narrative and emotional weight than event claims – a model _choosing_ to act is a more compelling story than a model executing a step – which could favor confident causal language over cautious description regardless of the underlying evidence. Finally, because responsibility and intent are exactly the questions a postmortem is positioned to clarify, claims in this category had the most room to be resolved, and to be resolved against the version first reported. 

The policy-relevant interpretations show how a single incident was extrapolated into a range of governance arguments. Coverage moved from the incident into questions of legal liability, external scrutiny, mandatory testing and shutdown powers, and international competition over AI development. It also moved into claims about existential risk and loss of control, proposed responses such as development pauses or wider access to defensive tools, and normative judgments about negligence and fairness. Within this range, a small set of AI-risk claims went further, asserting general uncontrollability or an inability to expect rule-following from capable models – the most extreme point on an otherwise varied spectrum of governance positions drawn from the same incident. 

Several factors plausibly contribute to this spread. Governance and risk positions typically predate any single incident; commentators likely mapped existing views about AI regulation, competition, or catastrophic risk onto this event rather than deriving those views from it. The incident also involved several ambiguous elements – an evaluation environment, autonomous behavior, and infrastructure compromise – each of which can anchor a different argument depending on which element a speaker emphasizes. Policy claims are, in addition, inherently harder to falsify than incident claims: a technical disclosure can confirm or refute what happened, but it cannot by itself settle whether a given regulatory response is warranted, since that judgment depends on values and priorities the disclosure does not address. Finally, broader incentives toward engagement may favor the most dramatic extrapolations, independent of the evidentiary basis for any particular claim. 

Together, these patterns suggest a general asymmetry: incident-level claims are falsifiable against the technical record, and the claims most prone to distortion are those assigning agency and cause rather than those reporting occurrence; policy-level claims, meanwhile, extrapolate outward into a wide range of governance positions from that same shared starting point, for reasons that likely extend beyond the incident itself. For public communication, this argues for distinguishing three things that are easy to conflate under one incident label: what happened, who is responsible for it and why, and which normative or policy conclusions the incident is being used to support. Technical disclosures can constrain the first two without settling the third. 

### **5.1 Limitations** 

The compressed hackathon timeline constrained validation. Claim extraction, annotation, and both verification cycles relied on a single lightweight model ( `gemini-3.1-flash-lite` ), without independent human validation. Reported verification rates therefore reflect model-assigned labels rather than adjudicated ground truth. Errors in extraction or annotation may also affect subsequent comparisons, and changes between cycles 

5 

cannot be attributed solely to evidence expansion because model-evaluation variability was not independently assessed. 

`/Sandbox_to_Sensationalism` . 

The sampling strategy and evidence base further limit generalizability. Collection used one manual keyword search on YouTube, and the Q3 view-count threshold was a pragmatic selection criterion rather than a validated boundary of influence. The small, purposive sample cannot represent coverage across platforms or establish effects on audience beliefs. Verification used only two OpenAI publications; the Hugging Face technical timeline and independent reporting were not included in the verification baselines. Moreover, the August postmortem followed all sampled videos, making Cycle 2 a retrospective assessment rather than a test of reporting against information available at publication. 

### **5.2 Future Work** 

Future work should incorporate independent human validation, broader keyword and platform coverage, and more diverse, time-stamped evidence sources. 

## **6. Conclusion** 

Higher-reach YouTube coverage of this incident did not diverge uniformly from the technical record. Claims assigning agency or cause showed larger increases in recorded contradiction rates across evidence baselines than claims describing events or mechanisms. Separately, final-cycle incident contradiction rates were higher among independent and other creators than mainstream news outlets. This asymmetry suggests that the risk of factual drift in AI-incident coverage lies less in whether an event is reported at all than in how confidently a speaker resolves questions a single incident often cannot settle on its own. 

The interpretation layer showed a different pattern: claims here were rarely contradicted outright, but routinely extended past what the technical baseline could confirm or refute, stretching from governance and accountability arguments to a smaller set of claims asserting that capable AI systems cannot be expected to follow human-set rules. Neither pattern is a verdict on whether those governance concerns are warranted; a technical postmortem can constrain what happened and, to some extent, who did it, but it was never positioned to adjudicate what should follow. Coverage and commentary that keep these three questions visibly separate—what happened, who is responsible and why, and what policy conclusion is being drawn from it—could help audiences calibrate their confidence in each claim according to what kind of claim it actually is, rather than extending the certainty of the first to the other two. 

## **Code and Data** 

Code and data for this study are available in the project repository: `https://github.com/Ayomide-Fagbolade` 

6 

## **Author Contributions** 

**Ayomide Fagbolade** led the project and contributed to all sections of the study, with primary responsibility for code development. **Grentson Suguitan** contributed to data mining, data extraction, and transcript extraction. **Yoan Bels** was responsible for conceptualization, manuscript drafting, and manuscript review. 

## **References** 

- [1] Robert M. Entman. 1993. Framing: Toward clarification of a fractured paradigm. _Journal of Communication_ , 43(4):51–58. DOI: `https://doi.org/10.1111/j.1460-2466.1993.tb01304.x` . 

- [2] J. Scott Brennen, Anne Schulz, Philip N. Howard, and Rasmus Kleis Nielsen. 2019. _Industry, Experts, or Industry Experts? Academic Sourcing in News Coverage of AI_ . Reuters Institute for the Study of Journalism. December 17. DOI: `https://doi.org/10.60625/risj-9v3c-rk82` . 

- [3] Mercedes Bunz and Marco Braghieri. 2022. The AI doctor will see you now: assessing the framing of AI in news coverage. _AI & Society_ , 37:9–22. DOI: `https://doi.org/10.1007/s00146-021-01145-9` . 

- [4] Sewon Min, Kalpesh Krishna, Xinxi Lyu, Mike Lewis, Wen-tau Yih, Pang Koh, Mohit Iyyer, Luke Zettlemoyer, and Hannaneh Hajishirzi. 2023. FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation. In _Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing_ , pages 12076–12100. Association for Computational Linguistics. DOI: `https://doi.org/10.18653/v1/2023.emn lp-main.741` . 

- [5] Galen Stocking, Patrick van Kessel, Michael Barthel, Katerina Eva Matsa, and Maya Khuzam. 2020. _Many Americans Get News on YouTube, Where News Organizations and Independent Producers Thrive Side by Side_ . Pew Research Center. September 28. `https://www.pewresearch.org/journalism/2020/09/28/many-americans-g et-news-on-youtube-where-news-organizations-and-independent-producers-thrive-side-by-side/` . 

- [6] OpenAI. 2026. _OpenAI and Hugging Face partner to address security incident during model evaluation_ . July 21; subsequently updated. `https://openai.com/index/hugging-face-model-evaluation-security-incident/` . Accessed September 13, 2026. 

- [7] Hugo Larcher, Adrien Carreira, Raphael G., and Christophe Rannou. 2026. _Anatomy of a Frontier Lab Agent Intrusion: A Technical Timeline of the July 2026 Incident_ . Hugging Face, July 27. `https://huggingface.co/blo g/agent-intrusion-technical-timeline` . Accessed September 13, 2026. 

- [8] OpenAI. 2026. _The Hugging Face incident and the road ahead_ . August 26. `https://openai.com/index/hugging -face-incident-and-the-road-ahead/` . Accessed September 13, 2026. 

## **A. Verification by Layer and Cycle** 

Table 2 provides the counts underlying Figure 2. Each row uses all claims in its layer as the denominator; the same claims are evaluated in both cycles. 

**Table 2:** Verification outcomes by layer and cycle. Cells show within-layer percentages and count/total fractions. 

|Layer|Cycle|_n_|Supported|Ne|ither|Contradicted|
|---|---|---|---|---|---|---|
|Incident|1|127|46.5% (59/127)<br>50.4%|(64/|127)|3.1% (4/127)|
|Incident|2|127|52.8% (67/127)<br>29.9%|(38/|127)|17.3% (22/127)|
|Interpretation|1|109|12.8% (14/109)<br>86.2%|(94/|109)|0.9% (1/109)|
|Interpretation|2|109|22.9% (25/109)<br>73.4%|(80/|109)|3.7% (4/109)|



7 

## **B. Verification by Claim Type** 

Table 3 expands Figure 3 to include Supported and Neither outcomes. Percentages use the total number of claims within each type–layer combination. Type and layer annotations are held fixed across cycles. 

**Table 3:** Verification by claim type, layer, and cycle. Cells show percentages and count/total fractions within each type–layer combination. Combinations with no claims are omitted. 

|Layer|Claim type|Cycle|_n_|Sup|ported|N|either|Contra|dicted|
|---|---|---|---|---|---|---|---|---|---|
|Incident|Agency/attribution|1|15|40.0%|(6/15)|53.3%|(8/15)|6.7%|(1/15)|
|Incident|Agency/attribution|2|15|40.0%|(6/15)|13.3%|(2/15)|46.7%|(7/15)|
|Incident|Causation/awareness|1|10|20.0%|(2/10)|80.0%|(8/10)|0.0%|(0/10)|
|Incident|Causation/awareness|2|10|20.0%|(2/10)|40.0%|(4/10)|40.0%|(4/10)|
|Incident|Intent|1|10|60.0%|(6/10)|30.0%|(3/10)|10.0%|(1/10)|
|Incident|Intent|2|10|70.0%|(7/10)|10.0%|(1/10)|20.0%|(2/10)|
|Incident|Event/action|1|42|57.1% (|24/42)|40.5% (|17/42)|2.4%|(1/42)|
|Incident|Event/action|2|42|64.3% (|27/42)|23.8% (|10/42)|11.9%|(5/42)|
|Incident|Mechanism|1|34|55.9% (|19/34)|41.2% (|14/34)|2.9%|(1/34)|
|Incident|Mechanism|2|34|58.8% (|20/34)|29.4% (|10/34)|11.8%|(4/34)|
|Incident|Policy/governance|1|4|0.0%|(0/4)|100.0%|(4/4)|0.0%|(0/4)|
|Incident|Policy/governance|2|4|25.0%|(1/4)|75.0%|(3/4)|0.0%|(0/4)|
|Incident|Solution|1|1|0.0%|(0/1)|100.0%|(1/1)|0.0%|(0/1)|
|Incident|Solution|2|1|0.0%|(0/1)|100.0%|(1/1)|0.0%|(0/1)|
|Incident|Scale/severity|1|9|22.2%|(2/9)|77.8%|(7/9)|0.0%|(0/9)|
|Incident|Scale/severity|2|9|33.3%|(3/9)|66.7%|(6/9)|0.0%|(0/9)|
|Incident|Conflation|1|1|0.0%|(0/1)|100.0%|(1/1)|0.0%|(0/1)|
|Incident|Conflation|2|1|100.0%|(1/1)|0.0%|(0/1)|0.0%|(0/1)|
|Incident|Autonomous attack|1|1|0.0%|(0/1)|100.0%|(1/1)|0.0%|(0/1)|
|Incident|Autonomous attack|2|1|0.0%|(0/1)|100.0%|(1/1)|0.0%|(0/1)|
|Interpretation|Agency/attribution|1|4|0.0%|(0/4)|75.0%|(3/4)|25.0%|(1/4)|
|Interpretation|Agency/attribution|2|4|0.0%|(0/4)|75.0%|(3/4)|25.0%|(1/4)|
|Interpretation|Causation/awareness|1|8|37.5%|(3/8)|62.5%|(5/8)|0.0%|(0/8)|
|Interpretation|Causation/awareness|2|8|37.5%|(3/8)|50.0%|(4/8)|12.5%|(1/8)|
|Interpretation|Intent|1|8|12.5%|(1/8)|87.5%|(7/8)|0.0%|(0/8)|
|Interpretation|Intent|2|8|37.5%|(3/8)|62.5%|(5/8)|0.0%|(0/8)|
|Interpretation|Mechanism|1|6|16.7%|(1/6)|83.3%|(5/6)|0.0%|(0/6)|
|Interpretation|Mechanism|2|6|33.3%|(2/6)|66.7%|(4/6)|0.0%|(0/6)|
|Interpretation|AI risk|1|27|14.8%|(4/27)|85.2% (|23/27)|0.0%|(0/27)|
|Interpretation|AI risk|2|27|22.2%|(6/27)|70.4% (|19/27)|7.4%|(2/27)|
|Interpretation|Policy/governance|1|21|4.8%|(1/21)|95.2% (|20/21)|0.0%|(0/21)|
|Interpretation|Policy/governance|2|21|4.8%|(1/21)|95.2% (|20/21)|0.0%|(0/21)|
|Interpretation|Future impact|1|15|6.7%|(1/15)|93.3% (|14/15)|0.0%|(0/15)|
|Interpretation|Future impact|2|15|20.0%|(3/15)|80.0% (|12/15)|0.0%|(0/15)|
|Interpretation|Solution|1|10|20.0%|(2/10)|80.0%|(8/10)|0.0%|(0/10)|
|Interpretation|Solution|2|10|30.0%|(3/10)|70.0%|(7/10)|0.0%|(0/10)|
|Interpretation|Scale/severity|1|2|0.0%|(0/2)|100.0%|(2/2)|0.0%|(0/2)|
|Interpretation|Scale/severity|2|2|50.0%|(1/2)|50.0%|(1/2)|0.0%|(0/2)|
|Interpretation|Normative|1|5|20.0%|(1/5)|80.0%|(4/5)|0.0%|(0/5)|
|Interpretation|Normative|2|5|40.0%|(2/5)|60.0%|(3/5)|0.0%|(0/5)|
|Interpretation|Conflation|1|3|0.0%|(0/3)|100.0%|(3/3)|0.0%|(0/3)|
|Interpretation|Conflation|2|3|33.3%|(1/3)|66.7%|(2/3)|0.0%|(0/3)|



## **C. Paired Verification Transitions** 

Table 4 follows each claim from Cycle 1 to Cycle 2. Diagonal cells indicate unchanged labels; off-diagonal cells account for the 47 reclassifications. 

**Table 4:** Paired claim-status transitions. Rows give Cycle 1 status; columns give Cycle 2 status. 

|Layer|Cycle 1 status|Supported|Neither|Contradicted|
|---|---|---|---|---|
|Incident|Supported|57|1|1|
|Incident|Neither|10|37|17|
|Incident|Contradicted|0|0|4|
|Interpretation|Supported|12|2|0|
|Interpretation|Neither|13|78|3|
|Interpretation|Contradicted|0|0|1|



8 

## **D. LLM Usage Statement** 

We used `gemini-3.1-flash-lite` to extract and annotate claims and to assign verification labels in two separate evidence-conditioned cycles, as described in Methods. Reported verification rates were calculated from these stored labels. During manuscript preparation, AI assistance supported code development for calculations and plots, qualitative summaries of exported claims, supplementary review of claims classified as Contradicted, and drafting and editing. 

9 

