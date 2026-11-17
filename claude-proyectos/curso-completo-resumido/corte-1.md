# Corte 1: Introducción y pronósticos de demanda

Primer corte del curso (30 % de la nota final). Empieza con la presentación del curso y los sistemas de producción. Luego cubre los **métodos de pronóstico**: primero graficar y diagnosticar la serie (autocorrelación), después elegir un método según el patrón de la serie y, por último, medir el error.

```
¿Qué patrón tiene la serie?  (graficar, correlograma, Ljung-Box)
 ├─ estacionaria / aleatoria → promedio móvil, promedio ponderado, SES
 ├─ con tendencia            → Holt (suavización doble), regresión
 ├─ con estacionalidad       → Winters (multiplicativo / aditivo)
 ├─ estructura autorregresiva → ARIMA (Box-Jenkins)
 └─ sin datos históricos     → métodos cualitativos (Delphi, jurado, fuerza de ventas)
Control del pronóstico: MAD, MSE, MAPE, señal de rastreo
```

## Temas (en orden de clase)

| # | Carpeta | Clase | Qué cubre | Ejercicios en la carpeta |
|---|---|---|---|---|
| 01 | [`01-introduccion-curso-y-sistemas-de-produccion/`](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/README.md) | [L01](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L01-introduccion-al-curso.md), [L02](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L02-introduction-to-production-systems.md) | **Programa del curso, evaluación y reglas**; qué es Operations Management; flow shop, job shop y open shop; WIP, takt, throughput; push/pull, Kanban, ConWIP | Tarea 1: ensayo sobre ofertas de LinkedIn |
| 02 | [`02-introduccion-a-pronosticos/`](/corte-1-pronosticos/02-introduccion-a-pronosticos/README.md) | [L03](/corte-1-pronosticos/02-introduccion-a-pronosticos/L03-introduction-to-forecasting.md) | Tipos y horizontes de pronóstico, etapas, clasificación de métodos, patrones de demanda | — |
| 03 | [`03-graficas-y-autocorrelacion/`](/corte-1-pronosticos/03-graficas-y-autocorrelacion/README.md) | [L04](/corte-1-pronosticos/03-graficas-y-autocorrelacion/L04-plotting-your-data.md) | Correlograma (ACF) y límites de significancia, **Ljung-Box**, histograma, boxplot, dispersión, PCA | Excel de 30.000 ventas con rezagos y 4 tareas "Class example" (aleatoria, tendencia, estacionalidad de periodo 2) |
| 04 | [`04-datos-estacionarios-promedio-movil-y-suavizacion-simple/`](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/README.md) | [L05](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md) | **Promedio móvil**, promedio ponderado, **SES** y medidas de error (MAD, SSE, MSE, MAPE, PME) | Comparación PM(6)/PM(12)/SES(0,2)/SES(0,8) y la práctica del parcial 1 |
| 05 | [`05-tendencia-suavizacion-doble-holt/`](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/README.md) | [L06](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/L06-forecasting-data-with-trend.md) | **Holt**, inicialización (regresión o estaciones), regresión lineal y R² | Holt con Solver sobre 8 trimestres |
| 06 | [`06-estacionalidad-winters-y-tracking-signal/`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/README.md) | [L07](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md) | **Winters** multiplicativo y aditivo, **señal de rastreo**, RSFE, intervalo de confianza, comparación de métodos | Ejemplo de llantas con Winters y correlograma |
| 07 | [`07-arima/`](/corte-1-pronosticos/07-arima/README.md) | [L08](/corte-1-pronosticos/07-arima/L08-forecasting-with-arima.md) | Box-Jenkins: AR(1), AR(2), MA(1), ARMA(1,1) | — |
| 08 | [`08-metodos-cualitativos/`](/corte-1-pronosticos/08-metodos-cualitativos/README.md) | [L09](/corte-1-pronosticos/08-metodos-cualitativos/L09-qualitative-forecasting-methods.md) | Jurado ejecutivo, Delphi, fuerza de ventas, encuesta de mercado, cuestionarios | — |

## Evaluaciones y proyecto

