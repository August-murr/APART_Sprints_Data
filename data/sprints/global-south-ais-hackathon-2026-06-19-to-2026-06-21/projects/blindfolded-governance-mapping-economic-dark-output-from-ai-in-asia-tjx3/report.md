# **Blindfolded Governance: Mapping Economic Dark Output from AI in Asia**<sup>**1**</sup> 

Mahi H Shah Independent 

**With** 

Apart Research 

## **Abstract** 

AI is making informal and self-employed workers across Asia more productive, yet this productivity gain often leaves no trace in GDP, tax records, or labour statistics, a phenomenon recently termed "Dark Output." This work does not attempt to measure Dark Output directly, an exercise that remains infeasible given current data; instead, it constructs the Asia Dark Output Index (ADOI), a composite, pre-emptive proxy for where AI-driven economic activity is most likely to escape formal measurement. ADOI combines four publicly available pillars: informal employment, self-employment, AI task exposure, and digital infrastructure, normalised and weighted across twelve Asian economies. India, Indonesia, Pakistan, and Cambodia emerge as highest-risk. The novel contribution of this work is the first cross-country index to combine informal-economy structure with AI task-exposure data specifically to anticipate measurement blind spots, rather than to assess AI readiness or labour displacement. South and Southeast Asia is the natural focus given the region's unusually high informal employment share alongside rapidly expanding digital infrastructure and AI exposure. The result is a tool for governance under uncertainty: identifying where policymakers are most likely to be acting on an incomplete picture of their own economies. 

> 1 Research conducted at the <u>The Global South AI Safety Hackathon, June 2026</u> 

## **1. Introduction** 

AI is already changing how informal and self-employed workers produce value. However, even if economic value is realised, it leaves no or minimal statistical trace. This gap (AI-driven productivity gains that exist but go uncounted by GDP, productivity statistics, and labour-market monitoring) has recently been termed "Dark Output."<sup>2</sup> Such Dark Output is disproportionately likely to concentrate in lower- and middle-income economies, and within them, especially in South and Southeast Asia. 

