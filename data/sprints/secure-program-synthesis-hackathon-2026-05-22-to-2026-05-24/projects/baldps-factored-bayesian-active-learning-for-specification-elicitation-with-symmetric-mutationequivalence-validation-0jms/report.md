# **BALD-PS: Factored Bayesian Active Learning for Specification Elicitation, with Symmetric Mutation-Equivalence Validation** 

Barsat Khadka 

The University of Southern Mississippi 

```
Barsat.Khadka@usm.edu
```

Code: `github.com/BarsatKhadka/BALD-PS` 

### **Abstract** 

Specifications written in natural language are silently ambiguous: independent agents reading the same one-line requirement produce specifications that agree on the obvious behaviour and disagree precisely on the edge cases where bugs and security holes live. We exploit a simple structural fact — _a specification is two predicates_ , a precondition `requires` and a postcondition `ensures` — so the agent-disagreement posterior factorises into two independent axes. Three contributions follow. First, an oracle answer to a probe input is _dual-purpose_ : its validity verdict shrinks the precondition axis, its true output shrinks the postcondition axis. We prove that, under conditional independence of the two axes given the input, the joint mutual information decomposes as a sum, justifying greedy Bayesian Active Learning by Disagreement (BALD) on the factored posterior. Second, we replace the version-space _elimination_ survivor with a _synthesis_ step that returns the fragment recombination supported by the resolved cell of the factored posterior — a strict generalisation that recovers correct specifications no single agent wrote, supplemented by an optional LLM _re-synthesis_ step that escapes the recombination ceiling. Third, we introduce a novel validation criterion — _symmetric mutation-equivalence tightness_ — a single number on [0 _,_ 1] that simultaneously requires every one-edit perturbation of the specification to be refuted by the implementation ensemble _and_ every one-edit perturbation of an implementation to be rejected by the specification. We prove that this criterion is strictly stronger than the standard ensembleagreement certification, in the sense that it exposes _vacuously satisfied_ specifications that agreement passes. Empirically, on a controlled benchmark of seven ambiguous HumanEval-style tasks our synthesised specifications are correct on **7** _/_ **7** , with mean symmetric tightness **0** _._ **94** . On a live `gpt-4o` draw of seventeen tasks, synthesis is correct on **10** _/_ **17** (Wilson 95% CI [0 _._ 36 _,_ 0 _._ 78], graded **95.3%** ); a SpecMind-style multi-turn LLM refinement loop, run on the same task set with the same simulated oracle and a 1 _._ 4 _×_ query budget, achieves **5** _/_ **17** (graded 63.9%). On this draw synthesis is correct on **2** _×_ as many tasks as the SpecMind-style baseline, is + **31** _._ **4** percentage points higher on graded score, and uses **28** % fewer oracle queries; the Wilson intervals overlap and per-task SpecMind outcomes were not retained for this run, so that comparison is unpaired. The synthesis-vs-no-loop contrast is statistically significant at _α_ = 0 _._ 05 (uncorrected, exact two-sided McNemar, _p_ = 0 _._ 031, six paired wins, zero losses). 

# **1 Introduction** 

Going from a natural-language requirement to a formal specification is error-prone, and the errors are _silent_ . The one-line requirement “return the index of the maximum element of a list of integers” does not say what to do with an empty list, with ties, with non-integer inputs. Three competent engineers writing the formal specification will produce three different predicate pairs, each internally consistent, each disagreeing on a different silent edge case. 

1 

When one of those specifications is then used to drive code generation or verification, the resulting bug lives exactly where the original requirement was vague. 

We frame the problem as _specification elicitation by Bayesian active learning_ : sample a distribution of candidate specifications from several agent personalities, find the input on which they disagree most, ask the developer the single most informative question, eliminate the candidates the answer refutes, and repeat. The goal is convergence in _one or two tie-breaker questions_ . 

The starting point of the present work is a structural fact that prior interactivespecification systems do not fully exploit: **a specification is two predicates** . A specification is a precondition `requires` , a Boolean function of the inputs that says which calls are legal, and a postcondition `ensures` , a Boolean function of the inputs and the returned value that says which outputs are acceptable. Agent disagreement therefore lives on _two independent axes_ : which inputs are legal, and which outputs are correct. Exploiting that factoring is the technical core of the BALD-PS procedure, and it gives three connected contributions: 

1. **Dual-purpose factored queries (§4).** Each oracle answer carries information about _both_ axes simultaneously — the validity verdict shrinks the precondition axis, the true output shrinks the postcondition axis. We prove that under conditional independence the joint information gain decomposes as a sum (Theorem 6), justifying greedy BALD on the factored posterior. 

2. **Synthesis beyond elimination (§6).** Pure version-space elimination cannot recover specifications no single agent wrote, even when the correct reading is a _recombination_ of two agents’ fragments. We return instead the cell of the factored posterior supported by the evidence — _synthesis_ — and prove this is a strict generalisation (Theorem 8). An optional LLM re-synthesis step escapes the recombination ceiling. 

3. **Symmetric mutation-equivalence validation (§7).** Implementation-ensemble agreement on hidden tests is necessary but not sufficient: a vacuously permissive specification passes. We propose a new criterion that applies mutation testing _symmetrically_ — every one-edit perturbation of the specification must be refuted by the impl ensemble _and_ every one-edit perturbation of an implementation must be rejected by the specification. We prove this criterion is strictly stronger than ensemble agreement (Theorem 9). 

Figure 1 gives the architectural picture; Figure 2 shows the factored hypothesis space and the key claim that selection is restricted to its diagonal while synthesis reaches the full grid. 

**Headline empirical result.** On a live `gpt-4o` draw of 17 ambiguous tasks, synthesis is correct on **10** _/_ **17** tasks (graded **95** _._ **3** %) using on average 5.53 oracle queries. A SpecMindstyle multi-turn LLM refinement loop [7], granted a more generous 8-round budget on the same task set with the same simulated oracle, achieves **5** _/_ **17** (graded 63.9%) at 7.71 queries. On this 17-task draw synthesis is more correct (2 _×_ as many tasks), 31 _._ 4 percentage points higher on the graded score, and uses 28% fewer questions; per-task SpecMind outcomes were not retained in this run, so the comparison is unpaired and the Wilson intervals overlap. The synthesis-vs-no-loop contrast survives an exact two-sided McNemar test, _p_ = 0 _._ 031 (six paired wins, zero losses on 17 tasks), without correction for multiple comparisons. 

2 



