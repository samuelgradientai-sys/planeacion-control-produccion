<!-- fuente: corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/README.md -->
# Datos estacionarios: promedio móvil y suavización exponencial simple (Corte 1)

## Qué cubre
Métodos de pronóstico para demanda **estacionaria** (una constante más ruido, sin tendencia ni estacionalidad): promedio móvil simple, promedio móvil ponderado y suavización exponencial simple, con sus ventajas, desventajas y la elección de $n$ y de $\alpha$. Cubre también cómo medir el error de un pronóstico (MAD, SSE, MSE, MAPE, PME) y por qué los indicadores no bastan: un buen método deja residuales aleatorios, sin sesgo, alrededor de cero. Los Excel comparan métodos sobre ventas reales y repasan los ejercicios de la clase antes del parcial 1.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [L05-forecasting-stationary-data-and-errors.md](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md) | Lecture 5 (31 diapositivas): MA simple y ponderado, suavización exponencial simple, elección de α, SES frente a MA, medidas de error y análisis de residuales. Incluye los datos de los ejemplos (21 periodos) y sus soluciones calculadas. | **Sí** |
| [promedio-movil-y-suavizacion-exponencial.md](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/promedio-movil-y-suavizacion-exponencial.md) | Excel de clase: compara PM(6), PM(12), SE(α = 0,2) y SE(α = 0,8) sobre 30 días de las ventas propias de la tarea del tema 03, con MAD, MSE y error %. Las otras 14 hojas son copia exacta de [tarea-class-example-1](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-1.md). | Segundo |
| [practica-metodos-pronostico-parcial-1.md](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/practica-metodos-pronostico-parcial-1.md) | Excel de práctica para el parcial 1: MA simple con MAD/SSE/MSE/MAPE, ejercicio de la diapositiva 30 (MA 3 frente a MA 5), MA ponderado y SES. Datos aleatorios (`RANDBETWEEN`), varios errores de fórmula documentados y hojas de Holt y Winters vacías. | Tercero |

CSV completo de la hoja larga de comparación: [promedio-movil-y-suavizacion-exponencial-datos/Ventas_propias_2.csv](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/promedio-movil-y-suavizacion-exponencial-datos/Ventas_propias_2.csv) (incluye pronósticos y errores); también están `Ventas_propias.csv` y `Ventas_competencia.csv` en la misma carpeta.

## Orden de estudio sugerido
1. [L05](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md), p. 1–11: promedio móvil simple y ponderado, con sus desventajas (recalcular, rezago frente a tendencias).
2. L05, p. 12–20: suavización exponencial simple, interpretación como corrección del error, elección de α y comparación con MA.
3. L05, p. 21–30: medidas de error y análisis de residuales.
4. [practica-metodos-pronostico-parcial-1](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/practica-metodos-pronostico-parcial-1.md): rehacer cada método en Excel (y revisar los errores señalados).
5. [promedio-movil-y-suavizacion-exponencial](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/promedio-movil-y-suavizacion-exponencial.md): comparación de cuatro métodos con datos reales.
6. Siguiente tema: [05 — tendencia y Holt](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/README.md).

## Conceptos y fórmulas clave
Detalle en [L05](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md).

- **Promedio móvil simple:** $F_t=\dfrac{A_{t-1}+A_{t-2}+\dots+A_{t-n}}{n}$ ($A$: demanda real; $n$: periodos promediados). $n$ grande suaviza más pero reacciona más lento.
- **Promedio móvil ponderado:** $F_t=w_0A_t+w_1A_{t-1}+\dots+w_nA_{t-n}$ con $\sum w_i=1$ y más peso en lo reciente (la diapositiva escribe el último término como $w_nA_t$).
- **Suavización exponencial simple:**
  $$F_t=\alpha D_{t-1}+(1-\alpha)F_{t-1}=F_{t-1}-\alpha e_{t-1}$$
  $D$: demanda; $\alpha\in[0,1]$; $e_{t-1}=F_{t-1}-D_{t-1}$. El dato con $k$ periodos de antigüedad pesa $\alpha(1-\alpha)^k$. Valores recomendados $0{,}1\le\alpha\le0{,}3$; α pequeño para demanda estable. $F_1$ se fija con un promedio móvil, el último dato o la opinión de un experto.
- **Pronóstico de varios pasos:** con un modelo estacionario, el mismo $F_{t+1}$ sirve para $t+2, t+3,\dots$
- **Medidas de error** ($e_t=F_t-D_t$; $n$ o $T$ = número de periodos con pronóstico):
  $$MAD=\frac{\sum|A_i-F_i|}{n},\quad SSE=\sum(A_i-F_i)^2,\quad MSE=\frac{SSE}{n},\quad MAPE=\frac{100}{n}\sum\frac{|A_i-F_i|}{A_i}$$
  PME (como está en la diapositiva): $PME=\frac{1}{n}\sum e_t^2/D_t$.
- **Residuales:** deben ser aleatorios y centrados en cero; un método con menor MSE pero errores siempre del mismo signo está sesgado (L05, p. 29).

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado principal |
|---|---|---|
| MA con $n=3$ y $n=9$ (datos de 21 periodos) | [L05](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md), p. 6 (solución calculada en el resumen) | $F_{22}=491{,}67$ ($n=3$) y $500{,}22$ ($n=9$) |
| MA rezagado frente a tendencia | L05, p. 8 | MA(3) queda 4 unidades y MA(6) 7 unidades por debajo de la demanda |
| WMA $n=3$, pesos 0,75/0,15/0,1 | L05, p. 11 (solución calculada) | $F_{22}=523{,}15$ |
| SES $\alpha=0{,}05$, $F_1=540$ | L05, p. 16 (solución calculada) | $F_{22}=511{,}89$ |
| ¿Método 1 (MAD 5,77; MSE 51,69) o método 2 (MAD 6; MSE 41,8)? | L05, p. 29 | Método 1: el método 2 tiene errores siempre negativos (sesgo) |
| MA $n=3$ frente a $n=5$ (diapositiva 30) | [practica-metodos-pronostico-parcial-1](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/practica-metodos-pronostico-parcial-1.md), hoja `EJERCICIO DIAPO` | MA(5) mejor: MAD 1,74 frente a 2,47; MSE 4,39 frente a 8,44; MAPE 10,8 % frente a 20,0 % |
| MA simple con datos aleatorios | práctica, hoja `MA SIMPLE` | $F_{22}=553{,}33$; MAD 23,30 en la hoja (28,22 con la alineación correcta) |
| WMA con datos aleatorios | práctica, hoja `MA PONDERADO` | La hoja da 177,017 por dividir entre $n$; lo correcto es 531,05 |
| SES con datos aleatorios | práctica, hoja `SE SIMPLE` | Un solo paso: 533,35 (con α = 0,95) |
| PM(6), PM(12), SE(0,2), SE(0,8) sobre 30 días de ventas | [promedio-movil-y-suavizacion-exponencial](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/promedio-movil-y-suavizacion-exponencial.md) | MAD 235,9 / 236,1 / **229,7** / 237,3; MSE **69.652** / 70.490 / 70.977 / 86.233; MAPE 12,21 % / 12,15 % / **11,98 %** / 12,34 % → SE(0,2) el mejor en MAD y MAPE, SE(0,8) el peor |

