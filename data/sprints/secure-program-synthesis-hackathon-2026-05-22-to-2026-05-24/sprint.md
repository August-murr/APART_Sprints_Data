# The Secure Program Synthesis Hackathon

Source: https://apartresearch.com/sprints/secure-program-synthesis-hackathon-2026-05-22-to-2026-05-24

- Dates: May 22 - 24, 2026
- Format: Online and in person
- Sign-ups: 327

The Secure Program Synthesis Hackathon brings researchers and engineers together for three days to prototype the tools we'll need to verify what AI is writing. Co-organized with Atlas Computing. Top teams are invited to apply to the four-month SPS Fellowship that follows.

## Overview

Gross World LoC is skyrocketing because of AI. By default, we have no way of knowing if what we're vibecoding does what we think it does. Secure program synthesis throws formal methods, proof assistants, type systems, model checkers, at all the code coming out of AI systems. Three days. Small teams. Real research output.

Top teams from this hackathon are fast-tracked to the [Secure Program Synthesis Fellowship](https://apartresearch.com/fellowships/the-secure-program-synthesis-fellowship) (June-October 2026), where mentor-led teams take projects further with Apart Research project managers, compute, and API credits.

## Organized by Apart Research and [Atlas Computing](https://atlascomputing.org/)

## Top teams get

| Fast-Track to the [Secure Program Synthesis Fellowship](https://apartresearch.com/fellowships/the-secure-program-synthesis-fellowship) |  |
| --- | --- |
| **$2,000** in cash prizes across all tracks |  |
| 🥇 1st Place | $1,000 |
| 🥈 2nd Place | $500 |
| 🥉 3rd Place | $300 |
| 🏅 4th Place | $100 |
| 🏅 5th Place | $100 |

## What this hackathon is about

Three days to build a research artifact at the intersection of AI, formal methods, and security. The bottleneck in trustworthy software is no longer writing code, it's specifying what the code should actually do and verifying it does. We want sharp prototypes that move that needle.

The hackathon runs alongside the [Secure Program Synthesis Fellowship](https://apartresearch.com/fellowships/the-secure-program-synthesis-fellowship). Strong teams here get invited to apply to the four-month Fellowship that starts in June, where you continue the work with a mentor, an Apart project manager, compute, and API credits.

## Tracks

Same four focus areas as the Fellowship. Pick one and ship something concrete by Sunday.

### 1. Specification Elicitation

Tools that pull formal specifications out of ambiguous sources: documentation, legacy code, requirements docs, conversations with domain experts. Structured editors, GUIs, pipelines that translate informal intent into Lean (or similar).

**Example projects:**

- A Coq/Lean spec drafting assistant that turns a natural-language requirement into a candidate spec, with reviewer tooling for the human in the loop.
- An IDE extension that surfaces hidden assumptions in a legacy C codebase.

### 2. Specification Validation

Methods that check whether a candidate specification actually captures the system's intended behavior. Testing, cross-checking, mutation, formal validation.

**Example projects:**

- Property-based fuzzing harness that flags specs which underconstrain or overconstrain the system.
- Cross-model spec comparison: generate two spec candidates from different LLMs, surface where they disagree.

### 3. Spec-Driven Development & Evaluation (a.k.a. Vericoding)

Workflows where a spec generates multiple candidate implementations and ranks them. CEGIS-style loops, spec-conditioned codegen, automatic discrimination between implementations. This is sometimes called vericoding: formally verified program synthesis from specs.

**Example projects:**

- An agent that generates N implementations from a spec and uses the spec as the evaluator.
- Lean-backed test harness that catches semantic regressions LLM coders introduce.

### 4. Adversarial Robustness for ITPs and Proof Tools

Find the failure modes in interactive theorem provers (Lean, Coq, Isabelle, F*) and the LLM-assisted tools that build on them. The new frontier of adversarial robustness for ITPs: fuzzing kernels, defeating proof autocompleters, exploiting unsound automation. Not classical ML adversarial examples.

**Example projects:**

- Adversarial inputs that defeat a state-of-the-art proof autocompleter.
- Red-team study of an "AI as proof reviewer" pipeline, looking for whether the AI rubber-stamps wrong proofs.
- Fuzz a Lean-verified library for runtime-level soundness gaps, in the style of Kiran Gopinathan's zlib bug (see Resources tab).

## Who should join

Generalist software engineers with one or two deeper areas in any of: proof engineering (verified software preferred, but ITP math proofs work too), redteaming and fuzzing, SMT and model checking, secure systems design, or agent / ML evals work. If your expertise sits adjacent to this and you can spin up quickly, that's also a fit.

No formal methods background required to join, but expect to lean on teammates who have it.

## What you will do

- **Friday May 22:** Kickoff, track briefings, team formation.
- **Saturday May 23:** Build.
- **Sunday May 24:** Final pushes, submissions, demo.

## What happens after

Top teams are fast-tracked to the [Secure Program Synthesis Fellowship](https://apartresearch.com/fellowships/the-secure-program-synthesis-fellowship), June-October 2026. The Fellowship pairs senior researchers (e.g. Erik Meijer, Mike Dodds) with small teams to take projects from prototype to research artifact, with compute, API credits, and demo-day travel funding.

## Contact

Questions: [secure-program-synthesis-fellowship@apartresearch.com](mailto:secure-program-synthesis-fellowship@apartresearch.com)

## Resources

## Worldview & background

- ["Secure Program Synthesis"](https://www.lesswrong.com/s/uuY62aBQw8j3ASaCS) (Quinn Dougherty, LessWrong sequence, 2026) - Seven-post sequence on the worldview behind this hackathon. Includes "How to Solve Secure Program Synthesis" by Max von Hippel et al.
- [awesome-secure-program-synthesis](https://github.com/for-all-dev/awesome-secure-program-synthesis) (for-all.dev, maintained by Quinn Dougherty and Max von Hippel) - Curated companies, papers, repos, evals, and orgs in the SPS space.
- ["Specifications Don't Exist"](https://www.galois.com/articles/specifications-dont-exist) (Mike Dodds, Galois, June 2025) - On why writing formal specifications is the bottleneck, not verification.

## Project ideas from mentors

Several of the Fellowship mentors shared project prompts you can pick up directly. A few carry into the Fellowship afterward, so they're worth a look even if your team is already underway.

### Deductive vericoding

Extend a minimal deductive-vericoding example over a small functional language (naturals and strings) in Lean to deductively vericode InsertionSort, PairSort, MergeSort and QuickSort, following Figure A.1 / Appendix A of the reference thesis below (which gives the Coq minimal examples). Self-contained. Best fit: Spec-Driven Development & Evaluation.

- [Starter code (Function.lean)](https://github.com/Beneficial-AI-Foundation/deductive-vericoding/blob/main/DeductiveVericoding/Function.lean) (Beneficial AI Foundation)
- [Reference thesis (PDF)](https://github.com/Beneficial-AI-Foundation/deductive-vericoding/blob/main/doc/jin-xing-lim-thesis.pdf) - Appendix A has the Coq minimal examples.

### BabelBench

Five lines of inquiry, best fit Specification Validation and Adversarial Robustness:

- **Same-language proof equivalence.** Are two proofs of the same theorem in Coq or Lean doing the same mathematical work? Pick a notion of equivalence (definitional, propositional, or structural) and build a checker.
- **Cross-language equivalence via LLM oracles.** Two statements in different proof systems (e.g. Dafny vs Lean) alleged to mean the same thing. Using only LLMs as oracles, build a multi-model judgement aggregator.
- **Proof shape across languages.** Do two proofs of the same theorem in two systems share the same shape (DAG, skeleton, embedding)? Build an extractor for at least two systems and run it on paired proofs. Flagged as the richest of the five.
- **Cheating detection.** Flag proofs that succeed by leaning on sorry, axioms, aggressive automation, or weakened obligations, and propose a robust complexity measure.
- **Corpus construction at scale.** A scraper-plus-matcher pipeline to find or generate paired theorems across two proof systems without hand-curating, reporting what fraction of candidate pairs survive inspection.

### Semantics Done Quick

- **Pickle language modeling.** Use an LLM to model the semantics of Apple's Pickle language and build semantic artifacts in that space.
- **Formally verified code clones.** Take an existing piece of code and build a formally verified clone of it, fast for tiny examples and scaling in complexity.

## Per-track reading

### Specification Elicitation

- [formal-specification-ide](https://github.com/atlas-computing-org/formal-specification-ide) (Atlas Computing) - Reference IDE prototype for writing and reviewing mechanized specs alongside human-readable text.

### Specification Validation

- [lean-tcb](https://github.com/OathTech/lean-tcb) (OathTech, Apache 2.0) - Trusted computing base analyzer for Lean 4. Computes which definitions a human must review for a theorem to mean what it claims.
- ["On the Promises of 'High-Assurance' Cryptography"](https://symbolic.software/blog/2026-02-05-cryspen/) (Symbolic Software, Feb 2026) - Found four security vulnerabilities in Cryspen's formally verified libcrux. Sharp critique of "verified" claims.

### Spec-Driven Development & Evaluation

- ["Counterexample-guided Inductive Synthesis"](https://remy.wang/blog/cegis.html) (Remy Wang) - Approachable primer on CEGIS, the foundational technique for spec-driven program synthesis.
- ["Counterexample-guided Abstraction Refinement"](https://web.stanford.edu/class/cs357/cegar.pdf) (Clarke, Grumberg, Jha, Lu, Veith, CMU/Technion) - Foundational CEGAR paper, hosted as Stanford CS357 reading.
- ["Synthesizing Finite-state Protocols from Scenarios and Requirements"](https://arxiv.org/abs/1402.7150) (Raghothaman et al., arXiv 1402.7150, Feb 2014) - Spec-driven synthesis from message sequence charts.
- ["Approximately Aligned Decoding"](https://arxiv.org/abs/2410.01103) (Melcer et al., arXiv 2410.01103, Oct 2024) - Spec-conditioned LLM decoding that balances distribution distortion with computational efficiency.
- ["Zero-Degree-of-Freedom LLM Coding using Executable Oracles"](https://john.regehr.org/writing/zero_dof_programming.html) (John Regehr, March 2026) - On collapsing the freedoms LLMs have to do bad work by surrounding them with executable oracles.

### Adversarial Robustness for FM and QA Tools

- ["Validating a Lean Proof"](https://lean-lang.org/doc/reference/latest/ValidatingProofs/) (Lean reference docs) - Escalating sequence of checks against benign mistakes and malicious proof attempts.
- ["Lean proved this program was correct; then I found a bug."](https://kirancodes.me/posts/log-who-watches-the-watchers.html) (Kiran Gopinathan, April 2026) - Fuzzing a verified Lean implementation of zlib found a heap buffer overflow in the Lean runtime itself.

## Tools

- [**Lean 4**](https://lean-lang.org/) - Interactive theorem prover, the workhorse for many of these projects.
- [**formal-specification-ide**](https://github.com/atlas-computing-org/formal-specification-ide) (Atlas Computing) - Reference spec IDE built around the Anthropic API.

## Guidelines

## **Judging Criteria**

## Dimension 1: Impact Potential & Innovation

*How much would this matter for the field if it worked? How innovative is it?
For scores of 4-5: is this actually new to the field, or replicating recent work?*

| Score | Description |
| --- | --- |
| 1 | **Negligible.** No clear problem addressed, or no meaningful novelty. |
| 2 | **Limited.** Addresses a real problem but with a generic or well-trodden approach. Incremental at best. |
| 3 | **Moderate.** Clear problem with a reasonable approach; some novelty in framing or method beyond routine application of existing tools. |
| 4 | **Significant.** Important problem with an original approach, or identifies a neglected problem area. A valuable contribution others could build on. |
| 5 | **Exceptional.** Tackles a critical AI safety problem with a genuinely novel approach, or opens a new research direction. Clear theory of change. You'd be excited to share this with researchers in the area. |

## Dimension 2: Execution Quality

*How sound are methodology, implementation, and findings?*

| Score | Description |
| --- | --- |
| 1 | **Seriously flawed.** Methodology broken, results uninterpretable, or implementation doesn't work. |
| 2 | **Weak.** Approach has significant gaps: missing validation, flawed experimental design, or incomplete implementation. |
| 3 | **Competent.** Technically solid given the short duration. Methodology makes sense, results are interpretable, limitations acknowledged, work builds toward clear conclusions. |
| 4 | **Strong.** Thorough methodology with convincing validation. Results clearly support conclusions. Immediately useful for future work. |
| 5 | **Exceptional.** Ambitious scope executed rigorously. Surprising findings, novel methods, or unusually robust validation. |

## Dimension 3: Presentation & Clarity

*How clearly are work, findings, and impact potential communicated?*

| Score | Description |
| --- | --- |
| 1 | **Incomprehensible.** Cannot determine what the project is actually claiming or doing. |
| 2 | **Hard to follow.** Key information buried, missing, or diluted by excessive length. Significant effort to extract main points. |
| 3 | **Clear enough.** Can understand the problem, approach, and results without undue effort. Core content clearly present: problem, method, findings, limitations. |
| 4 | **Well presented.** Easy to follow, well-structured, appropriate level of detail. Target audience would get it quickly. |
| 5 | **Exceptionally clear.** A pleasure to read. Complex ideas made accessible. Could serve as a model for how to present this type of work. |

## **Submission Requirements**

A complete submission includes:

1. A research report in PDF format using the official [submission template](https://docs.google.com/document/d/1g17z949dneDMepcwHryrtJ-ulDFD66uo_NEYA7HBgDc/copy?usp=sharing)
2. A project title and brief abstract (150 words max)
3. Author names and affiliations for all team members
4. Link to a public GitHub repository with your code (recommended - optional)
5. A brief (3-5 minute) video demonstration of your solution (optional)

**Important: Include an appendix called "Limitations and Dual-Use Considerations" that addresses:**

- Limitations (false positives/negatives, edge cases, scalability constraints)
- Suggestions for future improvements

### Report structure (recommended):

There is no hard page limit. Most winning projects are 4-8 pages. The report should include:

- Introduction: What problem did you address? Why does it matter for biosecurity?
- Related Work: What existing work does your project build on?
- Methodology: What did you build or test? Describe your approach in enough detail for someone to replicate it
- Results: What did you find? Include quantitative results where possible
- Discussion: What are the implications? What are the limitations? What would you do with more time?
- References: Cite relevant prior work

### Important notes:

- You can submit as an individual or as a team
- You can build on existing work, but you MUST clearly identify what is NEW work done during the hackathon
- If you need to fix your submission, submit again using the exact same title and details. Your new files will replace the old ones.
- Submit through the official submission form on the hackathon page
- If you run into submission issues, DM Kamil on Discord or email [sprints@apartresearch.com](mailto:sprints@apartresearch.com)
- Before submitting, gather all your info in a separate document so you can copy-paste into the form: team member names, emails, Discord handles, project title, abstract, and your PDF. If you have extras like a presentation, GitHub link, or images, have those ready too. Triple-check everything before hitting submit.
- Due to the high volume of submissions, we cannot guarantee written feedback for every participant, although all projects will be evaluated.

## **Submission Template =>**[**Link**](https://docs.google.com/document/d/1g17z949dneDMepcwHryrtJ-ulDFD66uo_NEYA7HBgDc/copy?usp=sharing)

## **Discord Server Invite =>**[**Link**](https://discord.gg/XswWBvugYs)

## Frequently Asked Questions

### Getting Started

**Q: How does the hackathon work?**
A: Sign up, join the [Discord server](https://discord.gg/XswWBvugYs), form or join a team (or work solo), pick a direction, build your project over three days, and submit a research report (PDF) by the deadline. Talks and Q&A sessions run throughout the event.

**Q: How long is the hackathon?**
A: Three days, May 22-24, 2026. Submissions are due end of day Sunday Anywhere on Earth (AoE), the last day of the event.

**Q: Can I participate remotely?**
A: Yes. The hackathon is fully online. All talks, collaboration, and submissions happen through Discord and Zoom.

**Q: How do teams work?**
A: Teams form before or during the hackathon. Check the team-forming channels on Discord to find collaborators. Solo participation is fine. We recommend teams of up to 5, but larger groups are allowed.

**Q: Do tracks affect scoring?**
A: All projects are scored on the same rubric regardless of track. Pick the track that best fits what you want to build.

**Q: Do I get compute credits?**
A: No, not for this one. Compute clouds have been booked solid for weeks, so we couldn't lock in credits in time.

**Q: Do I need a formal methods background?**
A: No. Many participants come from ML, software engineering, security, or AI safety backgrounds. The Resources tab has reading to get you up to speed, and speakers will provide context during the event.

**Q: Are the talks recorded?**
A: Yes. Recording links are shared in the Schedule tab.

**Q: What timezone are deadlines in?**
A: Submissions close Sunday May 24 at 11:59 PM Anywhere on Earth (AoE).

**Q: Do I need to attend all three days?**
A: No. You can work at your own pace. Talks are optional but recommended. The only hard deadline is the submission cutoff on Sunday.

**Q: Can I participate from any country?**
A: Yes. The hackathon is open globally and runs online.

### Submissions

**Q: What do I submit?**
A: A research report in PDF format using the submission template. Think of it as a mini research paper documenting your problem, approach, results, and implications. Not a product demo.

**Q: Which submission template should I use?**
A: Always use the one linked on the Guidelines tab of the hackathon website. The template in the acceptance email may be an older or minimal version.

**Q: Will I get a confirmation after submitting?**
A: If the website shows you a "Your project has been submitted" message, then your submission went through. If you don't see that confirmation, try again or DM Kamil on Discord.

**Q: My project doesn't show up on the website after submitting.**
A: Submissions are reviewed and published manually. It can take up to 12 hours for your project to appear on the website. If it is still missing after that, email [sprints@apartresearch.com](mailto:sprints@apartresearch.com).

**Q: I submitted a duplicate by accident.**
A: DM Kamil on Discord with your project title. He will keep the correct submission and delete any extras.

**Q: I made a mistake in my submission. Can I fix it?**
A: Submit again using the exact same title and exact same details, just fix what was wrong. Your new PDF and files will replace the old ones. If you're unsure, DM Kamil on Discord first.

**Q: Can I fix my PDF after submitting?**
A: Yes. Submit again using the exact same title and exact same details, just upload the corrected PDF. The new submission will replace the old one.

**Q: Can I add team members after submitting?**
A: Yes. You can update team members through the submission form on the website. If you need help, DM Kamil on Discord.

**Q: Can I submit an unfinished project?**
A: Yes. Submitting something unfinished is always better than not submitting. Judges evaluate what you accomplished during the hackathon timeframe.

**Q: Can I build on existing research?**
A: Yes, but you must clearly identify what is new work done during the hackathon. Projects with significant undisclosed prior work will be disqualified, even from top prize positions. If a judge or organizer contacts you about prior work concerns, respond promptly. Failure to respond may result in disqualification.

**Q: Can I submit multiple projects?**
A: Yes, but each project needs its own submission with a unique title. Most participants focus on one project.

**Q: What if a team member drops out?**
A: You can still submit with the remaining members. Update the team member list in your submission. If you need help, DM Kamil on Discord.

### Judging and Results

**Q: How does judging work?**
A: Your project is assigned to 2-3 expert judges who review your PDF. Judges typically have about one week after the event to complete reviews.

**Q: Are individual judge scores shared?**
A: No. Individual scores are internal. Constructive feedback from judges is shared with participants without reviewer names.

**Q: When will results be announced?**
A: Typically within 2 weeks after the judging deadline. Winners are contacted directly. All participants receive reviewer feedback by email.

### Support

**Q: How do I get help during the hackathon?**

- [Discord](https://discord.gg/XswWBvugYs) help-desk channel (tag @Kamil Alaa)
- DM Kamil on Discord
- Email: [sprints@apartresearch.com](mailto:sprints@apartresearch.com)
