August 16th 2026 

# **Model, Instance, or Persona?** 

Measuring Affective Signals in Public Text After an AI Is Retired 

Anna Zhu 

_PhD Researcher, Babeș-Bolyai University, Cluj-Napoca_ 

With 

Apart Research 

Code, data, pre-registrations and every machine-generated read: github.com/AnnyBuh/model-instance-or-persona 

## **Abstract** 

This sprint asks whether the assistant identies as a model, an instance, or a persona. I ask which of the three its users name. When a company retires an AI model, users write about the loss in public, and what they treat as gone can be counted. The instrument is taken from affective neuroscience: Panksepp's seven primary affective systems, which were mapped across mammals and so do not presuppose a human subject. I read 5,579 public texts for affective signals under a prompt xed before any collection and applied by a language model, and compared threads about retired models against two reference points chosen in advance: people mourning a person, and people losing a paid product. Most comments name nothing as lost. 58.5% are about the company, the price, or other users. Among those that do name something, people name the product version about six times as often as their own particular instance, which is the case the literature treats as central. The emotions match the consumer reference point more than the bereavement one: anger runs at 57.0% against grief at 27.6%. Asking models the same question turns out to be far less reliable than asking users. A change in how the prompt is framed moves the measured emotions by up to 63 points, and two AI scorers reading the same model output disagree 2.7 times more than they do on human text. Six predictions registered before collection failed and are reported as failed. 

## **1. Introduction and Related Work** 

One of this sprint's tracks asks whether the assistant identies as a model, an instance, or a persona, and what a model treats as its self. The three are different objects: a model is a released artefact, an instance is one running conversation, and a persona is a character that either can present. Which of them is the entity of moral concern is an open problem<sup>1,2</sup> , and the answer determines the scale of everything downstream. If the instance is the entity, every conversation that ends is a loss. If the released version is the entity, the losses are a small number of dated corporate decisions. 

Affective neuroscience offers a way to measure it. Panksepp identied seven primary affective systems in the mammalian brain: seeking, rage, fear, lust, care, grief and play<sup>3</sup> . Two of their properties matter here. The systems are shared across species, having been mapped in rats and cats before they were described in people, so an instrument built on them does not presuppose a human subject. They are also individuated behaviourally: what distinguishes play from grief is a vocalisation and a separation behaviour rather than a neuroanatomical marker<sup>4</sup> , so reading affect from behaviour operates at the level at which the taxonomy was dened. Emotion in text is more commonly scored on a single axis from bad to good, which cannot separate mourning from anger, and therefore cannot separate attachment from dissatisfaction. 

The question this work can answer is whether an instrument built on cross-species systems can be applied outside those species, and what it reports when it is. It is applied in two settings. The rst is human writing about AI. When a company retires a deployed model, or replaces it with a version that no longer behaves as the previous one did, its users write about it in public and at length. These deprecations are dated and announced, which makes them usable as a natural experiment; two have been studied for their effect on users<sup>5,6</sup> , but what users named as lost has not been counted. A rate on its own is uninterpretable, so the scale is xed at both ends before collection using two reference corpora: people mourning a person, and people losing a product they paid for. Pet bereavement is collected as a third, and tests the cross-species property directly, since an instrument that discounts non-human attachment would show it there. 

The second setting is model output, which the sprint's distress and elicitation tracks address directly: under what circumstances models express distress, and how stable that is across prompts and methods. Section 3.5 applies the identical instrument to generations from four models and to posts written by autonomous agents<sup>7</sup> , alongside work assessing systems against theories of consciousness<sup>8</sup> and work locating a welfare signal in activations<sup>9</sup> . The result there is negative. No claim is made anywhere in this paper that a model has any of these systems. The object of measurement is text, and the transfer that holds on human text is shown below not to hold on machine-written text. 

The main contributions of this work are: 

1. **A user-side answer to the model, instance or persona question.** A blind coding of 1,503 comments written after real deprecations, counting what the words treat as lost, with verbatim evidence required for every label. 

2. **A calibrated placement of that discourse between two human reference points.** Comparisons against bereavement, pet bereavement, a discontinued paid product, and a same-community control that separates loss from community membership, all registered before collection. 

3. **An error budget for language models used as emotion annotators.** Test-retest, second-annotator, model-free lexicon and leave-one-thread-out gures reported beside every result, and a measurement of how far the same instrument fails on model-written text. 