## Relación con otros temas y proyectos
- Viene de [03 — gráficas y autocorrelación](/corte-1-pronosticos/03-graficas-y-autocorrelacion/README.md): el correlograma dice si la serie es aleatoria (y entonces se usan estos métodos). La serie de ventas usada en [promedio-movil-y-suavizacion-exponencial](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/promedio-movil-y-suavizacion-exponencial.md) es la de [tarea-class-example-1](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-1.md), que allí se muestra aleatoria.
- Si la serie tiene tendencia: [05 — suavización doble de Holt](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/README.md). Si además tiene estacionalidad, y para controlar el sesgo con la señal de rastreo: [06 — Winters y tracking signal](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/README.md).
- Aplicación: el [proyecto THYMS de pronóstico](/corte-1-pronosticos/proyecto-thyms-pronostico/README.md) usa suavización exponencial simple; el [parcial 1](/corte-1-pronosticos/parcial-1/README.md) evalúa estos métodos y sus medidas de error.


---

<!-- fuente: corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md -->
# L05-forecasting-stationary-data-and-errors

> **Archivo:** [`L05-forecasting-stationary-data-and-errors.pdf`](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.pdf) · **Corte 1** · 31 páginas  
> **Nombre original:** `CORTE 1/Lec 5 - forecasting stationary data and errors.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** métodos de pronóstico para demanda estacionaria (sin tendencia ni estacionalidad): promedio móvil simple, promedio móvil ponderado y suavización exponencial simple, más las medidas de error (MAD, SSE, MSE, MAPE, PME) y el análisis de residuales para elegir el mejor método.

**Ideas clave**

- Los métodos de la clase sirven para datos aleatorios que «regresan al promedio», sin tendencia ni estacionalidad (p. 2, 4, 19).
- **Promedio móvil simple (MA):** el pronóstico es el promedio de las últimas $n$ demandas. Desventaja 1: hay que recalcular el promedio con cada dato nuevo; desventaja 2: se queda rezagado frente a una tendencia, más cuanto mayor es $n$ (p. 5–8).
- **Promedio móvil ponderado (WMA):** da más peso a los datos recientes; los pesos suman 1 y deben reflejar la importancia de cada periodo (fallas de máquina, eventos especiales, estacionalidad) (p. 9–10).
- **Suavización exponencial simple (SES):** el nuevo pronóstico es un promedio ponderado entre el último dato y el último pronóstico; equivale a corregir el pronóstico anterior con una fracción $\alpha$ del error. El peso de los datos decae geométricamente: $\alpha,\ \alpha(1-\alpha),\ \alpha(1-\alpha)^2,\dots$ (p. 12–15).
- El primer pronóstico de SES se puede fijar con un promedio móvil, con el dato más reciente o por opinión de expertos (p. 15).
- **Elección de α:** entre 0 y 1; α pequeño para demanda estable (más peso al pasado), α cercano a 1 para seguir variaciones fuertes. Se puede comparar 0,2 frente a 0,8 con el histórico o probar valores que minimicen el error; valores recomendados $0{,}1\le\alpha\le0{,}3$ (p. 17–18).
- MA y SES suponen un modelo estacionario: el pronóstico hecho en $t$ es para $t+1$ y sirve igual para varios pasos adelante (p. 19).
- **SES frente a MA** (p. 20): ambos modelan demanda = constante + ruido de media cero, dependen de un solo parámetro ($N$ pequeño o $\alpha$ grande = más sensibilidad y más varianza del error) y se rezagan con tendencias. Diferencias: SES pondera todo el pasado y MA solo los últimos $N$ datos; SES solo necesita guardar el último pronóstico (300.000 ítems: SES guarda 300.000 datos; MA de 12 meses, 300.000 × 12).
- **Errores** (p. 21–26): el error o residual es $e_t=F_t-D_t$; $T$ es el número de periodos con pronóstico (no confundir con el $n$ del MA).
- **Los indicadores no bastan** (p. 27–29): un buen método deja residuales aleatorios, sin patrón ni sesgo, distribuidos alrededor de cero. En la p. 29 el método 2 tiene menor MSE (41,8 frente a 51,69) pero todos sus errores son negativos (sesgo), mientras que los del método 1 oscilan alrededor de cero.

**Fórmulas y métodos**

| Método o medida | Fórmula | Símbolos y uso |
|---|---|---|
| Promedio móvil simple (p. 5) | $F_t=\dfrac{A_{t-1}+A_{t-2}+\dots+A_{t-n}}{n}$ | $A$: demanda real; $n$: número de periodos. Demanda estable sin tendencia. |
| Promedio móvil ponderado (p. 9) | $F_t=w_0A_t+w_1A_{t-1}+\dots+w_nA_{t-n}$, con $\sum w_i=1$ | $w_i$: peso del dato con $i$ periodos de antigüedad ($w_0$ el más reciente). La diapositiva escribe el último término como $w_nA_t$. |
| Suavización exponencial simple (p. 12) | $F_t=\alpha D_{t-1}+(1-\alpha)F_{t-1}$ | $D$: demanda; $\alpha\in[0,1]$: constante de suavización. |
| Forma de corrección del error (p. 15) | $F_t=F_{t-1}-\alpha(F_{t-1}-D_{t-1})=F_{t-1}-\alpha e_{t-1}$ | $e_{t-1}=F_{t-1}-D_{t-1}$. |
| Peso del dato con $k$ periodos de antigüedad (p. 13) | $\alpha(1-\alpha)^k$ | Con $\alpha=0{,}05$: 0,05; 0,0475; 0,045125; 0,04286875. |
| Error (p. 22) | $e_t=F_t-D_t$ | |
| MAD o DAM (p. 23) | $MAD=\dfrac{\sum_{i=1}^{n}\lvert A_i-F_i\rvert}{n}=\dfrac{\sum_{t=1}^{T}\lvert e_t\rvert}{T}$ | Dispersión del error, en unidades de la demanda. |
| SSE (p. 24) | $SSE=\sum_{i=1}^{n}(A_i-F_i)^2$ | Penaliza más los errores grandes. |
| MSE (p. 24) | $MSE=\dfrac{SSE}{n}=\dfrac{\sum E_t^2}{n}$ | |
| MAPE o EPAM (p. 25) | $MAPE=\dfrac{100}{n}\sum_{i=1}^{n}\dfrac{\lvert A_i-F_i\rvert}{A_i}$ | Error relativo en %, normaliza por la magnitud de los datos. |
| PME (p. 26) | $PME=\dfrac{1}{n}\sum_{t=1}^{n}\dfrac{e_t^2}{D_t}$ | Tal como está en la diapositiva (con el error al cuadrado). |

**Ejemplos resueltos**

Las diapositivas plantean los ejemplos pero no muestran la solución. Los resultados marcados como «calculado» se obtuvieron aplicando las fórmulas de la clase a los datos de la p. 6 (21 periodos, media 495,5); no aparecen en el PDF.

| Ejemplo | Página | Resultado |
|---|---|---|
| MA con $n=3$ y $n=9$, cuatro periodos adicionales | 6 | Calculado: $F_{22}=\frac{454+480+541}{3}=491{,}67$ con $n=3$ y $F_{22}=500{,}22$ con $n=9$; al ser un modelo estacionario, el mismo valor sirve para los periodos 22 a 25. |
| MA rezagado frente a una tendencia (demanda 2, 4, …, 24) | 8 | MA(3) queda 4 unidades por debajo y MA(6), 7 unidades por debajo de la demanda. |
| WMA con $n=3$, $w_0=0{,}75$, $w_1=0{,}15$, $w_2=0{,}1$ | 11 | Calculado: $F_{22}=0{,}75(541)+0{,}15(480)+0{,}1(454)=523{,}15$ (también para los periodos 23 a 25). |
| Pesos de SES con $\alpha=0{,}05$ | 13 | 0,05; 0,0475; 0,045125; 0,04286875. |
| SES con $\alpha=0{,}05$ y $F_1=540$ | 16 | Calculado: $F_2=0{,}05(482)+0{,}95(540)=537{,}1$, …, $F_{22}=511{,}89$. |
| Comparación α = 0,1 frente a α = 0,5 | 18 | Con α = 0,1 el pronóstico es casi plano (≈ 22,4–23,9); con α = 0,5 sigue la demanda con un periodo de retraso. |
| Residuales esperados | 28 | ME ≈ 0; MAD 18,2; MAPE ≈ 1 %; MSE 506,25; σE 22,50. |
| ¿Cuál es el mejor método? | 29 | Método 1: MAD 5,77, MSE 51,69, errores alrededor de cero; método 2: MAD 6, MSE 41,8, errores siempre negativos. Deducido de la p. 27: es preferible el método 1 porque el método 2 está sesgado, aunque tenga menor MSE. |
| Ejercicio MA $n=3$ frente a $n=5$ | 30 | Resuelto en [practica-metodos-pronostico-parcial-1.md](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/practica-metodos-pronostico-parcial-1.md) (hoja `EJERCICIO DIAPO`): MA(3) MAD 2,47, MSE 8,44, MAPE 20,0 %; MA(5) MAD 1,74, MSE 4,39, MAPE 10,8 % → MA(5) es mejor. |

**Páginas clave**

- p. 2–4: objetivo y alcance (datos estacionarios).
- p. 5–8: promedio móvil simple, ejemplo y desventajas.
- p. 9–11: promedio móvil ponderado y ejemplo.
- p. 12–18: suavización exponencial simple, interpretación, ejemplo y elección de α.
- p. 19–20: pronóstico de varios pasos y comparación SES frente a MA.
- p. 21–26: definiciones de error y medidas MAD, SSE, MSE, MAPE y PME.
- p. 27–30: análisis de residuales y ejercicios para elegir método.

**Relación con otros archivos del repo**

- [practica-metodos-pronostico-parcial-1.md](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/practica-metodos-pronostico-parcial-1.md): práctica antes del parcial 1 con MA simple, el ejercicio de la p. 30, MA ponderado y SES.
- [promedio-movil-y-suavizacion-exponencial.md](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/promedio-movil-y-suavizacion-exponencial.md): comparación PM(6), PM(12), SE(20 %) y SE(80 %) con MAD, MSE y error % sobre 30 días de ventas reales.
- [README de esta carpeta](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/README.md).
- Tema anterior: [03 — gráficas y autocorrelación](/corte-1-pronosticos/03-graficas-y-autocorrelacion/README.md). Temas siguientes: [05 — tendencia y Holt](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/) y [06 — Winters y tracking signal](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/).
- Aplicación: [proyecto THYMS de pronóstico](/corte-1-pronosticos/proyecto-thyms-pronostico/) (suavización exponencial simple) y [parcial 1](/corte-1-pronosticos/parcial-1/).

## Contenido completo (página por página)

### Página 1 — Operations Management / Introduction to Forecasting

Portada: **Operations Management** — **Introduction to Forecasting**. Universidad de La Sabana.

> [Imagen decorativa: foto del campus (edificio de la biblioteca), escudo de la Universidad de La Sabana y logo de licencia Creative Commons BY-NC-SA]

### Página 2 — Lecture Objective

- To introduce forecasting methods, with their advantages and disadvantages.
- The studied methods correspond to random data without trend or seasonality components

### Página 3 — FORECASTING METHODS

- MOVING AVERAGE
- EXPONENTIAL SMOOTHING

### Página 4 — MOVING AVERAGE

- Simple moving average
  - Demand does not grow or decrease rapidly.
  - Random data with regression to the average.

> [Gráfico: línea «demanda», eje X periodos 1–21, eje Y 0–600. La serie oscila alrededor de ≈ 500 sin tendencia, con mínimos de ≈ 397 (periodo 5) y ≈ 427 (periodo 16) y máximo ≈ 564 (periodo 17). Coincide con los datos del ejemplo de la página 6.]

### Página 5 — SIMPLE MOVING AVERAGE

$$F_t=\frac{A_{t-1}+A_{t-2}+\dots+A_{t-n}}{n}$$

How is ***n*** determined?

(Notación: $F_t$ pronóstico del periodo $t$; $A_{t-i}$ demanda real del periodo $t-i$; $n$ número de periodos promediados.)

### Página 6 — Example

- Perform the forecast for four additional periods considering n = 3 and n = 9 for the following data series:

| period | demand |
|---|---|
| 1 | 482 |
| 2 | 474 |
| 3 | 523 |
| 4 | 485 |
| 5 | 397 |
| 6 | 514 |
| 7 | 504 |
| 8 | 503 |
| 9 | 481 |

| period | demand |
|---|---|
| 10 | 538 |
| 11 | 463 |
| 12 | 540 |
| 13 | 511 |
| 14 | 504 |
| 15 | 537 |
| 16 | 427 |
| 17 | 564 |
| 18 | 484 |
| 19 | 454 |
| 20 | 480 |
| 21 | 541 |

(La diapositiva no muestra la solución.)

### Página 7 — Analysis

- The forecast changes because the average of the most recent n observations is used as a forecast for the next period.
- How can forecasts of several steps forward be obtained? ...
- **Disadvantage 1: Recalculate average given a new observation** (en rojo)

### Página 8 — Analysis

- **Disadvantage 2: Average against trend** (en rojo)

| Period | Demand | MA(3) | MA(6) |
|---|---|---|---|
| 1 | 2 | | |
| 2 | 4 | | |
| 3 | 6 | | |
| 4 | 8 | 4 | |
| 5 | 10 | 6 | |
| 6 | 12 | 8 | |
| 7 | 14 | 10 | 7 |
| 8 | 16 | 12 | 9 |
| 9 | 18 | 14 | 11 |
| 10 | 20 | 16 | 13 |
| 11 | 22 | 18 | 15 |
| 12 | 24 | 20 | 17 |

> [Gráfico: líneas, eje X periodos 1–12, eje Y 0–30. «Demanda» (naranja) recta creciente de 2 a 24; «PM(3)» (gris) paralela por debajo, de 4 (periodo 4) a 20 (periodo 12), siempre 4 unidades por debajo de la demanda; «PM(6)» (amarillo) de 7 (periodo 7) a 17 (periodo 12), siempre 7 unidades por debajo. Muestra que el promedio móvil se queda rezagado frente a una tendencia, y más cuanto mayor es n.]

### Página 9 — Weighted moving average

- The most recent data is more important.
- The weighting should add to 1

$$F_t=w_0A_t+w_1A_{t-1}+w_2A_{t-2}+\dots+w_nA_t$$

(Así aparece en la diapositiva; el último término debería ser $w_nA_{t-n}$. $w_i$ es el peso del dato con $i$ periodos de antigüedad y $\sum w_i=1$.)

### Página 10 — Weighting

- The weights should correspond to the importance of that period in the overall context.
- Example: there were machine failures, special events.
  - Seasonality of the product. Example: summer / winter products.

### Página 11 — Example

- Perform the forecast for four additional periods considering n = 3 and w0 = 0.75, w1 = 0.15, w2 = 0.1 of the following data series:

Mismos datos de la página 6:

| period | demand | period | demand |
|---|---|---|---|
| 1 | 482 | 10 | 538 |
| 2 | 474 | 11 | 463 |
| 3 | 523 | 12 | 540 |
| 4 | 485 | 13 | 511 |
| 5 | 397 | 14 | 504 |
| 6 | 514 | 15 | 537 |
| 7 | 504 | 16 | 427 |
| 8 | 503 | 17 | 564 |
| 9 | 481 | 18 | 484 |
| | | 19 | 454 |
| | | 20 | 480 |
| | | 21 | 541 |

(La diapositiva no muestra la solución.)

### Página 12 — Exponential Smoothing

- Recent data has more information from the past. The current forecast is the weighted average of the last forecast and the current value of demand:

$$\text{New Forecast}=\alpha(\text{Latest data value})+(1-\alpha)(\text{former forecast value})$$

$$F_t=\alpha D_{t-1}+(1-\alpha)F_{t-1}$$

($D_{t-1}$: demanda real del periodo anterior; $F_{t-1}$: pronóstico del periodo anterior; $\alpha$: constante de suavización.)

### Página 13 — Exponential Smoothing

- ✓ $\alpha$ is the smoothing constant. It determines the relative weighting placed on the current demand observation.
- ✓ $(1-\alpha)$ is the weight assigned to the past observations of the demand

| | α = 0.05 |
|---|---|
| Weight of most recent data (α) | 0,05 |
| t-1 : (α(1-α)) | 0,0475 |
| t-2 : (α(1-α)²) | 0,045125 |
| t-3 : (α(1-α)³) | 0,04286875 |

### Página 14 — Advantages of the method

- It's accurate!
- It's easy to use
- The user understands how it works
- Few calculations and parameters

### Página 15 — Exponential Smoothing

$$F_t=F_{t-1}-\alpha(F_{t-1}-D_{t-1})$$

$$F_t=F_{t-1}-\alpha e_{t-1}$$

- Interpretation: The forecast is the previous one minus a certain fraction of error. **positive and negative error?** (en rojo)
- The first forecast can be carried out in the following ways:
  - Simple Moving Average
  - The most recent data
  - Expert opinion

($e_{t-1}=F_{t-1}-D_{t-1}$ es el error del periodo anterior.)

### Página 16 — Example

- Make the forecast for an additional period considering α = 0.05 of the following data series: Use F(1) = 540.

| periodo | demanda | periodo | demanda |
|---|---|---|---|
| 1 | 482 | 10 | 538 |
| 2 | 474 | 11 | 463 |
| 3 | 523 | 12 | 540 |
| 4 | 485 | 13 | 511 |
| 5 | 397 | 14 | 504 |
| 6 | 514 | 15 | 537 |
| 7 | 504 | 16 | 427 |
| 8 | 503 | 17 | 564 |
| 9 | 481 | 18 | 484 |
| | | 19 | 454 |
| | | 20 | 480 |
| | | 21 | 541 |

(La diapositiva no muestra la solución.)

### Página 17 — Choosing Alfa

- Alpha must be a value between 0 and 1.
- If the alpha is small, it is due to a stable demand. Importance to past data.
- If the alpha is close to 1, the forecast may follow more important variations. Greater weighting to the current observation. A lot of variation from period to period
- How to determine the alpha?
  - Choose between two values: 0.2 and 0.8. Review historically
  - Try different values trying to minimize the error.

### Página 18 — Choosing Alfa

- The recommended values are $0.1\le\alpha\le0.3$
  - Try different values trying to minimize the error.

> [Gráfico: líneas, eje X 12 periodos, eje Y de 15 a 35. Tres series: **Demanda** (azul oscuro, rombos): ≈ 20, 18, 21, 25, 24, 27, 22, 30, 23, 20, 29, 22; **Pronóstico (alfa = 0.1)** (rosado, cuadrados), casi plano: ≈ 23,4; 23,1; 22,6; 22,4; 22,7; 22,8; 23,2; 23,1; 23,8; 23,7; 23,3; 23,9; **Pronóstico alfa = 0.5** (verde, triángulos), que sigue más de cerca la demanda con un periodo de retraso: ≈ 23,4; 21,7; 19,8; 20,4; 22,7; 23,3; 25,2; 23,6; 26,8; 24,9; 22,4; 25,7. Valores leídos del gráfico; son coherentes con $F_1\approx23{,}4$ (promedio de las 12 demandas) y la fórmula de la página 12.]

### Página 19 — Forecasts several steps forward

- In moving averages and exponential smoothing it is assumed that the forecast in period t is for demand in period t+1.
- The assumed model is stationary: it does not change with time
- For more steps forward? Ex: Retailer

> [Gráfico: «demanda estacionaria», puntos dispersos alrededor de una línea horizontal constante.]

### Página 20 — Exponential Smoothing vs Moving Averages

- SIMILARITIES
  - The demand is represented by a constant plus a random fluctuation with a mean equal to zero. Adjusting N and ∝: sensitivity to changes
  - Both depend on a single parameter. N small and ∝ large: greater weight to current data = sensitivity to changes in demand = errors with greater variance
  - Lag with trends
- DIFFERENCES :
  - Weighted average of all past data. MA of only the last data periods N. Outliers
  - MA history of all N past data. ES: You only need to save the last forecast:
  - E.g.: Demand for 300,000 inventory items is forecast every 12 months. MA: 300.000 \* 12 pieces of information, SE 300.000 pieces of information.

(En la diapositiva se usa el símbolo ∝ para referirse a α.)

### Página 21 — Errors of the forecast

- Error: Difference between the forecast and the actual value.
- Also called residual
- *There are different types of error.*

### Página 22 — Measurement of errors

- Let T be the number of periods in which a forecast was calculated. Not to be confused with the n-parameter for the MA method.
- Error: $e_t=F_t-D_t$

### Página 23 — Measurement of errors

- Mean absolute deviation (MAD):

$$MAD=\frac{\sum_{i=1}^{n}|A_i-F_i|}{n}$$

- Dispersion of error.
- Magnitud: units of A.

$$DAM=\frac{\sum_{t=1}^{T}|e_t|}{T}$$

### Página 24 — Measurement of errors

- Residual sum of squares

$$SSE=\sum_{i=1}^{n}(A_i-F_i)^2$$

Small deviations (nota al lado de la fórmula)

- Mean square error

$$MSE=\frac{SSE}{n}$$

$$MSE=\frac{\sum E_t^2}{n}$$

### Página 25 — Measurement of errors

- Error porcentual absoluto medio: *Mean absolute percent error* (expressed as %)

$$MAPE=\frac{\sum_{i=1}^{n}|A_i-F_i|/A_i}{n}\times100$$

This measure allows to normalize the errors according to the magnitude of the data.

$$EPAM=100\%\times\frac{\sum_{t=1}^{T}\left|\dfrac{e_t}{D_t}\right|}{T}$$

### Página 26 — Measurement of errors

- Percentage mean error (PME)

$$PME=\frac{\sum_{t=1}^{n}\dfrac{(e_i^2)}{D_t}}{n}$$

(Transcrito tal como aparece en la diapositiva.)

### Página 27 — Whats the best method?

- Indicators are not enough
- Wonder if:
  - Residuals are more or less evenly distributed around zero (0)
  - There are biases or trends
- In a good forecasting method, residuals should be seen as "random" (not discernible pattern) and distributed around zero.

### Página 28 — Expected behavior of forecast residuals

Errors should be 0

DESVIACIÓN ESTÁNDAR DEL ERROR (sE) → 0

> [Gráfico 1 «ERROR Et»: serie de ≈ 60 errores que oscilan alrededor de 0, casi todos entre −20 y +50, con un valor atípico cercano a −65.]

> [Gráfico 2: histograma de los errores con clases centradas en −70, −50, −30, −10, 10, 30 y 50, y curva normal roja superpuesta; la clase más alta es la de 10; hay una barra pequeña aislada en −70.]

> [Gráfico 3: curva normal teórica del error centrada en 0, eje X «ERROR» de −100 a 100.]

| ME | MAD | MAPE | MSE | σE |
|---|---|---|---|---|
| ≈ 0 | 18,2 | ≈ 1% | 506,25 | 22,50 |

### Página 29 — Whats the best method?

- Method 1: MAD = 5.77 ; MSE = 51.69
- Method 2: MAD = 6 ; MSE = 41.8
- So??

> [Gráfico «Errores de Pronóstico», eje X «Tiempo» 1–10, eje Y «Error» de −15 a 15. Serie **et1** (azul): ≈ −2,7; 12,7; 3,2; −0,4; −0,3; −10,2; −9,2; 2,5; 6,1; −10,1 — oscila alrededor de 0. Serie **et2** (rosado): −5; −7; −4; −4; −4; −4; −6; −8; −6; −12 — siempre negativa (sesgo). Valores leídos del gráfico; los de et2 reproducen exactamente MAD = 6 y MSE = 41,8.]

### Página 30 — Exercise

- For the next set of data, and their forecasts, say which method is best.

| Data | MA n = 3 | MA n = 5 |
|---|---|---|
| 13,9 | | |
| 13,4 | | |
| 16,4 | | |
| 14,1 | 14,6 | |
| 8,8 | 14,6 | |
| 15,8 | 13,1 | 13,3 |
| 15,2 | 12,9 | 13,7 |
| 15,2 | 13,3 | 14,1 |
| 13,9 | 15,4 | 13,8 |
| 17,3 | 14,7 | 13,8 |

### Página 31 — THANKS!

- THANKS!


---

<!-- fuente: corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/practica-metodos-pronostico-parcial-1.md -->
# practica-metodos-pronostico-parcial-1

> **Archivo:** [`practica-metodos-pronostico-parcial-1.xlsx`](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/practica-metodos-pronostico-parcial-1.xlsx) · **Corte 1** · Libro de Excel con 6 hoja(s): `MA SIMPLE`, `EJERCICIO DIAPO`, `MA PONDERADO`, `SE SIMPLE`, `SE DOBLE HOLT`, `SE TRIPLE WINTERS`  
> **Nombre original:** `CORTE 1/PARICAL 1.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Libro de práctica preparado antes del primer parcial (nombre original `CORTE 1/PARICAL 1.xlsx`). Repasa en Excel los métodos de la [Lección 5 — Forecasting stationary data and errors](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md): promedio móvil simple con sus medidas de error (MAD, SSE, MSE, MAPE), el ejercicio de la diapositiva 30 (¿MA de 3 o de 5?), promedio móvil ponderado y suavización exponencial simple. Tiene además dos hojas reservadas para Holt y Winters que quedaron **vacías**. Varias hojas tienen errores de fórmula (ver cada hoja y Observaciones).

