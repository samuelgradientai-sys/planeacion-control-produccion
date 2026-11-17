# Tendencia: suavización exponencial doble de Holt (Corte 1)

## Qué cubre

Pronóstico de demanda con **tendencia lineal y sin estacionalidad** mediante la suavización exponencial doble (método de Holt). Incluye las ecuaciones de nivel y pendiente, el pronóstico a $\tau$ periodos y tres formas de fijar los valores iniciales $S_0$ y $G_0$: diferencias, regresión lineal y estaciones. Cierra con un repaso de regresión lineal simple: supuestos, estimadores de mínimos cuadrados, $R^2$, residuos y la herramienta Regresión de Excel.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [`L06-forecasting-data-with-trend.md`](./L06-forecasting-data-with-trend.md) | Clase 6 (25 diapositivas): Holt, inicialización por regresión y por estaciones con ejemplos resueltos, y regresión lineal | Sí (1.º) |
| [`suavizacion-exponencial-doble-holt.md`](./suavizacion-exponencial-doble-holt.md) | Excel: Holt sobre 8 trimestres de demanda, inicializado por regresión, con $\alpha$ y $\beta$ hallados con Solver, MAD, MAPE y proyección de 4 periodos | Sí (2.º) |

Los binarios originales son [`L06-forecasting-data-with-trend.pdf`](./L06-forecasting-data-with-trend.pdf) y [`suavizacion-exponencial-doble-holt.xlsx`](./suavizacion-exponencial-doble-holt.xlsx).

## Orden de estudio sugerido

1. Repasar la suavización simple y las medidas de error (MAD, MSE, MAPE) en [`../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/`](../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/).
2. Leer L06, páginas 3–7: ecuaciones de Holt, interpretación gráfica y pronóstico a $\tau$ periodos.
3. Leer L06, páginas 8–15: las tres formas de inicializar y los dos ejemplos resueltos (regresión y estaciones con los mismos datos).
4. Estudiar el Excel [`suavizacion-exponencial-doble-holt.md`](./suavizacion-exponencial-doble-holt.md), sobre todo sus **Observaciones**: Solver quedó configurado para maximizar el MAD.
5. Leer L06, páginas 16–24, sobre regresión lineal; sirve para inicializar Holt y como método de pronóstico en sí.
6. Seguir con Winters en [`../06-estacionalidad-winters-y-tracking-signal/`](../06-estacionalidad-winters-y-tracking-signal/), que añade estacionalidad a Holt.

## Conceptos y fórmulas clave

Notación: $D_t$ = demanda real en $t$, $S_t$ = nivel (intercepto), $G_t$ = pendiente (tendencia), $\alpha$ y $\beta$ = constantes de suavización del nivel y de la pendiente.

- Holt (en general $\beta\le\alpha$):

$$S_t=\alpha D_t+(1-\alpha)(S_{t-1}+G_{t-1}),\qquad G_t=\beta(S_t-S_{t-1})+(1-\beta)G_{t-1}$$

- Pronóstico hecho en $t$ para $\tau$ periodos adelante: $F_{t,t+\tau}=S_t+\tau G_t$.
- Inicialización por regresión: $S_0$ = intercepto y $G_0$ = pendiente de la recta de $D_t$ contra $t$ (en Excel, `INTERSECCION.EJE` y `PENDIENTE`).
- Inicialización por estaciones, con $m$ grupos de $N$ datos y $V_i$ = promedio del grupo $i$:

$$G_0=\frac{V_m-V_1}{(m-1)N},\qquad S_0=V_1-G_0\frac{N+1}{2}$$

- Regresión lineal simple $Y=a+bx$:

$$b=\frac{\sum xy-n\bar x\bar y}{\sum x^2-n\bar x^2},\qquad a=\bar y-b\bar x$$

  - $R^2$ = proporción de la variación explicada.
  - Supuestos: residuos normales, independientes y homocedásticos.

El detalle está en el resumen de [`L06-forecasting-data-with-trend.md`](./L06-forecasting-data-with-trend.md).

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado principal |
|---|---|---|
| Holt con inicialización por regresión, demanda 15, 20, 26, 30, 35, 38, 40, 43, $\alpha=\beta=0{,}1$ | L06, p. 10–11 | $S_0=12{,}8$, $G_0=4{,}01$; pronósticos 16,8 … 45,1; errores entre −2,1 y 2,15 |
| Mismo ejercicio con inicialización por estaciones ($m=2$, $N=4$) | L06, p. 14–15 | $V_1=22{,}75$, $V_2=39$, $S_0=12{,}6$, $G_0=4{,}06$; pronósticos 16,7 … 45,3 |
| Demanda trimestral 200, 250, 175, 186, 225, 285, 305, 190 ($\alpha=\beta=0{,}1$, $S_0=200$, $G_0=10$) | Enunciado en L06, p. 6, sin solución en la diapositiva | El Excel lo resuelve con otros $S_0$, $G_0$, $\alpha$ y $\beta$; con los del enunciado, cálculo propio en el `.md` del Excel: MAD ≈ 41,3 y $F_9\approx275{,}5$ |
| Holt en Excel con los datos anteriores, $S_0=196{,}25$ y $G_0=6{,}83$ por regresión, $\alpha=0{,}831$, $\beta=0{,}999$ | [`suavizacion-exponencial-doble-holt.md`](./suavizacion-exponencial-doble-holt.md) | MAD = 60,78; MAPE = 29,6 %; proyección de los periodos 9–12: 120,6; 25,3; −70,1; −165,5 (inestable porque $\beta\approx1$) |
| Regresiones de viscosidad, granularidad y deformación contra la temperatura | L06, p. 21 | $R^2$ = 0,9058; 0,9218; 0,9087 |
| Salida de la herramienta Regresión de Excel | L06, p. 24 | $R^2=0{,}0017$: no hay relación lineal |

## Relación con otros temas y proyectos

- Tema anterior: [`../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/`](../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/) (suavización simple, a la que Holt añade la pendiente).
- Tema siguiente: [`../06-estacionalidad-winters-y-tracking-signal/`](../06-estacionalidad-winters-y-tracking-signal/). Winters añade la estacionalidad, y la p. 5 de L07 muestra por qué Holt falla con datos estacionales. Allí también están la señal de rastreo y la tabla comparativa de métodos.
- Autocorrelación y gráficas para detectar la tendencia: [`../03-graficas-y-autocorrelacion/`](../03-graficas-y-autocorrelacion/).
- Aplicación evaluada de Holt (demanda con tendencia decreciente, 48 meses): [`../parcial-1/README.md`](../parcial-1/README.md).
- Proyecto de pronóstico de THYMS: [`../proyecto-thyms-pronostico/README.md`](../proyecto-thyms-pronostico/README.md).
