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


---

<!-- fuente: corte-1-pronosticos/03-graficas-y-autocorrelacion/graficas-pronosticos-ventas-autocorrelacion.md -->
# graficas-pronosticos-ventas-autocorrelacion

> **Archivo:** [`graficas-pronosticos-ventas-autocorrelacion.xlsx`](/corte-1-pronosticos/03-graficas-y-autocorrelacion/graficas-pronosticos-ventas-autocorrelacion.xlsx) · **Corte 1** · Libro de Excel con 2 hoja(s): `ANALISIS DE CORRELACION`, `DATOS`  
> **Nombre original:** `CORTE 1/GRAFICAS PARAA PRONOSCTICOS DE VENTAS.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Hoja de clase (nombre original «GRAFICAS PARAA PRONOSCTICOS DE VENTAS») que aplica las herramientas de visualización de la [Lección 4 — Plotting your data](/corte-1-pronosticos/03-graficas-y-autocorrelacion/L04-plotting-your-data.md) a una serie larga de ventas: serie de tiempo, diagrama de dispersión $X_t$ frente a $X_{t-1}$ y **autocorrelograma** de 20 rezagos. Con ella se aprende a construir la tabla de rezagos en Excel, a obtener los coeficientes de autocorrelación con la matriz de correlación y a reconocer una serie **aleatoria** (sin tendencia, ciclo ni estacionalidad), en la que la venta de hoy no ayuda a predecir la de mañana.

### Hoja `DATOS`

**Objetivo (deducido):** preparar la serie y sus 20 rezagos para medir la autocorrelación y graficar los datos.

**Datos de entrada**

| Columna | Contenido |
|---|---|
| A `fecha` | Índice del periodo, de 1 a 30.000 (no es una fecha de calendario). |
| B `ventas` | Ventas por periodo: 30.000 datos enteros (filas 2–30001). |
| C–V `Rezago 1` … `Rezago 20` | La columna de ventas desplazada $k$ filas hacia abajo: en la fila del periodo $t$, `Rezago k` contiene $X_{t-k}$. Son valores pegados, no fórmulas; cada columna termina $k$ filas más abajo (hasta la fila 30021 para el rezago 20). |
| AE23, AE26 | Notas de texto del estudiante (ver «Gráficos»). |

Estadísticos de `ventas` (calculados sobre el CSV): $n=30.000$; mínimo 0; máximo 22; media 8,006; mediana 8; desviación estándar 2,808 (varianza ≈ 7,89, casi igual a la media, lo que sugiere —deducido— datos simulados con una distribución tipo Poisson de media ≈ 8).

Frecuencia de cada valor de ventas:

| Ventas | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Frecuencia | 10 | 83 | 310 | 788 | 1.716 | 2.807 | 3.581 | 4.291 | 4.221 | 3.658 | 3.012 | 2.191 |

| Ventas | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Frecuencia | 1.414 | 925 | 486 | 273 | 145 | 52 | 26 | 5 | 4 | 1 | 1 |

Todos los valores están en [`graficas-pronosticos-ventas-autocorrelacion-datos/DATOS.csv`](/corte-1-pronosticos/03-graficas-y-autocorrelacion/graficas-pronosticos-ventas-autocorrelacion-datos/DATOS.csv).

**Gráficos**

- «Serie de tiempos» (líneas, `B2:B30001`): las 30.000 ventas en orden; una banda de ruido alrededor de 8, sin tendencia ni estacionalidad.
- «SCATTER PLOT» (dispersión): eje X = `ventas` ($X_t$, `B2:B30021`), eje Y = `Rezago 1` ($X_{t-1}$, `C2:C30021`). La nube no muestra relación lineal. Las notas del estudiante junto al gráfico dicen: «LINEA TENDENCIA ESTA SE BASA EN SI LAS VENTAS DE HOY SE PUEDEN REDECIR MAÑANA SI SE ACERA A LA LINE» (AE23) y «LAS BOLITAS DICEN SI HOY COMPRO MAÑANA DE PRONTO NO Y ASI» (AE26). El archivo no guarda una línea de tendencia en el gráfico.

### Hoja `ANALISIS DE CORRELACION`

**Objetivo:** calcular el coeficiente de autocorrelación de los rezagos 1 a 20 y graficar el autocorrelograma.

**Método paso a paso**

1. Se aplicó la herramienta *Análisis de datos → Correlación* de Excel a las 21 columnas `ventas`, `Rezago 1` … `Rezago 20`. El resultado es la matriz triangular de correlaciones de Pearson pegada como valores (sin fórmulas) en `A1:V22`; las etiquetas originales «Columna 1…21» se cambiaron por «REZAGO 1…20» en la columna A.
2. La columna B (`COEFECIENTE DE AUTORRELACION 1` = correlación con `ventas`) es el autocorrelograma: la fila del rezago $k$ contiene
   $$r_k\approx\operatorname{corr}(X_t,\,X_{t-k}).$$
   Se comprobó que estos valores coinciden con la correlación de Pearson calculada sobre las filas 22–30001 (29.980 filas en las que las 21 columnas tienen dato). Es una aproximación de la fórmula de $r_k$ de la L04 (allí se usa una sola media y el denominador de toda la serie); con 30.000 datos la diferencia es mínima.
3. El resto de la matriz (columnas C–V) son correlaciones entre rezagos; repite los mismos valores desplazados en diagonal y no se usa.

**Resultados — coeficientes de autocorrelación (columna B)**

| Rezago $k$ | $r_k$ | Rezago $k$ | $r_k$ |
|---|---|---|---|
| 1 | −0,000119 | 11 | −0,003981 |
| 2 | −0,008582 | 12 | 0,008942 |
| 3 | −0,002835 | 13 | −0,012121 |
| 4 | 0,001826 | 14 | 0,004399 |
| 5 | 0,011852 | 15 | −0,007323 |
| 6 | 0,000173 | 16 | −0,010894 |
| 7 | −0,005568 | 17 | −0,004121 |
| 8 | −0,001765 | 18 | 0,007372 |
| 9 | −0,001287 | 19 | 0,003375 |
| 10 | −0,001295 | 20 | −0,003897 |

**Gráfico:** «AUTOCORRELOGRAMA DE LOS DATOS» (barras, `B3:B22`): 20 barras diminutas alrededor de cero, todas con $|r_k|<0{,}013$. La hoja no dibuja límites de significancia.

**Conclusión**

- Todos los coeficientes son prácticamente cero: la serie es **aleatoria** (ruido alrededor de una media constante ≈ 8); no hay tendencia (los $r_k$ no son altos ni decrecen lentamente) ni estacionalidad (ningún rezago destaca). Así lo indica también la nota del estudiante: conocer la venta de hoy no permite predecir la de mañana.
- Cálculo propio con la fórmula de la L04: el límite de significancia del rezago 1 es $\pm t_{0,05;\,29999}/\sqrt{30000}=\pm1{,}96/173{,}2\approx\pm0{,}0113$. Solo los rezagos 5 (0,0119) y 13 (−0,0121) lo superan por muy poco, lo que con 20 rezagos y 5 % de significancia es esperable por azar (≈ 1 de cada 20).
- Para una serie así, un método para datos estacionarios (promedio o suavización simple, [carpeta 04](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/README.md)) es el adecuado.

### Observaciones

- Ninguna celda tiene fórmulas: los rezagos y la matriz de correlación son valores pegados.
- El gráfico de dispersión toma hasta la fila 30021 aunque las ventas terminan en la 30001 (las últimas 20 filas solo tienen rezagos).
- La columna `fecha` es un contador de periodos, no una fecha.
- Hay errores ortográficos en los rótulos («COEFECIENTE DE AUTORRELACION», «PARAA PRONOSCTICOS»), sin efecto en los cálculos.


---

<!-- fuente: corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-1.md -->
# tarea-class-example-1

> **Archivo:** [`tarea-class-example-1.xlsx`](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-1.xlsx) · **Corte 1** · Libro de Excel con 14 hoja(s): `Ventas propias`, `Coeficientes ventas propias`, `Serie de tiempo  ventas propias`, `Histograma Ventas Propias`, `Autocorrelograma ventas propias`, `Boxplot Ventas Propias`, `Scatterplot Ventas Propias`, `Ventas competencia`, `Coeficientes ventas competencia`, `Serie de tiempo Ventas Comp`, `Histograma Ventas Competencia`, `Autocorrelograma Ventas Compete`, `Boxplot Ventas Competencia`, `Scatterplot Ventas Competencia`  
> **Nombre original:** `CORTE 1/TAREAS/PRONOSCITOS DE DEMANDAS/Class example 1.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Primer libro de la tarea «Pronósticos de demandas» (nombre original `TAREAS/PRONOSCITOS DE DEMANDAS/Class example 1.xlsx`). Aplica las herramientas de la [Lección 4 — Plotting your data](/corte-1-pronosticos/03-graficas-y-autocorrelacion/L04-plotting-your-data.md) a dos series diarias: **ventas propias** y **ventas de la competencia**. Para cada una construye la tabla de 20 rezagos, los coeficientes de autocorrelación con sus **límites de significancia** y cinco gráficos (serie de tiempo, histograma, autocorrelograma, boxplot y dispersión $X_t$ frente a $X_{t-1}$). Se aprende a detectar datos atípicos con el boxplot y a decidir, con el correlograma, si la serie es aleatoria.

