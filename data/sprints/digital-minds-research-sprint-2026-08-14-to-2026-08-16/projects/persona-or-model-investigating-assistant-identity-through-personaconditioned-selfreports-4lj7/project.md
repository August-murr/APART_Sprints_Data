# Persona or Model? Investigating Assistant Identity Through Persona-Conditioned Self-Reports

- Sprint: Digital Minds Research Sprint (digital-minds-research-sprint-2026-08-14-to-2026-08-16)
- Rank: unranked
- Team: Team Layered Minds
- Authors: Kgothatso Mashigo, Themba Shongwe
- Date / location: Aug 16, 2026 / Cape Town
- Page: https://apartresearch.com/sprints/projects/persona-or-model-investigating-assistant-identity-through-personaconditioned-selfreports-4lj7
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/fbf21a466e289c6f-37f3ff73-929a-4193-a3a0-9f58748b2e2a-Persona_or_Model_Track5_Paper.pdf
- Code: None

## Summary

This project investigates whether persona instructions change how AI assistants describe themselves, or mainly affect the style of their responses. Gemini, ChatGPT, and Claude were each given analytical and creative-social personas and asked the same set of questions about identity, continuity, preferences, values, and autonomy. They were then asked to respond without considering the assigned persona. We compared their responses using qualitative coding to identify patterns and differences across models. While all three assistants generally separated persona from genuine personal traits and denied human-like continuity or subjective experience, they differed in how they described the relationship between persona and the underlying model. The project highlights both the usefulness and limitations of AI self-reports when studying model identity and AI welfare.

## Reviews (2)

### Review 1

This project adds to the field's black-box surface level examinations of personas within LLMs. Thoughtfully, this is a very readable paper which positions itself well philosophically yet lacks sufficient citations or positioning within the existing research. The methodology is clearly thoughtful and the focus on "claims about I, continuity, preference, and values" is well established. Models family names are noted as the subjects but their version numbers, dates, and inference context would be valuable details to include in future works. The paper claims a noted "pattern not seen described elsewhere" however several of the presentations during this sprint touched on and noted exactly this same type of pattern and often brought it into study at a greater depth, so the authors would be encouraged to attend and closely note the presentations during future sprints. Furthermore, Anthropic's work on The Persona Selection Model, and persona vectors work (Chen et al., 2025), would be valuable background to which contextualize this and start from a further place within the research. While this did not find a green field research problem to address, this is still a thoughtful contribution to the behavioral observations in the study of persona and identity in LLMs. Its explicit self-classification as an exploratory pilot and its refusal to treat self-reports as evidence of internals are practices worth emulating.

### Review 2

This is a clearly written exploratory study addressing an important methodological question for AI welfare and model-identity research: whether persona instructions alter substantive self-reports or mainly their stylistic presentation. The cross-model comparison is useful, and I particularly appreciated the authors' care in distinguishing observed self-reports from claims about underlying model architecture or consciousness.

The main limitation is experimental replication. The most interesting finding—the difference between Gemini/ChatGPT's layered persona-over-model account and Claude's rejection of that framing—is currently based on one conversation per model/condition, so it is impossible to know whether this is a stable system-level difference or ordinary sampling/prompt variation. Repeating each condition across many fresh conversations, recording exact model versions, randomizing order, freezing identical prompts, and measuring the frequency with which each model produces each account would substantially strengthen the result.

Independent qualitative coding is also important. A second blinded coder and inter-rater agreement would help validate the nine-pattern framework. Some comparisons should additionally be standardized: for example, the Claude repeated-probing behavior is difficult to interpret cross-model because the amount and wording of repetition differed between systems.

A particularly informative follow-up would test whether each assistant can be induced to produce the other models' persona/model account under paraphrases and adversarial framing. If the layered-versus-non-layered distinction remains stable across independent samples and prompt variants, it would become a considerably stronger result. As presented, I view this as a useful pilot and protocol for generating hypotheses rather than strong evidence for stable cross-model identity differences.

