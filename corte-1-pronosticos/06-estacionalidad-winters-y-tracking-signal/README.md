# Estacionalidad: método de Winters y señal de rastreo (Corte 1)

## Qué cubre

Pronóstico de demanda con **tendencia y estacionalidad** mediante el método de Winters (suavización exponencial triple), en sus versiones multiplicativa y aditiva:

- modelo y ecuaciones de actualización de nivel, tendencia e índices estacionales;
- inicialización con dos ciclos de datos, normalización de factores y ejemplo numérico completo (llantas para nieve).

Se cubre además cómo elegir parámetros y métodos (datos de calibración y de prueba), la **señal de rastreo** (*tracking signal*) para detectar sesgo, el intervalo de confianza del pronóstico y una tabla comparativa de todos los métodos de pronóstico del corte.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [`L07-forecasting-seasonality-and-tracking-signal.md`](./L07-forecasting-seasonality-and-tracking-signal.md) | Clase 7 (40 diapositivas): resumen de los tres métodos de suavización, Holt con estacionalidad, Winters multiplicativo y aditivo, ejemplo de llantas, selección de parámetros, señal de rastreo, intervalo de confianza y comparación de métodos | Sí (1.º) |
| [`metodo-winters.md`](./metodo-winters.md) | Excel de 4 hojas: regresión sobre 24 meses (`INTERCEPTO`), inicialización, factores y pronóstico Winters del año 3 (`DATOS PARA WINTERS`), y correlograma de 19 rezagos (`FATOS PARA CORRELOGRAMA`, `CORRELOGRAMA`) | Sí (2.º) |

Los binarios originales son [`L07-forecasting-seasonality-and-tracking-signal.pdf`](./L07-forecasting-seasonality-and-tracking-signal.pdf) y [`metodo-winters.xlsx`](./metodo-winters.xlsx).

## Orden de estudio sugerido

1. L07, p. 4–5: tabla resumen de los métodos de suavización y por qué Holt no sirve con estacionalidad.
2. L07, p. 6–15: modelo multiplicativo, ecuaciones (en notación $S,G,c$ y $a_0,a_1,C$) e inicialización.
3. L07, p. 16–22, junto con la hoja `DATOS PARA WINTERS` de [`metodo-winters.md`](./metodo-winters.md): ejemplo numérico, factores normalizados, pronósticos y actualización. Revisar las notas de errores en ambos archivos.
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

El detalle está en el resumen de [`L07-forecasting-seasonality-and-tracking-signal.md`](./L07-forecasting-seasonality-and-tracking-signal.md).

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado principal |
|---|---|---|
| Holt aplicado a datos estacionales ($S_0=24$, $G_0=4$) con dos juegos de $\alpha,\beta$ | L07, p. 5 | El pronóstico no sigue los ciclos; con $\alpha=0{,}4$, $\beta=0{,}5$ los errores llegan a ±20 |
| Winters, llantas para nieve (2 años, $N=12$): inicialización | L07, p. 17–19 | $a_1=2{,}049$, $a_{0,24}=246{,}08$, $a_0=196{,}88$; factores normalizados 1,00; 1,22; 1,46; 1,33; 1,21; 1,01; 0,90; 0,76; 0,65; 0,62; 0,88; 0,96 |
| Winters, llantas: pronóstico | L07, p. 20 | $F_{25}=247{,}64$, $F_{26}=305{,}21$, $F_{27}=368{,}25$ |
| Winters, llantas: actualización con $x_{25}=245$ y $\alpha=\gamma=\phi=0{,}3$ | L07, p. 21–22 | $a_0=247{,}93$, $a_1=1{,}99$; $F_{26}=304{,}90$, $F_{27}=367{,}78$, $F_{28}=337{,}68$ (la diapositiva tiene errores aritméticos; ver notas) |
| Winters, llantas, en Excel (noviembre del año 2 = 208) | [`metodo-winters.md`](./metodo-winters.md), hoja `DATOS PARA WINTERS` | $a_1=2{,}0417$, $a_0=196{,}896$; pronósticos de los meses 25–36: 247,21; 305,27; 367,99; 337,90; 310,97; 260,20; 233,46; 200,04; 171,03; 165,08; 235,50; 260,84. MAD del ajuste ≈ 4,2 (≈ 2 %) |
| Regresión simple sobre los 24 meses | [`metodo-winters.md`](./metodo-winters.md), hoja `INTERCEPTO` | Intercepto 231,32, pendiente −0,71: la estacionalidad distorsiona la tendencia |
| Correlograma de la demanda de llantas | [`metodo-winters.md`](./metodo-winters.md), hoja `CORRELOGRAMA` | $r_1=0{,}77$, $r_6=-0{,}73$, $r_{12}=0{,}44$ (significativos con un límite de ±0,40): ciclo anual |
| Señal de rastreo, ventas 8, 11, 12, 14 con pronóstico fijo de 10 | L07, p. 32–37 | RSFE −2, −1, 1, 5; MAD 2; 1,5; 1,67; 2,25; señal −1; −0,67; 0,6; 2,22 |

## Relación con otros temas y proyectos

- Tema anterior: [`../05-tendencia-suavizacion-doble-holt/`](../05-tendencia-suavizacion-doble-holt/). Winters es Holt más un factor estacional.
- Correlograma y autocorrelación: [`../03-graficas-y-autocorrelacion/`](../03-graficas-y-autocorrelacion/).
- Medidas de error (MAD, MSE, MAPE) y suavización simple: [`../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/`](../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/).
- ARIMA (Box-Jenkins), que aparece en la tabla comparativa de la p. 39: [`../07-arima/`](../07-arima/).
- Métodos cualitativos, para cuando no hay datos: [`../08-metodos-cualitativos/`](../08-metodos-cualitativos/).
- En el parcial se descartó Winters por falta de estacionalidad y se usó la señal de rastreo: [`../parcial-1/README.md`](../parcial-1/README.md).
- Proyecto de pronóstico de THYMS: [`../proyecto-thyms-pronostico/README.md`](../proyecto-thyms-pronostico/README.md).
- Los pronósticos alimentan la planeación agregada del corte 2: [`../../corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/`](../../corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/).