**Advertencia general:** las demandas de `MA SIMPLE`, `MA PONDERADO` y `SE SIMPLE` se generan con `=RANDBETWEEN(480,600)`, que cambia cada vez que Excel recalcula. Los números de abajo son los que quedaron guardados en el archivo; al abrirlo se verán otros.

### Hoja `MA SIMPLE` — promedio móvil simple con n = 3

**Objetivo (deducido):** pronosticar con un promedio móvil de 3 periodos, calcular el pronóstico del periodo 22 y medir el error, como en el ejemplo de la p. 6 de la L05 pero con datos aleatorios.

**Datos de entrada** (periodos en `B2:B13`, demanda `D()` en `C2:C13`, generada con `RANDBETWEEN(480,600)`):

| Periodo | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Demanda | 504 | 598 | 553 | 531 | 540 | 569 | 587 | 505 | 570 | 583 | 537 | 540 |

**Parámetros:** $n=3$ (`B1` «n=3» y `C15`).

**Método (tal como está en la hoja)**

- `F()` (columna D, filas 5–13): `D5 = AVERAGE(C3:C5)`, … , `D13 = AVERAGE(C11:C13)`; es decir, en la fila del periodo $t$ se pone $\frac{1}{3}(D_{t-2}+D_{t-1}+D_t)$, que incluye la demanda del propio periodo.
- `MAD` (columna E): `=ABS(C5-D5)` → $|D_t-F|$; `SSE` (columna F): `=E5^2`; `MAPE` (columna G): `=E5/C5` → $|e|/D_t$.
- `F22` (`C16`): `=AVERAGE(C11:C13)` $=\frac{583+537+540}{3}=553{,}333$ (promedio de los periodos 19, 20 y 21).
- Resumen: MAD `E18 = AVERAGE(E5:E13)`; SSE `E19 = SUM(F5:F13)`; MSE `E20 = AVERAGE(F5:F13)`; MAPE `E21 = AVERAGE(G5:G13)`.

