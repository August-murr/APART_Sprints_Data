



**Autores:** Leonardo Párraga · Angie Giraldo · Víctor Gelves — AI Safety Colombia (AISCOL) 

**Con:** Apart Research 

## **Gobernanza de IA Militar mediante Control Humano por Diseño: el marco LIMAA–NRCH** 

_Una propuesta para prevenir la autonomía letal y garantizar la supervisión humana significativa en sistemas militares basados en IA._ 

# **Resumen** 

En Colombia, los grupos armados ilegales ya atacan con drones comerciales modificados y ya han herido y matado a civiles. Una pregunta decide cómo gobernar esta amenaza: ¿quién elige el blanco y aprieta el gatillo? Hoy, siempre un humano: con **ColDron** , un dataset abierto de 42 ataques documentados, mostramos que el 100% son drones operados por control remoto, sin autonomía. Pero esa situación está por cambiar, y no sólo por los grupos ilegales sino por la respuesta del Estado: un sistema antidrones de ~US$1.668 millones capaz de neutralizar blancos de forma automática, y la posible adquisición de _targeting_ con IA. La experiencia de Ucrania, Rusia e Irán muestra que la autonomía llega al conflicto armado mucho más rápido de lo que los marcos de gobernanza anticipan. Esa es la **ventana de prevención** : hay que fijar las reglas antes de que el salto ocurra. Aportamos tres herramientas, todas creaciones originales de este trabajo: ColDron (el dataset que documenta el daño y prueba la ausencia de autonomía); **LIMAA** (Lista Integral de Materiales de Autonomía del Arma; en inglés _Weapon-Autonomy Bill of Materials_ , WABOM), una “ficha técnica” legible por máquina del control humano de un arma, que un diagrama de flujo clasifica en un nivel de riesgo mediante el esquema **NRCH** (Niveles de Riesgo por Control Humano; en inglés _Human-Control Risk Tiering_ , HCRT); y un **protocolo de control humano significativo** para las operaciones militares colombianas, anclado en obligaciones vigentes (DIH, revisión del Artículo 36, Comunicado de Belén). El aporte transversal: llevar las herramientas técnicas de la seguridad de la IA al dominio de las armas autónomas letales (SAAL), desde un país donde el daño no es hipotético. 



# **1. Introducción** 

En Colombia, los grupos armados ilegales han incorporado drones comerciales modificados como arma, y ya hieren y matan civiles. El problema de gobernanza se reduce a una pregunta: ¿quién selecciona el blanco y ejecuta el ataque? De ella dependen el **control humano significativo** sobre el uso de la fuerza y la **rendición de cuentas** cuando hay daño civil. Hoy la respuesta es clara: siempre un humano. La amenaza, sin embargo, está a punto de transformarse, y de manera contraintuitiva: la autonomía no entrará al conflicto colombiano por los grupos ilegales primero, sino por la **respuesta del Estado** . Colombia adquirirá un Escudo Nacional Antidrones (~US$1.668 millones, en fase precontractual) capaz de neutralizar blancos de forma automática, y podría adquirir sistemas de _targeting_ asistidos por IA. Si estos sistemas operan sin supervisión humana adecuada sobre zonas pobladas, donde ocurren los ataques, el riesgo de daño civil masivo es alto. 

El modelo de fallo que abordamos es esta **transición de control remoto a autonomía (B→A)** , y la trayectoria global muestra que es rápida. Tras la invasión de Ucrania (febrero de 2022), las municiones merodeadoras entraron en ~7 meses, el FPV masivo en ~12–18 meses y la autonomía asistida por IA en ~2–3 años, empujada por la guerra electrónica: una vez que el dron va en modo autónomo, no se puede inhibir. Si bien hay varios casos en Colombia previos a 2024, este es el año en que se intensificó el uso de drones y hoy recorre la misma curva de otros conflictos (Figura 1). Esto abre una **ventana de prevención** : el momento de fijar reglas de control humano es ahora, antes del despliegue. 



