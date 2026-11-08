# **Markov Chain Lock Watermarking: Provably Secure Authentication for LLM Outputs**<sup>1</sup> 

Chengheng Li Chen Kyuhee Kim _AI Safety Barcelona & EPFL MATS & EPFL_ `chengheng.lichen@epfl.ch kyuhee.kim@epfl.ch` 

With 

**Apart Research** 

#### **Abstract** 

We present Markov Chain Lock (MCL) watermarking, a cryptographically secure framework for authenticating LLM outputs. MCL constrains token generation to follow a secret Markov chain over SHA-256 vocabulary partitions. Using doubly stochastic transition matrices, we prove four theoretical guarantees: (1) exponentially decaying false positive rates via Hoeffding bounds, (2) graceful degradation under adversarial modification with closed-form expected scores, (3) informationtheoretic security without key access, and (4) bounded quality loss via KL divergence. Experiments on 173 Wikipedia prompts using Llama-3.2-3B demonstrate that the optimal 7-state soft cycle configuration achieves 100% detection, 0% FPR, and perplexity 4.20. Robustness testing confirms detection above 96% even with 30% word replacement. The framework enables _O_ ( _n_ ) model-free detection, addressing EU AI Act Article 50 requirements. Code available at `https://github.com/ChenghengLi/MCLW` . 

## **1. Introduction** 

The EU AI Act Article 50 [1] mandates machine-readable marking of AI-generated content, with enforcement beginning August 2026. Current approaches partition into passive detection [2, 3] and active watermarking [4]. Passive methods suffer high false positive rates and paraphrasing vulnerability [5]; active schemes degrade under token substitution and require probabilistic sampling incompatible with greedy decoding. 

We introduce **Markov Chain Lock (MCL) watermarking** , constraining token generation to follow a secret finite-state Markov chain over cryptographic vocabulary partitions. Using doubly stochastic transition matrices (e.g., clockwork: _i →_ ( _i_ + 1) mod _S_ , or soft cycle: _i →{i_ + 1 _, i_ + 2 _}_ ), we create detectable state patterns verifiable only with the secret key (Figure 1). **Contributions.** (1) Complete mathematical framework with cryptographic state assignment and clockwork topology; (2) four theorems establishing exponential false positive decay (Theorem 4.1), robustness bounds (Theorem 4.3), information-theoretic security (Theorem 4.4), and quality preservation (Theorem 4.5); (3) empirical validation on 173 Wikipedia concepts across 28 configurations; (4) practical algorithms for _O_ ( _N_ ( _V_ + _T_ LM)) embedding and _O_ ( _n_ ) model-free detection. 

> 1Research conducted at the Technical AI Governance Challenge, 2026. More information: `https:// apartresearch.com/sprints/the-technical-ai-governance-challenge-2026-01-30-to-2026-02-01` 

1 



**Figure 1:** MCL watermarking overview. Each token is assigned to a state partition _Vs_ via SHA-256 hashing. Generation follows a clockwork Markov chain (0 _→_ 1 _→_ 2 _→_ 3 _→_ 0), constraining each token to the next state’s partition. Detection verifies the hidden state sequence. 

## **2. Related Work** 

Passive detection methods analyze statistical properties of generated text: DetectGPT [2] examines log-probability curvature, while GPTZero [3] combines perplexity and burstiness metrics. However, these approaches suffer high false positive rates on technical writing and fail under paraphrasing [5, 6]. Active watermarking embeds verifiable signals during generation. Kirchenbauer et al. [4] partition vocabulary into green/red lists via keyed hashing, but this degrades under paraphrasing and requires temperature sampling. Aaronson [7] proposes semantic-level embedding requiring expensive model queries, while Christ et al. [8] establish fundamental quality-security tradeoffs. 

Chen et al. [9] propose Pattern-Mark, a Markov-chain-based watermarking framework for orderagnostic language models using probabilistic transitions and pattern-frequency detection. MCL targets autoregressive LLMs with deterministic transitions, enabling greedy decoding compatibility and model-free O(n) detection via transition validity verification. 

MCL advances prior work through: (1) deterministic embedding compatible with greedy decoding; (2) model-free _O_ ( _n_ ) detection; (3) provable exponentially small FPR via Hoeffding bounds; and (4) explicit quality-security parameterization through tunable overlap _ρ_ . 

## **3. Methods** 

### **3.1 Cryptographic State Assignment** 

Let _V_ denote the vocabulary with size _V_ = _|V|_ , and let _H_ : _{_ 0 _,_ 1 _}_<sup>_∗_</sup> _→{_ 0 _,_ 1 _}_<sup>256</sup> denote SHA-256, a cryptographic hash function satisfying uniformity, one-wayness, and collision resistance. 

2 

**Definition 3.1** (Cryptographic State Assignment) **.** Given secret key _k ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> and number of states _S ∈_ N, the state assignment function is _σk_ : _V →S_ defined as _σk_ ( _t_ ) = _H_ ( _k∥t_ ) mod _S_ , where _∥_ denotes concatenation and _S_ = _{_ 0 _,_ 1 _, . . . , S −_ 1 _}_ . This induces vocabulary partition _V_ =<sup>�</sup><sup>_S_</sup> _s_ =0<sup>_−_1</sup><sup>_Vs_</sup> where _Vs_ = _{t ∈V_ : _σk_ ( _t_ ) = _s}_ . 