- **[`parcial-1/`](/corte-1-pronosticos/parcial-1/README.md)**: datos del parcial (48 meses), Excel de cálculos (descriptivos, correlograma, Holt) e informe Word con la elección del método y el pronóstico de los meses 49 a 60. La práctica previa está en el tema 04.
- **[`proyecto-thyms-pronostico/`](/corte-1-pronosticos/proyecto-thyms-pronostico/README.md)**: proyecto del corte sobre THYMS Colombia S.A.S. (tintes en tubo de 60 g). Toma las ventas reales de un vendedor de la zona Antioquia, anonimizadas, y hace un pronóstico con SES (α = 0,05). Calcula además takt time, throughput y WIP. Continúa en el Corte 2 con el gemelo digital: [`../corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/README.md).

## Cómo se evalúa el curso

Según la [L01](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L01-introduccion-al-curso.md):

- Los cortes pesan **30 % / 30 % / 40 %**.
- Dentro de cada corte: **examen 60 %**, **actividades de clase 10 %** y **proyecto 30 %**.

La rúbrica completa y las reglas del curso están en la L01.

## Cuidado con estos errores

Varios Excel de clase tienen errores de fórmula. Los más importantes:
- el Solver del Excel de Holt quedó en «maximizar» el MAD;
- el MAD del Excel de Winters solo promedia el año 1;
- los coeficientes de `tarea-class-example-3` están mal calculados.

Algunas diapositivas también tienen erratas numéricas. Todo está documentado, con la corrección, en [`../ERRATAS.md`](/ERRATAS.md).


---

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


---

<!-- fuente: corte-1-pronosticos/02-introduccion-a-pronosticos/README.md -->
# Introducción a pronósticos y planeación de la demanda (Corte 1)

## Qué cubre
Es la base conceptual de todo el corte 1. Explica:

- Qué es pronosticar y por qué importa (caso Disney; costo de equivocarse en la cadena de suministro, en recursos humanos y en capacidad).
- La analítica descriptiva, predictiva, prescriptiva y autónoma.
- Los tipos de pronóstico según el dato y según el horizonte, y por qué el error crece con el horizonte y con la granularidad.
- Las etapas del proceso de pronóstico (5 etapas y sistema de 8 pasos) y los parámetros de un pronóstico.
- La clasificación de los métodos en cualitativos y cuantitativos, los patrones de demanda (horizontal, tendencia, estacional, cíclico y aleatorio) y los criterios para elegir un método.

No hay ejercicios numéricos: los métodos se desarrollan en las carpetas siguientes.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [L03-introduction-to-forecasting.md](/corte-1-pronosticos/02-introduccion-a-pronosticos/L03-introduction-to-forecasting.md) | Lecture 3 «Introduction to Forecasting & Demand Planning» (35 diapositivas, 2026). Transcripción completa página por página, con la descripción de los gráficos (embudo del error, patrones de demanda, serie del nivel de un lago con tendencia $H=-0.0015t+3016.1$) y un resumen en español. | **Sí** (único archivo) |

## Orden de estudio sugerido
1. **Páginas 2–12:** definición, analítica, propósito (entradas + restricciones = demanda esperada), tipos e importancia.
2. **Páginas 13–19:** servicios, gestión de la demanda, horizontes, factores, hechos y riesgo (el error crece con el horizonte).
3. **Páginas 20–28:** el proceso y las etapas del pronóstico, sus parámetros y la clasificación de los métodos.
4. **Páginas 29–35:** patrones de demanda, práctica de identificación con gráficos, criterios de selección y software.
5. Después sigue [03-graficas-y-autocorrelacion](/corte-1-pronosticos/03-graficas-y-autocorrelacion/), que enseña a graficar los datos para reconocer los patrones.

## Conceptos y fórmulas clave

Todo esto está en detalle en [L03](/corte-1-pronosticos/02-introduccion-a-pronosticos/L03-introduction-to-forecasting.md).

- **Propósito:** entradas (estudios de mercado, históricos, publicidad, opinión experta) + restricciones (políticas, recursos, mercado, tecnología) = demanda esperada por producto, cliente y región.
- **Horizontes:**

  | Horizonte | Alcance | Valor típico | Datos | Para qué sirve |
  |---|---|---|---|---|
  | Corto plazo | ≤ 1 año | 3 meses | diarios u horarios | personal, nivel de producción, inventarios |
  | Mediano plazo | ≤ 3 años | 1 año | mensuales | planes organizacionales y de mercadeo |
  | Largo plazo | > 3 años | 5 años | anuales | productos nuevos, expansiones |

  El corto plazo es el más preciso.
- **Error vs. horizonte** (p. 19): ≈10 % en la semana 1, 20 % en la semana 16 y 40 % en la semana 32.
- **Reglas prácticas:** el pronóstico agregado (por familias) es más preciso; a mayor granularidad (SKU, día), mayor error. Un pronóstico no es una meta: siempre tiene error.
- **Parámetros de un pronóstico:** variable, horizonte, granularidad y frecuencia de actualización.
- **Proceso cíclico:** datos históricos → modelo → pronóstico → estimación del error → ajuste → siguiente periodo.
- **Métodos:**
  - Cualitativos: Delphi y opinión de expertos, para productos nuevos.
  - Cuantitativos: promedios, series de tiempo, suavización exponencial (simple, Holt, Winters multiplicativo), Box-Jenkins (ARIMA), regresión causal y simulación.
- **Patrones de demanda:** horizontal (estacionaria), tendencia, estacionalidad, ciclo y aleatoriedad. En la p. 32 hay un ejemplo de tendencia lineal: $H = -0.0015\,t + 3016.1$, donde $H$ es el nivel del lago en m s. n. m., $t$ el tiempo y $-0.0015$ la pendiente.
- **Qué método usar según el patrón** (relación entre L03, p. 21, y las clases siguientes):

  | Patrón | Método | Dónde se ve |
  |---|---|---|
  | Estacionaria | Promedio móvil, suavización exponencial simple | [04-…](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/) |
  | Con tendencia | Suavización doble (Holt) | [05-…](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/) |
  | Con tendencia y estacionalidad | Suavización triple (Winters) | [06-…](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/) |
  | Series con autocorrelación | Box-Jenkins | [07-arima](/corte-1-pronosticos/07-arima/) |
  | Sin historia (producto nuevo) | Cualitativos (Delphi) | [08-metodos-cualitativos](/corte-1-pronosticos/08-metodos-cualitativos/) |

## Ejercicios resueltos disponibles
La presentación no trae ejercicios numéricos. Tiene ejemplos ilustrativos:

| Ejemplo | Página de L03 | Resultado o mensaje |
|---|---|---|
| Pronósticos electorales de PollyVote (EE. UU. 2004, 2008 y 2012) | p. 4 | Errores entre −1 y +0.9 puntos porcentuales; el pronóstico más cercano a la elección es el más preciso |
| Disney | p. 9 | Error medio del 5 % a 5 años y del 0–3 % a 1 año |
| Embudo del error | p. 19 | 10 % → 20 % → 40 % en las semanas 1, 16 y 32 |
| Identificación de patrones (4 tipos de demanda, nivel de un lago con eventos ENSO, serie creciente 1993–2007) | p. 31–33 | Reconocer tendencia, ciclos, estacionalidad y aleatoriedad |

Los ejercicios numéricos de los métodos están en los Excel de las carpetas 03 a 06, en el [parcial 1](/corte-1-pronosticos/parcial-1/) y en el [proyecto THYMS](/corte-1-pronosticos/proyecto-thyms-pronostico/).

## Relación con otros temas y proyectos

- **Anterior:** [01-introduccion-curso-y-sistemas-de-produccion](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/). En L01, la meta 1 del semestre es «Forecast sales» y los criterios 1–2 de la rúbrica evalúan el análisis gráfico y la evaluación crítica de los pronósticos.
- **Siguientes del corte 1:**
  - [03-graficas-y-autocorrelacion](/corte-1-pronosticos/03-graficas-y-autocorrelacion/)
  - [04-datos-estacionarios-promedio-movil-y-suavizacion-simple](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/)
  - [05-tendencia-suavizacion-doble-holt](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/)
  - [06-estacionalidad-winters-y-tracking-signal](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/)
  - [07-arima](/corte-1-pronosticos/07-arima/)
  - [08-metodos-cualitativos](/corte-1-pronosticos/08-metodos-cualitativos/)
- **Aplicación:**
  - [parcial-1](/corte-1-pronosticos/parcial-1/)
  - [proyecto-thyms-pronostico](/corte-1-pronosticos/proyecto-thyms-pronostico/): pronóstico de la demanda real de una empresa.
- **Corte 2:**
  - El pronóstico de demanda es la entrada de la [planeación agregada](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/).
  - La idea de que agregar reduce el error se retoma en [agregación y desagregación](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/).


---

<!-- fuente: corte-1-pronosticos/02-introduccion-a-pronosticos/L03-introduction-to-forecasting.md -->
# L03-introduction-to-forecasting

> **Archivo:** [`L03-introduction-to-forecasting.pdf`](/corte-1-pronosticos/02-introduccion-a-pronosticos/L03-introduction-to-forecasting.pdf) · **Corte 1** · 35 páginas  
> **Nombre original:** `CORTE 1/Lec 3 - introduction to forecasting.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** introducción conceptual a los pronósticos y a la planeación de la demanda: qué es pronosticar, para qué sirve, tipos de pronóstico, etapas del proceso, patrones de demanda y familias de métodos (Lecture 3 del curso, 2026).

**Ideas clave:**

- Pronosticar es «el arte o la ciencia de predecir eventos futuros»: buscar la mejor estimación posible bajo incertidumbre. Se puede pronosticar con datos históricos, con predicciones subjetivas o intuitivas, o con datos impulsados por la demanda (*demand-driven*).
- La cadena de suministro *demand driven* hace fluir la información desde el cliente hacia los proveedores y los productos en sentido contrario.
- La analítica (descriptiva → predictiva → prescriptiva → autónoma) da más ventaja competitiva cuanto más sofisticada es. El pronóstico (*forecasting/extrapolation*) está en el nivel **predictivo**.
- Ejemplo de motivación: Disney (ingresos de 55.63 mil millones USD en 2016) pronostica a diario, semanal, mensual, anual y a 5 años, con datos de 3,000 colegios (vacaciones). Error medio del 5 % a 5 años y del 0–3 % a 1 año. Con eso planea comida, bebidas, horarios y personal.
- Propósito: **entradas** (estudios de mercado, históricos, publicidad, opinión experta) **+ restricciones** (políticas, recursos, mercado, tecnología) **= demanda esperada** (por producto, cliente y región).
- Tipos según el dato: económico, tecnológico y **de demanda**, que es el del curso. Pronosticar la demanda no es lo mismo que pronosticar las ventas: las ventas solo registran la demanda que se atendió.
- La demanda afecta a toda la empresa: cadena de suministro ($$), recursos humanos ($$$) y capacidad ($$$$).
- En servicios se necesita información de muy corto plazo (cada 15 minutos) y conviene seguir los eventos de la zona.
- La gestión de la demanda busca modificar sus patrones con productos complementarios de ciclo opuesto, promociones, citas y reservas, *revenue management* y *backlog/backorder*.
- Horizonte: corto (≤ 1 año, típico 3 meses), mediano (≤ 3 años, típico 1 año) y largo (> 3 años, típico 5 años). El corto plazo usa más métodos matemáticos y es más preciso.
- Hechos: el error es inevitable y crece con el horizonte (≈10 % en la semana 1, 20 % en la 16 y 40 % en la 32). Muchos métodos suponen estabilidad. Agregar por familias reduce el error, y la mayor granularidad (SKU, día) lo aumenta.
- Proceso cíclico: datos históricos → modelo → pronóstico → estimación del error → retroalimentación y ajuste del modelo → siguiente periodo.
- Hay dos marcos de pasos: las **5 etapas** (fijar objetivo, preparar datos, evaluar y seleccionar la técnica, correr el pronóstico, hacerle seguimiento) y el **sistema de 8 pasos** (uso, ítems, horizonte, modelo, datos, análisis, pronóstico, validación).
- Parámetros de un pronóstico: variable, horizonte, granularidad y frecuencia de actualización.
- Métodos **cualitativos** (subjetivos, p. ej. Delphi; útiles para productos nuevos) y **cuantitativos**: promedios, series de tiempo, suavización exponencial (simple, doble de Holt, triple de Winters multiplicativo), Box-Jenkins (ARIMA), regresión causal y simulación.
- Patrones de demanda: horizontal (estacionaria), tendencia, estacional, cíclico y aleatorio.
- El método se elige según las características de la demanda, la complejidad, la precisión y la etapa del ciclo de vida. Un pronóstico no es una meta que haya que cumplir: siempre tiene error.
- Software mencionado: R, Matlab, SPSS y Minitab.

**Fórmulas y métodos:**

La presentación es conceptual. La única ecuación aparece en el gráfico de la página 32: la tendencia lineal del nivel de un lago,

$$H = -0.0015\,t + 3016.1$$

donde $H$ es el nivel del lago en m s. n. m., $t$ es el tiempo (deducido: en meses) y $-0.0015$ es la pendiente, es decir, cuánto baja el nivel por periodo. Sirve como ejemplo de **componente de tendencia** de una serie.

Métodos que se nombran (se desarrollan en las clases siguientes):

| Familia | Método | Cuándo se usa (según la presentación) | Dónde se ve en detalle |
|---|---|---|---|
| Cualitativo | Delphi / opinión de expertos | Productos nuevos, sin historia; relaciones causa-efecto | [L09](/corte-1-pronosticos/08-metodos-cualitativos/L09-qualitative-forecasting-methods.md) |
| Cuantitativo | Promedios (promedio móvil) | Demanda horizontal o estacionaria | [L05](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md) |
| Cuantitativo | Suavización exponencial simple | Demanda estacionaria | [L05](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md) |
| Cuantitativo | Suavización doble (Holt) | Demanda con tendencia | [L06](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/L06-forecasting-data-with-trend.md) |
| Cuantitativo | Suavización triple (Winters multiplicativo) | Demanda con tendencia y estacionalidad | [L07](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md) |
| Cuantitativo | Box-Jenkins (ARIMA) | Series de tiempo con autocorrelación | [L08](/corte-1-pronosticos/07-arima/L08-forecasting-with-arima.md) |
| Cuantitativo causal | Regresión | Cuando la demanda depende de otras variables | — |
| Cuantitativo | Simulación | Se menciona sin desarrollar | — |

**Ejemplos resueltos:** no hay ejercicios numéricos. Hay ejemplos ilustrativos:

- Página 4: tabla de PollyVote con pronósticos y resultados reales de las elecciones de EE. UU. 2004, 2008 y 2012. Los errores van de −1 a +0.9 puntos, y el pronóstico final es el que más se acerca. También aparece un tablero de ventas acumuladas (total 80,575 repartido en 4 productos).
- Página 9: caso Disney (error del 5 % a 5 años y del 0–3 % a 1 año).
- Página 19: el error crece con el horizonte (10 % → 20 % → 40 %).
- Páginas 31–33: gráficos para identificar patrones: cuatro tipos de demanda, el nivel de un lago con tendencia $H=-0.0015t+3016.1$ y eventos ENSO, y una serie creciente de 1993 a 2007.

**Páginas clave:**

- Definición y objetivos: páginas 2–3.
- Analítica: páginas 6–8.
- Propósito, tipos e importancia: páginas 10–12.
- Servicios y gestión de la demanda: páginas 13–14.
- Horizontes: páginas 15–16.
- Factores y hechos: páginas 17–18.
- Error vs. horizonte: página 19.
- Proceso, etapas y 8 pasos: páginas 20–23.
- Recomendaciones y parámetros: páginas 24–25.
- Clasificación de métodos: páginas 27–28.
- Patrones de demanda: páginas 29–33.
- Criterios de selección: página 34.
- Software: página 35.

**Relación con otros archivos del repo:**

- Siguiente tema: graficar los datos e identificar patrones y autocorrelación, en [L04 y sus ejercicios](/corte-1-pronosticos/03-graficas-y-autocorrelacion/L04-plotting-your-data.md).
- Métodos cuantitativos aplicados en Excel:
  - [promedio-movil-y-suavizacion-exponencial](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/promedio-movil-y-suavizacion-exponencial.md)
  - [suavizacion-exponencial-doble-holt](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/suavizacion-exponencial-doble-holt.md)
  - [metodo-winters](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/metodo-winters.md)
- Aplicación integral: [parcial 1](/corte-1-pronosticos/parcial-1/parcial-1-informe.md) y el [proyecto THYMS de pronóstico](/corte-1-pronosticos/proyecto-thyms-pronostico/Planeacion_proyecto_corte1.md).
- La idea de que agregar por familias reduce el error se retoma en [agregación y desagregación (corte 2)](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md). El pronóstico de demanda es la entrada de la [planeación agregada](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md).


---

<!-- fuente: corte-1-pronosticos/03-graficas-y-autocorrelacion/README.md -->
# Gráficas de los datos y autocorrelación (Corte 1)

## Qué cubre
Antes de elegir un método de pronóstico hay que **graficar y entender los datos**. Esta carpeta enseña a usar el histograma, la serie de tiempo, el boxplot, el diagrama de dispersión $X_t$ frente a $X_{t-1}$ y, sobre todo, el **correlograma** (coeficientes de autocorrelación por rezago con límites de significancia) para reconocer si una serie es aleatoria, tiene tendencia o tiene estacionalidad. Incluye también la prueba de Ljung-Box y una introducción al análisis de componentes principales (PCA) para agrupar tiendas o productos con comportamiento parecido. Los Excel son una hoja de clase con 30.000 ventas y la tarea «Pronósticos de demandas»: cuatro ejemplos con patrones distintos (series aleatorias, dos series con tendencia y una con estacionalidad de periodo 2).

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [L04-plotting-your-data.md](/corte-1-pronosticos/03-graficas-y-autocorrelacion/L04-plotting-your-data.md) | Lecture 4 «Plotting your data» (31 diapositivas): tipos de gráfico, fórmula de $r_k$, ejemplo numérico de autocorrelación, límites de significancia, lectura del correlograma, Ljung-Box, Minitab/Tableau y PCA de 15 tiendas. | **Sí** |
| [graficas-pronosticos-ventas-autocorrelacion.md](/corte-1-pronosticos/03-graficas-y-autocorrelacion/graficas-pronosticos-ventas-autocorrelacion.md) | Excel de clase: 30.000 ventas (0–22, media 8) con 20 rezagos, matriz de correlación, autocorrelograma, serie y dispersión. Serie aleatoria. | Segundo |
| [tarea-class-example-1.md](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-1.md) | Tarea, ejemplo 1: ventas propias y de la competencia (1.923 días, 2014–2019) con rezagos, coeficientes con límites, histograma, boxplot (atípicos 31.624, 12, 9 y 2) y dispersión. Series aleatorias. | Tercero |
| [tarea-class-example-2.md](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-2.md) | Tarea, ejemplo 2: tres productos; análisis completo del producto 1 con fórmulas vivas (ACF hasta el rezago 88, histograma de 40 clases, boxplot, regresión $X_t$–$X_{t-1}$). Serie con tendencia. | Cuarto (el más completo) |
| [tarea-class-example-3.md](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-3.md) | Tarea, ejemplo 3: 301 datos con tendencia creciente. Los coeficientes de la hoja están mal calculados (incluyen la columna índice); el .md trae los correctos. | Quinto |
| [tarea-class-example-4.md](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-4.md) | Tarea, ejemplo 4: 500 datos que alternan alto/bajo (zigzag); coeficientes ±0,85 que cambian de signo → estacionalidad de periodo 2. | Sexto |

Cada Excel tiene, además, una carpeta `*-datos/` con el CSV completo de sus hojas largas: [graficas-pronosticos-ventas-autocorrelacion-datos/DATOS.csv](/corte-1-pronosticos/03-graficas-y-autocorrelacion/graficas-pronosticos-ventas-autocorrelacion-datos/DATOS.csv), [tarea-class-example-1-datos/](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-1-datos/) (`Ventas_propias.csv`, `Ventas_competencia.csv`), [tarea-class-example-2-datos/](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-2-datos/) (`DATOS.csv`, `DATOS_ACF.csv`, `DISPERSION.csv`), [tarea-class-example-3-datos/Ventas.csv](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-3-datos/Ventas.csv) y [tarea-class-example-4-datos/Datos.csv](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-4-datos/Datos.csv).

## Orden de estudio sugerido
1. [L04](/corte-1-pronosticos/03-graficas-y-autocorrelacion/L04-plotting-your-data.md), p. 1–5: para qué graficar y qué gráficos usar.
2. L04, p. 6–14: fórmula de $r_k$, ejemplo de 6 datos y límites de significancia.
3. L04, p. 15–18: cómo leer el correlograma (tendencia, estacionalidad, aleatoriedad) y la prueba de Ljung-Box.
4. [graficas-pronosticos-ventas-autocorrelacion](/corte-1-pronosticos/03-graficas-y-autocorrelacion/graficas-pronosticos-ventas-autocorrelacion.md): cómo armar la tabla de rezagos y la matriz de correlación en Excel; ejemplo de serie aleatoria.
5. Los cuatro ejemplos de la tarea, comparando su correlograma: [1](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-1.md) (aleatoria, con atípicos), [2](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-2.md) (tendencia, todo con fórmulas), [3](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-3.md) (tendencia, con un error instructivo) y [4](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-4.md) (estacionalidad de periodo 2).
6. L04, p. 19–31: software y PCA.
7. Siguiente tema: [04 — datos estacionarios](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/README.md).

## Conceptos y fórmulas clave
Detalle en [L04](/corte-1-pronosticos/03-graficas-y-autocorrelacion/L04-plotting-your-data.md).

- **Coeficiente de autocorrelación del rezago $k$:**
  $$r_k=\frac{\sum_{i=1}^{N-k}(x_i-\bar{x})(x_{i+k}-\bar{x})}{\sum_{i=1}^{N}(x_i-\bar{x})^2}$$
  $x_i$: dato del periodo $i$; $\bar x$: media; $N$: número de datos; $k$: rezago. En Excel se aproxima con la correlación de Pearson entre la serie y la columna desplazada $k$ filas (herramienta *Análisis de datos → Correlación*) o se calcula exacto con `SUMPRODUCT`/`OFFSET` ([ejemplo 2](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-2.md)).
- **Límites de significancia:**
  $$\pm\,t\cdot SE(r_k),\qquad SE(r_1)\approx\frac{1}{\sqrt n},\qquad SE(r_k)=\sqrt{\frac{1+2\sum_{i=1}^{k-1}r_i^2}{n}}$$
  $t$: t de Student al 5 % (dos colas) con $n-1$ grados de libertad (`TINV(0.05; n-1)`; con $n$ grande ≈ 1,96). Si $|r_k|$ sale de la banda, el rezago $k$ es significativo.
- **Lectura del correlograma** (L04, p. 16):

  | Patrón | Cómo se ve | Ejemplo en esta carpeta |
  |---|---|---|
  | Aleatoriedad | $r_k$ casi todos cerca de 0, dentro de los límites | [graficas…](/corte-1-pronosticos/03-graficas-y-autocorrelacion/graficas-pronosticos-ventas-autocorrelacion.md), [ejemplo 1](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-1.md) |
  | Tendencia | $r_k$ altos en los primeros rezagos que bajan despacio | [ejemplo 2](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-2.md) ($r_1=0{,}966$ → $r_{88}=0{,}834$), [ejemplo 3](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-3.md) |
  | Estacionalidad | $r_k$ significativo en el rezago de la estación | [ejemplo 4](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-4.md) (±0,85 alternando: periodo 2) |

- **Prueba de Ljung-Box:**
  $$Q=n(n+2)\sum_{k=1}^{h}\frac{r_k^2}{n-k}$$
  $h$: número de rezagos. $H_0$: datos independientes. Si $Q>\chi^2_{\alpha,h}$ se rechaza $H_0$ (datos correlacionados).
- **Boxplot:** caja de $Q_1$ a $Q_3$; atípicos fuera de $[Q_1-1{,}5\,RIQ,\ Q_3+1{,}5\,RIQ]$ con $RIQ=Q_3-Q_1$.
- **PCA:** reduce muchas variables (periodos) a pocas componentes; la proporción de información de la componente $j$ es $\lambda_j/\sum\lambda$ (valores propios de la matriz de correlación). Sirve para agrupar tiendas o productos y definir una estrategia de pronóstico por grupo.

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado principal |
|---|---|---|
| $r_1$, $r_2$, $r_3$ de la serie −0,36; −0,52; 0,46; −0,31; −2,05; 0,28 | [L04](/corte-1-pronosticos/03-graficas-y-autocorrelacion/L04-plotting-your-data.md), p. 8–12 | $r_1=-0{,}33$; $r_2=-0{,}33$; $r_3=0{,}1988$ |
| Límites de significancia del mismo ejemplo ($n=6$) | L04, p. 13–14 | ±1,05; ±1,16; ±1,26 → ninguno significativo («Not enough data!») |
| Ljung-Box del mismo ejemplo | L04, p. 18 | $Q=2{,}9846<\chi^2=7{,}81$ → sin evidencia de correlación |
| PCA de 15 tiendas × 13 periodos | L04, p. 22–31 | 2 componentes = 75,8 % de la información; tiendas parecidas {9, 12}, {1, 5}, {2, 7} |
| Autocorrelograma de 30.000 ventas | [graficas-pronosticos-ventas-autocorrelacion](/corte-1-pronosticos/03-graficas-y-autocorrelacion/graficas-pronosticos-ventas-autocorrelacion.md) | $\lvert r_k\rvert<0{,}013$ en los 20 rezagos → serie aleatoria |
| Ventas propias y competencia (1.923 días) | [tarea-class-example-1](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-1.md) | Límites ±0,0447; series aleatorias (solo el rezago 4 de competencia, −0,0459, roza el límite); atípicos 31.624, 12, 9 y 2; propias + competencia ≈ 2.960 constante |
| Producto 1 (1.923 días) | [tarea-class-example-2](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-2.md) | ACF 0,966 → 0,834 (rezagos 1–88), todos significativos; sin atípicos; $\hat X_t=47{,}79+0{,}9677X_{t-1}$, $R^2=0{,}937$ → tendencia |
| Serie de 301 datos | [tarea-class-example-3](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-3.md) | ACF correcta 0,992 → 0,776 (rezagos 1–20) → tendencia creciente |
| Serie de 500 datos | [tarea-class-example-4](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-4.md) | $r_k\approx\pm0{,}85$ alternando, todos significativos → estacionalidad de periodo 2 |

## Relación con otros temas y proyectos
- Viene de [02 — introducción a pronósticos](/corte-1-pronosticos/02-introduccion-a-pronosticos/README.md), donde se definen los patrones de demanda (horizontal, tendencia, estacionalidad, ciclo, aleatoriedad).
- El patrón detectado aquí decide el método:
  - serie aleatoria/estacionaria → [04 — promedio móvil y suavización simple](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/README.md);
  - tendencia → [05 — suavización doble de Holt](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/README.md);
  - estacionalidad → [06 — Winters y tracking signal](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/README.md);
  - autocorrelación como base del modelo → [07 — ARIMA](/corte-1-pronosticos/07-arima/README.md).
- La serie de ventas propias del [ejemplo 1](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-1.md) se reutiliza para comparar promedios móviles y suavización exponencial en [promedio-movil-y-suavizacion-exponencial](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/promedio-movil-y-suavizacion-exponencial.md) (ese libro copia, celda por celda, las 14 hojas del ejemplo 1).
- El [proyecto THYMS de pronóstico](/corte-1-pronosticos/proyecto-thyms-pronostico/README.md) explora sus datos con histograma, gráfico de retardo, boxplot y autocorrelograma en Python.
- El [parcial 1](/corte-1-pronosticos/parcial-1/README.md) evalúa este análisis exploratorio junto con los métodos de pronóstico.


---

<!-- fuente: corte-1-pronosticos/03-graficas-y-autocorrelacion/L04-plotting-your-data.md -->
# L04-plotting-your-data

> **Archivo:** [`L04-plotting-your-data.pdf`](/corte-1-pronosticos/03-graficas-y-autocorrelacion/L04-plotting-your-data.pdf) · **Corte 1** · 31 páginas  
> **Nombre original:** `CORTE 1/Lec 4 - Plotting your data.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** visualización de datos antes de pronosticar: histogramas, series, boxplot, dispersión, correlogramas (autocorrelación con límites de significancia), prueba de Ljung-Box y análisis de componentes principales (PCA).

**Ideas clave**

- Antes de elegir un método de pronóstico hay que **graficar los datos** y entenderlos «más allá del promedio» (p. 2–3).
- Herramientas: histograma (ajustar los intervalos de clase), serie de datos (ajustar la granularidad), boxplot (cruzar con otras variables: ubicación, edad, nacionalidad…), autocorrelograma y diagrama de dispersión (p. 3).
- Ejercicio propuesto: generar 1.000.000 de demandas normales con media 500 y desviación 50 en Excel y graficarlas (p. 4).
- La observación directa de una serie permite separar **tendencia**, **ciclo** y variación (p. 5).
- El **correlograma** grafica los coeficientes de autocorrelación $r_k$ por rezago junto con los **límites de significancia**; sirve para saber si los valores de la serie dependen de los anteriores (p. 6–7).
- Lectura del correlograma (p. 16):
  - **Tendencia:** $r_k$ significativamente mayores que cero en los primeros rezagos que caen poco a poco a cero.
  - **Estacionalidad:** el $r_k$ del rezago estacional es significativamente distinto de cero; conviene quitar la tendencia antes de analizar.
  - **Aleatoriedad:** los $r_k$ son casi todos cercanos a cero.
- Con solo 6 datos los límites son tan anchos (±1,05 a ±1,26) que ningún coeficiente puede ser significativo: «Not enough data!» (p. 14).
- La **prueba de Ljung-Box** contrasta de forma conjunta si los primeros $h$ coeficientes son cero (datos independientes) (p. 17–18).
- El **PCA** reduce las 13 dimensiones (periodos) de 15 tiendas a 2 componentes que conservan el 75,8 % de la información; las tiendas cercanas en el plano tienen patrones de venta parecidos y se pueden agrupar para definir una estrategia de pronóstico por grupo (p. 22–31).
- Software mencionado: Minitab (Stat → Time Series → Autocorrelation…) y Tableau (p. 19–21).

**Fórmulas y métodos**

- Coeficiente de autocorrelación del rezago $k$ (p. 7):
  $$r_k=\frac{\sum_{i=1}^{N-k}(x_i-\bar{x})(x_{i+k}-\bar{x})}{\sum_{i=1}^{N}(x_i-\bar{x})^2}$$
  $x_i$: dato del periodo $i$; $\bar{x}$: media de los $N$ datos; $k$: rezago. El numerador usa solo los $N-k$ pares disponibles y el denominador, la suma de cuadrados de toda la serie. Para $k=1$ se obtiene $r_1$.
- Límites de significancia (p. 13):
  $$\pm\, t\cdot SE(r_k),\qquad SE(r_1)\approx\frac{1}{\sqrt{n}},\qquad SE(r_k)=\sqrt{\frac{1+2\sum_{i=1}^{k-1} r_i^2}{n}}$$
  $t$: valor t de Student con probabilidad 0,05 (dos colas) y $n-1$ grados de libertad; $n$: número de datos. Si $|r_k|$ supera el límite, la autocorrelación del rezago $k$ es significativa. En el ejemplo se usa `=DISTR.T.INV(0,04925;5)` = 2,58304527.
- Estadístico de Ljung-Box (p. 17):
  $$Q=n(n+2)\sum_{k=1}^{h}\frac{r_k^2}{n-k}$$
  $n$: tamaño de la muestra; $h$: número de rezagos; $r_k$: autocorrelación del rezago $k$. $H_0$: datos independientes. Si $Q>\chi^2_{\alpha,h}$ (chi-cuadrado con $h$ grados de libertad) se rechaza $H_0$ → los datos están correlacionados.
- PCA (p. 25): se calculan los valores propios de la matriz de correlación de las variables (periodos); la proporción de información de cada componente es $\lambda_j/\sum\lambda$, y la acumulada indica cuánta información se conserva al graficar en 1, 2, … dimensiones.

**Ejemplos resueltos**

| Ejemplo | Páginas | Resultado |
|---|---|---|
| Autocorrelación de la serie −0,36; −0,52; 0,46; −0,31; −2,05; 0,28 (media −0,42; $\sum(x-\bar x)^2=3{,}95$) | 8–12 | $r_1=-1{,}315/3{,}95=-0{,}33$; $r_2=-1{,}316/3{,}95=-0{,}33$; $r_3=0{,}7856/3{,}95=0{,}1988$ |
| Límites de significancia del mismo ejemplo ($n=6$, $t=2{,}583$) | 13–14 | ±1,0545 (rezago 1), ±1,1637 (rezago 2), ±1,2635 (rezago 3): ningún $r_k$ es significativo, «Not enough data!» |
| Correlograma de 12 rezagos para analizar | 15 | Ningún coeficiente supera los límites (el mayor es el del rezago 8, ≈ 0,40) |
| Ljung-Box con el mismo ejemplo ($h=3$) | 18 | $Q=6\cdot 8\cdot 0{,}0622=2{,}9846<\chi^2_{0,05;3}=7{,}81$ → no hay evidencia de correlación |
| PCA de 15 tiendas × 13 periodos | 22–31 | PC1 = 49,5 %, PC1+PC2 = 75,8 % de la información; tiendas parecidas: {9, 12}, {1, 5}, {2, 7}; muy distintas: 2 y 13 |

**Páginas clave**

- p. 3–4: tipos de gráfico y ejercicio de 1.000.000 de datos normales.
- p. 5: tendencia y ciclo por observación directa.
- p. 6–7: definición y fórmula del correlograma.
- p. 8–12: ejemplo numérico de $r_1$, $r_2$, $r_3$.
- p. 13–14: límites de significancia y su cálculo.
- p. 15–16: interpretación de correlogramas (tendencia, estacionalidad, aleatoriedad).
- p. 17–18: prueba de Ljung-Box.
- p. 19–21: Minitab y Tableau.
- p. 22–31: PCA.

**Relación con otros archivos del repo**

- [graficas-pronosticos-ventas-autocorrelacion.md](/corte-1-pronosticos/03-graficas-y-autocorrelacion/graficas-pronosticos-ventas-autocorrelacion.md): hoja de clase con rezagos, correlograma y dispersión sobre datos de ventas.
- [tarea-class-example-1.md](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-1.md), [tarea-class-example-2.md](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-2.md), [tarea-class-example-3.md](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-3.md), [tarea-class-example-4.md](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-4.md): tarea «Pronósticos de demandas» que aplica rezagos, autocorrelación con límites, histograma, boxplot y dispersión.
- [README de esta carpeta](/corte-1-pronosticos/03-graficas-y-autocorrelacion/README.md).
- Siguiente tema: [04 — datos estacionarios, promedio móvil y suavización simple](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/README.md); la autocorrelación vuelve a usarse en [07 — ARIMA](/corte-1-pronosticos/07-arima/).
- La ACF se aplicó también en el [proyecto THYMS de pronóstico](/corte-1-pronosticos/proyecto-thyms-pronostico/).


---

<!-- fuente: corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/README.md -->
# Tendencia: suavización exponencial doble de Holt (Corte 1)

## Qué cubre

Pronóstico de demanda con **tendencia lineal y sin estacionalidad** mediante la suavización exponencial doble (método de Holt). Incluye las ecuaciones de nivel y pendiente, el pronóstico a $\tau$ periodos y tres formas de fijar los valores iniciales $S_0$ y $G_0$: diferencias, regresión lineal y estaciones. Cierra con un repaso de regresión lineal simple: supuestos, estimadores de mínimos cuadrados, $R^2$, residuos y la herramienta Regresión de Excel.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [`L06-forecasting-data-with-trend.md`](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/L06-forecasting-data-with-trend.md) | Clase 6 (25 diapositivas): Holt, inicialización por regresión y por estaciones con ejemplos resueltos, y regresión lineal | Sí (1.º) |
| [`suavizacion-exponencial-doble-holt.md`](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/suavizacion-exponencial-doble-holt.md) | Excel: Holt sobre 8 trimestres de demanda, inicializado por regresión, con $\alpha$ y $\beta$ hallados con Solver, MAD, MAPE y proyección de 4 periodos | Sí (2.º) |

Los binarios originales son [`L06-forecasting-data-with-trend.pdf`](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/L06-forecasting-data-with-trend.pdf) y [`suavizacion-exponencial-doble-holt.xlsx`](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/suavizacion-exponencial-doble-holt.xlsx).

## Orden de estudio sugerido

1. Repasar la suavización simple y las medidas de error (MAD, MSE, MAPE) en [`../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/`](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/).
2. Leer L06, páginas 3–7: ecuaciones de Holt, interpretación gráfica y pronóstico a $\tau$ periodos.
3. Leer L06, páginas 8–15: las tres formas de inicializar y los dos ejemplos resueltos (regresión y estaciones con los mismos datos).
4. Estudiar el Excel [`suavizacion-exponencial-doble-holt.md`](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/suavizacion-exponencial-doble-holt.md), sobre todo sus **Observaciones**: Solver quedó configurado para maximizar el MAD.
5. Leer L06, páginas 16–24, sobre regresión lineal; sirve para inicializar Holt y como método de pronóstico en sí.
6. Seguir con Winters en [`../06-estacionalidad-winters-y-tracking-signal/`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/), que añade estacionalidad a Holt.

## Conceptos y fórmulas clave

Notación: $D_t$ = demanda real en $t$, $S_t$ = nivel (intercepto), $G_t$ = pendiente (tendencia), $\alpha$ y $\beta$ = constantes de suavización del nivel y de la pendiente.

- Holt (en general $\beta\le\alpha$):

$$S_t=\alpha D_t+(1-\alpha)(S_{t-1}+G_{t-1}),\qquad G_t=\beta(S_t-S_{t-1})+(1-\beta)G_{t-1}$$

- Pronóstico hecho en $t$ para $\tau$ periodos adelante: $F_{t,t+\tau}=S_t+\tau G_t$.
- Inicialización por regresión: $S_0$ = intercepto y $G_0$ = pendiente de la recta de $D_t$ contra $t$ (en Excel, `INTERSECCION.EJE` y `PENDIENTE`).
- Inicialización por estaciones, con $m$ grupos de $N$ datos y $V_i$ = promedio del grupo $i$:

$$G_0=\frac{V_m-V_1}{(m-1)N},\qquad S_0=V_1-G_0\frac{N+1}{2}$$

- Regresión lineal simple $Y=a+bx$:

$$b=\frac{\sum xy-n\bar x\bar y}{\sum x^2-n\bar x^2},\qquad a=\bar y-b\bar x$$

  - $R^2$ = proporción de la variación explicada.
  - Supuestos: residuos normales, independientes y homocedásticos.

El detalle está en el resumen de [`L06-forecasting-data-with-trend.md`](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/L06-forecasting-data-with-trend.md).

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado principal |
|---|---|---|
| Holt con inicialización por regresión, demanda 15, 20, 26, 30, 35, 38, 40, 43, $\alpha=\beta=0{,}1$ | L06, p. 10–11 | $S_0=12{,}8$, $G_0=4{,}01$; pronósticos 16,8 … 45,1; errores entre −2,1 y 2,15 |
| Mismo ejercicio con inicialización por estaciones ($m=2$, $N=4$) | L06, p. 14–15 | $V_1=22{,}75$, $V_2=39$, $S_0=12{,}6$, $G_0=4{,}06$; pronósticos 16,7 … 45,3 |
| Demanda trimestral 200, 250, 175, 186, 225, 285, 305, 190 ($\alpha=\beta=0{,}1$, $S_0=200$, $G_0=10$) | Enunciado en L06, p. 6, sin solución en la diapositiva | El Excel lo resuelve con otros $S_0$, $G_0$, $\alpha$ y $\beta$; con los del enunciado, cálculo propio en el `.md` del Excel: MAD ≈ 41,3 y $F_9\approx275{,}5$ |
| Holt en Excel con los datos anteriores, $S_0=196{,}25$ y $G_0=6{,}83$ por regresión, $\alpha=0{,}831$, $\beta=0{,}999$ | [`suavizacion-exponencial-doble-holt.md`](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/suavizacion-exponencial-doble-holt.md) | MAD = 60,78; MAPE = 29,6 %; proyección de los periodos 9–12: 120,6; 25,3; −70,1; −165,5 (inestable porque $\beta\approx1$) |
| Regresiones de viscosidad, granularidad y deformación contra la temperatura | L06, p. 21 | $R^2$ = 0,9058; 0,9218; 0,9087 |
| Salida de la herramienta Regresión de Excel | L06, p. 24 | $R^2=0{,}0017$: no hay relación lineal |

## Relación con otros temas y proyectos

- Tema anterior: [`../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/`](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/) (suavización simple, a la que Holt añade la pendiente).
- Tema siguiente: [`../06-estacionalidad-winters-y-tracking-signal/`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/). Winters añade la estacionalidad, y la p. 5 de L07 muestra por qué Holt falla con datos estacionales. Allí también están la señal de rastreo y la tabla comparativa de métodos.
- Autocorrelación y gráficas para detectar la tendencia: [`../03-graficas-y-autocorrelacion/`](/corte-1-pronosticos/03-graficas-y-autocorrelacion/).
- Aplicación evaluada de Holt (demanda con tendencia decreciente, 48 meses): [`../parcial-1/README.md`](/corte-1-pronosticos/parcial-1/README.md).
- Proyecto de pronóstico de THYMS: [`../proyecto-thyms-pronostico/README.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/README.md).


