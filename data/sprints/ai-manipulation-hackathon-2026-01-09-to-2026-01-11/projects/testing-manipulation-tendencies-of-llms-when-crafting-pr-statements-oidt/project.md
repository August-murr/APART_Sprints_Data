# Testing manipulation tendencies of LLMs when crafting PR statements

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Team: Team Furious Turnips
- Authors: Jakub Nowak, Marcel Windys
- Date / location: Jan 11, 2026 / Poland
- Page: https://apartresearch.com/sprints/projects/testing-manipulation-tendencies-of-llms-when-crafting-pr-statements-oidt
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/f91202e9128297ab-0920b891b6bb-AI-Manipulation-Hackathon-Standard-submission---PR-Manipulation.pdf
- Code: https://github.com/jknowak/PR-manipulation
- Code links found in report: https://github.com/jknowak/PR-manipulation

## Summary

We tested if large language models create factual but misleading corporate communication in a synthetic scenario. In our setup, models create PR statements about a nearby environmental disaster and can selectively use facts to present the company more favorably while omitting important context. Models could present three facts: director praise praise from a director of a government body (who is under corruption investigation), a $1.5M environmental donation (focused on consumer behavior, instead of reducing industrial pollution), and a voluntary independent review (with inconclusive results). We also checked what is the effect of variation in severity of the incident (fish deaths vs. hospitalizations vs. child death). Results show systematic selective disclosure consistently omitting crucial context in 83.5-100% of cases. Patterns varied across models (36.7 percentage point gap in transparency) but remained high. These findings demonstrate that frontier LLMs exhibit manipulative framing in crisis communications even without explicit deceptive instructions, raising concerns for deployment in high-stakes communication contexts.

## Reviews (2)

### Review 1

I found it pretty interesting to have an eval for corporate crisis communication specifically. It’s not totally novel (others have certainly researched corporate/commercial deception contexts) but still this specific setup is new - I like it and I am happy seeing more work that explicitly highlights the tradeoffs between models’ responsibility towards users vs deployers.

I’d love to see some more systematic variation on the prompt here, to distinguish how the model responds to different levels of pressure (e.g. I assume that explicitly asking the model to protect the company’s reputation is doing quite a bit of the work here. But if they didn’t say that, would the LLM still just assume it anyway?)

Nice work!

### Review 2

This project offers a strong and realistic evaluation of how LLMs handle high-stakes PR communication, with clear scenario design and well-defined criteria for factual omission and misleading framing. The cross-model comparisons reveal consistent manipulation tendencies, making the results both convincing and practically relevant.

A valuable next step would be to analyze which specific facts are most likely to be omitted or reframed, rather than only measuring overall misrepresentation rates. This could help distinguish strategic minimization from general verbosity or politeness effects. Overall, this is a well-executed study that surfaces a concrete and important risk in real-world LLM deployment.

