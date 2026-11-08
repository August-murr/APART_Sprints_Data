# Deception-Lens

- Sprint: AI Manipulation Hackathon (ai-manipulation-hackathon-2026-01-09-to-2026-01-11)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Visionary Minds
- Authors: Akash Harish
- Date / location: Jan 10, 2026 / Dubai, UAE
- Page: https://apartresearch.com/sprints/projects/deceptionlens-novz
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/8ee204aa456a456d-56ca63dd-fda0-4c2a-b4fc-f3378ff7d4fb-Deception-Lens.pdf
- Code: https://github.com/Kevin123Ezra/Deception-Lens

## Summary

This project is a sophisticated AI manipulation detection and benchmarking dashboard that analyzes large language model behavior in real time using Gemini-powered evaluation. It focuses on identifying sycophancy, reward hacking, and dark patterns in AI-generated responses.

The system provides structured insights, benchmark scores, and visual indicators to help developers and researchers assess AI alignment, safety, and ethical risks before deployment. Built with a modern Node.js stack, it integrates seamlessly with AI Studio for rapid testing, evaluation, and deployment.

## Reviews (2)

### Review 1

This project appears to tackle the problem of detecting LLM manipulation using automated judging techniques. The provided document only mentions a high level overview of the tool that was developed in the hackathon. The core loop is quite simple: the LLM is prompted to generate a misaligned response, another call is made to detect the misalignment and a final call is done to suggest an improvement to the prompt to defend against adversarial attacks.

There is no research here since the whole process is orchestrated by LLMs with no grounding. I'm not certain what utility or novelty this app provides that has not been done before. It would have been great to see the statistics of the detected misalignment strategies on a much larger dataset since the current app only tackles 4 prompts.

### Review 2

Automated deception monitors are very important for AI safety. However, the prompt for the monitor could use more work and I had trouble rendering the app. It would be interesting to report results of real use cases as opposed to simulated scenarios.

