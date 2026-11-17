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
| [L01-introduccion-al-curso.md](./L01-introduccion-al-curso.md) | Lecture 1 (46 diapositivas). **Programa del curso**: profesor, objetivo, ABET, rúbrica, plan de estudios de Ingeniería Industrial, reglas, **porcentajes de evaluación**, proyectos en grupo, qué es OM, las 10 decisiones estratégicas, un ejemplo numérico de estrategias y la tarea 1. Al inicio del resumen hay una ficha rápida del curso. | **Sí, primero** (reglas y evaluación del curso) |
| [L02-introduction-to-production-systems.md](./L02-introduction-to-production-systems.md) | Lecture 2 (22 diapositivas, hechas con Gamma). Reglas de debate, lectura recomendada (*Factory Physics*, cap. 1), flowshop, jobshop y openshop, WIP, *takt time*, *throughput*, *cycle time*, *lead time*, push vs. pull, Kanban y ConWIP. | Segundo |
| [tarea-ensayo-linkedin-operations-manager.md](./tarea-ensayo-linkedin-operations-manager.md) | Entrega de la Homework 1 (Word): compara la oferta de Operations Manager de Lean Solutions Group (Barranquilla, BPO) con la de Subgerente de Operaciones de Falabella (Bogotá, retail) y elige la primera. | Opcional |

## Orden de estudio sugerido
1. **L01, páginas 1–24:** cómo funciona el curso. Las reglas están en la p. 9, las notas en la p. 22, los grupos en la p. 23, los proyectos en la p. 24 y la rúbrica en la p. 6.
2. **L01, páginas 25–46:** qué es OM, las 10 decisiones estratégicas y el ejemplo de la p. 41. Termina con la tarea 1 (p. 44).
3. **Tarea:** el ensayo de LinkedIn, como ejemplo de entrega.
4. **L02:** configuraciones de producción y control de piso. Es el vocabulario base que se retoma en el corte 3 (scheduling).

## Conceptos y fórmulas clave

- **Evaluación del curso** (detalle en [L01, p. 22](./L01-introduccion-al-curso.md)):
  - Pesos de los cortes: corte 1 = 30 %, corte 2 = 30 %, corte 3 = 40 %.
  - Dentro de cada corte: examen 60 %, actividades en clase 10 %, proyecto 30 %. En el corte 3 el examen es final acumulativo.
  - Sobre la nota final: exámenes 60 %, actividades 10 %, proyectos 30 %.
- **Reglas** ([L01, p. 9](./L01-introduccion-al-curso.md)): asistir a clase (20 %), fechas de entrega inamovibles, aprendizaje basado en la experiencia, plagio prohibido y citación obligatoria. Los proyectos se hacen en grupos de hasta 5 personas, con vestimenta profesional en las presentaciones.
- **Ejemplo de estrategias** ([L01, p. 41](./L01-introduccion-al-curso.md), Heizer et al. 2017):

  $$\text{Utilidad} = (1-t)\,\big[(V - C_p) - C_f\big]$$

  donde $V$ son las ventas, $C_p$ el costo de producción, $C_f$ el costo financiero y $t=0.25$ la tasa de impuestos. Reducir $C_p$ un 20 % da una utilidad de 22,500, frente a 18,000 al subir las ventas un 50 % y 12,750 al bajar $C_f$ un 50 %. La utilidad actual es 10,500.
- **Configuraciones** ([L02](./L02-introduction-to-production-systems.md)):
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
| Comparación de estrategias de mercadeo, finanzas y operaciones (estado de resultados) | [L01, p. 41](./L01-introduccion-al-curso.md) | La estrategia de operaciones (−20 % en costos) da la mayor utilidad: 22,500 |
| Cálculo del peso efectivo de cada componente en la nota final | [L01, p. 22](./L01-introduccion-al-curso.md) | Exámenes 60 %, actividades 10 %, proyectos 30 % |
| Homework 1: análisis de dos ofertas laborales de LinkedIn | [tarea-ensayo-linkedin-operations-manager.md](./tarea-ensayo-linkedin-operations-manager.md) | Se elige Operations Manager en Lean Solutions Group |
| Rutas de producción (ejemplo de jobshop con 3 referencias y 3 estaciones) | [L02, p. 5](./L02-introduction-to-production-systems.md) | Ref 1: A→C; ref 2: B→A→C; ref 3: C→A→B |

## Relación con otros temas y proyectos

- **Pronósticos** (meta 1 del semestre: «Forecast sales»):
  - Siguiente carpeta: [02-introduccion-a-pronosticos](../02-introduccion-a-pronosticos/).
  - Luego el resto del corte 1, hasta el [parcial 1](../parcial-1/) y el [proyecto THYMS de pronóstico](../proyecto-thyms-pronostico/).
- **Planeación** (criterio 3 de la rúbrica, «plan estratégico»; lógica push basada en pronósticos):
  - [Corte 2 — planeación agregada](../../corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/)
  - [BOM y MRP](../../corte-2-planeacion-agregada-mrp/04-bom-y-mrp/)
  - [MRP II](../../corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/)
- **Programación de la producción** (criterio 4 de la rúbrica; decisión estratégica 9; configuraciones de L02):
  - [Corte 3 — introducción a scheduling](../../corte-3-programacion-scheduling/01-introduccion-scheduling/)
  - [flow shop](../../corte-3-programacion-scheduling/04-flow-shop/)
  - [job shop](../../corte-3-programacion-scheduling/05-job-shop/)
  - [competencia de scheduling](../../corte-3-programacion-scheduling/proyecto-competencia-scheduling/)