**Lemma 3.2** (Partition Uniformity) **.** _Under the random oracle model for H, for any state s ∈S:_ E[ _|Vs|_ ] = _V/S and Var_ [ _|Vs|_ ] = _V_ ( _S −_ 1) _/S_<sup>2</sup> _. Proof._ For each token _t_ , the indicator ⊮[ _σk_ ( _t_ ) = _s_ ] is Bernoulli(1 _/S_ ) by hash uniformity. Thus _|Vs|_ =<sup>�</sup> _t∈V_<sup>⊮[</sup><sup>_σk_(</sup><sup>_t_) =</sup><sup>_s_]hasmean</sup><sup>_V/S_andvariance</sup><sup>_V·_(1</sup><sup>_/S_)</sup><sup>_·_(1</sup><sup>_−_1</sup><sup>_/S_) =</sup><sup>_V_(</sup><sup>_S −_1)</sup><sup>_/S_2.</sup> 

### **3.2 Transition Matrix Topologies** 

We consider transition matrices that are _doubly stochastic_ , ensuring uniform stationary distribution, a property essential for the theoretical guarantees in Section 4. 

**Definition 3.3** (Doubly Stochastic Transition Matrix) **.** A matrix **T** _∈_ R<sup>_S×S_</sup> is **doubly stochastic** if<sup>�</sup> _j_<sup>_Tij_= �</sup> _i_<sup>_Tij_= 1 for all</sup><sup>_i, j_.For irreducible, aperiodic chains, the Ergodic Theorem guarantees</sup> convergence to the unique stationary distribution _π_<sup>_∗_</sup> = (1 _/S, . . . ,_ 1 _/S_ ), yielding detection baseline E[ _ϕ_ ] = _k/S_ where _k_ is the number of valid successors per state. 

We present two topologies satisfying this definition. 

**Example 3.4** (Clockwork Matrix) **.** The clockwork matrix **T**<sup>clock</sup> _ij_ = ⊮[ _j ≡ i_ +1 (mod _S_ )] is a cyclic permutation with _k_ = 1 successor per state. For _S_ = 4: 



<!-- Start of picture text -->
00 10 01 00<br>T clock = 0 0 0 1 ⇒ p random = S 1<br>1 0 0 0<br><!-- End of picture text -->

**Example 3.5** (Soft Cycle Matrix) **.** The soft cycle matrix allows transitions to two successors ( _k_ = 2): 



<!-- Start of picture text -->
2 / 3 j ≡ i +1 (mod S )<br>T soft ij = 10 / 3 j otherwise ≡ i +2 (mod S ) ⇒ p random = S 2<br><!-- End of picture text -->

For _S_ = 4: 



<!-- Start of picture text -->
T soft =  00 2 / 03 12 // 33 10 / 3<br>1 / 3 0 0 2 / 3<br>2 / 3 1 / 3 0 0 <br><!-- End of picture text -->

This doubles available vocabulary at each step while halving detection power relative to clockwork. _Note:_ For soft cycle with _S_ = 7: _p_ random = 2 _/_ 7 _≈_ 0 _._ 29. 

### **3.3 Watermark Embedding and Detection** 

**Definition 3.6** (MCL Constrained Generation) **.** Given current state _s ∈S_ , the MCL-constrained distribution over next tokens is: 



<!-- Start of picture text -->
PM ( t ) /Zs if t ∈V ( s +1) mod  S<br>P MCL( t | s ) =<br>0 otherwise<br>�<br><!-- End of picture text -->

where _Zs_ =<sup>�</sup> _t_<sup>_′_</sup> _∈V_ ( _s_ +1) mod _S_<sup>_PM_(</sup><sup>_t′_)isthenormalizationconstant.</sup> 

3 

**Algorithm 1** MCL Watermark Embedding 

**Require:** Prompt _p_ , secret key _k_ , states _S_ , max tokens _N_ **Ensure:** Watermarked text 1: **tokens** _←_ Tokenize( _p_ ) 2: _s ← σk_ ( **tokens** [last]) _▷_ Initial state from prompt 3: **for** _i_ = 1 to _N_ **do** 4: **_ℓ_** _←M._ Forward( **tokens** ) _▷_ Get logits 5: _s_ next _←_ ( _s_ + 1) mod _S ▷_ Clockwork: next state 6: **for** each token _t ∈V_ **do** 7: **if** _σk_ ( _t_ ) _̸_ = _s_ next **then** 8: **_ℓ_** [ _t_ ] _←−∞ ▷_ Mask disallowed tokens 9: **end if** 10: **end for** 11: _t_ next _←_ arg max( **_ℓ_** ) _▷_ Greedy selection 12: **tokens** _._ Append( _t_ next); _s ← s_ next 13: **if** _t_ next = `EOS` **then** : **break** 14: **end if** 15: **end for** 

16: **return** Decode( **tokens** [len( _p_ ) :]) 

**Definition 3.7** (Fingerprint Score) **.** For token sequence **t** = ( _t_ 1 _, . . . , tn_ ), the fingerprint score is: 



<!-- Start of picture text -->
n− 1<br>1<br>ϕ ( t ) = n − 1 � T clock σk ( ti ) ,σk ( ti +1)<br>i =1<br><!-- End of picture text -->

