# L06-forecasting-data-with-trend

> **Archivo:** [`L06-forecasting-data-with-trend.pdf`](./L06-forecasting-data-with-trend.pdf) · **Corte 1** · 25 páginas  
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
- p. 6–7: demanda trimestral de 8 periodos (200, 250, 175, 186, 225, 285, 305, 190) con $\alpha=\beta=0{,}1$, $S_0=200$, $G_0=10$; se pide el pronóstico a un periodo y su error. La diapositiva no trae la solución; la resuelve el Excel [`suavizacion-exponencial-doble-holt.md`](./suavizacion-exponencial-doble-holt.md), aunque con otros valores iniciales y otros parámetros.
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
- [`suavizacion-exponencial-doble-holt.md`](./suavizacion-exponencial-doble-holt.md): el Excel de esta clase, con Holt aplicado a los datos de la p. 6 e inicializado por regresión.
- Paso previo, suavización simple y medidas de error: [`../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md`](../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md).
- Paso siguiente, Winters (Holt más estacionalidad), con la tabla que muestra por qué Holt falla con estacionalidad: [`../06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md`](../06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md).
- Aplicación de Holt en el parcial: [`../parcial-1/README.md`](../parcial-1/README.md).

**Errores o inconsistencias detectados en el material:**
- p. 8: las tres fórmulas se rotulan $S_1$, pero son estimaciones de la pendiente inicial (diferencias entre datos), no del nivel.
- p. 6: «Quater» por *quarter* (trimestre). p. 16: «Trend ver time» por *trend over time*. p. 19: «Minimim» por *minimum*.
- p. 22: el último gráfico (viscosidad contra tiempo de agitación) es claramente creciente, aunque curvo; un $R^2$ lineal de 0,0214 parece demasiado bajo.

## Contenido completo (página por página)

### Página 1 — Operations Management: Introduction to Forecasting (portada)

Operations Management · Introduction to Forecasting

> [Imagen decorativa: foto del campus, logo de la Universidad de La Sabana y logo de licencia Creative Commons BY-NC-SA]

### Página 2 — Lecture Objective

- To introduce forecasting methods, with their advantages and disadvantages for data with trend

### Página 3 — Double Exponential Smoothing using Holt's method

- Tracks time series with linear trend patterns
- Requires two smoothing constants $\alpha$ & $\beta$
- Uses two smoothing equations:
  1. Intercept: $S_t$
  2. Trend (slope): $G_t$

### Página 4 — Double Exponential Smoothing using Holt's method

- $S_t=\alpha(D_t)+(1-\alpha)(S_{t-1}+G_{t-1})$
- $G_t=\beta(S_t-S_{t-1})+(1-\beta)G_{t-1}$

In general $\beta\le\alpha$: greater stability to the estimated slope

### Página 5 — Explanation

> [Gráfico «Demand»: línea con marcadores (serie «Dt»), eje x = 0–4,5, eje y = 0–50. Puntos de demanda: (1, 15), (2, 25), (3, 36), (4, 44). En t = 2 está marcado $S_{t-1}$ (≈25). Desde ahí un triángulo azul de pendiente $G_{t-1}$ sube hasta $S_t'$ (≈36, en t = 3), que es la proyección de la recta. Un cuadrado negro marca $S_t$ (≈41, en t = 3), por encima de $S_t'$.]

Recuadros de texto:
- Note that $S_t$ "falls" in the segment between $S_t'$ and $D_t$
- $S_t'$ is the projection of the passing straight line by $S_{t-1}$ and that has slope $G_{t-1}$

(Es decir, $S_t'=S_{t-1}+G_{t-1}$ y $S_t=\alpha D_t+(1-\alpha)S_t'$ es un promedio ponderado entre la demanda observada y la proyección de la tendencia.)

### Página 6 — Double Exponential Smoothing using Holt's method

- Forecasting $\tau$ periods ahead, at period $t$:

$$F_{t,t+\tau}=S_t+\tau G_t$$

- Example:
  - $\beta$ and $\alpha=0{,}1$
  - $S_0=200$ and $G_0=10$
- Forecast one period ahead

Find the error and compare

