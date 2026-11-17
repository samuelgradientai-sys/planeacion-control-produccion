# tarea-class-example-2

> **Archivo:** [`tarea-class-example-2.xlsx`](./tarea-class-example-2.xlsx) · **Corte 1** · Libro de Excel con 10 hoja(s): `DATOS`, `DATOS ACF`, `DATOS HISTOGRAMA`, `DATOS BOX PLOT`, `DISPERSION`, `GRAFICO ACF`, `GRAFICO DE SERIES DE TIEMPO `, `GRAFICO HISTOGRAMA`, `GRAFICO BOX PLOT`, `GRAFICO DISPERSION`  
> **Nombre original:** `CORTE 1/TAREAS/PRONOSCITOS DE DEMANDAS/Class example 2.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Segundo libro de la tarea «Pronósticos de demandas» (nombre original `TAREAS/PRONOSCITOS DE DEMANDAS/Class example 2.xlsx`), basado en la [Lección 4 — Plotting your data](./L04-plotting-your-data.md). Tiene las ventas diarias de tres productos y analiza a fondo el **producto 1**: función de autocorrelación hasta el rezago 88 calculada con fórmulas (no con la herramienta de Análisis de datos), límites de significancia, histograma de 40 clases construido a mano, resumen del boxplot y diagrama de dispersión con regresión $X_t$ frente a $X_{t-1}$. A diferencia de los ejemplos 1, 3 y 4, todo está calculado con fórmulas vivas. Se aprende a reconocer en el correlograma la firma de una **tendencia**: coeficientes muy altos que bajan despacio.

### Hoja `DATOS`

**Datos de entrada:** 1.923 días consecutivos en orden descendente, del 2019-08-30 (fila 2) al 2014-05-26 (fila 1924). CSV completo: [`DATOS.csv`](./tarea-class-example-2-datos/DATOS.csv).

| Columna | n | Mínimo | Máximo | Media | Mediana | Desv. estándar | Comportamiento (calculado) |
|---|---|---|---|---|---|---|---|
| B `Ventas prod 1` | 1.923 | 934 | 2.052 | 1.497,55 | 1.498 | 281,69 | Tendencia decreciente casi lineal: media anual 1.925,8 (2014), 1.775,0 (2015), 1.592,7 (2016), 1.413,2 (2017), 1.230,4 (2018), 1.076,0 (2019); pendiente ≈ −0,50 unidades/día. |
| C `Ventas Prod 2` | 1.923 | −30 | 1.086 | 531,97 | 532 | 282,89 | Tendencia creciente: 103,0 (2014) → 953,0 (2019); pendiente ≈ +0,50 unidades/día. Tiene 4 valores negativos (−22, −7, −4 y −30 entre el 2014-05-27 y el 2014-06-02). |
| D `Ventas Prod 3` | 1.923 | 800 | 2.952 | 1.244,86 | 1.064 | 496,32 | Plana en ≈ 1.000 de 2014 a marzo de 2018; desde el segundo trimestre de 2018 crece con fuerza (media trimestral 1.185 → 1.514 → 1.811 → 2.114 → 2.418 → 2.700 en el tercer trimestre de 2019). |

Hallazgo propio: los productos 1 y 2 son casi espejo (correlación −0,97); su suma se mantiene alrededor de 2.030 (desviación 69).

**Gráfico:** líneas con las tres series (`B2:D1924`), en el orden de la hoja (del día más reciente al más antiguo, así que visualmente las tendencias aparecen invertidas).

### Hoja `DATOS ACF` — función de autocorrelación del producto 1

**Parámetros**

| Celda | Concepto | Fórmula | Valor |
|---|---|---|---|
| B26 | Observaciones $n$ | `=COUNT(DATOS!B2:B1924)` | 1.923 |
| B27 | Media $\bar x$ | `=AVERAGE(DATOS!B2:B1924)` | 1.497,55 |
| B28 | Suma de cuadrados $\sum(x_t-\bar x)^2$ | `=DEVSQ(DATOS!B2:B1924)` | 1,52512 × 10⁸ |
| B29 | Nivel de significancia ($z$, 5 %) | valor fijo | 1,96 |

**Método paso a paso**

1. **Autocorrelación** (columna B, filas 32–119, rezagos $k=1$ a 88), fórmula matricial
   `=SUMPRODUCT((OFFSET(DATOS!$B$2,0,0,$B$26-$A32,1)-$B$27)*(OFFSET(DATOS!$B$2,$A32,0,$B$26-$A32,1)-$B$27))/$B$28`, que es exactamente la fórmula de la L04:
   $$r_k=\frac{\sum_{t=1}^{n-k}(x_t-\bar x)(x_{t+k}-\bar x)}{\sum_{t=1}^{n}(x_t-\bar x)^2}.$$
2. **Límite superior** (columna C): `=$B$29*SQRT((1+2*(SUMSQ($B$32:$B32)-$B32^2))/$B$26)`, es decir
   $$L_k=1{,}96\sqrt{\frac{1+2\sum_{i=1}^{k-1}r_i^2}{n}}$$
   (la suma de cuadrados hasta $k$ menos $r_k^2$ deja solo los rezagos anteriores). **Límite inferior** (columna D): $-L_k$. Usa $z=1{,}96$ en vez del $t$ de Student de la L04; con $n=1.923$ son prácticamente iguales (1,9612).
3. **Matriz de correlaciones** (filas 1–22, rezagos 0 a 20): fórmulas matriciales `=IF($A2-(COLUMNS($B2:B2)-1)<0,"",IF(...=0,1,INDEX($B$32:$B$119,...)))` que reconstruyen, a partir de la columna B de abajo, una matriz triangular con el mismo formato que la salida de *Análisis de datos → Correlación* (1 en la diagonal y $r_{|i-j|}$ fuera de ella). Es solo presentación.

**Resultados (selección; los 88 valores están en el anexo y en [`DATOS_ACF.csv`](./tarea-class-example-2-datos/DATOS_ACF.csv))**

| Rezago | $r_k$ | Límite ± | Rezago | $r_k$ | Límite ± |
|---|---|---|---|---|---|
| 1 | 0,9661 | 0,0447 | 20 | 0,9377 | 0,2664 |
| 2 | 0,9654 | 0,0757 | 30 | 0,9214 | 0,3249 |
| 3 | 0,9633 | 0,0972 | 40 | 0,9070 | 0,3729 |
| 4 | 0,9623 | 0,1147 | 50 | 0,8921 | 0,4141 |
| 5 | 0,9599 | 0,1298 | 60 | 0,8775 | 0,4503 |
| 7 | 0,9592 | 0,1556 | 70 | 0,8631 | 0,4827 |
| 10 | 0,9545 | 0,1876 | 80 | 0,8477 | 0,5121 |
| 15 | 0,9459 | 0,2307 | 88 | 0,8339 | 0,5338 |

**Gráfico `GRAFICO ACF`:** «Función de autocorrelación para Ventas prod 1» (estilo Minitab; ejes «Desfase» y «Autocorrelación»): barras de $r_k$ para los rezagos 1–88 con las líneas de límite superior e inferior que se abren poco a poco. Todas las barras quedan muy por encima del límite y descienden lentamente de 0,97 a 0,83.

### Hoja `DATOS HISTOGRAMA`

**Parámetros:** $n=1.923$ (`B3`), mínimo 934 (`B4`), máximo 2.052 (`B5`), número de clases $k=40$ (`B6`, valor fijo) y ancho de clase $w=(\max-\min)/k=27{,}95$ (`B7`).

**Método:** clase $i$ con límite inferior $L_i=\min+(i-1)w$ (`B10`), superior $U_i=\min+i\,w$ (`C10`) y marca de clase $(L_i+U_i)/2$ (`D10`). Frecuencia con `COUNTIFS`: la clase 1 cuenta $L_1\le x\le U_1$ y las demás $L_i<x\le U_i$. Control: `B52 = SUM(E10:E49)` = 1.923.

**Resultados**

| Clase | Límites | Frec. | Clase | Límites | Frec. |
|---|---|---|---|---|---|
| 1 | 934 – 961,95 | 7 | 21 | 1.493 – 1.520,95 | 56 |
| 2 | 961,95 – 989,9 | 13 | 22 | 1.520,95 – 1.548,9 | 53 |
| 3 | 989,9 – 1.017,85 | 28 | 23 | 1.548,9 – 1.576,85 | 57 |
| 4 | 1.017,85 – 1.045,8 | 24 | 24 | 1.576,85 – 1.604,8 | 57 |
| 5 | 1.045,8 – 1.073,75 | 44 | 25 | 1.604,8 – 1.632,75 | 60 |
| 6 | 1.073,75 – 1.101,7 | 53 | 26 | 1.632,75 – 1.660,7 | 58 |
| 7 | 1.101,7 – 1.129,65 | 59 | 27 | 1.660,7 – 1.688,65 | 62 |
| 8 | 1.129,65 – 1.157,6 | 55 | 28 | 1.688,65 – 1.716,6 | 56 |
| 9 | 1.157,6 – 1.185,55 | 48 | 29 | 1.716,6 – 1.744,55 | 49 |
| 10 | 1.185,55 – 1.213,5 | 63 | 30 | 1.744,55 – 1.772,5 | 48 |
| 11 | 1.213,5 – 1.241,45 | 59 | 31 | 1.772,5 – 1.800,45 | 68 |
| 12 | 1.241,45 – 1.269,4 | 51 | 32 | 1.800,45 – 1.828,4 | 54 |
| 13 | 1.269,4 – 1.297,35 | 53 | 33 | 1.828,4 – 1.856,35 | 51 |
| 14 | 1.297,35 – 1.325,3 | 53 | 34 | 1.856,35 – 1.884,3 | 51 |
| 15 | 1.325,3 – 1.353,25 | 58 | 35 | 1.884,3 – 1.912,25 | 59 |
| 16 | 1.353,25 – 1.381,2 | 61 | 36 | 1.912,25 – 1.940,2 | 51 |
| 17 | 1.381,2 – 1.409,15 | 56 | 37 | 1.940,2 – 1.968,15 | 32 |
| 18 | 1.409,15 – 1.437,1 | 62 | 38 | 1.968,15 – 1.996,1 | 22 |
| 19 | 1.437,1 – 1.465,05 | 47 | 39 | 1.996,1 – 2.024,05 | 19 |
| 20 | 1.465,05 – 1.493 | 56 | 40 | 2.024,05 – 2.052 | 10 |

**Gráfico `GRAFICO HISTOGRAMA`:** columnas de frecuencia (`E10:E49`) sobre las marcas de clase (`D10:D49`), ejes «Ventas prod 1» y «Frecuencia». Forma casi plana entre ≈ 1.050 y ≈ 1.940 con colas cortas a ambos lados: es lo que produce una rampa lineal con ruido, no una campana.

### Hoja `DATOS BOX PLOT`

| Concepto | Fórmula | Valor |
|---|---|---|
| Observaciones | `COUNT` | 1.923 |
| Mínimo | `MIN` | 934 |
| Primer cuartil $Q_1$ | `QUARTILE.INC(…,1)` | 1.258,5 |
| Mediana $Q_2$ | `MEDIAN` | 1.498 |
| Tercer cuartil $Q_3$ | `QUARTILE.INC(…,3)` | 1.736,5 |
| Máximo | `MAX` | 2.052 |
| Rango intercuartílico $RIQ=Q_3-Q_1$ | `=B7-B5` | 478 |
| «Bigote inferior» $Q_1-1{,}5\,RIQ$ | `=B5-1.5*B9` | 541,5 |
| «Bigote superior» $Q_3+1{,}5\,RIQ$ | `=B7+1.5*B9` | 2.453,5 |

Como el mínimo (934) y el máximo (2.052) caen dentro de [541,5; 2.453,5], **no hay datos atípicos**. Gráfico `GRAFICO BOX PLOT`: caja y bigotes nativo de Excel sobre `DATOS!B2:B1924` (cuartiles exclusivos, marca de la media).

### Hoja `DISPERSION`

**Método:** columna A = venta del día anterior (`=DATOS!B3`, … ; como las fechas van en orden descendente, la fila siguiente es el día anterior) y columna B = venta del día (`=DATOS!B2`, …), 1.922 pares. Estadísticos de la regresión $X_t=a+b\,X_{t-1}$:

| Celda | Concepto | Fórmula | Valor |
|---|---|---|---|
| E2 | Correlación $r$ | `=CORREL(A2:A1923,B2:B1923)` | 0,96777 |
| E3 | $r^2$ | `=RSQ(B2:B1923,A2:A1923)` | 0,936579 |
| E4 | Pendiente $b$ | `=SLOPE(B2:B1923,A2:A1923)` | 0,967734 |
| E5 | Intercepto $a$ | `=INTERCEPT(B2:B1923,A2:A1923)` | 47,7904 |
| E6 | Pares de datos | `=COUNT(A2:A1923)` | 1.922 |

$$\hat X_t=47{,}79+0{,}9677\,X_{t-1},\qquad R^2=0{,}9366$$

**Gráfico `GRAFICO DISPERSION`:** «Gráfica de dispersión de Ventas prod 1 vs. periodo anterior», X = periodo anterior, Y = periodo actual: nube estrecha a lo largo de la diagonal. En el título del eje X el estudiante escribió: «LINEA TENDENCIA AZUL ESTA SE BASA EN SI LAS VENTAS DE HOY SE PUEDEN REDECIR MAÑANA SI SE ACERA A LA LINE».

### Hoja `GRAFICO DE SERIES DE TIEMPO `

«Gráfica de series de tiempo de Ventas prod 1», ejes «Índice» y «Ventas prod 1». Solo grafica `DATOS!B2:B251`: los 250 días más recientes (del 2019-08-30 hacia atrás hasta el 2018-12-24), no la serie completa.

### Conclusión

- El producto 1 tiene una **tendencia** clara (decreciente en el tiempo): $r_1=0{,}966$ y los coeficientes bajan muy despacio (0,834 en el rezago 88), siempre muy por encima de los límites. Es el patrón «Trendline» de la p. 16 de la L04.
- El diagrama de dispersión lo confirma: la venta de ayer explica el 93,7 % de la variación de la de hoy.
- El histograma plano y el boxplot sin atípicos describen una rampa, no un ruido alrededor de una media: **no** sirven los métodos para datos estacionarios; hay que usar un método con tendencia, como la [suavización doble de Holt](../05-tendencia-suavizacion-doble-holt/).
- Los productos 2 (tendencia creciente) y 3 (cambio de nivel en 2018) solo se grafican; no se analizan.

### Observaciones

- Las hojas de cálculo están completas y con fórmulas vivas; las hojas de gráfico dependen de ellas.
- El resumen del boxplot usa `QUARTILE.INC`, pero el gráfico nativo usa el método exclusivo; los cuartiles pueden diferir un poco.
- Las celdas `B10`/`B11` del boxplot se llaman «Bigote», pero son las vallas de Tukey ($Q_1-1{,}5\,RIQ$ y $Q_3+1{,}5\,RIQ$), no el extremo del bigote.
- El producto 2 tiene ventas negativas (mínimo −30), probablemente devoluciones o errores de registro.
- La serie de tiempo del producto 1 solo muestra 250 días, lo que oculta la tendencia de largo plazo.

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `DATOS` — 1924 filas × 7 columnas · 1 gráfico(s)

**Gráficos en esta hoja:**

- Gráfico de líneas — título «(sin título)»
  - Series: DATOS!$B$1: y = `DATOS!$B$2:$B$1924`; DATOS!$C$1: y = `DATOS!$C$2:$C$1924`; DATOS!$D$1: y = `DATOS!$D$2:$D$1924`

| Fila | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| 1 | Fecha | Ventas prod 1 | Ventas Prod 2 | Ventas Prod 3 |  |  |  |
| 2 | 2019-08-30 | 986 | 947 | 2705 |  |  |  |
| 3 | 2019-08-29 | 1005 | 995 | 2616 |  |  |  |
| 4 | 2019-08-28 | 1065 | 1008 | 2832 |  |  |  |
| 5 | 2019-08-27 | 952 | 1072 | 2671 |  |  |  |
| 6 | 2019-08-26 | 990 | 1030 | 2898 |  |  |  |
| 7 | 2019-08-25 | 993 | 1059 | 2950 |  |  |  |
| 8 | 2019-08-24 | 1053 | 1050 | 2605 |  |  |  |
| 9 | 2019-08-23 | 934 | 1063 | 2688 |  |  |  |
| 10 | 2019-08-22 | 1007 | 976 | 2923 |  |  |  |
| 11 | 2019-08-21 | 942 | 927 | 2889 |  |  |  |
| 12 | 2019-08-20 | 1029 | 1086 | 2585 |  |  |  |
| 13 | 2019-08-19 | 949 | 1085 | 2618 |  |  |  |
| 14 | 2019-08-18 | 995 | 937 | 2952 |  |  |  |
| 15 | 2019-08-17 | 978 | 1047 | 2896 |  |  |  |
| 16 | 2019-08-16 | 1086 | 991 | 2744 |  |  |  |
| 17 | 2019-08-15 | 1077 | 973 | 2602 |  |  |  |
| 18 | 2019-08-14 | 1005 | 1021 | 2552 |  |  |  |
| 19 | 2019-08-13 | 1097 | 1059 | 2837 |  |  |  |
| 20 | 2019-08-12 | 941 | 943 | 2736 |  |  |  |
| 21 | 2019-08-11 | 1049 | 1075 | 2635 |  |  | Las ventas negativas quieren decir que hubo devoluciones de productos vendidos en periodos pasados. Puede asumir cero ventas |
| 22 | 2019-08-10 | 1047 | 1011 | 2848 |  |  |  |
| 23 | 2019-08-09 | 946 | 959 | 2651 |  |  |  |
| 24 | 2019-08-08 | 984 | 984 | 2636 |  |  |  |
| 25 | 2019-08-07 | 1060 | 1031 | 2710 |  |  |  |
| 26 | 2019-08-06 | 1040 | 937 | 2856 |  |  |  |
| 27 | 2019-08-05 | 957 | 994 | 2799 |  |  |  |
| 28 | 2019-08-04 | 1037 | 1054 | 2827 |  |  |  |
| 29 | 2019-08-03 | 1059 | 1039 | 2814 |  |  |  |
| 30 | 2019-08-02 | 1059 | 1038 | 2592 |  |  |  |
| 31 | 2019-08-01 | 1100 | 1067 | 2691 |  |  |  |
| 32 | 2019-07-31 | 1049 | 982 | 2625 |  |  |  |
| 33 | 2019-07-30 | 1057 | 1050 | 2852 |  |  |  |
| 34 | 2019-07-29 | 978 | 1054 | 2575 |  |  |  |
| 35 | 2019-07-28 | 978 | 950 | 2595 |  |  |  |
| 36 | 2019-07-27 | 1078 | 1068 | 2704 |  |  |  |
| 37 | 2019-07-26 | 1077 | 957 | 2850 |  |  |  |
| 38 | 2019-07-25 | 1024 | 921 | 2684 |  |  |  |
| 39 | 2019-07-24 | 1005 | 977 | 2601 |  |  |  |
| 40 | 2019-07-23 | 1083 | 1048 | 2638 |  |  |  |
| 41 | 2019-07-22 | 1057 | 1051 | 2524 |  |  |  |
| 42 | 2019-07-21 | 994 | 1046 | 2483 |  |  |  |
| 43 | 2019-07-20 | 1022 | 1003 | 2816 |  |  |  |
| 44 | 2019-07-19 | 1038 | 995 | 2781 |  |  |  |
| 45 | 2019-07-18 | 964 | 939 | 2582 |  |  |  |
| 46 | 2019-07-17 | 1117 | 998 | 2650 |  |  |  |
| 47 | 2019-07-16 | 969 | 945 | 2577 |  |  |  |
| 48 | 2019-07-15 | 1102 | 1005 | 2762 |  |  |  |
| 49 | 2019-07-14 | 1089 | 935 | 2703 |  |  |  |
| 50 | 2019-07-13 | 1120 | 1024 | 2749 |  |  |  |
| 51 | 2019-07-12 | 1017 | 989 | 2806 |  |  |  |
| 52 | 2019-07-11 | 978 | 942 | 2649 |  |  |  |
| 53 | 2019-07-10 | 1081 | 1068 | 2708 |  |  |  |
| 54 | 2019-07-09 | 1059 | 922 | 2669 |  |  |  |
| 55 | 2019-07-08 | 1034 | 948 | 2439 |  |  |  |
| 56 | 2019-07-07 | 1119 | 1007 | 2464 |  |  |  |
| 57 | 2019-07-06 | 1051 | 1006 | 2700 |  |  |  |
| 58 | 2019-07-05 | 1014 | 1059 | 2685 |  |  |  |
| 59 | 2019-07-04 | 1128 | 905 | 2771 |  |  |  |
| 60 | 2019-07-03 | 1101 | 953 | 2414 |  |  |  |

> **Hoja larga:** arriba se muestran 60 de 1924 filas con datos. **Todos los valores de la hoja están en [`tarea-class-example-2-datos/DATOS.csv`](./tarea-class-example-2-datos/DATOS.csv)** (CSV, UTF-8).

### Hoja `DATOS ACF` — 119 filas × 22 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | REZAGO | COEFICIENTE DE AUTOCORRELACIÓN 1 | Columna 2 | Columna 3 | Columna 4 | Columna 5 | Columna 6 | Columna 7 | Columna 8 | Columna 9 | Columna 10 | Columna 11 | Columna 12 | Columna 13 | Columna 14 | Columna 15 | Columna 16 | Columna 17 | Columna 18 | Columna 19 | Columna 20 | Columna 21 |
| 2 | 0 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 | 1 | 0.966072 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 | 2 | 0.965379 | 0.966072 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 | 3 | 0.963278 | 0.965379 | 0.966072 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 | 4 | 0.962341 | 0.963278 | 0.965379 | 0.966072 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7 | 5 | 0.959916 | 0.962341 | 0.963278 | 0.965379 | 0.966072 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 | 6 | 0.960116 | 0.959916 | 0.962341 | 0.963278 | 0.965379 | 0.966072 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9 | 7 | 0.959178 | 0.960116 | 0.959916 | 0.962341 | 0.963278 | 0.965379 | 0.966072 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10 | 8 | 0.956141 | 0.959178 | 0.960116 | 0.959916 | 0.962341 | 0.963278 | 0.965379 | 0.966072 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |
| 11 | 9 | 0.955284 | 0.956141 | 0.959178 | 0.960116 | 0.959916 | 0.962341 | 0.963278 | 0.965379 | 0.966072 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| 12 | 10 | 0.954483 | 0.955284 | 0.956141 | 0.959178 | 0.960116 | 0.959916 | 0.962341 | 0.963278 | 0.965379 | 0.966072 | 1 |  |  |  |  |  |  |  |  |  |  |
| 13 | 11 | 0.951077 | 0.954483 | 0.955284 | 0.956141 | 0.959178 | 0.960116 | 0.959916 | 0.962341 | 0.963278 | 0.965379 | 0.966072 | 1 |  |  |  |  |  |  |  |  |  |
| 14 | 12 | 0.950387 | 0.951077 | 0.954483 | 0.955284 | 0.956141 | 0.959178 | 0.960116 | 0.959916 | 0.962341 | 0.963278 | 0.965379 | 0.966072 | 1 |  |  |  |  |  |  |  |  |
| 15 | 13 | 0.949003 | 0.950387 | 0.951077 | 0.954483 | 0.955284 | 0.956141 | 0.959178 | 0.960116 | 0.959916 | 0.962341 | 0.963278 | 0.965379 | 0.966072 | 1 |  |  |  |  |  |  |  |
| 16 | 14 | 0.947091 | 0.949003 | 0.950387 | 0.951077 | 0.954483 | 0.955284 | 0.956141 | 0.959178 | 0.960116 | 0.959916 | 0.962341 | 0.963278 | 0.965379 | 0.966072 | 1 |  |  |  |  |  |  |
| 17 | 15 | 0.945946 | 0.947091 | 0.949003 | 0.950387 | 0.951077 | 0.954483 | 0.955284 | 0.956141 | 0.959178 | 0.960116 | 0.959916 | 0.962341 | 0.963278 | 0.965379 | 0.966072 | 1 |  |  |  |  |  |
| 18 | 16 | 0.94371 | 0.945946 | 0.947091 | 0.949003 | 0.950387 | 0.951077 | 0.954483 | 0.955284 | 0.956141 | 0.959178 | 0.960116 | 0.959916 | 0.962341 | 0.963278 | 0.965379 | 0.966072 | 1 |  |  |  |  |
| 19 | 17 | 0.942721 | 0.94371 | 0.945946 | 0.947091 | 0.949003 | 0.950387 | 0.951077 | 0.954483 | 0.955284 | 0.956141 | 0.959178 | 0.960116 | 0.959916 | 0.962341 | 0.963278 | 0.965379 | 0.966072 | 1 |  |  |  |
| 20 | 18 | 0.940758 | 0.942721 | 0.94371 | 0.945946 | 0.947091 | 0.949003 | 0.950387 | 0.951077 | 0.954483 | 0.955284 | 0.956141 | 0.959178 | 0.960116 | 0.959916 | 0.962341 | 0.963278 | 0.965379 | 0.966072 | 1 |  |  |
| 21 | 19 | 0.939089 | 0.940758 | 0.942721 | 0.94371 | 0.945946 | 0.947091 | 0.949003 | 0.950387 | 0.951077 | 0.954483 | 0.955284 | 0.956141 | 0.959178 | 0.960116 | 0.959916 | 0.962341 | 0.963278 | 0.965379 | 0.966072 | 1 |  |
| 22 | 20 | 0.937685 | 0.939089 | 0.940758 | 0.942721 | 0.94371 | 0.945946 | 0.947091 | 0.949003 | 0.950387 | 0.951077 | 0.954483 | 0.955284 | 0.956141 | 0.959178 | 0.960116 | 0.959916 | 0.962341 | 0.963278 | 0.965379 | 0.966072 | 1 |
| 25 | Cálculo de la función de autocorrelación — Ventas prod 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 26 | Observaciones (n) | 1923 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 27 | Media | 1497.55 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 28 | Suma de cuadrados (DEVSQ) | 1.52512e+08 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 29 | Nivel de significancia (z, 5%) | 1.96 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 31 | Desfase | Autocorrelación | Límite superior 5% | Límite inferior 5% |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 32 | 1 | 0.966072 | 0.0446958 | -0.0446958 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 33 | 2 | 0.965379 | 0.0756744 | -0.0756744 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 34 | 3 | 0.963278 | 0.0972121 | -0.0972121 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 35 | 4 | 0.962341 | 0.114706 | -0.114706 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 36 | 5 | 0.959916 | 0.129837 | -0.129837 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 37 | 6 | 0.960116 | 0.143315 | -0.143315 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 38 | 7 | 0.959178 | 0.155635 | -0.155635 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 39 | 8 | 0.956141 | 0.167028 | -0.167028 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 40 | 9 | 0.955284 | 0.177626 | -0.177626 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 41 | 10 | 0.954483 | 0.187608 | -0.187608 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 42 | 11 | 0.951077 | 0.197071 | -0.197071 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 43 | 12 | 0.950387 | 0.206036 | -0.206036 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 44 | 13 | 0.949003 | 0.214615 | -0.214615 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 45 | 14 | 0.947091 | 0.222841 | -0.222841 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 46 | 15 | 0.945946 | 0.230742 | -0.230742 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 47 | 16 | 0.94371 | 0.238363 | -0.238363 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 48 | 17 | 0.942721 | 0.245714 | -0.245714 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 49 | 18 | 0.940758 | 0.252836 | -0.252836 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 50 | 19 | 0.939089 | 0.259735 | -0.259735 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 51 | 20 | 0.937685 | 0.266431 | -0.266431 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 52 | 21 | 0.93679 | 0.272945 | -0.272945 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 53 | 22 | 0.93518 | 0.279294 | -0.279294 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 54 | 23 | 0.932441 | 0.285481 | -0.285481 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 55 | 24 | 0.931751 | 0.291501 | -0.291501 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 56 | 25 | 0.929663 | 0.297392 | -0.297392 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 57 | 26 | 0.92657 | 0.303142 | -0.303142 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 58 | 27 | 0.926595 | 0.308748 | -0.308748 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 59 | 28 | 0.923916 | 0.314254 | -0.314254 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 60 | 29 | 0.926011 | 0.319634 | -0.319634 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 61 | 30 | 0.921425 | 0.324949 | -0.324949 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 62 | 31 | 0.921368 | 0.330128 | -0.330128 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 63 | 32 | 0.919567 | 0.335225 | -0.335225 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

> **Hoja larga:** arriba se muestran 60 de 116 filas con datos. **Todos los valores de la hoja están en [`tarea-class-example-2-datos/DATOS_ACF.csv`](./tarea-class-example-2-datos/DATOS_ACF.csv)** (CSV, UTF-8).

**Fórmulas (5 patrones distintos):**

- `B26`: `=COUNT(DATOS!B2:B1924)`
- `B27`: `=AVERAGE(DATOS!B2:B1924)`
- `B28`: `=DEVSQ(DATOS!B2:B1924)`
- `C32`: `=$B$29*SQRT((1+2*(SUMSQ($B$32:$B32)-$B32^2))/$B$26)`
- `D32`: `=-C32`

### Hoja `DATOS HISTOGRAMA` — 52 filas × 5 columnas

| Fila | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | Histograma de Ventas prod 1 |  |  |  |  |
| 3 | Observaciones (n) | 1923 |  |  |  |
| 4 | Mínimo | 934 |  |  |  |
| 5 | Máximo | 2052 |  |  |  |
| 6 | Número de clases | 40 |  |  |  |
| 7 | Ancho de clase | 27.95 |  |  |  |
| 9 | Clase | Límite inferior | Límite superior | Marca de clase | Frecuencia |
| 10 | 1 | 934 | 961.95 | 947.975 | 7 |
| 11 | 2 | 961.95 | 989.9 | 975.925 | 13 |
| 12 | 3 | 989.9 | 1017.85 | 1003.88 | 28 |
| 13 | 4 | 1017.85 | 1045.8 | 1031.83 | 24 |
| 14 | 5 | 1045.8 | 1073.75 | 1059.78 | 44 |
| 15 | 6 | 1073.75 | 1101.7 | 1087.72 | 53 |
| 16 | 7 | 1101.7 | 1129.65 | 1115.68 | 59 |
| 17 | 8 | 1129.65 | 1157.6 | 1143.62 | 55 |
| 18 | 9 | 1157.6 | 1185.55 | 1171.57 | 48 |
| 19 | 10 | 1185.55 | 1213.5 | 1199.53 | 63 |
| 20 | 11 | 1213.5 | 1241.45 | 1227.47 | 59 |
| 21 | 12 | 1241.45 | 1269.4 | 1255.43 | 51 |
| 22 | 13 | 1269.4 | 1297.35 | 1283.38 | 53 |
| 23 | 14 | 1297.35 | 1325.3 | 1311.32 | 53 |
| 24 | 15 | 1325.3 | 1353.25 | 1339.28 | 58 |
| 25 | 16 | 1353.25 | 1381.2 | 1367.22 | 61 |
| 26 | 17 | 1381.2 | 1409.15 | 1395.18 | 56 |
| 27 | 18 | 1409.15 | 1437.1 | 1423.12 | 62 |
| 28 | 19 | 1437.1 | 1465.05 | 1451.07 | 47 |
| 29 | 20 | 1465.05 | 1493 | 1479.03 | 56 |
| 30 | 21 | 1493 | 1520.95 | 1506.97 | 56 |
| 31 | 22 | 1520.95 | 1548.9 | 1534.92 | 53 |
| 32 | 23 | 1548.9 | 1576.85 | 1562.88 | 57 |
| 33 | 24 | 1576.85 | 1604.8 | 1590.82 | 57 |
| 34 | 25 | 1604.8 | 1632.75 | 1618.78 | 60 |
| 35 | 26 | 1632.75 | 1660.7 | 1646.72 | 58 |
| 36 | 27 | 1660.7 | 1688.65 | 1674.67 | 62 |
| 37 | 28 | 1688.65 | 1716.6 | 1702.62 | 56 |
| 38 | 29 | 1716.6 | 1744.55 | 1730.57 | 49 |
| 39 | 30 | 1744.55 | 1772.5 | 1758.53 | 48 |
| 40 | 31 | 1772.5 | 1800.45 | 1786.47 | 68 |
| 41 | 32 | 1800.45 | 1828.4 | 1814.42 | 54 |
| 42 | 33 | 1828.4 | 1856.35 | 1842.38 | 51 |
| 43 | 34 | 1856.35 | 1884.3 | 1870.32 | 51 |
| 44 | 35 | 1884.3 | 1912.25 | 1898.28 | 59 |
| 45 | 36 | 1912.25 | 1940.2 | 1926.22 | 51 |
| 46 | 37 | 1940.2 | 1968.15 | 1954.17 | 32 |
| 47 | 38 | 1968.15 | 1996.1 | 1982.12 | 22 |
| 48 | 39 | 1996.1 | 2024.05 | 2010.07 | 19 |
| 49 | 40 | 2024.05 | 2052 | 2038.03 | 10 |
| 52 | Total (control) | 1923 |  |  |  |

**Fórmulas (10 patrones distintos):**

- `B3`: `=COUNT(DATOS!B2:B1924)`
- `B4`: `=MIN(DATOS!B2:B1924)`
- `B5`: `=MAX(DATOS!B2:B1924)`
- `B7`: `=(B5-B4)/B6`
- `B10`: `=$B$4+(A10-1)*$B$7`
- `C10`: `=$B$4+A10*$B$7`
- `D10`: `=(B10+C10)/2`
- `E10`: `=COUNTIFS(DATOS!$B$2:$B$1924,">="&B10,DATOS!$B$2:$B$1924,"<="&C10)`
- `E11`: `=COUNTIFS(DATOS!$B$2:$B$1924,">"&B11,DATOS!$B$2:$B$1924,"<="&C11)`
- `B52`: `=SUM(E10:E49)`

### Hoja `DATOS BOX PLOT` — 11 filas × 2 columnas

| Fila | A | B |
|---|---|---|
| 1 | Gráfica de caja de Ventas prod 1 |  |
| 3 | Observaciones (n) | 1923 |
| 4 | Mínimo | 934 |
| 5 | Primer cuartil (Q1) | 1258.5 |
| 6 | Mediana (Q2) | 1498 |
| 7 | Tercer cuartil (Q3) | 1736.5 |
| 8 | Máximo | 2052 |
| 9 | Rango intercuartílico (RIQ) | 478 |
| 10 | Bigote inferior (Q1 − 1,5·RIQ) | 541.5 |
| 11 | Bigote superior (Q3 + 1,5·RIQ) | 2453.5 |

**Fórmulas (8 patrones distintos):**

- `B3`: `=COUNT(DATOS!B2:B1924)`
- `B4`: `=MIN(DATOS!B2:B1924)`
- `B5`: `=_xlfn.QUARTILE.INC(DATOS!B2:B1924,1)`
- `B6`: `=MEDIAN(DATOS!B2:B1924)`
- `B8`: `=MAX(DATOS!B2:B1924)`
- `B9`: `=B7-B5`
- `B10`: `=B5-1.5*B9`
- `B11`: `=B7+1.5*B9`

### Hoja `DISPERSION` — 1923 filas × 5 columnas

| Fila | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | Ventas prod 1 (periodo anterior) | Ventas prod 1 (periodo actual) |  |  |  |
| 2 | 1005 | 986 |  | Correlación (r) | 0.96777 |
| 3 | 1065 | 1005 |  | r² | 0.936579 |
| 4 | 952 | 1065 |  | Pendiente | 0.967734 |
| 5 | 990 | 952 |  | Intercepto | 47.7904 |
| 6 | 993 | 990 |  | Pares de datos | 1922 |
| 7 | 1053 | 993 |  |  |  |
| 8 | 934 | 1053 |  |  |  |
| 9 | 1007 | 934 |  |  |  |
| 10 | 942 | 1007 |  |  |  |
| 11 | 1029 | 942 |  |  |  |
| 12 | 949 | 1029 |  |  |  |
| 13 | 995 | 949 |  |  |  |
| 14 | 978 | 995 |  |  |  |
| 15 | 1086 | 978 |  |  |  |
| 16 | 1077 | 1086 |  |  |  |
| 17 | 1005 | 1077 |  |  |  |
| 18 | 1097 | 1005 |  |  |  |
| 19 | 941 | 1097 |  |  |  |
| 20 | 1049 | 941 |  |  |  |
| 21 | 1047 | 1049 |  |  |  |
| 22 | 946 | 1047 |  |  |  |
| 23 | 984 | 946 |  |  |  |
| 24 | 1060 | 984 |  |  |  |
| 25 | 1040 | 1060 |  |  |  |
| 26 | 957 | 1040 |  |  |  |
| 27 | 1037 | 957 |  |  |  |
| 28 | 1059 | 1037 |  |  |  |
| 29 | 1059 | 1059 |  |  |  |
| 30 | 1100 | 1059 |  |  |  |
| 31 | 1049 | 1100 |  |  |  |
| 32 | 1057 | 1049 |  |  |  |
| 33 | 978 | 1057 |  |  |  |
| 34 | 978 | 978 |  |  |  |
| 35 | 1078 | 978 |  |  |  |
| 36 | 1077 | 1078 |  |  |  |
| 37 | 1024 | 1077 |  |  |  |
| 38 | 1005 | 1024 |  |  |  |
| 39 | 1083 | 1005 |  |  |  |
| 40 | 1057 | 1083 |  |  |  |
| 41 | 994 | 1057 |  |  |  |
| 42 | 1022 | 994 |  |  |  |
| 43 | 1038 | 1022 |  |  |  |
| 44 | 964 | 1038 |  |  |  |
| 45 | 1117 | 964 |  |  |  |
| 46 | 969 | 1117 |  |  |  |
| 47 | 1102 | 969 |  |  |  |
| 48 | 1089 | 1102 |  |  |  |
| 49 | 1120 | 1089 |  |  |  |
| 50 | 1017 | 1120 |  |  |  |
| 51 | 978 | 1017 |  |  |  |
| 52 | 1081 | 978 |  |  |  |
| 53 | 1059 | 1081 |  |  |  |
| 54 | 1034 | 1059 |  |  |  |
| 55 | 1119 | 1034 |  |  |  |
| 56 | 1051 | 1119 |  |  |  |
| 57 | 1014 | 1051 |  |  |  |
| 58 | 1128 | 1014 |  |  |  |
| 59 | 1101 | 1128 |  |  |  |
| 60 | 1022 | 1101 |  |  |  |

> **Hoja larga:** arriba se muestran 60 de 1923 filas con datos. **Todos los valores de la hoja están en [`tarea-class-example-2-datos/DISPERSION.csv`](./tarea-class-example-2-datos/DISPERSION.csv)** (CSV, UTF-8).

**Fórmulas (6 patrones distintos):**

- `A2`: `=DATOS!B3`
- `E2`: `=CORREL(A2:A1923,B2:B1923)`
- `E3`: `=RSQ(B2:B1923,A2:A1923)`
- `E4`: `=SLOPE(B2:B1923,A2:A1923)`
- `E5`: `=INTERCEPT(B2:B1923,A2:A1923)`
- `E6`: `=COUNT(A2:A1923)`

### Hoja `GRAFICO ACF` — hoja de gráfico (sin celdas)

- Gráfico de barras + líneas — título «Función de autocorrelación para Ventas prod 1» · ejes: Desfase / Autocorrelación
  - Series: 'DATOS ACF'!$B$31: y = `'DATOS ACF'!$B$32:$B$119`, x = `'DATOS ACF'!$A$32:$A$119`; 'DATOS ACF'!$C$31: y = `'DATOS ACF'!$C$32:$C$119`, x = `'DATOS ACF'!$A$32:$A$119`; 'DATOS ACF'!$D$31: y = `'DATOS ACF'!$D$32:$D$119`, x = `'DATOS ACF'!$A$32:$A$119`

### Hoja `GRAFICO DE SERIES DE TIEMPO ` — hoja de gráfico (sin celdas)

- Gráfico de líneas — título «Gráfica de series de tiempo de Ventas prod 1» · ejes: Índice / Ventas prod 1
  - Series: (serie): y = `DATOS!$B$2:$B$251`

### Hoja `GRAFICO HISTOGRAMA` — hoja de gráfico (sin celdas)

- Gráfico de barras — título «Histograma de Ventas prod 1» · ejes: Ventas prod 1 / Frecuencia
  - Series: 'DATOS HISTOGRAMA'!$E$9: y = `'DATOS HISTOGRAMA'!$E$10:$E$49`, x = `'DATOS HISTOGRAMA'!$D$10:$D$49`

### Hoja `GRAFICO BOX PLOT` — hoja de gráfico (sin celdas)

- Gráfico de barras — título «(sin título)»

### Hoja `GRAFICO DISPERSION` — hoja de gráfico (sin celdas)

- Gráfico de dispersión — título «Gráfica de dispersión de Ventas prod 1 vs. periodo anterior» · ejes: Ventas prod 1 (periodo anterior)LINEA TENDENCIA AZUL ESTA SE BASA EN SI LAS VENTAS DE HOY SE PUEDEN REDECIR MAÑANA SI SE ACERA A LA LINE  / Ventas prod 1 (periodo actual)
  - Series: DISPERSION!$B$1: y = `DISPERSION!$B$2:$B$1923`, x = `DISPERSION!$A$2:$A$1923`

