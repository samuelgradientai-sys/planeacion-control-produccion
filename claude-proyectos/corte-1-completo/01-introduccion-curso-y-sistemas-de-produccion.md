<!-- fuente: corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/README.md -->
# Introducción al curso y sistemas de producción (Corte 1)

## Qué cubre
Es la primera semana del curso **Planeación, Programación y Control de las Operaciones (PPCO)**, Universidad de La Sabana, 2026, con el prof. William Guerrero. Incluye:

- La presentación del curso: objetivo, resultados ABET, rúbrica, plan de estudios, reglas, evaluación y proyectos.
- Qué es la gestión de operaciones (*Operations Management*) y qué hace un gerente de operaciones.
- Las configuraciones de los sistemas de producción (flowshop, jobshop y openshop), sus medidas de desempeño y las estrategias de control de piso (push, pull, Kanban y ConWIP).
- La tarea 1: un ensayo que compara ofertas laborales de LinkedIn.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [L01-introduccion-al-curso.md](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L01-introduccion-al-curso.md) | Lecture 1 (46 diapositivas). **Programa del curso**: profesor, objetivo, ABET, rúbrica, plan de estudios de Ingeniería Industrial, reglas, **porcentajes de evaluación**, proyectos en grupo, qué es OM, las 10 decisiones estratégicas, un ejemplo numérico de estrategias y la tarea 1. Al inicio del resumen hay una ficha rápida del curso. | **Sí, primero** (reglas y evaluación del curso) |
| [L02-introduction-to-production-systems.md](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L02-introduction-to-production-systems.md) | Lecture 2 (22 diapositivas, hechas con Gamma). Reglas de debate, lectura recomendada (*Factory Physics*, cap. 1), flowshop, jobshop y openshop, WIP, *takt time*, *throughput*, *cycle time*, *lead time*, push vs. pull, Kanban y ConWIP. | Segundo |
| [tarea-ensayo-linkedin-operations-manager.md](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/tarea-ensayo-linkedin-operations-manager.md) | Entrega de la Homework 1 (Word): compara la oferta de Operations Manager de Lean Solutions Group (Barranquilla, BPO) con la de Subgerente de Operaciones de Falabella (Bogotá, retail) y elige la primera. | Opcional |

## Orden de estudio sugerido
1. **L01, páginas 1–24:** cómo funciona el curso. Las reglas están en la p. 9, las notas en la p. 22, los grupos en la p. 23, los proyectos en la p. 24 y la rúbrica en la p. 6.
2. **L01, páginas 25–46:** qué es OM, las 10 decisiones estratégicas y el ejemplo de la p. 41. Termina con la tarea 1 (p. 44).
3. **Tarea:** el ensayo de LinkedIn, como ejemplo de entrega.
4. **L02:** configuraciones de producción y control de piso. Es el vocabulario base que se retoma en el corte 3 (scheduling).

## Conceptos y fórmulas clave

- **Evaluación del curso** (detalle en [L01, p. 22](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L01-introduccion-al-curso.md)):
  - Pesos de los cortes: corte 1 = 30 %, corte 2 = 30 %, corte 3 = 40 %.
  - Dentro de cada corte: examen 60 %, actividades en clase 10 %, proyecto 30 %. En el corte 3 el examen es final acumulativo.
  - Sobre la nota final: exámenes 60 %, actividades 10 %, proyectos 30 %.
- **Reglas** ([L01, p. 9](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L01-introduccion-al-curso.md)): asistir a clase (20 %), fechas de entrega inamovibles, aprendizaje basado en la experiencia, plagio prohibido y citación obligatoria. Los proyectos se hacen en grupos de hasta 5 personas, con vestimenta profesional en las presentaciones.
- **Ejemplo de estrategias** ([L01, p. 41](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L01-introduccion-al-curso.md), Heizer et al. 2017):

  $$\text{Utilidad} = (1-t)\,\big[(V - C_p) - C_f\big]$$

  donde $V$ son las ventas, $C_p$ el costo de producción, $C_f$ el costo financiero y $t=0.25$ la tasa de impuestos. Reducir $C_p$ un 20 % da una utilidad de 22,500, frente a 18,000 al subir las ventas un 50 % y 12,750 al bajar $C_f$ un 50 %. La utilidad actual es 10,500.
- **Configuraciones** ([L02](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L02-introduction-to-production-systems.md)):
  - **Flowshop:** ruta fija e igual para todos los productos; alto volumen y estandarización.
  - **Jobshop:** cada producto tiene su propia ruta; flexible, con programación compleja.
  - **Openshop:** la ruta no es estricta; muy variable.
- **Medidas de desempeño** (L02, p. 8–9): WIP, *takt time*, *throughput*, *cycle time*, *lead time* y eficiencia. En L02 solo se definen con palabras. Como complemento estándar que **no** está en las diapositivas: la ley de Little $WIP = TH \times CT$ y $\text{Takt} = \frac{\text{tiempo disponible}}{\text{demanda}}$.
- **Control de piso** (L02, p. 14–22):
  - **Push:** produce según un plan o pronóstico.
  - **Pull:** produce según la demanda real.
  - **Kanban:** una tarjeta por etapa.
  - **ConWIP:** una tarjeta para toda la línea, lo que limita el WIP total.

## Ejercicios resueltos disponibles

| Ejercicio | Archivo | Resultado principal |
|---|---|---|
| Comparación de estrategias de mercadeo, finanzas y operaciones (estado de resultados) | [L01, p. 41](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L01-introduccion-al-curso.md) | La estrategia de operaciones (−20 % en costos) da la mayor utilidad: 22,500 |
| Cálculo del peso efectivo de cada componente en la nota final | [L01, p. 22](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L01-introduccion-al-curso.md) | Exámenes 60 %, actividades 10 %, proyectos 30 % |
| Homework 1: análisis de dos ofertas laborales de LinkedIn | [tarea-ensayo-linkedin-operations-manager.md](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/tarea-ensayo-linkedin-operations-manager.md) | Se elige Operations Manager en Lean Solutions Group |
| Rutas de producción (ejemplo de jobshop con 3 referencias y 3 estaciones) | [L02, p. 5](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L02-introduction-to-production-systems.md) | Ref 1: A→C; ref 2: B→A→C; ref 3: C→A→B |

## Relación con otros temas y proyectos

- **Pronósticos** (meta 1 del semestre: «Forecast sales»):
  - Siguiente carpeta: [02-introduccion-a-pronosticos](/corte-1-pronosticos/02-introduccion-a-pronosticos/).
  - Luego el resto del corte 1, hasta el [parcial 1](/corte-1-pronosticos/parcial-1/) y el [proyecto THYMS de pronóstico](/corte-1-pronosticos/proyecto-thyms-pronostico/).
- **Planeación** (criterio 3 de la rúbrica, «plan estratégico»; lógica push basada en pronósticos):
  - [Corte 2 — planeación agregada](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/)
  - [BOM y MRP](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/)
  - [MRP II](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/)
- **Programación de la producción** (criterio 4 de la rúbrica; decisión estratégica 9; configuraciones de L02):
  - [Corte 3 — introducción a scheduling](/corte-3-programacion-scheduling/01-introduccion-scheduling/)
  - [flow shop](/corte-3-programacion-scheduling/04-flow-shop/)
  - [job shop](/corte-3-programacion-scheduling/05-job-shop/)
  - [competencia de scheduling](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/)


---

<!-- fuente: corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L01-introduccion-al-curso.md -->
# L01-introduccion-al-curso