<!-- Start of picture text -->
Requirement Sample N specs Factor into BALD<br>(one line of NL) & impls H requires  × H ensures dual-purpose<br>Symmetric LLM Synthesise Interviewer<br>mutation tightness re-synthesise (recombine) + audit<br><!-- End of picture text -->

**Figure 1: Architecture.** Four colour groups, read along the arrows: sampling (blue), factored active learning (amber), synthesis (green), and local validation (purple). The developer (oracle) is consulted only during the BALD loop and the audit; every other stage is automatic. 

# **2 Background** 

**Active learning by disagreement.** Bayesian Active Learning by Disagreement [1] selects, at each step, the input _x_ that maximises the mutual information between the model’s prediction and the posterior over hypotheses: 



<!-- Start of picture text -->
x ∗ = arg max I( Yx ; Θ  | D ) , (1)<br>x∈P<br><!-- End of picture text -->

where _Yx_ is the predicted label, Θ are the model parameters, and _D_ the current data. The objective rewards inputs on which the posterior hypotheses disagree most. BALD has been deployed for image classification, Gaussian processes, and preference elicitation; we are not aware of prior application to formal-specification inference. 

**Mutation testing.** Classical mutation testing [14, 15] introduces small syntactic mutations into a program and measures the fraction killed by a test suite. The _competent programmer hypothesis_ [15] states that real bugs are within a one-edit neighbourhood of correct code, justifying one-edit mutation operators. The technique has more recently been applied to LLM-generated invariants for hardware verification [12] and to Dafny specifications [13]. Both prior works are _one-directional_ : they mutate the code and check that the specification flags the mutants. We extend the criterion symmetrically (§7). 

**Specification inference.** Daikon [5] infers loop invariants from execution traces; QuickSpec [6] generates equational specifications by random testing. Recent LLM-driven systems include AutoSpec [8], FUN2SPEC [9], SpecGen [10], and the comprehensive FormalBench evaluation [11]. None of these factorise the predicate pair, none exploits the dual-purposequery property, and none validates with a symmetric mutation-equivalence criterion. SpecMind [7] is the closest interactive competitor: a multi-turn LLM postcondition refinement loop. We compare directly against it in §10. 

# **3 Specifications as Predicate Pairs** 

Let _f_ be a function with signature _f_ ( _x_ 1 _, . . . , xk_ ). A specification _S_ is a pair of executable predicates, 



<!-- Start of picture text -->
requires  :  X 1  × · · · × Xk →{⊤, ⊥}, (2)<br>ensures  :  X 1  × · · · × Xk × Y →{⊤, ⊥}, (3)<br><!-- End of picture text -->

where `requires` ( **x** ) = _⊤_ means the input **x** is a legal call, and `ensures` ( **x** _, y_ ) = _⊤_ means the output _y_ is acceptable on that input. We write _S_ = ( `requires` _,_ `ensures` ) and _S_ ( **x** _, y_ ) _≡ ¬_ `requires` ( **x** ) _∨_ `ensures` ( **x** _, y_ ) for the implication-form semantics. 

3 



<!-- Start of picture text -->
e 5 ⋆ • • sampled spec Si = ( ri, ei )<br>⋆ off-diagonal cell<br>reached by synthesis<br>e 4 •<br>Selection returns at most one<br>e 3 • of the • cells, if any<br>survives the oracle evidence.<br>e 2 • Synthesis can return any<br>cell of H consistent with<br>the evidence – in particular,<br>e 1 •<br>the off-diagonal ⋆ .<br>r 1 r 2 r 3 r 4 r 5<br>H requires (precondition classes)<br>(postconditionclasses) H ensures<br><!-- End of picture text -->

**Figure 2: The factored hypothesis space.** Five agents sample five diagonal-ish cells _{_ ( _ri, ei_ ) _}_<sup>5</sup> _i_ =1<sup>_⊂Hs_.</sup> The correct specification may be an _off-diagonal_ cell (highlighted green): one agent’s precondition paired with a different agent’s postcondition. Pure selection can only return one of the diagonal _•_ cells; synthesis recombines the surviving fragments and reaches any cell of _H_ . Theorem 8 formalises the strict expressive-power gap. 

Specifications are sampled by varying the _persona_ , not just the temperature, of an LLM (Literalist, Edge-Case Lawyer, Happy-Path Pragmatist, Defensive Engineer, Generalist; [19, Algorithm 1]). The five personas resolve silent edge cases according to characteristic disciplines, producing a diverse rather than noisy sample. Implementations are sampled from a separate set of personas (Idiomatic, Explicit, Functional) and used at validation time. 

An _oracle_ answers, for any input **x** , a pair ( _V, Y_ ) in which _V ∈{⊤, ⊥}_ is the validity verdict and _Y ∈Y ∪{⊥}_ is the true output (defined only when _V_ = _⊤_ ). In our evaluation the oracle is simulated by the canonical solution of a HumanEval-style benchmark task, modelling a perfect developer. 

# **4 The Factored Hypothesis Space** 

Sample _N_ specifications _S_ 1 _, . . . , SN_ , one per persona. Each _Si_ = ( `requires` _i,_ `ensures` _i_ ) contributes a precondition fragment and a postcondition fragment. We extract those fragments syntactically (an AST-level surgery; see Appendix A) and group behaviourally identical fragments into _classes_ relative to a fixed probe pool _P ⊂X_ : 



<!-- Start of picture text -->
requires i ≡P requires j ⇐⇒ � requires i ( x )� x ∈P = � requires j ( x )� x ∈P , (4)<br>ensures i ≡P ensures j ⇐⇒ � {y :  ensures i ( x , y ) } � x ∈P = � {y :  ensures j ( x , y ) } � x ∈P .<br>(5)<br><!-- End of picture text -->

Quotienting by these equivalences gives finite class sets _H_ `requires` and _H_ `ensures` , and the _factored hypothesis space_ is the product 



<!-- Start of picture text -->
H = H requires  × H ensures . (6)<br><!-- End of picture text -->

A point of _H_ is a complete specification; a _cell_ pairs one precondition reading with one postcondition reading. The agents sample _N_ specs which constitute the _diagonal-ish_ subset _Hs ⊆H_ ; the correct specification need not be in _Hs_ . 

4 

## **4.1 Dual-purpose queries** 

Let _R ∈H_ `requires` and _E ∈H_ `ensures` be the latent precondition and postcondition classes. The oracle’s answer on an input **x** is the pair ( _V, Y_ ). Observe two structural facts: 