Text is classified as watermarked if _ϕ_ ( **t** ) _> τ_ for detection threshold _τ ∈_ (1 _/S,_ 1). 

### **3.4 Soft Partitions** 

Hard partitions restrict each token to exactly one state, which may limit vocabulary choices and degrade generation quality. Soft partitions allow controlled overlap between states. 

**Definition 3.8** (Soft State Membership) **.** Given overlap ratio _ρ ∈_ [0 _,_ 1], the soft membership assigns each token to multiple states: Σ _k_ ( _t_ ) = _{s ∈S_ : _Hs_ ( _k∥t_ ) _< θρ}_ where _θρ_ = (1 _/S_ + _ρ_ (1 _−_ 1 _/S_ )) _·_ 2<sup>256</sup> . 

The expected tokens per state is _V_ (1 _/S_ + _ρ_ ( _S −_ 1) _/S_ ). For _S_ = 7: _ρ_ = 0 yields 14.3% vocabulary per state, while _ρ_ = 0 _._ 15 yields approximately 27%. Higher overlap improves quality but weakens detection, as demonstrated in our experiments. 

### **3.5 Algorithms** 

Algorithm 1 has complexity _O_ ( _N_ ( _V_ + _T_ LM)) where _T_ LM is the LLM forward pass time. Algorithm 2 requires only _O_ ( _n_ ) hash operations with **no model access** , enabling lightweight third-party verification. 

4 

**Algorithm 2** MCL Watermark Detection 

**Require:** Text _x_ , secret key _k_ , states _S_ , threshold _τ_ **Ensure:** ( _is_ _~~w~~ atermarked, score, p_ _~~v~~ alue_ ) 1: **tokens** _←_ Tokenize( _x_ ); _n ←|_ **tokens** _|_ ; _c ←_ 0 2: **for** _i_ = 1 to _n −_ 1 **do** 3: _si ← σk_ ( **tokens** [ _i_ ]); _si_ +1 _← σk_ ( **tokens** [ _i_ + 1]) 4: **if** _si_ +1 _≡ si_ + 1 (mod _S_ ) **then** : _c ← c_ + 1 5: **end if** _▷_ Valid clockwork transition 6: **end for** 7: _score ← c/_ ( _n −_ 1) 8: _z ←_ ( _score −_ 1 _/S_ ) _/_ ~~�~~ (1 _/S_ )(1 _−_ 1 _/S_ ) _/_ ( _n −_ 1) _▷_ Z-score 9: **return** ( _score > τ, score,_ 1 _−_ Φ( _z_ )) 

## **4. Theoretical Results** 

**Theorem 4.1** (Detection Bounds for Doubly Stochastic Chains) **.** _Let_ **T** _be an irreducible doubly stochastic transition matrix with k non-zero entries per row (average). Let_ **t**<sup>_w_</sup> _be a watermarked sequence of length n and_ **t**<sup>_r_</sup> _a random sequence. For threshold τ ∈_ ( _k/S,_ 1) _:_ 

_(i) Watermarked: ϕ_ ( **t**<sup>_w_</sup> ) = 1 _(all transitions valid by construction) (ii) Random baseline:_ E[ _ϕ_ ( **t**<sup>_r_</sup> )] = _k/S (uniform state distribution) (iii) False negative rate: FNR_ = 0 _(ϕ_ = 1 _> τ always) (iv) False positive rate: FPR ≤_ exp( _−_ 2( _n−_ 1)( _τ − k/S_ )<sup>2</sup> ) _(Hoeffding bound) Special cases: Clockwork (k_ =1 _): prandom_ = 1 _/S. Soft cycle (k_ =2 _): prandom_ = 2 _/S._ 

_Proof._ **(i)** Algorithm 1 enforces that each token’s state is a valid successor in **T** , so **T** _σk_ ( _ti_ ) _,σk_ ( _ti_ +1) _>_ 0 for all transitions, giving _ϕ_ ( **t**<sup>_w_</sup> ) = 1. **(ii)** For random text, each state _σk_ ( _t_ ) is uniformly distributed over _S_ by Lemma 3.2. Since **T** is doubly stochastic (Definition 3.3), the stationary distribution is uniform: _π_<sup>_∗_</sup> = (1 _/S, . . . ,_ 1 _/S_ ). With _k_ non-zero entries per row, _P_ (valid transition) = _k/S_ . **(iii)** Since _ϕ_ ( **t**<sup>_w_</sup> ) = 1 _> τ_ , FNR = 0. **(iv)** Let _Zi_ = **1** [ **T** _σk_ ( _ti_ ) _,σk_ ( _ti_ +1) _>_ 0] _∈{_ 0 _,_ 1 _}_ indicate valid transitions. For random text, _Zi_ are i.i.d. Bernoulli( _k/S_ ) by the doubly stochastic property. By Hoeffding’s inequality: 



<!-- Start of picture text -->
n− 1<br>P ( ϕ ( t r )  ≥ τ ) =  P � n − 1 1 � i =1 Zi ≥ τ � ≤ exp � − 2( n − 1) � τ − S k �2 �<br><!-- End of picture text -->

