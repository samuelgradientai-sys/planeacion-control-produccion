# L04-plotting-your-data

> **Archivo:** [`L04-plotting-your-data.pdf`](./L04-plotting-your-data.pdf) · **Corte 1** · 31 páginas  
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

- [graficas-pronosticos-ventas-autocorrelacion.md](./graficas-pronosticos-ventas-autocorrelacion.md): hoja de clase con rezagos, correlograma y dispersión sobre datos de ventas.
- [tarea-class-example-1.md](./tarea-class-example-1.md), [tarea-class-example-2.md](./tarea-class-example-2.md), [tarea-class-example-3.md](./tarea-class-example-3.md), [tarea-class-example-4.md](./tarea-class-example-4.md): tarea «Pronósticos de demandas» que aplica rezagos, autocorrelación con límites, histograma, boxplot y dispersión.
- [README de esta carpeta](./README.md).
- Siguiente tema: [04 — datos estacionarios, promedio móvil y suavización simple](../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/README.md); la autocorrelación vuelve a usarse en [07 — ARIMA](../07-arima/).
- La ACF se aplicó también en el [proyecto THYMS de pronóstico](../proyecto-thyms-pronostico/).

## Contenido completo (página por página)

### Página 1 — Operations Management / Forecasting

Portada: **Operations Management** — **Forecasting**. Universidad de La Sabana.

> [Imagen decorativa: foto del campus (edificio de la biblioteca), escudo de la Universidad de La Sabana y logo de licencia Creative Commons BY-NC-SA]

### Página 2 — Lecture Objective

- To introduce forecasting methods, it is important to learn how to visualize your data.
- Understand the data better than just the average.

> [Imagen decorativa: fotografía en blanco y negro de un hombre con casco mirando con binoculares desde un tejado, con la cúpula de la catedral de San Pablo (Londres) al fondo]

### Página 3 — Plot your data !

- Histograms
  - Tune the class intervals
- Data series
  - Tune the granularity
- Boxplot
  - Correlate with other variables (location, age, nationality, etc.)
- Autocorrelogram
- Scatter plot

> [Gráfico: barras apiladas «Sources of development assistance for health, 1990-2014 – IHME»; eje Y en «2014 U.S. Dollars», eje X años 1990–2014; series apiladas por fuente (Unallocable, Other, Debt repayments, Corporate donations, BMGF, Private other, Other governments, Australia, Canada, France, Germany, Japan, Netherlands, Norway, Spain, United Kingdom, United States). El total crece de forma sostenida, con fuerte aumento desde ~2002 hasta ~2010 y luego se estabiliza. Ejemplo ilustrativo de serie de datos.]

> [Gráfico: matriz de diagramas de dispersión «Iris Data (red=setosa, green=versicolor, blue=virginica)» con las variables Sepal.Length, Sepal.Width, Petal.Length y Petal.Width cruzadas entre sí; los puntos rojos (setosa) forman un grupo separado y versicolor/virginica muestran relación lineal positiva en las variables de pétalo. Ejemplo ilustrativo de scatter plot.]

### Página 4 — Plot your data !

- Exercise:
- Generate 1’000.000 demand data in an Excel spreadsheet using a normal distribution with mean 500 and standard deviation 50.
- Plot them!

### Página 5 — How to identify which elements on my time series data?

**Direct observation**

> [Gráfico: serie de tiempo con eje X de 60 a 90 (periodos/años) y eje Y de 100 a 500. Tres series: **VENTAS** (línea continua, muy oscilante, entre ~115 y ~450), **CICLO** (línea punteada que suaviza la serie: baja a ~200 cerca de 67–70, sube a ~330 hacia 72–73, cae a ~210 cerca de 75, alcanza su máximo ~360 hacia 77–78, cae a ~150 cerca de 82 y vuelve a ~290 hacia 86) y **TENDENCIA** (línea discontinua casi recta, crece suavemente de ~235 en 60 a ~275 en 90). Muestra cómo, por observación directa, se separan en una serie de ventas la tendencia, el ciclo y la variación aleatoria/estacional.]

### Página 6 — Correlograms

These are charts that show the autocorrelation coefficients of the data series.

Autocorrelation allows you to determine whether the values a variable takes over time are independent of each other or whether they depend on the previous data. That is, it allows you to determine values that are correlated at different lags over time.

These graphs are formed by the autocorrelation coefficients obtained with different lags, and by the limits of significance.

> [Gráfico (arriba): serie de tiempo x de 100 observaciones, eje Y de −4 a 4, puntos azules unidos por líneas que oscilan alrededor de 0.]

> [Gráfico (abajo): correlograma (ACF) de esa serie para rezagos 0 a 100; la barra del rezago 0 vale 1,0; las siguientes barras alternan signos con un patrón ondulatorio (valores entre ~−0,4 y ~0,4) que se amortigua a medida que crece el rezago; dos líneas azules discontinuas horizontales marcan los límites de significancia en aproximadamente ±0,2.]