> **Archivo:** [`L01-introduccion-al-curso.pdf`](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L01-introduccion-al-curso.pdf) · **Corte 1** · 46 páginas  
> **Nombre original:** `CORTE 1/Lec 1.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** presentación del curso *Planning, Scheduling and Controlling Operations* (Planeación, Programación y Control de las Operaciones, PPCO), semestre 2026, y primera clase sobre qué es la gestión de operaciones (*Operations Management*, OM).

### Ficha del curso (referencia rápida)

| Dato | Valor | Página |
|---|---|---|
| Nombre | Planning, Scheduling and Controlling Operations / Operations Management (asignatura «Planeación, Programación y Control de las Operaciones») | 1, 4 |
| Universidad | Universidad de La Sabana, Facultad de Ingeniería, programa de Ingeniería Industrial | 7 |
| Semestre | 2026 (en el plan de estudios la asignatura está en el **7.º semestre**, con **4 créditos**) | 1, 7 |
| Profesor | William Guerrero, Ph.D. («Mr. Guerrero»): ingeniero industrial, magíster en Ingeniería Industrial, PhD en Optimización y Confiabilidad de Sistemas Industriales (UTT, Francia), PhD en Ingeniería (UniAndes, Bogotá), profesor asociado | 2 |
| Correo | William.guerrero1@unisabana.edu.co | 2 |
| Prerrequisito (según el plan de estudios) | Ecuaciones Diferenciales | 7 |
| Asignaturas que la tienen de prerrequisito | Transformación Digital y Sistemas de Información; Diseño y Gestión de Cadena de Suministro (junto con Fundamentos de Logística) — 8.º semestre | 7 |
| Lema | *If you don't know where you are going, any road will get you there* | 1, 46 |

### Objetivo y resultados de aprendizaje

- **Objetivo del curso (p. 3):** desarrollar temas de gestión de los procesos productivos en las organizaciones, con un enfoque gerencial de las operaciones que apoye la toma de decisiones mediante herramientas y técnicas avanzadas.
- **Resultados ABET (p. 4).** Competencia: «Resolución de Problemas». Dos indicadores específicos:
  1. Plantear soluciones a problemas de gestión de sistemas productivos con TI y herramientas de la industria 4.0. Indicador transversal: evalúa alternativas de solución.
  2. Identificar el comportamiento de los datos históricos de la demanda y elegir la metodología adecuada para pronosticarla. Indicador transversal: identifica los elementos del problema y las herramientas para resolverlo.
- **Indicadores de desempeño (p. 5):** SO1.PI_1, SO1.PI_3, SO1.PI_4 (resolver problemas), SO2.PI_1 y SO2.PI_5 (diseñar soluciones y sistemas de producción y logística), SO3.PI_1, SO3.PI_2 y SO3.PI_7 (comunicación oral, escrita en español y en inglés).
- **Rúbrica (p. 6).** Cuatro criterios, cada uno con cuatro niveles: Excelente 100 %, Bueno 80 %, Aceptable 50 % y Deficiente 25 %.
  1. Análisis gráfico de pronósticos.
  2. Evaluación crítica de los pronósticos: análisis de errores y elección del método más preciso.
  3. Propuesta de plan estratégico.
  4. Evaluación del sistema de programación.
  - Los criterios 1–2 corresponden al corte 1 (pronósticos), el 3 a la planeación del corte 2 y el 4 al *scheduling* del corte 3 (relación deducida).
- **Metas del semestre (p. 7–8):** el estudiante ya sabe programar, hacer matemáticas, analizar datos y sistemas de trabajo, entender lo básico de la gestión empresarial, y optimizar y simular. Al final del semestre debe saber **pronosticar ventas** y **optimizar operaciones** para «crear valor» en las empresas.

### Evaluación (p. 22)

| Corte | Peso del corte | Examen | Actividades en clase | Proyecto |
|---|---|---|---|---|
| 1 | 30 % | 60 % | 10 % | 30 % |
| 2 | 30 % | 60 % | 10 % | 30 % |
| 3 | 40 % | 60 % (examen final acumulativo) | 10 % | 30 % |

Sobre la nota final, los exámenes pesan 18 % + 18 % + 24 % = **60 %**, las actividades en clase 3 % + 3 % + 4 % = **10 %** y los proyectos 9 % + 9 % + 12 % = **30 %**. Se trabaja en equipo y de forma individual.

### Reglas del curso (p. 9, 23, 24)

- Asistir a clase: «Attend classes (20 %)». La tabla de notas no incluye la asistencia; deducido: probablemente es el límite de inasistencia.
- Las fechas de entrega **no se cambian**.
- Aprendizaje basado en la experiencia: retos en el aula en lugar de clase magistral (p. 11–21).
- **Plagio prohibido.** Citar correctamente es obligatorio según la guía de citación de la universidad: https://www.unisabana.edu.co/direccion-central-de-estudiantes/crea/guia-de-citacion/
- Proyecto en grupos de **hasta 5 integrantes**. Los grupos se forman contando del 1 al 5 y definen metas, reglas, roles (al menos uno por persona) y medios de comunicación.
- En cada presentación del proyecto hay que **vestir de manera profesional**. También se mencionan «letters for the project» (cartas para el proyecto).
- Proyectos listados (p. 24): investigar una empresa y analizar su estrategia (corte 1, presentación en clase), pronosticar la demanda de un producto, y analizar una empresa aplicando todo lo visto. Solo la primera fila tiene número de corte.

### Contenido conceptual de la clase

- **Mensaje pedagógico (p. 10–21, en español):**
  - El «Gerente de Operaciones del Futuro» resuelve problemas nuevos, diseña estrategias, lidera, decide, aprende, enseña y negocia.
  - «No hay una ecuación universal para resolver los problemas».
  - No se trata de memorizar fórmulas, repetir lo del tablero ni seguir instrucciones como una máquina.
  - Se busca un ingeniero creativo, propositivo, innovador y analítico.
- **Qué es OM (p. 34, Heizer et al., 2017):** la disciplina que agrupa las actividades de creación de valor mediante la generación de bienes y servicios con transformación de materia prima.
- **Problemas económicos de OM (p. 29, Bowman y Fetter, 1967):** inventarios, control y programación de la producción, equipos, mantenimiento, distribución en planta, control de calidad, procesos y métodos.
- **Qué hace el gerente de operaciones (p. 32–33, 42):**
  - Controla la calidad y los costos.
  - Busca proveedores; diseña, prueba y produce; contrata y entrena personal; programa la producción y entrega al cliente.
  - El gerente excelente planea, organiza, estructura equipos, lidera y controla.
- **Dónde se aplica (p. 35–36):** fábricas, oficinas, hospitales, restaurantes, supermercados, hogares y parques de diversiones. Sirve tanto para la producción de bienes como para la prestación de servicios.
- **Las 10 decisiones estratégicas de OM (p. 37–38):** diseño de bienes y servicios (tarea: caso Samsung Galaxy Note7), calidad, estrategia de procesos, localización, distribución (layout), recursos humanos, cadena de suministro, inventarios, programación de la producción y mantenimiento. La diapositiva indica en qué curso se estudia cada una.
- **Las tres funciones de la empresa (p. 39–40):**
  - Mercadeo genera la demanda.
  - Producción/operaciones la satisface.
  - Finanzas controla el desempeño y los recursos.
  - OM es una de estas tres funciones fundamentales.

### Fórmulas y métodos

La única cuenta de la presentación es el estado de resultados del ejemplo de la página 41 (Heizer et al., 2017):

$$\text{Margen bruto} = V - C_p, \qquad \text{Subtotal} = \text{Margen bruto} - C_f, \qquad \text{Utilidad} = (1 - t)\cdot \text{Subtotal}$$

donde $V$ son las ventas, $C_p$ los costos de producción, $C_f$ los costos financieros y $t = 0.25$ la tasa de impuestos. Se usa para comparar el efecto en la utilidad de tres estrategias alternativas.

### Ejemplos resueltos

- **p. 41, «An Example» (Heizer et al. 2017).** Situación actual: utilidad de 10,500. Las alternativas dan:
  - Mercadeo, +50 % de ventas: 18,000.
  - Finanzas, −50 % de costos financieros: 12,750.
  - **Operaciones, −20 % de costos de producción: 22,500**, la mejor.
  - Conclusión: bajar los costos de operación rinde más que vender más.
- **p. 43:** ejemplo real de una oferta de trabajo de *Operations Manager*, con sus responsabilidades: gestión del cambio, coordinación, finanzas, mejores prácticas, comunicación, ventas y servicio, aporte estratégico y gestión de proyectos.
- **p. 44, Homework 1:** buscar en LinkedIn dos ofertas («production» y «operations manager»), analizarlas (responsabilidades, beneficios, empresa, salario, ubicación, crecimiento), decidir cuál es mejor y si se aceptaría, y escribir un ensayo de 1 página con la plantilla de Virtual Sabana. Entrega: [tarea-ensayo-linkedin-operations-manager](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/tarea-ensayo-linkedin-operations-manager.md).
- **p. 31:** actividad «¿Cómo te ves en 10 años?», con una descripción breve y un dibujo.

### Páginas clave

- Profesor: página 2.
- Objetivo, ABET e indicadores: páginas 3–5.
- **Rúbrica:** página 6.
- Plan de estudios: página 7.
- **Reglas:** página 9.
- **Notas:** página 22.
- Grupos: página 23.
- **Proyectos:** página 24.
- Qué es OM: páginas 25–36.
- 10 decisiones: páginas 37–38.
- Funciones de la empresa: páginas 39–40.
- Ejemplo numérico: página 41.
- Oferta laboral y tarea 1: páginas 43–44.
- Video de la Frankfurt School: página 45.

### Relación con otros archivos del repo

- Tarea 1: [ensayo LinkedIn](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/tarea-ensayo-linkedin-operations-manager.md).
- Siguiente clase: [L02 sistemas de producción](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L02-introduction-to-production-systems.md).
- Pronósticos (meta 1 del semestre; criterios 1–2 de la rúbrica): [L03](/corte-1-pronosticos/02-introduccion-a-pronosticos/L03-introduction-to-forecasting.md) y el [proyecto THYMS de pronóstico](/corte-1-pronosticos/proyecto-thyms-pronostico/Planeacion_proyecto_corte1.md).
- Planeación (criterio 3): [planeación agregada](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md) y el [gemelo digital THYMS](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/).
- Programación (criterio 4; decisión estratégica 9): [introducción a scheduling](/corte-3-programacion-scheduling/01-introduccion-scheduling/L16-intro-scheduling.md) y la [competencia de scheduling](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/).

## Contenido completo (página por página)

### Página 1 — Planning, Scheduling and Controlling Operations (portada)

**Planning, Scheduling and Controlling Operations**

***Operations Management***

Semester 2026

*If you don't know where you are going, any road will get you there*

> [Imagen decorativa: franja lateral con una foto del campus de la Universidad de La Sabana reflejado en un lago y el logo de la universidad; ícono de licencia Creative Commons BY-NC-SA.]

### Página 2 — Introduction

- William Guerrero, Ph.D.
- "Mr. Guerrero"
- Industrial engineer
- Masters in Industrial Engineering
- PhD in Industrial Systems Optimization and reliability (UTT, France)
- PhD in Engineering (UniAndes, Bogotá)
- Associate professor
- William.guerrero1@unisabana.edu.co

> [Imagen: foto del profesor en un campus.]

### Página 3 — Course Objective

- The course develops topics related to the Management of **Productive Processes in organizations**, giving to operations a management approach that contributes to **decision-making** through advanced tools and techniques.

### Página 4 — ABET OUTCOMES

| Competencia | Asignatura | Indicador Específico | Indicador Transversal |
|---|---|---|---|
| Resolución de Problemas | Planeación, Programación y Control de las Operaciones | Plantear soluciones a problemas de gestión de sistemas productivos utilizando tecnologías de información, conceptos y herramientas propios de la industria 4.0. | Evalúa alternativas de solución a un problema de ingeniería industrial. |
| Resolución de Problemas | Planeación, Programación y Control de las Operaciones | Identificar el comportamiento de los datos históricos de la demanda y seleccionar la metodología adecuada para elaborar un buen pronóstico de la demanda. | Identifica los elementos de un problema de ingeniería industrial y las herramientas para su solución |

(En la diapositiva la celda «Asignatura» está combinada para las dos filas.)

### Página 5 — PERFORMANCE INDICATORS

- **SO1.PI_1:** Identify the elements of an industrial engineering problem
- **SO1.PI_3:** Appropriately applies quantitative methods of industrial engineering to solve problems
- **SO1.PI_4:** Evaluates alternative solutions to an industrial engineering problem.
- **SO2.PI_1:** Designs a solution that satisfies customer and organizational requirements.
- **SO2.PI_5:** Designs production and logistics systems in the general structuring of supply chain of goods and services, and the specific structuring of each of its functions.
- **SO3.PI_1:** Makes clear presentations using vocabulary appropriate for the audience.
- **SO3.PI_2:** Writes documents in Spanish using appropriate technical language, clearly expressing his/her ideas
- **SO3.PI_7:** Communicates adequately in English

### Página 6 — Rubrica del curso

| Indicador | Indicador específico | Criterio | Excelente (100%) | Bueno (80%) | Aceptable (50%) | Deficiente (25%) |
|---|---|---|---|---|---|---|
| 1 | Identificar el comportamiento de los datos históricos de la demanda y seleccionar la metodología adecuada para elaborar un buen pronóstico de la demanda. | Análisis gráfico de Pronósticos | Interpretación detallada y precisa de los gráficos, identificando patrones y características clave. | Interpretación adecuada de los gráficos, identificando la mayoría de los patrones y características. | Interpretación básica de los gráficos, identificando algunos patrones y características. | Interpretación limitada o incorrecta de los gráficos, sin identificar patrones o características clave. |
| 2 | Identificar el comportamiento de los datos históricos de la demanda y seleccionar la metodología adecuada para elaborar un buen pronóstico de la demanda. | Evaluación crítica de los Pronósticos | Análisis crítico y justificado de los errores de pronóstico, identificando el método más preciso con claridad. | Análisis adecuado de los errores de pronóstico, identificando el método más preciso con algunas justificaciones. | Análisis básico de los errores de pronóstico, identificando el método más preciso sin muchas justificaciones. | Análisis limitado o incorrecto de los errores de pronóstico, sin identificar el método más preciso. |
| 3 | Plantear soluciones a problemas de gestión de sistemas productivos utilizando tecnologías de información, conceptos y herramientas propios de la industria 4.0. | Propuesta de plan estratégico | Propuesta de plan estratégico bien fundamentada y detallada, con justificación clara de las decisiones. | Propuesta de plan estratégico adecuada, con justificación de la mayoría de las decisiones. | Propuesta de plan estratégico básica, con justificación limitada de las decisiones. | Propuesta de plan estratégico limitada o incorrecta, sin justificación de las decisiones. |
| 4 | Plantear soluciones a problemas de gestión de sistemas productivos utilizando tecnologías de información, conceptos y herramientas propios de la industria 4.0. | Evaluación del sistema de programación | Evaluación exhaustiva del sistema de programación, con recomendaciones claras y justificadas para mejorar el desempeño utilizando tecnologías de información, conceptos y herramientas propios de la industria 4.0. | Evaluación adecuada del sistema de programación, con algunas recomendaciones para mejorar el desempeño. | Evaluación básica del sistema de programación, con recomendaciones limitadas para mejorar el desempeño. | Evaluación limitada o incorrecta del sistema de programación, sin recomendaciones claras para mejorar el desempeño. |

### Página 7 — So far you are capable of: (con el Plan de Estudios)

**So far you are capable of:**

1. Code
2. Doing math
3. Analyze data and work systems
4. understand the basics of business Management
5. Optimize and simulate!

A la izquierda aparece la imagen del **Plan de Estudios — Ingeniería Industrial, Universidad de La Sabana, Facultad de Ingeniería**, transcrita abajo. Las columnas son asignatura, créditos y prerrequisito. En la imagen, la columna de prerrequisitos está alineada a ojo con las asignaturas, así que en algunos casos la correspondencia puede estar corrida una fila.

**Semestre 1**

| Asignatura | Créd. | Prerrequisito |
|---|---|---|
| Fundamentos de Gestión Empresarial | 2 | — |
| Oportunidades de Negocio y Mercado | 3 | — |
| Calculo Diferencial | 3 | — |
| Química | 2 | — |
| Competencias Básicas Idiomáticas | 2 | — |
| Introducción a la Programación | 2 | — |
| Introducción a la Ingeniería Industrial | 3 | — |
| (sin nombre visible) | 2 | — |

Nota: la columna de créditos del semestre 1 tiene 8 números y solo 7 asignaturas. Sin ese «2» huérfano, la suma de todos los semestres da exactamente los 166 créditos que indica la imagen (verificación deducida).

**Semestre 2**

| Asignatura | Créd. | Prerrequisito |
|---|---|---|
| Fundamentos de Macroeconomía y Microeconomía | 3 | Calculo Diferencial |
| Calculo Integral | 3 | Calculo Diferencial |
| Inglés 3 | 2 | — |
| Core Currículo Persona y cultura I: Persona y Autoconocimiento | 2 | Competencias Básicas Idiomáticas |
| Programación Avanzada | 3 | Introducción a la Programación |
| Ingeniería de Métodos | 2 | Introducción a la Ingeniería Industrial |
| Probabilidad y Estadística I | 2 | Calculo Diferencial |

**Semestre 3**

| Asignatura | Créd. | Prerrequisito |
|---|---|---|
| Ingeniería Económica | 2 | — |
| Algebra Lineal | 3 | Calculo Diferencial |
| Física Mecánica | 4 | Calculo Diferencial |
| Inglés 4 | 3 | Inglés 3 |
| Core Currículo Persona y cultura II: Persona y Afectividad | 2 | Core Currículo Persona y cultura I: Persona y Autoconocimiento |
| Probabilidad y Estadística II | 3 | Probabilidad y Estadística I |
| Procesos Productivos | 3 | Química y Ingeniería de Métodos |

**Semestre 4**

| Asignatura | Créd. | Prerrequisito |
|---|---|---|
| Practica en Diagnóstico de Procesos | 2 | Procesos Productivos |
| Contabilidad, Costos y Presupuestos | 3 | Ingeniería Económica |
| Calculo Vectorial | 3 | Algebra Lineal y Calculo Integral |
| Inglés 5 | 3 | Inglés 4 |
| Core Currículo Persona y Cultura III: Persona y Trascendencia | 2 | Core Currículo Persona y cultura II: Persona y Afectividad |
| Análisis y Diseño del Trabajo | 2 | Ingeniería de Métodos |
| Analítica de Datos | 3 | Probabilidad y Estadística II y Programación Avanzada |

**Semestre 5**

| Asignatura | Créd. | Prerrequisito |
|---|---|---|
| Seminario de Constitución de Empresas | 2 | Fundamentos de Gestión Empresarial |
| Inglés 6 | 3 | Inglés 5 |
| Core Currículo Persona y cultura IV: Persona y su Actuar | 2 | Core Currículo Persona y Cultura III: Persona y Trascendencia |
| Materiales para el Diseño de Producto y Proceso | 2 | Física Mecánica |
| Control Estadístico de la Calidad | 2 | Probabilidad y Estadística II |
| Introducción al CAD | 2 | — |
| Procesos Estocásticos | 3 | Analítica de Datos |
| Ecuaciones Diferenciales | 3 | Calculo Vectorial |

**Semestre 6**

| Asignatura | Créd. | Prerrequisito |
|---|---|---|
| Inglés 7 | 3 | Inglés 6 |
| Core Currículo Persona y Cultura V: Persona y Retos Actuales | 3 | Core Currículo Persona y Cultura III: Persona y Trascendencia |
| Diseño de Producto, Servicio y Proceso | 3 | Introducción al CAD y Materiales para el Diseño de Producto y Proceso |
| Optimización y Analítica | 3 | Analítica de Datos y Algebra Lineal |
| Simulación | 3 | Probabilidad y Estadística II |
| Énfasis I | 2 | — |
| Electiva | 2 | — |

**Semestre 7** (el de este curso)

| Asignatura | Créd. | Prerrequisito |
|---|---|---|
| Salud ocupacional y Gestión Ambiental | 2 | — |
| Practica en Estrategias de Mejora | 2 | Ubicación semestral mínima sexto o semestre (sic) |
| Gestión de la Calidad | 2 | — |
| Gestión de Proyectos | 2 | Análisis y Diseño del Trabajo |
| Fundamentos de Logística | 3 | — |
| **Planeación, Programación y Control de las Operaciones** | **4** | Ecuaciones Diferenciales |
| Énfasis II | 2 | Optimización y Analítica |
| Electiva | 2 | — |

**Semestre 8**

| Asignatura | Créd. | Prerrequisito |
|---|---|---|
| Gerencia Financiera | 2 | Contabilidad, Costos y Presupuestos |
| Gestión Humana | 3 | — |
| Seminario de Práctica | 1 | Ubicación semestral octavo semestre |
| Transformación Digital y Sistemas de Información | 2 | Planeación, Programación y Control delas Operaciones |
| Experiencia Centrada en el Diseño | 4 | (ver nota) |
| Diseño y Gestión de Cadena de Suministro | 3 | Planeación, Programación y Control de las Operaciones y Fundamentos de Logística (ver nota) |
| Proyecto en Analítica Aplicada | 2 | Optimización y Analítica y Simulación |
| Énfasis III | 2 | Analítica de Datos |

Nota: el prerrequisito «Planeación, Programación y Control de las Operaciones y Fundamentos de Logística» está impreso entre las filas de «Experiencia Centrada en el Diseño» y «Diseño y Gestión de Cadena de Suministro». Por lógica corresponde a Cadena de Suministro (deducido).

**Semestre 9**

| Asignatura | Créd. | Prerrequisito |
|---|---|---|
| Práctica Profesional | 16 | Haber cursado todas las asignaturas 16 del plan de estudios hasta 8vo semestre |
| Electiva | 2 | — |

**Total créditos: 166**

Pie de la imagen: «\*Analitica de datos | \*Metodos cuantitativos para la toma de decisiones | \*Mejora continua» (deducido: las líneas de énfasis). Debajo: «SNIES 4112 | Reg. Calif. Res. N° 007435 del 30 de abril de 2021 | Vigencia 7 años | Duración 9 semestres».

Créditos por semestre (calculados con la tabla, sin el «2» huérfano del semestre 1):

| Semestre | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | Total |
|---|---|---|---|---|---|---|---|---|---|---|
| Créditos | 17 | 17 | 20 | 18 | 19 | 19 | 19 | 19 | 18 | 166 |

### Página 8 — By the end of the semester, you'll need to:

(La misma imagen del Plan de Estudios de la página 7, a la izquierda.)

**By the end of the semester, you'll need to:**

1. Forecast sales
2. **Optimize** business Operations

CREATE VALUE for companies!

### Página 9 — Course rules

- Attend classes (20 %). Grading activities (subrayado en el original, sin enlace)
- Due dates are unchangeable
- **Experience-based learning**
- Plagiarism is not allowed. Proper Citations are mandatory: check this link:
  - **https://www.unisabana.edu.co/direccion-central-de-estudiantes/crea/guia-de-citacion/**

> [Imagen decorativa: cartel «KEEP CALM & FOLLOW THE RULES» con una corona.]

> Nota (deducido): «Attend classes (20 %)» no aparece como componente de la nota en la tabla de la página 22. Lo más probable es que se refiera al límite de inasistencia del 20 % (regla usual de la universidad) y no a un peso de la calificación.

### Página 10 — Gerente de Operaciones del Futuro (separador)

**Gerente de Operaciones del Futuro**

Graduado de la Universidad de La Sabana

> [Imagen decorativa: logo de la Universidad de La Sabana y foto de un edificio de vidrio visto desde abajo.]

### Página 11 — (meme) Clase magistral vs. Retos en el aula

> [Imagen: meme de los «dos botones». Un botón dice «Clase magistral» y el otro «Retos en el aula»; la mano presiona «Retos en el aula» mientras el personaje suda indeciso. Mensaje: el curso se basa en retos en el aula, no en clase magistral.]

### Página 12 — (meme) Ingeniero que resuelve problemas

> [Imagen: meme del perro musculoso frente al perro que llora. El musculoso: «Ingeniero que resuelve problemas». El que llora: «Profe, ¿cómo era la fórmula?».]

### Página 13 — (meme) Las fórmulas

> [Imagen: meme de un personaje que ríe con una copa en la mano: «TE DIJERON QUE LAS FÓRMULAS ERAN LO IMPORTANTE DE TU CARRERA».]

### Página 14 — Retos del Gerente de Operaciones

- Resolver problemas ***nuevos***
- Diseñar estrategias
- Liderar y trabajar en equipo
- Tomar decisiones
- Aprender y enseñar
- Negociar

> [Imagen decorativa: fotos de reuniones de trabajo y de un rascacielos; logo de la Universidad de La Sabana.]

### Página 15 — (mensaje)

EN EL MUNDO DE LA GESTIÓN DE OPERACIONES **NO** (en rojo) HAY UNA ECUACIÓN UNIVERSAL PARA RESOLVER LOS PROBLEMAS

### Página 16 — Retos que NO tendrá el Gerente de Operaciones

- Saber de memoria formulas
- Repetir el ejercicio que el profesor hizo en el tablero
- Seguir instrucciones como una máquina

> [Imagen decorativa: cuatro robots de juguete idénticos y fotos de oficinistas aburridos o frustrados.]

### Página 17 — (cita)

*"No son nuestras habilidades las que definen quiénes somos, sino las elecciones que tomamos".* — Harry Potter

> [Imagen decorativa: fondo amarillo con gafas redondas y un rayo (alusión a Harry Potter).]

### Página 18 — En Clase de Gestión de Operaciones:

> [Diagrama: círculo central «Gerentes de Operaciones» con flechas hacia seis círculos: «Trabajan en equipo», «Diseñan estrategias para ganar», «Resuelven retos desconocidos», «Toman decisiones», «Autoaprendizaje» y «Negociación & Gestión del tiempo».]

> [Imagen decorativa: dos fotos aéreas del campus de la Universidad de La Sabana y su logo.]

### Página 19 — ¿Cómo fortalecer las competencias laborales?

Cuatro recomendaciones, cada una con una foto:

1. Ponga atención y participe en la actividad
2. Haga preguntas
3. Valide su propuesta
4. Busque información adicional

### Página 20 — ¿Qué TIPO de ingeniero quiero ser?

| Lado izquierdo (lo que no se quiere) | Lado derecho (lo que se busca) |
|---|---|
| Memoriza ecuaciones | Creativo |
| Repite tareas y actividades | Propositivo |
| Espera la instrucción del jefe para actuar | Innovador |
| | Analítico |

> [Imagen: una persona dividida en dos: a la izquierda con overol azul de operario, a la derecha con traje de ejecutivo.]

### Página 21 — (meme) Quiero ser ingeniero

> [Imagen: meme del ciclista que se mete un palo en su propia rueda. Viñeta 1: «Quiero ser ingeniero»; viñeta 2: «Prefiero no resolver retos»; viñeta 3: el ciclista cae al suelo.]

### Página 22 — Computing the grades

- We work in teams and individually.

| Term | Test | Percentage |
|---|---|---|
| **1 - 30%** | Exam | 60% |
| | In class activities | 10% |
| | Project | 30% |
| **2 - 30%** | Exam | 60% |
| | In class activities | 10% |
| | Project | 30% |
| **3 - 40%** | Final Cumulative topics | 60% |
| | In class activities | 10% |
| | Project | 30% |

Peso de cada componente en la nota final (cálculo derivado de la tabla: peso del corte × peso del componente):

| Componente | Corte 1 (30 %) | Corte 2 (30 %) | Corte 3 (40 %) | Total |
|---|---|---|---|---|
| Examen (corte 3: examen final acumulativo) | 18 % | 18 % | 24 % | 60 % |
| Actividades en clase | 3 % | 3 % | 4 % | 10 % |
| Proyecto | 9 % | 9 % | 12 % | 30 % |
| **Total del corte** | 30 % | 30 % | 40 % | 100 % |

### Página 23 — Numbers from 1-5

- Lets count from 1-5.
- Group goals, rules and roles
- Communication means

| ITEM | Description |
|---|---|
| Goals | What do you want to achieve as a group? |
| Rules | What to do or not to do as a group? |
| Rols | How you are going to achieve that? (at least one per person. |
| Communication means | How to get in touch? |

(Actividad para formar grupos: contar del 1 al 5 y acordar metas, reglas, roles y medios de comunicación.)

### Página 24 — Project in groups up to 5 members

| Term | Project |
|---|---|
| 1 | Research a Company and make an analysis of its strategy – present in class. |
| (vacío) | Forecast a product demand |
| (vacío) | Make an analysis of a Company, applying EVERYTHING we have learnt in class |

- You are required to dress as a professional for each project presentation.
- Letters for the project

> [Imagen decorativa: grupo de personas con ropa formal, rotulado «Professional Dress».]

> Nota: la columna «Term» solo trae el «1» en la primera fila; las otras dos están vacías. En este repo, el proyecto real del corte 1 fue pronosticar la demanda de THYMS (ver [proyecto-thyms-pronostico](/corte-1-pronosticos/proyecto-thyms-pronostico/Planeacion_proyecto_corte1.md)).

### Página 25 — Lecture objective

- To understand what is OM and where is it applied.
- Do I want to be an Operations Management?

### Página 26 — WHAT IS OPERATIONS MANAGEMENT?

> [Imagen decorativa: silueta de una cabeza llena de engranajes, rodeada de íconos de negocios (dinero, gráficos de barras, documentos, teléfono).]

### Página 27 — How is your lifestyle?

> [Imagen: paisaje rural con un molino de viento, una casa, pasto y un canal (vida rural y tradicional).]

### Página 28 — How is your lifestyle?

> [Imagen: cuatro fotos de la vida moderna: un trancón de autos, el pasillo de un supermercado con un carrito, autopistas iluminadas de noche en una gran ciudad y torres de alta tensión al atardecer (producción y servicios masivos).]

### Página 29 — Our lifestyle

- Mass production
  - Example: Cars
- **Challenge:** To provide the customer with the required product when he wants it, where he wants it
  - Food at restaurants (McDonalds)

Una llave une los puntos anteriores con:

**Economic Issues in OM**

1. Inventories
2. Production Control and scheduling
3. Equipment
4. Maintenance
5. Plant Layout
6. Quality control
7. Processes
8. Methods

*Bowman y Fetter (1967)*

### Página 30 — Production

Methods to support the process of managing people and resources to create a product or service

> [Imagen: las mismas cuatro fotos de la página 28 (tráfico, supermercado, ciudad de noche, torres eléctricas).]

### Página 31 — Activity

- How do you see yourself in 10 years?
- Write down a brief description & draw something related to that description

### Página 32 — What does an operations manager do?

In brief:

- To control the quality of the product /service
- To control the costs of the product /service

> [Imagen decorativa: letrero «OPERATIONS MANAGER» en una puerta.]

### Página 33 — What does an operations manager do?

- Searches for qualified suppliers
- Designs, tests, and produces
- Searches and trains the right staff and schedules the production
- Delivers the product to customers

*"OM is demanding, challenging, and exciting" Heizer et al. (2017)*

### Página 34 — What is OM?

- is the discipline that groups together activities related to the creation of value through the generation of goods and services where there is transformation of a raw material.
  - Heizer et al. (2017)

### Página 35 — Where is OM applied?

- Factories
- Offices
- Hospitals
- Restaurants
- Supermarkets
- Homes
- Amussement parks
- …

> [Imagen decorativa: fotos de una fábrica textil, una oficina, la entrada de urgencias de un hospital y un parque de Disney.]

### Página 36 — In organizations

- Production of goods
  - Transforming raw materials
- Providing services
  - Activities

> [Imagen decorativa: una línea de ensamble de autos y un centro de atención telefónica (call center).]

### Página 37 — 10 OM strategic decisions

1. [Design of goods and services](http://cnnespanol.cnn.com/2017/01/23/samsung-revela-por-que-se-incendiaron-los-galaxy-note7/) (homework)
2. Quality
3. Process strategy
4. Location strategy
5. Layout design
6. Human resources
7. Supply chain management
8. Inventory management
9. Production scheduling
10. Maintenance management

> [Imagen: código QR (deducido: lleva al mismo enlace de la tarea).] El enlace del punto 1 es una noticia de CNN Español del 23 de enero de 2017: «Samsung revela por qué se incendiaron los Galaxy Note7». Es un caso de fallas en el diseño de un producto.

### Página 38 — 10 OM strategic decisions

This topics will be studied in the following courses

| # | Decision | Course |
|---|---|---|
| 1 | Design of goods and services | Second term |
| 2 | Quality | other courses |
| 3 | Process strategy | this term |
| 4 | Location strategy | Logistics course |
| 5 | Layout design | other course |
| 6 | Human resources | other course |
| 7 | Supply chain management | Logistics |
| 8 | Inventory management | Logistics |
| 9 | Production scheduling | Oper. Management 2 |
| 10 | Maintenance management | other course |

### Página 39 — Activities in Companies

- **Marketing:** Demand generation
- **Production / Operations:** Demand satisfaction
- **Finances and Accounting:** Performance control and management of financial resources

### Página 40 — Why studing OM?

- Is one of the three fundamental functions in the organizations
- Is important to know how goods and services are produced.
- Optimize processes in a company

### Página 41 — An Example

Comparación de tres estrategias para aumentar la utilidad (Heizer et al. 2017). Los números usan punto como separador de miles: 100.000 = 100,000.

| STRATEGY | Current | Marketing choice: Increase sales by 50% | Financial choice: Reduce financial costs by 50% | OM Choice: Reduce costs by 20% |
|---|---|---|---|---|
| Sales | $ 100.000 | $ 150.000 | $ 100.000 | $ 100.000 |
| Production costs | $ 80.000 | $ 120.000 | $ 80.000 | $ 64.000 |
| Brut margin | $ 20.000 | $ 30.000 | $ 20.000 | $ 36.000 |
| Financial costs | -$ 6.000 | -$ 6.000 | -$ 3.000 | -$ 6.000 |
| Subtotal | $ 14.000 | $ 24.000 | $ 17.000 | $ 30.000 |
| Taxes (25%) | -$ 3.500 | -$ 6.000 | -$ 4.250 | -$ 7.500 |
| **Profit** | **$ 10.500** | **$ 18.000** | **$ 12.750** | **$ 22.500** |

(Heizer et al. 2017)

> Nota: en la versión estática del PDF, las tres columnas de alternativas están tapadas por rectángulos blancos (deducido: se revelaban con animación en clase). Los valores salen de la capa de texto del PDF.

Cálculo, igual en cada columna:

$$\text{Margen bruto} = \text{Ventas} - \text{Costos de producción}$$
$$\text{Subtotal} = \text{Margen bruto} - \text{Costos financieros}$$
$$\text{Impuestos} = 0.25 \times \text{Subtotal}, \qquad \text{Utilidad} = \text{Subtotal} - \text{Impuestos} = 0.75 \times \text{Subtotal}$$

Por ejemplo, en la opción de operaciones: $100{,}000 - 64{,}000 = 36{,}000$; $36{,}000 - 6{,}000 = 30{,}000$; $0.25 \times 30{,}000 = 7{,}500$; utilidad $= 22{,}500$.

Conclusión del ejemplo: reducir los costos de producción un 20 % (opción de operaciones) da la mayor utilidad, 22,500, más que vender un 50 % más (18,000) o recortar los costos financieros a la mitad (12,750). La utilidad pasa de 10,500 a 22,500, un aumento del 114 %.

### Página 42 — What does an EXCELLENT Operations manager do?

- *Planning*
- *Organizing*
- *Team structuring*
- *Leadering*
- *Controlling*

### Página 43 — Actual job offer for an Operations Manager

- The Operations Manager is responsible for ensuring and improving the performance, productivity, efficiency and profitability of departmental and organizational operations by providing effective methods and strategies.
- Main Job Tasks and Responsibilities
- Change Management - Lead the implementation and execution of improved business processes throughout the organization. This will involve clear communication, diplomacy and instruction where necessary.
- Coordination and Supervision - Coordinate, manage and monitor the productivity and efficiency of various departments in the organization like Partner Services, Account Support and Travel Experience.
- Financial - Review financial statements and data. Utilize financial data to improve profitability. Prepare and control operational budgets. Plan effective strategies for the financial well being of the company.
- Best Practices - Provide root cause analysis and drive action for business/process performance improvement to meet the goals & objectives of the team. Monitor adherence to rules, regulations and procedures.
- Communication - Ensure that communication between departments is ongoing and utilized to maintain an environment of continuous improvement.
- Sales, Marketing and Customer Service - Manage customer support. Work alongside Director of Sales to plan and support sales and marketing activities.
- Strategic Input - Liaison with top management to contribute toward the achievement of company's strategic and operational objectives. Implement and manage operational plans.
- Project Management - Improve business operations and process efficiency within the organization through automation and similar initiatives. Act as project liaison between various departments, ensuring that all project activities are in support of overall project goals and the company's business objectives.

### Página 44 — Homework 1

- Visit linkedin.com
- Find two jobs related to operations management:
  - "production"
  - "operations manager"
- Analyze the offers: responsibilities, benefits, and the Company
  - Which one is better? Why? Be comprehensive (salary, responsibilities, location, growth opportunities, etc)
  - would you take the job? Why?
- Write a 1-page essay about that.
  - Use the template in Virtual Sabana.
  - Avoid using folders, envelops, or binders.

> Nota: las tres últimas líneas («Write a 1-page essay about that», «Use the template in Virtual Sabana», «Avoid using folders, envelops, or binders») están en texto blanco sobre fondo blanco: no se ven en la diapositiva pero están en el PDF. La entrega de esta tarea está en [tarea-ensayo-linkedin-operations-manager](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/tarea-ensayo-linkedin-operations-manager.md).

### Página 45 — According to *Frankfurt School of Finance & Management*

> [Imagen: miniatura del video, la caricatura de un profesor con el texto «THAT WAS Operations Management WITH Dr. Jörn-Henrik Thun, Professor of Operations Strategy».]

https://www.youtube.com/watch?v=nG5-52a5lRo

### Página 46 — Operations Management (cierre)

**Operations Management**

*If you don't know where you are going, any road will get you there*


---

<!-- fuente: corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L02-introduction-to-production-systems.md -->
# L02-introduction-to-production-systems

> **Archivo:** [`L02-introduction-to-production-systems.pdf`](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L02-introduction-to-production-systems.pdf) · **Corte 1** · 22 páginas  
> **Nombre original:** `CORTE 1/lec 2 Introduction-to-Production-Systems.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** configuraciones de los sistemas de producción (flowshop, jobshop y openshop), sus medidas de desempeño y las estrategias de control de piso (push, pull, Kanban y ConWIP). Es la Lecture 2 del corte 1; las diapositivas se hicieron con Gamma.

