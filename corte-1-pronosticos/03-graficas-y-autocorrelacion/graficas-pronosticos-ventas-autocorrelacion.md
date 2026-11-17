# graficas-pronosticos-ventas-autocorrelacion

> **Archivo:** [`graficas-pronosticos-ventas-autocorrelacion.xlsx`](./graficas-pronosticos-ventas-autocorrelacion.xlsx) · **Corte 1** · Libro de Excel con 2 hoja(s): `ANALISIS DE CORRELACION`, `DATOS`  
> **Nombre original:** `CORTE 1/GRAFICAS PARAA PRONOSCTICOS DE VENTAS.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Hoja de clase (nombre original «GRAFICAS PARAA PRONOSCTICOS DE VENTAS») que aplica las herramientas de visualización de la [Lección 4 — Plotting your data](./L04-plotting-your-data.md) a una serie larga de ventas: serie de tiempo, diagrama de dispersión $X_t$ frente a $X_{t-1}$ y **autocorrelograma** de 20 rezagos. Con ella se aprende a construir la tabla de rezagos en Excel, a obtener los coeficientes de autocorrelación con la matriz de correlación y a reconocer una serie **aleatoria** (sin tendencia, ciclo ni estacionalidad), en la que la venta de hoy no ayuda a predecir la de mañana.

### Hoja `DATOS`

**Objetivo (deducido):** preparar la serie y sus 20 rezagos para medir la autocorrelación y graficar los datos.

**Datos de entrada**

| Columna | Contenido |
|---|---|
| A `fecha` | Índice del periodo, de 1 a 30.000 (no es una fecha de calendario). |
| B `ventas` | Ventas por periodo: 30.000 datos enteros (filas 2–30001). |
| C–V `Rezago 1` … `Rezago 20` | La columna de ventas desplazada $k$ filas hacia abajo: en la fila del periodo $t$, `Rezago k` contiene $X_{t-k}$. Son valores pegados, no fórmulas; cada columna termina $k$ filas más abajo (hasta la fila 30021 para el rezago 20). |
| AE23, AE26 | Notas de texto del estudiante (ver «Gráficos»). |

Estadísticos de `ventas` (calculados sobre el CSV): $n=30.000$; mínimo 0; máximo 22; media 8,006; mediana 8; desviación estándar 2,808 (varianza ≈ 7,89, casi igual a la media, lo que sugiere —deducido— datos simulados con una distribución tipo Poisson de media ≈ 8).

Frecuencia de cada valor de ventas:

| Ventas | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Frecuencia | 10 | 83 | 310 | 788 | 1.716 | 2.807 | 3.581 | 4.291 | 4.221 | 3.658 | 3.012 | 2.191 |

| Ventas | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Frecuencia | 1.414 | 925 | 486 | 273 | 145 | 52 | 26 | 5 | 4 | 1 | 1 |

Todos los valores están en [`graficas-pronosticos-ventas-autocorrelacion-datos/DATOS.csv`](./graficas-pronosticos-ventas-autocorrelacion-datos/DATOS.csv).

**Gráficos**

- «Serie de tiempos» (líneas, `B2:B30001`): las 30.000 ventas en orden; una banda de ruido alrededor de 8, sin tendencia ni estacionalidad.
- «SCATTER PLOT» (dispersión): eje X = `ventas` ($X_t$, `B2:B30021`), eje Y = `Rezago 1` ($X_{t-1}$, `C2:C30021`). La nube no muestra relación lineal. Las notas del estudiante junto al gráfico dicen: «LINEA TENDENCIA ESTA SE BASA EN SI LAS VENTAS DE HOY SE PUEDEN REDECIR MAÑANA SI SE ACERA A LA LINE» (AE23) y «LAS BOLITAS DICEN SI HOY COMPRO MAÑANA DE PRONTO NO Y ASI» (AE26). El archivo no guarda una línea de tendencia en el gráfico.

### Hoja `ANALISIS DE CORRELACION`

**Objetivo:** calcular el coeficiente de autocorrelación de los rezagos 1 a 20 y graficar el autocorrelograma.

**Método paso a paso**

1. Se aplicó la herramienta *Análisis de datos → Correlación* de Excel a las 21 columnas `ventas`, `Rezago 1` … `Rezago 20`. El resultado es la matriz triangular de correlaciones de Pearson pegada como valores (sin fórmulas) en `A1:V22`; las etiquetas originales «Columna 1…21» se cambiaron por «REZAGO 1…20» en la columna A.
2. La columna B (`COEFECIENTE DE AUTORRELACION 1` = correlación con `ventas`) es el autocorrelograma: la fila del rezago $k$ contiene
   $$r_k\approx\operatorname{corr}(X_t,\,X_{t-k}).$$
   Se comprobó que estos valores coinciden con la correlación de Pearson calculada sobre las filas 22–30001 (29.980 filas en las que las 21 columnas tienen dato). Es una aproximación de la fórmula de $r_k$ de la L04 (allí se usa una sola media y el denominador de toda la serie); con 30.000 datos la diferencia es mínima.
3. El resto de la matriz (columnas C–V) son correlaciones entre rezagos; repite los mismos valores desplazados en diagonal y no se usa.

**Resultados — coeficientes de autocorrelación (columna B)**

| Rezago $k$ | $r_k$ | Rezago $k$ | $r_k$ |
|---|---|---|---|
| 1 | −0,000119 | 11 | −0,003981 |
| 2 | −0,008582 | 12 | 0,008942 |
| 3 | −0,002835 | 13 | −0,012121 |
| 4 | 0,001826 | 14 | 0,004399 |
| 5 | 0,011852 | 15 | −0,007323 |
| 6 | 0,000173 | 16 | −0,010894 |
| 7 | −0,005568 | 17 | −0,004121 |
| 8 | −0,001765 | 18 | 0,007372 |
| 9 | −0,001287 | 19 | 0,003375 |
| 10 | −0,001295 | 20 | −0,003897 |

**Gráfico:** «AUTOCORRELOGRAMA DE LOS DATOS» (barras, `B3:B22`): 20 barras diminutas alrededor de cero, todas con $|r_k|<0{,}013$. La hoja no dibuja límites de significancia.

**Conclusión**

- Todos los coeficientes son prácticamente cero: la serie es **aleatoria** (ruido alrededor de una media constante ≈ 8); no hay tendencia (los $r_k$ no son altos ni decrecen lentamente) ni estacionalidad (ningún rezago destaca). Así lo indica también la nota del estudiante: conocer la venta de hoy no permite predecir la de mañana.
- Cálculo propio con la fórmula de la L04: el límite de significancia del rezago 1 es $\pm t_{0,05;\,29999}/\sqrt{30000}=\pm1{,}96/173{,}2\approx\pm0{,}0113$. Solo los rezagos 5 (0,0119) y 13 (−0,0121) lo superan por muy poco, lo que con 20 rezagos y 5 % de significancia es esperable por azar (≈ 1 de cada 20).
- Para una serie así, un método para datos estacionarios (promedio o suavización simple, [carpeta 04](../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/README.md)) es el adecuado.

### Observaciones

- Ninguna celda tiene fórmulas: los rezagos y la matriz de correlación son valores pegados.
- El gráfico de dispersión toma hasta la fila 30021 aunque las ventas terminan en la 30001 (las últimas 20 filas solo tienen rezagos).
- La columna `fecha` es un contador de periodos, no una fecha.
- Hay errores ortográficos en los rótulos («COEFECIENTE DE AUTORRELACION», «PARAA PRONOSCTICOS»), sin efecto en los cálculos.

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `ANALISIS DE CORRELACION` — 22 filas × 22 columnas · 1 gráfico(s)

**Gráficos en esta hoja:**

- Gráfico de barras — título «AUTOCORRELOGRAMA DE LOS DATOS»
  - Series: (serie): y = `'ANALISIS DE CORRELACION'!$B$3:$B$22`

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 |  | COEFECIENTE DE AUTORRELACION 1 | Columna 2 | Columna 3 | Columna 4 | Columna 5 | Columna 6 | Columna 7 | Columna 8 | Columna 9 | Columna 10 | Columna 11 | Columna 12 | Columna 13 | Columna 14 | Columna 15 | Columna 16 | Columna 17 | Columna 18 | Columna 19 | Columna 20 | Columna 21 |
| 2 | REZAGO | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 | 1 | -0.000119281 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 | 2 | -0.00858193 | -0.000153223 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 | 3 | -0.00283478 | -0.00864202 | -0.000195665 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 | 4 | 0.00182611 | -0.00286893 | -0.00867626 | -0.000297456 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7 | 5 | 0.0118515 | 0.00186863 | -0.00280973 | -0.00852097 | -0.000195872 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 | 6 | 0.000172731 | 0.0118689 | 0.00193659 | -0.00267034 | -0.00843682 | -0.000309717 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9 | 7 | -0.00556761 | 0.000147219 | 0.0118605 | 0.00189005 | -0.00270443 | -0.00838234 | -0.000254541 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10 | 8 | -0.00176469 | -0.00551712 | 0.000181178 | 0.0119847 | 0.00197483 | -0.00283564 | -0.0085012 | -0.000216395 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |
| 11 | 9 | -0.00128653 | -0.00174775 | -0.00546633 | 0.000291234 | 0.0120531 | 0.00188229 | -0.00289468 | -0.00845903 | -0.000309249 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| 12 | 10 | -0.00129509 | -0.00131212 | -0.00177325 | -0.00554321 | 0.000240292 | 0.0121305 | 0.00194598 | -0.00292025 | -0.00839612 | -0.000258406 | 1 |  |  |  |  |  |  |  |  |  |  |
| 13 | 11 | -0.00398138 | -0.00125299 | -0.00137143 | -0.00182434 | -0.00556021 | 0.000240279 | 0.012075 | 0.00191179 | -0.00287371 | -0.00842959 | -0.000271341 | 1 |  |  |  |  |  |  |  |  |  |
| 14 | 12 | 0.00894199 | -0.00391381 | -0.00125299 | -0.00128706 | -0.00175681 | -0.0056789 | 0.000105101 | 0.012092 | 0.00184429 | -0.00297518 | -0.00837905 | -0.00015303 | 1 |  |  |  |  |  |  |  |  |
| 15 | 13 | -0.0121205 | 0.00891654 | -0.00392232 | -0.00129978 | -0.00132109 | -0.00170179 | -0.00562394 | 9.2356e-05 | 0.0121309 | 0.0018868 | -0.00300075 | -0.00841254 | -0.000136132 | 1 |  |  |  |  |  |  |  |
| 16 | 14 | 0.00439874 | -0.012163 | 0.00890814 | -0.0039905 | -0.00135075 | -0.00123642 | -0.00161283 | -0.00564101 | 0.000147451 | 0.0121991 | 0.00184866 | -0.00306425 | -0.00839573 | -0.000153113 | 1 |  |  |  |  |  |  |
| 17 | 15 | -0.00732345 | 0.00434787 | -0.012163 | 0.00884521 | -0.00404151 | -0.00126181 | -0.0011347 | -0.00162556 | -0.00559041 | 0.000223783 | 0.0121612 | 0.00175948 | -0.00306425 | -0.00840851 | -0.000165835 | 1 |  |  |  |  |  |
| 18 | 16 | -0.0108937 | -0.00734887 | 0.00435633 | -0.0121809 | 0.00882845 | -0.00400772 | -0.00121506 | -0.0011347 | -0.0016128 | -0.00555648 | 0.000211036 | 0.0121051 | 0.00174257 | -0.00306425 | -0.00840431 | -0.000153113 | 1 |  |  |  |  |
| 19 | 17 | -0.00412105 | -0.0109108 | -0.00734887 | 0.00433537 | -0.0121983 | 0.00885891 | -0.0039738 | -0.00121932 | -0.00111772 | -0.00158729 | -0.00556936 | 0.000181216 | 0.0121051 | 0.00173832 | -0.00306854 | -0.00840431 | -0.000148855 | 1 |  |  |  |
| 20 | 18 | 0.00737241 | -0.00415463 | -0.0108593 | -0.00730247 | 0.00435228 | -0.0122025 | 0.00890144 | -0.00394387 | -0.00126137 | -0.001092 | -0.00157448 | -0.0056914 | 7.98187e-05 | 0.0121343 | 0.00179339 | -0.00299206 | -0.0083571 | -0.000123301 | 1 |  |  |
| 21 | 19 | 0.00337483 | 0.00738056 | -0.00419702 | -0.0109237 | -0.00733673 | 0.00439067 | -0.0121985 | 0.00887162 | -0.00388905 | -0.0012529 | -0.0011176 | -0.00150696 | -0.00560685 | 5.00425e-05 | 0.0120833 | 0.00172977 | -0.00302596 | -0.0083783 | -0.000178269 | 1 |  |
| 22 | 20 | -0.00389676 | 0.00336616 | 0.0073382 | -0.00428225 | -0.0109752 | -0.00726961 | 0.00442903 | -0.0122327 | 0.00894408 | -0.00385531 | -0.00129123 | -0.00107977 | -0.00142248 | -0.00564095 | -5.12144e-06 | 0.0120199 | 0.00170006 | -0.00304729 | -0.00840755 | -0.000178533 | 1 |

### Hoja `DATOS` — 30021 filas × 31 columnas · 2 gráfico(s)

**Gráficos en esta hoja:**

- Gráfico de dispersión — título «SCATTER PLOT»
  - Series: DATOS!$C$1: y = `DATOS!$C$2:$C$30021`, x = `DATOS!$B$2:$B$30021`
- Gráfico de líneas — título «Serie de tiempos»
  - Series: DATOS!$B$1: y = `DATOS!$B$2:$B$30001`

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | AA | AB | AC | AD | AE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | fecha | ventas | Rezago 1 | Rezago 2 | Rezago 3 | Rezago 4 | Rezago 5 | Rezago 6 | Rezago 7 | Rezago 8 | Rezago 9 | Rezago 10 | Rezago 11 | Rezago 12 | Rezago 13 | Rezago 14 | Rezago 15 | Rezago 16 | Rezago 17 | Rezago 18 | Rezago 19 | Rezago 20 |  |  |  |  |  |  |  |  |  |
| 2 | 1 | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 | 2 | 11 | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 | 3 | 3 | 11 | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 | 4 | 7 | 3 | 11 | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 | 5 | 6 | 7 | 3 | 11 | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7 | 6 | 5 | 6 | 7 | 3 | 11 | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 | 7 | 6 | 5 | 6 | 7 | 3 | 11 | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9 | 8 | 7 | 6 | 5 | 6 | 7 | 3 | 11 | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10 | 9 | 12 | 7 | 6 | 5 | 6 | 7 | 3 | 11 | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 11 | 10 | 14 | 12 | 7 | 6 | 5 | 6 | 7 | 3 | 11 | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 12 | 11 | 8 | 14 | 12 | 7 | 6 | 5 | 6 | 7 | 3 | 11 | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 13 | 12 | 6 | 8 | 14 | 12 | 7 | 6 | 5 | 6 | 7 | 3 | 11 | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 14 | 13 | 9 | 6 | 8 | 14 | 12 | 7 | 6 | 5 | 6 | 7 | 3 | 11 | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 15 | 14 | 7 | 9 | 6 | 8 | 14 | 12 | 7 | 6 | 5 | 6 | 7 | 3 | 11 | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 16 | 15 | 5 | 7 | 9 | 6 | 8 | 14 | 12 | 7 | 6 | 5 | 6 | 7 | 3 | 11 | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 17 | 16 | 7 | 5 | 7 | 9 | 6 | 8 | 14 | 12 | 7 | 6 | 5 | 6 | 7 | 3 | 11 | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 18 | 17 | 8 | 7 | 5 | 7 | 9 | 6 | 8 | 14 | 12 | 7 | 6 | 5 | 6 | 7 | 3 | 11 | 10 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 19 | 18 | 7 | 8 | 7 | 5 | 7 | 9 | 6 | 8 | 14 | 12 | 7 | 6 | 5 | 6 | 7 | 3 | 11 | 10 |  |  |  |  |  |  |  |  |  |  |  |  |
| 20 | 19 | 6 | 7 | 8 | 7 | 5 | 7 | 9 | 6 | 8 | 14 | 12 | 7 | 6 | 5 | 6 | 7 | 3 | 11 | 10 |  |  |  |  |  |  |  |  |  |  |  |
| 21 | 20 | 10 | 6 | 7 | 8 | 7 | 5 | 7 | 9 | 6 | 8 | 14 | 12 | 7 | 6 | 5 | 6 | 7 | 3 | 11 | 10 |  |  |  |  |  |  |  |  |  |  |
| 22 | 21 | 7 | 10 | 6 | 7 | 8 | 7 | 5 | 7 | 9 | 6 | 8 | 14 | 12 | 7 | 6 | 5 | 6 | 7 | 3 | 11 | 10 |  |  |  |  |  |  |  |  |  |
| 23 | 22 | 6 | 7 | 10 | 6 | 7 | 8 | 7 | 5 | 7 | 9 | 6 | 8 | 14 | 12 | 7 | 6 | 5 | 6 | 7 | 3 | 11 |  |  |  |  |  |  |  |  | LINEA TENDENCIA ESTA SE BASA EN SI LAS VENTAS DE HOY SE PUEDEN REDECIR MAÑANA SI SE ACERA A LA LINE |
| 24 | 23 | 10 | 6 | 7 | 10 | 6 | 7 | 8 | 7 | 5 | 7 | 9 | 6 | 8 | 14 | 12 | 7 | 6 | 5 | 6 | 7 | 3 |  |  |  |  |  |  |  |  |  |
| 25 | 24 | 6 | 10 | 6 | 7 | 10 | 6 | 7 | 8 | 7 | 5 | 7 | 9 | 6 | 8 | 14 | 12 | 7 | 6 | 5 | 6 | 7 |  |  |  |  |  |  |  |  |  |
| 26 | 25 | 6 | 6 | 10 | 6 | 7 | 10 | 6 | 7 | 8 | 7 | 5 | 7 | 9 | 6 | 8 | 14 | 12 | 7 | 6 | 5 | 6 |  |  |  |  |  |  |  |  | LAS BOLITAS DICEN SI HOY COMPRO MAÑANA DE PRONTO NO Y ASI |
| 27 | 26 | 12 | 6 | 6 | 10 | 6 | 7 | 10 | 6 | 7 | 8 | 7 | 5 | 7 | 9 | 6 | 8 | 14 | 12 | 7 | 6 | 5 |  |  |  |  |  |  |  |  |  |
| 28 | 27 | 8 | 12 | 6 | 6 | 10 | 6 | 7 | 10 | 6 | 7 | 8 | 7 | 5 | 7 | 9 | 6 | 8 | 14 | 12 | 7 | 6 |  |  |  |  |  |  |  |  |  |
| 29 | 28 | 7 | 8 | 12 | 6 | 6 | 10 | 6 | 7 | 10 | 6 | 7 | 8 | 7 | 5 | 7 | 9 | 6 | 8 | 14 | 12 | 7 |  |  |  |  |  |  |  |  |  |
| 30 | 29 | 16 | 7 | 8 | 12 | 6 | 6 | 10 | 6 | 7 | 10 | 6 | 7 | 8 | 7 | 5 | 7 | 9 | 6 | 8 | 14 | 12 |  |  |  |  |  |  |  |  |  |
| 31 | 30 | 7 | 16 | 7 | 8 | 12 | 6 | 6 | 10 | 6 | 7 | 10 | 6 | 7 | 8 | 7 | 5 | 7 | 9 | 6 | 8 | 14 |  |  |  |  |  |  |  |  |  |
| 32 | 31 | 7 | 7 | 16 | 7 | 8 | 12 | 6 | 6 | 10 | 6 | 7 | 10 | 6 | 7 | 8 | 7 | 5 | 7 | 9 | 6 | 8 |  |  |  |  |  |  |  |  |  |
| 33 | 32 | 10 | 7 | 7 | 16 | 7 | 8 | 12 | 6 | 6 | 10 | 6 | 7 | 10 | 6 | 7 | 8 | 7 | 5 | 7 | 9 | 6 |  |  |  |  |  |  |  |  |  |
| 34 | 33 | 7 | 10 | 7 | 7 | 16 | 7 | 8 | 12 | 6 | 6 | 10 | 6 | 7 | 10 | 6 | 7 | 8 | 7 | 5 | 7 | 9 |  |  |  |  |  |  |  |  |  |
| 35 | 34 | 10 | 7 | 10 | 7 | 7 | 16 | 7 | 8 | 12 | 6 | 6 | 10 | 6 | 7 | 10 | 6 | 7 | 8 | 7 | 5 | 7 |  |  |  |  |  |  |  |  |  |
| 36 | 35 | 4 | 10 | 7 | 10 | 7 | 7 | 16 | 7 | 8 | 12 | 6 | 6 | 10 | 6 | 7 | 10 | 6 | 7 | 8 | 7 | 5 |  |  |  |  |  |  |  |  |  |
| 37 | 36 | 6 | 4 | 10 | 7 | 10 | 7 | 7 | 16 | 7 | 8 | 12 | 6 | 6 | 10 | 6 | 7 | 10 | 6 | 7 | 8 | 7 |  |  |  |  |  |  |  |  |  |
| 38 | 37 | 7 | 6 | 4 | 10 | 7 | 10 | 7 | 7 | 16 | 7 | 8 | 12 | 6 | 6 | 10 | 6 | 7 | 10 | 6 | 7 | 8 |  |  |  |  |  |  |  |  |  |
| 39 | 38 | 6 | 7 | 6 | 4 | 10 | 7 | 10 | 7 | 7 | 16 | 7 | 8 | 12 | 6 | 6 | 10 | 6 | 7 | 10 | 6 | 7 |  |  |  |  |  |  |  |  |  |
| 40 | 39 | 5 | 6 | 7 | 6 | 4 | 10 | 7 | 10 | 7 | 7 | 16 | 7 | 8 | 12 | 6 | 6 | 10 | 6 | 7 | 10 | 6 |  |  |  |  |  |  |  |  |  |
| 41 | 40 | 5 | 5 | 6 | 7 | 6 | 4 | 10 | 7 | 10 | 7 | 7 | 16 | 7 | 8 | 12 | 6 | 6 | 10 | 6 | 7 | 10 |  |  |  |  |  |  |  |  |  |
| 42 | 41 | 7 | 5 | 5 | 6 | 7 | 6 | 4 | 10 | 7 | 10 | 7 | 7 | 16 | 7 | 8 | 12 | 6 | 6 | 10 | 6 | 7 |  |  |  |  |  |  |  |  |  |
| 43 | 42 | 7 | 7 | 5 | 5 | 6 | 7 | 6 | 4 | 10 | 7 | 10 | 7 | 7 | 16 | 7 | 8 | 12 | 6 | 6 | 10 | 6 |  |  |  |  |  |  |  |  |  |
| 44 | 43 | 8 | 7 | 7 | 5 | 5 | 6 | 7 | 6 | 4 | 10 | 7 | 10 | 7 | 7 | 16 | 7 | 8 | 12 | 6 | 6 | 10 |  |  |  |  |  |  |  |  |  |
| 45 | 44 | 10 | 8 | 7 | 7 | 5 | 5 | 6 | 7 | 6 | 4 | 10 | 7 | 10 | 7 | 7 | 16 | 7 | 8 | 12 | 6 | 6 |  |  |  |  |  |  |  |  |  |
| 46 | 45 | 4 | 10 | 8 | 7 | 7 | 5 | 5 | 6 | 7 | 6 | 4 | 10 | 7 | 10 | 7 | 7 | 16 | 7 | 8 | 12 | 6 |  |  |  |  |  |  |  |  |  |
| 47 | 46 | 7 | 4 | 10 | 8 | 7 | 7 | 5 | 5 | 6 | 7 | 6 | 4 | 10 | 7 | 10 | 7 | 7 | 16 | 7 | 8 | 12 |  |  |  |  |  |  |  |  |  |
| 48 | 47 | 2 | 7 | 4 | 10 | 8 | 7 | 7 | 5 | 5 | 6 | 7 | 6 | 4 | 10 | 7 | 10 | 7 | 7 | 16 | 7 | 8 |  |  |  |  |  |  |  |  |  |
| 49 | 48 | 9 | 2 | 7 | 4 | 10 | 8 | 7 | 7 | 5 | 5 | 6 | 7 | 6 | 4 | 10 | 7 | 10 | 7 | 7 | 16 | 7 |  |  |  |  |  |  |  |  |  |
| 50 | 49 | 12 | 9 | 2 | 7 | 4 | 10 | 8 | 7 | 7 | 5 | 5 | 6 | 7 | 6 | 4 | 10 | 7 | 10 | 7 | 7 | 16 |  |  |  |  |  |  |  |  |  |
| 51 | 50 | 7 | 12 | 9 | 2 | 7 | 4 | 10 | 8 | 7 | 7 | 5 | 5 | 6 | 7 | 6 | 4 | 10 | 7 | 10 | 7 | 7 |  |  |  |  |  |  |  |  |  |
| 52 | 51 | 7 | 7 | 12 | 9 | 2 | 7 | 4 | 10 | 8 | 7 | 7 | 5 | 5 | 6 | 7 | 6 | 4 | 10 | 7 | 10 | 7 |  |  |  |  |  |  |  |  |  |
| 53 | 52 | 10 | 7 | 7 | 12 | 9 | 2 | 7 | 4 | 10 | 8 | 7 | 7 | 5 | 5 | 6 | 7 | 6 | 4 | 10 | 7 | 10 |  |  |  |  |  |  |  |  |  |
| 54 | 53 | 8 | 10 | 7 | 7 | 12 | 9 | 2 | 7 | 4 | 10 | 8 | 7 | 7 | 5 | 5 | 6 | 7 | 6 | 4 | 10 | 7 |  |  |  |  |  |  |  |  |  |
| 55 | 54 | 8 | 8 | 10 | 7 | 7 | 12 | 9 | 2 | 7 | 4 | 10 | 8 | 7 | 7 | 5 | 5 | 6 | 7 | 6 | 4 | 10 |  |  |  |  |  |  |  |  |  |
| 56 | 55 | 8 | 8 | 8 | 10 | 7 | 7 | 12 | 9 | 2 | 7 | 4 | 10 | 8 | 7 | 7 | 5 | 5 | 6 | 7 | 6 | 4 |  |  |  |  |  |  |  |  |  |
| 57 | 56 | 6 | 8 | 8 | 8 | 10 | 7 | 7 | 12 | 9 | 2 | 7 | 4 | 10 | 8 | 7 | 7 | 5 | 5 | 6 | 7 | 6 |  |  |  |  |  |  |  |  |  |
| 58 | 57 | 8 | 6 | 8 | 8 | 8 | 10 | 7 | 7 | 12 | 9 | 2 | 7 | 4 | 10 | 8 | 7 | 7 | 5 | 5 | 6 | 7 |  |  |  |  |  |  |  |  |  |
| 59 | 58 | 7 | 8 | 6 | 8 | 8 | 8 | 10 | 7 | 7 | 12 | 9 | 2 | 7 | 4 | 10 | 8 | 7 | 7 | 5 | 5 | 6 |  |  |  |  |  |  |  |  |  |
| 60 | 59 | 5 | 7 | 8 | 6 | 8 | 8 | 8 | 10 | 7 | 7 | 12 | 9 | 2 | 7 | 4 | 10 | 8 | 7 | 7 | 5 | 5 |  |  |  |  |  |  |  |  |  |

> **Hoja larga:** arriba se muestran 60 de 30021 filas con datos. **Todos los valores de la hoja están en [`graficas-pronosticos-ventas-autocorrelacion-datos/DATOS.csv`](./graficas-pronosticos-ventas-autocorrelacion-datos/DATOS.csv)** (CSV, UTF-8).