### Página 7 — Correlograms

Autocorrelation coefficient at lag 1:

$$r_1=\frac{\sum_{t=1}^{N-1}(x_t-\bar{x})(x_{t+1}-\bar{x})}{\sum_{t=1}^{N}(x_t-\bar{x})^2}$$

Autocorrelation coefficient at lag k:

$$r_k=\frac{\sum_{i=1}^{N-k}(x_i-\bar{x})(x_{i+k}-\bar{x})}{\sum_{i=1}^{N}(x_i-\bar{x})^2}$$

Donde $x_t$ es el dato del periodo $t$, $\bar{x}$ la media de la serie, $N$ el número de datos y $k$ el rezago (desfase).

### Página 8 — Example

Lag 1:

| t | x(t) | x(t) − X | (x(t) − X)\*(x(t−1)−X) | (x(t) − X)^2 |
|---|---|---|---|---|
| 1 | −0,36 | | | |
| 2 | −0,52 | | | |
| 3 | 0,46 | | | |
| 4 | −0,31 | | | |
| 5 | −2,05 | | | |
| 6 | 0,28 | | | |
| **Average** | **−0,42** | | | |

autocorrelation coefficient at lag 1 =

(La tabla se presenta vacía para que el estudiante la complete; «X» denota la media $\bar{x}$.)

### Página 9 — Example

Lag 1:

| t | x(t) | x(t) − X | (x(t) − X)\*(x(t−1)−X) | (x(t) − X)^2 |
|---|---|---|---|---|
| 1 | −0,36 | 0,06 | | 0,00 |
| 2 | −0,52 | −0,10 | −0,006 | 0,01 |
| 3 | 0,46 | 0,88 | −0,091 | 0,77 |
| 4 | −0,31 | 0,11 | 0,094 | 0,01 |
| 5 | −2,05 | −1,63 | −0,174 | 2,67 |
| 6 | 0,28 | 0,70 | −1,138 | 0,49 |
| **Average** | **−0,42** | **sum =** | **−1,315** | **3,95** |

autocorrelation coefficient at lag 1 = −1,315 / 3,95 = −0,33

### Página 10 — Example

Lag 2

| t | x(t) | x(t) − X | (x(t) − X)\*(x(t−2)−X) | (x(t) − X)^2 |
|---|---|---|---|---|
| 1 | −0,36 | 0,06 | | 0,00 |
| 2 | −0,52 | −0,10 | | 0,01 |
| 3 | 0,46 | 0,88 | 0,0528 | 0,77 |
| 4 | −0,31 | 0,11 | −0,011 | 0,01 |
| 5 | −2,05 | −1,63 | −1,434 | 2,67 |
| 6 | 0,28 | 0,70 | 0,077 | 0,49 |
| **Average** | **−0,42** | **Sum =** | **−1,316** | **3,95** |

autocorrelation coefficient at lag 2 = −1,316 / 3,95 = −0,33

### Página 11 — Example

Lag 3:

| t | x(t) | x(t) − X | (x(t) − X)\*(x(t−3)−X) | (x(t) − X)^2 |
|---|---|---|---|---|
| 1 | −0,36 | 0,06 | | 0,00 |
| 2 | −0,52 | −0,10 | | 0,01 |
| 3 | 0,46 | 0,88 | | 0,77 |
| 4 | −0,31 | 0,11 | 0,0066 | 0,01 |
| 5 | −2,05 | −1,63 | 0,163 | 2,67 |
| 6 | 0,28 | 0,70 | 0,616 | 0,49 |
| **Average** | **−0,42** | **Sum =** | **0,7856** | **3,95** |

autocorrelation coefficient at lag 3 = 0,7856 / 3,95 = 0,1988

### Página 12 — Example (Summary)

| Lag | coefficient |
|---|---|
| 1 | −0,33 |
| 2 | −0,33 |
| 3 | 0,1988 |

> [Gráfico: columnas «Coeficiente de autocorrelación», eje X rezagos 1, 2, 3; eje Y de −0,4 a 0,3. Barras: rezago 1 ≈ −0,33, rezago 2 ≈ −0,33, rezago 3 ≈ 0,20.]

### Página 13 — How to identify which elements on my time series data?

$$\text{Significance limits}=\pm\, t\cdot SE(r_k)$$

- $SE(r_k)$: **Standard Error** del coeficiente de autocorrelación del rezago $k$.
- $t$: «t student value with probability 0.05 and n-1 gdegree of freedom» (valor t de Student con probabilidad 0,05 y $n-1$ grados de libertad).

$$SE(r_1)\approx\frac{1}{\sqrt{n}}$$