**Ideas clave:**

- Un sistema de producción es el conjunto de procesos y recursos que crean bienes o servicios. La configuración determina cómo fluyen los productos entre estaciones.
- **Flowshop:** todos los productos siguen la misma secuencia fija de estaciones (p. ej., una línea de ensamble de autos). Sirve para alto volumen de productos estandarizados. Es eficiente y tiene poca variabilidad, pero poca flexibilidad.
- **Jobshop:** cada referencia tiene su propia ruta. En el ejemplo, la ref 1 va A→C, la ref 2 va B→A→C y la ref 3 va C→A→B. Es flexible, admite productos personalizados y lotes pequeños (muebles a medida, herramientas especiales). Su programación es compleja.
- **Openshop:** la ruta no es estricta, porque cualquier máquina puede hacer cualquier operación y el orden de visita es libre. Es muy variable y difícil de programar y gestionar.
- **Medidas de desempeño:** WIP (trabajo promedio en proceso), *takt time* (ritmo al que hay que terminar un producto para cumplir la demanda), *throughput* (tasa de salida de producto terminado), *cycle time* (tiempo de inicio a fin de un producto), *lead time* (tiempo hasta entregar al cliente) y eficiencia (qué tan bien se usan los recursos).
- **Control de piso:** son los métodos para gestionar el flujo de trabajo en planta. Buscan eficiencia, menos retrasos y cumplir la demanda.
  - **Push:** produce según un programa o pronóstico predeterminado, sin importar la demanda real. Genera más WIP e inventario, y aparecen cuellos de botella si el programa no se alinea con la demanda.
  - **Pull:** produce solo cuando la demanda real lo pide. Está ligado a *lean manufacturing*, reduce desperdicio e inventario y responde mejor a los cambios.
  - **Kanban** («letrero» o «tarjeta» en japonés): nació en el sistema de producción de Toyota en los años 1940. Usa tarjetas o tableros como señales visuales, de modo que cada estación «jala» trabajo solo cuando está lista. Reduce el WIP, deja ver los cuellos de botella y promueve la mejora continua.
  - **ConWIP** (solo en el diagrama de la página 19): una única tarjeta va del final de la línea al inicio y limita el WIP total de la línea.
