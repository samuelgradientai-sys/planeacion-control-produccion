# modelo-desagregacion

> **Archivo:** [`modelo-desagregacion.xlsx`](./modelo-desagregacion.xlsx) · **Corte 2** · Libro de Excel con 2 hoja(s): `EJEMPLO 1`, `EJEMPLO 2`  
> **Nombre original:** `CORTE 2/MODELO DE DESAGREGACION.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Es el libro de Excel de la clase de desagregación ([`L11-aggregation-and-disaggregation.md`](./L11-aggregation-and-disaggregation.md)). Resuelve con **Solver (motor Simplex LP)** los dos pasos de la desagregación del ejemplo de 5 productos (A–E) y 12 meses:

1. **`EJEMPLO 1`**: el tiempo de ciclo máximo de una línea que fabrica los 5 productos en rotación, con producción y demanda constantes (L11, pp. 15–20). Resultado: $T^* = 1{,}5948$ meses.
2. **`EJEMPLO 2`**: desagrega mes a mes, en producción por producto, el plan agregado de 12 meses que sale del modelo de flujo en GAMS de la carpeta hermana ([`../01-planeacion-agregada-modelo-bowman/README.md`](../01-planeacion-agregada-modelo-bowman/README.md)). Busca el menor inventario sin faltantes. Resultado: inventario total de 7900 horas-mes.

Con estos ejemplos se aprende a pasar de un plan en horas-hombre a cantidades por producto. Hay dos maneras: ordenar por tiempo de agotamiento y fijar los tiempos de inicio dentro de un ciclo, o repartir cada mes la producción agregada sin que ningún producto se quede sin inventario. El libro se creó el 2026-09-10, el mismo día en que se corrió el modelo GAMS de la carpeta 01.

---

### Hoja `EJEMPLO 1`: tiempo de ciclo máximo en una línea

**Objetivo (deducido de L11, pp. 16–19).** Una sola línea produce 3700 h/mes y fabrica los productos uno tras otro, en orden creciente de tiempo de agotamiento. Hay que hallar cuándo empieza cada producto ($t_i$) y la duración máxima del ciclo completo ($T$) sin que ningún producto se agote. Un ciclo más largo implica menos set-ups.

**Datos de entrada** (filas 3–7):

| Fila | Producto (posición) | Inventario inicial $I_{0,i}$ (B) | Demanda/mes $d_i$ (C) | Tasa de producción $P$ (D, «Fase Produccion Mes») |
|---|---|---|---|---|
| 3 | A | 200 | 600 | 3700 |
| 4 | B | 300 | 600 | 3700 |
| 5 | C | 700 | 900 | 3700 |
| 6 | D | 800 | 800 | 3700 |
| 7 | E | 1000 | 800 | 3700 |

Ojo con las letras. Aquí A–E son las **posiciones** en la secuencia (ya ordenadas, como en la p. 15 de L11). Por los inventarios iniciales, corresponden a los productos C, A, B, D y E de la tabla de demanda (L11 p. 8 y hoja `EJEMPLO 2`), que es la secuencia de la p. 19 (deducido). Las tasas de demanda suman $600+600+900+800+800 = 3700 = P$, de modo que la línea produce justo lo que se consume.

**Parámetros:**

- Tasa de producción $P = 3700$ h/mes en D3:D7. Coincide con la plantilla regular de la solución de L11 p. 11.
- No hay costos: el modelo solo maximiza $T$.

**Método paso a paso:**

1. **Tiempo de agotamiento** (columna E, rotulada «INV En Meses» y «ORDERAR CRECIETE» en E1): `E3 = B3/C3`, es decir, $r_i = I_{0,i}/d_i$. Da 0,3333; 0,5; 0,7778; 1; 1,25. Los productos ya vienen ordenados de forma creciente.
2. **Variables de decisión** (columna F, «VAIRBLE DE DECISIÓN» en F1): F3:F7 son los tiempos de inicio $t_i$ y F8 es $T$ («T (Duracion del ciclo)»).
3. **Producción del producto $i$ en el ciclo** (columna G, «Produccion Total»): `G3 = (F4-F3)*D3`, es decir, $G_i = (t_{i+1}-t_i)\,P$. Para el último, `G7 = (F8-F7)*D7`, es decir, $G_5 = (T - t_5)\,P$ (reinicio del ciclo).
4. **Demanda del producto durante el ciclo** (columna H, «Demanda Total»): `H3 = $F$8*C3`, es decir, $H_i = T\,d_i$.
5. **Solver** (guardado en los nombres `solver_*` de la hoja):
   - Objetivo: **maximizar** F8 (`solver_typ = 1`).
   - Celdas variables: F3:F8.
   - Restricción 1: F3:F7 ≤ E3:E7, es decir, $t_i \le r_i$ (que no haya faltantes antes del primer lote).
   - Restricción 2: G3:G7 ≥ H3:H7, es decir, $(t_{i+1}-t_i)P \ge T d_i$ (lo producido cubre la demanda del ciclo). La nota en G12, «PRODUCCION TIENE QUE SER MAYOR O IGUAL», recuerda esta restricción.
   - Variables no negativas (`solver_neg = 1`); motor Simplex LP (`solver_eng = 2`).

Es la formulación de L11 p. 17 multiplicada por $d_i$:

$$
\max T\quad\text{s.a.}\quad t_i \le r_i,\qquad (t_{i+1}-t_i)P \ge T\,d_i\ (i=1,\dots,4),\qquad (T-t_5)P \ge T\,d_5,\qquad t_i, T\ge 0
$$

**Resultados** (valores guardados):

| Posición | Producto real (deducido) | $r_i$ (E) | Inicio $t_i$ (F) | Duración del lote $t_{i+1}-t_i$ | Producción en el ciclo (G) | Demanda en el ciclo (H) |
|---|---|---|---|---|---|---|
| A | C | 0,3333 | 0 | 0,2586 | 956,90 | 956,90 |
| B | A | 0,5 | 0,258621 | 0,2586 | 956,90 | 956,90 |
| C | B | 0,7778 | 0,517241 | 0,3879 | 1435,34 | 1435,34 |
| D | D | 1 | 0,905172 | 0,3448 | 1275,86 | 1275,86 |
| E | E | 1,25 | 1,25 | 0,3448 | 1275,86 | 1275,86 |
| | | | **$T^*$ = 1,594828** (F8) | | Σ = 5900,86 | Σ = 5900,86 |

- Todas las restricciones G ≥ H quedan activas (G = H), y la del último producto también: $t_5 = r_5 = 1{,}25$.
- Comprobación propia: $T^* = r_5 P / (d_1+d_2+d_3+d_4) = 1{,}25 \cdot 3700/2900 = 1{,}594828$, igual que en F8.
- Las duraciones de la tabla no están en el Excel: son diferencias entre las celdas de la columna F.

**Gráficos:** ninguno.

**Conclusión.** La rotación óptima dura 1,5948 meses: C desde 0, A desde 0,2586, B desde 0,5172, D desde 0,9052 y E desde 1,25. Lo que limita el ciclo es el producto E, que se agota exactamente cuando empieza a fabricarse. Los resultados coinciden con L11 pp. 19–20.

---

### Hoja `EJEMPLO 2`: desagregación mensual del plan agregado

**Objetivo (deducido).** Repartir cada mes la producción agregada entre los productos A–E. Cada mes la producción total debe ser al menos la del plan agregado, y ningún producto puede tener inventario negativo. Se busca el menor inventario total.

**Datos de entrada:**

- **Pronóstico** (C3:G14, totales en H; título «Pronostico» en D1:F1). Es la demanda en horas-hombre de L11 p. 8:

| Mes | A | B | C | D | E | Total |
|---|---|---|---|---|---|---|
| 1 | 300 | 300 | 600 | 600 | 800 | 2600 |
| 2 | 600 | 600 | 600 | 800 | 800 | 3400 |
| 3 | 600 | 900 | 600 | 1000 | 800 | 3900 |
| 4 | 800 | 1500 | 600 | 1600 | 800 | 5300 |
| 5 | 800 | 600 | 650 | 1400 | 800 | 4250 |
| 6 | 800 | 600 | 600 | 1400 | 800 | 4200 |
| 7 | 800 | 100 | 700 | 1400 | 800 | 3800 |
| 8 | 1000 | 0 | 700 | 2000 | 800 | 4500 |
| 9 | 600 | 0 | 700 | 2200 | 800 | 4300 |
| 10 | 500 | 0 | 600 | 1900 | 800 | 3800 |
| 11 | 400 | 0 | 600 | 1800 | 800 | 3600 |
| 12 | 0 | 0 | 600 | 1600 | 800 | 3000 |

- **Inventario inicial** (fila 17, «Initial Stock»): A 300, B 700, C 200, D 800, E 1000; total 3000.
- **Plan agregado** (Q3:Q14, valores fijos): 2880, 2880 y luego 3000 en los meses 3 a 12. Es exactamente la producción $P_t$ de la solución del modelo de flujo en GAMS ([`../01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/modelo-flujo.lst`](../01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/modelo-flujo.lst)).
- **Imagen:** en T1, a la derecha de las tablas, hay una captura de la tabla «Month / A–E / Total / Initial Stock» de L11 p. 8. Repite los mismos datos del pronóstico y del inventario inicial.

**Parámetros:** no hay costos. Las únicas constantes son el pronóstico, el inventario inicial y el plan agregado.

**Método paso a paso:**

1. **Variables de decisión:** K3:O14 = $Y_{j,t}$, la producción del producto $j$ en el mes $t$ (bloque «Produccion», título en L1:N1).
2. **Producción total:** `P3 = SUM(K3:O3)`, es decir, $P_t = \sum_j Y_{j,t}$.
3. **Inventario por producto** (bloque «inventarios», filas 18–29): `C18 = C17+K3-C3`, es decir, $I_{j,t} = I_{j,t-1} + Y_{j,t} - D_{j,t}$. La columna H usa el mismo balance con los totales: `H18 = H17+P3-H3`.
4. **Inventario total:** `K17 = SUM(C18:G29)`, es decir, $\sum_{t=1}^{12}\sum_j I_{j,t}$.
5. **Solver** (nombres `solver_*` de la hoja):
   - **Minimizar** (`solver_typ = 2`) la celda `N19`.
   - Variables K3:O14, no negativas.
   - Restricción 1: C18:G29 ≥ 0 (sin faltantes por producto).
   - Restricción 2: P3:P14 ≥ Q3:Q14 (producción ≥ plan agregado).
   - Motor Simplex LP.
   - La celda objetivo N19 está **vacía**: la que debería ir es K17 (deducido; la versión v2 usa la celda equivalente).

Formulación (deducida):

$$
\min \sum_{t=1}^{12}\sum_{j=A}^{E} I_{j,t}\quad\text{s.a.}\quad I_{j,t} = I_{j,t-1} + Y_{j,t} - D_{j,t}\ge 0,\qquad \sum_j Y_{j,t} \ge X_t^*,\qquad Y_{j,t}\ge 0
$$

donde $X_t^*$ es el plan agregado del mes $t$ (columna Q).

**Resultados.** Producción por producto (K3:P14):

| Mes | A | B | C | D | E | Total (P) | Plan agregado (Q) | Exceso sobre el plan |
|---|---|---|---|---|---|---|---|---|
| 1 | 600 | 0 | 1000 | 600 | 680 | 2880 | 2880 | 0 |
| 2 | 0 | 2600 | 0 | 0 | 280 | 2880 | 2880 | 0 |
| 3 | 600 | 0 | 600 | 1000 | 800 | 3000 | 3000 | 0 |
| 4 | 800 | 0 | 600 | 1600 | 440 | 3440 | 3000 | 440 |
| 5 | 800 | 600 | 650 | 1400 | 800 | 4250 | 3000 | 1250 |
| 6 | 800 | 600 | 600 | 1400 | 800 | 4200 | 3000 | 1200 |
| 7 | 800 | 100 | 700 | 1400 | 800 | 3800 | 3000 | 800 |
| 8 | 1000 | 0 | 700 | 2000 | 800 | 4500 | 3000 | 1500 |
| 9 | 600 | 0 | 700 | 2200 | 800 | 4300 | 3000 | 1300 |
| 10 | 500 | 0 | 600 | 1900 | 800 | 3800 | 3000 | 800 |
| 11 | 400 | 0 | 600 | 1800 | 800 | 3600 | 3000 | 600 |
| 12 | 0 | 0 | 600 | 1600 | 800 | 3000 | 3000 | 0 |

La última columna es cálculo propio (P − Q). Ese exceso coincide unidad por unidad con la **subcontratación** `OUTSOURCE(t)` de la solución GAMS (440, 1250, 1200, 800, 1500, 1300, 800 y 600 en los meses 4–11). Es decir, la columna P es la producción propia más la subcontratada (deducido).

Inventario al final de cada mes (C17:H29):

| Mes | A | B | C | D | E | Total |
|---|---|---|---|---|---|---|
| Inicial | 300 | 700 | 200 | 800 | 1000 | 3000 |
| 1 | 600 | 400 | 600 | 800 | 880 | 3280 |
| 2 | 0 | 2400 | 0 | 0 | 360 | 2760 |
| 3 | 0 | 1500 | 0 | 0 | 360 | 1860 |
| 4–12 | 0 | 0 | 0 | 0 | 0 | 0 |

- **Inventario total (K17) = 7900** = 3280 + 2760 + 1860. Coincide con la suma de `I(t)` de la solución GAMS (3280, 2760 y 1860 en los meses 1–3).
- En el mes 4 se consumen los últimos inventarios: B usa sus 1500 y no produce, y E usa 360 y produce 440. Desde el mes 5 la producción de cada producto es igual a su demanda.

**Gráficos:** ninguno (solo la imagen de la tabla de demanda).

**Conclusión.** En los meses 1–3 el plan agregado (2880, 2880 y 3000) se reparte de modo que todo producto llegue sin faltantes al mes 4. En el mes 1 el inventario queda repartido entre los cinco productos. En los meses 2–3 se concentra en B (2400 y 1500) y E (360), y a partir del mes 4 es cero. El total de 7900 queda fijado por el plan agregado. Cualquier reparto que cumpla las restricciones con P = Q en los meses 1–3 da el mismo total, así que hay **óptimos alternativos**: la versión v2 llega a otro reparto con el mismo 7900.

---

### Observaciones

- **Celda objetivo vacía en `EJEMPLO 2`:** Solver apunta a `N19`, que no tiene nada. Con esa configuración solo se obtiene una solución factible. El objetivo correcto sería K17 (inventario total), como en la hoja `Modelo` de [`modelo-desagregacion-v2.md`](./modelo-desagregacion-v2.md).
- **Fila 30 sobrante:** dice «Initial Stock», pero sus fórmulas (`C30 = C29+K15-C15`) apuntan a la fila 15, que está vacía. Es un arrastre de fórmulas y solo repite el inventario del mes 12 (0).
- **Errores de rótulo:** «ORDERAR CRECIETE» (ordenar creciente), «VAIRBLE DE DECISIÓN» (variable de decisión) y «Fase Produccion Mes» (debería ser «tasa de producción/mes»).
- **Letras A–E en `EJEMPLO 1`:** no son los productos de `EJEMPLO 2` sino posiciones en la secuencia (la A de `EJEMPLO 1` es el producto C). Mismo problema que la p. 15 de L11.
- La restricción es «producción ≥ plan agregado», no «=». Por eso, del mes 4 en adelante, la producción por producto supera el plan; esa diferencia corresponde a la subcontratación del modelo GAMS.
- Las demandas de `EJEMPLO 1` (600, 600, 900, 800, 800) no salen de un mes concreto del pronóstico. Son tasas constantes que suman 3700, igual a la tasa de producción.
- Comparación con [`modelo-desagregacion-v2.xlsx`](./modelo-desagregacion-v2.md): es el **mismo ejercicio**. `EJEMPLO 1` da los mismos resultados que la hoja `Para una línea de producción`. `EJEMPLO 2` corresponde a la hoja `Modelo`, con otro reparto por producto en los meses 1–4, el mismo inventario total (7900) y el objetivo de Solver bien configurado en v2. El detalle está en el .md de la v2.

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `EJEMPLO 1` — 12 filas × 8 columnas

| Fila | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| 1 |  |  |  |  | ORDERAR CRECIETE | VAIRBLE DE DECISIÓN |  |  |
| 2 | Producto | INV Inicial | Demanda Mes | Fase Produccion Mes | INV En Meses | Inicio De La Produccion | Produccion Total | Demanda Total |
| 3 | A | 200 | 600 | 3700 | 0.333333 | 0 | 956.897 | 956.897 |
| 4 | B | 300 | 600 | 3700 | 0.5 | 0.258621 | 956.897 | 956.897 |
| 5 | C | 700 | 900 | 3700 | 0.777778 | 0.517241 | 1435.34 | 1435.34 |
| 6 | D | 800 | 800 | 3700 | 1 | 0.905172 | 1275.86 | 1275.86 |
| 7 | E | 1000 | 800 | 3700 | 1.25 | 1.25 | 1275.86 | 1275.86 |
| 8 |  |  |  |  | T (Duracion del ciclo) | 1.59483 |  |  |
| 11 |  |  |  |  |  |  |  |  |
| 12 |  |  |  |  |  |  | PRODUCCION TIENE QUE SER MAYOR O IGUAL |  |

**Fórmulas (3 patrones distintos):**

- `E3`: `=B3/C3`
- `G3`: `=(F4-F3)*D3`
- `H3`: `=$F$8*C3`

### Hoja `EJEMPLO 2` — 30 filas × 17 columnas · 1 imagen(es)

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 |  |  |  | Pronostico |  |  |  |  |  |  |  | Produccion |  |  |  |  |  |
| 2 |  | Month | A | B | C | D | E | Total |  | Month | A | B | C | D | E | Total | Plan Agregado |
| 3 |  | 1 | 300 | 300 | 600 | 600 | 800 | 2600 |  | 1 | 600 | 0 | 1000 | 600 | 680 | 2880 | 2880 |
| 4 |  | 2 | 600 | 600 | 600 | 800 | 800 | 3400 |  | 2 | 0 | 2600 | 0 | 0 | 280 | 2880 | 2880 |
| 5 |  | 3 | 600 | 900 | 600 | 1000 | 800 | 3900 |  | 3 | 600 | 0 | 600 | 1000 | 800 | 3000 | 3000 |
| 6 |  | 4 | 800 | 1500 | 600 | 1600 | 800 | 5300 |  | 4 | 800 | 0 | 600 | 1600 | 440 | 3440 | 3000 |
| 7 |  | 5 | 800 | 600 | 650 | 1400 | 800 | 4250 |  | 5 | 800 | 600 | 650 | 1400 | 800 | 4250 | 3000 |
| 8 |  | 6 | 800 | 600 | 600 | 1400 | 800 | 4200 |  | 6 | 800 | 600 | 600 | 1400 | 800 | 4200 | 3000 |
| 9 |  | 7 | 800 | 100 | 700 | 1400 | 800 | 3800 |  | 7 | 800 | 100 | 700 | 1400 | 800 | 3800 | 3000 |
| 10 |  | 8 | 1000 | 0 | 700 | 2000 | 800 | 4500 |  | 8 | 1000 | 0 | 700 | 2000 | 800 | 4500 | 3000 |
| 11 |  | 9 | 600 | 0 | 700 | 2200 | 800 | 4300 |  | 9 | 600 | 0 | 700 | 2200 | 800 | 4300 | 3000 |
| 12 |  | 10 | 500 | 0 | 600 | 1900 | 800 | 3800 |  | 10 | 500 | 0 | 600 | 1900 | 800 | 3800 | 3000 |
| 13 |  | 11 | 400 | 0 | 600 | 1800 | 800 | 3600 |  | 11 | 400 | 0 | 600 | 1800 | 800 | 3600 | 3000 |
| 14 |  | 12 | 0 | 0 | 600 | 1600 | 800 | 3000 |  | 12 | 0 | 0 | 600 | 1600 | 800 | 3000 | 3000 |
| 16 |  |  |  | inventarios |  |  |  | TOTAL |  |  |  |  |  |  |  |  |  |
| 17 |  | Initial Stock | 300 | 700 | 200 | 800 | 1000 | 3000 |  | Inventario Total | 7900 |  |  |  |  |  |  |
| 18 |  | 1 | 600 | 400 | 600 | 800 | 880 | 3280 |  |  |  |  |  |  |  |  |  |
| 19 |  | 2 | 0 | 2400 | 0 | 0 | 360 | 2760 |  |  |  |  |  |  |  |  |  |
| 20 |  | 3 | 0 | 1500 | 0 | 0 | 360 | 1860 |  |  |  |  |  |  |  |  |  |
| 21 |  | 4 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |
| 22 |  | 5 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |
| 23 |  | 6 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |
| 24 |  | 7 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |
| 25 |  | 8 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |
| 26 |  | 9 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |
| 27 |  | 10 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |
| 28 |  | 11 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |
| 29 |  | 12 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |
| 30 |  | Initial Stock | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |

**Fórmulas (8 patrones distintos):**

- `P3`: `=SUM(K3:O3)`
- `K17`: `=SUM(C18:G29)`
- `C18`: `=C17+K3-C3`
- `D18`: `=D17+L3-D3`
- `E18`: `=E17+M3-E3`
- `F18`: `=F17+N3-F3`
- `G18`: `=G17+O3-G3`
- `H18`: `=H17+P3-H3`

