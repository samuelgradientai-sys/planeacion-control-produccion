# Compendio de métodos de programación de la producción (Corte 3)

## Qué cubre

Un único libro de Excel que resume, con fórmulas, todos los métodos de *machine scheduling* del corte. En una máquina: SPT, WSPT, EDD, MS, ATC, cadenas con factor $\rho$, *preemption* y Lawler. En máquinas paralelas: LPT, SPT, LNS/CP y LFJ/LFM. En *flow shop*: Johnson, CDS y NEH. Incluye además una hoja de CRP (capacidad) del corte 2. Sirve como repaso rápido: cada hoja trae los datos, el método paso a paso y la comparación de métricas. La explicación detallada de cada tema está en su carpeta.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [metodos-programacion-produccion-corte3.md](./metodos-programacion-produccion-corte3.md) (gemelo del .xlsx) | Compendio de 12 hojas (índice y 11 métodos), con explicación hoja por hoja, tabla de fuentes reales en el repo y errores detectados | **Sí** |

## Orden de estudio sugerido

1. Leer primero las presentaciones de cada tema: [L16](../01-introduccion-scheduling/L16-intro-scheduling.md) (notación), [L17](../02-una-maquina/L17-single-machine-scheduling.md), [L18](../03-maquinas-paralelas/L18-parallel-machine-scheduling.md) y [L19](../04-flow-shop/L19-flow-shop-scheduling.md).
2. Luego usar el compendio como resumen, hoja por hoja, en el orden del índice (02 → 11).
3. Antes de confiar en un número, revisar las "Observaciones" del .md: hay tres hojas con errores (07, 08 y 01).

## Mapa de hojas por tema

| Hoja | Método | Tema / carpeta |
|---|---|---|
| `01_CRP_Capacidad` | CRP (setup + proceso + movimiento) | Corte 2: [05-mrp-ii-y-capacidad](../../corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/) |
| `02_1Maq_Basicos` | Orden inicial, SPT, WSPT, EDD | [02-una-maquina](../02-una-maquina/) |
| `03_1Maq_MS_ATC` | Holgura mínima y ATC | [02-una-maquina](../02-una-maquina/) |
| `04_1Maq_Precedencia` | Cadenas sin romper y factor $\rho$ | [02-una-maquina](../02-una-maquina/) |
| `05_1Maq_Preemption` | $1\|r_j,prmp\|\sum w_jC_j$ | [02-una-maquina](../02-una-maquina/) |
| `06_1Maq_Lawler` | Lawler, $1\|prec\|h_{max}$ | [02-una-maquina](../02-una-maquina/) |
| `07_Paralelas_LPT_SPT` | LPT y SPT en $Pm$ | [03-maquinas-paralelas](../03-maquinas-paralelas/) |
| `08_Paralelas_Restric` | LNS/CP con precedencias; LFJ/LFM con elegibilidad | [03-maquinas-paralelas](../03-maquinas-paralelas/) |
| `09_FlowShop_Johnson` | Johnson $F2$ y $F3$ | [04-flow-shop](../04-flow-shop/) |
| `10_FlowShop_CDS` | Campbell-Dudek-Smith | [04-flow-shop](../04-flow-shop/) |
| `11_FlowShop_NEH` | Nawaz-Enscore-Ham | [04-flow-shop](../04-flow-shop/) |

## Conceptos y fórmulas clave

Detalle en [metodos-programacion-produccion-corte3.md](./metodos-programacion-produccion-corte3.md).

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

- Una máquina: [02-una-maquina](../02-una-maquina/README.md) (L17, Excel de clase y `atc.py`).
- Máquinas paralelas: [03-maquinas-paralelas](../03-maquinas-paralelas/README.md).
- Flow shop: [04-flow-shop](../04-flow-shop/README.md).
- Job shop: [05-job-shop](../05-job-shop/README.md).
- CRP: [corte 2 / 05-mrp-ii-y-capacidad](../../corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/README.md).
- Competencia de *scheduling* (flow shop de permutación y paralelas con precedencias): [proyecto-competencia-scheduling](../proyecto-competencia-scheduling/).