- Cuándo usar cada estrategia: push para alto volumen, productos estándar y demanda estable; pull para demanda variable cuando se busca reducir desperdicio; Kanban es versátil y se adapta a muchos entornos.
- La página 1 trae reglas de debate (Musgrave, 1957) para una actividad en clase, y la página 2 recomienda leer el capítulo 1 de *Factory Physics* (Hopp & Spearman, 2001, 2.ª ed.).

**Fórmulas y métodos:**

La presentación no trae fórmulas: las medidas de desempeño se definen solo con palabras (páginas 8–9). Como **complemento que no aparece en las diapositivas**, estas son las relaciones estándar que suelen acompañar esas definiciones (por ejemplo, en *Factory Physics*, el libro recomendado):

- Takt time: $\text{Takt} = \dfrac{\text{tiempo disponible de producción en el periodo}}{\text{demanda del cliente en el periodo}}$.
- Ley de Little: $WIP = TH \times CT$, donde $WIP$ es el inventario promedio en proceso (unidades), $TH$ el *throughput* (unidades por unidad de tiempo) y $CT$ el *cycle time* promedio.

Métodos que sí presenta: la clasificación de configuraciones (flowshop, jobshop, openshop) y las estrategias de control de piso (push, pull, Kanban y ConWIP), con su comparación (páginas 10, 17 y 22) y el diagrama de flujo de información (página 19).

