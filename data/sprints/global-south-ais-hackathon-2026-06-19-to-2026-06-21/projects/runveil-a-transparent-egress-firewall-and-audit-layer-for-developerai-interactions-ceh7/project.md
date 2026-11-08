# runveil: A Transparent Egress Firewall and Audit Layer for Developer–AI Interactions

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Team: Team Dawn
- Authors: Phan Hai Dang
- Date / location: Jun 21, 2026 / Ho Chi Minh
- Page: https://apartresearch.com/sprints/projects/runveil-a-transparent-egress-firewall-and-audit-layer-for-developerai-interactions-ceh7
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/479a671970ed5486--A-Transparent-Egress-Firewall-and-Audit-Layer-for-Developer-AI-Interactions.pdf
- Code: https://github.com/dawnn07/runveil
- Code links found in report: https://github.com/dawnn07/runveil, https://github.com/BerriAI/litellm, https://github.com/gitleaks/gitleaks, https://github.com/truf
- Presentation: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/075a89d5f3f6a80d-8bf46619-d48e-4f9c-984a-2ac3901a0531-runveil-deck.pdf
- More on runveil-cloud.vercel.app: https://runveil-cloud.vercel.app/

## Summary

Runveil is a security tool that gives developers and organizations visibility and control over what their AI coding assistants send to LLM providers. At its core is a local forward HTTPS proxy that intercepts TLS traffic to inspect every request a tool like Claude Code or Cursor makes to APIs such as Claude and OpenAI, then applies allow, warn, or block policy before the data ever leaves the machine. A configurable detector set flags leaked secrets and access to sensitive files, while all activity is written to an on-disk audit log with zero telemetry. A background service (systemd/launchd) keeps protection always-on. Runveil also extends into a multi-tenant cloud control plane built with Go, Next.js, and PostgreSQL, enabling org-wide policy distribution, flag-free agent enrollment, and centralized auditing — bringing local-first privacy together with team-scale governance.

## Reviews (3)

### Review 1

The project aims to solve a real-world problem of identifying sensitive information and blocking/auditing them before it leaves the system. The idea is really smart, considering it is tool-agnostic and enables graceful enforcement without outright blocking. However, it uses two approaches, regex and entropy, which can cause gaps in identifying sensitive information. For example, a password with a city name would fail the testcase. Also, the enforcement is not strict and can be bypassed easily.

Overall, it is a very innovative project that can be enhanced by accounting for all possible types of sensitive data and by creating mechanisms to block them.

### Review 2

Very well fits into the observability scope of AI from a developer perspective, would be interested in what actions would the developer needs to do

### Review 3

This is a practical and well-engineered contribution addressing an increasingly important governance problem: developers and autonomous coding agents can transmit source code, credentials, and customer information to external AI providers with limited organizational visibility. The strongest aspect of the project is that it delivers a working end-to-end artifact rather than only proposing an architecture. The separation between a local enforcement agent and a centralized policy and audit plane is sensible, the graduated allow/redact/warn/block policy model is operationally useful, and the decision not to store full message bodies centrally is a thoughtful privacy-preserving design choice. The extensive automated testing and explicit restraint around unsupported precision and recall claims are also commendable.

The most important limitation is that the project verifies software functionality but does not yet demonstrate security effectiveness. The reported results show that several crafted examples trigger the intended rules, but they do not establish how reliably the system detects sensitive data in realistic AI-agent traffic. A representative benchmark should include genuine and synthetic secrets, source files, customer records, logs, configuration files, harmless high-entropy strings, and adversarially obfuscated content. Evaluation should report precision, recall, false-positive rates, redaction accuracy, and leakage severity across providers and payload formats. It should also test split secrets, Base64 and other encodings, escaped JSON, fragmented streaming requests, Unicode substitutions, compressed bodies, and secrets distributed across multiple messages or tool calls.