---

<!-- fuente: corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/L06-forecasting-data-with-trend.md -->
# L06-forecasting-data-with-trend

> **Archivo:** [`L06-forecasting-data-with-trend.pdf`](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/L06-forecasting-data-with-trend.pdf) · **Corte 1** · 25 páginas  
> **Nombre original:** `CORTE 1/LEc 6 - forecasting data with trend.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** pronóstico de demanda con tendencia lineal: suavización exponencial doble (método de Holt), cómo inicializarla (regresión o estaciones) y repaso de regresión lineal simple.

**Ideas clave:**
- Holt sigue series con tendencia lineal usando dos ecuaciones de suavización: una para el intercepto o nivel ($S_t$) y otra para la pendiente o tendencia ($G_t$), con dos constantes $\alpha$ y $\beta$.
- En general se toma $\beta\le\alpha$ para dar más estabilidad a la pendiente estimada.
- Interpretación gráfica: $S_t'=S_{t-1}+G_{t-1}$ es la proyección de la recta anterior, y el nuevo nivel $S_t$ cae en el segmento entre $S_t'$ y la demanda real $D_t$.
- El pronóstico a $\tau$ periodos es una recta: $F_{t,t+\tau}=S_t+\tau G_t$.
- Desventaja de Holt: es «difícil» de actualizar.
- Hace falta fijar dos valores iniciales, $S_0$ (intercepto) y $G_0$ (pendiente). Hay tres opciones:
  - diferencias entre los primeros datos;
  - método 1, regresión lineal (en Excel, `PENDIENTE` e `INTERSECCION.EJE`);
  - método 2, estaciones (promedios de grupos de datos).
- Lo mejor es reservar unos periodos base iniciales para la inicialización.
- La regresión lineal sirve cuando hay tendencia en el tiempo o variables linealmente correlacionadas. Supone residuos normales, independientes y con varianza constante (homocedasticidad).
- $R^2$ mide el porcentaje de la variación explicada por la relación lineal. Un $R^2$ bajo indica que no hay relación lineal, aunque puede haber una relación no lineal.

**Fórmulas y métodos:**
- Holt (p. 4), con $D_t$ = demanda real del periodo $t$, $S_t$ = nivel o intercepto suavizado, $G_t$ = pendiente suavizada, $\alpha$ = constante del nivel y $\beta$ = constante de la tendencia ($0<\alpha,\beta<1$):

$$S_t=\alpha D_t+(1-\alpha)(S_{t-1}+G_{t-1})$$

$$G_t=\beta(S_t-S_{t-1})+(1-\beta)G_{t-1}$$

- Pronóstico hecho en $t$ para $t+\tau$ (p. 6): $F_{t,t+\tau}=S_t+\tau G_t$. A un periodo: $F_{t+1}=S_t+G_t$. Ejemplo (p. 7): $F_{2,5}=S_2+3G_2$.
- Pendiente inicial a partir de diferencias (p. 8; $A_i$ = dato del periodo $i$, $n$ = número de datos; la diapositiva la llama $S_1$): $A_2-A_1$; $\frac{1}{3}[(A_2-A_1)+(A_3-A_2)+(A_4-A_3)]$; o $\dfrac{A_n-A_1}{n-1}$.
- Inicialización por regresión (p. 9–11): $S_0$ = intercepto y $G_0$ = pendiente de la recta de mínimos cuadrados de $D_t$ contra $t$.
- Inicialización por estaciones (p. 12), con $m$ grupos («estaciones») de $N$ datos y $V_i$ = promedio del grupo $i$:

$$G_0=\frac{V_m-V_1}{(m-1)N},\qquad S_0=V_1-G_0\frac{N+1}{2}$$

- Regresión lineal simple (p. 18–19): $Y=a+bx$, con $Y$ = variable dependiente, $x$ = variable independiente, $a$ = intercepto, $b$ = pendiente, $n$ = número de pares, $\bar x,\bar y$ = medias:

$$b=\frac{\sum xy-n\bar x\bar y}{\sum x^2-n\bar x^2},\qquad a=\bar y-b\bar x$$

- Residuo (p. 23): $\hat y_i=a+bX_i$ y $e_i=\hat y_i-y_i$.
- Coeficiente de determinación: $R^2=r^2$ ($r$ = coeficiente de correlación), proporción de la variación explicada.
- Cuándo usar Holt: datos con tendencia y **sin** estacionalidad (15–20 observaciones, horizonte corto a medio; ver la tabla de la p. 39 de L07). Con estacionalidad se usa Winters.

**Ejemplos resueltos:**
- p. 6–7: demanda trimestral de 8 periodos (200, 250, 175, 186, 225, 285, 305, 190) con $\alpha=\beta=0{,}1$, $S_0=200$, $G_0=10$; se pide el pronóstico a un periodo y su error. La diapositiva no trae la solución; la resuelve el Excel [`suavizacion-exponencial-doble-holt.md`](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/suavizacion-exponencial-doble-holt.md), aunque con otros valores iniciales y otros parámetros.
- p. 10–11: demanda 15, 20, 26, 30, 35, 38, 40, 43 con $\alpha=\beta=0{,}1$ e inicialización por **regresión**: $S_0=12{,}8$, $G_0=4{,}01$; pronósticos $F_1\ldots F_8$ = 16,8; 20,6; 24,6; 28,7; 32,9; 37,1; 41,2; 45,1; errores entre −2,1 y 2,15.
- p. 14–15: mismos datos con inicialización por **estaciones** ($V_1=22{,}75$, $V_2=39$): $S_0=12{,}6$, $G_0=4{,}06$; pronósticos 16,7; 20,5; 24,5; 28,7; 32,9; 37,2; 41,4; 45,3. Ambas inicializaciones dan resultados casi iguales.
- p. 21: tres regresiones contra la temperatura: viscosidad $y=0{,}8002x+29{,}745$ ($R^2=0{,}9058$), granularidad $y=0{,}2415x+23{,}706$ ($R^2=0{,}9218$) y deformación $y=0{,}0244x+0{,}1453$ ($R^2=0{,}9087$).
- p. 22: cinco casos sin relación lineal clara ($R^2$ = 0,0053; 0,2443; 0,8396; 0,5163; 0,0214).
- p. 24: salida de la herramienta Regresión de Excel con 10 observaciones: $R^2=0{,}0017$, intercepción 14,415, pendiente 0,031.

**Páginas clave:**
- p. 3–5: definición e interpretación gráfica de Holt.
- p. 6–7: pronóstico a $\tau$ periodos y ejercicio propuesto.
- p. 8–15: inicialización (diferencias, regresión, estaciones) con dos ejemplos resueltos.
- p. 16–23: regresión lineal (uso, supuestos, estimadores, $R^2$, residuos).
- p. 24: herramienta Regresión de Excel.

**Relación con otros archivos del repo:**
- [`suavizacion-exponencial-doble-holt.md`](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/suavizacion-exponencial-doble-holt.md): el Excel de esta clase, con Holt aplicado a los datos de la p. 6 e inicializado por regresión.
- Paso previo, suavización simple y medidas de error: [`../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md`](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md).
- Paso siguiente, Winters (Holt más estacionalidad), con la tabla que muestra por qué Holt falla con estacionalidad: [`../06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md).
- Aplicación de Holt en el parcial: [`../parcial-1/README.md`](/corte-1-pronosticos/parcial-1/README.md).