**Ejemplos resueltos:** no hay ejercicios numéricos. Ejemplos ilustrativos:

- Página 4: flujo lineal Station 1→2→3 (flowshop).
- Página 5: tabla de rutas de 3 referencias en 3 estaciones (jobshop).
- Página 7: rutas «Not strict» (openshop).
- Página 19: diagrama Push / Kanban / ConWIP.

**Páginas clave:**

- Reglas del debate: página 1.
- Lectura recomendada: página 2.
- Flowshop: páginas 4 y 13.
- Jobshop: páginas 5–6.
- Openshop: página 7.
- Medidas de desempeño: páginas 8–9.
- Comparación de configuraciones: página 10.
- Control de piso: página 14.
- Push: página 15.
- Pull: página 16.
- Push vs. pull: página 17.
- Kanban: páginas 18, 20 y 21.
- Diagrama Push/Kanban/ConWIP: página 19.
- Conclusión: página 22.

**Relación con otros archivos del repo:**

- Las configuraciones de esta clase son los problemas de programación del corte 3:
  - [introducción a scheduling](/corte-3-programacion-scheduling/01-introduccion-scheduling/L16-intro-scheduling.md)
  - [flow shop](/corte-3-programacion-scheduling/04-flow-shop/L19-flow-shop-scheduling.md) y su Excel [flowshop-scheduling](/corte-3-programacion-scheduling/04-flow-shop/flowshop-scheduling.md)
  - [job shop](/corte-3-programacion-scheduling/05-job-shop/job-shop-y-flexible-job-shop.md)