| Quater | Demand |
|---|---|
| 1 | 200 |
| 2 | 250 |
| 3 | 175 |
| 4 | 186 |
| 5 | 225 |
| 6 | 285 |
| 7 | 305 |
| 8 | 190 |

(«Quater» está escrito así en la diapositiva; se refiere a trimestre, *quarter*.)

### Página 7 — Double Exponential Smoothing using Holt's method

- Last resource
- Forecast demand at 5, in period 2?

$$F_{2,5}=S_2+(3)G_2$$

- Holt's disadvantages: "difficult" to update

### Página 8 — Double Exponential Smoothing using Holt's method

Options for Setting Initial Conditions

- $S_1=A_2-A_1$
- $S_1=\frac{1}{3}\left[(A_2-A_1)+(A_3-A_2)+(A_4-A_3)\right]$
- $S_1=\dfrac{A_n-A_1}{n-1}$
- It is best to establish initial base periods

($A_i$ = dato real del periodo $i$, $n$ = número de datos. Las tres expresiones son diferencias entre datos, es decir, estimaciones de la **pendiente** inicial, aunque la diapositiva las nombra $S_1$.)

### Página 9 — Initializing the method

- Two parameters: Trend ($G_0$) intercept at *y-axe* ($S_0$)
- **Method 1. Linear regression**
- Excel spreadsheet equations ("pendiente" and "interseccion.eje")

### Página 10 — Initializing the method: Linear regression method

| t | Dt |
|---|---|
| 0 | |
| 1 | 15 |
| 2 | 20 |
| 3 | 26 |
| 4 | 30 |
| 5 | 35 |
| 6 | 38 |
| 7 | 40 |
| 8 | 43 |

- Calcule $S_0$ y $G_0$ con el método de regresión
- Calcule los pronósticos $F_t$ para cada periodo. Sean $\alpha$ y $\beta=0.1$

### Página 11 — Initializing the method: Linear regression method (solución)

| t | Dt | St | Gt | Ft | et |
|---|---|---|---|---|---|
| 0 | | 12.8 | 4.01 | | |
| 1 | 15 | 16.7 | 3.99 | 16.8 | 1.83 |
| 2 | 20 | 20.6 | 3.99 | 20.6 | 0.64 |
| 3 | 26 | 24.7 | 4 | 24.6 | -1.4 |
| 4 | 30 | 28.8 | 4.01 | 28.7 | -1.3 |
| 5 | 35 | 33.1 | 4.04 | 32.9 | -2.1 |
| 6 | 38 | 37.2 | 4.04 | 37.1 | -0.9 |
| 7 | 40 | 41.1 | 4.03 | 41.2 | 1.24 |
| 8 | 43 | 44.9 | 4.01 | 45.1 | 2.15 |

$S_0=12.8$ es el intercepto y $G_0=4.01$ la pendiente de la regresión de $D_t$ sobre $t$ ($t=1,\dots,8$). Cada fila usa $F_t=S_{t-1}+G_{t-1}$, $S_t=0.1D_t+0.9F_t$, $G_t=0.1(S_t-S_{t-1})+0.9G_{t-1}$, y el error es $e_t=F_t-D_t$ (p. ej. $16.8-15=1.8$).

### Página 12 — Initializing the method (Method 2. Seasons)

- **Method 2. Seasons**
- Tomar $m$ grupos de $N$ datos. Un grupo es una "estación"
- Tomar el promedio $V_i$ de cada estación
- La pendiente es: $G_0=(V_m-V_1)/[(m-1)N]$
- El corte con el eje ($t-1$) es: $V_1-G_0(N+1)/2$

(Es decir, $S_0=V_1-G_0\frac{N+1}{2}$: el promedio $V_1$ está ubicado en el centro de la primera estación, $t=(N+1)/2$, y se retrocede hasta $t=0$.)

### Página 13 — Interpretación: Método Estaciones

> [Gráfico «Demanda»: línea azul con rombos (serie «Dt»), eje x = 0–9, eje y = 0–50. Demanda 15, 20, 26, 30, 35, 38, 40, 43 en t = 1…8. Una línea vertical negra en t ≈ 4,5 separa «Estación 1» (t = 1–4) de «Estación 2» (t = 5–8). Flecha en t = 2,5 con el rótulo «$V_1$ = Promedio ($D_1\ldots D_4$)», a la altura ≈22,75 marcada en el eje y como $V_1$; flecha en t = 6,5 con el rótulo «$V_2$ = Promedio ($D_5\ldots D_8$)», a la altura ≈39 marcada como $V_2$. Una recta roja une ($2{,}5$; $V_1$) con ($6{,}5$; $V_2$): su pendiente es $G_0$.]

