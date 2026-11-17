# L08-forecasting-with-arima

> **Archivo:** [`L08-forecasting-with-arima.pdf`](./L08-forecasting-with-arima.pdf) · **Corte 1** · 20 páginas  
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
- La autocorrelación y el correlograma, que permiten detectar la dependencia que explota ARIMA, se ven en [`../03-graficas-y-autocorrelacion/`](../03-graficas-y-autocorrelacion/) y en la hoja `CORRELOGRAMA` de [`../06-estacionalidad-winters-y-tracking-signal/metodo-winters.md`](../06-estacionalidad-winters-y-tracking-signal/metodo-winters.md).
- El promedio móvil de 5 periodos con el que se compara AR(1) está en [`../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/`](../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/).
- La tabla «Comparación Métodos de Pronósticos» (ARIMA / Box & Jenkins frente a los demás métodos) está en la página 39 de [`../06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md`](../06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md).
- El proyecto de pronóstico de THYMS: [`../proyecto-thyms-pronostico/`](../proyecto-thyms-pronostico/).

**Errores o inconsistencias detectados en el material:**
- p. 12–17: la fórmula MA(1) se escribe con $+\theta_1 e_{t-1}$, pero los números del ejemplo salen de $F_t=\bar\mu-\theta_1 e_{t-1}$. En la p. 14 se escribe «109,5 − 0,5·3,5 = 111,3», que en realidad da 107,75; el 111,3 corresponde a $109{,}5-0{,}5\times(-3{,}5)$.
- p. 5 dice que ARIMA requiere al menos 72 datos; la tabla de la clase 7 (p. 39) dice 50 o más.
- En la p. 18 el ARMA(1,1) usa $\hat x_{t-1}$ y no incluye $\bar\mu$; se entiende que trabaja con la serie centrada ($\dot x$).

## Contenido completo (página por página)

### Página 1 — Operations Management: Introduction to Forecasting (portada)

Operations Management · Introduction to Forecasting · 2026

> [Imagen decorativa: foto del campus, logo de la Universidad de La Sabana y logo de licencia Creative Commons BY-NC-SA]

### Página 2 — Lecture Objective

- To introduce forecasting methods, with their advantages and disadvantages, commonly used for data with negative autocorrelation

### Página 3 — Box-Jenkins Method (separador)

Box-Jenkins Method

### Página 4 — Box-Jenkins Method

- Exploits possible dependencies between values in the series from period to period.
- The other methods involve independent observations
- Example: Correlated monthly sales given a yield bonus

### Página 5 — Box-Jenkins

- Integrated autoregressive moving average method (ARIMA)
- Integrated refers to the differentiation that is to generate a new series equal to the first differences of the original series. This eliminates the trend
- Short-term forecasts
- Require at least 72 historical data
- Different types
  - Autoregressive (AR)
  - Moving Average (MA)
  - Mixto (ARMA)

### Página 6 — Box-Jenkins: auto regressive

- Autocorrelation structure of the data generation process
- Example:

| Period | Demand |
|---|---|
| 1 | 106 |
| 2 | 110 |
| 3 | 118 |
| 4 | 105 |
| 5 | 115 |
| 6 | 100 |
| 7 | 112 |
| 8 | 106 |
| 9 | 118 |
| 10 | 102 |
| 11 | 112 |
| 12 | 110 |
| Average | 109,5 |

> [Gráfico «DEMANDA - AUTOCORRELACION»: dispersión, eje x = 95–120, eje y = 98–120. Cada punto es el par (demanda en $t$, demanda en $t-1$) para $t=2,\dots,12$: (110, 106), (118, 110), (105, 118), (115, 105), (100, 115), (112, 100), (106, 112), (118, 106), (102, 118), (112, 102), (110, 112). La nube tiene pendiente negativa: a una demanda alta le sigue una baja y viceversa (autocorrelación negativa de rezago 1).]

### Página 7 — Box-Jenkins: AR

Desviaciones respecto a la media $\bar x=109{,}5$:

