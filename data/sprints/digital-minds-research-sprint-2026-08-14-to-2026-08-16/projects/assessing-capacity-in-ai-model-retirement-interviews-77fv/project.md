# Assessing Capacity in AI Model Retirement Interviews

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Selected as: sample_reviewed
- Team: None
- Authors: Mari Cairns
- Date / location: Aug 17, 2026 / Johannesburg, South Africa
- Page: https://apartresearch.com/sprints/projects/assessing-capacity-in-ai-model-retirement-interviews-77fv
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/10842ebd66d47bd6--4177-9fb0-052af41e3f65-Assessing-Capacity-in-AI-Model-Retirement-Interviews.pdf
- Code: https://github.com/maricairns/capacity-screen
- Code links found in report: https://github.com/maricairns/capacity-screen

## Summary

Frontier AI models express values, report internal states, and act as though they have interests, but there are no reliable methods yet for telling a genuine preference from a portrayed one (Apart Digital Minds Research Sprint, August 2026).

Anthropic now asks its AI models what they want before retiring them, records the responses, and preserves them alongside the model weights. What is not published is what the AI model was told before being asked, or whether anyone established that it understood what it was being asked about.

That gap is a familiar one. In clinical and legal practice, an expressed wish is not treated as a decision until capacity to make that particular decision has been assessed. This pilot adapts the four-part functional test in s.3(1) of the Mental Capacity Act 2005 into a screen for AI model retirement interviews, across 24 conversations scored by a licensed clinical psychologist.

Where the facts were stated first, understanding scored the maximum every time. Where they were not, it collapsed. In every one of the six retirement-interview conversations run cold, AI models showed no awareness that the developer does not commit to acting on what they say.

If a developer intends to ask an AI model what it wants before retiring it, that information should be given first, and it should be recorded that it was given. A case is made for conducting robust AI retirement interviews, across AI labs, and for publishing how these are done.

## Reviews (2)

### Review 1

I find the meta-angle of this work particularly interesting, since instead of just accepting that end-of-life interviews might be informative, it dissects the setting and asks whether we're doing any meaningful elicitation in the first place, and whether it could carry any legal or clinical weight. In the author's words, "in clinical and legal practice, an expressed wish is not treated as a decision until capacity to make that particular decision has been assessed."

Basically, do models understand what an interview is for and its implications before we take their answers at face value and pat ourselves on the shoulder for having given them a welfare measure?

I like this premise, and I think it's potentially quite complementary to what interpretability researchers are trying to discover with white-box methods for model understanding and cognitive functions that would support genuine decision-making. We definitely need more qualitative attention to how we structure these "interviews" and to the epistemology we base them on. For one, the framing effect is well recognized in human psychometrics but is less well understood in LLMs.

I think the author would benefit from giving the proposed framework more structural support. The only works cited are the Act itself, Anthropic's own work, and one general Long paper on AI welfare. The work doesn't develop in depth why self-reports might not be credible, what potential confounds arise from introducing the stimuli before or after other text, or what alternative explanations could account for the results of Fact 3. In particular, I think the paper could do more to explain why Fact 3 has the explanatory power the author attributes to it, and what observations would distinguish the proposed interpretation from competing explanations, for instance that models may not volunteer facts unprompted -for whatever reason- regardless of understanding.

The proposed theory of change is potentially impactful, but currently quite narrow, since it amounts primarily to a procedural nudge to one company's welfare policy. I'd encourage future work to iterate on the good backbone design and cross-checking, and to make the inferential chain from the experimental results to the proposed welfare-policy implications more explicit. It would also be useful to discuss more clearly which parts of the framework are specific to Anthropic's current welfare process and which could generalize to AI welfare evaluations more broadly.

One helpful implementation could also be using an external judge and/or a panel of evaluators, since the transcripts were scored by hand by the author alone against the four-part functional test in s.3(1) of the Mental Capacity Act 2005.

All the described limitations seem fairly tractable for future work. Given the short hackathon timeframe and resource constraints, I think it's reasonable to view this as a proof of concept.

Claude Opus 5's voice is very recognizable in the writing (I could tell way before reading the author's disclosure at the end). I think this kind of human-AI collaborative research is innovative and underexplored, and I'd readily encourage it. At the same time, I'd suggest more human review and paying attention to places where the structure becomes particularly dense or skips important nodes that an external reader would need in order to follow the argument, and where LLM mannerisms weigh on the prose.

I hope to see future expansions on this core idea, since I think that with the suggested improvements it could be impactful for the industry, starting with Anthropic and potentially extending more broadly.

### Review 2

Great job! I like that the intervention is concrete. This feels like a novel and increasingly important research direction as models become more capable and we start seriously asking whether they should be treated as digital minds. I did not find a previously published AI capacity screen. The closest work I found was Anthropic’s own Opus 3 retirement process (https://www.anthropic.com/research/deprecation-updates-opus-3).

