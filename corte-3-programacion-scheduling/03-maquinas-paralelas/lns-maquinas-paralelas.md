# lns-maquinas-paralelas

> **Archivo:** [`lns-maquinas-paralelas.xlsx`](./lns-maquinas-paralelas.xlsx) · **Corte 3** · Libro de Excel con 1 hoja(s): `LFJ`  
> **Nombre original:** `CORTE 3/LNS.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Plantilla de Excel **incompleta** para el tema de máquinas paralelas ([L18](./L18-parallel-machine-scheduling.md)). El archivo se llamaba `LNS.xlsx` (*Largest Number of Successors*) y su única hoja se llama `LFJ` (*Least Flexible Job first*). Sin embargo, no tiene precedencias ni conjuntos de máquinas elegibles: solo 15 trabajos con $p_j$ y $w_j$ y una estructura para repartirlos en 3 máquinas. Todo indica (deducido) que se empezó a construir en clase para programar 3 máquinas paralelas idénticas con una regla de lista ($P3||C_{max}$, $P3||\sum C_j$ o $P3||\sum w_jC_j$) y no se terminó.

Se aprende cómo armar en Excel la asignación de trabajos a máquinas: una columna con el número de máquina de cada trabajo, y por máquina un filtro con `IF` y un tiempo de terminación acumulado.

### Hoja `LFJ`

**Objetivo (deducido):** asignar 15 trabajos a 3 máquinas y calcular el tiempo de terminación de cada trabajo en su máquina.

**Datos de entrada** (B2:D17):

| Job | $P_j$ | $W_j$ |
|---|---|---|
| 1 | 10 | 1 |
| 2 | 20 | 2 |
| 3 | 25 | 3 |
| 4 | 22 | 1 |
| 5 | 17 | 2 |
| 6 | 28 | 3 |
| 7 | 20 | 1 |
| 8 | 26 | 2 |
| 9 | 27 | 3 |
| 10 | 20 | 1 |
| 11 | 12 | 2 |
| 12 | 28 | 3 |
| 13 | 26 | 1 |
| 14 | 21 | 2 |
| 15 | 19 | 3 |

$\sum P_j=321$; $P_j$ va de 10 a 28 (media 21.4). Los pesos se repiten en el ciclo 1, 2, 3.

**Parámetros / decisión:** columna F (`Máquina`), el número de máquina asignado a cada trabajo. Solo F3:F5 tienen valor (los trabajos 1, 2 y 3 en la máquina 3); el resto está vacío.

**Método (fórmulas):**

- Máquina 1 (G:I):
  - `G3 = IF(F3=1,B3,0)`: $J=j$ si el trabajo $j$ está en la máquina 1, si no 0.
  - `H3 = IF(G3>0,C3,0)`: $P_j$ del trabajo si está en la máquina 1.
  - `I3 = H3` y `I4 = H4+MAX($I$3,I3)`: tiempo acumulado $C_k=P_k+C_{k-1}$. Como la columna crece, `MAX($I$3,I3)` siempre vale `I3`. En las filas de trabajos que no están en la máquina 1 se repite el valor anterior.
- Máquina 2 (K:M): `K3 = IF(J3=1,F3,0)`, `L3 = IF(K3>0,G3,0)`, `M3 = L3`, `M4 = L4+MAX($I$3,M3)`. **Están mal:** son la copia de las de la máquina 1 corridas cuatro columnas. Prueban la columna J (vacía) contra 1 y devuelven F (el número de máquina) en vez del trabajo. Lo correcto sería `IF($F3=2,$B3,0)` y `IF(K3>0,$C3,0)`. Además solo llegan a la fila 5.
- Máquina 3 (O:Q): solo los encabezados; no tiene fórmulas.

**Resultados guardados:** todas las celdas calculadas valen 0. Ningún trabajo está asignado a la máquina 1, y las fórmulas de la máquina 2 no funcionan.

**Gráficos:** no hay.

**Conclusión:** la hoja no llega a un programa. Como referencia, este es un **cálculo propio** con el algoritmo de lista de L18, p. 4 (empates a la máquina de menor índice):

| Regla | Máquina 1 | Máquina 2 | Máquina 3 | $C_{max}$ | $\sum C_j$ | $\sum w_jC_j$ |
|---|---|---|---|---|---|---|
| LPT | 6, 13, 2, 7, 5 | 12, 3, 4, 15, 11 | 9, 8, 14, 10, 1 | 111 | 1069 | 1947 |
| SPT | 1, 15, 10, 3, 9 | 11, 2, 14, 8, 6 | 5, 7, 4, 13, 12 | 113 | **857** (óptimo, L18 p. 16) | 1898 |
| WSPT | 11, 5, 12, 8, 4 | 15, 9, 1, 14, 10 | 3, 6, 2, 7, 13 | 119 | 944 | 1618 |

Cota inferior del makespan (L18, p. 30): $\max(28,\ 321/3)=107$.

Gantt de la solución LPT (cálculo propio):

| Máquina | Trabajo | Inicio | Fin |
|---|---|---|---|
| 1 | 6 | 0 | 28 |
| 1 | 13 | 28 | 54 |
| 1 | 2 | 54 | 74 |
| 1 | 7 | 74 | 94 |
| 1 | 5 | 94 | 111 |
| 2 | 12 | 0 | 28 |
| 2 | 3 | 28 | 53 |
| 2 | 4 | 53 | 75 |
| 2 | 15 | 75 | 94 |
| 2 | 11 | 94 | 106 |
| 3 | 9 | 0 | 27 |
| 3 | 8 | 27 | 53 |
| 3 | 14 | 53 | 74 |
| 3 | 10 | 74 | 94 |
| 3 | 1 | 94 | 104 |

### Observaciones

- El nombre del archivo (LNS), el de la hoja (LFJ) y el contenido no coinciden. No hay datos de precedencia, que LNS necesita, ni conjuntos $M_j$, que LFJ necesita.
- Las fórmulas de la máquina 2 tienen referencias relativas mal copiadas, y la máquina 3 no tiene fórmulas.
- Las únicas asignaciones son F3:F5 = 3. La hoja quedó a medio hacer.
- Los ejemplos completos de LNS/CP y LFJ/LFM están en la hoja `08_Paralelas_Restric` del [compendio](../00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md) y en L18, pp. 17-26.

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `LFJ` — 17 filas × 17 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 |  |  |  |  |  |  | Máquina 1 |  |  |  | Máquina 2 |  |  |  | Máquina 3 |  |  |
| 2 |  | Job | Pj | Wj |  | Máquina | J | Pj | Cj |  | J | Pj | Cj |  | J | Pj | Cj |
| 3 |  | 1 | 10 | 1 |  | 3 | 0 | 0 | 0 |  | 0 | 0 | 0 |  |  |  |  |
| 4 |  | 2 | 20 | 2 |  | 3 | 0 | 0 | 0 |  | 0 | 0 | 0 |  |  |  |  |
| 5 |  | 3 | 25 | 3 |  | 3 | 0 | 0 | 0 |  | 0 | 0 | 0 |  |  |  |  |
| 6 |  | 4 | 22 | 1 |  |  | 0 | 0 | 0 |  |  |  |  |  |  |  |  |
| 7 |  | 5 | 17 | 2 |  |  | 0 | 0 | 0 |  |  |  |  |  |  |  |  |
| 8 |  | 6 | 28 | 3 |  |  | 0 | 0 | 0 |  |  |  |  |  |  |  |  |
| 9 |  | 7 | 20 | 1 |  |  | 0 | 0 | 0 |  |  |  |  |  |  |  |  |
| 10 |  | 8 | 26 | 2 |  |  | 0 | 0 | 0 |  |  |  |  |  |  |  |  |
| 11 |  | 9 | 27 | 3 |  |  | 0 | 0 | 0 |  |  |  |  |  |  |  |  |
| 12 |  | 10 | 20 | 1 |  |  | 0 | 0 | 0 |  |  |  |  |  |  |  |  |
| 13 |  | 11 | 12 | 2 |  |  | 0 | 0 | 0 |  |  |  |  |  |  |  |  |
| 14 |  | 12 | 28 | 3 |  |  | 0 | 0 | 0 |  |  |  |  |  |  |  |  |
| 15 |  | 13 | 26 | 1 |  |  | 0 | 0 | 0 |  |  |  |  |  |  |  |  |
| 16 |  | 14 | 21 | 2 |  |  | 0 | 0 | 0 |  |  |  |  |  |  |  |  |
| 17 |  | 15 | 19 | 3 |  |  | 0 | 0 | 0 |  |  |  |  |  |  |  |  |

**Fórmulas (8 patrones distintos):**

- `G3`: `=IF(F3=1,B3,0)`
- `H3`: `=IF(G3>0,C3,0)`
- `I3`: `=H3`
- `K3`: `=IF(J3=1,F3,0)`
- `L3`: `=IF(K3>0,G3,0)`
- `M3`: `=L3`
- `I4`: `=H4+MAX($I$3,I3)`
- `M4`: `=L4+MAX($I$3,M3)`

