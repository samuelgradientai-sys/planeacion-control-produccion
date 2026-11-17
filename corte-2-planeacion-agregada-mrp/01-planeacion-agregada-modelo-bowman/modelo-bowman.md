# modelo-bowman

> **Archivo:** [`modelo-bowman.xlsx`](./modelo-bowman.xlsx) · **Corte 2** · Libro de Excel con 2 hoja(s): `COSTOS`, `PRODUCCION`  
> **Nombre original:** `CORTE 2/BOWMAN.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Este libro resuelve con Excel Solver el **ejemplo del modelo de Bowman** de la clase [L10 – Aggregate planning](./L10-aggregate-planning.md) (pp. 55-67). El ejemplo tiene dos productos (A y B), 4 meses y dos fuentes de capacidad por mes, tiempo regular y tiempo extra. Primero se agrega la demanda en horas de trabajo y después se decide cuántas horas producir en cada mes y en cada régimen para cubrir la demanda de cada mes de consumo al menor costo de producción más almacenamiento.

Con él se aprende a:
1. calcular la demanda neta agregada;
2. construir la matriz de costos producción→consumo, $C + (k-j)C_I$;
3. formular el problema de transporte en una hoja y resolverlo con Solver (Simplex LP);
4. leer el plan consolidado de horas regulares y extra.

Su nombre original era `CORTE 2/BOWMAN.xlsx`. El mismo ejercicio está reorganizado en una sola hoja en [ejemplo-modelo-bowman.md](./ejemplo-modelo-bowman.md).

### Hoja `COSTOS`: datos, demanda agregada y matrices de costo

**Objetivo (deducido):** preparar los datos del modelo, es decir, la demanda neta en horas por mes y los costos unitarios de cada par (mes de producción, mes de consumo).

**Datos de entrada (B2:F7)**

| Mes | Producto A (unid.) | Producto B (unid.) | Demanda agregada bruta (h), col. E | Demanda neta (h), col. F |
|---|---|---|---|---|
| 1 | 100 | 200 | 180 | 64 |
| 2 | 90 | 190 | 166 | 158 |
| 3 | 110 | 210 | 194 | 194 |
| 4 | 100 | 200 | 180 | 180 |
| **Total (fila 7)** | 400 | 800 | 720 | 596 |

**Parámetros (J2:K11)**

| Celda | Parámetro (rótulo de la hoja) | Valor |
|---|---|---|
| K3 | Costo hora regular (\$/hora), $C_R$ | 10 |
| K4 | Costo hora extra (\$/hora), $C_O$ | 15 |
| K5 | Costo almacenamiento (\$/unidad), $C_I$ (en realidad \$/hora-mes) | 4 |
| K6 | Capacidad regular (horas/mes) | 160 |
| K7 | Capacidad extra (horas/mes) | 40 |
| K8 | Horas por unidad – producto A, $h_A$ | 1 |
| K9 | Horas por unidad – producto B, $h_B$ | 0.4 |
| K10 | «Inventario inicial – producto A (unid.)» | 220 |
| K11 | «Inventario inicial – producto B (unid.)» | 36 |

> Los rótulos de K10 y K11 están invertidos. Según L10 p. 55 el inventario inicial es 36 de A y 220 de B, y la fórmula de F3 usa K11 = 36 para el producto A (ver Observaciones).

**Método paso a paso**

1. **Demanda agregada bruta en horas** (E3:E6), `=C3*$K$8+D3*$K$9`:
   $$D^{bruta}_t = h_A A_t + h_B B_t = 1{,}0\,A_t + 0{,}4\,B_t$$
   Da 180, 166, 194 y 180, con un total de 720 h (E7).
2. **Demanda neta en horas** (F3:F6):
   - F3 `=C3-$K$11*$K$8+0*$K$9`, es decir $(100-36)\cdot 1 + 0 \cdot 0{,}4 = 64$. A se descuenta su inventario de 36. B no aporta nada porque su inventario (220) cubre los 200 del mes 1 y sobran 20.
   - F4 `=C4*$K$8+170*$K$9`, es decir $90 + 170 \cdot 0{,}4 = 158$. El 170 está escrito a mano y equivale a $190 - 20$, la demanda de B del mes 2 menos lo que sobró del inventario.
   - F5 y F6 son iguales a la bruta (194 y 180), porque ya no queda inventario.
   - Total neto: 596 h (F7).
3. **Matriz de costos en tiempo regular** (C12:G15). Las filas son el mes de producción $j$ (1-4) y las columnas el mes de consumo $k$ (1-5). La columna 5 es el **inventario final** de L10 p. 62.
   - En la diagonal hay un 10 escrito a mano. A la derecha, cada celda vale la de su izquierda + 4 (`=C12+4`, `=D12+4`, …; G15 `=10+4`).
   - Debajo de la diagonal hay un 1000, que funciona como "M grande" para prohibir producir después del mes de consumo (no hay backlog).
   - Fórmula: $c^R_{jk} = C_R + (k-j)\,C_I$ si $k \ge j$, y $1000$ si $k < j$.

   | Producción \ Consumo | 1 | 2 | 3 | 4 | 5 (inv. final) |
   |---|---|---|---|---|---|
   | 1 | 10 | 14 | 18 | 22 | 26 |
   | 2 | 1000 | 10 | 14 | 18 | 22 |
   | 3 | 1000 | 1000 | 10 | 14 | 18 |
   | 4 | 1000 | 1000 | 1000 | 10 | 14 |

4. **Matriz de costos en tiempo extra** (C20:G23). Se arma igual, partiendo de 15 en la diagonal: $c^O_{jk} = C_O + (k-j)\,C_I$.

   | Producción \ Consumo | 1 | 2 | 3 | 4 | 5 (inv. final) |
   |---|---|---|---|---|---|
   | 1 | 15 | 19 | 23 | 27 | 31 |
   | 2 | 1000 | 15 | 19 | 23 | 27 |
   | 3 | 1000 | 1000 | 15 | 19 | 23 |
   | 4 | 1000 | 1000 | 1000 | 15 | 19 |

### Hoja `PRODUCCION`: modelo de transporte y solución con Solver

**Objetivo:** encontrar las horas $R_{jk}$ (regulares) y $O_{jk}$ (extra) producidas en el mes $j$ para el mes de consumo $k$ que minimizan el costo total.

**Estructura de la hoja**

| Rango | Contenido |
|---|---|
| D5:H8 | Variables $R_{jk}$: horas regulares (filas = mes de producción 1-4, columnas = mes de consumo 1-5) |
| D13:H16 | Variables $O_{jk}$: horas extra |
| I5:I8 | Horas regulares usadas: I5 `=SUM(D5:H5)`, I6 `=SUM(E6:H6)`, I7 `=SUM(F7:H7)`, I8 `=SUM(G8:H8)`. Solo suman desde la diagonal |
| J5:J8 | Capacidad regular: 160 |
| I13:I16 | Horas extra usadas: I13 tiene el **texto «-»**, I14 `=SUM(E14:H14)`, I15 `=SUM(F15:H15)`, I16 `=SUM(G16:H16)` |
| J13:J16 | Capacidad extra: 40 |
| D19:H19 | Demanda satisfecha: $\sum_{j \le k}(R_{jk}+O_{jk})$, p. ej. F19 `=SUM(F5:F7,F13:F15)` |
| D20:H20 | «Demanda Neta», escrita a mano: 64, 158, 194, 180, 80 (el 80 es el inventario final) |
| C23 | `=SUMPRODUCT(COSTOS!C12:G15,D5:H8)`: costo regular |
| C24 | `=SUMPRODUCT(COSTOS!C20:G23,D13:H16)`: costo extra |
| C25 | `=SUM(C23:C24)`: costo total (celda objetivo) |
| L5 | «investiario total» `=SUM(E5:H5,E13:H13)` = 52: horas producidas en el mes 1 para meses posteriores, es decir, el inventario que sale del mes 1 |

**Configuración de Solver** (guardada en los nombres ocultos de la hoja)

| Elemento | Valor |
|---|---|
| Objetivo | C25, minimizar (`solver_typ = 2`) |
| Celdas variables | D5:H8 y D13:H16 |
| Restricción 1 | D19:H19 = D20:H20 (satisfacer la demanda) |
| Restricción 2 | I13:I16 ≤ J13:J16 (capacidad extra) |
| Restricción 3 | I5:I8 ≤ J5:J8 (capacidad regular) |
| No negatividad | sí (`solver_neg = 1`) |
| Motor | Simplex LP (`solver_eng = 2`) |

**Modelo matemático equivalente** (Bowman, L10 p. 54):

$$\min Z = \sum_{j=1}^{4}\sum_{k=1}^{5}\left(c^R_{jk}R_{jk} + c^O_{jk}O_{jk}\right)$$

$$\text{s.a.}\quad \sum_{k} R_{jk} \le 160,\qquad \sum_{k} O_{jk} \le 40 \quad \forall j;\qquad \sum_{j=1}^{4}\left(R_{jk}+O_{jk}\right) = D_k \quad \forall k;\qquad R_{jk}, O_{jk} \ge 0$$

con $D = (64, 158, 194, 180, 80)$.

**Resultados (solución guardada)**

Horas en tiempo regular $R_{jk}$:

| Producción \ Consumo | 1 | 2 | 3 | 4 | 5 (inv. final) | Usadas | Capacidad |
|---|---|---|---|---|---|---|---|
| 1 | 64 | 0 | 0 | 12 | 40 | 116 | 160 |
| 2 | 0 | 158 | 0 | 2 | 0 | 160 | 160 |
| 3 | 0 | 0 | 154 | 6 | 0 | 160 | 160 |
| 4 | 0 | 0 | 0 | 160 | 0 | 160 | 160 |

Horas en tiempo extra $O_{jk}$:

| Producción \ Consumo | 1 | 2 | 3 | 4 | 5 (inv. final) | Usadas | Capacidad |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0 | 0 | «-» | 40 |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 40 |
| 3 | 0 | 0 | 40 | 0 | 0 | 40 | 40 |
| 4 | 0 | 0 | 0 | 0 | 40 | 40 | 40 |

| Concepto | Mes 1 | Mes 2 | Mes 3 | Mes 4 | Mes 5 (inv. final) |
|---|---|---|---|---|---|
| Demanda satisfecha (fila 19) | 64 | 158 | 194 | 180 | 80 |
| Demanda neta (fila 20) | 64 | 158 | 194 | 180 | 80 |

Plan consolidado (deducido de las tablas): regulares 116, 160, 160 y 160 h; extra 0, 0, 40 y 40 h; totales 116, 160, 200 y 200 h. Es el mismo plan de L10 p. 66.

Costos: **regular \$6784** (C23) + **extra \$1360** (C24) = **costo total \$8144** (C25).
- Detalle regular: $64(10)+12(22)+40(26)+158(10)+2(18)+154(10)+6(14)+160(10) = 6784$.
- Detalle extra: $40(15)+40(19) = 1360$.

**Gráficos:** el libro no tiene gráficos.

**Conclusión del ejemplo:** el costo mínimo coincide con el de la presentación (\$8144, L10 p. 67). El plan usa todo el tiempo regular de los meses 2 a 4 y deja libres 44 h regulares en el mes 1. Usa además todo el tiempo extra de los meses 3 y 4. Las 80 h de inventario final se cubren con 40 h regulares del mes 1 (a \$26) y 40 h extra del mes 4 (a \$19).

La asignación celda por celda **no es la misma** de L10 p. 65. La presentación pone, por ejemplo, 52 h regulares del mes 1 al inventario final, y 32 + 8 h extra en el mes 3. Ambas son **óptimos alternativos**, porque tienen el mismo costo y las mismas horas por mes y por régimen.

Esto pasa porque el costo de almacenar depende solo de cuántas horas-mes se guardan en total. Ese total queda fijo con la producción de cada mes, sin importar a qué mes de consumo se asigne cada hora. Un re-cálculo propio con PL (HiGHS) también da \$8144, con una tercera asignación distinta.

### Observaciones

- **Rótulos invertidos de inventario inicial.** K10 dice «producto A» = 220 y K11 «producto B» = 36, pero los datos de L10 p. 55 son A = 36 y B = 220. La fórmula F3 usa K11 = 36 para A, así que el cálculo está bien y solo están mal los rótulos.
- **Fórmulas con números escritos a mano.**
  - F4 tiene el 170 fijo, que equivale a $190-(220-200)$.
  - Las matrices de costo usan 10, 15 y "+4" fijos en lugar de referenciar K3, K4 y K5.
  - La fila 20 (demanda neta) está escrita a mano en vez de enlazar con `COSTOS!F3:F6`.
  - Si cambian los parámetros, el modelo no se actualiza.
- **F3 mezcla unidades.** `=C3-$K$11*$K$8` resta "inventario × horas por unidad" a una demanda en unidades. Funciona solo porque $h_A = 1$. La forma general sería $(A_1 - I_A)\,h_A + \max(0, B_1 - I_B)\,h_B$.
- **I13 contiene el texto «-»** en lugar de `=SUM(D13:H13)`. Por eso la restricción de capacidad extra del mes 1 no controla nada. No afecta a la solución porque esas celdas valen 0.
- Las sumas de capacidad (I6:I8, I14:I16) excluyen las celdas bajo la diagonal. Esas celdas son variables, pero su costo de 1000 impide que se usen.
- El «mes 5» de las tablas es el **inventario final** de 80 h que da la presentación (L10 p. 62). Ni la hoja ni la presentación explican de dónde sale ese valor.
- «Costo almacenamiento (\$/unidad)» es en realidad \$4 por hora agregada y por mes (L10 p. 55: «productos hechos en una hora»).
- Erratas en los rótulos: «Capaciad de horas», «investiario total», «costo total horaExtra».
- No hay hojas vacías ni gráficos.

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `COSTOS` — 23 filas × 11 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 |  | mes | producto A | producto B | demanda agregada (horas) | Demanda neta |  |  |  | Parámetros | Valor |
| 3 |  | 1 | 100 | 200 | 180 | 64 |  |  |  | Costo hora regular ($/hora) | 10 |
| 4 |  | 2 | 90 | 190 | 166 | 158 |  |  |  | Costo hora extra ($/hora) | 15 |
| 5 |  | 3 | 110 | 210 | 194 | 194 |  |  |  | Costo almacenamiento ($/unidad) | 4 |
| 6 |  | 4 | 100 | 200 | 180 | 180 |  |  |  | Capacidad regular (horas/mes) | 160 |
| 7 |  |  | 400 | 800 | 720 | 596 |  |  |  | Capacidad extra (horas/mes) | 40 |
| 8 |  |  |  |  |  |  |  |  |  | Horas por unidad – producto A | 1 |
| 9 |  |  | COSTOS UNITARIOS en periodo REGULAR |  |  |  |  |  |  | Horas por unidad – producto B | 0.4 |
| 10 |  |  | Mes de consumo |  |  |  |  |  |  | Inventario inicial – producto A (unid.) | 220 |
| 11 |  | mes | 1 | 2 | 3 | 4 | 5 |  |  | Inventario inicial – producto B (unid.) | 36 |
| 12 | Mes de produccion | 1 | 10 | 14 | 18 | 22 | 26 |  |  |  |  |
| 13 |  | 2 | 1000 | 10 | 14 | 18 | 22 |  |  |  |  |
| 14 |  | 3 | 1000 | 1000 | 10 | 14 | 18 |  |  |  |  |
| 15 |  | 4 | 1000 | 1000 | 1000 | 10 | 14 |  |  |  |  |
| 17 |  |  | COSTOS UNITARIOS en periodo EXTRA |  |  |  |  |  |  |  |  |
| 18 |  |  | Mes de consumo |  |  |  |  |  |  |  |  |
| 19 |  | MES | 1 | 2 | 3 | 4 | 5 |  |  |  |  |
| 20 | Mes de produccion | 1 | 15 | 19 | 23 | 27 | 31 |  |  |  |  |
| 21 |  | 2 | 1000 | 15 | 19 | 23 | 27 |  |  |  |  |
| 22 |  | 3 | 1000 | 1000 | 15 | 19 | 23 |  |  |  |  |
| 23 |  | 4 | 1000 | 1000 | 1000 | 15 | 19 |  |  |  |  |

**Fórmulas (12 patrones distintos):**

- `E3`: `=C3*$K$8+D3*$K$9`
- `F3`: `=C3-$K$11*$K$8+0*$K$9`
- `F4`: `=C4*$K$8+170*$K$9`
- `C7`: `=SUM(C3:C6)`
- `D7`: `=SUM(D3:D6)`
- `E7`: `=SUM(E3:E6)`
- `F7`: `=SUM(F3:F6)`
- `D12`: `=C12+4`
- `E12`: `=D12+4`
- `F12`: `=E12+4`
- `G12`: `=F12+4`
- `G15`: `=10+4`

### Hoja `PRODUCCION` — 25 filas × 12 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K | L |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 |  |  |  | UNIDADES DE PRODUCCION en periodo REGULAR |  |  |  |  |  |  |  |  |
| 3 |  |  |  | Mes de consumo |  |  |  |  |  |  |  |  |
| 4 |  |  | mes | 1 | 2 | 3 | 4 | 5 | Capaciad de horas  REGULAR |  |  | investiario total |
| 5 |  | Mes de produccion | 1 | 64 | 0 | 0 | 12 | 40 | 116 | 160 |  | 52 |
| 6 |  |  | 2 | 0 | 158 | 0 | 2 | 0 | 160 | 160 |  |  |
| 7 |  |  | 3 | 0 | 0 | 154 | 6 | 0 | 160 | 160 |  |  |
| 8 |  |  | 4 | 0 | 0 | 0 | 160 | 0 | 160 | 160 |  |  |
| 10 |  |  |  | UNIDADES DE PRODUCCION en periodo EXTRA |  |  |  |  |  |  |  |  |
| 11 |  |  |  | Mes de consumo |  |  |  |  |  |  |  |  |
| 12 |  |  | mes | 1 | 2 | 3 | 4 | 5 | Capaciad de horas EXTRA |  |  |  |
| 13 |  | Mes de produccion | 1 | 0 | 0 | 0 | 0 | 0 | - | 40 |  |  |
| 14 |  |  | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 40 |  |  |
| 15 |  |  | 3 | 0 | 0 | 40 | 0 | 0 | 40 | 40 |  |  |
| 16 |  |  | 4 | 0 | 0 | 0 | 0 | 40 | 40 | 40 |  |  |
| 19 |  | Demanda Satisfecha |  | 64 | 158 | 194 | 180 | 80 |  |  |  |  |
| 20 |  | Demanda Neta |  | 64 | 158 | 194 | 180 | 80 |  |  |  |  |
| 23 |  | Costo Total hora regular | 6784 |  |  |  |  |  |  |  |  |  |
| 24 |  | Costo total horaExtra | 1360 |  |  |  |  |  |  |  |  |  |
| 25 |  | Costo total | 8144 |  |  |  |  |  |  |  |  |  |

**Fórmulas (12 patrones distintos):**

- `I5`: `=SUM(D5:H5)`
- `L5`: `=SUM(E5:H5,E13:H13)`
- `I6`: `=SUM(E6:H6)`
- `I7`: `=SUM(F7:H7)`
- `I8`: `=SUM(G8:H8)`
- `D19`: `=SUM(D5,D13)`
- `E19`: `=SUM(E5:E6,E13:E14)`
- `F19`: `=SUM(F5:F7,F13:F15)`
- `G19`: `=SUM(G5:G8,G13:G16)`
- `H19`: `=SUM(H5:H8,H13:H16)`
- `C23`: `=SUMPRODUCT(COSTOS!C12:G15,D5:H8)`
- `C25`: `=SUM(C23:C24)`

