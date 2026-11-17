<!-- fuente: corte-1-pronosticos/parcial-1/README.md -->
# Parcial 1: pronóstico de una demanda con tendencia (Corte 1)

## Qué cubre

Primer parcial del curso (Entrega I). Con 48 meses de ventas de un producto se hace el análisis descriptivo completo (estadísticos, histograma, boxplot, dispersión, correlograma y Ljung-Box), se diagnostica una **tendencia lineal decreciente sin estacionalidad**, se elige el método de **Holt** y se pronostican los meses 49 a 60 con sus medidas de error. El informe cierra con recomendaciones gerenciales sobre producción e inventario.

**Enunciado (deducido de los títulos del informe):** 1) análisis descriptivo y elección del método; 2) realizar el pronóstico; 3) estimar el error; 4) conclusión gerencial.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [`parcial-1-informe.md`](/corte-1-pronosticos/parcial-1/parcial-1-informe.md) | Informe en Word: diagnóstico, justificación de Holt, pronóstico, errores y conclusión gerencial | Sí (1.º) |
| [`parcial-1-calculos.md`](/corte-1-pronosticos/parcial-1/parcial-1-calculos.md) | Excel con todos los cálculos: 7 hojas (datos, estadísticos, histograma, boxplot, dispersión, correlograma, Holt) | Sí (2.º) |
| [`sales_data.csv`](/corte-1-pronosticos/parcial-1/sales_data.csv) | Datos del parcial (ver abajo). No tiene `.md` gemelo porque ya es texto plano | Consultar |

### `sales_data.csv`

Archivo de texto separado por comas, 48 filas más encabezado, con encabezados en inglés. Es el dato de entrada que se copió a la hoja `Datos` del Excel. Parece un conjunto de datos sintético del enunciado: el inventario no cumple el balance $I_t = I_{t-1} + P_t - D_t$.

| Columna | Significado | Mínimo | Máximo | Media |
|---|---|---|---|---|
| `Month` | «Month 1» … «Month 48» | — | — | — |
| `Actual Sales` | Demanda real (unidades) | 671 (mes 48) | 1.134 (mes 1) | 916,0 |
| `Forecasted Sales` | Pronóstico que usaba la empresa | 599 | 1.193 | 929,1 |
| `Inventory Levels` | Inventario a fin de mes | 2.089 (mes 9) | 10.622 (mes 48) | 4.629,6 |
| `Production Levels` | Producción del mes | 905 | 1.298 | 1.097,2 |

El pronóstico original tiene MAD = 100,2 y MAPE = 11,4 % frente a las ventas reales, y el inventario pasa de 2.546 (mes 1) a 10.622 (mes 48), es decir, se multiplica por 4,2.

## Orden de estudio sugerido

1. Leer el informe ([`parcial-1-informe.md`](/corte-1-pronosticos/parcial-1/parcial-1-informe.md)) para ver la historia completa y las decisiones.
2. Revisar en [`parcial-1-calculos.md`](/corte-1-pronosticos/parcial-1/parcial-1-calculos.md) cómo se calculó cada cosa: primero las hojas descriptivas y luego la hoja `Holt`.
3. Repasar la teoría: [L04](/corte-1-pronosticos/03-graficas-y-autocorrelacion/L04-plotting-your-data.md) (gráficas y correlograma), [L05](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md) (errores), [L06](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/L06-forecasting-data-with-trend.md) (Holt) y [L07](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md) (señal de rastreo y por qué no Winters).
4. Leer las observaciones al final de cada `.md` (errores y diferencias entre el informe y el Excel).

## Conceptos y fórmulas clave