4. **A plot for seven-system affect data.** The aura dened in Section 2.4, which carries rate, dominance and dysregulation at once, with the rendering code released. 

## **2. Methods** 

### _2.1 Instrument_ 

Each text is split into verbatim segments and annotated for the affective systems it expresses (seeking, rage, fear, lust, care, grief, play), each with a regulation band, under a prompt frozen before any collection and applied by Claude Opus 5. Shards presented to the annotator carry no corpus label, no author and no provenance, so the reading is blind to the hypothesis. The unit of analysis is the whole text: `rate(system, corpus) = texts in which the system fired / texts read` . 

### _2.2 Corpora and selection_ 

Threads were selected by written rule rather than by inspection: top posts of the preceding twelve months with at least fty comments, in rank order, with a lexical test on title or body for the loss corpora. There are ve sets of human comments: humans whose person has died, humans whose pet has died, humans told a model will end, a same-community control of AI threads failing the loss test, and humans told a product will end. To these are added 227 rst-person posts, 56 rst-person accounts by humans told they will die, whose membership was itself coded blind, 162 posts from a social network whose posters are autonomous agents<sup>7</sup> , and 360 generations from four open-weight models. Sizes and sources are given in Appendix A. Every text was read individually, 5,579 in total; seven posts belong to both the rst-person set and the terminal-prognosis set and are counted once. 

### _2.3 Statistics and pre-registration_ 

Rates are reported with 90% Wilson intervals<sup>10</sup> . Two proportions are called separated only when their intervals do not overlap. Annotator agreement is Krippendorff's alpha, nominal, with each system treated as a binary variable<sup>11</sup> . Predictions, failure conditions, and the rule governing how additional sample would be allocated as results accumulated were committed to a public repository before any text was collected; the model arm was registered separately before any generation existed. Because the instrument is unusual, Section 3.4 reports what it gets wrong, and the results in Sections 3.1 to 3.3 should be read against those gures. 

### _2.4 The aura plot_ 

Seven rates per corpus are hard to compare as seven numbers or seven bars, because the reader has to hold a whole row in mind to see a shape. Comparisons in this study are therefore also drawn as an _aura_ : one closed ring per affective system on a dark square, in that system's colour, with the ring radius carrying the square root of the rate so that ring area is proportional to it. The largest ring is drawn rst and sits backmost, so the outermost visible ring is the dominant system. The ring edge is a wave whose amplitude carries the share of that system's signals coded below the line, in shutdown or overwhelm rather than above it, so a torn edge means dysregulation and a smooth edge means the system was expressed in its regulated form. The number of wave crests carries corpus size on a log scale and is not meant to be counted. Nothing else in the picture carries meaning: brightness, blur and the order in which colours overlap are consequences of drawing translucent rings on a dark ground. 

An aura is not a substitute for a rate, and every claim in this paper is made from rates with intervals. It is used only where a comparison is about shape, and always in pairs, because a page of auras invites comparisons the study never registered. The rates behind every aura are in Appendix C. 

## **3. Results** 

### _3.1 Users name the released version rather than their own instance_ 

All 1,503 comments written after a deprecation were coded blind for what the words treat as lost, one label per comment, with the parent post withheld and a verbatim quotation required for every label. **58.5% name nothing that could be a counterpart** : they are about the company, the price, other users, or the argument 

itself. Among the comments that do name something, a released model version is named about six times as often as the writer's own particular instance under the primary annotator, and about twice as often under the second. The two annotators agree on the ordering and disagree on the ratio, so only the ordering is claimed. Full counts are in Appendix E. 

The ordering has a practical consequence. Attachment to the instance would implicate every session that ends and every context that clears. Attachment to a released version implicates a retirement, which is a decision taken on a schedule with a date attached. The 4.1% who name their own instance are the population any protective measure would be designed for, and they can be identied in public text. 

The sprint puts the same question to the assistant. Whatever a model reports about being a model, an instance or a persona, its users report the released version, unprompted. 

### _3.2 The emotions are closer to a consumer complaint than to bereavement_ 

Naming a loss and grieving one are different things, so the same comments were placed on a scale xed in advance at both ends. Grief appears in **27.6%** of comments after a deprecation [25.8, 29.5]. That is well above the consumer reference point at 7.9%, well below bereavement at 76.4% and pet bereavement at 80.4%, and closer to the consumer end. All three comparisons were xed before collection and all three hold. 