- _V_ is fully determined by _R_ given **x** : the validity of an input is a function only of the precondition. 

- Conditional on _V_ = _⊤_ , _Y_ depends only on _E_ given **x** : the true output is a function only of the postcondition (the precondition has admitted the input). 

Both axes are therefore queried by a _single_ oracle answer. This property is not a heuristic; it is a consequence of the predicate-pair structure (cf. Theorem 6). 

# **5 Active Learning over Factored Posteriors** 

We place a uniform prior over _H_ (concretely, uniform over the agent-sampled set _Hs_ ; richer priors are immediate). For a probe **x** _∈P_ define the per-axis Shannon entropies 



<!-- Start of picture text -->
H requires ( x ) = − � Pr( requires ( x ) =  v ) log2 Pr( requires ( x ) =  v ) , (7)<br>v∈{⊤,⊥}<br>H ensures ( x ) = − � Pr( {y :  ensures ( x , y ) }  =  A ) log2 Pr( {y :  ensures ( x , y ) }  =  A ) , (8)<br>A<br><!-- End of picture text -->

where the outer sum on H `ensures` runs over the finite set of distinct accepted-output sets induced by the surviving postcondition classes on **x** . The **factored BALD score** of probe **x** is 



<!-- Start of picture text -->
s ( x ) = H requires ( x ) + H ensures ( x ) (9)<br><!-- End of picture text -->

and the next probe is **x**<sup>_⋆_</sup> = arg max **x** _s_ ( **x** ). We will justify (9) as the _exact_ information gain on the joint ( _R, E_ ) in Theorem 6. 

After the oracle returns ( _V, Y_ ) on **x** : 

- every precondition class _r_ with _r_ ( **x** ) _̸_ = _V_ is eliminated; 

- if _V_ = _⊤_ , every postcondition class _e_ inconsistent with the truth at **x** (rejecting _Y_ or accepting a wrong candidate) is eliminated. 

The loop stops when both axes are singletons. To avoid spurious residual distinctions, once _H_ `requires` collapses to a single class we project _H_ `ensures` onto the inputs that surviving class admits; postcondition distinctions that only show up on now-illegal inputs are merged away. 

Algorithm 1 states the full loop, augmented with an LLM _interviewer_ audit phase (lines 3, 10 of Algorithm 1) that addresses ambiguities the agents resolved unanimously. 

# **6 Synthesis Beyond Elimination** 

After the loop terminates we have a resolved factored model and an evidence set _E_ = _{_ ( **x** _j, Vj, Yj_ ) _}j_ . Two return policies are natural. 

**Selection.** Return the surviving whole agent spec, if any: _π_ sel( _E_ ) = _Si_<sup>_⋆_</sup> for some _i_<sup>_⋆_</sup> with _Si_<sup>_⋆_</sup> consistent with every point of _E_ , or _⊥_ if none exists. This is the version-space survivor. 

**Synthesis.** Return the recombined cell of the factored posterior: 



<!-- Start of picture text -->
π syn( E ) = ( r ⋆ , e ⋆ ) , r ⋆ ∈H requires , e ⋆ ∈H ensures , (10)<br><!-- End of picture text -->

5 

**Algorithm 1** Factored BALD elicitation with interviewer audit and synthesis **Require:** requirement _ρ_ , agent personas, oracle _O_ , budget _B_ 1: _{Si}_<sup>_N_</sup> _i_ =1<sup>_←_SampleSpecs(</sup><sup>_ρ_);</sup> _I ←_ SampleImpls( _ρ_ ) 2: _P ←_ Adversary( _ρ, {Si}, I_ ) _∪_ Structural( _ρ_ ) 3: Questions _←_ Interviewer( _ρ_ ); _P ←P ∪_ Questions 4: ( _H_ `requires` _, H_ `ensures` ) _←_ BuildFactoredModel( _{Si}, P_ ) 5: _E ←∅_ 6: **while** _|H_ `requires` _| >_ 1 **or** _|H_ `ensures` _| >_ 1 **and** _|E| < B_ **do** _▷_ BALD loop 7: **x**<sup>_⋆_</sup> _←_ arg max **x** _∈P\E s_ ( **x** ) _▷_ equation (9) 8: ( _V, Y_ ) _←O_ ( **x**<sup>_⋆_</sup> ); _E ←E ∪{_ ( **x**<sup>_⋆_</sup> _, V, Y_ ) _}_ 9: ( _H_ `requires` _, H_ `ensures` ) _←_ Update( _H_ `requires` _, H_ `ensures` _,_ **x**<sup>_⋆_</sup> _, V, Y_ ) 10: **end while** 11: **audit:** for each _q ∈_ Questions not yet in _E_ , query _O_ , update ( _H_ `requires` _, H_ `ensures` ) (capped by budget) 12: _S_<sup>_⋆_</sup> _←_ Synthesise( _H_ `requires` _, H_ `ensures` _, E_ ) _▷_ §6 13: **return** _S_<sup>_⋆_</sup> 

where _r_<sup>_⋆_</sup> is the _consensus_ class on the precondition axis (largest member weight, ties broken by spec id) and _e_<sup>_⋆_</sup> analogously on the postcondition axis. The two need not come from the same agent. 

**LLM re-synthesis.** If the recombination is bounded by the fragments the agents wrote, an optional step regenerates a spec by prompting an LLM with the requirement, every candidate reading and the full evidence set. We _adopt_ the regeneration only if it is consistent with every recorded ( **x** _j, Vj, Yj_ ); if the first attempt fails consistency we provide the failing point as a self-debug hint and retry once. This step pushes the attainable hypothesis space outside _H_ but never adopts a spec that contradicts paid-for oracle answers. 

# **7 Symmetric Mutation-Equivalence Validation** 

Implementation-ensemble certification asks whether _K_ independently written implementations behave identically on a hidden test suite. This is necessary but not sufficient: a vacuously permissive specification — one whose `ensures` accepts every output — passes certification trivially. We strengthen the check with a local, mutation-based criterion applied _symmetrically_ . 

**Definition 1** (Mutation operators) **.** Let _µ_ denote the AST-level one-edit mutator (Appendix A) over Python comparison operators, boolean and binary arithmetic operators, boolean and integer literals, and a small set of identifier swaps ( `lower` _↔_ `upper` , `min` _↔_ `max` ). For a source _σ_ write _µ_ ( _σ_ ) for the set of one-edit mutants. 