### Página 14 — Initializing the method: Método 2 Estaciones

| t | Dt |
|---|---|
| 0 | |
| 1 | 15 |
| 2 | 20 |
| 3 | 26 |
| 4 | 30 |
| 5 | 35 |
| 6 | 38 |
| 7 | 40 |
| 8 | 43 |

- Calcule $S_0$ y $G_0$ con el método de las estaciones
- Calcule los pronósticos $F_t$ para cada periodo. Sean $\alpha$ y $\beta=0.1$

### Página 15 — Initializing the method: Método 2 Estaciones (solución)

| t | Dt | St | Gt | Ft | et |
|---|---|---|---|---|---|
| 0 | | 12.6 | 4.06 | | |
| 1 | 15 | 16.5 | 4.05 | 16.7 | 1.66 |
| 2 | 20 | 20.5 | 4.04 | 20.5 | 0.54 |
| 3 | 26 | 24.7 | 4.06 | 24.5 | -1.5 |
| 4 | 30 | 28.9 | 4.07 | 28.7 | -1.3 |
| 5 | 35 | 33.1 | 4.09 | 32.9 | -2.1 |
| 6 | 38 | 37.3 | 4.1 | 37.2 | -0.8 |
| 7 | 40 | 41.3 | 4.08 | 41.4 | 1.39 |
| 8 | 43 | 45.1 | 4.06 | 45.3 | 2.34 |

(Con $m=2$ estaciones de $N=4$ datos: $V_1=(15+20+26+30)/4=22.75$, $V_2=(35+38+40+43)/4=39$, $G_0=(39-22.75)/[(2-1)4]=4.0625\approx4.06$ y $S_0=22.75-4.0625(4+1)/2=12.59\approx12.6$. Error $e_t=F_t-D_t$.)

### Página 16 — Regression Analysis

- When is it useful?
  - *Trend ver time* (se entiende *trend over time*)
  - *Linearly Correlated variables*

> [Gráfico superior «Forecasts from Linear regression model»: eje x = t (1980–2015), eje y = «International tourist arrivals to Australia (millions)» (≈1–7). Serie negra = llegadas reales de 1980 a 2010, de ≈0,9 a ≈5,4 millones; recta azul de regresión ajustada; desde 2011 a 2015 la recta se prolonga (≈6 a ≈6,7) con bandas grises de intervalo de predicción que se ensanchan.]

> [Gráfico inferior: dispersión «Sales» (eje y, 100–124) contra «Advertising Dollars (1,000s)» (eje x, 5,50–7,00). Puntos rosados de ≈(5,65; 108,5) a ≈(6,75; 117); recta de regresión creciente que se prolonga más allá de una línea vertical punteada en ≈6,9 con el rótulo «Future Prediction».]

### Página 17 — Regression Analysis

- Assumptions:
  - *Normality of the residuals*
  - *Independence*
  - *Homocedasticity*

### Página 18 — Statistical Model

$$Y=a+bx$$

- y Dependent variable
- X Independent variable

### Página 19 — Computing the estimators

Minimim square errors (mínimos cuadrados)

- $b=\dfrac{\sum xy-n\,\bar x\,\bar y}{\sum x^2-n\,\bar x^2}$
- $a=\bar y-b\,\bar x$

($n$ = número de pares de datos; $\bar x$, $\bar y$ = medias.)

> [Gráfico: dispersión de ≈100 puntos azules, eje x = −20 a 60, eje y ≈ 0 a 16, con una recta roja de mínimos cuadrados creciente (≈2,5 en x = −20; ≈5 en x = 0; ≈14 en x = 60).]

### Página 20 — Examples of Linear Regression

- Product Demand vs Temperature Forecast
- Is there a clear relationship (dependence) between the factors of interest and the temperature in the three cases illustrated in the graphs?

