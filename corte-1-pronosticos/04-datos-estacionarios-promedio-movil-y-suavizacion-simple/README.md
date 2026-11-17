# Datos estacionarios: promedio móvil y suavización exponencial simple (Corte 1)

## Qué cubre
Métodos de pronóstico para demanda **estacionaria** (una constante más ruido, sin tendencia ni estacionalidad): promedio móvil simple, promedio móvil ponderado y suavización exponencial simple, con sus ventajas, desventajas y la elección de $n$ y de $\alpha$. Cubre también cómo medir el error de un pronóstico (MAD, SSE, MSE, MAPE, PME) y por qué los indicadores no bastan: un buen método deja residuales aleatorios, sin sesgo, alrededor de cero. Los Excel comparan métodos sobre ventas reales y repasan los ejercicios de la clase antes del parcial 1.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [L05-forecasting-stationary-data-and-errors.md](./L05-forecasting-stationary-data-and-errors.md) | Lecture 5 (31 diapositivas): MA simple y ponderado, suavización exponencial simple, elección de α, SES frente a MA, medidas de error y análisis de residuales. Incluye los datos de los ejemplos (21 periodos) y sus soluciones calculadas. | **Sí** |
| [promedio-movil-y-suavizacion-exponencial.md](./promedio-movil-y-suavizacion-exponencial.md) | Excel de clase: compara PM(6), PM(12), SE(α = 0,2) y SE(α = 0,8) sobre 30 días de las ventas propias de la tarea del tema 03, con MAD, MSE y error %. Las otras 14 hojas son copia exacta de [tarea-class-example-1](../03-graficas-y-autocorrelacion/tarea-class-example-1.md). | Segundo |
| [practica-metodos-pronostico-parcial-1.md](./practica-metodos-pronostico-parcial-1.md) | Excel de práctica para el parcial 1: MA simple con MAD/SSE/MSE/MAPE, ejercicio de la diapositiva 30 (MA 3 frente a MA 5), MA ponderado y SES. Datos aleatorios (`RANDBETWEEN`), varios errores de fórmula documentados y hojas de Holt y Winters vacías. | Tercero |

CSV completo de la hoja larga de comparación: [promedio-movil-y-suavizacion-exponencial-datos/Ventas_propias_2.csv](./promedio-movil-y-suavizacion-exponencial-datos/Ventas_propias_2.csv) (incluye pronósticos y errores); también están `Ventas_propias.csv` y `Ventas_competencia.csv` en la misma carpeta.

## Orden de estudio sugerido
1. [L05](./L05-forecasting-stationary-data-and-errors.md), p. 1–11: promedio móvil simple y ponderado, con sus desventajas (recalcular, rezago frente a tendencias).
2. L05, p. 12–20: suavización exponencial simple, interpretación como corrección del error, elección de α y comparación con MA.
3. L05, p. 21–30: medidas de error y análisis de residuales.
4. [practica-metodos-pronostico-parcial-1](./practica-metodos-pronostico-parcial-1.md): rehacer cada método en Excel (y revisar los errores señalados).
5. [promedio-movil-y-suavizacion-exponencial](./promedio-movil-y-suavizacion-exponencial.md): comparación de cuatro métodos con datos reales.
6. Siguiente tema: [05 — tendencia y Holt](../05-tendencia-suavizacion-doble-holt/README.md).

## Conceptos y fórmulas clave
Detalle en [L05](./L05-forecasting-stationary-data-and-errors.md).

- **Promedio móvil simple:** $F_t=\dfrac{A_{t-1}+A_{t-2}+\dots+A_{t-n}}{n}$ ($A$: demanda real; $n$: periodos promediados). $n$ grande suaviza más pero reacciona más lento.
- **Promedio móvil ponderado:** $F_t=w_0A_t+w_1A_{t-1}+\dots+w_nA_{t-n}$ con $\sum w_i=1$ y más peso en lo reciente (la diapositiva escribe el último término como $w_nA_t$).
- **Suavización exponencial simple:**
  $$F_t=\alpha D_{t-1}+(1-\alpha)F_{t-1}=F_{t-1}-\alpha e_{t-1}$$
  $D$: demanda; $\alpha\in[0,1]$; $e_{t-1}=F_{t-1}-D_{t-1}$. El dato con $k$ periodos de antigüedad pesa $\alpha(1-\alpha)^k$. Valores recomendados $0{,}1\le\alpha\le0{,}3$; α pequeño para demanda estable. $F_1$ se fija con un promedio móvil, el último dato o la opinión de un experto.
