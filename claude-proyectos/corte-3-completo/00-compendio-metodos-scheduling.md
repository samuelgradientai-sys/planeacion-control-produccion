<!-- fuente: corte-3-programacion-scheduling/00-compendio-metodos-scheduling/README.md -->
# Compendio de métodos de programación de la producción (Corte 3)

## Qué cubre

Un único libro de Excel que resume, con fórmulas, todos los métodos de *machine scheduling* del corte. En una máquina: SPT, WSPT, EDD, MS, ATC, cadenas con factor $\rho$, *preemption* y Lawler. En máquinas paralelas: LPT, SPT, LNS/CP y LFJ/LFM. En *flow shop*: Johnson, CDS y NEH. Incluye además una hoja de CRP (capacidad) del corte 2. Sirve como repaso rápido: cada hoja trae los datos, el método paso a paso y la comparación de métricas. La explicación detallada de cada tema está en su carpeta.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [metodos-programacion-produccion-corte3.md](/corte-3-programacion-scheduling/00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md) (gemelo del .xlsx) | Compendio de 12 hojas (índice y 11 métodos), con explicación hoja por hoja, tabla de fuentes reales en el repo y errores detectados | **Sí** |

## Orden de estudio sugerido

1. Leer primero las presentaciones de cada tema: [L16](/corte-3-programacion-scheduling/01-introduccion-scheduling/L16-intro-scheduling.md) (notación), [L17](/corte-3-programacion-scheduling/02-una-maquina/L17-single-machine-scheduling.md), [L18](/corte-3-programacion-scheduling/03-maquinas-paralelas/L18-parallel-machine-scheduling.md) y [L19](/corte-3-programacion-scheduling/04-flow-shop/L19-flow-shop-scheduling.md).
2. Luego usar el compendio como resumen, hoja por hoja, en el orden del índice (02 → 11).
3. Antes de confiar en un número, revisar las "Observaciones" del .md: hay tres hojas con errores (07, 08 y 01).

## Mapa de hojas por tema

| Hoja | Método | Tema / carpeta |
|---|---|---|
| `01_CRP_Capacidad` | CRP (setup + proceso + movimiento) | Corte 2: [05-mrp-ii-y-capacidad](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/) |
| `02_1Maq_Basicos` | Orden inicial, SPT, WSPT, EDD | [02-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/) |
| `03_1Maq_MS_ATC` | Holgura mínima y ATC | [02-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/) |
| `04_1Maq_Precedencia` | Cadenas sin romper y factor $\rho$ | [02-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/) |
| `05_1Maq_Preemption` | $1\|r_j,prmp\|\sum w_jC_j$ | [02-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/) |
| `06_1Maq_Lawler` | Lawler, $1\|prec\|h_{max}$ | [02-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/) |
| `07_Paralelas_LPT_SPT` | LPT y SPT en $Pm$ | [03-maquinas-paralelas](/corte-3-programacion-scheduling/03-maquinas-paralelas/) |
| `08_Paralelas_Restric` | LNS/CP con precedencias; LFJ/LFM con elegibilidad | [03-maquinas-paralelas](/corte-3-programacion-scheduling/03-maquinas-paralelas/) |
| `09_FlowShop_Johnson` | Johnson $F2$ y $F3$ | [04-flow-shop](/corte-3-programacion-scheduling/04-flow-shop/) |
| `10_FlowShop_CDS` | Campbell-Dudek-Smith | [04-flow-shop](/corte-3-programacion-scheduling/04-flow-shop/) |
| `11_FlowShop_NEH` | Nawaz-Enscore-Ham | [04-flow-shop](/corte-3-programacion-scheduling/04-flow-shop/) |

## Conceptos y fórmulas clave

Detalle en [metodos-programacion-produccion-corte3.md](/corte-3-programacion-scheduling/00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md).