_Figura 1. Colombia recorre hoy la misma curva que Ucrania/Rusia hace dos años: una vez que los drones entran a un conflicto, el salto a la autonomía es rápido y se acorta._ 

**Nuestras contribuciones principales son:** 



- **ColDron** , el primer dataset abierto y estructurado de ataques con dron en Colombia (39 incidentes, 34 campos), que documenta el daño civil y prueba empíricamente que el 100% de los ataques son operados por humanos, sin autonomía. 

- **LIMAA/NRCH** , un esquema legible por máquina (JSON Schema) que declara el control humano de un sistema de armas y lo clasifica, mediante un diagrama de flujo, en un nivel de riesgo con su acción de gobernanza asociada. 

- Un **Protocolo de Control Humano Significativo** de ocho cláusulas para las operaciones militares colombianas, anclado en obligaciones jurídicas vigentes, con líneas rojas explícitas frente al _targeting_ autónomo. 

# **2. Trabajo relacionado** 

El campo de la **seguridad de la IA** ( _AI safety_ ) se ha concentrado en la alineación, los modelos de frontera y la interpretabilidad; el **desarme** de armas autónomas vive en los foros de la Convención sobre Ciertas Armas Convencionales (CCW) y el Derecho Internacional Humanitario (DIH). Hasta donde sabemos, ningún esfuerzo conocido aplica el instrumental técnico de la seguridad de la IA a las armas autónomas letales (SAAL) desde un conflicto del Sur Global. Ahí situamos nuestra contribución. Nuestro marco extiende la lógica de “lista de materiales” ( _bill of materials_ ) de la gobernanza técnica de IA al dominio del control humano sobre armas letales, y la aterriza a operaciones reales. 

Las armas autónomas ya aparecieron en conflicto —el caso contestado del dron Kargu-2 en Libia en 2020, durante una guerra interna— [1]–[3] y el _targeting_ masivo con IA también (los sistemas _Lavender_ y _Gospel_ en Gaza), pero siempre como sistemas de actores estatales o respaldados por Estados. Colombia podría convertirse en uno de los primeros conflictos armados internos donde **grupos no estatales** desplieguen autonomía. Ese vector de proliferación no es hipotético: existe un canal documentado y ya adjudicado en cortes de EE.UU. —la condena en marzo de 2026 de un traficante por intercambiar armas del régimen sirio de Assad por cocaína del ELN— [4], [5] y un nexo histórico, documentado por la DEA, entre Hezbolá (proxy de Irán) y las disidencias de las FARC, con el nodo Venezuela como punto de tránsito de tecnología iraní y rusa [6]–[8]. Hoy ese canal mueve armamento convencional, no drones; pero prueba que el canal hacia la industria armamentista iraní —que produce y exporta la munición merodeadora Shahed— existe y está documentado. 

Más preocupante aún es un **segundo vector de proliferación: el conocimiento** . Colombia es el mayor contingente extranjero de combatientes en la guerra de Ucrania [9] —miles de excombatientes, en parte desempleados tras el acuerdo de paz de 2016—, y existe una línea de investigación, recogida por la prensa colombiana, sobre el viaje de miembros de grupos ilegales (ELN, disidencias de las FARC, Clan del Golfo) a servir como mercenarios para adquirir experiencia real de combate con drones FPV y guerra electrónica, y regresar con ese conocimiento. En 2025, el vicepresidente del Consejo de Seguridad ruso, Dmitri Medvédev, señaló específicamente al Clan del Golfo y a una empresa de seguridad de Medellín como reclutadora, y la inteligencia ucraniana detectó voluntarios latinoamericanos con un interés desproporcionado en los módulos de drones [11]. Este vector es más alarmante que el del armamento, porque no transfiere una herramienta sino la **capacidad de construir y operar** sistemas cada vez más autónomos. Y ya tiene una 



