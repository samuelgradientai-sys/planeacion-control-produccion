# Máquinas paralelas (Corte 3)

## Qué cubre

Programación de $n$ trabajos de una sola operación en $m$ máquinas paralelas. Hay que decidir a qué máquina va cada trabajo y en qué orden. Incluye algoritmos de lista con LPT y SPT, la garantía de LPT para $Pm||C_{max}$, la optimalidad de SPT para $Pm||\sum C_j$, precedencias (CP y LNS), restricciones de elegibilidad $M_j$ (LFJ y LFM), *preemption* (modelo lineal y *wrap-around*) y el MIP para máquinas no relacionadas $Rm||\sum C_j$, más un Excel con algoritmo genético.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [L18-parallel-machine-scheduling.md](./L18-parallel-machine-scheduling.md) (gemelo del PDF) | Presentación "Lec 18 - Parallel Machine Scheduling", 40 diapositivas, con todos los Gantt (LPT, SPT, óptimo, LFJ, Excel) en tablas | **Sí (1.º)** |
| [lns-maquinas-paralelas.md](./lns-maquinas-paralelas.md) (gemelo del .xlsx) | Plantilla incompleta (hoja `LFJ`): 15 trabajos con $p_j$ y $w_j$ para repartir en 3 máquinas. Las fórmulas de la máquina 2 están mal; el .md trae un cálculo propio con LPT, SPT y WSPT | 2.º |

## Orden de estudio sugerido

1. L18, pp. 1-7: definiciones, algoritmo de lista y garantía de LPT.
2. L18, pp. 8-16: ejemplos LPT, SPT y óptimo ($P3$ con 15 trabajos y $P4$ con 9 trabajos) y SPT para $\sum C_j$.
3. Hoja `07_Paralelas_LPT_SPT` del [compendio](../00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md), para repasar los mismos ejemplos en Excel. Ojo con el error en $p_1$.
4. L18, pp. 17-27: precedencias y elegibilidad. Luego la hoja `08_Paralelas_Restric` del compendio, que da el resultado de LFM (p. 26); su solución LFJ omite un trabajo.
5. L18, pp. 28-39: *preemption*, $Rm||\sum C_j$ y el Excel con algoritmo genético.
6. [lns-maquinas-paralelas.md](./lns-maquinas-paralelas.md) como ejercicio para completar.

## Conceptos y fórmulas clave

Detalle en [L18-parallel-machine-scheduling.md](./L18-parallel-machine-scheduling.md).

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
| 15 trabajos en 3 máquinas | [lns-maquinas-paralelas.md](./lns-maquinas-paralelas.md) (cálculo propio) | LPT $C_{max}=111$ (cota 107); SPT $\sum C_j=857$; WSPT $\sum w_jC_j=1618$ |

## Relación con otros temas y proyectos

- Base de una máquina (SPT, WSPT, EDD): [02-una-maquina](../02-una-maquina/README.md).
- Cada estación de un *flexible flow shop* es un problema de máquinas paralelas: [04-flow-shop](../04-flow-shop/README.md) (L19, pp. 37-41).
- Compendio con las hojas 07 y 08: [00-compendio-metodos-scheduling](../00-compendio-metodos-scheduling/README.md).
- *Forward scheduling* con máquinas paralelas en MRP II: [corte 2 / 05-mrp-ii-y-capacidad](../../corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/README.md).
- El reto 2 de la competencia (Monstruópolis) es $P3|r_j,prec|\sum w_jT_j$: [proyecto-competencia-scheduling](../proyecto-competencia-scheduling/enunciados/reto-2-monstruopolis.md).
