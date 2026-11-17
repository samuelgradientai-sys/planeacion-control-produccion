# ARIMA: método de Box-Jenkins (Corte 1)

## Qué cubre

Introducción al método de **Box-Jenkins (ARIMA)**, pensado para series en las que un periodo depende de los anteriores, en especial con **autocorrelación negativa**. Explica qué significa «integrado» (diferenciar la serie para quitar la tendencia) y los modelos autorregresivos AR(1) y AR(2), de promedio móvil MA(1) y mixto ARMA(1,1). Se resuelven a mano un AR(1) y un MA(1) con 12 periodos de demanda. La carpeta solo tiene la presentación; no hay Excel ni código.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [`L08-forecasting-with-arima.md`](./L08-forecasting-with-arima.md) | Clase 8 (20 diapositivas): Box-Jenkins, AR(1) con estimación de $\phi_1$, AR(2), MA(1) paso a paso, ARMA(1,1) y su estimación | Sí |

El binario original es [`L08-forecasting-with-arima.pdf`](./L08-forecasting-with-arima.pdf).

## Orden de estudio sugerido

1. Repasar la autocorrelación y el correlograma en [`../03-graficas-y-autocorrelacion/`](../03-graficas-y-autocorrelacion/) y en la hoja `CORRELOGRAMA` de [`../06-estacionalidad-winters-y-tracking-signal/metodo-winters.md`](../06-estacionalidad-winters-y-tracking-signal/metodo-winters.md).
2. L08, p. 4–5: qué es Box-Jenkins y qué significa ARIMA.
3. L08, p. 6–9: ejemplo AR(1) completo (tabla de desviaciones, $\phi_1=-0{,}7$, pronóstico 109,2).
4. L08, p. 11–17: MA(1) paso a paso. Atención al signo: el ejemplo usa $F_t=\bar\mu-\theta_1e_{t-1}$ (ver notas del `.md`).
5. L08, p. 18–19: ARMA(1,1) y la estimación de sus parámetros.
6. Tabla comparativa de métodos (ARIMA frente a los demás): p. 39 de [`../06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md`](../06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md).

## Conceptos y fórmulas clave

Notación: $x_t$ = demanda del periodo $t$, $\bar x$ (o $\bar\mu$) = media de la serie, $\dot x_t=x_t-\bar x$ = desviación respecto a la media, $e_t=x_t-F_t$ = error de pronóstico, $n$ = número de datos.

- AR(1): $\dot x_t=\phi_1\dot x_{t-1}+e_t$, con

$$\phi_1=\frac{cov(\dot x_t,\dot x_{t-1})}{var(\dot x_t)}=\frac{\sum\dot x_t\dot x_{t-1}/(n-1)}{\sum\dot x_t^2/n}$$

  - Pronóstico: $F_t=\bar\mu+\hat\phi_1\dot x_{t-1}$.
- AR(2): $F_t=\bar\mu+\hat\phi_1\dot x_{t-1}+\hat\phi_2\dot x_{t-2}$.
- MA(1): $F_t=\bar\mu+\theta_1e_{t-1}$ según la diapositiva. Los números del ejemplo salen de $F_t=\bar\mu-\theta_1e_{t-1}$. $\theta_1$ se fija por mínimos cuadrados no lineales.
- ARMA(1,1): $F_t=\hat\phi_1\hat x_{t-1}-\hat\theta_1e_{t-1}$. Sus parámetros se estiman con

$$\rho_k=\frac{cov(\dot x_t,\dot x_{t-k})}{var(\dot x_t)},\qquad \phi_1=\frac{\rho_2}{\rho_1},\qquad \rho_1=\frac{(1-\phi_1\theta_1)(\phi_1-\theta_1)}{1+\theta_1^2-2\theta_1\phi_1}$$

- Requisitos según la clase: pronósticos de corto plazo y al menos 72 datos históricos (la tabla de L07 dice 50 o más).

El detalle está en el resumen de [`L08-forecasting-with-arima.md`](./L08-forecasting-with-arima.md).

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado principal |
|---|---|---|
| AR(1) con demanda 106, 110, 118, 105, 115, 100, 112, 106, 118, 102, 112, 110 (media 109,5) | L08, p. 6–9 | $\sum\dot x_{t-1}\dot x_t=-256{,}25$, $\sum\dot x_t^2=379$, $cov=-23{,}3$, $var=31{,}6$, $\phi_1=-0{,}7$; pronóstico del periodo 13 = 109,2 |
| Promedio móvil de 5 periodos y sus errores (periodos 6–12) | L08, p. 11 | Errores −10,8; 2,4; −4; 10,4; −8,2; 4,4; 0, que alternan de signo (correlación negativa) |
| MA(1) con $\theta_1=0{,}5$ y pronóstico inicial 109,5 | L08, p. 13–17 | Pronósticos 109,5; 111,3; 110,1; 105,6; 109,8; 106,9; 112,9; 110,0; 111,5; 106,2; 111,6; 109,3 |

## Relación con otros temas y proyectos

- Autocorrelación, base para identificar modelos AR y MA: [`../03-graficas-y-autocorrelacion/`](../03-graficas-y-autocorrelacion/).
- Promedio móvil, con el que se compara el AR(1): [`../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/`](../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/).
- Holt y Winters, alternativas para series con tendencia o estacionalidad: [`../05-tendencia-suavizacion-doble-holt/`](../05-tendencia-suavizacion-doble-holt/) y [`../06-estacionalidad-winters-y-tracking-signal/`](../06-estacionalidad-winters-y-tracking-signal/).
- Métodos cualitativos: [`../08-metodos-cualitativos/`](../08-metodos-cualitativos/).
- Proyecto de pronóstico de THYMS: [`../proyecto-thyms-pronostico/README.md`](../proyecto-thyms-pronostico/README.md).
