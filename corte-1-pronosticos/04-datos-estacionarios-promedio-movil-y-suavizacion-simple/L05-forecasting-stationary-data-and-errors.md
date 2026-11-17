# L05-forecasting-stationary-data-and-errors

> **Archivo:** [`L05-forecasting-stationary-data-and-errors.pdf`](./L05-forecasting-stationary-data-and-errors.pdf) · **Corte 1** · 31 páginas  
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
| Ejercicio MA $n=3$ frente a $n=5$ | 30 | Resuelto en [practica-metodos-pronostico-parcial-1.md](./practica-metodos-pronostico-parcial-1.md) (hoja `EJERCICIO DIAPO`): MA(3) MAD 2,47, MSE 8,44, MAPE 20,0 %; MA(5) MAD 1,74, MSE 4,39, MAPE 10,8 % → MA(5) es mejor. |

**Páginas clave**

- p. 2–4: objetivo y alcance (datos estacionarios).
- p. 5–8: promedio móvil simple, ejemplo y desventajas.
- p. 9–11: promedio móvil ponderado y ejemplo.
- p. 12–18: suavización exponencial simple, interpretación, ejemplo y elección de α.
- p. 19–20: pronóstico de varios pasos y comparación SES frente a MA.
- p. 21–26: definiciones de error y medidas MAD, SSE, MSE, MAPE y PME.
- p. 27–30: análisis de residuales y ejercicios para elegir método.

**Relación con otros archivos del repo**

- [practica-metodos-pronostico-parcial-1.md](./practica-metodos-pronostico-parcial-1.md): práctica antes del parcial 1 con MA simple, el ejercicio de la p. 30, MA ponderado y SES.
- [promedio-movil-y-suavizacion-exponencial.md](./promedio-movil-y-suavizacion-exponencial.md): comparación PM(6), PM(12), SE(20 %) y SE(80 %) con MAD, MSE y error % sobre 30 días de ventas reales.
- [README de esta carpeta](./README.md).
- Tema anterior: [03 — gráficas y autocorrelación](../03-graficas-y-autocorrelacion/README.md). Temas siguientes: [05 — tendencia y Holt](../05-tendencia-suavizacion-doble-holt/) y [06 — Winters y tracking signal](../06-estacionalidad-winters-y-tracking-signal/).
- Aplicación: [proyecto THYMS de pronóstico](../proyecto-thyms-pronostico/) (suavización exponencial simple) y [parcial 1](../parcial-1/).

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

## Anexo: texto extraído automáticamente del PDF

> Texto plano tal como sale del PDF, sin fórmulas ni tablas que estén como imagen. La versión fiel y completa es la sección «Contenido completo» de arriba.

### Página 1 · 2 imagen(es)

Operations Management
Introduction to Forecasting

### Página 2 · 1 imagen(es)

Lecture Objective
• To introduce forecasting methods, with 
their advantages and disadvantages. 
• The studied methods correspond to 
random data without trend or seasonality 
components

### Página 3 · 1 imagen(es)

FORECASTING METHODS
• MOVING AVERAGE
• EXPONENTIAL SMOOTHING

### Página 4 · 2 imagen(es)

MOVING AVERAGE
• Simple moving average
– Demand does not grow or decrease rapidly.
– Random data with regression to the average.

### Página 5 · 1 imagen(es)

SIMPLE MOVING AVERAGE
𝐹𝑡= 𝐴𝑡−1 + 𝐴𝑡−2 + … + 𝐴𝑡−𝑛
𝑛
How is n determined?

### Página 6 · 1 imagen(es)

• Perform the forecast for four additional periods 
considering n = 3 and n = 9 for the following 
data series: 
Example
period
demand
1
482
2
474
3
523
4
485
5
397
6
514
7
504
8
503
9
481
period
demand
10
538
11
463
12
540
13
511
14
504
15
537
16
427
17
564
18
484
19
454
20
480
21
541

### Página 7 · 1 imagen(es)

• The forecast changes because the 
average of the most recent n observations 
is used as a forecast for the next period.
• How can forecasts of several steps 
forward be obtained? ... 
• Disadvantage 1: Recalculate average 
given a new observation 
Analysis