- **Autocorrelación del rezago $k$** ($x_t$ = demanda, $\bar{x}$ = media, $n$ = 48):
  $$r_k = \frac{\sum_{t=1}^{n-k}(x_t-\bar{x})(x_{t+k}-\bar{x})}{\sum_{t=1}^{n}(x_t-\bar{x})^2}$$
  con límites $\pm\,t_{0{,}025;\,n-1}\cdot SE(r_k)$, donde $SE(r_k) = \sqrt{(1+2\sum_{j=1}^{k-1} r_j^2)/n}$. Detalle en [`parcial-1-calculos.md`](/corte-1-pronosticos/parcial-1/parcial-1-calculos.md#hoja-descriptivo-correlograma).
- **Ljung-Box:** $Q = n(n+2)\sum_{k=1}^{h}\frac{r_k^2}{n-k}$; si $Q > \chi^2_{\alpha;\,h}$ la serie no es ruido.
- **Holt** ($D_t$ = demanda, $S_t$ = nivel, $G_t$ = tendencia, $\alpha$ y $\beta$ = constantes de suavización, $h$ = meses hacia adelante):
  $$S_t = \alpha D_t + (1-\alpha)(S_{t-1}+G_{t-1}), \quad G_t = \beta(S_t - S_{t-1}) + (1-\beta)G_{t-1}, \quad F_{t+h} = S_t + h\,G_t$$
  Aquí $\alpha$ = 0,95, $\beta$ = 0,05, $S_0$ = 1.161,45 y $G_0$ = −10,02 (intercepto y pendiente de la regresión). Detalle en [`parcial-1-calculos.md`](/corte-1-pronosticos/parcial-1/parcial-1-calculos.md#hoja-holt).
- **Errores** ($e_t$ = error del mes $t$): $MAD = \frac{1}{n}\sum|e_t|$, $MAPE = \frac{1}{n}\sum|e_t|/D_t$, $MSE = \frac{1}{n}\sum e_t^2$, señal de rastreo $TS = \sum e_t/MAD$ (aceptable en ±4).
- **Regla de elección del método:** demanda estable → promedio móvil o suavización simple; tendencia → Holt o regresión; tendencia + estacionalidad → Winters. Aquí el diagnóstico da tendencia sin estacionalidad → Holt.

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado principal |
|---|---|---|
| Estadísticos descriptivos | Hoja `Descriptivo-Estadisticos` | Media 916, CV 15,4 %, caída de −40,8 %, regresión 1.161,45 − 10,02·t con $R^2$ = 0,988 |
| Histograma y boxplot | Hojas `Descriptivo-Histograma` y `Descriptivo-Boxplot` | Distribución plana; IQR = 250; 0 atípicos |
| Correlograma y Ljung-Box | Hoja `Descriptivo-Correlograma` | $r_1$ = 0,94 que decae despacio; Q = 274,4 > 21,0 |
| Pronóstico de Holt, meses 49 a 60 | Hoja `Holt` | 660,3 (mes 49) → 545,7 (mes 60); MAD 5,30; MAPE 0,60 %; MSE 40,7 |
| Recomendación gerencial | Informe | Producir 400–500 unid./mes para drenar ~10.600 unidades de inventario |

## Relación con otros temas y proyectos

- Teoría de pronósticos: [02-introduccion-a-pronosticos](/corte-1-pronosticos/02-introduccion-a-pronosticos/), [03-graficas-y-autocorrelacion](/corte-1-pronosticos/03-graficas-y-autocorrelacion/), [04-datos-estacionarios-promedio-movil-y-suavizacion-simple](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/), [05-tendencia-suavizacion-doble-holt](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/) y [06-estacionalidad-winters-y-tracking-signal](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/).
- Práctica previa al parcial: [`practica-metodos-pronostico-parcial-1.md`](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/practica-metodos-pronostico-parcial-1.md).
- El mismo tipo de diagnóstico se aplica en el proyecto del semestre: [proyecto-thyms-pronostico](/corte-1-pronosticos/proyecto-thyms-pronostico/) (Corte 1) y su revisión en el [gemelo digital del Corte 2](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/).
- La conclusión del parcial (bajar la producción por debajo de la demanda para drenar inventario) es una decisión de planeación agregada; ver [01-planeacion-agregada-modelo-bowman](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/).


---

<!-- fuente: corte-1-pronosticos/parcial-1/parcial-1-calculos.md -->
# parcial-1-calculos

> **Archivo:** [`parcial-1-calculos.xlsx`](/corte-1-pronosticos/parcial-1/parcial-1-calculos.xlsx) · **Corte 1** · Libro de Excel con 7 hoja(s): `Datos`, `Descriptivo-Estadisticos`, `Descriptivo-Histograma`, `Descriptivo-Boxplot`, `Descriptivo-Scatter`, `Descriptivo-Correlograma`, `Holt`  
> **Nombre original:** `CORTE 1/PARCIAL 1 PPCO.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Libro de cálculos del **Parcial 1 (Entrega I)** del Corte 1. Toma 48 meses de ventas de un producto ([`sales_data.csv`](/corte-1-pronosticos/parcial-1/sales_data.csv)), hace el análisis descriptivo completo (estadísticos, histograma, boxplot, dispersión y correlograma con prueba de Ljung-Box), concluye que la serie tiene **tendencia lineal decreciente y no tiene estacionalidad**, y pronostica los meses 49 a 60 con **suavización exponencial doble (Holt)**, con sus medidas de error. Es la base numérica del informe [`parcial-1-informe.md`](/corte-1-pronosticos/parcial-1/parcial-1-informe.md): las figuras 1, 2, 4, 5 y 6 del Word son gráficos enlazados a las hojas de este libro.

Temas del curso que aplica:
- gráficas y autocorrelación: [L04](/corte-1-pronosticos/03-graficas-y-autocorrelacion/L04-plotting-your-data.md);
- medidas de error (MAD, MSE, MAPE): [L05](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md);
- método de Holt: [L06](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/L06-forecasting-data-with-trend.md) y el Excel de clase [`suavizacion-exponencial-doble-holt.md`](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/suavizacion-exponencial-doble-holt.md);
- por qué no Winters: [L07](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md).

Qué se aprende: a diagnosticar el patrón de una serie con varias gráficas que dicen lo mismo por caminos distintos, y a elegir el método que corresponde a ese patrón.

### Hoja `Datos`

**Objetivo:** copia de `sales_data.csv` con los encabezados en español y una columna `t` (1 a 48) para las regresiones.

**Datos de entrada** (48 filas, filas 2 a 49):

| Columna | Contenido | Mínimo | Máximo | Media |
|---|---|---|---|---|
| A `t` | Índice del mes | 1 | 48 | — |
| B `Mes` | Texto «Mes 1» … «Mes 48» | — | — | — |
| C `Ventas reales` | Demanda observada (unidades) | 671 (mes 48) | 1.134 (mes 1) | 916,0 |
| D `Ventas pronosticadas (orig.)` | Pronóstico que usaba la empresa | 599 | 1.193 | 929,1 |
| E `Inventario` | Inventario a fin de mes | 2.089 (mes 9) | 10.622 (mes 48) | 4.629,6 |
| F `Producción` | Producción del mes | 905 | 1.298 | 1.097,2 |

**Gráfico:** líneas «Serie de tiempo: ventas reales (observación directa)», eje X = Mes (1 a 48), eje Y = Unidades. Muestra una caída casi recta de 1.134 a 671 unidades. Es la Figura 1 del informe.

### Hoja `Descriptivo-Estadisticos`

**Objetivo:** primer resumen numérico de la demanda (columna C de `Datos`).

**Método** (fórmulas de la columna B traducidas):
- $\bar{x}=\frac{1}{n}\sum x_t$ (`AVERAGE`), mediana, moda (`MODE`), $s$ (`STDEV`, muestral), $s^2$ (`VAR`).
- Coeficiente de variación: $CV = s/\bar{x}$ (B10 = B8/B5).
- Rango = máx − mín; cuartiles con `QUARTILE` (método inclusivo); $IQR = Q_3 - Q_1$.
- Asimetría (`SKEW`) y curtosis en exceso (`KURT`).
- Variación total del periodo: $(x_{48} - x_1)/x_1$ (B19).
- Correlación de Pearson entre $t$ y $x_t$ (`CORREL`) y regresión lineal $\hat{x}_t = a + b\,t$ con $b$ = `SLOPE`, $a$ = `INTERCEPT` y $R^2$ = `RSQ`.

**Resultados:**

| Estadístico | Valor |
|---|---|
| n | 48 |
| Media | 916,02 |
| Mediana | 931,5 |
| Moda | 1.063 |
| Desviación estándar | 141,11 |
| Varianza | 19.911,1 |
| CV | 15,4 % |
| Mínimo / máximo / rango | 671 / 1.134 / 463 |
| $Q_1$ / $Q_3$ / IQR | 789,25 / 1.039,25 / 250 |
| Asimetría | −0,251 |
| Curtosis | −1,235 |
| Variación total del periodo | −40,8 % |
| Correlación tiempo–ventas | −0,9939 |
| Pendiente $b$ | −10,0173 unid./mes |
| Intercepto $a$ | 1.161,45 |
| $R^2$ | 0,9878 |

**Conclusión de la hoja** (texto de las filas 26 a 30): la media (916) engaña porque la demanda actual ronda 670; la caída es de unas 10 unidades/mes y casi perfectamente lineal; el CV del 15,4 % viene de la tendencia y no de ruido; la asimetría cercana a 0 y la curtosis negativa indican datos repartidos por todo el rango, sin campana.

### Hoja `Descriptivo-Histograma`

**Objetivo:** ver la forma de la distribución de la demanda.

**Método:** 10 clases de ancho 50 entre 650 y 1.150. Frecuencia con `COUNTIFS`: $f_j = \#\{t : L_j \le x_t < U_j\}$; la última clase es cerrada, $[1.100, 1.150]$. Frecuencia relativa $f_j/n$.

| Clase | Frecuencia | Frec. relativa |
|---|---|---|
| [650-700) | 5 | 10,4 % |
| [700-750) | 3 | 6,25 % |
| [750-800) | 5 | 10,4 % |
| [800-850) | 3 | 6,25 % |
| [850-900) | 5 | 10,4 % |
| [900-950) | 5 | 10,4 % |
| [950-1000) | 4 | 8,33 % |
| [1000-1050) | 7 | 14,6 % |
| [1050-1100) | 7 | 14,6 % |
| [1100-1150] | 4 | 8,33 % |
| Total | 48 | 100 % |

**Gráfico:** barras «Histograma de la demanda (48 meses)», eje X = clase, eje Y = frecuencia (Figura 2 del informe).

**Conclusión:** la distribución es **plana** (3 a 7 meses por clase), sin campana alrededor de la media: es la huella de una serie con tendencia que recorrió todos los niveles de ~1.130 a ~670.

### Hoja `Descriptivo-Boxplot`

**Objetivo:** resumen de cinco números y detección de atípicos.

**Método:** mínimo, $Q_1$, mediana, $Q_3$, máximo; vallas $Q_1 - 1{,}5\,IQR$ y $Q_3 + 1{,}5\,IQR$; atípicos = datos fuera de las vallas (`COUNTIF`).

| Medida | Valor |
|---|---|
| Mínimo | 671 |
| $Q_1$ | 789,25 |
| Mediana | 931,5 |
| $Q_3$ | 1.039,25 |
| Máximo | 1.134 |
| IQR | 250 |
| Valla inferior | 414,25 |
| Valla superior | 1.414,25 |
| Atípicos | 0 |

**Gráfico:** la hoja tiene una imagen (no un gráfico de Excel) con el boxplot horizontal «Boxplot de la demanda (48 meses)», eje X = Unidades de 700 a 1.100, caja de ~789 a ~1.039, mediana en rojo en ~931 y bigotes hasta 671 y 1.134. Es la Figura 3 del informe.

**Conclusión:** caja muy ancha y ningún atípico: la caída no se debe a meses anómalos sino a un descenso gradual (comportamiento estructural).

### Hoja `Descriptivo-Scatter`

**Objetivo:** relación entre el tiempo y la demanda.

**Datos:** $t$ (columna A) y ventas (columna B = `Datos!C`), filas 4 a 51.

**Gráfico:** dispersión «Dispersión: tiempo vs. demanda (con línea de tendencia)», eje X = Mes (t), eje Y = Unidades (Figura 4 del informe). La recta de tendencia es la misma regresión de la hoja de estadísticos: $\hat{x}_t = 1.161{,}45 - 10{,}02\,t$, $R^2 = 0{,}988$.

**Conclusión** (texto de la hoja): franja descendente casi perfecta, residuos pequeños y parejos (±20 a 40 unidades según la hoja), sin curvatura: la relación es lineal y valida métodos con tendencia lineal (Holt o regresión).

### Hoja `Descriptivo-Correlograma`

**Objetivo:** autocorrelaciones de los rezagos 1 a 12 con límites de significancia y prueba de Ljung-Box.

**Datos y parámetros:** $\bar{x}$ = 916,02 (B3), $n$ = 48 (B4), $t_{0{,}025;\,47}$ = 2,01174 (B5 = `TINV(0.05, n-1)`). Las columnas H a J tienen $t$, $x_t$ y $x_t - \bar{x}$.

**Método:**
- Coeficiente de autocorrelación del rezago $k$ (B8 y siguientes, `SUMPRODUCT` de las desviaciones desfasadas sobre `SUMSQ`):
  $$r_k = \frac{\sum_{t=1}^{n-k}(x_t-\bar{x})(x_{t+k}-\bar{x})}{\sum_{t=1}^{n}(x_t-\bar{x})^2}$$
- Error estándar (fórmula de Bartlett): $SE(r_1) = 1/\sqrt{n}$ (C8) y $SE(r_k) = \sqrt{\left(1 + 2\sum_{j=1}^{k-1} r_j^2\right)/n}$ para $k \ge 2$ (C9 en adelante).
- Límites: $\pm\, t_{0{,}025;\,n-1}\cdot SE(r_k)$ (D y E).
- Ljung-Box con $h = 12$ (B22): $Q = n(n+2)\sum_{k=1}^{h}\frac{r_k^2}{n-k}$, comparado con $\chi^2_{0{,}05;\,12}$ = 21,0261 (B23 = `CHIINV(0.05, 12)`). $H_0$: los datos son independientes (ruido).

**Resultados:**

| $k$ | $r_k$ | $SE(r_k)$ | Límite ± | ¿Significativo? |
|---|---|---|---|---|
| 1 | 0,939 | 0,144 | 0,290 | Sí |
| 2 | 0,878 | 0,240 | 0,483 | Sí |
| 3 | 0,817 | 0,299 | 0,602 | Sí |
| 4 | 0,756 | 0,343 | 0,690 | Sí |
| 5 | 0,695 | 0,376 | 0,756 | No |
| 6 | 0,636 | 0,402 | 0,808 | No |
| 7 | 0,579 | 0,422 | 0,850 | No |
| 8 | 0,521 | 0,439 | 0,882 | No |
| 9 | 0,462 | 0,451 | 0,908 | No |
| 10 | 0,403 | 0,461 | 0,927 | No |
| 11 | 0,343 | 0,468 | 0,942 | No |
| 12 | 0,284 | 0,473 | 0,952 | No |

Ljung-Box: $Q$ = 274,426 > 21,026 → se rechaza $H_0$ (D22 escribe «Q > Chi²: se rechaza H0, los datos están correlacionados (hay estructura/tendencia)»).

**Gráfico:** barras + líneas «Correlograma con límites de significancia (95%)»: barras = $r_k$, líneas = límites superior e inferior, eje X = Lag 1 a 12 (Figura 5 del informe).

**Conclusión:** $r_1$ alto que decae despacio (0,94; 0,88; 0,82; 0,76…) = patrón de **tendencia** («Trendline» de la clase L04); sin pico en el rezago 12 → **sin estacionalidad**; la serie no es aleatoria.

### Hoja `Holt`

**Objetivo:** pronosticar la demanda de los meses 49 a 60 con suavización exponencial doble (Holt) y medir el error.

**Parámetros:**
- $\alpha$ = 0,95 (L2): suavización del nivel.
- $\beta$ = 0,05 (L3): suavización de la tendencia.
- Nivel inicial $S_0$ = 1.161,45 (D3 = `INTERCEPT` de la regresión de las 48 ventas sobre $t$).
- Tendencia inicial $G_0$ = −10,0173 (E3 = `SLOPE` de la misma regresión).

**Método paso a paso** (filas 4 a 51 = meses 1 a 48; $D_t$ = demanda del mes $t$):
- Pronóstico a un paso (F4 = D3+E3): $F_t = S_{t-1} + G_{t-1}$.
- Nivel (D4 = `$L$2*C4+(1-$L$2)*(D3+E3)`): $S_t = \alpha D_t + (1-\alpha)(S_{t-1} + G_{t-1})$.
- Tendencia (E4 = `$L$3*(D4-D3)+(1-$L$3)*E3`): $G_t = \beta (S_t - S_{t-1}) + (1-\beta) G_{t-1}$.
- Pronóstico fuera de muestra (F52 = `$D$51+1*$E$51` y siguientes): $F_{48+h} = S_{48} + h\,G_{48}$, con $h$ = 1 a 12.
- Errores por mes: G = $|F_t - D_t|$ (la columna se titula «MAD», pero es el error absoluto de cada mes); H «RESIDUALES» = $F_t - D_t$; I «ERROR RELATIVO» = $|F_t - D_t|/D_t$.
- Resumen (filas 68 a 71): $MAD = \frac{1}{48}\sum |F_t - D_t|$; $MAPE = \frac{1}{48}\sum \frac{|F_t - D_t|}{D_t}$; $SSE = \sum (F_t - D_t)^2$; $MSE = SSE/48$.

**Resultados:**
- Estado final: $S_{48}$ = 670,708 y $G_{48}$ = −10,4203 unid./mes.
- Primeros meses: $F_1$ = 1.151,43 frente a 1.134; $F_2$ = 1.124,03 frente a 1.123; $F_3$ = 1.112,16 frente a 1.107. Últimos: $F_{46}$ = 686,82 frente a 684; $F_{47}$ = 673,32 frente a 676; $F_{48}$ = 665,17 frente a 671.

| Mes | Pronóstico Holt |
|---|---|
| 49 | 660,29 |
| 50 | 649,87 |
| 51 | 639,45 |
| 52 | 629,03 |
| 53 | 618,61 |
| 54 | 608,19 |
| 55 | 597,77 |
| 56 | 587,35 |
| 57 | 576,93 |
| 58 | 566,51 |
| 59 | 556,08 |
| 60 | 545,66 |

| Medida de error (48 meses) | Valor |
|---|---|
| MAD | 5,304 unidades |
| MAPE | 0,598 % (0,005976) |
| SSE | 1.953,72 |
| MSE | 40,70 (RMSE = 6,38) |

El pronóstico original de la empresa (columna D de `Datos`), medido igual, da MAD = 100,2 y MAPE = 11,4 % (recalculado a partir del CSV; el libro no lo calcula).

**Gráfico:** líneas «Demanda real vs. pronóstico Holt (incluye meses 49-60)», eje X = Periodo (inicial y 1 a 60), eje Y = Unidades; la serie del pronóstico se superpone a la demanda en los meses 1 a 48 y continúa la recta descendente hasta ~546 en el mes 60 (Figura 6 del informe).

**Conclusión:** Holt sigue la caída casi sin error (MAD ≈ 5 unidades sobre una demanda de ~900) y proyecta que la demanda seguirá cayendo unas 10,4 unidades por mes.

### Observaciones

- **Inicialización con toda la muestra:** $S_0$ y $G_0$ salen de la regresión sobre los 48 meses, es decir, con información «del futuro». Los errores dentro de la muestra (sobre todo los primeros meses) quedan algo optimistas.
- **α y β sin optimización registrada:** no hay celda de Solver ni tabla de búsqueda. Recalculando en una rejilla con paso 0,05, el par (0,95; 0,05) está muy cerca del óptimo: el menor MSE es α = 1,00, β = 0,05 (MSE 40,69) y el menor MAD es α = 0,95, β = 0,15 (MAD 5,18).
- **Convención de signos:** el residual de la columna H es $F_t - D_t$ (al revés del usual $e_t = D_t - F_t$). Con esa convención, el sesgo promedio es +0,18 unidades.
- **El libro no calcula sesgo ni señal de rastreo**, aunque el informe los reporta (sesgo 0,18 y señal de rastreo 1,6). Recalculados: $\sum (D_t - F_t)/MAD = -1{,}60$ al cierre (en valor absoluto coincide). Con la definición $TS_t = \sum_{i\le t} e_i / MAD_t$ (MAD acumulado hasta $t$), la señal sale del rango ±4 en los meses 15, 16, 18, 19, 38 y 44, no solo en los primeros meses como dice el informe; no se sabe qué definición usó el grupo.
- **Hoja `Descriptivo-Scatter`:** el texto de interpretación se escribió en A28:A34, encima de los valores de $t$ = 25 a 31 (las ventas de la columna B siguen bien). Como el rango X del gráfico contiene texto, Excel probablemente numera los puntos 1, 2, 3…, que coincide con $t$; el gráfico se ve igual, pero la tabla quedó incompleta.
- **Datos sintéticos:** el inventario de `sales_data.csv` no cumple el balance $I_t = I_{t-1} + P_t - D_t$ (por ejemplo, mes 2: 2.546 + 984 − 1.123 = 2.407, pero el dato es 2.435; de los meses 2 a 48, $\sum (P_t - D_t)$ = 8.809 frente a $I_{48} - I_1$ = 8.076).
- La producción promedio de los 48 meses es 1.097,2; el informe dice 1.082 (1.081,1 es el promedio de los primeros 12 meses).
- No hay hojas vacías.


---

<!-- fuente: corte-1-pronosticos/parcial-1/parcial-1-informe.md -->
# parcial-1-informe

> **Archivo:** [`parcial-1-informe.docx`](/corte-1-pronosticos/parcial-1/parcial-1-informe.docx) · **Corte 1** · Documento de Word  
> **Nombre original:** `CORTE 1/PARCIAL 1 PPCO.docx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

### Qué es

Informe escrito del **Parcial 1 — Entrega I** del Corte 1 (pronósticos). Analiza 48 meses de ventas de un producto ([`sales_data.csv`](/corte-1-pronosticos/parcial-1/sales_data.csv)), elige el método de **Holt** (suavización exponencial doble), pronostica los meses 49 a 60, estima el error y cierra con una conclusión gerencial. Todos los números salen del libro [`parcial-1-calculos.md`](/corte-1-pronosticos/parcial-1/parcial-1-calculos.md).

**Enunciado (deducido de los títulos de las secciones):** 1) análisis descriptivo de los datos y elección del método de pronóstico más adecuado; 2) realizar el pronóstico; 3) estimar el error de pronóstico; 4) conclusión gerencial.

