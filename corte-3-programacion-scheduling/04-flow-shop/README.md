# Flow shop y flexible flow shop (Corte 3)

## Qué cubre

Programación de talleres en serie: todos los trabajos pasan por las mismas máquinas en el mismo orden ($Fm||C_{max}$). Incluye el cálculo de tiempos de terminación, la regla de Johnson (óptima para 2 máquinas) y su extensión a 3, el modelo MIP del *flow shop* permutacional y su código en GAMS, las heurísticas CDS y NEH, el *flexible flow shop* con reglas de prioridad y una introducción a los algoritmos genéticos.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [L19-flow-shop-scheduling.md](./L19-flow-shop-scheduling.md) (gemelo del PDF) | Presentación "Lec 19 - flow shop scheduling", 56 diapositivas: Johnson, MIP, código GAMS completo, CDS, NEH, *flexible flow shop* y algoritmos genéticos, con los Gantt en tablas | **Sí (1.º)** |
| [flowshop-scheduling.md](./flowshop-scheduling.md) (gemelo del .xlsx) | Excel de clase con 4 hojas: `Regla de Johnson` (2 y 3 máquinas), `Campbell ` (CDS del ejercicio de L19, solo la iteración 1 correcta), `CDS` y `NEH` (caso de 5 trabajos y 5 máquinas) | 2.º |
| [flowshop-scheduling-datos/CDS.csv](./flowshop-scheduling-datos/CDS.csv) | Volcado CSV completo de la hoja `CDS` | Solo como referencia |

## Orden de estudio sugerido

1. L19, pp. 3-9: definición, recursión de $C_{ij}$ y Johnson para 2 máquinas.
2. Hoja `Regla de Johnson` de [flowshop-scheduling.md](./flowshop-scheduling.md): secuencia al azar (110) frente a Johnson (92) y el caso de 3 máquinas (115).
3. L19, pp. 10-14: extensión de Johnson a 3 máquinas.
4. L19, pp. 15-24: modelo MIP y GAMS.
5. L19, pp. 25-29 (CDS) y pp. 30-36 (NEH). Luego las hojas `CDS` y `NEH` del Excel y las hojas 10-11 del [compendio](../00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md).
6. L19, pp. 37-55: *flexible flow shop* y algoritmos genéticos.

## Conceptos y fórmulas clave

Detalle en [L19-flow-shop-scheduling.md](./L19-flow-shop-scheduling.md).

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

- Máquinas paralelas, que forman cada estación del *flexible flow shop*: [03-maquinas-paralelas](../03-maquinas-paralelas/README.md).
- Job shop, la generalización a rutas distintas por trabajo: [05-job-shop](../05-job-shop/README.md).
- Compendio, hojas 09-11 (Johnson, CDS, NEH): [00-compendio-metodos-scheduling](../00-compendio-metodos-scheduling/README.md).
- El reto 1 de la competencia (Willy Wonka) es un flow shop de permutación $F3$ con alistamientos y restricción de secuencia: [proyecto-competencia-scheduling](../proyecto-competencia-scheduling/enunciados/reto-1-willy-wonka.md).
- Otros modelos en GAMS del curso: [modelo-flujo-gams](../../corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/).