Las dos partes (ventas propias y competencia) siguen exactamente la misma estructura de hojas.

### Hojas `Ventas propias` y `Ventas competencia` (datos y rezagos)

**Objetivo (deducido del enunciado de la tarea):** organizar cada serie con sus rezagos 1 a 20 para calcular la autocorrelación.

**Datos de entrada**

- Columna A `Fecha`: 1.923 días consecutivos, **en orden descendente**, del 2019-08-30 (fila 2) al 2014-05-26 (fila 1924), sin fechas faltantes ni repetidas.
- Columna B: ventas del día (filas 2–1924). En la hoja `Ventas competencia` el encabezado dice por error «Ventas propias».
- Columnas C–V `Rezago 1` … `Rezago 20`: la columna B desplazada $k$ filas hacia abajo (valores pegados, sin fórmulas). Como las fechas van de la más reciente a la más antigua, en la fila del día $d$ el `Rezago k` contiene la venta del día $d+k$ (el día siguiente), no la del anterior. Para la autocorrelación da igual, porque $\operatorname{corr}(X_t,X_{t+k})=\operatorname{corr}(X_t,X_{t-k})$.
- Nombres definidos en el libro: `DATOS` = `'Ventas propias'!A22:V1924`, `DATOS1` = `'Ventas propias'!B22:V1924`, `DATOS2` = `'Ventas competencia'!B22:V1924` (los rangos usados para la matriz de correlación).
- CSV completos: [`Ventas_propias.csv`](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-1-datos/Ventas_propias.csv) y [`Ventas_competencia.csv`](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-1-datos/Ventas_competencia.csv).

**Estadísticos (calculados sobre los datos)**

| Serie | n | Mínimo | Q1 | Mediana | Q3 | Máximo | Media | Desv. estándar |
|---|---|---|---|---|---|---|---|---|
| Ventas propias | 1.923 | 9 | 1.717 | 1.943 | 2.153 | 31.624 | 1.954,15 | 725,72 |
| Ventas competencia | 1.923 | 2 | 805 | 1.019 | 1.241 | 1.464 | 1.019,18 | 255,42 |

(Cuartiles con el método exclusivo, el mismo que usa el boxplot del archivo.)

**Datos atípicos** (fuera de $Q_1-1{,}5\,RIQ$ y $Q_3+1{,}5\,RIQ$; $RIQ=436$ en ambas series):

| Serie | Fecha | Valor | Límites del boxplot |
|---|---|---|---|
| Ventas propias | 2019-07-14 | 31.624 | 1.063 – 2.807 |
| Ventas propias | 2019-06-08 | 12 | 1.063 – 2.807 |
| Ventas propias | 2017-10-10 | 9 | 1.063 – 2.807 |
| Ventas competencia | 2017-06-19 | 2 | 151 – 1.895 |

Sin los atípicos, las ventas propias van de 1.500 a 2.400 (media 1.940,7; desviación 254,3) y las de la competencia de 550 a 1.464 (media 1.019,7; desviación 254,4); en ambos casos el histograma es casi plano. El valor 31.624 explica él solo el 87,7 % de la suma de cuadrados de las ventas propias e infla su desviación estándar de ≈ 254 a 726.

**Relación entre las dos series (hallazgo propio, no está en el archivo):** fuera de los días atípicos, ventas propias + ventas competencia está siempre entre 2.950 y 2.970 (media 2.960) y la correlación entre ambas es −0,9997. Es decir, el mercado diario es casi constante (≈ 2.960 unidades) y la competencia vende lo que la empresa no vende.

### Hojas `Coeficientes ventas propias` y `Coeficientes ventas competencia`

**Método paso a paso**