**Errores o inconsistencias detectados en el material:**
- p. 8: las tres fórmulas se rotulan $S_1$, pero son estimaciones de la pendiente inicial (diferencias entre datos), no del nivel.
- p. 6: «Quater» por *quarter* (trimestre). p. 16: «Trend ver time» por *trend over time*. p. 19: «Minimim» por *minimum*.
- p. 22: el último gráfico (viscosidad contra tiempo de agitación) es claramente creciente, aunque curvo; un $R^2$ lineal de 0,0214 parece demasiado bajo.


---

<!-- fuente: corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/README.md -->
# Estacionalidad: método de Winters y señal de rastreo (Corte 1)

## Qué cubre

Pronóstico de demanda con **tendencia y estacionalidad** mediante el método de Winters (suavización exponencial triple), en sus versiones multiplicativa y aditiva:

- modelo y ecuaciones de actualización de nivel, tendencia e índices estacionales;
- inicialización con dos ciclos de datos, normalización de factores y ejemplo numérico completo (llantas para nieve).

Se cubre además cómo elegir parámetros y métodos (datos de calibración y de prueba), la **señal de rastreo** (*tracking signal*) para detectar sesgo, el intervalo de confianza del pronóstico y una tabla comparativa de todos los métodos de pronóstico del corte.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [`L07-forecasting-seasonality-and-tracking-signal.md`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md) | Clase 7 (40 diapositivas): resumen de los tres métodos de suavización, Holt con estacionalidad, Winters multiplicativo y aditivo, ejemplo de llantas, selección de parámetros, señal de rastreo, intervalo de confianza y comparación de métodos | Sí (1.º) |
| [`metodo-winters.md`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/metodo-winters.md) | Excel de 4 hojas: regresión sobre 24 meses (`INTERCEPTO`), inicialización, factores y pronóstico Winters del año 3 (`DATOS PARA WINTERS`), y correlograma de 19 rezagos (`FATOS PARA CORRELOGRAMA`, `CORRELOGRAMA`) | Sí (2.º) |

Los binarios originales son [`L07-forecasting-seasonality-and-tracking-signal.pdf`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.pdf) y [`metodo-winters.xlsx`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/metodo-winters.xlsx).

## Orden de estudio sugerido

1. L07, p. 4–5: tabla resumen de los métodos de suavización y por qué Holt no sirve con estacionalidad.
2. L07, p. 6–15: modelo multiplicativo, ecuaciones (en notación $S,G,c$ y $a_0,a_1,C$) e inicialización.
3. L07, p. 16–22, junto con la hoja `DATOS PARA WINTERS` de [`metodo-winters.md`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/metodo-winters.md): ejemplo numérico, factores normalizados, pronósticos y actualización. Revisar las notas de errores en ambos archivos.
4. La hoja `INTERCEPTO` del Excel muestra por qué no se inicializa con una regresión simple sobre datos estacionales. Las hojas de correlograma muestran cómo se confirma un ciclo de 12 meses.
5. L07, p. 23–26: equivalencia con Minitab y Winters aditivo.
6. L07, p. 27–38: selección de parámetros, señal de rastreo con su ejemplo e intervalo de confianza.
7. L07, p. 39: tabla comparativa de métodos, útil para elegir el método en el parcial y en el proyecto.

## Conceptos y fórmulas clave

Notación: $D_t$ (o $x_t$) = demanda real; $S_t$ (o $a_{0,t}$) = nivel; $G_t$ (o $a_{1,t}$) = tendencia; $c_t$ (o $C_t$) = factor estacional; $N$ = periodos por ciclo. Las constantes de suavización son $\alpha$ (nivel), $\beta$ o $\phi$ (tendencia) y $\gamma$ (estacionalidad).

- **Winters multiplicativo:**

$$S_t=\alpha\frac{D_t}{c_{t-N}}+(1-\alpha)(S_{t-1}+G_{t-1})$$

$$G_t=\beta(S_t-S_{t-1})+(1-\beta)G_{t-1}$$

$$c_t=\gamma\frac{D_t}{S_t}+(1-\gamma)c_{t-N}$$

$$F_{t,t+\tau}=(S_t+\tau G_t)\,c_{t+\tau-N}$$

- **Winters aditivo:**
  - $S_t=\alpha(D_t-c_{t-N})+(1-\alpha)(S_{t-1}+G_{t-1})$
  - $c_t=\gamma(D_t-S_t)+(1-\gamma)c_{t-N}$
  - $F_{t,t+\tau}=S_t+\tau G_t+c_{t+\tau-N}$
- **Inicialización con dos ciclos:**
  - $a_1=(\bar S_2-\bar S_1)/N$
  - $a_{0,2N}=\bar S_2+a_1\frac{N-1}{2}$
  - $a_0=a_{0,2N}-2Na_1$
  - $C_t=\dfrac{x_t}{a_0+a_1t}$, promediando los dos años y normalizando con $C^{norm}=N\,C_t/\sum C_t$
- **Señal de rastreo:**
  - $E_t=\sum_{i\le t}e_i$ (RSFE)
  - $MAD_t=\frac{1}{t}\sum|e_i|$, o en versión suavizada $E_t=\omega e_t+(1-\omega)E_{t-1}$ y $MAD_t=\omega|e_t|+(1-\omega)MAD_{t-1}$
  - $T_t=E_t/MAD_t$, que debe estar cerca de 0
- **Intervalo de confianza aproximado del 95 % para $F_{t+1}$:** $F_{t+1}\pm z_{0.95}\cdot RMSE\cdot\sqrt{N/(N-p)}$, donde $p$ es el número de parámetros del método.
- **Autocorrelación de rezago $k$** (hoja `CORRELOGRAMA`): $r_k=\dfrac{\sum_{t=k+1}^{n}(x_t-\bar x)(x_{t-k}-\bar x)}{\sum(x_t-\bar x)^2}$, significativa si $|r_k|>1{,}96/\sqrt n$.

El detalle está en el resumen de [`L07-forecasting-seasonality-and-tracking-signal.md`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md).

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado principal |
|---|---|---|
| Holt aplicado a datos estacionales ($S_0=24$, $G_0=4$) con dos juegos de $\alpha,\beta$ | L07, p. 5 | El pronóstico no sigue los ciclos; con $\alpha=0{,}4$, $\beta=0{,}5$ los errores llegan a ±20 |
| Winters, llantas para nieve (2 años, $N=12$): inicialización | L07, p. 17–19 | $a_1=2{,}049$, $a_{0,24}=246{,}08$, $a_0=196{,}88$; factores normalizados 1,00; 1,22; 1,46; 1,33; 1,21; 1,01; 0,90; 0,76; 0,65; 0,62; 0,88; 0,96 |
| Winters, llantas: pronóstico | L07, p. 20 | $F_{25}=247{,}64$, $F_{26}=305{,}21$, $F_{27}=368{,}25$ |
| Winters, llantas: actualización con $x_{25}=245$ y $\alpha=\gamma=\phi=0{,}3$ | L07, p. 21–22 | $a_0=247{,}93$, $a_1=1{,}99$; $F_{26}=304{,}90$, $F_{27}=367{,}78$, $F_{28}=337{,}68$ (la diapositiva tiene errores aritméticos; ver notas) |
| Winters, llantas, en Excel (noviembre del año 2 = 208) | [`metodo-winters.md`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/metodo-winters.md), hoja `DATOS PARA WINTERS` | $a_1=2{,}0417$, $a_0=196{,}896$; pronósticos de los meses 25–36: 247,21; 305,27; 367,99; 337,90; 310,97; 260,20; 233,46; 200,04; 171,03; 165,08; 235,50; 260,84. MAD del ajuste ≈ 4,2 (≈ 2 %) |
| Regresión simple sobre los 24 meses | [`metodo-winters.md`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/metodo-winters.md), hoja `INTERCEPTO` | Intercepto 231,32, pendiente −0,71: la estacionalidad distorsiona la tendencia |
| Correlograma de la demanda de llantas | [`metodo-winters.md`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/metodo-winters.md), hoja `CORRELOGRAMA` | $r_1=0{,}77$, $r_6=-0{,}73$, $r_{12}=0{,}44$ (significativos con un límite de ±0,40): ciclo anual |
| Señal de rastreo, ventas 8, 11, 12, 14 con pronóstico fijo de 10 | L07, p. 32–37 | RSFE −2, −1, 1, 5; MAD 2; 1,5; 1,67; 2,25; señal −1; −0,67; 0,6; 2,22 |

## Relación con otros temas y proyectos