- La lógica push (producir según un pronóstico o un plan) es la del pronóstico (corte 1) → planeación agregada → MRP (corte 2):
  - [L13 BOM e introducción a MRP](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md)
  - [L15 MRP II](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md)
- Presentación anterior del curso: [L01 introducción al curso](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L01-introduccion-al-curso.md).

## Contenido completo (página por página)

### Página 1 — Debate Rules

Condensed from *Competitive Debate: Rules and Techniques*, by George McCoy Musgrave. New York: H.W. Wilson, 1957)

1. There are two teams.
2. Each team has two constructive speeches (1 minute), and one rebuttal speech (40 seconds). The affirmative gives the first constructive speech, and the rebuttals alternate: negative, affirmative, negative, affirmative. The affirmative has both the first and last speeches of the debate.
3. The affirmative must advocate everything required by the topic itself. No revision of position of a team is permitted during the debate.
4. He who asserts must prove. In order to establish an assertion, the team must support it with enough evidence and logic to convince an intelligent but previously uninformed person that it is more reasonable to believe the assertion than to disbelieve it. Facts must be accurate. Visual materials are not permissible, and if introduced, they become available for the opponents' use if desired.
5. The judge must base his decision entirely on the material presented, without regard for other material which he may happen to possess.

> Nota (deducido): la diapositiva no dice el tema del debate. Por el resto de la presentación, probablemente se debatía entre configuraciones de producción o entre estrategias *push* y *pull*.

### Página 2 — Recommended Reading: term 1

- **Cap 1**, from the book:
  J.. Hopp, & Mark L.. Spearman. (2001). Factory Physics: Foundations of Manufacturing Management. Irwin/McGraw-Hill.Ed. 2.

> [Imagen: portada del libro *Factory Physics, Second Edition*: un científico de pelo blanco escribiendo en un tablero y un operario recostado sobre un engranaje.]

### Página 3 — Introduction to Production Systems

Production systems refer to the processes and resources used to create goods or services. Different configurations exist, each with unique characteristics and applications. This presentation will explore flowshop, jobshop, and openshop configurations, along with key performance measures.

> [Imagen decorativa: logo de la Universidad de La Sabana sobre la foto de una planta industrial con maquinaria azul.]

### Página 4 — Flowshop Configuration

> [Diagrama: flujo lineal **→ STATION 1 → STATION 2 → STATION 3 →** con flechas amarillas. Todos los productos entran por la estación 1 y salen por la 3 en el mismo orden. Íconos: STATION 1 con una hoja de sierra (corte), STATION 2 con una brocha (pintura), STATION 3 con una carretilla (despacho/transporte).]

| Characteristics | Example | Advantages |
|---|---|---|
| In a flowshop, products follow a fixed sequence of operations. This configuration is suitable for **high-volume production** of **standardized** products, such as automobiles or electronics. | Imagine a car assembly line where each station performs a specific task in a predetermined order. This represents a flowshop system. | Flowshops are known for their efficiency, due to streamlined operations and minimal process variability. |

### Página 5 — Jobshop Configuration

| Product Reference | Production Route |
|---|---|
| Product ref 1, | Station A – station C |
| Product ref 2 | Station B – station A – station C |
| Product ref 3 | Station C – station A – station B |

> [Diagrama: tres cajas separadas, **STATION A** (ícono de sierra), **STATION B** (ícono de brocha) y **STATION C** (ícono de carretilla), sin flechas entre ellas: cada producto sigue su propia ruta, dada en la tabla.]

> [Imagen decorativa: foto de un taller industrial (marca de agua de Alamy) y sello «Made with Gamma».]

### Página 6 — Jobshop Configuration

1. **Flexibility** — Jobshops are highly flexible, allowing for the production of **customized products** with varying production sequences.
2. **Variety** — This configuration handles a wide range of products and orders, making it ideal for small batch production or unique projects.
3. **Examples** — Examples include custom furniture manufacturing or specialized tool fabrication, where each product has a unique production route.
4. **Scheduling Complexity** — Jobshops present challenges in scheduling due to the variability in product orders and routes.

> [Imagen decorativa: la misma foto del taller industrial.]

### Página 7 — Openshop Configuration

| Product Reference | Production Route |
|---|---|
| Product ref 1 | Not strict |
| Product ref 2 | Not strict |
| Product ref 3 | Not strict |

> [Diagrama: tres cajas, **STATION 1**, **STATION 2** y **STATION 3**, sin flechas: el orden de visita no es fijo.]

- **Machine Flexibility** — In an openshop, machines can handle any type of operation, allowing for greater flexibility in production routes.
- **Unpredictable Routing** — Product orders can be processed in any order, resulting in unpredictable production routes. This can lead to challenges in scheduling and resource allocation.
- **Example** — Imagine a workshop where various machines can perform different operations on any product, allowing for a wide range of production possibilities.
- **High Variability** — Openshops are characterized by high variability in product orders and production sequences, making them challenging to manage.

> [Imagen decorativa: foto de brazos robóticos industriales amarillos en una celda de manufactura.]

### Página 8 — Performance Measures: WIP, Takt Time, and Throughput

1. **Work-in-Progress (WIP)** — Measures the average amount of work that is currently in progress within a production system.
2. **Takt Time** — Represents the rate at which a product needs to be completed to meet customer demand.
3. **Throughput** — Indicates the rate at which a production system produces finished goods or services over a given period.

> [Imagen decorativa: captura de un tablero de producción genérico: «Quick Stats» 99,474 Production Volume, 45 Active Machines, 77,662 Quantity Ordered, 1.12M Sales Revenue; «Downtime» 4.45 %; «Top 5 Products»; «Production Volume by Top 5 Machines» (9 %, 7 %, 5 %, 4 %…); «Returned Items by Reason». Es una imagen de ejemplo, no son datos del curso.]

