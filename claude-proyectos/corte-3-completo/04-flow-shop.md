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

## Contenido completo (página por página)

### Página 1 — Portada

"Planeación de Operaciones" · "FLOW SHOPS & FLEXIBLE FLOW SHOPS" · "2026".

> [Imagen decorativa: foto del campus en tonos azules, logo "Universidad de La Sabana – Colombia" e ícono de licencia Creative Commons BY-NC-SA.]

### Página 2 — Agenda

- Flow Shop
- Algoritmo de Johnson
- Implementación en GAMS
- Flexible Flow shop
- Genetic Algorithms

### Página 3 — *DEFINICIÓN: flow shop*

- Cuando los trabajos deben pasar por un conjunto de máquinas, todos en el mismo orden (misma ruta)
- Máquinas en serie
- Buffer infinito entre máquinas

> [Diagrama: flechas amarillas en línea: → Maquina 1 → Maquina 2 → Maquina 3 →.]

### Página 4 — Flow Shop

- $Fm||C_{max}$
- No hay bloqueo: Ocurre cuando los productos son muy grandes y bloquean el trabajo en estaciones precedentes (Buffer limitado)
- En algunos casos, el orden de los trabajos en las máquinas puede cambiar.
  - Para $F2||C_{max}$ & $F3||C_{max}$ sí hay óptimos que mantienen la secuencia.

### Página 5 — Flow Shop

- Cálculo de tiempos de terminación para una secuencia $j_1,j_2,\dots,j_n$ dada en un conjunto de m máquinas
- $C_{i,j_1}=\sum_{l=1}^{i}p_{l,j_1}\qquad i=1,\dots,m$
- $C_{1,j_k}=\sum_{l=1}^{k}p_{1,j_l}\qquad k=1,\dots,n$
- $C_{i,j_k}=\max\left(C_{i-1,j_k},\,C_{i,j_{k-1}}\right)+p_{i,j_k},\qquad k=2,\dots,n;\ i=2,\dots,m$

### Página 6 — Regla de Johnson

- Regla óptima para $F2||C_{max}$
- Algoritmo:
  - Organice los trabajos en dos grupos:
    - Grupo 1: Todos los trabajos tal que $p_{1j}<p_{2j}$
    - Grupo 2: Todos los trabajos tal que $p_{1j}>p_{2j}$
    - Si $p_{1j}=p_{2j}$, asigne el trabajo a cualquier grupo.
  - Los trabajos del grupo 1 se programan primero con la regla SPT de $p_{1j}$.
  - Siguen los trabajos del grupo 2 con la regla LPT de $p_{2j}$
  - Los empates se resuelven arbitrariamente.

### Página 7 — Ejemplo

| Job | Work center A | Work center B |
|---|---|---|
| A | 3.2 | 4.2 |
| B | 4.7 | 1.5 |
| C | 2.2 | 5.0 |
| D | 5.8 | 4.0 |
| E | 3.1 | 2.8 |

### Página 8 — Ejemplo

La misma tabla, más:

- GRUPO 1: A , C
- GRUPO 2: B, D, E
- SPT: C -> A
- LPT: D -> E -> B

### Página 9 — Ejemplo

La misma tabla, más:

- GRUPO 1: A , C
- GRUPO 2: B, D, E
- SPT: C -> A -> D -> E -> B

(Es la secuencia completa de Johnson. Cálculo propio de los tiempos, que la diapositiva no muestra:

| Máquina | Trabajo | Inicio | Fin |
|---|---|---|---|
| WC A | C | 0 | 2.2 |
| WC A | A | 2.2 | 5.4 |
| WC A | D | 5.4 | 11.2 |
| WC A | E | 11.2 | 14.3 |
| WC A | B | 14.3 | 19.0 |
| WC B | C | 2.2 | 7.2 |
| WC B | A | 7.2 | 11.4 |
| WC B | D | 11.4 | 15.4 |
| WC B | E | 15.4 | 18.2 |
| WC B | B | 19.0 | 20.5 |

$C_{max}=20.5$.)

### Página 10 — Algoritmo de Johnson: Extensión a 3 máquinas

- Con 3 o más máquinas, el algoritmo de Johnson no puede utilizarse.
- Excepto en algunos casos especiales en que puede adaptarse
- Para $F_3||C_{max}$, cuando la máquina intermedia está dominada (cuando el tiempo de procesamiento más largo de algún trabajo es menor o igual que el tiempo de procesamiento más corto de alguna de las otras dos máquinas)

Recuadro azul:

$$\max\{p_{2,j}\}\le\max\left\{\min_{\forall j}\{p_{1,j}\},\ \min_{\forall j}\{p_{3,j}\}\right\}$$

### Página 11 — Algoritmo de Johnson: Extensión a 3 máquinas

- Entonces, el problema $F3||C_{max}$ se puede transformar en un problema equivalente $F2||C_{max}$
- Los tiempos de proceso equivalentes son:

$$p'_{1,j}=p_{1,j}+p_{2,j}$$
$$p'_{2,j}=p_{2,j}+p_{3,j}$$

### Página 12 — Algoritmo de Johnson: Extensión a 3 máquinas

Idéntica a la página 11.

### Página 13 — Algoritmo de Johnson: Extensión a 3 máquinas

Secuenciación obtenida: (5, 4, 1, 2, 3)

| Trabajo | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $p_{1,j}$ | 4 | 9 | 8 | 6 | 5 |
| $p_{2,j}$ | 6 | 5 | 3 | 3 | 2 |
| $p_{3,j}$ | 8 | 10 | 6 | 7 | 11 |

(Comprobación propia: $\max p_{2,j}=6\le\max(\min p_{1,j}=4,\ \min p_{3,j}=6)=6$. Entonces $p'_1=(10,14,11,9,7)$ y $p'_2=(14,15,9,10,13)$. El grupo 1 queda {1, 2, 4, 5} y en SPT de $p'_1$ es 5, 4, 1, 2. El grupo 2 es {3}. Resulta (5, 4, 1, 2, 3).)

### Página 14 — Algoritmo de Johnson: Extensión a 3 máquinas

La misma tabla y "Secuenciación obtenida: (5, 4, 1, 2, 3)", más un diagrama de Gantt de 3 filas con eje de 0 a 48:

| Máquina | Trabajo | Inicio | Fin |
|---|---|---|---|
| 1 | 5 | 0 | 5 |
| 1 | 4 | 5 | 11 |
| 1 | 1 | 11 | 15 |
| 1 | 2 | 15 | 24 |
| 1 | 3 | 24 | 32 |
| 2 | 5 | 5 | 7 |
| 2 | 4 | 11 | 14 |
| 2 | 1 | 15 | 21 |
| 2 | 2 | 24 | 29 |
| 2 | 3 | 32 | 35 |
| 3 | 5 | 7 | 18 |
| 3 | 4 | 18 | 25 |
| 3 | 1 | 25 | 33 |
| 3 | 2 | 33 | 43 |
| 3 | 3 | 43 | 49 |

(La última barra llega al borde del eje, marcado 48. Con los datos de la tabla termina en 49, que es el $C_{max}$ y también el óptimo por enumeración; cálculo propio.)

### Página 15 — ¿Y para el caso general?

- Programación entera mixta
- Algoritmos heurísticos
- Algoritmos metaheurísticos

### Página 16 — MIP Model: $Fm|prmu|C_{max}$

- Sea $x_{jk}=1$ si el trabajo j está en la posición k en la secuencia.
- Sea $I_{ik}$ el tiempo muerto en la máquina i entre los trabajos de la posición k y k+1.
- Sea $W_{ik}$ el tiempo de espera del trabajo en la posición k entre las máquinas i y i+1.
- Sea $\Delta_{ik}$ la diferencia entre el tiempo en que el trabajo de la posición k+1 inicia en la máquina i+1 y el trabajo en la posición k termina en la máquina i.

### Página 17 — MIP Model: $Fm|prmu|C_{max}$

$$\Delta_{ik}=I_{ik}+p_{i(k+1)}+W_{i,k+1}=W_{ik}+p_{i+1(k)}+I_{i+1,k}$$

> [Diagrama: dos filas de tiempo, "Machine i" y "Machine i+1". En la máquina $i$ están los bloques $p_{i(k)}$ y $p_{i(k+1)}$, separados por el tiempo muerto $I_{ik}$. En la máquina $i+1$ están $p_{i+1(k-1)}$, $p_{i+1(k)}$ y $p_{i+1(k+1)}$. $W_{ik}$ va desde el fin de $p_{i(k)}$ hasta el inicio de $p_{i+1(k)}$. $W_{i,k+1}$ va desde el fin de $p_{i(k+1)}$ hasta el inicio de $p_{i+1(k+1)}$. Una llave $\Delta_{ik}$ cubre desde el fin de $p_{i(k)}$ hasta el inicio de $p_{i+1(k+1)}$. Leyenda: "$W_{ik}>0$ and $I_{i+1,k}=0$". El diagrama muestra que el intervalo $\Delta_{ik}$ se puede recorrer por la máquina $i$ ($I_{ik}+p_{i(k+1)}+W_{i,k+1}$) o por la máquina $i+1$ ($W_{ik}+p_{i+1(k)}+I_{i+1,k}$).]

### Página 18 — MIP Model: $Fm|prmu|C_{max}$

Minimizar el makespan = minimizar el tiempo muerto de la última máquina.

$$\sum_{i=1}^{m-1}p_{i(1)}+\sum_{j=1}^{n-1}I_{mj}$$

### Página 19 — MIP Model: $Fm|prmu|C_{max}$

Usando la identidad

$$p_{i(k)}=\sum_{j=1}^{n}x_{jk}\,p_{ij}$$

### Página 20 — MIP Model: $Fm|prmu|C_{max}$

Sujeto a:

$$I_{ik}+\sum_{j=1}^{n}x_{j,k+1}\,p_{ij}+W_{i,k+1}-W_{ik}-\sum_{j=1}^{n}x_{jk}\,p_{i+1,j}-I_{i+1,k}=0\qquad\forall k=1,\dots,n-1;\ i=1,\dots,m-1$$

$$W_{i1}=0\qquad\forall i=1,\dots,m-1$$

$$I_{1k}=0\qquad\forall k=1,\dots,n-1$$

### Página 21 — MIP Model: $Fm|prmu|C_{max}$

Min

$$\sum_{i=1}^{m-1}\sum_{j=1}^{n}x_{jk}\,p_{ij}+\sum_{j=1}^{n-1}I_{mj}$$

Sujeto a:

$$\sum_{j=1}^{n}x_{jk}=1\qquad\forall k=1,\dots,n$$
$$\sum_{k=1}^{n}x_{jk}=1\qquad\forall j=1,\dots,n$$
$$I_{ik}+\sum_{j=1}^{n}x_{jk}\,p_{ij}+W_{i,k+1}=W_{ik}+p_{i+1(k)}+I_{i+1,k}$$

(Así está en la diapositiva. Por las pp. 18-20, en la función objetivo debería ir $x_{j1}$ y en la última restricción $x_{j,k+1}$.)

### Página 22 — Implementación en GAMS

- Ver ejemplo de GAMS
- Guéret, C, Prins, C, and Sevaux, M, Applications of Optimization with Xpress-MP, Translated and revised by Susanne Heipcke. Dash Optimization, 2002.
- Permutation flow shop: no se permiten cambios en la secuencia

### Página 23 — GAMS

> [Imagen: captura del IDE de GAMS (gamside) con el proyecto `gmsproj.gpr` y el archivo `flowshop.gms` abierto, con las pestañas `flowshop.gms` y `flowshop.lst`. Barra de estado "20: 38 Insert".]

Código visible (primera parte):

```gams
Sets i item / i1*i6 /
     m machine / bending, soldering, assembly /;

$set lastrank    i6
$set lastmachine assembly

table proctime(m,i)
           i1   i2   i3   i4   i5   i6
bending     3    6    3    5    5    7
soldering   5    4    2    4    4    5
assembly    5    2    4    6    3    6;

alias (i,k);

Variables
    rank(i,k)         item i has position k
    start(m,k)        start time for job in position k on m
    comp(m,k)         completion time for job in postion k on m
    totwait           time before first job + times between jobs on last machine;

Binary variables rank
Positive variables start, comp;

equations
  oneInPosition(k)    Every position gets a jobs
  oneRankPer(i)       Every job is assigned a rank
  onmachrel(m,k)      Relations between the end of job rank k on machine m and start of job rank k on machine m+1
  permachrel(m,k)     Relations between the end of job rank k on machine m and start of job rank k+1 on machine m
  defcomp(m,k)        Calculation of completetion time based on start time and proctime
  defobj              completion time of job rank last;
```

Datos del ejemplo: 6 ítems (i1-i6) y 3 máquinas en serie (bending, soldering, assembly):

| Máquina | i1 | i2 | i3 | i4 | i5 | i6 |
|---|---|---|---|---|---|---|
| bending | 3 | 6 | 3 | 5 | 5 | 7 |
| soldering | 5 | 4 | 2 | 4 | 4 | 5 |
| assembly | 5 | 2 | 4 | 6 | 3 | 6 |

### Página 24 — Decisiones (continuación del código GAMS)

> [Imagen: la misma ventana de gamside, desplazada hacia abajo. La captura tapa el título de la diapositiva ("Decisiones").]

```gams
Binary variables rank
Positive variables start, comp;

equations
  oneInPosition(k)    Every position gets a jobs
  oneRankPer(i)       Every job is assigned a rank
  onmachrel(m,k)      Relations between the end of job rank k on machine m and start of job rank k on machine m+1
  permachrel(m,k)     Relations between the end of job rank k on machine m and start of job rank k+1 on machine m
  defcomp(m,k)        Calculation of completetion time based on start time and proctime
  defobj              completion time of job rank last;

oneInPosition(k)..  sum(i, rank(i,k)) =e= 1;

oneRankPer(i)..     sum(k, rank(i,k)) =e= 1;

onmachrel(m,k+1)..  start(m,k+1) =g= comp(m,k);

permachrel(m+1,k).. start(m+1,k) =g= comp(m,k);

defcomp(m,k)..      comp(m,k) =e= start(m,k) + sum(i, proctime(m,i)*rank(i,k));

defobj..            totwait =g= comp('%lastmachine%','%lastrank%');

model sequence /all/;
option optcr=0;
solve sequence using mip min totwait;

* Maybe the following is better info to output
parameter startjob(m,i);
startjob(m,i) = sum(k$(rank.l(i,k)>0.5), start.l(m,k));
option startjob:0:1:1; display startjob, totwait.l;
```

Qué hace el modelo (explicación): `rank(i,k)` es la variable binaria de posición ($x_{jk}$). `oneInPosition` y `oneRankPer` son las restricciones de asignación. `defcomp` calcula el fin como inicio más el tiempo del trabajo que ocupa la posición. Las dos restricciones de precedencia exigen que una posición empiece después de que la anterior termine en la misma máquina y que una máquina empiece una posición después de que la máquina previa la termine. `defobj` minimiza el fin de la última posición en la última máquina, es decir, el makespan. Se resuelve como MIP con `optcr=0` (óptimo exacto) y se muestra el inicio de cada ítem en cada máquina. La diapositiva no muestra el resultado.

### Página 25 — Problema $Fm||C_{max}$, m>2: Heurísticos

- Un heurístico directo es forzar el problema para que se vea como uno de 2 máquinas y usar el algoritmo de Johnson.
- El problema está en hallar las dos máquinas equivalentes y los tiempos de los trabajos.

### Página 26 — Problema $Fm||C_{max}$, m>2: Heurístico CDS

- Capmbell, Dudek y Smith (1970)
  - El uso del algoritmo de Johnson para convertir un problema de tres máquinas en uno de dos máquinas, aún sin cumplir el criterio de optimalidad, brinda buenas soluciones como método de programación.

CDS utiliza el anterior resultado, es decir convierte un problema de n trabajos con m máquinas en (m-1) sub-problemas y se selecciona el mejor programa entre éstos.

### Página 27 — Problema $Fm||C_{max}$, m>2: Heurístico CDS

Recuadro azul:

$$p'^{(k)}_{1,j}=\sum_{i=1}^{k}p_{i,j}\qquad p'^{(k)}_{2,j}=\sum_{i=m-k+1}^{m}p_{i,j}\qquad\forall k\in\{1,\dots,m-1\}$$

De acuerdo con el experimento realizado por Dannenbring (1977), el algoritmo encontró soluciones óptimas para el 55% de un conjunto de 1.580 problemas.

### Página 28 — $Fm||C_{max}$, m>2: Ejercicio CDS

- Resolver por el método CDS

| Trabajo | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Máq. 1 | 1 | 10 | 17 | 12 | 11 |
| Máq. 2 | 13 | 12 | 9 | 17 | 3 |
| Máq. 3 | 6 | 18 | 13 | 2 | 5 |
| Máq. 4 | 2 | 18 | 4 | 6 | 16 |

### Página 29 — $Fm||C_{max}$, m>2: Ejercicio CDS

Tres tablas, una por iteración. La fila $[j]$ es la posición del trabajo $j$ en la secuencia de Johnson. Unas flechas señalan cómo se forman los tiempos ficticios: en $k=2$, $p_{11}+p_{21}=14$ y $p_{31}+p_{41}=8$ (encerrados en círculo); en $k=3$, $p_{11}+p_{21}+p_{31}=20$ y $p_{21}+p_{31}+p_{41}=21$.

**Iteración $k=1$** ($p'_1$ = máq. 1; $p'_2$ = máq. 4):

| j | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $p'_1$ | 1 | 10 | 17 | 12 | 11 |
| $p'_2$ | 2 | 18 | 4 | 6 | 16 |
| $[j]$ | 1 | 2 | 5 | 4 | 3 |

Secuencia 1, 2, 5, 4, 3 · $C_{max}=88$

**Iteración $k=2$** ($p'_1$ = máq. 1 + 2; $p'_2$ = máq. 3 + 4):

| j | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $p'_1$ | 14 | 22 | 26 | 29 | 14 |
| $p'_2$ | 8 | 36 | 17 | 8 | 21 |
| $[j]$ | 4 | 2 | 3 | 5 | 1 |

Secuencia 5, 2, 3, 1, 4 · $C_{max}=85$

**Iteración $k=3$** ($p'_1$ = máq. 1 + 2 + 3; $p'_2$ = máq. 2 + 3 + 4):

| j | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $p'_1$ | 20 | 40 | 39 | 31 | 19 |
| $p'_2$ | 21 | 48 | 26 | 25 | 24 |
| $[j]$ | 2 | 3 | 4 | 5 | 1 |

Secuencia 5, 1, 2, 3, 4 · $C_{max}=85$

Texto azul "Mejores secuencias", con flechas a 5,2,3,1,4 y 5,1,2,3,4.

(Gantt de la mejor secuencia 5-2-3-1-4, cálculo propio con la recursión de la p. 5:

| Máquina | Trabajo | Inicio | Fin |
|---|---|---|---|
| 1 | 5 | 0 | 11 |
| 1 | 2 | 11 | 21 |
| 1 | 3 | 21 | 38 |
| 1 | 1 | 38 | 39 |
| 1 | 4 | 39 | 51 |
| 2 | 5 | 11 | 14 |
| 2 | 2 | 21 | 33 |
| 2 | 3 | 38 | 47 |
| 2 | 1 | 47 | 60 |
| 2 | 4 | 60 | 77 |
| 3 | 5 | 14 | 19 |
| 3 | 2 | 33 | 51 |
| 3 | 3 | 51 | 64 |
| 3 | 1 | 64 | 70 |
| 3 | 4 | 77 | 79 |
| 4 | 5 | 19 | 35 |
| 4 | 2 | 51 | 69 |
| 4 | 3 | 69 | 73 |
| 4 | 1 | 73 | 75 |
| 4 | 4 | 79 | 85 |

$C_{max}=85$.)

### Página 30 — $Fm||C_{max}$, m>2: Algoritmo NEH

- Heurística de Inserción
- Nawaz, Enscore, Ham son los autores... por eso el nombre
- M. Nawaz, E. Enscore Jr. and I. Ham, A heuristic algorithm for the m- machine, n-job flow-shop sequencing problem, Omega, the International Journal of Management Science 11 (1983), pp. 91–95.
- Considerada una de las mejores heurísticas para el *Fm//Cmax*

### Página 31 — $Fm||C_{max}$, m>2: Algoritmo NEH

- *Paso 1:* Ordenar de los trabajos en orden no creciente de acuerdo a la suma de los tiempos totales de procesamiento en las máquinas
- *Paso 2:* Tomar los dos primeros trabajos y programarlos (F.O. minimizar el makespan parcial) como si sólo se tuvieran esos 2 trabajos
- *Paso 3:* Para k=3 hasta n, hacer el paso 4
- *Paso 4:* Insertar el *k-ésimo* trabajo en la posición que minimice el makespan parcial entre las k posibles posiciones.

$$\text{Número total de secuencias}=\frac{n(n+1)}{2}-1$$

### Página 32 — $Fm||C_{max}$, m>2: Ejercicio NEH

- Resolver por el método NEH

Misma tabla de la página 28.

### Página 33 — $Fm||C_{max}$, m>2: Ejercicio NEH

- Paso 1: Ordenar por LPT de acuerdo a la suma de tiempos totales

| Trabajo | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Maq.1 | 1 | 10 | 17 | 12 | 11 |
| Maq.2 | 13 | 12 | 9 | 17 | 3 |
| Maq.3 | 6 | 18 | 13 | 2 | 5 |
| Maq.4 | 2 | 18 | 4 | 6 | 16 |
| **Suma** | 22 | 58 | 43 | 37 | 35 |

Orden: J2 – J3 – J4 – J5 – J1

### Página 34 — $Fm||C_{max}$, m>2: Ejercicio NEH

- Paso 2: Probar con J2 y J3 y mirar con cuál programa J2 – J3 ó J3 – J2 se logra el mejor Cmax
  - Secuencia J2 – J3 Cmax = 62
  - Secuencia J3 – J2 Cmax = 75
- ✓ Escoger J2 – J3

### Página 35 — $Fm||C_{max}$, m>2: Ejercicio NEH

- Paso 3: Insertar trabajos:
  - Insertar J4 y evaluar las secuencias:
    - J4-J2-J3 Cmax = 81
    - J2-J4-J3 Cmax = 68
    - **J2-J3-J4 Cmax = 68** (en naranja: elegida)
  - Insertar J5:
    - **J5-J2-J3-J4 Cmax = 79** (en naranja: elegida)
    - J2-J5-J3-J4 Cmax = 84
    - J2-J3-J5-J4 Cmax = 84
    - J2-J3-J4-J5 Cmax = 84

### Página 36 — $Fm||C_{max}$, m>2: Ejercicio NEH

- Paso 3: Insertar trabajos:
  - Insertar J1 y evaluar las secuencias:
    - **J1-J5-J2-J3-J4 Cmax = 80** (en naranja: elegida)
    - J5-J1-J2-J3-J4 Cmax = 85
    - J5-J2-J1-J3-J4 Cmax = 81
    - J5-J2-J3-J1-J4 Cmax = 85
    - J5-J2-J3-J4-J1 Cmax = 88

Diagrama de Gantt de la secuencia final J1-J5-J2-J3-J4 (4 filas, eje de 0 a 80 con marcas cada 5):

| Máquina | Trabajo | Inicio | Fin |
|---|---|---|---|
| 1 | 1 | 0 | 1 |
| 1 | 5 | 1 | 12 |
| 1 | 2 | 12 | 22 |
| 1 | 3 | 22 | 39 |
| 1 | 4 | 39 | 51 |
| 2 | 1 | 1 | 14 |
| 2 | 5 | 14 | 17 |
| 2 | 2 | 22 | 34 |
| 2 | 3 | 39 | 48 |
| 2 | 4 | 51 | 68 |
| 3 | 1 | 14 | 20 |
| 3 | 5 | 20 | 25 |
| 3 | 2 | 34 | 52 |
| 3 | 3 | 52 | 65 |
| 3 | 4 | 68 | 70 |
| 4 | 1 | 20 | 22 |
| 4 | 5 | 25 | 41 |
| 4 | 2 | 52 | 70 |
| 4 | 3 | 70 | 74 |
| 4 | 4 | 74 | 80 |

$C_{max}=80$. (Verificado con la recursión de la p. 5. NEH mejora a CDS, que dio 85.)

### Página 37 — Flexible Flow Shop

- Cada estación tiene máquinas en paralelo
- Cada trabajo se procesa en máximo una máquina
- También llamado híbrido, compuesto, o multiprocesadores
- NP-Hard.
- Ver regla LPT / SPT (heurística)

> [Diagrama: flechas amarillas → estación 1 (Maquina 1A arriba, Maquina 1B abajo) → Maquina 2 → estación 3 (Maquina 3A, Maquina 3B, Maquina 3C apiladas) →.]

### Página 38 — Flowshop flexible: $FF_c/\beta/\gamma$

- Cada estación tiene máquinas en paralelo (pueden ser idénticas o no)
- Cada trabajo se procesa en máximo una máquina
- También llamado híbrido, compuesto, o multiprocesadores
- NP-Hard. Dos problemas: asignación y secuenciación
- Difícil de solucionar a optimalidad

> [Diagrama: cuatro columnas de máquinas. Estación 1: m1, m2, m3 (verde). Estación 2: m1, m2, m3, m4 (azul). Estación 3: m1, m2 (gris). Estación 4: m1, m2, m3 (magenta). Unas flechas dibujan la ruta de un trabajo: entra → estación 1 m3 → estación 2 m2 → estación 3 m1 → estación 4 m1. En cada estación el trabajo usa una sola máquina.]

### Página 39 — Flowshop flexible: $FF_c/\beta/\gamma$

> [Diagrama: ejemplo de planta en cuatro etapas, con encabezados "Fabricación Bases", "Fabricación Mixes: Bases más colorantes", "Proceso Enfriamiento" y "Línia de Envasado" (recuadro punteado). Hay dos bloques iguales separados por puntos verticales, que indican que se repiten. Bloque superior: una BASE alimenta 3 tanques de mezcla; cada mezcla va a un FREEZER (3 en total). Dos freezers alimentan una Llenadora y el tercero otra Llenadora. Cada llenadora pasa a un Túnel Congelación y a una Envolvedora. Bloque inferior: BASE → 3 mezclas → 3 FREEZER → una sola Llenadora → Túnel Congelación → Envolvedora. Por los nombres parece una planta de helados (deducido).]

### Página 40 — Reglas de prioridad

- La forma más sencilla de programar
- Se ordenan los trabajos de acuerdo con alguna regla de prioridad
- Algoritmo de lista en la primera estación de acuerdo a la regla elegida
- En las demás se emplea el algoritmo de lista con la regla FIFO
- ¿Garantiza el óptimo? No, pero soluciona el problema

### Página 41 — Ejemplo

> [Diagrama: arriba, barra "Trabajos" con bloques 1 a 5 de longitudes decrecientes (lista LPT). Abajo, "Diagrama de Gantt (2 máquinas)" con dos estaciones de dos máquinas cada una, sin eje numérico. Estación 1: Máquina 11 procesa 1 y 4; Máquina 12 procesa 2, 3 y 5. Estación 2: Máquina 21 procesa 2 y 3; Máquina 22 procesa 1, 4 y 5. En la estación 2 los trabajos entran en el orden en que salen de la estación 1 (FIFO).]

La diapositiva no tiene escala. Posiciones medidas en el dibujo (píxeles / 10, desde el inicio del Gantt), solo como referencia:

| Estación | Máquina | Trabajo | Inicio (aprox.) | Fin (aprox.) |
|---|---|---|---|---|
| 1 | 11 | 1 | 0 | 21.5 |
| 1 | 11 | 4 | 21.5 | 32.6 |
| 1 | 12 | 2 | 0 | 17.5 |
| 1 | 12 | 3 | 17.5 | 31.0 |
| 1 | 12 | 5 | 31.0 | 39.0 |
| 2 | 21 | 2 | 17.3 | 28.4 |
| 2 | 21 | 3 | 30.7 | 51.3 |
| 2 | 22 | 1 | 21.3 | 34.7 |
| 2 | 22 | 4 | 34.7 | 45.8 |
| 2 | 22 | 5 | 45.8 | 57.6 |

### Página 42 — Separador: Genetic Algorithms

"Gestión de Operaciones II" · "GENETIC ALGORITMS" (subrayado).

> [Imagen decorativa: foto del campus y logo de la Universidad de La Sabana.]

### Página 43 — Algoritmos Genéticos

- Provienen de la familia de modelo computacional basado en la evolución
- Introducidos por Holland en 1975
- Proveen una solución potencial a un problema específico en una estructura tipo **cromosoma** y aplican operadores de recombinación para preservar la información crítica
- Cualquier modelo basado en población que usa **selección y recombinación** para generar nuevos elementos en el espacio de búsqueda

### Página 44 — Conceptos Básicos

- Población
  - Conjunto de soluciones potenciales, donde la población inicial puede ser elegida randómicamente
  - Cambia con el tiempo pero su tamaño se mantiene
- Individuo
  - Elemento de la población
  - Cada individuo es representado por una cadena de caracteres

### Página 45 — Conceptos básicos

- Crossover
  - Dos nuevos individuos pueden ser obtenidos de dos padres en el mating pool, recombinando a ambos padres
- Mutación
  - Individuos en el mating pool también pueden cambiar a través de mutación randómica OJO
- Resultado -> Un nueva generación
  - El proceso se repite y converge a una población con individuos muy similares entre sí

> [Imagen decorativa: máscara de un monstruo, alusiva a la mutación.]

### Página 46 — Conceptos básicos

Idéntica a la página 45.

### Página 47 — Conceptos Básicos

- Fitness: Función de evaluación de la calidad de una solución. Qué tan adaptado es un individuo al medio. Ejemplos: Makespan, Tardanza máxima, Makespan + diversidad. Fi / F
- Población inicial: Conjunto de soluciones que dan inicio al algoritmo. Por lo general se eligen de forma aleatoria
- **Selección:** Forma de elegir a los individuos que pasarán de una generación a otra. Estrategias Elitistas, por ejemplo.

### Página 48 — Ejemplo

- Flow Shop:
  - Representación: Orden como se asignan a las máquinas.

Cromosoma: [1 | 2 | 3 | 4 | 5 | 6 | 7]

> [Diagrama: el mismo *flexible flow shop* de la p. 37: → Maquina 1A / Maquina 1B → Maquina 2 → Maquina 3A / 3B / 3C →.]

### Página 49 — Ejemplo

- Población Inicial: Generada aleatoriamente

| Individuo | Cromosoma |
|---|---|
| 1 | 1 2 3 4 5 6 7 |
| 2 | 5 1 3 4 6 2 7 |
| 3 | 7 2 3 1 5 6 4 |

### Página 50 — Ejemplo

- Cálculo de Fitness: Valor del makespan

| Individuo | Cromosoma (como aparece) | Fitness (makespan) |
|---|---|---|
| 1 | 1 2 3 4 5 6 7 | 45 |
| 2 | 5 1 3 4 5 2 7 | 50 |
| 3 | 7 2 3 1 5 6 4 | 75 |

(El segundo cromosoma tiene el 5 repetido y le falta el 6; en la p. 49 era 5 1 3 4 6 2 7.)

### Página 51 — Ejemplo

- Crossover: cruce 1 punto

| | Cromosoma | Fitness |
|---|---|---|
| Padre 1 | 1 2 3 \| **4 5 6 7** (recuadro rojo en 4 5 6 7) | 45 |
| Padre 2 | **5 1 3** \| 4 6 2 7 (recuadro rojo en 5 1 3) | 50 |
| Hijo | 5 1 3 4 **5 (2)** 6 7 | — |

El hijo toma los tres primeros genes del padre 2 (5 1 3) y los cuatro últimos del padre 1 (4 5 6 7). El 5 queda repetido (en rojo), así que se reemplaza por el gen que falta, el 2 (anotado entre paréntesis). El hijo reparado es 5 1 3 4 2 6 7.

### Página 52 — Ejemplo

- Mutación: Debe ser con baja probabilidad

5 1 3 4 2 6 7 → (flecha) → 5 **6** 3 4 2 **1** 7

(Los genes en rojo son las posiciones 2 y 6, que intercambian el 1 y el 6: mutación por intercambio.)

### Página 53 — Ejemplo

- Selección de una nueva generación

| Población actual | Fitness | → | Nueva generación |
|---|---|---|---|
| 1 2 3 4 5 6 7 | 45 | | 1 2 3 4 5 6 7 |
| 5 1 3 4 5 2 7 | 50 | | 5 1 3 4 5 2 7 |
| 7 2 3 1 5 6 4 | 75 | | (eliminado) |
| 5 **7** 3 4 2 **1** 7 | 46 | | 5 **7** 3 4 2 **1** 7 |

Repetir hasta que se cumpla algún criterio (en rojo).

(La selección conserva los tres mejores (45, 46 y 50) y descarta el de 75: es elitista. El mutado aparece como 5 7 3 4 2 1 7, distinto del 5 6 3 4 2 1 7 de la p. 52.)

### Página 54 — Algoritmo

```
Repetir
    para cada individuo i evaluar y calcular fitness f(i)
    Crear mating pool de tamaño N basado en los valores de fitness f(i)
    para i=1 hasta (N/2)
        quitar pares de individuos {j,k} del mating pool
        recombinar usando los individuos j y k
        aplicar mutación
Hasta 'condición de parada'
```

(Las palabras evaluar, fitness f(i), mating pool, quitar, recombinar y mutación están resaltadas en dorado.)

### Página 55 — Consideraciones

- Diferentes implementaciones. Idea básica: nuevas buenas soluciones pueden ser obtenidas a partir de bloques de soluciones existentes
- El tiempo de corrida va a depender de los parámetros con gran probabilidad de que si se deja correr por un buen tiempo se obtenga una solución óptima o casi óptima
- Trabajan sobre toda una población otorgando mayor paralelismo
- Pueden trabajar sobre un problema sin conocer los detalles del mismo con demasiada exactitud

### Página 56 — ¡Gracias!

William Guerrero, Ph.D.


---

<!-- fuente: corte-3-programacion-scheduling/04-flow-shop/flowshop-scheduling.md -->
# flowshop-scheduling

> **Archivo:** [`flowshop-scheduling.xlsx`](/corte-3-programacion-scheduling/04-flow-shop/flowshop-scheduling.xlsx) · **Corte 3** · Libro de Excel con 4 hoja(s): `Regla de Johnson`, `Campbell `, `CDS`, `NEH`  
> **Nombre original:** `CORTE 3/Flowshop Schedulling .xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Libro de Excel de clase para el tema **flow shop** ([L19](/corte-3-programacion-scheduling/04-flow-shop/L19-flow-shop-scheduling.md)). Resuelve a mano, con fórmulas, los métodos para minimizar el makespan en un taller en serie:

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
- El [compendio](/corte-3-programacion-scheduling/00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md) (hojas 09-11) rehace este libro con `VLOOKUP` y cita como fuente "Clase_3_11_2026.xlsx". Por los datos, es este mismo archivo (deducido).
