# metodos-programacion-produccion-corte3

> **Archivo:** [`metodos-programacion-produccion-corte3.xlsx`](./metodos-programacion-produccion-corte3.xlsx) · **Corte 3** · Libro de Excel con 12 hoja(s): `00_Indice_Metodos`, `01_CRP_Capacidad`, `02_1Maq_Basicos`, `03_1Maq_MS_ATC`, `04_1Maq_Precedencia`, `05_1Maq_Preemption`, `06_1Maq_Lawler`, `07_Paralelas_LPT_SPT`, `08_Paralelas_Restric`, `09_FlowShop_Johnson`, `10_FlowShop_CDS`, `11_FlowShop_NEH`  
> **Nombre original:** `CORTE 3/Metodos_Programacion_Produccion_Corte3.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Compendio en Excel de **todos los métodos de programación de la producción del corte 3**, más uno del corte 2 (CRP). Cada hoja resuelve un ejemplo de clase con fórmulas dinámicas (`VLOOKUP`, `MAX`, `RANK`, `SUMIF`…). La hoja `00_Indice_Metodos` resume el modelo $\alpha|\beta|\gamma$, la regla y el objetivo de cada hoja. Sirve como guía de repaso: en un solo archivo están SPT, WSPT, EDD, MS, ATC, cadenas con factor $\rho$, *preemption*, Lawler, LPT/SPT en paralelas, LNS/CP, LFJ/LFM, Johnson, CDS y NEH.

**Sobre las páginas citadas:** las hojas citan páginas de "el PDF" (p. 1-2, 4-5, 6, 6-8, 8-10, 10-11, 12-13, 14-15, 15). Esos números **no corresponden** a las presentaciones L15-L19 del repo; parecen referirse a otro documento, quizá unos apuntes o un resumen, que no está en el repo (deducido). Esta tabla da las fuentes reales dentro del repo:

| Hoja | Método | Fuente en el repo | Carpeta del tema |
|---|---|---|---|
| `01_CRP_Capacidad` | CRP (MRP II) | [L15](../../corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md), pp. 30-42 (lotes 300γ y 575γ) | [corte 2 / 05-mrp-ii-y-capacidad](../../corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/) |
| `02_1Maq_Basicos` | FIFO, SPT, WSPT, EDD | [programacion-produccion-una-maquina](../02-una-maquina/programacion-produccion-una-maquina.md) ("ejemplo clase 20/10"); teoría en [L17](../02-una-maquina/L17-single-machine-scheduling.md), pp. 7-12 | [02-una-maquina](../02-una-maquina/) |
| `03_1Maq_MS_ATC` | MS y ATC | Mismos datos; teoría en L17, p. 13 | [02-una-maquina](../02-una-maquina/) |
| `04_1Maq_Precedencia` | Cadenas y factor $\rho$ | [programacion-produccion-una-maquina](../02-una-maquina/programacion-produccion-una-maquina.md), hoja `Restricciones de Precedencia`; teoría en L17, pp. 14-23 | [02-una-maquina](../02-una-maquina/) |
| `05_1Maq_Preemption` | $1\|r_j,prmp\|\sum w_jC_j$ | L17, p. 25, y la misma hoja del Excel de una máquina | [02-una-maquina](../02-una-maquina/) |
| `06_1Maq_Lawler` | Lawler | L17, pp. 28-31 | [02-una-maquina](../02-una-maquina/) |
| `07_Paralelas_LPT_SPT` | LPT y SPT en paralelas | [L18](../03-maquinas-paralelas/L18-parallel-machine-scheduling.md), pp. 8-14 | [03-maquinas-paralelas](../03-maquinas-paralelas/) |
| `08_Paralelas_Restric` | LNS/CP y LFJ/LFM | L18, pp. 17-26 | [03-maquinas-paralelas](../03-maquinas-paralelas/) |
| `09_FlowShop_Johnson` | Johnson 2 y 3 máquinas | [flowshop-scheduling](../04-flow-shop/flowshop-scheduling.md), hoja `Regla de Johnson`; teoría en [L19](../04-flow-shop/L19-flow-shop-scheduling.md), pp. 6-14 | [04-flow-shop](../04-flow-shop/) |
| `10_FlowShop_CDS` | CDS | flowshop-scheduling, hoja `CDS`; L19, pp. 25-29 | [04-flow-shop](../04-flow-shop/) |
| `11_FlowShop_NEH` | NEH | flowshop-scheduling, hoja `NEH`; L19, pp. 30-36 | [04-flow-shop](../04-flow-shop/) |

**Notación común:** $p_j$ tiempo de proceso, $d_j$ fecha de entrega, $w_j$ peso, $C_j$ tiempo de terminación, $L_j=C_j-d_j$ retardo (*lateness*), $T_j=\max(0,L_j)$ tardanza, $U_j=1$ si $T_j>0$. $C_{max}=\max_j C_j$ es el makespan.

---

### Hoja `00_Indice_Metodos`

Índice con 11 filas: número, hoja, notación, regla, objetivo y estado ("Completo", con las páginas del PDF de origen). No tiene cálculos. Su contenido está en el anexo.

---

### Hoja `01_CRP_Capacidad` — Planeación de requerimientos de capacidad

**Objetivo:** calcular la carga en minutos de cada centro de trabajo (WC1, WC2, WC4) para dos lotes y compararla con la capacidad semanal disponible después del tiempo de movimiento.

**Datos de entrada:**

| Parámetro | Valor | Celda |
|---|---|---|
| Tiempo de movimiento | 480 min (1 día de 8 h) | B6 |
| Capacidad base por semana | 2400 min (5 días × 8 h × 60 min) | B7, I6:I8 |
| Lote "Producto Y" | 300 unidades | B8 |
| Lote "Producto B" | 575 unidades | B9 |

| Centro | Setup (min/lote) | Proceso (min/un) |
|---|---|---|
| WC1 | 120 | 3 |
| WC2 | 90 | 5 |
| WC4 | 30 | 2 |

**Método:**
- Tiempo por lote: $T=S+p\cdot Q$, donde $S$ es el setup, $p$ el tiempo unitario y $Q$ el lote (`B13 = E6+F6*G6`).
- Semana 1: se carga el lote de 300. Disponible $=2400-T_{300}-480$ (`E13 = I6-D13-$B$6`).
- Semana 2: se carga el lote de 575. Disponible $=2400-T_{575}-480$ (`G13`).
- Semana 3: si el disponible de la semana 2 es negativo, el exceso pasa a la semana 3: pendiente $=|\min(0,\text{disp}_2)|$ (`H13 = IF(G13<0,ABS(G13),0)`) y disponible final $=2400-\text{pendiente}$ (`I13`).

**Resultados:**

| Centro | $T_{300}$ | $T_{575}$ | Disp. sem. 1 | Disp. sem. 2 | Pendiente sem. 3 | Disp. final sem. 3 |
|---|---|---|---|---|---|---|
| WC1 | 1020 | 1845 | 900 | 75 | 0 | 2400 |
| WC2 | 1590 | 2965 | 330 | **−1045** | 1045 | 1355 |
| WC4 | 630 | 1180 | 1290 | 740 | 0 | 2400 |

**Conclusión:** WC2 es el cuello de botella. El lote de 575 necesita 2965 min, más que la capacidad semanal de 2400, así que 1045 min pasan a la semana 3.

**Observaciones:** en [L15](../../corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md) los lotes de 300 y 575 son ambos de la parte **γ** (ruta WC1 → WC2 → WC4, con estos mismos tiempos). La β tiene otra ruta y un lote de 2000. Los rótulos "Producto Y" y "Producto B" parecen una mala lectura de γ y β (deducido); el lote de 575 no es de β. Además, la hoja carga cada centro en una semana fija, sin la secuencia WC1 → movimiento → WC2 → movimiento → WC4 ni la programación hacia atrás de L15. Es una simplificación, aunque los tiempos 1845, 2965 y 1180 sí coinciden con L15. Esta hoja es del **corte 2**.

---

### Hoja `02_1Maq_Basicos` — Una máquina: orden inicial, SPT, WSPT y EDD

**Objetivo:** comparar cuatro secuencias de 6 trabajos en una máquina con varias métricas.

**Datos de entrada:**

| Job | $p_j$ | $d_j$ | $w_j$ | $w_j/p_j$ |
|---|---|---|---|---|
| 1 | 6 | 36 | 1 | 0.167 |
| 2 | 4 | 21 | 1 | 0.25 |
| 3 | 7 | 18 | 1 | 0.143 |
| 4 | 12 | 15 | 3 | 0.25 |
| 5 | 5 | 1 | 2 | 0.4 |
| 6 | 2 | 32 | 1 | 0.5 |

**Método:** la secuencia se escribe en la columna B y los datos se traen con `VLOOKUP`. $C_{[k]}=C_{[k-1]}+p_{[k]}$ (`F16 = F15+C16`); $L_j=C_j-d_j$; $T_j=\max(0,L_j)$; $w_jC_j$; $w_jT_j$; $U_j$ (`IF(H>0,1,0)`). Totales: $C_{max}$ (`MAX`), $\bar C$ (`AVERAGE`), $\sum C_j$, $L_{max}$ (`MAX` de $L_j$), $\sum T_j$, $\sum w_jC_j$, $\sum w_jT_j$, $\sum U_j$.

**Resultados:**

| Regla | Secuencia | $C_{max}$ | $\bar C$ | $\sum C_j$ | $L_{max}$ | $\sum T_j$ | $\sum w_jC_j$ | $\sum w_jT_j$ | $\sum U_j$ |
|---|---|---|---|---|---|---|---|---|---|
| Orden inicial | 1-2-3-4-5-6 | 36 | 22 | 132 | 33 | 51 | 224 | 112 | 3 |
| SPT | 6-2-5-1-3-4 | 36 | **16** | **96** | 21 | 37 | 179 | 89 | 3 |
| WSPT | 6-5-2-4-1-3 | 36 | 18 | 108 | 18 | 32 | **161** | 54 | 3 |
| EDD | 5-4-3-2-6-1 | 36 | 23.33 | 140 | **7** | **19** | 179 | **27** | 4 |

**Conclusión:** cada regla gana en el criterio para el que es óptima: SPT en $\sum C_j$, WSPT en $\sum w_jC_j$ y EDD en $L_{max}$. EDD también da la menor tardanza, pero tiene más trabajos tardíos. $C_{max}=36=\sum p_j$ no depende del orden. En WSPT los trabajos 2 y 4 empatan ($w/p=0.25$); la hoja pone primero el 2.

---

### Hoja `03_1Maq_MS_ATC` — Mínima holgura y ATC

**Objetivo:** secuenciar los mismos 6 trabajos con dos reglas dinámicas para $1||\sum w_jT_j$ y compararlas.

**Parámetro:** $K=2$ (celda G6).

**Método:**
- Holgura: $s_j(t)=\max(d_j-p_j-t,0)$ (`E15 = MAX(C15-B15-0,0)`). En cada instante de decisión se elige el trabajo de menor holgura; "X" marca los trabajos ya programados.
- Índice ATC:

$$I_j(t)=\frac{w_j}{p_j}\exp\left(-\frac{\max(d_j-p_j-t,0)}{K\,\bar p}\right)$$

donde $\bar p$ es el promedio de los $p_j$ **no programados** (cada columna promedia a mano los trabajos que quedan). Se elige el mayor índice.

**Holgura en cada instante (MS):**

| Job | t=0 | t=5 | t=17 | t=21 | t=28 | "t=30" | Orden MS |
|---|---|---|---|---|---|---|---|
| 1 | 30 | 25 | 13 | 9 | 2 | X | 5 |
| 2 | 17 | 12 | 0 | X | X | X | 3 |
| 3 | 11 | 6 | 0 | 0 | X | X | 4 |
| 4 | 3 | 0 | X | X | X | X | 2 |
| 5 | 0 | X | X | X | X | X | 1 |
| 6 | 30 | 25 | 13 | 9 | 2 | 0 | 6 |

**Índices ATC:**

| Job | t=0 | t=5 | t=17 | t=21 | t=23 | t=30 | Orden ATC |
|---|---|---|---|---|---|---|---|
| 1 | 0.0137 | 0.0222 | 0.0424 | 0.0678 | 0.0973 | 0.1667 | 6 |
| 2 | 0.0606 | 0.0950 | **0.25** | X | X | X | 3 |
| 3 | 0.0571 | 0.0881 | 0.1429 | 0.1429 | **0.1429** | X | 5 |
| 4 | 0.1947 | **0.25** | X | X | X | X | 2 |
| 5 | **0.4** | X | X | X | X | X | 1 |
| 6 | 0.0410 | 0.0666 | 0.1273 | **0.2033** | X | X | 4 |

($\bar p$ = 6, 6.2, 4.75, 5, 6.5 y 6 en cada columna.)

**Resultados:**

| Regla | Secuencia | $C_{max}$ | $\bar C$ | $\sum w_jC_j$ | $\sum T_j$ | $\sum w_jT_j$ |
|---|---|---|---|---|---|---|
| MS | 5-4-2-3-1-6 | 36 | 23.5 | 180 | 20 | 28 |
| ATC ($K=2$) | 5-4-2-6-3-1 | 36 | 22 | 171 | 18 | **26** |

Gantt ATC: 5 [0-5], 4 [5-17], 2 [17-21], 6 [21-23], 3 [23-30], 1 [30-36]. Gantt MS: 5 [0-5], 4 [5-17], 2 [17-21], 3 [21-28], 1 [28-34], 6 [34-36].

**Conclusión:** ATC logra menor tardanza ponderada (26) que MS (28) y que EDD en la hoja anterior (27).

**Observaciones:** en MS la última decisión es en $t=34$ (cuando termina el trabajo 1), no en $t=30$; el encabezado se copió de la tabla ATC. Hay empates que la hoja rompe sin decirlo: en $t=17$ los trabajos 2 y 3 tienen holgura 0 y se toma el 2; en $t=28$ los trabajos 1 y 6 tienen holgura 2 y se toma el 1.

---

### Hoja `04_1Maq_Precedencia` — Cadenas: sin romper y factor ρ

**Datos:** cadenas C → B → A, E → F y D (suelto).

| Trabajo | Cadena | Orden | $p_j$ | $w_j$ | $w_j/p_j$ |
|---|---|---|---|---|---|
| C | CBA | 1 | 11 | 3 | 0.273 |
| B | CBA | 2 | 4 | 2 | 0.5 |
| A | CBA | 3 | 2 | 1 | 0.5 |
| E | EF | 1 | 13 | 5 | 0.385 |
| F | EF | 2 | 20 | 1 | 0.05 |
| D | D | 1 | 30 | 2 | 0.067 |

**Caso A, cadenas que no se pueden romper:** se ordenan las cadenas por $\sum w_j/\sum p_j$ decreciente (`RANK`). CBA: 6/17 = 0.353; EF: 6/33 = 0.182; D: 2/30 = 0.067. Secuencia **C-B-A-E-F-D**.

**Caso B, cadenas que sí se pueden romper (factor ρ):**

$$\rho=\max_{1\le l\le k}\frac{\sum_{j=1}^{l}w_j}{\sum_{j=1}^{l}p_j}$$

y $l^*$ es el trabajo donde se alcanza el máximo.

| Cadena | Prefijos | Razones | ρ | $l^*$ | Decisión |
|---|---|---|---|---|---|
| CBA | C; C,B; C,B,A | 0.273; 0.333; 0.353 | 0.353 | A | No se corta |
| EF | E; E,F | 0.385; 0.182 | **0.385** | E | Se corta en E |
| D | D | 0.067 | 0.067 | D | |
| F (resto) | F | 0.05 | 0.05 | F | |

Secuencia **E-C-B-A-D-F**.

**Resultados ($\sum w_jC_j$):**

| Pos. | Sin romper | $C_j$ | $w_jC_j$ | Factor ρ | $C_j$ | $w_jC_j$ |
|---|---|---|---|---|---|---|
| 1 | C | 11 | 33 | E | 13 | 65 |
| 2 | B | 15 | 30 | C | 24 | 72 |
| 3 | A | 17 | 17 | B | 28 | 56 |
| 4 | E | 30 | 150 | A | 30 | 30 |
| 5 | F | 50 | 50 | D | 60 | 120 |
| 6 | D | 80 | 160 | F | 80 | 80 |
| Total | | | **440** | | | **423** |

(La columna H calcula $w_j\cdot C_j$ con `SUMPRODUCT(SUMIF(...))`, que suma los $p$ de los trabajos ya programados.)

**Conclusión:** poder romper las cadenas baja $\sum w_jC_j$ de 440 a 423.

---

### Hoja `05_1Maq_Preemption` — $1|r_j,prmp|\sum w_jC_j$

**Datos:** 7 trabajos con $w_j=1$.

| Trabajo | $p_j$ | $r_j$ | $w_j/p_j$ |
|---|---|---|---|
| 1 | 6 | 0 | 0.167 |
| 2 | 18 | 0 | 0.056 |
| 3 | 12 | 0 | 0.083 |
| 4 | 10 | 14 | 0.1 |
| 5 | 10 | 25 | 0.1 |
| 6 | 17 | 25 | 0.059 |
| 7 | 16 | 50 | 0.0625 |

**Método:** en cada evento (llegada o terminación) se elige, entre los trabajos disponibles, el de mayor $w_j/p_j^{\text{restante}}$. El trabajo en proceso puede interrumpirse.

**Traza de eventos (Gantt):**

| Evento | Trabajo | Inicio | Fin | Disponibles | Mejor razón | $p$ restante |
|---|---|---|---|---|---|---|
| 1 | 1 | 0 | 6 | 1, 2, 3 | 1/6 = 0.167 | 0 |
| 2 | 3 | 6 | 14 | 2, 3 | 1/12 = 0.083 | 4 |
| 3 | 3\* | 14 | 18 | 2, 3\*, 4 | 1/4 = 0.25 | 0 |
| 4 | 4 | 18 | 25 | 2, 4 | 1/10 = 0.1 | 3 |
| 5 | 4\* | 25 | 28 | 2, 4\*, 5, 6 | 1/3 = 0.333 | 0 |
| 6 | 5 | 28 | 38 | 2, 5, 6 | 1/10 = 0.1 | 0 |
| 7 | 6 | 38 | 50 | 2, 6 | 1/17 = 0.059 | 5 |
| 8 | 6\* | 50 | 55 | 2, 6\*, 7 | 1/5 = 0.2 | 0 |
| 9 | 7 | 55 | 71 | 2, 7 | 1/16 = 0.063 | 0 |
| 10 | 2 | 71 | 89 | 2 | 1/18 = 0.056 | 0 |

**Resultados:** $C_j$ = 6, 89, 18, 28, 38, 55, 71 (trabajos 1-7), calculado con `MAXIFS`. $C_{max}=89$, tiempo de flujo medio $\frac17\sum(C_j-r_j)=191/7=27.29$, $\sum w_jC_j=305$.

**Conclusión:** en cada llegada se revisa la prioridad, pero el trabajo en curso siempre conserva la mejor razón. En la práctica no hay cambio de trabajo, y el trabajo 2 (el más largo) queda de último.

---

### Hoja `06_1Maq_Lawler` — $1|prec|h_{max}$

**Datos:** 3 trabajos sin precedencias: $p=(2,3,5)$, $h_1(C)=1+C$, $h_2(C)=1.2\,C$, $h_3(C)=10$.

**Método (Lawler, hacia atrás):** con $J^c$ los trabajos no programados y $J'$ los que pueden ir al final, en cada paso se pone de último el $j^*\in J'$ con menor $h_j\left(\sum_{k\in J^c}p_k\right)$.

| Paso | $J^c$ | $\sum p$ | Evaluaciones | Elegido | Secuencia parcial |
|---|---|---|---|---|---|
| 1 | {1,2,3} | 10 | $h_1=11$, $h_2=12$, $h_3=10$ | 3 | [3] |
| 2 | {1,2} | 5 | $h_1=6$, $h_2=6$ (empate, se toma 2) | 2 | [2, 3] |
| 3 | {1} | 2 | $h_1=3$ | 1 | [1, 2, 3] |

**Resultado:** secuencia 1-2-3 con $C=(2,5,10)$, $h=(3,6,10)$ y $h_{max}=10$. Gantt: 1 [0-2], 2 [2-5], 3 [5-10].

**Observación:** las evaluaciones de E6:G8 son constantes escritas a mano (`=1+10`, `=1.2*10`…), no fórmulas generales.

---

### Hoja `07_Paralelas_LPT_SPT` — Máquinas paralelas idénticas

**Ejercicio 1: $P3||C_{max}$ con 15 trabajos y LPT** (L18, pp. 8-9).

| Máquina | Trabajos (orden) | $p_j$ | $C_j$ |
|---|---|---|---|
| M1 | 15, 10, 7, 6, 1 | 19, 13, 10, 10, **3** | 19, 32, 42, 52, 55 |
| M2 | 14, 11, 8, 5, 2 | 18, 13, 11, 9, 3 | 18, 31, 42, 51, 54 |
| M3 | 13, 12, 9, 4, 3 | 16, 14, 12, 6, 4 | 16, 30, 42, 48, 52 |

Resultados: $C_{max}=55$ (`J7`), $\sum C_j=584$ (`J9`), $\bar C=38.93$ (`J11`). Fila 12: "Cota Garantía LPT: $C_{max}(LPT)/C_{max}(OPT)\le4/3-1/(3m)=11/9=1.222$ → $C_{max}(OPT)\ge54/(11/9)=44.18$ → $C^*_{max}\ge45$".

**Error:** la hoja usa $p_1=3$, pero en L18 (p. 8) el trabajo 1 tiene $p_1=1$. Con el dato correcto, la máquina 1 termina en 53 y los resultados son los de la diapositiva: $C_{max}=54$, $\sum C_j=582$. La fila 12 usa 54 (dato de la diapositiva), que no coincide con el 55 de la propia hoja. Además, la cota $\sum p_j/m$ de L18, p. 30 es mucho más fuerte que 45: $159/3=53$ con los datos de la diapositiva.

**Ejercicio 2: $P4$ con 9 trabajos** ($p$ = 7, 7, 6, 6, 5, 5, 4, 4, 4) (L18, pp. 11-14):

| Regla | M1 | M2 | M3 | M4 | $C_{max}$ | $\sum C_j$ | $\bar C$ |
|---|---|---|---|---|---|---|---|
| SPT | 9 [0-4], 5 [4-9], 1 [9-16] | 8 [0-4], 4 [4-10] | 7 [0-4], 3 [4-10] | 6 [0-5], 2 [5-12] | 16 | 74 | 8.22 |
| LPT | 1 [0-7], 7 [7-11], 9 [11-15] | 2 [0-7], 8 [7-11] | 3 [0-6], 5 [6-11] | 4 [0-6], 6 [6-11] | 15 | 85 | 9.44 |

"Cota $C^*_{max}\ge12$" ($=48/4$). Según L18, p. 14, el óptimo es exactamente 12. La asignación SPT difiere de la de L18, p. 13 en cómo se rompen los empates entre trabajos de igual duración (en la diapositiva: M1: 7, 6, 2; M2: 8, 3; M3: 9, 4; M4: 5, 1), pero da los mismos $C_{max}$ y $\sum C_j$.

**Conclusión:** LPT reduce el makespan (15 frente a 16) y SPT reduce $\sum C_j$ (74 frente a 85). Ninguna de las dos llega al óptimo 12.

---

### Hoja `08_Paralelas_Restric` — Precedencias y elegibilidad

**Parte A: $Pm|prec|C_{max}$ con $p_j=1$** (grafo de L18, p. 19: 1 → 2 → 3, 4 → 3, 4 → 5, 6 → 3, 6 → 5). La hoja supone 2 máquinas:

| Máquina | t=1 | t=2 | t=3 | $C_{max}$ |
|---|---|---|---|---|
| M1 | Job 1 | Job 2 | Job 3 | 3 |
| M2 | Job 4 | Job 6 | Job 5 | 3 |

La hoja dice que LNS y CP dan $C_{max}=3$. (Análisis propio: CP siempre da 3. LNS da 3 solo si en $t=0$ rompe el empate entre 1, 4 y 6 eligiendo el 1; si elige 4 y 6, da 4.)

**Parte B: $P4|p_j=1,M_j|C_{max}$ con 8 trabajos** (L18, p. 22):

| Trabajo | $M_j$ | M1 | M2 | M3 | M4 | $\|M_j\|$ | Prioridad LFJ (`RANK` ascendente) |
|---|---|---|---|---|---|---|---|
| 1 | {1,2} | 1 | 1 | 0 | 0 | 2 | 2 |
| 2 | {1,3,4} | 1 | 0 | 1 | 1 | 3 | 7 |
| 3 | {1,3,4} | 1 | 0 | 1 | 1 | 3 | 7 |
| 4 | {2} | 0 | 1 | 0 | 0 | 1 | 1 |
| 5-8 | {3,4} | 0 | 0 | 1 | 1 | 2 | 2 |

Flexibilidad de las máquinas (trabajos que cada una puede hacer): M1 = 3, M2 = 2, M3 = 6, M4 = 6.

| Máquina | LFJ t=1 | LFJ t=2 | LFJ $C_{max}$ | LFM t=1 | LFM t=2 | LFM $C_{max}$ |
|---|---|---|---|---|---|---|
| M1 | Job 1 | Job 2 | 2 | Job 2 | Job 3 | 2 |
| M2 | Job 4 | – | 1 | Job 1 | Job 4 | 2 |
| M3 | Job 5 | Job 8 (o 3) | 2 | Job 6 | Job 8 | 2 |
| M4 | Job 6 | Job 7 | 2 | Job 5 | Job 7 | 2 |

Nota de la hoja: "Conjuntos Mj no son anidados"; "Cmax = 2 en ambos".

**Error:** la solución LFJ de la hoja deja sin programar un trabajo. Si M3 hace el 8, falta el 3; si hace el 3, falta el 8. Con LFJ el trabajo 3 tiene que esperar a $t=2$, y el resultado correcto es $C_{max}=3$ (L18, p. 25: Maq1 1-2, Maq2 4, Maq3 5-7-3, Maq4 6-8). La solución LFM sí es completa y factible, con $C_{max}=2$, que es el óptimo. Las columnas "Cmax" cuentan trabajos con `COUNTA`, lo que equivale a $C_{max}$ solo porque $p_j=1$.

**Conclusión (corregida):** con conjuntos no anidados, LFJ da 3 y LFM da 2.

---

### Hoja `09_FlowShop_Johnson` — $F2||C_{max}$ y $F3||C_{max}$

**Parte A (2 máquinas):** A (12, 16), B (3, 5), C (8, 3), D (15, 12), E (18, 22), F (23, 21). Grupo `D6 = IF(B6<C6,1,2)`. Grupo 1 en SPT: B-A-E; grupo 2 en LPT: F-D-C.

| Secuencia | $P_{1j}$ | $C_{1j}$ | $C_{2j}$ |
|---|---|---|---|
| B | 3 | 3 | 8 |
| A | 12 | 15 | 31 |
| E | 18 | 33 | 55 |
| F | 23 | 56 | 77 |
| D | 15 | 71 | 89 |
| C | 8 | 79 | **92** |

$C_{max}=92$.

**Parte B (3 máquinas):** A (12, 6, 18), B (13, 5, 17), C (8, 3, 14), D (15, 12, 14), E (18, 2, 27), F (23, 2, 13). Condición $\max P_2=12\le\max(\min P_1,\min P_3)=\max(8,13)=13$: cumple. $P'_1=P_1+P_2$ y $P'_2=P_2+P_3$:

| Job | $P'_1$ | $P'_2$ | Grupo |
|---|---|---|---|
| A | 18 | 24 | 1 |
| B | 18 | 22 | 1 |
| C | 11 | 17 | 1 |
| D | 27 | 26 | 2 |
| E | 20 | 29 | 1 |
| F | 25 | 15 | 2 |

| Pos. | Secuencia | $C_{1j}$ | $C_{2j}$ | $C_{3j}$ |
|---|---|---|---|---|
| 1 | C | 8 | 11 | 25 |
| 2 | A | 20 | 26 | 44 |
| 3 | B | 33 | 38 | 61 |
| 4 | E | 51 | 53 | 88 |
| 5 | D | 66 | 78 | 102 |
| 6 | F | 89 | 91 | **115** |

$C_{max}=115$, que es el óptimo (enumeración propia).

**Observaciones:** el texto de `B22` incluye "(12 <= 13)" escrito dentro de la fórmula, así que no se actualiza si cambian los datos. La columna "Secuencia Óptima" H16:H21 quedó vacía; la secuencia está en B25:B30. Es el mismo ejemplo de la hoja `Regla de Johnson` de [flowshop-scheduling](../04-flow-shop/flowshop-scheduling.md).

---

### Hoja `10_FlowShop_CDS` — Campbell-Dudek-Smith

**Datos:** 5 trabajos × 5 máquinas, los mismos de la hoja `CDS` de [flowshop-scheduling](../04-flow-shop/flowshop-scheduling.md): J1 (20, 30, 0, 5, 9), J2 (17, 14, 25, 28, 17), J3 (20, 30, 12, 16, 24), J4 (30, 19, 9, 5, 23), J5 (10, 4, 12, 7, 2).

**Método:** para $k=1,\dots,4$, $P'_{1j}=\sum_{i=1}^{k}P_{ij}$ y $P'_{2j}=\sum_{i=6-k}^{5}P_{ij}$ (`B22 = SUM(B6:C6)`, `C22 = SUM(E6:F6)`…). Se agrupa con `IF(P'1<=P'2,1,2)`, se ordena con Johnson y se evalúa la secuencia con la recursión del flow shop (`G15 = MAX(F15,G14)+VLOOKUP(...)`). En cada bloque, la columna A lista los trabajos 1-5 para $P'$ y la columna E la secuencia; las columnas F-J son los $C_{ij}$ **por posición** de la secuencia, no por trabajo.

| $k$ | $P'_1$ (J1..J5) | $P'_2$ (J1..J5) | Secuencia | $C_{max}$ |
|---|---|---|---|---|
| 1 | 20, 17, 20, 30, 10 | 9, 17, 24, 23, 2 | 2-3-4-1-5 | 159 |
| 2 | 50, 31, 50, 49, 14 | 14, 45, 40, 28, 9 | 2-3-4-1-5 | 159 |
| 3 | 50, 56, 62, 58, 26 | 14, 70, 52, 37, 21 | 2-3-4-5-1 | 159 |
| 4 | 55, 84, 78, 63, 33 | 44, 84, 82, 56, 25 | 3-2-4-1-5 | 168 |

**Mejor $C_{max}$ CDS = 159** (`C50 = MIN(C46:C49)`).

Gantt de 2-3-4-1-5 (inicio = fin − $P$):

| Máquina | J2 | J3 | J4 | J1 | J5 |
|---|---|---|---|---|---|
| 1 | 0-17 | 17-37 | 37-67 | 67-87 | 87-97 |
| 2 | 17-31 | 37-67 | 67-86 | 87-117 | 117-121 |
| 3 | 31-56 | 67-79 | 86-95 | 117-117 | 121-133 |
| 4 | 56-84 | 84-100 | 100-105 | 117-122 | 133-140 |
| 5 | 84-101 | 101-125 | 125-148 | 148-157 | 157-159 |

**Conclusión:** CDS da 159, que es el óptimo de este caso (enumeración propia de las 120 permutaciones).

---

### Hoja `11_FlowShop_NEH` — Nawaz-Enscore-Ham

**Paso 1:** sumas $\sum_i P_{ij}$ = 64, 101, 102, 86, 35 → orden NEH (`RANK`) 3, 2, 4, 1, 5.

**Pasos 2-4 (inserción):**

| $k$ | Opciones (Cmax parcial) | Elegida |
|---|---|---|
| 2 | 3-2 (134); **2-3 (125)** | 2-3 |
| 3 | 4-2-3 (157); 2-4-3 (149); **2-3-4 (148)** | 2-3-4 |
| 4 | 1-2-3-4 (181); 2-1-3-4 (172); **2-3-1-4 (157)**; **2-3-4-1 (157)** | empate; se sigue con 2-3-1-4 |
| 5 | 5-2-3-1-4 (167); 2-5-3-1-4 (163); **2-3-5-1-4 (159)**; **2-3-1-5-4 (159)**; **2-3-1-4-5 (159)** | empate; se toma 2-3-5-1-4 |

`D14 = IF(C14=MIN(...),"SELECCIONADA","Descartada")` marca como "SELECCIONADA" todas las opciones empatadas en el mínimo. Los Cmax parciales están escritos como valores; los verifiqué recalculando y son correctos.

**Cronograma final 2-3-5-1-4:**

| Pos. | Job | $C_1$ | $C_2$ | $C_3$ | $C_4$ | $C_5$ |
|---|---|---|---|---|---|---|
| 1 | 2 | 17 | 31 | 56 | 84 | 101 |
| 2 | 3 | 37 | 67 | 79 | 100 | 125 |
| 3 | 5 | 47 | 71 | 91 | 107 | 127 |
| 4 | 1 | 67 | 101 | 101 | 112 | 136 |
| 5 | 4 | 97 | 120 | 129 | 134 | **159** |

**Cmax óptimo NEH = 159.** El libro [flowshop-scheduling](../04-flow-shop/flowshop-scheduling.md) sigue la otra rama del empate (2-3-4-1) y llega a 2-3-5-4-1, también con 159.

---

### Observaciones generales

- `01_CRP_Capacidad` es del corte 2 (MRP II / CRP). Los rótulos "Y" y "B" deberían ser γ, y la lógica semanal simplifica el *backward scheduling* de L15.
- `07_Paralelas_LPT_SPT`: $p_1=3$ en vez de 1 (L18, p. 8). Por eso $C_{max}=55$ y $\sum C_j=584$, en vez de 54 y 582.
- `08_Paralelas_Restric`: la solución LFJ omite un trabajo y da $C_{max}=2$ cuando lo correcto es 3.
- `03_1Maq_MS_ATC`: el encabezado "t=30" de la tabla MS debería ser "t=34".
- Las páginas "PDF p. X" no corresponden a ningún PDF del repo (ver la tabla de fuentes al inicio).
- Varias celdas de "resultado" o "decisión" son texto o valores escritos a mano, no fórmulas: secuencias, decisiones de ρ, `B22` de la hoja 09, los Cmax parciales de NEH y la traza de *preemption*. Si se cambian los datos, esas celdas no se actualizan.
- Los demás cálculos (hojas 02, 04, 05, 06, 09, 10 y 11) se verificaron y son correctos.

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `00_Indice_Metodos` — 15 filas × 6 columnas

| Fila | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 1 | PROGRAMACIÓN DE LA PRODUCCIÓN (MACHINE SCHEDULING) - CORTE 3 |  |  |  |  |  |
| 2 | Compendio completo de todos los métodos del PDF con fórmulas dinámicas en Excel |  |  |  |  |  |
| 4 | # | Hoja / Pestaña | Notación / Modelo | Regla o Algoritmo | Objetivo Principal | Estado |
| 5 | 1 | 01_CRP_Capacidad | MRP II / CRP | Perfil de Capacidad (Setup + Run + Mov) | Validar capacidad disponible vs requerida | Completo (PDF p.1-2) |
| 6 | 2 | 02_1Maq_Basicos | 1 \|\| ΣCj, ΣwjCj, Lmax, ΣTj | Orden Inicial, SPT, WSPT, EDD | Minimizar C_prom, ΣwjCj, Lmax, ΣTj | Completo (PDF p.4-5) |
| 7 | 3 | 03_1Maq_MS_ATC | 1 \|\| ΣwjTj | Minimum Slack (MS) y ATC | Minimizar tardanza ponderada | Completo (PDF p.6) |
| 8 | 4 | 04_1Maq_Precedencia | 1 \| prec \| ΣwjCj | Cadenas sin romper y P-Factor (rotas) | Minimizar ΣwjCj con precedencias | Completo (PDF p.6-8) |
| 9 | 5 | 05_1Maq_Preemption | 1 \| rj, prmp \| ΣwjCj | WSPT Dinámico (Tiempo restante) | Minimizar ΣwjCj con llegadas e interrupción | Completo (PDF p.8-10) |
| 10 | 6 | 06_1Maq_Lawler | 1 \| prec \| h_max | Algoritmo de Lawler (Hacia atrás) | Minimizar penalidad máxima h_max | Completo (PDF p.10-11) |
| 11 | 7 | 07_Paralelas_LPT_SPT | Pm \|\| Cmax y Pm \|\| ΣCj | LPT (15 trabajos) y SPT vs LPT (9 trabajos) | Minimizar Makespan (Cmax) y ΣCj | Completo (PDF p.12-13) |
| 12 | 8 | 08_Paralelas_Restric | Pm\|prec\|Cmax y Pm\|Mj\|Cmax | LNS / CP y Least Flexible Job/Machine (LFJ/LFM) | Minimizar Cmax con precedencia o elegibilidad | Completo (PDF p.14-15) |
| 13 | 9 | 09_FlowShop_Johnson | F2 \|\| Cmax y F3 \|\| Cmax | Algoritmo de Johnson (2 y 3 máquinas) | Minimizar Makespan en Flow Shop | Completo (Excel + PDF p.15) |
| 14 | 10 | 10_FlowShop_CDS | Fm \|\| Cmax | Heurística CDS (Campbell-Dudek-Smith) | Minimizar Cmax en m máquinas | Completo (Excel + PDF p.15) |
| 15 | 11 | 11_FlowShop_NEH | Fm \|\| Cmax | Algoritmo Constructivo NEH | Minimizar Cmax por inserción | Completo (Excel + PDF p.15) |

### Hoja `01_CRP_Capacidad` — 15 filas × 9 columnas

| Fila | A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1. MRP II / CRP - PLANEACIÓN DE REQUERIMIENTOS DE CAPACIDAD |  |  |  |  |  |  |  |  |
| 2 | Cálculo de tiempos de setup, procesamiento, movimiento y capacidad disponible por centro de trabajo (WC) |  |  |  |  |  |  |  |  |
| 4 | Parámetros del Ejercicio (Productos Y y B) |  |  |  |  |  |  |  |  |
| 5 | Parámetro | Valor | Unidad | Centro Trabajo | Setup (min) | T. Proceso (min/un) | Lote Y (un) | Lote B (un) | Capacidad Semanal (min) |
| 6 | Tiempo movimiento | 480 | min (8 h) | WC1 | 120 | 3 | 300 | 575 | 2400 |
| 7 | Capacidad base/sem | 2400 | min | WC2 | 90 | 5 | 300 | 575 | 2400 |
| 8 | Lote Producto Y | 300 | unidades | WC4 | 30 | 2 | 300 | 575 | 2400 |
| 9 | Lote Producto B | 575 | unidades |  |  |  |  |  |  |
| 11 | Cálculo de Tiempo Requerido por Lote (Setup + T_proc * Tamaño Lote) |  |  |  |  |  |  |  |  |
| 12 | Centro Trabajo | T_300 Y (min) | T_575 B (min) | Sem 1: Lote 300 Y | Sem 1: Disp. tras Mov. | Sem 2: Lote 575 B | Sem 2: Disp. tras Mov. | Sem 3: Pendiente | Sem 3: Disp. Final |
| 13 | WC1 | 1020 | 1845 | 1020 | 900 | 1845 | 75 | 0 | 2400 |
| 14 | WC2 | 1590 | 2965 | 1590 | 330 | 2965 | -1045 | 1045 | 1355 |
| 15 | WC4 | 630 | 1180 | 630 | 1290 | 1180 | 740 | 0 | 2400 |

**Fórmulas (9 patrones distintos):**

- `A13`: `=D6`
- `B13`: `=E6+F6*G6`
- `C13`: `=E6+F6*H6`
- `D13`: `=B13`
- `E13`: `=I6-D13-$B$6`
- `F13`: `=C13`
- `G13`: `=I6-F13-$B$6`
- `H13`: `=IF(G13<0, ABS(G13), 0)`
- `I13`: `=I6-H13`

### Hoja `02_1Maq_Basicos` — 51 filas × 11 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2. UNA MÁQUINA: ORDEN INICIAL, SPT, WSPT Y EDD (1 \|\| Cmax, ΣCj, ΣwjCj, Lmax, ΣTj) |  |  |  |  |  |  |  |  |  |  |
| 2 | Comparación de métricas de desempeño para los 6 trabajos del PDF (páginas 4-5) |  |  |  |  |  |  |  |  |  |  |
| 4 | Datos Base de Trabajos (PDF págs. 4-5) |  |  |  |  |  |  |  |  |  |  |
| 5 | Job | pj (Proceso) | dj (Entrega) | wj (Peso) | Ratio wj/pj |  |  |  |  |  |  |
| 6 | 1 | 6 | 36 | 1 | 0.166667 |  |  |  |  |  |  |
| 7 | 2 | 4 | 21 | 1 | 0.25 |  |  |  |  |  |  |
| 8 | 3 | 7 | 18 | 1 | 0.142857 |  |  |  |  |  |  |
| 9 | 4 | 12 | 15 | 3 | 0.25 |  |  |  |  |  |  |
| 10 | 5 | 5 | 1 | 2 | 0.4 |  |  |  |  |  |  |
| 11 | 6 | 2 | 32 | 1 | 0.5 |  |  |  |  |  |  |
| 13 | Secuencia 1: Orden Inicial (1 - 2 - 3 - 4 - 5 - 6) |  |  |  |  |  |  |  |  |  |  |
| 14 | Pos | Job | pj | dj | wj | Cj (Fin) | Lj (Retardo) | Tj (Tardanza) | wj * Cj | wj * Tj | Uj (Tardío) |
| 15 | 1 | 1 | 6 | 36 | 1 | 6 | -30 | 0 | 6 | 0 | 0 |
| 16 | 2 | 2 | 4 | 21 | 1 | 10 | -11 | 0 | 10 | 0 | 0 |
| 17 | 3 | 3 | 7 | 18 | 1 | 17 | -1 | 0 | 17 | 0 | 0 |
| 18 | 4 | 4 | 12 | 15 | 3 | 29 | 14 | 14 | 87 | 42 | 1 |
| 19 | 5 | 5 | 5 | 1 | 2 | 34 | 33 | 33 | 68 | 66 | 1 |
| 20 | 6 | 6 | 2 | 32 | 1 | 36 | 4 | 4 | 36 | 4 | 1 |
| 21 | MÉTRICAS | Cmax = | 36 | C_prom = | 22 | 132 | 33 | 51 | 224 | 112 | 3 |
| 23 | Secuencia 2: SPT - Shortest Processing Time (Minimiza ΣCj y C_prom) |  |  |  |  |  |  |  |  |  |  |
| 24 | Pos | Job | pj | dj | wj | Cj (Fin) | Lj (Retardo) | Tj (Tardanza) | wj * Cj | wj * Tj | Uj (Tardío) |
| 25 | 1 | 6 | 2 | 32 | 1 | 2 | -30 | 0 | 2 | 0 | 0 |
| 26 | 2 | 2 | 4 | 21 | 1 | 6 | -15 | 0 | 6 | 0 | 0 |
| 27 | 3 | 5 | 5 | 1 | 2 | 11 | 10 | 10 | 22 | 20 | 1 |
| 28 | 4 | 1 | 6 | 36 | 1 | 17 | -19 | 0 | 17 | 0 | 0 |
| 29 | 5 | 3 | 7 | 18 | 1 | 24 | 6 | 6 | 24 | 6 | 1 |
| 30 | 6 | 4 | 12 | 15 | 3 | 36 | 21 | 21 | 108 | 63 | 1 |
| 31 | MÉTRICAS | Cmax = | 36 | C_prom = | 16 | 96 | 21 | 37 | 179 | 89 | 3 |
| 33 | Secuencia 3: WSPT - Weighted SPT (Orden decreciente wj/pj -> Minimiza ΣwjCj) |  |  |  |  |  |  |  |  |  |  |
| 34 | Pos | Job | pj | dj | wj | Cj (Fin) | Lj (Retardo) | Tj (Tardanza) | wj * Cj | wj * Tj | Uj (Tardío) |
| 35 | 1 | 6 | 2 | 32 | 1 | 2 | -30 | 0 | 2 | 0 | 0 |
| 36 | 2 | 5 | 5 | 1 | 2 | 7 | 6 | 6 | 14 | 12 | 1 |
| 37 | 3 | 2 | 4 | 21 | 1 | 11 | -10 | 0 | 11 | 0 | 0 |
| 38 | 4 | 4 | 12 | 15 | 3 | 23 | 8 | 8 | 69 | 24 | 1 |
| 39 | 5 | 1 | 6 | 36 | 1 | 29 | -7 | 0 | 29 | 0 | 0 |
| 40 | 6 | 3 | 7 | 18 | 1 | 36 | 18 | 18 | 36 | 18 | 1 |
| 41 | MÉTRICAS | Cmax = | 36 | C_prom = | 18 | 108 | 18 | 32 | 161 | 54 | 3 |
| 43 | Secuencia 4: EDD - Earliest Due Date (Orden creciente dj -> Minimiza Lmax y Tmax) |  |  |  |  |  |  |  |  |  |  |
| 44 | Pos | Job | pj | dj | wj | Cj (Fin) | Lj (Retardo) | Tj (Tardanza) | wj * Cj | wj * Tj | Uj (Tardío) |
| 45 | 1 | 5 | 5 | 1 | 2 | 5 | 4 | 4 | 10 | 8 | 1 |
| 46 | 2 | 4 | 12 | 15 | 3 | 17 | 2 | 2 | 51 | 6 | 1 |
| 47 | 3 | 3 | 7 | 18 | 1 | 24 | 6 | 6 | 24 | 6 | 1 |
| 48 | 4 | 2 | 4 | 21 | 1 | 28 | 7 | 7 | 28 | 7 | 1 |
| 49 | 5 | 6 | 2 | 32 | 1 | 30 | -2 | 0 | 30 | 0 | 0 |
| 50 | 6 | 1 | 6 | 36 | 1 | 36 | 0 | 0 | 36 | 0 | 0 |
| 51 | MÉTRICAS | Cmax = | 36 | C_prom = | 23.3333 | 140 | 7 | 19 | 179 | 27 | 4 |

**Fórmulas (17 patrones distintos):**

- `E6`: `=D6/B6`
- `C15`: `=VLOOKUP(B15,$A$6:$D$11,2,FALSE)`
- `F15`: `=C15`
- `G15`: `=F15-D15`
- `H15`: `=MAX(0,G15)`
- `I15`: `=E15*F15`
- `J15`: `=E15*H15`
- `K15`: `=IF(H15>0,1,0)`
- `F16`: `=F15+C16`
- `C21`: `=MAX(F15:F20)`
- `E21`: `=AVERAGE(F15:F20)`
- `F21`: `=SUM(F15:F20)`
- `G21`: `=MAX(G15:G20)`
- `H21`: `=SUM(H15:H20)`
- `I21`: `=SUM(I15:I20)`
- `J21`: `=SUM(J15:J20)`
- `K21`: `=SUM(K15:K20)`

### Hoja `03_1Maq_MS_ATC` — 34 filas × 11 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 3. UNA MÁQUINA: MINIMUM SLACK (MS) Y APPARENT TARDINESS COST (ATC) |  |  |  |  |  |  |  |  |  |  |
| 2 | Reglas dinámicas dependientes del tiempo t para minimizar tardanza ponderada (PDF pág. 6) |  |  |  |  |  |  |  |  |  |  |
| 4 | Datos Base y Parámetro K (ATC) |  |  |  |  |  |  |  |  |  |  |
| 5 | Job | pj | dj | wj |  | Parámetro | Valor |  |  |  |  |
| 6 | 1 | 6 | 36 | 1 |  | Constante K (ATC) | 2 |  |  |  |  |
| 7 | 2 | 4 | 21 | 1 |  |  |  |  |  |  |  |
| 8 | 3 | 7 | 18 | 1 |  |  |  |  |  |  |  |
| 9 | 4 | 12 | 15 | 3 |  |  |  |  |  |  |  |
| 10 | 5 | 5 | 1 | 2 |  |  |  |  |  |  |  |
| 11 | 6 | 2 | 32 | 1 |  |  |  |  |  |  |  |
| 13 | Secuencia 5: Minimum Slack (MS) -> sj(t) = max(dj - pj - t, 0) |  |  |  |  |  |  |  |  |  |  |
| 14 | Job | pj | dj | wj | t = 0 | t = 5 | t = 17 | t = 21 | t = 28 | t = 30 | Orden MS |
| 15 | 1 | 6 | 36 | 1 | 30 | 25 | 13 | 9 | 2 | X | 5 |
| 16 | 2 | 4 | 21 | 1 | 17 | 12 | 0 | X | X | X | 3 |
| 17 | 3 | 7 | 18 | 1 | 11 | 6 | 0 | 0 | X | X | 4 |
| 18 | 4 | 12 | 15 | 3 | 3 | 0 | X | X | X | X | 2 |
| 19 | 5 | 5 | 1 | 2 | 0 | X | X | X | X | X | 1 |
| 20 | 6 | 2 | 32 | 1 | 30 | 25 | 13 | 9 | 2 | 0 | 6 |
| 22 | Regla ATC (Apparent Tardiness Cost): Ij(t) = (wj/pj) * exp(-max(dj - pj - t, 0) / (K * p_prom)) |  |  |  |  |  |  |  |  |  |  |
| 23 | Job | pj | dj | wj | t = 0 | t = 5 | t = 17 | t = 21 | t = 23 | t = 30 | Orden ATC |
| 24 | 1 | 6 | 36 | 1 | 0.0136808 | 0.022195 | 0.0424181 | 0.0677616 | 0.0972742 | 0.166667 | 6 |
| 25 | 2 | 4 | 21 | 1 | 0.0606303 | 0.094985 | 0.25 | X | X | X | 3 |
| 26 | 3 | 7 | 18 | 1 | 0.0571214 | 0.0880561 | 0.142857 | 0.142857 | 0.142857 | X | 5 |
| 27 | 4 | 12 | 15 | 3 | 0.1947 | 0.25 | X | X | X | X | 2 |
| 28 | 5 | 5 | 1 | 2 | 0.4 | X | X | X | X | X | 1 |
| 29 | 6 | 2 | 32 | 1 | 0.0410425 | 0.066585 | 0.127254 | 0.203285 | X | X | 4 |
| 31 | Evaluación Comparativa: Secuencia MS vs Secuencia ATC |  |  |  |  |  |  |  |  |  |  |
| 32 | Regla | Secuencia Óptima | Cmax | C_prom | ΣwjCj | ΣTj | ΣwjTj (Objetivo) |  |  |  |  |
| 33 | Minimum Slack (MS) | 5 - 4 - 2 - 3 - 1 - 6 | 36 | 23.5 | 180 | 20 | 28 |  |  |  |  |
| 34 | ATC (K=2) | 5 - 4 - 2 - 6 - 3 - 1 | 36 | 22 | 171 | 18 | 26 |  |  |  |  |

**Fórmulas (7 patrones distintos):**

- `E15`: `=MAX(C15-B15-0,0)`
- `E24`: `=(D24/B24)*EXP(-MAX(C24-B24-0,0)/($G$6*AVERAGE(B24,B25,B26,B27,B28,B29)))`
- `F24`: `=(D24/B24)*EXP(-MAX(C24-B24-5,0)/($G$6*AVERAGE(B24,B25,B26,B27,B29)))`
- `G24`: `=(D24/B24)*EXP(-MAX(C24-B24-17,0)/($G$6*AVERAGE(B24,B25,B26,B29)))`
- `H24`: `=(D24/B24)*EXP(-MAX(C24-B24-21,0)/($G$6*AVERAGE(B24,B26,B29)))`
- `I24`: `=(D24/B24)*EXP(-MAX(C24-B24-23,0)/($G$6*AVERAGE(B24,B26)))`
- `J24`: `=(D24/B24)*EXP(-MAX(C24-B24-30,0)/($G$6*AVERAGE(B24)))`

### Hoja `04_1Maq_Precedencia` — 39 filas × 8 columnas

| Fila | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| 1 | 4. UNA MÁQUINA CON PRECEDENCIA: CADENAS SIN ROMPER Y P-FACTOR (1 \| prec \| ΣwjCj) |  |  |  |  |  |  |  |
| 2 | Cálculo de ratios Σwj/Σpj para cadenas rígidas y algoritmo de P-Factor para cadenas que se pueden romper (PDF págs. 6-8) |  |  |  |  |  |  |  |
| 4 | Datos de Trabajos y Cadenas de Precedencia (C -> B -> A, E -> F, D) |  |  |  |  |  |  |  |
| 5 | Trabajo | Cadena | Orden en Cadena | pj | wj | Ratio Individual wj/pj |  |  |
| 6 | C | Cadena CBA | 1 | 11 | 3 | 0.272727 |  |  |
| 7 | B | Cadena CBA | 2 | 4 | 2 | 0.5 |  |  |
| 8 | A | Cadena CBA | 3 | 2 | 1 | 0.5 |  |  |
| 9 | E | Cadena EF | 1 | 13 | 5 | 0.384615 |  |  |
| 10 | F | Cadena EF | 2 | 20 | 1 | 0.05 |  |  |
| 11 | D | Cadena D | 1 | 30 | 2 | 0.0666667 |  |  |
| 13 | Caso A: Cadenas NO se pueden romper (Se ordenan cadenas por Σwj / Σpj decreciente) |  |  |  |  |  |  |  |
| 14 | Cadena | Secuencia Interna | Σpj | Σwj | Ratio Σwj / Σpj | Prioridad |  |  |
| 15 | Cadena CBA | C - B - A | 17 | 6 | 0.352941 | 1 |  |  |
| 16 | Cadena EF | E - F | 33 | 6 | 0.181818 | 2 |  |  |
| 17 | Cadena D | D | 30 | 2 | 0.0666667 | 3 |  |  |
| 18 | Secuencia Óptima (Sin romper): | C - B - A - E - F - D |  |  |  |  |  |  |
| 20 | Caso B: Cadenas SÍ se pueden romper -> Algoritmo P-Factor: max_{1<=l<=k} (Σ_{j=1}^l wj / Σ_{j=1}^l pj) |  |  |  |  |  |  |  |
| 21 | Cadena | Prefijo (1..l) | Σwj Acum. | Σpj Acum. | Ratio Prefijo | P-Factor Cadena | Trabajo L* | Decisión |
| 22 | Cadena CBA | l = C | 3 | 11 | 0.272727 | 0.352941 | L* = A | No se corta CBA (P-Factor = 0.353) |
| 23 | Cadena CBA | l = C, B | 5 | 15 | 0.333333 |  |  |  |
| 24 | Cadena CBA | l = C, B, A | 6 | 17 | 0.352941 |  |  |  |
| 25 | Cadena EF | l = E | 5 | 13 | 0.384615 | 0.384615 | L* = E | Se corta en E (P-Factor = 0.385) |
| 26 | Cadena EF | l = E, F | 6 | 33 | 0.181818 |  |  |  |
| 27 | Cadena D | l = D | 2 | 30 | 0.0666667 | 0.0666667 | L* = D | P-Factor = 0.067 |
| 28 | Cadena F (Rem.) | l = F | 1 | 20 | 0.05 | 0.05 | L* = F | P-Factor = 0.050 |
| 29 | Secuencia Óptima (P-Factor): | E - C - B - A - D - F |  |  |  |  |  |  |
| 31 | Evaluación de Función Objetivo ΣwjCj: Sin Romper vs P-Factor |  |  |  |  |  |  |  |
| 32 | Pos | Job (Sin Romper) | pj | wj | Cj | wj*Cj | Job (P-Factor) | wj*Cj (P-Factor) |
| 33 | 1 | C | 11 | 3 | 11 | 33 | E | 65 |
| 34 | 2 | B | 4 | 2 | 15 | 30 | C | 72 |
| 35 | 3 | A | 2 | 1 | 17 | 17 | B | 56 |
| 36 | 4 | E | 13 | 5 | 30 | 150 | A | 30 |
| 37 | 5 | F | 20 | 1 | 50 | 50 | D | 120 |
| 38 | 6 | D | 30 | 2 | 80 | 160 | F | 80 |
| 39 | TOTAL ΣwjCj |  |  |  |  | 440 |  | 423 |

**Fórmulas (16 patrones distintos):**

- `F6`: `=E6/D6`
- `C15`: `=SUM(D6:D8)`
- `D15`: `=SUM(E6:E8)`
- `E15`: `=D15/C15`
- `F15`: `=RANK(E15,$E$15:$E$17)`
- `C17`: `=D11`
- `D17`: `=E11`
- `E22`: `=C22/D22`
- `F22`: `=MAX(E22:E24)`
- `C33`: `=VLOOKUP(B33,$A$6:$E$11,4,FALSE)`
- `E33`: `=C33`
- `F33`: `=D33*E33`
- `H33`: `=VLOOKUP(G33,$A$6:$E$11,5,FALSE)*SUMPRODUCT(SUMIF($A$6:$A$11,$G$33:G33,$D$6:$D$11))`
- `E34`: `=E33+C34`
- `F39`: `=SUM(F33:F38)`
- `H39`: `=SUM(H33:H38)`

### Hoja `05_1Maq_Preemption` — 36 filas × 9 columnas

| Fila | A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5. UNA MÁQUINA CON TIEMPOS DE LIBERACIÓN Y PREEMPTION (1 \| rj, prmp \| ΣwjCj) |  |  |  |  |  |  |  |  |
| 2 | Regla dinámica: seleccionar en cada evento el trabajo disponible con mayor tasa wj / pj_restante (PDF págs. 8-10) |  |  |  |  |  |  |  |  |
| 4 | Datos de Trabajos (wj = 1 para todos) |  |  |  |  |  |  |  |  |
| 5 | Trabajo | pj | rj (Llegada) | wj | Tasa Inicial wj/pj |  |  |  |  |
| 6 | 1 | 6 | 0 | 1 | 0.166667 |  |  |  |  |
| 7 | 2 | 18 | 0 | 1 | 0.0555556 |  |  |  |  |
| 8 | 3 | 12 | 0 | 1 | 0.0833333 |  |  |  |  |
| 9 | 4 | 10 | 14 | 1 | 0.1 |  |  |  |  |
| 10 | 5 | 10 | 25 | 1 | 0.1 |  |  |  |  |
| 11 | 6 | 17 | 25 | 1 | 0.0588235 |  |  |  |  |
| 12 | 7 | 16 | 50 | 1 | 0.0625 |  |  |  |  |
| 14 | Traza de Eventos y Diagrama de Ejecución (Preemption) |  |  |  |  |  |  |  |  |
| 15 | Evento # | t_inicio | t_fin | Duración | Trabajos Disponibles | Mejor Tasa (wj/p_rest) | Trabajo Elegido | p_restante tras evento | Observación |
| 16 | 1 | 0 | 6 | 6 | 1, 2, 3 | 1/6 = 0.167 (Job 1) | 1 | 0 | Termina Job 1 en t=6 |
| 17 | 2 | 6 | 14 | 8 | 2, 3 | 1/12 = 0.083 (Job 3) | 3 | 4 | Llega Job 4 en t=14 (Preemption check) |
| 18 | 3 | 14 | 18 | 4 | 2, 3*, 4 | 1/4 = 0.250 (Job 3*) | 3 | 0 | Continúa Job 3* (p_rest=4) y termina en t=18 |
| 19 | 4 | 18 | 25 | 7 | 2, 4 | 1/10 = 0.100 (Job 4) | 4 | 3 | Llegan Jobs 5 y 6 en t=25 (Preemption check) |
| 20 | 5 | 25 | 28 | 3 | 2, 4*, 5, 6 | 1/3 = 0.333 (Job 4*) | 4 | 0 | Continúa Job 4* (p_rest=3) y termina en t=28 |
| 21 | 6 | 28 | 38 | 10 | 2, 5, 6 | 1/10 = 0.100 (Job 5) | 5 | 0 | Termina Job 5 en t=38 |
| 22 | 7 | 38 | 50 | 12 | 2, 6 | 1/17 = 0.059 (Job 6) | 6 | 5 | Llega Job 7 en t=50 (Preemption check) |
| 23 | 8 | 50 | 55 | 5 | 2, 6*, 7 | 1/5 = 0.200 (Job 6*) | 6 | 0 | Continúa Job 6* (p_rest=5) y termina en t=55 |
| 24 | 9 | 55 | 71 | 16 | 2, 7 | 1/16 = 0.063 (Job 7) | 7 | 0 | Termina Job 7 en t=71 |
| 25 | 10 | 71 | 89 | 18 | 2 | 1/18 = 0.056 (Job 2) | 2 | 0 | Termina Job 2 en t=89 (Cmax = 89) |
| 27 | Cálculo de Tiempo de Finalización (Cj) y Métrica Objetivo ΣwjCj |  |  |  |  |  |  |  |  |
| 28 | Trabajo | rj | pj | wj | Cj (Finalización) | Flow Time (Cj - rj) | wj * Cj |  |  |
| 29 | 1 | 0 | 6 | 1 | 6 | 6 | 6 |  |  |
| 30 | 2 | 0 | 18 | 1 | 89 | 89 | 89 |  |  |
| 31 | 3 | 0 | 12 | 1 | 18 | 18 | 18 |  |  |
| 32 | 4 | 14 | 10 | 1 | 28 | 14 | 28 |  |  |
| 33 | 5 | 25 | 10 | 1 | 38 | 13 | 38 |  |  |
| 34 | 6 | 25 | 17 | 1 | 55 | 30 | 55 |  |  |
| 35 | 7 | 50 | 16 | 1 | 71 | 21 | 71 |  |  |
| 36 | TOTALES |  |  |  | 89 | 27.2857 | 305 |  |  |

**Fórmulas (12 patrones distintos):**

- `E6`: `=D6/B6`
- `D16`: `=C16-B16`
- `A29`: `=A6`
- `B29`: `=C6`
- `C29`: `=B6`
- `D29`: `=D6`
- `E29`: `=_xlfn.SINGLE(_xlfn.MAXIFS($C$16:$C$25,$G$16:$G$25,A29))`
- `F29`: `=E29-B29`
- `G29`: `=D29*E29`
- `E36`: `=MAX(E29:E35)`
- `F36`: `=AVERAGE(F29:F35)`
- `G36`: `=SUM(G29:G35)`

### Hoja `06_1Maq_Lawler` — 21 filas × 8 columnas

| Fila | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| 1 | 6. ALGORITMO DE LAWLER: MINIMIZAR PENALIDAD MÁXIMA (1 \| prec \| h_max) |  |  |  |  |  |  |  |
| 2 | Programación hacia atrás eligiendo en cada paso el trabajo sin sucesores con menor hj(Σpj) (PDF págs. 10-11) |  |  |  |  |  |  |  |
| 4 | Datos de Trabajos y Funciones de Penalidad hj(Cj) |  |  |  |  |  |  |  |
| 5 | Job | pj | Función hj(Cj) | Sucesores | Evaluación t=10 | Evaluación t=5 | Evaluación t=2 |  |
| 6 | 1 | 2 | 1 + Cj | Ninguno | 11 | 6 | 3 |  |
| 7 | 2 | 3 | 1.2 * Cj | Ninguno | 12 | 6 | X |  |
| 8 | 3 | 5 | 10 (Constante) | Ninguno | 10 | X | X |  |
| 10 | Iteraciones Hacia Atrás del Algoritmo de Lawler |  |  |  |  |  |  |  |
| 11 | Paso | Conjunto No Prog. (Jc) | Sin Sucesores (J') | Tiempo Acum. Σpj | Evaluaciones hj(Σpj) | Mínimo h_j* | Job Elegido j* | Secuencia Parcial J |
| 12 | Paso 1 | {1, 2, 3} | {1, 2, 3} | 10 | h1(10)=11, h2(10)=12, h3(10)=10 | 10 | 3 | [3] |
| 13 | Paso 2 | {1, 2} | {1, 2} | 5 | h1(5)=6, h2(5)=6 (Empate -> 2) | 6 | 2 | [2, 3] |
| 14 | Paso 3 | {1} | {1} | 2 | h1(2)=3 | 3 | 1 | [1, 2, 3] |
| 16 | Cronograma Final y Penalidad Máxima (h_max) |  |  |  |  |  |  |  |
| 17 | Posición | Job | pj | Cj (Finalización) | hj(Cj) |  |  |  |
| 18 | 1 | 1 | 2 | 2 | 3 |  |  |  |
| 19 | 2 | 2 | 3 | 5 | 6 |  |  |  |
| 20 | 3 | 3 | 5 | 10 | 10 |  |  |  |
| 21 | RESULTADO |  |  | 10 | 10 |  |  |  |

**Fórmulas (15 patrones distintos):**

- `E6`: `=1+10`
- `E7`: `=1.2*10`
- `E8`: `=10`
- `D12`: `=SUM(B6:B8)`
- `F12`: `=MIN(E6:E8)`
- `F13`: `=MIN(F6:F7)`
- `D14`: `=B6`
- `F14`: `=G6`
- `C18`: `=VLOOKUP(B18,$A$6:$B$8,2,FALSE)`
- `D18`: `=C18`
- `E18`: `=1+D18`
- `D19`: `=D18+C19`
- `E19`: `=1.2*D19`
- `D21`: `=MAX(D18:D20)`
- `E21`: `=MAX(E18:E20)`

### Hoja `07_Paralelas_LPT_SPT` — 25 filas × 12 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K | L |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 7. MÁQUINAS PARALELAS IDÉNTICAS: LPT (Pm \|\| Cmax) Y SPT (Pm \|\| ΣCj) |  |  |  |  |  |  |  |  |  |  |  |
| 2 | Ejercicios completos de las páginas 12 (P3 \|\| Cmax con 15 trabajos) y 13 (P4 \|\| Cmax vs SPT con 9 trabajos) |  |  |  |  |  |  |  |  |  |  |  |
| 4 | Ejercicio 1 (PDF pág. 12): P3 \|\| Cmax con 15 trabajos usando Regla LPT (Longest Processing Time) |  |  |  |  |  |  |  |  |  |  |  |
| 5 | Máquina 1: Job | pj | Cj | Máquina 2: Job | pj | Cj | Máquina 3: Job | pj | Cj | Resumen Métricas |  |  |
| 6 | 15 | 19 | 19 | 14 | 18 | 18 | 13 | 16 | 16 | Cmax (LPT) = |  |  |
| 7 | 10 | 13 | 32 | 11 | 13 | 31 | 12 | 14 | 30 | 55 |  |  |
| 8 | 7 | 10 | 42 | 8 | 11 | 42 | 9 | 12 | 42 | ΣCj = |  |  |
| 9 | 6 | 10 | 52 | 5 | 9 | 51 | 4 | 6 | 48 | 584 |  |  |
| 10 | 1 | 3 | 55 | 2 | 3 | 54 | 3 | 4 | 52 | C_prom = ΣCj / 15 |  |  |
| 11 |  |  |  |  |  |  |  |  |  | 38.9333 |  |  |
| 12 | Cota Garantía LPT: Cmax(LPT)/Cmax(OPT) <= 4/3 - 1/(3m) = 11/9 = 1.222 -> Cmax(OPT) >= 54 / (11/9) = 44.18 -> Cmax* >= 45 |  |  |  |  |  |  |  |  |  |  |  |
| 14 | Ejercicio 2 (PDF pág. 13): P4 con 9 trabajos (7, 7, 6, 6, 5, 5, 4, 4, 4) -> Comparación SPT vs LPT |  |  |  |  |  |  |  |  |  |  |  |
| 15 | SPT M1 Job | pj | Cj | SPT M2 Job | pj | Cj | SPT M3 Job | pj | Cj | SPT M4 Job | pj | Cj |
| 16 | 9 | 4 | 4 | 8 | 4 | 4 | 7 | 4 | 4 | 6 | 5 | 5 |
| 17 | 5 | 5 | 9 | 4 | 6 | 10 | 3 | 6 | 10 | 2 | 7 | 12 |
| 18 | 1 | 7 | 16 |  |  |  |  |  |  |  |  |  |
| 19 | SPT Cmax = | 16 |  | SPT ΣCj = | 74 |  | SPT C_prom = | 8.22222 |  |  |  |  |
| 21 | LPT M1 Job | pj | Cj | LPT M2 Job | pj | Cj | LPT M3 Job | pj | Cj | LPT M4 Job | pj | Cj |
| 22 | 1 | 7 | 7 | 2 | 7 | 7 | 3 | 6 | 6 | 4 | 6 | 6 |
| 23 | 7 | 4 | 11 | 8 | 4 | 11 | 5 | 5 | 11 | 6 | 5 | 11 |
| 24 | 9 | 4 | 15 |  |  |  |  |  |  |  |  |  |
| 25 | LPT Cmax = | 15 |  | LPT ΣCj = | 85 |  | LPT C_prom = | 9.44444 |  | Cota Cmax* >= 12 |  |  |

**Fórmulas (14 patrones distintos):**

- `C6`: `=B6`
- `F6`: `=E6`
- `I6`: `=H6`
- `C7`: `=C6+B7`
- `F7`: `=F6+E7`
- `I7`: `=I6+H7`
- `J7`: `=MAX(C6:C10,F6:F10,I6:I10)`
- `J9`: `=SUM(C6:C10,F6:F10,I6:I10)`
- `J11`: `=J9/15`
- `L16`: `=K16`
- `L17`: `=L16+K17`
- `B19`: `=MAX(C16:C18,F16:F18,I16:I18,L16:L18)`
- `E19`: `=SUM(C16:C18,F16:F18,I16:I18,L16:L18)`
- `H19`: `=E19/9`

### Hoja `08_Paralelas_Restric` — 26 filas × 8 columnas

| Fila | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| 1 | 8. PARALELAS CON PRECEDENCIA (Pm \| prec \| Cmax) Y ELEGIBILIDAD (Pm \| Mj, pj=1 \| Cmax) |  |  |  |  |  |  |  |
| 2 | Reglas LNS / CP (pág. 14) y Least Flexible Job / Machine First (LFJ / LFM, págs. 14-15) |  |  |  |  |  |  |  |
| 4 | Parte A: Pm \| prec \| Cmax (pj = 1) -> Comparación Regla LNS (Largest Number of Successors) vs CP |  |  |  |  |  |  |  |
| 5 | Máquina | t = 1 | t = 2 | t = 3 | Makespan (Cmax) | Regla Aplicada |  |  |
| 6 | Máquina 1 (M1) | Job 1 | Job 2 | Job 3 | 3 | LNS / CP (Cmax = 3) |  |  |
| 7 | Máquina 2 (M2) | Job 4 | Job 6 | Job 5 | 3 | LNS / CP (Cmax = 3) |  |  |
| 9 | Parte B: P4 \| pj = 1, Mj \| Cmax -> Restricciones de Elegibilidad de Máquina (8 Trabajos) |  |  |  |  |  |  |  |
| 10 | Trabajo | Conjunto Mj | M1 | M2 | M3 | M4 | Flexibilidad (\|Mj\|) | Prioridad LFJ |
| 11 | 1 | {1, 2} | 1 | 1 | 0 | 0 | 2 | 2 |
| 12 | 2 | {1, 3, 4} | 1 | 0 | 1 | 1 | 3 | 7 |
| 13 | 3 | {1, 3, 4} | 1 | 0 | 1 | 1 | 3 | 7 |
| 14 | 4 | {2} | 0 | 1 | 0 | 0 | 1 | 1 |
| 15 | 5 | {3, 4} | 0 | 0 | 1 | 1 | 2 | 2 |
| 16 | 6 | {3, 4} | 0 | 0 | 1 | 1 | 2 | 2 |
| 17 | 7 | {3, 4} | 0 | 0 | 1 | 1 | 2 | 2 |
| 18 | 8 | {3, 4} | 0 | 0 | 1 | 1 | 2 | 2 |
| 19 | Flexibilidad Máquina: |  | 3 | 2 | 6 | 6 |  |  |
| 21 | Asignación Resultante: LFJ (Least Flexible Job) y LFM (Least Flexible Machine) |  |  |  |  |  |  |  |
| 22 | Máquina | LFJ: t=1 | LFJ: t=2 | LFJ: Cmax | LFM: t=1 | LFM: t=2 | LFM: Cmax | Nota |
| 23 | M1 | Job 1 | Job 2 | 2 | Job 2 | Job 3 | 2 | Conjuntos Mj no son anidados |
| 24 | M2 | Job 4 | - | 1 | Job 1 | Job 4 | 2 |  |
| 25 | M3 | Job 5 | Job 8 (o 3) | 2 | Job 6 | Job 8 | 2 |  |
| 26 | M4 | Job 6 | Job 7 | 2 | Job 5 | Job 7 | 2 | Cmax = 2 en ambos |

**Fórmulas (10 patrones distintos):**

- `E6`: `=COUNTA(B6:D6)`
- `G11`: `=SUM(C11:F11)`
- `H11`: `=RANK(G11,$G$11:$G$18,1)`
- `C19`: `=SUM(C11:C18)`
- `D19`: `=SUM(D11:D18)`
- `E19`: `=SUM(E11:E18)`
- `F19`: `=SUM(F11:F18)`
- `D23`: `=COUNTA(B23:C23)`
- `G23`: `=COUNTA(E23:F23)`
- `D24`: `=COUNTA(B24:C24)-1`

### Hoja `09_FlowShop_Johnson` — 31 filas × 9 columnas

| Fila | A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 9. FLOW SHOP: ALGORITMO DE JOHNSON PARA 2 MÁQUINAS (F2 \|\| Cmax) Y 3 MÁQUINAS (F3 \|\| Cmax) |  |  |  |  |  |  |  |  |
| 2 | Minimización de Makespan en Flow Shop permutacional (PDF pág. 15 y hojas 1-2 de Clase_3_11_2026.xlsx) |  |  |  |  |  |  |  |  |
| 4 | Parte A: Regla de Johnson para 2 Máquinas (F2 \|\| Cmax) |  |  |  |  |  |  |  |  |
| 5 | Job | P1j | P2j | Grupo (P1j < P2j) |  | Secuencia Óptima | P1j | C1j | C2j |
| 6 | A | 12 | 16 | 1 |  | B | 3 | 3 | 8 |
| 7 | B | 3 | 5 | 1 |  | A | 12 | 15 | 31 |
| 8 | C | 8 | 3 | 2 |  | E | 18 | 33 | 55 |
| 9 | D | 15 | 12 | 2 |  | F | 23 | 56 | 77 |
| 10 | E | 18 | 22 | 1 |  | D | 15 | 71 | 89 |
| 11 | F | 23 | 21 | 2 |  | C | 8 | 79 | 92 |
| 12 | Regla: Grupo 1 (SPT en P1j): B-A-E \| Grupo 2 (LPT en P2j): F-D-C |  |  |  |  |  |  | Cmax = | 92 |
| 14 | Parte B: Extensión de Johnson para 3 Máquinas (F3 \|\| Cmax) -> Condición: max(P2j) <= max(min(P1j), min(P3j)) |  |  |  |  |  |  |  |  |
| 15 | Job | P1j | P2j | P3j | P'1j = P1j+P2j | P'2j = P2j+P3j | Grupo | Secuencia Óptima | C3j (Final) |
| 16 | A | 12 | 6 | 18 | 18 | 24 | 1 |  |  |
| 17 | B | 13 | 5 | 17 | 18 | 22 | 1 |  |  |
| 18 | C | 8 | 3 | 14 | 11 | 17 | 1 |  |  |
| 19 | D | 15 | 12 | 14 | 27 | 26 | 2 |  |  |
| 20 | E | 18 | 2 | 27 | 20 | 29 | 1 |  |  |
| 21 | F | 23 | 2 | 13 | 25 | 15 | 2 |  |  |
| 22 | Verificación Condición: | SÍ CUMPLE (12 <= 13) |  |  |  |  |  |  |  |
| 24 | Pos | Secuencia | P1j | P2j | P3j | C1j | C2j | C3j |  |
| 25 | 1 | C | 8 | 3 | 14 | 8 | 11 | 25 |  |
| 26 | 2 | A | 12 | 6 | 18 | 20 | 26 | 44 |  |
| 27 | 3 | B | 13 | 5 | 17 | 33 | 38 | 61 |  |
| 28 | 4 | E | 18 | 2 | 27 | 51 | 53 | 88 |  |
| 29 | 5 | D | 15 | 12 | 14 | 66 | 78 | 102 |  |
| 30 | 6 | F | 23 | 2 | 13 | 89 | 91 | 115 |  |
| 31 |  |  |  |  |  |  | Cmax = | 115 |  |

**Fórmulas (19 patrones distintos):**

- `D6`: `=IF(B6<C6, 1, 2)`
- `G6`: `=VLOOKUP(F6,$A$6:$C$11,2,FALSE)`
- `H6`: `=G6`
- `I6`: `=H6+VLOOKUP(F6,$A$6:$C$11,3,FALSE)`
- `H7`: `=H6+G7`
- `I7`: `=MAX(H7,I6)+VLOOKUP(F7,$A$6:$C$11,3,FALSE)`
- `I12`: `=MAX(I6:I11)`
- `E16`: `=B16+C16`
- `F16`: `=C16+D16`
- `G16`: `=IF(E16<F16, 1, 2)`
- `B22`: `=IF(MAX(C16:C21)<=MAX(MIN(B16:B21),MIN(D16:D21)),"SÍ CUMPLE (12 <= 13)","NO CUMPLE")`
- `C25`: `=VLOOKUP(B25,$A$16:$D$21,2,FALSE)`
- `F25`: `=C25`
- `G25`: `=F25+D25`
- `H25`: `=G25+E25`
- `F26`: `=F25+C26`
- `G26`: `=MAX(F26,G25)+D26`
- `H26`: `=MAX(G26,H25)+E26`
- `H31`: `=MAX(H25:H30)`

### Hoja `10_FlowShop_CDS` — 50 filas × 11 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 10. FLOW SHOP (m MÁQUINAS): HEURÍSTICA CDS (CAMPBELL - DUDEK - SMITH) |  |  |  |  |  |  |  |  |  |  |
| 2 | Genera m-1 subproblemas de 2 máquinas ficticias acumuladas y aplica Johnson en cada iteración (PDF pág. 15) |  |  |  |  |  |  |  |  |  |  |
| 4 | Datos Base: 5 Trabajos x 5 Máquinas (Ejercicio CDS de Clase) |  |  |  |  |  |  |  |  |  |  |
| 5 | Job | P1j | P2j | P3j | P4j | P5j |  |  |  |  |  |
| 6 | 1 | 20 | 30 | 0 | 5 | 9 |  |  |  |  |  |
| 7 | 2 | 17 | 14 | 25 | 28 | 17 |  |  |  |  |  |
| 8 | 3 | 20 | 30 | 12 | 16 | 24 |  |  |  |  |  |
| 9 | 4 | 30 | 19 | 9 | 5 | 23 |  |  |  |  |  |
| 10 | 5 | 10 | 4 | 12 | 7 | 2 |  |  |  |  |  |
| 12 | Iteración k = 1: P'1j = Σ(i=1..1) Pij  vs  P'2j = Σ(i=5..5) Pij |  |  |  |  |  |  |  |  |  |  |
| 13 | Job | P'1j | P'2j | Grupo | Seq Johnson | C1j | C2j | C3j | C4j | C5j | Cmax Iter |
| 14 | 1 | 20 | 9 | 2 | 2 | 17 | 31 | 56 | 84 | 101 | 159 |
| 15 | 2 | 17 | 17 | 1 | 3 | 37 | 67 | 79 | 100 | 125 |  |
| 16 | 3 | 20 | 24 | 1 | 4 | 67 | 86 | 95 | 105 | 148 |  |
| 17 | 4 | 30 | 23 | 2 | 1 | 87 | 117 | 117 | 122 | 157 |  |
| 18 | 5 | 10 | 2 | 2 | 5 | 97 | 121 | 133 | 140 | 159 |  |
| 20 | Iteración k = 2: P'1j = Σ(i=1..2) Pij  vs  P'2j = Σ(i=4..5) Pij |  |  |  |  |  |  |  |  |  |  |
| 21 | Job | P'1j | P'2j | Grupo | Seq Johnson | C1j | C2j | C3j | C4j | C5j | Cmax Iter |
| 22 | 1 | 50 | 14 | 2 | 2 | 17 | 31 | 56 | 84 | 101 | 159 |
| 23 | 2 | 31 | 45 | 1 | 3 | 37 | 67 | 79 | 100 | 125 |  |
| 24 | 3 | 50 | 40 | 2 | 4 | 67 | 86 | 95 | 105 | 148 |  |
| 25 | 4 | 49 | 28 | 2 | 1 | 87 | 117 | 117 | 122 | 157 |  |
| 26 | 5 | 14 | 9 | 2 | 5 | 97 | 121 | 133 | 140 | 159 |  |
| 28 | Iteración k = 3: P'1j = Σ(i=1..3) Pij  vs  P'2j = Σ(i=3..5) Pij |  |  |  |  |  |  |  |  |  |  |
| 29 | Job | P'1j | P'2j | Grupo | Seq Johnson | C1j | C2j | C3j | C4j | C5j | Cmax Iter |
| 30 | 1 | 50 | 14 | 2 | 2 | 17 | 31 | 56 | 84 | 101 | 159 |
| 31 | 2 | 56 | 70 | 1 | 3 | 37 | 67 | 79 | 100 | 125 |  |
| 32 | 3 | 62 | 52 | 2 | 4 | 67 | 86 | 95 | 105 | 148 |  |
| 33 | 4 | 58 | 37 | 2 | 5 | 77 | 90 | 107 | 114 | 150 |  |
| 34 | 5 | 26 | 21 | 2 | 1 | 97 | 127 | 127 | 132 | 159 |  |
| 36 | Iteración k = 4: P'1j = Σ(i=1..4) Pij  vs  P'2j = Σ(i=2..5) Pij |  |  |  |  |  |  |  |  |  |  |
| 37 | Job | P'1j | P'2j | Grupo | Seq Johnson | C1j | C2j | C3j | C4j | C5j | Cmax Iter |
| 38 | 1 | 55 | 44 | 2 | 3 | 20 | 50 | 62 | 78 | 102 | 168 |
| 39 | 2 | 84 | 84 | 1 | 2 | 37 | 64 | 89 | 117 | 134 |  |
| 40 | 3 | 78 | 82 | 1 | 4 | 67 | 86 | 98 | 122 | 157 |  |
| 41 | 4 | 63 | 56 | 2 | 1 | 87 | 117 | 117 | 127 | 166 |  |
| 42 | 5 | 33 | 25 | 2 | 5 | 97 | 121 | 133 | 140 | 168 |  |
| 44 | Resumen de Iteraciones CDS (Se selecciona la secuencia con menor Cmax) |  |  |  |  |  |  |  |  |  |  |
| 45 | Iteración k | Secuencia Obtenida | Cmax |  |  |  |  |  |  |  |  |
| 46 | 1 | 2 - 3 - 4 - 1 - 5 | 159 |  |  |  |  |  |  |  |  |
| 47 | 2 | 2 - 3 - 4 - 1 - 5 | 159 |  |  |  |  |  |  |  |  |
| 48 | 3 | 2 - 3 - 4 - 5 - 1 | 159 |  |  |  |  |  |  |  |  |
| 49 | 4 | 3 - 2 - 4 - 1 - 5 | 168 |  |  |  |  |  |  |  |  |
| 50 | MEJOR Cmax CDS = |  | 159 |  |  |  |  |  |  |  |  |

**Fórmulas (21 patrones distintos):**

- `B14`: `=SUM(B6:B6)`
- `C14`: `=SUM(F6:F6)`
- `D14`: `=IF(B14<=C14,1,2)`
- `F14`: `=VLOOKUP(E14,$A$6:$F$10,2,FALSE)`
- `G14`: `=F14+VLOOKUP(E14,$A$6:$F$10,3,FALSE)`
- `H14`: `=G14+VLOOKUP(E14,$A$6:$F$10,4,FALSE)`
- `I14`: `=H14+VLOOKUP(E14,$A$6:$F$10,5,FALSE)`
- `J14`: `=I14+VLOOKUP(E14,$A$6:$F$10,6,FALSE)`
- `K14`: `=MAX(F14:J18)`
- `G15`: `=MAX(F15,G14)+VLOOKUP(E15,$A$6:$F$10,3,FALSE)`
- `H15`: `=MAX(G15,H14)+VLOOKUP(E15,$A$6:$F$10,4,FALSE)`
- `I15`: `=MAX(H15,I14)+VLOOKUP(E15,$A$6:$F$10,5,FALSE)`
- `J15`: `=MAX(I15,J14)+VLOOKUP(E15,$A$6:$F$10,6,FALSE)`
- `B22`: `=SUM(B6:C6)`
- `C22`: `=SUM(E6:F6)`
- `B30`: `=SUM(B6:D6)`
- `C30`: `=SUM(D6:F6)`
- `B38`: `=SUM(B6:E6)`
- `C38`: `=SUM(C6:F6)`
- `C46`: `=K14`
- `C50`: `=MIN(C46:C49)`

### Hoja `11_FlowShop_NEH` — 45 filas × 9 columnas

| Fila | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| 1 | 11. FLOW SHOP (m MÁQUINAS): ALGORITMO CONSTRUCTIVO NEH (Fm \|\| Cmax) |  |  |  |  |  |  |  |
| 2 | Ordenamiento por suma total decreciente e inserción secuencial minimizando el makespan parcial (PDF pág. 15) |  |  |  |  |  |  |  |
| 4 | Paso 1: Ordenar Trabajos en Orden No Creciente de Suma Total de Procesamiento (ΣPij) |  |  |  |  |  |  |  |
| 5 | Job | P1j | P2j | P3j | P4j | P5j | Suma Total ΣPij | Orden NEH |
| 6 | 1 | 20 | 30 | 0 | 5 | 9 | 64 | 4 |
| 7 | 2 | 17 | 14 | 25 | 28 | 17 | 101 | 2 |
| 8 | 3 | 20 | 30 | 12 | 16 | 24 | 102 | 1 |
| 9 | 4 | 30 | 19 | 9 | 5 | 23 | 86 | 3 |
| 10 | 5 | 10 | 4 | 12 | 7 | 2 | 35 | 5 |
| 12 | Paso 2 (k = 2): Evaluar las 2 permutaciones iniciales con Jobs 3 y 2 |  |  |  |  |  |  |  |
| 13 | Opción | Secuencia Parcial | Cmax Parcial | Estado |  |  |  |  |
| 14 | Opción 1 | 3 - 2 | 134 | Descartada |  |  |  |  |
| 15 | Opción 2 | 2 - 3 | 125 | SELECCIONADA |  |  |  |  |
| 17 | Paso 3-4 (k = 3): Insertar Job 4 en las 3 posiciones posibles |  |  |  |  |  |  |  |
| 18 | Opción | Secuencia Parcial | Cmax Parcial | Estado |  |  |  |  |
| 19 | Opción 1 | 4 - 2 - 3 | 157 | Descartada |  |  |  |  |
| 20 | Opción 2 | 2 - 4 - 3 | 149 | Descartada |  |  |  |  |
| 21 | Opción 3 | 2 - 3 - 4 | 148 | SELECCIONADA |  |  |  |  |
| 23 | Paso 3-4 (k = 4): Insertar Job 1 en las 4 posiciones posibles |  |  |  |  |  |  |  |
| 24 | Opción | Secuencia Parcial | Cmax Parcial | Estado |  |  |  |  |
| 25 | Opción 1 | 1 - 2 - 3 - 4 | 181 | Descartada |  |  |  |  |
| 26 | Opción 2 | 2 - 1 - 3 - 4 | 172 | Descartada |  |  |  |  |
| 27 | Opción 3 | 2 - 3 - 1 - 4 | 157 | SELECCIONADA |  |  |  |  |
| 28 | Opción 4 | 2 - 3 - 4 - 1 | 157 | SELECCIONADA |  |  |  |  |
| 30 | Paso 3-4 (k = 5): Insertar Job 5 en las 5 posiciones posibles |  |  |  |  |  |  |  |
| 31 | Opción | Secuencia Parcial | Cmax Parcial | Estado |  |  |  |  |
| 32 | Opción 1 | 5 - 2 - 3 - 1 - 4 | 167 | Descartada |  |  |  |  |
| 33 | Opción 2 | 2 - 5 - 3 - 1 - 4 | 163 | Descartada |  |  |  |  |
| 34 | Opción 3 | 2 - 3 - 5 - 1 - 4 | 159 | SELECCIONADA |  |  |  |  |
| 35 | Opción 4 | 2 - 3 - 1 - 5 - 4 | 159 | SELECCIONADA |  |  |  |  |
| 36 | Opción 5 | 2 - 3 - 1 - 4 - 5 | 159 | SELECCIONADA |  |  |  |  |
| 38 | Cronograma Detallado de la Secuencia Óptima NEH: 2 - 3 - 5 - 1 - 4 |  |  |  |  |  |  |  |
| 39 | Posición | Job | C1j | C2j | C3j | C4j | C5j |  |
| 40 | 1 | 2 | 17 | 31 | 56 | 84 | 101 |  |
| 41 | 2 | 3 | 37 | 67 | 79 | 100 | 125 |  |
| 42 | 3 | 5 | 47 | 71 | 91 | 107 | 127 |  |
| 43 | 4 | 1 | 67 | 101 | 101 | 112 | 136 |  |
| 44 | 5 | 4 | 97 | 120 | 129 | 134 | 159 |  |
| 45 |  |  |  |  |  | Cmax Óptimo NEH = | 159 |  |

**Fórmulas (13 patrones distintos):**

- `G6`: `=SUM(B6:F6)`
- `H6`: `=RANK(G6,$G$6:$G$10)`
- `D14`: `=IF(C14=MIN($C$14:$C$15),"SELECCIONADA","Descartada")`
- `C40`: `=VLOOKUP(B40,$A$6:$F$10,2,FALSE)`
- `D40`: `=C40+VLOOKUP(B40,$A$6:$F$10,3,FALSE)`
- `E40`: `=D40+VLOOKUP(B40,$A$6:$F$10,4,FALSE)`
- `F40`: `=E40+VLOOKUP(B40,$A$6:$F$10,5,FALSE)`
- `G40`: `=F40+VLOOKUP(B40,$A$6:$F$10,6,FALSE)`
- `D41`: `=MAX(C41,D40)+VLOOKUP(B41,$A$6:$F$10,3,FALSE)`
- `E41`: `=MAX(D41,E40)+VLOOKUP(B41,$A$6:$F$10,4,FALSE)`
- `F41`: `=MAX(E41,F40)+VLOOKUP(B41,$A$6:$F$10,5,FALSE)`
- `G41`: `=MAX(F41,G40)+VLOOKUP(B41,$A$6:$F$10,6,FALSE)`
- `G45`: `=MAX(C40:G44)`