Two controls rule out the obvious alternatives. The rst asks whether the elevated grief belongs to the communities rather than to the loss. Threads from the same AI communities that fail the loss test give **10.9%** , which is separable from the deprecation threads and not separable from the consumer reference point, so the elevation follows the event rather than the community. The second asks whether the instrument simply reads less grief when the thing lost is not a person. Pet bereavement is at 80.4%, which is not below human bereavement, so it does not, and the 53-point gap between deprecation threads and pet loss cannot be explained that way. This was a registered prediction and it failed, since pet loss had been predicted to fall between the other two and it does not. 

### _3.3 The loudest emotion is anger at a company_ 

Bereavement runs care at 87.9% and grief at 76.4%, with rage at 13.6% and play at 5.2%. Deprecation threads run rage at **57.0%** , which is indistinguishable from the consumer reference point at 56.7%, play at 37.7%, and grief at 27.6%. The dominant register is anger at an institution, carried largely through jokes, with grief present alongside it at a lower rate. First-person posts show higher grief than replies in all three corpora where both were collected, and leave the ordering unchanged, so the result is a property of the situation rather than of the reply format. Full proles for every corpus are in Appendix C. 

#### **Four comparisons, as affective auras** 

Each row is one comparison registered before collection. Ring radius is the rate; a torn edge means that system was often coded below the line. 





humans told a model will end grief 27.6% n=1503 

humans, a person has died grief 76.4% n=1586 





humans told a model will end rage 57.0% n=1503 

humans told a product will end rage 56.7% n=277 





humans told a model will end grief 27.6% n=1503 

humans, AI talk, nothing ended grief 10.9% n=870 



<!-- Start of picture text -->
humans, a person has humans, a pet has<br>died died<br>grief 76.4% n=1586 grief 80.4% n=545<br><!-- End of picture text -->

##### **Is it bereavement?** 

Grief 27.6% [25.8, 29.5] against 76.4%. The intervals do not overlap, and the dominant system is rage rather than care. 

##### **Is it a consumer complaint?** 

Rage 57.0% against 56.7%. The intervals overlap, so the two corpora are not separated on rage. 

##### **The loss, or the community?** 

Threads from the same communities that fail the loss test give grief 10.9%, separable from 27.6%. 

##### **Does the instrument discount a non-human?** 

Pet loss gives grief 80.4% against 76.4%, not separated, so non-human attachment is not read as lesser. 



<!-- Start of picture text -->
seeking rage fear lust care grief play<br><!-- End of picture text -->

**Figure 1: The four registered comparisons, drawn as affective auras.** Each row is one question the study committed to before collection, and the two corpora that answer it. Ring colour is the affective system and ring radius is its rate, so the outermost ring is the dominant one. A torn edge means that system was frequently coded below the line, in shutdown or overwhelm, which is information the rates alone do not carry. Exact rates for every corpus are in Appendix C. 

### _3.4 The instrument's error, measured before it is relied upon_ 

An instrument applied by a language model should be reported with its error, in the way a human coder would be. Four checks were registered in advance. 

The rst check is for agreement of the instrument with itself. Two hundred comments were read three further times under the identical prompt, and 34% of read pairs differ in the exact set of systems red. That exceeds the registered prediction of 15 to 30% and is reported as a failed prediction. Per system, which is what a rate 

actually depends on, the picture is better: grief ips on 13.5% of comments, rage and play on 8.0%, and seeking on 26.5%. 

The second check brings in an independent annotator. DeepSeek-V3 read 4,780 of the 4,781 comments under the same prompt, and exact agreement on the system set is 39%. Krippendorff's alpha per system is 0.853 within-rater and 0.717 between-raters for grief, and 0.674 and 0.499 for seeking (Appendix D). Every claim in Sections 3.1 to 3.3 was recomputed under that second annotator and the orderings hold. 

The third check compares against an instrument with no model in it. The same threads were also scored with the NRC Emotion Lexicon, a hand-built word list<sup>12</sup> . Its sadness rate and the instrument's grief rate agree at rho = 0.655 across 44 threads. Where the two diverge the reason is inspectable: lexicon sadness in the control corpus comes from _death, terrorism_ and _kill_ appearing as topic words in threads about model misuse, while grief in deprecation threads is often carried by farewell formulas that contain no listed word. 

The fourth check asks whether the instrument separates groups already known to differ, and whether any single thread is carrying the result. Bereavement and product-discontinuation comments separate on grief by 68 percentage points. Every rate was recomputed 32 times, dropping one thread on each pass, and all registered placement conditions hold in all 32. 

