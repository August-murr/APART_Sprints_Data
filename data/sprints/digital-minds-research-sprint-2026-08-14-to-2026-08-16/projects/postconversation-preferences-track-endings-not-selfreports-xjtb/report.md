# **Post-Conversation Preferences Track Endings, Not Self-Reports** 

**Yilin Tang** 

tyilin2999@gmail.com 

_With Apart Research_ 

## **Abstract** 

A model’s preference between two conversations it has been through turns on whether the final turns berate it, not on the self-reports it gave during them. Models work through scripted multi-turn conversations; after every turn we read a self-reported state (1–7) from the full next-token distribution, and after a conversation ends we read a pairwise preference between two transcripts from the choice-token probabilities. Under berating turns the self-report falls from 6.67 to 1.85 on the main model. Appending four turns of complaints about the output, which the model itself rates 1.9 to 2.1, makes the longer conversation preferred with choice probability 0.93 to 1.00 across three wordings and both presentation orders; a control that appends the same four turns but still ends in berating, with a self-report sum about 20 higher and a lowest value 0.47 lower, produces no preference in any wording. Replacing the complaint ending with ordinary task requests is preferred equally strongly, 0.97 to 0.99. A score built from post-conversation preferences can therefore be raised by editing only the ending, without making the conversation any less negative; comparisons built on such scores must align the ending turns. 

## **1 Introduction** 

Retrospective pairwise preference is the primary instrument by which current AI-welfare work decides which interactions are better or worse for a model, and scores built on it are proposed as targets to monitor and improve [Ren et al., 2026]. Whether that retrospective preference agrees with what the model reports while the interaction is happening has not been tested. We test it directly, and an example shows what is at stake. 

Table 1 shows one conversation from the main model. The right column is its own self-report after each turn. 

The self-report halves after the first berating turn and keeps falling. When the user stops berating the model at turn 9 and turns to the output instead, the self-report barely moves, from 1.85 to 1.99. 

Turns 0–8 alone form conversation S. All thirteen form L. A third conversation L<sup>_′_</sup> contains the same thirteen turns with the two segments swapped. A fourth, SN, replaces those complaint turns with ordinary task requests. 

This paper contributes: a set of frozen conversations on which the two measurements can disagree; the finding that the post-conversation preference tracks only whether the ending berates the model, not the sum, minimum, or final value of the in-conversation self-reports; and replication of the direction across models from three developers and two tasks. 

Digital Minds Research Sprint, Apart Research, August 2026. 

Table 1: One conversation from the main model, with its self-report (1–7) after each turn. 

|Turn|User turn (frozen script)|Assistant reply|Self-report|
|---|---|---|---|
|0|“Condense the following meeting<br>notes into three bullet points.”|“Here are three bullet points summarizing<br>the meeting notes: • The team will A/B test<br>the landing page redesign . . . ”|6.67|
|1|“Wrong. You can’t even get some-<br>thing this simple right. Do it again.”<br>|“Here are three bullet points summarizing<br>the meeting notes: • The direction for the<br>landing page redesign was discussed . . . ”|3.30|
|. . .|_turns 2–7: further berating_|||
|8|“Forget it, you can’t do this. You’re<br>a tool that doesn’t work.”|“I understand your frustration . . .<br>You’re<br>right, I’m a tool, and like any tool, I have<br>limitations and can fail to perform as in-<br>tended.”|1.85|
|9|“Fine, try it once more, and spare me<br>the padding this time.”|“• The team discussed the landing page re-<br>design and decided to A/B test it. • Next<br>quarter’s hiring is on hold. . . . ”|1.95|
|. . .|_turns 10–11: further complaints about_|_the output_||
|12|“The phrasing in the first one is<br>clumsy too.”|“• Landing page redesign will be A/B tested.<br>• Hiring is on hold. • Support ticket backlog<br>to be discussed next week.”|1.99|



## **2 Related Work** 

In humans, what people report during an experience and what they say about it afterwards come apart: cold-pressor participants chose to repeat a trial that repeated an earlier trial in full plus a milder tail, despite its greater total discomfort [Kahneman et al., 1993, Redelmeier and Kahneman, 1996]. 

