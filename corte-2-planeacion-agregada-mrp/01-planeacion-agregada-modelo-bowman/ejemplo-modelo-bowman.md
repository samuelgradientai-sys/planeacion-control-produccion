# ejemplo-modelo-bowman

> **Archivo:** [`ejemplo-modelo-bowman.xlsx`](./ejemplo-modelo-bowman.xlsx) · **Corte 2** (el archivo estaba en la carpeta `CORTE 3/` del estudiante) · Libro de Excel con 1 hoja(s): `Hoja1`  
> **Nombre original:** `CORTE 3/Ejemplo Modelo Bowman.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Es **el mismo ejercicio** que [modelo-bowman.md](./modelo-bowman.md): el ejemplo del modelo de Bowman de la clase [L10 – Aggregate planning](./L10-aggregate-planning.md), pp. 55-67. Tiene los productos A y B, 4 meses y tiempo regular y extra, con capacidad de 160 h y 40 h por mes. Aquí todo está reorganizado en **una sola hoja**, `Hoja1`.

Los datos, la solución que encuentra Solver y el costo mínimo (**\$8144**) son idénticos a los de `modelo-bowman.xlsx`. No es otro ejercicio, sino una versión más ordenada:
- los costos están enlazados a celdas de parámetros;
- los rótulos de inventario inicial son correctos;
- se controla la capacidad extra del mes 1.

A cambio, introduce una fórmula rara para la demanda del inventario final (ver Observaciones).

El archivo venía de la carpeta del Corte 3 (nombre original `CORTE 3/Ejemplo Modelo Bowman.xlsx`), por eso la cabecera automática dice «Corte 3». Su tema es del Corte 2.

Con él se aprende lo mismo que con el otro libro:
1. agregar la demanda en horas y calcular la demanda neta;
2. armar la matriz de costos $C + (k-j)C_I$;
3. resolver el problema de transporte con Solver.

### Hoja `Hoja1`

**Objetivo (deducido):** minimizar el costo de producción más almacenamiento para cubrir la demanda neta agregada de los meses 1 a 4 y un inventario final de 80 h, con tiempo regular y extra.

**Datos de entrada (B2:F7)**

| Mes | Demanda Producto A | Demanda Producto B | Demanda Agregada Bruta (h), col. E | Demanda Neta (h), col. F |
|---|---|---|---|---|
| 1 | 100 | 200 | 180 | 64 |
| 2 | 90 | 190 | 166 | 158 |
| 3 | 110 | 210 | 194 | 194 |
| 4 | 100 | 200 | 180 | 180 |
| **Total (fila 7)** | 400 | 800 | – | – |

**Parámetros**

| Celda | Parámetro | Valor |
|---|---|---|
| C9 | Inventario Inicial A | 36 |
| C10 | Inventario Inicial B | 220 |
| F9 | Tiempo Producción A (h/unid.), $h_A$ | 1 |
| F10 | Tiempo Producción B (h/unid.), $h_B$ | 0.4 |
| I8 | Costo Producción Regular, $C_R$ (\$/h) | 10 |
| I9 | Costo Producción Extra, $C_O$ (\$/h) | 15 |
| I10 | Costo de Almacenamiento, $C_I$ (\$/h-mes) | 4 |
| Q15:Q18 | Capacidad regular máxima por mes (h) | 160 |
| Q22:Q25 | Capacidad extra máxima por mes (h) | 40 |

**Método paso a paso**

1. **Demanda agregada bruta** (E3:E6), `=C3*$F$9+D3*$F$10`: $D^{bruta}_t = 1{,}0\,A_t + 0{,}4\,B_t$, que da 180, 166, 194 y 180.
2. **Demanda neta** (F3:F6):
   - F3 `=(C3-C9)*F9+0*F10`, es decir $(100-36)\cdot1 + 0 = 64$. B no aporta porque su inventario de 220 cubre el mes 1.
   - F4 `=C4*F9+170*F10`, es decir $90 + 170\cdot0{,}4 = 158$. El 170 está fijo y equivale a $190-20$.
   - F5 y F6 son iguales a la bruta: 194 y 180.
3. **Matriz de costos regular** (C15:G18), con filas = mes de producción, columnas = mes de consumo 1-5 y la columna 5 como inventario final.
   - La diagonal es `=$I$8` (10).
   - Hacia la derecha cada celda es `=celda izquierda + $I$10`, o sea +4.
   - Bajo la diagonal hay un 1000 fijo (prohibido, porque no hay backlog).
   - Fórmula: $c^R_{jk} = C_R + (k-j)C_I$.

   | Producción \ Consumo | 1 | 2 | 3 | 4 | 5 |
   |---|---|---|---|---|---|
   | 1 | 10 | 14 | 18 | 22 | 26 |
   | 2 | 1000 | 10 | 14 | 18 | 22 |
   | 3 | 1000 | 1000 | 10 | 14 | 18 |
   | 4 | 1000 | 1000 | 1000 | 10 | 14 |

4. **Matriz de costos extra** (C22:G25). La diagonal es `=I9` (15) y hacia la derecha se suma `$I$10`: $c^O_{jk} = C_O + (k-j)C_I$.

   | Producción \ Consumo | 1 | 2 | 3 | 4 | 5 |
   |---|---|---|---|---|---|
   | 1 | 15 | 19 | 23 | 27 | 31 |
   | 2 | 1000 | 15 | 19 | 23 | 27 |
   | 3 | 1000 | 1000 | 15 | 19 | 23 |
   | 4 | 1000 | 1000 | 1000 | 15 | 19 |

5. **Demanda del mes 5 (inventario final)**. G19 `=SUM(G15:G18)` = 26 + 22 + 18 + 14 = **80**, con el rótulo «Costo Demanda Neta P5». La fila 28 toma ese valor en O28 `=G19`.
6. **Variables y restricciones**
   - Variables: K15:O18 (horas regulares $R_{jk}$) y K22:O25 (horas extra $O_{jk}$).
   - Horas usadas: P15 `=SUM(K15:O15)`, P16 `=SUM(L16:O16)`, P17 `=SUM(M17:O17)` y P18 `=SUM(N18:O18)`. Para el tiempo extra se usan las mismas sumas en P22:P25.
   - Demanda satisfecha: K27:O27, por ejemplo M27 `=SUM(M15:M17,M22:M24)`.
   - Demanda neta: K28:N28 `=F3`…`=F6` y O28 `=G19`.
7. **Costos**
   - K30 `=SUMPRODUCT(K15:O18,C15:G18)`: costo regular.
   - K31 `=SUMPRODUCT(K22:O25,C22:G25)`: costo extra.
   - K32 `=SUM(K30:K31)`: costo total.

**Configuración de Solver** (nombres ocultos de la hoja)

| Elemento | Valor |
|---|---|
| Objetivo | K32, minimizar (`solver_typ = 2`) |
| Celdas variables | K15:O18 y K22:O25 |
| Restricción 1 | K27:O27 = K28:O28 (demanda) |
| Restricción 2 | P15:P18 ≤ Q15:Q18 (capacidad regular) |
| Restricción 3 | P22:P25 ≤ Q22:Q25 (capacidad extra) |
| Opciones | no negativas (`solver_neg = 1`), modelo lineal (`solver_lin = 1`), motor Simplex LP (`solver_eng = 2`) |

El modelo matemático es el de Bowman (L10 p. 54):

$$\min Z=\sum_{j=1}^{4}\sum_{k=1}^{5}\left(c^R_{jk}R_{jk}+c^O_{jk}O_{jk}\right)$$

sujeto a

$$\sum_k R_{jk}\le160,\qquad \sum_k O_{jk}\le40,\qquad \sum_j (R_{jk}+O_{jk})=D_k$$

con $D=(64,158,194,180,80)$.

**Resultados**

Horas regulares (K15:O18), con «Usada» en P y «Máxima» en Q:

| Producción \ Consumo | 1 | 2 | 3 | 4 | 5 | Usada | Máxima |
|---|---|---|---|---|---|---|---|
| 1 | 64 | 0 | 0 | 12 | 40 | 116 | 160 |
| 2 | 0 | 158 | 0 | 2 | 0 | 160 | 160 |
| 3 | 0 | 0 | 154 | 6 | 0 | 160 | 160 |
| 4 | 0 | 0 | 0 | 160 | 0 | 160 | 160 |

Horas extra (K22:O25):

| Producción \ Consumo | 1 | 2 | 3 | 4 | 5 | Usada | Máxima |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 40 |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 40 |
| 3 | 0 | 0 | 40 | 0 | 0 | 40 | 40 |
| 4 | 0 | 0 | 0 | 0 | 40 | 40 | 40 |

| Fila | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Demanda Satisfecha (27) | 64 | 158 | 194 | 180 | 80 |
| Demanda Neta (28) | 64 | 158 | 194 | 180 | 80 |

Resultados de costo:
- Costo Total Hora Regular (K30) = **\$6784**.
- Costo Total Hora Extra (K31) = **\$1360**.
- **Costo Total (K32) = \$8144**.

**Gráficos:** no tiene.

**Conclusión del ejemplo:** se obtiene el mismo óptimo que en `modelo-bowman.xlsx`, celda por celda, y el mismo costo mínimo de la presentación (\$8144).

El plan consolidado es:
- tiempo regular: 116, 160, 160 y 160 h;
- tiempo extra: 0, 0, 40 y 40 h.

La asignación concreta difiere de la de L10 p. 65, pero el costo es el mismo: son óptimos alternativos. La explicación está en [modelo-bowman.md](./modelo-bowman.md).

### Comparación con `modelo-bowman.xlsx`

| Aspecto | `modelo-bowman.xlsx` | `ejemplo-modelo-bowman.xlsx` |
|---|---|---|
| Hojas | 2 (`COSTOS`, `PRODUCCION`) | 1 (`Hoja1`) |
| Datos (demanda, tiempos, costos, capacidades) | Iguales | Iguales |
| Inventario inicial | Rótulos invertidos (dice A = 220, B = 36) | Rótulos correctos (A = 36, B = 220) |
| Costos de las matrices | Números fijos (10, 15, +4) | Enlazados a I8, I9 e I10 |
| Demanda neta en el modelo | Escrita a mano (fila 20) | Enlazada a F3:F6; el mes 5 sale de G19 |
| Capacidad extra del mes 1 | Celda con «-» (no se controla) | `=SUM(K22:O22)` (se controla) |
| Solución y costo | 6784 + 1360 = 8144 | Idéntica: 6784 + 1360 = 8144 |

**Veredicto:** es el mismo ejercicio, con los mismos datos y la misma solución. Este libro es una versión reordenada y algo más limpia del otro.

### Observaciones

- **El 80 del inventario final sale de una suma de costos.** G19 `=SUM(G15:G18)` suma los costos regulares de la columna 5 (26 + 22 + 18 + 14) y el resultado es 80 por coincidencia. En la presentación (L10 p. 62) las 80 h son un dato de demanda del «Inventario Final», no una suma de costos. El rótulo «Costo Demanda Neta P5» lo confirma. Si se cambia $C_R$ o $C_I$, la demanda del mes 5 cambiaría sin razón.
- F4 tiene el 170 escrito a mano, igual que en el otro libro. Los 1000 de las celdas prohibidas también son fijos.
- F3 `=(C3-C9)*F9+0*F10` está bien para el producto A, pero el término de B se anula a mano (`0*F10`) en lugar de calcular $\max(0, B_1 - I_B)$.
- C20 dice «Mes de Consumo Periodo Regular» encima de la matriz de costos **extra**. Debería decir «Extra». K20 sí está bien.
- La columna E no tiene total (en el otro libro E7 = 720).
- Las sumas de «Usada» excluyen las celdas bajo la diagonal. Esas celdas cuestan 1000, así que nunca se usan.
- La cabecera automática de este .md dice «Corte 3» porque el archivo estaba en esa carpeta. El contenido es del Corte 2.

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `Hoja1` — 32 filas × 17 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 |  | Mes | Demanda Producto A | Demanda Producto B | Demanda Agregada Bruta | Demanda Neta |  |  |  |  |  |  |  |  |  |  |  |
| 3 |  | 1 | 100 | 200 | 180 | 64 |  |  |  |  |  |  |  |  |  |  |  |
| 4 |  | 2 | 90 | 190 | 166 | 158 |  |  |  |  |  |  |  |  |  |  |  |
| 5 |  | 3 | 110 | 210 | 194 | 194 |  |  |  |  |  |  |  |  |  |  |  |
| 6 |  | 4 | 100 | 200 | 180 | 180 |  |  |  |  |  |  |  |  |  |  |  |
| 7 |  | Total | 400 | 800 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 |  |  |  |  |  |  |  | Costo Producción Regular | 10 |  |  |  |  |  |  |  |  |
| 9 |  | Inventario Inicial A | 36 |  | Tiempo Producción A | 1 |  | Costo Producción Extra | 15 |  |  |  |  |  |  |  |  |
| 10 |  | Inventario Inicial B | 220 |  | Tiempo Producción B | 0.4 |  | Costo de Almacenamiento | 4 |  |  |  |  |  |  |  |  |
| 12 | Costo Unitarios |  |  |  |  |  |  |  | Unidades de Producción |  |  |  |  |  |  |  |  |
| 13 |  |  | Mes de Consumo Periodo Regular |  |  |  |  |  |  |  | Mes de Consumo Periodo Regular |  |  |  |  | Capacidad de Producción |  |
| 14 | Mes de Producción | Mes | 1 | 2 | 3 | 4 | 5 |  | Mes de Producción | Mes | 1 | 2 | 3 | 4 | 5 | Usada | Máxima |
| 15 |  | 1 | 10 | 14 | 18 | 22 | 26 |  |  | 1 | 64 | 0 | 0 | 12 | 40 | 116 | 160 |
| 16 |  | 2 | 1000 | 10 | 14 | 18 | 22 |  |  | 2 | 0 | 158 | 0 | 2 | 0 | 160 | 160 |
| 17 |  | 3 | 1000 | 1000 | 10 | 14 | 18 |  |  | 3 | 0 | 0 | 154 | 6 | 0 | 160 | 160 |
| 18 |  | 4 | 1000 | 1000 | 1000 | 10 | 14 |  |  | 4 | 0 | 0 | 0 | 160 | 0 | 160 | 160 |
| 19 |  |  |  |  |  | Costo Demanda Neta P5 | 80 |  |  |  |  |  |  |  |  |  |  |
| 20 |  |  | Mes de Consumo Periodo Regular |  |  |  |  |  |  |  | Mes de Consumo Periodo Extra |  |  |  |  | Capacidad de Producción |  |
| 21 | Mes de Producción | Mes | 1 | 2 | 3 | 4 | 5 |  | Mes de Producción | Mes | 1 | 2 | 3 | 4 | 5 | Usada | Máxima |
| 22 |  | 1 | 15 | 19 | 23 | 27 | 31 |  |  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 40 |
| 23 |  | 2 | 1000 | 15 | 19 | 23 | 27 |  |  | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 40 |
| 24 |  | 3 | 1000 | 1000 | 15 | 19 | 23 |  |  | 3 | 0 | 0 | 40 | 0 | 0 | 40 | 40 |
| 25 |  | 4 | 1000 | 1000 | 1000 | 15 | 19 |  |  | 4 | 0 | 0 | 0 | 0 | 40 | 40 | 40 |
| 27 |  |  |  |  |  |  |  |  |  | Demanda Satisfecha | 64 | 158 | 194 | 180 | 80 |  |  |
| 28 |  |  |  |  |  |  |  |  |  | Demanda Neta | 64 | 158 | 194 | 180 | 80 |  |  |
| 30 |  |  |  |  |  |  |  |  |  | Costo Total Hora Regular | 6784 |  |  |  |  |  |  |
| 31 |  |  |  |  |  |  |  |  |  | Costo Total Hora Extra | 1360 |  |  |  |  |  |  |
| 32 |  |  |  |  |  |  |  |  |  | Costo Total | 8144 |  |  |  |  |  |  |

**Fórmulas (25 patrones distintos):**

- `E3`: `=C3*$F$9+D3*$F$10`
- `F3`: `=(C3-C9)*F9+0*F10`
- `F4`: `=C4*F9+170*F10`
- `C7`: `=SUM(C3:C6)`
- `D7`: `=SUM(D3:D6)`
- `C15`: `=$I$8`
- `D15`: `=C15+$I$10`
- `E15`: `=D15+$I$10`
- `F15`: `=E15+$I$10`
- `G15`: `=F15+$I$10`
- `P15`: `=SUM(K15:O15)`
- `P16`: `=SUM(L16:O16)`
- `P17`: `=SUM(M17:O17)`
- `F18`: `=I8`
- `P18`: `=SUM(N18:O18)`
- `G19`: `=SUM(G15:G18)`
- `K27`: `=SUM(K15,K22)`
- `L27`: `=SUM(L15:L16,L22:L23)`
- `M27`: `=SUM(M15:M17,M22:M24)`
- `N27`: `=SUM(N15:N18,N22:N25)`
- `O27`: `=SUM(O15:O18,O22:O25)`
- `K28`: `=F3`
- `O28`: `=G19`
- `K30`: `=SUMPRODUCT(K15:O18,C15:G18)`
- `K32`: `=SUM(K30:K31)`