**Corollary 4.2** (Practical FPR Bounds) **.** _For soft cycle (k_ =2 _), S_ = 7 _, τ_ = 0 _._ 5 _: FPR ≤_ 1 _._ 1 _×_ 10<sup>_−_4</sup> _at n_ = 100 _tokens; FPR ≤_ 1 _._ 2 _×_ 10<sup>_−_8</sup> _at n_ = 200 _tokens._ 

**Theorem 4.3** (Adversarial Robustness) **.** _For a doubly stochastic chain with k valid successors per state, if an adversary modifies fraction δ of tokens uniformly at random:_ 



<!-- Start of picture text -->
E[ ϕ ( t mod )] = (1  − δ ) 2 + k · δ (2  − δ )<br>S<br><!-- End of picture text -->

_Proof._ Consider consecutive pair ( _ti, ti_ +1) with modification indicator _Mi ∼_ Bernoulli( _δ_ ). Four cases: (1) neither modified (prob. (1 _−δ_ )<sup>2</sup> ): contributes 1; (2) only _ti_ +1 modified (prob. (1 _−δ_ ) _δ_ ): 

5 

contributes _k/S_ ; (3) only _ti_ modified (prob. _δ_ (1 _−δ_ )): contributes _k/S_ ; (4) both modified (prob. _δ_<sup>2</sup> ): contributes _k/S_ . Summing: (1 _−δ_ )<sup>2</sup> + [2 _δ_ (1 _−δ_ ) + _δ_<sup>2</sup> ] _· k/S_ = (1 _−δ_ )<sup>2</sup> + _δ_ (2 _−δ_ ) _· k/S_ . 

_Example:_ For soft cycle ( _k_ =2), _S_ = 7, _τ_ = 0 _._ 5: at _δ_ = 0 _._ 3, E[ _ϕ_ ] = 0 _._ 49 + 0 _._ 51 _·_ 2 _/_ 7 _≈_ 0 _._ 64 _>_ 0 _._ 5 (detectable); at _δ_ = 0 _._ 5, E[ _ϕ_ ] = 0 _._ 25 + 0 _._ 75 _·_ 2 _/_ 7 _≈_ 0 _._ 46 _<_ 0 _._ 5 (undetectable). Experimental validation is presented in Section 6.3. 

**Theorem 4.4** (Information-Theoretic Security) **.** _Under the random oracle model, without secret key k, any polynomial-time adversary has negligible advantage:_ 



<!-- Start of picture text -->
AdvA =  |P [ A ( t w ) = 1]  − P [ A ( t r ) = 1] | ≤ negl (256)<br><!-- End of picture text -->

_Proof._ The state assignment _σk_ ( _t_ ) = _H_ ( _k∥t_ ) mod _S_ is a pseudorandom function under the random oracle model. Without _k_ , the adversary observes only the token sequence **t** , not the state sequence ( _s_ 1 _, . . . , sn_ ). Watermarked text has clockwork states; random text has i.i.d. uniform states. Distinguishing these from tokens alone requires inverting _H_ , which has probability _≤_ 2<sup>_−_256</sup> . 

**Theorem 4.5** (Quality Bound) **.** _The KL divergence between MCL-constrained and unconstrained distributions satisfies:_ 



<!-- Start of picture text -->
DKL ( PMCL∥PM ) = log(1 /Zs )  ≤ log  S<br><!-- End of picture text -->

_where Zs_ = _PM_ ( _V_ ( _s_ +1) mod _S_ ) _is the probability mass of the target partition._ 

_Proof._ MCL distribution: _P_ MCL( _t | s_ ) = _PM_ ( _t_ ) _/Zs_ for _t ∈V_ ( _s_ +1) mod _S_ , else 0. KL divergence: 



<!-- Start of picture text -->
PM ( t )<br>D KL = � log 1 = log(1 /Zs )<br>Zs Zs<br>t∈V ( s +1) mod S<br><!-- End of picture text -->

By Lemma 3.2, _|V_ ( _s_ +1) mod _S| ≈ V/S_ , so _Zs ≥_ 1 _/S_ , giving _D_ KL _≤_ log _S_ . 

_Implication:_ Quality degradation is logarithmic in states. For _S_ = 7: _D_ KL _≤_ log 7 _≈_ 1 _._ 95 nats. 

## **5. Experimental Design** 

To empirically validate our theoretical framework, we conduct comprehensive experiments across diverse textual domains and watermarking configurations. This section details the dataset construction, text generation methodology, and evaluation criteria. 

### **5.1 Dataset Construction** 

We construct an evaluation corpus comprising 173 concepts selected from the most frequently accessed Wikipedia articles, ensuring both topical diversity and practical relevance. The corpus systematically spans six semantic categories: _notable figures_ (e.g., Albert Einstein, William Shakespeare, Elon Musk), _historical events_ (e.g., World War II, French Revolution, the Renaissance), _scientific phenomena_ (e.g., quantum mechanics, DNA replication, black holes), _geographical entities_ (e.g., Mount Everest, Amazon River, Antarctica), _technological concepts_ (e.g., artificial intelligence, cryptocurrency, neural networks), and _cultural references_ (e.g., Star Wars, Harry Potter, Game of Thrones). 

For each concept _c_ , we construct a standardized prompt _pc_ of the form: _“Explain [concept] in a comprehensive way.”_ This formulation elicits informative, multi-sentence responses suitable for watermark embedding and detection analysis. 

