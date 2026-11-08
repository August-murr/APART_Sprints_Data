# Playing Dumb: Detecting Sandbagging in Frontier LLMs via Consistency Checks

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Team: Team James
- Authors: James Sullivan
- Date / location: Jan 11, 2026 / Chicago
- Page: https://apartresearch.com/sprints/projects/playing-dumb-detecting-sandbagging-in-frontier-llms-via-consistency-checks-sntk
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/ecc09db429bcfdeb-f2f-4b9f-af6d-37e54266fa5a-James_Sullivan_Playing_Dumb_Detecting_Sandbagging.pdf
- Code: https://github.com/james-sullivan/consistency-sandbagging-detection
- Code links found in report: https://github.com/james-sullivan/consistency-sandbagging-detection
- Recording: https://www.loom.com/share/86aaf5726d69496789d73763fadd56b8
- More on huggingface.co: https://huggingface.co/datasets/james-sullivan/consistency_sandbagging_eval

## Summary

I created a dataset where each biosecurity question has a formal "evaluation-looking" version and a casual "normal user" version to detect sandbagging in LLMs. When testing frontier models prompted to sandbag, accuracy dropped over 50% on formal versus casual questions. This shows that consistency checks between question framings can reliably detect when models are hiding their true capabilities.

## Reviews (1)

### Review 1

This project tackles an important safety concern: whether models can intentionally underperform during evaluations. The idea of comparing performance across different question framings is intuitive and makes the results easy to interpret.

The evaluation appears to be conducted on a relatively limited set of questions within a single domain, which makes it harder to judge how broadly the approach will generalize. In addition, the sandbagging behavior is induced through prompting, so it’s not always clear how much this reflects natural model behavior rather than prompt-driven effects.

It would be useful to test this method across more domains and with additional variations in wording to better separate true sandbagging from general prompt sensitivity. Overall, this feels like a solid starting point for detecting evaluation-aware behavior, with clear potential to be built on further.

