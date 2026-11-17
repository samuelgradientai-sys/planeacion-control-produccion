# tarea-class-example-3

> **Archivo:** [`tarea-class-example-3.xlsx`](./tarea-class-example-3.xlsx) · **Corte 1** · Libro de Excel con 7 hoja(s): `Ventas`, `Coeficientes de correlacion`, `Serie de tiempo de Ventas`, `Histograma de ventas`, `Boxplot de ventas`, `Autocorrelograma de ventas`, `Scatterplot de ventas`  
> **Nombre original:** `CORTE 1/TAREAS/PRONOSCITOS DE DEMANDAS/Class example 3.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Tercer libro de la tarea «Pronósticos de demandas» (nombre original `TAREAS/PRONOSCITOS DE DEMANDAS/Class example 3.xlsx`), con la misma plantilla que el ejemplo 1 y basado en la [Lección 4 — Plotting your data](./L04-plotting-your-data.md): tabla de 20 rezagos, coeficientes con límites de significancia, serie de tiempo, histograma, boxplot, autocorrelograma y dispersión $X_t$ frente a $X_{t-1}$. La serie tiene una **tendencia creciente** muy marcada, así que el ejemplo muestra cómo se ve la tendencia en cada gráfico. Ojo: los coeficientes de la hoja están mal calculados (ver Observaciones).

### Hoja `Ventas`

**Datos de entrada**

- Columna A `Dato`: índice del periodo, de 2 a 302 (coincide con el número de fila).
- Columna B `Ventas`: 301 datos (filas 2–302).
- Columnas C–V `Rezago 1` … `Rezago 20`: la columna B desplazada $k$ filas hacia abajo (valores pegados).
- Nombre definido `DATOS` = `Ventas!A22:V302` (incluye la columna A).
- CSV completo: [`Ventas.csv`](./tarea-class-example-3-datos/Ventas.csv).

**Estadísticos (calculados):** $n=301$; mínimo 1; máximo 315 (en el dato 272); media 151,45; mediana 153; desviación estándar 88,05; cuartiles (método exclusivo) $Q_1=88{,}5$, $Q_3=227$. Primeros valores: 1, 6, 7, 5, 10, 11, 9, 12, 9, 13, 11, 14, 18, 14, 19, 20, 20, 19, 26, 25, 28, 29… Recta de regresión sobre el índice (cálculo propio): pendiente ≈ 0,98 por periodo.

Media por bloques de 25 datos (cálculo propio), que muestra la tendencia con algunos tramos planos o de retroceso:

| Datos | Media | Mín. | Máx. |
|---|---|---|---|
| 2–26 | 16,2 | 1 | 29 |
| 27–51 | 35,0 | 27 | 43 |
| 52–76 | 65,9 | 42 | 90 |
| 77–101 | 94,8 | 89 | 100 |
| 102–126 | 100,8 | 87 | 124 |
| 127–151 | 156,9 | 133 | 170 |
| 152–176 | 150,3 | 140 | 162 |
| 177–201 | 191,5 | 153 | 232 |
| 202–226 | 229,0 | 206 | 243 |
| 227–251 | 210,4 | 193 | 249 |
| 252–276 | 296,2 | 257 | 315 |
| 277–301 | 266,3 | 246 | 301 |
| 302 | 253 | 253 | 253 |

### Hoja `Coeficientes de correlacion`

**Método (tal como está en el archivo)**

1. Columna B (`Columna 1`, filas 3–23, etiquetadas `REZAGOS` 1 a 21): valores pegados de *Análisis de datos → Correlación* aplicada al rango `DATOS` = `Ventas!A22:V302`. Como ese rango empieza en la columna A (`Dato`), la primera columna de la matriz es el **índice del periodo** y no las ventas. Se comprobó que la fila «1» es $\operatorname{corr}(\text{Dato},\text{Ventas})$ y la fila «$k+1$» es $\operatorname{corr}(\text{Dato},\text{Rezago }k)$.
2. Límites (columnas C y D), con $n=$ `COUNT(Ventas!B2:B302)` $=301$ y $t=$ `TINV(0.05; 300)` $=1{,}9679$:
   - fila 3: $\pm t/\sqrt n=\pm0{,}113428$;
   - fila $j\ge4$: $\pm t\sqrt{\left(1+2\sum r_i^2\right)/n}$ con la suma de los valores de la columna B de las filas anteriores (`SUMSQ($B$3:B(j-1))`).

**Resultados que muestra la hoja**

| Fila (rezago) | Columna 1 | Límite ± | Fila (rezago) | Columna 1 | Límite ± |
|---|---|---|---|---|---|
| 1 | 0,964075 | 0,113428 | 12 | 0,972500 | 0,527341 |
| 2 | 0,964832 | 0,191787 | 13 | 0,972995 | 0,549931 |
| 3 | 0,965643 | 0,246447 | 14 | 0,973475 | 0,571651 |
| 4 | 0,966384 | 0,291084 | 15 | 0,973907 | 0,592596 |
| 5 | 0,967124 | 0,329789 | 16 | 0,974208 | 0,612843 |
| 6 | 0,967983 | 0,364457 | 17 | 0,974412 | 0,632454 |
| 7 | 0,968851 | 0,396156 | 18 | 0,974597 | 0,651483 |
| 8 | 0,969577 | 0,425550 | 19 | 0,974669 | 0,669978 |
| 9 | 0,970398 | 0,453082 | 20 | 0,974753 | 0,687979 |
| 10 | 0,971160 | 0,479076 | 21 | 0,974810 | 0,705524 |
| 11 | 0,971885 | 0,503769 | | | |

**Autocorrelación correcta (cálculo propio, no está en el archivo)**

| Rezago $k$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| $r_k$ (fórmula de la L04) | 0,9921 | 0,9845 | 0,9763 | 0,9673 | 0,9584 | 0,9489 | 0,9386 | 0,9282 | 0,9172 | 0,9058 |
| Pearson ventas–rezago (filas 22–302) | 0,9992 | 0,9981 | 0,9966 | 0,9944 | 0,9917 | 0,9884 | 0,9846 | 0,9804 | 0,9758 | 0,9707 |

| Rezago $k$ | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| $r_k$ (fórmula de la L04) | 0,8938 | 0,8814 | 0,8691 | 0,8562 | 0,8433 | 0,8300 | 0,8164 | 0,8026 | 0,7892 | 0,7756 |
| Pearson ventas–rezago (filas 22–302) | 0,9654 | 0,9597 | 0,9540 | 0,9481 | 0,9422 | 0,9362 | 0,9302 | 0,9244 | 0,9187 | 0,9133 |

### Hojas de gráficos

| Hoja | Tipo | Qué muestra |
|---|---|---|
| `Serie de tiempo de Ventas` | Líneas, `Ventas!B2:B302` | Serie que sube de ≈ 1 a ≈ 300 con escalones y retrocesos (tramos planos en 77–126 y 152–176, caídas en 227–251 y al final). |
| `Histograma de ventas` | Histograma nativo de Excel sobre `B2:B302` | Distribución extendida de 1 a 315, sin una moda clara: refleja la rampa, no un ruido alrededor de una media. |
| `Boxplot de ventas` | Caja y bigotes nativo (cuartiles exclusivos, marca de la media) | Caja de 88,5 a 227 con mediana 153 y bigotes de 1 a 315; sin atípicos. |
| `Autocorrelograma de ventas` | Barras (`B3:B23`) + límites (`C3:D23`) | 21 barras ≈ 0,96–0,97 muy por encima de los límites, que crecen de 0,11 a 0,71. |
| `Scatterplot de ventas` | Dispersión, X = ventas (`B2:B322`), Y = rezago 1 (`C2:C322`) | «X(t) vs X(t-1)»: puntos alineados en una diagonal casi perfecta. |

### Conclusión

- La serie tiene una **tendencia creciente** fuerte: el autocorrelograma correcto empieza en 0,992 y baja despacio hasta 0,776 en el rezago 20, siempre muy por encima de los límites (patrón «Trendline» de la L04, p. 16), y la dispersión $X_t$–$X_{t-1}$ es casi una recta.
- La conclusión de la hoja (todos los coeficientes significativos → hay tendencia) es correcta aunque los números estén mal calculados.
- Para pronosticarla no sirven los métodos estacionarios; corresponde un método con tendencia, como [Holt](../05-tendencia-suavizacion-doble-holt/).

### Observaciones

- **Error en los coeficientes:** la correlación se calculó sobre `A22:V302`, que incluye la columna `Dato`; la columna B de la hoja es la correlación del índice del periodo con las ventas y sus rezagos, no la autocorrelación. Por eso los valores *suben* con el rezago (0,964 → 0,975), algo imposible en un correlograma de tendencia. Además hay 21 filas: la etiqueta «1» corresponde en realidad al rezago 0 (ventas) y la etiqueta «$k+1$» al rezago $k$.
- En consecuencia, los límites de las filas 4–23 también están inflados (se calcularon con esos coeficientes).
- El gráfico de dispersión toma hasta la fila 322 aunque las ventas terminan en la 302.
- Los coeficientes son valores pegados; no se recalculan.

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `Ventas` — 322 filas × 22 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Dato | Ventas | Rezago 1 | Rezago 2 | Rezago 3 | Rezago 4 | Rezago 5 | Rezago 6 | Rezago 7 | Rezago 8 | Rezago 9 | Rezago 10 | Rezago 11 | Rezago 12 | Rezago 13 | Rezago 14 | Rezago 15 | Rezago 16 | Rezago 17 | Rezago 18 | Rezago 19 | Rezago 20 |
| 2 | 2 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 | 3 | 6 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 | 4 | 7 | 6 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 | 5 | 5 | 7 | 6 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 | 6 | 10 | 5 | 7 | 6 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7 | 7 | 11 | 10 | 5 | 7 | 6 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 | 8 | 9 | 11 | 10 | 5 | 7 | 6 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9 | 9 | 12 | 9 | 11 | 10 | 5 | 7 | 6 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10 | 10 | 9 | 12 | 9 | 11 | 10 | 5 | 7 | 6 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |
| 11 | 11 | 13 | 9 | 12 | 9 | 11 | 10 | 5 | 7 | 6 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| 12 | 12 | 11 | 13 | 9 | 12 | 9 | 11 | 10 | 5 | 7 | 6 | 1 |  |  |  |  |  |  |  |  |  |  |
| 13 | 13 | 14 | 11 | 13 | 9 | 12 | 9 | 11 | 10 | 5 | 7 | 6 | 1 |  |  |  |  |  |  |  |  |  |
| 14 | 14 | 18 | 14 | 11 | 13 | 9 | 12 | 9 | 11 | 10 | 5 | 7 | 6 | 1 |  |  |  |  |  |  |  |  |
| 15 | 15 | 14 | 18 | 14 | 11 | 13 | 9 | 12 | 9 | 11 | 10 | 5 | 7 | 6 | 1 |  |  |  |  |  |  |  |
| 16 | 16 | 19 | 14 | 18 | 14 | 11 | 13 | 9 | 12 | 9 | 11 | 10 | 5 | 7 | 6 | 1 |  |  |  |  |  |  |
| 17 | 17 | 20 | 19 | 14 | 18 | 14 | 11 | 13 | 9 | 12 | 9 | 11 | 10 | 5 | 7 | 6 | 1 |  |  |  |  |  |
| 18 | 18 | 20 | 20 | 19 | 14 | 18 | 14 | 11 | 13 | 9 | 12 | 9 | 11 | 10 | 5 | 7 | 6 | 1 |  |  |  |  |
| 19 | 19 | 19 | 20 | 20 | 19 | 14 | 18 | 14 | 11 | 13 | 9 | 12 | 9 | 11 | 10 | 5 | 7 | 6 | 1 |  |  |  |
| 20 | 20 | 26 | 19 | 20 | 20 | 19 | 14 | 18 | 14 | 11 | 13 | 9 | 12 | 9 | 11 | 10 | 5 | 7 | 6 | 1 |  |  |
| 21 | 21 | 25 | 26 | 19 | 20 | 20 | 19 | 14 | 18 | 14 | 11 | 13 | 9 | 12 | 9 | 11 | 10 | 5 | 7 | 6 | 1 |  |
| 22 | 22 | 28 | 25 | 26 | 19 | 20 | 20 | 19 | 14 | 18 | 14 | 11 | 13 | 9 | 12 | 9 | 11 | 10 | 5 | 7 | 6 | 1 |
| 23 | 23 | 29 | 28 | 25 | 26 | 19 | 20 | 20 | 19 | 14 | 18 | 14 | 11 | 13 | 9 | 12 | 9 | 11 | 10 | 5 | 7 | 6 |
| 24 | 24 | 27 | 29 | 28 | 25 | 26 | 19 | 20 | 20 | 19 | 14 | 18 | 14 | 11 | 13 | 9 | 12 | 9 | 11 | 10 | 5 | 7 |
| 25 | 25 | 26 | 27 | 29 | 28 | 25 | 26 | 19 | 20 | 20 | 19 | 14 | 18 | 14 | 11 | 13 | 9 | 12 | 9 | 11 | 10 | 5 |
| 26 | 26 | 26 | 26 | 27 | 29 | 28 | 25 | 26 | 19 | 20 | 20 | 19 | 14 | 18 | 14 | 11 | 13 | 9 | 12 | 9 | 11 | 10 |
| 27 | 27 | 32 | 26 | 26 | 27 | 29 | 28 | 25 | 26 | 19 | 20 | 20 | 19 | 14 | 18 | 14 | 11 | 13 | 9 | 12 | 9 | 11 |
| 28 | 28 | 30 | 32 | 26 | 26 | 27 | 29 | 28 | 25 | 26 | 19 | 20 | 20 | 19 | 14 | 18 | 14 | 11 | 13 | 9 | 12 | 9 |
| 29 | 29 | 27 | 30 | 32 | 26 | 26 | 27 | 29 | 28 | 25 | 26 | 19 | 20 | 20 | 19 | 14 | 18 | 14 | 11 | 13 | 9 | 12 |
| 30 | 30 | 29 | 27 | 30 | 32 | 26 | 26 | 27 | 29 | 28 | 25 | 26 | 19 | 20 | 20 | 19 | 14 | 18 | 14 | 11 | 13 | 9 |
| 31 | 31 | 34 | 29 | 27 | 30 | 32 | 26 | 26 | 27 | 29 | 28 | 25 | 26 | 19 | 20 | 20 | 19 | 14 | 18 | 14 | 11 | 13 |
| 32 | 32 | 34 | 34 | 29 | 27 | 30 | 32 | 26 | 26 | 27 | 29 | 28 | 25 | 26 | 19 | 20 | 20 | 19 | 14 | 18 | 14 | 11 |
| 33 | 33 | 31 | 34 | 34 | 29 | 27 | 30 | 32 | 26 | 26 | 27 | 29 | 28 | 25 | 26 | 19 | 20 | 20 | 19 | 14 | 18 | 14 |
| 34 | 34 | 31 | 31 | 34 | 34 | 29 | 27 | 30 | 32 | 26 | 26 | 27 | 29 | 28 | 25 | 26 | 19 | 20 | 20 | 19 | 14 | 18 |
| 35 | 35 | 34 | 31 | 31 | 34 | 34 | 29 | 27 | 30 | 32 | 26 | 26 | 27 | 29 | 28 | 25 | 26 | 19 | 20 | 20 | 19 | 14 |
| 36 | 36 | 30 | 34 | 31 | 31 | 34 | 34 | 29 | 27 | 30 | 32 | 26 | 26 | 27 | 29 | 28 | 25 | 26 | 19 | 20 | 20 | 19 |
| 37 | 37 | 34 | 30 | 34 | 31 | 31 | 34 | 34 | 29 | 27 | 30 | 32 | 26 | 26 | 27 | 29 | 28 | 25 | 26 | 19 | 20 | 20 |
| 38 | 38 | 34 | 34 | 30 | 34 | 31 | 31 | 34 | 34 | 29 | 27 | 30 | 32 | 26 | 26 | 27 | 29 | 28 | 25 | 26 | 19 | 20 |
| 39 | 39 | 36 | 34 | 34 | 30 | 34 | 31 | 31 | 34 | 34 | 29 | 27 | 30 | 32 | 26 | 26 | 27 | 29 | 28 | 25 | 26 | 19 |
| 40 | 40 | 36 | 36 | 34 | 34 | 30 | 34 | 31 | 31 | 34 | 34 | 29 | 27 | 30 | 32 | 26 | 26 | 27 | 29 | 28 | 25 | 26 |
| 41 | 41 | 32 | 36 | 36 | 34 | 34 | 30 | 34 | 31 | 31 | 34 | 34 | 29 | 27 | 30 | 32 | 26 | 26 | 27 | 29 | 28 | 25 |
| 42 | 42 | 36 | 32 | 36 | 36 | 34 | 34 | 30 | 34 | 31 | 31 | 34 | 34 | 29 | 27 | 30 | 32 | 26 | 26 | 27 | 29 | 28 |
| 43 | 43 | 34 | 36 | 32 | 36 | 36 | 34 | 34 | 30 | 34 | 31 | 31 | 34 | 34 | 29 | 27 | 30 | 32 | 26 | 26 | 27 | 29 |
| 44 | 44 | 37 | 34 | 36 | 32 | 36 | 36 | 34 | 34 | 30 | 34 | 31 | 31 | 34 | 34 | 29 | 27 | 30 | 32 | 26 | 26 | 27 |
| 45 | 45 | 40 | 37 | 34 | 36 | 32 | 36 | 36 | 34 | 34 | 30 | 34 | 31 | 31 | 34 | 34 | 29 | 27 | 30 | 32 | 26 | 26 |
| 46 | 46 | 40 | 40 | 37 | 34 | 36 | 32 | 36 | 36 | 34 | 34 | 30 | 34 | 31 | 31 | 34 | 34 | 29 | 27 | 30 | 32 | 26 |
| 47 | 47 | 42 | 40 | 40 | 37 | 34 | 36 | 32 | 36 | 36 | 34 | 34 | 30 | 34 | 31 | 31 | 34 | 34 | 29 | 27 | 30 | 32 |
| 48 | 48 | 38 | 42 | 40 | 40 | 37 | 34 | 36 | 32 | 36 | 36 | 34 | 34 | 30 | 34 | 31 | 31 | 34 | 34 | 29 | 27 | 30 |
| 49 | 49 | 40 | 38 | 42 | 40 | 40 | 37 | 34 | 36 | 32 | 36 | 36 | 34 | 34 | 30 | 34 | 31 | 31 | 34 | 34 | 29 | 27 |
| 50 | 50 | 43 | 40 | 38 | 42 | 40 | 40 | 37 | 34 | 36 | 32 | 36 | 36 | 34 | 34 | 30 | 34 | 31 | 31 | 34 | 34 | 29 |
| 51 | 51 | 41 | 43 | 40 | 38 | 42 | 40 | 40 | 37 | 34 | 36 | 32 | 36 | 36 | 34 | 34 | 30 | 34 | 31 | 31 | 34 | 34 |
| 52 | 52 | 42 | 41 | 43 | 40 | 38 | 42 | 40 | 40 | 37 | 34 | 36 | 32 | 36 | 36 | 34 | 34 | 30 | 34 | 31 | 31 | 34 |
| 53 | 53 | 43 | 42 | 41 | 43 | 40 | 38 | 42 | 40 | 40 | 37 | 34 | 36 | 32 | 36 | 36 | 34 | 34 | 30 | 34 | 31 | 31 |
| 54 | 54 | 49 | 43 | 42 | 41 | 43 | 40 | 38 | 42 | 40 | 40 | 37 | 34 | 36 | 32 | 36 | 36 | 34 | 34 | 30 | 34 | 31 |
| 55 | 55 | 52 | 49 | 43 | 42 | 41 | 43 | 40 | 38 | 42 | 40 | 40 | 37 | 34 | 36 | 32 | 36 | 36 | 34 | 34 | 30 | 34 |
| 56 | 56 | 51 | 52 | 49 | 43 | 42 | 41 | 43 | 40 | 38 | 42 | 40 | 40 | 37 | 34 | 36 | 32 | 36 | 36 | 34 | 34 | 30 |
| 57 | 57 | 52 | 51 | 52 | 49 | 43 | 42 | 41 | 43 | 40 | 38 | 42 | 40 | 40 | 37 | 34 | 36 | 32 | 36 | 36 | 34 | 34 |
| 58 | 58 | 55 | 52 | 51 | 52 | 49 | 43 | 42 | 41 | 43 | 40 | 38 | 42 | 40 | 40 | 37 | 34 | 36 | 32 | 36 | 36 | 34 |
| 59 | 59 | 52 | 55 | 52 | 51 | 52 | 49 | 43 | 42 | 41 | 43 | 40 | 38 | 42 | 40 | 40 | 37 | 34 | 36 | 32 | 36 | 36 |
| 60 | 60 | 55 | 52 | 55 | 52 | 51 | 52 | 49 | 43 | 42 | 41 | 43 | 40 | 38 | 42 | 40 | 40 | 37 | 34 | 36 | 32 | 36 |

> **Hoja larga:** arriba se muestran 60 de 322 filas con datos. **Todos los valores de la hoja están en [`tarea-class-example-3-datos/Ventas.csv`](./tarea-class-example-3-datos/Ventas.csv)** (CSV, UTF-8).

### Hoja `Coeficientes de correlacion` — 23 filas × 4 columnas

| Fila | A | B | C | D |
|---|---|---|---|---|
| 1 |  | Columna 1 | Limite inf | Limite sup |
| 2 | REZAGOS | 1 |  |  |
| 3 | 1 | 0.964075 | -0.113428 | 0.113428 |
| 4 | 2 | 0.964832 | -0.191787 | 0.191787 |
| 5 | 3 | 0.965643 | -0.246447 | 0.246447 |
| 6 | 4 | 0.966384 | -0.291084 | 0.291084 |
| 7 | 5 | 0.967124 | -0.329789 | 0.329789 |
| 8 | 6 | 0.967983 | -0.364457 | 0.364457 |
| 9 | 7 | 0.968851 | -0.396156 | 0.396156 |
| 10 | 8 | 0.969577 | -0.42555 | 0.42555 |
| 11 | 9 | 0.970398 | -0.453082 | 0.453082 |
| 12 | 10 | 0.97116 | -0.479076 | 0.479076 |
| 13 | 11 | 0.971885 | -0.503769 | 0.503769 |
| 14 | 12 | 0.9725 | -0.527341 | 0.527341 |
| 15 | 13 | 0.972995 | -0.549931 | 0.549931 |
| 16 | 14 | 0.973475 | -0.571651 | 0.571651 |
| 17 | 15 | 0.973907 | -0.592596 | 0.592596 |
| 18 | 16 | 0.974208 | -0.612843 | 0.612843 |
| 19 | 17 | 0.974412 | -0.632454 | 0.632454 |
| 20 | 18 | 0.974597 | -0.651483 | 0.651483 |
| 21 | 19 | 0.974669 | -0.669978 | 0.669978 |
| 22 | 20 | 0.974753 | -0.687979 | 0.687979 |
| 23 | 21 | 0.97481 | -0.705524 | 0.705524 |

**Fórmulas (4 patrones distintos):**

- `C3`: `=-TINV(0.05,COUNT(Ventas!$B$2:$B$302)-1)*(1/SQRT(COUNT(Ventas!$B$2:$B$302)))`
- `D3`: `=TINV(0.05,COUNT(Ventas!$B$2:$B$302)-1)*(1/SQRT(COUNT(Ventas!$B$2:$B$302)))`
- `C4`: `=-TINV(0.05,COUNT(Ventas!$B$2:$B$302)-1)*SQRT((1+2*SUMSQ($B$3:B3))/COUNT(Ventas!$B$2:$B$302))`
- `D4`: `=TINV(0.05,COUNT(Ventas!$B$2:$B$302)-1)*SQRT((1+2*SUMSQ($B$3:B3))/COUNT(Ventas!$B$2:$B$302))`

### Hoja `Serie de tiempo de Ventas` — hoja de gráfico (sin celdas)

- Gráfico de líneas — título «Serie de tiempo de Ventas»
  - Series: Ventas!$B$1: y = `Ventas!$B$2:$B$302`

### Hoja `Histograma de ventas` — hoja de gráfico (sin celdas)

- Gráfico de barras — título «(sin título)»

### Hoja `Boxplot de ventas` — hoja de gráfico (sin celdas)

- Gráfico de barras — título «(sin título)»

### Hoja `Autocorrelograma de ventas` — hoja de gráfico (sin celdas)

- Gráfico de barras + líneas — título «Autocorrelograma de ventas»
  - Series: (serie): y = `'Coeficientes de correlacion'!$B$3:$B$23`; 'Coeficientes de correlacion'!$C$1: y = `'Coeficientes de correlacion'!$C$3:$C$23`; 'Coeficientes de correlacion'!$D$1: y = `'Coeficientes de correlacion'!$D$3:$D$23`

### Hoja `Scatterplot de ventas` — hoja de gráfico (sin celdas)

- Gráfico de dispersión — título «Scatterplot de ventasX(t) vs X(t-1)»
  - Series: Ventas!$C$1: y = `Ventas!$C$2:$C$322`, x = `Ventas!$B$2:$B$322`