6 

### **5.2 Text Generation Protocol** 

We generate paired samples for each concept to enable controlled comparison between watermarked and baseline conditions: 

- **Watermarked generation.** Text is produced using Algorithm 1 with **soft cycle** transition enforcement (Example 3.5). At each decoding step, the model’s output distribution is masked to permit only tokens belonging to valid successor partitions _V_ ( _s_ +1) mod _S_ or _V_ ( _s_ +2) mod _S_ , followed by sampling from the masked distribution. This procedure guarantees _ϕ_ ( **t** ) _≈_ 1 _._ 0 for all generated sequences. 

- **Baseline generation.** Non-watermarked text is produced using standard nucleus sampling with temperature _T_ = 0 _._ 7 and cumulative probability threshold _p_ = 0 _._ 9, without any vocabulary constraints. These samples establish the null distribution for false positive rate estimation. 

All experiments employ Llama-3.2-3B-Instruct as the base language model, with a maximum generation length of 200 tokens. We systematically evaluate 7 _×_ 4 = 28 configurations spanning state counts _S ∈{_ 2 _,_ 4 _,_ 5 _,_ 7 _,_ 9 _,_ 11 _,_ 15 _}_ and overlap ratios _ρ ∈{_ 0% _,_ 5% _,_ 10% _,_ 15% _}_ . Reproducibility is ensured through fixed random seed (42) and cryptographic key ( `curated` ~~`w`~~ `iki` ~~`d`~~ `ataset` ~~`2`~~ `024` ). 

### **5.3 Evaluation Metrics** 

We quantify watermarking performance along four complementary dimensions: 

- **Fingerprint Score** _ϕ_ ( **t** ) _∈_ [0 _,_ 1]: The proportion of consecutive token pairs exhibiting valid transitions according to the transition matrix (Definition 3.7). For watermarked text using soft cycle, _ϕ ≈_ 1 _._ 0 by construction; for random text, E[ _ϕ_ ] = 2 _/S_ (Theorem 4.1). 

- **True Positive Rate (TPR)** : The fraction of watermarked samples correctly identified, computed as TPR = _|{_ **t**<sup>_w_</sup> : _ϕ_ ( **t**<sup>_w_</sup> ) _> τ }|/|{_ **t**<sup>_w_</sup> _}|_ with threshold _τ_ = 0 _._ 5. 

- **False Positive Rate (FPR)** : The fraction of non-watermarked samples erroneously classified as watermarked, representing the Type I error rate critical for deployment reliability. 

- <sup><u>1</u></sup> 

- • **Perplexity (PPL)** : The exponential of cross-entropy loss, PPL = exp � _n_ � _ni_ =1<sup>log</sup><sup>_PM_(</sup><sup>_ti|t<i_)</sup> �, measuring linguistic fluency. Lower values indicate higher generation quality. 

### **5.4 Robustness Evaluation Protocol** 

To evaluate robustness against adversarial attacks, we perform controlled word replacement experiments on the optimal configuration ( _S_ = 7, soft cycle, _ρ_ = 0%). For each modification rate _δ ∈{_ 10% _,_ 20% _,_ 30% _,_ 40% _,_ 50% _,_ 60% _}_ , we randomly select _δ_ fraction of word positions in each watermarked text and replace them with the word “masked”. The modified text is re-tokenized using Llama-3.2’s tokenizer, and detection scores are computed using Algorithm 2. Table 2 reports the observed mean fingerprint score _ϕ_ across 173 samples, the theoretical expectation E[ _ϕ_ ] from Theorem 4.3, and the detection rate (fraction with _ϕ > τ_ = 0 _._ 5). 

7 

## **6. Experimental Results** 

### **6.1 Main Results** 

Table 1 presents the top-performing configurations. All 0% overlap configurations with _S ≥_ 5 achieve perfect detection (100% TPR, 0% FPR), confirming Theorem 4.1. The optimal _S_ = 7 configuration balances detection with minimal perplexity (4.20). Complete results for all 28 configurations are provided in Appendix A. 

**Table 1:** Top configurations (0% overlap): Score gap = WM avg _−_ Non-WM avg 

|**States**|**WM Avg**|**Non-WM Avg**|**Gap**|**Det%**|**FPR%**|**PPL**|
|---|---|---|---|---|---|---|
|5|0.991|0.402|0.59|100|0|4.98|
|**7**|**0.991**|**0.290**|**0.70**|**100**|**0**|**4.20**|
|9|0.984|0.221|0.76|100|0|5.37|
|11|0.988|0.197|0.79|100|0|4.61|
|15|0.988|0.138|0.85|100|0|5.11|



### **6.2 Key Observations** 

Our experiments reveal four critical findings. **First** , configurations with _S ≥_ 5 and _ρ_ = 0% achieve _perfect separability_ : the minimum watermarked score exceeds the maximum non-watermarked score, enabling simultaneous 0% FPR and 0% FNR at threshold _τ_ = 0 _._ 5, directly confirming Theorem 4.1. **Second** , the optimal configuration is _S_ = 7 with _ρ_ = 0%, achieving 100% TPR, 0% FPR, lowest perplexity (4.20), and strong separation (gap = 0.70), the Pareto-optimal choice consistent with Theorem 4.5. **Third** , low state counts fail: _S_ = 2 yields 100% FPR (all sequences trivially alternate), while _S_ = 4 suffers 33.5% FPR due to insufficient separation. **Fourth** , overlap catastrophically degrades detection: for _S_ = 7, TPR drops from 100% ( _ρ_ = 0%) to 92% ( _ρ_ = 5%), 35% ( _ρ_ = 10%), and 13% ( _ρ_ = 15%). 