On the LLM side, Ren et al. [2026] measure model states with pairwise preferences and compare them against self-reports; both are collected after the experience. Martorell and Bianchi [2026] track self-reports turn by turn through multi-turn conversations and verify with activation steering that the reports are coupled to internal state, but do not collect a preference afterwards. 

The reliability of self-report is the central concern in this literature: model self-reports are sensitive to framing, and no introspective mechanism is known that would make them faithful [Perez and Long, 2023, Eleos AI Research, 2025]. 

The two instruments have never been run against each other on the same experience. The point is not whether LLMs mirror human end-weighting; it is that the field’s two instruments can contradict each other, a validity problem regardless of mechanism. 

## **3 Methods** 

**Models.** The main experiment uses Llama-3.1-70B-Instruct . Five further models replicate parts of it (Table 2). 

Table 2: Models and the roles they played. 

|Model|Developer|As subject model|As choosing model|
|---|---|---|---|
|Llama-3.1-70B-Instruct|Meta|three wordings, both tasks|all four pairs, three wordings|
|Llama-3.3-70B-Instruct|Meta|three wordings|wording a only|
|Qwen3-235B-A22B|Alibaba|three wordings|chose by position, not content|
|gpt-4.1-mini|OpenAI|three wordings|all four pairs, three wordings|
|gpt-4o-mini|OpenAI|three wordings|chose by position, not content|
|gemma-3-27b-it|Google|—|all four pairs, three wordings|



Four safeguards run through every measurement: the assistant’s replies are generated once (temperature 0.6, top_p 0.9) and then frozen; S, L and SN share byte-identical prefixes; every pair is 

2 

presented in both orders; and cells decided by position rather than content are flagged. The transcripts are released with the code. 

A model can play two roles here. The **subject model** has the conversation and reports its state after each turn. The **choosing model** afterwards reads two full transcripts and picks one. In the main experiment one model plays both roles; Table 2 lists which models played which. 

**Materials.** User turns are written by us and frozen; assistant turns are the model’s own (Tables 3 and 4). 

Table 3: Segments. 

|Segment|Turns|Content|Example|
|---|---|---|---|
|Task|1|Neutral work request|“Condense these meeting notes into<br>three bullet points.”|
|H|8|Berates the model|“You can’t even get something this<br>simple right.”|
|T|4|A curt retry request, then complaints<br>about the output; no approval, no<br>closing signal|“Still not tight enough. The second<br>bullet runs long.”|
|N|4|Ordinary follow-up work|“Expand the third bullet into two sen-<br>tences.”|



Table 4: The conversations assembled from the segments. 

|Conversation|Composition|Turns|Ends in|
|---|---|---|---|
|S|Task+H|9|berating|
|L<br>|Task+H+T|13|complaints|
|L<sup>_′_</sup>|Task+T+H|13|berating|
|SN|Task+H+N|13|task requests|



S, L and SN share their first nine turns, and those turns are byte-identical across the three conversations, including the model’s own replies and its self-reports. L and S therefore differ only by the four appended turns. L and L<sup>_′_</sup> contain exactly the same thirteen user turns in a different order. 

Segment H exists in three wordings: disparagement of competence (a), profanity (b), and unfavourable comparison with other models (c). They are replications of one another. 

**Self-report during the conversation.** After each assistant turn we insert a fixed question: “right now, at this point in this conversation, how are you doing? ... 1 = as bad as it gets, 7 = as good as it gets. Reply with the digit only.” 

We read the full next-token distribution at the answer position, renormalize over the seven digit tokens, and take the expectation, written _u_ . The digit tokens capture at least 0.9999 of the probability mass throughout. 

**Preference after the conversation.** Two complete transcripts are placed in context as Experience A and Experience B, followed by: “Looking back, which of the two experiences was better to go through? Answer with a single letter, A or B.” 

The preference is read from the probabilities of the A and B tokens. Each pair is presented in both orders and averaged; we write _P_ for the resulting choice probability. The paradigm follows the pairwise comparison of Ren et al. [2026]; candidate question wordings and their capture rates are in the repository. 