**Resultados guardados**

| Periodo | D() | F() | Error abs. | Error² | Error % |
|---|---|---|---|---|---|
| 13 | 531 | 560,667 | 29,667 | 880,111 | 5,59 % |
| 14 | 540 | 541,333 | 1,333 | 1,778 | 0,25 % |
| 15 | 569 | 546,667 | 22,333 | 498,778 | 3,93 % |
| 16 | 587 | 565,333 | 21,667 | 469,444 | 3,69 % |
| 17 | 505 | 553,667 | 48,667 | 2.368,44 | 9,64 % |
| 18 | 570 | 554,000 | 16,000 | 256,000 | 2,81 % |
| 19 | 583 | 552,667 | 30,333 | 920,111 | 5,20 % |
| 20 | 537 | 563,333 | 26,333 | 693,444 | 4,90 % |
| 21 | 540 | 553,333 | 13,333 | 177,778 | 2,47 % |

| F22 | MAD | SSE | MSE | MAPE |
|---|---|---|---|---|
| 553,333 | 23,2963 | 6.265,89 | 696,21 | 0,0427443 (4,27 %) |

**Error de alineación:** cada valor de `F()` está una fila más arriba de donde debería; el número de la fila del periodo $t$ es en realidad el pronóstico del periodo $t+1$ (por ejemplo, 560,667 es $F_{14}=\frac{598+553+531}{3}$, no $F_{13}$). Al compararlo con $D_t$, la demanda que se quiere pronosticar entra en su propio pronóstico y el error sale menor. Con la alineación correcta, $F_t=\frac{D_{t-1}+D_{t-2}+D_{t-3}}{3}$ (cálculo propio con los mismos datos):

