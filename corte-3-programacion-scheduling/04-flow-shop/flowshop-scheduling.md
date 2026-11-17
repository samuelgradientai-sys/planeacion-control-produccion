# flowshop-scheduling

> **Archivo:** [`flowshop-scheduling.xlsx`](./flowshop-scheduling.xlsx) · **Corte 3** · Libro de Excel con 4 hoja(s): `Regla de Johnson`, `Campbell `, `CDS`, `NEH`  
> **Nombre original:** `CORTE 3/Flowshop Schedulling .xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Libro de Excel de clase para el tema **flow shop** ([L19](./L19-flow-shop-scheduling.md)). Resuelve a mano, con fórmulas, los métodos para minimizar el makespan en un taller en serie:

1. `Regla de Johnson`: $F2||C_{max}$ con una secuencia al azar frente a la regla de Johnson, y $F3||C_{max}$ con la comprobación de dominancia y las máquinas ficticias.
2. `Campbell ` (el nombre tiene un espacio al final): el ejercicio CDS de L19, pp. 28-29 (5 trabajos, 4 máquinas). Solo la iteración 1 está bien terminada.
3. `CDS`: heurística CDS en otro caso de 5 trabajos y 5 máquinas.
4. `NEH`: heurística NEH con los mismos datos de la hoja `CDS`.

Se aprende a calcular $C_{ij}$ con la recursión del flow shop, a armar los grupos de Johnson, a construir las máquinas ficticias de CDS y a evaluar las inserciones de NEH.

**Recursión que usan todas las hojas** (L19, p. 5). Para el trabajo en la posición $k$ en la máquina $i$:

$$C_{1,[1]}=p_{1,[1]},\qquad C_{1,[k]}=C_{1,[k-1]}+p_{1,[k]},\qquad C_{i,[k]}=\max\left(C_{i,[k-1]},\,C_{i-1,[k]}\right)+p_{i,[k]}$$

En Excel aparece, por ejemplo, como `D28 = MAX(D27,C28)+D16`: el fin en la máquina 2 es el máximo entre el fin del trabajo anterior en la máquina 2 (`D27`) y el fin del mismo trabajo en la máquina 1 (`C28`), más el tiempo del trabajo en la máquina 2 (`D16`). La secuencia se escribe a mano en la columna de trabajos y cada fórmula apunta a mano a la fila del trabajo correspondiente; no se usa `VLOOKUP`.

No hay gráficos de Excel. La hoja `Regla de Johnson` tiene una imagen con la condición de dominancia.

---

### Hoja `Regla de Johnson`

#### Bloque 1 (B2:I11): secuencia al azar en 2 máquinas

**Objetivo (deducido):** mostrar el makespan de una secuencia arbitraria para compararlo después con el de Johnson.

**Datos de entrada** (B3:D8, los mismos del bloque 2):

| Job | $P_{1j}$ | $P_{2j}$ |
|---|---|---|
| A | 12 | 16 |
| B | 3 | 5 |
| C | 8 | 3 |
| D | 15 | 12 |
| E | 18 | 22 |
| F | 23 | 21 |

Nota en L2: "1. se acumulan los tiempos del primer trabajo y de la primera máquina".

**Secuencia (aleatoria)** D-C-F-A-E-B, con `H3 = C6`, `I3 = H3+D6`, `H4 = H3+C5`, `I4 = MAX(I3,H4)+D5`, etc.:

| Secuencia | $C_{1j}$ | $C_{2j}$ |
|---|---|---|
| D | 15 | 27 |
| C | 23 | 30 |
| F | 46 | 67 |
| A | 58 | 83 |
| E | 76 | 105 |
| B | 79 | 110 |

- $C_{max}$ = `H10 = I8` = **110**.
- "Tiempo de Flujo" = `H11 = AVERAGE(I3:I8)` = **70.33**, el promedio de los $C_{2j}$, es decir, $\bar F=\frac1n\sum_j C_j$ con $r_j=0$.

#### Bloque 2 (B13:F35): regla de Johnson para 2 máquinas

- Columna `Grupo` (E16:E21), escrita a mano: A 1, B 1, C 2, D 2, E 1, F 2. Grupo 1 si $P_{1j}<P_{2j}$; grupo 2 si $P_{1j}>P_{2j}$. Nota en F15: "Grupo: en qué máquina el trabajo va más rápido".
- B23:E24: "Grupo 1 - SPT" (nota: "mira los tiempos de la máquina 1 - SPT (menor a mayor)") → **B-A-E**. "Grupo 2 - LPT" (nota: "mira los tiempos de la máquina 2 - LPT (mayor a menor)") → **F-D-C**.

Programa resultante (B26:D32):

| Secuencia | $C_{1j}$ | $C_{2j}$ |
|---|---|---|
| B | 3 | 8 |
| A | 15 | 31 |
| E | 33 | 55 |
| F | 56 | 77 |
| D | 71 | 89 |
| C | 79 | 92 |

Gantt equivalente (inicio = fin − $p$):

| Máquina | Trabajo | Inicio | Fin |
|---|---|---|---|
| 1 | B | 0 | 3 |
| 1 | A | 3 | 15 |
| 1 | E | 15 | 33 |
| 1 | F | 33 | 56 |
| 1 | D | 56 | 71 |
| 1 | C | 71 | 79 |
| 2 | B | 3 | 8 |
| 2 | A | 15 | 31 |
| 2 | E | 33 | 55 |
| 2 | F | 56 | 77 |
| 2 | D | 77 | 89 |
| 2 | C | 89 | 92 |

- $C_{max}$ = `C34 = D32` = **92**, frente a 110 de la secuencia al azar.
- Tiempo de flujo = `C35 = AVERAGE(D27:D32)` = **58.67**.

#### Bloque 3 (H13:L57): Johnson para 3 máquinas

Encabezado: "Regla de Johnson (3 Máquinas) — se usa cuando la máquina de la mitad no tiene cuello de botella". La imagen anclada cerca de J13 muestra la condición de dominancia (L19, p. 10):

$$\max\{p_{2,j}\}\le\max\left\{\min_{\forall j}\{p_{1,j}\},\ \min_{\forall j}\{p_{3,j}\}\right\}$$

**Caso 1 (H15:K21), no cumple la condición:**

| Job | $P_{1j}$ | $P_{2j}$ | $P_{3j}$ |
|---|---|---|---|
| A | 12 | 16 | 8 |
| B | 3 | 5 | 7 |
| C | 8 | 3 | 11 |
| D | 15 | 12 | 14 |
| E | 18 | 22 | 27 |
| F | 23 | 21 | 10 |

`H23 = MAX(J16:J21)` = 22; `J23 = MAX(MIN(I16:I21),MIN(K16:K21))` = max(3, 7) = 7. 22 ≤ 7 es falso: `K23` = False (escrito a mano) y L23 dice "no se debe usar la regla de johnson de 3 máquinas". La hoja no sigue con este caso.

(Cálculo propio, fuera de la hoja: si se aplica Johnson de todos modos, la secuencia es B-C-E-F-D-A con $C_{max}=110$. Por enumeración de las 720 permutaciones, 110 también es el óptimo. Aquí la heurística acierta aunque la condición no se cumple.)

**Caso 2 (H26:K32), sí cumple:**

| Job | $P_{1j}$ | $P_{2j}$ | $P_{3j}$ |
|---|---|---|---|
| A | 12 | 6 | 18 |
| B | 13 | 5 | 17 |
| C | 8 | 3 | 14 |
| D | 15 | 12 | 14 |
| E | 18 | 2 | 27 |
| F | 23 | 2 | 13 |

`H34 = MAX(J27:J32)` = 12; `J34 = MAX(MIN(I27:I32),MIN(K27:K32))` = max(8, 13) = 13. 12 ≤ 13: `K34` = True (escrito a mano) y L34 dice "se debe usar la regla de johnson de 3 máquinas".

**Máquinas ficticias** (H36:K43): `I38 = SUM(I27:J27)` → $P'_{1j}=P_{1j}+P_{2j}$; `J38 = SUM(J27:K27)` → $P'_{2j}=P_{2j}+P_{3j}$. El grupo se escribe a mano.

| Job | $P'_{1j}$ | $P'_{2j}$ | Grupo |
|---|---|---|---|
| A | 18 | 24 | 1 |
| B | 18 | 22 | 1 |
| C | 11 | 17 | 1 |
| D | 27 | 26 | 2 |
| E | 20 | 29 | 1 |
| F | 25 | 15 | 2 |

Grupo 1 - SPT: **C-A-B-E** (A y B empatan con 18). Grupo 2 - LPT: **D-F**.

Programa (H48:K54):

| Secuencia | $C_{1j}$ | $C_{2j}$ | $C_{3j}$ |
|---|---|---|---|
| C | 8 | 11 | 25 |
| A | 20 | 26 | 44 |
| B | 33 | 38 | 61 |
| E | 51 | 53 | 88 |
| D | 66 | 78 | 102 |
| F | 89 | 91 | 115 |

Gantt equivalente:

| Máquina | Trabajo | Inicio | Fin |
|---|---|---|---|
| 1 | C | 0 | 8 |
| 1 | A | 8 | 20 |
| 1 | B | 20 | 33 |
| 1 | E | 33 | 51 |
| 1 | D | 51 | 66 |
| 1 | F | 66 | 89 |
| 2 | C | 8 | 11 |
| 2 | A | 20 | 26 |
| 2 | B | 33 | 38 |
| 2 | E | 51 | 53 |
| 2 | D | 66 | 78 |
| 2 | F | 89 | 91 |
| 3 | C | 11 | 25 |
| 3 | A | 26 | 44 |
| 3 | B | 44 | 61 |
| 3 | E | 61 | 88 |
| 3 | D | 88 | 102 |
| 3 | F | 102 | 115 |

- $C_{max}$ = `I56 = K54` = **115**. Tiempo de flujo = `I57 = AVERAGE(K49:K54)` = **72.5**.
- Por enumeración de las 720 permutaciones, 115 es el óptimo (cálculo propio), como garantiza la condición de dominancia.

**Conclusión:** Johnson reduce el makespan de 110 a 92 frente a un orden al azar. Con 3 máquinas y la máquina central dominada da el óptimo (115).

---

### Hoja `Campbell ` (CDS sobre el ejercicio de L19, p. 28)

**Objetivo:** aplicar CDS a $F4||C_{max}$ con 5 trabajos.

**Datos de entrada** (B2:F7):

| Trabajo | M1 | M2 | M3 | M4 |
|---|---|---|---|---|
| 1 | 1 | 13 | 6 | 2 |
| 2 | 10 | 12 | 18 | 18 |
| 3 | 17 | 9 | 13 | 4 |
| 4 | 12 | 17 | 2 | 6 |
| 5 | 11 | 3 | 5 | 16 |

**Iteración 1** ($P'_1=M1$, $P'_2=M4$; valores escritos a mano en C11:D15):

| Trabajo | $P'_{1j}$ | $P'_{2j}$ | Grupo |
|---|---|---|---|
| 1 | 1 | 2 | 1 |
| 2 | 10 | 18 | 1 |
| 3 | 17 | 4 | 2 |
| 4 | 12 | 6 | 2 |
| 5 | 11 | 16 | 1 |

Grupo 1 - SPT: 1 2 5. Grupo 2 - LPT: 4 3. Secuencia **1-2-5-4-3**. Tiempos de terminación (B21:F26, fórmulas correctas):

| Secuencia | M1 | M2 | M3 | M4 |
|---|---|---|---|---|
| 1 | 1 | 14 | 20 | 22 |
| 2 | 11 | 26 | 44 | 62 |
| 5 | 22 | 29 | 49 | 78 |
| 4 | 34 | 51 | 53 | 84 |
| 3 | 51 | 60 | 73 | 88 |

$C_{max}=88$, igual que en L19, p. 29.

**Iteración 2** ($P'_1=M1+M2$ con `C30 = C3+D3`; $P'_2=M3+M4$ con `D30 = E3+F3`):

| Trabajo | $P'_{1j}$ | $P'_{2j}$ | Grupo |
|---|---|---|---|
| 1 | 14 | 8 | 2 |
| 2 | 22 | 36 | 1 |
| 3 | 26 | 17 | 2 |
| 4 | 29 | 8 | 2 |
| 5 | 14 | 21 | 1 |

Grupo 1 - SPT: 5 2. Grupo 2 - LPT: 3 1 4. Secuencia **5-2-3-1-4**, la misma de L19. **El bloque de tiempos (B39:F44) está mal:** la columna M1 está vacía y las fórmulas suman los **tiempos de terminación de la iteración 1** en vez de los tiempos de proceso (p. ej. `D41 = MAX(D40,C41)+D22`). Por eso salen valores sin sentido (14, 34, 56, …, 342). El valor correcto es $C_{max}=85$ (L19, p. 29; verificado).

**Iteración 3** ($P'_1=M1+M2+M3$, `C48 = C3+D3+E3`; $P'_2=M2+M3+M4$, `D48 = D3+E3+F3`):

| Trabajo | $P'_{1j}$ | $P'_{2j}$ | Grupo (hoja) |
|---|---|---|---|
| 1 | 20 | 21 | 1 |
| 2 | 40 | 48 | 1 |
| 3 | 39 | 26 | 2 |
| 4 | 31 | 25 | 2 |
| 5 | 19 | 24 | **2 (error: 19 < 24, debería ser 1)** |

La hoja pone Grupo 1: 1 2 y Grupo 2: 3 4 5. Con el grupo correcto la secuencia es **5-1-2-3-4** y da $C_{max}=85$ (L19, p. 29; verificado). Además, el bloque de tiempos (B57:F62) copia la secuencia 5-2-3-1-4 de la iteración 2 y tiene fórmulas que apuntan al bloque roto anterior (`D59 = MAX(D58,C59)+D40`…). Los valores (0, 94, 261, 541, …, 799) no significan nada.

**Conclusión (con los valores correctos de L19):** CDS da 88, 85 y 85. Las mejores secuencias son 5-2-3-1-4 y 5-1-2-3-4, con $C_{max}=85$.

---

### Hoja `CDS` (5 trabajos × 5 máquinas)

**Objetivo:** aplicar CDS a $F5||C_{max}$. Las $m-1=4$ iteraciones están en la hoja.

**Datos de entrada** (B2:G7):

| Job | $P_{1j}$ | $P_{2j}$ | $P_{3j}$ | $P_{4j}$ | $P_{5j}$ |
|---|---|---|---|---|---|
| 1 | 20 | 30 | 0 | 5 | 9 |
| 2 | 17 | 14 | 25 | 28 | 17 |
| 3 | 20 | 30 | 12 | 16 | 24 |
| 4 | 30 | 19 | 9 | 5 | 23 |
| 5 | 10 | 4 | 12 | 7 | 2 |

(El trabajo 1 no usa la máquina 3: $P_{31}=0$.)

**Máquinas ficticias** ($k$ = iteración): $P'^{(k)}_{1j}=\sum_{i=1}^{k}P_{ij}$ y $P'^{(k)}_{2j}=\sum_{i=6-k}^{5}P_{ij}$. Por ejemplo, `C43 = C3+D3+E3` y `D43 = E3+F3+G3` para $k=3$. En la iteración 1 los valores están escritos a mano.

| Job | $k=1$: $P'_1$ / $P'_2$ / G | $k=2$: $P'_1$ / $P'_2$ / G | $k=3$: $P'_1$ / $P'_2$ / G | $k=4$: $P'_1$ / $P'_2$ / G |
|---|---|---|---|---|
| 1 | 20 / 9 / 2 | 50 / 14 / 2 | 50 / 14 / 2 | 55 / 44 / 2 |
| 2 | 17 / 17 / 1 | 31 / 45 / 1 | 56 / 70 / 1 | 84 / 84 / 1 |
| 3 | 20 / 24 / 1 | 50 / 40 / 2 | 62 / 52 / 2 | 78 / 82 / 1 |
| 4 | 30 / 23 / 2 | 49 / 28 / 2 | 58 / 37 / 2 | 63 / 56 / 2 |
| 5 | 10 / 2 / 2 | 14 / 9 / 2 | 26 / 21 / 2 | 33 / 25 / 2 |

(Los empates $P'_1=P'_2$ del trabajo 2 en $k=1$ y $k=4$ se asignan al grupo 1.)

| $k$ | Grupo 1 (SPT de $P'_1$) | Grupo 2 (LPT de $P'_2$) | Secuencia | $C_{max}$ |
|---|---|---|---|---|
| 1 | 2 3 | 4 1 5 | 2-3-4-1-5 | 159 |
| 2 | 2 | 3 4 1 5 | 2-3-4-1-5 | 159 (`K4` escrito a mano: la secuencia repite la de $k=1$, así que no se recalcula) |
| 3 | 2 | 3 4 5 1 | 2-3-4-5-1 | 159 |
| 4 | 3 2 | 4 1 5 | 3-2-4-1-5 | 168 |

**Tiempos de terminación** de cada secuencia (filas 21-26, 52-57 y 71-76):

$k=1$ y $k=2$, secuencia 2-3-4-1-5:

| Job | $C_1$ | $C_2$ | $C_3$ | $C_4$ | $C_5$ |
|---|---|---|---|---|---|
| 2 | 17 | 31 | 56 | 84 | 101 |
| 3 | 37 | 67 | 79 | 100 | 125 |
| 4 | 67 | 86 | 95 | 105 | 148 |
| 1 | 87 | 117 | 117 | 122 | 157 |
| 5 | 97 | 121 | 133 | 140 | **159** |

$k=3$, secuencia 2-3-4-5-1:

| Job | $C_1$ | $C_2$ | $C_3$ | $C_4$ | $C_5$ |
|---|---|---|---|---|---|
| 2 | 17 | 31 | 56 | 84 | 101 |
| 3 | 37 | 67 | 79 | 100 | 125 |
| 4 | 67 | 86 | 95 | 105 | 148 |
| 5 | 77 | 90 | 107 | 114 | 150 |
| 1 | 97 | 127 | 127 | 132 | **159** |

$k=4$, secuencia 3-2-4-1-5 (valores de la hoja):

| Job | $C_1$ | $C_2$ | $C_3$ | $C_4$ | $C_5$ |
|---|---|---|---|---|---|
| 3 | 20 | 50 | 62 | 78 | 102 |
| 2 | 37 | 64 | 89 | 117 | 134 |
| 4 | 57 | 83 | 98 | 122 | 157 |
| 1 | 87 | 117 | 117 | 127 | 166 |
| 5 | 97 | 121 | 133 | 140 | **168** |

(La fila del trabajo 4 tiene un error de referencia: `C74 = C73+C5` suma el $P_1$ del trabajo 3 (20) en vez del trabajo 4 (30). Lo correcto es $C_1=67$ y $C_2=86$. `C75 = C74+C6` comete el error inverso y lo compensa, así que $C_{max}=168$ no cambia.)

**Resumen** (I2:K8): `K3 = G26`, `K5 = G57`, `K6 = G76`, `K8 = MIN(K3:K6)` = **159**. "Mejor Secuencia" = `J8 = J3` = **2 3 4 1 5**. La celda apunta fija a la primera fila, no busca el mínimo; aquí coincide porque las iteraciones 1-3 empatan en 159.

**Conclusión:** CDS da $C_{max}=159$. Por enumeración de las 120 permutaciones, 159 es el óptimo de este caso (cálculo propio).

---

### Hoja `NEH` (mismos datos de la hoja `CDS`)

**Paso 1** (B2:H7): `H3 = SUM(C3:G3)` → $\sum_i P_{ij}$.

| Job | Suma |
|---|---|
| 1 | 64 |
| 2 | 101 |
| 3 | 102 |
| 4 | 86 |
| 5 | 35 |

Orden no creciente: **3, 2, 4, 1, 5**. La columna I trae unos números escritos a mano (I3 = 3, I4 = 1, I5 = 1, I6 = 2, I7 vacía) sin rótulo; su significado no se puede establecer.

`C9 = ((B7*(B7+1))/2)-1` = **14**: número de secuencias que evalúa NEH, $\frac{n(n+1)}{2}-1$ con $n=5$ (L19, p. 31).

**Pasos 2-4.** Cada secuencia parcial tiene su propio bloque de tiempos de terminación, calculado con la recursión. Todos los valores se verificaron recalculando.

| $k$ | Secuencia parcial | $C_{max}$ parcial | Elegida |
|---|---|---|---|
| 2 | 3-2 | 134 | |
| 2 | 2-3 | **125** | ✓ (`D18 = MIN(C16,J16)`) |
| 3 | 4-2-3 | 157 | |
| 3 | 2-4-3 | 149 | |
| 3 | 2-3-4 | **148** | ✓ (`D29 = MIN(C27,J27,Q27)`) |
| 4 | 1-2-3-4 | 181 | |
| 4 | 2-1-3-4 | 172 | |
| 4 | 2-3-1-4 | 157 | |
| 4 | 2-3-4-1 | **157** | ✓ (empate con 2-3-1-4; `C40 = W31`) |
| 5 | 5-2-3-4-1 | 167 | |
| 5 | 2-5-3-4-1 | 163 | |
| 5 | 2-3-5-4-1 | **159** | ✓ (`C53 = P43`) |
| 5 | 2-3-4-1-5 | 159 | empate |
| 5 | 2-3-4-5-1 | 159 | empate |

Tiempos de terminación de la secuencia elegida 2-3-5-4-1 (P44:U49):

| Job | $C_1$ | $C_2$ | $C_3$ | $C_4$ | $C_5$ |
|---|---|---|---|---|---|
| 2 | 17 | 31 | 56 | 84 | 101 |
| 3 | 37 | 67 | 79 | 100 | 125 |
| 5 | 47 | 71 | 91 | 107 | 127 |
| 4 | 77 | 96 | 105 | 112 | 150 |
| 1 | 97 | 127 | 127 | 132 | **159** |

Gantt de 2-3-5-4-1 (inicio = fin − $P_{ij}$):

| Máquina | Trabajo | Inicio | Fin |
|---|---|---|---|
| 1 | 2 | 0 | 17 |
| 1 | 3 | 17 | 37 |
| 1 | 5 | 37 | 47 |
| 1 | 4 | 47 | 77 |
| 1 | 1 | 77 | 97 |
| 2 | 2 | 17 | 31 |
| 2 | 3 | 37 | 67 |
| 2 | 5 | 67 | 71 |
| 2 | 4 | 77 | 96 |
| 2 | 1 | 97 | 127 |
| 3 | 2 | 31 | 56 |
| 3 | 3 | 67 | 79 |
| 3 | 5 | 79 | 91 |
| 3 | 4 | 96 | 105 |
| 3 | 1 | 127 | 127 (dura 0) |
| 4 | 2 | 56 | 84 |
| 4 | 3 | 84 | 100 |
| 4 | 5 | 100 | 107 |
| 4 | 4 | 107 | 112 |
| 4 | 1 | 127 | 132 |
| 5 | 2 | 84 | 101 |
| 5 | 3 | 101 | 125 |
| 5 | 5 | 125 | 127 |
| 5 | 4 | 127 | 150 |
| 5 | 1 | 150 | 159 |

**Conclusión:** NEH da $C_{max}=159$, igual que CDS y que el óptimo de este caso.

### Observaciones

- Hoja `Campbell `: iteraciones 2 y 3 incompletas o con errores (bloques de tiempos que suman tiempos de terminación, columna M1 vacía, trabajo 5 en el grupo equivocado en la iteración 3). Los resultados correctos están en L19, p. 29: 88, 85 y 85.
- Hoja `CDS`: error de referencia en `C74`/`C75` (iteración 4) que no altera el $C_{max}$. `K4` está escrito a mano. `J8` toma siempre la primera secuencia.
- Hoja `NEH`: en el paso 4 hay empate (2-3-1-4 y 2-3-4-1 con 157). La hoja sigue con 2-3-4-1; el compendio sigue con 2-3-1-4. Ambos llegan a 159. `D40 = MIN(C38,J38,Q38)` no incluye la cuarta opción (`X38`), y `D53 = MIN(C51,J51,Q51)` deja fuera la cuarta y la quinta. No cambia el resultado. Los rótulos de los bloques 4 y 5 del paso 5 ("2 3 4 1 5" en W43 y "2 3 4 5 1" en AD43) no siguen el orden de las posiciones de inserción, pero coinciden con su contenido.
- `Regla de Johnson`: las celdas `K23` (False) y `K34` (True) y los grupos están escritos a mano, no calculados.
- "Tiempo de Flujo" es el promedio de los tiempos de terminación en la última máquina.
- El [compendio](../00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md) (hojas 09-11) rehace este libro con `VLOOKUP` y cita como fuente "Clase_3_11_2026.xlsx". Por los datos, es este mismo archivo (deducido).

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `Regla de Johnson` — 57 filas × 12 columnas · 1 imagen(es)

| Fila | A | B | C | D | E | F | G | H | I | J | K | L |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 |  | Job | P1j | P2j |  |  | Secuencia (Aleatoria) | C1j | C2j |  |  | 1. se acumulan los tiempos del primer trabajo y de la primera máquina |
| 3 |  | A | 12 | 16 |  |  | D | 15 | 27 |  |  |  |
| 4 |  | B | 3 | 5 |  |  | C | 23 | 30 |  |  |  |
| 5 |  | C | 8 | 3 |  |  | F | 46 | 67 |  |  |  |
| 6 |  | D | 15 | 12 |  |  | A | 58 | 83 |  |  |  |
| 7 |  | E | 18 | 22 |  |  | E | 76 | 105 |  |  |  |
| 8 |  | F | 23 | 21 |  |  | B | 79 | 110 |  |  |  |
| 10 |  |  |  |  |  |  | Cmax | 110 |  |  |  |  |
| 11 |  |  |  |  |  |  | Tiempo de Flujo | 70.3333 |  |  |  |  |
| 13 |  | Regla de Johnson |  |  |  |  |  | Regla de Johnson (3 Máquinas) | se usa cuando la máquina de la mitad no tiene cuello de botella |  |  |  |
| 15 |  | Job | P1j | P2j | Grupo | Grupo: en qué máquina el trabajo va más rápido |  | Job | P1j | P2j | P3j |  |
| 16 |  | A | 12 | 16 | 1 |  |  | A | 12 | 16 | 8 |  |
| 17 |  | B | 3 | 5 | 1 |  |  | B | 3 | 5 | 7 |  |
| 18 |  | C | 8 | 3 | 2 |  |  | C | 8 | 3 | 11 |  |
| 19 |  | D | 15 | 12 | 2 |  |  | D | 15 | 12 | 14 |  |
| 20 |  | E | 18 | 22 | 1 |  |  | E | 18 | 22 | 27 |  |
| 21 |  | F | 23 | 21 | 2 |  |  | F | 23 | 21 | 10 |  |
| 23 |  | Grupo 1 - SPT | mira los tiempos de la máquina 1 - SPT (menor a mayor) | Grupo 2 - LPT | mira los tiempos de la máquina 2 - LPT (mayor a menor) |  |  | 22 | <= | 7 | False | no se debe usar la regla de johnson de 3 máquinas |
| 24 |  | B-A-E |  | F-D-C |  |  |  |  |  |  |  |  |
| 26 |  | Secuencia | C1j | C2j |  |  |  | Job | P1j | P2j | P3j |  |
| 27 |  | B | 3 | 8 |  |  |  | A | 12 | 6 | 18 |  |
| 28 |  | A | 15 | 31 |  |  |  | B | 13 | 5 | 17 |  |
| 29 |  | E | 33 | 55 |  |  |  | C | 8 | 3 | 14 |  |
| 30 |  | F | 56 | 77 |  |  |  | D | 15 | 12 | 14 |  |
| 31 |  | D | 71 | 89 |  |  |  | E | 18 | 2 | 27 |  |
| 32 |  | C | 79 | 92 |  |  |  | F | 23 | 2 | 13 |  |
| 34 |  | Cmax | 92 |  |  |  |  | 12 | <= | 13 | True | se debe usar la regla de johnson de 3 máquinas |
| 35 |  | Tiempo de Flujo | 58.6667 |  |  |  |  |  |  |  |  |  |
| 36 |  |  |  |  |  |  |  | máquinas ficticias |  |  |  |  |
| 37 |  |  |  |  |  |  |  | Job | P1j´ | P2j´ | Grupo |  |
| 38 |  |  |  |  |  |  |  | A | 18 | 24 | 1 |  |
| 39 |  |  |  |  |  |  |  | B | 18 | 22 | 1 |  |
| 40 |  |  |  |  |  |  |  | C | 11 | 17 | 1 |  |
| 41 |  |  |  |  |  |  |  | D | 27 | 26 | 2 |  |
| 42 |  |  |  |  |  |  |  | E | 20 | 29 | 1 |  |
| 43 |  |  |  |  |  |  |  | F | 25 | 15 | 2 |  |
| 45 |  |  |  |  |  |  |  | Grupo 1 - SPT |  | Grupo 2 - LPT |  |  |
| 46 |  |  |  |  |  |  |  | C-A-B-E |  | D-F |  |  |
| 48 |  |  |  |  |  |  |  | Secuencia | C1j | C2j | C3j |  |
| 49 |  |  |  |  |  |  |  | C | 8 | 11 | 25 |  |
| 50 |  |  |  |  |  |  |  | A | 20 | 26 | 44 |  |
| 51 |  |  |  |  |  |  |  | B | 33 | 38 | 61 |  |
| 52 |  |  |  |  |  |  |  | E | 51 | 53 | 88 |  |
| 53 |  |  |  |  |  |  |  | D | 66 | 78 | 102 |  |
| 54 |  |  |  |  |  |  |  | F | 89 | 91 | 115 |  |
| 56 |  |  |  |  |  |  |  | Cmax | 115 |  |  |  |
| 57 |  |  |  |  |  |  |  | Tiempo de Flujo | 72.5 |  |  |  |

**Fórmulas (22 patrones distintos):**

- `H3`: `=C6`
- `I3`: `=H3+D6`
- `H4`: `=H3+C5`
- `I4`: `=(MAX(I3,H4))+D5`
- `H10`: `=I8`
- `H11`: `=AVERAGE(I3:I8)`
- `H23`: `=MAX(J16:J21)`
- `J23`: `=MAX(MIN(I16:I21),MIN(K16:K21))`
- `D27`: `=C27+D17`
- `C28`: `=C27+C16`
- `D28`: `=MAX(D27,C28)+D16`
- `C34`: `=D32`
- `C35`: `=AVERAGE(D27:D32)`
- `I38`: `=SUM(I27:J27)`
- `J38`: `=SUM(J27:K27)`
- `J49`: `=I49+J29`
- `K49`: `=J49+K29`
- `I50`: `=I49+I27`
- `J50`: `=MAX(J49,I50)+J27`
- `K50`: `=MAX(K49,J50)+K27`
- `I56`: `=K54`
- `I57`: `=AVERAGE(K49:K54)`

### Hoja `Campbell ` — 62 filas × 6 columnas

| Fila | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 2 |  | Trabajo | M1 | M2 | M3 | M4 |
| 3 |  | 1 | 1 | 13 | 6 | 2 |
| 4 |  | 2 | 10 | 12 | 18 | 18 |
| 5 |  | 3 | 17 | 9 | 13 | 4 |
| 6 |  | 4 | 12 | 17 | 2 | 6 |
| 7 |  | 5 | 11 | 3 | 5 | 16 |
| 9 |  | Iteración 1 |  |  |  |  |
| 10 |  | Trabajo | P1j´ | P2j´ | Grupo |  |
| 11 |  | 1 | 1 | 2 | 1 |  |
| 12 |  | 2 | 10 | 18 | 1 |  |
| 13 |  | 3 | 17 | 4 | 2 |  |
| 14 |  | 4 | 12 | 6 | 2 |  |
| 15 |  | 5 | 11 | 16 | 1 |  |
| 18 |  | Grupo 1 - SPT |  | Grupo 2 - LPT |  |  |
| 19 |  | 1 2 5 |  | 4 3 |  |  |
| 21 |  | Secuencia | M1 | M2 | M3 | M4 |
| 22 |  | 1 | 1 | 14 | 20 | 22 |
| 23 |  | 2 | 11 | 26 | 44 | 62 |
| 24 |  | 5 | 22 | 29 | 49 | 78 |
| 25 |  | 4 | 34 | 51 | 53 | 84 |
| 26 |  | 3 | 51 | 60 | 73 | 88 |
| 28 |  | Iteración 2 |  |  |  |  |
| 29 |  | Trabajo | P1j´ | P2j´ | Grupo |  |
| 30 |  | 1 | 14 | 8 | 2 |  |
| 31 |  | 2 | 22 | 36 | 1 |  |
| 32 |  | 3 | 26 | 17 | 2 |  |
| 33 |  | 4 | 29 | 8 | 2 |  |
| 34 |  | 5 | 14 | 21 | 1 |  |
| 36 |  | Grupo 1 - SPT |  | Grupo 2 - LPT |  |  |
| 37 |  | 5 2 |  | 3 1 4 |  |  |
| 39 |  | Secuencia | M1 | M2 | M3 | M4 |
| 40 |  | 5 |  |  |  |  |
| 41 |  | 2 |  | 14 | 34 | 56 |
| 42 |  | 3 |  | 65 | 118 | 202 |
| 43 |  | 1 |  | 94 | 167 | 280 |
| 44 |  | 4 |  | 120 | 211 | 342 |
| 46 |  | Iteración 3 |  |  |  |  |
| 47 |  | Trabajo | P1j´ | P2j´ | Grupo |  |
| 48 |  | 1 | 20 | 21 | 1 |  |
| 49 |  | 2 | 40 | 48 | 1 |  |
| 50 |  | 3 | 39 | 26 | 2 |  |
| 51 |  | 4 | 31 | 25 | 2 |  |
| 52 |  | 5 | 19 | 24 | 2 |  |
| 54 |  | Grupo 1 - SPT |  | Grupo 2 - LPT |  |  |
| 55 |  | 1 2 |  | 3 4 5 |  |  |
| 57 |  | Secuencia | M1 | M2 | M3 | M4 |
| 58 |  | 5 |  |  |  |  |
| 59 |  | 2 |  | 0 | 0 | 0 |
| 60 |  | 3 |  | 94 | 261 | 541 |
| 61 |  | 1 |  | 159 | 379 | 743 |
| 62 |  | 4 |  | 173 | 413 | 799 |

**Fórmulas (10 patrones distintos):**

- `C22`: `=C3`
- `D22`: `=C22+D3`
- `E22`: `=D22+E3`
- `F22`: `=E22+F3`
- `C23`: `=C22+C4`
- `D23`: `=MAX(D22,C23)+D4`
- `E23`: `=MAX(E22,D23)+E4`
- `F23`: `=MAX(F22,E23)+F4`
- `C48`: `=C3+D3+E3`
- `D48`: `=D3+E3+F3`

### Hoja `CDS` — 76 filas × 11 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 |  | Job | P1j | P2j | P3j | P4j | P5j |  | Iteración | Secuencia | C max |
| 3 |  | 1 | 20 | 30 | 0 | 5 | 9 |  | 1 | 2 3 4 1 5 | 159 |
| 4 |  | 2 | 17 | 14 | 25 | 28 | 17 |  | 2 | 2 3 4 1 5 | 159 |
| 5 |  | 3 | 20 | 30 | 12 | 16 | 24 |  | 3 | 2 3 4 5 1 | 159 |
| 6 |  | 4 | 30 | 19 | 9 | 5 | 23 |  | 4 | 3 2 4 1 5 | 168 |
| 7 |  | 5 | 10 | 4 | 12 | 7 | 2 |  |  |  |  |
| 8 |  |  |  |  |  |  |  |  | Mejor Secuencia | 2 3 4 1 5 | 159 |
| 9 |  | Iteración 1 | P1j´= P1 ; P2j´ = P5 |  |  |  |  |  |  |  |  |
| 11 |  | Job | P1j´ | P2j´ | Grupo |  |  |  |  |  |  |
| 12 |  | 1 | 20 | 9 | 2 |  |  |  |  |  |  |
| 13 |  | 2 | 17 | 17 | 1 |  |  |  |  |  |  |
| 14 |  | 3 | 20 | 24 | 1 |  |  |  |  |  |  |
| 15 |  | 4 | 30 | 23 | 2 |  |  |  |  |  |  |
| 16 |  | 5 | 10 | 2 | 2 |  |  |  |  |  |  |
| 18 |  | Grupo 1 SPT | Grupo 2 LPT |  |  |  |  |  |  |  |  |
| 19 |  | 2 3 | 4 1 5 |  |  |  |  |  |  |  |  |
| 21 |  | Job | P1j | P2j | P3j | P4j | P5j |  |  |  |  |
| 22 |  | 2 | 17 | 31 | 56 | 84 | 101 |  |  |  |  |
| 23 |  | 3 | 37 | 67 | 79 | 100 | 125 |  |  |  |  |
| 24 |  | 4 | 67 | 86 | 95 | 105 | 148 |  |  |  |  |
| 25 |  | 1 | 87 | 117 | 117 | 122 | 157 |  |  |  |  |
| 26 |  | 5 | 97 | 121 | 133 | 140 | 159 |  |  |  |  |
| 28 |  | Iteración 2 | P1j´= P1+P2 ; P2j´ = P5+P4 |  |  |  |  |  |  |  |  |
| 30 |  | Job | P1j´ | P2j´ | Grupo |  |  |  |  |  |  |
| 31 |  | 1 | 50 | 14 | 2 |  |  |  |  |  |  |
| 32 |  | 2 | 31 | 45 | 1 |  |  |  |  |  |  |
| 33 |  | 3 | 50 | 40 | 2 |  |  |  |  |  |  |
| 34 |  | 4 | 49 | 28 | 2 |  |  |  |  |  |  |
| 35 |  | 5 | 14 | 9 | 2 |  |  |  |  |  |  |
| 37 |  | Grupo 1 SPT | Grupo 2 LPT |  |  |  |  |  |  |  |  |
| 38 |  | 2 | 3 4 1 5 |  |  |  |  |  |  |  |  |
| 40 |  | Iteración 3 | P1j´= P1+P2+P3 ; P2j´ = P5+P4+P3 |  |  |  |  |  |  |  |  |
| 42 |  | Job | P1j´ | P2j´ | Grupo |  |  |  |  |  |  |
| 43 |  | 1 | 50 | 14 | 2 |  |  |  |  |  |  |
| 44 |  | 2 | 56 | 70 | 1 |  |  |  |  |  |  |
| 45 |  | 3 | 62 | 52 | 2 |  |  |  |  |  |  |
| 46 |  | 4 | 58 | 37 | 2 |  |  |  |  |  |  |
| 47 |  | 5 | 26 | 21 | 2 |  |  |  |  |  |  |
| 49 |  | Grupo 1 SPT | Grupo 2 LPT |  |  |  |  |  |  |  |  |
| 50 |  | 2 | 3 4 5 1 |  |  |  |  |  |  |  |  |
| 52 |  | Job | P1j | P2j | P3j | P4j | P5j |  |  |  |  |
| 53 |  | 2 | 17 | 31 | 56 | 84 | 101 |  |  |  |  |
| 54 |  | 3 | 37 | 67 | 79 | 100 | 125 |  |  |  |  |
| 55 |  | 4 | 67 | 86 | 95 | 105 | 148 |  |  |  |  |
| 56 |  | 5 | 77 | 90 | 107 | 114 | 150 |  |  |  |  |
| 57 |  | 1 | 97 | 127 | 127 | 132 | 159 |  |  |  |  |
| 59 |  | Iteración 4 | P1j´= P1+P2+P3+P4 ; P2j´ = P5+P4+P3+P2 |  |  |  |  |  |  |  |  |
| 61 |  | Job | P1j´ | P2j´ | Grupo |  |  |  |  |  |  |
| 62 |  | 1 | 55 | 44 | 2 |  |  |  |  |  |  |
| 63 |  | 2 | 84 | 84 | 1 |  |  |  |  |  |  |
| 64 |  | 3 | 78 | 82 | 1 |  |  |  |  |  |  |
| 65 |  | 4 | 63 | 56 | 2 |  |  |  |  |  |  |
| 66 |  | 5 | 33 | 25 | 2 |  |  |  |  |  |  |
| 68 |  | Grupo 1 SPT | Grupo 2 LPT |  |  |  |  |  |  |  |  |
| 69 |  | 3 2 | 4 1 5 |  |  |  |  |  |  |  |  |
| 71 |  | Job | P1j | P2j | P3j | P4j | P5j |  |  |  |  |
| 72 |  | 3 | 20 | 50 | 62 | 78 | 102 |  |  |  |  |
| 73 |  | 2 | 37 | 64 | 89 | 117 | 134 |  |  |  |  |
| 74 |  | 4 | 57 | 83 | 98 | 122 | 157 |  |  |  |  |
| 75 |  | 1 | 87 | 117 | 117 | 127 | 166 |  |  |  |  |

> **Hoja larga:** arriba se muestran 60 de 61 filas con datos. **Todos los valores de la hoja están en [`flowshop-scheduling-datos/CDS.csv`](./flowshop-scheduling-datos/CDS.csv)** (CSV, UTF-8).

**Fórmulas (17 patrones distintos):**

- `K3`: `=G26`
- `J8`: `=J3`
- `K8`: `=MIN(K3:K6)`
- `D22`: `=C22+D4`
- `E22`: `=D22+E4`
- `F22`: `=E22+F4`
- `G22`: `=F22+G4`
- `C23`: `=C22+C5`
- `D23`: `=MAX(D22,C23)+D5`
- `E23`: `=MAX(E22,D23)+E5`
- `F23`: `=MAX(F22,E23)+F5`
- `G23`: `=MAX(G22,F23)+G5`
- `C43`: `=C3+D3+E3`
- `D43`: `=E3+F3+G3`
- `C53`: `=C4`
- `C62`: `=C3+D3+E3+F3`
- `D62`: `=D3+E3+F3+G3`

### Hoja `NEH` — 53 filas × 35 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | AA | AB | AC | AD | AE | AF | AG | AH | AI |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 |  | Job | P1j | P2j | P3j | P4j | P5j | Suma |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 3 |  | 1 | 20 | 30 | 0 | 5 | 9 | 64 | 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 |  | 2 | 17 | 14 | 25 | 28 | 17 | 101 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 |  | 3 | 20 | 30 | 12 | 16 | 24 | 102 | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 |  | 4 | 30 | 19 | 9 | 5 | 23 | 86 | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7 |  | 5 | 10 | 4 | 12 | 7 | 2 | 35 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9 |  | # Secuencias | 14 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 11 |  | 3 2 |  |  |  |  |  |  | 2 3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 12 |  | Job | P1j | P2j | P3j | P4j | P5j |  | Job | P1j | P2j | P3j | P4j | P5j |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 13 |  | 3 | 20 | 50 | 62 | 78 | 102 |  | 2 | 17 | 31 | 56 | 84 | 101 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 14 |  | 2 | 37 | 64 | 89 | 117 | 134 |  | 3 | 37 | 67 | 79 | 100 | 125 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 16 |  | Cmax | 134 |  |  |  |  |  | Cmax | 125 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 18 |  | Elegido | 2 3 | 125 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 21 |  | 4 2 3 |  |  |  |  |  |  | 2 4 3 |  |  |  |  |  |  | 2 3 4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 22 |  | Job | P1j | P2j | P3j | P4j | P5j |  | Job | P1j | P2j | P3j | P4j | P5j |  | Job | P1j | P2j | P3j | P4j | P5j |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 23 |  | 4 | 30 | 49 | 58 | 63 | 86 |  | 2 | 17 | 31 | 56 | 84 | 101 |  | 2 | 17 | 31 | 56 | 84 | 101 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 24 |  | 2 | 47 | 63 | 88 | 116 | 133 |  | 4 | 47 | 66 | 75 | 89 | 124 |  | 3 | 37 | 67 | 79 | 100 | 125 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 25 |  | 3 | 67 | 97 | 109 | 132 | 157 |  | 3 | 67 | 97 | 109 | 125 | 149 |  | 4 | 67 | 86 | 95 | 105 | 148 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 27 |  | Cmax | 157 |  |  |  |  |  | Cmax | 149 |  |  |  |  |  | Cmax | 148 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 29 |  | Elegido | 2 3 4 | 148 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 31 |  | 1 2 3 4 |  |  |  |  |  |  | 2 1 3 4 |  |  |  |  |  |  | 2 3 1 4 |  |  |  |  |  |  | 2 3 4 1 |  |  |  |  |  |  |  |  |  |  |  |  |
| 32 |  | Job | P1j | P2j | P3j | P4j | P5j |  | Job | P1j | P2j | P3j | P4j | P5j |  | Job | P1j | P2j | P3j | P4j | P5j |  | Job | P1j | P2j | P3j | P4j | P5j |  |  |  |  |  |  |  |
| 33 |  | 1 | 20 | 50 | 50 | 55 | 64 |  | 2 | 17 | 31 | 56 | 84 | 101 |  | 2 | 17 | 31 | 56 | 84 | 101 |  | 2 | 17 | 31 | 56 | 84 | 101 |  |  |  |  |  |  |  |
| 34 |  | 2 | 37 | 64 | 89 | 117 | 134 |  | 1 | 37 | 67 | 67 | 89 | 110 |  | 3 | 37 | 67 | 79 | 100 | 125 |  | 3 | 37 | 67 | 79 | 100 | 125 |  |  |  |  |  |  |  |
| 35 |  | 3 | 57 | 94 | 106 | 133 | 158 |  | 3 | 57 | 97 | 109 | 125 | 149 |  | 1 | 57 | 97 | 97 | 105 | 134 |  | 4 | 67 | 86 | 95 | 105 | 148 |  |  |  |  |  |  |  |
| 36 |  | 4 | 87 | 113 | 122 | 138 | 181 |  | 4 | 87 | 116 | 125 | 130 | 172 |  | 4 | 87 | 116 | 125 | 130 | 157 |  | 1 | 87 | 117 | 117 | 122 | 157 |  |  |  |  |  |  |  |
| 38 |  | Cmax | 181 |  |  |  |  |  | Cmax | 172 |  |  |  |  |  | Cmax | 157 |  |  |  |  |  | Cmax | 157 |  |  |  |  |  |  |  |  |  |  |  |
| 40 |  | Elegido | 2 3 4 1 | 157 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 43 |  | 5 2 3 4 1 |  |  |  |  |  |  | 2 5 3 4 1 |  |  |  |  |  |  | 2 3 5 4 1 |  |  |  |  |  |  | 2 3 4 1 5 |  |  |  |  |  |  | 2 3 4 5 1 |  |  |  |  |  |
| 44 |  | Job | P1j | P2j | P3j | P4j | P5j |  | Job | P1j | P2j | P3j | P4j | P5j |  | Job | P1j | P2j | P3j | P4j | P5j |  | Job | P1j | P2j | P3j | P4j | P5j |  | Job | P1j | P2j | P3j | P4j | P5j |
| 45 |  | 5 | 10 | 14 | 26 | 33 | 35 |  | 2 | 17 | 31 | 56 | 84 | 101 |  | 2 | 17 | 31 | 56 | 84 | 101 |  | 2 | 17 | 31 | 56 | 84 | 101 |  | 2 | 17 | 31 | 56 | 84 | 101 |
| 46 |  | 2 | 27 | 41 | 66 | 94 | 111 |  | 5 | 27 | 35 | 68 | 91 | 103 |  | 3 | 37 | 67 | 79 | 100 | 125 |  | 3 | 37 | 67 | 79 | 100 | 125 |  | 3 | 37 | 67 | 79 | 100 | 125 |
| 47 |  | 3 | 47 | 77 | 89 | 110 | 135 |  | 3 | 47 | 77 | 89 | 107 | 131 |  | 5 | 47 | 71 | 91 | 107 | 127 |  | 4 | 67 | 86 | 95 | 105 | 148 |  | 4 | 67 | 86 | 95 | 105 | 148 |
| 48 |  | 4 | 77 | 96 | 105 | 115 | 158 |  | 4 | 77 | 96 | 105 | 112 | 154 |  | 4 | 77 | 96 | 105 | 112 | 150 |  | 1 | 87 | 117 | 117 | 122 | 157 |  | 5 | 77 | 90 | 107 | 114 | 150 |
| 49 |  | 1 | 97 | 127 | 127 | 132 | 167 |  | 1 | 97 | 127 | 127 | 132 | 163 |  | 1 | 97 | 127 | 127 | 132 | 159 |  | 5 | 97 | 121 | 133 | 140 | 159 |  | 1 | 97 | 127 | 127 | 132 | 159 |
| 51 |  | Cmax | 167 |  |  |  |  |  | Cmax | 163 |  |  |  |  |  | Cmax | 159 |  |  |  |  |  | Cmax | 159 |  |  |  |  |  | Cmax | 159 |  |  |  |  |
| 53 |  | Elegido | 2 3 5 4 1 | 159 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

**Fórmulas (59 patrones distintos):**

- `H3`: `=SUM(C3:G3)`
- `C9`: `=((B7*(B7+1))/2)-1`
- `C13`: `=C5`
- `D13`: `=C13+D5`
- `E13`: `=D13+E5`
- `F13`: `=E13+F5`
- `G13`: `=F13+G5`
- `K13`: `=J13+D4`
- `L13`: `=K13+E4`
- `M13`: `=L13+F4`
- `N13`: `=M13+G4`
- `C14`: `=C13+C4`
- `D14`: `=MAX(D13,C14)+D4`
- `E14`: `=MAX(E13,D14)+E4`
- `F14`: `=MAX(F13,E14)+F4`
- `G14`: `=MAX(G13,F14)+G4`
- `J14`: `=J13+C5`
- `K14`: `=MAX(K13,J14)+D5`
- `L14`: `=MAX(L13,K14)+E5`
- `M14`: `=MAX(M13,L14)+F5`
- `N14`: `=MAX(N13,M14)+G5`
- `C16`: `=G14`
- `J16`: `=N14`
- `C18`: `=I11`
- `D18`: `=MIN(C16,J16)`
- `R23`: `=Q23+D4`
- `S23`: `=R23+E4`
- `T23`: `=S23+F4`
- `U23`: `=T23+G4`
- `Q24`: `=Q23+C5`
- `R24`: `=MAX(R23,Q24)+D5`
- `S24`: `=MAX(S23,R24)+E5`
- `T24`: `=MAX(T23,S24)+F5`
- `U24`: `=MAX(U23,T24)+G5`
- `Q27`: `=U25`
- `C29`: `=P21`
- `D29`: `=MIN(C27,J27,Q27)`
- `Y33`: `=X33+D4`
- `Z33`: `=Y33+E4`
- `AA33`: `=Z33+F4`
- `AB33`: `=AA33+G4`
- `X34`: `=X33+C5`
- `Y34`: `=MAX(Y33,X34)+D5`
- `Z34`: `=MAX(Z33,Y34)+E5`
- `AA34`: `=MAX(AA33,Z34)+F5`
- `AB34`: `=MAX(AB33,AA34)+G5`
- `X38`: `=AB36`
- `C40`: `=W31`
- `Q45`: `=$C$4`
- `R45`: `=$Q$45+$D$4`
- `S45`: `=$R$45+$E$4`
- `T45`: `=$S$45+$F$4`
- `U45`: `=$T$45+$G$4`
- `AE46`: `=AE45+C5`
- `AF46`: `=MAX(AF45,AE46)+D5`
- `AG46`: `=MAX(AG45,AF46)+E5`
- `AH46`: `=MAX(AH45,AG46)+F5`
- `AI46`: `=MAX(AI45,AH46)+G5`
- `AE51`: `=AI49`

