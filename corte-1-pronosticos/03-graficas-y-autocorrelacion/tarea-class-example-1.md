# tarea-class-example-1

> **Archivo:** [`tarea-class-example-1.xlsx`](./tarea-class-example-1.xlsx) · **Corte 1** · Libro de Excel con 14 hoja(s): `Ventas propias`, `Coeficientes ventas propias`, `Serie de tiempo  ventas propias`, `Histograma Ventas Propias`, `Autocorrelograma ventas propias`, `Boxplot Ventas Propias`, `Scatterplot Ventas Propias`, `Ventas competencia`, `Coeficientes ventas competencia`, `Serie de tiempo Ventas Comp`, `Histograma Ventas Competencia`, `Autocorrelograma Ventas Compete`, `Boxplot Ventas Competencia`, `Scatterplot Ventas Competencia`  
> **Nombre original:** `CORTE 1/TAREAS/PRONOSCITOS DE DEMANDAS/Class example 1.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Primer libro de la tarea «Pronósticos de demandas» (nombre original `TAREAS/PRONOSCITOS DE DEMANDAS/Class example 1.xlsx`). Aplica las herramientas de la [Lección 4 — Plotting your data](./L04-plotting-your-data.md) a dos series diarias: **ventas propias** y **ventas de la competencia**. Para cada una construye la tabla de 20 rezagos, los coeficientes de autocorrelación con sus **límites de significancia** y cinco gráficos (serie de tiempo, histograma, autocorrelograma, boxplot y dispersión $X_t$ frente a $X_{t-1}$). Se aprende a detectar datos atípicos con el boxplot y a decidir, con el correlograma, si la serie es aleatoria.

Las dos partes (ventas propias y competencia) siguen exactamente la misma estructura de hojas.

### Hojas `Ventas propias` y `Ventas competencia` (datos y rezagos)

**Objetivo (deducido del enunciado de la tarea):** organizar cada serie con sus rezagos 1 a 20 para calcular la autocorrelación.

**Datos de entrada**

- Columna A `Fecha`: 1.923 días consecutivos, **en orden descendente**, del 2019-08-30 (fila 2) al 2014-05-26 (fila 1924), sin fechas faltantes ni repetidas.
- Columna B: ventas del día (filas 2–1924). En la hoja `Ventas competencia` el encabezado dice por error «Ventas propias».
- Columnas C–V `Rezago 1` … `Rezago 20`: la columna B desplazada $k$ filas hacia abajo (valores pegados, sin fórmulas). Como las fechas van de la más reciente a la más antigua, en la fila del día $d$ el `Rezago k` contiene la venta del día $d+k$ (el día siguiente), no la del anterior. Para la autocorrelación da igual, porque $\operatorname{corr}(X_t,X_{t+k})=\operatorname{corr}(X_t,X_{t-k})$.
- Nombres definidos en el libro: `DATOS` = `'Ventas propias'!A22:V1924`, `DATOS1` = `'Ventas propias'!B22:V1924`, `DATOS2` = `'Ventas competencia'!B22:V1924` (los rangos usados para la matriz de correlación).
- CSV completos: [`Ventas_propias.csv`](./tarea-class-example-1-datos/Ventas_propias.csv) y [`Ventas_competencia.csv`](./tarea-class-example-1-datos/Ventas_competencia.csv).

**Estadísticos (calculados sobre los datos)**

| Serie | n | Mínimo | Q1 | Mediana | Q3 | Máximo | Media | Desv. estándar |
|---|---|---|---|---|---|---|---|---|
| Ventas propias | 1.923 | 9 | 1.717 | 1.943 | 2.153 | 31.624 | 1.954,15 | 725,72 |
| Ventas competencia | 1.923 | 2 | 805 | 1.019 | 1.241 | 1.464 | 1.019,18 | 255,42 |

(Cuartiles con el método exclusivo, el mismo que usa el boxplot del archivo.)

**Datos atípicos** (fuera de $Q_1-1{,}5\,RIQ$ y $Q_3+1{,}5\,RIQ$; $RIQ=436$ en ambas series):

| Serie | Fecha | Valor | Límites del boxplot |
|---|---|---|---|
| Ventas propias | 2019-07-14 | 31.624 | 1.063 – 2.807 |
| Ventas propias | 2019-06-08 | 12 | 1.063 – 2.807 |
| Ventas propias | 2017-10-10 | 9 | 1.063 – 2.807 |
| Ventas competencia | 2017-06-19 | 2 | 151 – 1.895 |

Sin los atípicos, las ventas propias van de 1.500 a 2.400 (media 1.940,7; desviación 254,3) y las de la competencia de 550 a 1.464 (media 1.019,7; desviación 254,4); en ambos casos el histograma es casi plano. El valor 31.624 explica él solo el 87,7 % de la suma de cuadrados de las ventas propias e infla su desviación estándar de ≈ 254 a 726.

**Relación entre las dos series (hallazgo propio, no está en el archivo):** fuera de los días atípicos, ventas propias + ventas competencia está siempre entre 2.950 y 2.970 (media 2.960) y la correlación entre ambas es −0,9997. Es decir, el mercado diario es casi constante (≈ 2.960 unidades) y la competencia vende lo que la empresa no vende.

### Hojas `Coeficientes ventas propias` y `Coeficientes ventas competencia`

**Método paso a paso**

1. **Coeficiente de autocorrelación** (columna B, `Columna 1`, filas 3–22): valores pegados de la herramienta *Análisis de datos → Correlación* aplicada a `DATOS1` / `DATOS2` (filas 22–1924, las 1.903 filas en que las 21 columnas tienen dato). Se comprobó que coinciden con la correlación de Pearson entre la columna de ventas y cada rezago:
   $$r_k\approx\operatorname{corr}(X_t,\,X_{t-k}),\qquad k=1,\dots,20.$$
   La fila 2 (`REZAGO`, valor 1) es la correlación de la serie consigo misma (rezago 0).
2. **Límites de significancia** (columnas C y D), según la p. 13 de la L04, con $n=$ `COUNT(B2:B1924)` $=1.923$ y $t=$ `TINV(0.05; n−1)` $=1{,}9612$:
   - Rezago 1: `=±TINV(0.05,COUNT(...)-1)*(1/SQRT(COUNT(...)))`, es decir $\pm t\cdot\dfrac{1}{\sqrt n}=\pm0{,}0447231$.
   - Rezago $k\ge2$: `=±TINV(0.05,COUNT(...)-1)*SQRT((1+2*SUMSQ($B$3:B(k+1)))/COUNT(...))`, es decir
     $$\pm\,t\sqrt{\frac{1+2\sum_{i=1}^{k-1}r_i^2}{n}}.$$

**Resultados**

| Rezago | $r_k$ propias | Límite propias (±) | $r_k$ competencia | Límite competencia (±), alineado como en el gráfico |
|---|---|---|---|---|
| 1 | −0,000466 | 0,044723 | 0,019231 | 0,044723 |
| 2 | 0,002065 | 0,044723 | −0,022244 | 0,044740 |
| 3 | −0,006008 | 0,044723 | −0,001451 | 0,044762 |
| 4 | −0,029202 | 0,044725 | **−0,045928** | 0,044762 |
| 5 | 0,006566 | 0,044763 | 0,020306 | 0,044856 |
| 6 | −0,012125 | 0,044765 | −0,016478 | 0,044874 |
| 7 | 0,021697 | 0,044772 | −0,009156 | 0,044887 |
| 8 | 0,011315 | 0,044793 | 0,019201 | 0,044890 |
| 9 | 0,001126 | 0,044798 | 0,002754 | 0,044907 |
| 10 | 0,009834 | 0,044798 | 0,027866 | 0,044907 |
| 11 | −0,005085 | 0,044803 | 0,018966 | 0,044942 |
| 12 | −0,019854 | 0,044804 | −0,007965 | 0,044958 |
| 13 | −0,003052 | 0,044821 | −0,014783 | 0,044960 |
| 14 | 0,004551 | 0,044822 | −0,027259 | 0,044970 |
| 15 | −0,001138 | 0,044823 | −0,012767 | 0,045003 |
| 16 | −0,003143 | 0,044823 | 0,001042 | 0,045010 |
| 17 | −0,001804 | 0,044823 | 0,015883 | 0,045010 |
| 18 | −0,000902 | 0,044823 | 0,014358 | 0,045022 |
| 19 | 0,000319 | 0,044823 | 0,038556 | 0,045031 |
| 20 | 0,001122 | 0,044823 | 0,001481 | 0,045097 |

(En la tabla de la hoja de competencia, cada límite aparece una fila más abajo; ver Observaciones. El límite inferior del rezago 1 de ventas propias es −0,0447231 y el superior 0,0447348.)

### Hojas de gráficos (iguales para las dos series)

| Hoja | Tipo | Qué muestra |
|---|---|---|
| `Serie de tiempo  ventas propias` / `Serie de tiempo Ventas Comp` | Líneas, `B2:B1944` | Las 1.923 ventas diarias (en el orden de la hoja, del día más reciente al más antiguo). En ventas propias el pico de 31.624 aplasta el resto de la serie; en competencia se ve una banda de ruido entre 550 y 1.464 con la caída a 2. |
| `Histograma Ventas Propias` / `Histograma Ventas Competencia` | Histograma nativo de Excel (agrupación automática) | Distribución casi uniforme de las ventas; en ventas propias el atípico estira el eje. |
| `Autocorrelograma ventas propias` / `Autocorrelograma Ventas Compete` | Barras ($r_k$) + dos líneas (límites inferior y superior) | 20 barras pequeñas alrededor de cero dentro de la banda de ≈ ±0,045. |
| `Boxplot Ventas Propias` / `Boxplot Ventas Competencia` | Caja y bigotes nativo (cuartiles exclusivos, marca de la media, atípicos visibles) | Caja de 1.717 a 2.153 (propias) y de 805 a 1.241 (competencia), con los atípicos de la tabla de arriba. |
| `Scatterplot Ventas Propias` / `Scatterplot Ventas Competencia` | Dispersión, X = ventas (`B2:B1924`), Y = rezago 1 (`C2:C1924`) | «X(t) vs X(t-1)»: nube sin relación lineal. |

### Conclusión

- **Ventas propias:** todos los $r_k$ están dentro de los límites (el mayor en valor absoluto es −0,0292 en el rezago 4) → serie **aleatoria**, sin tendencia ni estacionalidad. Pero el atípico de 31.624 encoge los coeficientes: recalculando la autocorrelación con los tres atípicos reemplazados por la mediana (cálculo propio), los $r_k$ quedan casi iguales a los de la competencia (máximo $|r_k|=0{,}041$ en el rezago 19 y −0,041 en el rezago 4), todavía dentro de los límites.
- **Ventas competencia:** solo el rezago 4 (−0,0459) supera por muy poco el límite (±0,0448); con 20 rezagos al 5 % es esperable que uno salga por azar. En la práctica también es una serie aleatoria.
- Ninguna serie muestra tendencia ni estacionalidad (el rezago 7, que delataría un patrón semanal, no es significativo, y las medias anuales de ventas propias sin atípicos apenas varían entre 1.917 y 1.953): son candidatas a métodos para datos estacionarios ([carpeta 04](../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/README.md)). Antes de pronosticar hay que depurar los atípicos (31.624, 12, 9 y 2), que parecen errores de registro.

### Observaciones

- **Límite superior del rezago 1 de ventas propias:** `D3` cuenta `C2:C1924` (1.922 datos) en vez de `B2:B1924` (1.923), por eso vale 0,0447348 y no 0,0447231. Diferencia despreciable.
- **Límites de la hoja de competencia desplazados una fila:** `C2:D2` (fila `REZAGO`, rezago 0) tiene el límite del rezago 1, y la fila del rezago $k$ usa `SUMSQ($B$3:B(k+2))` $=\sum_{i=1}^{k}r_i^2$ (incluye el propio $r_k$) en vez de $\sum_{i=1}^{k-1}r_i^2$. El gráfico toma los límites de `C2:D22` y las barras de `B3:B22`, así que en el gráfico cada barra queda frente a su límite correcto; solo la tabla está corrida (y el gráfico dibuja un punto de límite de más, el 21).
- Los coeficientes no se recalculan solos: son valores pegados; si se corrigen los atípicos hay que repetir la correlación.
- El encabezado de la columna B de `Ventas competencia` dice «Ventas propias».
- Las hojas de este libro son idénticas, celda por celda, a las del mismo nombre en [promedio-movil-y-suavizacion-exponencial.md](../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/promedio-movil-y-suavizacion-exponencial.md), que además añade la hoja `Ventas propias (2)` con promedios móviles y suavización exponencial.

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `Ventas propias` — 1944 filas × 22 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Fecha | Ventas propias | Rezago 1 | Rezago 2 | Rezago 3 | Rezago 4 | Rezago 5 | Rezago 6 | Rezago 7 | Rezago 8 | Rezago 9 | Rezago 10 | Rezago 11 | Rezago 12 | Rezago 13 | Rezago 14 | Rezago 15 | Rezago 16 | Rezago 17 | Rezago 18 | Rezago 19 | Rezago 20 |
| 2 | 2019-08-30 | 1841 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 | 2019-08-29 | 2219 | 1841 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 | 2019-08-28 | 2188 | 2219 | 1841 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 | 2019-08-27 | 1920 | 2188 | 2219 | 1841 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 | 2019-08-26 | 2100 | 1920 | 2188 | 2219 | 1841 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7 | 2019-08-25 | 1860 | 2100 | 1920 | 2188 | 2219 | 1841 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 | 2019-08-24 | 1733 | 1860 | 2100 | 1920 | 2188 | 2219 | 1841 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9 | 2019-08-23 | 1776 | 1733 | 1860 | 2100 | 1920 | 2188 | 2219 | 1841 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10 | 2019-08-22 | 1707 | 1776 | 1733 | 1860 | 2100 | 1920 | 2188 | 2219 | 1841 |  |  |  |  |  |  |  |  |  |  |  |  |
| 11 | 2019-08-21 | 1896 | 1707 | 1776 | 1733 | 1860 | 2100 | 1920 | 2188 | 2219 | 1841 |  |  |  |  |  |  |  |  |  |  |  |
| 12 | 2019-08-20 | 2253 | 1896 | 1707 | 1776 | 1733 | 1860 | 2100 | 1920 | 2188 | 2219 | 1841 |  |  |  |  |  |  |  |  |  |  |
| 13 | 2019-08-19 | 1971 | 2253 | 1896 | 1707 | 1776 | 1733 | 1860 | 2100 | 1920 | 2188 | 2219 | 1841 |  |  |  |  |  |  |  |  |  |
| 14 | 2019-08-18 | 1807 | 1971 | 2253 | 1896 | 1707 | 1776 | 1733 | 1860 | 2100 | 1920 | 2188 | 2219 | 1841 |  |  |  |  |  |  |  |  |
| 15 | 2019-08-17 | 1502 | 1807 | 1971 | 2253 | 1896 | 1707 | 1776 | 1733 | 1860 | 2100 | 1920 | 2188 | 2219 | 1841 |  |  |  |  |  |  |  |
| 16 | 2019-08-16 | 2020 | 1502 | 1807 | 1971 | 2253 | 1896 | 1707 | 1776 | 1733 | 1860 | 2100 | 1920 | 2188 | 2219 | 1841 |  |  |  |  |  |  |
| 17 | 2019-08-15 | 2320 | 2020 | 1502 | 1807 | 1971 | 2253 | 1896 | 1707 | 1776 | 1733 | 1860 | 2100 | 1920 | 2188 | 2219 | 1841 |  |  |  |  |  |
| 18 | 2019-08-14 | 1935 | 2320 | 2020 | 1502 | 1807 | 1971 | 2253 | 1896 | 1707 | 1776 | 1733 | 1860 | 2100 | 1920 | 2188 | 2219 | 1841 |  |  |  |  |
| 19 | 2019-08-13 | 2210 | 1935 | 2320 | 2020 | 1502 | 1807 | 1971 | 2253 | 1896 | 1707 | 1776 | 1733 | 1860 | 2100 | 1920 | 2188 | 2219 | 1841 |  |  |  |
| 20 | 2019-08-12 | 2064 | 2210 | 1935 | 2320 | 2020 | 1502 | 1807 | 1971 | 2253 | 1896 | 1707 | 1776 | 1733 | 1860 | 2100 | 1920 | 2188 | 2219 | 1841 |  |  |
| 21 | 2019-08-11 | 2186 | 2064 | 2210 | 1935 | 2320 | 2020 | 1502 | 1807 | 1971 | 2253 | 1896 | 1707 | 1776 | 1733 | 1860 | 2100 | 1920 | 2188 | 2219 | 1841 |  |
| 22 | 2019-08-10 | 2075 | 2186 | 2064 | 2210 | 1935 | 2320 | 2020 | 1502 | 1807 | 1971 | 2253 | 1896 | 1707 | 1776 | 1733 | 1860 | 2100 | 1920 | 2188 | 2219 | 1841 |
| 23 | 2019-08-09 | 2235 | 2075 | 2186 | 2064 | 2210 | 1935 | 2320 | 2020 | 1502 | 1807 | 1971 | 2253 | 1896 | 1707 | 1776 | 1733 | 1860 | 2100 | 1920 | 2188 | 2219 |
| 24 | 2019-08-08 | 2167 | 2235 | 2075 | 2186 | 2064 | 2210 | 1935 | 2320 | 2020 | 1502 | 1807 | 1971 | 2253 | 1896 | 1707 | 1776 | 1733 | 1860 | 2100 | 1920 | 2188 |
| 25 | 2019-08-07 | 1586 | 2167 | 2235 | 2075 | 2186 | 2064 | 2210 | 1935 | 2320 | 2020 | 1502 | 1807 | 1971 | 2253 | 1896 | 1707 | 1776 | 1733 | 1860 | 2100 | 1920 |
| 26 | 2019-08-06 | 2026 | 1586 | 2167 | 2235 | 2075 | 2186 | 2064 | 2210 | 1935 | 2320 | 2020 | 1502 | 1807 | 1971 | 2253 | 1896 | 1707 | 1776 | 1733 | 1860 | 2100 |
| 27 | 2019-08-05 | 1693 | 2026 | 1586 | 2167 | 2235 | 2075 | 2186 | 2064 | 2210 | 1935 | 2320 | 2020 | 1502 | 1807 | 1971 | 2253 | 1896 | 1707 | 1776 | 1733 | 1860 |
| 28 | 2019-08-04 | 2000 | 1693 | 2026 | 1586 | 2167 | 2235 | 2075 | 2186 | 2064 | 2210 | 1935 | 2320 | 2020 | 1502 | 1807 | 1971 | 2253 | 1896 | 1707 | 1776 | 1733 |
| 29 | 2019-08-03 | 1775 | 2000 | 1693 | 2026 | 1586 | 2167 | 2235 | 2075 | 2186 | 2064 | 2210 | 1935 | 2320 | 2020 | 1502 | 1807 | 1971 | 2253 | 1896 | 1707 | 1776 |
| 30 | 2019-08-02 | 1945 | 1775 | 2000 | 1693 | 2026 | 1586 | 2167 | 2235 | 2075 | 2186 | 2064 | 2210 | 1935 | 2320 | 2020 | 1502 | 1807 | 1971 | 2253 | 1896 | 1707 |
| 31 | 2019-08-01 | 1820 | 1945 | 1775 | 2000 | 1693 | 2026 | 1586 | 2167 | 2235 | 2075 | 2186 | 2064 | 2210 | 1935 | 2320 | 2020 | 1502 | 1807 | 1971 | 2253 | 1896 |
| 32 | 2019-07-31 | 1930 | 1820 | 1945 | 1775 | 2000 | 1693 | 2026 | 1586 | 2167 | 2235 | 2075 | 2186 | 2064 | 2210 | 1935 | 2320 | 2020 | 1502 | 1807 | 1971 | 2253 |
| 33 | 2019-07-30 | 1752 | 1930 | 1820 | 1945 | 1775 | 2000 | 1693 | 2026 | 1586 | 2167 | 2235 | 2075 | 2186 | 2064 | 2210 | 1935 | 2320 | 2020 | 1502 | 1807 | 1971 |
| 34 | 2019-07-29 | 1846 | 1752 | 1930 | 1820 | 1945 | 1775 | 2000 | 1693 | 2026 | 1586 | 2167 | 2235 | 2075 | 2186 | 2064 | 2210 | 1935 | 2320 | 2020 | 1502 | 1807 |
| 35 | 2019-07-28 | 2384 | 1846 | 1752 | 1930 | 1820 | 1945 | 1775 | 2000 | 1693 | 2026 | 1586 | 2167 | 2235 | 2075 | 2186 | 2064 | 2210 | 1935 | 2320 | 2020 | 1502 |
| 36 | 2019-07-27 | 1650 | 2384 | 1846 | 1752 | 1930 | 1820 | 1945 | 1775 | 2000 | 1693 | 2026 | 1586 | 2167 | 2235 | 2075 | 2186 | 2064 | 2210 | 1935 | 2320 | 2020 |
| 37 | 2019-07-26 | 1578 | 1650 | 2384 | 1846 | 1752 | 1930 | 1820 | 1945 | 1775 | 2000 | 1693 | 2026 | 1586 | 2167 | 2235 | 2075 | 2186 | 2064 | 2210 | 1935 | 2320 |
| 38 | 2019-07-25 | 2017 | 1578 | 1650 | 2384 | 1846 | 1752 | 1930 | 1820 | 1945 | 1775 | 2000 | 1693 | 2026 | 1586 | 2167 | 2235 | 2075 | 2186 | 2064 | 2210 | 1935 |
| 39 | 2019-07-24 | 2172 | 2017 | 1578 | 1650 | 2384 | 1846 | 1752 | 1930 | 1820 | 1945 | 1775 | 2000 | 1693 | 2026 | 1586 | 2167 | 2235 | 2075 | 2186 | 2064 | 2210 |
| 40 | 2019-07-23 | 2089 | 2172 | 2017 | 1578 | 1650 | 2384 | 1846 | 1752 | 1930 | 1820 | 1945 | 1775 | 2000 | 1693 | 2026 | 1586 | 2167 | 2235 | 2075 | 2186 | 2064 |
| 41 | 2019-07-22 | 2205 | 2089 | 2172 | 2017 | 1578 | 1650 | 2384 | 1846 | 1752 | 1930 | 1820 | 1945 | 1775 | 2000 | 1693 | 2026 | 1586 | 2167 | 2235 | 2075 | 2186 |
| 42 | 2019-07-21 | 2261 | 2205 | 2089 | 2172 | 2017 | 1578 | 1650 | 2384 | 1846 | 1752 | 1930 | 1820 | 1945 | 1775 | 2000 | 1693 | 2026 | 1586 | 2167 | 2235 | 2075 |
| 43 | 2019-07-20 | 1893 | 2261 | 2205 | 2089 | 2172 | 2017 | 1578 | 1650 | 2384 | 1846 | 1752 | 1930 | 1820 | 1945 | 1775 | 2000 | 1693 | 2026 | 1586 | 2167 | 2235 |
| 44 | 2019-07-19 | 1978 | 1893 | 2261 | 2205 | 2089 | 2172 | 2017 | 1578 | 1650 | 2384 | 1846 | 1752 | 1930 | 1820 | 1945 | 1775 | 2000 | 1693 | 2026 | 1586 | 2167 |
| 45 | 2019-07-18 | 1518 | 1978 | 1893 | 2261 | 2205 | 2089 | 2172 | 2017 | 1578 | 1650 | 2384 | 1846 | 1752 | 1930 | 1820 | 1945 | 1775 | 2000 | 1693 | 2026 | 1586 |
| 46 | 2019-07-17 | 2145 | 1518 | 1978 | 1893 | 2261 | 2205 | 2089 | 2172 | 2017 | 1578 | 1650 | 2384 | 1846 | 1752 | 1930 | 1820 | 1945 | 1775 | 2000 | 1693 | 2026 |
| 47 | 2019-07-16 | 1732 | 2145 | 1518 | 1978 | 1893 | 2261 | 2205 | 2089 | 2172 | 2017 | 1578 | 1650 | 2384 | 1846 | 1752 | 1930 | 1820 | 1945 | 1775 | 2000 | 1693 |
| 48 | 2019-07-15 | 2026 | 1732 | 2145 | 1518 | 1978 | 1893 | 2261 | 2205 | 2089 | 2172 | 2017 | 1578 | 1650 | 2384 | 1846 | 1752 | 1930 | 1820 | 1945 | 1775 | 2000 |
| 49 | 2019-07-14 | 31624 | 2026 | 1732 | 2145 | 1518 | 1978 | 1893 | 2261 | 2205 | 2089 | 2172 | 2017 | 1578 | 1650 | 2384 | 1846 | 1752 | 1930 | 1820 | 1945 | 1775 |
| 50 | 2019-07-13 | 1832 | 31624 | 2026 | 1732 | 2145 | 1518 | 1978 | 1893 | 2261 | 2205 | 2089 | 2172 | 2017 | 1578 | 1650 | 2384 | 1846 | 1752 | 1930 | 1820 | 1945 |
| 51 | 2019-07-12 | 2345 | 1832 | 31624 | 2026 | 1732 | 2145 | 1518 | 1978 | 1893 | 2261 | 2205 | 2089 | 2172 | 2017 | 1578 | 1650 | 2384 | 1846 | 1752 | 1930 | 1820 |
| 52 | 2019-07-11 | 1545 | 2345 | 1832 | 31624 | 2026 | 1732 | 2145 | 1518 | 1978 | 1893 | 2261 | 2205 | 2089 | 2172 | 2017 | 1578 | 1650 | 2384 | 1846 | 1752 | 1930 |
| 53 | 2019-07-10 | 1564 | 1545 | 2345 | 1832 | 31624 | 2026 | 1732 | 2145 | 1518 | 1978 | 1893 | 2261 | 2205 | 2089 | 2172 | 2017 | 1578 | 1650 | 2384 | 1846 | 1752 |
| 54 | 2019-07-09 | 2041 | 1564 | 1545 | 2345 | 1832 | 31624 | 2026 | 1732 | 2145 | 1518 | 1978 | 1893 | 2261 | 2205 | 2089 | 2172 | 2017 | 1578 | 1650 | 2384 | 1846 |
| 55 | 2019-07-08 | 1637 | 2041 | 1564 | 1545 | 2345 | 1832 | 31624 | 2026 | 1732 | 2145 | 1518 | 1978 | 1893 | 2261 | 2205 | 2089 | 2172 | 2017 | 1578 | 1650 | 2384 |
| 56 | 2019-07-07 | 2380 | 1637 | 2041 | 1564 | 1545 | 2345 | 1832 | 31624 | 2026 | 1732 | 2145 | 1518 | 1978 | 1893 | 2261 | 2205 | 2089 | 2172 | 2017 | 1578 | 1650 |
| 57 | 2019-07-06 | 1979 | 2380 | 1637 | 2041 | 1564 | 1545 | 2345 | 1832 | 31624 | 2026 | 1732 | 2145 | 1518 | 1978 | 1893 | 2261 | 2205 | 2089 | 2172 | 2017 | 1578 |
| 58 | 2019-07-05 | 1870 | 1979 | 2380 | 1637 | 2041 | 1564 | 1545 | 2345 | 1832 | 31624 | 2026 | 1732 | 2145 | 1518 | 1978 | 1893 | 2261 | 2205 | 2089 | 2172 | 2017 |
| 59 | 2019-07-04 | 1971 | 1870 | 1979 | 2380 | 1637 | 2041 | 1564 | 1545 | 2345 | 1832 | 31624 | 2026 | 1732 | 2145 | 1518 | 1978 | 1893 | 2261 | 2205 | 2089 | 2172 |
| 60 | 2019-07-03 | 1548 | 1971 | 1870 | 1979 | 2380 | 1637 | 2041 | 1564 | 1545 | 2345 | 1832 | 31624 | 2026 | 1732 | 2145 | 1518 | 1978 | 1893 | 2261 | 2205 | 2089 |

> **Hoja larga:** arriba se muestran 60 de 1944 filas con datos. **Todos los valores de la hoja están en [`tarea-class-example-1-datos/Ventas_propias.csv`](./tarea-class-example-1-datos/Ventas_propias.csv)** (CSV, UTF-8).

### Hoja `Coeficientes ventas propias` — 22 filas × 4 columnas

| Fila | A | B | C | D |
|---|---|---|---|---|
| 1 |  | Columna 1 | Lim Inf | Lim Sup |
| 2 | REZAGO | 1 |  |  |
| 3 | 1 | -0.000466399 | -0.0447231 | 0.0447348 |
| 4 | 2 | 0.00206497 | -0.0447231 | 0.0447231 |
| 5 | 3 | -0.00600842 | -0.0447233 | 0.0447233 |
| 6 | 4 | -0.0292024 | -0.0447249 | 0.0447249 |
| 7 | 5 | 0.00656572 | -0.044763 | 0.044763 |
| 8 | 6 | -0.0121249 | -0.044765 | 0.044765 |
| 9 | 7 | 0.0216974 | -0.0447715 | 0.0447715 |
| 10 | 8 | 0.0113151 | -0.0447926 | 0.0447926 |
| 11 | 9 | 0.0011257 | -0.0447983 | 0.0447983 |
| 12 | 10 | 0.00983445 | -0.0447983 | 0.0447983 |
| 13 | 11 | -0.00508523 | -0.0448027 | 0.0448027 |
| 14 | 12 | -0.0198538 | -0.0448038 | 0.0448038 |
| 15 | 13 | -0.00305243 | -0.0448214 | 0.0448214 |
| 16 | 14 | 0.00455089 | -0.0448218 | 0.0448218 |
| 17 | 15 | -0.00113847 | -0.0448227 | 0.0448227 |
| 18 | 16 | -0.00314348 | -0.0448228 | 0.0448228 |
| 19 | 17 | -0.0018041 | -0.0448232 | 0.0448232 |
| 20 | 18 | -0.000902116 | -0.0448234 | 0.0448234 |
| 21 | 19 | 0.000318792 | -0.0448234 | 0.0448234 |
| 22 | 20 | 0.00112178 | -0.0448234 | 0.0448234 |

**Fórmulas (4 patrones distintos):**

- `C3`: `=-TINV(0.05,COUNT('Ventas propias'!B2:B1924)-1)*(1/SQRT(COUNT('Ventas propias'!B2:B1924)))`
- `D3`: `=TINV(0.05,COUNT('Ventas propias'!C2:C1924)-1)*(1/SQRT(COUNT('Ventas propias'!C2:C1924)))`
- `C4`: `=-TINV(0.05,COUNT('Ventas propias'!$B$2:$B$1924)-1)*SQRT((1+2*SUMSQ($B$3:B3))/COUNT('Ventas propias'!$B$2:$B$1924))`
- `D4`: `=TINV(0.05,COUNT('Ventas propias'!$B$2:$B$1924)-1)*SQRT((1+2*SUMSQ($B$3:B3))/COUNT('Ventas propias'!$B$2:$B$1924))`

### Hoja `Serie de tiempo  ventas propias` — hoja de gráfico (sin celdas)

- Gráfico de líneas — título «(sin título)»
  - Series: 'Ventas propias'!$B$1: y = `'Ventas propias'!$B$2:$B$1944`

### Hoja `Histograma Ventas Propias` — hoja de gráfico (sin celdas)

- Gráfico de barras — título «(sin título)»

### Hoja `Autocorrelograma ventas propias` — hoja de gráfico (sin celdas)

- Gráfico de barras + líneas — título «Autocorrelograma de ventas propias»
  - Series: (serie): y = `'Coeficientes ventas propias'!$B$3:$B$22`; 'Coeficientes ventas propias'!$C$1: y = `'Coeficientes ventas propias'!$C$3:$C$22`; 'Coeficientes ventas propias'!$D$1: y = `'Coeficientes ventas propias'!$D$3:$D$22`

### Hoja `Boxplot Ventas Propias` — hoja de gráfico (sin celdas)

- Gráfico de barras — título «(sin título)»

### Hoja `Scatterplot Ventas Propias` — hoja de gráfico (sin celdas)

- Gráfico de dispersión — título «Scatterplot Ventas PropiasX(t) vs X(t-1)»
  - Series: 'Ventas propias'!$C$1: y = `'Ventas propias'!$C$2:$C$1924`, x = `'Ventas propias'!$B$2:$B$1924`

### Hoja `Ventas competencia` — 1944 filas × 22 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Fecha | Ventas propias | Rezago 1 | Rezago 2 | Rezago 3 | Rezago 4 | Rezago 5 | Rezago 6 | Rezago 7 | Rezago 8 | Rezago 9 | Rezago 10 | Rezago 11 | Rezago 12 | Rezago 13 | Rezago 14 | Rezago 15 | Rezago 16 | Rezago 17 | Rezago 18 | Rezago 19 | Rezago 20 |
| 2 | 2019-08-30 | 1113 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 | 2019-08-29 | 750 | 1113 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 | 2019-08-28 | 771 | 750 | 1113 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 | 2019-08-27 | 1050 | 771 | 750 | 1113 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 | 2019-08-26 | 862 | 1050 | 771 | 750 | 1113 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7 | 2019-08-25 | 1101 | 862 | 1050 | 771 | 750 | 1113 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 | 2019-08-24 | 1218 | 1101 | 862 | 1050 | 771 | 750 | 1113 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9 | 2019-08-23 | 1194 | 1218 | 1101 | 862 | 1050 | 771 | 750 | 1113 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10 | 2019-08-22 | 1257 | 1194 | 1218 | 1101 | 862 | 1050 | 771 | 750 | 1113 |  |  |  |  |  |  |  |  |  |  |  |  |
| 11 | 2019-08-21 | 1071 | 1257 | 1194 | 1218 | 1101 | 862 | 1050 | 771 | 750 | 1113 |  |  |  |  |  |  |  |  |  |  |  |
| 12 | 2019-08-20 | 710 | 1071 | 1257 | 1194 | 1218 | 1101 | 862 | 1050 | 771 | 750 | 1113 |  |  |  |  |  |  |  |  |  |  |
| 13 | 2019-08-19 | 987 | 710 | 1071 | 1257 | 1194 | 1218 | 1101 | 862 | 1050 | 771 | 750 | 1113 |  |  |  |  |  |  |  |  |  |
| 14 | 2019-08-18 | 1157 | 987 | 710 | 1071 | 1257 | 1194 | 1218 | 1101 | 862 | 1050 | 771 | 750 | 1113 |  |  |  |  |  |  |  |  |
| 15 | 2019-08-17 | 1460 | 1157 | 987 | 710 | 1071 | 1257 | 1194 | 1218 | 1101 | 862 | 1050 | 771 | 750 | 1113 |  |  |  |  |  |  |  |
| 16 | 2019-08-16 | 941 | 1460 | 1157 | 987 | 710 | 1071 | 1257 | 1194 | 1218 | 1101 | 862 | 1050 | 771 | 750 | 1113 |  |  |  |  |  |  |
| 17 | 2019-08-15 | 644 | 941 | 1460 | 1157 | 987 | 710 | 1071 | 1257 | 1194 | 1218 | 1101 | 862 | 1050 | 771 | 750 | 1113 |  |  |  |  |  |
| 18 | 2019-08-14 | 1029 | 644 | 941 | 1460 | 1157 | 987 | 710 | 1071 | 1257 | 1194 | 1218 | 1101 | 862 | 1050 | 771 | 750 | 1113 |  |  |  |  |
| 19 | 2019-08-13 | 744 | 1029 | 644 | 941 | 1460 | 1157 | 987 | 710 | 1071 | 1257 | 1194 | 1218 | 1101 | 862 | 1050 | 771 | 750 | 1113 |  |  |  |
| 20 | 2019-08-12 | 894 | 744 | 1029 | 644 | 941 | 1460 | 1157 | 987 | 710 | 1071 | 1257 | 1194 | 1218 | 1101 | 862 | 1050 | 771 | 750 | 1113 |  |  |
| 21 | 2019-08-11 | 764 | 894 | 744 | 1029 | 644 | 941 | 1460 | 1157 | 987 | 710 | 1071 | 1257 | 1194 | 1218 | 1101 | 862 | 1050 | 771 | 750 | 1113 |  |
| 22 | 2019-08-10 | 882 | 764 | 894 | 744 | 1029 | 644 | 941 | 1460 | 1157 | 987 | 710 | 1071 | 1257 | 1194 | 1218 | 1101 | 862 | 1050 | 771 | 750 | 1113 |
| 23 | 2019-08-09 | 721 | 882 | 764 | 894 | 744 | 1029 | 644 | 941 | 1460 | 1157 | 987 | 710 | 1071 | 1257 | 1194 | 1218 | 1101 | 862 | 1050 | 771 | 750 |
| 24 | 2019-08-08 | 790 | 721 | 882 | 764 | 894 | 744 | 1029 | 644 | 941 | 1460 | 1157 | 987 | 710 | 1071 | 1257 | 1194 | 1218 | 1101 | 862 | 1050 | 771 |
| 25 | 2019-08-07 | 1382 | 790 | 721 | 882 | 764 | 894 | 744 | 1029 | 644 | 941 | 1460 | 1157 | 987 | 710 | 1071 | 1257 | 1194 | 1218 | 1101 | 862 | 1050 |
| 26 | 2019-08-06 | 941 | 1382 | 790 | 721 | 882 | 764 | 894 | 744 | 1029 | 644 | 941 | 1460 | 1157 | 987 | 710 | 1071 | 1257 | 1194 | 1218 | 1101 | 862 |
| 27 | 2019-08-05 | 1257 | 941 | 1382 | 790 | 721 | 882 | 764 | 894 | 744 | 1029 | 644 | 941 | 1460 | 1157 | 987 | 710 | 1071 | 1257 | 1194 | 1218 | 1101 |
| 28 | 2019-08-04 | 955 | 1257 | 941 | 1382 | 790 | 721 | 882 | 764 | 894 | 744 | 1029 | 644 | 941 | 1460 | 1157 | 987 | 710 | 1071 | 1257 | 1194 | 1218 |
| 29 | 2019-08-03 | 1187 | 955 | 1257 | 941 | 1382 | 790 | 721 | 882 | 764 | 894 | 744 | 1029 | 644 | 941 | 1460 | 1157 | 987 | 710 | 1071 | 1257 | 1194 |
| 30 | 2019-08-02 | 1006 | 1187 | 955 | 1257 | 941 | 1382 | 790 | 721 | 882 | 764 | 894 | 744 | 1029 | 644 | 941 | 1460 | 1157 | 987 | 710 | 1071 | 1257 |
| 31 | 2019-08-01 | 1140 | 1006 | 1187 | 955 | 1257 | 941 | 1382 | 790 | 721 | 882 | 764 | 894 | 744 | 1029 | 644 | 941 | 1460 | 1157 | 987 | 710 | 1071 |
| 32 | 2019-07-31 | 1030 | 1140 | 1006 | 1187 | 955 | 1257 | 941 | 1382 | 790 | 721 | 882 | 764 | 894 | 744 | 1029 | 644 | 941 | 1460 | 1157 | 987 | 710 |
| 33 | 2019-07-30 | 1206 | 1030 | 1140 | 1006 | 1187 | 955 | 1257 | 941 | 1382 | 790 | 721 | 882 | 764 | 894 | 744 | 1029 | 644 | 941 | 1460 | 1157 | 987 |
| 34 | 2019-07-29 | 1111 | 1206 | 1030 | 1140 | 1006 | 1187 | 955 | 1257 | 941 | 1382 | 790 | 721 | 882 | 764 | 894 | 744 | 1029 | 644 | 941 | 1460 | 1157 |
| 35 | 2019-07-28 | 583 | 1111 | 1206 | 1030 | 1140 | 1006 | 1187 | 955 | 1257 | 941 | 1382 | 790 | 721 | 882 | 764 | 894 | 744 | 1029 | 644 | 941 | 1460 |
| 36 | 2019-07-27 | 1311 | 583 | 1111 | 1206 | 1030 | 1140 | 1006 | 1187 | 955 | 1257 | 941 | 1382 | 790 | 721 | 882 | 764 | 894 | 744 | 1029 | 644 | 941 |
| 37 | 2019-07-26 | 1384 | 1311 | 583 | 1111 | 1206 | 1030 | 1140 | 1006 | 1187 | 955 | 1257 | 941 | 1382 | 790 | 721 | 882 | 764 | 894 | 744 | 1029 | 644 |
| 38 | 2019-07-25 | 944 | 1384 | 1311 | 583 | 1111 | 1206 | 1030 | 1140 | 1006 | 1187 | 955 | 1257 | 941 | 1382 | 790 | 721 | 882 | 764 | 894 | 744 | 1029 |
| 39 | 2019-07-24 | 784 | 944 | 1384 | 1311 | 583 | 1111 | 1206 | 1030 | 1140 | 1006 | 1187 | 955 | 1257 | 941 | 1382 | 790 | 721 | 882 | 764 | 894 | 744 |
| 40 | 2019-07-23 | 867 | 784 | 944 | 1384 | 1311 | 583 | 1111 | 1206 | 1030 | 1140 | 1006 | 1187 | 955 | 1257 | 941 | 1382 | 790 | 721 | 882 | 764 | 894 |
| 41 | 2019-07-22 | 750 | 867 | 784 | 944 | 1384 | 1311 | 583 | 1111 | 1206 | 1030 | 1140 | 1006 | 1187 | 955 | 1257 | 941 | 1382 | 790 | 721 | 882 | 764 |
| 42 | 2019-07-21 | 703 | 750 | 867 | 784 | 944 | 1384 | 1311 | 583 | 1111 | 1206 | 1030 | 1140 | 1006 | 1187 | 955 | 1257 | 941 | 1382 | 790 | 721 | 882 |
| 43 | 2019-07-20 | 1066 | 703 | 750 | 867 | 784 | 944 | 1384 | 1311 | 583 | 1111 | 1206 | 1030 | 1140 | 1006 | 1187 | 955 | 1257 | 941 | 1382 | 790 | 721 |
| 44 | 2019-07-19 | 985 | 1066 | 703 | 750 | 867 | 784 | 944 | 1384 | 1311 | 583 | 1111 | 1206 | 1030 | 1140 | 1006 | 1187 | 955 | 1257 | 941 | 1382 | 790 |
| 45 | 2019-07-18 | 1442 | 985 | 1066 | 703 | 750 | 867 | 784 | 944 | 1384 | 1311 | 583 | 1111 | 1206 | 1030 | 1140 | 1006 | 1187 | 955 | 1257 | 941 | 1382 |
| 46 | 2019-07-17 | 810 | 1442 | 985 | 1066 | 703 | 750 | 867 | 784 | 944 | 1384 | 1311 | 583 | 1111 | 1206 | 1030 | 1140 | 1006 | 1187 | 955 | 1257 | 941 |
| 47 | 2019-07-16 | 1222 | 810 | 1442 | 985 | 1066 | 703 | 750 | 867 | 784 | 944 | 1384 | 1311 | 583 | 1111 | 1206 | 1030 | 1140 | 1006 | 1187 | 955 | 1257 |
| 48 | 2019-07-15 | 940 | 1222 | 810 | 1442 | 985 | 1066 | 703 | 750 | 867 | 784 | 944 | 1384 | 1311 | 583 | 1111 | 1206 | 1030 | 1140 | 1006 | 1187 | 955 |
| 49 | 2019-07-14 | 1331 | 940 | 1222 | 810 | 1442 | 985 | 1066 | 703 | 750 | 867 | 784 | 944 | 1384 | 1311 | 583 | 1111 | 1206 | 1030 | 1140 | 1006 | 1187 |
| 50 | 2019-07-13 | 1137 | 1331 | 940 | 1222 | 810 | 1442 | 985 | 1066 | 703 | 750 | 867 | 784 | 944 | 1384 | 1311 | 583 | 1111 | 1206 | 1030 | 1140 | 1006 |
| 51 | 2019-07-12 | 608 | 1137 | 1331 | 940 | 1222 | 810 | 1442 | 985 | 1066 | 703 | 750 | 867 | 784 | 944 | 1384 | 1311 | 583 | 1111 | 1206 | 1030 | 1140 |
| 52 | 2019-07-11 | 1412 | 608 | 1137 | 1331 | 940 | 1222 | 810 | 1442 | 985 | 1066 | 703 | 750 | 867 | 784 | 944 | 1384 | 1311 | 583 | 1111 | 1206 | 1030 |
| 53 | 2019-07-10 | 1399 | 1412 | 608 | 1137 | 1331 | 940 | 1222 | 810 | 1442 | 985 | 1066 | 703 | 750 | 867 | 784 | 944 | 1384 | 1311 | 583 | 1111 | 1206 |
| 54 | 2019-07-09 | 922 | 1399 | 1412 | 608 | 1137 | 1331 | 940 | 1222 | 810 | 1442 | 985 | 1066 | 703 | 750 | 867 | 784 | 944 | 1384 | 1311 | 583 | 1111 |
| 55 | 2019-07-08 | 1315 | 922 | 1399 | 1412 | 608 | 1137 | 1331 | 940 | 1222 | 810 | 1442 | 985 | 1066 | 703 | 750 | 867 | 784 | 944 | 1384 | 1311 | 583 |
| 56 | 2019-07-07 | 575 | 1315 | 922 | 1399 | 1412 | 608 | 1137 | 1331 | 940 | 1222 | 810 | 1442 | 985 | 1066 | 703 | 750 | 867 | 784 | 944 | 1384 | 1311 |
| 57 | 2019-07-06 | 977 | 575 | 1315 | 922 | 1399 | 1412 | 608 | 1137 | 1331 | 940 | 1222 | 810 | 1442 | 985 | 1066 | 703 | 750 | 867 | 784 | 944 | 1384 |
| 58 | 2019-07-05 | 1087 | 977 | 575 | 1315 | 922 | 1399 | 1412 | 608 | 1137 | 1331 | 940 | 1222 | 810 | 1442 | 985 | 1066 | 703 | 750 | 867 | 784 | 944 |
| 59 | 2019-07-04 | 995 | 1087 | 977 | 575 | 1315 | 922 | 1399 | 1412 | 608 | 1137 | 1331 | 940 | 1222 | 810 | 1442 | 985 | 1066 | 703 | 750 | 867 | 784 |
| 60 | 2019-07-03 | 1408 | 995 | 1087 | 977 | 575 | 1315 | 922 | 1399 | 1412 | 608 | 1137 | 1331 | 940 | 1222 | 810 | 1442 | 985 | 1066 | 703 | 750 | 867 |

> **Hoja larga:** arriba se muestran 60 de 1944 filas con datos. **Todos los valores de la hoja están en [`tarea-class-example-1-datos/Ventas_competencia.csv`](./tarea-class-example-1-datos/Ventas_competencia.csv)** (CSV, UTF-8).

### Hoja `Coeficientes ventas competencia` — 22 filas × 4 columnas

| Fila | A | B | C | D |
|---|---|---|---|---|
| 1 |  | Columna 1 | Limite inf | Limite sup |
| 2 | REZAGO | 1 | -0.0447231 | 0.0447231 |
| 3 | 1 | 0.0192309 | -0.0447396 | 0.0447396 |
| 4 | 2 | -0.0222436 | -0.0447618 | 0.0447618 |
| 5 | 3 | -0.00145145 | -0.0447619 | 0.0447619 |
| 6 | 4 | -0.0459283 | -0.044856 | 0.044856 |
| 7 | 5 | 0.0203058 | -0.0448744 | 0.0448744 |
| 8 | 6 | -0.0164776 | -0.0448865 | 0.0448865 |
| 9 | 7 | -0.00915642 | -0.0448902 | 0.0448902 |
| 10 | 8 | 0.0192009 | -0.0449067 | 0.0449067 |
| 11 | 9 | 0.00275363 | -0.044907 | 0.044907 |
| 12 | 10 | 0.0278658 | -0.0449416 | 0.0449416 |
| 13 | 11 | 0.0189656 | -0.0449576 | 0.0449576 |
| 14 | 12 | -0.00796532 | -0.0449604 | 0.0449604 |
| 15 | 13 | -0.0147826 | -0.0449701 | 0.0449701 |
| 16 | 14 | -0.0272593 | -0.0450032 | 0.0450032 |
| 17 | 15 | -0.0127668 | -0.0450104 | 0.0450104 |
| 18 | 16 | 0.00104184 | -0.0450104 | 0.0450104 |
| 19 | 17 | 0.0158827 | -0.0450217 | 0.0450217 |
| 20 | 18 | 0.0143576 | -0.0450308 | 0.0450308 |
| 21 | 19 | 0.0385564 | -0.0450968 | 0.0450968 |
| 22 | 20 | 0.00148077 | -0.0450969 | 0.0450969 |

**Fórmulas (6 patrones distintos):**

- `C2`: `=-TINV(0.05,COUNT('Ventas competencia'!$B$2:$B$1924)-1)*(1/SQRT(COUNT('Ventas competencia'!$B$2:$B$1924)))`
- `D2`: `=TINV(0.05,COUNT('Ventas competencia'!$B$2:$B$1924)-1)*(1/SQRT(COUNT('Ventas competencia'!$B$2:$B$1924)))`
- `C3`: `=-TINV(0.05,COUNT('Ventas competencia'!$B$2:$B$1924)-1)*SQRT((1+2*SUMSQ($B3:B$3))/COUNT('Ventas competencia'!$B$2:$B$1924))`
- `D3`: `=TINV(0.05,COUNT('Ventas competencia'!$B$2:$B$1924)-1)*SQRT((1+2*SUMSQ($B3:B$3))/COUNT('Ventas competencia'!$B$2:$B$1924))`
- `C4`: `=-TINV(0.05,COUNT('Ventas competencia'!$B$2:$B$1924)-1)*SQRT((1+2*SUMSQ($B$3:B4))/COUNT('Ventas competencia'!$B$2:$B$1924))`
- `D4`: `=TINV(0.05,COUNT('Ventas competencia'!$B$2:$B$1924)-1)*SQRT((1+2*SUMSQ($B$3:B4))/COUNT('Ventas competencia'!$B$2:$B$1924))`

### Hoja `Serie de tiempo Ventas Comp` — hoja de gráfico (sin celdas)

- Gráfico de líneas — título «Serie de tiempo Ventas Competencia»
  - Series: 'Ventas competencia'!$B$1: y = `'Ventas competencia'!$B$2:$B$1944`

### Hoja `Histograma Ventas Competencia` — hoja de gráfico (sin celdas)

- Gráfico de barras — título «(sin título)»

### Hoja `Autocorrelograma Ventas Compete` — hoja de gráfico (sin celdas)

- Gráfico de barras + líneas — título «Autocorrelograma Ventas Competencia»
  - Series: (serie): y = `'Coeficientes ventas competencia'!$B$3:$B$22`; 'Coeficientes ventas competencia'!$C$1: y = `'Coeficientes ventas competencia'!$C$2:$C$22`; 'Coeficientes ventas competencia'!$D$1: y = `'Coeficientes ventas competencia'!$D$2:$D$22`

### Hoja `Boxplot Ventas Competencia` — hoja de gráfico (sin celdas)

- Gráfico de barras — título «(sin título)»

### Hoja `Scatterplot Ventas Competencia` — hoja de gráfico (sin celdas)

- Gráfico de dispersión — título «Scatterplot Ventas CompetenciaX(t) vs X(t-1)»
  - Series: 'Ventas competencia'!$C$1: y = `'Ventas competencia'!$C$2:$C$1924`, x = `'Ventas competencia'!$B$2:$B$1924`