### Estructura

| Sección | Qué hace |
|---|---|
| Portada | Logo de la Universidad de La Sabana (imagen), «PARCIAL», «ENTREGA I», miembros y «UNIVERSIDAD DE LA SABANA, CHÍA». La primera línea dice «Gerencia Financiera» (error de plantilla, ver advertencias). |
| Análisis descriptivo y elección del método | Estadísticos básicos y cinco gráficos: serie de tiempo (Fig. 1), histograma (Fig. 2), boxplot (Fig. 3), dispersión tiempo vs. demanda (Fig. 4) y correlograma (Fig. 5). Diagnóstico: tendencia decreciente fuerte, sin estacionalidad. |
| Por qué elegimos Holt | Descarta, uno por uno, el promedio móvil simple, el ponderado, la suavización exponencial simple y Winters, y justifica Holt (Fig. 6: demanda real vs. Holt). Menciona la regresión lineal como otra candidata válida. |
| Realizar el pronóstico | Explica $F_{48+h} = S_{48} + h\,G_{48}$ con $S_{48}$ = 670,7 y $G_{48}$ = −10,43 y da los pronósticos de los meses 49 a 60. |
| Estimar el error | MAD, MAPE, SSE, MSE, RMSE, sesgo, señal de rastreo e intervalo del 95 %. |
| Conclusión gerencial | Declive estructural, exceso de inventario y tres decisiones. |

