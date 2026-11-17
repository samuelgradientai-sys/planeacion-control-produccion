# tarea-class-example-4

> **Archivo:** [`tarea-class-example-4.xlsx`](./tarea-class-example-4.xlsx) · **Corte 1** · Libro de Excel con 7 hoja(s): `Datos`, `Coeficientes `, `Serie de tiempo de los datos`, `Histograma de los datos`, `Autocorrelograma de los datos`, `Boxplot de los datos`, `Scatterplot de los datos`  
> **Nombre original:** `CORTE 1/TAREAS/PRONOSCITOS DE DEMANDAS/Class example 4.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Cuarto libro de la tarea «Pronósticos de demandas» (nombre original `TAREAS/PRONOSCITOS DE DEMANDAS/Class example 4.xlsx`), con la misma plantilla que el ejemplo 1 y basado en la [Lección 4 — Plotting your data](./L04-plotting-your-data.md). La serie **alterna** un valor alto y uno bajo en cada periodo, de modo que el ejemplo enseña cómo se ve en el correlograma un patrón periódico (estacionalidad de periodo 2): coeficientes grandes que cambian de signo en cada rezago y no se apagan.

### Hoja `Datos`

**Datos de entrada**

- Columna A `dato`: índice del periodo, de 1 a 500.
- Columna B `DATO`: 500 valores (filas 2–501).
- Columnas C–V `Rezago 1` … `Rezago 20`: la columna B desplazada $k$ filas hacia abajo (valores pegados; terminan en la fila 521).
- CSV completo: [`Datos.csv`](./tarea-class-example-4-datos/Datos.csv).

**Estadísticos (calculados):** $n=500$; mínimo 3.895; máximo 3.918; media 3.906,98; mediana 3.907; desviación estándar 5,61; cuartiles (método exclusivo) $Q_1=3.902$, $Q_3=3.912$. Primeros valores: 3.904, 3.914, 3.904, 3.916, 3.901, 3.911, 3.904, 3.912, 3.902, 3.908, …

**Patrón (cálculo propio):** los datos en posición impar (1.º, 3.º, …) promedian 3.901,8 (rango 3.895–3.907) y los de posición par 3.912,1 (rango 3.907–3.918). En los 250 pares, el dato par siempre es mayor que el impar anterior, y el signo de la diferencia $X_t-X_{t-1}$ cambia en el 100 % de los periodos: la serie es un zigzag perfecto. No hay tendencia: la media de los primeros 250 datos es 3.906,84 y la de los últimos 250, 3.907,12 (pendiente ≈ 0,0013 por periodo).

Distribución de valores:

| Valor | 3.895 | 3.896 | 3.897 | 3.898 | 3.899 | 3.900 | 3.901 | 3.902 | 3.903 | 3.904 | 3.905 | 3.906 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Frecuencia | 1 | 2 | 4 | 8 | 24 | 30 | 41 | 45 | 36 | 31 | 16 | 10 |

| Valor | 3.907 | 3.908 | 3.909 | 3.910 | 3.911 | 3.912 | 3.913 | 3.914 | 3.915 | 3.916 | 3.917 | 3.918 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Frecuencia | 3 | 6 | 21 | 28 | 47 | 33 | 49 | 34 | 16 | 11 | 1 | 3 |

### Hoja `Coeficientes `

**Método**

1. Columna B (`Columna 1`, filas 3–22): valores pegados de *Análisis de datos → Correlación*. Se comprobó que coinciden con la correlación de Pearson entre `DATO` y cada `Rezago k` sobre las filas 22–501 (480 filas completas):
   $$r_k\approx\operatorname{corr}(X_t,\,X_{t-k}).$$
2. Límites (columnas C y D), con $n=$ `COUNT(Datos!B2:B501)` $=500$ y $t=$ `TINV(0.05; 499)` $=1{,}9647$:
   - rezago 1: $\pm t/\sqrt n=\pm0{,}0878654$;
   - rezago $k\ge2$: $\pm t\sqrt{\left(1+2\sum_{i=1}^{k-1}r_i^2\right)/n}$ (`SUMSQ($B$3:B(k+1))`), fórmula de la p. 13 de la L04, bien implementada.

**Resultados**

| Rezago $k$ | $r_k$ | Límite ± | $r_k$ con la fórmula de la L04 (cálculo propio) |
|---|---|---|---|
| 1 | −0,848281 | 0,087865 | −0,8451 |
| 2 | 0,850925 | 0,137226 | 0,8459 |
| 3 | −0,855568 | 0,173238 | −0,8489 |
| 4 | 0,852494 | 0,203258 | 0,8429 |
| 5 | −0,852179 | 0,229206 | −0,8422 |
| 6 | 0,852084 | 0,252484 | 0,8394 |
| 7 | −0,850560 | 0,273786 | −0,8381 |
| 8 | 0,847797 | 0,293478 | 0,8331 |
| 9 | −0,861220 | 0,311814 | −0,8444 |
| 10 | 0,846456 | 0,329666 | 0,8319 |
| 11 | −0,850312 | 0,346039 | −0,8336 |
| 12 | 0,836787 | 0,361811 | 0,8198 |
| 13 | −0,855348 | 0,376456 | −0,8349 |
| 14 | 0,852107 | 0,391172 | 0,8307 |
| 15 | −0,859963 | 0,405249 | −0,8380 |
| 16 | 0,854492 | 0,419101 | 0,8289 |
| 17 | −0,852548 | 0,432342 | −0,8278 |
| 18 | 0,861264 | 0,445132 | 0,8329 |
| 19 | −0,847809 | 0,457817 | −0,8169 |
| 20 | 0,849091 | 0,469781 | 0,8159 |

### Hojas de gráficos

| Hoja | Tipo | Qué muestra |
|---|---|---|
| `Serie de tiempo de los datos` | Líneas, `Datos!B2:B501` | Zigzag constante entre ≈ 3.900 y ≈ 3.913 alrededor de 3.907, sin tendencia. |
| `Histograma de los datos` | Histograma nativo de Excel sobre `B2:B501` | Distribución **bimodal**: un grupo alrededor de 3.901–3.902 (datos impares) y otro alrededor de 3.911–3.913 (datos pares), con un valle en 3.906–3.908. |
| `Autocorrelograma de los datos` | Barras (`B3:B22`) + límites (`C3:D22`) | Barras de ±0,85 que alternan signo (negativas en rezagos impares, positivas en pares), todas fuera de los límites. |
| `Boxplot de los datos` | Caja y bigotes nativo sobre `B2:B501` (cuartiles exclusivos) | Caja de 3.902 a 3.912, mediana 3.907, bigotes 3.895–3.918; sin atípicos. |
| `Scatterplot de los datos` | Dispersión, X = dato (`B2:B1944`), Y = rezago 1 (`C2:C1944`) | «X(t) vs X(t-1)»: dos nubes separadas (alto–bajo y bajo–alto) que forman una relación negativa. |

### Conclusión

- Todos los coeficientes son significativos, grandes (|r| ≈ 0,85) y **alternan de signo sin decaer**: la serie tiene un patrón periódico de longitud 2 (un periodo alto, uno bajo), es decir, **estacionalidad** de periodo 2 (patrón «Seasonality» de la L04, p. 16), sin tendencia.
- Un promedio móvil o una suavización simple promediarían el zigzag y fallarían en cada periodo; corresponde un método con estacionalidad, como [Winters](../06-estacionalidad-winters-y-tracking-signal/), con longitud de estación 2.

### Observaciones

- El libro conserva restos de la plantilla del ejemplo 1: los nombres definidos `DATOS`, `DATOS1` y varios `_xlchart.v1.*` apuntan a `#REF!`, `DATOS2` apunta a `Datos!C22:V1924` y el gráfico de dispersión toma hasta la fila 1944 aunque los datos terminan en la 501 (o la 502 para el rezago 1). No afecta a los resultados.
- `DATOS3` = `Datos!B22:V501` es el rango usado para la matriz de correlación (deducido: coincide con los coeficientes).
- Los coeficientes son valores pegados; no se recalculan.

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `Datos` — 1944 filas × 22 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | dato | DATO | Rezago 1 | Rezago 2 | Rezago 3 | Rezago 4 | Rezago 5 | Rezago 6 | Rezago 7 | Rezago 8 | Rezago 9 | Rezago 10 | Rezago 11 | Rezago 12 | Rezago 13 | Rezago 14 | Rezago 15 | Rezago 16 | Rezago 17 | Rezago 18 | Rezago 19 | Rezago 20 |
| 2 | 1 | 3904 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 | 2 | 3914 | 3904 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 | 3 | 3904 | 3914 | 3904 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 | 4 | 3916 | 3904 | 3914 | 3904 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 | 5 | 3901 | 3916 | 3904 | 3914 | 3904 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7 | 6 | 3911 | 3901 | 3916 | 3904 | 3914 | 3904 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 | 7 | 3904 | 3911 | 3901 | 3916 | 3904 | 3914 | 3904 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9 | 8 | 3912 | 3904 | 3911 | 3901 | 3916 | 3904 | 3914 | 3904 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10 | 9 | 3902 | 3912 | 3904 | 3911 | 3901 | 3916 | 3904 | 3914 | 3904 |  |  |  |  |  |  |  |  |  |  |  |  |
| 11 | 10 | 3908 | 3902 | 3912 | 3904 | 3911 | 3901 | 3916 | 3904 | 3914 | 3904 |  |  |  |  |  |  |  |  |  |  |  |
| 12 | 11 | 3902 | 3908 | 3902 | 3912 | 3904 | 3911 | 3901 | 3916 | 3904 | 3914 | 3904 |  |  |  |  |  |  |  |  |  |  |
| 13 | 12 | 3911 | 3902 | 3908 | 3902 | 3912 | 3904 | 3911 | 3901 | 3916 | 3904 | 3914 | 3904 |  |  |  |  |  |  |  |  |  |
| 14 | 13 | 3904 | 3911 | 3902 | 3908 | 3902 | 3912 | 3904 | 3911 | 3901 | 3916 | 3904 | 3914 | 3904 |  |  |  |  |  |  |  |  |
| 15 | 14 | 3916 | 3904 | 3911 | 3902 | 3908 | 3902 | 3912 | 3904 | 3911 | 3901 | 3916 | 3904 | 3914 | 3904 |  |  |  |  |  |  |  |
| 16 | 15 | 3902 | 3916 | 3904 | 3911 | 3902 | 3908 | 3902 | 3912 | 3904 | 3911 | 3901 | 3916 | 3904 | 3914 | 3904 |  |  |  |  |  |  |
| 17 | 16 | 3911 | 3902 | 3916 | 3904 | 3911 | 3902 | 3908 | 3902 | 3912 | 3904 | 3911 | 3901 | 3916 | 3904 | 3914 | 3904 |  |  |  |  |  |
| 18 | 17 | 3905 | 3911 | 3902 | 3916 | 3904 | 3911 | 3902 | 3908 | 3902 | 3912 | 3904 | 3911 | 3901 | 3916 | 3904 | 3914 | 3904 |  |  |  |  |
| 19 | 18 | 3909 | 3905 | 3911 | 3902 | 3916 | 3904 | 3911 | 3902 | 3908 | 3902 | 3912 | 3904 | 3911 | 3901 | 3916 | 3904 | 3914 | 3904 |  |  |  |
| 20 | 19 | 3899 | 3909 | 3905 | 3911 | 3902 | 3916 | 3904 | 3911 | 3902 | 3908 | 3902 | 3912 | 3904 | 3911 | 3901 | 3916 | 3904 | 3914 | 3904 |  |  |
| 21 | 20 | 3913 | 3899 | 3909 | 3905 | 3911 | 3902 | 3916 | 3904 | 3911 | 3902 | 3908 | 3902 | 3912 | 3904 | 3911 | 3901 | 3916 | 3904 | 3914 | 3904 |  |
| 22 | 21 | 3901 | 3913 | 3899 | 3909 | 3905 | 3911 | 3902 | 3916 | 3904 | 3911 | 3902 | 3908 | 3902 | 3912 | 3904 | 3911 | 3901 | 3916 | 3904 | 3914 | 3904 |
| 23 | 22 | 3913 | 3901 | 3913 | 3899 | 3909 | 3905 | 3911 | 3902 | 3916 | 3904 | 3911 | 3902 | 3908 | 3902 | 3912 | 3904 | 3911 | 3901 | 3916 | 3904 | 3914 |
| 24 | 23 | 3903 | 3913 | 3901 | 3913 | 3899 | 3909 | 3905 | 3911 | 3902 | 3916 | 3904 | 3911 | 3902 | 3908 | 3902 | 3912 | 3904 | 3911 | 3901 | 3916 | 3904 |
| 25 | 24 | 3909 | 3903 | 3913 | 3901 | 3913 | 3899 | 3909 | 3905 | 3911 | 3902 | 3916 | 3904 | 3911 | 3902 | 3908 | 3902 | 3912 | 3904 | 3911 | 3901 | 3916 |
| 26 | 25 | 3899 | 3909 | 3903 | 3913 | 3901 | 3913 | 3899 | 3909 | 3905 | 3911 | 3902 | 3916 | 3904 | 3911 | 3902 | 3908 | 3902 | 3912 | 3904 | 3911 | 3901 |
| 27 | 26 | 3912 | 3899 | 3909 | 3903 | 3913 | 3901 | 3913 | 3899 | 3909 | 3905 | 3911 | 3902 | 3916 | 3904 | 3911 | 3902 | 3908 | 3902 | 3912 | 3904 | 3911 |
| 28 | 27 | 3901 | 3912 | 3899 | 3909 | 3903 | 3913 | 3901 | 3913 | 3899 | 3909 | 3905 | 3911 | 3902 | 3916 | 3904 | 3911 | 3902 | 3908 | 3902 | 3912 | 3904 |
| 29 | 28 | 3911 | 3901 | 3912 | 3899 | 3909 | 3903 | 3913 | 3901 | 3913 | 3899 | 3909 | 3905 | 3911 | 3902 | 3916 | 3904 | 3911 | 3902 | 3908 | 3902 | 3912 |
| 30 | 29 | 3900 | 3911 | 3901 | 3912 | 3899 | 3909 | 3903 | 3913 | 3901 | 3913 | 3899 | 3909 | 3905 | 3911 | 3902 | 3916 | 3904 | 3911 | 3902 | 3908 | 3902 |
| 31 | 30 | 3911 | 3900 | 3911 | 3901 | 3912 | 3899 | 3909 | 3903 | 3913 | 3901 | 3913 | 3899 | 3909 | 3905 | 3911 | 3902 | 3916 | 3904 | 3911 | 3902 | 3908 |
| 32 | 31 | 3901 | 3911 | 3900 | 3911 | 3901 | 3912 | 3899 | 3909 | 3903 | 3913 | 3901 | 3913 | 3899 | 3909 | 3905 | 3911 | 3902 | 3916 | 3904 | 3911 | 3902 |
| 33 | 32 | 3914 | 3901 | 3911 | 3900 | 3911 | 3901 | 3912 | 3899 | 3909 | 3903 | 3913 | 3901 | 3913 | 3899 | 3909 | 3905 | 3911 | 3902 | 3916 | 3904 | 3911 |
| 34 | 33 | 3901 | 3914 | 3901 | 3911 | 3900 | 3911 | 3901 | 3912 | 3899 | 3909 | 3903 | 3913 | 3901 | 3913 | 3899 | 3909 | 3905 | 3911 | 3902 | 3916 | 3904 |
| 35 | 34 | 3910 | 3901 | 3914 | 3901 | 3911 | 3900 | 3911 | 3901 | 3912 | 3899 | 3909 | 3903 | 3913 | 3901 | 3913 | 3899 | 3909 | 3905 | 3911 | 3902 | 3916 |
| 36 | 35 | 3905 | 3910 | 3901 | 3914 | 3901 | 3911 | 3900 | 3911 | 3901 | 3912 | 3899 | 3909 | 3903 | 3913 | 3901 | 3913 | 3899 | 3909 | 3905 | 3911 | 3902 |
| 37 | 36 | 3908 | 3905 | 3910 | 3901 | 3914 | 3901 | 3911 | 3900 | 3911 | 3901 | 3912 | 3899 | 3909 | 3903 | 3913 | 3901 | 3913 | 3899 | 3909 | 3905 | 3911 |
| 38 | 37 | 3905 | 3908 | 3905 | 3910 | 3901 | 3914 | 3901 | 3911 | 3900 | 3911 | 3901 | 3912 | 3899 | 3909 | 3903 | 3913 | 3901 | 3913 | 3899 | 3909 | 3905 |
| 39 | 38 | 3910 | 3905 | 3908 | 3905 | 3910 | 3901 | 3914 | 3901 | 3911 | 3900 | 3911 | 3901 | 3912 | 3899 | 3909 | 3903 | 3913 | 3901 | 3913 | 3899 | 3909 |
| 40 | 39 | 3902 | 3910 | 3905 | 3908 | 3905 | 3910 | 3901 | 3914 | 3901 | 3911 | 3900 | 3911 | 3901 | 3912 | 3899 | 3909 | 3903 | 3913 | 3901 | 3913 | 3899 |
| 41 | 40 | 3913 | 3902 | 3910 | 3905 | 3908 | 3905 | 3910 | 3901 | 3914 | 3901 | 3911 | 3900 | 3911 | 3901 | 3912 | 3899 | 3909 | 3903 | 3913 | 3901 | 3913 |
| 42 | 41 | 3901 | 3913 | 3902 | 3910 | 3905 | 3908 | 3905 | 3910 | 3901 | 3914 | 3901 | 3911 | 3900 | 3911 | 3901 | 3912 | 3899 | 3909 | 3903 | 3913 | 3901 |
| 43 | 42 | 3910 | 3901 | 3913 | 3902 | 3910 | 3905 | 3908 | 3905 | 3910 | 3901 | 3914 | 3901 | 3911 | 3900 | 3911 | 3901 | 3912 | 3899 | 3909 | 3903 | 3913 |
| 44 | 43 | 3903 | 3910 | 3901 | 3913 | 3902 | 3910 | 3905 | 3908 | 3905 | 3910 | 3901 | 3914 | 3901 | 3911 | 3900 | 3911 | 3901 | 3912 | 3899 | 3909 | 3903 |
| 45 | 44 | 3912 | 3903 | 3910 | 3901 | 3913 | 3902 | 3910 | 3905 | 3908 | 3905 | 3910 | 3901 | 3914 | 3901 | 3911 | 3900 | 3911 | 3901 | 3912 | 3899 | 3909 |
| 46 | 45 | 3899 | 3912 | 3903 | 3910 | 3901 | 3913 | 3902 | 3910 | 3905 | 3908 | 3905 | 3910 | 3901 | 3914 | 3901 | 3911 | 3900 | 3911 | 3901 | 3912 | 3899 |
| 47 | 46 | 3914 | 3899 | 3912 | 3903 | 3910 | 3901 | 3913 | 3902 | 3910 | 3905 | 3908 | 3905 | 3910 | 3901 | 3914 | 3901 | 3911 | 3900 | 3911 | 3901 | 3912 |
| 48 | 47 | 3904 | 3914 | 3899 | 3912 | 3903 | 3910 | 3901 | 3913 | 3902 | 3910 | 3905 | 3908 | 3905 | 3910 | 3901 | 3914 | 3901 | 3911 | 3900 | 3911 | 3901 |
| 49 | 48 | 3914 | 3904 | 3914 | 3899 | 3912 | 3903 | 3910 | 3901 | 3913 | 3902 | 3910 | 3905 | 3908 | 3905 | 3910 | 3901 | 3914 | 3901 | 3911 | 3900 | 3911 |
| 50 | 49 | 3899 | 3914 | 3904 | 3914 | 3899 | 3912 | 3903 | 3910 | 3901 | 3913 | 3902 | 3910 | 3905 | 3908 | 3905 | 3910 | 3901 | 3914 | 3901 | 3911 | 3900 |
| 51 | 50 | 3911 | 3899 | 3914 | 3904 | 3914 | 3899 | 3912 | 3903 | 3910 | 3901 | 3913 | 3902 | 3910 | 3905 | 3908 | 3905 | 3910 | 3901 | 3914 | 3901 | 3911 |
| 52 | 51 | 3901 | 3911 | 3899 | 3914 | 3904 | 3914 | 3899 | 3912 | 3903 | 3910 | 3901 | 3913 | 3902 | 3910 | 3905 | 3908 | 3905 | 3910 | 3901 | 3914 | 3901 |
| 53 | 52 | 3912 | 3901 | 3911 | 3899 | 3914 | 3904 | 3914 | 3899 | 3912 | 3903 | 3910 | 3901 | 3913 | 3902 | 3910 | 3905 | 3908 | 3905 | 3910 | 3901 | 3914 |
| 54 | 53 | 3898 | 3912 | 3901 | 3911 | 3899 | 3914 | 3904 | 3914 | 3899 | 3912 | 3903 | 3910 | 3901 | 3913 | 3902 | 3910 | 3905 | 3908 | 3905 | 3910 | 3901 |
| 55 | 54 | 3912 | 3898 | 3912 | 3901 | 3911 | 3899 | 3914 | 3904 | 3914 | 3899 | 3912 | 3903 | 3910 | 3901 | 3913 | 3902 | 3910 | 3905 | 3908 | 3905 | 3910 |
| 56 | 55 | 3900 | 3912 | 3898 | 3912 | 3901 | 3911 | 3899 | 3914 | 3904 | 3914 | 3899 | 3912 | 3903 | 3910 | 3901 | 3913 | 3902 | 3910 | 3905 | 3908 | 3905 |
| 57 | 56 | 3916 | 3900 | 3912 | 3898 | 3912 | 3901 | 3911 | 3899 | 3914 | 3904 | 3914 | 3899 | 3912 | 3903 | 3910 | 3901 | 3913 | 3902 | 3910 | 3905 | 3908 |
| 58 | 57 | 3900 | 3916 | 3900 | 3912 | 3898 | 3912 | 3901 | 3911 | 3899 | 3914 | 3904 | 3914 | 3899 | 3912 | 3903 | 3910 | 3901 | 3913 | 3902 | 3910 | 3905 |
| 59 | 58 | 3910 | 3900 | 3916 | 3900 | 3912 | 3898 | 3912 | 3901 | 3911 | 3899 | 3914 | 3904 | 3914 | 3899 | 3912 | 3903 | 3910 | 3901 | 3913 | 3902 | 3910 |
| 60 | 59 | 3900 | 3910 | 3900 | 3916 | 3900 | 3912 | 3898 | 3912 | 3901 | 3911 | 3899 | 3914 | 3904 | 3914 | 3899 | 3912 | 3903 | 3910 | 3901 | 3913 | 3902 |