**Figure 2:** Detection metrics (0% overlap, soft cycle). **Left:** Watermarked text achieves _ϕ ≈_ 1 _._ 0; non-watermarked follows 2 _/S_ baseline. **Right:** FPR by state count; _S ≤_ 4 yields unacceptable false positives. 

8 



**Figure 3:** Quality-detection trade-off (bubble size _∝_ score gap). _S_ = 7 at 0% overlap minimizes PPL while achieving 100% detection. 

### **6.3 Robustness Analysis** 

Table 2 presents the robustness validation results following the protocol in Section 5.4. The baseline (unmodified text) achieves _ϕ_ = 0 _._ 991 with 100% detection as shown in Table 1. 

**Table 2:** Robustness to word replacement (soft cycle, _S_ = 7, _n_ = 173). 

|_δ_|Observed _ϕ_|Std Dev|E[_ϕ_] (Thm. 4.3)|Detection Rate|
|---|---|---|---|---|
|0%|0.991|0.014|1.000|100%|
|10%|0.839|0.068|0.864|99.4%|
|20%|0.738|0.072|0.743|99.4%|
|30%|0.642|0.073|0.636|96.5%|
|40%|0.543|0.080|0.543|76.3%|
|50%|0.455|0.084|0.464|17.9%|
|60%|0.365|0.084|0.400|5.8%|



Observed scores match Theorem 4.3 within 1 to 6%. Detection remains above 96% for _δ ≤_ 30%. The critical threshold is _δ ≈_ 45% where E[ _ϕ_ ] = _τ_ = 0 _._ 5. Beyond this point, an adversary must corrupt nearly half the text to evade detection, which would likely render the content incoherent. 

## **7. Discussion** 

MCL watermarking addresses EU AI Act Article 50 [1] requirements for machine-readable AI content marking. The model-free detection (Algorithm 2) enables third-party auditing without LLM access, supporting transparency frameworks [10], while provable guarantees (Theorems 4.1 to 4.5) provide legally defensible authentication with quantifiable error rates. 

**Limitations.** (1) Detection requires the same tokenizer used during generation; (2) at least 5 states are needed for reliable detection ( _S_ = 2 is unusable); (3) overlap _ρ ≥_ 10% severely degrades detection; (4) perplexity increases with states, though _S_ = 7 achieves reasonable PPL = 4.20. 

9 

**Future Work.** A promising direction is _sparse watermarking_ : introducing a “full vocabulary” state that allows unrestricted token selection, watermarking only every _N_ -th token (e.g., _N_ = 10). This preserves generation quality while maintaining theoretical guarantees, since any doubly stochastic transition matrix ensures uniform stationary distribution. Other directions include adaptive overlap selection based on token probability mass, C2PA metadata integration for end-to-end provenance, robustness against learned adversarial attacks, and multi-model coordination for heterogeneous deployments. Preliminary experiments on Mistral-7B and GPT-2-XL (Appendix E) confirm consistent behavior across model architectures. We hypothesize that larger vocabulary sizes reduce perplexity under partitioning, as each partition contains more candidate tokens. 

## **8. Conclusion** 

We established complete mathematical foundations for Markov Chain Lock watermarking using doubly stochastic transition matrices over SHA-256-based vocabulary partitions. Our theoretical results generalize to any irreducible doubly stochastic chain with _k_ valid successors per state, providing: (1) exponentially decaying false positive rates bounded by Hoeffding’s inequality (Theorem 4.1), (2) quantified robustness under adversarial token modification with formula E[ _ϕ_ ] = (1 _− δ_ )<sup>2</sup> + _kδ_ (2 _− δ_ ) _/S_ (Theorem 4.3), (3) information-theoretic security under the random oracle model (Theorem 4.4), and (4) logarithmic quality degradation in state count (Theorem 4.5). Experiments on 173 Wikipedia concepts across 28 configurations demonstrate that 7-state soft cycle ( _k_ = 2) with 0% overlap is optimal, achieving 100% detection, 0% FPR, and perplexity 4.20. Robustness validation confirms detection remains above 96% even with 30% word modification. The framework provides _O_ ( _n_ ) model-free detection, directly addressing EU AI Act Article 50 requirements. 

## **LLM Usage Statement** 

Claude (Anthropic) assisted with LaTeX formatting. All proofs, algorithms, and experiments independently developed and verified by the authors. 

## **Code and Data** 

**Repository** : `https://github.com/ChenghengLi/MCLW` . **Model** : Llama-3.2-3B-Instruct. **Dataset** : 173 curated Wikipedia concepts, seed 42, secret key `curated` ~~`w`~~ `iki` ~~`d`~~ `ataset` ~~`2`~~ `024` . 

## **Author Contributions** 

**Chengheng Li** : Theoretical framework design, mathematical proofs, algorithm implementation, experiments, manuscript writing. **Kyuhee Kim** : Experimental design, theoretical review, AI governance analysis. 

