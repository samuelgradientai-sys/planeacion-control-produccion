# modelo-desagregacion-v2

> **Archivo:** [`modelo-desagregacion-v2.xlsx`](./modelo-desagregacion-v2.xlsx) · **Corte 2** (el archivo estaba en la carpeta `CORTE 3/` del estudiante) · Libro de Excel con 2 hoja(s): `Para una línea de producción`, `Modelo`  
> **Nombre original:** `CORTE 3/Modelo de Desagregación .xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Es otra versión del mismo libro de desagregación de la clase L11 ([`L11-aggregation-and-disaggregation.md`](./L11-aggregation-and-disaggregation.md)). Estaba en la carpeta del Corte 3, pero el tema es del Corte 2 (desagregación del plan agregado) y por eso vive aquí. Se creó el 2026-09-10, el mismo día que [`modelo-desagregacion.xlsx`](./modelo-desagregacion.md), en Excel para Mac, y se modificó por última vez el 2026-09-11. Resuelve con **Solver (Simplex LP)** los dos mismos ejemplos:

1. **`Para una línea de producción`**: tiempo de ciclo máximo de una línea con 5 productos, con producción y demanda constantes (L11, pp. 15–20). Resultado: $T^* = 1{,}5948$ meses.
2. **`Modelo`**: desagregación mensual, por producto, del plan agregado de 12 meses del modelo de flujo en GAMS ([`../01-planeacion-agregada-modelo-bowman/README.md`](../01-planeacion-agregada-modelo-bowman/README.md)), minimizando el inventario total. Resultado: 7900 horas-mes.

**¿Mismo ejercicio que `modelo-desagregacion.xlsx`?** Sí: mismos datos, mismo método y mismos resultados en el objetivo. Las diferencias, detalladas al final, son de presentación y de configuración de Solver (aquí el objetivo sí está bien puesto), más un reparto distinto por producto en los meses 1–4 que tiene el mismo inventario total. Ese reparto es un óptimo alternativo.

---

### Hoja `Para una línea de producción`: tiempo de ciclo máximo

**Objetivo (deducido de L11, pp. 16–19).** Hallar los tiempos de inicio $t_i$ de cada producto y el ciclo completo $T$ más largo posible, sin que ningún producto se agote, en una línea que produce 3700 h/mes y fabrica los productos uno tras otro en orden creciente de tiempo de agotamiento.

**Datos de entrada** (filas 5–9; encabezado «Parámetros del Modelo» en B3:D3):

| Fila | Producto (posición) | Inventario Inicial (B) | Demanda Mes $d_i$ (C) | tasa de producción/mes $P$ (D) |
|---|---|---|---|---|
| 5 | A | 200 | 600 | 3700 |
| 6 | B | 300 | 600 | 3700 |
| 7 | C | 700 | 900 | 3700 |
| 8 | D | 800 | 800 | 3700 |
| 9 | E | 1000 | 800 | 3700 |

Las letras A–E son **posiciones** en la secuencia, no los productos de la tabla de demanda. Por los inventarios iniciales, son los productos C, A, B, D y E de la hoja `Modelo` y de L11 p. 8 (deducido). Las tasas de demanda suman 3700, igual a $P$.

**Parámetros:** $P = 3700$ h/mes en D5:D9. No hay costos.

**Método paso a paso:**

1. **Inventario en meses** (E, «ordenar creciente»): `E5 = +B5/C5`, es decir, $r_i = I_{0,i}/d_i$, que da 0,3333; 0,5; 0,7778; 1; 1,25.
2. **Variables** («Variable de decisión», F): F5:F9 son los inicios $t_i$ y F10 es $T$ («T (duración del ciclo)»).
3. **Producción total** (G): `G5 = +(F6-F5)*D5`, es decir, $G_i = (t_{i+1}-t_i)P$. La última fila usa F10: $G_5 = (T-t_5)P$.
4. **Demanda total** (H): `H5 = +$F$10*C5`, es decir, $H_i = T\,d_i$.
5. **Solver** (nombres `solver_*`):
   - **Maximizar** F10.
   - Celdas variables: F5:F10.
   - Restricción F5:F9 ≤ E5:E9 ($t_i \le r_i$).
   - Restricción G5:G9 ≥ H5:H9 (lo producido cubre la demanda del ciclo).
   - No negatividad; motor Simplex LP, con la opción «asumir modelo lineal» activada (`solver_lin = 1`).

$$
\max T\quad\text{s.a.}\quad t_i\le r_i,\qquad (t_{i+1}-t_i)P\ge T d_i\ (i=1,\dots,4),\qquad (T-t_5)P\ge T d_5
$$

**Resultados:**

| Posición | Producto real (deducido) | $r_i$ | Inicio $t_i$ | Producción en el ciclo (G) | Demanda en el ciclo (H) |
|---|---|---|---|---|---|
| A | C | 0,3333 | 0 | 956,90 | 956,90 |
| B | A | 0,5 | 0,258621 | 956,90 | 956,90 |
| C | B | 0,7778 | 0,517241 | 1435,34 | 1435,34 |
| D | D | 1 | 0,905172 | 1275,86 | 1275,86 |
| E | E | 1,25 | 1,25 | 1275,86 | 1275,86 |
| | | | **$T^*$ = 1,5948276** (F10) | | |

Todas las restricciones de demanda están activas y el producto E arranca justo cuando se agota ($t_5 = r_5 = 1{,}25$). Comprobación propia: $T^* = 1{,}25\cdot 3700/2900 = 1{,}594828$.

**Gráficos:** ninguno.

**Conclusión.** El resultado es el mismo de L11 p. 19: rotación de 1,5948 meses con la secuencia C (0) → A (0,2586) → B (0,5172) → D (0,9052) → E (1,25).

---

### Hoja `Modelo`: desagregación mensual del plan agregado

**Objetivo (deducido).** Repartir cada mes la producción agregada entre los productos A–E. Cada mes la producción total debe ser al menos la del plan agregado, sin inventarios negativos por producto, y se minimiza el inventario total.

**Datos de entrada:**

- **Pronóstico de la Demanda** (B3:F14, total en G; título en A1:G1). Es la tabla de L11 p. 8, en horas-hombre, por mes:
  - A: 300, 600, 600, 800, 800, 800, 800, 1000, 600, 500, 400, 0.
  - B: 300, 600, 900, 1500, 600, 600, 100, 0, 0, 0, 0, 0.
  - C: 600, 600, 600, 600, 650, 600, 700, 700, 700, 600, 600, 600.
  - D: 600, 800, 1000, 1600, 1400, 1400, 1400, 2000, 2200, 1900, 1800, 1600.
  - E: 800 todos los meses.
  - Totales: 2600, 3400, 3900, 5300, 4250, 4200, 3800, 4500, 4300, 3800, 3600, 3000.
- **Initial Stock** (fila 19): A 300, B 700, C 200, D 800, E 1000; total 3000.
- **Plan Agregado** (P3:P14, valores fijos): 2880, 2880 y luego 3000 en los meses 3–12. Es la producción $P_t$ del modelo de flujo en GAMS ([`../01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/modelo-flujo.lst`](../01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/modelo-flujo.lst)).

**Parámetros:** no hay costos.

**Método paso a paso:**

1. **Variables:** J3:N14 = $Y_{j,t}$, la producción por producto y mes (bloque «Producción», I1:P1).
2. **Total:** `O3 = SUM(J3:N3)`, es decir, $P_t=\sum_j Y_{j,t}$.
3. **Inventarios** (bloque «Inventarios», filas 21–32). El mes 1 sale de `B21 = $B$19+J3-B3` y los siguientes de `B22 = B21+J4-B4`; es decir, $I_{j,t} = I_{j,t-1}+Y_{j,t}-D_{j,t}$. El total por mes es `G21 = SUM(B21:F21)`.
4. **Inventario Total:** `J18 = SUM(B21:F32)`.
5. **Solver:**
   - **Minimizar J18** (`solver_typ = 2`).
   - Variables J3:N14, no negativas.
   - Restricción B21:F32 ≥ 0.
   - Restricción O3:O14 ≥ P3:P14.
   - Simplex LP, con «asumir modelo lineal».

$$
\min \sum_{t=1}^{12}\sum_{j} I_{j,t}\quad\text{s.a.}\quad I_{j,t} = I_{j,t-1}+Y_{j,t}-D_{j,t}\ge 0,\qquad \sum_j Y_{j,t}\ge X^*_t,\qquad Y_{j,t}\ge 0
$$

**Resultados.** Producción por producto (J3:P14):

| Mes | A | B | C | D | E | Total (O) | Plan Agregado (P) |
|---|---|---|---|---|---|---|---|
| 1 | 280 | 0 | 400 | 0 | 2200 | 2880 | 2880 |
| 2 | 920 | 760 | 600 | 600 | 0 | 2880 | 2880 |
| 3 | 0 | 340 | 600 | 2060 | 0 | 3000 | 3000 |
| 4 | 800 | 1500 | 600 | 540 | 0 | 3440 | 3000 |
| 5 | 800 | 600 | 650 | 1400 | 800 | 4250 | 3000 |
| 6 | 800 | 600 | 600 | 1400 | 800 | 4200 | 3000 |
| 7 | 800 | 100 | 700 | 1400 | 800 | 3800 | 3000 |
| 8 | 1000 | 0 | 700 | 2000 | 800 | 4500 | 3000 |
| 9 | 600 | 0 | 700 | 2200 | 800 | 4300 | 3000 |
| 10 | 500 | 0 | 600 | 1900 | 800 | 3800 | 3000 |
| 11 | 400 | 0 | 600 | 1800 | 800 | 3600 | 3000 |
| 12 | 0 | 0 | 600 | 1600 | 800 | 3000 | 3000 |

Inventario al final de cada mes (B19:G32):

| Mes | A | B | C | D | E | Total |
|---|---|---|---|---|---|---|
| Inicial | 300 | 700 | 200 | 800 | 1000 | 3000 |
| 1 | 280 | 400 | 0 | 200 | 2400 | 3280 |
| 2 | 600 | 560 | 0 | 0 | 1600 | 2760 |
| 3 | 0 | 0 | 0 | 1060 | 800 | 1860 |
| 4–12 | 0 | 0 | 0 | 0 | 0 | 0 |

- **Inventario Total (J18) = 7900.**
- Del mes 4 al 11, el exceso de la producción sobre el plan (440, 1250, 1200, 800, 1500, 1300, 800, 600) es igual a la subcontratación `OUTSOURCE(t)` del modelo GAMS (deducido). Los inventarios totales mensuales (3280, 2760, 1860) son los `I(t)` de la solución GAMS.

**Gráficos:** ninguno.

**Conclusión.** En esta solución el inventario de los primeros meses se acumula sobre todo en E (2400 en el mes 1) y luego en D (1060 en el mes 3). Hace falta para cubrir el pico de demanda del mes 4 (5300) con un plan agregado de 3000. Desde el mes 5 cada producto se fabrica igual a su demanda.

---

### Comparación con [`modelo-desagregacion.xlsx`](./modelo-desagregacion.md)

| Aspecto | `modelo-desagregacion.xlsx` (Corte 2) | `modelo-desagregacion-v2.xlsx` (este) |
|---|---|---|
| Hojas | `EJEMPLO 1`, `EJEMPLO 2` | `Para una línea de producción`, `Modelo` |
| Posición de las tablas | Filas 2–8; bloque mensual desde la columna B | Filas 3–10; bloque mensual desde la columna A |
| Rótulos | Con errores («ORDERAR CRECIETE», «VAIRBLE DE DECISIÓN», «Fase Produccion Mes») | Corregidos («ordenar creciente», «Variable de decisión», «tasa de producción/mes») |
| Fórmulas | `=B3/C3`, `=(F4-F3)*D3` | Las mismas con prefijo `=+` (`=+B5/C5`); el mes 1 de inventario usa referencia absoluta `$B$19`; total mensual con `SUM(B21:F21)` en vez del balance agregado |
| Objetivo de Solver (mensual) | `N19`, celda **vacía** (error) | `J18`, el inventario total (correcto) |
| Imagen | Captura de la tabla de demanda de L11 p. 8 | No tiene |
| Fila extra | Fila 30 «Initial Stock» con fórmulas que apuntan a una fila vacía | No tiene |
| $T^*$ y tiempos de inicio | 1,594828; 0; 0,258621; 0,517241; 0,905172; 1,25 | Idénticos (diferencias a partir del 11.º decimal) |
| Producción meses 1–4 | A 600/0/600/800; B 0/2600/0/0; C 1000/0/600/600; D 600/0/1000/1600; E 680/280/800/440 | A 280/920/0/800; B 0/760/340/1500; C 400/600/600/600; D 0/600/2060/540; E 2200/0/0/0 |
| Producción meses 5–12 | Igual a la demanda | Igual a la demanda |
| Inventario total | 7900 (3280 + 2760 + 1860) | 7900 (3280 + 2760 + 1860) |

**Conclusión de la comparación:** es el mismo ejercicio. La hoja de una línea da exactamente los mismos resultados en los dos libros. La hoja mensual tiene **óptimos alternativos**: el inventario total queda fijado por el plan agregado (en los meses 1–3 la producción tiene que ser igual al plan y desde el mes 4 no conviene guardar nada). Por eso los dos repartos por producto son distintos pero igual de buenos. Esta versión v2 es la mejor configurada, porque su Solver tiene la celda objetivo correcta.

### Observaciones

- El encabezado automático dice «Corte 3» porque el archivo original estaba en `CORTE 3/`, pero el contenido es del Corte 2 (L11, desagregación).
- La restricción «producción ≥ plan agregado» deja que la producción supere el plan del mes 4 en adelante. Esa diferencia representa la subcontratación del modelo GAMS (deducido); la hoja no la rotula.
- Las letras A–E de la hoja `Para una línea de producción` son posiciones de la secuencia (la A es el producto C), no los mismos productos de la hoja `Modelo`.
- Las demandas de la hoja de una línea (600, 600, 900, 800, 800) son tasas constantes elegidas para que sumen 3700. No corresponden a un mes concreto del pronóstico.

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `Para una línea de producción` — 10 filas × 8 columnas

| Fila | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| 3 |  | Parámetros del Modelo |  |  | ordenar creciente | Variable de decisión |  |  |
| 4 | Producto | Inventario Inicial | Demanda Mes | tasa de producción/mes | Inventario en meses | Inicio de la producción | Producción Total | Demanda Total |
| 5 | A | 200 | 600 | 3700 | 0.333333 | 0 | 956.897 | 956.897 |
| 6 | B | 300 | 600 | 3700 | 0.5 | 0.258621 | 956.897 | 956.897 |
| 7 | C | 700 | 900 | 3700 | 0.777778 | 0.517241 | 1435.34 | 1435.34 |
| 8 | D | 800 | 800 | 3700 | 1 | 0.905172 | 1275.86 | 1275.86 |
| 9 | E | 1000 | 800 | 3700 | 1.25 | 1.25 | 1275.86 | 1275.86 |
| 10 |  |  |  |  | T (duración del ciclo) | 1.59483 |  |  |

**Fórmulas (3 patrones distintos):**

- `E5`: `=+B5/C5`
- `G5`: `=+(F6-F5)*D5`
- `H5`: `=+$F$10*C5`

### Hoja `Modelo` — 32 filas × 16 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Pronóstico de la Demanda |  |  |  |  |  |  |  | Producción |  |  |  |  |  |  |  |
| 2 | Month | A | B | C | D | E | Total |  | Month | A | B | C | D | E | Total | Plan Agregado |
| 3 | 1 | 300 | 300 | 600 | 600 | 800 | 2600 |  | 1 | 280 | 0 | 400 | 0 | 2200 | 2880 | 2880 |
| 4 | 2 | 600 | 600 | 600 | 800 | 800 | 3400 |  | 2 | 920 | 760 | 600 | 600 | 0 | 2880 | 2880 |
| 5 | 3 | 600 | 900 | 600 | 1000 | 800 | 3900 |  | 3 | 0 | 340 | 600 | 2060 | 0 | 3000 | 3000 |
| 6 | 4 | 800 | 1500 | 600 | 1600 | 800 | 5300 |  | 4 | 800 | 1500 | 600 | 540 | 0 | 3440 | 3000 |
| 7 | 5 | 800 | 600 | 650 | 1400 | 800 | 4250 |  | 5 | 800 | 600 | 650 | 1400 | 800 | 4250 | 3000 |
| 8 | 6 | 800 | 600 | 600 | 1400 | 800 | 4200 |  | 6 | 800 | 600 | 600 | 1400 | 800 | 4200 | 3000 |
| 9 | 7 | 800 | 100 | 700 | 1400 | 800 | 3800 |  | 7 | 800 | 100 | 700 | 1400 | 800 | 3800 | 3000 |
| 10 | 8 | 1000 | 0 | 700 | 2000 | 800 | 4500 |  | 8 | 1000 | 0 | 700 | 2000 | 800 | 4500 | 3000 |
| 11 | 9 | 600 | 0 | 700 | 2200 | 800 | 4300 |  | 9 | 600 | 0 | 700 | 2200 | 800 | 4300 | 3000 |
| 12 | 10 | 500 | 0 | 600 | 1900 | 800 | 3800 |  | 10 | 500 | 0 | 600 | 1900 | 800 | 3800 | 3000 |
| 13 | 11 | 400 | 0 | 600 | 1800 | 800 | 3600 |  | 11 | 400 | 0 | 600 | 1800 | 800 | 3600 | 3000 |
| 14 | 12 | 0 | 0 | 600 | 1600 | 800 | 3000 |  | 12 | 0 | 0 | 600 | 1600 | 800 | 3000 | 3000 |
| 18 | Inventarios |  |  |  |  |  |  |  | Inventario Total | 7900 |  |  |  |  |  |  |
| 19 | Initial Stock | 300 | 700 | 200 | 800 | 1000 | 3000 |  |  |  |  |  |  |  |  |  |
| 20 | Month | A | B | C | D | E | TOTAL |  |  |  |  |  |  |  |  |  |
| 21 | 1 | 280 | 400 | 0 | 200 | 2400 | 3280 |  |  |  |  |  |  |  |  |  |
| 22 | 2 | 600 | 560 | 0 | 0 | 1600 | 2760 |  |  |  |  |  |  |  |  |  |
| 23 | 3 | 0 | 0 | 0 | 1060 | 800 | 1860 |  |  |  |  |  |  |  |  |  |
| 24 | 4 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |
| 25 | 5 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |
| 26 | 6 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |
| 27 | 7 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |
| 28 | 8 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |
| 29 | 9 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |
| 30 | 10 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |
| 31 | 11 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |
| 32 | 12 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |

**Fórmulas (12 patrones distintos):**

- `O3`: `=SUM(J3:N3)`
- `J18`: `=SUM(B21:F32)`
- `B21`: `=$B$19+J3-B3`
- `C21`: `=$C$19+K3-C3`
- `D21`: `=$D$19+L3-D3`
- `E21`: `=$E$19+M3-E3`
- `F21`: `=$F$19+N3-F3`
- `B22`: `=B21+J4-B4`
- `C22`: `=C21+K4-C4`
- `D22`: `=D21+L4-D4`
- `E22`: `=E21+M4-E4`
- `F22`: `=F21+N4-F4`