$$SE(r_k)=\sqrt{\frac{1+2\sum_{i=1}^{k-1} r_i^2}{n}}$$

Donde $n$ es el número de datos y $r_i$ el coeficiente de autocorrelación del rezago $i$.

### Página 14 — Example (Summary)

| Lag | coefficient | Upper Limit | Lower Limit |
|---|---|---|---|
| 1 | −0,33 | 1,054524 | −1,05452 |
| 2 | −0,33 | 1,163709 | −1,16371 |
| 3 | 0,1988 | 1,263494 | −1,26349 |

**Not enough data!** (en rojo)

T student value (in this case):

=DISTR.T.INV(0,04925;5)

= 2,58304527

Significance at 4,925% and 5 degrees of freedom

> [Gráfico: salida de Minitab «Función de autocorrelación para C1 (con límites de significancia de 5% para las autocorrelaciones)»; eje Y «Autocorrelación» de −1,0 a 1,0; eje X «Desfase» 1 y 2. Barras azules hacia abajo de ≈ −0,33 en los desfases 1 y 2; líneas rojas discontinuas de límites en ≈ +1,05 → +1,16 y ≈ −1,05 → −1,16. Ninguna barra sale de los límites.]

### Página 15 — Another example

- Make your analysis

> [Gráfico: correlograma de Excel con 12 rezagos (eje X 1–12, eje Y de −1 a 1). Barras azules aproximadas: rezago 1 ≈ −0,38; 2 ≈ −0,12; 3 ≈ 0,14; 4 ≈ −0,20; 5 ≈ 0,07; 6 ≈ 0,00; 7 ≈ −0,26; 8 ≈ 0,40; 9 ≈ −0,08; 10 ≈ −0,11; 11 ≈ 0,02; 12 ≈ 0,04. Límite superior (línea naranja) creciente: ≈ 0,58 en el rezago 1, ≈ 0,66 en el 2, ≈ 0,67–0,70 entre el 3 y el 7, ≈ 0,73 en el 8, ≈ 0,80–0,81 entre el 9 y el 12. Límite inferior (línea gris) simétrico, de ≈ −0,58 a ≈ −0,81. Ninguna barra supera los límites; la más alta es la del rezago 8 (≈ 0,40).]

(Valores leídos del gráfico, aproximados.)

### Página 16 — How does the data series behave according to the correlogram?

- ***Trendline:*** the autocorrelation coefficients are significantly higher than zero in the first lags and gradually fall to zero.
- ***Seasonality:*** the autocorrelation coefficient corresponding to a certain lag (according to seasonality) is significantly different from zero, it is convenient to perform the analysis by removing the trend from the series.
- ***Randomness:*** the autocorrelation coefficients are mostly close to zero.

> [Gráfico 1 «Trendline»: ventas (eje Y «Sales», 0–140) contra periodo (eje X «Period», 0–14). Datos aproximados de los periodos 1 a 10: 20, 32, 51, 43, 62, 63, 82, 75, 92, 89. Línea de tendencia punteada extendida hasta el periodo 13 con ecuación $y = 7{,}7515x + 18{,}267$ y $R^2 = 0{,}9295$.]

> [Gráfico 2: serie mensual «Reported cases of malaria in pregnancy» de 2009 a 2014 (eje Y 0–12000); patrón estacional claro, con picos anuales (≈ 6800 en 2010, ≈ 7500 en 2011, ≈ 8500 en 2013, ≈ 10300 en 2014) y valles de ≈ 3000–4000. Ilustra estacionalidad.]

> [Gráfico 3 «Trajectory»: serie roja muy ruidosa d contra N (0 a 50000), con valores entre ≈ −70 y ≈ 70 alrededor de 0. Ilustra aleatoriedad.]

### Página 17 — How to identify which elements on my time series data?

***Ljung-Box Test***

H0: The data are independently distributed (i.e. the correlations in the population from which the sample is taken from are zero, so that any correlations observed in the data are the result of the randomness of the sampling process).

Ha: The data is not independently distributed.

$$Q=n(n+2)\sum_{k=1}^{h}\frac{r_k^2}{n-k}$$

- $Q$: test statistic.
- $n$: sample size (number of data values).
- $h$: number of lags («Number lof lags» en la diapositiva).
- $r_k$: autocorrelation coefficient at lag k.

If $Q>\chi^2_{\alpha,h}$, reject H0 → correlated data.

### Página 18 — Example

Using the data series from the previous example, determine whether or not there is data independence.

Answer:

| t | r(t) | r²(t) | r²(t)/n−k |
|---|---|---|---|
| 1 | −0,33 | 0,1089 | 0,0218 |
| 2 | −0,33 | 0,1089 | 0,0272 |
| 3 | 0,1988 | 0,03952144 | 0,01317 |
| | | **suma** | **0,0622** |