## **Acknowledgments** 

We thank Apart Research and the Technical AI Governance Challenge organizers for hosting this event. 

10 

## **References** 

- [1] European Parliament and Council. EU AI Act (Regulation 2024/1689), 2024. URL `https: //eur-lex.europa.eu/eli/reg/2024/1689` . Official Journal of the European Union. 

- [2] Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, and Chelsea Finn. DetectGPT: Zero-shot machine-generated text detection using probability curvature. In _International Conference on Machine Learning (ICML)_ , pages 24950–24962, 2023. 

- [3] Edward Tian. GPTZero: An AI plagiarism detection tool, 2023. URL `https://gptzero.me` . Software tool. 

- [4] John Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, and Tom Goldstein. A watermark for large language models. In _International Conference on Machine Learning (ICML)_ , pages 17061–17084, 2023. 

- [5] Kalpesh Krishna, Yixiao Song, Marzena Karpinska, John Wieting, and Mohit Iyyer. Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense. In _Advances in Neural Information Processing Systems (NeurIPS)_ , pages 13287–13300, 2023. 

- [6] Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, and Soheil Feizi. Can AI-generated text be reliably detected? _arXiv preprint arXiv:2303.11156_ , 2023. 

- [7] Scott Aaronson. Watermarking GPT outputs. 2023. URL `https://scottaaronson.blog/ ?p=6823` . Blog post. 

- [8] Miranda Christ, Sam Gunn, and Or Zamir. Undetectable watermarks for language models, 2023. URL `https://arxiv.org/abs/2306.09194` . 

- [9] Ruibo Chen, Yihan Wu, Yanshuo Chen, Chenxi Liu, Junfeng Guo, and Heng Huang. A watermark for order-agnostic language models, 2024. URL `https://arxiv.org/abs/2410. 13805` . 

- [10] OECD. Hiroshima AI process international code of conduct for organizations developing advanced AI systems, 2024. URL `https://oecd.ai/en/g7-reporting-framework` . G7 Hiroshima AI Process. 

11 

## **A. Complete Experimental Results** 

Table 3 presents complete results for all 28 configurations. Verdict classification: **Excellent** (gap _>_ 0 _._ 5, 100% detection, 0% FPR); **Good** (gap _>_ 0 _._ 3, _>_ 90% detection); **Marginal** (gap _>_ 0 _._ 15); **Poor** (gap _<_ 0 _._ 15 or high FPR). 

**Table 3:** Complete results for all 28 configurations 

|**Config**|_S_|_ρ_|**Non-WM**|**WM**|**Gap**|**Det%**|**FPR%**|**PPL**|
|---|---|---|---|---|---|---|---|---|
|states2<br>~~o~~verlap0pct|2|0%|1.000|1.000|0.00|100|100|1.29|
|states2<br>~~o~~verlap5pct|2|5%|1.000|1.000|0.00|100|100|1.29|
|states2<br>~~o~~verlap10pct|2|10%|1.000|1.000|0.00|100|100|1.29|
|states2<br>~~o~~verlap15pct|2|15%|1.000|1.000|0.00|100|100|1.29|
|states4<br>~~o~~verlap0pct|4|0%|0.489|0.989|0.50|100|33.5|4.89|
|states4<br>~~o~~verlap5pct|4|5%|0.489|0.842|0.35|99.4|33.5|4.48|
|states4<br>~~o~~verlap10pct|4|10%|0.489|0.696|0.21|98.8|33.5|4.00|
|states4<br>~~o~~verlap15pct|4|15%|0.489|0.626|0.14|96.0|33.5|3.84|
|states5<br>~~o~~verlap0pct|5|0%|0.402|0.991|0.59|100|0|4.98|
|states5<br>~~o~~verlap5pct|5|5%|0.402|0.726|0.32|96.5|0|4.74|
|states5<br>~~o~~verlap10pct|5|10%|0.402|0.639|0.24|95.4|0|4.86|
|states5<br>~~o~~verlap15pct|5|15%|0.402|0.542|0.14|70.5|0|4.22|
|states7<br>~~o~~verlap0pct|7|0%|0.290|0.991|0.70|100|0|4.20|
|states7<br>~~o~~verlap5pct|7|5%|0.290|0.643|0.35|91.9|0|4.76|
|states7<br>~~o~~verlap10pct|7|10%|0.290|0.477|0.19|35.3|0|5.32|
|states7<br>~~o~~verlap15pct|7|15%|0.290|0.414|0.12|12.7|0|5.01|
|states9<br>~~o~~verlap0pct|9|0%|0.221|0.984|0.76|100|0|5.37|
|states9<br>~~o~~verlap5pct|9|5%|0.221|0.531|0.31|60.1|0|5.25|
|states9<br>~~o~~verlap10pct|9|10%|0.221|0.379|0.16|9.8|0|5.56|
|states9<br>~~o~~verlap15pct|9|15%|0.221|0.307|0.09|0.6|0|5.40|
|states11<br>~~o~~verlap0pct|11|0%|0.197|0.987|0.79|100|0|4.61|
|states11<br>~~o~~verlap5pct|11|5%|0.197|0.431|0.23|27.2|0|6.18|
|states11<br>~~o~~verlap10pct|11|10%|0.197|0.315|0.12|2.9|0|6.86|
|states11<br>~~o~~verlap15pct|11|15%|0.197|0.255|0.06|0.6|0|6.26|
|states15<br>~~o~~verlap0pct|15|0%|0.138|0.988|0.85|100|0|5.11|
|states15<br>~~o~~verlap5pct|15|5%|0.138|0.347|0.21|8.1|0|5.89|
|states15<br>~~o~~verlap10pct|15|10%|0.138|0.257|0.12|1.2|0|8.05|
|states15<br>~~o~~verlap15pct|15|15%|0.138|0.203|0.07|1.2|0|7.10|



