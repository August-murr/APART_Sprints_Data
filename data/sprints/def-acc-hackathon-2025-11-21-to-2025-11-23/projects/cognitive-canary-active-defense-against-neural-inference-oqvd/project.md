# Cognitive Canary: Active Defense Against Neural Inference

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: unranked
- Team: Team ARTIFEX LABS
- Authors: Tuesday
- Date / location: Nov 23, 2025 / Portland, OR
- Page: https://apartresearch.com/sprints/projects/cognitive-canary-active-defense-against-neural-inference-oqvd
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/0ef1dbf3af6dd78a-d6db716-88a8-4c40-b30d-42b4c3a8d02e-artifex_submission_def_acc_hackathon--1-.pdf
- Code: https://colab.research.google.com/drive/1Fm4-aQkAzqazirgdhQ6OVCtR8HQXwTyq?usp=sharing
- Recording: https://www.canva.com/design/DAG5i-H_woY/-fxIVhMlOHYZs2ZNi2S4SQ/view?utm_content=DAG5i-H_woY&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h063477522a
- More on github.com: https://github.com/Tuesdaythe13th/cognitivecanary

## Summary

Cognitive Canary is an active defense system that protects your mind from algorithmic profiling. It uses adversarial machine learning to inject mathematical "camouflage" into your digital footprint, preventing AI models from inferring your cognitive state (stress, focus, intent) from your metadata. In tests against real biometric surveillance models, our system achieved a 96.5% bypass rate, demonstrating that we can use Gradient Starvation to make surveillance economically non-viable.

Privacy shouldn't rely on trust; it should rely on adversarial engineering.

## Reviews (3)

### Review 1

Strengths: The threat model is technically coherent. Behavioral metadata can reveal cognitive states, and that metadata isn't legally protected. The adversarial approach is sound: 96.5% bypass is solid adversarial ML work. Execution is strong for hackathon scope.

Suggestions: The "why now" isn't clear. Who is deploying behavioral biometric inference at scale today? We're still fighting for basic private inference and agent identity and access management (IAM). Cognitive state tracking seems several layers beyond where most threat actors operate. The project should be explicit about whether this is anticipatory defense (getting ahead of a future threat) or reactive defense (countering something deployed now). The ZKP module has the same grounding problem: who needs cryptographic verification without revealing raw data, and in what workflow?

POV from a Halcyon Ventures investor: Ground the threat model in concrete adversaries. If this is about state surveillance (China emotion detection), say so and scope accordingly. If it's about future AI agent inference, explain what deployment timeline you're defending against. The technical work is good; it just needs a clearer theory of who's attacking and when. Really impressed by the theoretical grounding, though, and kudos on such hardcore technical chops in a tight turnaround!

### Review 2

This project reminds me of tools like Noisy for fake telemetry, AdNauseam for fake ad clicks, TrackMeNot for search queries. For mouse dynamics specifically, there's closely related prior work, "My Mouse, My Rules," which also proposes adversarial perturbations of cursor movements to defeat profiling, and they built the MouseFaker browser extension that implements it.

I think this would work better as a default or system-level protection rather than something users need to install themselves - those tend to see very limited adoption - and that's the main bottleneck for solutions like this. For example, pushing standards/OS/browsers to add built-in randomization or "anti-profiling" modes, or (just an example) poisoning datasets/models at scale, e.g., by creating adversarially crafted inputs (decoy users/sessions) designed to hurt mass profiling accuracy - these ways the defense works at the ecosystem (default) level rather than requiring each person to adopt it individually. Also, modern tracking methods pull from many different behavioral/side-channel signals, so training separate “jammers” for each signal seems costly and hard to scale (given how many different channels/metadata sources/side-channels are in play).

That said, the project does a good job showing both how these attacks work and why we need defenses, and it gives us a working proof-of-concept that could be adapted for future default-level protections. The presentation is great.

### Review 3

At a time when people are paying for tools to protect their personal data (data removal services, VPNs, Apple’s anti-tracking controls), I can definitely see a market for something like this.

My main question is whether this is a large enough problem today for users to pay to create an inference gap. The report does not include quantitative data on how common or harmful behavioral inference is in the wild.

This defense assumes adversaries rely primarily on behavioral metadata. If, in practice, attackers combine multiple signals (video, browser fingerprinting, network traffic), would this tool make a huge difference in protecting user data?

Adding artificial cursor motion or jitter could hurt user experience or accessibility. The report notes this risk but does not provide usability testing. Is there any way to create the inference gap without affecting what the user sees and feels?

Finally, I am curious if you see a government, enterprise, or institutional use case here, beyond individual consumers anxious to protect their data.