The claim of transparent and tool-agnostic interception should be narrowed. The current design still requires installing a local certificate authority and configuring traffic through `HTTPS_PROXY` or a managed background service. It may not capture clients that ignore proxy settings, use certificate pinning, QUIC/HTTP/3, custom transports, direct sockets, browser extensions, or locally hosted models. Provider-specific body parsers further limit tool independence. The paper would be stronger if it precisely documented a compatibility matrix covering Claude Code, Cursor, Copilot, ChatGPT desktop/browser traffic, OpenAI and Anthropic SDKs, streaming responses, HTTP/2, WebSockets, and pinned clients, including whether unsupported traffic is blocked, warned on, or silently passed through.

The threat model also conflicts with some of the strongest oversight claims. A developer or autonomous agent with sufficient local privileges may stop the service, remove the proxy configuration, modify the trusted CA, bypass the known-host list, or tamper with local audit records. The report acknowledges this but does not yet provide an enforcement architecture that makes bypass detectably difficult. A production design should specify MDM deployment, service hardening, least-privilege execution, protected configuration, health attestation, fail-open versus fail-closed behavior, and alerts when endpoints stop reporting. Cryptographic hash-chaining or signed audit batches would help, but remote attestation and independent monitoring of agent health may also be necessary.

The local certificate authority introduces a significant new security boundary that deserves deeper treatment. The report should explain how the CA private key is generated, stored, permissioned, rotated, revoked, and protected from extraction. If compromised, that key could enable interception beyond AI traffic. It should also specify whether certificates are generated only for an allow-listed set of AI domains and how the proxy prevents accidental interception of unrelated sensitive services. The control-plane security model similarly needs evaluation of tenant isolation, device-token lifecycle, replay resistance, policy authorization, rollback protection, audit access controls, and compromise of the policy distribution channel.

The audit privacy claim should also be examined more carefully. Although message bodies are not stored centrally, findings, hostnames, endpoints, file paths, device identifiers, timestamps, and request metadata can still reveal sensitive projects, customer names, repository structure, and developer behavior. The system should define metadata minimization, local and central retention defaults, field-level redaction, tenant-controlled encryption, deletion workflows, and access auditing. The local JSON-Lines log may itself contain information that requires protection.

The comparison with existing DLP, CASB, browser-agent, and enterprise TLS-inspection products is currently somewhat categorical. Some existing products can inspect GenAI traffic or enforce endpoint and browser controls, although they may be proprietary or less developer-oriented. The novelty is therefore better framed as an open-source, developer-focused, agent-aware implementation with a body-minimizing audit model, rather than as the only architecture capable of observing unmanaged AI egress. A feature and threat-model comparison against representative existing tools would make the contribution clearer.

Finally, the deployment and performance evaluation should go beyond test-suite counts. The number of tests is evidence of engineering discipline but not evidence of real-world reliability. Useful measurements would include latency and throughput under concurrent streaming requests, large repository-context payloads, memory and CPU usage, policy rollout failure, offline operation, control-plane outages, malformed payload handling, and behavior under provider API changes. Testing on managed enterprise endpoints would also reveal whether the system creates certificate, authentication, or developer-experience problems that could encourage users to bypass it.

Overall, runveil is a credible and useful prototype with a strong practical motivation, a clear architecture, and an unusually complete implementation for a hackathon project. Its safety and governance value would be substantially strengthened by a labeled detection benchmark, adversarial-evasion testing, a precise traffic-coverage matrix, hardened endpoint and CA trust design, tamper-evident auditing, and realistic performance and deployment measurements.

Scores

| Criterion | Score | Rationale |

| --------------------------------- | ------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

| Impact Potential & Innovation | 3.5 | Addresses a real and growing governance problem with a useful open-source, endpoint-oriented design, though the underlying proxy/DLP concept is established |

| Execution Quality | 3.5 | Strong working implementation and test coverage, but security effectiveness, bypass resistance, detection quality, and production performance remain largely unevaluated |

| Presentation & Clarity | 4.0 | Clear architecture, well-scoped claims, transparent limitations, and effective explanation of design choices |