## **B. Separability and Overlap Analysis** 

Table 4 demonstrates perfect separability: for _S ≥_ 5 with _ρ_ = 0%, the minimum watermarked score exceeds the maximum non-watermarked score, enabling zero-error detection. 

**Table 4:** Score range separability and overlap impact 

|_S_|**Sep**<br>**WM Min**|**arability (0% ov**<br>**Non-WM Max**|**erlap)**<br>**Gap**|**Sep?**|**Detec**<br>**0%**|**tion Ra**<br>**5%**|**te by O**<br>**10%**|**verlap**<br>**15%**|
|---|---|---|---|---|---|---|---|---|
|5|0.607|0.500|+0.11|Yes|100%|96.5%|95.4%|70.5%|
|7|0.707|0.400|+0.31|Yes|100%|91.9%|35.3%|12.7%|
|9|0.653|0.333|+0.32|Yes|100%|60.1%|9.8%|0.6%|
|11|0.720|0.313|+0.41|Yes|100%|27.2%|2.9%|0.6%|
|15|0.787|0.247|+0.54|Yes|100%|8.1%|1.2%|1.2%|



12 

## **C. Supplementary Visualizations** 

This section provides additional visualizations supporting the main experimental findings. 



**Figure 4:** Overlap impact on watermark performance. **Left:** Score gap heatmap across 28 configurations, gap decreases with higher overlap and lower states. **Right:** Detection rate degradation curves showing higher state counts are more sensitive to overlap. 



**Figure 5:** Theoretical properties validation. **Left:** Perfect separation for _S ≥_ 5, minimum WM score exceeds maximum non-WM score. **Right:** Observed vs theoretical baseline E[ _ϕ_ ] = 1 _/S_ , validating Theorem 4.1. 

## **D. Implementation Details** 

**Hash function** : SHA-256 via Python `hashlib` . **State assignment** : `hash(key, token` ~~`i`~~ `d)` mod _S_ . **Model** : Llama-3.2-3B-Instruct. **Generation** : greedy decoding ( _T_ = 0), max 200 tokens. **Reproducibility** : seed 42, key `curated` ~~`w`~~ `iki` ~~`d`~~ `ataset` ~~`2`~~ `024` . 

13 

## **E. Cross-Model Validation** 

To verify that MCL watermarking generalizes across model architectures and transition topologies, we conducted experiments on Mistral-7B-v0.3 and GPT-2-XL using identical protocols (173 Wikipedia prompts). We tested both soft cycle and clockwork transition matrices. 

**Table 5:** Mistral-7B-v0.3 results (173 samples). 

|_S_|_ρ_|Topology|Avg _ϕ_|Detection|PPL|
|---|---|---|---|---|---|
|2|0%|soft cycle|1.000|100%|1.35|
|2|0%|clockwork|0.992|100%|2.05|
|2|5%|soft cycle|1.000|100%|1.35|
|2|5%|clockwork|0.876|99.4%|1.98|
|2|10%|soft cycle|1.000|100%|1.35|
|2|15%|soft cycle|1.000|100%|1.35|
|4|0%|soft cycle|0.992|100%|1.85|
|4|5%|soft cycle|0.847|98.8%|1.93|
|4|10%|soft cycle|0.749|97.1%|2.01|
|4|15%|soft cycle|0.673|91.3%|2.13|
|7|0%|soft cycle|0.985|100%|1.71|
|7|5%|soft cycle|0.607|69.9%|2.04|
|7|10%|soft cycle|0.499|49.7%|2.27|
|7|15%|clockwork|0.314|8.1%|2.38|
|11|0%|soft cycle|0.990|100%|2.33|
|11|5%|soft cycle|0.431|28.9%|2.10|



**Table 6:** GPT-2-XL results (173 samples). 

|_S_|_ρ_|Topology|Avg _ϕ_|Detection|PPL|
|---|---|---|---|---|---|
|2|0%|soft cycle|1.000|100%|1.52|
|2|5%|soft cycle|1.000|100%|1.52|
|2|10%|soft cycle|1.000|100%|1.52|
|2|15%|soft cycle|1.000|100%|1.52|
|4|0%|soft cycle|1.000|100%|2.14|



**Summary.** All three models (Llama-3.2-3B, Mistral-7B, GPT-2-XL) achieve 100% detection at _ρ_ = 0% across all tested state counts and both transition topologies (soft cycle and clockwork). Mistral-7B exhibits notably lower perplexity (1.71 vs 4.20 for Llama at _S_ = 7), suggesting larger vocabulary sizes reduce partitioning constraints. The overlap sensitivity pattern ( _ρ ≥_ 5% degrades detection) is consistent across architectures and topologies, confirming theoretical predictions hold regardless of model or transition matrix choice. 

14 