> **Hoja larga:** arriba se muestran 60 de 521 filas con datos. **Todos los valores de la hoja están en [`tarea-class-example-4-datos/Datos.csv`](./tarea-class-example-4-datos/Datos.csv)** (CSV, UTF-8).

### Hoja `Coeficientes ` — 22 filas × 4 columnas

| Fila | A | B | C | D |
|---|---|---|---|---|
| 1 |  | Columna 1 | Limite inf | Limite sup |
| 2 | REZAGO | 1 |  |  |
| 3 | 1 | -0.848281 | -0.0878654 | 0.0878654 |
| 4 | 2 | 0.850925 | -0.137226 | 0.137226 |
| 5 | 3 | -0.855568 | -0.173238 | 0.173238 |
| 6 | 4 | 0.852494 | -0.203258 | 0.203258 |
| 7 | 5 | -0.852179 | -0.229206 | 0.229206 |
| 8 | 6 | 0.852084 | -0.252484 | 0.252484 |
| 9 | 7 | -0.85056 | -0.273786 | 0.273786 |
| 10 | 8 | 0.847797 | -0.293478 | 0.293478 |
| 11 | 9 | -0.86122 | -0.311814 | 0.311814 |
| 12 | 10 | 0.846456 | -0.329666 | 0.329666 |
| 13 | 11 | -0.850312 | -0.346039 | 0.346039 |
| 14 | 12 | 0.836787 | -0.361811 | 0.361811 |
| 15 | 13 | -0.855348 | -0.376456 | 0.376456 |
| 16 | 14 | 0.852107 | -0.391172 | 0.391172 |
| 17 | 15 | -0.859963 | -0.405249 | 0.405249 |
| 18 | 16 | 0.854492 | -0.419101 | 0.419101 |
| 19 | 17 | -0.852548 | -0.432342 | 0.432342 |
| 20 | 18 | 0.861264 | -0.445132 | 0.445132 |
| 21 | 19 | -0.847809 | -0.457817 | 0.457817 |
| 22 | 20 | 0.849091 | -0.469781 | 0.469781 |