implementación doméstica: la inteligencia militar ha rastreado **escuelas clandestinas** de pilotaje (en el Catatumbo y en la frontera venezolana) donde, según los reportes, se instruye en enjambres de drones con coordinación asistida por IA y mecanismos de liberación de carga impresos en 3D, reclutando incluso a menores [10]. La transición hacia la autonomía no es solo una hipótesis importada: se está construyendo activamente en el territorio. 

# **3. Métodos** 

**ColDron.** Construimos un dataset abierto a partir de fuentes públicas (prensa nacional y local, reportes oficiales del Ministerio de Defensa, comunicados de la ONU/OCHA y el CICR). Cada incidente se codifica en 34 campos: fecha, ubicación (con coordenadas), perpetrador, clase de blanco, víctimas (civiles y militares, muertos y heridos), y los campos de autonomía de LIMAA. Adoptamos una **codificación conservadora** : ante ambigüedad o conflicto entre fuentes, se asigna la categoría más cauta y el caso se envía a una cola de revisión. 

**Verificación de fuentes.** Como el dataset se construye sobre reportes de prensa, su fiabilidad depende de la verificación de las fuentes. Aplicamos un protocolo de tres pasos: (i) **Triangulación** : Cada incidente requiere al menos dos fuentes independientes que confirmen el hecho—; (ii) **Jerarquía de credibilidad** : Se priorizan agencias de noticias y fuentes oficiales sobre prensa nacional, y esta sobre prensa local o redes sociales; y (iii) **Contraste con agregados oficiales:** Las cifras de magnitud y tendencia se anclan en registros de la ONU/OCHA, el CICR y el Ministerio de Defensa [12]–[14], no en la prensa. La confiabilidad inter-codificador de los campos de juicio (p. ej., la clase de blanco) se evalúa con el coeficiente κ de Cohen. Sobre los 34 incidentes codificados de forma independiente por dos investigadores, obtuvimos κ = 0,70 (concordancia simple: 79%), calificado como _sustancial_ según la escala de Landis y Koch (1977). 

**LIMAA (Lista Integral de Materiales de Autonomía del Arma) — creación original de este trabajo.** Es un manifiesto legible por máquina que declara, en doce campos, el grado de control humano de un sistema de armas (autonomía del _targeting_ , humano en el bucle, capacidad de distinción, anulación humana, registro de decisiones, revisión del Artículo 36, etc.). El conjunto de campos, sus valores y su semántica son de nuestra autoría; los expresamos en **JSON Schema** el estándar abierto de validación (draft 2020-12) para que cualquier validador estándar pueda comprobar un manifiesto de forma automática. 

**NRCH (Niveles de Riesgo por Control Humano).** Una regla simple representada como el diagrama de flujo de la Figura 5 lee el manifiesto LIMAA y asigna un nivel de riesgo, cada uno con su acción de gobernanza anclada en marcos convenidos: **T0** (prohibición, como el enfoque de “prohibir” de la CCW), **T1** (regulación estricta y revisión reforzada del Artículo 36), **T2** (uso bajo controles y condiciones de despliegue) y **T3** (línea base, donde aplica el DIH ordinario). 

**Protocolo.** Derivamos un protocolo operacional de ocho cláusulas, anclado en obligaciones que Colombia ya tiene (DIH; la revisión de armas del Artículo 36 del Protocolo Adicional I [28]; el Comunicado de Belén de 2023 [26]), con una matriz tarea × efector × entorno para el caso defensivo y líneas rojas frente al _targeting_ autónomo. 



# **4. Resultados** 