- Medidas: $L_j=C_j-d_j$, $T_j=\max(0,L_j)$, $U_j=\mathbb{1}[T_j>0]$, $C_{max}=\max_j C_j$.
- Reglas óptimas en una máquina: SPT para $\sum C_j$, WSPT ($w_j/p_j$ decreciente) para $\sum w_jC_j$, EDD para $L_{max}$.
- Índice ATC, con $\bar p$ el promedio de los no programados y $K$ una constante:
  $$I_j(t)=\frac{w_j}{p_j}\exp\left(-\frac{\max(d_j-p_j-t,0)}{K\bar p}\right)$$
- Factor $\rho$ de una cadena: $\rho=\max_{l}\dfrac{\sum_{j\le l}w_j}{\sum_{j\le l}p_j}$.
- Garantía de LPT en $Pm||C_{max}$: $C_{max}(LPT)/C_{max}(OPT)\le\frac43-\frac1{3m}$.
- Johnson ($F2$): grupo 1 ($p_1<p_2$) en SPT de $p_1$, luego grupo 2 en LPT de $p_2$. Extensión a $F3$ si $\max p_2\le\max(\min p_1,\min p_3)$, con $p'_1=p_1+p_2$ y $p'_2=p_2+p_3$.
- CDS: $p'^{(k)}_1=\sum_{i\le k}p_i$, $p'^{(k)}_2=\sum_{i>m-k}p_i$, $k=1..m-1$. NEH: inserción en orden decreciente de $\sum_i p_{ij}$.
- Flow shop: $C_{i,[k]}=\max(C_{i,[k-1]},C_{i-1,[k]})+p_{i,[k]}$.

## Ejercicios resueltos disponibles

| Hoja | Ejemplo | Resultado principal |
|---|---|---|
| 01 | Lotes 300 y 575 en WC1, WC2, WC4 | WC2 se sobrecarga 1045 min en la semana 2 |
| 02 | 6 trabajos, 4 reglas | SPT $\bar C=16$; WSPT $\sum w_jC_j=161$; EDD $L_{max}=7$ |
| 03 | Mismos 6 trabajos, MS frente a ATC ($K=2$) | ATC 5-4-2-6-3-1, $\sum w_jT_j=26$; MS 28 |
| 04 | Cadenas CBA, EF, D | Sin romper C-B-A-E-F-D (440); con $\rho$ E-C-B-A-D-F (423) |
| 05 | 7 trabajos con liberaciones | $C_{max}=89$, $\sum w_jC_j=305$ |
| 06 | Lawler, 3 trabajos | 1-2-3, $h_{max}=10$ |
| 07 | $P3$ (15 trabajos) y $P4$ (9 trabajos) | LPT 55 (54 con el dato correcto); $P4$: SPT 16, LPT 15 |
| 08 | LNS/CP y LFJ/LFM | $C_{max}=3$ con precedencias; LFM 2; LFJ: la hoja dice 2, lo correcto es 3 |
| 09 | Johnson $F2$ y $F3$ (6 trabajos) | 92 y 115 |
| 10 | CDS 5×5 | 159 |
| 11 | NEH 5×5 | 2-3-5-1-4, 159 |

## Relación con otros temas y proyectos

- Una máquina: [02-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/README.md) (L17, Excel de clase y `atc.py`).
- Máquinas paralelas: [03-maquinas-paralelas](/corte-3-programacion-scheduling/03-maquinas-paralelas/README.md).
- Flow shop: [04-flow-shop](/corte-3-programacion-scheduling/04-flow-shop/README.md).
- Job shop: [05-job-shop](/corte-3-programacion-scheduling/05-job-shop/README.md).
- CRP: [corte 2 / 05-mrp-ii-y-capacidad](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/README.md).
- Competencia de *scheduling* (flow shop de permutación y paralelas con precedencias): [proyecto-competencia-scheduling](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/).


---