Las figuras 1, 2, 4, 5 y 6 son gráficos de Word enlazados a las hojas `Datos`, `Descriptivo-Histograma`, `Descriptivo-Scatter`, `Descriptivo-Correlograma` y `Holt` del Excel; la Figura 3 es una imagen del boxplot (caja de ~789 a ~1.039, mediana ~931 en rojo, bigotes de 671 a 1.134).

### Datos que usa

`sales_data.csv`: 48 meses con ventas reales, pronóstico original de la empresa, inventario y producción (ver el [README de la carpeta](/corte-1-pronosticos/parcial-1/README.md)).

### Métodos

- Estadística descriptiva: media, mediana, desviación estándar, $CV = s/\bar{x}$, cuartiles e IQR.
- Gráficas de diagnóstico (clase [L04](/corte-1-pronosticos/03-graficas-y-autocorrelacion/L04-plotting-your-data.md)): serie, histograma, boxplot con vallas $Q_1 - 1{,}5\,IQR$ y $Q_3 + 1{,}5\,IQR$, dispersión con regresión $\hat{x}_t = a + b\,t$.
- Correlograma: $r_k = \frac{\sum_{t=1}^{n-k}(x_t-\bar{x})(x_{t+k}-\bar{x})}{\sum_{t=1}^{n}(x_t-\bar{x})^2}$ con límites de significancia al 95 %, y prueba de Ljung-Box $Q = n(n+2)\sum_{k=1}^{12}\frac{r_k^2}{n-k}$ frente a $\chi^2_{0{,}05;\,12}$.
- Holt ([L06](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/L06-forecasting-data-with-trend.md)): $S_t = \alpha D_t + (1-\alpha)(S_{t-1}+G_{t-1})$, $G_t = \beta(S_t - S_{t-1}) + (1-\beta)G_{t-1}$, $F_{t+h} = S_t + h\,G_t$, con $\alpha$ = 0,95 y $\beta$ = 0,05 ($S_t$ = nivel, $G_t$ = tendencia, $D_t$ = demanda, $h$ = meses hacia adelante).
- Errores ([L05](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md)): $MAD = \frac{1}{n}\sum|e_t|$, $MAPE = \frac{1}{n}\sum\frac{|e_t|}{D_t}$, $SSE = \sum e_t^2$, $MSE = SSE/n$, $RMSE = \sqrt{MSE}$, sesgo $= \frac{1}{n}\sum e_t$.
- Señal de rastreo ([L07](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md)): $TS = \sum e_t / MAD$, aceptable entre −4 y +4.
- Intervalo del 95 % para el mes siguiente: $F \pm 1{,}96 \cdot RMSE$.