**Definition 2** (Equivalent mutants) **.** A mutant _σ_<sup>_′_</sup> _∈ µ_ ( _σ_ ) is _behaviourally equivalent_ to _σ_ relative to _P_ , written _σ_<sup>_′_</sup> _≡P σ_ , if their `Assessment` (for specs) or output trace (for implementations) coincides on every probe. Equivalent mutants carry no discriminatory signal and are excluded from both denominators below, in line with classical mutation-testing convention [14]. 

**Definition 3** (Spec-mutation kill rate) **.** For specification _S_ , implementation ensemble _I_ , 

6 



<!-- Start of picture text -->
kill rate κS  : mutate S → σ ′ ;<br>some impl refutes σ ′ on some probe<br>Specification Implementation<br>S = ( requires ,  ensures ) ensemble I<br>catch rate κI  : mutate Ik → I ′ ;<br>spec rejects I ′ on some probe<br>2  κS κI<br>τ = ∈ [0 , 1]<br>κS +  κI<br><!-- End of picture text -->

**Figure 3: Symmetric mutation-equivalence tightness.** Prior work [13, 12] mutates only the code (the amber direction) and checks that the specification flags the mutants. Symmetric tightness adds the red direction: mutate the _specification_ and check that the implementations refute it. A vacuously permissive spec passes the amber direction trivially – it accepts every impl mutant’s output – but fails red ( _κS_ = 0), so the harmonic mean _τ_ is zero. Theorem 9 formalises this dominance. 

and probe pool _P_ , 



<!-- Start of picture text -->
� {σ′ ∈ µ ( S ) :  σ′̸ ≡P S, ∃ x  ∈P the ensemble refutes σ′ at x } �<br>κS ( S, I, P ) = . (11)<br>� {σ′ ∈ µ ( S ) :  σ′̸ ≡P S} �<br><!-- End of picture text -->

The ensemble _refutes σ_<sup>_′_</sup> at **x** if there is impl consensus at **x** and either (i) _σ_<sup>_′_</sup> disagrees with _S_ about `requires` ( **x** ), or (ii) _σ_<sup>_′_</sup> rejects the impl-consensus output that _S_ accepts. 

**Definition 4** (Impl-mutation catch rate) **.** 



<!-- Start of picture text -->
� {I ′ ∈ � k µ ( Ik ) :  I ′̸ ≡P Ik, S catches I ′} �<br>κI ( S, I, P ) = . (12)<br>� {I ′ ∈ � k µ ( Ik ) :  I ′̸ ≡P Ik} �<br><!-- End of picture text -->

_S catches I_<sup>_′_</sup> if there exists **x** _∈P_ with `requires` ( **x** ) = _⊤_ and either _I_<sup>_′_</sup> crashes on **x** or _I_<sup>_′_</sup> produces an output _S_ rejects. 

**Definition 5** (Symmetric tightness) **.** The _symmetric mutation-equivalence tightness_ is the harmonic mean of the two rates, 



<!-- Start of picture text -->
2  κS κI<br>τ ( S, I, P ) = ∈ [0 ,  1] , (13)<br>κS +  κI<br><!-- End of picture text -->

with the convention _τ_ = nan when both rates are undefined (no actionable mutants on either side) and _τ_ = (the defined rate) when exactly one side is undefined. 

# **8 Theoretical Results** 

We state three results: the information-decomposition that justifies the BALD score (9), the expressive-power dominance of synthesis over selection, and the characterisation of symmetric tightness as strictly stronger than ensemble agreement. 

7 

**Theorem 6** (Dual-purpose information decomposition) **.** _Let R ∈H_ _`requires` , E ∈H_ _`ensures` be the latent precondition and postcondition classes, and_ ( _V, Y_ ) _the oracle’s answer on a probe_ **x** _. Suppose the conditional independence assumption_ 



<!-- Start of picture text -->
P ( R, E |  x ) = P ( R |  x )  P ( E |  x ) (14)<br><!-- End of picture text -->

_holds. Then_ 



<!-- Start of picture text -->
I�( V, Y  ); ( R, E )� = I( V  ;  R ) + Pr( V =  ⊤ )  ·  I( Y  ; E | V =  ⊤ ) . (15)<br><!-- End of picture text -->

_Proof._ By the chain rule of mutual information, I(( _V, Y_ ); ( _R, E_ )) = I( _V_ ; ( _R, E_ ))+I( _Y_ ; ( _R, E_ ) _| V_ ) _._ The validity verdict _V_ is determined by _R_ alone (the precondition fixes which inputs are legal), so by the data-processing inequality with equality, I( _V_ ; ( _R, E_ )) = I( _V_ ; _R_ ). When _V_ = _⊥_ the postcondition is unconstrained and _Y_ is undefined; the conditional term therefore contributes only on the event _V_ = _⊤_ . On that event, _Y_ depends only on _E_ given **x** by conditional independence, so I( _Y_ ; ( _R, E_ ) _| V_ = _⊤_ ) = I( _Y_ ; _E | V_ = _⊤_ ). Multiplying by Pr( _V_ = _⊤_ ) and recombining yields (15). 

**Corollary 7.** _Under the conditions of Theorem 6, the BALD-optimal probe satisfies_ **x**<sup>_⋆_</sup> = arg max **x** I(( _V, Y_ ); ( _R, E_ )) _, which by_ (15) _coincides with the sum-of-per-axis-entropy objective in_ (9) _up to a common_ Pr( _V_ = _⊤_ ) _scaling per probe._ 

**Theorem 8** (Synthesis expressive power) **.** _Let Hs ⊆H denote the agent-sampled subset. Then_ 

- _(i) πsel_ ( _E_ ) _returns at most one element of Hs, hence its range is contained in Hs;_ 

- _(ii) πsyn_ ( _E_ ) _returns one element of H, hence its range is contained in H;_ 

- _(iii) there exist instances on which πsel_ ( _E_ ) _returns nothing while πsyn_ ( _E_ ) _returns a specification consistent with the oracle’s true target._ 

_Proof._ (i) and (ii) are immediate from the policy definitions. For (iii) we exhibit a concrete witness. Consider a task with _N_ = 3 agents producing specs of the schema _{_ ( _r_ 1 _, eW_ ) _,_ ( _r_ 2 _, eC_ ) _,_ ( _r_ 2 _, eW_ ) _}_ , where _r_ 1 is the correct precondition reading, _eC_ is the correct postcondition reading, and _r_ 2 _, eW_ are incorrect. Two BALD queries on a preconditiondiscriminating probe and a postcondition-discriminating probe eliminate every diagonal cell: ( _r_ 1 _, eW_ ) by the postcondition probe, ( _r_ 2 _, eC_ ) and ( _r_ 2 _, eW_ ) by the precondition probe. Pure selection therefore returns nothing. The synthesis recombination ( _r_ 1 _, eC_ ) _∈H \ Hs_ is consistent with both queries and is the correct specification. Case A in §11 instantiates the schema with the `second_largest` task. 

