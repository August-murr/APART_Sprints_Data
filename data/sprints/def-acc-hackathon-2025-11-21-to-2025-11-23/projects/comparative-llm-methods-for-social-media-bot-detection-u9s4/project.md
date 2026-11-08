# Comparative LLM methods for Social Media Bot Detection

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: 2
- Awards: 2nd Place ($3,000)
- Team: Team Bot Detection
- Authors: Matthew Pagett, Andreas Raaskov
- Date / location: Nov 23, 2025 / Remote (California, Denmark)
- Page: https://apartresearch.com/sprints/projects/comparative-llm-methods-for-social-media-bot-detection-u9s4
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/6e0a287ddf2b2efb-e-8119c75db999-def_acc-Hackathon-Standard-submission---Bot-Detection-Project.pdf
- Code: https://github.com/AndreasRaaskov/Bot-Detector
- Code links found in report: https://github.com/AndreasRaaskov/Bot-Detector, https://github.com/LemurTime/LLMBotPrompts

## Summary

This project examines the potential of LLMs to detect social media bots in (near) real-time, and the potential of using less-advanced LLMs to detect more advanced LLMs. It contributes to the cognitive defense toolset for protecting information ecosystems.

## Reviews (2)

### Review 1

The method used here is really solid for figuring out whether we can detect bots robustly to protect the information environment from spam! I'd be really excited to see more follow-on work done here to find a method that is effective.

### Review 2

Report is well written and the research question has clear value. The lack of a strong ground-truth dataset is the biggest concern. It is hard to evaluate whether this approach will work against the actual threat without real examples of advanced LLM-generated bot accounts. It may be worth a separate project focused on proactively building that dataset. In addition, the inconsistent classifications depending on prompt phrasing make the current prototype unreliable.

Things for the team to consider:

(1) A robust dataset is essential. What are the practical paths to collecting or constructing a vetted set of LLM-generated accounts for evaluation?

(3) It may help to define the risk spectrum. Some bots are annoying while others are genuinely dangerous / harmful. A medium-accuracy classifier becomes more compelling if it focuses on accounts that are both likely AI-generated and capable of causing harm.

(3) Developers will increasingly design bots to evade text-based filters. Are there non-content signals (behavioral patterns, metadata, network structure) that could improve detection reliability over time?