> [Tres gráficos de dispersión con eje x «Temperatura» (0–200):
> 1. «Viscosidad» (eje y 0–180): ≈25 puntos de (80, 92) a (158, 160), relación lineal creciente clara.
> 2. «Granularidad» (eje y 0–160): ≈35 puntos de (80, 40) a (152, 62), relación lineal creciente con poca pendiente.
> 3. «Deformación» (eje y 0–1,4): ≈25 puntos con temperatura entre ≈22 y ≈55, de (22, 0,67) a (55, 1,38), relación lineal creciente con mucha pendiente.]

### Página 21 — Examples of Linear Regression

- The index or coefficient of determination $R^2$ measures % of variation explained by the relationship between the variables.

Los mismos tres gráficos de la página 20, con sus estadísticos:

| Gráfico | Coeficiente de correlación $r$ | $R^2$ | Recta ajustada |
|---|---|---|---|
| Viscosidad vs Temperatura | 0.9517 | 0,9058 | $y=0{,}8002x+29{,}745$ |
| Granularidad vs Temperatura | 0,9601 | 0,9218 | $y=0{,}2415x+23{,}706$ |
| Deformación vs Temperatura | 0,9532 | 0,9087 | $y=0{,}0244x+0{,}1453$ |

(Se cumple $R^2=r^2$: $0{,}9517^2=0{,}9057$; $0{,}9601^2=0{,}9218$; $0{,}9532^2=0{,}9086$. La pendiente depende de las unidades; la fuerza de la relación la mide $r$ o $R^2$.)

### Página 22 — Cases where there is no linear relation or dependence of the variables

> [Cinco gráficos de dispersión, cada uno con su $R^2$:
> 1. Deformación (0–180) vs Temperatura (0–200): puntos dispersos sin patrón; $R^2=0{,}0053$.
> 2. Deformación (0–180) vs Temperatura (0–200): puntos dispersos, dos grupos (≈20–60 y ≈90–160 de temperatura); $R^2=0{,}2443$.
> 3. Viscosidad (0–180) vs Temperatura (0–150): relación lineal creciente de (20, 70) a (95, 132); $R^2=0{,}8396$.
> 4. Viscosidad (0–180) vs Vel.Rotación (0–4000): nube creciente con bastante dispersión, de (800, 68) a (2000, 172); $R^2=0{,}5163$.
> 5. Viscosidad (0–180) vs TiempoAgitación (0–100): relación curva (no lineal), plana en ≈25–60 hasta ≈55 y luego sube rápido hasta ≈160 en ≈85; $R^2=0{,}0214$.]

Mensaje: un $R^2$ bajo indica que no hay relación **lineal**; puede no haber relación (gráficos 1–2) o haber una relación no lineal (gráfico 5).

> Nota del transcriptor: en el gráfico 5 la nube es claramente creciente, por lo que un $R^2$ lineal de 0,0214 parece demasiado bajo; puede ser un rótulo intercambiado o un error de la diapositiva.

### Página 23 — Linear Regression Model Assumptions

> [Diagrama superior: dispersión de puntos azules ($y_i$) alrededor de una recta de regresión creciente. Un punto morado ($\hat y_i$) sobre la recta y un segmento vertical que lo une con el dato real representan el residuo.]

Leyenda y fórmulas:
- ◆ $y_i$ (dato real); ● $\hat y_i$ (valor estimado)
- $\hat y_i=a+bX_i$
- $e_i=\hat y_i-y_i$

> [Gráfico «Histograma de los residuos»: eje x = «Residuals» (−50 a 40), eje y = «Frequency» (0–10). Barras con forma de campana centradas en 0 (frecuencias aproximadas de izquierda a derecha: 1, 2, 4, 6, 9, 10, 8, 6, 2, 2) y una curva normal roja superpuesta. Sirve para revisar la **normalidad** de los residuos.]

> [Gráfico «Gráfico de los residuales»: eje y = «Residuos» (−20 a 25), eje x = 0–120. ≈35 puntos dispersos al azar alrededor de 0, sin patrón y con dispersión similar a lo largo del eje x. Sirve para revisar **independencia** y **homocedasticidad**.]

> [Gráfico «Gráfico de probabilidad normal»: eje x = 0–100 (percentil), eje y = «Y» (0–180). Puntos crecientes de ≈(1, 65) a ≈(98, 155), casi alineados. Sirve para revisar la normalidad.]

