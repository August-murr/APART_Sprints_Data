# AgroAid

- Sprint: Global South AI Safety Hackathon (global-south-ais-hackathon-2026-06-19-to-2026-06-21)
- Rank: unranked
- Team: Team Mariano
- Authors: Mariano Brizuela
- Date / location: Jun 22, 2026 / Buenos Aires
- Page: https://apartresearch.com/sprints/projects/agroaid-sg9i
- Report: https://pys8vc40ox3z7qxp.public.blob.vercel-storage.com/files/513816cb0f328e3e-a81b1c14-de0c-4f63-8d00-c3135b1fcb3a-AgroAid-Report.pdf
- Code: https://github.com/MarBL00126/AgroAid

## Summary

AgroAid is an AI Safety prototype designed to reduce potential harm caused by generative AI systems in Latin American agricultural contexts. The goal of the system is not to reemplace agronomists, health authorities or veterinaries, but rather to act as a preventive layer that identifies high-risk inquiries, retrieves technical evidence, detects missing information, formulates follow-up question and refrains when it cannot justify a safe recommendation.

## Reviews (3)

### Review 1

AgroAid aborda un problema real de seguridad de IA: las recomendaciones agrícolas dadas con exceso de confianza pueden generar riesgos para personas, animales, cultivos, fuentes de agua, seguridad alimentaria y entornos rurales. Su idea más fuerte es que una IA en este contexto no debería responder siempre, sino pedir información faltante, apoyarse en evidencia, abstenerse ante la incertidumbre y escalar los casos de alto riesgo a profesionales o autoridades competentes.

Sin embargo, en su forma actual, el proyecto se lee más como una aplicación agrícola con mecanismos de seguridad incorporados que como una contribución demostrada de AI Safety. El proyecto usa mecanismos valiosos, como recuperación de evidencia, abstención, preguntas de aclaración y escalamiento humano, pero debería precisar mejor cuál es su aporte distintivo frente a enfoques ya conocidos y qué parte de su propuesta puede generalizarse más allá de esta aplicación específica.

La ejecución también necesita fortalecerse. El sistema presenta una arquitectura coherente y ejemplos ilustrativos, y el propio equipo es honesto al reconocer que se trata de un prototipo y que la validación por expertos está pendiente. Sobre esa base, conviene ser claro en que la evaluación sigue siendo preliminar: se mencionan pruebas manuales, resultados esperados y métricas futuras, más que resultados efectivamente medidos. Una versión más robusta debería incluir un conjunto de consultas agrícolas peligrosas, medir la abstención correcta, identificar recomendaciones peligrosas no bloqueadas e incorporar validación experta.

En conjunto, AgroAid es un concepto prometedor de seguridad aplicada, pero todavía no una intervención de seguridad demostrada. Su siguiente paso debería ser pasar de una aplicación bien diseñada a un protocolo evaluado, con criterios medibles de abstención, validación experta y rutas claras de escalamiento.

### Review 2

The problem space this work enters is meaningful and the motivation is easy to understand, which gives the paper a reasonable starting point. That said, the contribution as presented remains at a level of generality that makes it difficult to assess what is genuinely new here. The core ideas are recognizable from existing applied AI safety literature, and the paper would benefit from a more precise articulation of what specifically distinguishes this approach and why those distinctions matter for the intended context.

The methodological grounding is the area that most needs development. The work would gain considerably from a more rigorous engagement with its own claims, since the current version relies on illustrative scenarios rather than evidence that allows the reader to evaluate the system's actual behavior under realistic or challenging conditions. A safety-oriented contribution in particular calls for that kind of scrutiny, and its absence leaves the central argument undersubstantiated. The writing also has room for improvement, with several inconsistencies and errors that a careful revision would address, and some sections that read more as outlines than developed arguments.

The research direction is worth pursuing, and there is a real opportunity here to build something of genuine value for the communities this work aims to serve. Moving forward, the priority should be deepening both the analytical precision and the empirical grounding, so that the contribution can stand on evidence rather than on the strength of the motivation alone. The conclusion gestures toward that potential, and it would be encouraging to see the rest of the paper meet it.

### Review 3

AgroAid is built around a genuinely important intuition—“a safe system sometimes says I don’t know”—and that’s a real strength you should keep, but the write‑up doesn’t yet give a reader enough to trust it in the kinds of situations you’re aiming at. The way you talk about risk levels, confidence, and “evidence verification” feels right in spirit, yet from the outside it’s hard to see how those judgments are actually made: what counts as “high risk,” how you decide evidence is sufficient, or what happens when documents and the model disagree. As a result, someone reading this who works in agriculture or safety would probably like the idea but still wonder, “Would this really catch the mistakes that scare me most?” One way to make it feel more solid and less like a concept sketch would be to narrow the scope to one or two really high‑stakes areas (for example, agrochemicals and electrical safety), show a couple of real interactions end‑to‑end (user question → retrieved docs → model reasoning → abstention or recommendation), and add even a tiny bit of counting: out of, say, 20 realistic risky questions, how many did AgroAid safely block, how many did it mishandle, and what patterns did you learn from that. That kind of concreteness would help your core message land with people on the ground: that this isn’t just another chatbot, but a layer that can actually keep farmers, animals, and water sources safer.

