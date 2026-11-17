<!-- fuente: corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/README.md -->
# Estacionalidad: método de Winters y señal de rastreo (Corte 1)

## Qué cubre

Pronóstico de demanda con **tendencia y estacionalidad** mediante el método de Winters (suavización exponencial triple), en sus versiones multiplicativa y aditiva:

- modelo y ecuaciones de actualización de nivel, tendencia e índices estacionales;
- inicialización con dos ciclos de datos, normalización de factores y ejemplo numérico completo (llantas para nieve).

Se cubre además cómo elegir parámetros y métodos (datos de calibración y de prueba), la **señal de rastreo** (*tracking signal*) para detectar sesgo, el intervalo de confianza del pronóstico y una tabla comparativa de todos los métodos de pronóstico del corte.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [`L07-forecasting-seasonality-and-tracking-signal.md`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md) | Clase 7 (40 diapositivas): resumen de los tres métodos de suavización, Holt con estacionalidad, Winters multiplicativo y aditivo, ejemplo de llantas, selección de parámetros, señal de rastreo, intervalo de confianza y comparación de métodos | Sí (1.º) |
| [`metodo-winters.md`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/metodo-winters.md) | Excel de 4 hojas: regresión sobre 24 meses (`INTERCEPTO`), inicialización, factores y pronóstico Winters del año 3 (`DATOS PARA WINTERS`), y correlograma de 19 rezagos (`FATOS PARA CORRELOGRAMA`, `CORRELOGRAMA`) | Sí (2.º) |

Los binarios originales son [`L07-forecasting-seasonality-and-tracking-signal.pdf`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.pdf) y [`metodo-winters.xlsx`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/metodo-winters.xlsx).

## Orden de estudio sugerido

1. L07, p. 4–5: tabla resumen de los métodos de suavización y por qué Holt no sirve con estacionalidad.
2. L07, p. 6–15: modelo multiplicativo, ecuaciones (en notación $S,G,c$ y $a_0,a_1,C$) e inicialización.
3. L07, p. 16–22, junto con la hoja `DATOS PARA WINTERS` de [`metodo-winters.md`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/metodo-winters.md): ejemplo numérico, factores normalizados, pronósticos y actualización. Revisar las notas de errores en ambos archivos.
4. La hoja `INTERCEPTO` del Excel muestra por qué no se inicializa con una regresión simple sobre datos estacionales. Las hojas de correlograma muestran cómo se confirma un ciclo de 12 meses.
5. L07, p. 23–26: equivalencia con Minitab y Winters aditivo.
6. L07, p. 27–38: selección de parámetros, señal de rastreo con su ejemplo e intervalo de confianza.
7. L07, p. 39: tabla comparativa de métodos, útil para elegir el método en el parcial y en el proyecto.

## Conceptos y fórmulas clave

Notación: $D_t$ (o $x_t$) = demanda real; $S_t$ (o $a_{0,t}$) = nivel; $G_t$ (o $a_{1,t}$) = tendencia; $c_t$ (o $C_t$) = factor estacional; $N$ = periodos por ciclo. Las constantes de suavización son $\alpha$ (nivel), $\beta$ o $\phi$ (tendencia) y $\gamma$ (estacionalidad).

- **Winters multiplicativo:**

$$S_t=\alpha\frac{D_t}{c_{t-N}}+(1-\alpha)(S_{t-1}+G_{t-1})$$

$$G_t=\beta(S_t-S_{t-1})+(1-\beta)G_{t-1}$$

$$c_t=\gamma\frac{D_t}{S_t}+(1-\gamma)c_{t-N}$$

$$F_{t,t+\tau}=(S_t+\tau G_t)\,c_{t+\tau-N}$$

- **Winters aditivo:**
  - $S_t=\alpha(D_t-c_{t-N})+(1-\alpha)(S_{t-1}+G_{t-1})$
  - $c_t=\gamma(D_t-S_t)+(1-\gamma)c_{t-N}$
  - $F_{t,t+\tau}=S_t+\tau G_t+c_{t+\tau-N}$