| Periodo | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |
|---|---|---|---|---|---|---|---|---|---|---|
| $F_t$ correcto | 551,67 | 560,67 | 541,33 | 546,67 | 565,33 | 553,67 | 554,00 | 552,67 | 563,33 | 553,33 |

MAD = 28,22; SSE = 8.784,22; MSE = 976,02; MAPE = 5,16 %. El pronóstico $F_{22}=553{,}33$ de la hoja sí es correcto.

### Hoja `EJERCICIO DIAPO` — ejercicio de la diapositiva 30

**Enunciado** (imagen pegada en la hoja, igual a la p. 30 de la L05): «Exercise — For the next set of data, and their forecasts, say which method is best.»

> [Imagen: captura de la diapositiva «Exercise» con la tabla Data / MA n = 3 / MA n = 5 que se transcribe abajo.]

**Datos y método:** demandas en `B3:B12` (y repetidas en `B15:B24`); pronósticos copiados de la diapositiva como valores (`C6:C12` para MA n = 3 y `C20:C24` para MA n = 5). Error absoluto `D = ABS(B−C)`, error al cuadrado `E = D^2`, error relativo `F = D/B`. Resumen: MAD = promedio de D; SSE = suma de E; MSE = promedio de E; MAPE = promedio de F.

| Dato | MA n = 3 | Error abs. | Error² | Error % | MA n = 5 | Error abs. | Error² | Error % |
|---|---|---|---|---|---|---|---|---|
| 13,9 | | | | | | | | |
| 13,4 | | | | | | | | |
| 16,4 | | | | | | | | |
| 14,1 | 14,6 | 0,5 | 0,25 | 3,55 % | | | | |
| 8,8 | 14,6 | 5,8 | 33,64 | 65,91 % | | | | |
| 15,8 | 13,1 | 2,7 | 7,29 | 17,09 % | 13,3 | 2,5 | 6,25 | 15,82 % |
| 15,2 | 12,9 | 2,3 | 5,29 | 15,13 % | 13,7 | 1,5 | 2,25 | 9,87 % |
| 15,2 | 13,3 | 1,9 | 3,61 | 12,50 % | 14,1 | 1,1 | 1,21 | 7,24 % |
| 13,9 | 15,4 | 1,5 | 2,25 | 10,79 % | 13,8 | 0,1 | 0,01 | 0,72 % |
| 17,3 | 14,7 | 2,6 | 6,76 | 15,03 % | 13,8 | 3,5 | 12,25 | 20,23 % |