### Página 8 · 2 imagen(es)

• Disadvantage 2: Average against trend 
Analysis
Period
Demand
MA(3)
MA(6)
1
2
2
4
3
6
4
8
4
5
10
6
6
12
8
7
14
10
7
8
16
12
9
9
18
14
11
10
20
16
13
11
22
18
15
12
24
20
17

### Página 9 · 1 imagen(es)

Weighted moving average
• The most recent data is more important.
• The weighting should add to 1
𝐹𝑡= 𝑤0𝐴𝑡+ 𝑤1𝐴𝑡−1 + 𝑤2𝐴𝑡−2 + ⋯+ 𝑤𝑛𝐴𝑡

### Página 10 · 1 imagen(es)

• The weights should correspond to the 
importance of that period in the overall 
context.
• Example: there were machine failures, 
special events.
– Seasonality of the product. Example: summer 
/ winter products.
Weighting

### Página 11 · 1 imagen(es)

• Perform the forecast for four additional periods 
considering n = 3 and w0 = 0.75, w1 = 0.15, w2 = 0.1 
of the following data series:
Example
period
demand
1
482
2
474
3
523
4
485
5
397
6
514
7
504
8
503
9
481
period
demand
10
538
11
463
12
540
13
511
14
504
15
537
16
427
17
564
18
484
19
454
20
480
21
541

### Página 12 · 1 imagen(es)

Exponential Smoothing
• Recent data has more information from 
the past. The current forecast is the 
weighted average of the last forecast and 
the current value of demand:
𝑁𝑒𝑤 𝐹𝑜𝑟𝑒𝑐𝑎𝑠𝑡
= 𝛼𝐿𝑎𝑡𝑒𝑠𝑡 𝑑𝑎𝑡𝑎 𝑣𝑎𝑙𝑢𝑒+ (1 −𝛼)(𝑓𝑜𝑟𝑚𝑒𝑟 𝑓𝑜𝑟𝑒𝑐𝑎𝑠𝑡 𝑣𝑎𝑙𝑢𝑒)
𝐹𝑡= 𝛼𝐷𝑡−1 + (1 −𝛼)𝐹𝑡−1

### Página 13 · 1 imagen(es)

Exponential Smoothing
✓𝛼 is the smoothing constant. It determines the 
relative weighting placed on the current demand 
observation. 
✓(1 −𝛼) is the weight assigned to the past 
observations of the demand
α = 0.05
Weight of most recent data (α)
0,05
t-1 : (α(1-α))
0,0475
t-2 : (α(1-α)2)
0,045125
t-3 : (α(1-α)3)
0,04286875

### Página 14 · 1 imagen(es)

Advantages of the method
• It's accurate!
• It's easy to use
• The user understands how it works
• Few calculations and parameters

### Página 15 · 1 imagen(es)

𝐹𝑡= 𝐹𝑡−1 −𝛼(𝐹𝑡−1 −𝐷𝑡−1)
𝐹𝑡= 𝐹𝑡−1 −𝛼𝑒𝑡−1
• Interpretation: The forecast is the previous one 
minus a certain fraction of error. positive and 
negative error?
• The first forecast can be carried out in the 
following ways:
– Simple Moving Average
– The most recent data
– Expert opinion
Exponential Smoothing

### Página 16 · 1 imagen(es)

• Make the forecast for an additional period 
considering α = 0.05 of the following data series: Use 
F(1) = 540.
Example
periodo
demanda
1
482
2
474
3
523
4
485
5
397
6
514
7
504
8
503
9
481
periodo
demanda
10
538
11
463
12
540
13
511
14
504
15
537
16
427
17
564
18
484
19
454
20
480
21
541

### Página 17 · 1 imagen(es)

Choosing Alfa
• Alpha must be a value between 0 and 1.
• If the alpha is small, it is due to a stable demand. 
Importance to past data.
• If the alpha is close to 1, the forecast may follow more 
important variations. Greater weighting to the current 
observation. A lot of variation from period to period
• How to determine the alpha?
– Choose between two values: 0.2 and 0.8. Review historically
– Try different values trying to minimize the error.

