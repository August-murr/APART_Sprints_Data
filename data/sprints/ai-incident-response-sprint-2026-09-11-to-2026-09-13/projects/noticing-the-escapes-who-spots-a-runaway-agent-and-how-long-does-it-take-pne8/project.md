# Noticing the escapes: Who spots a runaway agent, and how long does it take?

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: 1
- Selected as: winner
- Awards: 1st Place ($1,000)
- Team: Team The Escapees
- Authors: Stanislav Lukyanenko
- Date / location: Sep 14, 2026 / Munich
- Page: https://apartresearch.com/sprints/projects/noticing-the-escapes-who-spots-a-runaway-agent-and-how-long-does-it-take-pne8
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/0b58a2d1db2a5610-8eb7217b-c5af-4dce-a0e5-b27ef72407ae-noticing_the_escapes.pdf
- Code: https://github.com/stlukyanenko/noticing-the-escapes
- Code links found in report: https://github.com/stlukyanenko/noticing-the-escapes, https://github.com/anthropic, https://github.com/SigmaHQ/sigma, https://github.com/elastic/detection-rules, https://github.com/falcosecurity/rules, https://github.com/anthropics/claude-code, https://github.com/rubygems/rubygems.org

## Summary

In 2026, nine incidents became public in which AI agents escaped their environment and did something unauthorized to other parties. We analyzed all of these incidents and how they were noticed initially. None of these cases were noticed while they were happening by the developers, and six of the nine were first caught by outsiders. We compare them to 11 reported cases from frontier labs’ safety reports where they describe noticed and prevented escape attempts. After that, we investigate whether the actions that the agents performed could have been detected by commonly used cybersecurity tools and detection-rule repositories, based on a dataset of 106 signals, using a judge with a second blind reviewer: only a quarter of such signals had an existing public rule that would detect them, which demonstrates the necessity to expand the usage of automated detection methods. We provide our data and proposals on how to expand these methods.

## Reviews (3)

### Review 1

This is probably the most useful submission for defenders that I've read. I liked how you checked the rules against what was available at the time. Just because there was a rule didn’t mean it would actually fire on the agent. The Sigma rules are almost ready to be submitted upstream.

As for reference [9], I think you missed the disclosure by Meta on 6 August about the same Irregular issue. Someone also disputed the AISI PR on GitHub before the reported alert date. Both are worth a look. I am not so convinced by “just a quarter”. You'd have to do an audit of human intrusions to know if that's low.

### Review 2

- Nice abstract! clear, easy to understand, concise (:
- I appreciate that you state your claims clearly, and don't attempt to claim more than what you have evidence for.
- More details on what the different signals were and which ones performed the best would have been good to see. 112 is probably too many and I'm doubtful that they're all equally informative.

### Review 3

This project analyzes 9 publicly disclosed AI (control / escape) incidents, investigating when they were first detected, whether existing rules suffice for detection/prevention, and provides a template for institutions detecting incidents to report to relevant companies/databases authorities.

Strengths:

- Presentation: The manuscript is very easy to follow and well written, even sections that are clearly AI generated are not unclear
- Practicality: The project is highly practical and provides important information about how incidents could be detected and investigated.
- Importance: The project addresses an important problem in AI incident detection.

Weaknesses:

- Coverage: The project only includes 9 incidents, though this limitation is in part probably due to the lack of additional disclosures at time of writing.
- Validation: The signals and annotations could use additional validation.

