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

## Contenido completo (página por página)

### Página 1 — Operations Management: Introduction to Forecasting (portada)

Operations Management · Introduction to Forecasting · 2026

> [Imagen decorativa: foto del campus, logo de la Universidad de La Sabana y logo de licencia Creative Commons BY-NC-SA]

### Página 2 — Lecture Objective

- To introduce forecasting methods, with their advantages and disadvantages for cases where no historical data exist.

### Página 3 — Qualitative Methods

- **Executive Opinion Jury:** Opinion of high-level experts and managers. Use statistical tools. E.g.: 200 experts. Knowledge of context.
- **Delphi Method:** meeting of decision-makers, staff, and other respondents. 5-10 experts. Personal and undisclosed identity survey questionnaires. The survey is sent out, the results are collected and socialized. Repeat until consensus is reached.

### Página 4 — Qualitative Methods

- **Sales force committee:** Salespeople or sales agents forecast sales. Their veracity is verified.
- **Market survey:** Questions about future purchasing plans.

### Página 5 — How to design a questionnaire?

- Decide what information I want to get.
- Clear and short questions.
  - Closed-ended questions: specific answers
  - Open-ended questions: opinions
- Questions that are NOT biased. You can ask the same question several times, in a different way.
- Structure the order of questions (where possible, vary the order).
- Few questions

### Página 6 — Ejercicio

- Diseñe una encuesta de máximo tres preguntas para pronosticar la demanda de la red wifi de la universidad.
- Diseñe una encuesta de máximo tres preguntas para pronosticar la generación de basura de la universidad.

(La diapositiva no trae solución.)

### Página 7 — Cierre

- Thanks!

William Guerrero, Ph.D.