| Medida | MA n = 3 (`I3:I6`) | MA n = 5 (`I15:I18`) |
|---|---|---|
| MAD | 2,47143 | **1,74** |
| SSE | 59,09 | **21,97** |
| MSE | 8,44143 | **4,394** |
| MAPE | 0,199994 (20,0 %) | **0,107757 (10,8 %)** |

**Conclusión:** el promedio móvil de 5 periodos es mejor en las cuatro medidas. Comprobación propia: si se compara solo en los 5 periodos que ambos pronostican (sin el atípico 8,8), MA n = 3 da MAD 2,2, SSE 25,2, MSE 5,04 y MAPE 14,1 %, y MA n = 5 sigue siendo mejor.

### Hoja `MA PONDERADO` — promedio móvil ponderado

**Objetivo (deducido):** pronosticar el periodo 22 con $n=3$ y pesos $w_0=0{,}75$, $w_1=0{,}15$, $w_2=0{,}1$, como en el ejemplo de la p. 11 de la L05.

**Datos de entrada** (`C2:C13`, `RANDBETWEEN(480,600)`):

| Periodo | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Demanda | 545 | 585 | 506 | 533 | 544 | 529 | 487 | 501 | 529 | 590 | 522 | 525 |

**Parámetros:** `W0` = 0,75 (`C16`), `W2` = 0,15 (`C17`), `W3` = 0,1 (`C18`), `n=` 3 (`C20`).

**Método:** `F22` (`C21`) `=(((C13*C16)+(C17*C12)+(C18*C11))/C20)`, es decir
$$F_{22}=\frac{w_0D_{21}+w_1D_{20}+w_2D_{19}}{n}=\frac{0{,}75(525)+0{,}15(522)+0{,}1(590)}{3}=\frac{531{,}05}{3}=177{,}017.$$

**Resultado guardado:** F22 = 177,017.

**Error:** como los pesos ya suman 1, no se debe dividir entre $n$. El pronóstico correcto es $F_{22}=531{,}05$. Además, los rótulos `W2` y `W3` corresponden a $w_1$ y $w_2$, y la hoja solo calcula un pronóstico (no hay errores ni serie de pronósticos).

### Hoja `SE SIMPLE` — suavización exponencial simple

**Objetivo (deducido):** aplicar la suavización exponencial simple con pronóstico inicial 540, como en el ejemplo de la p. 16 de la L05.

**Datos de entrada** (`C2:C13`, `RANDBETWEEN(480,600)`):

| Periodo | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Demanda | 533 | 545 | 537 | 514 | 552 | 592 | 524 | 492 | 550 | 549 | 480 | 537 |

**Parámetros:** pronóstico inicial 540 (`D1`); `ALFA` = 0,95 (`C17`); `ALFA-1` = `=1-C17` = 0,05 (`C18`), que es $1-\alpha$.

**Método:** `F10` (`C19`) `=(C17*C2)+(C18*D1)`, es decir
$$F=\alpha D_{10}+(1-\alpha)F_{10}=0{,}95(533)+0{,}05(540)=533{,}35.$$

**Resultado guardado:** 533,35 (rotulado «F10»).

**Observaciones de la hoja:** solo se calcula un paso (falta continuar hasta $F_{22}$); con la convención de la L05 ($F_t=\alpha D_{t-1}+(1-\alpha)F_{t-1}$) el valor calculado es el pronóstico del periodo 11, no el del 10; y el ejemplo de la diapositiva usa $\alpha=0{,}05$, mientras que aquí el peso 0,95 se aplica al dato (α efectivo = 0,95), es decir, los pesos están invertidos respecto al ejemplo.

### Hojas `SE DOBLE HOLT` y `SE TRIPLE WINTERS`

Vacías. Estaban reservadas para la suavización doble de Holt (tema [05](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/)) y el método de Winters (tema [06](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/)).

### Observaciones

- Datos aleatorios (`RANDBETWEEN`) en tres hojas: los valores cambian al recalcular; no son los datos de las diapositivas (482, 474, 523, …).
- `MA SIMPLE`: pronósticos desalineados una fila (el error sale subestimado: MAD 23,30 en vez de 28,22).
- `MA PONDERADO`: división entre $n$ sobrante (177,017 en vez de 531,05) y rótulos de pesos `W0`, `W2`, `W3`.
- `SE SIMPLE`: un solo paso, rótulo «F10» y α = 0,95 en lugar de 0,05.
- `EJERCICIO DIAPO`: `I16 = SUM(E19:E24)` incluye la celda vacía `E19`, sin efecto. El último pronóstico MA n = 3 de la diapositiva (14,7) es en rigor 14,77 ≈ 14,8.
- Las hojas de Holt y Winters están vacías.
- Por su contenido (MA, WMA y SES), el archivo encaja en esta carpeta; las hojas vacías de Holt y Winters pertenecen a los temas 05 y 06.


---

<!-- fuente: corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/promedio-movil-y-suavizacion-exponencial.md -->
# promedio-movil-y-suavizacion-exponencial