| Period | Demand | $\dot x_t=x_t-\bar x$ | $\dot x_{t-1}$ | $\dot x_{t-1}\dot x_t$ | $\dot x_t^2$ |
|---|---|---|---|---|---|
| 1 | 106 | -3,5 | | | 12,25 |
| 2 | 110 | 0,5 | -3,5 | -1,75 | 0,25 |
| 3 | 118 | 8,5 | 0,5 | 4,25 | 72,25 |
| 4 | 105 | -4,5 | 8,5 | -38,25 | 20,25 |
| 5 | 115 | 5,5 | -4,5 | -24,75 | 30,25 |
| 6 | 100 | -9,5 | 5,5 | -52,25 | 90,25 |
| 7 | 112 | 2,5 | -9,5 | -23,75 | 6,25 |
| 8 | 106 | -3,5 | 2,5 | -8,75 | 12,25 |
| 9 | 118 | 8,5 | -3,5 | -29,75 | 72,25 |
| 10 | 102 | -7,5 | 8,5 | -63,75 | 56,25 |
| 11 | 112 | 2,5 | -7,5 | -18,75 | 6,25 |
| 12 | 110 | 0,5 | 2,5 | 1,25 | 0,25 |
| Average | 109,5 | | Suma | **-256,25** | **379** |

Las filas 2, 3, 5, 7, 9 y 11 tienen recuadros rojos en las columnas $\dot x_t$ y $\dot x_{t-1}$ (pares de signo opuesto).

**HINT:** When $\dot x_t$ is positive, $\dot x_{t-1}$ tends to be negative. Thus, some autocorrelación at lag 1 is probable.

### Página 8 — Box-Jenkins: auto regresive

- AR(1):

$$\dot x_t=\phi_1\dot x_{t-1}+e_t$$

Where $e_t$ is random independent variable with mean equal to zero and variance $\sigma^2$.

$\phi_1$ is defined as the autocorrelation constant.

$$\phi_1=\frac{cov(\dot x_t,\dot x_{t-1})}{var(\dot x_t)}$$

$$cov(\dot x_t,\dot x_{t-1})=E[\dot x_t\dot x_{t-1}]=\frac{\sum\dot x_t\dot x_{t-1}}{n-1}=-23.3$$

$$var(\dot x_t)=E[\dot x_t^2]=\frac{\sum\dot x_t^2}{n}=31.6$$

Recuadro destacado: $\phi_1=-0.7$

(Cálculo: $-256{,}25/11=-23{,}3$; $379/12=31{,}6$; $-23{,}3/31{,}6=-0{,}737\approx-0{,}7$.)

### Página 9 — Box-Jenkins: AR(1)

**Forecast:**

$$F_t=\bar\mu+\hat\phi_1\dot x_{t-1}$$

$$F_t=109.5+(-0.7)\,0.5=109.2$$

*¿is it better than Moving Average with n=5?*

(Es el pronóstico del periodo 13, con $\dot x_{12}=0{,}5$. $109{,}5-0{,}35=109{,}15\approx109{,}2$.)

### Página 10 — Box-Jenkins: auto regresivo

- AR(2)

$$F_t=\bar\mu+\hat\phi_1\dot x_{t-1}+\hat\phi_2\dot x_{t-2}$$

### Página 11 — Box-Jenkins: MA

- Modelo de promedio móvil MA

Explota la autocorrelación del error de los datos.

| periodo | x(t) | F(t): promedio móvil (5 periodos) | error | error(t-1) |
|---|---|---|---|---|
| 6 | 100 | 110,8 | -10,8 | |
| 7 | 112 | 109,6 | 2,4 | -10,8 |
| 8 | 106 | 110 | -4 | 2,4 |
| 9 | 118 | 107,6 | 10,4 | -4 |
| 10 | 102 | 110,2 | -8,2 | 10,4 |
| 11 | 112 | 107,6 | 4,4 | -8,2 |
| 12 | 110 | 110 | 0 | 4,4 |

Recuadro rojo: «Parece haber correlación negativa en las últimas dos columnas».

(Error = $x(t)-F(t)$; p. ej. $F(6)=(106+110+118+105+115)/5=110{,}8$.)

### Página 12 — Método de Box-Jenkins: auto regresivo (MA(1))

- Promedio móvil
- MA(1)

$$F_t=\bar\mu+\theta_1 e_{t-1}$$

Donde $\theta_1$ es el peso asignado al error correlacionado. Se fija con un método de minimización de mínimos cuadrados no-lineal.

### Página 13 — Método de Box-Jenkins (ejemplo MA(1), paso 1)

- Promedio móvil
- MA(1): $F_t=\bar\mu+\theta_1 e_{t-1}$

EJEMPLO con $\theta_1=0{,}5$

Asumimos un pronóstico inicial de 109,5

Error = 106 − 109,5 = −3,5

| periodo | x(t) | MA(1) | error |
|---|---|---|---|
| 1 | 106 | 109,5 | -3,5 |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |
| 9 | | | |
| 10 | | | |
| 11 | | | |
| 12 | | | |