1. **Coeficiente de autocorrelación** (columna B, `Columna 1`, filas 3–22): valores pegados de la herramienta *Análisis de datos → Correlación* aplicada a `DATOS1` / `DATOS2` (filas 22–1924, las 1.903 filas en que las 21 columnas tienen dato). Se comprobó que coinciden con la correlación de Pearson entre la columna de ventas y cada rezago:
   $$r_k\approx\operatorname{corr}(X_t,\,X_{t-k}),\qquad k=1,\dots,20.$$
   La fila 2 (`REZAGO`, valor 1) es la correlación de la serie consigo misma (rezago 0).
2. **Límites de significancia** (columnas C y D), según la p. 13 de la L04, con $n=$ `COUNT(B2:B1924)` $=1.923$ y $t=$ `TINV(0.05; n−1)` $=1{,}9612$:
   - Rezago 1: `=±TINV(0.05,COUNT(...)-1)*(1/SQRT(COUNT(...)))`, es decir $\pm t\cdot\dfrac{1}{\sqrt n}=\pm0{,}0447231$.
   - Rezago $k\ge2$: `=±TINV(0.05,COUNT(...)-1)*SQRT((1+2*SUMSQ($B$3:B(k+1)))/COUNT(...))`, es decir
     $$\pm\,t\sqrt{\frac{1+2\sum_{i=1}^{k-1}r_i^2}{n}}.$$

**Resultados**

| Rezago | $r_k$ propias | Límite propias (±) | $r_k$ competencia | Límite competencia (±), alineado como en el gráfico |
|---|---|---|---|---|
| 1 | −0,000466 | 0,044723 | 0,019231 | 0,044723 |
| 2 | 0,002065 | 0,044723 | −0,022244 | 0,044740 |
| 3 | −0,006008 | 0,044723 | −0,001451 | 0,044762 |
| 4 | −0,029202 | 0,044725 | **−0,045928** | 0,044762 |
| 5 | 0,006566 | 0,044763 | 0,020306 | 0,044856 |
| 6 | −0,012125 | 0,044765 | −0,016478 | 0,044874 |
| 7 | 0,021697 | 0,044772 | −0,009156 | 0,044887 |
| 8 | 0,011315 | 0,044793 | 0,019201 | 0,044890 |
| 9 | 0,001126 | 0,044798 | 0,002754 | 0,044907 |
| 10 | 0,009834 | 0,044798 | 0,027866 | 0,044907 |
| 11 | −0,005085 | 0,044803 | 0,018966 | 0,044942 |
| 12 | −0,019854 | 0,044804 | −0,007965 | 0,044958 |
| 13 | −0,003052 | 0,044821 | −0,014783 | 0,044960 |
| 14 | 0,004551 | 0,044822 | −0,027259 | 0,044970 |
| 15 | −0,001138 | 0,044823 | −0,012767 | 0,045003 |
| 16 | −0,003143 | 0,044823 | 0,001042 | 0,045010 |
| 17 | −0,001804 | 0,044823 | 0,015883 | 0,045010 |
| 18 | −0,000902 | 0,044823 | 0,014358 | 0,045022 |
| 19 | 0,000319 | 0,044823 | 0,038556 | 0,045031 |
| 20 | 0,001122 | 0,044823 | 0,001481 | 0,045097 |

(En la tabla de la hoja de competencia, cada límite aparece una fila más abajo; ver Observaciones. El límite inferior del rezago 1 de ventas propias es −0,0447231 y el superior 0,0447348.)

### Hojas de gráficos (iguales para las dos series)

| Hoja | Tipo | Qué muestra |
|---|---|---|
| `Serie de tiempo  ventas propias` / `Serie de tiempo Ventas Comp` | Líneas, `B2:B1944` | Las 1.923 ventas diarias (en el orden de la hoja, del día más reciente al más antiguo). En ventas propias el pico de 31.624 aplasta el resto de la serie; en competencia se ve una banda de ruido entre 550 y 1.464 con la caída a 2. |
| `Histograma Ventas Propias` / `Histograma Ventas Competencia` | Histograma nativo de Excel (agrupación automática) | Distribución casi uniforme de las ventas; en ventas propias el atípico estira el eje. |
| `Autocorrelograma ventas propias` / `Autocorrelograma Ventas Compete` | Barras ($r_k$) + dos líneas (límites inferior y superior) | 20 barras pequeñas alrededor de cero dentro de la banda de ≈ ±0,045. |
| `Boxplot Ventas Propias` / `Boxplot Ventas Competencia` | Caja y bigotes nativo (cuartiles exclusivos, marca de la media, atípicos visibles) | Caja de 1.717 a 2.153 (propias) y de 805 a 1.241 (competencia), con los atípicos de la tabla de arriba. |
| `Scatterplot Ventas Propias` / `Scatterplot Ventas Competencia` | Dispersión, X = ventas (`B2:B1924`), Y = rezago 1 (`C2:C1924`) | «X(t) vs X(t-1)»: nube sin relación lineal. |

### Conclusión

- **Ventas propias:** todos los $r_k$ están dentro de los límites (el mayor en valor absoluto es −0,0292 en el rezago 4) → serie **aleatoria**, sin tendencia ni estacionalidad. Pero el atípico de 31.624 encoge los coeficientes: recalculando la autocorrelación con los tres atípicos reemplazados por la mediana (cálculo propio), los $r_k$ quedan casi iguales a los de la competencia (máximo $|r_k|=0{,}041$ en el rezago 19 y −0,041 en el rezago 4), todavía dentro de los límites.
- **Ventas competencia:** solo el rezago 4 (−0,0459) supera por muy poco el límite (±0,0448); con 20 rezagos al 5 % es esperable que uno salga por azar. En la práctica también es una serie aleatoria.
- Ninguna serie muestra tendencia ni estacionalidad (el rezago 7, que delataría un patrón semanal, no es significativo, y las medias anuales de ventas propias sin atípicos apenas varían entre 1.917 y 1.953): son candidatas a métodos para datos estacionarios ([carpeta 04](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/README.md)). Antes de pronosticar hay que depurar los atípicos (31.624, 12, 9 y 2), que parecen errores de registro.

### Observaciones

- **Límite superior del rezago 1 de ventas propias:** `D3` cuenta `C2:C1924` (1.922 datos) en vez de `B2:B1924` (1.923), por eso vale 0,0447348 y no 0,0447231. Diferencia despreciable.
- **Límites de la hoja de competencia desplazados una fila:** `C2:D2` (fila `REZAGO`, rezago 0) tiene el límite del rezago 1, y la fila del rezago $k$ usa `SUMSQ($B$3:B(k+2))` $=\sum_{i=1}^{k}r_i^2$ (incluye el propio $r_k$) en vez de $\sum_{i=1}^{k-1}r_i^2$. El gráfico toma los límites de `C2:D22` y las barras de `B3:B22`, así que en el gráfico cada barra queda frente a su límite correcto; solo la tabla está corrida (y el gráfico dibuja un punto de límite de más, el 21).
- Los coeficientes no se recalculan solos: son valores pegados; si se corrigen los atípicos hay que repetir la correlación.
- El encabezado de la columna B de `Ventas competencia` dice «Ventas propias».
- Las hojas de este libro son idénticas, celda por celda, a las del mismo nombre en [promedio-movil-y-suavizacion-exponencial.md](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/promedio-movil-y-suavizacion-exponencial.md), que además añade la hoja `Ventas propias (2)` con promedios móviles y suavización exponencial.


