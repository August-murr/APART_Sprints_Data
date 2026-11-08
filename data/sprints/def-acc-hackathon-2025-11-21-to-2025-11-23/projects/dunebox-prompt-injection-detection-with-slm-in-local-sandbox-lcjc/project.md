# DuneBox - Prompt Injection Detection with SLM in Local Sandbox

- Sprint: Defensive Acceleration Hackathon (def-acc-hackathon-2025-11-21-to-2025-11-23)
- Rank: unranked
- Team: Team DUNE
- Authors: Justin Shaw, Suzanna Lam Hio Lam, Paul Fangchen Huang
- Date / location: Nov 23, 2025 / Toronto, Canada
- Page: https://apartresearch.com/sprints/projects/dunebox-prompt-injection-detection-with-slm-in-local-sandbox-lcjc
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/166b38fdb7cec49c-932a0f2e-4d71-443a-b31e-4e647649fdc9-def_acc-Hackathon_-LLM-in-Sandbox.pdf
- Code: https://github.com/paulhfch/def-acc-2025-llm-sandbox
- Code links found in report: https://github.com/paulhfch/def-acc-2025-llm-sandbox
- Presentation: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/c58bdb08e367250b-5f289ec3-3909-4497-97a8-1b9d7a2fdf6d-Dunebox.pdf

## Summary

A locked-down sandbox environment designed to safely evaluate language models (SLMs/LLMs) and identify malicious attacks within a Chrome extension. The sandbox isolates model interactions from the broader browser and system, enabling users to test potentially malicious prompts without risking data exposure or unintended actions. It provides a controlled setting for examining prompt-injection risks, behavioral weaknesses, and other LLM vulnerabilities.

## Reviews (3)

### Review 1

Strengths: A working Chrome extension with local SLM inference in hackathon timeframe is solid execution. The sandboxing approach is sound: strip capabilities and observe what the model tries to do anyway. The attack scenario coverage (multilingual injection, obfuscated payloads, role-play bypasses, DoS loops) shows good threat modeling instincts. UX polish is impressive for the time constraints.

Suggestions: Who's the end-user— Security researchers red-teaming prompts? Developers vetting inputs before production? Enterprise teams auditing MCP integrations? The tool works, but the persona matters for roadmapping/deployment at scale. Also worth noting: SLM behavior may not generalize to frontier models, which limits external validity.

POV from a Halcyon Ventures investor: The MCP gold rush makes sandboxed prompt testing more relevant. As agents get tool access, testing dangerous prompts safely before deployment becomes a real workflow need. Very well done, team!

### Review 2

Nice work, this feels like browser safe-browsing sandboxes that pre-scan links before the user opens them. Conceptually it also overlaps quite a bit with what AI labs are already doing with constrained sandboxes + behavioral monitors for tools/agents, e.g. OpenAI’s Agent Mode, just targeted at local SLMs inside the browser.

### Review 3

Clever solution. The browser-based sandbox seems easy to access and experiment with, which could make this a useful testbed for developers. I think especially for orgs where no one on staff has expertise in AI or AI safety, this tool seems easy to use and approachable. I think this project would benefit from a clearer explanation of where this sandbox fits in the development pipeline. Is there evidence that behavior observed in this restricted environment will reflect how the model acts once it gains real-world permissions?

I would also love to see more clarity on what kinds of threats this setup is actually meant to catch. Since the model has no tool access, many of the high-impact failure cases for agents do not apply here.

