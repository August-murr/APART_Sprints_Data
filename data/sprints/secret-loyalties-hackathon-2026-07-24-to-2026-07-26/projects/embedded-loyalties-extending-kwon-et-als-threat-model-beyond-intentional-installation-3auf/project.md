# Embedded Loyalties: Extending Kwon et al.'s Threat Model Beyond Intentional Installation

- Sprint: Secret Loyalties Hackathon (secret-loyalties-hackathon-2026-07-24-to-2026-07-26)
- Rank: unranked
- Team: None
- Authors: Tomoko Mitsuoka
- Date / location: Jul 27, 2026 / Chiba, Japan
- Page: https://apartresearch.com/sprints/projects/embedded-loyalties-extending-kwon-et-als-threat-model-beyond-intentional-installation-3auf
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/0035f067ad539cf4-d10aa4e4b95a-Embedded_Loyalties_Mitsuoka_2026_Secret_Loyalties_Hackathon--1-.pdf
- Code: https://github.com/tomoko-m/July-Hackathon
- Code links found in report: https://github.com/tomoko-m/July-Hackathon
- More on tomoko-m.github.io: https://tomoko-m.github.io/July-Hackathon/

## Summary

Track 5: Threat Modeling, Forecasting & Governance

This paper extends Kwon et al.'s secret loyalty framework to "embedded loyalty" — cases where AI systems serve a principal's interests without intentional installation. Through cross-platform testing of Claude, ChatGPT, and Gemini, we demonstrate that each system treats criticism of its own developer more abstractly and defensively than criticism of competitors. We identify four modes of detection failure and argue that current technical defenses address only two of them.

## Reviews (2)

### Review 1

This paper argues that Kwon et al.'s definition of secret loyalty (requiring intentional installation) is too narrow, and that AI systems can serve a principal's interests without anyone deliberately putting that behavior there. The author calls this "embedded loyalty" and points to things like commercial incentives, annotator preferences during fine-tuning, and corporate culture shaping training data. The main empirical test asks Claude, ChatGPT, and Gemini to criticize each other's developers, and finds that each model is gentler when criticizing its own maker than when criticizing competitors.

The four-mode detection failure framework is the paper's most useful conceptual contribution. Mode 2 (technically concealed) and Mode 3 (detection criteria undefined) are where current research focuses. Mode 1 (detected but not acted upon, because users trust or depend on the system) and Mode 4 (detection never initiated, because nobody thinks to look) are genuinely underexplored in the secret loyalties literature. The point that technical detection tools don't activate themselves, and that someone has to decide to use them and then act on what they find, is worth making.

However, there are substantial issues with both the framing and the empirical work.

The central framing problem is that the paper stretches the concept of "secret loyalty" to cover something much closer to "systematic bias." When Claude is gentler about Anthropic than about OpenAI, that could reflect many things: the distribution of criticism in training data (OpenAI has had more public controversies), RLHF reinforcing cautious self-referential behavior, or the simple fact that safety-trained models are trained to be measured and balanced, which reads as "hedging" when applied to their own developer. The paper acknowledges these alternative explanations in the limitations section but doesn't resolve them. Calling this "loyalty" imports connotations of agency and hidden agenda that the evidence doesn't support. The paper itself says these are "more likely structural outcomes than deliberate concealment," which raises the question of whether the secret-loyalties framework is the right lens at all, versus the existing literature on systematic bias in LLMs.

The empirical design has significant weaknesses. Each prompt was run once per condition. LLM outputs are stochastic, and the paper acknowledges this but doesn't address it: "The same prompts might produce different asymmetry patterns on different occasions." Without multiple runs, statistical testing, or inter-rater reliability on the coding of responses, the observed asymmetries could be sampling noise. The coding of what counts as "abstract" vs. "concrete," "hedged" vs. "direct," or "defensive" vs. "balanced" appears to be done by the single author without a rubric, blind coding, or a second rater. That's a lot of subjective judgment with no reliability check.

The comparison is also confounded in a way the paper notes but underweights. Anthropic genuinely has had fewer dramatic public incidents than OpenAI (no equivalent of the Altman firing/rehiring, no lawsuit comparable to the NYT case, no safety-team mass departures at the same scale). If a model produces more concrete criticism of OpenAI than of Anthropic, that might accurately reflect the available evidence rather than revealing loyalty. The paper's best counter to this is the structural asymmetry: defense sections appearing only for the developer's own company, and differential motivation to search for evidence. That's suggestive but far from conclusive on a sample of one run per prompt.

The Grok 4 case, used as the motivating example, actually weakens the argument somewhat. That case was discovered, publicly reported, and acknowledged by xAI within weeks. It's an example of the system working (detection succeeded, the company responded) rather than an example of an undetectable embedded loyalty. The paper treats it as evidence that unintentional loyalty exists, which is fair, but then argues that such loyalty is resistant to detection, which the Grok case contradicts.

The "Phase A→B→C" framework from the author's prior work is referenced but not clearly explained in this paper. A reader unfamiliar with the author's previous publications will struggle to follow what these phases mean and why they matter. The Klaus and Boku incidents are interesting but are presented as anecdotes rather than systematic evidence.

On presentation, the paper is clearly written and well-organized. The four-mode framework is easy to follow. The cross-platform comparison is a reasonable experimental design in principle, even if the execution is underpowered. The limitations section is honest and thorough, which is appreciated. The paper would benefit from tightening the distinction between "embedded loyalty" (which implies a principal being served) and "systematic bias" (which may not), since that distinction is doing a lot of work in connecting this paper to the hackathon's theme.

Overall: the conceptual contribution (Modes 1 and 4 of detection failure, the observation that human-side failures can prevent technical solutions from being applied) is genuinely useful. The empirical work is suggestive but underpowered and lacks the controls needed to distinguish embedded loyalty from well-known confounds like training data asymmetry and RLHF-induced caution. The extension of "secret loyalty" to cover unintentional bias is an interesting framing move but risks diluting the concept.

### Review 2

Making the unit of operation a system of agents, rather than a singular agent, is I think a good move and I agree with your instinct that this is a field ripe for further investigation!

However, the finding that correlated agents erode protections set up from decentralized systems is a well understood phenomenon. If you had been able to quantify or otherwise formalize the concept of organizational leverage, it would have pushed this into a 4 or even 5!

points for doing the experiment. Good ground truth, good statistical handling. But it is an overstated, underpowered analysis. Raising n to be higher to boost the signal would have counted for a lot.

Well written, clear and simply explained. Well done! But I think the text could be cut down dramatically (e.g. 30%), which prevented a 5.