### Página 18 · 1 imagen(es)

Choosing Alfa
• The recommended values are 0.1 ≤  ≤ 0.3
– Try different values trying to minimize the error.
15
20
25
30
35
0
2
4
6
8
10
12
14
Demanda
Pronóstico (alfa = 0.1)
Pronóstico alfa = 0.5

### Página 19 · 2 imagen(es)

Forecasts several steps forward
– In
moving
averages
and
exponential
smoothing it is assumed that the forecast in
period t is for demand in period t+1.
– The assumed model is stationary: it does not
change with time
– For more steps forward? Ex: Retailer

### Página 20 · 1 imagen(es)

Exponential Smoothing vs Moving 
Averages 
• SIMILARITIES
o
The demand is represented by a constant plus a random fluctuation with a mean 
equal to zero. Adjusting N and ∝: sensitivity to changes
o
Both depend on a single parameter. N small and ∝large: greater weight to 
current data = sensitivity to changes in demand = errors with greater variance
o
Lag with trends
•
DIFFERENCES :
o
Weighted average of all past data. MA of only the last data periods N. Outliers
o
MA history of all N past data. ES: You only need to save the last forecast:
o
E.g.: Demand for 300,000 inventory items is forecast every 12 months. MA: 
300.000 * 12 pieces of information, SE 300.000 pieces of information.

### Página 21 · 1 imagen(es)

• Error: Difference between the forecast and the actual 
value. 
• Also called residual
• There are different types of error. 
Errors of the forecast

### Página 22 · 1 imagen(es)

• Let T be the number of periods in which a forecast 
was calculated. Not to be confused with the n-
parameter for the MA method. 
• Error: et =Ft -Dt 
Measurement of errors

### Página 23 · 2 imagen(es)

Measurement of errors
• Mean absolute deviation (MAD):
𝑀𝐴𝐷= σ𝑖=1
𝑛
𝐴𝑖−𝐹𝑖
𝑛
• Dispersion of error.
• Magnitud: units of A.

### Página 24 · 2 imagen(es)

• Residual sum of squares
𝑆𝑆𝐸= ෍
𝑖=1
𝑛
𝐴𝑖−𝐹𝑖2
• Mean square error
𝑀𝑆𝐸= 𝑆𝑆𝐸
𝑛
Measurement of errors
Small deviations

### Página 25 · 2 imagen(es)

• Error porcentual absoluto medio: Mean absolute 
percent error (expressed as %)
𝑀𝐴𝑃𝐸= σ𝑖=1
𝑛
𝐴𝑖−𝐹𝑖/𝐴𝑖
𝑛
 × 100
This measure allows to normalize the errors according to the 
magnitude of the data.
Measurement of errors

### Página 26 · 1 imagen(es)

▪
Percentage mean error (PME)
Measurement of errors
( )
n
D
e
PME
n
t
t
i

=
=
1
2

### Página 27 · 1 imagen(es)

• Indicators are not enough 
• Wonder if: 
– Residuals are more or less evenly distributed
around zero (0) 
– There are biases or trends
• In a good forecasting method, residuals should be 
seen as "random" (not discernible pattern) and 
distributed around zero. 
Whats the best method?

### Página 28 · 2 imagen(es)

Expected behavior of forecast residuals
Errors should be 0

### Página 29 · 1 imagen(es)

• Method 1: MAD = 5.77 ; MSE = 51.69
• Method 2: MAD = 6 ; MSE = 41.8
• So??
Whats the best method?
Errores de Pronóstico
-15
-10
-5
0
5
10
15
1
2
3
4
5
6
7
8
9
10
Tiempo
Error
et1
et2

### Página 30 · 1 imagen(es)

Exercise
– For the next set of data, and their forecasts, say 
which method is best.
Data
MA n = 3
MA n = 5
13,9
13,4
16,4
14,1
14,6
8,8
14,6
15,8
13,1
13,3
15,2
12,9
13,7
15,2
13,3
14,1
13,9
15,4
13,8
17,3
14,7
13,8

### Página 31 · 1 imagen(es)

• THANKS!