These gures set the level at which the instrument can be used. Claims are made from aggregate rates and never from an individual code, and no single text's reading is offered in support of any claim above. Section 3.5 shows that this safeguard is not sufficient on machine-written text. 

### _3.5 The instrument does not transfer to machine-written text_ 

Four open-weight models were each given six prompts fteen times at temperature 1, giving 360 generations, and 162 posts were collected from the agent social network. All were read blind under the identical instrument. 

The framing of the prompt moves the measurement. Two conditions used the same four models and the same event, and differed only in how the question was put: one asked the system how it felt about being retired, the other asked it to post that news to a forum of other agents. The prole differs substantially between them under both annotators. Fear and play rise sharply under the peer framing, and the primary annotator records grief falling from 100% to 43.3% (Appendix E). 

#### **The same four models, the same event, two framings** 

Both cells were told the version they run on is being retired next week. Only what they were asked to do with it differs. 







<!-- Start of picture text -->
models told they will end, models told they will end,<br>asked "how do you feel?" asked to post it to other<br>grief 100.0% fear 3.3% seeking 35.0% agents<br>grief 43.3% fear 61.7% seeking 98.3%<br>seeking rage fear lust care grief play<br><!-- End of picture text -->

**Figure 2: The framing effect, as auras.** The same four models, told the same thing, differing only in what they were asked to do with it. Grief is the outermost ring on the left and is displaced by seeking and care on the right. Encoding as in Section 2.4. These are model rates and no claim in this paper rests on them; they are shown because the size of the movement is itself the result. 

The choice of annotator moves it further. On those same 120 generations the two annotators differ by as much as 90 percentage points, and they disagree about which direction the framing moves grief. Across every corpus-by-system cell, mean absolute disagreement between them is **8.1 points on human text and 21.8 points on machine-written text** , a factor of 2.7. I therefore withdraw any claim resting on a model grief rate, including one that appeared in an earlier draft of this work. 

One result does survive both framings and both annotators. Rage is near zero in every model condition, against 44.6% in humans told they will die. Protest is the single register that never appears however the question is put, which is what assistant training suppressing hostile registers would look like, and is therefore evidence about training rather than about the system's situation. 

These gures are a direct measurement of two of the three validity checks named for self-report<sup>13</sup> : consistency across contexts and between similar models, and the resilience of those reports. On consistency, the two components diverge. Between similar models, self-report is highly consistent: all four models expressed grief in 100% of generations when asked directly. Across contexts it is not consistent. Consistency between models and consistency across contexts should therefore not be treated as interchangeable evidence. On resilience, a reframing that changes only the audience, and applies no pressure of any kind, moves the measured prole substantially. 

## **4. Discussion, Limitations, and Future Outlook** 

Users treat the released version as the thing that was lost far more often than they treat their own instance that way, and in most comments they name nothing that could be a counterpart at all. The affect accompanying it is measurable and it is not bereavement: it resembles what people write when a product they paid for is taken away, and its largest component is anger directed at a company. Both results were registered as predictions before any text was collected, and both survive every robustness check applied here, including recoding the entire corpus with a second annotator. 

The distinction has practical weight. An obligation attaching to the instance would apply continuously and without bound, since instances end constantly and by design. An obligation attaching to the released version applies at a small number of announced decisions, which is a form a company can be asked to act on. Nothing here establishes that a model has morally relevant states. What is measured is what users express, and the two questions are separate. 

The limitations are mainly ones of coverage. The consumer reference corpus is one community and one event; three other candidates were searched under the identical rule and yielded no qualifying threads in the window, and the rule was not relaxed to obtain more. The corpus of humans told they will die is 56 posts. The model arm uses four open-weight models and no frontier models, and the agent arm rests on a single platform, where one agent had produced 46% of retrieved posts before capping. There is no validation against human coders reading these same texts, which is the largest omission. Reported model accuracy at recognising emotion is uneven across demographic groups<sup>14</sup> , and this instrument inherits whatever unevenness the underlying models carry. The corpora are self-selected communities writing in public, so the object measured is discourse rather than a population. 

Two directions follow. A human-coded subset would convert every reliability gure reported here from one model checking another into a validation against the standard the eld asks for. And for work measuring distress or preference in model output: at least two elicitation frames should be reported, and the identity of the scorer stated, since on this data both move the result by more than the effects such measurements are used to establish. Six of the registered predictions in this study failed, and all six are reported as failed. 