- **Inicialización con dos ciclos:**
  - $a_1=(\bar S_2-\bar S_1)/N$
  - $a_{0,2N}=\bar S_2+a_1\frac{N-1}{2}$
  - $a_0=a_{0,2N}-2Na_1$
  - $C_t=\dfrac{x_t}{a_0+a_1t}$, promediando los dos años y normalizando con $C^{norm}=N\,C_t/\sum C_t$
- **Señal de rastreo:**
  - $E_t=\sum_{i\le t}e_i$ (RSFE)
  - $MAD_t=\frac{1}{t}\sum|e_i|$, o en versión suavizada $E_t=\omega e_t+(1-\omega)E_{t-1}$ y $MAD_t=\omega|e_t|+(1-\omega)MAD_{t-1}$
  - $T_t=E_t/MAD_t$, que debe estar cerca de 0
- **Intervalo de confianza aproximado del 95 % para $F_{t+1}$:** $F_{t+1}\pm z_{0.95}\cdot RMSE\cdot\sqrt{N/(N-p)}$, donde $p$ es el número de parámetros del método.
- **Autocorrelación de rezago $k$** (hoja `CORRELOGRAMA`): $r_k=\dfrac{\sum_{t=k+1}^{n}(x_t-\bar x)(x_{t-k}-\bar x)}{\sum(x_t-\bar x)^2}$, significativa si $|r_k|>1{,}96/\sqrt n$.

El detalle está en el resumen de [`L07-forecasting-seasonality-and-tracking-signal.md`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md).

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado principal |
|---|---|---|
| Holt aplicado a datos estacionales ($S_0=24$, $G_0=4$) con dos juegos de $\alpha,\beta$ | L07, p. 5 | El pronóstico no sigue los ciclos; con $\alpha=0{,}4$, $\beta=0{,}5$ los errores llegan a ±20 |
| Winters, llantas para nieve (2 años, $N=12$): inicialización | L07, p. 17–19 | $a_1=2{,}049$, $a_{0,24}=246{,}08$, $a_0=196{,}88$; factores normalizados 1,00; 1,22; 1,46; 1,33; 1,21; 1,01; 0,90; 0,76; 0,65; 0,62; 0,88; 0,96 |
| Winters, llantas: pronóstico | L07, p. 20 | $F_{25}=247{,}64$, $F_{26}=305{,}21$, $F_{27}=368{,}25$ |
| Winters, llantas: actualización con $x_{25}=245$ y $\alpha=\gamma=\phi=0{,}3$ | L07, p. 21–22 | $a_0=247{,}93$, $a_1=1{,}99$; $F_{26}=304{,}90$, $F_{27}=367{,}78$, $F_{28}=337{,}68$ (la diapositiva tiene errores aritméticos; ver notas) |
| Winters, llantas, en Excel (noviembre del año 2 = 208) | [`metodo-winters.md`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/metodo-winters.md), hoja `DATOS PARA WINTERS` | $a_1=2{,}0417$, $a_0=196{,}896$; pronósticos de los meses 25–36: 247,21; 305,27; 367,99; 337,90; 310,97; 260,20; 233,46; 200,04; 171,03; 165,08; 235,50; 260,84. MAD del ajuste ≈ 4,2 (≈ 2 %) |
| Regresión simple sobre los 24 meses | [`metodo-winters.md`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/metodo-winters.md), hoja `INTERCEPTO` | Intercepto 231,32, pendiente −0,71: la estacionalidad distorsiona la tendencia |
| Correlograma de la demanda de llantas | [`metodo-winters.md`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/metodo-winters.md), hoja `CORRELOGRAMA` | $r_1=0{,}77$, $r_6=-0{,}73$, $r_{12}=0{,}44$ (significativos con un límite de ±0,40): ciclo anual |
| Señal de rastreo, ventas 8, 11, 12, 14 con pronóstico fijo de 10 | L07, p. 32–37 | RSFE −2, −1, 1, 5; MAD 2; 1,5; 1,67; 2,25; señal −1; −0,67; 0,6; 2,22 |