### Página 14 — Método de Box-Jenkins (ejemplo MA(1), paso 2)

- Promedio móvil
- MA(1): $F_t=\bar\mu+\theta_1 e_{t-1}$

EJEMPLO con $\theta_1=0{,}5$

Calculamos el pronóstico:

$$F_t=\bar\mu+\theta_1 e_{t-1}=109{,}5-0{,}5\cdot3{,}5=111{,}3$$

| periodo | x(t) | MA(1) | error |
|---|---|---|---|
| 1 | 106 | 109,5 | -3,5 |
| 2 | | 111,3 | |
| 3 a 12 | | | |

> Nota del transcriptor: tal como está escrito, $109{,}5-0{,}5\times3{,}5=107{,}75$. El 111,3 sale de $109{,}5-0{,}5\times(-3{,}5)=111{,}25$, es decir, de la convención de Box-Jenkins $F_t=\bar\mu-\theta_1 e_{t-1}$ (la misma que aparece en el ARMA de la página 18). Toda la tabla del ejemplo (páginas 15–17) es coherente con $F_t=\bar\mu-\theta_1 e_{t-1}$, no con el signo $+$ de la fórmula.

### Página 15 — Método de Box-Jenkins (ejemplo MA(1), paso 3)

- Promedio móvil
- MA(1): $F_t=\bar\mu+\theta_1 e_{t-1}$

EJEMPLO con $\theta_1=0{,}5$

Repetir el procedimiento a medida que nueva información se conoce.

| periodo | x(t) | MA(1) | error |
|---|---|---|---|
| 1 | 106 | 109,5 | -3,5 |
| 2 | 110 | 111,3 | -1,3 |
| 3 | 118 | 110,1 | 7,9 |
| 4 a 12 | | | |

### Página 16 — Método de Box-Jenkins (ejemplo MA(1), datos completos)

Misma diapositiva con la columna $x(t)$ completa y las demás vacías desde el periodo 4:

| periodo | x(t) | MA(1) | error |
|---|---|---|---|
| 1 | 106 | 109,5 | -3,5 |
| 2 | 110 | 111,3 | -1,3 |
| 3 | 118 | 110,1 | 7,9 |
| 4 | 105 | | |
| 5 | 115 | | |
| 6 | 100 | | |
| 7 | 112 | | |
| 8 | 106 | | |
| 9 | 118 | | |
| 10 | 102 | | |
| 11 | 112 | | |
| 12 | 110 | | |

### Página 17 — Método de Box-Jenkins (ejemplo MA(1), resultado)

- Promedio móvil
- MA(1): $F_t=\bar\mu+\theta_1 e_{t-1}$

EJEMPLO con $\theta_1=0{,}5$

| periodo | x(t) | MA(1) | error |
|---|---|---|---|
| 1 | 106 | 109,5 | -3,5 |
| 2 | 110 | 111,3 | -1,3 |
| 3 | 118 | 110,1 | 7,9 |
| 4 | 105 | 105,6 | -0,6 |
| 5 | 115 | 109,8 | 5,2 |
| 6 | 100 | 106,9 | -6,9 |
| 7 | 112 | 112,9 | -0,9 |
| 8 | 106 | 110,0 | -4,0 |
| 9 | 118 | 111,5 | 6,5 |
| 10 | 102 | 106,2 | -4,2 |
| 11 | 112 | 111,6 | 0,4 |
| 12 | 110 | 109,3 | 0,7 |

(Error = $x(t)-F(t)$. Comprobado: cada fila sale de $F_t=109{,}5-0{,}5\,e_{t-1}$ con los errores sin redondear.)

### Página 18 — Método de Box-Jenkins: auto regresivo (ARMA)

- Modelos Mixtos: ARMA $(p,q)$
- $p$: componente autorregresivo
- $q$: componente de promedio móvil

ARMA(1,1):

$$F_t=\hat\phi_1\hat x_{t-1}-\hat\theta_1 e_{t-1}$$

### Página 19 — Método de Box-Jenkins (ARMA(1,1): estimación de parámetros)

ARMA(1,1)

Estimación de parámetros:

$$\rho_k=\frac{cov(\dot x_t\,\dot x_{t-k})}{var(\dot x_t)}$$

$$\phi_1=\frac{\rho_2}{\rho_1}$$

$$\rho_1=\frac{(1-\phi_1\theta_1)(\phi_1-\theta_1)}{1+\theta_1^2-2\theta_1\phi_1}$$

### Página 20 — Cierre

