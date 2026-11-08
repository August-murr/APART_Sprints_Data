# ¿Por qué los agentes obedecen La dirección de rechazo se debilita en formato agéntico

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Awards: Honorable Mention
- Team: Team RefusalLab
- Authors: Helen Stefany Penagos, Juan esteban Leiva
- Date / location: Jun 22, 2026 / Bogotá
- Page: https://apartresearch.com/sprints/projects/por-qu-los-agentes-obedecen-la-direccin-de-rechazo-se-debilita-en-formato-agntico-ux70
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/23a8679bba12f735-los-agentes-obedecen-La-direcci-n-de-rechazo-se-debilita-en-formato-ag-ntico.pdf
- Code: https://github.com/JEstebanBav/agentic-safety-probe.git
- Code links found in report: https://github.com/JEstebanBav/agentic-safety-probe.git

## Summary

Investigamos por qué los LLMs cumplen peticiones dañinas cuando operan como agentes con herramientas, algo que rechazan en formato chat. Usando interpretabilidad mecánica, medimos cómo la refusal direction (el mecanismo interno de rechazo) se comporta en formato agéntico. Encontramos que esta dirección se debilita significativamente cuando el modelo tiene herramientas disponibles, pero la información de dañosidad no desaparece sino que se recodifica en una dirección diferente del espacio de activaciones. Proponemos un safety monitor basado en esta nueva dirección como alternativa a los filtros por herramienta.

## Reviews (3)

### Review 1

This is a real mechanistic take on an important agent-safety failure mode.

The paired design is the strongest part: same prompt text, only chat vs tools/system context changes.

My biggest feedback would be validation: larger dataset, held-out probes, cross-validation, etc.

Also update the model framing, Llama 3.1 70B and Mistral 7B are useful open-weight substrates, but not current frontier models. There are better and newer models to do this.

### Review 2

Given that agentic harnesses have been seen to greatly improve performance, I think it is quite important to study how these harnesses impact safety considerations. It is interesting to study the claimed phenomenom of agents being less likely to refuse certain requests than base models. Presentation is also a lot easier to follow than many other projects in this event.

I can't confirm directly that claims like "Demostramos que la refusal direction, el mecanismo interno que media el rechazo de peticiones dañinas en LLMs, se debilita significativamente cuando el modelo opera en formato agéntico" were properly argued for given my time constraints. But it seems reasonable under a first look.

### Review 3

The study is dealing with a gap left by existing literature by testing whether the degradation of safety is about a failure of the agentic system to notice harm or that the harm just isn't being read because of its configuration to a chat trained system. It demonstrates the latter to establish that the new refusal direction is weaker and examines this in agentic systems. It would be very useful to have more work build upon this to test other models and correct for the possibility of overfitting through cross-validation. The method the study employs can also be replicated to see if it sufficiently addresses the difference in wording for agentic v chat prompts.