---

<!-- fuente: corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-2.md -->
# tarea-class-example-2

> **Archivo:** [`tarea-class-example-2.xlsx`](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-2.xlsx) · **Corte 1** · Libro de Excel con 10 hoja(s): `DATOS`, `DATOS ACF`, `DATOS HISTOGRAMA`, `DATOS BOX PLOT`, `DISPERSION`, `GRAFICO ACF`, `GRAFICO DE SERIES DE TIEMPO `, `GRAFICO HISTOGRAMA`, `GRAFICO BOX PLOT`, `GRAFICO DISPERSION`  
> **Nombre original:** `CORTE 1/TAREAS/PRONOSCITOS DE DEMANDAS/Class example 2.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Segundo libro de la tarea «Pronósticos de demandas» (nombre original `TAREAS/PRONOSCITOS DE DEMANDAS/Class example 2.xlsx`), basado en la [Lección 4 — Plotting your data](/corte-1-pronosticos/03-graficas-y-autocorrelacion/L04-plotting-your-data.md). Tiene las ventas diarias de tres productos y analiza a fondo el **producto 1**: función de autocorrelación hasta el rezago 88 calculada con fórmulas (no con la herramienta de Análisis de datos), límites de significancia, histograma de 40 clases construido a mano, resumen del boxplot y diagrama de dispersión con regresión $X_t$ frente a $X_{t-1}$. A diferencia de los ejemplos 1, 3 y 4, todo está calculado con fórmulas vivas. Se aprende a reconocer en el correlograma la firma de una **tendencia**: coeficientes muy altos que bajan despacio.

### Hoja `DATOS`

**Datos de entrada:** 1.923 días consecutivos en orden descendente, del 2019-08-30 (fila 2) al 2014-05-26 (fila 1924). CSV completo: [`DATOS.csv`](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-2-datos/DATOS.csv).

| Columna | n | Mínimo | Máximo | Media | Mediana | Desv. estándar | Comportamiento (calculado) |
|---|---|---|---|---|---|---|---|
| B `Ventas prod 1` | 1.923 | 934 | 2.052 | 1.497,55 | 1.498 | 281,69 | Tendencia decreciente casi lineal: media anual 1.925,8 (2014), 1.775,0 (2015), 1.592,7 (2016), 1.413,2 (2017), 1.230,4 (2018), 1.076,0 (2019); pendiente ≈ −0,50 unidades/día. |
| C `Ventas Prod 2` | 1.923 | −30 | 1.086 | 531,97 | 532 | 282,89 | Tendencia creciente: 103,0 (2014) → 953,0 (2019); pendiente ≈ +0,50 unidades/día. Tiene 4 valores negativos (−22, −7, −4 y −30 entre el 2014-05-27 y el 2014-06-02). |
| D `Ventas Prod 3` | 1.923 | 800 | 2.952 | 1.244,86 | 1.064 | 496,32 | Plana en ≈ 1.000 de 2014 a marzo de 2018; desde el segundo trimestre de 2018 crece con fuerza (media trimestral 1.185 → 1.514 → 1.811 → 2.114 → 2.418 → 2.700 en el tercer trimestre de 2019). |

Hallazgo propio: los productos 1 y 2 son casi espejo (correlación −0,97); su suma se mantiene alrededor de 2.030 (desviación 69).

**Gráfico:** líneas con las tres series (`B2:D1924`), en el orden de la hoja (del día más reciente al más antiguo, así que visualmente las tendencias aparecen invertidas).

### Hoja `DATOS ACF` — función de autocorrelación del producto 1

**Parámetros**

| Celda | Concepto | Fórmula | Valor |
|---|---|---|---|
| B26 | Observaciones $n$ | `=COUNT(DATOS!B2:B1924)` | 1.923 |
| B27 | Media $\bar x$ | `=AVERAGE(DATOS!B2:B1924)` | 1.497,55 |
| B28 | Suma de cuadrados $\sum(x_t-\bar x)^2$ | `=DEVSQ(DATOS!B2:B1924)` | 1,52512 × 10⁸ |
| B29 | Nivel de significancia ($z$, 5 %) | valor fijo | 1,96 |

**Método paso a paso**

1. **Autocorrelación** (columna B, filas 32–119, rezagos $k=1$ a 88), fórmula matricial
   `=SUMPRODUCT((OFFSET(DATOS!$B$2,0,0,$B$26-$A32,1)-$B$27)*(OFFSET(DATOS!$B$2,$A32,0,$B$26-$A32,1)-$B$27))/$B$28`, que es exactamente la fórmula de la L04:
   $$r_k=\frac{\sum_{t=1}^{n-k}(x_t-\bar x)(x_{t+k}-\bar x)}{\sum_{t=1}^{n}(x_t-\bar x)^2}.$$
2. **Límite superior** (columna C): `=$B$29*SQRT((1+2*(SUMSQ($B$32:$B32)-$B32^2))/$B$26)`, es decir
   $$L_k=1{,}96\sqrt{\frac{1+2\sum_{i=1}^{k-1}r_i^2}{n}}$$
   (la suma de cuadrados hasta $k$ menos $r_k^2$ deja solo los rezagos anteriores). **Límite inferior** (columna D): $-L_k$. Usa $z=1{,}96$ en vez del $t$ de Student de la L04; con $n=1.923$ son prácticamente iguales (1,9612).
3. **Matriz de correlaciones** (filas 1–22, rezagos 0 a 20): fórmulas matriciales `=IF($A2-(COLUMNS($B2:B2)-1)<0,"",IF(...=0,1,INDEX($B$32:$B$119,...)))` que reconstruyen, a partir de la columna B de abajo, una matriz triangular con el mismo formato que la salida de *Análisis de datos → Correlación* (1 en la diagonal y $r_{|i-j|}$ fuera de ella). Es solo presentación.

**Resultados (selección; los 88 valores están en el anexo y en [`DATOS_ACF.csv`](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-2-datos/DATOS_ACF.csv))**

| Rezago | $r_k$ | Límite ± | Rezago | $r_k$ | Límite ± |
|---|---|---|---|---|---|
| 1 | 0,9661 | 0,0447 | 20 | 0,9377 | 0,2664 |
| 2 | 0,9654 | 0,0757 | 30 | 0,9214 | 0,3249 |
| 3 | 0,9633 | 0,0972 | 40 | 0,9070 | 0,3729 |
| 4 | 0,9623 | 0,1147 | 50 | 0,8921 | 0,4141 |
| 5 | 0,9599 | 0,1298 | 60 | 0,8775 | 0,4503 |
| 7 | 0,9592 | 0,1556 | 70 | 0,8631 | 0,4827 |
| 10 | 0,9545 | 0,1876 | 80 | 0,8477 | 0,5121 |
| 15 | 0,9459 | 0,2307 | 88 | 0,8339 | 0,5338 |

**Gráfico `GRAFICO ACF`:** «Función de autocorrelación para Ventas prod 1» (estilo Minitab; ejes «Desfase» y «Autocorrelación»): barras de $r_k$ para los rezagos 1–88 con las líneas de límite superior e inferior que se abren poco a poco. Todas las barras quedan muy por encima del límite y descienden lentamente de 0,97 a 0,83.

### Hoja `DATOS HISTOGRAMA`

**Parámetros:** $n=1.923$ (`B3`), mínimo 934 (`B4`), máximo 2.052 (`B5`), número de clases $k=40$ (`B6`, valor fijo) y ancho de clase $w=(\max-\min)/k=27{,}95$ (`B7`).

**Método:** clase $i$ con límite inferior $L_i=\min+(i-1)w$ (`B10`), superior $U_i=\min+i\,w$ (`C10`) y marca de clase $(L_i+U_i)/2$ (`D10`). Frecuencia con `COUNTIFS`: la clase 1 cuenta $L_1\le x\le U_1$ y las demás $L_i<x\le U_i$. Control: `B52 = SUM(E10:E49)` = 1.923.

**Resultados**

| Clase | Límites | Frec. | Clase | Límites | Frec. |
|---|---|---|---|---|---|
| 1 | 934 – 961,95 | 7 | 21 | 1.493 – 1.520,95 | 56 |
| 2 | 961,95 – 989,9 | 13 | 22 | 1.520,95 – 1.548,9 | 53 |
| 3 | 989,9 – 1.017,85 | 28 | 23 | 1.548,9 – 1.576,85 | 57 |
| 4 | 1.017,85 – 1.045,8 | 24 | 24 | 1.576,85 – 1.604,8 | 57 |
| 5 | 1.045,8 – 1.073,75 | 44 | 25 | 1.604,8 – 1.632,75 | 60 |
| 6 | 1.073,75 – 1.101,7 | 53 | 26 | 1.632,75 – 1.660,7 | 58 |
| 7 | 1.101,7 – 1.129,65 | 59 | 27 | 1.660,7 – 1.688,65 | 62 |
| 8 | 1.129,65 – 1.157,6 | 55 | 28 | 1.688,65 – 1.716,6 | 56 |
| 9 | 1.157,6 – 1.185,55 | 48 | 29 | 1.716,6 – 1.744,55 | 49 |
| 10 | 1.185,55 – 1.213,5 | 63 | 30 | 1.744,55 – 1.772,5 | 48 |
| 11 | 1.213,5 – 1.241,45 | 59 | 31 | 1.772,5 – 1.800,45 | 68 |
| 12 | 1.241,45 – 1.269,4 | 51 | 32 | 1.800,45 – 1.828,4 | 54 |
| 13 | 1.269,4 – 1.297,35 | 53 | 33 | 1.828,4 – 1.856,35 | 51 |
| 14 | 1.297,35 – 1.325,3 | 53 | 34 | 1.856,35 – 1.884,3 | 51 |
| 15 | 1.325,3 – 1.353,25 | 58 | 35 | 1.884,3 – 1.912,25 | 59 |
| 16 | 1.353,25 – 1.381,2 | 61 | 36 | 1.912,25 – 1.940,2 | 51 |
| 17 | 1.381,2 – 1.409,15 | 56 | 37 | 1.940,2 – 1.968,15 | 32 |
| 18 | 1.409,15 – 1.437,1 | 62 | 38 | 1.968,15 – 1.996,1 | 22 |
| 19 | 1.437,1 – 1.465,05 | 47 | 39 | 1.996,1 – 2.024,05 | 19 |
| 20 | 1.465,05 – 1.493 | 56 | 40 | 2.024,05 – 2.052 | 10 |

**Gráfico `GRAFICO HISTOGRAMA`:** columnas de frecuencia (`E10:E49`) sobre las marcas de clase (`D10:D49`), ejes «Ventas prod 1» y «Frecuencia». Forma casi plana entre ≈ 1.050 y ≈ 1.940 con colas cortas a ambos lados: es lo que produce una rampa lineal con ruido, no una campana.

### Hoja `DATOS BOX PLOT`

| Concepto | Fórmula | Valor |
|---|---|---|
| Observaciones | `COUNT` | 1.923 |
| Mínimo | `MIN` | 934 |
| Primer cuartil $Q_1$ | `QUARTILE.INC(…,1)` | 1.258,5 |
| Mediana $Q_2$ | `MEDIAN` | 1.498 |
| Tercer cuartil $Q_3$ | `QUARTILE.INC(…,3)` | 1.736,5 |
| Máximo | `MAX` | 2.052 |
| Rango intercuartílico $RIQ=Q_3-Q_1$ | `=B7-B5` | 478 |
| «Bigote inferior» $Q_1-1{,}5\,RIQ$ | `=B5-1.5*B9` | 541,5 |
| «Bigote superior» $Q_3+1{,}5\,RIQ$ | `=B7+1.5*B9` | 2.453,5 |

Como el mínimo (934) y el máximo (2.052) caen dentro de [541,5; 2.453,5], **no hay datos atípicos**. Gráfico `GRAFICO BOX PLOT`: caja y bigotes nativo de Excel sobre `DATOS!B2:B1924` (cuartiles exclusivos, marca de la media).

### Hoja `DISPERSION`

**Método:** columna A = venta del día anterior (`=DATOS!B3`, … ; como las fechas van en orden descendente, la fila siguiente es el día anterior) y columna B = venta del día (`=DATOS!B2`, …), 1.922 pares. Estadísticos de la regresión $X_t=a+b\,X_{t-1}$:

| Celda | Concepto | Fórmula | Valor |
|---|---|---|---|
| E2 | Correlación $r$ | `=CORREL(A2:A1923,B2:B1923)` | 0,96777 |
| E3 | $r^2$ | `=RSQ(B2:B1923,A2:A1923)` | 0,936579 |
| E4 | Pendiente $b$ | `=SLOPE(B2:B1923,A2:A1923)` | 0,967734 |
| E5 | Intercepto $a$ | `=INTERCEPT(B2:B1923,A2:A1923)` | 47,7904 |
| E6 | Pares de datos | `=COUNT(A2:A1923)` | 1.922 |

$$\hat X_t=47{,}79+0{,}9677\,X_{t-1},\qquad R^2=0{,}9366$$

**Gráfico `GRAFICO DISPERSION`:** «Gráfica de dispersión de Ventas prod 1 vs. periodo anterior», X = periodo anterior, Y = periodo actual: nube estrecha a lo largo de la diagonal. En el título del eje X el estudiante escribió: «LINEA TENDENCIA AZUL ESTA SE BASA EN SI LAS VENTAS DE HOY SE PUEDEN REDECIR MAÑANA SI SE ACERA A LA LINE».

### Hoja `GRAFICO DE SERIES DE TIEMPO `

«Gráfica de series de tiempo de Ventas prod 1», ejes «Índice» y «Ventas prod 1». Solo grafica `DATOS!B2:B251`: los 250 días más recientes (del 2019-08-30 hacia atrás hasta el 2018-12-24), no la serie completa.

### Conclusión

- El producto 1 tiene una **tendencia** clara (decreciente en el tiempo): $r_1=0{,}966$ y los coeficientes bajan muy despacio (0,834 en el rezago 88), siempre muy por encima de los límites. Es el patrón «Trendline» de la p. 16 de la L04.
- El diagrama de dispersión lo confirma: la venta de ayer explica el 93,7 % de la variación de la de hoy.
- El histograma plano y el boxplot sin atípicos describen una rampa, no un ruido alrededor de una media: **no** sirven los métodos para datos estacionarios; hay que usar un método con tendencia, como la [suavización doble de Holt](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/).
- Los productos 2 (tendencia creciente) y 3 (cambio de nivel en 2018) solo se grafican; no se analizan.

### Observaciones

- Las hojas de cálculo están completas y con fórmulas vivas; las hojas de gráfico dependen de ellas.
- El resumen del boxplot usa `QUARTILE.INC`, pero el gráfico nativo usa el método exclusivo; los cuartiles pueden diferir un poco.
- Las celdas `B10`/`B11` del boxplot se llaman «Bigote», pero son las vallas de Tukey ($Q_1-1{,}5\,RIQ$ y $Q_3+1{,}5\,RIQ$), no el extremo del bigote.
- El producto 2 tiene ventas negativas (mínimo −30), probablemente devoluciones o errores de registro.
- La serie de tiempo del producto 1 solo muestra 250 días, lo que oculta la tendencia de largo plazo.


---

<!-- fuente: corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-3.md -->
# tarea-class-example-3

> **Archivo:** [`tarea-class-example-3.xlsx`](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-3.xlsx) · **Corte 1** · Libro de Excel con 7 hoja(s): `Ventas`, `Coeficientes de correlacion`, `Serie de tiempo de Ventas`, `Histograma de ventas`, `Boxplot de ventas`, `Autocorrelograma de ventas`, `Scatterplot de ventas`  
> **Nombre original:** `CORTE 1/TAREAS/PRONOSCITOS DE DEMANDAS/Class example 3.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Tercer libro de la tarea «Pronósticos de demandas» (nombre original `TAREAS/PRONOSCITOS DE DEMANDAS/Class example 3.xlsx`), con la misma plantilla que el ejemplo 1 y basado en la [Lección 4 — Plotting your data](/corte-1-pronosticos/03-graficas-y-autocorrelacion/L04-plotting-your-data.md): tabla de 20 rezagos, coeficientes con límites de significancia, serie de tiempo, histograma, boxplot, autocorrelograma y dispersión $X_t$ frente a $X_{t-1}$. La serie tiene una **tendencia creciente** muy marcada, así que el ejemplo muestra cómo se ve la tendencia en cada gráfico. Ojo: los coeficientes de la hoja están mal calculados (ver Observaciones).