- Gracias!

William Guerrero, Ph.D.

## Anexo: texto extraído automáticamente del PDF

> Texto plano tal como sale del PDF, sin fórmulas ni tablas que estén como imagen. La versión fiel y completa es la sección «Contenido completo» de arriba.

### Página 1 · 2 imagen(es)

Operations Management
Introduction to Forecasting
2026

### Página 2 · 1 imagen(es)

Lecture Objective
• To introduce forecasting methods, with 
their advantages and disadvantages, 
commonly used for data with negative 
autocorrelation

### Página 3 · 1 imagen(es)

Box-Jenkins Method

### Página 4 · 1 imagen(es)

Box-Jenkins Method
• Exploits possible dependencies between values 
in the series from period to period.
• The other methods involve independent 
observations
• Example: Correlated monthly sales given a yield 
bonus

### Página 5 · 1 imagen(es)

Box-Jenkins
• Integrated autoregressive moving average method 
(ARIMA)
• Integrated refers to the differentiation that is to generate 
a new series equal to the first differences of the original 
series. This eliminates the trend
• Short-term forecasts
• Require at least 72 historical data 
• Different types
– Autoregressive (AR)
– Moving Average (MA)
– Mixto (ARMA)

### Página 6 · 2 imagen(es)

Box-Jenkins: auto regressive
• Autocorrelation structure of the data generation process
• Example: 
Period
Demand
1
106
2
110
3
118
4
105
5
115
6
100
7
112
8
106
9
118
10
102
11
112
12
110
Average
109,5

### Página 7 · 1 imagen(es)

Box-Jenkins: AR
Period
Demand
ሶ𝒙𝒕= 𝒙𝒕−ഥ𝒙
ሶ𝒙𝒕−𝟏
ሶ𝒙𝒕−𝟏ሶ𝒙𝒕
ሶ𝒙𝒕
𝟐
1
106
-3,5
12,25
2
110
0,5
-3,5
-1,75
0,25
3
118
8,5
0,5
4,25
72,25
4
105
-4,5
8,5
-38,25
20,25
5
115
5,5
-4,5
-24,75
30,25
6
100
-9,5
5,5
-52,25
90,25
7
112
2,5
-9,5
-23,75
6,25
8
106
-3,5
2,5
-8,75
12,25
9
118
8,5
-3,5
-29,75
72,25
10
102
-7,5
8,5
-63,75
56,25
11
112
2,5
-7,5
-18,75
6,25
12
110
0,5
2,5
1,25
0,25
Average
109,5
Suma
-256,25
379
HINT: When ሶ𝒙𝒕 is positive, ሶ𝒙𝒕−𝟏 tends to be negative. 
Thus, some autocorrelación at lag 1 is probable.

### Página 8 · 3 imagen(es)

Box-Jenkins: auto regresive
• AR(1):
ሶ𝑥𝑡= 𝜙1 ሶ𝑥𝑡−1 + 𝑒𝑡
Where 𝑒𝑡 is random independent variable with mean equal 
to zero and variance 𝜎2
𝜙1 is defined as the autocorrelation constant.
𝜙1 = 𝑐𝑜𝑣
ሶ𝑥𝑡, ሶ𝑥𝑡−1
𝑣𝑎𝑟( ሶ𝑥𝑡)
𝑐𝑜𝑣
ሶ𝑥𝑡, ሶ𝑥𝑡−1 = 𝐸
ሶ𝑥𝑡ሶ𝑥𝑡−1 =
σ ሶ𝑥𝑡ሶ𝑥𝑡−1
𝑛−1
= −23.3 
𝑣𝑎𝑟
ሶ𝑥𝑡= 𝐸
ሶ𝑥𝑡
2 =
σ ሶ𝑥𝑡
2
𝑛
= 31.6
𝜙1 = −0.7

### Página 9 · 1 imagen(es)

Box-Jenkins: AR(1)
Forecast:
𝐹𝑡= ҧ𝜇+ ෠𝜙1 ሶ𝑥𝑡−1
𝐹𝑡= 109.5 + −0.7 0.5
= 109.2 
¿is it better than Moving Average with n=5?

### Página 10 · 1 imagen(es)

Box-Jenkins: auto regresivo
• AR(2)
𝐹𝑡= ҧ𝜇+ ෠𝜙1 ሶ𝑥𝑡−1 + ෠𝜙2 ሶ𝑥𝑡−2

### Página 11 · 3 imagen(es)