**Fórmulas (4 patrones distintos):**

- `C3`: `=-TINV(0.05,COUNT(Datos!$B$2:$B$501)-1)*(1/SQRT(COUNT(Datos!$B$2:$B$501)))`
- `D3`: `=TINV(0.05,COUNT(Datos!$B$2:$B$501)-1)*(1/SQRT(COUNT(Datos!$B$2:$B$501)))`
- `C4`: `=-TINV(0.05,COUNT(Datos!$B$2:$B$501)-1)*SQRT((1+2*SUMSQ($B$3:B3))/COUNT(Datos!$B$2:$B$501))`
- `D4`: `=TINV(0.05,COUNT(Datos!$B$2:$B$501)-1)*SQRT((1+2*SUMSQ($B$3:B3))/COUNT(Datos!$B$2:$B$501))`

### Hoja `Serie de tiempo de los datos` — hoja de gráfico (sin celdas)

- Gráfico de líneas — título «Serie de tiempo de los datos»
  - Series: (serie): y = `Datos!$B$2:$B$501`

### Hoja `Histograma de los datos` — hoja de gráfico (sin celdas)

- Gráfico de barras — título «(sin título)»

### Hoja `Autocorrelograma de los datos` — hoja de gráfico (sin celdas)

- Gráfico de barras + líneas — título «Autocorrelograma de los datos»
  - Series: (serie): y = `'Coeficientes '!$B$3:$B$22`; 'Coeficientes '!$C$1: y = `'Coeficientes '!$C$3:$C$22`; 'Coeficientes '!$D$1: y = `'Coeficientes '!$D$3:$D$22`

### Hoja `Boxplot de los datos` — hoja de gráfico (sin celdas)

- Gráfico de barras — título «(sin título)»

### Hoja `Scatterplot de los datos` — hoja de gráfico (sin celdas)

- Gráfico de dispersión — título «Scatterplot de los datosX(t) vs X(t-1)»
  - Series: Datos!$C$1: y = `Datos!$C$2:$C$1944`, x = `Datos!$B$2:$B$1944`