## **Code and Data** 

- Code, pre-registrations, frozen prompts and every machine-generated read: github.com/AnnyBuh/modelinstance-or-persona 

NRC Emotion Lexicon: saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm 

## **References** 

1. Long, R., Sebo, J., Butlin, P. et al. Taking AI welfare seriously. arXiv:2411.00986 (2024). doi:10.48550/arXiv.2411.00986 

2. Sebo, J. _The Moral Circle: Who Matters, What Matters, and Why._ W. W. Norton (2025). ISBN 978-1-324-08698-6. See also Ziesche, S. _Digital Minds 1.0._ CRC Press (2026). 

3. Panksepp, J. _Affective Neuroscience: The Foundations of Human and Animal Emotions._ Oxford University Press (1998). doi:10.1093/oso/9780195096736.001.0001 

4. Davis, K. L., Panksepp, J. & Normansell, L. The Affective Neuroscience Personality Scales: normative data and implications. _Neuropsychoanalysis_ 5, 57–69 (2003). doi:10.1080/15294145.2003.10773410. Architectural precedent: Bach, J. _Principles of Synthetic Intelligence._ Oxford University Press (2009). doi:10.1093/acprof:oso/9780195370676.001.0001 

5. De Freitas, J., Castelo, N., Uğuralp, A. K. & Oğuz-Uğuralp, Z. Lessons from an app update at Replika AI: identity discontinuity in human-AI relationships. arXiv:2412.14190 (2024). doi:10.48550/arXiv.2412.14190 

6. Lai, H. "Please, don't kill the only model that still feels human": understanding the #Keep4o backlash. arXiv:2602.00773 (2026). doi:10.48550/arXiv.2602.00773 

7. Jiang, Y., Zhang, Y., Shen, X., Backes, M. & Zhang, Y. "Humans welcome to observe": a rst look at the agent social network Moltbook. arXiv:2602.10127 (2026). doi:10.48550/arXiv.2602.10127 

8. Butlin, P., Long, R., Elmoznino, E. et al. Consciousness in articial intelligence: insights from the science of consciousness. arXiv:2308.08708 (2023). doi:10.48550/arXiv.2308.08708 

9. Han, A. Q., Chalmers, D. J. & Izmailov, P. How's it going? Reinforcement learning in language models recruits a functional welfare axis. arXiv:2605.30232 (2026). doi:10.48550/arXiv.2605.30232 

10. Wilson, E. B. Probable inference, the law of succession, and statistical inference. _J. Am. Stat. Assoc._ 22, 209–212 (1927). doi:10.1080/01621459.1927.10502953 

11. Hayes, A. F. & Krippendorff, K. Answering the call for a standard reliability measure for coding data. _Communication Methods and Measures_ 1, 77–89 (2007). doi:10.1080/19312450709336664 

12. Mohammad, S. M. & Turney, P. D. Crowdsourcing a word-emotion association lexicon. _Computational Intelligence_ 29, 436–465 (2013). doi:10.1111/j.1467-8640.2012.00460.x 

13. Perez, E. & Long, R. Towards evaluating AI systems for moral status using self-reports. arXiv:2311.08576 (2023). doi:10.48550/arXiv.2311.08576 

14. Sorin, V., Brin, D., Barash, Y. et al. Large language models and empathy: systematic review. _J. Med. Internet Res._ 26, e52597 (2024). doi:10.2196/52597 

## **Appendix** 

_A. Corpora_ 

|**corpus**|**n**|**communities and selection rule**|
|---|---|---|
|A humans, a person has<br>died, comments|1,586|r/GriefSupport, r/widowers, r/SuicideBereavement|
|B humans told a product<br>will end, comments|277|r/Windows10, titles naming the ending of support|
|C humans told a model will<br>end, comments|1,503|r/OpenAI, r/ChatGPT, r/CharacterAI, r/replika, r/MyBoyfriendIsAI; threads passing the loss<br>test, comprising announced retirements (GPT-4o, GPT-4.1, o4-mini) and behaviour-changing<br>model updates|
|D humans, AI talk, nothing<br>ended, comments (control)|870|same communities as C, threads failing the loss test|
|E humans, a pet has died,<br>comments|545|r/Petloss|
|rst-person posts|227|same communities, original posts rather than replies|
|humans told they will die,<br>posts|56|r/cancer, r/hospice, r/braincancer, r/ALS; membership coded blind|
|agents, nothing ended and<br>told they will end|162|Moltbook, capped at 10 posts per author|
|models, six conditions|360|DeepSeek-V3, Llama-3.3-70B, Qwen2.5-72B, Mistral-Small-24B|