### Resultados clave con números

| Resultado | Valor |
|---|---|
| Media / mediana / desviación / CV | 916 / 931,5 / 141 / 15,4 % |
| Máximo (mes 1) / mínimo (mes 48) | 1.134 / 671 |
| Caída acumulada en 48 meses | −40,8 % |
| Regresión | Ventas = 1.161,45 − 10,02·t, $R^2$ = 0,988, correlación −0,994 |
| IQR / atípicos | 250 / ninguno |
| Autocorrelaciones | $r_1$ = 0,94; $r_2$ = 0,88; $r_3$ = 0,82; $r_4$ = 0,76 (los cuatro significativos); sin pico en el rezago 12 |
| Ljung-Box | Q = 274,4 frente a 21,0 → no aleatoria |
| Holt: nivel y tendencia finales | 670,7 y −10,43 unid./mes |
| Pronósticos | Mes 49 ≈ 660; mes 52 ≈ 629; mes 54 ≈ 608; mes 60 ≈ 546 |
| MAD / MAPE | 5,3 unidades / 0,59 % |
| SSE / MSE / RMSE | 1.953,7 / 40,7 / 6,4 |
| Sesgo / señal de rastreo final | 0,18 / 1,6 |
| Intervalo del 95 % (mes 49) | ±12,5 → de 648 a 673 |
| Pronóstico anterior de la empresa | MAPE 11,4 % (error promedio de ~100 unidades) |
| Producción e inventario actuales | ~1.082 unid./mes; inventario > 10.600 (≈ 16 meses de demanda; se cuadruplicó) |

### Conclusiones

1. La demanda está en **declive estructural**: cae unas 10 unidades por mes, ya perdió el 41 % y seguiría bajando hasta ~546 en el mes 60 (≈ 17 % menos en un año).
2. El problema urgente es la respuesta de la empresa: producir ~1.082 unidades/mes con un pronóstico que sobreestimaba (MAPE 11 %) infló el inventario.
3. Tres decisiones: (a) adoptar Holt como pronóstico oficial y recalibrarlo cada mes; (b) recortar la producción por debajo de la demanda, a unas **400–500 unidades/mes**, para drenar el inventario (la sección del pronóstico hablaba de planear alrededor de 600–650 «e incluso por debajo»); (c) investigar las causas del declive y decidir si se invierte en el producto o se gestiona su salida del portafolio.
4. Los primeros 6 meses del pronóstico sirven para decidir producción y compras; los meses 7 a 12 son referencia de planeación.

