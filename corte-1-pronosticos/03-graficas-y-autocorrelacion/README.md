# Gráficas de los datos y autocorrelación (Corte 1)

## Qué cubre
Antes de elegir un método de pronóstico hay que **graficar y entender los datos**. Esta carpeta enseña a usar el histograma, la serie de tiempo, el boxplot, el diagrama de dispersión $X_t$ frente a $X_{t-1}$ y, sobre todo, el **correlograma** (coeficientes de autocorrelación por rezago con límites de significancia) para reconocer si una serie es aleatoria, tiene tendencia o tiene estacionalidad. Incluye también la prueba de Ljung-Box y una introducción al análisis de componentes principales (PCA) para agrupar tiendas o productos con comportamiento parecido. Los Excel son una hoja de clase con 30.000 ventas y la tarea «Pronósticos de demandas»: cuatro ejemplos con patrones distintos (series aleatorias, dos series con tendencia y una con estacionalidad de periodo 2).

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [L04-plotting-your-data.md](./L04-plotting-your-data.md) | Lecture 4 «Plotting your data» (31 diapositivas): tipos de gráfico, fórmula de $r_k$, ejemplo numérico de autocorrelación, límites de significancia, lectura del correlograma, Ljung-Box, Minitab/Tableau y PCA de 15 tiendas. | **Sí** |
| [graficas-pronosticos-ventas-autocorrelacion.md](./graficas-pronosticos-ventas-autocorrelacion.md) | Excel de clase: 30.000 ventas (0–22, media 8) con 20 rezagos, matriz de correlación, autocorrelograma, serie y dispersión. Serie aleatoria. | Segundo |
| [tarea-class-example-1.md](./tarea-class-example-1.md) | Tarea, ejemplo 1: ventas propias y de la competencia (1.923 días, 2014–2019) con rezagos, coeficientes con límites, histograma, boxplot (atípicos 31.624, 12, 9 y 2) y dispersión. Series aleatorias. | Tercero |
| [tarea-class-example-2.md](./tarea-class-example-2.md) | Tarea, ejemplo 2: tres productos; análisis completo del producto 1 con fórmulas vivas (ACF hasta el rezago 88, histograma de 40 clases, boxplot, regresión $X_t$–$X_{t-1}$). Serie con tendencia. | Cuarto (el más completo) |
| [tarea-class-example-3.md](./tarea-class-example-3.md) | Tarea, ejemplo 3: 301 datos con tendencia creciente. Los coeficientes de la hoja están mal calculados (incluyen la columna índice); el .md trae los correctos. | Quinto |
| [tarea-class-example-4.md](./tarea-class-example-4.md) | Tarea, ejemplo 4: 500 datos que alternan alto/bajo (zigzag); coeficientes ±0,85 que cambian de signo → estacionalidad de periodo 2. | Sexto |

Cada Excel tiene, además, una carpeta `*-datos/` con el CSV completo de sus hojas largas: [graficas-pronosticos-ventas-autocorrelacion-datos/DATOS.csv](./graficas-pronosticos-ventas-autocorrelacion-datos/DATOS.csv), [tarea-class-example-1-datos/](./tarea-class-example-1-datos/) (`Ventas_propias.csv`, `Ventas_competencia.csv`), [tarea-class-example-2-datos/](./tarea-class-example-2-datos/) (`DATOS.csv`, `DATOS_ACF.csv`, `DISPERSION.csv`), [tarea-class-example-3-datos/Ventas.csv](./tarea-class-example-3-datos/Ventas.csv) y [tarea-class-example-4-datos/Datos.csv](./tarea-class-example-4-datos/Datos.csv).

## Orden de estudio sugerido
1. [L04](./L04-plotting-your-data.md), p. 1–5: para qué graficar y qué gráficos usar.
2. L04, p. 6–14: fórmula de $r_k$, ejemplo de 6 datos y límites de significancia.
3. L04, p. 15–18: cómo leer el correlograma (tendencia, estacionalidad, aleatoriedad) y la prueba de Ljung-Box.
4. [graficas-pronosticos-ventas-autocorrelacion](./graficas-pronosticos-ventas-autocorrelacion.md): cómo armar la tabla de rezagos y la matriz de correlación en Excel; ejemplo de serie aleatoria.
5. Los cuatro ejemplos de la tarea, comparando su correlograma: [1](./tarea-class-example-1.md) (aleatoria, con atípicos), [2](./tarea-class-example-2.md) (tendencia, todo con fórmulas), [3](./tarea-class-example-3.md) (tendencia, con un error instructivo) y [4](./tarea-class-example-4.md) (estacionalidad de periodo 2).
6. L04, p. 19–31: software y PCA.
7. Siguiente tema: [04 — datos estacionarios](../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/README.md).

## Conceptos y fórmulas clave
Detalle en [L04](./L04-plotting-your-data.md).

- **Coeficiente de autocorrelación del rezago $k$:**
  $$r_k=\frac{\sum_{i=1}^{N-k}(x_i-\bar{x})(x_{i+k}-\bar{x})}{\sum_{i=1}^{N}(x_i-\bar{x})^2}$$
  $x_i$: dato del periodo $i$; $\bar x$: media; $N$: número de datos; $k$: rezago. En Excel se aproxima con la correlación de Pearson entre la serie y la columna desplazada $k$ filas (herramienta *Análisis de datos → Correlación*) o se calcula exacto con `SUMPRODUCT`/`OFFSET` ([ejemplo 2](./tarea-class-example-2.md)).