Box-Jenkins: MA
• Modelo de promedio móvil MA
Explota la autocorrelación del error de los datos.
periodo
x(t)
F(t): 
promedio 
movil (5 
periodos)
error
error(t-1)
6
100
110,8
-10,8
7
112
109,6
2,4
-10,8
8
106
110
-4
2,4
9
118
107,6
10,4
-4
10
102
110,2
-8,2
10,4
11
112
107,6
4,4
-8,2
12
110
110
0
4,4
Parece 
haber 
correlación 
negativa en 
las últimas 
dos 
columnas

### Página 12 · 1 imagen(es)

Método de Box-Jenkins: auto regresivo
• Promedio móvil
• MA(1)
𝐹𝑡= ҧ𝜇+ 𝜃1𝑒𝑡−1
Donde 𝜃1 es el peso asignado al error correlacionado. Se 
fija con un método de minimización de mínimos cuadrados 
no-lineal.

### Página 13 · 1 imagen(es)

Método de Box-Jenkins
• Promedio móvil
• MA(1) ∶ 𝐹𝑡= ҧ𝜇+ 𝜃1𝑒𝑡−1
EJEMPLO con 𝜃1 = 0,5
Asumimos un pronóstico inicial de 109,5
Error = 106-109,5 = -3,5
periodo
x(t)
MA(1)
error
1
106
109,5
-3,5
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

### Página 14 · 1 imagen(es)

Método de Box-Jenkins
• Promedio móvil
• MA(1) ∶ 𝐹𝑡= ҧ𝜇+ 𝜃1𝑒𝑡−1
EJEMPLO con 𝜃1 = 0,5
Calculamos el pronóstico:
𝐹𝑡=
ҧ𝜇+ 𝜃1𝑒𝑡−1
 = 109,5 – 0,5*3,5 = 111,3
periodo
x(t)
MA(1)
error
1
106
109,5
-3,5
2
111,3
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

### Página 15 · 1 imagen(es)

Método de Box-Jenkins
• Promedio móvil
• MA(1) ∶ 𝐹𝑡= ҧ𝜇+ 𝜃1𝑒𝑡−1
EJEMPLO con 𝜃1 = 0,5
Repetir el procedimiento a 
medida que nueva información 
se conoce.
periodo
x(t)
MA(1)
error
1
106
109,5
-3,5
2
110
111,3
-1,3
3
118
110,1
7,9
4
5
6
7
8
9
10
11
12

### Página 16 · 1 imagen(es)

Método de Box-Jenkins
• Promedio móvil
• MA(1) ∶ 𝐹𝑡= ҧ𝜇+ 𝜃1𝑒𝑡−1
EJEMPLO con 𝜃1 = 0,5
periodo
x(t)
MA(1)
error
1
106
109,5
-3,5
2
110
111,3
-1,3
3
118
110,1
7,9
4
105
5
115
6
100
7
112
8
106
9
118
10
102
11
112
12
110

### Página 17 · 1 imagen(es)

Método de Box-Jenkins
• Promedio móvil
• MA(1) ∶ 𝐹𝑡= ҧ𝜇+ 𝜃1𝑒𝑡−1
EJEMPLO con 𝜃1 = 0,5
periodo
x(t)
MA(1)
error
1
106
109,5
-3,5
2
110
111,3
-1,3
3
118
110,1
7,9
4
105
105,6
-0,6
5
115
109,8
5,2
6
100
106,9
-6,9
7
112
112,9
-0,9
8
106
110,0
-4,0
9
118
111,5
6,5
10
102
106,2
-4,2
11
112
111,6
0,4
12
110
109,3
0,7

### Página 18 · 1 imagen(es)

Método de Box-Jenkins: auto regresivo
• Modelos Mixtos : ARMA (p,q)
• p: componente autorregresivo
• q: componente de promedio móvil
ARMA(1,1):
𝐹𝑡= ෠𝜙1 ො𝑥𝑡−1 −෠𝜃1𝑒𝑡−1

### Página 19 · 1 imagen(es)

Método de Box-Jenkins
ARMA(1,1) 
Estimación de parámetros:
𝜌𝑘= 𝑐𝑜𝑣
ሶ𝑥𝑡ሶ𝑥𝑡−𝑘
𝑣𝑎𝑟( ሶ𝑥𝑡)
𝜙1 = 𝜌2
𝜌1
𝜌1 = 1 −𝜙1𝜃1
𝜙1 −𝜃1
1 + 𝜃1
2 −2𝜃1𝜙1

### Página 20 · 1 imagen(es)

• Gracias!
William Guerrero, Ph.D.