Estimating the realised economic value of Dark Output would require observing transactions that are, by definition, not recorded in any administrative dataset. Even adjacent efforts to value uncounted digital activity (such as GDP-B's attempt to quantify the welfare contribution of free digital goods) were built to measure consumer welfare from large platforms,<sup>3</sup> not producer-side informal output spread across millions of individually small transactions. This work does not attempt to measure Dark Output directly; that problem is out of scope for a project of this duration, and it will remain deeply difficult for the foreseeable future. 

However, this sort of measurement gap is not without precedent. Early internet governance faced a similar problem: regulators in the 1990s could see that e-commerce and cross-border data flows were growing, but lacked any reliable way to measure their scale before deciding how (or whether) to regulate them, leading to years of reactive, after-the-fact policymaking once harms had already compounded. A pre-emptive proxy, even an imperfect one, gives policymakers something to act on before the activity is large enough to show up unambiguously in the data it is hiding from. 

The main contributions of this work are: 

- Identifying a small set of observable, currently-available factors (informality, self-employment, AI task exposure, and digital infrastructure) that can be combined to pre-emptively estimate a country's structural propensity for Dark Output, without requiring direct measurement of the phenomenon itself 

- Constructing the Asia Dark Output Index (ADOI), a composite ranking of twelve Asian economies by their relative exposure to this dynamic, built entirely from existing, publicly available cross-country statistics 

- Using the resulting rankings to motivate epistemic governance implications 

> 2 Malcolm Spittler and Dylan Patel. ‘AI Dark Output: The Visible Cost of Invisible Output’. Accessed 21 June 2026. <u>https://newsletter.semianalysis.com/p/ai-dark-output-the-visible-cost-of.</u> 3 Brynjolfsson, Erik, Avinash Collis, W. Erwin Diewert, Felix Eggers, and Kevin J. Fox. ‘GDP-B: Accounting for the Value of New and Free Goods in the Digital Economy’. Working Paper No. 25695. Working Paper Series. National Bureau of Economic Research, March 2019. <u>https://doi.org/10.3386/w25695.</u> 

## **2. Related Work** 

No existing line of work directly uses informal-economy measurement for Dark Output estimation. 

A succession of papers has built increasingly granular methods for estimating which occupations and tasks are exposed to AI capability. Eloundou et al. established that exposure is best measured at the task level rather than the occupation level.<sup>4</sup> The Global Automation Atlas extends this further, building a task-level dictionary across 18,797 tasks and 124 countries (this is the dataset ADOI’s AI exposure pillar draws on).<sup>5</sup> None of these papers, however, ask how exposure interacts with the formality of the labour market into which it lands. 

Other literature establishes that large amounts of real economic value already sit outside formal measurement in developing economies. De Soto's foundational argument is that the poor possess substantial assets and economic activity that remain "dead capital" because they lack the formal legal/representational systems that would let that value be counted, financed, or taxed.<sup>6</sup> Sen's capability approach pushes this further, arguing that development and welfare should be measured through people's real opportunities and capabilities, not through GDP, meaning that AI-driven gains in capability (information access, skill acquisition, market participation) can be real and significant even where they generate no measurable GDP increase at all.<sup>7</sup> 

A body of work, mostly associated with Brynjolfsson and collaborators, has proposed supplementary metrics to GDP for the digital economy.<sup>8</sup> This is an important precedent for the general project of measuring what GDP misses, but its target is different. Dark Output, as used here, is a dual-side, hidden-productivity question that is not accounted for in other methods. 

Even the most directly relevant cross-country AI-and-development literature, such as the IMF's AI Preparedness Index,<sup>9</sup> measure countries' readiness to benefit from AI (infrastructure, human capital, regulation), not their propensity to generate AI-driven output that escapes measurement. 

> 4 Eloundou, Tyna, Sam Manning, Pamela Mishkin, and Daniel Rock. ‘GPTs Are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Models’. arXiv:2303.10130. Preprint, arXiv, 21 August 2023. <u>https://doi.org/10.48550/arXiv.2303.10130.</u> 

> 5 Garg, Prashant, Tommaso Crosta, and Jasmin Baier. ‘Global Automation Atlas’. arXiv:2605.17086. Preprint, arXiv, 16 May 2026. <u>https://doi.org/10.48550/arXiv.2605.17086.</u> 

> 6 De Soto, Hernando. ‘The Mystery of Capital Why Capitalism Triumphs in the West and Fails Everywhere Else. New York Basic Books. - References - Scientific Research Publishing’. 2000. 

> <u>https://www.scirp.org/reference/referencespapers?referenceid=2522378.</u> 

> 7 Frediani, Alexandre Apsan. ‘Sen’s Capability Approach as a Framework to the Practice of Development’. _Development in Practice_ 20, no. 2 (2010): 173–87. 

> 8 Brynjolfsson, Erik, Daniel Rock, and Chad Syverson. ‘Artificial Intelligence and the Modern Productivity Paradox: A Clash of Expectations and Statistics’. Working Paper No. 24001. Working Paper Series. National Bureau of Economic Research, November 2017. <u>https://doi.org/10.3386/w24001.</u> 9 ‘AI Preparedness Index (AIPI)’. Accessed 21 June 2026. <u>https://www.imf.org/external/datamapper/datasets/AIPI.</u> 

## **3. Methods** 

The Asia Dark Output Index (ADOI) is constructed from four publicly available indicators: 

- **Informal employment rate (30% weight).** Sourced from ILOSTAT, using the most recently available year per country.<sup>10</sup> This is the most direct proxy available for Dark Output risk: informal workers, by definition, operate outside the registration, taxation, and labour-force-survey systems that feed GDP and productivity statistics. 

- **Self-employment rate (30% weight).** Sourced from World Bank Open Data.<sup>11</sup> Self-employed and gig workers (freelancers, consultants, small-scale traders) are typically the earliest individual adopters of consumer-facing AI tools, since they personally absorb both the cost and the benefit of new tools with no firm-level IT department, procurement process, or HR policy mediating adoption. 

- **AI task exposure (20% weight, split 10%/10%).** Sourced from the Global Automation Atlas,<sup>12</sup> using general task exposure and high-confidence task exposure as separate sub-components [5]. Both are relevant to Dark Output risk 

- **Digital infrastructure (20% weight).** Sourced from World Bank internet penetration data (% of population),<sup>13</sup> most recent year available per country. This is included as a necessary enabler rather than a driver: AI exposure is a measure of task susceptibility in principle, but task susceptibility cannot translate into actual AI-assisted output without basic connectivity. This is weighted lower than informality/self-employment because infrastructure is necessary but not sufficient. 

Each raw indicator is first min-max normalised across the twelve countries to a common scale, then combined using the weights described above: 





where, for country  and any raw indicator , the min-max normalisation is: 



> 10 ‘Informal Employment Rate - ILOSTAT’. Accessed 19June 2026. 

> <u>https://ilostat.ilo.org/data/snapshots/informal-employment-rate/.</u> 

> 11 ‘Self-Employed, Total (% of Total Employment) (Modeled ILO Estimate) | Data’. Accessed 20 June 2026. <u>https://data.worldbank.org/indicator/SL.EMP.SELF.ZS.</u> 

> 12 Garg, Prashant, Tommaso Crosta, and Jasmin Baier. ‘Global Automation Atlas’. arXiv:2605.17086. Preprint, arXiv, 16 May 2026. <u>https://doi.org/10.48550/arXiv.2605.17086.</u> 

> 13 ‘Individuals Using the Internet (% of Population) | Data’. Accessed 20 June 2026. <u>https://data.worldbank.org/indicator/IT.NET.USER.ZS.</u> 

Here , , , , and denote the normalised informal employment rate, self-employment rate, share of tasks exposed to AI, share of tasks highly exposed to AI, and digital infrastructure (internet penetration) respectively, with weights summing to 1. 

The resulting weighted score is then converted to the final 0 to 100 ADOI scale using z-score standardization followed by a logistic (sigmoid) transformation: 



where is country 's raw weighted score, and are the sample mean and standard deviation across the twelve countries. 

This pulls in extreme scores naturally rather than via an arbitrary hard clip, keeping the index intuitive (low ADOI = least Dark Output potential, high ADOI = most) whilst avoiding the appearance of false certainty at the sample's edges. 

## **4. Results** 

The final ADOI scores are presented below. Countries are ranked from highest to lowest estimated susceptibility to AI-generated Dark Output, reflecting the extent to which AI-enabled productivity gains may occur outside traditional systems of economic measurement. 

#### Table 1. Ranked Asia Dark Output Index (ADOI) scores by country 

|Rank|Country|ADOI score|Rank|Country|ADOI score|
|---|---|---|---|---|---|
|1|India|87.7|7|Vietnam|56.4|
|2|Indonesia|65.4|8|Bangladesh|49.9|
|3|Pakistan|58.4|9|Afghanistan|43.4|
|4|Cambodia|58.1|10|Myanmar|40.6|
|5|Nepal|57.5|11|Sri Lanka|19.3|
|6|Thailand|56.8|12|South Korea|12.4|



To facilitate geographic comparison, Figure 1 visualizes ADOI scores across the study region. 

Figure 1. Geographic distribution of Asia Dark Output Index (ADOI) scores. 



Whilst overall rankings provide a useful summary, they do not reveal the underlying drivers of each country's score. To address this, Figure 2 presents a criterion-level breakdown of the index components for each country. 

Figure 2. Criterion-level decomposition of ADOI scores by country. 



## **5. Discussion and Limitations** 

Within the current sample, India anchors the highest ADOI score. This compounds standard statistical blind spots into a fiscal and social-protection concern of considerable magnitude: even a modest fraction of India's labour force generating AI-assisted, unmeasured output represents a substantial quantity of economic activity moving simultaneously beyond the reach of tax authorities, labour statistics, and social protection systems. 

This is precisely the condition that blindfolded governance describes. Where Dark Output is likely to be largest, the institutions tasked with observing and regulating AI's economic effects, namely statistical agencies, labour ministries, and tax authorities, are the least likely to possess the data needed to do so. A regulator attempting to calibrate AI policy, social protection thresholds, or labour-market interventions using official statistics alone is, in effect, acting on an incomplete picture of the economy it governs, and the size of that gap scales with what ADOI measures. 

Across Asia, this suggests that AI governance built solely on conventional economic indicators risks being calibrated to the visible economy whilst the most consequential shifts occur outside its view, which is the justification for treating pre-emptive, proxy-based estimation (imperfect as it is) as a governance tool in its own right rather than a substitute for measurement still to come. 

### **Limitations** 

Several limitations ought to be acknowledged: The sample comprises only twelve economies, so the ADOI rankings will shift as additional countries are included. Crucially, the exclusion of China reduces regional completeness and may understate the scale of Dark Output dynamics across Asia. 

ADOI also assumes uniform AI utilisation across languages, despite lower-resource languages likely experiencing lower levels of adoption. ADOI’s weighting scheme reflects theoretical judgment rather than empirical calibration, as no ground-truth measure of Dark Output currently exists for validation. 

Finally, the concept itself assumes that economic invisibility is undesirable, whereas some informal activity may remain outside formal systems by preference, independent of AI's influence. 

### **Future Work** 

Future work could expand the index to additional countries and ultimately develop a Global South Dark Output Index (GSDOI). The index itself could be refined through the inclusion of additional indicators, such as microenterprise prevalence. More fundamentally, future research should explore how to directly measure and validate Dark Output rather than merely estimating its likelihood. 

## **6. Conclusion** 

AI will continue to make informal and self-employed workers more productive across Asia (and beyond), yet this productivity gain remains largely invisible to GDP, taxation, and labour statistics. ADOI offers a pre-emptive, replicable proxy for where this blind spot is structurally most likely to emerge. 

As AI adoption accelerates, governance built on incomplete visibility risks regulating an economy that no longer fully exists on paper. 

## **Code and Data** 

All code, data, and supporting materials used in this project are publicly available in the project repository. 

**Repository:** <u>https://github.com/mahihshah/dark-output-adoi</u> 

## **References** 

- Achkar, Souleima El. _Micro and Small Enterprises: Engines of Job Creation_ . 23 June 2023. <u>https://ilostat.ilo.org/blog/micro-and-small-enterprises-engines-of-job-creation/.</u> 

- ‘AI Preparedness Index (AIPI)’. Accessed 21 June 2026. <u>https://www.imf.org/external/datamapper/datasets/AIPI.</u> 

- ‘Automation and New Tasks: How Technology Displaces and Reinstates Labor | NBER’. Accessed 21 June 2026. <u>https://www.nber.org/papers/w25684.</u> 

- Brynjolfsson, Erik, Avinash Collis, W. Erwin Diewert, Felix Eggers, and Kevin J. Fox. ‘GDP-B: Accounting for the Value of New and Free Goods in the Digital Economy’. Working Paper No. 25695. Working Paper Series. National Bureau of Economic Research, March 2019. <u>https://doi.org/10.3386/w25695.</u> 

- Brynjolfsson, Erik, Daniel Rock, and Chad Syverson. ‘Artificial Intelligence and the Modern Productivity Paradox: A Clash of Expectations and Statistics’. Working Paper No. 24001. Working Paper Series. National Bureau of Economic Research, November 2017. <u>https://doi.org/10.3386/w24001.</u> 

- Cerutti, Eugenio, Antonio Garcia Pascual, Yosuke Kido, et al. ‘The Global Impact of AI: Mind the Gap’. _Mind the Gap_ , n.d. 

- Clark, David A. _The Capability Approach: Its Development, Critiques and Recent Advances_ . n.d. 

- De Soto, Hernando. ‘The Mystery of Capital Why Capitalism Triumphs in the West and Fails Everywhere Else. New York Basic Books. - References - Scientific Research Publishing’. 2000. <u>https://www.scirp.org/reference/referencespapers?referenceid=2522378.</u> 

- Eloundou, Tyna, Sam Manning, Pamela Mishkin, and Daniel Rock. ‘GPTs Are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Models’. arXiv:2303.10130. Preprint, arXiv, 21 August 2023. <u>https://doi.org/10.48550/arXiv.2303.10130.</u> 

- Finance and Development | F&D. ‘Finance and Development’. Accessed 21 June 2026. <u>https://www.imf.org/external/pubs/ft/fandd/2001/03/desoto.htm.</u> 

- Frediani, Alexandre Apsan. ‘Sen’s Capability Approach as a Framework to the Practice of Development’. _Development in Practice_ 20, no. 2 (2010): 173–87. 

- Garg, Prashant, Tommaso Crosta, and Jasmin Baier. ‘Global Automation Atlas’. arXiv:2605.17086. Preprint, arXiv, 16 May 2026. <u>https://doi.org/10.48550/arXiv.2605.17086.</u> 

- ‘Individuals Using the Internet (% of Population) | Data’. Accessed 21 June 2026. <u>https://data.worldbank.org/indicator/IT.NET.USER.ZS.</u> 

- ‘Informal Employment Rate - ILOSTAT’. Accessed 21 June 2026. <u>https://ilostat.ilo.org/data/snapshots/informal-employment-rate/.</u> 

- López, L. Julián Lechuga, and Luis Lara. ‘The Invisibility Hypothesis: Promises of AGI and the Future of the Global South’. arXiv:2603.01616. Preprint, arXiv, 3 March 2026. <u>https://doi.org/10.48550/arXiv.2603.01616.</u> 

- Malcolm Spittler and Dylan Patel. ‘AI Dark Output: The Visible Cost of Invisible Output’. Accessed 21 June 2026. <u>https://newsletter.semianalysis.com/p/ai-dark-output-the-visible-cost-of.</u> 

- Rahman, ATM Mizanur, Md Romael Haque, and Sharifa Sultana. ‘DAIEM: Decolonizing Algorithm’s Role as a Team-Member in Informal E-Market’. arXiv:2506.12910. Preprint, arXiv, 15 June 2025. <u>https://doi.org/10.48550/arXiv.2506.12910.</u> 

- ‘Self-Employed, Total (% of Total Employment) (Modeled ILO Estimate) | Data’. Accessed 21 June 2026. <u>https://data.worldbank.org/indicator/SL.EMP.SELF.ZS.</u> 

- ‘Women and Men in the Informal Economy: A Statistical Picture. Third Edition | International Labour Organization’. 30 April 2018. <u>https://www.ilo.org/publications/women-and-men-informal-economy-statistical-picturethird-edition.</u> 

- World Bank Open Data. ‘World Bank Open Data’. Accessed 21 June 2026. 

   - <u>https://data.worldbank.org.</u> 