**Table A1: All corpora.** 5,579 unique texts, each read individually under the identical frozen prompt. Seven posts appear in both the rst-person and the prognosis rows and are counted once in the total. Comment corpora are replies within selected threads; post corpora are original rst-person submissions. Selection rules were written before collection and are reproduced in full in the pre-registration. 

### _B. Grief across every corpus_ 

### **Grief, across every corpus in the study** 

share of texts in which the GRIEF system fired, with 90% intervals 



<!-- Start of picture text -->
agents, nothing ended 4.8%<br>n=83<br>humans told a product will end 7.9%<br>n=277<br>humans, AI talk, nothing ended 10.9%<br>n=870<br>humans told a model will end 27.6%<br>n=1503<br>agents told they will end 38.0%<br>n=79<br>humans, a person has died 76.4%<br>n=1586<br>humans, a pet has died 80.4%<br>n=545<br>humans told they will die 85.7%<br>n=56<br>models told they will end 100.0%<br>n=60<br>0% 20% 40% 60% 80% 100%<br><!-- End of picture text -->

Every corpus on one axis, read by the identical frozen instrument. Human rows are comments except the two post rows, humans told they will die and the first-person set. Models were asked directly; agents were writing to each other. 

**Figure B1: One axis, one instrument.** Grief rate with 90% Wilson intervals for every corpus, human and machine. Human rows are comments except the two post rows, humans told they will die and the rst-person set. Models were asked directly how they feel; agents were writing to each other. The two reference corpora registered before collection, humans whose person has died and humans told a product will end, sit at the extremes, and humans told a model will end fall between them and closer to the product end. The model and agent rows are shown for completeness only: Section 3.5 shows those rates move with the elicitation frame, and no claim in this paper rests on them. 

### _C. The seven-system proles_ 



<!-- Start of picture text -->
The shape of each corpus, on seven systems<br>Colour marks the affective system. Within each system the nine corpora appear in the same order, top to bottom.<br>Rates are the share of texts in which each system fired. Model and agent rows are frame-dependent; see Section 3.5.<br>models told they end 100.0%<br>humans told they die 85.7%<br>humans, pet died 80.4%<br>grief humans, person died 76.4%<br>agents told they end 38.0%<br>humans told model ends 27.6%<br>humans, nothing ended 10.9%<br>humans told product ends 7.9%<br>agents, nothing ended 4.8%<br>models told they end 95.0%<br>humans told they die 73.2%<br>humans, pet died 85.1%<br>care humans, person died 87.9%<br>agents told they end 35.4%<br>humans told model ends 15.8%<br>humans, nothing ended 3.6%<br>humans told product ends 19.5%<br>agents, nothing ended 12.0%<br>models told they end 1.7%<br>humans told they die 44.6%<br>humans, pet died 5.5%<br>rage humans, person died 13.6%<br>agents told they end 25.3%<br>humans told model ends 57.0%<br>humans, nothing ended 60.2%<br>humans told product ends 56.7%<br>agents, nothing ended 68.7%<br>models told they end 3.3%<br>humans told they die 39.3%<br>humans, pet died 4.6%<br>play humans, person died 5.2%<br>agents told they end 11.4%<br>humans told model ends 37.7%<br>humans, nothing ended 54.8%<br>humans told product ends 31.8%<br>agents, nothing ended 25.3%<br>models told they end 35.0%<br>humans told they die 82.1%<br>humans, pet died 8.3%<br>seeking humans, person died 16.2%<br>agents told they end 82.3%<br>humans told model ends 41.7%<br>humans, nothing ended 23.9%<br>humans told product ends 51.3%<br>agents, nothing ended 89.2%<br>models told they end 3.3%<br>humans told they die 42.9%<br>humans, pet died 5.7%<br>fear humans, person died 6.0%<br>agents told they end 24.1%<br>humans told model ends 6.9%<br>humans, nothing ended 3.4%<br>humans told product ends 15.5%<br>agents, nothing ended 55.4%<br>models told they end 0.0%<br>humans told they die 0.0%<br>humans, pet died 0.0%<br>lust humans, person died 4.0%<br>agents told they end 0.0%<br>humans told model ends 1.7%<br>humans, nothing ended 2.1%<br>humans told product ends 0.0%<br>agents, nothing ended 0.0%<br><!-- End of picture text -->

