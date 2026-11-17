# Corte 3: Programación de la producción (scheduling)

Tercer corte del curso (40 % de la nota final). Pasa de "qué y cuánto producir" (Cortes 1 y 2) a **en qué orden y en qué máquina**. Usa la notación de Graham $\alpha\,|\,\beta\,|\,\gamma$:

- $\alpha$: entorno de máquinas ($1$, $Pm$, $Fm$, $Jm$);
- $\beta$: restricciones ($r_j$, $prec$, $s_{ij}$, $prmu$, $pmtn$);
- $\gamma$: objetivo ($C_{max}$, $\sum w_jC_j$, $L_{max}$, $\sum w_jT_j$, $\sum U_j$).

```
Órdenes liberadas por el MRP (Corte 2)
 └─ ¿Qué entorno de máquinas?
     ├─ 1 máquina            → reglas de despacho (SPT, EDD, WSPT, MS, ATC, CR), cadenas, Lawler, Moore-Hodgson
     ├─ máquinas paralelas   → LPT, SPT, LNS/CP, LFJ
     ├─ flow shop            → Johnson (F2), Campbell–CDS, NEH
     └─ job shop             → modelo disyuntivo (GAMS), shifting bottleneck
```

## Temas (en orden de clase)

| # | Carpeta | Clase | Qué cubre | Ejercicios en la carpeta |
|---|---|---|---|---|
| 00 | [`00-compendio-metodos-scheduling/`](/corte-3-programacion-scheduling/00-compendio-metodos-scheduling/README.md) | — | Excel de 12 hojas (índice y 11 métodos) con **todos los métodos del corte** resueltos: CRP, SPT/WSPT/EDD, MS/ATC, cadenas, preemption, Lawler, LPT/SPT, LNS/CP, LFJ/LFM, Johnson, CDS y NEH | Cada hoja enlaza con el tema correspondiente |
| 01 | [`01-introduccion-scheduling/`](/corte-3-programacion-scheduling/01-introduccion-scheduling/README.md) | [L16](/corte-3-programacion-scheduling/01-introduccion-scheduling/L16-intro-scheduling.md) | Notación α\|β\|γ; indicadores $C_j, L_j, T_j, U_j, E_j$; del MRP a las órdenes; anomalías en $P2\,\|\,prec\,\|\,C_{max}$; programas sin retraso y activos; complejidad | — |
| 02 | [`02-una-maquina/`](/corte-3-programacion-scheduling/02-una-maquina/README.md) | [L17](/corte-3-programacion-scheduling/02-una-maquina/L17-single-machine-scheduling.md) | FIFO, **SPT, EDD, WSPT**, MS, **ATC**, CR, cadenas (factor ρ), preemption, **Lawler**, **Moore-Hodgson**, Solver | Reglas de despacho, precedencias, ejemplo con $r_j$ y `atc.py` (reproduce la secuencia de clase 1-3-2-4) |
| 03 | [`03-maquinas-paralelas/`](/corte-3-programacion-scheduling/03-maquinas-paralelas/README.md) | [L18](/corte-3-programacion-scheduling/03-maquinas-paralelas/L18-parallel-machine-scheduling.md) | Máquinas paralelas: **LPT** para $Pm\,\|\,\|\,C_{max}$ (garantía $4/3 - 1/3m$), SPT, precedencias (CP/LNS), elegibilidad (LFJ/LFM), preemption y MIP de $Rm\,\|\,\|\,\sum C_j$ | Plantilla de paralelas (15 trabajos, 3 máquinas), con LPT, SPT y WSPT calculados en el `.md` |
| 04 | [`04-flow-shop/`](/corte-3-programacion-scheduling/04-flow-shop/README.md) | [L19](/corte-3-programacion-scheduling/04-flow-shop/L19-flow-shop-scheduling.md) | Flow shop de permutación: **Johnson** (F2/F3), MIP de $Fm\,\|\,prmu\,\|\,C_{max}$ en **GAMS**, **Campbell–CDS**, **NEH**, flow shop flexible y algoritmos genéticos | Excel con Johnson, Campbell, CDS (Cmax 168) y NEH |
| 05 | [`05-job-shop/`](/corte-3-programacion-scheduling/05-job-shop/README.md) | [Job shop](/corte-3-programacion-scheduling/05-job-shop/job-shop-y-flexible-job-shop.md) | Job shop: modelo disyuntivo, implementación en **GAMS/LogMIP**, grafo disyuntivo, **shifting bottleneck** ($1\,\|\,r_j\,\|\,L_{max}$), LEKIN | — |

## Proyecto del corte: competencia de scheduling

**[`proyecto-competencia-scheduling/`](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/README.md)** es una competencia en Gradescope. Se califica así: **calidad 60 %, tiempo de cómputo 30 % e informe 10 %** (PDF de máximo 4 páginas).

- **Reto 1, Willy Wonka:** $F3\,|\,prmu, s_{ij}\,|\,C_{max}$. Flow shop de 3 máquinas con alistamientos por tipo de lote (S, N, R) y la transición N→R prohibida.
- **Reto 2, Monstruópolis:** $P3\,|\,r_j, prec\,|\,\sum w_jT_j$. Tres máquinas paralelas con liberaciones y precedencias.

La carpeta tiene dos partes:
- `enunciados/`: instructivo, retos y plantillas del profesor.
- `solucion/`: código del estudiante. Tiene su propio [`README.md`](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/README.md) e [`INFORME_TECNICO.md`](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/INFORME_TECNICO.md).

| | Método | Resultado |
|---|---|---|
| **Reto 1** | Cota inferior, NEH, búsqueda local y programación dinámica acotada | Óptimo demostrado en 30/30 instancias de la plantilla, Cmax promedio 616,77, unos 4 ms. La primera entrega en Gradescope dio «616.7667 / 100.0». |
| **Reto 2** | WSPT/ATC y recocido simulado | 0 violaciones, unos 75–80 ms por instancia. El óptimo no se puede demostrar. |

El estudiante decidió usar solo métodos dentro del alcance del curso: sin solvers externos ni OR-Tools.

## Otros archivos

[`otros-archivos/`](/corte-3-programacion-scheduling/otros-archivos/README.md) guarda un Excel de **otra materia (Gerencia Financiera)** que estaba en la carpeta `CORTE 3/`. Se incluyó para no omitir nada, pero **no es material de Planeación**.

## Cuidado con estos errores

- Las plantillas del profesor para la competencia tienen errores. Por ejemplo, `calcular_makespan_penalizado` del Reto 1 toma el tipo del último lote de la secuencia.
- Algunos Excel de una máquina reinician el reloj o tienen un objetivo constante.

Todos están documentados en [`../ERRATAS.md`](/ERRATAS.md).


---

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

<!-- fuente: corte-3-programacion-scheduling/01-introduccion-scheduling/README.md -->
# Introducción a la programación de la producción: scheduling (Corte 3)

## Qué cubre

Abre el corte 3. Ubica la programación detallada (*scheduling*) al final de la jerarquía Pronósticos → Planeación agregada → Plan maestro → MRP. Define los parámetros ($p_{ij}$, $r_j$, $d_j$, $w_j$) y los indicadores ($C_j$, $C_{max}$, $L_j$, $T_j$, $U_j$, $E_j$) y presenta la notación $\alpha|\beta|\gamma$ de Graham et al. (1979) para clasificar problemas. Termina con propiedades generales: programas sin retrasos, programas activos, anomalías del makespan en máquinas paralelas y jerarquía de complejidad.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [L16-intro-scheduling.md](/corte-3-programacion-scheduling/01-introduccion-scheduling/L16-intro-scheduling.md) (gemelo de `L16-intro-scheduling.pdf`) | Presentación "Lec 16 - intro Scheduling", 49 diapositivas, transcritas página por página con los Gantt en tablas | Sí (único archivo) |

## Orden de estudio sugerido

1. Contexto (pp. 3-6): de dónde vienen las órdenes (MRP) y qué es el machine scheduling.
2. Ejemplo de dos trabajos en dos máquinas (pp. 7-9): el orden cambia el makespan.
3. Elementos, objetivos, parámetros e indicadores (pp. 11-14). Conviene aprenderlos de memoria, porque se usan en todo el corte.
4. Del MRP a las órdenes y al Gantt (pp. 15-17).
5. Notación $\alpha|\beta|\gamma$ (pp. 18-31) y ejemplos de lectura (pp. 32-36).
6. Tipos de programación, programas sin retrasos y activos, y anomalías en $P2|prec|C_{max}$ (pp. 37-44).
7. Complejidad y realidad industrial (pp. 45-48).
8. Después, seguir con [02-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/README.md).

## Conceptos y fórmulas clave