**ColDron: el daño es real y aún no hay autonomía.** De 39 incidentes, 32 son ataques confirmados (más un ataque fallido). Su composición por clase de blanco muestra predominio civil (12) y militar (11), con infraestructura (6) y mixto (6) en proporciones similares (Figura 2). El hallazgo central de gobernanza: **el 100% de los ataques son** **`operados remotamente` con un humano en el bucle** (ninguno selecciona o ataca blancos por sí mismo—; en el esquema NRCH, todos caen en T3. Es la evidencia de que la ventana de prevención sigue abierta. Una salvedad honesta: señales recientes escuelas clandestinas que, según la inteligencia militar, entrenan en enjambres con coordinación asistida por IA [10] indican que esa frontera se acerca. Hay que separar la **coordinación de enjambre** (sincronizar varios drones) de la **autonomía en la selección del blanco** (que un sistema elija y ataque por sí mismo), que es lo que ColDron mide y que sigue siendo humana. 



_Figura 2. Composición de los 32 ataques por clase de blanco._ 



**La escalada documentada.** ColDron caracteriza la _naturaleza_ del daño; su _magnitud_ proviene de registros oficiales y de la ONU [12]–[15], que documentan una escalada inequívoca: los incidentes con artefactos explosivos improvisados —drones incluidos— pasaron de 167 (2024) a 414 (2025), y las víctimas civiles de explosivos aumentaron 145% en ese período, con un alza del 342% en las causadas por artefactos lanzados y tres de cada cuatro víctimas civiles (Figura 3). Además, detectamos un fuerte **subregistro oficial del daño civil** : la mayoría de los ataques con víctimas civiles documentados por prensa no figuran en los conteos oficiales como eventos civiles, lo que tiene implicaciones directas para cómo se evaluará el desempeño del Escudo Antidrones. 



_Figura 3. La escalada del daño con drones en Colombia (2024–2025), según registros oficiales y de la ONU._ 

La intensidad es implacable: un informe de inteligencia citado por _El Tiempo_ [16] establece, a partir de la intensificación del conflicto, una frecuencia promedio de **un ataque con dron cada 28 horas** (un día y cuatro horas) y, en promedio, **tres artefactos explosivos lanzados con drones cada dos días** (Figura 4). 





_Figura 4. El ritmo de los ataques con dron, según un informe de inteligencia citado por El Tiempo._ 

**LIMAA/NRCH discrimina y es reproducible.** El esquema valida contra el meta-esquema estándar, y cuatro manifiestos de ejemplo se clasifican correctamente en los cuatro niveles (de T0 a T3). El árbol de decisión (Figura 5) convierte el esquema en una herramienta usable: tres preguntas sobre el control humano bastan para clasificar cualquier sistema, e incorpora la mitigación clave del antidrón (un sistema de selección autónoma pasa de prohibido, T0, a moderado, T2, si tiene salvaguardas: efector no letal o geocerca, anulación humana y trazabilidad). 



_Figura 5. El árbol de decisión de LIMAA–NRCH: tres preguntas clasifican cualquier sistema en un nivel de riesgo, cada uno con su acción de gobernanza._ 

**Protocolo.** Las ocho cláusulas operacionalizan el control humano significativo: verificación humana individualizada del blanco, prohibición de listas de objetivos autónomas y de tuberías objetivo-ataque automáticas, anulación humana siempre disponible, trazabilidad completa, y condiciones de despliegue por entorno. La matriz tarea × efector × entorno permite distinguir usos defensivos aceptables de los inaceptables. 



# **5. Discusión y limitaciones** 

**Implicaciones para la seguridad de la IA: los dos vectores del Estado.** El riesgo inmediato no viene de robots asesinos, sino de cómo el Estado responda. **Vector A (antidrón):** aun siendo defensivo, un sistema que neutraliza de forma automática puede causar daño civil por mala clasificación o por los efectos de la neutralización sobre población. **Vector B (** **_targeting_ con IA):** en Gaza, _Lavender_ marcó personas para una lista de muerte y _Gospel_ marcó edificios; lo catastrófico no fue la IA sino su uso —error reconocido de ~10%, revisión humana de ~20 segundos, ratios de daño colateral preautorizadas—. 

**La presión por resultados es un multiplicador de daño civil, y Colombia ya vivió su versión más atroz.** Entre 2002 y 2008, la presión institucional por mostrar bajas produjo los “falsos positivos”: al menos 6.402 civiles asesinados y presentados como muertos en combate, según la Jurisdicción Especial para la Paz (JEP) [17], [18], que concluyó que el crimen no habría ocurrido sin la política de “conteo de cuerpos”. El _targeting_ con IA automatiza ese peligro a velocidad de máquina. Y el contexto lo acerca: el presidente electo (que se posesiona en agosto de 2026) ha planteado retomar bombardeos, “afinar” la inteligencia militar, adquirir tecnología de vigilancia, drones e IA en cooperación con EE.UU. e Israel, y eliminar la JEP —el mecanismo que documentó los falsos positivos—. Es un análisis de riesgo sobre posturas declaradas, no una predicción; pero refuerza por qué la ventana de prevención es ahora. 

**Un fenómeno del Sur Global, no del Norte.** La misma dinámica —drones improvisados en conflictos internos, dentro de zonas pobladas, con vacíos de rendición de cuentas— aparece en Sudán, Myanmar, el Sahel y México. **Haití** es el caso más alarmante y el espejo de nuestra advertencia: desde marzo de 2025, fuerzas haitianas y contratistas privados usan drones kamikaze sobre Puerto Príncipe [20], [21]; según Human Rights Watch [19], mataron al menos 1.243 personas (60 civiles, 17 niños) en ataques aparentemente ilegales y sin control. El debate del Norte gira en torno a la guerra interestatal y se rige por controles de exportación. El Sur enfrenta otra cosa: grupos armados no estatales, zonas urbanas, armas improvisadas, y vacíos de accountability que los mecanismos existentes no cubren. Las respuestas tienen que salir de ese contexto, no importarse. 

## **Ruta de adopción e interoperabilidad** 

Una herramienta de gobernanza que nadie puede adoptar no sirve. Por eso el diseño de LIMAA/NRCH priorizó la interoperabilidad con los marcos existentes. La ruta de adopción es concreta: el **Ministerio de Defensa** incorpora la revisión del Artículo 36, con un manifiesto LIMAA, como requisito en la adquisición del Escudo y de cualquier sistema de _targeting_ con IA; el **Congreso** y la **Defensoría del Pueblo** adoptan el protocolo de control humano como directiva y mecanismo de supervisión, en línea con la política nacional de IA (CONPES 4144) [27]. El resultado concreto: el control humano queda fijado antes del despliegue, verificable por diseño, no por declaración. Lo que se evita es el desenlace que Haití ya muestra. Y LIMAA/NRCH no reinventa el marco existente: lo complementa y lo vuelve operacional y legible por máquina (Tabla 1). 



_Tabla 1. Cómo LIMAA/NRCH complementa los instrumentos de gobernanza existentes._ 

|Instrumento existente|Qué cubre|Qué aporta<br>LIMAA/NRCH|
|---|---|---|
|Directiva 3000.09<br>(Dpto. de Defensa de<br>EE.UU.) [22]|Revisión de alto nivel<br>para sistemas con<br>autonomía, solo para<br>fuerzas estatales de<br>EE.UU.|Lo vuelve legible por<br>máquina y aplicable a<br>adquisiciones de<br>cualquier Estado<br>—incluido el Sur<br>Global— y a la<br>evaluación de sistemas<br>no estatales|
|Ley de IA de la UE<br>(niveles de riesgo) [23]|Clasifica los sistemas<br>de IA por riesgo, pero<br>excluye explícitamente<br>los usos militares|Traslada la lógica de<br>niveles de riesgo al<br>dominio de las armas<br>autónomas que la UE<br>deja fuera|
|Declaración Política<br>sobre uso militar<br>responsable de la IA<br>(2023) [24]|Principios voluntarios<br>(control humano,<br>revisiones jurídicas),<br>sin mecanismo<br>operacional|Convierte esos<br>principios en un<br>manifiesto verificable y<br>un protocolo<br>operacional|
|Enfoque de dos niveles<br>de la CCW (prohibir /<br>regular) [25]|Debate diplomático<br>sobre prohibir o<br>regular las SAAL, sin<br>criterio técnico para<br>clasificar un sistema|Aporta el criterio<br>operacional (el árbol de<br>decisión) que mapea<br>un sistema a “prohibir”<br>(T0) o “regular”<br>(T1–T3)|
|Revisión del Artículo<br>36 (Protocolo Adicional<br>I) [28]|Obliga a revisar la<br>legalidad de armas<br>nuevas, sin un formato<br>estándar|Provee el formato<br>estructurado y legible<br>por máquina para esa<br>revisión|



## **Limitaciones** 

ColDron no es exhaustivo: tiene un **sesgo de selección** (depende de la cobertura de prensa, concentrada particularmente en 2025) y por eso no puede sostener por sí solo una tendencia temporal del daño civil. Por ello anclemos la magnitud en fuentes oficiales—. El nivel NRCH del dataset es **degenerado** (todos T3), porque aún no hay autonomía; esto es, de hecho, nuestro hallazgo, pero impide demostrar la discriminación del esquema con datos reales (la demostramos con manifiestos de ejemplo). La confiabilidad inter-codificador es κ = 0,70 ( _sustancial_ ), calculado sobre los 33 incidentes de la doble codificación; las 7 discordancias se concentran en casos limítrofes entre categorías (mixto/civil y mixto/militar), lo que señala una zona de ambigüedad conceptual a refinar 



en versiones futuras. Hay incertidumbre por incidente en algunas cifras de víctimas. El análisis del contexto político es prospectivo y se basa en posturas declaradas. 

## **Trabajo futuro** 

Conectar ColDron con fuentes estructuradas (ACLED) para ampliar y validar la cobertura; extender el marco a otros conflictos internos del Sur Global; y articular con una pieza complementaria sobre **ciberresiliencia** de los sistemas autónomos del Estado (la posibilidad de que un actor malicioso comprometa el antidrón o el _targeting_ y lo vuelva contra civiles). 

# **6. Conclusión** 

El daño a civiles derivado de drones ya ocurre, pero la autonomía letal todavía no llega al conflicto colombiano. Esta es una ventana de oportunidad, y es estrecha: la trayectoria global muestra la rapidez con que puede ocurrir, y la propia respuesta del Estado puede cerrarla si adquiere sistemas autónomos sin fijar antes las reglas. ColDron demuestra que la ventana sigue abierta; LIMAA/NRCH y el protocolo dan los instrumentos para usarla. El momento para actuar e influir en diferentes elementos de la gobernanza de SAAL es antes del despliegue del Escudo Anti-drones, no después. Además, este es un modelo transferible: la misma transición ocurre hoy en otros conflictos del Sur Global y las soluciones planteadas acá pueden implementarse en otros territorios como Haití y 

# **Código y datos** 

- **Repositorio de código:** _<u>[https://github.com/manueloff14/coldrone]</u>_ — incluye el esquema `wabom.schema` , los manifiestos de ejemplo, la implementación de referencia del _tiering_ (./framework/ `hcrt_tier.py` ) 

- **Datos:** ColDron ( `./public/coldron_seed.csv` ), publicado bajo licencia abierta. 

- **Mapa interactivo:** <u>`https://coldrone.onrender.com/`</u> — georreferencia los 34 ataques de ColDron (color por clase de blanco, tamaño por número de víctimas), con detalle por incidente. 

# **Contribuciones de los autores** 

_Los autores contribuyeron conjuntamente al diseño del proyecto, la construcción de ColDron, el desarrollo del marco LIMAA–NRCH, la redacción del informe y la creación de un observatorio de datos ColDron de los ataques de drones en Colombia._ 

# **Referencias** 

[1] Consejo de Seguridad de las Naciones Unidas, “Informe final del Grupo de Expertos sobre Libia establecido en virtud de la resolución 1973 (2011),” Naciones Unidas, Rep. S/2021/229, 2021. 

[2] Z. Kallenborn, “Was a flying killer robot used in Libya? Quite possibly,” _Bulletin of the Atomic Scientists_ , 2021. 



[3] Lieber Institute West Point, “El informe de la ONU sobre Libia y los sistemas de armas autónomas,” _Articles of War_ , United States Military Academy, 2021. 

[4] Cambio, “El régimen sirio envió armas y dinero a grupos terroristas colombianos,” _Cambio_ , 2026. 

[5] “Inside the trans-Atlantic trade in Iranian weapons for Colombian coke,” _The Wall Street Journal_ , 2026. 

[6] Drug Enforcement Administration, “Operación Titán y Proyecto Cassandra,” DEA. 

[7] Atlantic Council, “The Maduro–Hezbollah nexus,” Atlantic Council. 

[8] U.S. Department of the Treasury, “Sanciones al comercio de armas entre Irán y Venezuela,” U.S. Dept. of the Treasury, 2025. 

[9] “Criminales estarían reclutando mercenarios colombianos que vienen de la guerra en Ucrania para usar drones con fines terroristas,” _El Colombiano_ , Mar. 11, 2026. [Online]. Available: 

https://www.elcolombiano.com/colombia/disidencias-drones-mercenarios-ucrania-HA34 525112 

[10] “Drones en Colombia: el auge de escuelas clandestinas de grupos armados,” _KCH FM_ , Apr. 5, 2026. [Online]. Available: https://kchcomunicacion.com/2026/04/05/drones-en-colombia-el-auge-de-escuelas-clan destinas-de-grupos-armados/ 

[11] “Narcos mexicanos y colombianos buscan en Ucrania entrenamiento con drones y táctica de guerra,” _Politico_ , Mar. 28, 2026. [Online]. Available: https://politico.mx/2026/03/28/narcos-mexicanos-y-colombianos-buscan-en-ucrania-ent renamiento-con-drones-y-tactica-de-guerra/ 

[12] Oficina de Coordinación de Asuntos Humanitarios (OCHA), “Colombia: afectación de la población civil por artefactos explosivos, 2024–2025,” ONU OCHA, 2025. 

[13] Comité Internacional de la Cruz Roja, “Afectación de civiles por artefactos explosivos lanzados con drones en Colombia,” CICR, 2025. 

[14] Ministerio de Defensa Nacional, “Cifras de ataques con dron y artefactos explosivos en Colombia,” MinDefensa, 2025. 

[15] Human Rights Watch, “Informe mundial 2026,” Human Rights Watch, 2026. 

[16] “Informe de inteligencia: frecuencia de los ataques con dron en Colombia,” _El Tiempo_ , 2025. 

[17] Jurisdicción Especial para la Paz, “Auto No. 033 de 2021. Caso 03: muertes ilegítimamente presentadas como bajas en combate por agentes del Estado,” JEP, 2021. 



[18] Comisión de la Verdad, “Hay futuro si hay verdad: Informe final,” Comisión para el Esclarecimiento de la Verdad, la Convivencia y la No Repetición, 2022. 

[19] Human Rights Watch, “Haiti: Drone strikes put residents at risk,” Human Rights Watch, 2026. 

[20] R. Muggah, “Puerto Príncipe como laboratorio del uso de drones armados,” Igarapé Institute, 2026. 

[21] International Crisis Group, “Haití: la violencia de las pandillas y el uso de drones armados,” ICG, 2026. 

[22] U.S. Department of Defense, “Autonomy in weapon systems,” DoD Directive 3000.09, 2023. 

[23] Parlamento Europeo y Consejo de la Unión Europea, “Reglamento (UE) 2024/1689 por el que se establecen normas armonizadas en materia de inteligencia artificial (Ley de Inteligencia Artificial),” Diario Oficial de la Unión Europea, 2024. 

[24] U.S. Department of State, “Political declaration on responsible military use of artificial intelligence and autonomy,” U.S. Dept. of State, 2023. 

[25] Grupo de Expertos Gubernamentales sobre Sistemas de Armas Autónomas Letales, “Informe del Grupo de Expertos Gubernamentales,” Convención sobre Ciertas Armas Convencionales, Naciones Unidas, 2023. 

[26] “Comunicado de Belén: Conferencia regional de América Latina y el Caribe sobre el impacto social y humanitario de las armas autónomas,” San José, Costa Rica, 2023. 

[27] Departamento Nacional de Planeación, “Documento CONPES 4144: Política nacional de inteligencia artificial,” DNP, 2025. 

[28] Protocolo Adicional I a los Convenios de Ginebra de 1949 relativo a la protección de las víctimas de los conflictos armados internacionales, Artículo 36, 1977. 

**Apéndice A — Especificación LIMAA y demostración del** **_tiering_** 

LIMAA es una contribución original de este trabajo: el conjunto de campos, sus valores y su semántica —y el concepto mismo de una “lista integral de materiales de autonomía del arma”— son de nuestra autoría. Lo expresamos en JSON Schema, el estándar abierto de validación (draft 2020-12); verificamos que el esquema conforma al meta-esquema del estándar y que los cuatro manifiestos de ejemplo validan contra él. 

**Campos del manifiesto:** `manifest_version` , `system_name` , `operator_class` , `operational_role` , `targeting_autonomy` , `human_in_loop` , `distinction_capability` , `effector_type` , `engagement_environment_constraint` , `human_override` , `decision_logging` , `article36_review` . 

**Demostración del tiering** (la versión visual es la Figura 5): 



|#|Sistema<br>(ejemplo)|targeting ·<br>humano · efector|Nivel|
|---|---|---|---|
|1|Antidrón sin<br>salvaguardas|autónomo ·<br>ninguno ·<br>cinético|**T0**|
|2|Munición<br>merodeadora|autónomo ·<br>parcial · cinético|**T1**|
|3|Antidrón con<br>salvaguardas|autónomo ·<br>ninguno · no<br>letal + geocerca<br>+ anulación|**T2**|
|4|Dron FPV ilegal|remoto ·<br>completo ·<br>cinético|**T3**|



El par T0→T2 (filas 1 y 3) es la prueba de que el esquema premia las salvaguardas: el mismo sistema autónomo baja de “prohibido” a “moderado” cuando incorpora efector no letal o geocerca, anulación humana y trazabilidad. 

# **Apéndice B — Resumen de política (para tomadores de decisión)** 

**Dirigido a:** Ministerio de Defensa, Congreso de la República y entidades a cargo del Escudo Nacional Antidrones. 

**El problema en una frase.** Los grupos ilegales atacan con drones operados por humanos y ya matan civiles; la autonomía aún no llega, pero la trayectoria global muestra que llega rápido, y la respuesta del Estado (el Escudo y posibles sistemas de _targeting_ con IA) la introducirá sin un marco público de control humano. 

**La oportunidad.** El Escudo está en fase precontractual: es el momento de fijar el control humano por diseño antes de desplegar. 

**Cuatro acciones inmediatas:** (1) aplicar la revisión del Artículo 36 a los modos autónomos del Escudo y a cualquier _targeting_ con IA, antes de adquirirlos; (2) incorporar condiciones contractuales de control-humano-por-diseño, auditabilidad y pruebas de protección civil; (3) adoptar el protocolo de ocho cláusulas como directiva, con líneas rojas explícitas; (4) establecer supervisión independiente y trazabilidad para cerrar la brecha de responsabilidad. 

**El costo de no actuar.** Haití muestra el desenlace de desplegar drones letales en zonas pobladas sin control ni rendición de cuentas: más de 1.200 muertos, decenas de civiles y niños, en ataques calificados de ilegales. Colombia está a tiempo de no repetirlo. 



# **Declaración de uso de LLM** 

Usamos Claude Opus 4.8 (Anthropic) como apoyo para la investigación y verificación de fuentes, la estructuración del informe, la generación de figuras y la implementación del esquema LIMAA y del código de _tiering_ . Todas las afirmaciones, cifras y resultados fueron verificados de forma independiente por el equipo. La versión final del informe fue revisada y editada por los autores. 