- **Límites de significancia:**
  $$\pm\,t\cdot SE(r_k),\qquad SE(r_1)\approx\frac{1}{\sqrt n},\qquad SE(r_k)=\sqrt{\frac{1+2\sum_{i=1}^{k-1}r_i^2}{n}}$$
  $t$: t de Student al 5 % (dos colas) con $n-1$ grados de libertad (`TINV(0.05; n-1)`; con $n$ grande ≈ 1,96). Si $|r_k|$ sale de la banda, el rezago $k$ es significativo.
- **Lectura del correlograma** (L04, p. 16):

  | Patrón | Cómo se ve | Ejemplo en esta carpeta |
  |---|---|---|
  | Aleatoriedad | $r_k$ casi todos cerca de 0, dentro de los límites | [graficas…](./graficas-pronosticos-ventas-autocorrelacion.md), [ejemplo 1](./tarea-class-example-1.md) |
  | Tendencia | $r_k$ altos en los primeros rezagos que bajan despacio | [ejemplo 2](./tarea-class-example-2.md) ($r_1=0{,}966$ → $r_{88}=0{,}834$), [ejemplo 3](./tarea-class-example-3.md) |
  | Estacionalidad | $r_k$ significativo en el rezago de la estación | [ejemplo 4](./tarea-class-example-4.md) (±0,85 alternando: periodo 2) |

- **Prueba de Ljung-Box:**
  $$Q=n(n+2)\sum_{k=1}^{h}\frac{r_k^2}{n-k}$$
  $h$: número de rezagos. $H_0$: datos independientes. Si $Q>\chi^2_{\alpha,h}$ se rechaza $H_0$ (datos correlacionados).
- **Boxplot:** caja de $Q_1$ a $Q_3$; atípicos fuera de $[Q_1-1{,}5\,RIQ,\ Q_3+1{,}5\,RIQ]$ con $RIQ=Q_3-Q_1$.
- **PCA:** reduce muchas variables (periodos) a pocas componentes; la proporción de información de la componente $j$ es $\lambda_j/\sum\lambda$ (valores propios de la matriz de correlación). Sirve para agrupar tiendas o productos y definir una estrategia de pronóstico por grupo.

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado principal |
|---|---|---|
| $r_1$, $r_2$, $r_3$ de la serie −0,36; −0,52; 0,46; −0,31; −2,05; 0,28 | [L04](./L04-plotting-your-data.md), p. 8–12 | $r_1=-0{,}33$; $r_2=-0{,}33$; $r_3=0{,}1988$ |
| Límites de significancia del mismo ejemplo ($n=6$) | L04, p. 13–14 | ±1,05; ±1,16; ±1,26 → ninguno significativo («Not enough data!») |
| Ljung-Box del mismo ejemplo | L04, p. 18 | $Q=2{,}9846<\chi^2=7{,}81$ → sin evidencia de correlación |
| PCA de 15 tiendas × 13 periodos | L04, p. 22–31 | 2 componentes = 75,8 % de la información; tiendas parecidas {9, 12}, {1, 5}, {2, 7} |
| Autocorrelograma de 30.000 ventas | [graficas-pronosticos-ventas-autocorrelacion](./graficas-pronosticos-ventas-autocorrelacion.md) | $\lvert r_k\rvert<0{,}013$ en los 20 rezagos → serie aleatoria |
| Ventas propias y competencia (1.923 días) | [tarea-class-example-1](./tarea-class-example-1.md) | Límites ±0,0447; series aleatorias (solo el rezago 4 de competencia, −0,0459, roza el límite); atípicos 31.624, 12, 9 y 2; propias + competencia ≈ 2.960 constante |
| Producto 1 (1.923 días) | [tarea-class-example-2](./tarea-class-example-2.md) | ACF 0,966 → 0,834 (rezagos 1–88), todos significativos; sin atípicos; $\hat X_t=47{,}79+0{,}9677X_{t-1}$, $R^2=0{,}937$ → tendencia |
| Serie de 301 datos | [tarea-class-example-3](./tarea-class-example-3.md) | ACF correcta 0,992 → 0,776 (rezagos 1–20) → tendencia creciente |
| Serie de 500 datos | [tarea-class-example-4](./tarea-class-example-4.md) | $r_k\approx\pm0{,}85$ alternando, todos significativos → estacionalidad de periodo 2 |

## Relación con otros temas y proyectos
- Viene de [02 — introducción a pronósticos](../02-introduccion-a-pronosticos/README.md), donde se definen los patrones de demanda (horizontal, tendencia, estacionalidad, ciclo, aleatoriedad).
- El patrón detectado aquí decide el método:
  - serie aleatoria/estacionaria → [04 — promedio móvil y suavización simple](../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/README.md);
  - tendencia → [05 — suavización doble de Holt](../05-tendencia-suavizacion-doble-holt/README.md);
  - estacionalidad → [06 — Winters y tracking signal](../06-estacionalidad-winters-y-tracking-signal/README.md);
  - autocorrelación como base del modelo → [07 — ARIMA](../07-arima/README.md).
- La serie de ventas propias del [ejemplo 1](./tarea-class-example-1.md) se reutiliza para comparar promedios móviles y suavización exponencial en [promedio-movil-y-suavizacion-exponencial](../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/promedio-movil-y-suavizacion-exponencial.md) (ese libro copia, celda por celda, las 14 hojas del ejemplo 1).
- El [proyecto THYMS de pronóstico](../proyecto-thyms-pronostico/README.md) explora sus datos con histograma, gráfico de retardo, boxplot y autocorrelograma en Python.
- El [parcial 1](../parcial-1/README.md) evalúa este análisis exploratorio junto con los métodos de pronóstico.