### Hoja `Ventas`

**Datos de entrada**

- Columna A `Dato`: índice del periodo, de 2 a 302 (coincide con el número de fila).
- Columna B `Ventas`: 301 datos (filas 2–302).
- Columnas C–V `Rezago 1` … `Rezago 20`: la columna B desplazada $k$ filas hacia abajo (valores pegados).
- Nombre definido `DATOS` = `Ventas!A22:V302` (incluye la columna A).
- CSV completo: [`Ventas.csv`](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-3-datos/Ventas.csv).

**Estadísticos (calculados):** $n=301$; mínimo 1; máximo 315 (en el dato 272); media 151,45; mediana 153; desviación estándar 88,05; cuartiles (método exclusivo) $Q_1=88{,}5$, $Q_3=227$. Primeros valores: 1, 6, 7, 5, 10, 11, 9, 12, 9, 13, 11, 14, 18, 14, 19, 20, 20, 19, 26, 25, 28, 29… Recta de regresión sobre el índice (cálculo propio): pendiente ≈ 0,98 por periodo.

Media por bloques de 25 datos (cálculo propio), que muestra la tendencia con algunos tramos planos o de retroceso:

| Datos | Media | Mín. | Máx. |
|---|---|---|---|
| 2–26 | 16,2 | 1 | 29 |
| 27–51 | 35,0 | 27 | 43 |
| 52–76 | 65,9 | 42 | 90 |
| 77–101 | 94,8 | 89 | 100 |
| 102–126 | 100,8 | 87 | 124 |
| 127–151 | 156,9 | 133 | 170 |
| 152–176 | 150,3 | 140 | 162 |
| 177–201 | 191,5 | 153 | 232 |
| 202–226 | 229,0 | 206 | 243 |
| 227–251 | 210,4 | 193 | 249 |
| 252–276 | 296,2 | 257 | 315 |
| 277–301 | 266,3 | 246 | 301 |
| 302 | 253 | 253 | 253 |