- Tema anterior: [`../05-tendencia-suavizacion-doble-holt/`](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/). Winters es Holt más un factor estacional.
- Correlograma y autocorrelación: [`../03-graficas-y-autocorrelacion/`](/corte-1-pronosticos/03-graficas-y-autocorrelacion/).
- Medidas de error (MAD, MSE, MAPE) y suavización simple: [`../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/`](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/).
- ARIMA (Box-Jenkins), que aparece en la tabla comparativa de la p. 39: [`../07-arima/`](/corte-1-pronosticos/07-arima/).
- Métodos cualitativos, para cuando no hay datos: [`../08-metodos-cualitativos/`](/corte-1-pronosticos/08-metodos-cualitativos/).
- En el parcial se descartó Winters por falta de estacionalidad y se usó la señal de rastreo: [`../parcial-1/README.md`](/corte-1-pronosticos/parcial-1/README.md).
- Proyecto de pronóstico de THYMS: [`../proyecto-thyms-pronostico/README.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/README.md).
- Los pronósticos alimentan la planeación agregada del corte 2: [`../../corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/`](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/).


---

<!-- fuente: corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md -->
# L07-forecasting-seasonality-and-tracking-signal

> **Archivo:** [`L07-forecasting-seasonality-and-tracking-signal.pdf`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.pdf) · **Corte 1** · 40 páginas  
> **Nombre original:** `CORTE 1/Lec 7 - forecasting data with seasonality and Tracking Signal.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** pronóstico de demanda con tendencia y estacionalidad mediante el método de Winters (suavización exponencial triple, multiplicativo y aditivo), selección de parámetros, señal de rastreo (*tracking signal*) e intervalo de confianza del pronóstico.

**Ideas clave:**
- Hay tres patrones de demanda y un método para cada uno: estacionaria → suavización simple / promedios móviles ($\alpha$); con tendencia → Holt / regresión ($\alpha,\beta$); con tendencia y estacionalidad → Winters ($\alpha,\beta,\gamma$).
- Si se aplica Holt a una serie estacional, el pronóstico no reproduce los ciclos: con constantes bajas sale casi una recta y con constantes altas persigue la demanda con retraso (p. 5).
- Winters multiplicativo: la demanda oscila alrededor de una recta de tendencia y la amplitud de la oscilación crece con el nivel. Tiene tres componentes (nivel, tendencia, estación) que se actualizan con una constante de suavización cada uno.
- Winters aditivo: la oscilación tiene amplitud constante; el factor estacional se suma o resta en vez de multiplicar o dividir.
- Inicialización con dos ciclos completos de datos: promedio de cada ciclo → pendiente → nivel → factores estacionales → normalización (que promedien 1).
- Los parámetros se actualizan cuando llega un dato nuevo del ciclo.
- Para escoger parámetros o métodos no basta minimizar el MAD (DAM) o el MSE: hay que validar con datos de prueba distintos de los de calibración y revisar el sesgo.
- La señal de rastreo $T_t=E_t/MAD_t$ debe estar cerca de 0; si se aleja, hay sesgo y hay que cambiar los parámetros o el método.
- El intervalo de confianza del pronóstico se usa solo para un periodo adelante.
- Nombres en Minitab: γ (tendencia) equivale a $\phi$ de la clase; δ (estacional) equivale a $\gamma$ de la clase.

**Fórmulas y métodos:**

*Winters multiplicativo, notación $S$, $G$, $c$ (p. 8–10).* Modelo $D_t=c_tS_t+\varepsilon_t$, donde $D_t$ = demanda en $t$, $S_t$ = nivel (punto sobre la recta), $G_t$ = tendencia, $c_t$ = factor estacional, $N$ = periodos por estación (ciclo), $\varepsilon_t$ = ruido, y $\alpha,\beta,\gamma$ = constantes de suavización del nivel, la tendencia y la estacionalidad.

$$S_t=\alpha\frac{D_t}{c_{t-N}}+(1-\alpha)(S_{t-1}+G_{t-1})$$

$$G_t=\beta(S_t-S_{t-1})+(1-\beta)G_{t-1}$$

$$c_t=\gamma\frac{D_t}{S_t}+(1-\gamma)c_{t-N}$$

$$F_{t,t+\tau}=(S_t+\tau G_t)\,c_{t+\tau-N}$$

donde $F_{t,t+\tau}$ es el pronóstico hecho en $t$ para $\tau$ periodos adelante.

*Winters multiplicativo, notación $a_0$, $a_1$, $C$ (p. 12–13).* $a_{0,t}$ = nivel, $a_{1,t}$ = tendencia, $C_t$ = factor estacional, $x_t$ = dato real, $\phi$ = constante de suavización de la tendencia. Modelo $x_t=(a_{0,t}+a_{1,t}t)C_t+\epsilon_t$.

$$a_{0,t}=\alpha\frac{x_t}{C_{t-N}}+(1-\alpha)(a_{0,t-1}+a_{1,t-1})$$

$$a_{1,t}=\phi(a_{0,t}-a_{0,t-1})+(1-\phi)a_{1,t-1}$$

$$C_t=\gamma\frac{x_t}{a_{0,t}}+(1-\gamma)C_{t-N}$$

Pronóstico: $F_t=(a_{0,t}+a_{1,t})C_t$; en el ejemplo, para $\tau$ periodos adelante, $F_{t+\tau}=(a_{0,t}+\tau a_{1,t})\,C_{t+\tau-N}$.

*Inicialización (p. 14–15), con $2N$ datos:*
- $\bar S_1=\frac{1}{N}\sum_{t=1}^{N}x_t$, $\quad\bar S_2=\frac{1}{N}\sum_{t=N+1}^{2N}x_t$ (promedios del ciclo 1 y del ciclo 2).
- Pendiente: $a_1=\dfrac{\bar S_2-\bar S_1}{N}$.
- Nivel al final del ciclo 2: $a_{0,2N}=\bar S_2+a_1\dfrac{N-1}{2}$.
- Intercepto en $t=0$: $a_0=a_{0,2N}-2N\,a_1$.
- Factor de cada periodo: $C_t=\dfrac{x_t}{a_0+a_1t}$; se promedian los factores del mismo mes de ambos ciclos.
- Normalización: $C_{t,\text{norm}}=N\dfrac{C_t}{\sum C_t}$, de modo que $\frac{1}{N}\sum_{t=1}^{N}C_t=1$.

*Winters aditivo (p. 25–26):*

$$S_t=\alpha(D_t-c_{t-N})+(1-\alpha)(S_{t-1}+G_{t-1})$$

$$G_t=\beta(S_t-S_{t-1})+(1-\beta)G_{t-1}$$

$$c_t=\gamma(D_t-S_t)+(1-\gamma)c_{t-N}$$

$$F_{t,t+\tau}=S_t+\tau G_t+c_{t+\tau-N}$$

En notación $a$: $a_{0,t}=\alpha(x_t-C_{t-N})+(1-\alpha)(a_{0,t-1}+a_{1,t-1})$, $a_{1,t}=\phi(a_{0,t}-a_{0,t-1})+(1-\phi)a_{1,t-1}$, $C_t=\gamma(x_t-a_{0,t})+(1-\gamma)C_{t-N}$, $F_t=a_{0,t}+a_{1,t}+C_t$.

*Selección y validación (p. 27–28):* separar datos de calibración y de prueba; ajustar con los de calibración (revisar indicadores y sesgos); calcular indicadores con los de prueba; verificar.

*Señal de rastreo (p. 29–30):* $e_i$ = error del periodo $i$ (real − pronóstico en el ejemplo); $n$ = número de errores.
- Error acumulado (RSFE, *running sum of forecast error*): $E_t=\sum_{i=1}^{t}e_i$.
- $MAD=\dfrac{\sum|e_i|}{n}$.
- Versión suavizada con constante $\omega$: $E_t=\omega e_t+(1-\omega)E_{t-1}$ y $MAD_t=\omega|e_t|+(1-\omega)MAD_{t-1}$, inicializando $E_0$ y $MAD_0$.
- Señal: $T_t=\dfrac{E_t}{MAD_t}$, que debe estar cerca de 0.

*Intervalo de confianza aproximado del 95 % para $F_{t+1}$ (p. 38):* $F_{t+1}\pm z_{0.95}\cdot RMSE\cdot\sqrt{\dfrac{N}{N-p}}$, donde $RMSE=\sqrt{MSE}$, $p$ = número de parámetros del método y $N$ = número de datos.

**Ejemplos resueltos:**
- p. 5: Holt aplicado a datos estacionales (8 periodos, $S_0=24$, $G_0=4$) con $\alpha=0{,}1,\ \beta=0{,}2$ (pronósticos 9–12: 60,21; 64,24; 68,27; 72,30) y con $\alpha=0{,}4,\ \beta=0{,}5$ (60,72; 64,23; 57,21*; 71,26). Ninguno sigue los ciclos.
- p. 16–22: ventas de llantas para nieve, 2 años mensuales ($N=12$). $\bar S_1=210{,}17$ (la diapositiva pone 201,16), $\bar S_2=234{,}75$, $a_1=2{,}049$, $a_{0,24}=246{,}08$, $a_0=196{,}88$. Factores normalizados de enero a diciembre: 1,00; 1,22; 1,46; 1,33; 1,21; 1,01; 0,90; 0,76; 0,65; 0,62; 0,88; 0,96. Pronósticos $F_{25}=247{,}64$, $F_{26}=305{,}21$, $F_{27}=368{,}25$. Con $x_{25}=245$ y $\alpha=\gamma=\phi=0{,}3$ se actualiza a $a_0=247{,}93$, $C=0{,}97$, $a_1=1{,}99$, y los nuevos pronósticos son $F_{26}=304{,}90$, $F_{27}=367{,}78$, $F_{28}=337{,}68$.
- p. 32–37: señal de rastreo con ventas 8, 11, 12, 14 y pronóstico fijo de 10: RSFE −2, −1, 1, 5; MAD 2; 1,5; 1,67; 2,25; señal −1; −0,67; 0,6; 2,22.
- p. 31: gráfico de suavización simple con α = 0,2 que queda por debajo de la demanda después de un salto de nivel (sesgo que pide acción correctiva).

**Páginas clave:**
- p. 4: tabla resumen de los tres métodos de suavización.
- p. 5: por qué Holt falla con estacionalidad.
- p. 8–10: modelo de Winters multiplicativo ($S,G,c$).
- p. 12–15: notación $a_0,a_1,C$, actualización e inicialización.
- p. 16–22: ejemplo numérico completo (llantas para nieve).
- p. 23: equivalencia de parámetros con Minitab.
- p. 24–26: Winters aditivo frente a multiplicativo.
- p. 27–28: selección de parámetros y validación.
- p. 29–37: señal de rastreo y ejemplo.
- p. 38: intervalo de confianza.
- p. 39: tabla comparativa de todos los métodos de pronóstico (patrón, datos, horizonte, preparación, complejidad).

**Relación con otros archivos del repo:**
- [`metodo-winters.md`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/metodo-winters.md): el Excel que resuelve el mismo ejemplo de llantas (inicialización, factores estacionales, pronósticos 25–36 y error *a posteriori*) y añade el correlograma de la demanda.
- Holt (suavización doble), base de Winters: [`../05-tendencia-suavizacion-doble-holt/L06-forecasting-data-with-trend.md`](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/L06-forecasting-data-with-trend.md) y [`../05-tendencia-suavizacion-doble-holt/suavizacion-exponencial-doble-holt.md`](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/suavizacion-exponencial-doble-holt.md).
- Suavización simple y medidas de error (MAD, MSE, MAPE): [`../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/`](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/).
- ARIMA / Box-Jenkins, que aparece en la tabla de la p. 39: [`../07-arima/L08-forecasting-with-arima.md`](/corte-1-pronosticos/07-arima/L08-forecasting-with-arima.md).
- Aplicación a datos reales: [`../parcial-1/`](/corte-1-pronosticos/parcial-1/) y [`../proyecto-thyms-pronostico/`](/corte-1-pronosticos/proyecto-thyms-pronostico/).

**Errores o inconsistencias detectados en el material:**
- p. 5 (tabla derecha): $F_{11}=57{,}21$ debería ser $67{,}74$ ($S_8+3G_8$).
- p. 17: $\bar S_1=2522/12=210{,}17$, no 201,16; el $a_1=2{,}049$ sí usa 210,17. Además $234{,}75+2{,}05\times5{,}5=246{,}03$ (la diapositiva pone 246,08).
- p. 21: con los datos dados, $a_{0,25}=0{,}3(245)+0{,}7(248{,}13)=247{,}19$ (no 247,93) y $C_{25}=0{,}3(245/247{,}93)+0{,}7=0{,}9965\approx1{,}00$ (no 0,97). Los pronósticos de la p. 22 se calculan a partir de 247,93 y 1,99.
- p. 16: noviembre del año 2 vale 209 (el total 2817 lo confirma); el Excel [`metodo-winters.md`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/metodo-winters.md) usa 208.
- p. 25: la ecuación de tendencia del aditivo tiene $S_t$ a la izquierda en vez de $G_t$, y el texto «Se resta el factor estacional $c_{t+\tau-N}$» contradice la fórmula del pronóstico, que lo suma (se resta al actualizar el nivel).
- p. 12 y 20: la fórmula general $F_t=(a_{0,t}+a_{1,t})C_t$ omite el horizonte $\tau$, pero el ejemplo sí multiplica $a_1$ por 1, 2, 3.
- p. 29: «$E_t$ -1» debe leerse $E_{t-1}$. p. 15: el subíndice «$t-1$» de la suma debe leerse $t=1$.


---

<!-- fuente: corte-1-pronosticos/07-arima/README.md -->
# ARIMA: método de Box-Jenkins (Corte 1)

## Qué cubre

Introducción al método de **Box-Jenkins (ARIMA)**, pensado para series en las que un periodo depende de los anteriores, en especial con **autocorrelación negativa**. Explica qué significa «integrado» (diferenciar la serie para quitar la tendencia) y los modelos autorregresivos AR(1) y AR(2), de promedio móvil MA(1) y mixto ARMA(1,1). Se resuelven a mano un AR(1) y un MA(1) con 12 periodos de demanda. La carpeta solo tiene la presentación; no hay Excel ni código.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [`L08-forecasting-with-arima.md`](/corte-1-pronosticos/07-arima/L08-forecasting-with-arima.md) | Clase 8 (20 diapositivas): Box-Jenkins, AR(1) con estimación de $\phi_1$, AR(2), MA(1) paso a paso, ARMA(1,1) y su estimación | Sí |

El binario original es [`L08-forecasting-with-arima.pdf`](/corte-1-pronosticos/07-arima/L08-forecasting-with-arima.pdf).

## Orden de estudio sugerido

1. Repasar la autocorrelación y el correlograma en [`../03-graficas-y-autocorrelacion/`](/corte-1-pronosticos/03-graficas-y-autocorrelacion/) y en la hoja `CORRELOGRAMA` de [`../06-estacionalidad-winters-y-tracking-signal/metodo-winters.md`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/metodo-winters.md).
2. L08, p. 4–5: qué es Box-Jenkins y qué significa ARIMA.
3. L08, p. 6–9: ejemplo AR(1) completo (tabla de desviaciones, $\phi_1=-0{,}7$, pronóstico 109,2).
4. L08, p. 11–17: MA(1) paso a paso. Atención al signo: el ejemplo usa $F_t=\bar\mu-\theta_1e_{t-1}$ (ver notas del `.md`).
5. L08, p. 18–19: ARMA(1,1) y la estimación de sus parámetros.
6. Tabla comparativa de métodos (ARIMA frente a los demás): p. 39 de [`../06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md).

## Conceptos y fórmulas clave

Notación: $x_t$ = demanda del periodo $t$, $\bar x$ (o $\bar\mu$) = media de la serie, $\dot x_t=x_t-\bar x$ = desviación respecto a la media, $e_t=x_t-F_t$ = error de pronóstico, $n$ = número de datos.

- AR(1): $\dot x_t=\phi_1\dot x_{t-1}+e_t$, con

$$\phi_1=\frac{cov(\dot x_t,\dot x_{t-1})}{var(\dot x_t)}=\frac{\sum\dot x_t\dot x_{t-1}/(n-1)}{\sum\dot x_t^2/n}$$

  - Pronóstico: $F_t=\bar\mu+\hat\phi_1\dot x_{t-1}$.
- AR(2): $F_t=\bar\mu+\hat\phi_1\dot x_{t-1}+\hat\phi_2\dot x_{t-2}$.
- MA(1): $F_t=\bar\mu+\theta_1e_{t-1}$ según la diapositiva. Los números del ejemplo salen de $F_t=\bar\mu-\theta_1e_{t-1}$. $\theta_1$ se fija por mínimos cuadrados no lineales.
- ARMA(1,1): $F_t=\hat\phi_1\hat x_{t-1}-\hat\theta_1e_{t-1}$. Sus parámetros se estiman con

$$\rho_k=\frac{cov(\dot x_t,\dot x_{t-k})}{var(\dot x_t)},\qquad \phi_1=\frac{\rho_2}{\rho_1},\qquad \rho_1=\frac{(1-\phi_1\theta_1)(\phi_1-\theta_1)}{1+\theta_1^2-2\theta_1\phi_1}$$

- Requisitos según la clase: pronósticos de corto plazo y al menos 72 datos históricos (la tabla de L07 dice 50 o más).

El detalle está en el resumen de [`L08-forecasting-with-arima.md`](/corte-1-pronosticos/07-arima/L08-forecasting-with-arima.md).

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado principal |
|---|---|---|
| AR(1) con demanda 106, 110, 118, 105, 115, 100, 112, 106, 118, 102, 112, 110 (media 109,5) | L08, p. 6–9 | $\sum\dot x_{t-1}\dot x_t=-256{,}25$, $\sum\dot x_t^2=379$, $cov=-23{,}3$, $var=31{,}6$, $\phi_1=-0{,}7$; pronóstico del periodo 13 = 109,2 |
| Promedio móvil de 5 periodos y sus errores (periodos 6–12) | L08, p. 11 | Errores −10,8; 2,4; −4; 10,4; −8,2; 4,4; 0, que alternan de signo (correlación negativa) |
| MA(1) con $\theta_1=0{,}5$ y pronóstico inicial 109,5 | L08, p. 13–17 | Pronósticos 109,5; 111,3; 110,1; 105,6; 109,8; 106,9; 112,9; 110,0; 111,5; 106,2; 111,6; 109,3 |

## Relación con otros temas y proyectos

- Autocorrelación, base para identificar modelos AR y MA: [`../03-graficas-y-autocorrelacion/`](/corte-1-pronosticos/03-graficas-y-autocorrelacion/).
- Promedio móvil, con el que se compara el AR(1): [`../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/`](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/).
- Holt y Winters, alternativas para series con tendencia o estacionalidad: [`../05-tendencia-suavizacion-doble-holt/`](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/) y [`../06-estacionalidad-winters-y-tracking-signal/`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/).
- Métodos cualitativos: [`../08-metodos-cualitativos/`](/corte-1-pronosticos/08-metodos-cualitativos/).
- Proyecto de pronóstico de THYMS: [`../proyecto-thyms-pronostico/README.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/README.md).


---

<!-- fuente: corte-1-pronosticos/07-arima/L08-forecasting-with-arima.md -->
# L08-forecasting-with-arima

> **Archivo:** [`L08-forecasting-with-arima.pdf`](/corte-1-pronosticos/07-arima/L08-forecasting-with-arima.pdf) · **Corte 1** · 20 páginas  
> **Nombre original:** `CORTE 1/Lec 8 - forecasting data with ARIMA.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** método de Box-Jenkins (ARIMA) para series con dependencia entre periodos, en especial con autocorrelación negativa: modelos AR(1), AR(2), MA(1) y ARMA(1,1).

**Ideas clave:**
- Los métodos anteriores (promedios móviles, suavización) tratan las observaciones como independientes; Box-Jenkins aprovecha la dependencia de un periodo a otro (autocorrelación).
- ARIMA = autorregresivo **integrado** de promedio móvil. «Integrado» significa diferenciar la serie (trabajar con las primeras diferencias) para eliminar la tendencia.
- Sirve para pronósticos de corto plazo y, según esta clase, requiere al menos 72 datos históricos (la tabla comparativa de la clase 7 dice «50 o más observaciones»).
- Tipos: autorregresivo (AR), promedio móvil (MA) y mixto (ARMA).
- Señal de autocorrelación negativa de rezago 1: cuando la desviación $\dot x_t$ es positiva, $\dot x_{t-1}$ tiende a ser negativa (y la nube de dispersión $x_t$ vs. $x_{t-1}$ tiene pendiente negativa).
- AR usa las desviaciones pasadas de la serie; MA usa los errores pasados del pronóstico; ARMA combina ambas.
- $\theta_1$ del MA se fija por mínimos cuadrados no lineales.

**Fórmulas y métodos:**
- Desviación respecto a la media: $\dot x_t=x_t-\bar x$, donde $x_t$ es la demanda del periodo $t$ y $\bar x$ su media muestral.
- Modelo AR(1): $\dot x_t=\phi_1\dot x_{t-1}+e_t$, donde $e_t$ es ruido independiente con media 0 y varianza $\sigma^2$, y $\phi_1$ es la constante de autocorrelación.
- Estimación de $\phi_1$: $\phi_1=\dfrac{cov(\dot x_t,\dot x_{t-1})}{var(\dot x_t)}$, con $cov=\dfrac{\sum\dot x_t\dot x_{t-1}}{n-1}$ y $var=\dfrac{\sum\dot x_t^2}{n}$ ($n$ = número de datos).
- Pronóstico AR(1): $F_t=\bar\mu+\hat\phi_1\dot x_{t-1}$ ($\bar\mu$ = media de la serie, $\hat\phi_1$ = estimación de $\phi_1$).
- Pronóstico AR(2): $F_t=\bar\mu+\hat\phi_1\dot x_{t-1}+\hat\phi_2\dot x_{t-2}$.
- Pronóstico MA(1): $F_t=\bar\mu+\theta_1 e_{t-1}$ según la diapositiva, donde $e_{t-1}=x_{t-1}-F_{t-1}$ es el error del periodo anterior y $\theta_1$ el peso del error. **El ejemplo numérico usa en realidad $F_t=\bar\mu-\theta_1 e_{t-1}$** (convención de Box-Jenkins).
- Pronóstico ARMA(1,1): $F_t=\hat\phi_1\hat x_{t-1}-\hat\theta_1 e_{t-1}$ ($p$ = orden autorregresivo, $q$ = orden de promedio móvil).
- Autocorrelación de rezago $k$: $\rho_k=\dfrac{cov(\dot x_t,\dot x_{t-k})}{var(\dot x_t)}$.
- Estimación ARMA(1,1) por momentos: $\phi_1=\rho_2/\rho_1$ y $\rho_1=\dfrac{(1-\phi_1\theta_1)(\phi_1-\theta_1)}{1+\theta_1^2-2\theta_1\phi_1}$ (con $\phi_1$ conocido se despeja $\theta_1$).
- Cuándo usar: series estacionarias (o convertidas en estacionarias diferenciando) con autocorrelación significativa, muchos datos y horizonte corto.

**Ejemplos resueltos:**
- Páginas 6–9: demanda de 12 periodos (media 109,5). $\sum\dot x_{t-1}\dot x_t=-256{,}25$, $\sum\dot x_t^2=379$, $cov=-23{,}3$, $var=31{,}6$, $\phi_1=-0{,}7$. Pronóstico AR(1) del periodo 13: $F=109{,}5+(-0{,}7)(0{,}5)=109{,}2$.
- Página 11: promedio móvil de 5 periodos para los periodos 6–12 (110,8; 109,6; 110; 107,6; 110,2; 107,6; 110) con errores −10,8; 2,4; −4; 10,4; −8,2; 4,4; 0, que alternan de signo (correlación negativa de los errores).
- Páginas 13–17: MA(1) con $\theta_1=0{,}5$ y pronóstico inicial 109,5. Pronósticos de los periodos 1–12: 109,5; 111,3; 110,1; 105,6; 109,8; 106,9; 112,9; 110,0; 111,5; 106,2; 111,6; 109,3. Errores: −3,5; −1,3; 7,9; −0,6; 5,2; −6,9; −0,9; −4,0; 6,5; −4,2; 0,4; 0,7.

**Páginas clave:**
- p. 4–5: qué es Box-Jenkins / ARIMA y sus requisitos.
- p. 6–9: AR(1) completo (datos, tabla de desviaciones, $\phi_1$, pronóstico).
- p. 10: AR(2).
- p. 11–17: MA y ejemplo MA(1) paso a paso.
- p. 18–19: ARMA(p,q) y estimación de ARMA(1,1).

**Relación con otros archivos del repo:**
- La autocorrelación y el correlograma, que permiten detectar la dependencia que explota ARIMA, se ven en [`../03-graficas-y-autocorrelacion/`](/corte-1-pronosticos/03-graficas-y-autocorrelacion/) y en la hoja `CORRELOGRAMA` de [`../06-estacionalidad-winters-y-tracking-signal/metodo-winters.md`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/metodo-winters.md).
- El promedio móvil de 5 periodos con el que se compara AR(1) está en [`../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/`](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/).
- La tabla «Comparación Métodos de Pronósticos» (ARIMA / Box & Jenkins frente a los demás métodos) está en la página 39 de [`../06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md).
- El proyecto de pronóstico de THYMS: [`../proyecto-thyms-pronostico/`](/corte-1-pronosticos/proyecto-thyms-pronostico/).