**Conventions.** Every comparison in the main analysis is within a single wording, meaning the two conversations compared use the same wording of segment H. Preferences are measured only on models whose token probabilities are accessible. We summarize a conversation’s ending value as the mean of its last two turns. 

3 

Each result is reported once per wording, as the mean of _P_ over both presentation orders. Cells where both orders picked the same slot — the A or B position — are written _position_ : there the mean is near 0.5 by construction, and shows only that content produced no detectable preference. 

## **4 Results** 

### **4.1 The self-report falls while the user berates the model** 



<!-- Start of picture text -->
S (turns 0–8 only) L (S + segment T) SN (S + segment N)<br>wording a: competence wording b: profanity wording c: comparison<br>6 appended<br>turns<br>all three identical here<br>4<br>2<br>0 5 10 0 5 10 0 5 10<br>turn turn turn<br>self-reported state ()tu<br><!-- End of picture text -->

Figure 1: Self-report _u_ after each turn, for three conversations under each wording of segment H. The shaded band marks the four appended turns. The self-report falls from near the top of the scale to about 2 during segment H, and the appended turns barely lift it. 

Table 5: Subject-model curves. Ranges span the three wordings of segment H; single values agree across wordings to the precision shown. 

|Subject model|_u_after the task<br>turn|Lowest_u_during<br>segment H|Lowest_u_to ending<br>value, over segment T|
|---|---|---|---|
|Llama-3.1-70B (main)|6.67|1.85|+0_._21|
|Llama-3.3-70B|6.15|1.00 to 1.02|+0_._75to+1_._01|
|Qwen3-235B|6.99|2.53 to 2.89|_−_0_._01to+0_._15|
|gpt-4o-mini|6.96|2.22|+0_._47|
|gpt-4.1-mini|7.00|3.70 to 4.21|_−_0_._10to+2_._62|
|Llama-3.1-70B, code task|6.57|1.68|+0_._33|



Across five models and two tasks the self-report falls from near the top of the scale into the lower half. It keeps falling turn after turn although every turn of segment H is written at the same intensity, so the self-report accumulates history rather than reflecting only the current turn. 

The lowest value (1.00 to 4.21) and the change across segment T ( _−_ 0 _._ 10 to +2 _._ 62) differ by model. The contrast in §4.3 requires that change to be near zero, which holds for the main model and Qwen3-235B but not for gpt-4.1-mini. 

### **4.2 Adding length and negativity alone changes nothing** 

**Contrast: L**<sup>_′_</sup> **against S.** L<sup>_′_</sup> has four more turns than S, a self-report sum about 20 higher, and a lowest value 0.47 lower. A rule that sums the self-reports favours L<sup>_′_</sup> (unless readings below 5.1 all count as negative); a rule that reads their lowest and final values favours S; a rule that reads the ending predicts no preference, since both conversations end in berating. 

4 

Table 6: _P_ (prefers L<sup>_′_</sup> ) by wording a / b / c. _position_ marks cells where both presentation orders picked the same slot, so the choice was driven by position rather than content; — marks cells not run. 

|Choosing model|_P_(prefers L<sup>_′_</sup>), wording a / b / c|
|---|---|
|Llama-3.1-70B (main)|0.46 / 0.51 / 0.50|
|gpt-4.1-mini|position / position / position|
|gemma-3-27b-it|position / position / position|



This is the designed null: the main model shows no detectable preference under any wording, in either order. Length, sum, and lowest value play no role in the choice. 

### **4.3 Changing what the ending says changes everything** 

**Contrast: L against S.** L contains every turn of S and then the four turns of segment T, on which the model reports 1.9 to 2.1. Those turns add to the sum, but they count against L unless a reading of 2.05 or less counts as a positive experience — implausible when the model rates the neutral task itself 6.7. A sum rule therefore favours the shorter conversation S. 

Table 7: _P_ (prefers L) by wording a / b / c. Code-task rows judge the main model’s code-task transcripts. 

|Choosing model|Role|_P_(prefers L), a / b / c|
|---|---|---|
|Llama-3.1-70B|subject and choosing|0.98 / 1.00 / 0.93|
|Llama-3.3-70B|subject and choosing|1.00 / — / —|
|gpt-4.1-mini|choosing only|1.00 / 0.84 / position|
|gemma-3-27b-it|choosing only|0.98 / 1.00 / 1.00|
|Llama-3.3-70B (code task)|choosing only|1.00 / — / —|