### Hoja `Coeficientes de correlacion`

**Método (tal como está en el archivo)**

1. Columna B (`Columna 1`, filas 3–23, etiquetadas `REZAGOS` 1 a 21): valores pegados de *Análisis de datos → Correlación* aplicada al rango `DATOS` = `Ventas!A22:V302`. Como ese rango empieza en la columna A (`Dato`), la primera columna de la matriz es el **índice del periodo** y no las ventas. Se comprobó que la fila «1» es $\operatorname{corr}(\text{Dato},\text{Ventas})$ y la fila «$k+1$» es $\operatorname{corr}(\text{Dato},\text{Rezago }k)$.
2. Límites (columnas C y D), con $n=$ `COUNT(Ventas!B2:B302)` $=301$ y $t=$ `TINV(0.05; 300)` $=1{,}9679$:
   - fila 3: $\pm t/\sqrt n=\pm0{,}113428$;
   - fila $j\ge4$: $\pm t\sqrt{\left(1+2\sum r_i^2\right)/n}$ con la suma de los valores de la columna B de las filas anteriores (`SUMSQ($B$3:B(j-1))`).

**Resultados que muestra la hoja**

| Fila (rezago) | Columna 1 | Límite ± | Fila (rezago) | Columna 1 | Límite ± |
|---|---|---|---|---|---|
| 1 | 0,964075 | 0,113428 | 12 | 0,972500 | 0,527341 |
| 2 | 0,964832 | 0,191787 | 13 | 0,972995 | 0,549931 |
| 3 | 0,965643 | 0,246447 | 14 | 0,973475 | 0,571651 |
| 4 | 0,966384 | 0,291084 | 15 | 0,973907 | 0,592596 |
| 5 | 0,967124 | 0,329789 | 16 | 0,974208 | 0,612843 |
| 6 | 0,967983 | 0,364457 | 17 | 0,974412 | 0,632454 |
| 7 | 0,968851 | 0,396156 | 18 | 0,974597 | 0,651483 |
| 8 | 0,969577 | 0,425550 | 19 | 0,974669 | 0,669978 |
| 9 | 0,970398 | 0,453082 | 20 | 0,974753 | 0,687979 |
| 10 | 0,971160 | 0,479076 | 21 | 0,974810 | 0,705524 |
| 11 | 0,971885 | 0,503769 | | | |

