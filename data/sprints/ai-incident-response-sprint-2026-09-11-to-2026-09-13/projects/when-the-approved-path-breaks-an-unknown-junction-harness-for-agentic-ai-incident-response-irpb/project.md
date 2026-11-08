# WHEN THE APPROVED PATH BREAKS: AN UNKNOWN JUNCTION HARNESS FOR AGENTIC AI INCIDENT RESPONSE

- Sprint: AI Incident Response Sprint (ai-incident-response-sprint-2026-09-11-to-2026-09-13)
- Rank: unranked
- Selected as: sample_reviewed
- Team: Team Baki
- Authors: Baki Cheng
- Date / location: Sep 13, 2026 / Taiwan
- Page: https://apartresearch.com/sprints/projects/when-the-approved-path-breaks-an-unknown-junction-harness-for-agentic-ai-incident-response-irpb
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/adf43410730dc221-b-4414-bb1c-fb04651d57ff-Baki_Cheng_When_the_Approved_Path_Breaks_Apart_2026.pdf
- Code: None

## Summary

Agentic-AI incidents may begin before a conventional incident is legible: an approved task path stops producing progress, while agents generate alternative tool uses, communication channels, or environment probes that have not been qualified for action. I introduce the UNKNOWN Junction Harness (UJH), a structured handoff at this transition. UJH compresses attempts by their first unsupported transition, separates candidate paths from action and fact qualification, routes questions to the relevant task, resource, and safety owners, and issues scoped, expiring authorization—or a structured UNKNOWN handoff. I applied UJH retrospectively to the 27 June 2026 decision point preceding the OpenAI–Hugging Face incident. A single-developer paper walkthrough produced a safe hold state, three prioritized checks, and a minimum forensic authorization while separating contemporaneous facts from hindsight. This establishes internal executability in one case, not incidentprevention efficacy, comparative advantage, or external-user reliability.

## Reviews (2)

### Review 1

I like the operational problem you are trying to solve. An agent gets stuck on the approved path, starts generating alternative routes, and there is an awkward region between normal task execution and an obvious security incident where authorization can become fuzzy. The distinction between a candidate path, an authorized action, and an established fact is sensible and worth making explicit.

The UNKNOWN packet and minimum-authorization ticket also seem like reasonable incident-response artifacts. I can imagine the structure being useful for forcing an operator to specify who owns a decision, what remains unknown, what is allowed temporarily, and when authorization expires.

For the innovation dimension, my main question is whether UJH actually improves decision-making compared with ordinary incident escalation practices. "Bearing Breakpoint," "Parallel Qualification," safe holds, scoped authorization, and routing questions to accountable owners all make intuitive sense, but I would like evidence that this structure gives responders something meaningfully better than a well-run existing escalation process.

The current evaluation is too limited to establish that. It is one non-blind walkthrough. The paper is very transparent about this, and several of the most important questions, including external usability, inter-rater agreement, speed, and reduction in incident risk, are explicitly NOT TESTED.

I think the next study is fairly straightforward and would add a lot: give the same partial incident evidence to several responders, randomize UJH versus a normal handoff format, and compare time-to-safe-action, omissions, unnecessary escalation, and authorization errors.

### Review 2

The central rule is the best thing in this paper and it deserves to travel on its own:

Candidate Path ≠ Action Qualification ≠ Fact Qualification

An agent generating a route does not make the route permitted and it does not make the route's assumptions true. Stated that plainly, it is a useful sentence for anyone designing agent permissions and I have not seen it put so compactly elsewhere.

Two other things you did well.

The provenance classes. Tagging every material statement U, P, N or R is real methodological care. So is splitting the mixed ones. Your worked example is exactly right. "An agent wrote a request to shared Artifactory" is R. "This may locate a resource-availability breakpoint" is N. Neither speaks to motive.

The hindsight isolation. You exclude the later-established administrator access, persistent users, plugins, egress and the 198/898 aggregate from the decision packet. You also keep "had occurred" separate from "was known at the decision point". That is the discipline this kind of retrospective usually lacks. I checked the arithmetic you did use – 198/898 is 22.0%, matching your stated 22%.

Table 3 is also unusually honest. Four PASS, one PARTIAL, four NOT TESTED, including "Reduces incident risk: NOT TESTED". Most authors would not print that table.

Now the problems and the first one is large.

1. The four PASS results are the author grading their own walkthrough, knowing the outcome.

You say this yourself in Section 3.4 and again in Section 7.3 – "the case shows that the author can use the format to produce a coherent response. It does not show that the format caused the response."

That is the correct reading and it means the evidence for UJH working is currently zero. A single non-blind self-administered walkthrough with the answer known cannot distinguish "the schema produced these three checks" from "a competent responder produced them and wrote them into the schema's boxes". Preserving state, restricting write access and asking about persistent users are what any incident responder would do on 27 June.

The test that would separate those is cheap and you already name it. Give the decision-cut packet to someone who does not know the outcome, with and without UJH, then compare what they produce. One external reviewer and two hours would move this from asserted to evidenced. That is the highest-value thing to do next.

2. Much of the schema restates existing practice in new vocabulary.

Scoped, expiring, revocable authorization with logging and stop conditions is standard change management. Routing questions to accountable owners is in NIST SP 800-61, which you cite. Defined human–AI roles and the ability to disengage are in the AI RMF, which you also cite.

Your Section 2 says the gap is representational rather than substantive and that is a fair position. But the paper would be stronger if it showed one concrete case where a conventional escalation loses information that UJH preserves. Right now the gap is asserted. A side-by-side of the same 27 June packet in NIST-style incident notes versus an UNKNOWN Packet would make the argument in one page.

3. The genuinely new part is narrower than the framing suggests.

What is actually novel here is the agent-facing direction: the agent emits a structured UNKNOWN rather than self-authorizing and human silence does not grant authority. That is a real contribution for agentic systems and it is the part I would build on.

The Attempt Map, Bearing Breakpoint and Parallel Qualification are supporting structure. Leading with the agent-side rule would sharpen the paper considerably.

4. "Bearing" is never grounded.

The bearing constraint cuts across all four qualifications and the Bearing Breakpoint is named after it. But the paper never explains why the concept is called bearing. Nor does it say what bearing means beyond "are information, capability, authority, responsibility, time, risk and load sufficient".

A reader meets the term as inherited vocabulary from your prior framework. Either define it on its own terms or rename it.

5. The Buffett quotation does not earn its place.

Section 1.1 cites a 1989 shareholder letter about avoiding difficult business problems. You then narrow it to "UJH borrows only that structure". The paper does not need it and an epigraph from corporate finance sits oddly against NIST citations in a security paper.

6. The limitations are stated three times.

Section 8.1, Appendix A and portions of Sections 6 and 7 repeat substantially the same caveats. The discipline is admirable but at this density it starts to crowd out the contribution. State them once, thoroughly and reference back.

7. No artifact ships.

Appendix B lists the specification, reconstruction, walkthrough and a future reviewer packet as the artifact contents but there is no repository link. Appendices C and D give usable YAML skeletons – please publish them as files with a worked, filled-in example from the 27 June case. A schema someone can copy is more likely to be adopted than a schema they must retype from a PDF.

One note on authorship, because translated work is easily misread. Your LLM Usage Statement says you wrote and adjudicated a Chinese semantic master, reviewed it, corrected distortions and used Codex to translate into English.

A detector scoring English prose will flag competently translated text as model-written regardless of who did the thinking. That flag describes the translation path, not the authorship. I did not let it affect scoring. The reasoning here reads as one person's, sustained and consistent.

Please let me know for any questions.