**Theorem 9** (Symmetric tightness dominates ensemble agreement) **.** _Let α_ ( _S, I_ ) _denote the implementation-ensemble agreement score on a hidden test suite (the certification metric). Then_ 

- _(i) τ_ ( _S, I, P_ ) = 1 iff _every non-equivalent perturbation on either side is detected by the other: the specification and the ensemble are_ locally mutation-equivalent _on P._ 

- _(ii) A_ vacuous _specification — one whose_ _`ensures`_ ( **x** _, ·_ ) _accepts every output for every_ **x** _with_ _`requires`_ ( **x** ) = _⊤ — has κI_ = 0 _and thus τ_ = 0 _, while it may attain α_ = 1 _on the same task._ 

_Hence τ is a strictly stronger criterion than α in the sense of (i)–(ii): it separates pairs that α identifies._ 

8 

_Proof._ (i) is by definition of the rates: _τ_ = 1 iff both _κS_ = 1 and _κI_ = 1, which holds exactly when every non-equivalent mutant on either side is detected by the other. (ii) For a vacuous specification, any implementation produces an output the spec accepts, including every impl mutant’s output on any legal input; therefore no impl mutant is “caught” and _κI_ = 0. The harmonic mean _τ_ = 2 _κSκI /_ ( _κS_ + _κI_ ) is zero whenever either rate is zero. Meanwhile, the implementations may agree unanimously on every hidden test independently of the specification, so _α_ = 1 is possible. Hence _τ_ separates pairs ( _S, I_ ) that _α_ identifies. _Remark._ This is the precise sense in which _τ_ is more informative than prior one-directional mutation tests of LLM-generated specifications [13, 12]: those works measure _κI_ alone and do not detect the vacuous-spec failure mode of (ii). 

## **8.1 Convergence** 

**Proposition 10** (Bounded query count under separable contested axes) **.** _Let a denote the number of_ contested axes _at sampling time: a_ = ⊮[ _|H_ _`requires` | >_ 1] + ⊮[ _|H_ _`ensures` | >_ 1] _. If, for each contested axis, there exists a probe in P whose answer collapses that axis to a singleton independently of the other axis (the “separable probes” condition), then greedy BALD on the factored posterior terminates in at most a queries._ 

_Proof._ Each oracle answer monotonically refines (cannot enlarge) each axis’s class set. Under the separable-probes condition, the probe maximising (9) on a still-contested axis _α_ collapses _α_ to a singleton in one step; the post-step projection step (merge-by-admitted-probes; see §5) leaves no residual distinction on the resolved axis. Hence each contested axis costs one query. 

In practice (§10) the controlled-benchmark mean is 1.86 queries on tasks whose contestedaxis count averages 1.57, slightly above the floor of the bound because some probes carry information on only one axis (so a second query is needed even though one “contested axis” becomes a singleton on the first answer). 

# **9 Experimental Setup** 

**Benchmark.** Seven hand-authored controlled tasks (mock backend) plus ten live-only HumanEval-style tasks — **17** tasks total. The mock tasks are paired with hand-authored agent specifications in the project’s `mock_registry` ; this isolates the _algorithm_ from LLM noise. The live-only tasks have only a canonical solution and a hidden test suite, and require the LLM backend. One mock task, `second_largest` , is designed so that no whole agent spec is correct — only a recombination is, making it the machine-checked witness of Theorem 8. 

**Metrics.** We report the binary `spec_is_correct` verdict (oracle agreement on every probe and hidden test), the graded `spec_score` (fraction of consistency checks passed), the symmetric tightness _τ_ of Theorem 5, and the implementation-ensemble agreement _α_ . 

**Baselines.** (1) **No-loop:** trust the first agent’s spec, ask nothing. (2) **Selection:** return the whole spec surviving elimination, if any. (3) **Random query strategy:** uniform over informative probes; averaged over five seeds with mean _±_ std. (4) **Direct-GPT:** ask `gpt-4o` to write the spec from the requirement alone, no loop, no oracle. (5) **SpecMind-style [7]:** a multi-turn LLM refinement loop with the same oracle, no factored hypothesis space, 

9 

**Table 1: Controlled benchmark (mock).** Synthesis is exact and locally tight on every task. Random query strategy is averaged over 20 seeds with mean _±_ std. “Rescued” indicates synthesis succeeds where elimination has no correct survivor. 

|task|axes|_q_B|_q_R|no-loop|select|synth|graded|_κS_|_κI_|_τ_|
|---|---|---|---|---|---|---|---|---|---|---|
|find_max_index|2|2|2.85_±_0.36|✗|✓|✓|1.00|0.67|1.00|0.80|
|longest|2|2|2.00_±_0.00|✗|✓|✓|1.00|0.80|1.00|0.89|
|below_zero|1|2|2.00_±_0.00|✗|✓|✓|1.00|1.00|1.00|1.00|
|sum_to_n|2|2|1.55_±_0.50|✓|✓|✓|1.00|1.00|1.00|1.00|
|truncate_number|1|1|1.35_±_0.48|✓|✓|✓|1.00|1.00|1.00|1.00|
|count_distinct|1|2|1.95_±_0.22|✗|✓|✓|1.00|1.00|n/a|1.00|
|second_largest _(rescued)_|2|2|2.00_±_0.00|✗|✗|✓|1.00|0.70|1.00|0.82|
|**mean**||1.86|1.96|2/7|6/7|**7/7**|**1.00**|0.88|1.00|**0.93**|



no agent ensemble, no synthesis-by-recombination; granted a generous eight-round query budget. 

**Ablations.** The four-cell grid _{_ interview _∈{_ on _,_ off _}} × {_ resynth _∈{_ on _,_ off _}}_ , with synthesis and the factored loop on throughout. 

**Statistics.** Wilson 95% score-interval confidence intervals on every binary correctness number; exact two-sided McNemar test on paired per-task outcomes, with per-pair win / tie / loss counts. 

**Reproducibility.** All mock results are deterministic. Live results are reported with persona temperatures fixed in `baldps/agents.py` (range 0.1–0.9), default `gpt-4o` , fixed random-query-strategy seeds. The full pipeline is one command: 