**Autocorrelación correcta (cálculo propio, no está en el archivo)**

| Rezago $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| $r_k$ (fórmula de la L04) | 0,9921 | 0,9845 | 0,9763 | 0,9673 | 0,9584 | 0,9489 | 0,9386 | 0,9282 | 0,9172 | 0,9058 |
| Pearson ventas–rezago (filas 22–302) | 0,9992 | 0,9981 | 0,9966 | 0,9944 | 0,9917 | 0,9884 | 0,9846 | 0,9804 | 0,9758 | 0,9707 |

| Rezago $k$ | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| $r_k$ (fórmula de la L04) | 0,8938 | 0,8814 | 0,8691 | 0,8562 | 0,8433 | 0,8300 | 0,8164 | 0,8026 | 0,7892 | 0,7756 |
| Pearson ventas–rezago (filas 22–302) | 0,9654 | 0,9597 | 0,9540 | 0,9481 | 0,9422 | 0,9362 | 0,9302 | 0,9244 | 0,9187 | 0,9133 |

### Hojas de gráficos

| Hoja | Tipo | Qué muestra |
|---|---|---|
| `Serie de tiempo de Ventas` | Líneas, `Ventas!B2:B302` | Serie que sube de ≈ 1 a ≈ 300 con escalones y retrocesos (tramos planos en 77–126 y 152–176, caídas en 227–251 y al final). |
| `Histograma de ventas` | Histograma nativo de Excel sobre `B2:B302` | Distribución extendida de 1 a 315, sin una moda clara: refleja la rampa, no un ruido alrededor de una media. |
| `Boxplot de ventas` | Caja y bigotes nativo (cuartiles exclusivos, marca de la media) | Caja de 88,5 a 227 con mediana 153 y bigotes de 1 a 315; sin atípicos. |
| `Autocorrelograma de ventas` | Barras (`B3:B23`) + límites (`C3:D23`) | 21 barras ≈ 0,96–0,97 muy por encima de los límites, que crecen de 0,11 a 0,71. |
| `Scatterplot de ventas` | Dispersión, X = ventas (`B2:B322`), Y = rezago 1 (`C2:C322`) | «X(t) vs X(t-1)»: puntos alineados en una diagonal casi perfecta. |

### Conclusión

- La serie tiene una **tendencia creciente** fuerte: el autocorrelograma correcto empieza en 0,992 y baja despacio hasta 0,776 en el rezago 20, siempre muy por encima de los límites (patrón «Trendline» de la L04, p. 16), y la dispersión $X_t$–$X_{t-1}$ es casi una recta.
- La conclusión de la hoja (todos los coeficientes significativos → hay tendencia) es correcta aunque los números estén mal calculados.
- Para pronosticarla no sirven los métodos estacionarios; corresponde un método con tendencia, como [Holt](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/).

### Observaciones

- **Error en los coeficientes:** la correlación se calculó sobre `A22:V302`, que incluye la columna `Dato`; la columna B de la hoja es la correlación del índice del periodo con las ventas y sus rezagos, no la autocorrelación. Por eso los valores *suben* con el rezago (0,964 → 0,975), algo imposible en un correlograma de tendencia. Además hay 21 filas: la etiqueta «1» corresponde en realidad al rezago 0 (ventas) y la etiqueta «$k+1$» al rezago $k$.
- En consecuencia, los límites de las filas 4–23 también están inflados (se calcularon con esos coeficientes).
- El gráfico de dispersión toma hasta la fila 322 aunque las ventas terminan en la 302.
- Los coeficientes son valores pegados; no se recalculan.


---

<!-- fuente: corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-4.md -->
# tarea-class-example-4

