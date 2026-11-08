# TheWizard

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: 4
- Awards: 4th Place ($1,000)
- Team: Team Oz Labs
- Authors: Guy Nachshon, Zack Zornstain
- Date / location: Nov 23, 2025 / Tel Aviv
- Page: https://apartresearch.com/sprints/projects/thewizard-u2dk
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/e8459db61e4157dd-2e4c32c8-9eba-40a2-9fac-edf81ce70107-TheWizard.pdf
- Code: https://github.com/ozlabsai/TheWizard/

## Summary

TheWizard is a tiny cyber world model built to defend systems against AI agents. TheWizard constructs a symbolic digital twin of an environment and simulates how agents plan and act—files touched, logs queried, credentials accessed—to generate 10–20 plausible futures from any partial trajectory. If an agent’s predicted path contains harmful intent, TheWizard blocks it before execution. Powered by HRM-, TRM-, and VibeThinker-inspired reasoning enhancements, our 10–20M model brings anticipatory defense, agent-misuse detection, and multi-step threat prevention to edge devices.

## Reviews (2)

### Review 1

Interesting idea! Would be keen to see how this works in cases where the user genuinely wants to perform actions which are suspicious. The current setup seems to indicate that it might block those requests all the time, making it frustrating for the user, and more likely they would turn it off.

### Review 2

As a proof-of-concept, TheWizard shows promising groundwork.

It would help to include a brief note about operational cost. How often does Wizard need to run predictions, and how does that scale with agent complexity? Clarifying this would help assess compute cost vs. benefit.

I would also like to see a clearer articulation of the deployment model. Who runs the digital twin and where does it sit relative to the agent? A bit more framing around the types of high-stakes domains this is intended for would make the real-world value even more concrete.

