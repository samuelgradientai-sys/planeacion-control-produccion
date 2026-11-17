# L07-forecasting-seasonality-and-tracking-signal

> **Archivo:** [`L07-forecasting-seasonality-and-tracking-signal.pdf`](./L07-forecasting-seasonality-and-tracking-signal.pdf) · **Corte 1** · 40 páginas  
> **Nombre original:** `CORTE 1/Lec 7 - forecasting data with seasonality and Tracking Signal.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** pronóstico de demanda con tendencia y estacionalidad mediante el método de Winters (suavización exponencial triple, multiplicativo y aditivo), selección de parámetros, señal de rastreo (*tracking signal*) e intervalo de confianza del pronóstico.

**Ideas clave:**
- Hay tres patrones de demanda y un método para cada uno: estacionaria → suavización simple / promedios móviles ($\alpha$); con tendencia → Holt / regresión ($\alpha,\beta$); con tendencia y estacionalidad → Winters ($\alpha,\beta,\gamma$).
- Si se aplica Holt a una serie estacional, el pronóstico no reproduce los ciclos: con constantes bajas sale casi una recta y con constantes altas persigue la demanda con retraso (p. 5).
- Winters multiplicativo: la demanda oscila alrededor de una recta de tendencia y la amplitud de la oscilación crece con el nivel. Tiene tres componentes (nivel, tendencia, estación) que se actualizan con una constante de suavización cada uno.
- Winters aditivo: la oscilación tiene amplitud constante; el factor estacional se suma o resta en vez de multiplicar o dividir.
- Inicialización con dos ciclos completos de datos: promedio de cada ciclo → pendiente → nivel → factores estacionales → normalización (que promedien 1).
- Los parámetros se actualizan cuando llega un dato nuevo del ciclo.
- Para escoger parámetros o métodos no basta minimizar el MAD (DAM) o el MSE: hay que validar con datos de prueba distintos de los de calibración y revisar el sesgo.
- La señal de rastreo $T_t=E_t/MAD_t$ debe estar cerca de 0; si se aleja, hay sesgo y hay que cambiar los parámetros o el método.
- El intervalo de confianza del pronóstico se usa solo para un periodo adelante.
- Nombres en Minitab: γ (tendencia) equivale a $\phi$ de la clase; δ (estacional) equivale a $\gamma$ de la clase.

**Fórmulas y métodos:**

*Winters multiplicativo, notación $S$, $G$, $c$ (p. 8–10).* Modelo $D_t=c_tS_t+\varepsilon_t$, donde $D_t$ = demanda en $t$, $S_t$ = nivel (punto sobre la recta), $G_t$ = tendencia, $c_t$ = factor estacional, $N$ = periodos por estación (ciclo), $\varepsilon_t$ = ruido, y $\alpha,\beta,\gamma$ = constantes de suavización del nivel, la tendencia y la estacionalidad.

$$S_t=\alpha\frac{D_t}{c_{t-N}}+(1-\alpha)(S_{t-1}+G_{t-1})$$

$$G_t=\beta(S_t-S_{t-1})+(1-\beta)G_{t-1}$$

$$c_t=\gamma\frac{D_t}{S_t}+(1-\gamma)c_{t-N}$$

$$F_{t,t+\tau}=(S_t+\tau G_t)\,c_{t+\tau-N}$$

donde $F_{t,t+\tau}$ es el pronóstico hecho en $t$ para $\tau$ periodos adelante.

*Winters multiplicativo, notación $a_0$, $a_1$, $C$ (p. 12–13).* $a_{0,t}$ = nivel, $a_{1,t}$ = tendencia, $C_t$ = factor estacional, $x_t$ = dato real, $\phi$ = constante de suavización de la tendencia. Modelo $x_t=(a_{0,t}+a_{1,t}t)C_t+\epsilon_t$.

$$a_{0,t}=\alpha\frac{x_t}{C_{t-N}}+(1-\alpha)(a_{0,t-1}+a_{1,t-1})$$

$$a_{1,t}=\phi(a_{0,t}-a_{0,t-1})+(1-\phi)a_{1,t-1}$$

$$C_t=\gamma\frac{x_t}{a_{0,t}}+(1-\gamma)C_{t-N}$$

Pronóstico: $F_t=(a_{0,t}+a_{1,t})C_t$; en el ejemplo, para $\tau$ periodos adelante, $F_{t+\tau}=(a_{0,t}+\tau a_{1,t})\,C_{t+\tau-N}$.

*Inicialización (p. 14–15), con $2N$ datos:*
- $\bar S_1=\frac{1}{N}\sum_{t=1}^{N}x_t$, $\quad\bar S_2=\frac{1}{N}\sum_{t=N+1}^{2N}x_t$ (promedios del ciclo 1 y del ciclo 2).
- Pendiente: $a_1=\dfrac{\bar S_2-\bar S_1}{N}$.
- Nivel al final del ciclo 2: $a_{0,2N}=\bar S_2+a_1\dfrac{N-1}{2}$.
- Intercepto en $t=0$: $a_0=a_{0,2N}-2N\,a_1$.
- Factor de cada periodo: $C_t=\dfrac{x_t}{a_0+a_1t}$; se promedian los factores del mismo mes de ambos ciclos.
- Normalización: $C_{t,\text{norm}}=N\dfrac{C_t}{\sum C_t}$, de modo que $\frac{1}{N}\sum_{t=1}^{N}C_t=1$.

*Winters aditivo (p. 25–26):*

$$S_t=\alpha(D_t-c_{t-N})+(1-\alpha)(S_{t-1}+G_{t-1})$$

$$G_t=\beta(S_t-S_{t-1})+(1-\beta)G_{t-1}$$

$$c_t=\gamma(D_t-S_t)+(1-\gamma)c_{t-N}$$

$$F_{t,t+\tau}=S_t+\tau G_t+c_{t+\tau-N}$$

En notación $a$: $a_{0,t}=\alpha(x_t-C_{t-N})+(1-\alpha)(a_{0,t-1}+a_{1,t-1})$, $a_{1,t}=\phi(a_{0,t}-a_{0,t-1})+(1-\phi)a_{1,t-1}$, $C_t=\gamma(x_t-a_{0,t})+(1-\gamma)C_{t-N}$, $F_t=a_{0,t}+a_{1,t}+C_t$.

*Selección y validación (p. 27–28):* separar datos de calibración y de prueba; ajustar con los de calibración (revisar indicadores y sesgos); calcular indicadores con los de prueba; verificar.

*Señal de rastreo (p. 29–30):* $e_i$ = error del periodo $i$ (real − pronóstico en el ejemplo); $n$ = número de errores.
- Error acumulado (RSFE, *running sum of forecast error*): $E_t=\sum_{i=1}^{t}e_i$.
- $MAD=\dfrac{\sum|e_i|}{n}$.
- Versión suavizada con constante $\omega$: $E_t=\omega e_t+(1-\omega)E_{t-1}$ y $MAD_t=\omega|e_t|+(1-\omega)MAD_{t-1}$, inicializando $E_0$ y $MAD_0$.
- Señal: $T_t=\dfrac{E_t}{MAD_t}$, que debe estar cerca de 0.

*Intervalo de confianza aproximado del 95 % para $F_{t+1}$ (p. 38):* $F_{t+1}\pm z_{0.95}\cdot RMSE\cdot\sqrt{\dfrac{N}{N-p}}$, donde $RMSE=\sqrt{MSE}$, $p$ = número de parámetros del método y $N$ = número de datos.

**Ejemplos resueltos:**
- p. 5: Holt aplicado a datos estacionales (8 periodos, $S_0=24$, $G_0=4$) con $\alpha=0{,}1,\ \beta=0{,}2$ (pronósticos 9–12: 60,21; 64,24; 68,27; 72,30) y con $\alpha=0{,}4,\ \beta=0{,}5$ (60,72; 64,23; 57,21*; 71,26). Ninguno sigue los ciclos.
- p. 16–22: ventas de llantas para nieve, 2 años mensuales ($N=12$). $\bar S_1=210{,}17$ (la diapositiva pone 201,16), $\bar S_2=234{,}75$, $a_1=2{,}049$, $a_{0,24}=246{,}08$, $a_0=196{,}88$. Factores normalizados de enero a diciembre: 1,00; 1,22; 1,46; 1,33; 1,21; 1,01; 0,90; 0,76; 0,65; 0,62; 0,88; 0,96. Pronósticos $F_{25}=247{,}64$, $F_{26}=305{,}21$, $F_{27}=368{,}25$. Con $x_{25}=245$ y $\alpha=\gamma=\phi=0{,}3$ se actualiza a $a_0=247{,}93$, $C=0{,}97$, $a_1=1{,}99$, y los nuevos pronósticos son $F_{26}=304{,}90$, $F_{27}=367{,}78$, $F_{28}=337{,}68$.
- p. 32–37: señal de rastreo con ventas 8, 11, 12, 14 y pronóstico fijo de 10: RSFE −2, −1, 1, 5; MAD 2; 1,5; 1,67; 2,25; señal −1; −0,67; 0,6; 2,22.
- p. 31: gráfico de suavización simple con α = 0,2 que queda por debajo de la demanda después de un salto de nivel (sesgo que pide acción correctiva).

**Páginas clave:**
- p. 4: tabla resumen de los tres métodos de suavización.
- p. 5: por qué Holt falla con estacionalidad.
- p. 8–10: modelo de Winters multiplicativo ($S,G,c$).
- p. 12–15: notación $a_0,a_1,C$, actualización e inicialización.
- p. 16–22: ejemplo numérico completo (llantas para nieve).
- p. 23: equivalencia de parámetros con Minitab.
- p. 24–26: Winters aditivo frente a multiplicativo.
- p. 27–28: selección de parámetros y validación.
- p. 29–37: señal de rastreo y ejemplo.
- p. 38: intervalo de confianza.
- p. 39: tabla comparativa de todos los métodos de pronóstico (patrón, datos, horizonte, preparación, complejidad).

**Relación con otros archivos del repo:**
- [`metodo-winters.md`](./metodo-winters.md): el Excel que resuelve el mismo ejemplo de llantas (inicialización, factores estacionales, pronósticos 25–36 y error *a posteriori*) y añade el correlograma de la demanda.
- Holt (suavización doble), base de Winters: [`../05-tendencia-suavizacion-doble-holt/L06-forecasting-data-with-trend.md`](../05-tendencia-suavizacion-doble-holt/L06-forecasting-data-with-trend.md) y [`../05-tendencia-suavizacion-doble-holt/suavizacion-exponencial-doble-holt.md`](../05-tendencia-suavizacion-doble-holt/suavizacion-exponencial-doble-holt.md).
- Suavización simple y medidas de error (MAD, MSE, MAPE): [`../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/`](../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/).
- ARIMA / Box-Jenkins, que aparece en la tabla de la p. 39: [`../07-arima/L08-forecasting-with-arima.md`](../07-arima/L08-forecasting-with-arima.md).
- Aplicación a datos reales: [`../parcial-1/`](../parcial-1/) y [`../proyecto-thyms-pronostico/`](../proyecto-thyms-pronostico/).

**Errores o inconsistencias detectados en el material:**
- p. 5 (tabla derecha): $F_{11}=57{,}21$ debería ser $67{,}74$ ($S_8+3G_8$).
- p. 17: $\bar S_1=2522/12=210{,}17$, no 201,16; el $a_1=2{,}049$ sí usa 210,17. Además $234{,}75+2{,}05\times5{,}5=246{,}03$ (la diapositiva pone 246,08).
- p. 21: con los datos dados, $a_{0,25}=0{,}3(245)+0{,}7(248{,}13)=247{,}19$ (no 247,93) y $C_{25}=0{,}3(245/247{,}93)+0{,}7=0{,}9965\approx1{,}00$ (no 0,97). Los pronósticos de la p. 22 se calculan a partir de 247,93 y 1,99.
- p. 16: noviembre del año 2 vale 209 (el total 2817 lo confirma); el Excel [`metodo-winters.md`](./metodo-winters.md) usa 208.
- p. 25: la ecuación de tendencia del aditivo tiene $S_t$ a la izquierda en vez de $G_t$, y el texto «Se resta el factor estacional $c_{t+\tau-N}$» contradice la fórmula del pronóstico, que lo suma (se resta al actualizar el nivel).
- p. 12 y 20: la fórmula general $F_t=(a_{0,t}+a_{1,t})C_t$ omite el horizonte $\tau$, pero el ejemplo sí multiplica $a_1$ por 1, 2, 3.
- p. 29: «$E_t$ -1» debe leerse $E_{t-1}$. p. 15: el subíndice «$t-1$» de la suma debe leerse $t=1$.

## Contenido completo (página por página)

### Página 1 — Operations Management: Forecasting (portada)

Operations Management · Forecasting · 2026

> [Imagen decorativa: foto del campus y logo de la Universidad de La Sabana]

### Página 2 — Lecture Objective

- To introduce forecasting methods for seasonal data, with their advantages and disadvantages.

### Página 3 — Winters method for data with seasonality patterns (separador)

Winters method for data with seasonality patterns

### Página 4 — Summary

Tabla resumen de los tres patrones de demanda y su método de suavización:

| | DEMANDA ESTACIONARIA | DEMANDA CON TENDENCIA | DEMANDA CON TENDENCIA Y ESTACIONALIDAD |
|---|---|---|---|
| Patrón (gráfico) | puntos que oscilan alrededor de una línea horizontal | puntos alineados sobre una recta creciente | puntos que oscilan (suben y bajan) alrededor de una recta creciente |
| Método | SE Simple – Promedios Móviles | SE Doble (Holt) – Regresión Lineal | SE Triple (Winters) |
| Constantes | $\alpha$ | $\alpha$, $\beta$ | $\alpha$, $\beta$, $\gamma$ |
| Inicializar | $\alpha$, $S_0$ | $\alpha$, $\beta$, $S_0$, $G_0$ | $\alpha$, $\beta$, $\gamma$, $S_0$, $G_0$ y $C_t$'s |
| Fórmula | $S_t=\alpha D_t+(1-\alpha)S_{t-1}$; $F_{t+1}=S_t$ | $F_{t,t+\tau}=S_t+\tau G_t$ | $F_{t,t+\tau}=(S_t+\tau G_t)\,c_{t+\tau-N}$ |

(SE = suavización exponencial.)

### Página 5 — What if I use Holt's method when seasonality is present?

Dos hojas de cálculo «SUAVIZACION EXPONENCIAL DOBLE / HOLT CON TENDENCIA» con la misma demanda (que tiene estacionalidad) y distintos parámetros. Inicialización en ambas: $S_0=24{,}00$, $G_0=4{,}00$.

**Tabla izquierda: ALPHA = 0,10; BETA = 0,20** (error definido como $E=F_t-D_t$)

| t | Dt | St | Gt | Ft | E=Ft-Dt | \|E\| | % | E2 |
|---|---|---|---|---|---|---|---|---|
| 0 | | 24,00 | 4,00 | | | | | |
| 1 | 20 | 27,20 | 3,84 | 28,00 | 8,00 | 8,00 | 0,40 | 64,00 |
| 2 | 40 | 31,94 | 4,02 | 31,04 | -8,96 | 8,96 | 0,22 | 80,28 |
| 3 | 44 | 36,76 | 4,18 | 35,96 | -8,04 | 8,04 | 0,18 | 64,72 |
| 4 | 32 | 40,05 | 4,00 | 40,94 | 8,94 | 8,94 | 0,28 | 79,92 |
| 5 | 30 | 42,64 | 3,72 | 44,05 | 14,05 | 14,05 | 0,47 | 197,32 |
| 6 | 60 | 47,73 | 3,99 | 46,36 | -13,64 | 13,64 | 0,23 | 185,97 |
| 7 | 66 | 53,15 | 4,28 | 51,72 | -14,28 | 14,28 | 0,22 | 203,93 |
| 8 | 45 | 56,18 | 4,03 | 57,43 | 12,43 | 12,43 | 0,28 | 154,41 |
| 9 | | | | 60,21 | | | | |
| 10 | | | | 64,24 | | | | |
| 11 | | | | 68,27 | | | | |
| 12 | | | | 72,30 | | | | |

Debajo de la tabla hay una fila de totales tapada por el gráfico: [ilegible].

> [Gráfico (izquierda): líneas, eje x = periodo 1–12, eje y = 0–80. Serie azul = demanda $D_t$ (20, 40, 44, 32, 30, 60, 66, 45 en t = 1…8); serie rosada = pronóstico $F_t$ (28,00 → 72,30), casi una recta creciente que no sigue los picos y valles de la demanda.]

**Tabla derecha: ALPHA = 0,40; BETA = 0,50** (error definido como $E=D_t-F_t$)

| t | Dt | St | Gt | Ft | E=Dt-Ft | \|E\| | % | E2 |
|---|---|---|---|---|---|---|---|---|
| 0 | | 24,00 | 4,00 | | | | | |
| 1 | 20 | 24,80 | 2,40 | 28,00 | -8,00 | 8,00 | 0,40 | 64,00 |
| 2 | 40 | 32,32 | 4,96 | 27,20 | 12,80 | 12,80 | 0,32 | 163,84 |
| 3 | 44 | 39,97 | 6,30 | 37,28 | 6,72 | 6,72 | 0,15 | 45,16 |
| 4 | 32 | 40,56 | 3,45 | 46,27 | -14,27 | 14,27 | 0,45 | 203,69 |
| 5 | 30 | 38,41 | 0,65 | 44,01 | -14,01 | 14,01 | 0,47 | 196,36 |
| 6 | 60 | 47,43 | 4,84 | 39,05 | 20,95 | 20,95 | 0,35 | 438,70 |
| 7 | 66 | 57,76 | 7,58 | 52,27 | 13,73 | 13,73 | 0,21 | 188,54 |
| 8 | 45 | 57,21 | 3,51 | 65,34 | -20,34 | 20,34 | 0,45 | 413,86 |
| 9 | | | | 60,72 | | | | |
| 10 | | | | 64,23 | | | | |
| 11 | | | | 57,21 | | | | |
| 12 | | | | 71,26 | | | | |

> [Gráfico (derecha): líneas, eje x = 1–12, eje y = 0–80. Serie azul = demanda; serie rosada = pronóstico, que reacciona con retraso a los picos (sube cuando la demanda ya bajó) y en t = 11 cae a 57,21.]

Mensaje de la diapositiva: con estacionalidad, Holt no captura las oscilaciones; con α y β bajos el pronóstico es casi una recta, y con α y β altos persigue la demanda con un periodo de retraso y los errores crecen.

> Nota del transcriptor: en la tabla derecha, $F_{11}$ debería ser $S_8+3G_8=57{,}21+3(3{,}51)=67{,}74$; el 57,21 que aparece es el valor de $S_8$ (error de la diapositiva). $F_{12}=57{,}21+4(3{,}51)=71{,}25\approx71{,}26$ sí es coherente.

### Página 6 — Winter's Method

- Demand is oscilating around a trend line

> [Gráfico «Winters Multiplicativo»: línea con marcadores, eje x = 0–30 (periodos 1–24), eje y = 0–80, serie «Dt». La demanda tiene un ciclo de 3 periodos (pico, valor medio, valle) alrededor de una tendencia creciente, y la amplitud de las oscilaciones crece con el nivel. Valores aproximados leídos del gráfico: 15, 14, 12, 22.5, 20, 16.5, 30, 26, 21, 37.5, 32, 25.5, 45, 38, 30, 52.5, 44, 34.5, 60, 50, 39, 67.5, 56, 43.5.]

### Página 7 — Winter's Method

- Multiplicative version
  - Level component: average
  - Trend component: increase / decrease
  - Season component
- The components are continuously updated with a smoothing constant, applied to the most recent data and its forecast.

### Página 8 — Winters method

- La serie tiene una estacionalidad cuyo periodo es $N$
- La demanda se comporta como $D_t = c_t S_t + \varepsilon_t$
- donde $c_t$ es un FACTOR ESTACIONAL y $S_t$ corresponde a los puntos sobre la recta. $\varepsilon_t$ es el ruido o error.
- Este es el **modelo multiplicativo**.

### Página 9 — Método de Winters

- Definiciones:
- Nivel de la serie de tiempo en $t$: $S_t$
- Tendencia de la serie de tiempo en $t$: $G_t$
- Índice estacional en $t$: $c_t$
- Parámetro de suavización de nivel: $\alpha$
- Parámetro de suavización de tendencia: $\beta$
- Parámetro de suavización de índice estacional: $\gamma$

### Página 10 — Método de Winters

- Modelo:

$$S_t=\alpha\frac{D_t}{c_{t-N}}+(1-\alpha)\left(S_{t-1}+G_{t-1}\right)$$

$$G_t=\beta\left(S_t-S_{t-1}\right)+(1-\beta)G_{t-1}$$

$$c_t=\gamma\frac{D_t}{S_t}+(1-\gamma)c_{t-N}$$

- Pronóstico:

$$F_{t,t+\tau}=\left(S_t+\tau G_t\right)c_{t+\tau-N}$$

- Escogencia de $\alpha$, $\beta$ y $\gamma$

### Página 11 — Suavización exponencial triple

> [Gráfico «Demanda vs Tiempo»: eje x = 0–9, eje y = 0–35. Tres series: «Demanda» (azul oscuro, rombos): 10, 20, 26, 17, 11, 19, 27, 18 en t = 1…8; «Pronóstico (a= b= g = 0.1)» (rosado discontinuo, cuadros), valores aproximados 9.3, 18.6, 24.7, 17.3, 13.2, 25.3, 32.3, 21.8; «Lineal (Demanda)» (línea de tendencia negra) que sube de ≈15.8 en t = 1 a ≈21.2 en t = 8. El pronóstico de Winters reproduce el patrón estacional (ciclo de 4 periodos) alrededor de la tendencia; en t = 6 y 7 sobreestima.]

(Esta diapositiva no tiene el pie de página de la universidad.)

### Página 12 — Método de Winters

$$x_t=\left(a_{0,t}+a_{1,t}\,t\right)C_t+\epsilon_t$$

Sea:
- $C_t$: el factor estacional
- $x_t$: Dato real en el periodo t
- $N$: Número de periodos en la estación
- $\alpha$: Constante de suavización para el parámetro $a_{0,t}$
- $\phi$: Constante de suavización para el parámetro $a_{1,t}$
- $\gamma$: Constante de suavización para el parámetro $C_t$
- Pronóstico: $F_t=\left(a_{0,t}+a_{1,t}\right)C_t$

### Página 13 — Método de Winters

$a_{0,t}$, $a_{1,t}$ y $C_t$ son continuamente actualizados

**Procedimiento de actualización de parámetros:**

$a_{0,t}$: nivel suavizado exponencialmente para el proceso al final del periodo $t$

$$a_{0,t}=\alpha\frac{x_t}{C_{t-N}}+(1-\alpha)\left(a_{0,t-1}+a_{1,t-1}\right)$$

$x_t$: demanda actual en el periodo $t$; $N$: periodos de la estación.

$a_{1,t-1}$: Tendencia para el periodo $t-1$

$$a_{1,t}=\phi\left(a_{0,t}-a_{0,t-1}\right)+(1-\phi)\,a_{1,t-1}$$

$$C_t=\gamma\frac{x_t}{a_{0,t}}+(1-\gamma)\,C_{t-N}$$

### Página 14 — Método de Winters (inicialización)

**Inicialización de parámetros:**

1. Cálculo de las pendientes de históricas de los datos en cada ciclo:
   - $\bar S_1=\dfrac{\sum_{t=1}^{N}x_t}{N}$, $\quad\bar S_2=\dfrac{\sum_{t=N+1}^{2N}x_t}{N}$
   - $a_1=\dfrac{\bar S_2-\bar S_1}{N}$
2. Cálculo del nivel:
   - $a_{0,2N}=\bar S_2+a_1\dfrac{N-1}{2}$
3. Cálculo del factor de estacionalidad:
   - $C_t=\dfrac{x_t}{a_0+a_1 t}$, considerando $a_0=a_{0,2N}-(2N)\,a_1$

### Página 15 — Método de Winters (normalización)

4. Normalizar los factores estacionales de tal forma que:

$$\frac{\sum_{t=1}^{N}C_t}{N}=1$$

(En la diapositiva el subíndice de la suma aparece como «$t-1$»; se entiende $t=1$.)

### Página 16 — Ejemplo numérico

- Considere los siguientes datos de ventas de llantas para la nieve de los últimos dos años:

| mes | año 1 | año 2 |
|---|---|---|
| Enero | 195 | 229 |
| Febrero | 252 | 271 |
| Marzo | 299 | 333 |
| Abril | 276 | 305 |
| Mayo | 258 | 277 |
| Junio | 210 | 239 |
| Julio | 192 | 211 |
| Agosto | 154 | 193 |
| Septiembre | 141 | 155 |
| Octubre | 128 | 159 |
| Noviembre | 200 | 209 |
| Diciembre | 217 | 236 |
| **Total** | **2522** | **2817** |

> [Gráfico «Demanda Mensual de llantas para la nieve»: líneas, eje x = Enero…Diciembre, eje y = 100–350. Serie «año 1» (azul) y «año 2» (naranja). Ambas suben de enero a un máximo en marzo (299 y 333), bajan hasta un mínimo en octubre (128) / septiembre-octubre (155–159) y repuntan en noviembre-diciembre. El año 2 está por encima del año 1 en todos los meses (tendencia creciente).]

### Página 17 — Ejemplo numérico: inicialización de parámetros

- Pendiente:
  - $\bar S_1=\dfrac{\sum_{t=1}^{N}x_t}{N}=\dfrac{2522}{12}=201.16$
  - $\bar S_2=\dfrac{\sum_{t=N+1}^{2N}x_t}{N}=\dfrac{2817}{12}=234.75$
  - $a_1=\dfrac{\bar S_2-\bar S_1}{N}=\left(\dfrac{234.75-201.16}{12}\right)=2.049$
- Nivel:
  - $a_{0,2N}=\bar S_2+a_1\dfrac{N-1}{2}=234.75+2.05\left(\dfrac{11}{2}\right)=246.08$
- Estacionalidad:
  - $a_0=a_{0,2N}-(2N)\,a_1=246.08-(24)(2.05)=196.88$

> Nota del transcriptor: $2522/12=210{,}17$, no 201,16 (dígitos transpuestos). El resultado $a_1=2{,}049$ sí corresponde a $(234{,}75-210{,}17)/12$. Además $234{,}75+2{,}05\times5{,}5=246{,}03$; la diapositiva usa 246,08.

### Página 18 — Factores de estacionalidad

| t (año 1) | a(0) + a(1)t | C(t) = X(t) / (a(0) + a(1)t) | t (año 2) | a(0) + a(1)t | C(t) = X(t) / (a(0) + a(1)t) | Ct (promedio) |
|---|---|---|---|---|---|---|
| 1 | 198,93 | 0,98 | 13 | 223,53 | 1,02 | 1,00 |
| 2 | 200,98 | 1,25 | 14 | 225,58 | 1,20 | 1,23 |
| 3 | 203,03 | 1,47 | 15 | 227,63 | 1,46 | 1,47 |
| 4 | 205,08 | 1,35 | 16 | 229,68 | 1,33 | 1,34 |
| 5 | 207,13 | 1,25 | 17 | 231,73 | 1,20 | 1,22 |
| 6 | 209,18 | 1,00 | 18 | 233,78 | 1,02 | 1,01 |
| 7 | 211,23 | 0,91 | 19 | 235,83 | 0,89 | 0,90 |
| 8 | 213,28 | 0,72 | 20 | 237,88 | 0,81 | 0,77 |
| 9 | 215,33 | 0,65 | 21 | 239,93 | 0,65 | 0,65 |
| 10 | 217,38 | 0,59 | 22 | 241,98 | 0,66 | 0,62 |
| 11 | 219,43 | 0,91 | 23 | 244,03 | 0,86 | 0,88 |
| 12 | 221,48 | 0,98 | 24 | 246,08 | 0,96 | 0,97 |

La última columna $C_t$ es el promedio de los dos factores del mismo mes (año 1 y año 2).

### Página 19 — Factores de estacionalidad (normalizados)

| t (año 1) | Ct Normalizado |
|---|---|
| 1 | 1,00 |
| 2 | 1,22 |
| 3 | 1,46 |
| 4 | 1,33 |
| 5 | 1,21 |
| 6 | 1,01 |
| 7 | 0,90 |
| 8 | 0,76 |
| 9 | 0,65 |
| 10 | 0,62 |
| 11 | 0,88 |
| 12 | 0,96 |

$$C_{t,\text{normalizado}}=N\cdot\frac{C_t}{\sum C_t}$$

### Página 20 — Método de Winters (pronóstico)

- Pronóstico:
  - $F_t=\left(a_{0,t}+a_{1,t}\right)C_t$
  - $F_{25}=\big(246.08+(2.05)(1)\big)(1.00)=247.64$
  - $F_{26}=\big(246.08+(2.05)(2)\big)(1.22)=305.21$
  - $F_{27}=\big(246.08+(2.05)(3)\big)(1.46)=368.25$

$F_{25}$: ¿Qué periodo, qué año? (en rojo; respuesta deducida: enero del año 3).

> Nota del transcriptor: en el ejemplo la tendencia se multiplica por el horizonte $\tau=1,2,3$, es decir $F_{24+\tau}=(a_{0,24}+\tau a_{1,24})\,C_{24+\tau-N}$. $(248{,}13)(1{,}00)=248{,}13$; el 247,64 sale de usar el factor sin redondear (≈0,998).

### Página 21 — ¿Cuándo se pueden actualizar los parámetros?

- Cuando se conozca información más reciente del ciclo.
- Ejemplo:
  - $x_{25}=245$
  - $\alpha=\gamma=\phi=0.3$ (fijados experimentalmente)
  - $a_0=0.3\left(\dfrac{245}{1.00}\right)+(0.7)(246.08+2.05)=247.93$
  - $C_t=0.3\left(\dfrac{245}{247.93}\right)+0.7(1.00)=0.97$
  - $a_1=0.3(247.93-246.08)+0.7(2.05)=1.99$

> Nota del transcriptor: con esos números, $0{,}3(245)+0{,}7(248{,}13)=73{,}5+173{,}69=247{,}19$ (no 247,93), y $0{,}3(245/247{,}93)+0{,}7=0{,}9965\approx1{,}00$ (no 0,97). El valor $a_1=1{,}99$ es coherente con el 247,93 de la diapositiva.

### Página 22 — Nuevos pronósticos

- $F_t=\left(a_{0,t}+a_{1,t}\right)C_t$
- $F_{26}=[247.93+(1.99)(1)]\,(1.22)=304.90$
- $F_{27}=367.78$
- $F_{28}=337.68$

(Comprobación: $F_{27}=(247{,}93+2\times1{,}99)(1{,}46)=367{,}79$; $F_{28}=(247{,}93+3\times1{,}99)(1{,}33)=337{,}69$.)

### Página 23 — Minitab

- Parámetro de tendencia γ
  - En nuestro caso lo llamamos $\phi$
- Parámetro de estacional δ
  - En nuestro caso lo llamamos $\gamma$

(Equivalencia de nombres entre Minitab y la clase: Minitab usa α nivel, γ tendencia, δ estacional.)

### Página 24 — Winter's Aditivo vs Multiplicativo

> [Gráfico izquierdo «Winters Multiplicativo»: el mismo de la página 6 (serie Dt, 24 periodos, ciclo de 3 periodos alrededor de una tendencia creciente; la amplitud de la oscilación crece con el nivel, de ≈3 unidades al inicio a ≈24 al final).]

> [Gráfico derecho «Winters Aditivo»: línea morada con marcadores en «x», «Serie 1», eje x = 0–30, eje y = 0–70. Ciclo de 3 periodos alrededor de una tendencia creciente con amplitud constante. Valores aproximados: 22, 8, 12, 28, 14, 18, 34, 20, 24, 40, 26, 30, 46, 32, 36, 52, 38, 42, 58, 44, 48, 64, 50, 54.]

Idea: en el multiplicativo la estacionalidad es proporcional al nivel (oscilación cada vez mayor); en el aditivo es una cantidad fija que se suma o resta (oscilación de tamaño constante).

### Página 25 — Método de Winters Aditivo

- Modelo:

$$S_t=\alpha\left(D_t-c_{t-N}\right)+(1-\alpha)\left(S_{t-1}+G_{t-1}\right)$$

$$S_t=\beta\left(S_t-S_{t-1}\right)+(1-\beta)G_{t-1}$$

$$c_t=\gamma\left(D_t-S_t\right)+(1-\gamma)c_{t-N}$$

- Pronóstico:

$$F_{t,t+\tau}=\left(S_t+\tau G_t+c_{t+\tau-N}\right)$$

- ✓ Se resta el factor estacional $c_{t+\tau-N}$

> Nota del transcriptor: la segunda ecuación debería tener $G_t$ a la izquierda ($G_t=\beta(S_t-S_{t-1})+(1-\beta)G_{t-1}$). El factor estacional se **resta** de la demanda al actualizar el nivel y se **suma** en el pronóstico.

### Página 26 — Método de Winters Aditivo (notación $a_0$, $a_1$, $C$)

- $F_t=a_{0,t}+a_{1,t}+C_t$
- $a_{0,t}=\alpha\left(x_t-C_{t-N}\right)+(1-\alpha)\left(a_{0,t-1}+a_{1,t-1}\right)$
- $a_{1,t}=\phi\left(a_{0,t}-a_{0,t-1}\right)+(1-\phi)\,a_{1,t-1}$
- $C_t=\gamma\left(x_t-a_{0,t}\right)+(1-\gamma)\,C_{t-N}$

(Los términos que cambian respecto al multiplicativo están resaltados en azul: $+C_t$, $x_t-C_{t-N}$ y $x_t-a_{0,t}$.)

### Página 27 — ¿Cómo seleccionar los parámetros de un método o entre varios métodos de pronóstico?

- No es tan simple como hallar los parámetros que minimicen el DAM o el MSE para una serie de tiempo.
- ¿Qué hace falta?
  - Evaluar el método con otros datos
  - Evaluar sesgos

### Página 28 — Evaluar método con otros datos

1. Tomar datos de (1) calibración y de (2) prueba
2. Ajustar los parámetros y el modelo con los datos de calibración. (Verificar indicadores y sesgos)
3. Calcular indicadores con los datos de prueba
4. Verificar

### Página 29 — Señal de seguimiento: Tracking Signal

Concepts
- Cumulative error: $E_t=\sum e_i$, $\quad i=1\ldots t$
- MAD: $=\sum |e_i|/n$
- Alternatively (smoothing model):
  - $E_t=\omega e_t+(1-\omega)E_{t-1}$
  - $MAD_t=\omega|e_t|+(1-\omega)MAD_{t-1}$
- Initialize $E_0$ y $MAD_0$

(En la diapositiva la primera ecuación suavizada aparece como «$E_t$ -1»; se entiende $E_{t-1}$. $\omega$ es la constante de suavización del error.)

### Página 30 — Detección de sesgos y señal de rastreo

- *Tracking signal*

$$T_t=\frac{E_t}{MAD_t}$$

- The tracking signal should be close to 0.
- If not, you must update the parameters or adjust the method.

### Página 31 — Corrective Actions

- Change the parameters of the forecasting method
- Change the forecasting method

> [Gráfico: líneas, eje x = Tiempo 1–12, eje y = Valores 15–33. Serie «Demanda» (azul): 20, 22, 21, 22, 23, 22, 28, 29, 31, 32, 31, 30. Serie «Ft (a cte = 0.2)» (rosada, suavización exponencial simple con α = 0,2): ≈21.7, 21.3, 21.5, 21.4, 21.5, 21.8, 21.8, 23.1, 24.3, 25.6, 26.9, 27.7. A partir de t = 7 la demanda salta a un nivel más alto y el pronóstico queda sistemáticamente por debajo (sesgo): es la situación que la señal de rastreo detecta y que exige acciones correctivas.]

### Página 32 — Example

- Consider the following historical data and historical forecast

| Month | Actual Sales | Forecast Sales |
|---|---|---|
| 1 | 8 | 10 |
| 2 | 11 | 10 |
| 3 | 12 | 10 |

### Página 33 — Example (RSFE, mes 1)

- Consider the following historical data and historical forecast. RSFE: Running sum of forecast error

| Month | Actual Sales | Forecast Sales | Forecast Error | RSFE |
|---|---|---|---|---|
| 1 | 8 | 10 | **-2** | **-2** |
| 2 | 11 | 10 | | |
| 3 | 12 | 10 | | |
| 4 | 14 | 10 | | |

(Error = real − pronóstico.)

### Página 34 — Example (mes 2)

| Month | Actual Sales | Forecast Sales | Forecast Error | RSFE |
|---|---|---|---|---|
| 1 | 8 | 10 | -2 | -2 |
| 2 | 11 | 10 | **1** | **-1** |
| 3 | 12 | 10 | | |
| 4 | 14 | 10 | | |

### Página 35 — Example (mes 3)

| Month | Actual Sales | Forecast Sales | Forecast Error | RSFE |
|---|---|---|---|---|
| 1 | 8 | 10 | -2 | -2 |
| 2 | 11 | 10 | 1 | -1 |
| 3 | 12 | 10 | **2** | **1** |
| 4 | 14 | 10 | | |

### Página 36 — Example (mes 4)

| Month | Actual Sales | Forecast Sales | Forecast Error | RSFE |
|---|---|---|---|---|
| 1 | 8 | 10 | -2 | -2 |
| 2 | 11 | 10 | 1 | -1 |
| 3 | 12 | 10 | 2 | 1 |
| 4 | 14 | 10 | **4** | **5** |

### Página 37 — Example (Computation of Tracking signal)

- Consider the following historical data and historical forecast
- Computation of Tracking signal

| Month | Actual Sales | Forecast Sales | RSFE | Absolute Error | MAD | Tracking Signal |
|---|---|---|---|---|---|---|
| 1 | 8 | 10 | -2 | 2 | 2 | -1 |
| 2 | 11 | 10 | -1 | 1 | 1.5 | -0.67 |
| 3 | 12 | 10 | 1 | 2 | 1.67 | 0.6 |
| 4 | 14 | 10 | 5 | **4** | **2.25** | **2.22** |

$MAD_t$ es el promedio acumulado de los errores absolutos ($2$; $(2+1)/2=1.5$; $(2+1+2)/3=1.67$; $(2+1+2+4)/4=2.25$) y $T_t=RSFE_t/MAD_t$ ($-2/2=-1$; $-1/1.5=-0.67$; $1/1.67=0.6$; $5/2.25=2.22$). La señal crece porque el pronóstico fijo de 10 se queda corto ante ventas crecientes.

### Página 38 — Confidence interval for tracking signal

- Un intervalo aproximado del 95% confianza para $F_{t+1}$ es

$$F_{t+1}\pm z_{0.95}\times RMSE\times\sqrt{\frac{N}{N-p}}$$

donde $p$ es el número de parámetros del método de pronóstico. RMSE: Root-mean-square deviation: Square-root of MSE.

- I.C, para más de un periodo son complicados, se utilizan para un solo periodo

(La diapositiva muestra solo la semiamplitud $z_{0.95}\times RMSE\times\sqrt{N/(N-p)}$; $N$ es el número de datos usados para calcular el RMSE.)

### Página 39 — Comparación Métodos de Pronósticos

| MÉTODO | PATRÓN DE DATOS | CANTIDAD DE DATOS HISTÓRICOS | HORIZONTE DEL PRONÓSTICO | TIEMPO DE PREPARACIÓN | COMPLEJIDAD |
|---|---|---|---|---|---|
| SUAVIZACIÓN EXPONENCIAL SIMPLE | ESTACIONARIO | 10-15 Observaciones | CORTO | CORTO | POCA |
| SUAVIZACIÓN EXPONENCIAL HOLT | CON TENDENCIA SIN ESTACIONALIDAD | 15-20 Observaciones | CORTO A MEDIO | CORTO | LIGERA |
| SUAVIZACIÓN EXPONENCIAL WINTERS | CON TENDENCIA Y ESTACIONALIDAD | Al menos 4 observaciones por ciclo estacional; 2 Ciclos estacionales | CORTO A MEDIO | CORTO | MODERADA |
| REGRESIÓN | RELACIONES COMPLEJAS | 20 Observaciones | CORTO, MEDIO O LARGO | CORTO A MODERADO | MAYOR |
| DESCOMPOSICIÓN | CON TENDENCIA Y ESTACIONALIDAD | Al menos 4 observaciones por ciclo estacional; 2 Ciclos estacionales | CORTO A MEDIO | CORTO A MODERADO | MODERADA |
| BOX & JENKINS | ESTACIONARIOS O TRANSFORMADOS A ESTACIONARIOS | 50 o más observaciones | CORTO, MEDIO O LARGO | LARGO | CONSIDERABLE |
| ARIMA | PATRONES COMPLEJOS AUTOREGRESIVOS | 50 o más observaciones | CORTO, MEDIO O LARGO | LARGO | CONSIDERABLE |

### Página 40 — Cierre

- Gracias!

William Guerrero, Ph.D.

## Anexo: texto extraído automáticamente del PDF

> Texto plano tal como sale del PDF, sin fórmulas ni tablas que estén como imagen. La versión fiel y completa es la sección «Contenido completo» de arriba.

### Página 1 · 2 imagen(es)

Operations Management 
Forecasting
2026

### Página 2 · 1 imagen(es)

Lecture Objective
• To introduce forecasting methods for 
seasonal data, with their advantages and 
disadvantages.

### Página 3 · 1 imagen(es)

Winters method for data with 
seasonality patterns

### Página 4 · 2 imagen(es)

Summary

### Página 5 · 2 imagen(es)

What if I use Holt’s method when seasonality
 is present?

### Página 6 · 1 imagen(es)

Winter’s Method
• Demand is oscilating around a trend line
Winters Multiplicativo
0
10
20
30
40
50
60
70
80
0
5
10
15
20
25
30
Dt

### Página 7 · 1 imagen(es)

Winter’s Method
• Multiplicative version
– Level component: average
– Trend component: increase / decrease
– Season component 
• The components are continuously updated with 
a smoothing constant, applied to the most recent 
data and its forecast.

### Página 8 · 1 imagen(es)

Winters method
• La serie tiene una estacionalidad cuyo periodo es N
• La demanda se comporta como Dt = ct St + t 
• donde ct es un FACTOR ESTACIONAL y St corresponde a 
los puntos sobre la recta. t es el ruido o error. 
• Este es el modelo multiplicativo.

### Página 9 · 1 imagen(es)

Método de Winters
• Definiciones:
• Nivel de la serie de tiempo en t: St
• Tendencia de la serie de tiempo en t: Gt
• Índice estacional en t: ct
• Parámetro de suavización de nivel: 
• Parámetro de suavización de tendencia :
• Parámetro de suavización de índice estacional: 

### Página 10 · 1 imagen(es)

Método de Winters
•
Modelo:
•
Pronóstico:
•
Escogencia de   y 
(
)(
)
1
1
1
−
−
−
+
−
+
=
t
t
N
t
t
t
G
S
c
D
S


(
) (
)
1
1
1
−
−
−
+
−
=
t
t
t
t
G
S
S
G


(
)
N
t
t
t
t
t
c
G
S
F
−
+
+
+
=



,
(
)
N
t
t
t
t
c
S
D
c
−
−
+
=


1

### Página 11

Suavización exponencial triple
0
5
10
15
20
25
30
35
0
1
2
3
4
5
6
7
8
9
Demanda vs Tiempo
Demanda
Pronóstico (a= b= g = 0.1)
Lineal (Demanda)

### Página 12 · 1 imagen(es)

Método de Winters
𝑥𝑡= 𝑎𝑜,𝑡+ 𝑎1,𝑡𝑡𝐶𝑡+ 𝜖𝑡
Sea: 
• 𝐶𝑡 : el factor estacional
• 𝑥𝑡: Dato real en el periodo t
• 𝑁: Número de periodos en la estación
• 𝛼: Constante de suavización para el parámetro 𝑎0,𝑡
• 𝜙: Constante de suavización para el parámetro 𝑎1,𝑡
• 𝛾: Constante de suavización para el parámetro 𝐶𝑡
• Pronóstico: 𝐹t = 𝑎0,𝑡+ 𝑎1,𝑡𝐶𝑡

### Página 13

Método de Winters
𝑎0,𝑡, 𝑎1,𝑡 𝑦 𝐶𝑡 𝑠𝑜𝑛 𝑐𝑜𝑛𝑡𝑖𝑛𝑢𝑎𝑚𝑒𝑛𝑡𝑒 𝑎𝑐𝑡𝑢𝑎𝑙𝑖𝑧𝑎𝑑𝑜𝑠
Procedimiento de actualización de parámetros:
𝑎0,𝑡: nivel suavizado exponencialmente para el proceso al 
final del periodo t
𝑎0,𝑡= 𝛼𝑥𝑡
𝐶𝑡−𝑁
+ 1 −𝛼(𝑎𝑜,𝑡−1 + 𝑎1,𝑡−1)
𝑥𝑡: 𝑑𝑒𝑚𝑎𝑛𝑑𝑎 𝑎𝑐𝑡𝑢𝑎𝑙 𝑒𝑛 𝑒𝑙 𝑝𝑒𝑟𝑖𝑜𝑑𝑜 𝑡 
𝑁: 𝑃𝑒𝑟𝑖𝑜𝑑𝑜𝑠 𝑑𝑒 𝑙𝑎 𝑒𝑠𝑡𝑎𝑐𝑖ó𝑛
𝑎1,𝑡−1: Tendencia para el periodo t-1
𝑎1,𝑡= 𝜙𝑎0,𝑡−𝑎0,𝑡−1 + 1 −𝜙𝑎1,𝑡−1
𝐶𝑡= 𝛾𝑥𝑡
𝑎0,𝑡
+ 1 −𝛾𝐶𝑡−𝑁

### Página 14 · 1 imagen(es)

Método de Winters
Inicialización de parámetros:
1.
Cálculo de las pendientes de históricas de los datos en 
cada ciclo:
–
ഥ𝑺𝟏=
σ𝒕=𝟏
𝑵
𝒙𝒕
𝑵
, ഥ𝑺𝟐=
σ𝒕=𝑵+𝟏
𝟐𝑵
𝒙𝒕
𝑵
–
𝑎1 =
ഥ𝑺2 −ഥ𝑺1
𝑁
2.
Cálculo del nivel:
–
𝑎0,2𝑁= ഥ𝑺𝟐+ 𝒂𝟏
𝑵−𝟏
𝟐 
3.
Cálculo del factor de estacionalidad:
–
𝐶𝑡=
𝑥𝑡
𝑎0+𝑎1𝑡, considerando 𝑎0 = 𝑎0,2𝑁 −2𝑁𝑎1

### Página 15 · 1 imagen(es)

Método de Winters
4. Normalizar los factores estacionales de tal 
forma que:
σ𝑡−1
𝑁
𝐶𝑡
𝑁
= 1

### Página 16 · 2 imagen(es)

Ejemplo numérico
• Considere los siguientes datos de ventas de llantas para 
la nieve de los últimos dos años:
mes
año 1
año 2
Enero
195
229
Febrero
252
271
Marzo
299
333
Abril
276
305
Mayo
258
277
Junio
210
239
Julio
192
211
Agosto
154
193
Septiembre
141
155
Octubre
128
159
Noviembre
200
209
Diciembre
217
236
Total
2522
2817

### Página 17 · 1 imagen(es)

Ejemplo numérico: inicialización de 
parámetros
• Pendiente:
–
ഥ𝑺𝟏=
σ𝒕=𝟏
𝑵
𝒙𝒕
𝑵
=
𝟐𝟓𝟐𝟐
𝟏𝟐= 𝟐𝟎𝟏. 𝟏𝟔
–
ഥ𝑺𝟐=
σ𝒕=𝑵+𝟏
𝟐𝑵
𝒙𝒕
𝑵
=
𝟐𝟖𝟏𝟕
𝟏𝟐= 𝟐𝟑𝟒. 𝟕𝟓
–
𝑎1 =
ഥ𝑺2 −ഥ𝑺1
𝑁
=
234.75−201.16
12
= 2.049
• Nivel:
– 𝑎0,2𝑁= ഥ𝑺𝟐+ 𝒂𝟏
𝑵−𝟏
𝟐
= 234.75 + 2.05
11
2
= 246.08 
• Estacionalidad:
– 𝑎0 = 𝑎0,2𝑁 −2𝑁𝑎1 = 246.08 −24
2.05 = 196.88

### Página 18 · 1 imagen(es)

Factores de estacionalidad
t (año 1) a(0) + a(1)t
C(t) = X(t) / 
 (a(0) + a(1)t)
t (año 2) a(0) + a(1)t
C(t) = X(t) / 
 (a(0) + a(1)t)
Ct
1
198,93
0,98
13
223,53
1,02
1,00
2
200,98
1,25
14
225,58
1,20
1,23
3
203,03
1,47
15
227,63
1,46
1,47
4
205,08
1,35
16
229,68
1,33
1,34
5
207,13
1,25
17
231,73
1,20
1,22
6
209,18
1,00
18
233,78
1,02
1,01
7
211,23
0,91
19
235,83
0,89
0,90
8
213,28
0,72
20
237,88
0,81
0,77
9
215,33
0,65
21
239,93
0,65
0,65
10
217,38
0,59
22
241,98
0,66
0,62
11
219,43
0,91
23
244,03
0,86
0,88
12
221,48
0,98
24
246,08
0,96
0,97

### Página 19 · 1 imagen(es)

Factores de estacionalidad 
(normalizados)
t (año 1)
Ct 
Normalizado
1
1,00
2
1,22
3
1,46
4
1,33
5
1,21
6
1,01
7
0,90
8
0,76
9
0,65
10
0,62
11
0,88
12
0,96
𝐶𝑡,𝑛𝑜𝑟𝑚𝑎𝑙𝑖𝑧𝑎𝑑𝑜= 𝑁 ∗𝐶𝑡
σ 𝐶𝑡

### Página 20 · 1 imagen(es)

Método de Winters
• Pronóstico:
– 𝐹t = 𝑎0,𝑡+ 𝑎1,𝑡𝐶𝑡
– 𝐹25 = 246.08 + 2.05
1
1.00 = 247.64
– 𝐹26 = 246.08 + 2.05
2
1.22 = 305.21
– 𝐹27 = 246.08 + 2.05
3
1.46 = 368.25
𝐹25: Qué periodo, qué año?

### Página 21 · 1 imagen(es)

¿Cuándo se pueden actualizar los 
parámetros?
• Cuando se conozca información más reciente del 
ciclo.
• Ejemplo: 
– 𝑥25 = 245
– 𝛼= 𝛾= 𝜙= 0.3 (fijados experimentalmente)
– 𝑎0 = 0.3
245
1.00 + 0.7
246.08 + 2.05 = 247.93 
– 𝐶𝑡= 0.3
245
247.93 + 0.7 1.00 = 0.97
– 𝑎1 = 0.3 247.93 −246.08 + 0.7 2.05 = 1.99

### Página 22 · 1 imagen(es)

Nuevos pronósticos
• 𝐹t = 𝑎0,𝑡+ 𝑎1,𝑡𝐶𝑡
• 𝐹26 = 247.93 + 1.99
1
1.22 = 304.90
• 𝐹27 = 367.78
• 𝐹28 = 337.68

### Página 23 · 1 imagen(es)

Minitab
• Parámetro de tendencia γ 
– En nuestro caso lo llamamos 𝜙
• Parámetro de estacional δ 
– En nuestro caso lo llamamos 𝛾

### Página 24 · 2 imagen(es)

Winter’s Aditivo vs Multiplicativo

### Página 25 · 1 imagen(es)

Método de Winters Aditivo
•
Modelo:
𝑆𝑡= 𝛼𝐷𝑡−𝑐𝑡−𝑁+ 1 −𝛼
𝑆𝑡−1 + 𝐺𝑡−1
𝑆𝑡= 𝛽𝑆𝑡−𝑆𝑡−1 + (1 −𝛽)𝐺𝑡−1
𝑐𝑡= 𝛾𝐷𝑡−𝑆𝑡+ (1 −𝛾)𝑐𝑡−𝑁
•
Pronóstico: 
𝐹𝑡,𝑡+𝜏= 𝑆𝑡+ 𝜏𝐺𝑡+ 𝑐𝑡+𝜏−𝑁
✓Se resta el factor estacional 𝑐𝑡+𝜏−𝑁

### Página 26 · 1 imagen(es)

Método de Winters Aditivo
• 𝐹t = 𝑎0,𝑡+ 𝑎1,𝑡+ 𝐶𝑡
• 𝑎0,𝑡= 𝛼(𝑥𝑡 −𝐶𝑡−𝑁) + 1 −𝛼(𝑎𝑜,𝑡−1 + 𝑎1,𝑡−1)
• 𝑎1,𝑡= 𝜙𝑎0,𝑡−𝑎0,𝑡−1 + 1 −𝜙𝑎1,𝑡−1
• 𝐶𝑡= 𝛾(𝑥𝑡−𝑎0,𝑡) + 1 −𝛾𝐶𝑡−𝑁

### Página 27 · 1 imagen(es)

¿Cómo seleccionar los parámetros de un método o entre 
varios métodos de pronóstico? 
• No es tan simple como hallar los parámetros que 
minimicen el DAM o el MSE para una serie de 
tiempo. 
• ¿Qué hace falta?
– Evaluar el método con otros datos
– Evaluar sesgos

### Página 28 · 1 imagen(es)

Evaluar método con otros datos 
1. Tomar datos de (1) calibración y de (2) prueba 
2. Ajustar los parámetros y el modelo con los datos 
de calibración. (Verificar indicadores y sesgos) 
3. Calcular indicadores con los datos de prueba 
4. Verificar

### Página 29 · 1 imagen(es)

Señal de seguimiento: Tracking Signal 
Concepts 
• Cumulative error: Et = ∑ ei i = 1...t
• MAD: = ∑ |ei|/ n
• Alternatively (smoothing model): 
– Et = ω et + (1- ω) Et -1
– MADt = ω |et | + (1-ω) MADt-1 
• Initialize E0 y MAD0

### Página 30 · 1 imagen(es)

Detección de sesgos y señal de rastreo
• Tracking signal 
Tt = Et / MADt 
• The tracking signal should be 
close to 0. 
• If not, you must update the 
parameters or adjust the method.

### Página 31 · 2 imagen(es)

Corrective Actions
• Change the parameters of the forecasting method
• Change the forecasting method

### Página 32 · 1 imagen(es)

Example
• Consider the following historical data and historical 
forecast
Actual
Forecast
Month
Sales
Sales
1
8
10
2
11
10
3
12
10

### Página 33 · 1 imagen(es)

Example
• Consider the following historical data and historical 
forecast. RSFE: Running sum of forecast error
Actual
Forecast Forecast
Month
Sales
Sales
Error
RSFE
1
8
10
-2
-2
2
11
10
3
12
10
4
14
10

### Página 34 · 1 imagen(es)

Example
• Consider the following historical data and historical 
forecast
Actual
Forecast Forecast
Month
Sales
Sales
Error
RSFE
1
8
10
-2
-2
2
11
10
1
-1
3
12
10
4
14
10

### Página 35 · 1 imagen(es)

Example
• Consider the following historical data and historical 
forecast
Actual
Forecast Forecast
Month
Sales
Sales
Error
RSFE
1
8
10
-2
-2
2
11
10
1
-1
3
12
10
2
1
4
14
10

### Página 36 · 1 imagen(es)

Example
• Consider the following historical data and historical 
forecast
Actual
Forecast Forecast
Month
Sales
Sales
Error
RSFE
1
8
10
-2
-2
2
11
10
1
-1
3
12
10
2
1
4
14
10
4
5

### Página 37 · 1 imagen(es)

Example
• Consider the following historical data and historical 
forecast
• Computation of Tracking signal
Actual
Forecast
Absolute
Tracking
Month
Sales
Sales
RSFE
Error
MAD
Signal
1
8
10
-2
2
2
-1
2
11
10
-1
1
1.5
-0.67
3
12
10
1
2
1.67
0.6
4
14
10
5
4
2.25
2.22

### Página 38 · 2 imagen(es)

Confidence interval for tracking signal
• Un intervalo aproximado del 95% confianza para Ft+1 es 
 donde p es el número de parámetros del método de pronóstico
 RMSE: Root-mean-square deviation : Square-root of MSE.
• I.C, para más de un periodo son complicados, se utilizan 
para un solo periodo

### Página 39 · 2 imagen(es)

Comparación Métodos de Pronósticos

### Página 40 · 1 imagen(es)

• Gracias!
William Guerrero, Ph.D.

