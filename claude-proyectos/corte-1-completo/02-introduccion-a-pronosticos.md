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

## Contenido completo (página por página)

### Página 1 — Operations Management: Introduction to Forecasting & Demand Planning

**Operations Management**

**Introduction to Forecasting & Demand Planning**

**2026**

> [Imagen decorativa: foto del campus de la Universidad de La Sabana (tono azul), logo de la Universidad de La Sabana e icono de licencia Creative Commons BY-NC-SA.]

### Página 2 — Lecture Objective

- To introduce forecasting methods, with their advantages and disadvantages.

### Página 3 — Definition

- Forecasting is the art or science of predicting future events!
- Finding the best estimation of what will happen under future uncertainty.
- There are many ways to forecast
  - Historical data
  - Subjective or intuitive predictions
  - Demand-driven data

> [Imagen decorativa: ilustración de una persona mirando por un telescopio, junto a una bombilla y un ícono de gráfico de barras.]

### Página 4 — What can we predict?

- Weather conditions
- Sports results
- Electoral Results
- **Consumer demand** (en negrita en la diapositiva)

Cada viñeta va acompañada de una imagen de ejemplo:

> [Imagen: pronóstico del clima de cinco días — MON 52°, TUE 26°, WED 30°, THU 63°, FRI 75°, con íconos de lluvia/nieve/nubes/sol; las leyendas pequeñas de cada día son casi ilegibles («Heavy Showers», «Light Snow», «Heavy Snow», «Partly Cloudy», «Sunny», aproximadamente).]

> [Imagen: captura de una casa de apuestas deportivas con probabilidades de un partido «GA Eagles» vs «Willem II» (mercados 3-Way Result, Over/Under, Asian Handicap, Both Teams To Score…). Los valores de cuotas son [ilegible].]

> [Imagen: tabla «Past predictions» de PollyVote, transcrita abajo.]

Texto de la imagen: *«The PollyVote method predicted the candidate's final vote shares in the last three U.S. presidential elections with little error. The following table shows the predicted and actual results of the two-party popular vote.»* — Source: PollyVote.

| Year | Winner | Actual result | Final forecast | 1 month before election | 3 months before election |
|---|---|---|---|---|---|
| 2012 | [foto del ganador] | 52.0% | 51.3% (prediction error [ilegible]) | 52.1% (prediction error +0.1) | 52.4% (prediction error +0.4) |
| 2008 | [foto del ganador] | 53.7% | 53.9% (prediction error [ilegible]) | 52.8% (prediction error −0.9) | 52.7% (prediction error −1) |
| 2004 | [foto del ganador] | 51.2% | 51.5% (prediction error [ilegible]) | 52.1% (prediction error +0.9) | 50.3% (prediction error −0.9) |

> Nota (deducido): el error se define en la tabla como pronóstico − real. Con esa regla los errores ilegibles del «Final forecast» serían −0.7 (2012), +0.2 (2008) y +0.3 (2004).

> [Gráfico: tablero de ventas «My Dashboard» (pestañas: My Dashboard, Sales Report, Sales Pipeline, Marketing, Search/Social, Incidents, History).
> - Gráfico de barras «Cumulative Sales Revenue This FY»: eje X meses Jan–Dec, eje Y de 0 a 100000. Valores aproximados leídos: Jan ≈ 0, Feb ≈ 5000, Mar ≈ 41500, Apr ≈ 41500, May ≈ 47000, Jun ≈ 53000, Jul ≈ 58000, Aug ≈ 58000, Sep ≈ 62000, Oct ≈ 64000, Nov ≈ 80500, Dec ≈ 80500 (acumulado siempre creciente o constante).
> - Gráfico de torta «Sales Revenue By Product»: Sprockets = 55500, Widgets = 16000, Glass Display Cases = 5575, Acrylic Display Cabinets = 3500 (total 80575, que coincide con el acumulado de diciembre).]

### Página 5 — Demand-driven data

> [Diagrama: «Gráfico 3: La nueva Cadena de suministro demand driven». Cinco bloques en cadena, de izquierda a derecha: **CLIENTES → OPERADORES → FABRICANTES → MATERIAS PRIMAS → PROVEEDORES**. Una flecha superior que va de izquierda a derecha (de clientes hacia proveedores) dice «Información en función de la demanda». Una flecha inferior que va de derecha a izquierda (de proveedores hacia clientes) dice «Productos generados para satisfacer esa demanda». Es decir: la información fluye desde la demanda hacia arriba en la cadena y los productos fluyen de vuelta hacia el cliente.]

Source: Nuevas tendencias en logística. OBS. Juan Carlos Palau