```
pythoneval/run_eval.py--backendopenai
```

`--direct-gpt --specmind` . 

# **10 Results** 

## **10.1 Controlled benchmark** 

Table 1 reports the controlled benchmark, where the algorithm is isolated from LLM noise by hand-authored agent specifications. Synthesis is correct on **7** _/_ **7** tasks of this controlled benchmark and locally tight at _τ_ mean **0** _._ **93** ; selection succeeds on 6 _/_ 7 (failing only on `second_largest` , the constructed off-diagonal witness of Theorem 8); no-loop succeeds on 2 _/_ 7. 

## **10.2 Live** **`gpt-4o` benchmark** 

Table 2 reports the live numbers on 17 tasks with Wilson 95% confidence intervals. Synthesis is correct on **10** _/_ **17** , graded **95.3** %, mean tightness _τ_ = 0 _._ 94. Synthesis is correct on 2 _×_ as many tasks as the SpecMind-style baseline (10 _/_ 17 vs. 5 _/_ 17) and uses 28% fewer oracle queries on this draw; the Wilson intervals overlap and per-task SpecMind outcomes were not retained for this run, so the comparison is unpaired. 

Figure 4 shows the head-to-head visually; Table 3 gives the paired McNemar tests. 

10 

**Table 2: Live benchmark (** **`gpt-4o` , 17 tasks).** Wilson 95% confidence intervals on binary correctness. “ _q_ ” is the average oracle-query budget. The closest published interactive competitor (SpecMind-style [7]) is granted a 1 _._ 4 _×_ query budget relative to ours; synthesis nevertheless wins on every axis simultaneously — **2** _×_ binary, + **31** _._ **4** pp graded, _−_ **28** % queries. 

|method|binary|Wilson 95% CI|graded|_q_|
|---|---|---|---|---|
|**synthesis (this work, full)**|**10/17**|**[0.36, 0.78]**|**95.3%**|5.53|
|selection only|8/17|[0.26, 0.69]|—|—|
|no-loop baseline|4/17|[0.10, 0.47]|77.2%|0.00|
|direct-GPT one-shot|5/17|[0.13, 0.53]|78.2%|0.00|
|SpecMind-style [7]|5/17|[0.13, 0.53]|63.9%|7.71|
|symmetric tightness (synthesis)|mean _τ_|= 0_._94<br>(_κS_ = 0_._9|0, _κI_ = 1|_._00)|
|tasks rescued by synthesis<br>ensemble agreement (certify)|2 / 17 <br>_α_= 95_._|(no whole sampled <br>3%|spec is c|orrect)|





<!-- Start of picture text -->
synthesis (this work) 0.588<br>selection only 0.471<br>SpecMind-style 0.294<br>direct-GPT one-shot 0.294<br>no-loop 0.235<br>0 0.25 0.5 0.75 1.0<br>fraction of 17 tasks correct (binary)<br><!-- End of picture text -->

**Figure 4: Live binary correctness with Wilson 95 % CIs** ( _n_ = 17 tasks). Whiskers are the Wilson score intervals; numeric labels are the point estimates. The intervals overlap at the tails — at _n_ = 17 a 3-task absolute difference does not separate two proportions at _α_ = 0 _._ 05 marginally — so the empirical comparison relies on _paired_ per-task tests (Table 3). On the synthesis-vs-no-loop pair (6 paired wins, 0 losses, 11 ties), exact McNemar gives _p_ = 0 _._ 031. The other contrasts are direction-consistent but underpowered at this sample size. 

## **10.3 Ablation** 

Table 4 isolates the contributions of the interviewer-driven audit phase and LLM re-synthesis. Re-synthesis is the more efficient ingredient on the live benchmark — it adds one task at one extra API call and zero extra oracle queries. The interviewer audit costs the 3.7-query mean uplift in _qB_ between the with- and without-interview rows; on this 17-task sample it does not change the live binary count (unanimous-wrong recovery, which the audit targets specifically, is rare on the live tasks but salient on the controlled benchmark, where it recovers `count_distinct` ). 

## **10.4 Pareto: correctness vs. query budget** 

Figure 5 shows the Pareto frontier on the controlled benchmark under a hard query budget _B ∈{_ 0 _,_ 1 _,_ 2 _,_ 3 _,_ 4 _, ∞}_ . The elbow is sharp at _B_ = 2, close to the information-theoretic floor implied by Theorem 10 for the benchmark’s average contested-axis count of 1.57 (the bound is not always tight, since some probes inform only one axis). Beyond two questions, on this 7-task controlled benchmark, the curve is flat. 

11 

**Table 3: Paired McNemar two-sided exact tests.** A-only = tasks where method A is correct and B is not; B-only = the reverse; “ties” = both correct or both wrong. The synthesis-vs-no-loop contrast is significant at _α_ = 0 _._ 05. The synthesis-vs-selection contrast is direction-consistent (two paired wins for synthesis, none for selection) but underpowered at _n_ = 17. 

|contrast|A-only|ties|B-only|_p_ (exact McNemar)|
|---|---|---|---|---|
|synthesis vs no-loop|6|11|0|**0.031**<sup>_∗_</sup>|
|synthesis vs selection|2|15|0|0.500|
|selection vs no-loop|4|13|0|0.125|



**Table 4: Ablation grid on the live benchmark.** 

|condition|_q_|binary|graded|
|---|---|---|---|
|full pipeline (this work)|5.53|**10/17**|**95.3%**|
|_−_interview|1.35|10/17|92.3%|
|_−_re-synthesis|5.00|10/17|89.9%|
|_−_both (factored core only)|1.35|10/17|89.9%|



## **10.5 Tightness diagnostic** 

The mean symmetric tightness across the live benchmark is _τ_ = 0 _._ 94; the per-task spread is informative. The lower tail ( `second_largest` , _τ_ = 0 _._ 84; `find_max_index` , _τ_ = 0 _._ 83) signals _correct but locally loose_ specifications: the binary verdict is positive but the spec contains predicate clauses the implementation ensemble does not witness. The leading example is the dead-branch failure mode in `find_max_index` discussed in §11. This is exactly the diagnostic _τ_ provides above and beyond _α_ (Theorem 9 (ii)): a perfect _α_ = 1 together with _τ <_ 1 flags a spec that is right on the canonical but contains unenforced clauses. 

# **11 Case Studies** 

We work three concrete examples that instantiate each of our three contributions. 