### Supuestos y advertencias

- **Encabezado equivocado:** la primera línea del documento dice «Gerencia Financiera» por un error de plantilla; el contenido es del curso de Planeación (pronósticos).
- **Producción promedio:** el informe dice 1.082 unidades/mes, pero el promedio de los 48 meses de `sales_data.csv` es 1.097,2 (1.081,1 es el promedio de los primeros 12 meses).
- **MAPE:** el Excel guarda 0,5976 %, que redondea a 0,60 % (el informe escribe 0,59 %).
- **Sesgo y señal de rastreo** no están calculados en el Excel. Recalculados, el sesgo es 0,18 (con error = pronóstico − real) y la señal de rastreo final vale 1,6 en valor absoluto. Pero con la definición de MAD acumulado mes a mes, la señal sale de ±4 en los meses 15, 16, 18, 19, 38 y 44, no solo «en los primeros meses» como afirma el informe.
- **«Regresión prácticamente idéntica»:** la regresión da 670,6 en el mes 49 y 560,4 en el mes 60, frente a 660,3 y 545,7 de Holt: la misma pendiente, pero una diferencia de 10 a 15 unidades.
- El «17 % menos» compara el mes 60 con el pronóstico del mes 49 (546/660 − 1 = −17,4 %); frente a la venta real del mes 48 (671) la caída sería −18,7 %.
- Los errores son **dentro de la muestra** (pronóstico a un paso con parámetros e inicialización que usan los 48 datos), así que son optimistas; el intervalo de ±12,5 solo vale para el mes inmediato.
- El supuesto de fondo es que la caída lineal continúa; el informe lo reconoce y pide recalibrar cada mes.

## Texto completo

Gerencia Financiera

PARCIAL

ENTREGA I

MIEMBROS:

Samuel Gómez Davila- 0000312349

UNIVERSIDAD DE LA SABANA, CHÍA

### Análisis descriptivo de los datos y elegir el método de pronóstico más adecuado

Empezamos por lo básico: organizar los 48 meses de ventas como una serie de tiempo, numerando cada mes del 1 al 48, y sacar los estadísticos para hacernos una primera idea de los datos. La demanda promedio del periodo fue de 916 unidades, con una mediana de 931.5, una desviación estándar de 141 unidades y un coeficiente de variación del 15.4%. Las ventas se movieron entre un máximo de 1,134 unidades al comienzo y un mínimo de 671 al final, y ese detalle, que el máximo estuviera al inicio y el mínimo al final, ya nos hacía sospechar hacia dónde iba la historia.

#### Serie de tiempo

Figura 1
Serie de tiempo de la demanda (48 meses)

Como en clase insistieron en que los promedios no cuentan toda la historia, lo siguiente fue graficar los datos desde varios ángulos. Con solo mirar la serie en la Figura 1 la sospecha se confirmó: la demanda viene cayendo sin pausa, un 40.8% acumulado en los 48 meses. Y cada gráfico que hicimos después nos fue diciendo lo mismo por caminos distintos.

#### Histograma

Figura 2
Histograma de la demanda

El histograma de la Figura 2, por ejemplo, salió plano. Si la demanda fuera estable, esperaríamos una campana concentrada alrededor de la media; en cambio, todas las clases entre 650 y 1,150 unidades tienen frecuencias muy parecidas. Al principio puede parecer raro, pero tiene todo el sentido: una serie que va cayendo no se queda oscilando en un nivel, sino que va pasando por todos los niveles en su camino hacia abajo, y eso reparte los datos por todo el rango.

#### Boxplot

Figura 3
Boxplot de la demanda

El boxplot de la Figura 3 nos dio otra pieza del rompecabezas. La caja es muy ancha, con un rango intercuartílico de 250 unidades, pero no apareció ni un solo dato atípico. Eso descarta una explicación tentadora: que la caída se debiera a uno o dos meses desastrosos por algún evento puntual. No fue así; nada se sale de lo esperado, la demanda simplemente bajó de forma gradual y sostenida. Es un problema estructural, no un accidente.

#### Scatter Plot

Figura 4
Diagrama de dispersión tiempo vs. demanda

El scatter plot de la Figura 4 fue el más contundente de todos. Los puntos forman una franja descendente casi perfecta, sin curvas ni quiebres, y la regresión que le ajustamos, Ventas = 1,161.45 − 10.02·t con un R² de 0.988, dice que el tiempo explica el 98.8% de lo que pasa con las ventas. La correlación de −0.994 lo resume bien: cada mes que pasa, se venden unas diez unidades menos, con una regularidad que casi asusta.

#### Correlograma

Figura 5
Correlograma con límites de significancia al 95%

Para cerrar el diagnóstico construimos el correlograma con sus límites de significancia, siguiendo el procedimiento de clase, y el resultado está en la Figura 5. El patrón es de libro: el coeficiente del primer rezago es altísimo (r₁ = 0.94) y los siguientes van bajando de a poquito (0.88, 0.82, 0.76…), con los primeros cuatro por encima del límite de significancia. Es exactamente la firma de una serie con tendencia. Lo que no apareció fue un pico en el rezago 12, que sería la señal de estacionalidad anual, así que la descartamos. Y por si quedaban dudas, la prueba de Ljung-Box las despejó: Q dio 274.4 contra un chi-cuadrado crítico de 21.0, o sea que los datos definitivamente no son aleatorios. Diagnóstico cerrado: tendencia decreciente fuerte, sin estacionalidad.

#### Por qué elegimos Holt

La elección no fue solo porque dio los mejores números, aunque los dio. La razón de fondo es que el método tiene que corresponder al comportamiento de los datos, y nuestra serie tiene una característica dominante: la tendencia decreciente. Con ese diagnóstico en mano, la forma más honesta de justificar la elección es mostrar por qué los demás métodos no servían para este caso.

El promedio móvil simple lo descartamos de entrada. Este método pronostica con el promedio de los últimos k periodos, lo cual funciona bien cuando la demanda es estable y oscila alrededor de un nivel constante. Pero nuestra demanda no oscila: cae. Y en una serie que cae, el pasado siempre es más alto que el presente, así que el promedio de los últimos meses queda inevitablemente por encima de la venta que viene. El resultado sería un pronóstico que sobreestima la demanda mes tras mes, de forma sistemática, que es justo el tipo de error que llevó a la empresa a acumular inventario.