<!-- fuente: corte-3-programacion-scheduling/00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md -->
# metodos-programacion-produccion-corte3

> **Archivo:** [`metodos-programacion-produccion-corte3.xlsx`](/corte-3-programacion-scheduling/00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.xlsx) · **Corte 3** · Libro de Excel con 12 hoja(s): `00_Indice_Metodos`, `01_CRP_Capacidad`, `02_1Maq_Basicos`, `03_1Maq_MS_ATC`, `04_1Maq_Precedencia`, `05_1Maq_Preemption`, `06_1Maq_Lawler`, `07_Paralelas_LPT_SPT`, `08_Paralelas_Restric`, `09_FlowShop_Johnson`, `10_FlowShop_CDS`, `11_FlowShop_NEH`  
> **Nombre original:** `CORTE 3/Metodos_Programacion_Produccion_Corte3.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Compendio en Excel de **todos los métodos de programación de la producción del corte 3**, más uno del corte 2 (CRP). Cada hoja resuelve un ejemplo de clase con fórmulas dinámicas (`VLOOKUP`, `MAX`, `RANK`, `SUMIF`…). La hoja `00_Indice_Metodos` resume el modelo $\alpha|\beta|\gamma$, la regla y el objetivo de cada hoja. Sirve como guía de repaso: en un solo archivo están SPT, WSPT, EDD, MS, ATC, cadenas con factor $\rho$, *preemption*, Lawler, LPT/SPT en paralelas, LNS/CP, LFJ/LFM, Johnson, CDS y NEH.

**Sobre las páginas citadas:** las hojas citan páginas de "el PDF" (p. 1-2, 4-5, 6, 6-8, 8-10, 10-11, 12-13, 14-15, 15). Esos números **no corresponden** a las presentaciones L15-L19 del repo; parecen referirse a otro documento, quizá unos apuntes o un resumen, que no está en el repo (deducido). Esta tabla da las fuentes reales dentro del repo:

| Hoja | Método | Fuente en el repo | Carpeta del tema |
|---|---|---|---|
| `01_CRP_Capacidad` | CRP (MRP II) | [L15](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md), pp. 30-42 (lotes 300γ y 575γ) | [corte 2 / 05-mrp-ii-y-capacidad](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/) |
| `02_1Maq_Basicos` | FIFO, SPT, WSPT, EDD | [programacion-produccion-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/programacion-produccion-una-maquina.md) ("ejemplo clase 20/10"); teoría en [L17](/corte-3-programacion-scheduling/02-una-maquina/L17-single-machine-scheduling.md), pp. 7-12 | [02-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/) |
| `03_1Maq_MS_ATC` | MS y ATC | Mismos datos; teoría en L17, p. 13 | [02-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/) |
| `04_1Maq_Precedencia` | Cadenas y factor $\rho$ | [programacion-produccion-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/programacion-produccion-una-maquina.md), hoja `Restricciones de Precedencia`; teoría en L17, pp. 14-23 | [02-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/) |
| `05_1Maq_Preemption` | $1\|r_j,prmp\|\sum w_jC_j$ | L17, p. 25, y la misma hoja del Excel de una máquina | [02-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/) |
| `06_1Maq_Lawler` | Lawler | L17, pp. 28-31 | [02-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/) |
| `07_Paralelas_LPT_SPT` | LPT y SPT en paralelas | [L18](/corte-3-programacion-scheduling/03-maquinas-paralelas/L18-parallel-machine-scheduling.md), pp. 8-14 | [03-maquinas-paralelas](/corte-3-programacion-scheduling/03-maquinas-paralelas/) |
| `08_Paralelas_Restric` | LNS/CP y LFJ/LFM | L18, pp. 17-26 | [03-maquinas-paralelas](/corte-3-programacion-scheduling/03-maquinas-paralelas/) |
| `09_FlowShop_Johnson` | Johnson 2 y 3 máquinas | [flowshop-scheduling](/corte-3-programacion-scheduling/04-flow-shop/flowshop-scheduling.md), hoja `Regla de Johnson`; teoría en [L19](/corte-3-programacion-scheduling/04-flow-shop/L19-flow-shop-scheduling.md), pp. 6-14 | [04-flow-shop](/corte-3-programacion-scheduling/04-flow-shop/) |
| `10_FlowShop_CDS` | CDS | flowshop-scheduling, hoja `CDS`; L19, pp. 25-29 | [04-flow-shop](/corte-3-programacion-scheduling/04-flow-shop/) |
| `11_FlowShop_NEH` | NEH | flowshop-scheduling, hoja `NEH`; L19, pp. 30-36 | [04-flow-shop](/corte-3-programacion-scheduling/04-flow-shop/) |

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

**Observaciones:** en [L15](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md) los lotes de 300 y 575 son ambos de la parte **γ** (ruta WC1 → WC2 → WC4, con estos mismos tiempos). La β tiene otra ruta y un lote de 2000. Los rótulos "Producto Y" y "Producto B" parecen una mala lectura de γ y β (deducido); el lote de 575 no es de β. Además, la hoja carga cada centro en una semana fija, sin la secuencia WC1 → movimiento → WC2 → movimiento → WC4 ni la programación hacia atrás de L15. Es una simplificación, aunque los tiempos 1845, 2965 y 1180 sí coinciden con L15. Esta hoja es del **corte 2**.

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

**Observaciones:** el texto de `B22` incluye "(12 <= 13)" escrito dentro de la fórmula, así que no se actualiza si cambian los datos. La columna "Secuencia Óptima" H16:H21 quedó vacía; la secuencia está en B25:B30. Es el mismo ejemplo de la hoja `Regla de Johnson` de [flowshop-scheduling](/corte-3-programacion-scheduling/04-flow-shop/flowshop-scheduling.md).

---

### Hoja `10_FlowShop_CDS` — Campbell-Dudek-Smith

**Datos:** 5 trabajos × 5 máquinas, los mismos de la hoja `CDS` de [flowshop-scheduling](/corte-3-programacion-scheduling/04-flow-shop/flowshop-scheduling.md): J1 (20, 30, 0, 5, 9), J2 (17, 14, 25, 28, 17), J3 (20, 30, 12, 16, 24), J4 (30, 19, 9, 5, 23), J5 (10, 4, 12, 7, 2).

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

**Cmax óptimo NEH = 159.** El libro [flowshop-scheduling](/corte-3-programacion-scheduling/04-flow-shop/flowshop-scheduling.md) sigue la otra rama del empate (2-3-4-1) y llega a 2-3-5-4-1, también con 159.

---

### Observaciones generales

- `01_CRP_Capacidad` es del corte 2 (MRP II / CRP). Los rótulos "Y" y "B" deberían ser γ, y la lógica semanal simplifica el *backward scheduling* de L15.
- `07_Paralelas_LPT_SPT`: $p_1=3$ en vez de 1 (L18, p. 8). Por eso $C_{max}=55$ y $\sum C_j=584$, en vez de 54 y 582.
- `08_Paralelas_Restric`: la solución LFJ omite un trabajo y da $C_{max}=2$ cuando lo correcto es 3.
- `03_1Maq_MS_ATC`: el encabezado "t=30" de la tabla MS debería ser "t=34".
- Las páginas "PDF p. X" no corresponden a ningún PDF del repo (ver la tabla de fuentes al inicio).
- Varias celdas de "resultado" o "decisión" son texto o valores escritos a mano, no fórmulas: secuencias, decisiones de ρ, `B22` de la hoja 09, los Cmax parciales de NEH y la traza de *preemption*. Si se cambian los datos, esas celdas no se actualizan.
- Los demás cálculos (hojas 02, 04, 05, 06, 09, 10 y 11) se verificaron y son correctos.