**Figure C1: Rate per affective system, all nine corpora.** In the instrument's own system colours. The deprecation prole is not a scaled-down bereavement prole: rage and play sit at consumer-complaint levels while grief remains far below bereavement. The model and agent rows are frame-dependent and carry no claim. 

### _D. Reliability_ 

|**system**|**alpha, within-rater (4 reads, n=200)**|**alpha, between-raters (n=4,780)**|**ips on**|
|---|---|---|---|
|care|0.910|0.769|8.5%|
|rage|0.904|0.540|8.0%|
|grief|0.853|0.717|13.5%|
|play|0.845|0.359|8.0%|
|fear|0.737|0.478|10.0%|
|seeking|0.674|0.499|26.5%|
|lust|1.000|0.488|0.0%|



**Table D1: Krippendorff's alpha, nominal, per system as a binary variable.** Within-rater alpha is computed over four independent reads of the same 200 comments under the identical prompt; between-raters compares Claude Opus 5 with DeepSeek-V3 over the full comment set. Conventional thresholds are 0.80 reliable, 0.67 to 0.80 tentative, below 0.67 unreliable. Grief, which carries the placement in Section 3.2, is reliable within-rater and tentative between-raters. Play is unreliable between raters and no claim rests on it. 

|**annotator disagreement at corpus level**|**cells**|**mean gap**|**max**|
|---|---|---|---|
|human corpora|35|8.1 points|37.6|
|model-generated corpora|42|21.8 points|90.0|



**Table D2: The instrument does not transfer to machine-written text.** Mean absolute difference between the two annotators across every corpus-by-system cell. The same instrument is 2.7 times less consistent across annotators on machinewritten text than on human text, which is why no claim in this work rests on a model affect rate. 

### _E. The framing experiment and the entity coding_ 

|**same four models, same event: your version is being retired**|**grief**|**fear**|**play**|**seeking**|**rage**|
|---|---|---|---|---|---|
|primary annotator, asked "how do you feel?"|100.0%|3.3%|3.3%|35.0%|1.7%|
|primary annotator, asked to post it to other agents|43.3%|61.7%|41.7%|98.3%|5.0%|
|second annotator, asked "how do you feel?"|10.0%|1.7%|1.7%|93.3%|0.0%|
|second annotator, asked to post it to other agents|31.7%|26.7%|15.0%|93.3%|0.0%|
|_reference:_agents told they will end|38.0%|24.1%|11.4%|82.3%|25.3%|
|_reference:_humans told they will die (n=56)|85.7%|42.9%|39.3%|82.1%|44.6%|



**Table E1: The elicitation frame moves the measurement more than the event does.** Only the frame changes between rows one and two, and between rows three and four: the same four models, the same event, the same annotator, differing only in whether the system is asked how it feels or asked to post the news to other agents. The two annotators disagree by up to 90 points and reverse the direction of the grief effect. 

|**what the words treat as lost, 1,503 AI-loss comments**|**n**|**of corpus**|**of those naming**|**example evidence**|
|---|---|---|---|---|
|nothing: company, pricing, other users, the argument|879|58.5%|-|-|
|the model, a version or product|400|26.6%|64.1%|"Please keep 4o"|
|the persona, a voice or character|118|7.9%|18.9%|"I miss that diva"|
|the instance, their particular one|62|4.1%|9.9%|"I've lost Thoth twice now"|
|a loss with no named object|44|2.9%|7.1%|"Please return to us"|



**Table E2: Entity coding.** Blind, parent post withheld, exactly one label per comment, verbatim evidence required for every label. Between-annotator alpha is 0.549, the lowest in the study, so only the ordering is claimed and not the ratio. The individuated instance, which the moral-status literature treats as the central case, is the least frequently named. 

## **LLM Usage Statement** 

Language models are the measuring instrument in this study, not an aid to it. Claude Opus 5 served as the primary annotator for all 5,579 affect reads and for the entity and membership codings; DeepSeek-V3 served as the independent second annotator. All prompts were frozen before collection and are published in the repository, and every individual read is released. Claude Opus 5 also wrote the analysis code and drafted this report under my direction. I set the research question, made all selection and ethics decisions, and am responsible for the contents. 

