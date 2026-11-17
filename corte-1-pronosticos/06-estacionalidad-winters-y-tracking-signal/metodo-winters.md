# metodo-winters

> **Archivo:** [`metodo-winters.xlsx`](./metodo-winters.xlsx) · **Corte 1** · Libro de Excel con 4 hoja(s): `INTERCEPTO`, `DATOS PARA WINTERS`, `FATOS PARA CORRELOGRAMA`, `CORRELOGRAMA`  
> **Nombre original:** `CORTE 1/METODO WINTERS.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Libro con 4 hojas que resuelve el **ejemplo numérico del método de Winters multiplicativo** de la clase 7 (ventas mensuales de llantas para nieve durante 2 años; páginas 16–20 de [`L07-forecasting-seasonality-and-tracking-signal.md`](./L07-forecasting-seasonality-and-tracking-signal.md)). Hace tres cosas:

- `INTERCEPTO` muestra qué pasa si se ajusta una sola recta de regresión a los 24 meses.
- `DATOS PARA WINTERS` inicializa Winters con el método de los dos ciclos, calcula y normaliza los factores estacionales, pronostica los meses 25–36 y mide el error *a posteriori* sobre los datos históricos.
- `FATOS PARA CORRELOGRAMA` y `CORRELOGRAMA` calculan la función de autocorrelación (FAC) de la demanda, que confirma la estacionalidad de 12 meses.

Con él se aprende a inicializar Winters, a construir los índices estacionales y a justificar el método con el correlograma.

**Datos comunes (24 meses, enero del año 1 a diciembre del año 2):**

| Mes | Año 1 (t = 1–12) | Año 2 (t = 13–24) |
|---|---|---|
| enero | 195 | 229 |
| febrero | 252 | 271 |
| marzo | 299 | 333 |
| abril | 276 | 305 |
| mayo | 258 | 277 |
| junio | 210 | 239 |
| julio | 192 | 211 |
| agosto | 154 | 193 |
| septiembre | 141 | 155 |
| octubre | 128 | 159 |
| noviembre | 200 | **208** |
| diciembre | 217 | 236 |
| **Total** | 2522 | 2816 |

Media de los 24 meses: 222,417. Mínimo 128 (octubre, año 1); máximo 333 (marzo, año 2).

### Hoja `INTERCEPTO`

**Objetivo (deducido):** ajustar una recta de tendencia a los 24 meses y quitarle la tendencia a la demanda, para ver la componente estacional.

**Método:**
- Intercepto (J2): $a=$ `INTERCEPT(C2:C25,B2:B25)` $=231{,}319$.
- Pendiente (J3): $b=$ `SLOPE(C2:C25,B2:B25)` $=-0{,}712174$.
- Tendencia (columna D): $T_t=a+bt$ (`=$J$2+$J$3*B2`).
- Demanda sin tendencia (columna E): $D_t-T_t$ (`=C2-D2`).

**Resultados (extracto):** la tendencia baja de 230,607 ($t=1$) a 214,227 ($t=24$). La demanda sin tendencia va de −96,20 (octubre, año 1) a +112,36 (marzo, año 2) y repite el mismo patrón en ambos años: positiva de febrero a mayo y negativa de julio a noviembre.

**Gráficos:**
- En G5, una línea con la serie E2:E26, demanda sin tendencia; muestra dos ciclos casi idénticos.
- En G20, líneas con la demanda C2:C25 y la tendencia D2:D26; la recta es levemente decreciente.

**Conclusión:** la regresión sobre los 24 meses da una pendiente **negativa** (−0,71), aunque el año 2 vende más que el año 1 (promedio 234,7 frente a 210,2). La razón es que dentro de cada año la demanda es alta al inicio y baja al final, y ese patrón estacional distorsiona la recta. Por eso Winters no se inicializa con esta regresión sino con los promedios de cada ciclo (hoja siguiente), que dan una pendiente de +2,04.

### Hoja `DATOS PARA WINTERS`

**Objetivo:** inicializar Winters multiplicativo con $N=12$, obtener los 12 factores estacionales normalizados, pronosticar el año 3 (t = 25–36) y medir el error de ajuste en los años 1 y 2.

**Datos de entrada:** C2:C13 = ciclo 1 (año 1), D2:D13 = ciclo 2 (año 2), B2:B13 = mes 1–12.

**Inicialización (método de los dos ciclos de L07, p. 14):**

| Concepto | Celda | Fórmula Excel | Fórmula | Valor |
|---|---|---|---|---|
| $\bar S_1$ (S_BARRA ciclo 1) | C16 | `=AVERAGE(C2:C13)` | $\bar S_1=\frac{1}{12}\sum_{t=1}^{12}x_t$ | 210,167 |
| $\bar S_2$ (S_BARRA ciclo 2) | D16 | `=AVERAGE(D2:D13)` | $\bar S_2=\frac{1}{12}\sum_{t=13}^{24}x_t$ | 234,667 |
| Pendiente $a_1$ (A1) | C17 | `=(D16-C16)/12` | $a_1=(\bar S_2-\bar S_1)/N$ | 2,04167 |
| Nivel $a_{0,2N}$ («proyectarla primer punto») | C18 | `=D16+C17*11/2` | $a_{0,24}=\bar S_2+a_1\frac{N-1}{2}$ | 245,896 |
| Intercepto original $a_0$ | C19 | `=C18-(2*12)*C17` | $a_0=a_{0,24}-2N\,a_1$ | 196,896 |

**Factores estacionales:**
- Columna F, año 1 (`=C2/($C$19+$C$17*B2)`): $C_t=\dfrac{x_t}{a_0+a_1t}$ para $t=1..12$.
- Columna G, año 2 (`=D2/($C$19+$C$17*(B2+12))`): lo mismo para $t=13..24$.
- Columna H: promedio de los dos años, $\bar C_j=(C_j+C_{j+12})/2$.
- Columna I, normalizado (`=12*H2/SUM($H$2:$H$13)`): $C_j^{norm}=N\,\bar C_j/\sum_k\bar C_k$. La suma de los $\bar C$ es 12,0658 y la de los normalizados es exactamente 12.

**Pronóstico (columna L, `=($C$19+$C$17*K2)*I2`):** $F_t=(a_0+a_1t)\,C^{norm}_{t-24}$ para $t=25..36$ (columna K). Equivale a $(a_{0,24}+\tau a_1)\,C_{24+\tau-N}$ con $\tau=t-24$, como en L07.

**Error *a posteriori*** (ajuste sobre los datos históricos con los mismos factores):
- Ciclo 1: $\hat x_t=(a_0+a_1t)C^{norm}_t$ (columna O, $t=1..12$ en N) y error absoluto $|\hat x_t-x_t|$ (columna P).
- Ciclo 2: igual con $t=13..24$ (columna S, $t$ en R) y error en la columna T.

**Resultados:**

| Mes | $C_t$ año 1 | $C_t$ año 2 | Promedio | Normalizado | t | Pronóstico $F_t$ | Ajuste año 1 | \|e\| año 1 | Ajuste año 2 | \|e\| año 2 |
|---|---|---|---|---|---|---|---|---|---|---|
| enero | 0,9802 | 1,0249 | 1,0026 | 0,9971 | 25 | 247,21 | 198,36 | 3,36 | 222,79 | 6,21 |
| febrero | 1,2539 | 1,2019 | 1,2279 | 1,2212 | 26 | 305,27 | 245,43 | 6,57 | 275,35 | 4,35 |
| marzo | 1,4728 | 1,4636 | 1,4682 | 1,4602 | 27 | 367,99 | 296,45 | 2,55 | 332,22 | 0,78 |
| abril | 1,3459 | 1,3286 | 1,3373 | 1,3300 | 28 | 337,90 | 272,73 | 3,27 | 305,31 | 0,31 |
| mayo | 1,2458 | 1,1960 | 1,2209 | 1,2142 | 29 | 310,97 | 251,47 | 6,53 | 281,22 | 4,22 |
| junio | 1,0041 | 1,0229 | 1,0135 | 1,0080 | 30 | 260,20 | 210,81 | 0,81 | 235,51 | 3,49 |
| julio | 0,9091 | 0,8953 | 0,9022 | 0,8973 | 31 | 233,46 | 189,49 | 2,51 | 211,48 | 0,48 |
| agosto | 0,7222 | 0,8118 | 0,7670 | 0,7629 | 32 | 200,04 | 162,66 | 8,66 | 181,35 | 11,65 |
| septiembre | 0,6550 | 0,6465 | 0,6507 | 0,6472 | 33 | 171,03 | 139,32 | 1,68 | 155,17 | 0,17 |
| octubre | 0,5890 | 0,6575 | 0,6233 | 0,6199 | 34 | 165,08 | 134,71 | 6,71 | 149,89 | 9,11 |
| noviembre | 0,9118 | 0,8530 | 0,8824 | 0,8776 | 35 | 235,50 | 192,50 | 7,50 | 214,00 | 6,00 |
| diciembre | 0,9801 | 0,9598 | 0,9700 | 0,9647 | 36 | 260,84 | 213,57 | 3,43 | 237,21 | 1,21 |

- MAD (P16, `=AVERAGE(P2:P13,U2:U13)`): **4,46552**. Solo promedia el ciclo 1; ver **Observaciones**.
- Total pronosticado para el año 3: 3.095,5 unidades.
- MAPE (O17): rótulo sin valor.

**Gráficos:**
- «3 CICLOS» (en F14): tres líneas de 12 meses, ciclo 1 (C2:C13), ciclo 2 (D2:D13) y pronóstico Winters (L2:L13). Los tres tienen la misma forma (pico en marzo, valle en octubre), cada año por encima del anterior.
- Sin título (en J14): una sola serie «DEMANDA + PROYECCION», que encadena C2:C13, D2:D13 y L2:L13 (36 meses). Muestra los dos años reales y el año pronosticado como una serie continua con tendencia creciente y ciclo anual.

**Conclusión:** los factores normalizados coinciden con los de la clase (1,00; 1,22; 1,46; 1,33; 1,21; 1,01; 0,90; 0,76; 0,65; 0,62; 0,88; 0,96). Los pronósticos de enero a marzo del año 3 (247,21; 305,27; 367,99) son casi iguales a los de la diapositiva (247,64; 305,21; 368,25); la diferencia viene de redondeos y del dato de noviembre. El ajuste histórico es muy bueno: el error medio es de unas 4 unidades, alrededor del 2 % de la demanda. Este Excel solo hace la **inicialización y el pronóstico estático**: no aplica las ecuaciones de actualización con $\alpha$, $\phi$ y $\gamma$ (p. 21–22 de L07).

### Hoja `FATOS PARA CORRELOGRAMA`

**Objetivo:** preparar la serie desplazada para calcular autocorrelaciones.

**Contenido:** columna A = mes, B = demanda (24 datos, B2:B25), y C a U = rezagos 1 a 19. La columna del rezago $k$ es la demanda desplazada $k$ filas hacia abajo, de modo que en la fila $t$ queda $x_{t-k}$. Son valores pegados, sin fórmulas, y la tabla se extiende hasta la fila 44 para que quepan todos los desplazamientos. El nombre de la hoja tiene un error de tipeo: «FATOS» por «DATOS».

### Hoja `CORRELOGRAMA`

**Objetivo:** calcular y graficar la FAC de la demanda para 19 rezagos, con límites de significancia al 95 %.

**Parámetros y método:**
- $n$ (B3) = `COUNT` de la demanda = 24.
- Media $\bar x$ (B4) = 222,417.
- $z$ (B5) = 1,96.
- Límite crítico (B6) = $z/\sqrt n=1{,}96/\sqrt{24}=0{,}400083$.
- FAC (B9:B27), con una fórmula matricial `SUMPRODUCT(OFFSET(...)-media)*(OFFSET(...)-media)/DEVSQ(...)`:

$$r_k=\frac{\sum_{t=k+1}^{n}(x_t-\bar x)(x_{t-k}-\bar x)}{\sum_{t=1}^{n}(x_t-\bar x)^2}$$

- Límites (columnas C y D): $\pm0{,}400083$.
- «Significativo» (columna E): «Sí» si $|r_k|>0{,}400083$.

**Resultados:**

| k | $r_k$ | ¿Significativo? | k | $r_k$ | ¿Significativo? |
|---|---|---|---|---|---|
| 1 | 0,76773 | Sí | 11 | 0,33579 | No |
| 2 | 0,38098 | No | 12 | 0,43996 | Sí |
| 3 | −0,00424 | No | 13 | 0,34712 | No |
| 4 | −0,34573 | No | 14 | 0,15735 | No |
| 5 | −0,63403 | Sí | 15 | 0,02361 | No |
| 6 | −0,72823 | Sí | 16 | −0,08160 | No |
| 7 | −0,60771 | Sí | 17 | −0,13429 | No |
| 8 | −0,31622 | No | 18 | −0,14385 | No |
| 9 | −0,04243 | No | 19 | −0,09297 | No |
| 10 | 0,14390 | No | | | |

Valores verificados con un cálculo independiente.

**Gráfico:** «Correlograma de la demanda (FAC) - 19 rezagos». Barras de $r_k$ contra el rezago $k$ (eje x «Rezago (k)», eje y «Autocorrelación»), con dos líneas horizontales en $\pm0{,}400$ (límites superior e inferior). Las barras dibujan una onda: positiva en $k=1$, mínimo en $k=6$ y de nuevo positiva en $k=12$.

**Interpretación escrita en la hoja (A30:A32):**
- «r1=0,77 positivo, mínimo en r6=-0,73 y repunte en r12=0,44: onda completa de 12 meses → estacionalidad anual con tendencia (adecuado para Winters).»
- «Barras que superan las líneas rojas (±1,96/√n = ±0,400) = autocorrelación significativa al 95%.»
- «Cautela: con n=24, los rezagos altos usan pocas parejas (k=19 solo 5), por lo que r_k a partir de ~k=12 es poco confiable. Regla práctica: k ≤ n/4.»

### Observaciones

- **MAD incompleto (P16).** La fórmula `=AVERAGE(P2:P13,U2:U13)` toma la columna U, que está vacía, en lugar de la T, donde están los errores del ciclo 2. Por eso el MAD de 4,4655 corresponde solo al año 1. Cálculo propio: el MAD del año 2 es 3,998, el MAD de los 24 meses es **4,232** y el MAPE de los 24 meses es ≈ 2,13 %. El MAPE de la celda O17 quedó sin calcular.
- **Dato distinto al de la clase.** Noviembre del año 2 vale 208 en el Excel y 209 en la diapositiva (total 2817 en L07). Por eso $\bar S_2=234{,}667$ (clase: 234,75), $a_1=2{,}0417$ (clase: 2,049), $a_{0,24}=245{,}896$ (clase: 246,08) y $a_0=196{,}896$ (clase: 196,88).
- El Excel usa correctamente $\bar S_1=210{,}167$; la diapositiva escribe 201,16 por error de tipeo.
- **Sin parámetros de suavización.** No hay $\alpha$, $\phi$ ni $\gamma$. El «pronóstico Winters» es el pronóstico estático desde la inicialización y no se actualiza con datos nuevos.
- **Rangos de los gráficos de `INTERCEPTO`.** Llegan hasta la fila 26 (E2:E26, D2:D26), una fila más que los datos (fila 25). La fila 26 está vacía y no afecta.
- **Orden de las series del gráfico «3 CICLOS».** Es ciclo 2, pronóstico y ciclo 1, en ese orden.
- La hoja `INTERCEPTO` muestra que una regresión lineal simple sobre datos estacionales puede dar una pendiente con el signo equivocado (−0,71 frente a +2,04).

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `INTERCEPTO` — 44 filas × 25 columnas · 2 gráfico(s)

**Gráficos en esta hoja:**

- Gráfico de líneas — título «(sin título)»
  - Series: INTERCEPTO!$E$1: y = `INTERCEPTO!$E$2:$E$26`
- Gráfico de líneas — título «(sin título)»
  - Series: INTERCEPTO!$C$1: y = `INTERCEPTO!$C$2:$C$25`; INTERCEPTO!$D$1: y = `INTERCEPTO!$D$2:$D$26`

| Fila | A | B | C | D | E | F | G | H | I | J |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | MES |  | DEMANDA | TENDENCIA | DEMANDA SIN TENDECIA |  |  |  |  |  |
| 2 | enero | 1 | 195 | 230.607 | -35.6067 |  |  |  | intercepto | 231.319 |
| 3 | febrero | 2 | 252 | 229.894 | 22.1055 |  |  |  | pendiente | -0.712174 |
| 4 | marzo | 3 | 299 | 229.182 | 69.8177 |  |  |  |  |  |
| 5 | abril | 4 | 276 | 228.47 | 47.5299 |  |  |  |  |  |
| 6 | mayo | 5 | 258 | 227.758 | 30.242 |  |  |  |  |  |
| 7 | junio | 6 | 210 | 227.046 | -17.0458 |  |  |  |  |  |
| 8 | julio | 7 | 192 | 226.334 | -34.3336 |  |  |  |  |  |
| 9 | agosto | 8 | 154 | 225.621 | -71.6214 |  |  |  |  |  |
| 10 | septiembre | 9 | 141 | 224.909 | -83.9093 |  |  |  |  |  |
| 11 | octubre | 10 | 128 | 224.197 | -96.1971 |  |  |  |  |  |
| 12 | noviembre | 11 | 200 | 223.485 | -23.4849 |  |  |  |  |  |
| 13 | diciembre | 12 | 217 | 222.773 | -5.77275 |  |  |  |  |  |
| 14 | enero | 13 | 229 | 222.061 | 6.93942 |  |  |  |  |  |
| 15 | febrero | 14 | 271 | 221.348 | 49.6516 |  |  |  |  |  |
| 16 | marzo | 15 | 333 | 220.636 | 112.364 |  |  |  |  |  |
| 17 | abril | 16 | 305 | 219.924 | 85.0759 |  |  |  |  |  |
| 18 | mayo | 17 | 277 | 219.212 | 57.7881 |  |  |  |  |  |
| 19 | junio | 18 | 239 | 218.5 | 20.5003 |  |  |  |  |  |
| 20 | julio | 19 | 211 | 217.788 | -6.78754 |  |  |  |  |  |
| 21 | agosto | 20 | 193 | 217.075 | -24.0754 |  |  |  |  |  |
| 22 | septiembre | 21 | 155 | 216.363 | -61.3632 |  |  |  |  |  |
| 23 | octubre | 22 | 159 | 215.651 | -56.651 |  |  |  |  |  |
| 24 | noviembre | 23 | 208 | 214.939 | -6.93884 |  |  |  |  |  |
| 25 | diciembre | 24 | 236 | 214.227 | 21.7733 |  |  |  |  |  |

**Fórmulas (4 patrones distintos):**

- `D2`: `=$J$2+$J$3*B2`
- `E2`: `=C2-D2`
- `J2`: `=INTERCEPT(C2:C25,B2:B25)`
- `J3`: `=SLOPE(C2:C25,B2:B25)`

### Hoja `DATOS PARA WINTERS` — 25 filas × 20 columnas · 2 gráfico(s)

**Gráficos en esta hoja:**

- Gráfico de líneas — título «3 CICLOS»
  - Series: 'DATOS PARA WINTERS'!$D$1: y = `'DATOS PARA WINTERS'!$D$2:$D$13`; 'DATOS PARA WINTERS'!$L$1: y = `'DATOS PARA WINTERS'!$L$2:$L$13`; 'DATOS PARA WINTERS'!$C$1: y = `'DATOS PARA WINTERS'!$C$2:$C$13`
- Gráfico de líneas — título «(sin título)»
  - Series: "DEMANDA + PROYECCION": y = `('DATOS PARA WINTERS'!$C$2:$C$13,'DATOS PARA WINTERS'!$D$2:$D$13,'DATOS PARA WINTERS'!$L$2:$L$13)`

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | MES |  | CICLO 1 | CICLO 2 |  | COEFICIENTES AÑO 1 | COEFICIENTES AÑO 2 | COEFICIENTE PROMEDIO | COEFICIENTE NORMALIZADO |  | PRONOSTICO (t) | PRONOSTICO WINTERS F(t) |  | PRONOSTICO APOSTERIORI |  | ERROR |  | PRONOSTICO APOSTERIORI |  | ERROR |
| 2 | enero | 1 | 195 | 229 |  | 0.980207 | 1.0249 | 1.00255 | 0.997084 |  | 25 | 247.214 |  | 1 | 198.357 | 3.35733 |  | 13 | 222.786 | 6.21412 |
| 3 | febrero | 2 | 252 | 271 |  | 1.25386 | 1.20188 | 1.22787 | 1.22118 |  | 26 | 305.269 |  | 2 | 245.431 | 6.56893 |  | 14 | 275.35 | 4.3499 |
| 4 | marzo | 3 | 299 | 333 |  | 1.47276 | 1.4636 | 1.46818 | 1.46017 |  | 27 | 367.994 |  | 3 | 296.445 | 2.5547 |  | 15 | 332.22 | 0.780496 |
| 5 | abril | 4 | 276 | 305 |  | 1.34593 | 1.32861 | 1.33727 | 1.32998 |  | 28 | 337.898 |  | 4 | 272.729 | 3.27105 |  | 16 | 305.313 | 0.313449 |
| 6 | mayo | 5 | 258 | 277 |  | 1.24575 | 1.19601 | 1.22088 | 1.21422 |  | 29 | 310.967 |  | 5 | 251.47 | 6.53003 |  | 17 | 281.218 | 4.21836 |
| 7 | junio | 6 | 210 | 239 |  | 1.00408 | 1.02292 | 1.0135 | 1.00797 |  | 30 | 260.204 |  | 6 | 210.813 | 0.813274 |  | 18 | 235.509 | 3.4914 |
| 8 | julio | 7 | 192 | 211 |  | 0.909145 | 0.895253 | 0.902199 | 0.897279 |  | 31 | 233.461 |  | 7 | 189.494 | 2.50596 |  | 19 | 211.477 | 0.477372 |
| 9 | agosto | 8 | 154 | 193 |  | 0.722228 | 0.811848 | 0.767038 | 0.762855 |  | 32 | 200.043 |  | 8 | 162.663 | 8.66289 |  | 20 | 181.353 | 11.6472 |
| 10 | septiembre | 9 | 141 | 155 |  | 0.654989 | 0.646451 | 0.65072 | 0.647171 |  | 33 | 171.028 |  | 9 | 139.317 | 1.68297 |  | 21 | 155.173 | 0.172714 |
| 11 | octubre | 10 | 128 | 159 |  | 0.589014 | 0.657534 | 0.623274 | 0.619875 |  | 34 | 165.08 |  | 10 | 134.707 | 6.70653 |  | 22 | 149.893 | 9.10654 |
| 12 | noviembre | 11 | 200 | 208 |  | 0.911767 | 0.852969 | 0.882368 | 0.877556 |  | 35 | 235.496 |  | 11 | 192.496 | 7.50443 |  | 23 | 213.996 | 5.99569 |
| 13 | diciembre | 12 | 217 | 236 |  | 0.980145 | 0.959756 | 0.96995 | 0.964661 |  | 36 | 260.84 |  | 12 | 213.572 | 3.42815 |  | 24 | 237.206 | 1.20604 |
| 15 |  |  | CICLO 1 | CICLO 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 16 |  | S_BARRA | 210.167 | 234.667 |  |  |  |  |  |  |  |  |  |  | MAD | 4.46552 |  |  |  |  |
| 17 | PENDIENTE | A1 | 2.04167 |  |  |  |  |  |  |  |  |  |  |  | MAPE |  |  |  |  |  |
| 18 | PROYECTARLA PRIMER PUNTO | nivel a0,2n | 245.896 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 19 | INTERCEPTO ORIGINAL | nivel a0 | 196.896 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

**Fórmulas (15 patrones distintos):**

- `F2`: `=C2/($C$19+$C$17*B2)`
- `G2`: `=D2/($C$19+$C$17*(B2+12))`
- `H2`: `=AVERAGE(F2:G2)`
- `I2`: `=12*H2/SUM($H$2:$H$13)`
- `L2`: `=($C$19+$C$17*K2)*I2`
- `O2`: `=($C$19+$C$17*N2)*I2`
- `P2`: `=ABS(O2-C2)`
- `S2`: `=($C$19+$C$17*R2)*I2`
- `T2`: `=ABS(S2-D2)`
- `C16`: `=AVERAGE(C2:C13)`
- `D16`: `=AVERAGE(D2:D13)`
- `P16`: `=AVERAGE(P2:P13,U2:U13)`
- `C17`: `=(D16-C16)/12`
- `C18`: `=D16+C17*11/2`
- `C19`: `=C18-(2*12)*C17`

### Hoja `FATOS PARA CORRELOGRAMA` — 44 filas × 21 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | MES | DEMANDA | REZAGO 1 | REZAGO 2 | REZAGO 3 | REZAGO 4 | REZAGO 5 | REZAGO 6 | REZAGO 7 | REZAGO 8 | REZAGO 9 | REZAGO 10 | REZAGO 11 | REZAGO 12 | REZAGO 13 | REZAGO 14 | REZAGO 15 | REZAGO 16 | REZAGO 17 | REZAGO 18 | REZAGO 19 |
| 2 | enero | 195 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 | febrero | 252 | 195 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 | marzo | 299 | 252 | 195 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 | abril | 276 | 299 | 252 | 195 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 | mayo | 258 | 276 | 299 | 252 | 195 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7 | junio | 210 | 258 | 276 | 299 | 252 | 195 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 | julio | 192 | 210 | 258 | 276 | 299 | 252 | 195 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9 | agosto | 154 | 192 | 210 | 258 | 276 | 299 | 252 | 195 |  |  |  |  |  |  |  |  |  |  |  |  |
| 10 | septiembre | 141 | 154 | 192 | 210 | 258 | 276 | 299 | 252 | 195 |  |  |  |  |  |  |  |  |  |  |  |
| 11 | octubre | 128 | 141 | 154 | 192 | 210 | 258 | 276 | 299 | 252 | 195 |  |  |  |  |  |  |  |  |  |  |
| 12 | noviembre | 200 | 128 | 141 | 154 | 192 | 210 | 258 | 276 | 299 | 252 | 195 |  |  |  |  |  |  |  |  |  |
| 13 | diciembre | 217 | 200 | 128 | 141 | 154 | 192 | 210 | 258 | 276 | 299 | 252 | 195 |  |  |  |  |  |  |  |  |
| 14 | enero | 229 | 217 | 200 | 128 | 141 | 154 | 192 | 210 | 258 | 276 | 299 | 252 | 195 |  |  |  |  |  |  |  |
| 15 | febrero | 271 | 229 | 217 | 200 | 128 | 141 | 154 | 192 | 210 | 258 | 276 | 299 | 252 | 195 |  |  |  |  |  |  |
| 16 | marzo | 333 | 271 | 229 | 217 | 200 | 128 | 141 | 154 | 192 | 210 | 258 | 276 | 299 | 252 | 195 |  |  |  |  |  |
| 17 | abril | 305 | 333 | 271 | 229 | 217 | 200 | 128 | 141 | 154 | 192 | 210 | 258 | 276 | 299 | 252 | 195 |  |  |  |  |
| 18 | mayo | 277 | 305 | 333 | 271 | 229 | 217 | 200 | 128 | 141 | 154 | 192 | 210 | 258 | 276 | 299 | 252 | 195 |  |  |  |
| 19 | junio | 239 | 277 | 305 | 333 | 271 | 229 | 217 | 200 | 128 | 141 | 154 | 192 | 210 | 258 | 276 | 299 | 252 | 195 |  |  |
| 20 | julio | 211 | 239 | 277 | 305 | 333 | 271 | 229 | 217 | 200 | 128 | 141 | 154 | 192 | 210 | 258 | 276 | 299 | 252 | 195 |  |
| 21 | agosto | 193 | 211 | 239 | 277 | 305 | 333 | 271 | 229 | 217 | 200 | 128 | 141 | 154 | 192 | 210 | 258 | 276 | 299 | 252 | 195 |
| 22 | septiembre | 155 | 193 | 211 | 239 | 277 | 305 | 333 | 271 | 229 | 217 | 200 | 128 | 141 | 154 | 192 | 210 | 258 | 276 | 299 | 252 |
| 23 | octubre | 159 | 155 | 193 | 211 | 239 | 277 | 305 | 333 | 271 | 229 | 217 | 200 | 128 | 141 | 154 | 192 | 210 | 258 | 276 | 299 |
| 24 | noviembre | 208 | 159 | 155 | 193 | 211 | 239 | 277 | 305 | 333 | 271 | 229 | 217 | 200 | 128 | 141 | 154 | 192 | 210 | 258 | 276 |
| 25 | diciembre | 236 | 208 | 159 | 155 | 193 | 211 | 239 | 277 | 305 | 333 | 271 | 229 | 217 | 200 | 128 | 141 | 154 | 192 | 210 | 258 |
| 26 |  |  | 236 | 208 | 159 | 155 | 193 | 211 | 239 | 277 | 305 | 333 | 271 | 229 | 217 | 200 | 128 | 141 | 154 | 192 | 210 |
| 27 |  |  |  | 236 | 208 | 159 | 155 | 193 | 211 | 239 | 277 | 305 | 333 | 271 | 229 | 217 | 200 | 128 | 141 | 154 | 192 |
| 28 |  |  |  |  | 236 | 208 | 159 | 155 | 193 | 211 | 239 | 277 | 305 | 333 | 271 | 229 | 217 | 200 | 128 | 141 | 154 |
| 29 |  |  |  |  |  | 236 | 208 | 159 | 155 | 193 | 211 | 239 | 277 | 305 | 333 | 271 | 229 | 217 | 200 | 128 | 141 |
| 30 |  |  |  |  |  |  | 236 | 208 | 159 | 155 | 193 | 211 | 239 | 277 | 305 | 333 | 271 | 229 | 217 | 200 | 128 |
| 31 |  |  |  |  |  |  |  | 236 | 208 | 159 | 155 | 193 | 211 | 239 | 277 | 305 | 333 | 271 | 229 | 217 | 200 |
| 32 |  |  |  |  |  |  |  |  | 236 | 208 | 159 | 155 | 193 | 211 | 239 | 277 | 305 | 333 | 271 | 229 | 217 |
| 33 |  |  |  |  |  |  |  |  |  | 236 | 208 | 159 | 155 | 193 | 211 | 239 | 277 | 305 | 333 | 271 | 229 |
| 34 |  |  |  |  |  |  |  |  |  |  | 236 | 208 | 159 | 155 | 193 | 211 | 239 | 277 | 305 | 333 | 271 |
| 35 |  |  |  |  |  |  |  |  |  |  |  | 236 | 208 | 159 | 155 | 193 | 211 | 239 | 277 | 305 | 333 |
| 36 |  |  |  |  |  |  |  |  |  |  |  |  | 236 | 208 | 159 | 155 | 193 | 211 | 239 | 277 | 305 |
| 37 |  |  |  |  |  |  |  |  |  |  |  |  |  | 236 | 208 | 159 | 155 | 193 | 211 | 239 | 277 |
| 38 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 236 | 208 | 159 | 155 | 193 | 211 | 239 |
| 39 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 236 | 208 | 159 | 155 | 193 | 211 |
| 40 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 236 | 208 | 159 | 155 | 193 |
| 41 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 236 | 208 | 159 | 155 |
| 42 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 236 | 208 | 159 |
| 43 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 236 | 208 |
| 44 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 236 |

### Hoja `CORRELOGRAMA` — 32 filas × 5 columnas · 1 gráfico(s)

**Gráficos en esta hoja:**

- Gráfico de barras + líneas — título «Correlograma de la demanda (FAC) - 19 rezagos» · ejes: Rezago (k) / Autocorrelación
  - Series: CORRELOGRAMA!$B$8: y = `CORRELOGRAMA!$B$9:$B$27`, x = `CORRELOGRAMA!$A$9:$A$27`; CORRELOGRAMA!$C$8: y = `CORRELOGRAMA!$C$9:$C$27`; CORRELOGRAMA!$D$8: y = `CORRELOGRAMA!$D$9:$D$27`

| Fila | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | CORRELOGRAMA (FAC) - DEMANDA |  |  |  |  |
| 3 | Observaciones (n) | 24 |  |  |  |
| 4 | Media de la demanda | 222.417 |  |  |  |
| 5 | Nivel de confianza (z) | 1.96 |  |  |  |
| 6 | Límite crítico ±z/√n | 0.400083 |  |  |  |
| 8 | Rezago | FAC (r_k) | Lím. sup. | Lím. inf. | Significativo |
| 9 | 1 | 0.76773 | 0.400083 | -0.400083 | Sí |
| 10 | 2 | 0.380982 | 0.400083 | -0.400083 | No |
| 11 | 3 | -0.00423634 | 0.400083 | -0.400083 | No |
| 12 | 4 | -0.345731 | 0.400083 | -0.400083 | No |
| 13 | 5 | -0.634025 | 0.400083 | -0.400083 | Sí |
| 14 | 6 | -0.728229 | 0.400083 | -0.400083 | Sí |
| 15 | 7 | -0.607711 | 0.400083 | -0.400083 | Sí |
| 16 | 8 | -0.316215 | 0.400083 | -0.400083 | No |
| 17 | 9 | -0.0424322 | 0.400083 | -0.400083 | No |
| 18 | 10 | 0.143898 | 0.400083 | -0.400083 | No |
| 19 | 11 | 0.335794 | 0.400083 | -0.400083 | No |
| 20 | 12 | 0.439964 | 0.400083 | -0.400083 | Sí |
| 21 | 13 | 0.347116 | 0.400083 | -0.400083 | No |
| 22 | 14 | 0.157351 | 0.400083 | -0.400083 | No |
| 23 | 15 | 0.0236116 | 0.400083 | -0.400083 | No |
| 24 | 16 | -0.0815957 | 0.400083 | -0.400083 | No |
| 25 | 17 | -0.134286 | 0.400083 | -0.400083 | No |
| 26 | 18 | -0.143851 | 0.400083 | -0.400083 | No |
| 27 | 19 | -0.0929708 | 0.400083 | -0.400083 | No |
| 29 | Interpretación |  |  |  |  |
| 30 | r1=0,77 positivo, mínimo en r6=-0,73 y repunte en r12=0,44: onda completa de 12 meses → estacionalidad anual con tendencia (adecuado para Winters). |  |  |  |  |
| 31 | Barras que superan las líneas rojas (±1,96/√n = ±0,400) = autocorrelación significativa al 95%. |  |  |  |  |
| 32 | Cautela: con n=24, los rezagos altos usan pocas parejas (k=19 solo 5), por lo que r_k a partir de ~k=12 es poco confiable. Regla práctica: k ≤ n/4. |  |  |  |  |

**Fórmulas (6 patrones distintos):**

- `B3`: `=COUNT('FATOS PARA CORRELOGRAMA'!$B$2:$B$25)`
- `B4`: `=AVERAGE('FATOS PARA CORRELOGRAMA'!$B$2:$B$25)`
- `B6`: `=$B$5/SQRT($B$3)`
- `C9`: `=$B$6`
- `D9`: `=-$B$6`
- `E9`: `=IF(ABS($B9)>$B$6,"Sí","No")`

