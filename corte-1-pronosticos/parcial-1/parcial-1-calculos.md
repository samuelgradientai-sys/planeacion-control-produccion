# parcial-1-calculos

> **Archivo:** [`parcial-1-calculos.xlsx`](./parcial-1-calculos.xlsx) · **Corte 1** · Libro de Excel con 7 hoja(s): `Datos`, `Descriptivo-Estadisticos`, `Descriptivo-Histograma`, `Descriptivo-Boxplot`, `Descriptivo-Scatter`, `Descriptivo-Correlograma`, `Holt`  
> **Nombre original:** `CORTE 1/PARCIAL 1 PPCO.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Libro de cálculos del **Parcial 1 (Entrega I)** del Corte 1. Toma 48 meses de ventas de un producto ([`sales_data.csv`](./sales_data.csv)), hace el análisis descriptivo completo (estadísticos, histograma, boxplot, dispersión y correlograma con prueba de Ljung-Box), concluye que la serie tiene **tendencia lineal decreciente y no tiene estacionalidad**, y pronostica los meses 49 a 60 con **suavización exponencial doble (Holt)**, con sus medidas de error. Es la base numérica del informe [`parcial-1-informe.md`](./parcial-1-informe.md): las figuras 1, 2, 4, 5 y 6 del Word son gráficos enlazados a las hojas de este libro.

Temas del curso que aplica:
- gráficas y autocorrelación: [L04](../03-graficas-y-autocorrelacion/L04-plotting-your-data.md);
- medidas de error (MAD, MSE, MAPE): [L05](../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md);
- método de Holt: [L06](../05-tendencia-suavizacion-doble-holt/L06-forecasting-data-with-trend.md) y el Excel de clase [`suavizacion-exponencial-doble-holt.md`](../05-tendencia-suavizacion-doble-holt/suavizacion-exponencial-doble-holt.md);
- por qué no Winters: [L07](../06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md).

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

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `Datos` — 49 filas × 6 columnas · 1 gráfico(s)

**Gráficos en esta hoja:**

- Gráfico de líneas — título «Serie de tiempo: ventas reales (observación directa)» · ejes: Mes / Unidades
  - Series: Datos!$C$1: y = `Datos!$C$2:$C$49`, x = `Datos!$A$2:$A$49`

| Fila | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 1 | t | Mes | Ventas reales | Ventas pronosticadas (orig.) | Inventario | Producción |
| 2 | 1 | Mes 1 | 1134 | 1193 | 2546 | 1023 |
| 3 | 2 | Mes 2 | 1123 | 1098 | 2435 | 984 |
| 4 | 3 | Mes 3 | 1107 | 1087 | 2296 | 1162 |
| 5 | 4 | Mes 4 | 1102 | 913 | 2351 | 1083 |
| 6 | 5 | Mes 5 | 1088 | 1022 | 2332 | 1021 |
| 7 | 6 | Mes 6 | 1081 | 912 | 2265 | 976 |
| 8 | 7 | Mes 7 | 1071 | 1056 | 2160 | 1104 |
| 9 | 8 | Mes 8 | 1063 | 1002 | 2193 | 959 |
| 10 | 9 | Mes 9 | 1063 | 949 | 2089 | 1298 |
| 11 | 10 | Mes 10 | 1059 | 884 | 2324 | 972 |
| 12 | 11 | Mes 11 | 1051 | 902 | 2237 | 1160 |
| 13 | 12 | Mes 12 | 1043 | 1049 | 2346 | 1231 |
| 14 | 13 | Mes 13 | 1038 | 1116 | 2534 | 968 |
| 15 | 14 | Mes 14 | 1034 | 980 | 2464 | 1047 |
| 16 | 15 | Mes 15 | 1026 | 851 | 2477 | 1166 |
| 17 | 16 | Mes 16 | 1024 | 897 | 2617 | 982 |
| 18 | 17 | Mes 17 | 1008 | 910 | 2575 | 913 |
| 19 | 18 | Mes 18 | 1000 | 1177 | 2480 | 1144 |
| 20 | 19 | Mes 19 | 997 | 934 | 2624 | 1201 |
| 21 | 20 | Mes 20 | 980 | 1119 | 2828 | 1177 |
| 22 | 21 | Mes 21 | 971 | 1137 | 3025 | 1289 |
| 23 | 22 | Mes 22 | 951 | 954 | 3343 | 1237 |
| 24 | 23 | Mes 23 | 938 | 966 | 3629 | 1289 |
| 25 | 24 | Mes 24 | 935 | 1028 | 3980 | 1129 |
| 26 | 25 | Mes 25 | 928 | 996 | 4174 | 905 |
| 27 | 26 | Mes 26 | 918 | 768 | 4151 | 1095 |
| 28 | 27 | Mes 27 | 911 | 942 | 4328 | 954 |
| 29 | 28 | Mes 28 | 892 | 921 | 4371 | 987 |
| 30 | 29 | Mes 29 | 887 | 779 | 4466 | 1122 |
| 31 | 30 | Mes 30 | 871 | 905 | 4701 | 997 |
| 32 | 31 | Mes 31 | 866 | 973 | 4827 | 1289 |
| 33 | 32 | Mes 32 | 862 | 923 | 5250 | 1237 |
| 34 | 33 | Mes 33 | 847 | 1009 | 5625 | 906 |
| 35 | 34 | Mes 34 | 826 | 1069 | 5684 | 1090 |
| 36 | 35 | Mes 35 | 805 | 716 | 5948 | 974 |
| 37 | 36 | Mes 36 | 793 | 874 | 6117 | 1291 |
| 38 | 37 | Mes 37 | 778 | 732 | 6615 | 999 |
| 39 | 38 | Mes 38 | 765 | 770 | 6836 | 981 |
| 40 | 39 | Mes 39 | 763 | 929 | 7052 | 1024 |
| 41 | 40 | Mes 40 | 753 | 628 | 7313 | 1242 |
| 42 | 41 | Mes 41 | 738 | 965 | 7802 | 978 |
| 43 | 42 | Mes 42 | 735 | 947 | 8042 | 1073 |
| 44 | 43 | Mes 43 | 716 | 734 | 8380 | 1213 |
| 45 | 44 | Mes 44 | 699 | 750 | 8877 | 922 |
| 46 | 45 | Mes 45 | 698 | 837 | 9100 | 1296 |
| 47 | 46 | Mes 46 | 684 | 876 | 9698 | 1079 |
| 48 | 47 | Mes 47 | 676 | 819 | 10093 | 1205 |
| 49 | 48 | Mes 48 | 671 | 599 | 10622 | 1293 |

### Hoja `Descriptivo-Estadisticos` — 30 filas × 2 columnas

| Fila | A | B |
|---|---|---|
| 1 | 1. Análisis descriptivo — estadísticos |  |
| 3 | Estadístico | Valor |
| 4 | Número de observaciones (n) | 48 |
| 5 | Media | 916.021 |
| 6 | Mediana | 931.5 |
| 7 | Moda | 1063 |
| 8 | Desviación estándar | 141.107 |
| 9 | Varianza | 19911.1 |
| 10 | Coeficiente de variación (CV) | 0.154043 |
| 11 | Mínimo | 671 |
| 12 | Máximo | 1134 |
| 13 | Rango | 463 |
| 14 | Cuartil 1 (Q1) | 789.25 |
| 15 | Cuartil 3 (Q3) | 1039.25 |
| 16 | Rango intercuartílico (IQR) | 250 |
| 17 | Asimetría | -0.250804 |
| 18 | Curtosis | -1.23493 |
| 19 | Variación total del periodo | -0.408289 |
| 20 | Correlación tiempo vs. ventas | -0.993875 |
| 21 | Pendiente de la tendencia (unid./mes) | -10.0173 |
| 22 | Intercepto de la tendencia | 1161.45 |
| 23 | R² de la regresión lineal | 0.987788 |
| 25 | Interpretación: |  |
| 26 | • La media (916) supera a la demanda actual (~670): en una serie con tendencia, el promedio engaña. |  |
| 27 | • Pendiente de -10 unid./mes con R² = 0.99: la caída es fuerte y casi perfectamente lineal. |  |
| 28 | • CV = 15.4%: la dispersión proviene de la tendencia, no de volatilidad aleatoria. |  |
| 29 | • Asimetría cercana a 0 y curtosis negativa: valores repartidos a lo largo del rango, sin campana. |  |
| 30 | • Ver las hojas siguientes para el análisis gráfico: histograma, boxplot, scatter y correlograma. |  |

**Fórmulas (18 patrones distintos):**

- `B4`: `=COUNT(Datos!C2:C49)`
- `B5`: `=AVERAGE(Datos!C2:C49)`
- `B6`: `=MEDIAN(Datos!C2:C49)`
- `B7`: `=MODE(Datos!C2:C49)`
- `B8`: `=STDEV(Datos!C2:C49)`
- `B9`: `=VAR(Datos!C2:C49)`
- `B10`: `=B8/B5`
- `B11`: `=MIN(Datos!C2:C49)`
- `B12`: `=MAX(Datos!C2:C49)`
- `B13`: `=B12-B11`
- `B14`: `=QUARTILE(Datos!C2:C49,1)`
- `B17`: `=SKEW(Datos!C2:C49)`
- `B18`: `=KURT(Datos!C2:C49)`
- `B19`: `=(Datos!C49-Datos!C2)/Datos!C2`
- `B20`: `=CORREL(Datos!A2:A49,Datos!C2:C49)`
- `B21`: `=SLOPE(Datos!C2:C49,Datos!A2:A49)`
- `B22`: `=INTERCEPT(Datos!C2:C49,Datos!A2:A49)`
- `B23`: `=RSQ(Datos!C2:C49,Datos!A2:A49)`

### Hoja `Descriptivo-Histograma` — 22 filas × 5 columnas · 1 gráfico(s)

**Gráficos en esta hoja:**

- Gráfico de barras — título «Histograma de la demanda (48 meses)» · ejes: Clase (unidades) / Frecuencia
  - Series: 'Descriptivo-Histograma'!$D$3: y = `'Descriptivo-Histograma'!$D$4:$D$13`, x = `'Descriptivo-Histograma'!$C$4:$C$13`

| Fila | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | 1a. Histograma de la demanda |  |  |  |  |
| 3 | Límite inferior | Límite superior | Clase | Frecuencia | Frec. relativa |
| 4 | 650 | 700 | [650-700) | 5 | 0.104167 |
| 5 | 700 | 750 | [700-750) | 3 | 0.0625 |
| 6 | 750 | 800 | [750-800) | 5 | 0.104167 |
| 7 | 800 | 850 | [800-850) | 3 | 0.0625 |
| 8 | 850 | 900 | [850-900) | 5 | 0.104167 |
| 9 | 900 | 950 | [900-950) | 5 | 0.104167 |
| 10 | 950 | 1000 | [950-1000) | 4 | 0.0833333 |
| 11 | 1000 | 1050 | [1000-1050) | 7 | 0.145833 |
| 12 | 1050 | 1100 | [1050-1100) | 7 | 0.145833 |
| 13 | 1100 | 1150 | [1100-1150) | 4 | 0.0833333 |
| 14 |  |  | Total | 48 | 1 |
| 16 | Interpretación del histograma: |  |  |  |  |
| 17 | • La distribución es PLANA: todas las clases tienen frecuencias parecidas (3 a 7 meses cada una). |  |  |  |  |
| 18 | • No aparece una campana centrada en la media, que es lo que se esperaría de una demanda estable. |  |  |  |  |
| 19 | • Esa forma extendida es la huella de una serie con tendencia: la demanda no oscila alrededor de |  |  |  |  |
| 20 | un nivel, sino que fue pasando por todos los niveles desde ~1,130 hasta ~670. |  |  |  |  |
| 21 | • Conclusión: el histograma descarta el modelo de 'demanda constante + ruido' y apunta a que el |  |  |  |  |
| 22 | tiempo es la variable clave (lo confirman el scatter y el correlograma). |  |  |  |  |

**Fórmulas (5 patrones distintos):**

- `D4`: `=COUNTIFS(Datos!$C$2:$C$49,">="&A4,Datos!$C$2:$C$49,"<"&B4)`
- `E4`: `=D4/COUNT(Datos!$C$2:$C$49)`
- `D13`: `=COUNTIFS(Datos!$C$2:$C$49,">="&A13,Datos!$C$2:$C$49,"<="&B13)`
- `D14`: `=SUM(D4:D13)`
- `E14`: `=SUM(E4:E13)`

### Hoja `Descriptivo-Boxplot` — 22 filas × 2 columnas · 1 imagen(es)

| Fila | A | B |
|---|---|---|
| 1 | 1b. Boxplot (diagrama de caja) de la demanda |  |
| 3 | Medida | Valor |
| 4 | Mínimo | 671 |
| 5 | Cuartil 1 (Q1) | 789.25 |
| 6 | Mediana (Q2) | 931.5 |
| 7 | Cuartil 3 (Q3) | 1039.25 |
| 8 | Máximo | 1134 |
| 9 | IQR (Q3-Q1) | 250 |
| 10 | Límite inferior atípicos (Q1-1.5·IQR) | 414.25 |
| 11 | Límite superior atípicos (Q3+1.5·IQR) | 1414.25 |
| 12 | Datos atípicos detectados | 0 |
| 15 | Interpretación del boxplot: |  |
| 16 | • Caja muy ancha: IQR = 250 unidades (Q1 = 789, Q3 = 1,039). El 50% central de los datos abarca |  |
| 17 | un rango enorme, señal de que la serie recorrió muchos niveles distintos. |  |
| 18 | • La mediana (931.5) está levemente cargada hacia arriba dentro de la caja, reflejo de que la serie |  |
| 19 | pasó más tiempo en niveles altos al inicio y ha ido descendiendo. |  |
| 20 | • No hay datos atípicos (ningún punto fuera de los límites de 1.5·IQR): la caída no se debe a |  |
| 21 | meses anómalos o eventos puntuales, sino a un descenso gradual y sostenido. |  |
| 22 | • Conclusión: variabilidad amplia SIN outliers = comportamiento estructural (tendencia), no ruido. |  |

**Fórmulas (8 patrones distintos):**

- `B4`: `=MIN(Datos!C2:C49)`
- `B5`: `=QUARTILE(Datos!C2:C49,1)`
- `B6`: `=MEDIAN(Datos!C2:C49)`
- `B8`: `=MAX(Datos!C2:C49)`
- `B9`: `=B7-B5`
- `B10`: `=B5-1.5*B9`
- `B11`: `=B7+1.5*B9`
- `B12`: `=COUNTIF(Datos!C2:C49,"<"&B10)+COUNTIF(Datos!C2:C49,">"&B11)`

### Hoja `Descriptivo-Scatter` — 51 filas × 2 columnas · 1 gráfico(s)

**Gráficos en esta hoja:**

- Gráfico de dispersión — título «Dispersión: tiempo vs. demanda (con línea de tendencia)» · ejes: Mes (t) / Unidades
  - Series: 'Descriptivo-Scatter'!$B$3: y = `'Descriptivo-Scatter'!$B$4:$B$51`, x = `'Descriptivo-Scatter'!$A$4:$A$51`

| Fila | A | B |
|---|---|---|
| 1 | 1c. Scatter plot: tiempo (t) vs. demanda |  |
| 3 | t | Ventas reales |
| 4 | 1 | 1134 |
| 5 | 2 | 1123 |
| 6 | 3 | 1107 |
| 7 | 4 | 1102 |
| 8 | 5 | 1088 |
| 9 | 6 | 1081 |
| 10 | 7 | 1071 |
| 11 | 8 | 1063 |
| 12 | 9 | 1063 |
| 13 | 10 | 1059 |
| 14 | 11 | 1051 |
| 15 | 12 | 1043 |
| 16 | 13 | 1038 |
| 17 | 14 | 1034 |
| 18 | 15 | 1026 |
| 19 | 16 | 1024 |
| 20 | 17 | 1008 |
| 21 | 18 | 1000 |
| 22 | 19 | 997 |
| 23 | 20 | 980 |
| 24 | 21 | 971 |
| 25 | 22 | 951 |
| 26 | 23 | 938 |
| 27 | 24 | 935 |
| 28 | Interpretación del scatter plot: | 928 |
| 29 | • Los puntos forman una franja descendente casi perfecta: a mayor t, menor demanda, sin excepciones. | 918 |
| 30 | • La línea de tendencia ajustada es Ventas = 1,161.45 - 10.02·t con R² = 0.988: el tiempo explica | 911 |
| 31 | el 98.8% de la variación de las ventas. | 892 |
| 32 | • La dispersión alrededor de la recta es pequeña y pareja (±20-40 unidades), sin curvatura visible: | 887 |
| 33 | la relación es LINEAL, no exponencial ni con quiebres. | 871 |
| 34 | • Conclusión: el scatter valida usar métodos con componente de tendencia lineal (Holt / regresión). | 866 |
| 35 | 32 | 862 |
| 36 | 33 | 847 |
| 37 | 34 | 826 |
| 38 | 35 | 805 |
| 39 | 36 | 793 |
| 40 | 37 | 778 |
| 41 | 38 | 765 |
| 42 | 39 | 763 |
| 43 | 40 | 753 |
| 44 | 41 | 738 |
| 45 | 42 | 735 |
| 46 | 43 | 716 |
| 47 | 44 | 699 |
| 48 | 45 | 698 |
| 49 | 46 | 684 |
| 50 | 47 | 676 |
| 51 | 48 | 671 |

**Fórmulas (1 patrones distintos):**

- `B4`: `=Datos!C2`

### Hoja `Descriptivo-Correlograma` — 56 filas × 10 columnas · 1 gráfico(s)

**Gráficos en esta hoja:**

- Gráfico de barras + líneas — título «Correlograma con límites de significancia (95%)» · ejes: Lag / Autocorrelación
  - Series: 'Descriptivo-Correlograma'!$B$7: y = `'Descriptivo-Correlograma'!$B$8:$B$19`, x = `'Descriptivo-Correlograma'!$A$8:$A$19`; 'Descriptivo-Correlograma'!$D$7: y = `'Descriptivo-Correlograma'!$D$8:$D$19`, x = `'Descriptivo-Correlograma'!$A$8:$A$19`; 'Descriptivo-Correlograma'!$E$7: y = `'Descriptivo-Correlograma'!$E$8:$E$19`, x = `'Descriptivo-Correlograma'!$A$8:$A$19`

| Fila | A | B | C | D | E | F | G | H | I | J |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1d. Correlograma (coeficientes de autocorrelación) |  |  |  |  |  |  |  |  |  |
| 3 | Media | 916.021 |  |  |  |  |  | t | x(t) | x(t) - media |
| 4 | n | 48 |  |  |  |  |  | 1 | 1134 | 217.979 |
| 5 | t student (95%, n-1 g.l.) | 2.01174 |  |  |  |  |  | 2 | 1123 | 206.979 |
| 6 |  |  |  |  |  |  |  | 3 | 1107 | 190.979 |
| 7 | Lag (k) | r(k) | SE r(k) | Límite superior | Límite inferior |  |  | 4 | 1102 | 185.979 |
| 8 | 1 | 0.939256 | 0.144338 | 0.29037 | -0.29037 |  |  | 5 | 1088 | 171.979 |
| 9 | 2 | 0.877616 | 0.239983 | 0.482783 | -0.482783 |  |  | 6 | 1081 | 164.979 |
| 10 | 3 | 0.817051 | 0.299473 | 0.602461 | -0.602461 |  |  | 7 | 1071 | 154.979 |
| 11 | 4 | 0.756431 | 0.342782 | 0.689588 | -0.689588 |  |  | 8 | 1063 | 146.979 |
| 12 | 5 | 0.695256 | 0.375953 | 0.75632 | -0.75632 |  |  | 9 | 1063 | 146.979 |
| 13 | 6 | 0.635649 | 0.401848 | 0.808413 | -0.808413 |  |  | 10 | 1059 | 142.979 |
| 14 | 7 | 0.578955 | 0.422276 | 0.849509 | -0.849509 |  |  | 11 | 1051 | 134.979 |
| 15 | 8 | 0.520779 | 0.438501 | 0.88215 | -0.88215 |  |  | 12 | 1043 | 126.979 |
| 16 | 9 | 0.46227 | 0.451202 | 0.907702 | -0.907702 |  |  | 13 | 1038 | 121.979 |
| 17 | 10 | 0.403378 | 0.460964 | 0.927339 | -0.927339 |  |  | 14 | 1034 | 117.979 |
| 18 | 11 | 0.342795 | 0.46826 | 0.942017 | -0.942017 |  |  | 15 | 1026 | 109.979 |
| 19 | 12 | 0.283766 | 0.473459 | 0.952476 | -0.952476 |  |  | 16 | 1024 | 107.979 |
| 20 |  |  |  |  |  |  |  | 17 | 1008 | 91.9792 |
| 21 | Prueba de Ljung-Box (h = 12 lags) |  |  | Conclusión: |  |  |  | 18 | 1000 | 83.9792 |
| 22 | Q | 274.426 |  | Q > Chi²: se rechaza H0, los datos están correlacionados (hay estructura/tendencia) |  |  |  | 19 | 997 | 80.9792 |
| 23 | Chi² crítico (95%, 12 g.l.) | 21.0261 |  |  |  |  |  | 20 | 980 | 63.9792 |
| 24 |  |  |  |  |  |  |  | 21 | 971 | 54.9792 |
| 25 |  |  |  |  |  |  |  | 22 | 951 | 34.9792 |
| 26 |  |  |  |  |  |  |  | 23 | 938 | 21.9792 |
| 27 |  |  |  |  |  |  |  | 24 | 935 | 18.9792 |
| 28 |  |  |  |  |  |  |  | 25 | 928 | 11.9792 |
| 29 |  |  |  |  |  |  |  | 26 | 918 | 1.97917 |
| 30 |  |  |  |  |  |  |  | 27 | 911 | -5.02083 |
| 31 |  |  |  |  |  |  |  | 28 | 892 | -24.0208 |
| 32 |  |  |  |  |  |  |  | 29 | 887 | -29.0208 |
| 33 |  |  |  |  |  |  |  | 30 | 871 | -45.0208 |
| 34 |  |  |  |  |  |  |  | 31 | 866 | -50.0208 |
| 35 |  |  |  |  |  |  |  | 32 | 862 | -54.0208 |
| 36 |  |  |  |  |  |  |  | 33 | 847 | -69.0208 |
| 37 |  |  |  |  |  |  |  | 34 | 826 | -90.0208 |
| 38 |  |  |  |  |  |  |  | 35 | 805 | -111.021 |
| 39 |  |  |  |  |  |  |  | 36 | 793 | -123.021 |
| 40 |  |  |  |  |  |  |  | 37 | 778 | -138.021 |
| 41 |  |  |  |  |  |  |  | 38 | 765 | -151.021 |
| 42 |  |  |  |  |  |  |  | 39 | 763 | -153.021 |
| 43 |  |  |  |  |  |  |  | 40 | 753 | -163.021 |
| 44 |  |  |  |  |  |  |  | 41 | 738 | -178.021 |
| 45 |  |  |  |  |  |  |  | 42 | 735 | -181.021 |
| 46 |  |  |  |  |  |  |  | 43 | 716 | -200.021 |
| 47 |  |  |  |  |  |  |  | 44 | 699 | -217.021 |
| 48 |  |  |  |  |  |  |  | 45 | 698 | -218.021 |
| 49 |  |  |  |  |  |  |  | 46 | 684 | -232.021 |
| 50 | Interpretación del correlograma (según la guía de clase): |  |  |  |  |  |  | 47 | 676 | -240.021 |
| 51 | • Patrón de TENDENCIA: r(1) = 0.94 es alto y los coeficientes caen de forma gradual hacia cero |  |  |  |  |  |  | 48 | 671 | -245.021 |
| 52 | (0.94, 0.88, 0.82, 0.76...), exactamente el comportamiento 'Trendline' descrito en la lección. |  |  |  |  |  |  |  |  |  |
| 53 | • Los primeros lags (1 a 4) superan el límite de significancia: la autocorrelación es real, no azar. |  |  |  |  |  |  |  |  |  |
| 54 | • NO hay un pico aislado en el lag 12, que sería la señal de estacionalidad anual → sin estacionalidad. |  |  |  |  |  |  |  |  |  |
| 55 | • Ljung-Box: Q = 274.4 >> Chi² = 21.0 → se rechaza H0: los datos NO son independientes. |  |  |  |  |  |  |  |  |  |
| 56 | • Conclusión: la serie tiene estructura de tendencia aprovechable por el método de Holt. |  |  |  |  |  |  |  |  |  |

**Fórmulas (13 patrones distintos):**

- `B3`: `=AVERAGE(Datos!C2:C49)`
- `B4`: `=COUNT(Datos!C2:C49)`
- `I4`: `=Datos!C2`
- `J4`: `=I4-$B$3`
- `B5`: `=TINV(0.05,B4-1)`
- `B8`: `=SUMPRODUCT($J$4:$J$50,$J$5:$J$51)/SUMSQ($J$4:$J$51)`
- `C8`: `=1/SQRT($B$4)`
- `D8`: `=$B$5*C8`
- `E8`: `=-$B$5*C8`
- `C9`: `=SQRT((1+2*SUMSQ($B$8:B8))/$B$4)`
- `B22`: `=$B$4*($B$4+2)*SUMPRODUCT(B8:B19^2/($B$4-A8:A19))`
- `D22`: `=IF(B22>B23,"Q > Chi²: se rechaza H0, los datos están correlacionados (hay estructura/tendencia)","Q < Chi²: no hay evidencia de correlación (serie aleatoria)")`
- `B23`: `=CHIINV(0.05,12)`

### Hoja `Holt` — 71 filas × 12 columnas · 1 gráfico(s)

**Gráficos en esta hoja:**

- Gráfico de líneas — título «Demanda real vs. pronóstico Holt (incluye meses 49-60)» · ejes: Periodo / Unidades
  - Series: Holt!$C$2: y = `Holt!$C$3:$C$51`, x = `Holt!$B$3:$B$63`; Holt!$F$2: y = `Holt!$F$3:$F$63`, x = `Holt!$B$3:$B$63`

| Fila | A | B | C | D | E | F | G | H | I | J | K | L |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2. Pronóstico por suavización exponencial doble (Holt) |  |  |  |  |  |  |  |  |  |  |  |
| 2 |  | Periodo | Demanda | S(t) | G(t) | F(t) | MAD | RESIDUALES | ERROR RELATIVO |  | Alpha | 0.95 |
| 3 |  | Inicial (0) |  | 1161.45 | -10.0173 |  |  |  |  |  | Beta | 0.05 |
| 4 |  | 1 | 1134 | 1134.87 | -10.8451 | 1151.43 | 17.4277 | 17.4277 | 0.0153684 |  |  |  |
| 5 |  | 2 | 1123 | 1123.05 | -10.8939 | 1124.03 | 1.02625 | 1.02625 | 0.000913851 |  |  |  |
| 6 |  | 3 | 1107 | 1107.26 | -11.1389 | 1112.16 | 5.15743 | 5.15743 | 0.00465893 |  |  |  |
| 7 |  | 4 | 1102 | 1101.71 | -10.8595 | 1096.12 | 5.88098 | -5.88098 | 0.00533665 |  |  |  |
| 8 |  | 5 | 1088 | 1088.14 | -10.9947 | 1090.85 | 2.84644 | 2.84644 | 0.00261621 |  |  |  |
| 9 |  | 6 | 1081 | 1080.81 | -10.8117 | 1077.15 | 3.85239 | -3.85239 | 0.00356373 |  |  |  |
| 10 |  | 7 | 1071 | 1070.95 | -10.764 | 1070 | 1.00435 | -1.00435 | 0.000937765 |  |  |  |
| 11 |  | 8 | 1063 | 1062.86 | -10.6303 | 1060.19 | 2.81424 | -2.81424 | 0.00264745 |  |  |  |
| 12 |  | 9 | 1063 | 1062.46 | -10.1187 | 1052.23 | 10.7711 | -10.7711 | 0.0101327 |  |  |  |
| 13 |  | 10 | 1059 | 1058.67 | -9.8025 | 1052.34 | 6.65727 | -6.65727 | 0.00628638 |  |  |  |
| 14 |  | 11 | 1051 | 1050.89 | -9.70107 | 1048.86 | 2.13536 | -2.13536 | 0.00203174 |  |  |  |
| 15 |  | 12 | 1043 | 1042.91 | -9.6152 | 1041.19 | 1.80784 | -1.80784 | 0.0017333 |  |  |  |
| 16 |  | 13 | 1038 | 1037.76 | -9.39168 | 1033.29 | 4.70559 | -4.70559 | 0.00453332 |  |  |  |
| 17 |  | 14 | 1034 | 1033.72 | -9.1244 | 1028.37 | 5.62696 | -5.62696 | 0.00544193 |  |  |  |
| 18 |  | 15 | 1026 | 1025.93 | -9.05763 | 1024.59 | 1.40575 | -1.40575 | 0.00137013 |  |  |  |
| 19 |  | 16 | 1024 | 1023.64 | -8.71905 | 1016.87 | 7.12791 | -7.12791 | 0.00696085 |  |  |  |
| 20 |  | 17 | 1008 | 1008.35 | -9.04797 | 1014.92 | 6.92455 | 6.92455 | 0.0068696 |  |  |  |
| 21 |  | 18 | 1000 | 999.965 | -9.01464 | 999.298 | 0.70174 | -0.70174 | 0.00070174 |  |  |  |
| 22 |  | 19 | 997 | 996.698 | -8.72727 | 990.95 | 6.04972 | -6.04972 | 0.00606793 |  |  |  |
| 23 |  | 20 | 980 | 980.399 | -9.10586 | 987.97 | 7.97024 | 7.97024 | 0.0081329 |  |  |  |
| 24 |  | 21 | 971 | 971.015 | -9.11976 | 971.293 | 0.292652 | 0.292652 | 0.000301393 |  |  |  |
| 25 |  | 22 | 951 | 951.545 | -9.63727 | 961.895 | 10.8949 | 10.8949 | 0.0114562 |  |  |  |
| 26 |  | 23 | 938 | 938.195 | -9.82287 | 941.907 | 3.90748 | 3.90748 | 0.00416575 |  |  |  |
| 27 |  | 24 | 935 | 934.669 | -9.50807 | 928.373 | 6.6275 | -6.6275 | 0.00708823 |  |  |  |
| 28 |  | 25 | 928 | 927.858 | -9.37319 | 925.161 | 2.83944 | -2.83944 | 0.00305974 |  |  |  |
| 29 |  | 26 | 918 | 918.024 | -9.39622 | 918.485 | 0.484835 | 0.484835 | 0.000528143 |  |  |  |
| 30 |  | 27 | 911 | 910.881 | -9.28355 | 908.628 | 2.37198 | -2.37198 | 0.00260371 |  |  |  |
| 31 |  | 28 | 892 | 892.48 | -9.73945 | 901.598 | 9.59785 | 9.59785 | 0.0107599 |  |  |  |
| 32 |  | 29 | 887 | 886.787 | -9.53712 | 882.74 | 4.25956 | -4.25956 | 0.00480221 |  |  |  |
| 33 |  | 30 | 871 | 871.312 | -9.83399 | 877.25 | 6.2499 | 6.2499 | 0.00717555 |  |  |  |
| 34 |  | 31 | 866 | 865.774 | -9.61922 | 861.479 | 4.5215 | -4.5215 | 0.00522113 |  |  |  |
| 35 |  | 32 | 862 | 861.708 | -9.34157 | 856.155 | 5.8453 | -5.8453 | 0.00678109 |  |  |  |
| 36 |  | 33 | 847 | 847.268 | -9.59646 | 852.366 | 5.36617 | 5.36617 | 0.0063355 |  |  |  |
| 37 |  | 34 | 826 | 826.584 | -10.1509 | 837.672 | 11.6718 | 11.6718 | 0.0141306 |  |  |  |
| 38 |  | 35 | 805 | 805.572 | -10.6939 | 816.433 | 11.4327 | 11.4327 | 0.0142021 |  |  |  |
| 39 |  | 36 | 793 | 793.094 | -10.7831 | 794.878 | 1.87771 | 1.87771 | 0.00236785 |  |  |  |
| 40 |  | 37 | 778 | 778.216 | -10.9879 | 782.311 | 4.31077 | 4.31077 | 0.00554083 |  |  |  |
| 41 |  | 38 | 765 | 765.111 | -11.0937 | 767.228 | 2.22766 | 2.22766 | 0.00291197 |  |  |  |
| 42 |  | 39 | 763 | 762.551 | -10.667 | 754.018 | 8.98231 | -8.98231 | 0.0117724 |  |  |  |
| 43 |  | 40 | 753 | 752.944 | -10.614 | 751.884 | 1.11615 | -1.11615 | 0.00148227 |  |  |  |
| 44 |  | 41 | 738 | 738.217 | -10.8197 | 742.33 | 4.33017 | 4.33017 | 0.00586744 |  |  |  |
| 45 |  | 42 | 735 | 734.62 | -10.4585 | 727.397 | 7.60319 | -7.60319 | 0.0103445 |  |  |  |
| 46 |  | 43 | 716 | 716.408 | -10.8462 | 724.161 | 8.16129 | 8.16129 | 0.0113985 |  |  |  |
| 47 |  | 44 | 699 | 699.328 | -11.1579 | 705.562 | 6.56185 | 6.56185 | 0.00938749 |  |  |  |
| 48 |  | 45 | 698 | 697.509 | -10.691 | 688.17 | 9.82981 | -9.82981 | 0.0140828 |  |  |  |
| 49 |  | 46 | 684 | 684.141 | -10.8248 | 686.818 | 2.81753 | 2.81753 | 0.00411919 |  |  |  |
| 50 |  | 47 | 676 | 675.866 | -10.6973 | 673.316 | 2.68394 | -2.68394 | 0.00397032 |  |  |  |
| 51 |  | 48 | 671 | 670.708 | -10.4203 | 665.168 | 5.83153 | -5.83153 | 0.0086908 |  |  |  |
| 52 |  | 49 |  |  |  | 660.288 |  |  |  |  |  |  |
| 53 |  | 50 |  |  |  | 649.868 |  |  |  |  |  |  |
| 54 |  | 51 |  |  |  | 639.447 |  |  |  |  |  |  |
| 55 |  | 52 |  |  |  | 629.027 |  |  |  |  |  |  |
| 56 |  | 53 |  |  |  | 618.607 |  |  |  |  |  |  |
| 57 |  | 54 |  |  |  | 608.186 |  |  |  |  |  |  |
| 58 |  | 55 |  |  |  | 597.766 |  |  |  |  |  |  |
| 59 |  | 56 |  |  |  | 587.346 |  |  |  |  |  |  |
| 60 |  | 57 |  |  |  | 576.925 |  |  |  |  |  |  |

> **Hoja larga:** arriba se muestran 60 de 69 filas con datos. **Todos los valores de la hoja están en [`parcial-1-calculos-datos/Holt.csv`](./parcial-1-calculos-datos/Holt.csv)** (CSV, UTF-8).

**Fórmulas (14 patrones distintos):**

- `D3`: `=INTERCEPT(C4:C51,B4:B51)`
- `E3`: `=SLOPE(C4:C51,B4:B51)`
- `C4`: `=Datos!C2`
- `D4`: `=$L$2*C4+(1-$L$2)*(D3+E3)`
- `E4`: `=$L$3*(D4-D3)+(1-$L$3)*E3`
- `F4`: `=D3+E3`
- `G4`: `=ABS(F4-C4)`
- `H4`: `=F4-C4`
- `I4`: `=G4/C4`
- `F52`: `=$D$51+1*$E$51`
- `C68`: `=AVERAGE(G4:G51)`
- `C69`: `=AVERAGE(I4:I51)`
- `C70`: `=SUMSQ(H4:H51)`
- `C71`: `=SUMSQ(H4:H51)/COUNT(H4:H51)`