- **Pronóstico de varios pasos:** con un modelo estacionario, el mismo $F_{t+1}$ sirve para $t+2, t+3,\dots$
- **Medidas de error** ($e_t=F_t-D_t$; $n$ o $T$ = número de periodos con pronóstico):
  $$MAD=\frac{\sum|A_i-F_i|}{n},\quad SSE=\sum(A_i-F_i)^2,\quad MSE=\frac{SSE}{n},\quad MAPE=\frac{100}{n}\sum\frac{|A_i-F_i|}{A_i}$$
  PME (como está en la diapositiva): $PME=\frac{1}{n}\sum e_t^2/D_t$.
- **Residuales:** deben ser aleatorios y centrados en cero; un método con menor MSE pero errores siempre del mismo signo está sesgado (L05, p. 29).

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado principal |
|---|---|---|
| MA con $n=3$ y $n=9$ (datos de 21 periodos) | [L05](./L05-forecasting-stationary-data-and-errors.md), p. 6 (solución calculada en el resumen) | $F_{22}=491{,}67$ ($n=3$) y $500{,}22$ ($n=9$) |
| MA rezagado frente a tendencia | L05, p. 8 | MA(3) queda 4 unidades y MA(6) 7 unidades por debajo de la demanda |
| WMA $n=3$, pesos 0,75/0,15/0,1 | L05, p. 11 (solución calculada) | $F_{22}=523{,}15$ |
| SES $\alpha=0{,}05$, $F_1=540$ | L05, p. 16 (solución calculada) | $F_{22}=511{,}89$ |
| ¿Método 1 (MAD 5,77; MSE 51,69) o método 2 (MAD 6; MSE 41,8)? | L05, p. 29 | Método 1: el método 2 tiene errores siempre negativos (sesgo) |
| MA $n=3$ frente a $n=5$ (diapositiva 30) | [practica-metodos-pronostico-parcial-1](./practica-metodos-pronostico-parcial-1.md), hoja `EJERCICIO DIAPO` | MA(5) mejor: MAD 1,74 frente a 2,47; MSE 4,39 frente a 8,44; MAPE 10,8 % frente a 20,0 % |
| MA simple con datos aleatorios | práctica, hoja `MA SIMPLE` | $F_{22}=553{,}33$; MAD 23,30 en la hoja (28,22 con la alineación correcta) |
| WMA con datos aleatorios | práctica, hoja `MA PONDERADO` | La hoja da 177,017 por dividir entre $n$; lo correcto es 531,05 |
| SES con datos aleatorios | práctica, hoja `SE SIMPLE` | Un solo paso: 533,35 (con α = 0,95) |
| PM(6), PM(12), SE(0,2), SE(0,8) sobre 30 días de ventas | [promedio-movil-y-suavizacion-exponencial](./promedio-movil-y-suavizacion-exponencial.md) | MAD 235,9 / 236,1 / **229,7** / 237,3; MSE **69.652** / 70.490 / 70.977 / 86.233; MAPE 12,21 % / 12,15 % / **11,98 %** / 12,34 % → SE(0,2) el mejor en MAD y MAPE, SE(0,8) el peor |

## Relación con otros temas y proyectos
- Viene de [03 — gráficas y autocorrelación](../03-graficas-y-autocorrelacion/README.md): el correlograma dice si la serie es aleatoria (y entonces se usan estos métodos). La serie de ventas usada en [promedio-movil-y-suavizacion-exponencial](./promedio-movil-y-suavizacion-exponencial.md) es la de [tarea-class-example-1](../03-graficas-y-autocorrelacion/tarea-class-example-1.md), que allí se muestra aleatoria.
- Si la serie tiene tendencia: [05 — suavización doble de Holt](../05-tendencia-suavizacion-doble-holt/README.md). Si además tiene estacionalidad, y para controlar el sesgo con la señal de rastreo: [06 — Winters y tracking signal](../06-estacionalidad-winters-y-tracking-signal/README.md).
- Aplicación: el [proyecto THYMS de pronóstico](../proyecto-thyms-pronostico/README.md) usa suavización exponencial simple; el [parcial 1](../parcial-1/README.md) evalúa estos métodos y sus medidas de error.