**Errores o inconsistencias detectados en el material:**
- p. 12–17: la fórmula MA(1) se escribe con $+\theta_1 e_{t-1}$, pero los números del ejemplo salen de $F_t=\bar\mu-\theta_1 e_{t-1}$. En la p. 14 se escribe «109,5 − 0,5·3,5 = 111,3», que en realidad da 107,75; el 111,3 corresponde a $109{,}5-0{,}5\times(-3{,}5)$.
- p. 5 dice que ARIMA requiere al menos 72 datos; la tabla de la clase 7 (p. 39) dice 50 o más.
- En la p. 18 el ARMA(1,1) usa $\hat x_{t-1}$ y no incluye $\bar\mu$; se entiende que trabaja con la serie centrada ($\dot x$).


---

<!-- fuente: corte-1-pronosticos/08-metodos-cualitativos/README.md -->
# Métodos cualitativos de pronóstico (Corte 1)

## Qué cubre

Métodos de pronóstico para cuando **no existen datos históricos**, como un producto nuevo o una situación sin precedentes: jurado de opinión ejecutiva, método Delphi, comité de la fuerza de ventas y encuesta de mercado. Incluye pautas para diseñar un cuestionario y un ejercicio propuesto. Es la última clase de pronósticos del corte 1. La carpeta solo tiene la presentación.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [`L09-qualitative-forecasting-methods.md`](/corte-1-pronosticos/08-metodos-cualitativos/L09-qualitative-forecasting-methods.md) | Clase 9 (7 diapositivas): cuatro métodos cualitativos, diseño de cuestionarios y ejercicio de encuesta | Sí |

El binario original es [`L09-qualitative-forecasting-methods.pdf`](/corte-1-pronosticos/08-metodos-cualitativos/L09-qualitative-forecasting-methods.pdf).

## Orden de estudio sugerido

1. L09, p. 2–4: objetivo y los cuatro métodos cualitativos.
2. L09, p. 5: cómo diseñar un cuestionario.
3. L09, p. 6: hacer el ejercicio (encuestas de máximo tres preguntas).
4. Para contrastar, la introducción a pronósticos de [`../02-introduccion-a-pronosticos/`](/corte-1-pronosticos/02-introduccion-a-pronosticos/), donde se clasifican los métodos en cualitativos y cuantitativos.

## Conceptos y fórmulas clave

La clase no tiene fórmulas. Los conceptos son:

| Método | Quién opina | Cómo funciona |
|---|---|---|
| Jurado de opinión ejecutiva | Expertos y gerentes de alto nivel (p. ej. 200) | Se combinan sus opiniones con herramientas estadísticas; aprovecha su conocimiento del contexto |
| Delphi | Tomadores de decisiones, personal y otros encuestados (5–10 expertos) | Cuestionarios individuales y anónimos; se recogen y comparten los resultados y se repite hasta el consenso |
| Comité de la fuerza de ventas | Vendedores o agentes de ventas | Cada uno pronostica sus ventas y se verifica su veracidad |
| Encuesta de mercado | Clientes | Preguntas sobre sus planes de compra futuros |

Pautas para el cuestionario:
- definir qué información se busca;
- preguntas claras y cortas, cerradas para respuestas concretas y abiertas para opiniones;
- preguntas sin sesgo, repitiendo una pregunta de distintas formas para comprobar la consistencia;
- ordenar las preguntas (y variar el orden si se puede);
- pocas preguntas.

El detalle está en [`L09-qualitative-forecasting-methods.md`](/corte-1-pronosticos/08-metodos-cualitativos/L09-qualitative-forecasting-methods.md).

## Ejercicios resueltos disponibles

No hay ejercicios resueltos. La p. 6 de L09 propone, sin solución, diseñar una encuesta de máximo tres preguntas para pronosticar (a) la demanda de la red wifi de la universidad y (b) la generación de basura de la universidad.

## Relación con otros temas y proyectos

- Introducción a pronósticos y su clasificación: [`../02-introduccion-a-pronosticos/`](/corte-1-pronosticos/02-introduccion-a-pronosticos/).
- Métodos cuantitativos del corte, para cuando sí hay datos: [`../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/`](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/), [`../05-tendencia-suavizacion-doble-holt/`](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/), [`../06-estacionalidad-winters-y-tracking-signal/`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/) y [`../07-arima/`](/corte-1-pronosticos/07-arima/).
- Ningún Excel ni proyecto del repo aplica estos métodos.


---

<!-- fuente: corte-1-pronosticos/08-metodos-cualitativos/L09-qualitative-forecasting-methods.md -->
# L09-qualitative-forecasting-methods

> **Archivo:** [`L09-qualitative-forecasting-methods.pdf`](/corte-1-pronosticos/08-metodos-cualitativos/L09-qualitative-forecasting-methods.pdf) · **Corte 1** · 7 páginas  
> **Nombre original:** `CORTE 1/Lec 9 - Qualitative methods for forecasting.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** métodos cualitativos de pronóstico, que se usan cuando no hay datos históricos (por ejemplo, un producto nuevo), y cómo diseñar un cuestionario.

**Ideas clave:**
- Cuando no existen datos históricos no se pueden aplicar los métodos cuantitativos de series de tiempo (clases 3 a 8); el pronóstico se basa en la opinión y el juicio de personas.
- Cuatro métodos cualitativos:

| Método | Quién opina | Cómo funciona | Tamaño o rasgo distintivo |
|---|---|---|---|
| Jurado de opinión ejecutiva (*Executive Opinion Jury*) | Expertos y gerentes de alto nivel | Se recoge su opinión y se procesa con herramientas estadísticas; aprovecha su conocimiento del contexto | Ejemplo: 200 expertos |
| Método Delphi | Tomadores de decisiones, personal y otros encuestados | Cuestionarios individuales y anónimos; se envía la encuesta, se recogen y comparten los resultados, y se repite hasta llegar a un consenso | 5–10 expertos |
| Comité de la fuerza de ventas (*Sales force committee*) | Vendedores o agentes de ventas | Cada uno pronostica sus ventas; se verifica la veracidad de sus estimaciones | Cercanía al cliente |
| Encuesta de mercado (*Market survey*) | Clientes | Preguntas sobre sus planes de compra futuros | Requiere un buen cuestionario |

- Reglas para diseñar un cuestionario: decidir qué información se quiere obtener; preguntas claras y cortas (cerradas para respuestas concretas, abiertas para opiniones); preguntas **no** sesgadas (se puede hacer la misma pregunta varias veces de distinta forma para comprobar la consistencia); ordenar las preguntas con cuidado (y, si se puede, variar el orden); pocas preguntas.

**Fórmulas y métodos:** la clase no tiene fórmulas. Los métodos son los cuatro de la tabla, junto con las pautas para diseñar el cuestionario.

**Ejemplos resueltos:** ninguno. La página 6 plantea un ejercicio sin solución: diseñar una encuesta de máximo tres preguntas para pronosticar (a) la demanda de la red wifi de la universidad y (b) la generación de basura de la universidad.

**Páginas clave:**
- p. 2: objetivo (pronóstico sin datos históricos).
- p. 3: jurado de opinión ejecutiva y método Delphi.
- p. 4: comité de la fuerza de ventas y encuesta de mercado.
- p. 5: diseño de cuestionarios.
- p. 6: ejercicio propuesto.

**Relación con otros archivos del repo:**
- Es el contrapunto de los métodos cuantitativos del corte 1: introducción a pronósticos en [`../02-introduccion-a-pronosticos/`](/corte-1-pronosticos/02-introduccion-a-pronosticos/), y suavización, Holt, Winters y ARIMA en [`../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/`](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/), [`../05-tendencia-suavizacion-doble-holt/`](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/), [`../06-estacionalidad-winters-y-tracking-signal/`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/) y [`../07-arima/`](/corte-1-pronosticos/07-arima/).
- No hay Excel ni proyecto del repo que aplique estos métodos.


---

<!-- fuente: corte-1-pronosticos/parcial-1/README.md -->
# Parcial 1: pronóstico de una demanda con tendencia (Corte 1)

## Qué cubre

Primer parcial del curso (Entrega I). Con 48 meses de ventas de un producto se hace el análisis descriptivo completo (estadísticos, histograma, boxplot, dispersión, correlograma y Ljung-Box), se diagnostica una **tendencia lineal decreciente sin estacionalidad**, se elige el método de **Holt** y se pronostican los meses 49 a 60 con sus medidas de error. El informe cierra con recomendaciones gerenciales sobre producción e inventario.

**Enunciado (deducido de los títulos del informe):** 1) análisis descriptivo y elección del método; 2) realizar el pronóstico; 3) estimar el error; 4) conclusión gerencial.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [`parcial-1-informe.md`](/corte-1-pronosticos/parcial-1/parcial-1-informe.md) | Informe en Word: diagnóstico, justificación de Holt, pronóstico, errores y conclusión gerencial | Sí (1.º) |
| [`parcial-1-calculos.md`](/corte-1-pronosticos/parcial-1/parcial-1-calculos.md) | Excel con todos los cálculos: 7 hojas (datos, estadísticos, histograma, boxplot, dispersión, correlograma, Holt) | Sí (2.º) |
| [`sales_data.csv`](/corte-1-pronosticos/parcial-1/sales_data.csv) | Datos del parcial (ver abajo). No tiene `.md` gemelo porque ya es texto plano | Consultar |

### `sales_data.csv`

Archivo de texto separado por comas, 48 filas más encabezado, con encabezados en inglés. Es el dato de entrada que se copió a la hoja `Datos` del Excel. Parece un conjunto de datos sintético del enunciado: el inventario no cumple el balance $I_t = I_{t-1} + P_t - D_t$.

| Columna | Significado | Mínimo | Máximo | Media |
|---|---|---|---|---|
| `Month` | «Month 1» … «Month 48» | — | — | — |
| `Actual Sales` | Demanda real (unidades) | 671 (mes 48) | 1.134 (mes 1) | 916,0 |
| `Forecasted Sales` | Pronóstico que usaba la empresa | 599 | 1.193 | 929,1 |
| `Inventory Levels` | Inventario a fin de mes | 2.089 (mes 9) | 10.622 (mes 48) | 4.629,6 |
| `Production Levels` | Producción del mes | 905 | 1.298 | 1.097,2 |

El pronóstico original tiene MAD = 100,2 y MAPE = 11,4 % frente a las ventas reales, y el inventario pasa de 2.546 (mes 1) a 10.622 (mes 48), es decir, se multiplica por 4,2.

## Orden de estudio sugerido

1. Leer el informe ([`parcial-1-informe.md`](/corte-1-pronosticos/parcial-1/parcial-1-informe.md)) para ver la historia completa y las decisiones.
2. Revisar en [`parcial-1-calculos.md`](/corte-1-pronosticos/parcial-1/parcial-1-calculos.md) cómo se calculó cada cosa: primero las hojas descriptivas y luego la hoja `Holt`.
3. Repasar la teoría: [L04](/corte-1-pronosticos/03-graficas-y-autocorrelacion/L04-plotting-your-data.md) (gráficas y correlograma), [L05](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md) (errores), [L06](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/L06-forecasting-data-with-trend.md) (Holt) y [L07](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md) (señal de rastreo y por qué no Winters).
4. Leer las observaciones al final de cada `.md` (errores y diferencias entre el informe y el Excel).

## Conceptos y fórmulas clave

- **Autocorrelación del rezago $k$** ($x_t$ = demanda, $\bar{x}$ = media, $n$ = 48):
  $$r_k = \frac{\sum_{t=1}^{n-k}(x_t-\bar{x})(x_{t+k}-\bar{x})}{\sum_{t=1}^{n}(x_t-\bar{x})^2}$$
  con límites $\pm\,t_{0{,}025;\,n-1}\cdot SE(r_k)$, donde $SE(r_k) = \sqrt{(1+2\sum_{j=1}^{k-1} r_j^2)/n}$. Detalle en [`parcial-1-calculos.md`](/corte-1-pronosticos/parcial-1/parcial-1-calculos.md#hoja-descriptivo-correlograma).
- **Ljung-Box:** $Q = n(n+2)\sum_{k=1}^{h}\frac{r_k^2}{n-k}$; si $Q > \chi^2_{\alpha;\,h}$ la serie no es ruido.
- **Holt** ($D_t$ = demanda, $S_t$ = nivel, $G_t$ = tendencia, $\alpha$ y $\beta$ = constantes de suavización, $h$ = meses hacia adelante):
  $$S_t = \alpha D_t + (1-\alpha)(S_{t-1}+G_{t-1}), \quad G_t = \beta(S_t - S_{t-1}) + (1-\beta)G_{t-1}, \quad F_{t+h} = S_t + h\,G_t$$
  Aquí $\alpha$ = 0,95, $\beta$ = 0,05, $S_0$ = 1.161,45 y $G_0$ = −10,02 (intercepto y pendiente de la regresión). Detalle en [`parcial-1-calculos.md`](/corte-1-pronosticos/parcial-1/parcial-1-calculos.md#hoja-holt).
- **Errores** ($e_t$ = error del mes $t$): $MAD = \frac{1}{n}\sum|e_t|$, $MAPE = \frac{1}{n}\sum|e_t|/D_t$, $MSE = \frac{1}{n}\sum e_t^2$, señal de rastreo $TS = \sum e_t/MAD$ (aceptable en ±4).
- **Regla de elección del método:** demanda estable → promedio móvil o suavización simple; tendencia → Holt o regresión; tendencia + estacionalidad → Winters. Aquí el diagnóstico da tendencia sin estacionalidad → Holt.

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado principal |
|---|---|---|
| Estadísticos descriptivos | Hoja `Descriptivo-Estadisticos` | Media 916, CV 15,4 %, caída de −40,8 %, regresión 1.161,45 − 10,02·t con $R^2$ = 0,988 |
| Histograma y boxplot | Hojas `Descriptivo-Histograma` y `Descriptivo-Boxplot` | Distribución plana; IQR = 250; 0 atípicos |
| Correlograma y Ljung-Box | Hoja `Descriptivo-Correlograma` | $r_1$ = 0,94 que decae despacio; Q = 274,4 > 21,0 |
| Pronóstico de Holt, meses 49 a 60 | Hoja `Holt` | 660,3 (mes 49) → 545,7 (mes 60); MAD 5,30; MAPE 0,60 %; MSE 40,7 |
| Recomendación gerencial | Informe | Producir 400–500 unid./mes para drenar ~10.600 unidades de inventario |

## Relación con otros temas y proyectos

- Teoría de pronósticos: [02-introduccion-a-pronosticos](/corte-1-pronosticos/02-introduccion-a-pronosticos/), [03-graficas-y-autocorrelacion](/corte-1-pronosticos/03-graficas-y-autocorrelacion/), [04-datos-estacionarios-promedio-movil-y-suavizacion-simple](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/), [05-tendencia-suavizacion-doble-holt](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/) y [06-estacionalidad-winters-y-tracking-signal](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/).
- Práctica previa al parcial: [`practica-metodos-pronostico-parcial-1.md`](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/practica-metodos-pronostico-parcial-1.md).
- El mismo tipo de diagnóstico se aplica en el proyecto del semestre: [proyecto-thyms-pronostico](/corte-1-pronosticos/proyecto-thyms-pronostico/) (Corte 1) y su revisión en el [gemelo digital del Corte 2](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/).
- La conclusión del parcial (bajar la producción por debajo de la demanda para drenar inventario) es una decisión de planeación agregada; ver [01-planeacion-agregada-modelo-bowman](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/).


---

<!-- fuente: corte-1-pronosticos/parcial-1/parcial-1-informe.md -->
# parcial-1-informe

> **Archivo:** [`parcial-1-informe.docx`](/corte-1-pronosticos/parcial-1/parcial-1-informe.docx) · **Corte 1** · Documento de Word  
> **Nombre original:** `CORTE 1/PARCIAL 1 PPCO.docx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