> **Archivo:** [`tarea-class-example-4.xlsx`](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-4.xlsx) · **Corte 1** · Libro de Excel con 7 hoja(s): `Datos`, `Coeficientes `, `Serie de tiempo de los datos`, `Histograma de los datos`, `Autocorrelograma de los datos`, `Boxplot de los datos`, `Scatterplot de los datos`  
> **Nombre original:** `CORTE 1/TAREAS/PRONOSCITOS DE DEMANDAS/Class example 4.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Cuarto libro de la tarea «Pronósticos de demandas» (nombre original `TAREAS/PRONOSCITOS DE DEMANDAS/Class example 4.xlsx`), con la misma plantilla que el ejemplo 1 y basado en la [Lección 4 — Plotting your data](/corte-1-pronosticos/03-graficas-y-autocorrelacion/L04-plotting-your-data.md). La serie **alterna** un valor alto y uno bajo en cada periodo, de modo que el ejemplo enseña cómo se ve en el correlograma un patrón periódico (estacionalidad de periodo 2): coeficientes grandes que cambian de signo en cada rezago y no se apagan.

### Hoja `Datos`

**Datos de entrada**

- Columna A `dato`: índice del periodo, de 1 a 500.
- Columna B `DATO`: 500 valores (filas 2–501).
- Columnas C–V `Rezago 1` … `Rezago 20`: la columna B desplazada $k$ filas hacia abajo (valores pegados; terminan en la fila 521).
- CSV completo: [`Datos.csv`](/corte-1-pronosticos/03-graficas-y-autocorrelacion/tarea-class-example-4-datos/Datos.csv).

**Estadísticos (calculados):** $n=500$; mínimo 3.895; máximo 3.918; media 3.906,98; mediana 3.907; desviación estándar 5,61; cuartiles (método exclusivo) $Q_1=3.902$, $Q_3=3.912$. Primeros valores: 3.904, 3.914, 3.904, 3.916, 3.901, 3.911, 3.904, 3.912, 3.902, 3.908, …

**Patrón (cálculo propio):** los datos en posición impar (1.º, 3.º, …) promedian 3.901,8 (rango 3.895–3.907) y los de posición par 3.912,1 (rango 3.907–3.918). En los 250 pares, el dato par siempre es mayor que el impar anterior, y el signo de la diferencia $X_t-X_{t-1}$ cambia en el 100 % de los periodos: la serie es un zigzag perfecto. No hay tendencia: la media de los primeros 250 datos es 3.906,84 y la de los últimos 250, 3.907,12 (pendiente ≈ 0,0013 por periodo).

Distribución de valores:

| Valor | 3.895 | 3.896 | 3.897 | 3.898 | 3.899 | 3.900 | 3.901 | 3.902 | 3.903 | 3.904 | 3.905 | 3.906 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Frecuencia | 1 | 2 | 4 | 8 | 24 | 30 | 41 | 45 | 36 | 31 | 16 | 10 |

| Valor | 3.907 | 3.908 | 3.909 | 3.910 | 3.911 | 3.912 | 3.913 | 3.914 | 3.915 | 3.916 | 3.917 | 3.918 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Frecuencia | 3 | 6 | 21 | 28 | 47 | 33 | 49 | 34 | 16 | 11 | 1 | 3 |

### Hoja `Coeficientes `

**Método**

1. Columna B (`Columna 1`, filas 3–22): valores pegados de *Análisis de datos → Correlación*. Se comprobó que coinciden con la correlación de Pearson entre `DATO` y cada `Rezago k` sobre las filas 22–501 (480 filas completas):
   $$r_k\approx\operatorname{corr}(X_t,\,X_{t-k}).$$
2. Límites (columnas C y D), con $n=$ `COUNT(Datos!B2:B501)` $=500$ y $t=$ `TINV(0.05; 499)` $=1{,}9647$:
   - rezago 1: $\pm t/\sqrt n=\pm0{,}0878654$;
   - rezago $k\ge2$: $\pm t\sqrt{\left(1+2\sum_{i=1}^{k-1}r_i^2\right)/n}$ (`SUMSQ($B$3:B(k+1))`), fórmula de la p. 13 de la L04, bien implementada.

**Resultados**

| Rezago $k$ | $r_k$ | Límite ± | $r_k$ con la fórmula de la L04 (cálculo propio) |
|---|---|---|---|
| 1 | −0,848281 | 0,087865 | −0,8451 |
| 2 | 0,850925 | 0,137226 | 0,8459 |
| 3 | −0,855568 | 0,173238 | −0,8489 |
| 4 | 0,852494 | 0,203258 | 0,8429 |
| 5 | −0,852179 | 0,229206 | −0,8422 |
| 6 | 0,852084 | 0,252484 | 0,8394 |
| 7 | −0,850560 | 0,273786 | −0,8381 |
| 8 | 0,847797 | 0,293478 | 0,8331 |
| 9 | −0,861220 | 0,311814 | −0,8444 |
| 10 | 0,846456 | 0,329666 | 0,8319 |
| 11 | −0,850312 | 0,346039 | −0,8336 |
| 12 | 0,836787 | 0,361811 | 0,8198 |
| 13 | −0,855348 | 0,376456 | −0,8349 |
| 14 | 0,852107 | 0,391172 | 0,8307 |
| 15 | −0,859963 | 0,405249 | −0,8380 |
| 16 | 0,854492 | 0,419101 | 0,8289 |
| 17 | −0,852548 | 0,432342 | −0,8278 |
| 18 | 0,861264 | 0,445132 | 0,8329 |
| 19 | −0,847809 | 0,457817 | −0,8169 |
| 20 | 0,849091 | 0,469781 | 0,8159 |

### Hojas de gráficos

| Hoja | Tipo | Qué muestra |
|---|---|---|
| `Serie de tiempo de los datos` | Líneas, `Datos!B2:B501` | Zigzag constante entre ≈ 3.900 y ≈ 3.913 alrededor de 3.907, sin tendencia. |
| `Histograma de los datos` | Histograma nativo de Excel sobre `B2:B501` | Distribución **bimodal**: un grupo alrededor de 3.901–3.902 (datos impares) y otro alrededor de 3.911–3.913 (datos pares), con un valle en 3.906–3.908. |
| `Autocorrelograma de los datos` | Barras (`B3:B22`) + límites (`C3:D22`) | Barras de ±0,85 que alternan signo (negativas en rezagos impares, positivas en pares), todas fuera de los límites. |
| `Boxplot de los datos` | Caja y bigotes nativo sobre `B2:B501` (cuartiles exclusivos) | Caja de 3.902 a 3.912, mediana 3.907, bigotes 3.895–3.918; sin atípicos. |
| `Scatterplot de los datos` | Dispersión, X = dato (`B2:B1944`), Y = rezago 1 (`C2:C1944`) | «X(t) vs X(t-1)»: dos nubes separadas (alto–bajo y bajo–alto) que forman una relación negativa. |

### Conclusión

- Todos los coeficientes son significativos, grandes (|r| ≈ 0,85) y **alternan de signo sin decaer**: la serie tiene un patrón periódico de longitud 2 (un periodo alto, uno bajo), es decir, **estacionalidad** de periodo 2 (patrón «Seasonality» de la L04, p. 16), sin tendencia.
- Un promedio móvil o una suavización simple promediarían el zigzag y fallarían en cada periodo; corresponde un método con estacionalidad, como [Winters](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/), con longitud de estación 2.

### Observaciones

- El libro conserva restos de la plantilla del ejemplo 1: los nombres definidos `DATOS`, `DATOS1` y varios `_xlchart.v1.*` apuntan a `#REF!`, `DATOS2` apunta a `Datos!C22:V1924` y el gráfico de dispersión toma hasta la fila 1944 aunque los datos terminan en la 501 (o la 502 para el rezago 1). No afecta a los resultados.
- `DATOS3` = `Datos!B22:V501` es el rango usado para la matriz de correlación (deducido: coincide con los coeficientes).
- Los coeficientes son valores pegados; no se recalculan.