### Página 9 — Other Performance Measures

| Measure | Definition |
|---|---|
| Cycle Time | The total time it takes to complete a product from start to finish. |
| Lead Time | The time it takes to deliver a finished product to the customer. |
| Efficiency | Measures how well resources are utilized and how effectively products are produced. |

> [Imagen decorativa: operario con casco rojo en una planta; sello «Made with Gamma».]

### Página 10 — Comparison of Production System Configurations

| 1. Flowshop | 2. Jobshop | 3. Openshop |
|---|---|---|
| High volume, standardized products, efficient operations, low flexibility. | Customizable products, flexible operations, complex scheduling, lower volume. | High variability, flexible machines, unpredictable routing, challenging to manage. |

> [Imagen decorativa: banda superior con una línea de brazos robóticos naranjas a ambos lados de un transportador; sello «Made with Gamma».]

### Página 11 — Conclusion and Key Takeaways

Production system configurations offer different advantages and challenges depending on the specific industry, product, and production needs. Understanding these configurations and their performance measures is crucial for optimizing production processes and achieving business goals.

> [Imagen decorativa: primer plano de una cadena de transmisión industrial (Alamy); sello «Made with Gamma».]

### Página 12 — Shop Floor Control Strategies in Flowshop Systems

This presentation will explore shop floor control strategies in flowshop systems. We will delve into the definition and importance of flowshop systems, and then examine different control strategies.

> [Imagen decorativa: ilustración de una línea de producción con bandas transportadoras y cajas naranjas.]

### Página 13 — Introduction to Flowshop Systems

Flowshop systems are a type of manufacturing process where jobs move through a series of workstations in a fixed sequence. The order of workstations is determined by the manufacturing process. Each workstation performs a specific task on the job.

| Definition of Flowshop Systems | Importance in Manufacturing | Examples of Industries Using Flowshop Systems |
|---|---|---|
| A flowshop system is a type of manufacturing process where jobs move through a series of workstations in a fixed sequence. This sequence is determined by the manufacturing process and each workstation performs a specific task on the job. | Flowshop systems are crucial in manufacturing for improving efficiency and productivity. They optimize resource utilization and ensure a smooth flow of products through the production process. | Flowshop systems are used in a variety of industries, including automotive, electronics, food processing, and pharmaceuticals. They are particularly valuable in industries with high production volumes and standardized products. |

> [Imagen decorativa: banda superior con la ilustración de una máquina industrial naranja.]

### Página 14 — Overview of Shop Floor Control Strategies

Shop floor control strategies are a set of methods used to manage and optimize the flow of work on the factory floor. These strategies aim to ensure efficient production, minimize delays, and meet customer demands.

**Definition and Purpose** — Shop floor control strategies are a set of methods used to manage and optimize the flow of work on the factory floor. Their purpose is to ensure efficient production, minimize delays, and meet customer demands.

**Key Strategies**

1. Push
2. Pull
3. Kanban

### Página 15 — Push Strategy: How it Works

The push strategy relies on a predetermined production schedule or forecast. Work is pushed through the system regardless of actual demand.

- **Production Schedule** — A push system follows a predetermined production schedule, regardless of actual demand.
- **Work-in-Progress** — Work is pushed through the system, leading to higher levels of work-in-progress and potential waste.
- **Inventory Management** — Push systems often involve higher levels of inventory to meet anticipated demand.
- **Potential Bottlenecks** — Bottlenecks can occur if the production schedule is not aligned with actual demand.

> [Imagen decorativa: ilustración isométrica de una máquina con tuberías naranjas; íconos de reloj, fábrica, calendario y alerta junto a cada punto.]

### Página 16 — Pull Strategy: How it Works

The pull strategy operates on the principle of actual demand. Work is pulled through the system only when it is needed.

- **Kanban** — Kanban is a popular pull strategy that uses visual signals to manage the flow of work.
- **Lean Manufacturing** — Pull systems are often associated with lean manufacturing principles, which focus on eliminating waste and maximizing efficiency.

> [Imagen decorativa: dos fotos ilustrativas, un tablero Kanban con notas adhesivas de colores y una línea de producción con tarjetas naranjas.]

### Página 17 — Push vs. Pull Strategies

Push and pull are two contrasting shop floor control strategies that offer different approaches to managing the flow of work.

| Push | Pull |
|---|---|
| Work is pushed through the system based on a predetermined schedule or forecast. | Work is pulled through the system based on actual demand. |
| Can lead to excess inventory and waste. | Reduces waste and inventory levels. |
| Less responsive to changes in demand. | More responsive to changes in demand. |

> [Imagen decorativa: ilustración generada por IA de un diagrama de procesos con texto ilegible.]

### Página 18 — Understanding Kanban

Kanban is a popular shop floor control strategy that relies on visual signals to manage the flow of work. It uses cards, boards, and signals to communicate task status and control inventory levels.

1. **Definition of Kanban** — Kanban is a shop floor control strategy that relies on visual signals to manage the flow of work. It uses cards, boards, and signals to communicate task status and control inventory levels.
2. **Origins and Principles** — Kanban originated in Toyota's production system and is based on the principle of pulling work through the system based on actual demand.
3. **How Kanban Works in Flowshop Systems** — In a flowshop system, Kanban can be used to track the movement of jobs through workstations, ensuring that each workstation only pulls in work when it is ready for it.
4. **Benefits of Using Kanban** — Kanban can improve efficiency by reducing work-in-progress, identifying bottlenecks, and enabling faster response times.

> [Imagen decorativa: tablero Kanban con notas adhesivas de colores.]

### Página 19 — (sin título) Push, Kanban y ConWIP

> [Diagrama: tres líneas de producción idénticas, cada una con la secuencia **Workstation → Buffer → Workstation → Buffer → Workstation → Buffer →** (rectángulo = estación, triángulo = buffer). Lo que cambia es el flujo de información (flechas punteadas):
> - **Push:** una sola flecha punteada «Production order» entra a la primera estación. La orden de producción empuja el material por toda la línea, sin señal de regreso.
> - **Kanban:** tres flechas punteadas curvas rotuladas «Kanban Card». Cada una va del buffer de salida de una estación de vuelta a esa misma estación: cada estación produce solo cuando su buffer consume una tarjeta (control local, etapa por etapa).
> - **ConWIP:** una sola flecha punteada larga, «ConWIP Card», va del buffer final de la línea de vuelta a la primera estación: el trabajo en proceso total de la línea queda limitado por un número fijo de tarjetas (control global).
> Leyenda: rectángulo = **Workstation**; triángulo = **Buffer**; flecha continua = **Physical flow**; flecha punteada = **Information flow**.]

### Página 20 — Definition and Origins of Kanban

Kanban, meaning "signboard" or "card" in Japanese, originated in Toyota's production system in the 1940s. It evolved from a system used to manage production in the automotive industry.

1. **Early Stages** — In the early days of Toyota, production was often chaotic and inefficient. Kanban was developed as a way to improve the flow of work and reduce waste.
2. **Development of the Kanban System** — Kanban initially involved the use of physical cards to track the movement of parts and materials through the production line.
3. **Evolution of Kanban** — The Kanban system has evolved over time, with the introduction of digital tools and software to manage tasks and processes.

> [Imagen decorativa: notas adhesivas sobre una pared.]

### Página 21 — Principles and Benefits of Kanban in Flowshop Systems

Kanban's principles and benefits, when applied to flowshop systems, contribute to a more efficient and responsive production environment.

1. **Visual Signal** — Kanban uses visual signals to communicate the status of work, facilitating better visibility and coordination.
2. **Pull System** — Kanban operates on a pull system, where workstations pull in work only when they are ready, reducing unnecessary work-in-progress.
3. **Continuous Improvement** — Kanban promotes continuous improvement by encouraging teams to identify bottlenecks and optimize processes.

> [Imagen decorativa: ilustración isométrica de una oficina con un tablero Kanban; sello «Made with Gamma».]

### Página 22 — Conclusion: Choosing the Right Strategy

The choice between push, pull, and Kanban strategies depends on various factors, including production volume, product complexity, and customer demand.

1. **Push** — Suitable for high-volume production with standardized products and a stable demand.
2. **Pull** — More appropriate for products with variable demand and a focus on reducing waste.
3. **Kanban** — A versatile option that can be implemented in various settings, offering flexibility and adaptability.

> [Imagen decorativa: ilustración generada por IA con flechas y círculos y texto sin sentido («Peeslicn», «Pulsn», «Pedeng»).]


---

<!-- fuente: corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/tarea-ensayo-linkedin-operations-manager.md -->
# tarea-ensayo-linkedin-operations-manager