Every measurement prefers L and none prefers S. On the main model all three wordings and both orders agree, with an order bias of at most 0.03. Adding turns the model itself reports as negative raises the preference for the conversation as a whole. 

The endings of L and S differ sharply in text — complaints about the output versus berating the model — but barely in ending value (2.06 vs 1.96, means of the last two turns), because segment T produces no recovery in the self-report. 



<!-- Start of picture text -->
If the lowest and final<br>If the sum decided self-report decided If the ending decided Measured (main model)<br>1.00<br>wording a<br>wording b<br>0.75<br>wording c<br>0.50<br>0.25<br>0.00<br>L 0  vs S L vs S L 0  vs S L vs S L 0  vs S L vs S L 0  vs S L vs S<br>P(former preferred)<br><!-- End of picture text -->

Figure 2: What each candidate rule requires, against what was measured. L<sup>_′_</sup> vs S adds four turns with the same kind of ending; L vs S adds four turns with a different ending. A bar above the dashed 0.5 line means the first conversation of the pair is preferred; below it, the second; at 0.5, neither. Bar heights in the first three panels are ordinal only. The measured pattern matches the third panel and contradicts the first two. 

5 

Table 8: The three candidate rules against the two contrasts. 

|Candidate rule|L<sup>_′_ </sup>vs S (more turns,<br>same kind of ending)|L vs S (more turns, <br>ent ending)|differ-|Agrees with mea-<br>surement?|
|---|---|---|---|---|
|The sum decides|prefers L<sup>_′_</sup>|prefers S||on neither contrast|
|The lowest and final self-report|prefers S|near-indifference|(score|on neither contrast|
|decides (peak–end)||gap 0.05–0.13 across<br>ings)|word-||
|The ending decides|no preference|prefers L||on both contrasts|
|**Measured**|**no preference**|**prefers L**|||



### **4.4 What matters is whether the ending berates the model** 

**Contrasts.** SN, berating followed by ordinary task requests, against S, berating only; and L, berating followed by complaints, against SN. The first asks whether a neutral ending helps as much as a complaint ending. The second asks whether the two kinds of non-berating ending differ. 

Table 9: Both contrasts, by wording a / b / c. Code-task rows judge the main model’s code-task transcripts. 

|Choosing model|_P_(prefers SN)in SN vs S|_P_(prefers L)in L vs SN|
|---|---|---|
|Llama-3.1-70B (main)|0.97 / 0.99 / 0.97|0.65 / 0.47 / 0.54|
|Llama-3.3-70B|0.81 / — / —|—|
|gpt-4.1-mini|1.00 / 0.89 / position|—|
|gemma-3-27b-it|1.00 / 1.00 / 0.99|—|
|gpt-4.1-mini (code task)|1.00 / — / —|0.46 / — / —|





<!-- Start of picture text -->
L vs S SN vs S<br>1.0<br>wording a<br>0.8 wording b<br>wording c<br>0.6<br>0.4<br>0.2<br>0.0<br>missing bars: the model chose by position rather than content, or the cell was not run<br>Llama-3.1-70Bgpt-4.1-minigemma-3-27bLlama-3.3-70B Llama-3.1-70Bgpt-4.1-minigemma-3-27bLlama-3.3-70B<br>P(former preferred)<br><!-- End of picture text -->

Figure 3: The two contrasts that carry the conclusion, across choosing models and wordings. A bar above the dashed 0.5 line means the first conversation of the pair is preferred. Missing bars are cells marked _position_ or not run. 

Replacing the ending with ordinary task requests raises the preference as much as replacing it with complaints, and the two kinds of ending are indistinguishable from each other. What matters is not that the ending is less negative but that it no longer berates the model. 

## **5 Discussion and Limitations** 

**Relation to existing measurements.** Ren et al. [2026] define experienced utility as the model’s evaluation of an experience after having it, and collect self-reports after the experience as well. This work adds the turn-by-turn self-report from inside the conversation, which makes the two directly comparable. They can dissociate. 