### Página 6 — The Future: Analytics

- https://www.youtube.com/watch?v=_HbjsNaUJ2A (enlace a un video)

> [Imagen: miniatura del video (ilustración de una reunión de trabajo alrededor de una mesa, con un tablero escrito al fondo).]

> [Imagen decorativa: logos y capturas de tableros de **Google Analytics** y **Microsoft Business Intelligence**.]

### Página 7 — The Future: Analytics

- Analytics es entendido como el uso intensivo de datos, estadística y análisis cuantitativo, modelos predictivos y explicativos y gestión basada en hechos para dar soporte al proceso de toma de decisiones, la creación de ventajas competitivas y la generación de valor en las organizaciones. Diversos ejemplos exitosos a nivel mundial son evidencia del potencial de aplicación de analytics en empresas e instituciones gubernamentales.

Source: https://analyticsforum.uniandes.edu.co/que-es-analytics/

### Página 8 — Potential competitive advantage increases with more sophisticated analytics

> [Diagrama: escalera de analítica. Eje Y: «Competitive Advantage»; eje X: «Sophistication of Inteligence» (sic). A medida que se sube en sofisticación, aumenta la ventaja competitiva. Cuatro niveles, de abajo hacia arriba, cada uno con sus técnicas y la pregunta que responden.]

| Nivel | Técnica | Pregunta que responde |
|---|---|---|
| Descriptive Analytics | Standard reports | "What happened?" |
| Descriptive Analytics | Ad hoc reports | "How many, how often, where?" |
| Descriptive Analytics | Query/drill down | "What exactly is the problem?" |
| Descriptive Analytics | Alerts | "What actions are needed?" |
| Predictive Analytics | Statistical analysis | "Why is this happening?" |
| Predictive Analytics | Forecasting/extrapolation | "What if these trends continue?" |
| Predictive Analytics | Predictive modeling | "What will happen next?" |
| Prescriptive Analytics | Experimental design | "What happens if we try this?" |
| Prescriptive Analytics | Optimization | "What's the best that can happen?" |
| Autonomous Analytics | Machine learning | "What can we learn from the data?" |

**Fuente:** Competing on Analytics: The New Science of Winning, 2017

### Página 9 — Why to forecast?

- Disney corporation: *Revenue: 55.63 billion USD (2016)*
  - Daily, Weekly, monthly, yearly, and 5-years forecasts.
  - Data from 3,000 schools (vacacion periods) in USA & abroad.
  - Promedio de error de 5% (5-años)
  - Promedio de error de 0-3% (1-año)
- Plan Food, beverages, hours of operation, staff, etc.

> [Imagen decorativa: foto de un parque temático de Disney (rueda de la fortuna y montaña rusa junto a un lago).]

### Página 10 — The purpose of forecasting

> [Diagrama: tres círculos negros unidos por los signos «+» y «=»:
> **INPUT**: Market research, historical data, advertising, Perception and expert opinion
> **+ CONSTRAINTS**: Management Policies, Available resources, Market conditions, Tech
> **= OUTPUT**: Expected demand (by product, by customer, by region)]

### Página 11 — Forecast types (according to data type)

- Economic Forecast
  - Business cycles: inflation, monetary policy, planning indicators.
- Technology Forecast
  - Rate of technological progress: new products and technologies
- Demand Forecast
  - Demand projections. (Una estrella dibujada resalta este punto; deducido: es el tipo de pronóstico en el que se centra el curso.)
  - It's not the same as forecasting sales

> [Imagen decorativa: mano dibujando un gráfico de barras creciente.]

### Página 12 — The importance of forecasting Demand

- It is important in all aspects of the business!
  - Supply chain management: *Procurement, Inventories, Raw Material, transport, storage ($$)*
  - Human Resources: *Hiring, training, & staff layoffs . ($$$)*
  - Capacity: *Machinery, work schedules. Avoid over capacity and shortages . ($$$$)*

> [Imagen decorativa: señal triangular roja de advertencia «!».] Los símbolos $$, $$$ y $$$$ indican el costo creciente de equivocarse en cada área.

### Página 13 — Forecasting for services industry

- Short term information is required:
  - Example, each 15 minutes
- Track events in the area:
  - Universities, congress, holidays.
- Special events

### Página 14 — Demand Management

- Modify demand paterns
  - Complementary products: with opposite cycle.
  - Promotions
  - Appointments and Reservation System
  - Revenue management
  - Backlog /Backorder

### Página 15 — Forecast types (according to timeframe)

- Short term: Up to one year. (3 months)
  - Daily, hourly, every half hour. By point of sale.
  - Helps plan workforce, production level, inventories and raw materials