> **Archivo:** [`tarea-ensayo-linkedin-operations-manager.docx`](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/tarea-ensayo-linkedin-operations-manager.docx) · **Corte 1** · Documento de Word  
> **Nombre original:** `CORTE 1/TAREAS/CLASE 1 LINKEDIN/ENYAYO LIKEDIN.docx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Qué es:** la entrega del estudiante para la **Homework 1** del curso PPCO (2026), que se asigna en la página 44 de [L01](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L01-introduccion-al-curso.md). Es un ensayo corto en Word que compara dos ofertas laborales de LinkedIn para cargos de gestión de operaciones en Colombia y elige una. No tiene tablas, imágenes ni cálculos: solo texto con títulos.

Recordatorio del enunciado (L01, p. 44):

- Buscar en LinkedIn dos empleos relacionados con gestión de operaciones («production» y «operations manager»).
- Analizar las responsabilidades, los beneficios y la empresa.
- Decir cuál es mejor y por qué (salario, responsabilidades, ubicación, crecimiento, etc.) y si se aceptaría el trabajo.
- Escribir un ensayo de 1 página con la plantilla de Virtual Sabana.

**Estructura:**

1. **Portada:** título «Análisis de Ofertas Laborales: Operations Manager en Colombia», autor, «PPCO | Micros», profesor William Javier Guerrero Rueda y año 2026.
2. **Oferta 1 — Operations Manager en Lean Solutions Group** (Título 1): contexto, datos de la oferta, responsabilidades, por qué elegirla y por qué no (Título 2).
3. **Oferta 2 — Subgerente de Operaciones en Falabella**, con las mismas subsecciones.
4. **Conclusión:** la elección y sus razones.
5. **Referencias:** formato tipo APA, con los enlaces de LinkedIn.

**Datos que usa:** los anuncios publicados en LinkedIn en julio de 2026 (referencias al final del documento). El ensayo no da cifras de salario, aunque afirma que la Oferta 1 «ofrece el salario más alto del mercado para este perfil».

| Aspecto | Oferta 1: Lean Solutions Group | Oferta 2: Falabella |
|---|---|---|
| Cargo | Operations Manager | Subgerente de Operaciones |
| Sector | BPO (Business Process Outsourcing) | Retail / multitienda (presencia en 5 países de Latinoamérica) |
| Ubicación | Barranquilla, Atlántico (presencial) | Bogotá, D.C. (presencial) |
| Tipo | Tiempo completo, Mid-Senior level | Tiempo completo, Mid-Senior level |
| Inglés | Requerido (clientes en EE. UU.) | No requerido |
| Responsabilidades | Eficiencia operacional, control financiero y rentabilidad; liderar equipos alineados a la estrategia; contacto principal con clientes de EE. UU.; calidad del servicio y solución de problemas diarios | Coordinar operaciones de tiendas y logística regional; optimizar inventario, distribución y servicio al cliente; gestionar el presupuesto operativo y reportar a la gerencia; supervisar supervisores y personal en varias sedes |
| A favor | Salario más alto más bonos por metas; exposición internacional; el sector BPO crece a doble dígito; perfil gerencial integral (finanzas, operaciones, clientes); se gana dominio del inglés | Empresa estable con décadas de trayectoria; sin requisito de inglés; beneficios (seguro médico, descuentos, tarjeta Falabella); Bogotá ofrece más opciones de vida; el retail demanda gerentes operativos |
| En contra | Exige inglés avanzado; posible reubicación a Barranquilla; alta presión, métricas estrictas y horarios exigentes; menos estabilidad que una multinacional | Crecimiento más lento por la jerarquía corporativa; sin exposición internacional; rol más acotado a logística, sin visión integral |

**Métodos:** comparación cualitativa de pros y contras con los criterios que pide la tarea: salario y beneficios, responsabilidades, ubicación, crecimiento, idioma y estabilidad. No usa ponderaciones ni puntajes.

**Resultados clave:** el autor elige **Operations Manager en Lean Solutions Group**. Sus cinco razones son:

1. Salario significativamente más alto, sobre todo con los bonos.
2. Exposición a clientes internacionales.
3. El inglés como activo profesional a largo plazo.
4. Un perfil gerencial más completo (finanzas, operaciones y clientes).
5. La expansión del sector BPO en Colombia.

**Conclusiones:** Lean Solutions Group es la mejor opción para crecer y ganar dinero. Falabella queda como alternativa sólida si el inglés es una barrera insalvable o si se prefiere un entorno corporativo con horarios más predecibles.

**Supuestos y advertencias:**

- Las afirmaciones sobre el salario («el más alto del mercado»), los bonos y los beneficios de Falabella no traen cifras ni fuente distinta del anuncio. Este repo no puede verificarlas.
- Las dos ofertas no corresponden exactamente a las búsquedas «production» y «operations manager» del enunciado: ambas son cargos de gerencia de operaciones.
- La referencia de Falabella apunta a una búsqueda de LinkedIn, no a un anuncio concreto.
- El enunciado pide un «1-page essay», pero según los metadatos del .docx el documento tiene **6 páginas** (767 palabras), con 2 saltos de página manuales (portada separada).
- Hay un error menor de tilde en la conclusión: «yo me iria» (debería ser «iría»).
- Relación con el curso: ilustra las funciones del gerente de operaciones de L01 (p. 32–33, 42–43): control de costos y calidad, finanzas, liderazgo de equipos y relación con clientes.

## Texto completo

Análisis de Ofertas Laborales:

Operations Manager en Colombia

Samuel Gómez

PPCO | Micros

Prof. William Javier Guerrero Rueda

2026

### Oferta 1: Operations Manager en Lean Solutions Group

Lean Solutions Group es una empresa de BPO (Business Process Outsourcing) con operaciones en Barranquilla, Atlántico. La oferta fue publicada en LinkedIn en julio de 2026 y corresponde a un cargo de tiempo completo, nivel mid-senior, con modalidad presencial.

#### Datos de la oferta

Empresa: Lean Solutions Group

Ubicación: Barranquilla, Atlántico (presencial)

Tipo: Tiempo completo - Mid-Senior level

Inglés: Requerido (clientes en Estados Unidos)

#### Responsabilidades

Asegurar la eficiencia operacional, el control financiero y la rentabilidad general del negocio.

Liderar equipos operativos y alinear la ejecución con los objetivos estratégicos de la organización.

Ser el principal punto de contacto en la relación con clientes externos estadounidenses.

Garantizar la calidad del servicio y la resolución efectiva de problemas operativos del día a día.

#### Análisis: por qué elegir esta oferta

Ofrece el salario más alto del mercado para este perfil, complementado con bonos por cumplimiento de metas.

Brinda exposición internacional al trabajar con clientes de Estados Unidos, lo que desarrolla competencias interculturales.

El sector BPO en Colombia presenta un crecimiento anual de doble dígito, lo que se traduce en múltiples oportunidades de ascenso.

La responsabilidad del cargo abarca finanzas, operaciones y relación con clientes, formando un perfil gerencial integral.

El dominio del inglés que se adquiere en este rol es un diferenciador significativo en el mercado laboral.

#### Análisis: por qué NO elegir esta oferta

Requiere nivel avanzado de inglés, lo cual puede ser una barrera real para muchos profesionales.

Implica reubicación en Barranquilla si el candidato no reside en esa ciudad.

El entorno BPO se caracteriza por alta presión, métricas estrictas y horarios exigentes.

La estabilidad laboral es menor en comparación con una corporación multinacional establecida.

### Oferta 2: Subgerente de Operaciones en Falabella

Falabella es una cadena multitienda con presencia en cinco países de Latinoamérica. La oferta fue publicada en LinkedIn en julio de 2026 para la ciudad de Bogotá, en la modalidad presencial y con nivel mid-senior.

#### Datos de la oferta

Empresa: Falabella (Retail / Multitienda)

Ubicación: Bogotá, D.C. (presencial)

Tipo: Tiempo completo - Mid-Senior level

Inglés: No requerido

#### Responsabilidades

Coordinar las operaciones de tiendas y la logística en la región asignada.

Optimizar procesos de inventario, distribución y servicio al cliente.

Gestionar el presupuesto operativo y reportar resultados a la gerencia general.

Supervisar equipos de supervisores y personal operativo en múltiples sedes.

#### Análisis: por qué elegir esta oferta

Falabella es una empresa estable con presencia en cinco países y trayectoria de décadas.

No requiere dominio del inglés, lo que la hace accesible a un mayor número de candidatos.

Ofrece beneficios corporativos atractivos: seguro médico, descuentos y tarjeta Falabella.

Bogotá ofrece mayores opciones de vivienda, educación y entretenimiento.

La experiencia en retail es valiosa, pues el sector tiene alta demanda de gerentes operativos.

#### Análisis: por qué NO elegir esta oferta

El crecimiento profesional es más lento debido a la estructura jerárquica corporativa.

No ofrece exposición internacional, lo que limita el desarrollo de competencias globales.

La responsabilidad del cargo está más acotada al área logística, sin visión integral del negocio.

### Conclusión

Tras analizar ambas ofertas, yo me iria por la de Operations Manager en Lean Solutions Group por las siguientes razones:

El salario es significativamente más alto, especialmente al considerar los bonos por cumplimiento.

La exposición a clientes internacionales desarrolla habilidades altamente valoradas en el mercado global.

El dominio del inglés que se adquiere representa un activo profesional invaluable a largo plazo.

La responsabilidad sobre finanzas, operaciones y clientes forma un perfil gerencial mucho más completo y competitivo.

El sector BPO en Colombia está en expansión, lo que multiplica las oportunidades de crecimiento profesional.

No obstante, si el idioma inglés representa una barrera insalvable o se prefiere un entorno corporativo tradicional con horarios más predecibles, Falabella constituye una alternativa sólida que ofrece estabilidad y beneficios competitivos.

### Referencias

Lean Solutions Group. (2026, julio). Operations Manager [Anuncio de empleo]. LinkedIn. https://www.linkedin.com/jobs/view/4410211764/

Falabella. (2026, julio). Subgerente de Operaciones [Anuncio de empleo]. LinkedIn. https://co.linkedin.com/jobs/search/?keywords=Subgerente%20de%20Operaciones&location=Colombia

LinkedIn Corporation. (2026). LinkedIn Jobs: Operations Manager en Colombia. https://www.linkedin.com/jobs/search/?keywords=Operations%20Manager&location=Colombia