### Qué es

Informe escrito del **Parcial 1 — Entrega I** del Corte 1 (pronósticos). Analiza 48 meses de ventas de un producto ([`sales_data.csv`](/corte-1-pronosticos/parcial-1/sales_data.csv)), elige el método de **Holt** (suavización exponencial doble), pronostica los meses 49 a 60, estima el error y cierra con una conclusión gerencial. Todos los números salen del libro [`parcial-1-calculos.md`](/corte-1-pronosticos/parcial-1/parcial-1-calculos.md).

**Enunciado (deducido de los títulos de las secciones):** 1) análisis descriptivo de los datos y elección del método de pronóstico más adecuado; 2) realizar el pronóstico; 3) estimar el error de pronóstico; 4) conclusión gerencial.

### Estructura

| Sección | Qué hace |
|---|---|
| Portada | Logo de la Universidad de La Sabana (imagen), «PARCIAL», «ENTREGA I», miembros y «UNIVERSIDAD DE LA SABANA, CHÍA». La primera línea dice «Gerencia Financiera» (error de plantilla, ver advertencias). |
| Análisis descriptivo y elección del método | Estadísticos básicos y cinco gráficos: serie de tiempo (Fig. 1), histograma (Fig. 2), boxplot (Fig. 3), dispersión tiempo vs. demanda (Fig. 4) y correlograma (Fig. 5). Diagnóstico: tendencia decreciente fuerte, sin estacionalidad. |
| Por qué elegimos Holt | Descarta, uno por uno, el promedio móvil simple, el ponderado, la suavización exponencial simple y Winters, y justifica Holt (Fig. 6: demanda real vs. Holt). Menciona la regresión lineal como otra candidata válida. |
| Realizar el pronóstico | Explica $F_{48+h} = S_{48} + h\,G_{48}$ con $S_{48}$ = 670,7 y $G_{48}$ = −10,43 y da los pronósticos de los meses 49 a 60. |
| Estimar el error | MAD, MAPE, SSE, MSE, RMSE, sesgo, señal de rastreo e intervalo del 95 %. |
| Conclusión gerencial | Declive estructural, exceso de inventario y tres decisiones. |

Las figuras 1, 2, 4, 5 y 6 son gráficos de Word enlazados a las hojas `Datos`, `Descriptivo-Histograma`, `Descriptivo-Scatter`, `Descriptivo-Correlograma` y `Holt` del Excel; la Figura 3 es una imagen del boxplot (caja de ~789 a ~1.039, mediana ~931 en rojo, bigotes de 671 a 1.134).

### Datos que usa

`sales_data.csv`: 48 meses con ventas reales, pronóstico original de la empresa, inventario y producción (ver el [README de la carpeta](/corte-1-pronosticos/parcial-1/README.md)).

### Métodos

- Estadística descriptiva: media, mediana, desviación estándar, $CV = s/\bar{x}$, cuartiles e IQR.
- Gráficas de diagnóstico (clase [L04](/corte-1-pronosticos/03-graficas-y-autocorrelacion/L04-plotting-your-data.md)): serie, histograma, boxplot con vallas $Q_1 - 1{,}5\,IQR$ y $Q_3 + 1{,}5\,IQR$, dispersión con regresión $\hat{x}_t = a + b\,t$.
- Correlograma: $r_k = \frac{\sum_{t=1}^{n-k}(x_t-\bar{x})(x_{t+k}-\bar{x})}{\sum_{t=1}^{n}(x_t-\bar{x})^2}$ con límites de significancia al 95 %, y prueba de Ljung-Box $Q = n(n+2)\sum_{k=1}^{12}\frac{r_k^2}{n-k}$ frente a $\chi^2_{0{,}05;\,12}$.
- Holt ([L06](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/L06-forecasting-data-with-trend.md)): $S_t = \alpha D_t + (1-\alpha)(S_{t-1}+G_{t-1})$, $G_t = \beta(S_t - S_{t-1}) + (1-\beta)G_{t-1}$, $F_{t+h} = S_t + h\,G_t$, con $\alpha$ = 0,95 y $\beta$ = 0,05 ($S_t$ = nivel, $G_t$ = tendencia, $D_t$ = demanda, $h$ = meses hacia adelante).
- Errores ([L05](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md)): $MAD = \frac{1}{n}\sum|e_t|$, $MAPE = \frac{1}{n}\sum\frac{|e_t|}{D_t}$, $SSE = \sum e_t^2$, $MSE = SSE/n$, $RMSE = \sqrt{MSE}$, sesgo $= \frac{1}{n}\sum e_t$.
- Señal de rastreo ([L07](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md)): $TS = \sum e_t / MAD$, aceptable entre −4 y +4.
- Intervalo del 95 % para el mes siguiente: $F \pm 1{,}96 \cdot RMSE$.

### Resultados clave con números

| Resultado | Valor |
|---|---|
| Media / mediana / desviación / CV | 916 / 931,5 / 141 / 15,4 % |
| Máximo (mes 1) / mínimo (mes 48) | 1.134 / 671 |
| Caída acumulada en 48 meses | −40,8 % |
| Regresión | Ventas = 1.161,45 − 10,02·t, $R^2$ = 0,988, correlación −0,994 |
| IQR / atípicos | 250 / ninguno |
| Autocorrelaciones | $r_1$ = 0,94; $r_2$ = 0,88; $r_3$ = 0,82; $r_4$ = 0,76 (los cuatro significativos); sin pico en el rezago 12 |
| Ljung-Box | Q = 274,4 frente a 21,0 → no aleatoria |
| Holt: nivel y tendencia finales | 670,7 y −10,43 unid./mes |
| Pronósticos | Mes 49 ≈ 660; mes 52 ≈ 629; mes 54 ≈ 608; mes 60 ≈ 546 |
| MAD / MAPE | 5,3 unidades / 0,59 % |
| SSE / MSE / RMSE | 1.953,7 / 40,7 / 6,4 |
| Sesgo / señal de rastreo final | 0,18 / 1,6 |
| Intervalo del 95 % (mes 49) | ±12,5 → de 648 a 673 |
| Pronóstico anterior de la empresa | MAPE 11,4 % (error promedio de ~100 unidades) |
| Producción e inventario actuales | ~1.082 unid./mes; inventario > 10.600 (≈ 16 meses de demanda; se cuadruplicó) |

### Conclusiones

1. La demanda está en **declive estructural**: cae unas 10 unidades por mes, ya perdió el 41 % y seguiría bajando hasta ~546 en el mes 60 (≈ 17 % menos en un año).
2. El problema urgente es la respuesta de la empresa: producir ~1.082 unidades/mes con un pronóstico que sobreestimaba (MAPE 11 %) infló el inventario.
3. Tres decisiones: (a) adoptar Holt como pronóstico oficial y recalibrarlo cada mes; (b) recortar la producción por debajo de la demanda, a unas **400–500 unidades/mes**, para drenar el inventario (la sección del pronóstico hablaba de planear alrededor de 600–650 «e incluso por debajo»); (c) investigar las causas del declive y decidir si se invierte en el producto o se gestiona su salida del portafolio.
4. Los primeros 6 meses del pronóstico sirven para decidir producción y compras; los meses 7 a 12 son referencia de planeación.

### Supuestos y advertencias

- **Encabezado equivocado:** la primera línea del documento dice «Gerencia Financiera» por un error de plantilla; el contenido es del curso de Planeación (pronósticos).
- **Producción promedio:** el informe dice 1.082 unidades/mes, pero el promedio de los 48 meses de `sales_data.csv` es 1.097,2 (1.081,1 es el promedio de los primeros 12 meses).
- **MAPE:** el Excel guarda 0,5976 %, que redondea a 0,60 % (el informe escribe 0,59 %).
- **Sesgo y señal de rastreo** no están calculados en el Excel. Recalculados, el sesgo es 0,18 (con error = pronóstico − real) y la señal de rastreo final vale 1,6 en valor absoluto. Pero con la definición de MAD acumulado mes a mes, la señal sale de ±4 en los meses 15, 16, 18, 19, 38 y 44, no solo «en los primeros meses» como afirma el informe.
- **«Regresión prácticamente idéntica»:** la regresión da 670,6 en el mes 49 y 560,4 en el mes 60, frente a 660,3 y 545,7 de Holt: la misma pendiente, pero una diferencia de 10 a 15 unidades.
- El «17 % menos» compara el mes 60 con el pronóstico del mes 49 (546/660 − 1 = −17,4 %); frente a la venta real del mes 48 (671) la caída sería −18,7 %.
- Los errores son **dentro de la muestra** (pronóstico a un paso con parámetros e inicialización que usan los 48 datos), así que son optimistas; el intervalo de ±12,5 solo vale para el mes inmediato.
- El supuesto de fondo es que la caída lineal continúa; el informe lo reconoce y pide recalibrar cada mes.


---

<!-- fuente: corte-1-pronosticos/proyecto-thyms-pronostico/README.md -->
# Proyecto THYMS, Corte 1: pronóstico de ventas y métricas del sistema (Corte 1)

## Qué cubre

Primera entrega del proyecto del semestre sobre **THYMS Colombia S.A.S.**, que fabrica tintes para el cabello en tubos de 60 g. La empresa tiene una familia de tres productos:
- A: Kolorezza permanente;
- B: Visalia sin amoníaco;
- C: Thym's Coloring permanente.

Con las ventas reales de 2026 de **un vendedor (401) de la zona Antioquia**, el grupo:
1. exploró los datos;
2. pronosticó las ventas mensuales con **suavización exponencial simple** ($\alpha$ = 0,05);
3. calculó **takt time, throughput y WIP** de la línea de tubos.

Esta entrega es el punto de partida del [proyecto del Corte 2](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/) (S&OP y gemelo digital).

### Enunciado o entregable (deducido de los archivos)

No hay enunciado escrito en la carpeta. Por lo que contienen los archivos, se pidió:
1. análisis descriptivo y gráfico de las ventas reales (histograma, dispersión, boxplot, autocorrelograma, serie de tiempo);
2. elegir y aplicar un método de pronóstico con sus medidas de error (MAD, MSE, MAPE);
3. estudio preliminar del sistema: takt time, throughput y WIP, con la ley de Little.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [`VENTAS.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/VENTAS.md) | Datos de la empresa: ventas mensuales en COP de enero a agosto de 2026 (`UNIFICADO`) y 464 facturas de mayo a julio (`MAY-JUN-JUL`), anonimizadas | Sí (1.º) |
| [`Planeacion_proyecto_corte1.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/Planeacion_proyecto_corte1.md) | Cuaderno de Colab: gráficas exploratorias de las facturas, paso a unidades (12.900 COP/tubo), takt time, throughput y WIP | Sí (2.º) |
| [`pronostico-expo-simple-ppco.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple-ppco.md) | Excel con el pronóstico SES ($\alpha$ = 0,05) de enero a julio y el pronóstico de agosto; **versión corregida y final** | Sí (3.º) |
| [`pronostico-expo-simple.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple.md) | Primera versión del mismo Excel; MAD y MAPE mal promediados (incluyen enero, con error 0) | Solo para comparar |

**Diferencia entre los dos Excel de SES:**
- Datos, $\alpha$, pronósticos, SSE y MSE: idénticos.
- La primera versión promedia el MAD y el MAPE de enero a julio (`AVERAGE(D4:D10)`, `AVERAGE(F4:F10)`), incluyendo el error 0 de enero, y obtiene **68,7 millones y 45,8 %**.
- La versión PPCO los promedia de febrero a julio, igual que el SSE y el MSE, y obtiene **80,2 millones y 53,4 %**.
- La PPCO también corrige los títulos de las columnas («Error absoluto» y «Error % absoluto (APE)» en lugar de «MAD» y «MAPE») y cambia el orden de las hojas.

## Orden de estudio sugerido