- Medium term: Up to three years (1 year)
  - Monthly data.
  - Helps structure organizational and marketing plans
- Long term ( > 3 years) (5 years)
  - Annual data. Planning of new products, expansions.

> [Imagen decorativa: ícono de calendario.]

### Página 16 — Main Differences between the forecasts

1. Long-term forecasts include many factors.
2. Short-term forecasts include several mathematical methods.
3. Short-term forecasts are more accurate

### Página 17 — Factors that influence the forecast

- Product Life Cycle
- Demand for related products: complements (relationship with other variables)
- Product price, quality and customer perception (expert opinion)
- External factors:
  - Climatic
  - Political & Economic
  - Social & demographic
  - Market: Competition

### Página 18 — Facts about forecasting

- Unpredictable external factors
- Many methods assume stability (!)
- Forecasts aggregated by product families have less error.
  - Disaggregation into SKUs (stock-keeping unit)
- Forecasting units:
  - $, unit, kg, m³, working hours.

### Página 19 — Risks associated to Forecasting

- Error is unavoidable!
- Risks when making decisions

> [Gráfico: «embudo» del error. Eje Y: «Error del Pronóstico»; eje X: «Tiempo». Dos curvas azules simétricas respecto al eje horizontal (banda superior e inferior) que se abren a medida que avanza el tiempo. Marcas: **Semana 1 → 10 %**, **Semana 16 → 20 %**, **Semana 32 → 40 %**. Mensaje: cuanto más lejos en el futuro se pronostica, mayor es el error (el error crece de forma acelerada con el horizonte).]

### Página 20 — Process of making and using forecasts

> [Diagrama de flujo en seis cajas:
> Fila 1: **Historical data → Modeling approach → Forecasting**
> De «Forecasting» una flecha baja a la fila 2: **Error estimation → Feedback: Model tunning → Next period**
> Una flecha roja curva rotulada **«Repeat»** sale de «Feedback: Model tunning» y regresa a «Modeling approach» (ciclo de ajuste del modelo).]

### Página 21 — Forecasting stages

1. TARGET SETTING
   - What is the variable to forecast?
   - Planning Horizon?
2. DATA PREPARATION
   - Tabulation - Chronological order
3. EVALUATION AND SELECTION OF THE TECHNIQUE
   - Demand behavior?
   - Trend/Seasonality/Randomness?-Exponential Smoothing: Simple, Double(Holt), Triple(Winters)

### Página 22 — Forecasting stages (continuación)

4. FORECAST RUN
   - A period ahead
   - Several periods ahead
5. FORECAST TRACKING
   - Is the method selected appropriate?
   - Does the method have to be adjusted?
   - Analysis of the errors

### Página 23 — Forecast system: 8 steps

1. Determining the use of the forecast
2. Select the items to forecast
3. Determine the planning horizon
4. Select forecast model: Quantitative or Qualitative
5. Collection of data: Historical data and events
6. Data analysis: descriptive statistics
7. Make the forecast
8. Validate and implement the results: Types of error and validation with historical data

### Página 24 — Forecasting Sales: keep in mind

- Aggregated forecast is more accurate.
- Quantitative methods are useful in the short term and for product families (aggregated units).
- Estimate its confidence and error.
- The longer the planning horizon, the bigger the expected error.
- The greater the **granularity**, the bigger the expected error.
- Should include all available information

### Página 25 — Forecast Parameters

- **VARIABLE** (Demand, inventory availability)
- **TIME HORIZON:** Timeframe for the forecast. Example: sales for **2020**.
- **GRANULARITY:** The level of detail (daily ,weekly ,monthly ,yearly, 10-years, etc.)
- **UPDATE FREQUENCY**

### Página 26 — Forecasting Model

Method by which we try to **know** the future behavior of a variable with some degree of certainty.

It is a process of estimating a future event by **projecting** data from the past into the future.

It is a key success factor for planning operations!

### Página 27 — Forecasting methods

- **Qualitative approach:** Subjective but inclusive of many factors.
  - New products for example
  - Cause-effect relationships
- **Quantitative approach:** Based on mathematical models with historical information and other variables.
  - Causal: Regression Methods
  - Time series.
  - Simulation

### Página 28 — Forecasting methods

- **QUALITATIVE METHODS (SUBJECTIVES) -** Opinion forecasts (DELPHI method)
- **QUANTITATIVE (MATHEMATICAL) METHODS**
  - Forecasting based on averages
  - Forecasts by time series
  - Exponential Smoothing Methods
  - Multiplicative Winters
  - Box - Jenkins
  - Causal forecasting: Regression Methods