$Q = 6 \cdot 8 \cdot 0{,}0622 = 2{,}9846$

$\chi^2_{\alpha,h} = 7{,}81$

Conclusion: $Q < \chi^2_{\alpha,h}$ → No evidence of data correlation

### Página 19 — Exercise

- Go to Cloud and use Minitab
- Go to Excel and program a spreadsheet to compute a correlogram.

### Página 20 — Minitab options

- Check the time-series options

> [Imagen: captura de pantalla de Minitab con el menú **Stat → Time Series** desplegado. Opciones del submenú: Time Series Plot…, Trend Analysis…, Decomposition…, Moving Average…, Single Exp Smoothing…, Double Exp Smoothing…, Winters' Method…, Differences…, Lag…, **Autocorrelation…** (resaltada), Partial Autocorrelation…, Cross Correlation…, ARIMA…. Otras entradas del menú Stat: Basic Statistics, Regression, ANOVA, DOE, Control Charts, Quality Tools, Reliability/Survival, Multivariate, Tables, Nonparametrics, Equivalence Tests, Power and Sample Size. Tooltip de Autocorrelation: «Measure how well observations at different time points correlate with each other and look for a seasonal pattern. Use this analysis in conjunction with the Partial autocorrelation function to identify the components for an ARIMA model.»]

### Página 21 — Other software

- Tableau

> [Imagen: captura de un tablero de Tableau «Asset Output - Time Trends by Well and Fault Types»: mapa de África occidental con burbujas por pozo, filtro «Select Fault Type» (Ring Type I, Ring Type II, Dip Type I…), gráfico «Oil Output by Well & Year» (curvas acumuladas 2006–2009, 0–3K kbbl), gráfico de barras «Oil Output by Well» (0–120K, avg 28,768) y un control deslizante «Oil Cumulative (kbbl)» de 0 a 273,462.]

> [Imagen: captura de Tableau Server, proyecto «Manufacturing Indicators», con miniaturas de libros de trabajo (Product Defects, Key Metrics, Defect Age Tracking, Shipping Rates, Cluster Analysis, Best Data Opportunities, Arrival Trends, Demand Site Performance).]

### Página 22 — Principal Component Analysis

- Imagine that you have historical data for the sales of 15 stores (or products for 13 periods (months) as shown in the table.
- Each period is a dimension of data.

| Store | day 1 | day 2 | day 3 | day 4 | day 5 | day 6 | day 7 | day 8 | day 9 | day 10 | day 11 | day 12 | day 13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 76,4 | 9,7 | 28,8 | 79,6 | 18,2 | 18,5 | 79,6 | 28,5 | 10,0 | 76,5 | 39,6 | 3,8 | 70,5 |
| 2 | 76,0 | 73,0 | 74,0 | 73,0 | 72,0 | 69,0 | 67,0 | 68,0 | 69,0 | 68,0 | 67,0 | 65,0 | 63,0 |
| 3 | 25,0 | 30,0 | 30,0 | 33,0 | 36,0 | 41,0 | 42,0 | 43,0 | 48,0 | 48,0 | 47,0 | 47,0 | 52,0 |
| 4 | 26,0 | 22,0 | 23,0 | 23,0 | 28,0 | 28,0 | 23,0 | 30,0 | 29,0 | 21,0 | 20,0 | 22,0 | 25,0 |
| 5 | 67,3 | 17,3 | 31,6 | 69,7 | 23,7 | 23,9 | 69,7 | 31,4 | 17,5 | 67,4 | 39,7 | 12,8 | 62,9 |
| 6 | 20,0 | 19,0 | 23,0 | 21,0 | 27,0 | 26,0 | 26,0 | 27,0 | 33,0 | 38,0 | 44,0 | 44,0 | 45,0 |
| 7 | 80,0 | 77,0 | 75,0 | 73,0 | 71,0 | 68,0 | 67,0 | 65,0 | 62,0 | 59,0 | 56,0 | 54,0 | 53,0 |
| 8 | 39,0 | 39,0 | 45,0 | 44,0 | 46,0 | 49,0 | 51,0 | 50,0 | 51,0 | 58,0 | 64,0 | 71,0 | 73,0 |
| 9 | 43,2 | 9,9 | 19,4 | 44,8 | 14,1 | 14,3 | 44,8 | 19,2 | 10,0 | 43,3 | 24,8 | 6,9 | 40,3 |
| 10 | 18,5 | 11,4 | 59,8 | 26,6 | 5,8 | 56,3 | 35,1 | 2,3 | 50,8 | 43,2 | 1,0 | 43,7 | 50,4 |
| 11 | 23,4 | 13,9 | 78,4 | 34,2 | 6,4 | 73,8 | 45,5 | 1,7 | 66,4 | 56,3 | 0,0 | 57,0 | 65,9 |
| 12 | 46,6 | 4,5 | 20,4 | 49,2 | 9,4 | 13,8 | 50,0 | 15,4 | 8,0 | 48,7 | 22,3 | 3,5 | 45,6 |
| 13 | 16,7 | 11,9 | 44,2 | 22,1 | 8,2 | 41,9 | 27,7 | 5,8 | 38,2 | 33,2 | 5,0 | 33,5 | 37,9 |
| 14 | 32,5 | 25,4 | 73,8 | 40,6 | 19,8 | 70,3 | 49,1 | 16,3 | 64,8 | 57,2 | 15,0 | 57,7 | 64,4 |
| 15 | 93,0 | 86,0 | 79,0 | 74,0 | 68,0 | 67,0 | 63,0 | 57,0 | 52,0 | 46,0 | 39,0 | 34,0 | 33,0 |

### Página 23 — Principal Component Analysis

- Lets plot the total (sum) of sales per period. Do you see a pattern?

> [Gráfico: línea «Total sales per period», eje X periodos 1–13, eje Y 0–900. La suma de la tabla de la página 22 por periodo es: 683,6; 450,0; 705,4; 707,8; 453,6; 660,8; 740,5; 460,6; 609,7; 763,8; 484,4; 555,9; 781,9 (totales calculados a partir de la tabla; coinciden con la gráfica). La serie oscila en zigzag entre ≈ 450 y ≈ 780 con caídas en los periodos 2, 5, 8 y 11 (cada 3 periodos) y una ligera tendencia creciente en los picos.]

### Página 24 — Principal Component Analysis

- Lets plot the sales per store per period. Do you see a pattern?

> [Gráfico: líneas «Sales per store per period» con 15 series (Series1 a Series15, una por tienda), eje X periodos 1–13, eje Y 0–100. Se superponen series casi planas o con tendencia (tiendas 2, 3, 4, 6, 7, 8, 15) y series muy oscilantes (tiendas 1, 5, 9, 10, 11, 12, 13, 14); a simple vista es difícil distinguir patrones.]

### Página 25 — Principal Component Analysis

- Lets compute the principal components (using Minitab for example)

Salida de Minitab — «Análisis de los valores y vectores propios de la matriz de correlación»:

| | PC1 | PC2 | PC3 | PC4 | PC5 | PC6 | PC7 | PC8 | PC9 | PC10 | PC11 | PC12 | PC13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Eigenvalue | 6,4285 | 3,4265 | 2,0129 | 1,0798 | 0,0306 | 0,0144 | 0,0053 | 0,0018 | 0,0002 | 0,0000 | 0,0000 | 0,0000 | −0,0000 |
| Proporción | 0,495 | 0,264 | 0,155 | 0,083 | 0,002 | 0,001 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | −0,000 |
| Acumulada | **0,495** | **0,758** | 0,913 | 0,996 | 0,998 | 0,999 | 1,000 | 1,000 | 1,000 | 1,000 | 1,000 | 1,000 | 1,000 |

(Los valores acumulados 0,495 y 0,758 aparecen encerrados en círculos rojos.)

- Plotting your data in one dimensión you obtain **49.5%** of you information. In two dimensions you obtain **75.8%** of the information

### Página 26 — Principal Component Analysis

- Lets plot the behavior per store in two dimensions

> [Gráfico: Minitab «Gráfica de puntuación de day 1; ...; day 13»; eje X «Primer componente» (−3 a 5), eje Y «Segundo componente» (−4 a 3). Posiciones aproximadas de cada tienda (PC1, PC2): 1 (0,6; −3,8), 2 (4,7; 0,5), 3 (−0,2; 0,5), 4 (−2,9; 0,5), 5 (0,4; −2,8), 6 (−2,0; 0,5), 7 (4,2; 0,3), 8 (1,8; 0,6), 9 (−2,4; −1,8), 10 (−2,0; 1,9), 11 (−0,6; 2,5), 12 (−2,3; −2,2), 13 (−2,9; 1,4), 14 (0,3; 2,0), 15 (3,3; 0,1). Tres grupos encerrados en círculos rojos: {9, 12}, {5, 1} y {7, 2}.]

- Stores 9 and 12 are similar (close)
- Stores 1 and 5 are similar (close)
- Stores 7 and 2 are similar (close)

### Página 27 — Principal Component Analysis

- Lets check the results:

> [Gráfico: «Sales per store per period», Series9 (gris) y Series12 (verde), periodos 1–13, eje Y 0–60. Ambas siguen el mismo zigzag con picos en los periodos 1, 4, 7, 10 y 13 (≈ 43–50) y valles en 2, 5–6, 9 y 12 (≈ 4–14).]

- **Stores 9 and 12 are similar (close)** (resaltado)
- Stores 1 and 5 are similar (close) (atenuado)
- Stores 7 and 2 are similar (close) (atenuado)

### Página 28 — Principal Component Analysis

- Lets check the results:

> [Gráfico: «Sales per store per period», Series1 y Series5, periodos 1–13, eje Y 0–90. Ambas con el mismo patrón en zigzag: picos ≈ 67–80 en los periodos 1, 4, 7, 10 y 13 y valles ≈ 4–24 en 2, 5–6, 9 y 12.]

- Stores 9 and 12 are similar (close) (atenuado)
- **Stores 1 and 5 are similar (close)** (resaltado)
- Stores 7 and 2 are similar (close) (atenuado)

### Página 29 — Principal Component Analysis

- Lets check the results:

> [Gráfico: «Sales per store per period», Series2 (naranja) y Series7 (azul), periodos 1–13, eje Y 0–90. Ambas descienden suavemente: la tienda 2 de 76 a 63 y la tienda 7 de 80 a 53; casi coinciden hasta el periodo 7.]

- Stores 9 and 12 are similar (close) (atenuado)
- Stores 1 and 5 are similar (close) (atenuado)
- **Stores 7 and 2 are similar (close)** (resaltado)

### Página 30 — Principal Component Analysis

- Lets check the results:

> [Gráfico: «Sales per store per period», Series2 (naranja) y Series13 (azul claro), periodos 1–13, eje Y 0–80. La tienda 2 es casi plana y decreciente (76 → 63); la tienda 13 oscila entre ≈ 5 y ≈ 44 con picos en los periodos 3, 6, 9 y 12–13.]

- Stores 2 and 13 are VERY DIFFERENT (far)

### Página 31 — Principal Component Analysis

- Conclusions:

The PCA may help you define a forecasting strategy for different stores (or products) according to their particular behavior

You may “cluster” stores (or products) with similar behavior.

Thanks to PCA you will better understand your data!

## Anexo: texto extraído automáticamente del PDF

> Texto plano tal como sale del PDF, sin fórmulas ni tablas que estén como imagen. La versión fiel y completa es la sección «Contenido completo» de arriba.

### Página 1 · 2 imagen(es)

Operations Management
Forecasting

### Página 2 · 2 imagen(es)

Lecture Objective
• To introduce forecasting methods, it is 
important to learn how to visualize your 
data. 
• Understand the data better than just the 
average.

### Página 3 · 3 imagen(es)

Plot your data !
• Histograms
– Tune the class intervals
• Data series
– Tune the granularity
• Boxplot
– Correlate with other variables 
(location, age, nationality, etc.)
• Autocorrelogram
• Scatter plot

### Página 4 · 1 imagen(es)

Plot your data !
• Exercise:
• Generate 1’000.000 demand data in an Excel 
spreadsheet using a normal distribution with 
mean 500 and standard deviation 50. 
• Plot them!

### Página 5 · 1 imagen(es)

How to identify which elements on my time series data?
100
200
300
400
500
60
65
70
75
80
85
90
VENTAS
CICLO
TENDENCIA
Direct observation

### Página 6 · 2 imagen(es)

These
are
charts
that
show
the
autocorrelation
coefficients of the data series.
Autocorrelation allows you to determine whether the
values a variable takes over time are independent of
each other or whether they depend on the previous data.
That is, it allows you to determine values that are
correlated at different lags over time.
These
graphs
are
formed
by
the
autocorrelation
coefficients obtained with different lags, and by the limits
of significance.
Correlograms

### Página 7 · 3 imagen(es)

autocorrelation coefficient at lag 1
autocorrelation coefficient at lag k
Correlograms

### Página 8 · 1 imagen(es)

Example
t
x(t)
x(t) - X
(x(t) - X)*(x(t-1)-X)
(x(t) - X)^2
1
-0,36
2
-0,52
3
0,46
4
-0,31
5
-2,05
6
0,28
Average
-0,42
autocorrelation coefficient at lag 1 =
Lag 1:

### Página 9 · 1 imagen(es)

Example
t
x(t)
x(t) - X
(x(t) - X)*(x(t-1)-X)
(x(t) - X)^2
1
-0,36
0,06
0,00
2
-0,52
-0,10
-0,006
0,01
3
0,46
0,88
-0,091
0,77
4
-0,31
0,11
0,094
0,01
5
-2,05
-1,63
-0,174
2,67
6
0,28
0,70
-1,138
0,49
Average
-0,42
sum =
-1,315
3,95
autocorrelation coefficient at lag 1 = -1,315 / 3,95 = -0,33 
Lag 1:

### Página 10 · 1 imagen(es)

Example
t
x(t)
x(t) - X
(x(t) - X)*(x(t-2)-X)
(x(t) - X)^2
1
-0,36
0,06
0,00
2
-0,52
-0,10
0,01
3
0,46
0,88
0,0528
0,77
4
-0,31
0,11
-0,011
0,01
5
-2,05
-1,63
-1,434
2,67
6
0,28
0,70
0,077
0,49
Average
-0,42
Sum =
-1,316
3,95
autocorrelation coefficient at lag 2 = -1,316 / 3,95 = -0,33 
Lag 2

### Página 11 · 1 imagen(es)

Example
t
x(t)
x(t) - X
(x(t) - X)*(x(t-3)-X)
(x(t) - X)^2
1
-0,36
0,06
0,00
2
-0,52
-0,10
0,01
3
0,46
0,88
0,77
4
-0,31
0,11
0,0066
0,01
5
-2,05
-1,63
0,163
2,67
6
0,28
0,70
0,616
0,49
Average
-0,42
Sum =
0,7856
3,95
autocorrelation coefficient at lag 3 = 0,7856 / 3,95 = 0,1988 
Lag 3:

### Página 12 · 2 imagen(es)

Example (Summary)
Lag
coefficient
1
-0,33
2
-0,33
3
0,1988

### Página 13 · 1 imagen(es)

Significance limits = ± 𝑡∗𝑆𝐸𝑟𝑘
t student value with 
probability 0.05 and 
n-1 gdegree of 
freedom
𝑆𝐸𝑟1 ≈1
𝑛
𝑆𝐸𝑟𝑘=
1 + 2 σ𝑖=1
𝑘−1 𝑟𝑖
2
𝑛
Standard Error
How to identify which elements 
on my time series data?

### Página 14 · 1 imagen(es)

Example (Summary)
2
1
1,0
0,8
0,6
0,4
0,2
0,0
-0,2
-0,4
-0,6
-0,8
-1,0
Desfase
Autocorrelación
Función de autocorrelación para C1
(con límites de significancia de 5% para las autocorrelaciones)
Lag
coefficient 
Upper Limit
Lower Limit
1
-0,33
1,054524
-1,05452
2
-0,33
1,163709
-1,16371
3
0,1988
1,263494
-1,26349
T student value (in this case): 
=DISTR.T.INV(0,04925;5) 
= 2,58304527 
Significance at 4,925% and 5 
degrees of freedom
Not enough data!

### Página 15 · 2 imagen(es)

Another example
•
Make your analysis

### Página 16 · 4 imagen(es)

How does the data series behave 
according to the correlogram?
Trendline: 
the
autocorrelation
coefficients
are
significantly higher than zero in the first lags and
gradually fall to zero. 
Seasonality 
: 
the
autocorrelation
coefficient
corresponding to a certain lag (according to seasonality)
is significantly different from zero, it is convenient to
perform the analysis by removing the trend from the
series.
Randomness : the
autocorrelation
coefficients
are
mostly close to zero.

### Página 17 · 1 imagen(es)

Ljung-Box Test
H0: The data are independently distributed (i.e. the correlations in the population from
which the sample is taken from are zero, so that any correlations observed in the data
are the result of the randomness of the sampling process).
Ha: The data is not independently distributed.
𝑄= 𝑛(𝑛+ 2) ෍
𝑘=1
ℎ
𝑟𝑘
2
𝑛−𝑘
test statistic
Sample size (number of data values)
autocorrelation 
coefficient at lag k
Number lof lags
If 𝑄> 𝑥𝛼,ℎ
2 , reject H0 -> correlated data
How to identify which elements on my time series data?

### Página 18 · 1 imagen(es)

Example
Using the data series from the previous example, determine whether or not there 
is data independence.
Answer:
Q= 6*8*0,0622 = 2,9846
𝑥𝛼,ℎ
2 = 7,81 
Conclusion: Q < 𝑥𝛼,ℎ
2 -> No evidence of data correlation
t
r(t)
r2(t)
r2(t)/n-k
1
-0,33
0,1089
0,0218
2
-0,33
0,1089
0,0272
3
0,1988
0,03952144
0,01317
suma
0,0622

### Página 19 · 1 imagen(es)

Exercise
• Go to Cloud and use Minitab
• Go to Excel and program a spreadsheet to 
compute a correlogram.

### Página 20 · 2 imagen(es)

Minitab options
•
Check the time-series options

### Página 21 · 3 imagen(es)

Other software
•
Tableau

### Página 22 · 1 imagen(es)

Principal Component Analysis
•
Imagine that you have historical data for the sales of 15 stores (or 
products for 13 periods (months) as shown in the table.
•
Each period is a dimension of data.
Store
day 1
day 2
day 3
day 4
day 5
day 6
day 7
day 8
day 9
day 10
day 11
day 12
day 13
1
76,4
9,7
28,8
79,6
18,2
18,5
79,6
28,5
10,0
76,5
39,6
3,8
70,5
2
76,0
73,0
74,0
73,0
72,0
69,0
67,0
68,0
69,0
68,0
67,0
65,0
63,0
3
25,0
30,0
30,0
33,0
36,0
41,0
42,0
43,0
48,0
48,0
47,0
47,0
52,0
4
26,0
22,0
23,0
23,0
28,0
28,0
23,0
30,0
29,0
21,0
20,0
22,0
25,0
5
67,3
17,3
31,6
69,7
23,7
23,9
69,7
31,4
17,5
67,4
39,7
12,8
62,9
6
20,0
19,0
23,0
21,0
27,0
26,0
26,0
27,0
33,0
38,0
44,0
44,0
45,0
7
80,0
77,0
75,0
73,0
71,0
68,0
67,0
65,0
62,0
59,0
56,0
54,0
53,0
8
39,0
39,0
45,0
44,0
46,0
49,0
51,0
50,0
51,0
58,0
64,0
71,0
73,0
9
43,2
9,9
19,4
44,8
14,1
14,3
44,8
19,2
10,0
43,3
24,8
6,9
40,3
10
18,5
11,4
59,8
26,6
5,8
56,3
35,1
2,3
50,8
43,2
1,0
43,7
50,4
11
23,4
13,9
78,4
34,2
6,4
73,8
45,5
1,7
66,4
56,3
0,0
57,0
65,9
12
46,6
4,5
20,4
49,2
9,4
13,8
50,0
15,4
8,0
48,7
22,3
3,5
45,6
13
16,7
11,9
44,2
22,1
8,2
41,9
27,7
5,8
38,2
33,2
5,0
33,5
37,9
14
32,5
25,4
73,8
40,6
19,8
70,3
49,1
16,3
64,8
57,2
15,0
57,7
64,4
15
93,0
86,0
79,0
74,0
68,0
67,0
63,0
57,0
52,0
46,0
39,0
34,0
33,0

### Página 23 · 1 imagen(es)

Principal Component Analysis
•
Lets plot the total (sum) of sales per period. Do you see a pattern?
0
100
200
300
400
500
600
700
800
900
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
11
12
13
Total sales per period

### Página 24 · 2 imagen(es)

Principal Component Analysis
•
Lets plot the sales per store per period. Do you see a pattern?

### Página 25 · 1 imagen(es)

Principal Component Analysis
•
Lets compute the principal components (using Minitab for example)
•
Plotting your data in one dimensión you obtain 49.5% of you 
information. In two dimensions you obtain 75.8% of the information
Análisis de los valores y vectores propios de la matriz de correlación
Eigenvalue 6,4285 3,4265 2,0129 1,0798 0,0306 0,0144 0,0053 0,0018
Proporción 0,495 0,264 0,155 0,083 0,002 0,001 0,000 0,000
Acumulada
0,495 0,758 0,913 0,996 0,998 0,999 1,000 1,000
Eigenvalue 0,0002 0,0000 0,0000 0,0000 -0,0000
Proporción 0,000 0,000 0,000 0,000 -0,000
Acumulada
1,000 1,000 1,000 1,000 1,000

### Página 26 · 1 imagen(es)

Principal Component Analysis
•
Lets plot the behavior per store in two dimensions
5
4
3
2
1
0
-1
-2
-3
3
2
1
0
-1
-2
-3
-4
Primer componente
Segundo componente
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
Gráfica de puntuación de day 1; ...; day 13
•
Stores 9 and 12 
are similar (close)
•
Stores 1 and 5 
are similar (close)
•
Stores 7 and 2 
are similar (close)

### Página 27 · 2 imagen(es)

Principal Component Analysis
•
Lets check the results:
•
Stores 9 and 12 
are similar (close)
•
Stores 1 and 5 
are similar (close)
•
Stores 7 and 2 
are similar (close)

### Página 28 · 2 imagen(es)

Principal Component Analysis
•
Lets check the results:
•
Stores 9 and 12 
are similar (close)
•
Stores 1 and 5 
are similar (close)
•
Stores 7 and 2 
are similar (close)

### Página 29 · 2 imagen(es)

Principal Component Analysis
•
Lets check the results:
•
Stores 9 and 12 
are similar (close)
•
Stores 1 and 5 
are similar (close)
•
Stores 7 and 2 
are similar (close)

### Página 30 · 2 imagen(es)

Principal Component Analysis
•
Lets check the results:
•
Stores 2 and 13 
are VERY 
DIFFERENT (far)

### Página 31 · 1 imagen(es)

Principal Component Analysis
•
Conclusions:
The PCA may help you define a forecasting strategy for different stores 
(or products) according to their particular behavior 
You may “cluster” stores (or products) with similar behavior.
Thanks to PCA you will better understand your data!