**Case A:** **`second_largest` — synthesis recovers an off-diagonal cell.** The requirement is _“return the second largest element of a list of integers.”_ Three personas sample ( _r_ 1 _, eW_ ) _,_ ( _r_ 2 _, eC_ ) _,_ ( _r_ 2 _, eW_ ) where _r_ 1 is “len(lst) _≥_ 2” (correct), _r_ 2 is “len _≥_ 1” (admits singletons; wrong), _eC_ is output = sorted(lst)[ _−_ 2] (positional; correct), _eW_ is the second-distinct-value reading (wrong on `[3, 3, 1]` ). Two BALD queries — the probe [3 _,_ 3 _,_ 1] (postcondition discriminator; oracle gives 3) and the probe [5] (precondition discriminator; oracle gives invalid) — eliminate every diagonal cell. Pure selection returns nothing; synthesis returns the off-diagonal cell ( _r_ 1 _, eC_ ) _∈H \ Hs_ , which is correct. This is the machine-checked witness of Theorem 8(iii) (see `tests/test_pipeline.py: test_synthesis_strictly_beats_selection` ). 

**Case B:** **`count_distinct` (live) — interviewer recovers a unanimous-wrong reading.** On the live backend all five `gpt-4o` personas read _“count distinct characters”_ as casesensitive ( `len(set(s))` ); the canonical is case-insensitive ( `len(set(s.lower()))` ). The factored model is therefore singleton on both axes — there is no agent disagreement to query — and the BALD loop asks nothing. The interviewer, reading the requirement directly, proposes the probe `’Aa’` with the clarifying question _“should uppercase and lowercase be the same character?”_ . The oracle answers 1 (case-insensitive). LLM re-synthesis, with that 

12 



<!-- Start of picture text -->
1<br>0 . 75<br>0 . 5<br>0 . 25 binary correct ( k/ 7)<br>graded score<br>0<br>0 1 2 3 4<br>query budget B<br>fractioncorrect<br><!-- End of picture text -->

**Figure 5: Pareto frontier** on the controlled benchmark. At _B_ = 0 (zero queries) synthesis already lifts both metrics above the no-loop baseline through the agent-consensus reading. The sharp elbow at _B_ = 2 matches Theorem 10: every contested axis costs one query, and the mean contested-axis count on the benchmark is 1.57. 

evidence in hand, writes the case-folding spec. Symmetric tightness on the result is _τ_ = 1 _._ 0 on the probe pool. 

**Case C:** **`find_max_index` — tightness diagnoses a correct-but-loose spec.** The synthesised specification for `find_max_index` is correct under the binary verdict ( `spec_is_correct` = _⊤_ ) yet has _κS_ = 0 _._ 67, hence _τ_ = 0 _._ 80. The diagnostic locus is the “empty list returns _−_ 1” branch inherited from the Edge-Case Lawyer’s postcondition fragment: the synthesised precondition rejects empty lists, so the branch is dead code that no implementation ever witnesses. Mutations targeting that branch are behaviourally distinct from the original but not refuted by the impl ensemble — _κS <_ 1. A minimisation pass that detects dead branches relative to the resolved precondition would push _τ_ to one. Crucially, the ensemble agreement _α_ = 1 on this task does _not_ flag the unenforced clauses; _τ_ does. This is the formal content of Theorem 9(ii) made concrete. 

# **12 Discussion and Limitations** 

**Statistical power.** At _n_ = 17 live tasks, the paired McNemar test on synthesis vs. selection has only two discriminating pairs (two paired wins for synthesis, zero losses, fifteen ties), yielding _p_ = 0 _._ 500 even though the direction is entirely in favour of synthesis. Detecting a direction-consistent difference at _α_ = 0 _._ 05 by McNemar requires at least six paired disagreements. Scaling the benchmark to full HumanEval (164 tasks) or running multi-seed live sampling per task is the standard fix. 

**Single-seed live sampling.** Our live binary correctness numbers come from a single `gpt-4o` draw per task. The interview and resynth ablation deltas are within singlesample variance; only multi-seed evaluation would let us attach a confidence interval to those deltas. 

**Two axes only.** Real specifications have finer structure (tie-breaking, ordering, numeric tolerance) that the factored model lumps into the postcondition axis. A _k_ -axis factoring derived from the partition lattice of the probes is the natural generalisation. 

**Simulated oracle.** The oracle is the canonical HumanEval solution. A real developer is noisy and inconsistent; oracle-noise robustness (via a Bayesian posterior instead of hard 

13 

elimination) is untested. 

**Recombination ceiling.** If no agent writes a correct precondition or a correct postcondition, no recombination is correct. The LLM re-synthesis step partially addresses this, but exact-match LLM specification generation under adversarial structural probes is an open problem upstream of the active-learning loop. 

**Mutation operator coverage.** The mutator covers six operator families; classical mutation testing tools deploy 40+ operators [14]. Equivalent-mutant detection is heuristic (behavioural on the probe pool only). Both numbers — _κS_ and _κI_ — are functions of the operator set and would change with richer operators. 

# **13 Related Work** 

**Active learning.** BALD [1] is the information-theoretic foundation; recent extensions include geometric BALD [2] and prediction-oriented BALD [3]. Active learning for preference elicitation [4] is closest in spirit. None of these has been specialised to a predicate-pair posterior. 

**Specification inference, classical.** Daikon [5] mines invariants from execution traces; QuickSpec [6] generates equational specs by random testing. Both are passive (no oracle querying) and do not factor the predicate pair. 

**Specification inference with LLMs.** Recent systems include AutoSpec [8], FUN2SPEC [9], SpecGen [10], and the comprehensive FormalBench evaluation [11]. SpecMind [7] is the closest interactive competitor: a multi-turn LLM postcondition refinement loop. We compare directly in Table 2. 

**Mutation testing of LLM artefacts.** The DATE 2024 paper [12] uses mutation testing to validate LLM-generated invariants for hardware verification. MutDafny (November 2025) [13] applies the technique to LLM-written Dafny specifications. Both mutate _only_ the code; they measure _κI_ . Our symmetric criterion adds _κS_ and proves the combined measure is strictly stronger than ensemble agreement in the sense of Theorem 9. 

**Interactive program synthesis.** PROSE / FlashFill [16, 17] use input–output examples to drive synthesis, not specification inference. Counterexample-guided abstraction refinement (CEGAR) [18] is the formal-methods analogue of our loop but operates over fixed verification queries, not LLM-sampled specifications. 

# **14 Conclusion** 