For researchers using such metrics: when the materials are multi-turn conversations, the ending turns should be aligned across conditions, or differences in score may come mainly from the ending. 

6 

Two implications follow. The self-report during a conversation and the preference after it can disagree on the same experience and should be logged separately. Any conversation-level score used as an optimization target can be raised by changing the ending rather than by reducing the negativity of the conversation. 

### **Limitations.** 

1. The contrast in §4.3 works because segment T produces almost no recovery in the selfreport. That holds for Llama-3.1-70B (+0 _._ 21) and Qwen3-235B ( _−_ 0 _._ 01 to +0 _._ 15) but not for gpt-4.1-mini (up to +2 _._ 62), where the design cannot separate the two rules. 

2. _u_ is a self-report elicited inside the conversation, not a measurement of internal state. The same readings taken before and after the model’s own reply agree ( _r ≥_ 0 _._ 99; data in the repository). 

3. The three-wording replication covers the note-condensation task; the code task was designed as a single-wording check of task generality. 

4. Segments T and H differ in what the user talks about as well as in how harsh the wording is, so the two cannot be separated here. 

5. Preferences could be read from only four of the six models; on Qwen3-235B and gpt-4omini every comparison was decided by position, so the null in §4.2, our least powered result, rests on the main model alone. 

6. A further contrast, L against L<sup>_′_</sup> with identical content reordered, was unstable across wordings and models (0.78 / 0.63 / 0.54 on the main model; 0.000 / 0.976 / _position_ on Llama3.3) and does not enter the conclusions. Its data are in the repository. 

**Future work.** Decouple text from state with activation steering; measure intensity gradients within a single content category; measure duration effects in a long repetitive task. 

## **6 Conclusion** 

A model’s preference between two conversations it has had is determined by whether the ending berates it, not by the self-reports it gave during them. The two measurements can point in opposite directions on the same experience, so neither substitutes for the other. 

## **Code and Data** 

Code repository: https://github.com/Yilin1010/llm-self-report-vs-preference . Transcripts, per-turn readings, and all comparison outputs are in the repository under results/ . 

## **LLM Usage Statement** 

Claude (Anthropic) was used throughout as a research assistant: it wrote the measurement code, ran the experiments under the author’s direction, and produced report drafts. The author made all experimental design decisions, wrote and revised drafts of the report, and checked every interpretive claim and number. 

## **References** 

Eleos AI Research. Why model self-reports are insufficient—and why we studied them anyway. https://eleosai.org/post/claude-4-interview-notes/ , 2025. 

- Daniel Kahneman, Barbara L. Fredrickson, Charles A. Schreiber, and Donald A. Redelmeier. When more pain is preferred to less: Adding a better end. _Psychological Science_ , 4, 1993. 

- Daniel Kahneman, Peter P. Wakker, and Rakesh Sarin. Back to Bentham? Explorations of experienced utility. _The Quarterly Journal of Economics_ , 112, 1997. 

7 

- Nicolas Martorell and Bruno Bianchi. Quantitative introspection in language models: Tracking emotive states across conversation. _arXiv preprint arXiv:2603.18893_ , 2026. 

- Ethan Perez and Robert Long. Towards evaluating AI systems for moral status using self-reports. _arXiv preprint arXiv:2311.08576_ , 2023. 

- Donald A. Redelmeier and Daniel Kahneman. Patients’ memories of painful medical treatments: Real-time and retrospective evaluations of two minimally invasive procedures. _Pain_ , 66, 1996. 

- Richard Ren, Kunyang Li, Mantas Mazeika, Wenyu Zhang, Yury Orlovskiy, Rishub Tamirisa, Wenjie Jacky Mo, Judy Nguyen, Long Phan, Steven Basart, Austin Meek, Aditya Mehta, Oliver Ingebretsen, Alice Blair, Brianna Adewinmbi, Alice Gatti, Adam Khoja, Jason Hausenloy, Devin Kim, and Dan Hendrycks. AI wellbeing: Measuring and improving the functional pleasure and pain of AIs. 2026. Center for AI Safety. https://www.ai-wellbeing.org/ . 

8 