### Página 24 — EXCEL Tool

> [Captura de pantalla de Excel (pestaña Datos → Análisis de datos → Regresión), hoja «Hoja3» de un libro con hojas Hoja1, Hoja3 y Hoja2.]

Cuadro de diálogo «Regresión»:
- Entrada: Rango Y de entrada = `$B$2:$B$11`; Rango X de entrada = `$A$2:$A$11`; Rótulos ☐; Constante igual a cero ☐; Nivel de confianza ☐ 95 %.
- Opciones de salida: ◉ En una hoja nueva.
- Residuales: ☑ Residuos; ☐ Residuos estándares; ☑ Gráfico de residuales; ☐ Curva de regresión ajustada.
- Probabilidad normal: ☑ Gráfico de probabilidad normal.

Salida «Resumen» visible en la hoja:

| Estadísticas de la regresión | Valor |
|---|---|
| Coeficiente de correlación múltiple | 0,04172837 |
| Coeficiente de determinación R^2 | 0,00174126 |
| R^2 ajustado | -0,12304109 |
| Error típico | 2,38902078 |
| Observaciones | 10 |

ANÁLISIS DE VARIANZA (parcialmente tapado por el cuadro de diálogo):

| | Grados de libertad | Suma de cuadrados |
|---|---|---|
| Regresión | 1 | 0,07964 [resto ilegible] |
| Residuos | 8 | 45,6593 [resto ilegible] |
| Total | 9 | 45,7390 [resto ilegible] |

| | Coeficientes | Error típico | … | Inferior 95,0% | Superior 95,0% |
|---|---|---|---|---|---|
| Intercepción | 14,4152352 | 1,63201 [resto ilegible] | [tapado] | 10,651809 | 18,1786613 |
| Variable X 1 | 0,03107047 | 0,26302 [resto ilegible] | [tapado] | [ilegible] 57546058 (negativo; dígitos iniciales tapados) | 0,63760151 |

Fila 22: «Análisis de los residuales».

> [Gráfico «Variable X 1 Gráfico de los residuales»: eje x = Variable X 1 (0–10), eje y = Residuos (−6 a 4); 10 puntos dispersos alrededor de 0, aprox. −0,5; −3; 2,2; 1,3; 2,5; 0; 1,1; −4,6; 0,6; 0,7.]

> [Gráfico «Gráfico de probabilidad normal»: eje x = Muestra percentil (0–80+), eje y = Y (0–20); puntos crecientes de ≈10 a ≈15,5.]

Lectura: en este ejemplo $R^2=0{,}0017$, es decir, la variable X casi no explica a Y (no hay relación lineal).

### Página 25 — Cierre

- Thanks!

William Guerrero, Ph.D.

## Anexo: texto extraído automáticamente del PDF

> Texto plano tal como sale del PDF, sin fórmulas ni tablas que estén como imagen. La versión fiel y completa es la sección «Contenido completo» de arriba.

### Página 1 · 2 imagen(es)

Operations Management 
Introduction to Forecasting

### Página 2 · 1 imagen(es)

Lecture Objective
• To introduce forecasting methods, with 
their advantages and disadvantages for 
data with trend

### Página 3 · 1 imagen(es)

Double Exponential Smoothing 
using Holt's method
• Tracks time series with linear trend 
patterns
• Requires two smoothing constants 𝛼 & 𝛽
• Uses two smoothing equations :
1. Intercept: 𝑆𝑡 
2. Trend (slope): 𝐺𝑡

### Página 4 · 1 imagen(es)

Double Exponential Smoothing 
using Holt's method
• 𝑆𝑡= 𝛼𝐷𝑡+ (1 −𝛼)(𝑆𝑡−1 + 𝐺𝑡−1)
• 𝐺𝑡= 𝛽𝑆𝑡−𝑆𝑡−1 + 1 −𝛽𝐺𝑡−1
In general 𝛽 ≤𝛼: greater stability to the 
estimated slope

### Página 5 · 1 imagen(es)

Explanation
0
5
10
15
20
25
30
35
40
45
50
0
0,5
1
1,5
2
2,5
3
3,5
4
4,5
Demand
Dt
St-1
St
Gt-1
St’
Note that St 
"falls" in the 
segment 
between St' and 
Dt
St' is the projection of the 
passing straight line 
by St-1 and that has slope 
Gt-1