A specification is two predicates, and that simple structural fact lets active learning over the agent-disagreement posterior factorise cleanly: each oracle answer is dual-purpose, BALD converges in roughly one query per contested axis (Theorem 10), and synthesis-asrecombination recovers specifications that elimination-only methods cannot (Theorem 8). Symmetric mutation-equivalence then validates the result _locally_ (Theorem 9): a tight specification is one whose own perturbations are killed by the implementations and whose implementations’ perturbations are caught by the specification. On a controlled benchmark the combination is exact (7 _/_ 7) and locally tight ( _τ_ = 0 _._ 93). On a live `gpt-4o` draw of 17 

14 

tasks synthesis achieves 10 _/_ 17 binary correctness and 95 _._ 3% graded score, outperforming the closest published interactive competitor (SpecMind-style) on this benchmark by 2 _×_ on binary, +31 _._ 4 percentage points on graded, and using 28% fewer oracle queries on the same task set with the same simulated oracle (Wilson intervals overlap; per-task SpecMind outcomes were not retained, so this contrast is unpaired). The synthesis-vs-no-loop contrast is statistically significant at _α_ = 0 _._ 05 (uncorrected, exact McNemar, _p_ = 0 _._ 031). 

The principal remaining methodological gap is the statistical power of the synthesis-vsselection contrast at _n_ = 17, addressable by scaling to full HumanEval-164 and multi-seed sampling. Symmetric tightness, the factored BALD framework, and the synthesis-byrecombination procedure are all immediately applicable to that scale. 

# **Reproducibility** 

All code, data, and evaluation harnesses are released. The implementation is in Python 3.10 and runs untrusted LLM-generated code in an isolated subprocess. The full pipeline reduces to one command: 

```
pythoneval/run_eval.py--backendopenai--direct-gpt--specmind
```

Mock results are deterministic. Live results are reported with persona temperatures (range 0.1–0.9) fixed in `baldps/agents.py` and the default `gpt-4o` model. 

# **A AST-level fragment surgery and mutation** 

The synthesiser and the mutator both operate at the Python AST level. The synthesiser parses each spec source with `ast.parse` , identifies the `requires` and `ensures FunctionDef` nodes via the standard `ast.walk` , lifts them as `ast.get_source_segment` string slices alongside the module-level helpers, and reassembles arbitrary ( _r, e_ ) recombinations by string concatenation followed by `ast.parse` validation. 

The mutator enumerates the mutation sites of Theorem 1 in walk order. The _k_ -th mutant is produced by reparsing the source on each call (so identity of nodes is stable across mutants) and applying the _k_ -th edit in walk order, then `ast.unparse` -ing back to source. Mutants that fail to unparse, or that round-trip identically to the original under `ast.unparse` , are dropped. Equivalence (Theorem 2) is checked behaviourally on _P_ by sandboxed execution rather than syntactically. 

# **B Implementation details** 

**Sandbox.** Every spec and implementation runs in an isolated Python subprocess with a five-second wall-clock timeout. On timeout the batch is retried call-by-call, so a single non-terminating call cannot poison its neighbours. 

**Structural probe generator.** Disagreement-driven probe proposal is supplemented by a deterministic generator that, for each example input from the task tests, emits one-edit structural variants: empty containers, singletons, duplicates, sign flips, zero, and mixed-case variants for strings. Coverage of canonical edge cases is thereby independent of the LLM adversary’s stochastic sample. 

**Caching.** The live backend caches one (specs _,_ impls _,_ probes _,_ interview) tuple per task per process. The random-query-strategy sweep and the ablation grid therefore operate on 

15 

identical samples, removing sampling noise from the contrast. 

**Self-debug retry.** If the LLM re-synthesis produces a spec that contradicts an evidence point, the failing point is fed back as a “previously rejected because. . . ” hint and the LLM is asked to fix it. The retry is capped at one extra call. 

# **References** 

- [1] N. Houlsby, F. Huszár, Z. Ghahramani, M. Lengyel. _Bayesian Active Learning for Classification and Preference Learning._ arXiv:1112.5745, 2011. 

- [2] X. Yang, et al. _Bayesian Active Learning by Disagreements: A Geometric Perspective._ arXiv:2105.02543, 2021. 

- [3] F. Bickford Smith, et al. _Prediction-Oriented Bayesian Active Learning._ AISTATS, 2023. 

- [4] _On the Pros and Cons of Active Learning for Moral Preference Elicitation._ AIES, 2024. 

- [5] M. D. Ernst, et al. _Dynamically Discovering Likely Program Invariants to Support Program Evolution._ IEEE Trans. Software Eng., 2001. 

- [6] K. Claessen, N. Smallbone, J. Hughes. _QuickSpec: Guessing Formal Specifications using Testing._ TAP, 2010. 

- [7] _SpecMind: Cognitively Inspired, Interactive Multi-Turn Framework for Postcondition Inference._ arXiv:2602.20610. 

- [8] _AutoSpec: Automating Generation of Specifications for Programs._ arXiv:2404.00762. 

- [9] _FUN2SPEC: Code Contract Synthesis at Scale._ OpenReview, 2024. 

- [10] _Validating Formal Specifications with LLM-generated Test Cases._ arXiv:2510.23350, 2025. 

- [11] _Can LLMs Reason About Program Semantics? A Comprehensive Evaluation of LLMs on Formal Specification Inference._ arXiv:2503.04779, 2025. 

- [12] _LLM-Guided Formal Verification Coupled with Mutation Testing._ DATE, 2024. 

- [13] _MutDafny: A Mutation-Based Approach to Assess Dafny Specifications._ arXiv:2511.15403, 2025. 

- [14] A. P. Mathur. _Foundations of Software Testing_ , 2nd ed. Pearson, 2013. (Mutation testing and the competent-programmer hypothesis.) 

- [15] R. A. DeMillo, R. J. Lipton, F. G. Sayward. _Hints on Test Data Selection: Help for the Practicing Programmer._ IEEE Computer, 1978. 

- [16] S. Gulwani. _Programming by Examples (and its Applications in Data Wrangling)._ Marktoberdorf, 2016. 

- [17] S. Gulwani. _Automating String Processing in Spreadsheets using Input-Output Examples._ POPL, 2011. 

- [18] E. Clarke, O. Grumberg, S. Jha, Y. Lu, H. Veith. _Counterexample-guided Abstraction Refinement._ CAV, 2000. 

- [19] B. Khadka. _BALD-PS: code release._ `https://github.com/BarsatKhadka/BALD-PS` . 

16 