## Relación con otros temas y proyectos

- Tema anterior: [`../05-tendencia-suavizacion-doble-holt/`](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/). Winters es Holt más un factor estacional.
- Correlograma y autocorrelación: [`../03-graficas-y-autocorrelacion/`](/corte-1-pronosticos/03-graficas-y-autocorrelacion/).
- Medidas de error (MAD, MSE, MAPE) y suavización simple: [`../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/`](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/).
- ARIMA (Box-Jenkins), que aparece en la tabla comparativa de la p. 39: [`../07-arima/`](/corte-1-pronosticos/07-arima/).
- Métodos cualitativos, para cuando no hay datos: [`../08-metodos-cualitativos/`](/corte-1-pronosticos/08-metodos-cualitativos/).
- En el parcial se descartó Winters por falta de estacionalidad y se usó la señal de rastreo: [`../parcial-1/README.md`](/corte-1-pronosticos/parcial-1/README.md).
- Proyecto de pronóstico de THYMS: [`../proyecto-thyms-pronostico/README.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/README.md).
- Los pronósticos alimentan la planeación agregada del corte 2: [`../../corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/`](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/).


---

<!-- fuente: corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md -->
# L07-forecasting-seasonality-and-tracking-signal

> **Archivo:** [`L07-forecasting-seasonality-and-tracking-signal.pdf`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.pdf) · **Corte 1** · 40 páginas  
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
- [`metodo-winters.md`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/metodo-winters.md): el Excel que resuelve el mismo ejemplo de llantas (inicialización, factores estacionales, pronósticos 25–36 y error *a posteriori*) y añade el correlograma de la demanda.
- Holt (suavización doble), base de Winters: [`../05-tendencia-suavizacion-doble-holt/L06-forecasting-data-with-trend.md`](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/L06-forecasting-data-with-trend.md) y [`../05-tendencia-suavizacion-doble-holt/suavizacion-exponencial-doble-holt.md`](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/suavizacion-exponencial-doble-holt.md).
- Suavización simple y medidas de error (MAD, MSE, MAPE): [`../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/`](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/).
- ARIMA / Box-Jenkins, que aparece en la tabla de la p. 39: [`../07-arima/L08-forecasting-with-arima.md`](/corte-1-pronosticos/07-arima/L08-forecasting-with-arima.md).
- Aplicación a datos reales: [`../parcial-1/`](/corte-1-pronosticos/parcial-1/) y [`../proyecto-thyms-pronostico/`](/corte-1-pronosticos/proyecto-thyms-pronostico/).

**Errores o inconsistencias detectados en el material:**
- p. 5 (tabla derecha): $F_{11}=57{,}21$ debería ser $67{,}74$ ($S_8+3G_8$).
- p. 17: $\bar S_1=2522/12=210{,}17$, no 201,16; el $a_1=2{,}049$ sí usa 210,17. Además $234{,}75+2{,}05\times5{,}5=246{,}03$ (la diapositiva pone 246,08).
- p. 21: con los datos dados, $a_{0,25}=0{,}3(245)+0{,}7(248{,}13)=247{,}19$ (no 247,93) y $C_{25}=0{,}3(245/247{,}93)+0{,}7=0{,}9965\approx1{,}00$ (no 0,97). Los pronósticos de la p. 22 se calculan a partir de 247,93 y 1,99.
- p. 16: noviembre del año 2 vale 209 (el total 2817 lo confirma); el Excel [`metodo-winters.md`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/metodo-winters.md) usa 208.
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


---

<!-- fuente: corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/metodo-winters.md -->
# metodo-winters

> **Archivo:** [`metodo-winters.xlsx`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/metodo-winters.xlsx) · **Corte 1** · Libro de Excel con 4 hoja(s): `INTERCEPTO`, `DATOS PARA WINTERS`, `FATOS PARA CORRELOGRAMA`, `CORRELOGRAMA`  
> **Nombre original:** `CORTE 1/METODO WINTERS.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Libro con 4 hojas que resuelve el **ejemplo numérico del método de Winters multiplicativo** de la clase 7 (ventas mensuales de llantas para nieve durante 2 años; páginas 16–20 de [`L07-forecasting-seasonality-and-tracking-signal.md`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md)). Hace tres cosas:

- `INTERCEPTO` muestra qué pasa si se ajusta una sola recta de regresión a los 24 meses.
- `DATOS PARA WINTERS` inicializa Winters con el método de los dos ciclos, calcula y normaliza los factores estacionales, pronostica los meses 25–36 y mide el error *a posteriori* sobre los datos históricos.
- `FATOS PARA CORRELOGRAMA` y `CORRELOGRAMA` calculan la función de autocorrelación (FAC) de la demanda, que confirma la estacionalidad de 12 meses.

Con él se aprende a inicializar Winters, a construir los índices estacionales y a justificar el método con el correlograma.

**Datos comunes (24 meses, enero del año 1 a diciembre del año 2):**

| Mes | Año 1 (t = 1–12) | Año 2 (t = 13–24) |
|---|---|---|
| enero | 195 | 229 |
| febrero | 252 | 271 |
| marzo | 299 | 333 |
| abril | 276 | 305 |
| mayo | 258 | 277 |
| junio | 210 | 239 |
| julio | 192 | 211 |
| agosto | 154 | 193 |
| septiembre | 141 | 155 |
| octubre | 128 | 159 |
| noviembre | 200 | **208** |
| diciembre | 217 | 236 |
| **Total** | 2522 | 2816 |

Media de los 24 meses: 222,417. Mínimo 128 (octubre, año 1); máximo 333 (marzo, año 2).

### Hoja `INTERCEPTO`

**Objetivo (deducido):** ajustar una recta de tendencia a los 24 meses y quitarle la tendencia a la demanda, para ver la componente estacional.

**Método:**
- Intercepto (J2): $a=$ `INTERCEPT(C2:C25,B2:B25)` $=231{,}319$.
- Pendiente (J3): $b=$ `SLOPE(C2:C25,B2:B25)` $=-0{,}712174$.
- Tendencia (columna D): $T_t=a+bt$ (`=$J$2+$J$3*B2`).
- Demanda sin tendencia (columna E): $D_t-T_t$ (`=C2-D2`).

**Resultados (extracto):** la tendencia baja de 230,607 ($t=1$) a 214,227 ($t=24$). La demanda sin tendencia va de −96,20 (octubre, año 1) a +112,36 (marzo, año 2) y repite el mismo patrón en ambos años: positiva de febrero a mayo y negativa de julio a noviembre.

**Gráficos:**
- En G5, una línea con la serie E2:E26, demanda sin tendencia; muestra dos ciclos casi idénticos.
- En G20, líneas con la demanda C2:C25 y la tendencia D2:D26; la recta es levemente decreciente.

**Conclusión:** la regresión sobre los 24 meses da una pendiente **negativa** (−0,71), aunque el año 2 vende más que el año 1 (promedio 234,7 frente a 210,2). La razón es que dentro de cada año la demanda es alta al inicio y baja al final, y ese patrón estacional distorsiona la recta. Por eso Winters no se inicializa con esta regresión sino con los promedios de cada ciclo (hoja siguiente), que dan una pendiente de +2,04.

### Hoja `DATOS PARA WINTERS`

**Objetivo:** inicializar Winters multiplicativo con $N=12$, obtener los 12 factores estacionales normalizados, pronosticar el año 3 (t = 25–36) y medir el error de ajuste en los años 1 y 2.

**Datos de entrada:** C2:C13 = ciclo 1 (año 1), D2:D13 = ciclo 2 (año 2), B2:B13 = mes 1–12.

**Inicialización (método de los dos ciclos de L07, p. 14):**

| Concepto | Celda | Fórmula Excel | Fórmula | Valor |
|---|---|---|---|---|
| $\bar S_1$ (S_BARRA ciclo 1) | C16 | `=AVERAGE(C2:C13)` | $\bar S_1=\frac{1}{12}\sum_{t=1}^{12}x_t$ | 210,167 |
| $\bar S_2$ (S_BARRA ciclo 2) | D16 | `=AVERAGE(D2:D13)` | $\bar S_2=\frac{1}{12}\sum_{t=13}^{24}x_t$ | 234,667 |
| Pendiente $a_1$ (A1) | C17 | `=(D16-C16)/12` | $a_1=(\bar S_2-\bar S_1)/N$ | 2,04167 |
| Nivel $a_{0,2N}$ («proyectarla primer punto») | C18 | `=D16+C17*11/2` | $a_{0,24}=\bar S_2+a_1\frac{N-1}{2}$ | 245,896 |
| Intercepto original $a_0$ | C19 | `=C18-(2*12)*C17` | $a_0=a_{0,24}-2N\,a_1$ | 196,896 |

**Factores estacionales:**
- Columna F, año 1 (`=C2/($C$19+$C$17*B2)`): $C_t=\dfrac{x_t}{a_0+a_1t}$ para $t=1..12$.
- Columna G, año 2 (`=D2/($C$19+$C$17*(B2+12))`): lo mismo para $t=13..24$.
- Columna H: promedio de los dos años, $\bar C_j=(C_j+C_{j+12})/2$.
- Columna I, normalizado (`=12*H2/SUM($H$2:$H$13)`): $C_j^{norm}=N\,\bar C_j/\sum_k\bar C_k$. La suma de los $\bar C$ es 12,0658 y la de los normalizados es exactamente 12.

**Pronóstico (columna L, `=($C$19+$C$17*K2)*I2`):** $F_t=(a_0+a_1t)\,C^{norm}_{t-24}$ para $t=25..36$ (columna K). Equivale a $(a_{0,24}+\tau a_1)\,C_{24+\tau-N}$ con $\tau=t-24$, como en L07.

**Error *a posteriori*** (ajuste sobre los datos históricos con los mismos factores):
- Ciclo 1: $\hat x_t=(a_0+a_1t)C^{norm}_t$ (columna O, $t=1..12$ en N) y error absoluto $|\hat x_t-x_t|$ (columna P).
- Ciclo 2: igual con $t=13..24$ (columna S, $t$ en R) y error en la columna T.

**Resultados:**

| Mes | $C_t$ año 1 | $C_t$ año 2 | Promedio | Normalizado | t | Pronóstico $F_t$ | Ajuste año 1 | \|e\| año 1 | Ajuste año 2 | \|e\| año 2 |
|---|---|---|---|---|---|---|---|---|---|---|
| enero | 0,9802 | 1,0249 | 1,0026 | 0,9971 | 25 | 247,21 | 198,36 | 3,36 | 222,79 | 6,21 |
| febrero | 1,2539 | 1,2019 | 1,2279 | 1,2212 | 26 | 305,27 | 245,43 | 6,57 | 275,35 | 4,35 |
| marzo | 1,4728 | 1,4636 | 1,4682 | 1,4602 | 27 | 367,99 | 296,45 | 2,55 | 332,22 | 0,78 |
| abril | 1,3459 | 1,3286 | 1,3373 | 1,3300 | 28 | 337,90 | 272,73 | 3,27 | 305,31 | 0,31 |
| mayo | 1,2458 | 1,1960 | 1,2209 | 1,2142 | 29 | 310,97 | 251,47 | 6,53 | 281,22 | 4,22 |
| junio | 1,0041 | 1,0229 | 1,0135 | 1,0080 | 30 | 260,20 | 210,81 | 0,81 | 235,51 | 3,49 |
| julio | 0,9091 | 0,8953 | 0,9022 | 0,8973 | 31 | 233,46 | 189,49 | 2,51 | 211,48 | 0,48 |
| agosto | 0,7222 | 0,8118 | 0,7670 | 0,7629 | 32 | 200,04 | 162,66 | 8,66 | 181,35 | 11,65 |
| septiembre | 0,6550 | 0,6465 | 0,6507 | 0,6472 | 33 | 171,03 | 139,32 | 1,68 | 155,17 | 0,17 |
| octubre | 0,5890 | 0,6575 | 0,6233 | 0,6199 | 34 | 165,08 | 134,71 | 6,71 | 149,89 | 9,11 |
| noviembre | 0,9118 | 0,8530 | 0,8824 | 0,8776 | 35 | 235,50 | 192,50 | 7,50 | 214,00 | 6,00 |
| diciembre | 0,9801 | 0,9598 | 0,9700 | 0,9647 | 36 | 260,84 | 213,57 | 3,43 | 237,21 | 1,21 |

- MAD (P16, `=AVERAGE(P2:P13,U2:U13)`): **4,46552**. Solo promedia el ciclo 1; ver **Observaciones**.
- Total pronosticado para el año 3: 3.095,5 unidades.
- MAPE (O17): rótulo sin valor.

**Gráficos:**
- «3 CICLOS» (en F14): tres líneas de 12 meses, ciclo 1 (C2:C13), ciclo 2 (D2:D13) y pronóstico Winters (L2:L13). Los tres tienen la misma forma (pico en marzo, valle en octubre), cada año por encima del anterior.
- Sin título (en J14): una sola serie «DEMANDA + PROYECCION», que encadena C2:C13, D2:D13 y L2:L13 (36 meses). Muestra los dos años reales y el año pronosticado como una serie continua con tendencia creciente y ciclo anual.

**Conclusión:** los factores normalizados coinciden con los de la clase (1,00; 1,22; 1,46; 1,33; 1,21; 1,01; 0,90; 0,76; 0,65; 0,62; 0,88; 0,96). Los pronósticos de enero a marzo del año 3 (247,21; 305,27; 367,99) son casi iguales a los de la diapositiva (247,64; 305,21; 368,25); la diferencia viene de redondeos y del dato de noviembre. El ajuste histórico es muy bueno: el error medio es de unas 4 unidades, alrededor del 2 % de la demanda. Este Excel solo hace la **inicialización y el pronóstico estático**: no aplica las ecuaciones de actualización con $\alpha$, $\phi$ y $\gamma$ (p. 21–22 de L07).

### Hoja `FATOS PARA CORRELOGRAMA`

**Objetivo:** preparar la serie desplazada para calcular autocorrelaciones.

**Contenido:** columna A = mes, B = demanda (24 datos, B2:B25), y C a U = rezagos 1 a 19. La columna del rezago $k$ es la demanda desplazada $k$ filas hacia abajo, de modo que en la fila $t$ queda $x_{t-k}$. Son valores pegados, sin fórmulas, y la tabla se extiende hasta la fila 44 para que quepan todos los desplazamientos. El nombre de la hoja tiene un error de tipeo: «FATOS» por «DATOS».

### Hoja `CORRELOGRAMA`

**Objetivo:** calcular y graficar la FAC de la demanda para 19 rezagos, con límites de significancia al 95 %.

**Parámetros y método:**
- $n$ (B3) = `COUNT` de la demanda = 24.
- Media $\bar x$ (B4) = 222,417.
- $z$ (B5) = 1,96.
- Límite crítico (B6) = $z/\sqrt n=1{,}96/\sqrt{24}=0{,}400083$.
- FAC (B9:B27), con una fórmula matricial `SUMPRODUCT(OFFSET(...)-media)*(OFFSET(...)-media)/DEVSQ(...)`:

$$r_k=\frac{\sum_{t=k+1}^{n}(x_t-\bar x)(x_{t-k}-\bar x)}{\sum_{t=1}^{n}(x_t-\bar x)^2}$$

- Límites (columnas C y D): $\pm0{,}400083$.
- «Significativo» (columna E): «Sí» si $|r_k|>0{,}400083$.

**Resultados:**

| k | $r_k$ | ¿Significativo? | k | $r_k$ | ¿Significativo? |
|---|---|---|---|---|---|
| 1 | 0,76773 | Sí | 11 | 0,33579 | No |
| 2 | 0,38098 | No | 12 | 0,43996 | Sí |
| 3 | −0,00424 | No | 13 | 0,34712 | No |
| 4 | −0,34573 | No | 14 | 0,15735 | No |
| 5 | −0,63403 | Sí | 15 | 0,02361 | No |
| 6 | −0,72823 | Sí | 16 | −0,08160 | No |
| 7 | −0,60771 | Sí | 17 | −0,13429 | No |
| 8 | −0,31622 | No | 18 | −0,14385 | No |
| 9 | −0,04243 | No | 19 | −0,09297 | No |
| 10 | 0,14390 | No | | | |

Valores verificados con un cálculo independiente.

**Gráfico:** «Correlograma de la demanda (FAC) - 19 rezagos». Barras de $r_k$ contra el rezago $k$ (eje x «Rezago (k)», eje y «Autocorrelación»), con dos líneas horizontales en $\pm0{,}400$ (límites superior e inferior). Las barras dibujan una onda: positiva en $k=1$, mínimo en $k=6$ y de nuevo positiva en $k=12$.

**Interpretación escrita en la hoja (A30:A32):**
- «r1=0,77 positivo, mínimo en r6=-0,73 y repunte en r12=0,44: onda completa de 12 meses → estacionalidad anual con tendencia (adecuado para Winters).»
- «Barras que superan las líneas rojas (±1,96/√n = ±0,400) = autocorrelación significativa al 95%.»
- «Cautela: con n=24, los rezagos altos usan pocas parejas (k=19 solo 5), por lo que r_k a partir de ~k=12 es poco confiable. Regla práctica: k ≤ n/4.»

### Observaciones

- **MAD incompleto (P16).** La fórmula `=AVERAGE(P2:P13,U2:U13)` toma la columna U, que está vacía, en lugar de la T, donde están los errores del ciclo 2. Por eso el MAD de 4,4655 corresponde solo al año 1. Cálculo propio: el MAD del año 2 es 3,998, el MAD de los 24 meses es **4,232** y el MAPE de los 24 meses es ≈ 2,13 %. El MAPE de la celda O17 quedó sin calcular.
- **Dato distinto al de la clase.** Noviembre del año 2 vale 208 en el Excel y 209 en la diapositiva (total 2817 en L07). Por eso $\bar S_2=234{,}667$ (clase: 234,75), $a_1=2{,}0417$ (clase: 2,049), $a_{0,24}=245{,}896$ (clase: 246,08) y $a_0=196{,}896$ (clase: 196,88).
- El Excel usa correctamente $\bar S_1=210{,}167$; la diapositiva escribe 201,16 por error de tipeo.
- **Sin parámetros de suavización.** No hay $\alpha$, $\phi$ ni $\gamma$. El «pronóstico Winters» es el pronóstico estático desde la inicialización y no se actualiza con datos nuevos.
- **Rangos de los gráficos de `INTERCEPTO`.** Llegan hasta la fila 26 (E2:E26, D2:D26), una fila más que los datos (fila 25). La fila 26 está vacía y no afecta.
- **Orden de las series del gráfico «3 CICLOS».** Es ciclo 2, pronóstico y ciclo 1, en ese orden.
- La hoja `INTERCEPTO` muestra que una regresión lineal simple sobre datos estacionales puede dar una pendiente con el signo equivocado (−0,71 frente a +2,04).
