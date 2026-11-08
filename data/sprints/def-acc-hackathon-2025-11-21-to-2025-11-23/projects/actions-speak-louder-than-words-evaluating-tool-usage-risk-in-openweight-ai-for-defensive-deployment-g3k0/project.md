# Actions speak louder than words: Evaluating Tool Usage Risk in Open-Weight AI for Defensive Deployment

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: 3
- Selected as: winner
- Awards: 3rd Place ($1,500)
- Team: Team Actions speak louder than words
- Authors: Ana Belen Barbero Castejon, Carlos Vecina Tebar
- Date / location: Nov 23, 2025 / Spain
- Page: https://apartresearch.com/sprints/projects/actions-speak-louder-than-words-evaluating-tool-usage-risk-in-openweight-ai-for-defensive-deployment-g3k0
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/3fc61c6b8a85fe85-words_-Evaluating-Tool-Usage-Risk-in-Open-Weight-AI-for-Defensive-Deployment.pdf
- Code: https://github.com/AnaBelenBarbero/OW-AI-cyber-bio-actions-eval
- Code links found in report: https://github.com/AnaBelenBarbero/OW-AI-cyber-bio-actions-eval, https://github.com/microsoft/evodiff
- More on ow-ai-cyber-bio-actions-eval.streamlit.app: https://ow-ai-cyber-bio-actions-eval.streamlit.app/

## Summary

Open-weight language models are increasingly deployed in agentic workflows where they can invoke external tools, creating new attack vectors beyond traditional text generation. We present a systematic evaluation framework that measures how model tampering affects tool-usage behavior across cybersecurity, bioengineering, and decision-making domains. Evaluating 10 model variants (5 base + 5 tampered) across 125 scenarios, we find statistically significant that tampering increases harmful tool invocation rates, with effects varying significantly by domain. Our framework, released as open-source with an interactive dashboard, provides a foundation for monitoring AI agent behavior in production deployments and highlights tool-usage / MCP security as a critical defensive intervention point. (https://github.com/AnaBelenBarbero/OW-AI-cyber-bio-actions-eval)

Keywords: AI tools security, open-weight models, model tampering, agentic AI

## Reviews (2)

### Review 1

This is a helpful exploration of an important set of questions: tool usage could be a key threat vector and it's great that you have put the time in to carefully evaluate this. It has clear relevance for AIS. The abliterations are welcomed, as are the coverage of multiple domains and statistical rigour. And tool usage monitoring could be the right solution here. The execution is also solid, and it was helpful to see the dashboard - the one flag here is the '-1%' success rate that appeared for GPT-OSS in two instances. Was this just a rendering issue? It would also be helpful to read more about what should be done about the results you identify - though of course that would be difficult to complete in a weekend.

I think (low-confidence) that you're correct on looking into MCP gateways as a next step. Some other things you could do:

- Include scenarios with subtle or implicit malicious framing that aren't just explicit instructions
- Test on llama models
- Add a policy engine to enforce rules based on risk levels and contexts + perhaps an alerting mechanism

### Review 2

Strong prototype and written report does a great job to shift thinking about AI risk from what models say to what models do. Also appreciate the great title and inclusion of a real-world case.

For this project, I would appreciate seeing a short literature review just to show that this research is not repeating work happening elsewhere. I would also like a slightly firmer argument for why open-weight models are higher risk.

Team clearly outlined application to a variety of domains. Next step would be to anchor one of those in a more realistic scenario and show how this evaluation framework would identify and quantify risk in a real setting. With such a robust report, I'd like to see an example of what a final deployment would look like.