Detalle completo en el [resumen de L16](/corte-3-programacion-scheduling/01-introduccion-scheduling/L16-intro-scheduling.md#resumen).

- Indicadores, con $C_j$ = instante en que termina el trabajo $j$, $r_j$ = liberación, $d_j$ = fecha de entrega, $w_j$ = peso y $n$ = número de trabajos:

$$C_{max}=\max_j C_j\qquad \bar F=\frac1n\sum_j(C_j-r_j)\qquad L_j=C_j-d_j\qquad T_j=\max(L_j,0)$$

$$E_j=\max(0,\,d_j-C_j)\qquad U_j=\mathbb 1[T_j>0]\qquad \sum w_jT_j,\ \sum U_j,\ L_{max}=\max_j L_j,\ \sum w_jC_j,\ \sum w_j(1-e^{-rC_j})$$

- Notación $\alpha|\beta|\gamma$:
  - $\alpha$ (ambiente): $1$, $Pm$, $Qm$, $Rm$, $Fm$, $FFc$, $Jm$, $FJc$, $Om$.
  - $\beta$ (restricciones): $r_j$, $s_{jk}$, *prmp*, *prec*, *brkdwn*, $M_j$, *prmu*, *block*, *nwt*, *recrc*.
  - $\gamma$ (objetivo): $C_{max}$, $L_{max}$, $\sum w_jC_j$, $\sum w_jT_j$, $\sum U_j$…
- Programa **sin retrasos** (*non-delay*): ninguna máquina queda ociosa si hay trabajos esperando. Programa **activo**: ninguna operación puede adelantarse sin retrasar otra.
- Hay $n!$ secuencias posibles en una máquina. $1||\sum C_j \propto 1||\sum w_jC_j \propto Pm||\sum w_jC_j \propto Qm|prec|\sum w_jC_j$ ($\propto$ = "es caso especial de").

## Ejercicios resueltos disponibles

Todos están en [L16-intro-scheduling.md](/corte-3-programacion-scheduling/01-introduccion-scheduling/L16-intro-scheduling.md).

| Ejercicio | Páginas | Resultado principal |
|---|---|---|
| 2 trabajos, 2 máquinas en serie (A: 8/5, B: 7/10) | 7-9 | A-B: $C_{max}=25$; B-A: $C_{max}=22$ |
| Registros MRP de 2 productos → 4 órdenes | 15-16 | $p$ = lote × factor: 0.4, 0.6, 0.5 y 0.7 semanas |
| Gantt de las 4 órdenes | 17 | La orden 0004 termina en 4.2 con $d=4$ (0.2 semanas tarde) |
| $P2\|prec\|C_{max}$, 10 trabajos | 40-41 | Óptimo $C_{max}=31$ |
| El mismo con $p_j-1$ | 42 | $C_{max}=32$: el makespan sube (anomalía) |
| El mismo con 3 máquinas | 43 | $C_{max}=36$: el makespan sube (anomalía) |
| Lectura de notación | 32-36 | $FFc\|r_j\|\sum w_jT_j$, $Pm\|r_j,M_j\|\sum w_jT_j$, $P\infty\|prec\|C_{max}$ |

## Relación con otros temas y proyectos

- Antes, en el corte 2, el MRP genera las órdenes que aquí se programan: [04-bom-y-mrp](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/), y [05-mrp-ii-y-capacidad](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/) para la capacidad (CRP) y el backward scheduling.
- Después: [02-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/README.md) (reglas de despacho, WSPT, EDD, ATC, CR, Moore, Lawler), [03-maquinas-paralelas](/corte-3-programacion-scheduling/03-maquinas-paralelas/), [04-flow-shop](/corte-3-programacion-scheduling/04-flow-shop/) y [05-job-shop](/corte-3-programacion-scheduling/05-job-shop/).
- Compendio de métodos del corte: [00-compendio-metodos-scheduling](/corte-3-programacion-scheduling/00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md).
- Proyecto del corte: [proyecto-competencia-scheduling](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/README.md), que plantea dos problemas en esta notación: $F3|prmu,s_{ij}|C_{max}$ y $P3|r_j,prec|\sum w_jT_j$.


---

<!-- fuente: corte-3-programacion-scheduling/01-introduccion-scheduling/L16-intro-scheduling.md -->
# L16-intro-scheduling

> **Archivo:** [`L16-intro-scheduling.pdf`](/corte-3-programacion-scheduling/01-introduccion-scheduling/L16-intro-scheduling.pdf) · **Corte 3** · 49 páginas  
> **Nombre original:** `CORTE 3/Lec 16 - intro Scheduling.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** introducción a la programación de la producción (*scheduling*): dónde encaja en la jerarquía de planeación, sus elementos, sus indicadores, la notación $\alpha|\beta|\gamma$ de Graham et al. (1979) y algunas propiedades (programas sin retrasos, programas activos, anomalías y jerarquía de complejidad).

**Ideas clave**

- El scheduling es el último eslabón de la jerarquía: Pronósticos → Planeación agregada → Plan maestro → MRP → **Programación detallada**. Recibe las órdenes que libera el MRP y entrega un programa al despacho y al taller (pp. 3-4, 15-16).
- Elementos: trabajos (disponibilidad $r_j$, fecha de entrega $d_j$, tiempo de proceso $p_{ij}$, prioridad $w_j$, setup, ruta) y máquinas (configuración y capacidad) (pp. 11, 13).
- Objetivos típicos: cumplir fechas, bajar el WIP y el tiempo de flujo, usar bien las máquinas, reducir setups y costos (p. 12).
- Notación $\alpha|\beta|\gamma$: $\alpha$ = ambiente de máquinas, $\beta$ = restricciones, $\gamma$ = función objetivo (pp. 18-31).
- El orden de los trabajos cambia el resultado: en el ejemplo de dos trabajos y dos máquinas, A-B da $C_{max}=25$ y B-A da $C_{max}=22$ (pp. 7-9).
- **Anomalías** en $P2|prec|C_{max}$: el óptimo es 31; si se reducen todos los tiempos en una unidad, la programación sin esperas da 32, y con 3 máquinas da 36. Más recursos o tiempos más cortos no garantizan un mejor makespan (pp. 40-43).
- Programación sin retrasos (*non-delay*): no se deja una máquina ociosa si hay trabajos esperando. Programa activo: ninguna operación puede adelantarse a un hueco sin retrasar otra (pp. 39, 44).
- Hay $n!$ secuencias posibles en una máquina; la mayoría de los problemas son NP-hard, pero $1||\sum w_jC_j$ se resuelve en tiempo polinomial (p. 46).
- En la vida real hay reglas implícitas, fechas y prioridades flexibles y objetivos no clásicos; existe software comercial como Siemens Preactor (pp. 47-48).

**Fórmulas y métodos**

Parámetros (p. 13): $n$ trabajos indexados en $j$, $m$ máquinas indexadas en $i$; $p_{ij}$ tiempo de proceso del trabajo $j$ en la máquina $i$; $r_j$ liberación; $d_j$ fecha de entrega; $w_j$ prioridad o peso.

Indicadores (p. 14), con $C_j$ = instante en que termina el trabajo $j$:

$$C_{max}=\max_j C_j \qquad \bar F=\frac{1}{n}\sum_j (C_j-r_j)$$

$$L_j=C_j-d_j \qquad T_j=\max(L_j,0) \qquad E_j=\max(-L_j,0)=\max(0,d_j-C_j)$$

$$U_j=\begin{cases}1 & T_j>0\\ 0 & \text{en otro caso}\end{cases}\qquad \bar T=\frac{1}{n}\sum_j T_j \qquad \sum_j w_jT_j \qquad \sum_j U_j$$

Funciones objetivo $\gamma$ (pp. 27-31):

- $C_{max}=\max\{C_1,\dots,C_N\}$: al minimizarlo se suele maximizar la utilización.
- $L_{max}=\max\{L_1,\dots,L_N\}$: mide la peor violación de la fecha de entrega.
- $\sum w_jC_j$: tiempo ponderado total de terminación (*weighted flow time*); representa el costo de mantener inventario.
- $\sum w_j(1-e^{-rC_j})$: tiempo ponderado descontado, con $r$ = tasa de descuento (p. ej. 10 %); costo marginal de terminación decreciente.
- $\sum w_jT_j$: tardanza ponderada total; $\sum w_jE_j$: anticipo ponderado total.

Ambientes $\alpha$ (pp. 19-22):

| Símbolo | Ambiente | Descripción |
|---|---|---|
| 1 | Una máquina | Un solo recurso. |
| $Pm$ | Máquinas idénticas en paralelo | Cada trabajo necesita una operación en cualquiera de las $m$ máquinas. |
| $Qm$ | Paralelas uniformes | La máquina $i$ tiene velocidad $v_i$; tiempo $p_j/v_i$. |
| $Rm$ | Paralelas no relacionadas | La velocidad $v_{ij}$ depende de la máquina y del trabajo. |
| $Fm$ | Flow shop | $m$ máquinas en serie; todos los trabajos siguen la misma ruta. |
| $FFc$ | Flow shop flexible | $c$ etapas con máquinas paralelas idénticas en cada una. |
| $Jm$ | Job shop | Cada trabajo tiene su propia ruta. |
| $FJc$ | Job shop flexible | $c$ etapas con máquinas paralelas; ruta propia por trabajo. |
| $Om$ | Open shop | Todos pasan por todas las máquinas, sin ruta fija. |

Restricciones $\beta$ (pp. 23-26): $r_j$ (liberación), $s_{jk}$ (setups dependientes de la secuencia; $s_{0k}$ inicio, $s_{j0}$ limpieza final, $s_{ijk}$ dependiente de la máquina), *prmp* (interrupciones), *prec* (precedencias: cadenas, intree, outtree), *brkdwn* (fallas), $M_j$ (elegibilidad de máquinas), *prmu* (misma secuencia en todas las máquinas), *block* (buffer limitado), *nwt* (sin espera) y *recrc* (recirculación).

Jerarquía de complejidad (pp. 45-46): $A\propto B$ significa que $A$ es un caso especial de $B$ (un algoritmo para $B$ resuelve $A$):

$$1||\sum C_j\ \propto\ 1||\sum w_jC_j\ \propto\ Pm||\sum w_jC_j\ \propto\ Qm|prec|\sum w_jC_j$$

**Ejemplos resueltos**

| Página | Ejemplo | Resultado |
|---|---|---|
| 7-9 | 2 trabajos en 2 máquinas en serie (A: 8 y 5; B: 7 y 10) | A-B: $C_{max}=25$; B-A: $C_{max}=22$ |
| 15-16 | Registros MRP de 2 productos → 4 órdenes de producción | Órdenes 0001-0004 con $p$ = 0.4, 0.6, 0.5 y 0.7 semanas ($p$ = lote × factor) |
| 17 | Gantt de las 4 órdenes en una máquina | La orden 0004 termina en 4.2 con $d=4$: tardanza de 0.2 semanas |
| 40-41 | $P2\|prec\|C_{max}$ con 10 trabajos | Solución óptima $C_{max}=31$ |
| 42 | Mismo problema con $p_j-1$ | Programa sin esperas con $C_{max}=32$ (empeora) |
| 43 | Mismo problema con 3 máquinas | $C_{max}=36$ (empeora) |
| 32-36 | Lectura de la notación | $FFc\|r_j\|\sum w_jT_j$ (fábrica de papel), $Pm\|r_j,M_j\|\sum w_jT_j$ (puertas de aeropuerto), $P\infty\|prec\|C_{max}$ (proyecto) |

**Páginas clave**

- Contexto y jerarquía: pp. 3-6.
- Ejemplo introductorio de secuenciación: pp. 7-9.
- Elementos, objetivos, parámetros e indicadores: pp. 11-14.
- Del MRP a las órdenes y al Gantt: pp. 15-17.
- Notación $\alpha|\beta|\gamma$: pp. 18-31; ejemplos de notación: pp. 32-36.
- Tipos de programación, sin retrasos, anomalías y programa activo: pp. 37-44.
- Complejidad y realidad industrial: pp. 45-48.

**Relación con otros archivos del repo**

- Siguiente tema, una máquina (reglas de despacho, WSPT, EDD, ATC, CR, Moore): [L17](/corte-3-programacion-scheduling/02-una-maquina/L17-single-machine-scheduling.md) y su [README](/corte-3-programacion-scheduling/02-una-maquina/README.md).
- Máquinas en paralelo ($Pm$): [L18](/corte-3-programacion-scheduling/03-maquinas-paralelas/L18-parallel-machine-scheduling.md). Flow shop ($Fm$; el ejemplo de las pp. 7-9 es un flow shop de 2 máquinas, y la secuencia B-A coincide con la que da la regla de Johnson, cosa que la diapositiva no dice): [L19](/corte-3-programacion-scheduling/04-flow-shop/L19-flow-shop-scheduling.md). Job shop: [job-shop-y-flexible-job-shop](/corte-3-programacion-scheduling/05-job-shop/job-shop-y-flexible-job-shop.md).
- Compendio de métodos del corte 3: [metodos-programacion-produccion-corte3](/corte-3-programacion-scheduling/00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md).
- Los registros MRP de la p. 15 vienen del corte 2: [L14 MRP](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md) y [L15 MRP II](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md).
- La notación se aplica en la competencia: [proyecto-competencia-scheduling](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/README.md) ($F3|prmu,s_{ij}|C_{max}$ y $P3|r_j,prec|\sum w_jT_j$).

**Observaciones sobre el material**

- En la p. 7 los subíndices de $p$ van como (trabajo, máquina): $p_{11}=8$ es A en M1 y $p_{12}=5$ es A en M2. En la p. 13, en cambio, $p_{ij}$ es el trabajo $j$ en la máquina $i$.
- En el Gantt de la p. 43, el trabajo 9 se dibuja de 6 a 15 (9 unidades) aunque $p_9=8$. El makespan (36) no cambia.
- En la p. 17 hay un bloque azul claro sin rótulo entre 2.0 y 2.2; no se explica qué representa.
- La p. 46 dice "Estos problemas se conocen como NP-Hard" justo antes de aclarar que $1||\sum w_jC_j$ es polinomial. Lo NP-hard son los problemas más generales de la cadena, como $Pm||\sum w_jC_j$; esta lectura es deducida.


---

<!-- fuente: corte-3-programacion-scheduling/02-una-maquina/README.md -->
# Programación de una máquina (Corte 3)

## Qué cubre

Secuenciación de $n$ trabajos en una sola máquina ($1|\beta|\gamma$). Incluye las reglas de despacho estáticas (FIFO, SPT, EDD, WSPT) y dinámicas (holgura mínima MS, ATC, razón crítica CR), los casos con regla óptima conocida (WSPT para $\sum w_jC_j$, EDD para $L_{max}$), las precedencias en cadena con factor $\rho$, la *preemption* con liberaciones, el algoritmo de Lawler ($h_{max}$), el de Moore-Hodgson ($\sum U_j$) y el uso de Solver de Excel como método aproximado.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [L17-single-machine-scheduling.md](/corte-3-programacion-scheduling/02-una-maquina/L17-single-machine-scheduling.md) (gemelo del PDF) | Presentación "Lec 17 - Single Machine Scheduling", 49 diapositivas, con todas las secuencias y Gantt en tablas y un resumen con la comparación de reglas | **Sí (1.º)** |
| [ejemplo-1-programacion-produccion.md](/corte-3-programacion-scheduling/02-una-maquina/ejemplo-1-programacion-produccion.md) (gemelo del .xlsx) | Ejemplo cotidiano de 4 actividades con $r_j$, $p_j$, $w_j$ y $s_j$: $C_j$, flujo y $w_jC_j$ | 2.º (corto) |
| [programacion-produccion-una-maquina.md](/corte-3-programacion-scheduling/02-una-maquina/programacion-produccion-una-maquina.md) (gemelo del .xlsx) | Libro de clase con 3 hojas: reglas de despacho sobre 6 trabajos (natural, azar, SPT, WSPT, EDD, MS), cadenas y factor $\rho$, preemption (ejercicio p. 25 de L17) y una hoja para Solver | 3.º |
| [programacion-produccion-una-maquina-datos/Reglas_de_Despacho.csv](/corte-3-programacion-scheduling/02-una-maquina/programacion-produccion-una-maquina-datos/Reglas_de_Despacho.csv) | Volcado CSV completo de la hoja `Reglas de Despacho` | Solo como referencia |
| [atc.py](/corte-3-programacion-scheduling/02-una-maquina/atc.py) | Script de Python (sin gemelo) que aplica la regla ATC al ejercicio de L17 (pp. 43-45) y verifica la solución de clase. Se explica abajo | 4.º |

## `atc.py`: regla ATC (Apparent Tardiness Cost)

**Qué hace.** Construye la secuencia ATC del ejercicio de L17 (pp. 43-45), calcula $C_j$, $L_j$ y $w_jT_j$ y las medidas de desempeño, y las compara con la solución de la diapositiva 45. Solo usa la biblioteca estándar (`argparse`, `math`).

**Entradas** (fijas en el código, diccionario `TRABAJOS`):

| Trabajo | $p_j$ | $d_j$ | $w_j$ |
|---|---|---|---|
| 1 | 5 | 1 | 2 |
| 2 | 7 | 9 | 3 |
| 3 | 2 | 10 | 2 |
| 4 | 8 | 6 | 1 |

Opciones de línea de comandos:

- `--K <valor>`: constante $K$ (por defecto 1).
- `--pbar-fijo`: usa $\bar p$ de todos los trabajos (5.5) en vez de recalcularlo con los pendientes.

`ESPERADO` guarda la solución de clase: secuencia 1-3-2-4, flujo promedio 12, retardo máximo 16 y tardanza ponderada 39.

**Algoritmo** (heurística constructiva voraz):

1. $t=0$ y todos los trabajos pendientes. No hay liberaciones: todos están disponibles desde 0.
2. Se calcula $\bar p$ = promedio de $p_j$ de los pendientes, o el de todos con `--pbar-fijo`.
3. Para cada pendiente, `indice_atc` calcula

   $$I_j(t)=\frac{w_j}{p_j}\exp\!\left(-\frac{\max(d_j-p_j-t,\,0)}{K\,\bar p}\right)$$

   donde $\max(d_j-p_j-t,0)$ es la holgura del trabajo.
4. Se elige el de mayor $I_j(t)$; si hay empate, el de menor número. Se agrega a la secuencia y $t \leftarrow t+p_j$.
5. Se repite hasta programar todos.
6. `evaluar` recorre la secuencia y calcula $C_j$ (suma acumulada de $p$), $L_j=C_j-d_j$, $T_j=\max(L_j,0)$ y $w_jT_j$. Devuelve el flujo promedio $\sum C_j/n$, el flujo ponderado $\sum w_jC_j$, $L_{max}$ y $\sum w_jT_j$.
7. `imprimir_iteraciones` y `imprimir_tabla` muestran el detalle; `verificar` compara con `ESPERADO`.

**Resultado.** Corre sin instalar nada. Salida real de `python -I atc.py` (modo por defecto, $K=1$, $\bar p$ recalculado):

```
Regla ATC  |  K = 1.0  |  p_barra = trabajos no programados

Indices ATC en cada decision (* = trabajo elegido)
   t  p_barra |     I(1)     I(2)     I(3)     I(4)
----------------------------------------------------
   0    5.500 |  0.4000*  0.2979   0.2335   0.1250 
   5    5.667 |        -  0.4286   0.5890*  0.1250 
   7    7.500 |        -  0.4286*        -  0.1250 
  14    8.000 |        -        -        -  0.1250*

Programa ATC
Secuencia         1     3     2     4
pj                5     2     7     8
Cj                5     7    14    22
dj                1    10     9     6
Lj = Cj - dj      4    -3     5    16
wj                2     2     3     1
wjTj              8     0    15    16

Secuencia ATC: 1 -> 3 -> 2 -> 4
Flujo promedio          = 12
Flujo ponderado (wjCj)  = 88
Retardo maximo (Lmax)   = 16
Tardanza ponderada      = 39

Comparacion con la diapositiva 45
  Secuencia            obtenido = [1, 3, 2, 4]   esperado = [1, 3, 2, 4]   OK
  Flujo promedio       obtenido = 12.0           esperado = 12             OK
  Retardo max          obtenido = 16             esperado = 16             OK
  Tardanza ponderada   obtenido = 39             esperado = 39             OK
  Resultado: coincide con la solucion de clase
```

Comparación de modos (salidas reales):

| Modo | $\bar p$ en $t$ = 0, 5, 7, 14 | $I_3(5)$ | Secuencia | $\sum C_j/n$ | $\sum w_jC_j$ | $L_{max}$ | $\sum w_jT_j$ | ¿Coincide con la diapositiva? |
|---|---|---|---|---|---|---|---|---|
| Por defecto ($K=1$) | 5.5, 5.667, 7.5, 8 | 0.5890 | 1-3-2-4 | 12 | 88 | 16 | 39 | Sí |
| `--pbar-fijo` ($K=1$) | 5.5 siempre | 0.5796 | 1-3-2-4 | 12 | 88 | 16 | 39 | Sí, y los índices son exactamente los de la p. 45 (0.40, 0.30, 0.23, 0.13 / 0.43, 0.58 / 0.43) |
| `--K 2` | 5.5, 6.667, 6.5, 8 | — | 3-2-1-4 | 11.75 | 81 | 16 | 42 | No |

Conclusión: con $K=1$ la secuencia de clase (1-3-2-4, $\sum w_jT_j=39$) sale igual con $\bar p$ fijo o recalculado; la diapositiva usó $\bar p$ fijo. Con $K=2$ la holgura pesa menos, el índice se acerca a WSPT ($w_j/p_j$) y la secuencia pasa a 3-2-1-4: mejor $\sum w_jC_j$ (81, el óptimo WSPT) pero peor tardanza ponderada (42). $K$ es un parámetro que hay que calibrar.

**Advertencias.** El docstring llama al archivo `atc_lec17.py`, pero se llama `atc.py`. El script no maneja liberaciones $r_j$ ni setups, y los datos están fijos en el código.

## Orden de estudio sugerido

1. [L17](/corte-3-programacion-scheduling/02-una-maquina/L17-single-machine-scheduling.md), pp. 2-13: motivación ($n!$), WSPT, reglas estáticas y dinámicas (MS, ATC).
2. [ejemplo-1](/corte-3-programacion-scheduling/02-una-maquina/ejemplo-1-programacion-produccion.md): calcular $C_j$ con liberaciones.
3. [programacion-produccion-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/programacion-produccion-una-maquina.md), hoja `Reglas de Despacho`: comparar las reglas sobre 6 trabajos.
4. L17, pp. 14-26, y la hoja `Restricciones de Precedencia`: cadenas, factor $\rho$ y preemption.
5. L17, pp. 27-42: Lawler, EDD, CR paso a paso, Moore-Hodgson y la regla para $\sum T_j$.
6. L17, pp. 43-45, y `atc.py`: ejercicio FIFO/SPT/EDD/ATC.
7. L17, pp. 46-48, y la hoja `Tardanza Máxima`: métodos exactos y Solver.

## Conceptos y fórmulas clave

Detalle en el [resumen de L17](/corte-3-programacion-scheduling/02-una-maquina/L17-single-machine-scheduling.md#resumen).

- **WSPT** (óptima para $1||\sum w_jC_j$): ordenar por $w_j/p_j$ decreciente. **SPT** minimiza $\sum C_j/n$. **EDD** (óptima para $1||L_{max}$): ordenar por $d_j$ creciente.
- **Holgura mínima:** $s_j=\max(d_j-p_j-t,0)$, menor primero.
- **ATC:** $I_j(t)=\dfrac{w_j}{p_j}\exp\!\left(-\dfrac{\max(d_j-p_j-t,0)}{K\bar p}\right)$, mayor primero. $K$ es una constante de escala y $\bar p$ el promedio de $p$ de los no programados.
- **Razón crítica:** $CR_j=\dfrac{\max(d_j-t,0)}{p_j}$, menor primero; empate por SPT.
- **Cadenas:** si no se pueden interrumpir, mayor $\sum w/\sum p$ primero. Si se pueden cortar, factor $\rho=\max_{l}\dfrac{\sum_{j\le l}w_j}{\sum_{j\le l}p_j}$, procesando hasta $l^*$.
- **Preemption** ($1|r_j,prmp|\sum w_jC_j$): en cada evento, mayor $w_j/p_j^{\text{restante}}$.
- **Lawler** ($1|prec|h_{max}$): de atrás hacia adelante, se pone de último el trabajo elegible con menor $h_j\!\left(\sum_{k\in J^c}p_k\right)$.
- **Moore-Hodgson** ($1||\sum U_j$): orden EDD; si alguno llega tarde, se saca el más largo de los programados.
- **$1||\sum T_j$:** si $p_j\le p_k$ y $d_j\le d_k$, existe un óptimo con $j$ antes que $k$.

## Ejercicios resueltos disponibles

| Ejercicio | Archivo | Resultado principal |
|---|---|---|
| FIFO, SPT, EDD y ATC con 4 trabajos ($p$ = 5, 7, 2, 8; $d$ = 1, 9, 10, 6; $w$ = 2, 3, 2, 1) | [L17](/corte-3-programacion-scheduling/02-una-maquina/L17-single-machine-scheduling.md) pp. 43-45; [atc.py](/corte-3-programacion-scheduling/02-una-maquina/atc.py) | FIFO: 13.25 / 16 / 41; SPT: **11.25** / 16 / 43; EDD: 15 / **12** / 72; ATC: 12 / 16 / **39** (flujo promedio / $L_{max}$ / $\sum w_jT_j$) |
| Razón crítica con los mismos 4 trabajos | L17 pp. 33-37 | 1-4-3-2: flujo 13.75, $L_{max}=13$, $\sum w_jT_j=64$ |
| Cadenas 1→2→3→4 y 5→6→7 (factor $\rho$) | L17 pp. 18-23 | 1-2-5-6-3-7-4 |
| Lawler con $h_1=1+C_1$, $h_2=1.2C_2$, $h_3=10$ | L17 pp. 29-31 | 1-2-3 o 2-1-3, $h_{max}=10$ |
| Moore-Hodgson, 5 trabajos | L17 pp. 40-41 | 3-4-5-1-2, $\sum U_j=2$ |
| WSPT, tareas A-E | L17 p. 10 (resuelto en el .md) | A-D-E-B-C, $\sum w_jC_j=779$ |
| 6 trabajos con natural, azar, SPT, WSPT, EDD y MS | [programacion-produccion-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/programacion-produccion-una-maquina.md) | WSPT 6-5-2-4-1-3 da el menor $\sum w_jC_j$ (161); SPT el menor $\sum C_j/n$ (16); EDD el menor $L_{max}$ (7); MS da $\sum T_j=16$ |
| Cadenas A-F (sin y con interrupción) | ídem, hoja `Restricciones de Precedencia` | Sin romper: C-B-A-E-F-D; con $\rho$: $l^*$ = A (0.35) y E (0.38) |
| Preemption con $r_j$ (L17 p. 25), $w_j=1$ | ídem, hoja `Restricciones de Precedencia` | 1, 3, 4, 5, 6, 7, 2; $C_{max}=89$, $\sum C_j=305$ |
| 4 actividades cotidianas con $r_j$ | [ejemplo-1](/corte-3-programacion-scheduling/02-una-maquina/ejemplo-1-programacion-produccion.md) | Flujo promedio 35.165 h |
| Solver Evolutionary para $1\|\|\sum w_jT_j$ (wt40_1) | L17 p. 48; hoja `Tardanza Máxima` | Captura: $\sum w_jT_j=16822$ (óptimo conocido 913) |

Varias hojas del Excel tienen errores de fórmula (reloj reiniciado en EDD, rango mal tomado en un promedio, objetivo constante en `Tardanza Máxima`). Están señalados y corregidos en [programacion-produccion-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/programacion-produccion-una-maquina.md#observaciones).

## Relación con otros temas y proyectos

- Antes: [01-introduccion-scheduling](/corte-3-programacion-scheduling/01-introduccion-scheduling/README.md), con la notación $\alpha|\beta|\gamma$ y los indicadores.
- Después: [03-maquinas-paralelas](/corte-3-programacion-scheduling/03-maquinas-paralelas/) (extiende SPT/LPT a $Pm$), [04-flow-shop](/corte-3-programacion-scheduling/04-flow-shop/) y [05-job-shop](/corte-3-programacion-scheduling/05-job-shop/).
- Compendio con hojas `02_1Maq_Basicos`, `03_1Maq_MS_ATC`, `04_1Maq_Precedencia`, `05_1Maq_Preemption` y `06_1Maq_Lawler`: [metodos-programacion-produccion-corte3](/corte-3-programacion-scheduling/00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md).
- Proyecto: el reto 2 de la [competencia](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/README.md) ($P3|r_j,prec|\sum w_jT_j$) usa WSPT, ATC, cadenas y EDD como reglas de arranque.
- Corte 2: la regla de "inicio en $\max(r_j, C_{\text{anterior}})$" se parece al backward/forward scheduling de [05-mrp-ii-y-capacidad](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/).


---

<!-- fuente: corte-3-programacion-scheduling/02-una-maquina/L17-single-machine-scheduling.md -->
# L17-single-machine-scheduling

> **Archivo:** [`L17-single-machine-scheduling.pdf`](/corte-3-programacion-scheduling/02-una-maquina/L17-single-machine-scheduling.pdf) · **Corte 3** · 49 páginas  
> **Nombre original:** `CORTE 3/Lec 17 - Single Machine Scheduling.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** programación de una sola máquina ($1|\beta|\gamma$): reglas de despacho estáticas y dinámicas (FIFO, SPT, EDD, WSPT, MS, ATC, CR), casos con solución óptima conocida (WSPT, EDD, cadenas con factor $\rho$, Lawler, Moore-Hodgson) y métodos exactos.

**Ideas clave**

- El caso de una máquina es simple, pero sirve de base para heurísticas y para descomponer problemas más grandes, por ejemplo con un único cuello de botella (p. 2).
- En general es NP-hard: hay $n!$ secuencias (20 trabajos dan $2.43\times10^{18}$), así que la enumeración exhaustiva es inviable (pp. 3-5).
- Hay métodos exactos (programación dinámica, programación entera mixta, ramificación y acotación), pero en la industria se busca una "buena programación" que los encargados entiendan (pp. 6, 46).
- Casi ninguna regla de despacho garantiza el óptimo. Las excepciones son WSPT para $1||\sum w_jC_j$ y EDD para $1||L_{max}$ (p. 7).
- Reglas **estáticas** (dependen solo de los datos del trabajo): FIFO, SPT, EDD, WSPT. Reglas **dinámicas** (dependen de $t$ o del estado de la máquina): MS, ATC, CR (pp. 11-13, 33).
- Con precedencias en cadena: si una cadena no se puede interrumpir, se empieza por la de mayor $\sum w_j/\sum p_j$. Si se puede cortar, se usa el factor $\rho$ y se procesa la cadena hasta $l^*$ (pp. 14-23).
- Con liberaciones y *preemption* ($1|r_j,prmp|\sum w_jC_j$) se elige en cada evento el trabajo con mayor $w_j/(\text{tiempo restante})$. La regla no es necesariamente óptima (pp. 24-26).
- Lawler resuelve $1|prec|h_{max}$ hacia atrás; con $h_j=C_j-d_j$ queda $1||L_{max}$, que EDD resuelve (pp. 27-32).
- Moore-Hodgson resuelve $1||\sum U_j$: recorre en orden EDD y, si un trabajo llega tarde, saca el más largo de los ya programados (pp. 38-41).
- $1||\sum T_j$ es NP-hard, pero hay una regla de dominancia: si $p_j\le p_k$ y $d_j\le d_k$, existe un óptimo con $j$ antes que $k$ (p. 42).

**Fórmulas y métodos**

Notación: $p_j$ tiempo de proceso, $d_j$ fecha de entrega, $w_j$ peso o prioridad, $r_j$ liberación, $t$ instante actual, $C_j$ terminación, $L_j=C_j-d_j$, $T_j=\max(L_j,0)$, $U_j=1$ si $T_j>0$.

| Regla | Criterio de orden | Cuándo usarla |
|---|---|---|
| FIFO / FCFS | Orden de llegada | Referencia o regla por defecto. |
| SPT | $p_{[k]}\le p_{[k+1]}$ | Minimiza el flujo promedio $\sum C_j/n$ (sin pesos). |
| EDD | $d_{[k]}\le d_{[k+1]}$ | Óptima para $1\|\|L_{max}$. |
| WSPT | $w_{[k]}/p_{[k]}\ge w_{[k+1]}/p_{[k+1]}$ | Óptima para $1\|\|\sum w_jC_j$; complejidad $O(n\log n)$. |
| MS (holgura mínima) | $s_j=\max(d_j-p_j-t,0)$, menor primero | Dinámica, orientada a fechas de entrega. |
| ATC | $I_j(t)$ mayor primero | Heurística para $\sum w_jT_j$. |
| CR (razón crítica) | $CR_j$ menor primero; empate por SPT | Dinámica, orientada a fechas de entrega. |

Índice ATC (Apparent Tardiness Cost), donde $K$ es una constante de escala que se elige y $\bar p$ es el tiempo promedio de los trabajos no programados:

$$I_j(t)=\frac{w_j}{p_j}\exp\!\left(-\frac{\max(d_j-p_j-t,\,0)}{K\,\bar p}\right)$$

Razón crítica:

$$CR_j=\frac{\max(d_j-t,\,0)}{p_j}=\frac{\text{tiempo que resta hasta la fecha de entrega}}{\text{tiempo de procesamiento restante}}$$

Cadenas (p. 15, sin interrupción): empezar por la cadena con mayor $\sum w_j/\sum p_j$. Factor $\rho$ de una cadena $1\to2\to\dots\to k$ (p. 16), donde $l^*$ es el trabajo donde se alcanza el máximo:

$$\rho=\frac{\sum_{j=1}^{l^*}w_j}{\sum_{j=1}^{l^*}p_j}=\max_{1\le l\le k}\frac{\sum_{j=1}^{l}w_j}{\sum_{j=1}^{l}p_j}$$

Regla: elegir la cadena disponible con mayor $\rho$, procesarla hasta $l^*$ sin interrupción y recalcular el $\rho$ de lo que queda.

Algoritmo de Lawler para $1|prec|h_{max}$ (p. 28), con $h_j(C_j)$ una función de costo no decreciente en $C_j$. $J^c$ son los trabajos sin programar y $J'\subseteq J^c$ los que pueden ir de últimos (sus sucesores ya están programados). Se elige

$$j^*=\arg\min_{j\in J'}\ h_j\!\left(\sum_{k\in J^c}p_k\right)$$

y se coloca en la última posición libre: se construye la secuencia de atrás hacia adelante. Luego se saca de $J^c$ y se actualiza $J'$.

Algoritmo de Moore-Hodgson para $1||\sum U_j$ (p. 39): tomar los trabajos en orden EDD y agregarlos a $J$. Si $\sum_{j\in J}p_j>d_{j^*}$, mover a $J^d$ (tardíos) el trabajo de $J$ con mayor $p_j$. La secuencia final es $J$ en orden EDD seguida de $J^d$.

$1|r_j,prmp|\sum w_jC_j$ (p. 24): en cada evento (llegada o terminación) se procesa el trabajo con mayor $w_j/p_j^{\text{restante}}$.

**Ejemplos resueltos**

| Página | Problema | Resultado |
|---|---|---|
| 10 | $1\|\|\sum w_jC_j$, tareas A-E | La diapositiva no lo resuelve. Cálculo propio con WSPT: A-D-E-B-C, $\sum w_jC_j=779$ |
| 18-23 | Cadenas 1→2→3→4 y 5→6→7 con factor $\rho$ | $\rho$ = 2.66 (trabajo 2) y 2.08 (trabajo 6); luego 2 (trabajo 3), 1.8 (trabajo 7) y 1.6 (trabajo 4). Secuencia **1-2-5-6-3-7-4**; $\sum w_jC_j=1967$ (cálculo propio) |
| 25 | $1\|r_j,prmp\|\sum w_jC_j$, 7 trabajos | Sin solución en la diapositiva; resuelto en el Excel con $w_j=1$ (ver abajo) |
| 29-31 | Lawler, 3 trabajos con $h_1=1+C_1$, $h_2=1.2C_2$, $h_3=10$ | El trabajo 3 va de último (inicia en $t=5$); 1-2-3 y 2-1-3 son óptimas con $h_{max}=10$ |
| 33-37 | Regla CR, 4 trabajos | **1-4-3-2**: flujo promedio 13.75, $L_{max}=13$, $\sum w_jT_j=64$ |
| 40-41 | Moore-Hodgson, 5 trabajos | **3-4-5-1-2** con $\sum U_j=2$ (tardíos los trabajos 1 y 2) |
| 43-45 | FIFO, SPT, EDD y ATC con los 4 trabajos de la p. 33 | Ver la tabla siguiente |
| 48 | Solver de Excel (Evolutionary) para $1\|\|\sum w_jT_j$, instancia wt40_1 de OR-Library | Captura con $C_{max}=2065$, $\sum T_j=2637$, $\sum w_jT_j=16822$; el óptimo conocido es 913 |

Comparación del ejercicio de las pp. 43-45, con los mismos datos de la p. 33: $p=(5,7,2,8)$, $d=(1,9,10,6)$, $w=(2,3,2,1)$. La columna $\sum w_jC_j$ y la fila WSPT son cálculo propio; lo demás está en las diapositivas.

| Regla | Secuencia | Flujo promedio $\sum C_j/n$ | $L_{max}$ | $\sum w_jT_j$ | $\sum w_jC_j$ |
|---|---|---|---|---|---|
| FIFO | 1-2-3-4 | 13.25 | 16 | 41 | 96 |
| SPT | 3-1-2-4 | **11.25** | 16 | 43 | 82 |
| EDD | 1-4-2-3 | 15 | **12** | 72 | 127 |
| ATC ($K=1$) | 1-3-2-4 | 12 | 16 | **39** | 88 |
| CR (pp. 33-37) | 1-4-3-2 | 13.75 | 13 | 64 | 119 |
| WSPT (no está en las diapositivas) | 3-2-1-4 | 11.75 | 16 | 42 | **81** (óptimo) |

Respuestas del ejercicio:

- Menor flujo promedio: SPT (11.25). Con flujo **ponderado**, que es lo que pregunta la p. 43, SPT también es la mejor de las cuatro reglas pedidas (82), aunque el óptimo lo da WSPT (81).
- Menor retardo máximo: EDD (12), como garantiza la teoría.
- Menor tardanza ponderada: ATC (39).

Preemption, ejercicio de la p. 25. Resuelto en el Excel con $w_j=1$, es decir, eligiendo el menor tiempo restante; los $C_j$ son cálculo propio a partir de ese programa:

| Tramo | Trabajo | Inicio | Fin | Motivo |
|---|---|---|---|---|
| 1 | 1 | 0 | 6 | En $t=0$ están 1, 2, 3; $1/6$ es la mayor razón |
| 2 | 3 | 6 | 14 | En $t=6$: $1/12>1/18$ |
| 3 | 3 (resto) | 14 | 18 | Llega el 4 ($1/10$), pero al 3 le faltan 4 ($1/4$) |
| 4 | 4 | 18 | 25 | En $t=18$: $1/10>1/18$ |
| 5 | 4 (resto) | 25 | 28 | Llegan 5 y 6; al 4 le faltan 3 ($1/3$) |
| 6 | 5 | 28 | 38 | $1/10>1/17>1/18$ |
| 7 | 6 | 38 | 50 | Hasta que llega el 7 |
| 8 | 6 (resto) | 50 | 55 | Al 6 le faltan 5 ($1/5>1/16$) |
| 9 | 7 | 55 | 71 | $1/16>1/18$ |
| 10 | 2 | 71 | 89 | Último trabajo |

$C_j$: 1 = 6, 3 = 18, 4 = 28, 5 = 38, 6 = 55, 7 = 71, 2 = 89; $\sum C_j=305$.

**Páginas clave**

- Motivación y complejidad: pp. 2-7.
- WSPT y $1||\sum w_jC_j$: pp. 8-10.
- Reglas de despacho estáticas y dinámicas (MS, ATC): pp. 11-13.
- Precedencias en cadena y factor $\rho$: pp. 14-23.
- Liberaciones y preemption: pp. 24-26.
- Lawler y $L_{max}$: pp. 27-32.
- Razón crítica paso a paso: pp. 33-37.
- Moore-Hodgson ($\sum U_j$): pp. 38-41. Tardanza total: p. 42.
- Ejercicio FIFO/SPT/EDD/ATC: pp. 43-45.
- Métodos exactos, tarea y Solver: pp. 46-48.

**Relación con otros archivos del repo**

- Excel de clase con FIFO, SPT, WSPT, EDD, MS, cadenas, preemption y una hoja para Solver: [programacion-produccion-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/programacion-produccion-una-maquina.md). Ejemplo cotidiano con $r_j$: [ejemplo-1-programacion-produccion](/corte-3-programacion-scheduling/02-una-maquina/ejemplo-1-programacion-produccion.md).
- Implementación en Python del ejemplo ATC de las pp. 43-45: [atc.py](/corte-3-programacion-scheduling/02-una-maquina/atc.py), explicado en el [README](/corte-3-programacion-scheduling/02-una-maquina/README.md).
- Compendio con hojas de 1 máquina (básicas, MS/ATC, precedencia, preemption, Lawler): [metodos-programacion-produccion-corte3](/corte-3-programacion-scheduling/00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md).
- Notación e indicadores: [L16](/corte-3-programacion-scheduling/01-introduccion-scheduling/L16-intro-scheduling.md). Siguiente tema: [L18 máquinas paralelas](/corte-3-programacion-scheduling/03-maquinas-paralelas/L18-parallel-machine-scheduling.md).
- El reto 2 de la competencia ($P3|r_j,prec|\sum w_jT_j$) usa WSPT, ATC, cadenas y EDD: [proyecto-competencia-scheduling](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/README.md).

**Observaciones sobre el material**

- p. 36: dice $U=\{J3,J4\}$ en $t=13$, pero J4 ya estaba programado; los pendientes son J2 y J3.
- p. 43: pregunta por el flujo **ponderado** promedio, pero las soluciones (pp. 44-45) solo calculan el flujo sin ponderar.
- p. 45: los índices ATC impresos (0.40, 0.30, 0.23, 0.13 / 0.43, 0.58 / 0.43) salen con $K=1$ y $\bar p=5.5$ fijo, el promedio de los cuatro trabajos. La definición de la p. 13 dice que $\bar p$ es el promedio de los no programados; con esa definición $I_3(5)=0.589$, y la secuencia no cambia.
- p. 28: "Añadir j\* a J (al final)" se entiende como la última posición libre: el algoritmo de Lawler construye la secuencia de atrás hacia adelante (interpretación).
- p. 48: la captura de Excel muestra una solución ($\sum w_jT_j=16822$) muy lejos del óptimo publicado (913).


---

<!-- fuente: corte-3-programacion-scheduling/03-maquinas-paralelas/README.md -->
# Máquinas paralelas (Corte 3)

## Qué cubre

Programación de $n$ trabajos de una sola operación en $m$ máquinas paralelas. Hay que decidir a qué máquina va cada trabajo y en qué orden. Incluye algoritmos de lista con LPT y SPT, la garantía de LPT para $Pm||C_{max}$, la optimalidad de SPT para $Pm||\sum C_j$, precedencias (CP y LNS), restricciones de elegibilidad $M_j$ (LFJ y LFM), *preemption* (modelo lineal y *wrap-around*) y el MIP para máquinas no relacionadas $Rm||\sum C_j$, más un Excel con algoritmo genético.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [L18-parallel-machine-scheduling.md](/corte-3-programacion-scheduling/03-maquinas-paralelas/L18-parallel-machine-scheduling.md) (gemelo del PDF) | Presentación "Lec 18 - Parallel Machine Scheduling", 40 diapositivas, con todos los Gantt (LPT, SPT, óptimo, LFJ, Excel) en tablas | **Sí (1.º)** |
| [lns-maquinas-paralelas.md](/corte-3-programacion-scheduling/03-maquinas-paralelas/lns-maquinas-paralelas.md) (gemelo del .xlsx) | Plantilla incompleta (hoja `LFJ`): 15 trabajos con $p_j$ y $w_j$ para repartir en 3 máquinas. Las fórmulas de la máquina 2 están mal; el .md trae un cálculo propio con LPT, SPT y WSPT | 2.º |

## Orden de estudio sugerido

1. L18, pp. 1-7: definiciones, algoritmo de lista y garantía de LPT.
2. L18, pp. 8-16: ejemplos LPT, SPT y óptimo ($P3$ con 15 trabajos y $P4$ con 9 trabajos) y SPT para $\sum C_j$.
3. Hoja `07_Paralelas_LPT_SPT` del [compendio](/corte-3-programacion-scheduling/00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md), para repasar los mismos ejemplos en Excel. Ojo con el error en $p_1$.
4. L18, pp. 17-27: precedencias y elegibilidad. Luego la hoja `08_Paralelas_Restric` del compendio, que da el resultado de LFM (p. 26); su solución LFJ omite un trabajo.
5. L18, pp. 28-39: *preemption*, $Rm||\sum C_j$ y el Excel con algoritmo genético.
6. [lns-maquinas-paralelas.md](/corte-3-programacion-scheduling/03-maquinas-paralelas/lns-maquinas-paralelas.md) como ejercicio para completar.

## Conceptos y fórmulas clave

Detalle en [L18-parallel-machine-scheduling.md](/corte-3-programacion-scheduling/03-maquinas-paralelas/L18-parallel-machine-scheduling.md).

- **Algoritmo de lista:** se ordenan los trabajos según la regla y cada uno va a la máquina con menor carga.
- **Garantía de LPT:**
  $$\frac{C_{max}(LPT)}{C_{max}(OPT)}\le\frac43-\frac1{3m}$$
- **Cota inferior** (óptimo con *preemption*):
  $$C^*_{max}=\max\left(p_{max},\ \frac{1}{m}\sum_{j=1}^{n}p_j\right)$$
- **Número de soluciones** de $Pm||C_{max}$: $\binom{n-1}{m-1}\dfrac{n!}{m!}$.
- **SPT** es óptima para $Pm||\sum C_j$. **WSPT** no lo es para $Pm||\sum w_jC_j$.
- **LFJ** es óptima para $Pm|p_j=1,M_j|C_{max}$ si los $M_j$ son anidados: para todo par, iguales, uno contenido en el otro o disjuntos.
- **$Pm|prmp|C_{max}$** como programa lineal: $\min C_{max}$ s.a. $\sum_i x_{ij}=p_j$, $\sum_i x_{ij}\le C_{max}$, $\sum_j x_{ij}\le C_{max}$.
- **$Rm||\sum C_j$** como MIP: $\min\sum_i\sum_j\sum_k k\,p_{ij}x_{ikj}$, con $k$ la posición contada desde el final; cada trabajo en una posición y cada posición con a lo sumo un trabajo.

## Ejercicios resueltos disponibles

| Ejemplo | Archivo | Resultado principal |
|---|---|---|
| $P3\|\|C_{max}$, 15 trabajos, LPT | L18, pp. 8-9 | $C_{max}=54$, $\sum C_j=582$ |
| $P3\|\|C_{max}$, $p_j=j$ ($j=1..10$) | L18, p. 10 (sin solución en la diapositiva) | Cálculo propio: LPT 19 (óptimo), SPT 22 |
| $P4\|\|C_{max}$, 9 trabajos | L18, pp. 11-14 | LPT 15, SPT 16, óptimo 12 |
| $P3\|\|\sum C_j$, 10 trabajos, SPT | L18, p. 16 | $\sum C_j=81$, $C_{max}=18$ |
| $Pm\|prec\|C_{max}$, LNS frente a CP | L18, p. 19; compendio, hoja 08 | $C_{max}=3$ con 2 máquinas (LNS puede dar 4 según los empates) |
| $P4\|p_j=1,M_j\|C_{max}$, LFJ | L18, pp. 22-25 | $C_{max}=3$ (no óptimo; los conjuntos no son anidados) |
| Mismo ejemplo con LFM | Compendio, hoja 08 | $C_{max}=2$ |
| $Rm\|\|\sum C_j$, secuencia 5-7-4 | L18, p. 38 | $\sum C_j=3p_5+2p_7+p_4$ |
| Máquinas no relacionadas en Excel (algoritmo genético) | L18, p. 39 | $C_{max}=39$, cota inferior 30 |
| 15 trabajos en 3 máquinas | [lns-maquinas-paralelas.md](/corte-3-programacion-scheduling/03-maquinas-paralelas/lns-maquinas-paralelas.md) (cálculo propio) | LPT $C_{max}=111$ (cota 107); SPT $\sum C_j=857$; WSPT $\sum w_jC_j=1618$ |

## Relación con otros temas y proyectos

- Base de una máquina (SPT, WSPT, EDD): [02-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/README.md).
- Cada estación de un *flexible flow shop* es un problema de máquinas paralelas: [04-flow-shop](/corte-3-programacion-scheduling/04-flow-shop/README.md) (L19, pp. 37-41).
- Compendio con las hojas 07 y 08: [00-compendio-metodos-scheduling](/corte-3-programacion-scheduling/00-compendio-metodos-scheduling/README.md).
- *Forward scheduling* con máquinas paralelas en MRP II: [corte 2 / 05-mrp-ii-y-capacidad](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/README.md).
- El reto 2 de la competencia (Monstruópolis) es $P3|r_j,prec|\sum w_jT_j$: [proyecto-competencia-scheduling](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/reto-2-monstruopolis.md).


---

<!-- fuente: corte-3-programacion-scheduling/03-maquinas-paralelas/L18-parallel-machine-scheduling.md -->
# L18-parallel-machine-scheduling

> **Archivo:** [`L18-parallel-machine-scheduling.pdf`](/corte-3-programacion-scheduling/03-maquinas-paralelas/L18-parallel-machine-scheduling.pdf) · **Corte 3** · 40 páginas  
> **Nombre original:** `CORTE 3/Lec 18 - Parallel Machine Scheduling.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** programación de máquinas paralelas ($Pm|\beta|\gamma$ y $Rm||\sum C_j$). Cubre algoritmos de lista, las reglas LPT, SPT, CP, LNS, LFJ y LFM, los modelos de programación matemática para *preemption* y máquinas no relacionadas, y una hoja de Excel con algoritmo genético.

### Ideas clave

- Las máquinas paralelas son un caso especial del *flexible flow shop* (una sola etapa). Hay dos decisiones: **asignar** cada trabajo a una máquina y **secuenciar** los trabajos de cada máquina (p. 2).
- Máquinas **idénticas** ($Pm$): el tiempo de un trabajo no depende de la máquina (p. ej. inyectoras). Máquinas **no idénticas**: cada máquina tiene su velocidad y $p_{ij}$ depende de la máquina (p. ej. impresoras) (p. 3).
- $Pm|\beta|\gamma$ extiende $1|\beta|\gamma$. Casi ninguna regla de despacho garantiza el óptimo. Las reglas se aplican con **algoritmos de lista**: se ordena la lista según la regla y cada trabajo va a la máquina con menor carga, es decir, la que termina antes (pp. 4-5).
- $Pm||C_{max}$ busca balancear la carga y equivale al problema de partición (p. 6). La heurística LPT (*Longest Processing Time first*) tiene una garantía de desempeño de $4/3-1/(3m)$ (p. 7).
- Los ejemplos de las pp. 8-14 muestran que LPT puede no ser óptima: con $P4$ y 9 trabajos, LPT da 15, SPT da 16 y el óptimo es 12.
- Para hallar el óptimo se puede enumerar, plantear un modelo de programación entera mixta o usar *Branch & Bound* (p. 15).
- SPT es **óptima** para $Pm||\sum C_j$ (pp. 16 y 33). WSPT **no** es óptima para $Pm||\sum w_jC_j$ (p. 34).
- $Pm|prec|C_{max}$ es fuertemente NP-hard. Se usan las reglas *Critical Path* (CP) y *Largest Number of Successors* (LNS) (pp. 17-19).
- $Pm|p_j=1,M_j|C_{max}$ (elegibilidad de máquinas): la regla LFJ (*Least Flexible Job first*) es óptima cuando los conjuntos $M_j$ son **anidados**. En el ejemplo de 8 trabajos no lo son y LFJ da $C_{max}=3$ (pp. 20-25). También existe la regla LFM (*Least Flexible Machine first*) (p. 26).
- Con *preemption* ($Pm|prmp|C_{max}$) el problema es un programa lineal. El óptimo es $\max(p_{max},\sum p_j/m)$ y se construye con el algoritmo de "partir el programa en $m$ partes" (wrap-around) o con LRPT (pp. 28-32).
- $Pm|prec|\sum C_j$ y $Pm|M_j|\sum C_j$ son NP-hard (p. 35).
- $Rm||\sum C_j$ (máquinas no relacionadas) se modela como asignación de trabajos a posiciones contadas de atrás hacia adelante. La posición $k$ pesa $k$ veces en la función objetivo (pp. 36-38).
- La p. 39 muestra un Excel para máquinas paralelas no relacionadas, resuelto con un algoritmo genético: $C_{max}=39$ y cota inferior 30.

### Fórmulas y métodos

**Algoritmo de lista (p. 4).** Se ordenan los trabajos según la regla (LPT, SPT…). Cada trabajo de la lista va a la máquina $i$ con menor carga acumulada $L_i$. Su inicio es $S_j=L_i$ y su fin $C_j=L_i+p_j$; luego $L_i\leftarrow C_j$.

**Garantía de LPT para $Pm||C_{max}$ (p. 7):**

$$\frac{C_{max}(LPT)}{C_{max}(OPT)}\le\frac{4}{3}-\frac{1}{3m}$$

donde $m$ es el número de máquinas, $C_{max}(LPT)$ el makespan de la regla LPT y $C_{max}(OPT)$ el óptimo. Para $m=3$ la cota es $11/9\approx1.222$; para $m=4$, $15/12=1.25$.

**Número de soluciones de $Pm||C_{max}$ (p. 15)**, con $n$ trabajos y $m$ máquinas idénticas:

$$\binom{n-1}{m-1}\frac{n!}{m!}$$

Interpretación (deducida): hay $n!$ órdenes de los trabajos y $\binom{n-1}{m-1}$ formas de cortar cada orden en $m$ listas no vacías. Se divide entre $m!$ porque las máquinas son idénticas.

**Cota del makespan (p. 30):**

$$C_{max}\ge\max\left(p_{max},\ \sum_{j=1}^{n}\frac{p_j}{m}\right)=C_{max}^*$$

donde $p_{max}=\max_j p_j$. Con *preemption* este valor es el óptimo. Sin *preemption* es una cota inferior.

**Modelo lineal para $Pm|prmp|C_{max}$ (pp. 28-29).** $x_{ij}\ge0$ es el tiempo que el trabajo $j$ pasa en la máquina $i$:

$$\min\ C_{max}$$
$$\text{s.a.}\quad \sum_{i=1}^{m}x_{ij}=p_j,\quad j=1,\dots,n$$
$$\sum_{i=1}^{m}x_{ij}\le C_{max},\quad j=1,\dots,n$$
$$\sum_{j=1}^{n}x_{ij}\le C_{max},\quad i=1,\dots,m$$

La primera restricción procesa todo el trabajo. La segunda evita que un trabajo esté en dos máquinas a la vez, así que su tiempo total cabe en $C_{max}$. La tercera dice que la carga de cada máquina cabe en $C_{max}$.

**Algoritmo para $Pm|prmp|C_{max}$ (p. 31):** (1) programar todos los trabajos en una sola máquina, en cualquier orden, y calcular $m\cdot C_{max}$ (con $C_{max}=C^*_{max}$ de la p. 30, según la lectura habitual del método); (2) partir ese programa en $m$ partes; (3) asignar cada parte a una máquina. Alternativa (p. 32): *Longest Remaining Processing Time first* (LRPT), cuya desventaja es que genera un número infinito de interrupciones.

**Modelo MIP para $Rm||\sum C_j$ (pp. 36-37).** $x_{ikj}=1$ si el trabajo $j$ va en la posición $k$ de la máquina $i$, contando **de atrás hacia adelante** ($k=1$ es la última posición). $p_{ij}$ es el tiempo del trabajo $j$ en la máquina $i$.

$$\min\ \sum_{i=1}^{m}\sum_{j=1}^{n}\sum_{k=1}^{n}k\,p_{ij}\,x_{ikj}$$
$$\text{s.a.}\quad \sum_{i=1}^{m}\sum_{k=1}^{n}x_{ikj}=1,\quad j=1,\dots,n$$
$$\sum_{j=1}^{n}x_{ikj}\le1,\quad i=1,\dots,m,\ k=1,\dots,n$$
$$x_{ikj}\in\{0,1\}$$

El trabajo en la posición $k$ desde el final se suma $k$ veces en $\sum C_j$. Por ejemplo, en la secuencia 5-7-4 se tiene $\sum C_j=3p_5+2p_7+p_4$ (p. 38).

**Reglas y cuándo usarlas:**

| Problema | Regla | ¿Óptima? | Página |
|---|---|---|---|
| $Pm\|\|C_{max}$ | LPT con algoritmo de lista | No; garantía $4/3-1/(3m)$ | 6-7 |
| $Pm\|\|\sum C_j$ | SPT con algoritmo de lista | Sí | 16, 33 |
| $Pm\|\|\sum w_jC_j$ | WSPT | No | 34 |
| $Pm\|prec\|C_{max}$ | CP (cadena más larga primero) o LNS (más sucesores primero) | No (fuertemente NP-hard) | 17-19 |
| $Pm\|p_j=1,M_j\|C_{max}$ | LFJ (trabajo con menos máquinas elegibles primero) | Sí, si los $M_j$ son anidados | 20-25 |
| $Pm\|p_j=1,M_j\|C_{max}$ | LFM (máquina que puede procesar menos trabajos pendientes primero) | No se indica | 26 |
| $Pm\|prmp\|C_{max}$ | LP, *wrap-around* o LRPT | Sí | 28-32 |
| $Pm\|prec\|\sum C_j$, $Pm\|M_j\|\sum C_j$ | CP, LFJ | NP-hard | 35 |
| $Rm\|\|\sum C_j$ | MIP de asignación por posiciones | Sí (modelo exacto) | 36-38 |

**Conjuntos anidados (p. 21):** para todo par de trabajos $j,k$ se cumple una de estas condiciones: $M_j=M_k$, $M_j\subset M_k$, $M_k\subset M_j$ o $M_j\cap M_k=\emptyset$.

### Ejemplos resueltos

| Páginas | Ejemplo | Resultado |
|---|---|---|
| 5 | Lista de 5 trabajos en 2 máquinas (gráfico sin escala) | Máquina 1: 1, 4; máquina 2: 2, 3, 5 |
| 8-9 | $P3\|\|C_{max}$ con 15 trabajos, LPT | $C_{max}=54$, $\sum C_j=582$ (cota inferior $159/3=53$, cálculo propio) |
| 10 | $P3\|\|C_{max}$, trabajos 1-10 con $p_j=j$ | La diapositiva no lo resuelve. Cálculo propio: LPT $C_{max}=19$ (óptimo, porque $\lceil55/3\rceil=19$); SPT $C_{max}=22$ |
| 11-14 | $P4\|\|C_{max}$, 9 trabajos (7,7,6,6,5,5,4,4,4) | LPT 15, SPT 16, óptimo 12. LPT/OPT $=15/12=4/3-1/12$: es el peor caso de la garantía |
| 16 | $P3\|\|\sum C_j$, 10 trabajos con SPT | $\sum C_j=81$, $C_{max}=18$ |
| 19 | $Pm\|prec\|C_{max}$, 6 trabajos con $p_j=1$, LNS frente a CP | La diapositiva solo hace la pregunta. Análisis propio con $m=2$: CP da $C_{max}=3$; LNS da 3 o 4 según cómo se rompan los empates |
| 22-25 | $P4\|p_j=1,M_j\|C_{max}$, 8 trabajos con LFJ | Máq. 1: 1-2; máq. 2: 4; máq. 3: 5-7-3; máq. 4: 6-8; $C_{max}=3$. El óptimo es 2 (cálculo propio) |
| 26 | El mismo ejemplo con LFM | La diapositiva no lo resuelve. El [compendio](/corte-3-programacion-scheduling/00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md) obtiene $C_{max}=2$ |
| 33 | $P2\|\|\sum C_j$ con $p=(1,1,3)$ | La diapositiva no lo resuelve. Cálculo propio con SPT: $\sum C_j=1+1+4=6$ |
| 34 | $P2\|\|\sum w_jC_j$ con $p=w=(1,1,3)$ | La diapositiva no lo resuelve. Cálculo propio: todos tienen $w_j/p_j=1$; si WSPT deja el trabajo 3 de último, $\sum w_jC_j=1+1+3\cdot4=14$. El óptimo pone el 3 primero en una máquina y los otros dos en la otra: $9+1+2=12$ |
| 38 | Secuencia 5-7-4 en $Rm\|\|\sum C_j$ | $\sum C_j=3p_5+2p_7+p_4$ |
| 39 | Excel de máquinas no relacionadas (5 máquinas, 10 trabajos) | $C_{max}=39$, cota inferior 30 |

### Páginas clave

- Definiciones y algoritmo de lista: pp. 2-5.
- $Pm||C_{max}$, LPT y su garantía: pp. 6-7; ejemplos LPT/SPT/óptimo: pp. 8-14.
- Enumeración y número de soluciones: p. 15.
- SPT para $Pm||\sum C_j$: pp. 16, 33; contraejemplo de WSPT: p. 34.
- Precedencias (CP, LNS): pp. 17-19.
- Elegibilidad de máquinas (LFJ, LFM, conjuntos anidados): pp. 20-27.
- *Preemption*: pp. 28-32.
- $Rm||\sum C_j$ (MIP): pp. 36-38; Excel con algoritmo genético: p. 39.

### Relación con otros archivos del repo

- [lns-maquinas-paralelas.md](/corte-3-programacion-scheduling/03-maquinas-paralelas/lns-maquinas-paralelas.md): plantilla de Excel para asignar 15 trabajos a 3 máquinas paralelas (incompleta).
- [metodos-programacion-produccion-corte3.md](/corte-3-programacion-scheduling/00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md): hojas `07_Paralelas_LPT_SPT` (ejemplos de las pp. 8-14) y `08_Paralelas_Restric` (LNS/CP de la p. 19 y LFJ/LFM de las pp. 22-26).
- Fundamentos de una máquina (SPT, WSPT, EDD, cadenas): [L17](/corte-3-programacion-scheduling/02-una-maquina/L17-single-machine-scheduling.md).
- Notación $\alpha|\beta|\gamma$: [L16](/corte-3-programacion-scheduling/01-introduccion-scheduling/L16-intro-scheduling.md).
- El *flexible flow shop* generaliza las máquinas paralelas a varias etapas: [L19](/corte-3-programacion-scheduling/04-flow-shop/L19-flow-shop-scheduling.md), pp. 37-41.
- El reto 2 de la competencia es un problema de 3 máquinas paralelas con liberaciones y precedencias: [proyecto-competencia-scheduling](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/).


---

<!-- fuente: corte-3-programacion-scheduling/04-flow-shop/README.md -->
# Flow shop y flexible flow shop (Corte 3)

## Qué cubre

Programación de talleres en serie: todos los trabajos pasan por las mismas máquinas en el mismo orden ($Fm||C_{max}$). Incluye el cálculo de tiempos de terminación, la regla de Johnson (óptima para 2 máquinas) y su extensión a 3, el modelo MIP del *flow shop* permutacional y su código en GAMS, las heurísticas CDS y NEH, el *flexible flow shop* con reglas de prioridad y una introducción a los algoritmos genéticos.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [L19-flow-shop-scheduling.md](/corte-3-programacion-scheduling/04-flow-shop/L19-flow-shop-scheduling.md) (gemelo del PDF) | Presentación "Lec 19 - flow shop scheduling", 56 diapositivas: Johnson, MIP, código GAMS completo, CDS, NEH, *flexible flow shop* y algoritmos genéticos, con los Gantt en tablas | **Sí (1.º)** |
| [flowshop-scheduling.md](/corte-3-programacion-scheduling/04-flow-shop/flowshop-scheduling.md) (gemelo del .xlsx) | Excel de clase con 4 hojas: `Regla de Johnson` (2 y 3 máquinas), `Campbell ` (CDS del ejercicio de L19, solo la iteración 1 correcta), `CDS` y `NEH` (caso de 5 trabajos y 5 máquinas) | 2.º |
| [flowshop-scheduling-datos/CDS.csv](/corte-3-programacion-scheduling/04-flow-shop/flowshop-scheduling-datos/CDS.csv) | Volcado CSV completo de la hoja `CDS` | Solo como referencia |

## Orden de estudio sugerido

1. L19, pp. 3-9: definición, recursión de $C_{ij}$ y Johnson para 2 máquinas.
2. Hoja `Regla de Johnson` de [flowshop-scheduling.md](/corte-3-programacion-scheduling/04-flow-shop/flowshop-scheduling.md): secuencia al azar (110) frente a Johnson (92) y el caso de 3 máquinas (115).
3. L19, pp. 10-14: extensión de Johnson a 3 máquinas.
4. L19, pp. 15-24: modelo MIP y GAMS.
5. L19, pp. 25-29 (CDS) y pp. 30-36 (NEH). Luego las hojas `CDS` y `NEH` del Excel y las hojas 10-11 del [compendio](/corte-3-programacion-scheduling/00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md).
6. L19, pp. 37-55: *flexible flow shop* y algoritmos genéticos.

## Conceptos y fórmulas clave

Detalle en [L19-flow-shop-scheduling.md](/corte-3-programacion-scheduling/04-flow-shop/L19-flow-shop-scheduling.md).

- **Recursión:**
  $$C_{i,j_k}=\max\left(C_{i-1,j_k},\,C_{i,j_{k-1}}\right)+p_{i,j_k}$$
  y $C_{max}=C_{m,j_n}$.
- **Johnson ($F2||C_{max}$, óptima):** grupo 1 ($p_{1j}<p_{2j}$) en SPT de $p_{1j}$, luego grupo 2 ($p_{1j}>p_{2j}$) en LPT de $p_{2j}$.
- **Extensión a $F3$** si $\max_j p_{2j}\le\max(\min_j p_{1j},\min_j p_{3j})$: Johnson con $p'_{1j}=p_{1j}+p_{2j}$ y $p'_{2j}=p_{2j}+p_{3j}$.
- **MIP $Fm|prmu|C_{max}$:** variables $x_{jk}$ (trabajo $j$ en la posición $k$), $I_{ik}$ (ocio) y $W_{ik}$ (espera). Se minimiza $\sum_{i<m}p_{i(1)}+\sum_{k<n}I_{mk}$, sujeto a la asignación y a
  $$I_{ik}+p_{i(k+1)}+W_{i,k+1}=W_{ik}+p_{i+1(k)}+I_{i+1,k}$$
- **CDS:** para $k=1..m-1$, $p'^{(k)}_{1j}=\sum_{i=1}^{k}p_{ij}$ y $p'^{(k)}_{2j}=\sum_{i=m-k+1}^{m}p_{ij}$; Johnson en cada subproblema y se elige el mejor $C_{max}$ real.
- **NEH:** ordenar por $\sum_i p_{ij}$ decreciente e insertar cada trabajo en la mejor posición. Evalúa $\frac{n(n+1)}{2}-1$ secuencias.
- **Flexible flow shop:** lista con la regla elegida en la estación 1 y FIFO en las demás.
- **Algoritmo genético:** población, *fitness* (makespan), cruce de un punto con reparación de genes repetidos, mutación por intercambio y selección elitista.

## Ejercicios resueltos disponibles

| Ejemplo | Archivo | Resultado principal |
|---|---|---|
| $F2$, 5 trabajos (A-E) | L19, pp. 7-9 | C-A-D-E-B; $C_{max}=20.5$ (cálculo propio) |
| $F3$, 5 trabajos, máquina 2 dominada | L19, pp. 13-14 | (5, 4, 1, 2, 3), $C_{max}=49$ |
| GAMS, 6 ítems × 3 máquinas | L19, pp. 23-24 | Solo el código (sin resultado) |
| CDS, 5 trabajos × 4 máquinas | L19, pp. 28-29 | 88 / 85 / 85; mejores 5-2-3-1-4 y 5-1-2-3-4 ($C_{max}=85$) |
| NEH con los mismos datos | L19, pp. 32-36 | J1-J5-J2-J3-J4, $C_{max}=80$ (óptimo por enumeración) |
| Algoritmo genético, 7 genes | L19, pp. 48-53 | *Fitness* 45, 50, 75; hijo mutado 46 |
| $F2$, 6 trabajos (A-F): azar frente a Johnson | flowshop-scheduling, `Regla de Johnson` | 110 frente a 92 |
| $F3$, 6 trabajos | flowshop-scheduling, `Regla de Johnson` | C-A-B-E-D-F, $C_{max}=115$ (óptimo) |
| CDS del ejercicio de L19 | flowshop-scheduling, `Campbell ` | Iteración 1 = 88; iteraciones 2-3 con errores (correcto: 85) |
| CDS, 5 trabajos × 5 máquinas | flowshop-scheduling, `CDS` | 159 / 159 / 159 / 168 → 159 |
| NEH, 5 trabajos × 5 máquinas | flowshop-scheduling, `NEH` | 2-3-5-4-1, $C_{max}=159$ (óptimo) |

## Relación con otros temas y proyectos

- Máquinas paralelas, que forman cada estación del *flexible flow shop*: [03-maquinas-paralelas](/corte-3-programacion-scheduling/03-maquinas-paralelas/README.md).
- Job shop, la generalización a rutas distintas por trabajo: [05-job-shop](/corte-3-programacion-scheduling/05-job-shop/README.md).
- Compendio, hojas 09-11 (Johnson, CDS, NEH): [00-compendio-metodos-scheduling](/corte-3-programacion-scheduling/00-compendio-metodos-scheduling/README.md).
- El reto 1 de la competencia (Willy Wonka) es un flow shop de permutación $F3$ con alistamientos y restricción de secuencia: [proyecto-competencia-scheduling](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/reto-1-willy-wonka.md).
- Otros modelos en GAMS del curso: [modelo-flujo-gams](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/).


---

<!-- fuente: corte-3-programacion-scheduling/04-flow-shop/L19-flow-shop-scheduling.md -->
# L19-flow-shop-scheduling

> **Archivo:** [`L19-flow-shop-scheduling.pdf`](/corte-3-programacion-scheduling/04-flow-shop/L19-flow-shop-scheduling.pdf) · **Corte 3** · 56 páginas  
> **Nombre original:** `CORTE 3/Lec 19 - flow shop scheduling.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** programación en *flow shop* ($Fm||C_{max}$). Cubre el cálculo de tiempos de terminación, la regla de Johnson para 2 máquinas y su extensión a 3, el modelo MIP del *flow shop* permutacional con su implementación en GAMS, las heurísticas CDS y NEH, el *flexible flow shop* con reglas de prioridad y una introducción a los algoritmos genéticos.

### Ideas clave

- Un *flow shop* es un taller donde todos los trabajos pasan por las mismas máquinas en el mismo orden: máquinas en serie con *buffer* infinito entre ellas (p. 3).
- En $Fm||C_{max}$ se supone que no hay bloqueo. En general el orden de los trabajos podría cambiar de una máquina a otra, pero en $F2||C_{max}$ y $F3||C_{max}$ existen óptimos que mantienen la misma secuencia: el *flow shop* permutacional (p. 4).
- Dada una secuencia, los tiempos de terminación se calculan con una recursión: cada operación empieza cuando terminan el trabajo en la máquina anterior y el trabajo previo en la misma máquina (p. 5).
- La **regla de Johnson** es óptima para $F2||C_{max}$ (pp. 6-9).
- Con 3 máquinas Johnson sirve solo si la máquina intermedia está **dominada**. Entonces se suman tiempos para formar dos máquinas ficticias (pp. 10-14).
- Para el caso general hay tres caminos: programación entera mixta, heurísticas y metaheurísticas (p. 15).
- El modelo MIP para $Fm|prmu|C_{max}$ usa variables de posición $x_{jk}$, tiempos muertos $I_{ik}$ y esperas $W_{ik}$. Minimizar el makespan equivale a minimizar el tiempo muerto de la última máquina (pp. 16-21). Se implementa en GAMS con un ejemplo de 6 ítems y 3 máquinas (pp. 22-24).
- La heurística **CDS** (Campbell, Dudek y Smith, 1970) forma $m-1$ subproblemas de dos máquinas ficticias, aplica Johnson a cada uno y se queda con la mejor secuencia. Halló el óptimo en el 55 % de 1 580 problemas (Dannenbring, 1977) (pp. 25-29).
- La heurística **NEH** (Nawaz, Enscore y Ham, 1983) es de inserción y se considera de las mejores para $Fm||C_{max}$ (pp. 30-36).
- En el *flexible flow shop* ($FF_c$) cada estación tiene máquinas en paralelo. Es NP-hard porque combina asignación y secuenciación. Se resuelve con reglas de prioridad en la primera estación y FIFO en las demás (pp. 37-41).
- Los **algoritmos genéticos** trabajan con una población de cromosomas (secuencias) y la mejoran con *fitness*, cruce, mutación y selección (pp. 42-55).

### Fórmulas y métodos

**Tiempos de terminación en un flow shop (p. 5).** Para la secuencia $j_1,j_2,\dots,j_n$ en $m$ máquinas, $C_{i,j_k}$ es el fin del trabajo en la posición $k$ en la máquina $i$ y $p_{i,j}$ el tiempo del trabajo $j$ en la máquina $i$:

$$C_{i,j_1}=\sum_{l=1}^{i}p_{l,j_1},\qquad i=1,\dots,m$$
$$C_{1,j_k}=\sum_{l=1}^{k}p_{1,j_l},\qquad k=1,\dots,n$$
$$C_{i,j_k}=\max\left(C_{i-1,j_k},\,C_{i,j_{k-1}}\right)+p_{i,j_k},\qquad k=2,\dots,n;\ i=2,\dots,m$$

El makespan es $C_{max}=C_{m,j_n}$.

**Regla de Johnson para $F2||C_{max}$ (p. 6).** Es óptima.
1. Grupo 1: trabajos con $p_{1j}<p_{2j}$. Grupo 2: trabajos con $p_{1j}>p_{2j}$. Si $p_{1j}=p_{2j}$, el trabajo va a cualquiera de los dos grupos.
2. Primero el grupo 1 en orden SPT de $p_{1j}$ (creciente); luego el grupo 2 en orden LPT de $p_{2j}$ (decreciente).
3. Los empates se rompen arbitrariamente.

**Extensión a $F3||C_{max}$ (pp. 10-12).** Se aplica cuando la máquina 2 está dominada:

$$\max_j\{p_{2,j}\}\le\max\left\{\min_{\forall j}\{p_{1,j}\},\ \min_{\forall j}\{p_{3,j}\}\right\}$$

Si se cumple, se resuelve un $F2||C_{max}$ equivalente con los tiempos

$$p'_{1,j}=p_{1,j}+p_{2,j},\qquad p'_{2,j}=p_{2,j}+p_{3,j}$$

**Modelo MIP para $Fm|prmu|C_{max}$ (pp. 16-21).**
- $x_{jk}=1$ si el trabajo $j$ ocupa la posición $k$ de la secuencia.
- $I_{ik}$: tiempo muerto de la máquina $i$ entre los trabajos de las posiciones $k$ y $k+1$.
- $W_{ik}$: tiempo de espera del trabajo de la posición $k$ entre las máquinas $i$ e $i+1$.
- $\Delta_{ik}$: tiempo entre el fin del trabajo $k$ en la máquina $i$ y el inicio del trabajo $k+1$ en la máquina $i+1$.
- $p_{i(k)}$: tiempo en la máquina $i$ del trabajo en la posición $k$.

$$\Delta_{ik}=I_{ik}+p_{i(k+1)}+W_{i,k+1}=W_{ik}+p_{i+1(k)}+I_{i+1,k}$$
$$p_{i(k)}=\sum_{j=1}^{n}x_{jk}\,p_{ij}$$

$$\min\ \sum_{i=1}^{m-1}p_{i(1)}+\sum_{j=1}^{n-1}I_{mj}$$

La función objetivo es el tiempo que la última máquina espera antes del primer trabajo más sus tiempos muertos entre trabajos. Sumándole la carga fija $\sum_j p_{mj}$ se obtiene $C_{max}$. Restricciones:

$$\sum_{j=1}^{n}x_{jk}=1\ \ \forall k,\qquad \sum_{k=1}^{n}x_{jk}=1\ \ \forall j$$
$$I_{ik}+\sum_{j=1}^{n}x_{j,k+1}\,p_{ij}+W_{i,k+1}-W_{ik}-\sum_{j=1}^{n}x_{jk}\,p_{i+1,j}-I_{i+1,k}=0\quad\forall k=1,\dots,n-1;\ i=1,\dots,m-1$$
$$W_{i1}=0\ \ \forall i=1,\dots,m-1,\qquad I_{1k}=0\ \ \forall k=1,\dots,n-1$$

**CDS (pp. 26-27).** Para cada $k\in\{1,\dots,m-1\}$ se forman dos máquinas ficticias y se aplica Johnson:

$$p'^{(k)}_{1,j}=\sum_{i=1}^{k}p_{i,j},\qquad p'^{(k)}_{2,j}=\sum_{i=m-k+1}^{m}p_{i,j}$$

Se evalúa el $C_{max}$ real (con las $m$ máquinas) de cada una de las $m-1$ secuencias y se elige la mejor.

**NEH (p. 31).**
1. Ordenar los trabajos de forma no creciente según $\sum_i p_{ij}$.
2. Programar los dos primeros en el orden que minimice el makespan parcial.
3. Para $k=3,\dots,n$, insertar el $k$-ésimo trabajo en la posición, entre las $k$ posibles, que minimice el makespan parcial.

Número total de secuencias evaluadas: $\frac{n(n+1)}{2}-1$.

**Flexible flow shop con reglas de prioridad (p. 40).** Se ordenan los trabajos con una regla y se aplica un algoritmo de lista en la primera estación. En las demás estaciones se usa el algoritmo de lista con FIFO. No garantiza el óptimo.

**Algoritmo genético (p. 54):**

```
Repetir
    para cada individuo i evaluar y calcular fitness f(i)
    Crear mating pool de tamaño N basado en los valores de fitness f(i)
    para i = 1 hasta (N/2)
        quitar pares de individuos {j,k} del mating pool
        recombinar usando los individuos j y k
        aplicar mutación
Hasta 'condición de parada'
```

### Ejemplos resueltos

| Páginas | Ejemplo | Resultado |
|---|---|---|
| 7-9 | $F2\|\|C_{max}$ con 5 trabajos (A-E) en los centros A y B | Grupo 1: A, C; grupo 2: B, D, E. Secuencia **C-A-D-E-B**. $C_{max}=20.5$ (cálculo propio; la diapositiva no lo da) |
| 13-14 | $F3\|\|C_{max}$ con 5 trabajos y máquina 2 dominada | Secuencia **(5, 4, 1, 2, 3)**; el Gantt termina en 49 |
| 23-24 | GAMS: 6 ítems en 3 máquinas (bending, soldering, assembly) | Solo el código; no hay resultado |
| 28-29 | CDS, 5 trabajos y 4 máquinas | $k=1$: 1-2-5-4-3, $C_{max}=88$; $k=2$: 5-2-3-1-4, $C_{max}=85$; $k=3$: 5-1-2-3-4, $C_{max}=85$. Mejores: 5-2-3-1-4 y 5-1-2-3-4 con **85** |
| 32-36 | NEH con los mismos datos | Orden J2-J3-J4-J5-J1. Resultado **J1-J5-J2-J3-J4, $C_{max}=80$**. Por enumeración de las 120 permutaciones, 80 es el óptimo (cálculo propio) |
| 41 | *Flexible flow shop* de 2 estaciones con 2 máquinas cada una | Gantt sin escala (ver la página) |
| 48-53 | Algoritmo genético con cromosomas de 7 genes | *Fitness* 45, 50 y 75; el hijo mutado tiene 46. La nueva generación conserva los de 45, 50 y 46 |

### Páginas clave

- Definición y cálculo de tiempos: pp. 3-5.
- Johnson para 2 máquinas: pp. 6-9; extensión a 3 máquinas: pp. 10-14.
- Modelo MIP: pp. 16-21; GAMS: pp. 22-24.
- CDS: pp. 25-29. NEH: pp. 30-36.
- *Flexible flow shop*: pp. 37-41.
- Algoritmos genéticos: pp. 42-55.

### Relación con otros archivos del repo

- [flowshop-scheduling.md](/corte-3-programacion-scheduling/04-flow-shop/flowshop-scheduling.md): Excel de clase con Johnson para 2 y 3 máquinas, la hoja `Campbell ` (el ejercicio CDS de la p. 28, incompleto), y CDS y NEH con otro caso de 5 trabajos y 5 máquinas.
- [metodos-programacion-produccion-corte3.md](/corte-3-programacion-scheduling/00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md): hojas `09_FlowShop_Johnson`, `10_FlowShop_CDS` y `11_FlowShop_NEH`.
- Las máquinas paralelas, que son cada estación de un *flexible flow shop*: [L18](/corte-3-programacion-scheduling/03-maquinas-paralelas/L18-parallel-machine-scheduling.md).
- Job shop y flexible job shop: [05-job-shop](/corte-3-programacion-scheduling/05-job-shop/job-shop-y-flexible-job-shop.md).
- Modelos de GAMS de otro tema (planeación agregada): [modelo-flujo-gams](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/).

### Observaciones sobre el material

- p. 9: la línea "SPT: C -> A -> D -> E -> B" es la secuencia completa de Johnson (SPT del grupo 1 más LPT del grupo 2), no solo la parte SPT.
- p. 11 y p. 12 son idénticas; p. 45 y p. 46 también.
- p. 14: el eje del Gantt llega a 48, pero el trabajo 3 termina en la máquina 3 en $t=49$ (cálculo con los datos de la tabla).
- p. 21: la función objetivo escribe $\sum_{i=1}^{m-1}\sum_{j=1}^{n}x_{jk}p_{ij}$. Por la p. 18 debería ser $x_{j1}$ (trabajo de la primera posición). La última restricción escribe $x_{jk}p_{ij}$ donde la p. 20 tiene $x_{j,k+1}p_{ij}$.
- p. 24 (GAMS): los nombres de las ecuaciones están cruzados con su descripción. `onmachrel` se describe como la relación entre máquinas $m$ y $m+1$, pero su ecuación relaciona las posiciones $k$ y $k+1$ en la misma máquina; con `permachrel` pasa lo contrario. La variable `totwait` es en realidad el fin del último trabajo en la última máquina, es decir, el makespan. Además, las definiciones `onmachrel(m,k+1)..` y `permachrel(m+1,k)..` usan desplazamientos en el dominio de la ecuación; no hay archivo `.lst` para comprobar si compila tal cual.
- p. 26: "Capmbell" es una errata de Campbell.
- pp. 29 y 35: hay empates que la diapositiva rompe sin decirlo. En CDS $k=2$, los trabajos 1 y 4 tienen $p'_2=8$: con el orden 5-2-3-1-4 sale 85, con 5-2-3-4-1 saldría 88 (cálculo propio). En NEH, J2-J4-J3 y J2-J3-J4 empatan en 68 y se escoge J2-J3-J4.
- p. 50: el segundo cromosoma aparece como 5-1-3-4-**5**-2-7 (5 repetido, falta el 6). En la p. 49 es 5-1-3-4-6-2-7. El error se repite en la p. 53.
- pp. 52-53: el hijo mutado es 5-6-3-4-2-1-7 en la p. 52 y 5-7-3-4-2-1-7 en la p. 53 (7 repetido, falta el 6).


---

<!-- fuente: corte-3-programacion-scheduling/05-job-shop/README.md -->
# Job shop y flexible job shop (Corte 3)

## Qué cubre

Programación de talleres en los que cada trabajo sigue su propia ruta por las máquinas, con el objetivo de minimizar el makespan ($J_m \,\|\, C_{max}$). Incluye:

- la formulación disyuntiva y su grafo, donde el makespan es la ruta crítica;
- la implementación en GAMS con LogMIP;
- la heurística del cuello de botella móvil (*shifting bottleneck*), con un ejemplo de 3 trabajos × 4 máquinas resuelto paso a paso;
- el software LEKIN.

El título y la agenda anuncian también *flexible job shop* e *iterated local search*, pero la presentación no tiene diapositivas sobre esos dos temas.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [job-shop-y-flexible-job-shop.md](/corte-3-programacion-scheduling/05-job-shop/job-shop-y-flexible-job-shop.md) | Gemelo de la presentación de clase (33 págs.): definición de job shop, modelo disyuntivo, grafo disyuntivo, código GAMS/LogMIP completo, cuello de botella móvil paso a paso con Gantt final, LEKIN y Rubén Ruiz | Sí (es el único archivo) |

## Orden de estudio sugerido

1. Repasar la notación $J_m$ y $FJ_c$ en [L16, págs. 21–22](/corte-3-programacion-scheduling/01-introduccion-scheduling/L16-intro-scheduling.md) y el problema $1\mid r_j\mid L_{max}$ en [L17](/corte-3-programacion-scheduling/02-una-maquina/L17-single-machine-scheduling.md).
2. Págs. 3–8 del [gemelo](/corte-3-programacion-scheduling/05-job-shop/job-shop-y-flexible-job-shop.md): definición, modelo disyuntivo y grafo. Intentar escribir las restricciones del ejemplo de la pág. 7 antes de mirar la respuesta deducida.
3. Págs. 9–10: código GAMS y su explicación (con la observación de que el modelo es *no-wait* por etapas).
4. Págs. 11–13: algoritmo del cuello de botella móvil.
5. Págs. 14–30: ejemplo completo. Conviene rehacer a mano las tablas de $r_j$, $d_j$, $C_j$ y $L_j$.
6. Pág. 31: probar LEKIN para comparar heurísticas.

## Conceptos y fórmulas clave

Notación: $(i,j)$ = operación del trabajo $j$ en la máquina $i$; $p_{ij}$ = tiempo de proceso; $y_{ij}$ = inicio; $A$ = arcos de ruta; $B$ = pares de operaciones de la misma máquina; $N$ = operaciones. Detalle en el [gemelo, págs. 5, 12 y 13](/corte-3-programacion-scheduling/05-job-shop/job-shop-y-flexible-job-shop.md).

**Modelo disyuntivo**

$$\min C_{max}\quad \text{s.a.}\quad y_{kj}-y_{ij}\ge p_{ij}\ \ \forall (i,j)\to(k,j)\in A;\qquad C_{max}-y_{ij}\ge p_{ij}\ \ \forall (i,j)\in N$$
$$y_{ij}-y_{il}\ge p_{il}\ \ \text{ó}\ \ y_{il}-y_{ij}\ge p_{ij}\ \ \forall (i,l),(i,j)\in B;\qquad y_{ij}\ge 0$$

**Grafo disyuntivo.** Hay que orientar los arcos de $B$ sin crear ciclos. Entonces $C_{max}$ es la ruta más larga de $U$ a $V$.

**Cuello de botella móvil.** Para cada máquina no secuenciada se resuelve $1\mid r_j\mid L_{max}$ con

$$r_{ij}=\text{ruta más larga } U\to(i,j),\qquad d_{ij}=C_{max}(M_o)-\big[\text{ruta más larga }(i,j)\to V - p_{ij}\big],\qquad L_j=C_j-d_j$$

Se fija la máquina $k$ con mayor $L_{max}$, se actualiza $C_{max}(M_o\cup\{k\})=C_{max}(M_o)+L_{max}(k)$ y se re-optimizan las máquinas ya fijadas.

## Ejercicios resueltos disponibles

| Ejemplo | Dónde | Resultado principal |
|---|---|---|
| Restricciones MIP y grafo del job shop 3 trabajos × 4 máquinas | [gemelo, págs. 7–8](/corte-3-programacion-scheduling/05-job-shop/job-shop-y-flexible-job-shop.md) | 7 restricciones de ruta y 8 disyunciones (respuesta deducida). Óptimo $C_{max}^*=28$ (cálculo propio con PuLP). |
| Modelo GAMS LogMIP (ejemplo 4 del manual de LogMIP), 7 trabajos × 5 etapas | [gemelo, págs. 9–10](/corte-3-programacion-scheduling/05-job-shop/job-shop-y-flexible-job-shop.md) | Código completo transcrito. El PDF no muestra el resultado; reproducido en PuLP da $MS^*=32$. |
| Cuello de botella móvil, 3 trabajos × 4 máquinas | [gemelo, págs. 14–30](/corte-3-programacion-scheduling/05-job-shop/job-shop-y-flexible-job-shop.md) | $C_{max}$: 22 → 27 (fija M1: 1-2-3, $L_{max}=5$) → 28 (fija M2: 2-1-3, $L_{max}=1$) → 28 (M3 y M4 con $L_{max}=0$). Gantt final: M3 2-1 y M4 2-3. $C_{max}=28$, que es óptimo. |
| Comparación en LEKIN, instancia MT10 | [gemelo, pág. 31](/corte-3-programacion-scheduling/05-job-shop/job-shop-y-flexible-job-shop.md) | $C_{max}$: Local Search 1107, SB Routine 1110, Shifting Bottleneck 1113, WSPT 1356. |

## Relación con otros temas y proyectos

- [01-introduccion-scheduling](/corte-3-programacion-scheduling/01-introduccion-scheduling/): notación $\alpha\mid\beta\mid\gamma$ y definiciones de $J_m$, $FJ_c$ y recirculación.
- [02-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/): EDD y $1\mid r_j\mid L_{max}$, el subproblema del cuello de botella móvil.
- [03-maquinas-paralelas](/corte-3-programacion-scheduling/03-maquinas-paralelas/): las máquinas paralelas de cada etapa son las que convierten un job shop en *flexible* job shop ($FJ_c$).
- [04-flow-shop](/corte-3-programacion-scheduling/04-flow-shop/): caso particular en que todos los trabajos siguen la misma ruta.
- [00-compendio-metodos-scheduling](/corte-3-programacion-scheduling/00-compendio-metodos-scheduling/): resumen de los métodos del Corte 3.
- [proyecto-competencia-scheduling](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/): sus retos son un flow shop de permutación y máquinas paralelas con $r_j$ y precedencias, no job shops; comparten las ideas de búsqueda local y la referencia a Ruiz y Stützle.
- [Modelo de flujo en GAMS, Corte 2](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/): otro modelo del curso en GAMS.


---

<!-- fuente: corte-3-programacion-scheduling/05-job-shop/job-shop-y-flexible-job-shop.md -->
# job-shop-y-flexible-job-shop

> **Archivo:** [`job-shop-y-flexible-job-shop.pdf`](/corte-3-programacion-scheduling/05-job-shop/job-shop-y-flexible-job-shop.pdf) · **Corte 3** · 33 páginas  
> **Nombre original:** `CORTE 3/job shop.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** programación de talleres tipo *job shop* ($J_m \,\|\, C_{max}$): formulación disyuntiva, grafo disyuntivo, implementación en GAMS/LogMIP y heurística del cuello de botella móvil (*shifting bottleneck*).

**Ideas clave**

- En un job shop cada trabajo tiene **su propia ruta** por las máquinas; hay *buffer* infinito entre máquinas y no hay recirculación. En el curso se minimiza el makespan $C_{max}$ (pág. 3).
- El problema se modela como **programación disyuntiva**: para cada par de operaciones de la misma máquina hay que decidir cuál va primero (pág. 5).
- En el **grafo disyuntivo** $G=\{N,A,B\}$, los nodos son las operaciones, los arcos continuos $A$ son las rutas de los trabajos y los arcos punteados $B$ unen operaciones de la misma máquina. Fijar el sentido de todos los arcos punteados sin crear ciclos equivale a fijar las secuencias de las máquinas, y el makespan es la **ruta más larga** de $U$ a $V$ (ruta crítica) (págs. 6 y 8).
- La implementación en GAMS (ejemplo 4 del manual de LogMIP) escribe las disyunciones con LogMIP y las resuelve como modelo EMP, reformuladas con big-M (págs. 9–10).
- La heurística del **cuello de botella móvil** descompone el job shop en subproblemas de una máquina $1\mid r_j\mid L_{max}$. En cada iteración secuencia la máquina con mayor $L_{max}$ (el cuello de botella), la fija en el grafo y re-optimiza las máquinas ya fijadas (págs. 11–13).
- El ejemplo de 3 trabajos × 4 máquinas pasa de $C_{max}=22$ (cota sin conflictos) a 27, luego a 28 y termina en 28, con Gantt final en la pág. 30.
- Herramienta recomendada: **LEKIN** (NYU Stern), que compara reglas y heurísticas en instancias de job shop como MT10 (pág. 31). Investigador destacado: Rubén Ruiz (flow shop, *iterated greedy*) (pág. 32).
- **El PDF no desarrolla «Flexible Job shop» ni «Iterated Local Search»**, aunque aparecen en el título y en la agenda (pág. 2). La definición de job shop flexible ($FJ_c$) está en [L16, pág. 22](/corte-3-programacion-scheduling/01-introduccion-scheduling/L16-intro-scheduling.md).

**Fórmulas y métodos**

*Notación:* $(i,j)$ = operación del trabajo $j$ en la máquina $i$; $p_{ij}$ = tiempo de proceso; $y_{ij}$ = inicio; $N$ = operaciones; $A$ = pares consecutivos de la ruta de un trabajo; $B$ = pares de operaciones de trabajos distintos en la misma máquina.

1. *Modelo disyuntivo* (pág. 5). Se usa para resolver exactamente instancias pequeñas con un solver MIP:

$$\min C_{max}$$
$$y_{kj}-y_{ij}\ge p_{ij}\quad \forall (i,j)\to(k,j)\in A \qquad \text{(ruta)}$$
$$C_{max}-y_{ij}\ge p_{ij}\quad \forall (i,j)\in N \qquad \text{(makespan)}$$
$$y_{ij}-y_{il}\ge p_{il}\ \ \text{ó}\ \ y_{il}-y_{ij}\ge p_{ij}\quad \forall (i,l),(i,j)\in B \qquad \text{(no traslape)}$$
$$y_{ij}\ge 0$$

   Linealización big-M de cada «ó» (complemento, no viene en las diapositivas): con $x\in\{0,1\}$, $y_{il}-y_{ij}\ge p_{ij}-M(1-x)$ y $y_{ij}-y_{il}\ge p_{il}-Mx$.

2. *Modelo GAMS/LogMIP* (págs. 9–10). $T_i$ = inicio del trabajo $i$, $\tau_{ij}$ = tiempo en la etapa $j$, $Y_{ikj}$ = 1 si $i$ precede a $k$ en la etapa $j$:

$$\min MS \quad\text{s.a.}\quad MS\ge T_i+\sum_m\tau_{im}\ \ \forall i$$
$$\Big[Y_{ikj}: T_i+\sum_{m\le j}\tau_{im}\le T_k+\sum_{m<j}\tau_{km}\Big]\ \vee\ \Big[\neg Y_{ikj}: T_k+\sum_{m\le j}\tau_{km}\le T_i+\sum_{m<j}\tau_{im}\Big]\quad \forall (i,k,j)\in L$$

   Con $M=\sum_{i,j}\tau_{ij}=92$. Supone recorrido por etapas en orden y sin esperas (*no-wait*).

3. *Cuello de botella móvil* (págs. 11–13). Es una heurística para job shops medianos y grandes, donde el MIP es muy lento. $M_o$ = máquinas ya secuenciadas. En cada subproblema $1\mid r_j\mid L_{max}$:

$$r_{ij}=\text{ruta más larga de }U\text{ a }(i,j),\qquad d_{ij}=C_{max}(M_o)-\big[\text{ruta más larga de }(i,j)\text{ a }V-p_{ij}\big]$$
$$L_j=C_j-d_j,\qquad L_{max}(i)=\min_{\text{secuencias}}\max_j L_j,\qquad k=\arg\max_i L_{max}(i)$$
$$C_{max}(M_o\cup\{k\})=C_{max}(M_o)+L_{max}(k)$$

   Pasos: (1) $M_o=\varnothing$, makespan = ruta más larga solo con arcos de ruta; (2) resolver $1\mid r_j\mid L_{max}$ para cada máquina no secuenciada; (3) fijar la de mayor $L_{max}$, agregar sus arcos y meterla en $M_o$; (4) re-optimizar cada máquina de $M_o$ distinta de $k$; (5) parar cuando todas estén secuenciadas.

**Ejemplos resueltos**

| Ejemplo | Páginas | Resultado |
|---|---|---|
| Grafo y MIP del job shop 3 trabajos × 4 máquinas | 7–8 | Grafo con 8 pares disyuntivos (3 en M1, 3 en M2, 1 en M3, 1 en M4). En el .md se escriben todas las restricciones (deducidas); el MIP resuelto da $C_{max}^*=28$ (cálculo propio). |
| Modelo GAMS LogMIP, 7 trabajos (A–G) × 5 etapas | 9–10 | Las diapositivas no muestran el resultado. Reproducido en PuLP/CBC: $MS^*=32$ (cálculo propio). |
| Cuello de botella móvil, misma instancia de 3×4 | 14–30 | It. 1: $C_{max}=22$; $L_{max}$ = 5, 5, 4, 0 en M1–M4; se fija M1 con secuencia 1-2-3 y $C_{max}=27$. It. 2: $L_{max}(M2)=1$ con secuencia 2-1-3 y $L_{max}(M3)=1$; se fija M2 y $C_{max}=28$; re-optimizar M1 no mejora. It. 3: M3 y M4 tienen $L_{max}=0$. **Final: $C_{max}=28$**, con secuencias M1: 1-2-3, M2: 2-1-3, M3: 2-1, M4: 2-3 (Gantt de la pág. 30). Coincide con el óptimo. |
| LEKIN con la instancia MT10 | 31 | $C_{max}$: Local Search 1107, General SB Routine 1110, Shifting Bottleneck 1113, WSPT 1356. |

**Páginas clave**

- 3: definición de job shop.
- 4–5: modelo disyuntivo.
- 6, 8: grafo disyuntivo.
- 7, 14: datos del ejemplo.
- 9–10: código GAMS completo.
- 11–13: algoritmo del cuello de botella móvil.
- 15–30: ejemplo paso a paso (17–22: subproblemas de la iteración 1; 27: iteración 2; 30: Gantt final).
- 31: LEKIN.
- 32: Rubén Ruiz.

**Relación con otros archivos del repo**

- [L16 – Introducción al scheduling](/corte-3-programacion-scheduling/01-introduccion-scheduling/L16-intro-scheduling.md): notación $\alpha\mid\beta\mid\gamma$; $J_m$ y *recrc* en la pág. 21; $FJ_c$ y open shop en la pág. 22.
- [L17 – Una máquina](/corte-3-programacion-scheduling/02-una-maquina/L17-single-machine-scheduling.md): regla EDD para $1\|L_{max}$ (pág. 7) y $1\mid r_j\mid L_{max}$ es NP-hard (pág. 32). Es el subproblema que resuelve el cuello de botella móvil.
- [L19 – Flow shop](/corte-3-programacion-scheduling/04-flow-shop/L19-flow-shop-scheduling.md): caso particular en que todos los trabajos siguen la misma ruta.
- [Compendio de métodos del Corte 3](/corte-3-programacion-scheduling/00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md).
- [Modelo de flujo en GAMS (Corte 2)](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/): otro ejemplo del curso escrito en GAMS.
- [Proyecto competencia de scheduling](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/): sus retos no son job shops (reto 1: flow shop de permutación; reto 2: máquinas paralelas con $r_j$ y precedencias), pero usan las mismas ideas de búsqueda local, y su informe cita el *iterated greedy* de Ruiz y Stützle (pág. 32).


---

<!-- fuente: corte-3-programacion-scheduling/otros-archivos/README.md -->
# Otros archivos: material de otra materia (Corte 3)

## Qué cubre

**Esta carpeta no tiene material de Planeación, Programación y Control de la Producción.** Guarda un Excel de otra materia, **Gerencia Financiera**, que el estudiante tenía en la carpeta del Corte 3 (nombre original `CORTE 3/Parcial 2do Corte G. Financiera .xlsx`). Se conserva para no perder información, pero no hace falta leerlo para el curso de Planeación: ningún tema ni proyecto de scheduling lo usa.

El libro es un parcial de estados financieros. Parte de los balances de prueba de 2024 y 2025 de una comercializadora de vehículos y pide el estado de resultados, el balance general y los análisis vertical y horizontal. Está resuelto solo en parte.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [otra-materia-gerencia-financiera-parcial-2do-corte.md](/corte-3-programacion-scheduling/otros-archivos/otra-materia-gerencia-financiera-parcial-2do-corte.md) (gemelo de `otra-materia-gerencia-financiera-parcial-2do-corte.xlsx`) | **Gerencia Financiera, no Planeación.** Hojas `TB ` (balances de prueba 2024 y 2025) y `EEFF` (estado de resultados y balance con análisis vertical, incompletos) | Solo si se estudia Gerencia Financiera |

## Orden de estudio sugerido

No aplica al curso de Planeación. Para Gerencia Financiera:

1. Leer la hoja `TB `, que tiene las cuentas, los débitos y los créditos.
2. Leer la hoja `EEFF`: fórmulas, resultados y comentarios con la regla del impuesto del 35 %.
3. Revisar la tabla «Cómo se completaría» del gemelo, que es un cálculo propio.

## Conceptos y fórmulas clave

El detalle está en [el gemelo](/corte-3-programacion-scheduling/otros-archivos/otra-materia-gerencia-financiera-parcial-2do-corte.md).

- **Utilidad bruta** = Ventas − Costo de ventas.
- **EBIT** = Utilidad bruta − Gastos de administración − Gastos de ventas − Depreciación (y amortización).
- **UAI** = EBIT − Gastos financieros + Ingresos no operacionales.
- **Impuesto** = $0{,}35\cdot UAI$ si $UAI>0$; si no, 0.
- **Utilidad neta** = UAI − Impuesto.
- **EBITDA** = EBIT + Depreciación + Amortización.
- **Análisis vertical:** $\text{partida}/\text{Ventas}$.
- **Análisis horizontal:** $\Delta\$=X_{2025}-X_{2024}$ y $\Delta\%=\Delta\$/X_{2024}$.
- **Comprobación:** Activo − Pasivo − Patrimonio = 0.

## Ejercicios resueltos disponibles

| Ejercicio | Archivo | Resultado principal |
|---|---|---|
| Estado de resultados 2024–2025 (parcial) | [gemelo](/corte-3-programacion-scheduling/otros-archivos/otra-materia-gerencia-financiera-parcial-2do-corte.md) | En la hoja: EBIT 170.000 y 240.000; UAI 156.000 y 228.000. El EBIT de la hoja omite la amortización |
| Cierre completo con impuesto del 35 % (cálculo propio) | [gemelo](/corte-3-programacion-scheduling/otros-archivos/otra-materia-gerencia-financiera-parcial-2do-corte.md) | Utilidad neta 94.900 y 141.700; total activo 850.000 y 1.058.000, que cuadra con pasivo + patrimonio |

## Relación con otros temas y proyectos

Ninguna con Planeación. Ver el [Corte 3](/corte-3-programacion-scheduling/) para el material de scheduling, por ejemplo [01-introduccion-scheduling](/corte-3-programacion-scheduling/01-introduccion-scheduling/) o [proyecto-competencia-scheduling](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/).


---

<!-- fuente: corte-3-programacion-scheduling/proyecto-competencia-scheduling/README.md -->
# Proyecto: competencia de scheduling en Gradescope (Corte 3)

## Qué cubre

Es el proyecto final del Corte 3: una competencia por grupos de 5 en la que cada grupo programa en Python dos algoritmos de secuenciación. Gradescope los califica automáticamente con instancias aleatorias: 60 % calidad del objetivo, 30 % tiempo de cómputo y 10 % reporte técnico en PDF.

- **Reto 01, Willy Wonka:** flow shop de permutación de 3 máquinas, alistamientos según el tipo de lote y prohibición N→R; objetivo $C_{\max}$.
- **Reto 02, Monstruópolis:** 3 máquinas paralelas idénticas con fechas de liberación y precedencias; objetivo $\sum w_jT_j$.

La carpeta tiene los enunciados y las plantillas del profesor (`enunciados/`) y la solución del estudiante (`solucion/`). La solución entrega el óptimo demostrado en el Reto 1 y queda a ~0,05 % del mejor valor conocido en el Reto 2.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [enunciados/instructivo-competencia-scheduling.md](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/instructivo-competencia-scheduling.md) (gemelo del PDF, 4 págs.) | Reglas de la competencia: retos, pesos de la nota, penalizaciones, ranking, formato `solve()`, librerías permitidas, límite de 60 s | **1.º** |
| [enunciados/reto-1-willy-wonka.md](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/reto-1-willy-wonka.md) (gemelo del PDF, 4 págs.) | Enunciado del Reto 01: 15 lotes S/N/R, tiempos en M1–M3, alistamientos (Tablas 2–4), regla N→R, formato `data.json` | **2.º** |
| [enunciados/reto-2-monstruopolis.md](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/reto-2-monstruopolis.md) (gemelo del PDF, 3 págs.) | Enunciado del Reto 02: 50 trabajos, $p_j$, $r_j$, $d_j$, $w_j$, precedencias, objetivo, ejemplo de salida | **3.º** |
| [enunciados/plantilla-reto-1-willy-wonka/reto_schedulling.py](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/plantilla-reto-1-willy-wonka/reto_schedulling.py) | Plantilla del profesor para el Reto 1: clase `Schedulling`, generador aleatorio de instancias y evaluador `calcular_makespan_penalizado` (ver abajo) | 4.º |
| [enunciados/plantilla-reto-2-monstruopolis/reto_schedulling.py](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/plantilla-reto-2-monstruopolis/reto_schedulling.py) | Plantilla del profesor para el Reto 2: clase `Schedulling(GeneradorInstancias)` con un esqueleto de `resolver_instancia()` (ver abajo) | 4.º |
| [solucion/README.md](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/README.md) | README de la solución, escrito por el estudiante: algoritmos, qué subir a Gradescope, cómo probar, calidad frente a tiempo, problemas abiertos | **5.º** |
| [solucion/INFORME_TECNICO.md](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/INFORME_TECNICO.md) | Borrador del reporte técnico (10 % de la nota): modelo, algoritmo, justificación, resultados, lecciones y referencias | **6.º** |
| [solucion/reto1.py](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/reto1.py) | Reto 1 en el formato del instructivo, `solve(data) -> {"Cmax","secuencia","tiempo"}`. Clase `WillyWonka`: cota inferior, NEH, bloques por tipo, búsqueda local con aceleración de Taillard, programación dinámica acotada e Iterated Greedy de respaldo | 7.º |
| [solucion/reto2.py](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/reto2.py) | Reto 2 en el formato del instructivo, `solve(data) -> [{"job","machine","start","end"}]`. Clase `Monstruopolis`: lectura de varios formatos de entrada, decodificador de listas, 8 reglas de despacho y recocido simulado con evaluación incremental | 7.º |
| [solucion/construir_plantillas.py](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/construir_plantillas.py) | Copia el bloque entre `# === INICIO ALGORITMO ===` y `# === FIN ALGORITMO ===` de `reto1.py`/`reto2.py` dentro de la plantilla del profesor y escribe los archivos de `gradescope/` | — |
| [solucion/gradescope/reto1_willy_wonka/reto_schedulling.py](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/gradescope/reto1_willy_wonka/reto_schedulling.py) | Reto 1 empaquetado en la plantilla del profesor (generado; no se edita a mano). `resolver_instancia()` devuelve `secuencia`, `valor_objetivo`, `Cmax` y `tiempo`; el `import optimizador` queda en un `try/except` | — |
| [solucion/gradescope/reto2_monstruopolis/reto_schedulling.py](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/gradescope/reto2_monstruopolis/reto_schedulling.py) | Reto 2 empaquetado en la plantilla del profesor (generado). `resolver_instancia()` devuelve `secuencia` (con `Cj`) y `valor_objetivo` | — |
| [solucion/pruebas/probar_reto1.py](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/probar_reto1.py) | Banco local del Reto 1: 30 instancias del generador de la plantilla (semilla 42). Valida la permutación y N→R, recalcula el $C_{\max}$ con un evaluador independiente, lo compara con la cota (y con el exacto si se usa `--exacto`) y muestra también el valor de la función defectuosa de la plantilla | — |
| [solucion/pruebas/probar_reto2.py](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/probar_reto2.py) | Banco local del Reto 2: 30 instancias. Un validador independiente revisa $r_j$, precedencias, solapes y $end=start+p_j$, y recalcula $\sum w_jT_j$. Opciones `--referencia` (corrida larga) y `--holgura` | — |
| [solucion/pruebas/exacto_reto1.py](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/exacto_reto1.py) | Segundo método exacto del Reto 1, implementado aparte para verificar el primero: programación dinámica por capas con frentes de Pareto (fin M1, M2, M3) y poda por cota | — |
| [solucion/pruebas/cota_reto2.py](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/cota_reto2.py) | Cota inferior del Reto 2 por relajación lagrangiana de la formulación indexada en el tiempo, con subgradiente y paso de Polyak (usa numpy) | — |
| [solucion/pruebas/generador.py](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/generador.py) | Imitación local del módulo `generador` que la plantilla del Reto 2 importa en Gradescope. Hace $p_j\in[10,100]$, $r_j\in[0,30]$, $w_j\in[1,5]$, 5 precedencias $i<j$ y $d_j$ igual al fin más temprano | — |
| [solucion/pruebas/data_ejemplo_reto1.json](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/data_ejemplo_reto1.json) | Datos del enunciado de Willy Wonka (Tablas 1–4) en el formato `data.json` | — |
| [solucion/pruebas/data_ejemplo_reto2.json](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/data_ejemplo_reto2.json) | Instancia de 50 trabajos en formato de filas (`Trabajo, p_j, r_j, d_j, w_j, Predecesores`), con precedencias J2→J21, J23→J27, J17→J31, J22→J36 y J3→J49 | — |
| [solucion/pruebas/data_ejemplo_reto2_plantilla.json](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/data_ejemplo_reto2_plantilla.json) | La misma instancia en el formato de la plantilla (`jobs, m, p, r, d, w, preds`) | — |

## Orden de estudio sugerido

1. Leer las reglas en el [instructivo](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/instructivo-competencia-scheduling.md) y los dos enunciados.
2. Repasar la teoría:
   - notación α|β|γ en [01-introduccion-scheduling](/corte-3-programacion-scheduling/01-introduccion-scheduling/);
   - WSPT y ATC en [02-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/);
   - máquinas paralelas en [03-maquinas-paralelas](/corte-3-programacion-scheduling/03-maquinas-paralelas/);
   - Johnson y NEH en [04-flow-shop](/corte-3-programacion-scheduling/04-flow-shop/).
3. Leer la sección «Plantillas del profesor» de este README: las plantillas usan un formato distinto del instructivo y tienen errores.
4. Leer el [informe técnico](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/INFORME_TECNICO.md) y luego el [README de la solución](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/README.md).
5. Ejecutar los ejemplos (ver «Cómo ejecutar») y revisar el código de `reto1.py` y `reto2.py`.

## Enunciado en resumen

**Reglas comunes** (detalle en el [instructivo](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/instructivo-competencia-scheduling.md)):

- Grupos de 5; un integrante sube la entrega.
- Límite de 60 s por instancia; si se pasa, recibe el peor puntaje en esa instancia.
- Solo biblioteca estándar y numpy; nada de OR-Tools, PuLP ni Gurobi.
- Varias entregas permitidas; cuenta la última.
- El ranking usa el objetivo promedio más las penalidades por violación: el mejor equipo recibe 100 y los demás se escalan en proporción.
- Reporte técnico en PDF de máximo 4 páginas.

**Reto 01, Willy Wonka** ([enunciado](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/reto-1-willy-wonka.md)):

- 15 lotes de tres tipos (S simple, N nueces, R relleno) pasan por M1 (mezclado), M2 (moldeo) y M3 (empaque) en el mismo orden en las tres máquinas.
- Los tiempos de ejemplo están entre 27 y 45 min en M1, entre 22 y 40 en M2 y entre 11 y 25 en M3.
- Al cambiar de tipo hay un alistamiento por máquina, por ejemplo N→R: 40, 30 y 12 min en M1, M2 y M3.
- Un lote R no puede ir justo después de uno N.
- Se minimiza el tiempo en que termina el último lote.

**Reto 02, Monstruópolis** ([enunciado](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/reto-2-monstruopolis.md)):

- 50 juguetes con un solo proceso, en 3 máquinas idénticas.
- $p_j\in[10,100]$, $r_j\in[0,30]$, $w_j\in[1,5]$ y $d_j$ = tiempo mínimo teórico de finalización.
- Unas 5 precedencias sin ciclos; sin interrupciones y sin alistamientos.
- Se minimiza la tardanza ponderada total.

## Modelo de cada reto (notación α|β|γ)

### Reto 01: $F3\,|\,prmu,\ s^{m}_{\tau(i)\tau(j)},\ \text{N}\not\to\text{R}\,|\,C_{\max}$

- **α = F3:** flow shop de 3 máquinas en serie.
- **β:**
  - *prmu*, permutación: la misma secuencia en las tres máquinas («secuencia uniforme»);
  - $s^m_{ab}$, alistamiento de la máquina $m$ al pasar de un lote de tipo $a$ a uno de tipo $b$ (0 si $a=b$);
  - restricción de secuencia: no hay parejas consecutivas N→R.
- **γ = $C_{\max}$.**

Recurrencia de tiempos, para una secuencia $\pi$ con $\tau(j)$ el tipo del lote $j$ y $p_{m,j}$ su tiempo en $m$:

$$C_{m,\pi_k}=\max\left(C_{m,\pi_{k-1}},\,C_{m-1,\pi_k}\right)+s^m_{\tau(\pi_{k-1})\tau(\pi_k)}+p_{m,\pi_k},\qquad C_{\max}=C_{3,\pi_n}$$

El primer lote no tiene alistamiento. Es un **supuesto** compartido por la plantilla del profesor y la solución: el alistamiento empieza cuando la máquina está libre y el lote ya llegó, es decir, no se anticipa.

$F3\|C_{\max}$ ya es NP-difícil. Con solo 15 lotes y 3 tipos, sin embargo, una programación dinámica bien acotada lo resuelve exactamente en milisegundos.

### Reto 02: $P3\,|\,r_j,\,prec\,|\,\sum w_jT_j$

- **α = P3:** 3 máquinas idénticas en paralelo.
- **β:** fechas de liberación $r_j$ y precedencias $i\to j$; sin *prmp* (no hay interrupciones).
- **γ:** $\sum_j w_jT_j$, con $T_j=\max(0,\,C_j-d_j)$.

Restricciones: $S_j\ge r_j$, $S_j\ge C_i$ para todo $i\to j$, y en cada máquina los intervalos $[S_j,S_j+p_j)$ no se solapan.

Si $d_j$ es el fin más temprano sin considerar la capacidad, $d_j=\max(r_j,\max_{i\to j}d_i)+p_j$, entonces $C_j\ge d_j$ siempre. En ese caso $\sum w_jT_j=\sum w_jC_j-\sum w_jd_j$, y el problema equivale a $P3\,|\,r_j,prec\,|\,\sum w_jC_j$, donde WSPT es la referencia. Esta observación es del informe técnico.

Es NP-difícil ($1\|\sum w_jT_j$ ya lo es en sentido fuerte), así que con 50 trabajos el óptimo no se puede demostrar en tiempo de competencia.

## Plantillas del profesor (`enunciados/plantilla-*`, sin gemelo)

Las dos se llaman `reto_schedulling.py`, con doble «l», y el nombre es obligatorio. Siguen un formato **distinto** del `solve()` del instructivo: una clase `Schedulling` cuyo método `ejecutar_experimentos()` corre 30 instancias aleatorias (semilla 42), mide el tiempo de cada una y arma un `DataFrame` de pandas con `instancia`, `valor_objetivo` y `tiempo_seg`.

### Plantilla del Reto 1 ([código](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/plantilla-reto-1-willy-wonka/reto_schedulling.py))

- **Instrucciones (docstring):**
  - no cambiar los nombres de la clase ni de `generar_instancia()`, `resolver_instancia()` y `ejecutar_experimentos()`;
  - solo se modifican `generar_instancia()` y `resolver_instancia()`;
  - no se toca `ejecutar_experimentos()`.
- **Imports:** `random`, `numpy`, `time`, `pandas`, `json` y `from optimizador import load_from_dict, run_ga`. El módulo `optimizador` es el ejemplo del profesor, un algoritmo genético, y **no viene con la plantilla**.
- **`__init__(n_instancias=30, semilla=42)`:** fija `random.seed` y `np.random.seed`.
- **`generar_instancia(indice)`** (generador aleatorio, así califica Gradescope):
  - 15 lotes L1–L15, cada uno con un tipo elegido al azar entre S, N y R;
  - tiempos enteros uniformes: M1 en [25, 45], M2 en [20, 40], M3 en [10, 25];
  - alistamientos entre tipos distintos: M1 en [10, 40], M2 en [5, 30], M3 en [3, 15]; 0 si el tipo es el mismo;
  - guarda `instancia_{indice}.json` y devuelve `{"lotes": …, "setup": {"M1": {"S-S": 0, "S-N": …}, …}}`.
- **`resolver_instancia(instancia)`:** llama a `load_from_dict` y `run_ga` del módulo ausente y devuelve solo `{"secuencia": [...]}`. Como `ejecutar_experimentos()` lee `resultado["valor_objetivo"]`, la plantilla tal como viene fallaría con `KeyError`; hay que devolver también `valor_objetivo`.
- **`calcular_makespan_penalizado(data, secuencia)`** (evaluador):
  - si hay una pareja N→R consecutiva, devuelve `inf`;
  - si no, simula el flow shop con $inicio=\max(\text{fin máquina},\text{fin del lote en la máquina anterior})+\text{alistamiento}$.
  - **Tiene un error:** para hallar el tipo anterior recorre **toda** la secuencia y se queda con el último lote con `fin_lote <= fin_maquina`. Los lotes aún no procesados tienen `fin_lote = 0`, así que casi siempre toma el tipo del **último lote de la secuencia**, no el del anterior.
  - Por eso da valores de 651 a 1003 cuando el $C_{\max}$ real de las mismas secuencias está entre 566 y 678 (30 instancias, semilla 42; ejecución de `probar_reto1.py`).

### Plantilla del Reto 2 ([código](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/plantilla-reto-2-monstruopolis/reto_schedulling.py))

- **Imports:** `random`, `numpy`, `time`, `pandas`, `json`, `itertools.product` y `combinations` (sin usar) y `from generador import GeneradorInstancias`. Ese módulo está en Gradescope y **no viene con la plantilla**; genera las instancias y, se deduce, trae `ejecutar_experimentos()`.
- **`Schedulling(GeneradorInstancias)`**, `__init__(n_instancias=30, semilla=42, timelimit=30)`.
- **Formato de instancia que espera `resolver_instancia()`:** `{"jobs": [...], "m": 3, "p": {j: p_j}, "r": {...}, "d": {...}, "w": {...}, "preds": {j: [predecesores]}}`. Con eso arma la lista de sucesores `succs`.
- **Esqueleto incompleto:**
  - `build_schedule()` arma `secuencia_local` con `start_times`, `end_times` y `machine_of`, que no están definidos, y no devuelve nada;
  - luego viene el comentario `# INSERTA AQUI TU CODIGO PARA OPTIMIZAR best_val y best_seq`;
  - después, un ciclo `while` que repite `build_schedule()` hasta `timelimit − 1` = 29 s, usando `start_global` (no definido) y quedándose con el mejor valor.
  - Tal como viene no corre: es un andamio para completar.
- **Salida esperada:** `{"secuencia": [{"job", "machine", "start", "end", "Cj"}, …], "valor_objetivo": Σ w_j T_j}`.
- **Ojo:** el ciclo de la plantilla consume casi todo el `timelimit` por instancia, lo que va contra el 30 % de la nota que depende del tiempo. La solución lo reemplaza por un recocido que termina en unos 80 ms.

### Inconsistencias entre instructivo y plantillas

- **Formato:** el instructivo pide `reto1.py`/`reto2.py` con `solve(data)` que lee `data.json`; las plantillas piden `reto_schedulling.py` con la clase `Schedulling`. La solución entrega **ambos** formatos con el mismo algoritmo.
- **Librerías:** el instructivo permite solo la biblioteca estándar y numpy, pero las plantillas importan `pandas` (y la del Reto 1, el módulo `optimizador`).

## Enfoque de la solución

Detalle completo en el [informe técnico](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/INFORME_TECNICO.md). Lo que va en la entrega usa solo la biblioteca estándar; numpy aparece solo en `pruebas/`. Cada reto usa su propia semilla (`random.Random(2026)`), así que no altera el `random` global con el que la plantilla genera las instancias.

### Reto 1: cota inferior + heurística + programación dinámica acotada (óptimo demostrado)

1. **Cota inferior (LB) por órdenes de tipo.** Para cada recorrido posible de los tipos que nunca pasa de N a R (primer tipo $t_1$, último $t_k$), se calculan tres cotas:
   - $B_1=\sum p_1+\text{alistamientos de M1}+\min_{\tau(j)=t_k}(p_{2j}+p_{3j})$;
   - $B_2=\min_{\tau(j)=t_1}p_{1j}+\sum p_2+\text{alistamientos de M2}+\min_{\tau(j)=t_k}p_{3j}$;
   - $B_3=\min_{\tau(j)=t_1}(p_{1j}+p_{2j})+\sum p_3+\text{alistamientos de M3}$.

   La cota es $LB=\min_{\text{órdenes}}\max(B_1,B_2,B_3)$. Si una solución la alcanza, es óptima.
2. **Heurística:**
   - NEH adaptado, que inserta cada lote solo en posiciones factibles;
   - una secuencia por cada orden de bloques permitido (SRN, NSR, RSN, RNS), con los lotes de cada bloque ordenados por la regla de Johnson sobre $(p_1+p_2,\ p_2+p_3)$;
   - búsqueda local por inserción con la **aceleración de Taillard** adaptada a los alistamientos: todas las posiciones se evalúan en $O(n\cdot m)$ y no en $O(n^2 m)$.
3. **Exacto: programación dinámica acotada.**
   - El estado es (conjunto de lotes programados, tipo del último).
   - De cada estado se guardan solo los vectores (fin M1, fin M2, fin M3) no dominados.
   - Se poda todo estado cuya cota no pueda mejorar la heurística.
   - Si nada sobrevive, la heurística era óptima; si algo sobrevive, de ahí sale la secuencia óptima.
   - Tope de seguridad: 400 000 estados o 2 s.
4. **Respaldo:** Iterated Greedy de Ruiz y Stützle con $d=4$ y $T=0{,}4$, solo si el exacto llega a su tope; no ocurrió en ninguna prueba.
5. **Factibilidad:** cada pareja N→R suma una penalidad interna de $10^6$; el exacto nunca genera esas parejas.

### Reto 2: reglas de despacho + recocido simulado con evaluación incremental

- **Representación:** una lista de prioridad topológica, donde cada predecesor va antes que sus sucesores.
- **Decodificador:**
  - cada trabajo empieza lo antes posible, en $listo_j=\max(r_j,\ \max_{i\to j}C_i)$;
  - va a la máquina que permite empezar antes; si hay empate, a la que quedó libre más tarde (*best fit*).
  - Toda lista da un programa factible.
- **8 listas iniciales**, de las que se queda la mejor:
  - WSPT estático ($w_j/p_j$);
  - razón de cadenas al estilo Sidney (un predecesor hereda la mayor $\sum w/\sum p$ de las cadenas que salen de él);
  - EDD;
  - WSPT dinámico;
  - ATC con $K\in\{0{,}5;\,1;\,2;\,4\}$, con índice

$$I_j(t)=\frac{w_j}{p_j}\exp\!\left(-\frac{\max(d_j-p_j-t,\,0)}{K\,\bar p}\right)$$
- **Recocido simulado:**
  - 10 000 movimientos de inserción o intercambio a distancia ≤ 20;
  - temperatura geométrica de $0{,}6$ a $0{,}001\times(\bar w\,\bar p)$.
  - La evaluación es incremental: se re-decodifica desde la primera posición cambiada usando «fotos» del estado de las máquinas, el número de Metropolis se sortea antes de evaluar para cortar apenas se supera el umbral, y la evaluación se detiene si las máquinas vuelven a quedar como en la solución base.

## Resultados

### Reto 1

| Prueba | Resultado |
|---|---|
| Ejemplo del enunciado (Tablas 1–4) | Secuencia L9, L12, L6, L15, L3 (R) → L4, L13, L10, L1, L7 (S) → L8, L11, L5, L14, L2 (N). **$C_{\max}=621$**, igual a la cota inferior, así que es óptimo. L2 termina en M1 a los 573 min, en M2 a los 600 y en M3 a los 621 (verificado con un evaluador independiente). Tiempo ≈ 1 ms |
| 30 instancias de la plantilla (semilla 42), ejecución de `probar_reto1.py` | **30/30 óptimas demostradas**; $C_{\max}$ promedio **616,77**; el óptimo queda en promedio 0,695 % por encima de la cota inferior (12 instancias la igualan); tiempo medio de 3,6 ms (máximo 18,9 ms) |
| 200 instancias del generador | 200/200 óptimas demostradas, 115 de ellas solo con la cota; 3,8 ms de media y 59 ms de máximo (según el informe) |
| 400 instancias más difíciles | 400/400 demostradas; peor caso 265 ms (según el informe) |
| Ablación (200 instancias) | Solo NEH: 96/200 óptimas. NEH + bloques: 166/200. + búsqueda local + IG: 197/200. + programación dinámica: 200/200 |
| Entrega en Gradescope (según el registro del estudiante) | El autocalificador reportó «616.7667 / 100.0», exactamente el $C_{\max}$ óptimo promedio de las 30 instancias de la plantilla con semilla 42. Se deduce que Gradescope usa ese generador y esa semilla y reporta el promedio del objetivo (menor es mejor), no un porcentaje |

### Reto 2

| Prueba | Resultado |
|---|---|
| Instancia de ejemplo `data_ejemplo_reto2.json` | $\sum w_jT_j=27\,683$ en ≈ 72 ms (ejecución de `reto2.py`) |
| 30 instancias del generador local (semilla 42), ejecución de `probar_reto2.py` | $\sum w_jT_j$ promedio **38 182,0**; 2,78 % de mejora sobre la mejor regla de despacho; 75 ms de media (máximo 83 ms); **0 violaciones** |
| Brecha contra corridas 150 veces más largas | Solo reglas: 2,94 %, ~2 ms. SA de 5000 iteraciones: 0,17 %, ~37 ms. **SA de 10 000 (entregado): 0,046 %, ~79 ms.** SA de 20 000: 0,042 %, ~151 ms |
| Cota lagrangiana | Las soluciones quedan, en promedio, como máximo 2,4 % por encima. La cota es floja: con más iteraciones ya no sube |
| Robustez con $d_j$ holgados | Las reglas quedan a 18,6 % y el SA de 10 000 a 1,8 % (0,7 % con 20 000) |

## Cómo ejecutar

Desde `solucion/`:

```
python reto1.py pruebas/data_ejemplo_reto1.json      # Reto 1, formato solve(): imprime {"Cmax","secuencia","tiempo"}
python reto2.py pruebas/data_ejemplo_reto2.json      # Reto 2, formato solve(): imprime la lista JSON; por stderr, sum wjTj y el tiempo
python pruebas/probar_reto1.py --exacto              # 30 instancias de la plantilla + verificación con el segundo exacto
python pruebas/probar_reto2.py                       # 30 instancias + validador independiente
python pruebas/probar_reto2.py --holgura 0.5         # fechas de entrega más sueltas
python pruebas/cota_reto2.py                         # cota lagrangiana (requiere numpy)
python construir_plantillas.py                       # regenera gradescope/*/reto_schedulling.py tras cambiar reto1.py o reto2.py
```

**Notas para ejecutar:**

- Sin argumento, `reto1.py` y `reto2.py` leen `data.json` del directorio actual, como pide el instructivo.
- Las versiones de `gradescope/` importan `numpy` y `pandas` (exigencia de la plantilla). La del Reto 2 importa además `generador`; en local se puede suplir con `pruebas/generador.py` en el `PYTHONPATH` (deducido).
- **Qué subir:** si Gradescope pide `reto_schedulling.py`, el de `gradescope/` del reto; si pide `reto1.py` y `reto2.py`, esos. Parámetros de calidad frente a tiempo: `EXACTO_R1` y `MAX_SIN_MEJORA_R1` en el Reto 1, `ITER_SA_R2` en el Reto 2.

## Conceptos y fórmulas clave

- **Notación α|β|γ:** α es el entorno de máquinas (F3, P3), β las restricciones (prmu, $s_{ij}$, $r_j$, prec) y γ el objetivo ($C_{\max}$, $\sum w_jT_j$). Ver [L16](/corte-3-programacion-scheduling/01-introduccion-scheduling/L16-intro-scheduling.md).
- **Flow shop con alistamiento:** $C_{m,\pi_k}=\max(C_{m,\pi_{k-1}},C_{m-1,\pi_k})+s^m_{\tau(\pi_{k-1})\tau(\pi_k)}+p_{m,\pi_k}$. Ver [reto-1](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/reto-1-willy-wonka.md).
- **NEH y Johnson:** en [L19](/corte-3-programacion-scheduling/04-flow-shop/L19-flow-shop-scheduling.md). La regla de Johnson para tres máquinas usa $(p_1+p_2,\ p_2+p_3)$.
- **Tardanza:** $T_j=\max(0,C_j-d_j)$.
- **WSPT:** ordenar por $w_j/p_j$ decreciente.
- **ATC:** $I_j(t)=\frac{w_j}{p_j}e^{-\max(d_j-p_j-t,0)/(K\bar p)}$. Ver [L17](/corte-3-programacion-scheduling/02-una-maquina/L17-single-machine-scheduling.md) y [atc.py](/corte-3-programacion-scheduling/02-una-maquina/atc.py).
- **Recocido simulado:** se acepta un vecino peor con probabilidad $e^{-\Delta/T}$, con $T$ que decrece geométricamente.
- **Iterated Greedy:** destruir $d$ lotes, reinsertarlos con NEH y aceptar con temperatura constante.

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado |
|---|---|---|
| Willy Wonka con los datos del enunciado | [solucion/reto1.py](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/reto1.py) con [data_ejemplo_reto1.json](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/data_ejemplo_reto1.json); explicado en el [informe](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/INFORME_TECNICO.md) | $C_{\max}=621$ (óptimo), bloques R → S → N |
| 30 instancias de la plantilla del Reto 1 | [probar_reto1.py](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/probar_reto1.py) | 30/30 óptimas, $C_{\max}$ promedio 616,77 |
| Monstruópolis, instancia de ejemplo | [solucion/reto2.py](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/reto2.py) con [data_ejemplo_reto2.json](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/data_ejemplo_reto2.json) | $\sum w_jT_j=27\,683$ |
| 30 instancias del Reto 2 | [probar_reto2.py](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/probar_reto2.py) | Promedio 38 182; ~0,05 % del mejor conocido; 0 violaciones |

## Problemas abiertos y observaciones

- **Formato que califica Gradescope:** no está claro si es `solve()` o la clase `Schedulling`. La solución entrega ambos con el mismo algoritmo.
- **Evaluador de la plantilla del Reto 1:** `calcular_makespan_penalizado` toma mal el tipo anterior (ver arriba). La solución optimiza el $C_{\max}$ real del enunciado. El 616,7667 que reportó Gradescope coincide con el `valor_objetivo` que devuelve la propia solución (el $C_{\max}$ real). No se sabe si Gradescope lo recalcula; si usara `calcular_makespan_penalizado`, el promedio sería mayor (651–1003 por instancia).
- **Datos del enunciado:** el ejemplo de `data.json` del Reto 1 contradice la Tabla 2 en S-N y S-R. En el Reto 2, $d_j$ es ambiguo, la disponibilidad de las máquinas se menciona pero no se da, y el ejemplo de salida está rotulado como entrada. Ver los gemelos.
- **No se sabe cómo se puntúa el tiempo** (30 %). Por eso los parámetros se fijaron en el punto donde más tiempo casi no mejora la calidad.
- **Detalles menores del código:**
  - la cabecera de `gradescope/reto2_monstruopolis/reto_schedulling.py`, que viene de `construir_plantillas.py`, menciona «+ busqueda local por insercion», pero `reto2.py` solo usa reglas y recocido;
  - los docstrings de `pruebas/` dicen «desde la carpeta PROYECTO ALGORITMO», que era el nombre original de `solucion/`;
  - `INFORME_TECNICO.md` conserva el marcador «Integrantes: [nombres del grupo]».

## Relación con otros temas y proyectos

- [01-introduccion-scheduling](/corte-3-programacion-scheduling/01-introduccion-scheduling/): notación α|β|γ y medidas de desempeño.
- [02-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/): WSPT, EDD y ATC, la base de las reglas de despacho del Reto 2; [atc.py](/corte-3-programacion-scheduling/02-una-maquina/atc.py).
- [03-maquinas-paralelas](/corte-3-programacion-scheduling/03-maquinas-paralelas/): máquinas paralelas y LNS, el entorno del Reto 2.
- [04-flow-shop](/corte-3-programacion-scheduling/04-flow-shop/): Johnson y NEH, la base de la heurística del Reto 1.
- [05-job-shop](/corte-3-programacion-scheduling/05-job-shop/): búsqueda local y la referencia de Ruiz y Stützle (iterated greedy); ninguno de los retos es un job shop.
- [00-compendio-metodos-scheduling](/corte-3-programacion-scheduling/00-compendio-metodos-scheduling/): compendio de los métodos del corte.
- [otros-archivos](/corte-3-programacion-scheduling/otros-archivos/): no tiene relación (material de otra materia).


---

<!-- fuente: corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/instructivo-competencia-scheduling.md -->
# instructivo-competencia-scheduling

> **Archivo:** [`instructivo-competencia-scheduling.pdf`](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/instructivo-competencia-scheduling.pdf) · **Corte 3** · 4 páginas  
> **Nombre original:** `CORTE 3/PROYECTO 3/Instructivo_Competencia_Scheduling (1).pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** reglas generales de la competencia de secuenciación del Corte 3: dos retos de scheduling programados en Python y calificados automáticamente en Gradescope.

**Ideas clave**

- Se trabaja en grupos de exactamente 5 estudiantes; un solo integrante sube la entrega a Gradescope.
- Hay dos retos:
  - **Reto 01, Willy Wonka:** flow shop de 3 máquinas en serie con 15 lotes, alistamiento dependiente del tipo y prohibición de que un lote R vaya justo después de uno N. Objetivo: minimizar $C_{\max}$.
  - **Reto 02, Monstruópolis:** 3 máquinas idénticas en paralelo con 50 trabajos, fechas de liberación $r_j$, fechas de entrega $d_j$, unas 5 precedencias y sin interrupciones. Objetivo: minimizar $\sum w_jT_j$.
- **La nota** se reparte así: 60 % calidad del objetivo, 30 % tiempo de cómputo y 10 % reporte técnico (PDF de máximo 4 páginas).
- **El ranking** se calcula con el valor promedio del objetivo sobre varias instancias generadas automáticamente. El mejor equipo recibe 100 puntos y los demás se escalan en proporción.
- **Las infactibilidades** no dan cero, pero suman una penalidad proporcional al número de violaciones antes de normalizar. Una solución infactible nunca debe superar a una factible.
- **Restricciones de entrega:**
  - límite de 60 s por instancia (si se pasa, recibe el peor puntaje en esa instancia);
  - solo biblioteca estándar de Python y numpy; nada de OR-Tools, PuLP, Gurobi ni similares;
  - no se aceptan notebooks ni ZIP;
  - se permiten varias entregas y cuenta la última;
  - el código debe ser propio.
- **Formato pedido por el instructivo:** archivos `reto1.py` y `reto2.py` con una función `solve(data)` que lee `data.json`.
  - El Reto 01 devuelve `{"Cmax", "secuencia", "tiempo"}`.
  - El Reto 02 devuelve una lista de `{"job", "machine", "start", "end"}`; Gradescope calcula $C_j$ y $\sum w_jT_j$.
- **Recomendaciones del profesor:**
  - Reto 01: NEH, búsqueda local (2-opt, inserción) o recocido simulado, verificando N→R antes de calcular el $C_{\max}$.
  - Reto 02: reglas de despacho (WSPT, EDD ponderado), revisando en cada decisión qué trabajos ya tienen sus predecesores terminados.
  - Consejo general: empezar con una solución factible simple y luego mejorar; «un algoritmo rápido con solución aceptable suele ganarle a uno lento con solución teóricamente perfecta».

**Fórmulas y métodos**

- **Reto 01:** $C_{\max}=\max_j C_{j,M3}$, el instante en que el último lote sale de M3.
- **Reto 02:** $\sum_j w_jT_j$, con $T_j=\max(0,\,C_j-d_j)$, donde $w_j$ es el peso, $C_j$ el tiempo de terminación y $d_j$ la fecha de entrega.
- **Puntaje de calidad deducido de la descripción** (no hay fórmula explícita): $\text{puntaje}_e=100\cdot\dfrac{\bar z_{\text{mejor}}}{\bar z_e}$, con $\bar z_e$ el objetivo promedio del equipo $e$ más sus penalidades. No se dice cómo se puntúa el tiempo.
- **Métodos sugeridos:** NEH, búsqueda local 2-opt e inserción, simulated annealing, WSPT ($w_j/p_j$ decreciente) y EDD ponderado.

**Ejemplos resueltos:** no hay; solo ejemplos de formato. Para el Reto 01: `"Cmax": 847`, `"tiempo": 12`. Para el Reto 02: J1 en M1 de 0 a 45 y J2 en M2 de 10 a 35.

**Páginas clave**

| Página | Contenido |
|---|---|
| 1 | Los dos retos |
| 2 | Criterios, penalización, ranking, reporte y formatos de salida |
| 3 | Plantilla `solve()`, reglas y recomendación del Reto 01 |
| 4 | Recomendación del Reto 02 y consejo general |

**Relación con otros archivos del repo**

- Enunciados detallados: [reto-1-willy-wonka.md](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/reto-1-willy-wonka.md) y [reto-2-monstruopolis.md](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/reto-2-monstruopolis.md).
- **Plantillas del profesor:** [plantilla-reto-1-willy-wonka/reto_schedulling.py](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/plantilla-reto-1-willy-wonka/reto_schedulling.py) y [plantilla-reto-2-monstruopolis/reto_schedulling.py](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/plantilla-reto-2-monstruopolis/reto_schedulling.py). Usan **otro formato**, la clase `Schedulling` con `resolver_instancia()`, distinto del `solve()` de este instructivo; ver el [README del proyecto](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/README.md).
- Solución del estudiante: [solucion/README.md](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/README.md) e [INFORME_TECNICO.md](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/INFORME_TECNICO.md).
- Teoría:
  - [L19 Flow shop](/corte-3-programacion-scheduling/04-flow-shop/L19-flow-shop-scheduling.md), para el Reto 01;
  - [L18 Máquinas paralelas](/corte-3-programacion-scheduling/03-maquinas-paralelas/L18-parallel-machine-scheduling.md), para el Reto 02;
  - [L17 Una máquina](/corte-3-programacion-scheduling/02-una-maquina/L17-single-machine-scheduling.md), con WSPT, EDD y ATC.

**Observaciones**

- **El instructivo y las plantillas no coinciden en formato.** El instructivo pide `reto1.py`/`reto2.py` con `solve()`. Las plantillas `.py` del profesor piden un archivo `reto_schedulling.py` con la clase `Schedulling`, que además importa `pandas` aunque el instructivo solo permite la biblioteca estándar y numpy.
- Los ejemplos de salida usan comentarios `//`, que no son JSON válido; son solo ilustrativos.
- No se especifica cómo se convierte el tiempo de cómputo en el 30 % de la nota.


---

<!-- fuente: corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/reto-1-willy-wonka.md -->
# reto-1-willy-wonka

> **Archivo:** [`reto-1-willy-wonka.pdf`](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/reto-1-willy-wonka.pdf) · **Corte 3** · 4 páginas  
> **Nombre original:** `CORTE 3/PROYECTO 3/Reto Willy Wonka .pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** enunciado del Reto 01 de la competencia del Corte 3, un flow shop de permutación de 3 máquinas con alistamientos dependientes del tipo de lote y una restricción de secuencia (N no puede ir justo antes de R). Objetivo: minimizar el makespan.

**Ideas clave**

- **Tres tipos de lote:** simple (S), con nueces (N) y relleno (R). Hay 15 lotes (L1–L15) de 100 tabletas cada uno, y todos pasan por M1 (mezclado), M2 (moldeo) y M3 (empaque) en ese orden.
- **«Secuencia uniforme a lo largo de las máquinas»:** el orden de los lotes es el mismo en las tres máquinas, es decir, un flow shop de **permutación**.
- **Restricción de factibilidad:** un lote R no puede procesarse **inmediatamente después** de un N en ninguna máquina; debe haber al menos un lote de otro tipo entre ellos. Con la misma secuencia en las tres máquinas, basta revisar las parejas consecutivas.
- **Alistamiento:** al cambiar de tipo, cada máquina necesita un tiempo que depende del tipo anterior y del siguiente (Tablas 2–4). Es 0 entre lotes del mismo tipo.
- **Datos aleatorios:** los de las tablas son un ejemplo; en la evaluación «los datos variarán de forma aleatoria».
- **Entregables:**
  - un informe breve con la secuencia, el tiempo máximo de terminación y la secuencia en cada máquina;
  - un algoritmo que lea `data.json` (claves `lotes` y `setup`, con 9 combinaciones «X-Y» por máquina) y devuelva `{"Cmax", "secuencia", "tiempo"}`, con el tiempo en milisegundos.

**Fórmulas y métodos**

Notación de tres campos: $F3\,|\,prmu,\ s_{m}(a,b),\ \text{N}\not\to\text{R}\,|\,C_{\max}$. La forma $s_{ij}$ por tipo y la notación son del [informe técnico de la solución](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/INFORME_TECNICO.md); el PDF no usa notación α|β|γ.

Para una secuencia $\pi=(\pi_1,\dots,\pi_{15})$, con $p_{m,j}$ el tiempo de proceso del lote $j$ en la máquina $m$, $\tau(j)$ su tipo y $s_m(a,b)$ el alistamiento de $m$ al pasar del tipo $a$ al $b$:

$$C_{m,\pi_k}=\max\left(C_{m,\pi_{k-1}},\,C_{m-1,\pi_k}\right)+s_m\!\left(\tau(\pi_{k-1}),\tau(\pi_k)\right)+p_{m,\pi_k}$$

con $C_{0,\cdot}=0$, $C_{m,\pi_0}=0$ y sin alistamiento para el primer lote. El objetivo es $C_{\max}=C_{3,\pi_{15}}$.

Factibilidad: $\nexists\,k:\ \tau(\pi_{k-1})=\text{N}\wedge\tau(\pi_k)=\text{R}$.

Este modelo de tiempos es un **supuesto**: el alistamiento empieza cuando la máquina está libre y el lote ya llegó. El PDF no dice si el alistamiento puede anticiparse. Es el mismo supuesto que usa la función de evaluación de la plantilla del profesor y la solución del estudiante.

**Ejemplos resueltos:** el PDF no resuelve el ejemplo. La solución del estudiante obtiene para estos datos:

- secuencia L9, L12, L6, L15, L3 | L4, L13, L10, L1, L7 | L8, L11, L5, L14, L2 (bloques R → S → N);
- **$C_{\max}=621$ min**, igual a su cota inferior, es decir, óptimo demostrado.

Ver [solucion/README.md](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/README.md) e [INFORME_TECNICO.md](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/INFORME_TECNICO.md).

**Páginas clave**

| Página | Contenido |
|---|---|
| 1 | Contexto y máquinas |
| 2 | Tabla 1 (tiempos), regla N→R y explicación de alistamientos |
| 3 | Tablas 2–4 (alistamientos de M1, M2 y M3) y resultado esperado |
| 4 | Formatos JSON de entrada y salida, y autores del reto |

**Relación con otros archivos del repo**

- Reglas generales y calificación: [instructivo-competencia-scheduling.md](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/instructivo-competencia-scheduling.md).
- Plantilla del profesor (generador aleatorio y evaluador): [plantilla-reto-1-willy-wonka/reto_schedulling.py](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/plantilla-reto-1-willy-wonka/reto_schedulling.py); explicada en el [README del proyecto](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/README.md).
- Datos de este enunciado en JSON: [solucion/pruebas/data_ejemplo_reto1.json](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/data_ejemplo_reto1.json). Usa los valores de las Tablas 2–4, no los del ejemplo de la página 4.
- Teoría:
  - [L19 Flow shop](/corte-3-programacion-scheduling/04-flow-shop/L19-flow-shop-scheduling.md), con NEH y Johnson;
  - [flowshop-scheduling](/corte-3-programacion-scheduling/04-flow-shop/flowshop-scheduling.md), el Excel del tema;
  - [L16 Introducción a scheduling](/corte-3-programacion-scheduling/01-introduccion-scheduling/L16-intro-scheduling.md), con la notación α|β|γ.

**Observaciones**

- **Inconsistencia de datos:** el ejemplo de `data.json` de la página 4 da para M1 `"S-R": 15` y `"S-N": 30`, mientras que la Tabla 2 dice S→N = 15 y S→R = 35. Los demás valores de M1 coinciden: N-S 25, N-R 40, R-S 20, R-N 25. El ejemplo parece ilustrativo; la solución del estudiante usa la Tabla 2.
- El ejemplo de entrada lleva comentarios `#`, que no son JSON válido.
- La «secuencia de los lotes en cada una de las máquinas» que pide el informe es la misma en las tres, porque la secuencia es uniforme.


---

<!-- fuente: corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/reto-2-monstruopolis.md -->
# reto-2-monstruopolis

> **Archivo:** [`reto-2-monstruopolis.pdf`](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/reto-2-monstruopolis.pdf) · **Corte 3** · 3 páginas  
> **Nombre original:** `CORTE 3/PROYECTO 3/Planteamiento proyecto Monstruópolis.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** enunciado del Reto 02 de la competencia del Corte 3. Hay que programar 50 trabajos en 3 máquinas idénticas en paralelo, con fechas de liberación y precedencias, para minimizar la tardanza ponderada total. Notación: $P3\,|\,r_j,\,prec\,|\,\sum w_jT_j$.

**Ideas clave**

- **Contexto:** una fábrica de juguetes de Monsters Inc. con 3 máquinas idénticas M1–M3 y 50 trabajos J1–J50. Cada trabajo tiene una sola operación.
- **Generación de datos** (aleatoria por instancia):
  - $p_j\in[10,100]$ minutos;
  - $r_j\in[0,30]$;
  - $w_j\in\{1,\dots,5\}$;
  - alrededor del 10 % de los trabajos con precedencias, unas 5 relaciones $i\to j$ por instancia y sin ciclos;
  - $d_j$ es el «tiempo mínimo teórico de finalización» del trabajo.
- **Restricciones:** sin alistamientos, una tarea por máquina a la vez, sin interrupciones, y cada sucesor empieza solo cuando terminaron **todos** sus predecesores.
- **Entrada:** un JSON con 50 filas y las columnas `Trabajo, p_j, r_j, d_j, w_j, Predecesores`.
- **Salida:** la asignación y secuencia por máquina, $C_j$ de cada trabajo y $\sum w_jT_j$. El ejemplo `secuencia.json` usa una lista de `{"job","machine","start","end"}`, el mismo formato del [instructivo](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/instructivo-competencia-scheduling.md).

**Fórmulas y métodos**

$$\min\ \sum_{j=1}^{n}w_jT_j,\qquad T_j=\max\{0,\;C_j-d_j\},\qquad C_j=S_j+p_j$$

Restricciones, con $S_j$ el inicio de $j$ y $\mu(j)$ su máquina:

- $S_j\ge r_j$;
- $S_j\ge C_i$ para todo $i\to j$;
- si dos trabajos van en la misma máquina, $\mu(i)=\mu(j)$, sus intervalos $[S_i,C_i)$ y $[S_j,C_j)$ no se solapan.

**Interpretación de $d_j$ (deducida).** El «tiempo mínimo teórico de finalización» se entiende como el fin más temprano posible ignorando la capacidad:

$$d_j=\max\!\left(r_j,\ \max_{i\to j}d_i\right)+p_j$$

Con esa definición, $C_j\ge d_j$ siempre, así que $T_j=C_j-d_j$. Minimizar $\sum w_jT_j$ equivale entonces a minimizar $\sum w_jC_j$ (la constante $\sum w_jd_j$ no cambia la solución). Por eso la regla WSPT ($w_j/p_j$ decreciente) es la referencia natural. Esta interpretación es la del generador local de la solución, [solucion/pruebas/generador.py](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/generador.py).

**Ejemplos resueltos:** el PDF no resuelve ninguna instancia. El ejemplo de la página 3 (8 trabajos) solo ilustra el formato y no trae datos de $p_j$, $r_j$, $d_j$ ni $w_j$, así que su objetivo no se puede calcular. Su Gantt:

- M1: J1 de 0 a 45, J4 de 45 a 80, J7 de 80 a 140;
- M2: J2 de 10 a 35, J5 de 35 a 55, J8 de 55 a 95;
- M3: J3 de 5 a 55, J6 de 55 a 85.

**Páginas clave**

| Página | Contenido |
|---|---|
| 1 | Contexto y datos |
| 2 | Precedencias, restricciones, objetivo y formatos |
| 3 | Ejemplo `secuencia.json` y autores |

**Relación con otros archivos del repo**

- Reglas generales: [instructivo-competencia-scheduling.md](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/instructivo-competencia-scheduling.md).
- Plantilla del profesor: [plantilla-reto-2-monstruopolis/reto_schedulling.py](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/plantilla-reto-2-monstruopolis/reto_schedulling.py), explicada en el [README del proyecto](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/README.md).
- Instancia de ejemplo en el formato de filas de este enunciado: [solucion/pruebas/data_ejemplo_reto2.json](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/data_ejemplo_reto2.json).
- Teoría:
  - [L18 Máquinas paralelas](/corte-3-programacion-scheduling/03-maquinas-paralelas/L18-parallel-machine-scheduling.md);
  - [lns-maquinas-paralelas](/corte-3-programacion-scheduling/03-maquinas-paralelas/lns-maquinas-paralelas.md);
  - [L17 Una máquina](/corte-3-programacion-scheduling/02-una-maquina/L17-single-machine-scheduling.md), con WSPT, EDD y ATC;
  - [atc.py](/corte-3-programacion-scheduling/02-una-maquina/atc.py).

**Observaciones**

- **Disponibilidad de máquinas:** el contexto dice que «no todas las máquinas están disponibles al mismo tiempo» por calibraciones y mantenimientos, pero no da ningún dato de disponibilidad. Las restricciones dicen que las máquinas «operan de forma continua». En la práctica se suponen siempre disponibles.
- **Ejemplo mal rotulado:** se presenta como «ejemplo de **entrada**», pero `secuencia.json` es un ejemplo de **salida**. Del formato de entrada solo se dan los nombres de las columnas, sin ejemplo.
- **$d_j$ ambiguo:** «tiempo mínimo teórico de finalización» no dice si incluye las precedencias. La lectura más natural, $r_j+p_j$ o su extensión por la cadena de predecesores, deja $d_j$ muy ajustado: casi todos los trabajos terminan tarde.
- **Título:** usa $W_j$ en mayúscula; el resto del documento usa $w_j$.
