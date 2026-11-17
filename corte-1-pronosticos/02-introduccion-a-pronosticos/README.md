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
| [L03-introduction-to-forecasting.md](./L03-introduction-to-forecasting.md) | Lecture 3 «Introduction to Forecasting & Demand Planning» (35 diapositivas, 2026). Transcripción completa página por página, con la descripción de los gráficos (embudo del error, patrones de demanda, serie del nivel de un lago con tendencia $H=-0.0015t+3016.1$) y un resumen en español. | **Sí** (único archivo) |

## Orden de estudio sugerido
1. **Páginas 2–12:** definición, analítica, propósito (entradas + restricciones = demanda esperada), tipos e importancia.
2. **Páginas 13–19:** servicios, gestión de la demanda, horizontes, factores, hechos y riesgo (el error crece con el horizonte).
3. **Páginas 20–28:** el proceso y las etapas del pronóstico, sus parámetros y la clasificación de los métodos.
4. **Páginas 29–35:** patrones de demanda, práctica de identificación con gráficos, criterios de selección y software.
5. Después sigue [03-graficas-y-autocorrelacion](../03-graficas-y-autocorrelacion/), que enseña a graficar los datos para reconocer los patrones.

## Conceptos y fórmulas clave

Todo esto está en detalle en [L03](./L03-introduction-to-forecasting.md).

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
  | Estacionaria | Promedio móvil, suavización exponencial simple | [04-…](../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/) |
  | Con tendencia | Suavización doble (Holt) | [05-…](../05-tendencia-suavizacion-doble-holt/) |
  | Con tendencia y estacionalidad | Suavización triple (Winters) | [06-…](../06-estacionalidad-winters-y-tracking-signal/) |
  | Series con autocorrelación | Box-Jenkins | [07-arima](../07-arima/) |
  | Sin historia (producto nuevo) | Cualitativos (Delphi) | [08-metodos-cualitativos](../08-metodos-cualitativos/) |

## Ejercicios resueltos disponibles
La presentación no trae ejercicios numéricos. Tiene ejemplos ilustrativos:

| Ejemplo | Página de L03 | Resultado o mensaje |
|---|---|---|
| Pronósticos electorales de PollyVote (EE. UU. 2004, 2008 y 2012) | p. 4 | Errores entre −1 y +0.9 puntos porcentuales; el pronóstico más cercano a la elección es el más preciso |
| Disney | p. 9 | Error medio del 5 % a 5 años y del 0–3 % a 1 año |
| Embudo del error | p. 19 | 10 % → 20 % → 40 % en las semanas 1, 16 y 32 |
| Identificación de patrones (4 tipos de demanda, nivel de un lago con eventos ENSO, serie creciente 1993–2007) | p. 31–33 | Reconocer tendencia, ciclos, estacionalidad y aleatoriedad |

Los ejercicios numéricos de los métodos están en los Excel de las carpetas 03 a 06, en el [parcial 1](../parcial-1/) y en el [proyecto THYMS](../proyecto-thyms-pronostico/).

## Relación con otros temas y proyectos

- **Anterior:** [01-introduccion-curso-y-sistemas-de-produccion](../01-introduccion-curso-y-sistemas-de-produccion/). En L01, la meta 1 del semestre es «Forecast sales» y los criterios 1–2 de la rúbrica evalúan el análisis gráfico y la evaluación crítica de los pronósticos.
- **Siguientes del corte 1:**
  - [03-graficas-y-autocorrelacion](../03-graficas-y-autocorrelacion/)
  - [04-datos-estacionarios-promedio-movil-y-suavizacion-simple](../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/)
  - [05-tendencia-suavizacion-doble-holt](../05-tendencia-suavizacion-doble-holt/)
  - [06-estacionalidad-winters-y-tracking-signal](../06-estacionalidad-winters-y-tracking-signal/)
  - [07-arima](../07-arima/)
  - [08-metodos-cualitativos](../08-metodos-cualitativos/)
- **Aplicación:**
  - [parcial-1](../parcial-1/)
  - [proyecto-thyms-pronostico](../proyecto-thyms-pronostico/): pronóstico de la demanda real de una empresa.
- **Corte 2:**
  - El pronóstico de demanda es la entrada de la [planeación agregada](../../corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/).
  - La idea de que agregar reduce el error se retoma en [agregación y desagregación](../../corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/).