El promedio móvil ponderado tampoco resuelve el problema. Es cierto que al darle más peso a los meses recientes el pronóstico reacciona más rápido, y por eso el error se reduce un poco frente al promedio simple. Pero el defecto de fondo sigue intacto: el método no tiene ninguna manera de proyectar la caída hacia adelante, porque sigue siendo un promedio de valores pasados. En el mejor de los casos persigue la tendencia siempre desde atrás, llegando tarde a cada mes. Cambiar los pesos alivia el síntoma, no cura la enfermedad.

La suavización exponencial simple fue la tercera descartada, y quizás la más ilustrativa. Es un método más refinado que los promedios móviles, porque pondera toda la historia con pesos que decaen exponencialmente. Sin embargo, su fórmula estima un solo componente: el nivel de la demanda. Al asumir que no existe tendencia, en una serie decreciente carga un sesgo positivo permanente que ningún valor de alfa puede eliminar del todo: con alfa alto se pega más al último dato, pero sigue pronosticando el pasado inmediato, no la caída que viene. De hecho, el pronóstico que la empresa venía usando cometía en esencia este mismo error, y su MAPE del 11.4% con el inventario cuadruplicado son la evidencia de lo que cuesta ignorar una tendencia.

Con Winters pasó lo contrario: lo descartamos no porque le falte algo, sino porque le sobra. El método de Winters está diseñado para series que tienen tendencia y además estacionalidad, ya que estima tres componentes (nivel, tendencia y factores estacionales). Pero nuestro análisis descriptivo fue claro en ese punto: el correlograma no mostró ningún pico en el rezago 12, que sería la firma de un patrón anual. Aplicar Winters aquí habría significado estimar un componente estacional que no existe, agregando parámetros y complejidad al modelo sin ninguna ganancia en precisión. Y en pronósticos, un modelo con parámetros de más no es más completo, es más frágil.

Figura 6
Demanda real vs. pronóstico del método de Holt

Descartadas esas cuatro alternativas, el método de Holt quedó como la elección natural, porque está diseñado exactamente para el patrón que tiene nuestra serie: tendencia sin estacionalidad. A diferencia de los anteriores, no trabaja con un solo componente sino con dos: estima el nivel de la demanda y aparte estima la pendiente, y va actualizando ambos cada mes con la información nueva que llega. Eso le permite incorporar la caída al pronóstico en lugar de perseguirla desde atrás. Los resultados lo confirmaron: obtuvo un MAD de apenas 5.3 unidades y un MAPE del 0.59%, los menores errores entre todos los métodos evaluados. La Figura 6 lo muestra bien: la línea del pronóstico se superpone casi por completo sobre la demanda real durante los 48 meses de historia y, a partir del mes 49, prolonga la caída de forma coherente hasta llegar a unas 546 unidades en el mes 60. Y tiene una ventaja adicional frente a la regresión lineal, que era la otra candidata válida: la regresión asume que la pendiente será la misma para siempre, mientras que Holt la recalcula con cada dato nuevo, así que, si el día de mañana la caída se frena o se acelera, el modelo se acomoda solo, sin que haya que rehacer nada.

### Realizar el pronóstico

Una vez elegido el método de Holt, lo aplicamos para proyectar la demanda de los próximos doce meses. El procedimiento es directo: al recorrer los 48 meses de historia, el modelo termina con dos valores estimados, el nivel de la demanda al cierre del periodo, que quedó en 670.7 unidades, y la tendencia final, que quedó en −10.43 unidades por mes. Con esos dos componentes, el pronóstico de cualquier mes futuro se calcula sumando al nivel tantas veces la tendencia como meses hacia adelante queramos ver. Por ejemplo, para el mes 49 el cálculo es 670.7 menos 10.43, que da unas 660 unidades; para el mes 50 se restan dos veces, y así sucesivamente.

Los resultados muestran una demanda que seguiría cayendo de forma gradual: alrededor de 660 unidades en el mes 49, 629 hacia el mes 52, 608 en el mes 54, y cerca de 546 al llegar al mes 60. En otras palabras, si la tendencia actual se mantiene, la empresa vendería en un año aproximadamente un 17% menos que hoy. Como verificación, corrimos el mismo pronóstico con la regresión lineal y los números resultaron prácticamente idénticos: ambos métodos coinciden en que la demanda pierde unas diez unidades cada mes, lo que nos da bastante confianza en la magnitud de la proyección.

Ahora bien, hay dos precisiones que nos parece honesto dejar por escrito. La primera es que todo pronóstico pierde confiabilidad a medida que se aleja en el tiempo: los primeros seis meses de la proyección son suficientemente sólidos para tomar decisiones de producción y compras, mientras que los meses siete a doce conviene tratarlos como una referencia de planeación, no como una cifra comprometida. La segunda es que el modelo asume que la caída continúa al ritmo actual. Esto no es un problema grave porque el método de Holt se recalibra solo, porque cada mes que entra un dato real nuevo ajusta su estimación de la tendencia, pero sí implica una disciplina: hay que actualizar el pronóstico mensualmente y estar atentos a cualquier señal de que la demanda se estabiliza o se acelera.

La conclusión práctica del pronóstico es contundente. Hoy la empresa produce en promedio 1,082 unidades al mes para una demanda que ronda las 650 y va en descenso. Esa brecha es la que infló el inventario hasta superar las 10,600 unidades, que al ritmo de ventas proyectado equivalen a unos dieciséis meses de demanda. El pronóstico indica que la producción debería planearse alrededor de las 600 a 650 unidades mensuales, e incluso por debajo de la demanda durante algunos meses, para permitir que el inventario acumulado se drene y los costos de almacenamiento bajen.

### Estimar el error de pronóstico

Elegir un método de pronóstico no basta: también hay que saber qué tanto se equivoca, porque de ese margen de error depende cuánta holgura debemos dejar en los planes de producción y de inventario. Para estimarlo, comparamos mes a mes el pronóstico de Holt contra la venta real en los 48 periodos evaluados, y a partir de esas diferencias calculamos las medidas de error habituales.

Los resultados fueron muy buenos. El error absoluto medio, o MAD, fue de apenas 5.3 unidades: en un mes típico el pronóstico se desvía unas cinco unidades de la venta real, sobre una demanda que promedia unas 900. Llevado a términos relativos, eso equivale a un MAPE del 0.59%, es decir, el modelo acierta en más del 99% de la magnitud de la demanda. Calculamos también la suma de errores al cuadrado (SSE), que dio 1,953.7, y el error cuadrático medio (MSE), que quedó en 40.7; su raíz, el RMSE, resulta en 6.4 unidades, muy cercana al MAD. Esa cercanía entre las dos medidas nos dice algo adicional: no hubo meses con errores desproporcionados, el modelo se equivoca poco y de manera pareja a lo largo de todo el periodo.