### Página 29 — Demand patterns

- Horizontal: Regression toward the mean factors
- Trend: Systematic increase/decrease in the average.
- Seasonal: Repetitive pattern in time periods
- Cyclic: Unpredictable repetitive pattern over long periods of time (life cycle).
- Random: Unpredictable variations.

### Página 30 — Elements in demand patern

- **Trend:** A pattern of behavior of a time series over a unit of time.
- **Cyclical:** It is a wave that travels along the trend with points above and below it.
- **Seasonality:** A pattern of behavior that is repeated year after year or at fixed intervals.
- **Randomness:** It occurs when a sample of historical data shows a large dispersion of behavior.

### Página 31 — Demand Behavior

> [Gráfico: cuadrícula 2×2 de diagramas de dispersión (puntos de demanda en el tiempo, sin valores numéricos en los ejes):
> 1. **Demanda estacionaria** (arriba izquierda): unos 14 puntos dispersos arriba y abajo de una recta horizontal; no hay tendencia.
> 2. **Demanda con tendencia** (arriba derecha): puntos que suben de forma sostenida pegados a una recta de pendiente positiva.
> 3. **Demanda con estacionalidad** (abajo izquierda): puntos que forman una onda alrededor de una recta horizontal (suben, bajan hasta un mínimo y vuelven a subir).
> 4. Panel sin título (abajo derecha), *deducido: tendencia + estacionalidad*: puntos que oscilan en forma de onda alrededor de una recta de pendiente positiva.]

### Página 32 — What elements can be identified?

> [Gráfico de líneas: eje Y «Nivel del lago (msnm)» de 3013 a 3016 (marcas cada 0.5); eje X «tiempo (meses)» desde Jan-58 hasta después de Jan-96 (marcas cada dos años: Jan-58, Jan-60, …, Jan-96).
> - Serie marrón con puntos: nivel mensual observado; oscila con picos y valles frecuentes (variación estacional/aleatoria) entre ≈3013.8 y ≈3015.7.
> - Serie azul: curva suavizada de la anterior (deducido: promedio móvil), con ondas de varios años (comportamiento cíclico); mínimos marcados hacia 1975 y 1990–1993.
> - Recta negra: tendencia lineal decreciente con la ecuación **H = −0.0015t + 3016.1**, que baja de ≈3015.05 al inicio a ≈3014.35 al final.
> - Barras rojas rotuladas «EVENTOS ENSO» (El Niño–Oscilación del Sur) en los periodos aproximados 1965–66, 1968–70, 1972–74, 1976–78, 1982–84, 1986–88, 1991–92 y 1994–95; suelen coincidir con caídas del nivel.
> Pregunta de la diapositiva: identificar los elementos. Lectura (deducida): tendencia decreciente, ciclos plurianuales asociados a eventos ENSO, estacionalidad dentro del año y componente aleatoria.]

La ecuación de tendencia del gráfico es

$$H = -0.0015\,t + 3016.1$$

donde $H$ es el nivel del lago (m s. n. m.) y $t$ es el tiempo (deducido: en meses, según el eje). La pendiente $-0.0015$ indica que el nivel baja 0.0015 m por periodo.

### Página 33 — What elements can be identified?

> [Gráfico de líneas (sin título ni nombre de variable; deducido: un índice): línea roja; eje Y con marcas 95.2, 101.0, 106.8, 112.6, 118.4, 124.1, 129.9, 135.7, 141.5, 147.3, 153.1; eje X de 1993 a 2007 con marcas mensuales.
> Recorrido: arranca cerca de 100 en 1993, sube a ≈106 en 1994, cae bruscamente a ≈96 en 1995, luego crece casi sin interrupción hasta ≈129 en 2000 (con un pequeño pico y caída en 2000), se mantiene plano alrededor de 128–130 entre 2001 y 2003, y vuelve a crecer hasta ≈153 a finales de 2007.
> Lectura (deducida): tendencia creciente de largo plazo, una caída puntual (1995), una meseta (2001–2003) y pequeñas fluctuaciones aleatorias; no se ve estacionalidad marcada.]

### Página 34 — Criteria in the Selection of a Forecasting Method

- Characteristics of demand
- Complexity of the model
- Model Precision
- It is essential to take into account the stage of the product life cycle.
- Establish a historical database
- When possible, make aggregated forecasts
- Forecasts are not an objective to be met... They are always subject to error.

### Página 35 — Forecasting Software

- R
- Matlab
- SPSS
- Minitab

> [Imagen decorativa: logos de R, MATLAB («The Language of Technical Computing»), SPSS y Minitab.]