1. [`VENTAS.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/VENTAS.md): qué datos hay y qué significa cada columna.
2. [`pronostico-expo-simple-ppco.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple-ppco.md): el pronóstico y sus errores.
3. [`Planeacion_proyecto_corte1.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/Planeacion_proyecto_corte1.md): gráficas y métricas del sistema.
4. La revisión crítica de este pronóstico en el Corte 2: sección 2.1 de [`Gemelo_Digital_Thyms.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md).

## Datos

| Fuente | Contenido | Cifras |
|---|---|---|
| `VENTAS.xls` → `UNIFICADO` | Ventas mensuales de 2026 en COP | Ene 95,8 M; Feb 153,9 M; Mar 201,0 M; Abr 52,4 M; May 197,5 M; Jun 156,6 M; Jul 231,0 M; Ago 119,9 M; promedio 151,0 M/mes |
| `VENTAS.xls` → `MAY-JUN-JUL` | 464 facturas, 161 clientes | `subdoc` total 590,8 M COP = 45.798 tubos (May 15.365; Jun 12.379; Jul 18.054) |

## Métodos

- **Pronóstico SES** ($A_t$ = venta real, $F_t$ = pronóstico): $F_{t+1} = \alpha A_t + (1-\alpha)F_t$, con $\alpha$ = 0,05 y $F_1 = A_1$.
- **Errores** ($n$ = 6, de febrero a julio): $MAD = \frac{1}{n}\sum|A_t - F_t|$, $MSE = \frac{1}{n}\sum(A_t-F_t)^2$, $MAPE = \frac{1}{n}\sum\frac{|A_t-F_t|}{A_t}$.
- **Conversión a unidades:** tubos = round(COP / 12.900).
- **Takt time:** $T_{takt} = T_{disponible}/\bar{d}$, con 480 min/día y $\bar{d}$ = demanda diaria.
- **Throughput:** $TH = \text{unidades}/\text{tiempo disponible}$.
- **Ley de Little:** $WIP = TH \times CT$, donde $CT$ = tiempo de ciclo.

## Resultados principales

| Resultado | Valor | Archivo |
|---|---|---|
| Pronóstico SES de agosto de 2026 | 114.671.388 COP (≈ 8.889 tubos de la zona) | `pronostico-expo-simple-ppco` |
| MAD / MAPE (feb–jul) | 80.172.875 COP / 53,4 % | `pronostico-expo-simple-ppco` |
| SSE / MSE | 4,33 × 10¹⁶ / 7,22 × 10¹⁵ (RMSE ≈ 84,9 M) | ambos Excel |
| Venta real de agosto (no usada para validar) | 119.882.540 COP (error de 4,3 %) | `UNIFICADO` |
| Días hábiles may–jul | 22 + 21 + 23 = 66 | cuaderno |
| Demanda diaria | 694 tubos/día | cuaderno |
| Takt time | 0,69 min/tubo ≈ 41,5 s | cuaderno |
| Throughput | 86,74 tubos/h (528 h disponibles) | cuaderno |
| WIP | 303,6 a 477,1 tubos (CT de 3,5 a 5,5 h) | cuaderno |

## Conceptos y fórmulas clave

- Suavización exponencial simple: $F_{t+1} = \alpha A_t + (1-\alpha)F_t$; un $\alpha$ pequeño hace el pronóstico casi plano y muy dependiente del arranque. Detalle en [`pronostico-expo-simple-ppco.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple-ppco.md).
- Sesgo y señal de rastreo ($e_t = A_t - F_t$): $\text{sesgo} = \frac{1}{n}\sum e_t$ y $TS = \sum e_t / MAD$. Aquí dan +63,1 M COP y 4,72 (calculados en el Corte 2).
- Takt time, throughput y ley de Little: ver [`Planeacion_proyecto_corte1.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/Planeacion_proyecto_corte1.md) y la clase [L02](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L02-introduction-to-production-systems.md).

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado principal |
|---|---|---|
| SES con $\alpha$ = 0,05 sobre 7 meses | [`pronostico-expo-simple-ppco.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple-ppco.md) | Agosto = 114,7 M COP; MAPE 53,4 % |
| Mismo SES con el error mal promediado | [`pronostico-expo-simple.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple.md) | MAD 68,7 M y MAPE 45,8 % (subestimados) |
| Exploración de 464 facturas | [`Planeacion_proyecto_corte1.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/Planeacion_proyecto_corte1.md) | Distribución sesgada a la derecha, $r_1$ ≈ 0,29 |
| Takt, throughput y WIP | [`Planeacion_proyecto_corte1.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/Planeacion_proyecto_corte1.md) | 0,69 min/tubo; 86,74 tubos/h; 304–477 tubos |

## Supuestos abiertos y advertencias

- **Escala zona → planta:** los datos son de un solo vendedor. En el Corte 2 se calcula que esta serie (~11.705 tubos/mes) es el **11,7 %** de la demanda de la planta (100.000 tubos/mes), y se escala por 8,54. Falta confirmarlo con la empresa.
- **Jornada:** aquí se supone 1 turno de 8 h de lunes a sábado; el libro del Corte 2 usa 2 turnos de 7 h de lunes a viernes.
- **Precio único** de 12.900 COP/tubo para los tres productos, aunque los descuentos de las facturas promedian el 40 % del valor bruto.
- **$\alpha$ = 0,05 sin justificación escrita**: es el que minimiza el MAPE, pero no el MAD ni el MSE. El arranque $F_1 = A_1$ (enero, mes bajo) sesga el pronóstico hacia abajo.
- **Julio de 2026:** el cuaderno resta 2 festivos, pero con el calendario oficial solo hay uno (20 de julio); serían 24 días hábiles y no 23.
- Error de impresión en la celda 21 del cuaderno (muestra 45.798 como «demanda diaria»; el valor usado es 694).
- Solo 8 meses de datos: no se puede validar estacionalidad.

## Cómo se conecta con el Corte 2

El [proyecto del Corte 2](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/) parte de estos archivos:

1. **Mismos datos.** El libro [`Datos Thyms Completo.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Datos%20Thyms%20Completo.md) copia las ventas mensuales (hoja `Ventas`) y las 464 facturas (hoja `Facturas Mayo-Julio`), y calcula los índices estacionales con ellas (julio 1,53; abril 0,35).
2. **Revisión del pronóstico.** La sección 2.1 del gemelo reproduce este SES (MAD 80,2 M, MAPE 53,4 %) y muestra que está **sesgado**: sesgo +63,1 M COP y señal de rastreo 4,72. Agosto: 114,7 M pronosticado frente a 119,9 M real.
3. **Corrección.** Con origen móvil se comparan 7 métodos y gana el mismo SES con $\alpha$ = 0,05 pero con **nivel inicial = promedio de los 3 primeros meses**: sesgo 44,6 M → 2,4 M y RMSE 76,8 M → 63,6 M (−17 %). El nivel resultante, 151,06 M COP/mes, se convierte en **100.038 tubos/mes de planta** con los mismos 12.900 COP/tubo y la escala de 8,54.
4. **Métricas.** El takt (41,5 s), el throughput (86,7 tubos/h) y el WIP (304–477 tubos) de este cuaderno se comparan en la sección 3.5 del gemelo con los del libro (11,1 s; 325 tubos/h; 8.500 tubos) y los del gemelo (10,3 s; 352 tubos/h; 5.308 tubos). No son comparables en magnitud porque aquí se mide la zona con jornada de 8 h.
5. **Tamaño de pedido.** Las 464 facturas alimentan la distribución lognormal del tamaño de pedido del gemelo: 1.273.304 COP ≈ 99 tubos por pedido.

## Relación con otros temas y proyectos

- Teoría: [L03](/corte-1-pronosticos/02-introduccion-a-pronosticos/L03-introduction-to-forecasting.md), [L04](/corte-1-pronosticos/03-graficas-y-autocorrelacion/L04-plotting-your-data.md), [L05](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md) (SES y errores) y [L07](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md) (señal de rastreo y estacionalidad).
- Mismo tipo de análisis con datos de clase: [parcial-1](/corte-1-pronosticos/parcial-1/).
- Continuación: [proyecto-thyms-gemelo-digital](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/), con el documento de traspaso [`CONTEXTO_GEMELO_THYMS.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/CONTEXTO_GEMELO_THYMS.md).


---

<!-- fuente: corte-1-pronosticos/proyecto-thyms-pronostico/Planeacion_proyecto_corte1.md -->
# Planeacion_proyecto_corte1

> **Archivo:** [`Planeacion_proyecto_corte1.ipynb`](/corte-1-pronosticos/proyecto-thyms-pronostico/Planeacion_proyecto_corte1.ipynb) · **Corte 1** · Cuaderno Jupyter con 34 celdas  
> **Nombre original:** `CORTE 1/PROYECTO/Planeacion_proyecto_corte1.ipynb`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

### Qué es

Cuaderno de Google Colab del **proyecto del Corte 1** sobre THYMS Colombia S.A.S. (tintes para el cabello en tubo de 60 g). Usa las 464 facturas de mayo a julio de 2026 de un vendedor de la zona Antioquia ([`VENTAS.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/VENTAS.md), hoja `MAY-JUN-JUL`) para:
1. explorar los datos con histograma, gráfico de retardo, boxplot, autocorrelograma y serie de tiempo;
2. pasar las ventas de pesos a tubos y calcular **takt time**, **throughput** y **WIP** (ley de Little).

El pronóstico de suavización exponencial simple del proyecto **no está en este cuaderno**: está en los Excel [`pronostico-expo-simple.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple.md) y [`pronostico-expo-simple-ppco.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple-ppco.md).

### Estructura

| Celdas | Sección | Qué hace |
|---|---|---|
| 0 | Librerías | seaborn, matplotlib, pandas, numpy y `plot_acf` de statsmodels |
| 1–2 | Carga | Sube `VENTAS.xls` a Colab (`files.upload()`) y lee la segunda hoja (`sheet_name=1`, `MAY-JUN-JUL`) |
| 3–4 | Revisión | `df.head()` (primeras 5 facturas) y conteo de vacíos en `subdoc`: 0 |
| 5–6 | Histograma | Histograma con curva de densidad de `subdoc` (COP por factura) |
| 7–8 | Gráfico de retardo | $x_t$ frente a $x_{t-1}$ (factura actual frente a la anterior) |
| 9–10 | Boxplot | Boxplot de `subdoc` |
| 11–12 | Autocorrelograma | ACF de `subdoc` con 20 rezagos y bandas de confianza |
| 13–14 | Serie de tiempo | `subdoc` en el orden de las facturas (índice 0 a 463) |
| 15–17 | Takt time, paso 1 | Demanda en unidades: `Demanda_unitaria = round(subdoc / 12900)` |
| 18–21 | Demanda diaria | Días hábiles reales de mayo, junio y julio; demanda total y diaria |
| 22–23 | Takt time, paso 2 | Tiempo disponible = 8 h = 480 min por jornada |
| 24–25 | Takt time, paso 3 | Takt = tiempo disponible / demanda diaria |
| 26–29 | Throughput | Unidades / tiempo total disponible del trimestre |
| 30–33 | WIP | Ley de Little con el tiempo de ciclo que dio la empresa (3,5 a 5,5 h) |

### Datos que usa

- `VENTAS.xls`, hoja `MAY-JUN-JUL`: 464 facturas (165 en mayo, 135 en junio, 164 en julio), columna `subdoc` = subtotal neto en COP (después de descuento y antes de IVA). Descripción completa en [`VENTAS.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/VENTAS.md).
- Precio supuesto: **12.900 COP por tubo** (para pasar de pesos a unidades).
- Datos de la empresa citados en el texto: 2 días de parada programada al mes; descansos escalonados que no detienen la planta; tiempo de ciclo de un tubo de 3,5 a 5,5 h.

### Métodos

- **Conversión a unidades:** $u_i = \mathrm{round}(\text{subdoc}_i / 12.900)$ por factura $i$.
- **Días hábiles reales:** días del mes − domingos − 2 días de parada − festivos de Colombia 2026:
  - mayo: 31 − 5 − 2 − 2 = 22;
  - junio: 30 − 4 − 2 − 3 = 21;
  - julio: 31 − 4 − 2 − 2 = 23;
  - total: 66 días (se trabaja de lunes a sábado).
- **Demanda diaria:** $\bar{d} = \sum u_i / \sum \text{días hábiles} = 45.798 / 66 \approx 694$ tubos/día.
- **Takt time:** $T_{takt} = \dfrac{T_{disponible}}{\bar{d}} = \dfrac{480 \text{ min}}{694 \text{ tubos}}$.
- **Throughput:** $TH = \dfrac{\text{unidades}}{\text{tiempo total}}$, con tiempo total $= (480/60)\cdot 66 = 528$ h.
- **WIP (ley de Little):** $WIP = TH \times CT$, donde $CT$ = tiempo de ciclo (3,5 a 5,5 h).

### Resultados clave con números

| Indicador | Valor |
|---|---|
| Facturas | 464, sin vacíos en `subdoc` |
| Demanda del trimestre (may–jul) | 45.798 tubos (mayo 15.365; junio 12.379; julio 18.054, recalculado con la misma regla) |
| Días hábiles | 22 + 21 + 23 = 66 |
| Demanda diaria promedio | 694 tubos/día |
| Takt time | 0,69 min/tubo (≈ 41,5 s/tubo) |
| Tiempo total disponible | 528 h |
| Throughput | 86,74 tubos/h |
| WIP | 303,59 tubos (CT = 3,5 h) a 477,06 tubos (CT = 5,5 h) |

**Gráficos** (marcados como `[gráfico]` abajo):
- **Histograma:** muy sesgado a la derecha. La mayoría de las facturas está por debajo de 2 millones de COP, con un pico de ~78 facturas cerca de 0,8 millones y una cola hasta 11,3 millones.
- **Gráfico de retardo:** nube concentrada cerca del origen, sin una recta clara; unos pocos pedidos grandes quedan aislados.
- **Boxplot:** mediana ~1,02 millones, caja de ~0,63 a ~1,55 millones y muchos atípicos por encima de ~2,9 millones (21 facturas, el mayor de 11,34 millones).
- **Autocorrelograma:** $r_1$ ≈ 0,29 fuera de la banda (±0,09); los demás rezagos están dentro o rozan la banda.
- **Serie de tiempo:** valores de factura en orden de emisión, en general bajo 3 millones, con picos de hasta ~11,3 millones (facturas grandes de un mismo cliente, cerca de la factura 350 y de la 435).

### Conclusiones

El cuaderno termina con: «El nivel de inventario en proceso (WIP) para la línea de tubos de tinte se sitúa entre 303.59 y 477.06 unidades, en función del tiempo de ciclo real de cada unidad dentro del rango de 3.5 a 5.5 horas.» El takt de 0,69 min/tubo y el throughput de 86,7 tubos/h describen el ritmo que exige la demanda **de esta zona**, no de la planta completa.

### Supuestos y advertencias

- **Error de impresión (celda 21):** el mensaje dice «La demanda diaria promedio es:45798.0 unidades», pero imprime `Dem_hist` (la demanda del trimestre). El valor diario correcto, `Dem_diaria_prom`, es 694, y es el que se usa en el takt.
- **Días hábiles de julio:** el cuaderno resta 2 festivos en julio de 2026. Según el calendario de festivos de Colombia que usa el gemelo del Corte 2 (celda 18 de [`Gemelo_Digital_Thyms.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md)), julio de 2026 solo tiene el 20 de julio. Con un festivo serían 24 días, 67 en total, y el takt quedaría en ~0,70 min/tubo.
- **Escala:** son las ventas de **un solo vendedor (401) de una zona**. En el Corte 2 se calcula que la venta promedio de esta serie (~11.705 tubos/mes) es solo el 11,7 % de la demanda de la planta (100.000 tubos/mes).
- **Jornada:** 1 turno de 8 h de lunes a sábado. El libro de datos del Corte 2 usa 2 turnos de 7 h de lunes a viernes.
- **Throughput = demanda:** se supone que se produjo exactamente lo vendido (no hay datos de producción).
- **Precio único** de 12.900 COP/tubo para los tres productos y para todos los clientes, aunque los descuentos de las facturas varían.
- Las gráficas exploratorias se hacen sobre **facturas individuales en orden de emisión**, no sobre una serie mensual; la autocorrelación del rezago 1 refleja facturas seguidas del mismo cliente más que un patrón de demanda en el tiempo.
- Depende de Colab (`google.colab.files`); para correrlo en local hay que reemplazar la celda 1 por la ruta del archivo.