### Página 6 · 1 imagen(es)

Double Exponential Smoothing 
using Holt's method
• Forecasting 𝜏 periods ahead, at period t:
 𝐹𝑡,𝑡+𝜏= 𝑆𝑡+ 𝜏𝐺𝑡
• Example: 
 𝛽 𝑎𝑛𝑑 𝛼= 0,1
𝑆0 = 200 𝑎𝑛𝑑 𝐺0 = 10
• Forecast one period ahead
Find the error and compare
Quater Demand
1
200
2
250
3
175
4
186
5
225
6
285
7
305
8
190

### Página 7 · 1 imagen(es)

Double Exponential Smoothing 
using Holt's method
• Last resource
• Forecast demand at 5,in period 2? 
𝐹2,5 = 𝑆2 + (3)𝐺2
• Holt's disadvantages: “difficult” to update

### Página 8 · 1 imagen(es)

Double Exponential Smoothing 
using Holt's method
Options for Setting Initial Conditions
• 𝑆1 = 𝐴2 −𝐴1
• 𝑆1 =
1
3
𝐴2 −𝐴1 + 𝐴3 −𝐴2 + 𝐴4 −𝐴3
• 𝑆1 =
𝐴𝑛−𝐴1
𝑛−1
• It is best to establish initial base periods

### Página 9 · 1 imagen(es)

Initializing the method
• Two parameters: Trend (G0) intercept at y-axe 
(S0)
• Method 1. Linear regression
• Excel spreadsheet equations (“pendiente” and 
“interseccion.eje”)

### Página 10 · 2 imagen(es)

Initializing the method: 
Linear regression method
Calcule S0 y G0 con el método de regresión
Calcule los pronósticos Ft para cada periodo. 
Sean  y  = 0.1

### Página 11 · 2 imagen(es)

Initializing the method: Linear 
regression method

### Página 12 · 1 imagen(es)

Initializing the method
• Method 2. Seasons
• Tomar m grupos de N datos. Un grupo es una 
“estación”
• Tomar el promedio Vi de cada estación
• La pendiente es: G0= (Vm-V1)/[(m-1)N] 
• El corte con el eje (t-1) es: V1- G0(N+1)/2

### Página 13 · 2 imagen(es)

Interpretación: Método Estaciones

### Página 14 · 2 imagen(es)

Initializing the method: Método 2 
Estaciones
Calcule S0 y G0 con el 
método de las estaciones
Calcule los pronósticos Ft 
para cada periodo. Sean  y 
 = 0.1

### Página 15 · 2 imagen(es)

Initializing the method: Método 2 
Estaciones

### Página 16 · 3 imagen(es)

• When is it useful?
– Trend ver time 
– Linearly Correlated variables 
Regression Analysis

### Página 17 · 1 imagen(es)

• Assumptions:
– Normality of the residuals
– Independence
– Homocedasticity
Regression Analysis

### Página 18 · 1 imagen(es)

Statistical Model
𝑌= 𝑎+ 𝑏𝑥
y Dependent variable
X Independent variable

### Página 19 · 2 imagen(es)

Computing the estimators
Minimim square errors
• 𝑏=
σ 𝑥𝑦−𝑛 ҧ𝑥 ത𝑦
σ 𝑥2 −𝑛 ҧ𝑥2
• 𝑎= ത𝑦 −𝑏 ҧ𝑥

### Página 20 · 2 imagen(es)

Examples of Linear Regression
– Product Demand vs Temperature Forecast
– Is there a clear relationship (dependence) between the factors of 
interest and the temperature in the three cases illustrated in the 
graphs?

### Página 21 · 3 imagen(es)

Examples of Linear Regression
•
The index or coefficient of determination R2 measures % of variation 
explained by the relationship between the variables.

### Página 22 · 3 imagen(es)

Cases where there is no linear relation or 
dependence of the variables

### Página 23 · 4 imagen(es)

Linear Regression Model Assumptions

### Página 24 · 2 imagen(es)

EXCEL Tool

### Página 25 · 1 imagen(es)

• Thanks!
William Guerrero, Ph.D.