> **Archivo:** [`promedio-movil-y-suavizacion-exponencial.xlsx`](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/promedio-movil-y-suavizacion-exponencial.xlsx) · **Corte 1** · Libro de Excel con 16 hoja(s): `Ventas propias (2)`, `Ventas propias`, `Hoja1`, `Coeficientes ventas propias`, `Serie de tiempo  ventas propias`, `Histograma Ventas Propias`, `Autocorrelograma ventas propias`, `Boxplot Ventas Propias`, `Scatterplot Ventas Propias`, `Ventas competencia`, `Coeficientes ventas competencia`, `Serie de tiempo Ventas Comp`, `Histograma Ventas Competencia`, `Autocorrelograma Ventas Compete`, `Boxplot Ventas Competencia`, `Scatterplot Ventas Competencia`  
> **Nombre original:** `CORTE 1/PROMEDIO MOVIL Y SUAVIZACION EXPO.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Libro de clase (nombre original «PROMEDIO MOVIL Y SUAVIZACION EXPO») que toma la serie diaria de **ventas propias** de la tarea [tarea-class-example-1](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-1.md) y, en la hoja nueva `Ventas propias (2)`, compara cuatro métodos de la [Lección 5 — Forecasting stationary data and errors](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md): **promedio móvil de 6 y de 12 días**, y **suavización exponencial simple con α = 0,2 y α = 0,8**, midiendo su error con **MAD**, **MSE** y **error porcentual** sobre los 30 últimos días de la hoja. Se aprende a programar estos métodos en Excel y a elegir entre ellos con las medidas de error.

El libro tiene 16 hojas, pero solo `Ventas propias (2)` es propia de este archivo:

| Hojas | Contenido |
|---|---|
| `Ventas propias (2)` | Comparación PM(6), PM(12), SE(20 %), SE(80 %) con MAD, MSE y error %. **Es lo nuevo y lo propio del tema 04.** |
| `Hoja1` | Vacía. |
| `Ventas propias`, `Coeficientes ventas propias`, `Ventas competencia`, `Coeficientes ventas competencia` y las 10 hojas de gráficos (serie de tiempo, histograma, autocorrelograma, boxplot y dispersión de cada serie) | Copia exacta, celda por celda, de las hojas del mismo nombre de [tarea-class-example-1](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-1.md) (rezagos 1–20, coeficientes de autocorrelación con límites de significancia y gráficos de la L04). Su explicación completa está en ese archivo. |

### Hoja `Ventas propias (2)`

**Objetivo (deducido):** pronosticar las ventas diarias con cuatro métodos para datos estacionarios y decidir cuál tiene menor error en un periodo de prueba de 30 días.

**Datos de entrada**

- Columna A `Fecha` y columna B `Ventas propias`: la misma serie de [tarea-class-example-1](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-1.md) (1.923 días, del 2019-08-30 en la fila 2 al 2014-05-26 en la fila 1927, en orden **descendente**). Se insertaron tres filas vacías (1894–1896) para poner los encabezados; quitándolas, la columna B es idéntica a la de la hoja `Ventas propias`.
- Estadísticos de la serie completa: media 1.954,15; mediana 1.943; mínimo 9; máximo 31.624 (ver atípicos en el ejemplo 1). Media de los 30 días de prueba (filas 1898–1927): 1.983,47.
- CSV completo, incluidos los pronósticos y errores: [`Ventas_propias_2.csv`](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/promedio-movil-y-suavizacion-exponencial-datos/Ventas_propias_2.csv).

**Parámetros**

| Método | Parámetro | Dónde |
|---|---|---|
| PM(6) | $n=6$ | rango de 6 celdas en la fórmula de la columna C |
| PM(12) | $n=12$ | rango de 12 celdas en la columna D |
| SE(20%) | $\alpha=0{,}2$ | escrito dentro de la fórmula de la columna E |
| SE(80%) | $\alpha=0{,}8$ | escrito dentro de la fórmula de la columna F |
| Valores iniciales de SE | $F^{(0,2)}=1.957{,}55852$ y $F^{(0,8)}=1.904{,}30691$ | `E1893`, `F1893` (valores escritos, sin fórmula) |

Los valores iniciales coinciden (comprobación propia) con aplicar la suavización exponencial desde la fila 2 hasta la 1892 con cada α; es decir, se calcularon antes sobre toda la serie y se pegaron como valores.

**Método paso a paso.** La hoja trata el orden de las filas como orden del tiempo: «periodo anterior» = fila de arriba. La venta real de la fila $r$ es $D_r$ (columna B).

1. **Suavización exponencial simple** (columnas E y F, filas 1897–1927). Fórmulas `=0.2*B1897+0.8*E1897` y `=0.8*B1897+0.2*F1897` (la fila 1897 toma la 1893 porque salta las filas vacías):
   $$F_r=\alpha D_{r-1}+(1-\alpha)F_{r-1},\qquad \alpha=0{,}2\ \text{o}\ 0{,}8.$$
   Cada pronóstico usa la venta real del periodo anterior: es un pronóstico **a un paso**, actualizado cada día.
2. **Promedio móvil de 6** (columna C, filas 1898–1927).
   - Primer pronóstico: `C1898 = AVERAGE(B1889:B1897)`; el rango incluye las 3 filas vacías, que `AVERAGE` ignora, así que promedia las 6 ventas reales de las filas 1889–1893 y 1897.
   - Siguientes: `C1899 = AVERAGE(C1898, B1890:B1897)`, `C1900 = AVERAGE(C1898:C1899, B1891:B1897)`, … , `C1904 = AVERAGE(C1898:C1903)` y desde ahí `C(r) = AVERAGE(C(r-6):C(r-1))`. Es decir, cada día se reemplaza la venta real más antigua por el **pronóstico** anterior, no por la venta real:
   $$F_r=\frac{1}{6}\sum_{i=1}^{6}\tilde D_{r-i},\qquad \tilde D_{j}=\begin{cases}D_j & j\le1897\\ F_j & j\ge1898\end{cases}$$
   Desde la fila 1904 ya no entra ninguna venta real: es un pronóstico de **varios pasos adelante** sin actualizar, que converge a ≈ 1.979,5.
3. **Promedio móvil de 12** (columna D): igual, con `D1898 = AVERAGE(B1883:B1897)` (12 ventas reales) y `D1899 = AVERAGE(D1898, B1884:B1897)`, … , `D1909 = AVERAGE(D1898:D1908, B1897)`, `D1910 = AVERAGE(D1898:D1909)`; converge a ≈ 1.970,1.
4. **Error absoluto** (bloque `MAD`, filas 1932–1961, columnas C–F): `=ABS(B1898-C1898)`, … , es decir $|e_r|=|D_r-F_r|$ para los 30 días de prueba (filas 1898–1927).
5. **Error porcentual** (bloque `ERROR %`, columnas J–M): `=C1932/B1898`, … , es decir $|e_r|/D_r$.
6. **Resumen** (filas 1963–1964):
   - `MAD` (`C1963`) `=AVERAGE(C1932:C1959:C1960:C1961)`, equivalente a $\dfrac{1}{30}\sum|e_r|$.
   - `MSE` (`C1964`) `=SUMSQ(C1932:C1961)/30`, es decir $\dfrac{1}{30}\sum e_r^2$.

**Resultados — pronósticos y errores absolutos de los 30 días de prueba** (redondeados a un decimal; valores exactos en el CSV)

| Fila | Fecha | Venta real | PM(6) | PM(12) | SE(20%) | SE(80%) | Error abs. PM(6) | Error abs. PM(12) | Error abs. SE(20%) | Error abs. SE(80%) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1893 | 2014-06-26 | 1.973 |  |  | 1.957,6 | 1.904,3 |  |  |  |  |
| 1897 | 2014-06-25 | 1.998 |  |  | 1.960,6 | 1.959,3 |  |  |  |  |
| 1898 | 2014-06-24 | 2.361 | 1.952,2 | 1.915,3 | 1.968,1 | 1.990,3 | 408,8 | 445,7 | 392,9 | 370,7 |
| 1899 | 2014-06-23 | 1.784 | 1.996,2 | 1.941,4 | 2.046,7 | 2.286,9 | 212,2 | 157,4 | 262,7 | 502,9 |
| 1900 | 2014-06-22 | 1.622 | 2.001,1 | 1.970,6 | 1.994,2 | 1.884,6 | 379,1 | 348,6 | 372,2 | 262,6 |
| 1901 | 2014-06-21 | 1.707 | 1.958,9 | 1.994,2 | 1.919,7 | 1.674,5 | 251,9 | 287,2 | 212,7 | 32,5 |
| 1902 | 2014-06-20 | 1.551 | 1.979,9 | 1.973,6 | 1.877,2 | 1.700,5 | 428,9 | 422,6 | 326,2 | 149,5 |
| 1903 | 2014-06-19 | 1.896 | 1.981,0 | 1.981,3 | 1.811,9 | 1.580,9 | 85,0 | 85,3 | 84,1 | 315,1 |
| 1904 | 2014-06-18 | 1.757 | 1.978,2 | 1.957,5 | 1.828,8 | 1.833,0 | 221,2 | 200,5 | 71,8 | 76,0 |
| 1905 | 2014-06-17 | 1.734 | 1.982,5 | 1.979,9 | 1.814,4 | 1.772,2 | 248,5 | 245,9 | 80,4 | 38,2 |
| 1906 | 2014-06-16 | 2.111 | 1.980,3 | 1.981,0 | 1.798,3 | 1.741,6 | 130,7 | 130,0 | 312,7 | 369,4 |
| 1907 | 2014-06-15 | 2.200 | 1.976,8 | 1.958,2 | 1.860,9 | 2.037,1 | 223,2 | 241,8 | 339,1 | 162,9 |
| 1908 | 2014-06-14 | 2.133 | 1.979,8 | 1.968,7 | 1.928,7 | 2.167,4 | 153,2 | 164,3 | 204,3 | 34,4 |
| 1909 | 2014-06-13 | 2.374 | 1.979,8 | 1.968,3 | 1.969,5 | 2.139,9 | 394,2 | 405,7 | 404,5 | 234,1 |
| 1910 | 2014-06-12 | 1.905 | 1.979,6 | 1.965,8 | 2.050,4 | 2.327,2 | 74,6 | 60,8 | 145,4 | 422,2 |
| 1911 | 2014-06-11 | 2.334 | 1.979,8 | 1.970,0 | 2.021,4 | 1.989,4 | 354,2 | 364,0 | 312,6 | 344,6 |
| 1912 | 2014-06-10 | 2.333 | 1.979,3 | 1.972,4 | 2.083,9 | 2.265,1 | 353,7 | 360,6 | 249,1 | 67,9 |
| 1913 | 2014-06-09 | 2.135 | 1.979,2 | 1.972,6 | 2.133,7 | 2.319,4 | 155,8 | 162,4 | 1,3 | 184,4 |
| 1914 | 2014-06-08 | 1.836 | 1.979,6 | 1.970,8 | 2.134,0 | 2.171,9 | 143,6 | 134,8 | 298,0 | 335,9 |
| 1915 | 2014-06-07 | 2.040 | 1.979,5 | 1.970,5 | 2.074,4 | 1.903,2 | 60,5 | 69,5 | 34,4 | 136,8 |
| 1916 | 2014-06-06 | 1.957 | 1.979,5 | 1.969,6 | 2.067,5 | 2.012,6 | 22,5 | 12,6 | 110,5 | 55,6 |
| 1917 | 2014-06-05 | 2.257 | 1.979,5 | 1.970,7 | 2.045,4 | 1.968,1 | 277,5 | 286,3 | 211,6 | 288,9 |
| 1918 | 2014-06-04 | 1.644 | 1.979,4 | 1.969,9 | 2.087,7 | 2.199,2 | 335,4 | 325,9 | 443,7 | 555,2 |
| 1919 | 2014-06-03 | 2.320 | 1.979,5 | 1.969,0 | 1.999,0 | 1.755,0 | 340,5 | 351,0 | 321,0 | 565,0 |
| 1920 | 2014-06-02 | 2.238 | 1.979,5 | 1.969,9 | 2.063,2 | 2.207,0 | 258,5 | 268,1 | 174,8 | 31,0 |
| 1921 | 2014-06-01 | 2.264 | 1.979,5 | 1.970,0 | 2.098,1 | 2.231,8 | 284,5 | 294,0 | 165,9 | 32,2 |
| 1922 | 2014-05-31 | 1.684 | 1.979,5 | 1.970,1 | 2.131,3 | 2.257,6 | 295,5 | 286,1 | 447,3 | 573,6 |
| 1923 | 2014-05-30 | 2.097 | 1.979,5 | 1.970,5 | 2.041,9 | 1.798,7 | 117,5 | 126,5 | 55,1 | 298,3 |
| 1924 | 2014-05-29 | 2.068 | 1.979,5 | 1.970,5 | 2.052,9 | 2.037,3 | 88,5 | 97,5 | 15,1 | 30,7 |
| 1925 | 2014-05-28 | 1.881 | 1.979,5 | 1.970,3 | 2.055,9 | 2.061,9 | 98,5 | 89,3 | 174,9 | 180,9 |
| 1926 | 2014-05-27 | 1.552 | 1.979,5 | 1.970,1 | 2.020,9 | 1.917,2 | 427,5 | 418,1 | 468,9 | 365,2 |
| 1927 | 2014-05-26 | 1.729 | 1.979,5 | 1.970,1 | 1.927,1 | 1.625,0 | 250,5 | 241,1 | 198,1 | 104,0 |

**Resultados — medidas de error**

| Medida | PM(6) | PM(12) | SE(20%) | SE(80%) |
|---|---|---|---|---|
| MAD (fila 1963) | 235,876 | 236,125 | **229,711** | 237,346 |
| MSE (fila 1964) | **69.651,52** | 70.490,14 | 70.977,45 | 86.233,33 |
| Error % promedio (MAPE, cálculo propio con J–M; la hoja no lo resume) | 12,21 % | 12,15 % | **11,98 %** | 12,34 % |

**Gráficos:** esta hoja no tiene gráficos.

**Conclusión**

- **SE(20 %)** tiene el menor MAD (229,7) y el menor MAPE (11,98 %); **PM(6)** tiene el menor MSE (69.651,5). **SE(80 %)** es el peor en las tres medidas: con α alto el pronóstico persigue el ruido diario (sus errores van de 30,7 a 573,6), tal como advierte la L05 (p. 17–18: para demanda estable conviene α pequeño, entre 0,1 y 0,3).
- Las diferencias entre PM(6), PM(12) y SE(20 %) son pequeñas porque la serie es aleatoria alrededor de ≈ 1.950 (ver el correlograma en [tarea-class-example-1](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-1.md)): cualquier método que se acerque a la media funciona parecido.
- Los promedios móviles se vuelven constantes (≈ 1.979,5 y ≈ 1.970,1) porque se alimentan de sus propios pronósticos; la suavización sí se actualiza con las ventas reales.

### Observaciones

- **Comparación desigual:** las columnas de suavización usan la venta real anterior (pronóstico a un paso), mientras que los promedios móviles, desde la segunda fila, reemplazan las ventas reales por pronósticos (pronóstico a varios pasos). Para una comparación justa los promedios móviles deberían ser `=AVERAGE(B(r-6):B(r-1))` con datos reales.
- **Tiempo invertido:** como las fechas están en orden descendente y la hoja toma la fila de arriba como «periodo anterior», en realidad se pronostica cada día con los días *posteriores* del calendario (el periodo de prueba es mayo–junio de 2014, el inicio de la serie). Con una serie estacionaria no cambia el ejercicio, pero no es un pronóstico hacia el futuro.
- `E1932` usa `$B$1898` con referencia absoluta; como es la primera fila, el resultado es correcto.
- La fórmula de MAD `AVERAGE(C1932:C1959:C1960:C1961)` usa una cadena de rangos poco habitual; Excel la interpreta como `C1932:C1961` (30 celdas).
- La hoja no calcula el promedio del error % (MAPE); se calculó aparte arriba.
- Los nombres definidos `DATOS` y `DATOS1` locales a esta hoja (`A22:X1927`, `B22:X1927`) son restos de copiar la hoja `Ventas propias`; no se usan.
- `Hoja1` está vacía.
- **Ubicación:** aunque 14 de sus 16 hojas duplican [tarea-class-example-1](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-1.md) (tema 03), el contenido propio del archivo —promedios móviles, suavización exponencial y medidas de error— corresponde al tema 04, así que su ubicación en esta carpeta es correcta.