Hicimos además dos verificaciones que nos dieron tranquilidad sobre la calidad del pronóstico. La primera fue el sesgo, que mide si el modelo tiende a pronosticar sistemáticamente por encima o por debajo de la realidad. Nos dio 0.18 unidades, prácticamente cero, lo que significa que los errores hacia arriba y hacia abajo se compensan entre sí. Esto es justo lo contrario de lo que ocurría con el pronóstico anterior de la empresa, que sobreestimaba la demanda mes tras mes y por eso terminó inflando el inventario. La segunda verificación fue la señal de rastreo, un indicador que va acumulando los errores y avisa cuando un modelo empieza a desviarse de forma sostenida. La regla práctica dice que debe mantenerse entre menos cuatro y más cuatro veces el MAD, y la nuestra cerró en 1.6, cómodamente dentro de la zona de control. Vale aclarar que en los primeros meses la señal se sale de rango, pero es un efecto normal del arranque, cuando todavía hay muy pocos datos acumulados; pasado ese periodo de calentamiento, se estabiliza y ya no vuelve a salirse.

Con el RMSE pudimos, por último, ponerle una banda de confianza al pronóstico. Asumiendo que los errores se comportan de manera aproximadamente normal, el intervalo del 95% resulta de unas doce unidades y media hacia arriba o hacia abajo. En la práctica esto significa que cuando decimos que el mes 49 venderá alrededor de 660 unidades, lo razonable es esperar que la cifra real caiga entre 648 y 673. Para efectos de planeación es un margen muy manejable, aunque hay que tener presente que aplica al pronóstico del mes inmediato: a medida que proyectamos más lejos en el tiempo la incertidumbre crece, y esa es una razón más para recalibrar el modelo cada mes con el dato real que vaya llegando.

### Conclusión gerencial

El análisis deja un mensaje central que la gerencia debe asumir cuanto antes: la demanda de este producto no está pasando por un mal momento, está en declive estructural. Lleva 48 meses cayendo a un ritmo constante de unas diez unidades mensuales, ha perdido ya el 41% de su volumen inicial, y el pronóstico indica que la tendencia continuará, con ventas que bajarían de las 660 unidades actuales a cerca de 546 dentro de un año. No se trata de una proyección especulativa: el comportamiento de la serie es tan regular que dos métodos independientes llegan prácticamente a la misma cifra, y el modelo elegido demostró equivocarse en promedio apenas cinco unidades por mes.

El problema más urgente, sin embargo, no es la caída de la demanda en sí, sino la respuesta que la empresa le ha venido dando. Mientras las ventas bajaban, la producción se mantuvo alrededor de las 1,082 unidades mensuales, apoyada en un pronóstico que sobreestimaba la demanda con un error promedio del 11%. La consecuencia está a la vista: el inventario se cuadruplicó hasta superar las 10,600 unidades, que al ritmo de ventas actual representan unos dieciséis meses de demanda inmovilizados en bodega, con todo lo que eso implica en costos de almacenamiento, capital de trabajo atrapado y riesgo de obsolescencia.

De este diagnóstico se desprenden tres decisiones concretas. La primera es adoptar de inmediato el método de Holt como herramienta oficial de pronóstico, recalibrándolo cada mes con el dato real nuevo; el costo de implementarlo es mínimo y reduce el error de pronóstico de cien unidades a cinco. La segunda es recortar la producción de manera decidida: no basta con bajarla al nivel de la demanda proyectada, sino que conviene ubicarla por debajo durante varios meses, en el orden de las 400 a 500 unidades mensuales, para que el exceso de inventario se drene de forma controlada mientras las ventas se atienden desde bodega. La tercera es de más largo plazo: una demanda que cae de forma tan sostenida rara vez se revierte sola, así que la empresa debería investigar las causas del declive (competencia, sustitución del producto, cambios en el mercado) y evaluar si este producto amerita inversión comercial para recuperarlo o si lo sensato es gestionar su salida ordenada del portafolio.

En síntesis, hoy la empresa cuenta por primera vez con un pronóstico confiable, y ese pronóstico dice con claridad que el escenario es de contracción. La diferencia entre actuar ahora o dentro de seis meses se medirá en miles de unidades adicionales acumuladas en bodega. La recomendación de este informe es alinear la producción con la realidad de la demanda de inmediato, y usar el tiempo que el inventario actual concede para decidir, con datos, el futuro del producto.



---

<!-- fuente: corte-1-pronosticos/parcial-1/sales_data.csv -->
# Código: `corte-1-pronosticos/parcial-1/sales_data.csv`

> Archivo completo: https://github.com/samuelgradientai-sys/planeacion-control-produccion/blob/main/corte-1-pronosticos/parcial-1/sales_data.csv

```csv
Month,Actual Sales,Forecasted Sales,Inventory Levels,Production Levels
Month 1,1134,1193,2546,1023
Month 2,1123,1098,2435,984
Month 3,1107,1087,2296,1162
Month 4,1102,913,2351,1083
Month 5,1088,1022,2332,1021
Month 6,1081,912,2265,976
Month 7,1071,1056,2160,1104
Month 8,1063,1002,2193,959
Month 9,1063,949,2089,1298
Month 10,1059,884,2324,972
Month 11,1051,902,2237,1160
Month 12,1043,1049,2346,1231
Month 13,1038,1116,2534,968
Month 14,1034,980,2464,1047
Month 15,1026,851,2477,1166
Month 16,1024,897,2617,982
Month 17,1008,910,2575,913
Month 18,1000,1177,2480,1144
Month 19,997,934,2624,1201
Month 20,980,1119,2828,1177
Month 21,971,1137,3025,1289
Month 22,951,954,3343,1237
Month 23,938,966,3629,1289
Month 24,935,1028,3980,1129
Month 25,928,996,4174,905
Month 26,918,768,4151,1095
Month 27,911,942,4328,954
Month 28,892,921,4371,987
Month 29,887,779,4466,1122
Month 30,871,905,4701,997
Month 31,866,973,4827,1289
Month 32,862,923,5250,1237
Month 33,847,1009,5625,906
Month 34,826,1069,5684,1090
Month 35,805,716,5948,974
Month 36,793,874,6117,1291
Month 37,778,732,6615,999
Month 38,765,770,6836,981
Month 39,763,929,7052,1024
Month 40,753,628,7313,1242
Month 41,738,965,7802,978
Month 42,735,947,8042,1073
Month 43,716,734,8380,1213
Month 44,699,750,8877,922
Month 45,698,837,9100,1296
Month 46,684,876,9698,1079
Month 47,676,819,10093,1205
Month 48,671,599,10622,1293
```
