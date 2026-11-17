# L19-flow-shop-scheduling

> **Archivo:** [`L19-flow-shop-scheduling.pdf`](./L19-flow-shop-scheduling.pdf) · **Corte 3** · 56 páginas  
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

- [flowshop-scheduling.md](./flowshop-scheduling.md): Excel de clase con Johnson para 2 y 3 máquinas, la hoja `Campbell ` (el ejercicio CDS de la p. 28, incompleto), y CDS y NEH con otro caso de 5 trabajos y 5 máquinas.
- [metodos-programacion-produccion-corte3.md](../00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md): hojas `09_FlowShop_Johnson`, `10_FlowShop_CDS` y `11_FlowShop_NEH`.
- Las máquinas paralelas, que son cada estación de un *flexible flow shop*: [L18](../03-maquinas-paralelas/L18-parallel-machine-scheduling.md).
- Job shop y flexible job shop: [05-job-shop](../05-job-shop/job-shop-y-flexible-job-shop.md).
- Modelos de GAMS de otro tema (planeación agregada): [modelo-flujo-gams](../../corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/).

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

## Anexo: texto extraído automáticamente del PDF

> Texto plano tal como sale del PDF, sin fórmulas ni tablas que estén como imagen. La versión fiel y completa es la sección «Contenido completo» de arriba.

### Página 1 · 2 imagen(es)

Planeación de Operaciones
FLOW SHOPS &
FLEXIBLE FLOW SHOPS
2026

### Página 2 · 1 imagen(es)

Agenda
• Flow Shop
• Algoritmo de Johnson
• Implementación en GAMS
• Flexible Flow shop
• Genetic Algorithms

### Página 3 · 1 imagen(es)

DEFINICIÓN: flow shop
• Cuando los trabajos deben pasar por un 
conjunto de máquinas, todos en el mismo 
orden (misma ruta)
• Máquinas en serie
• Buffer infinito entre máquinas
Maquina 1
Maquina 2
Maquina 3

### Página 4 · 1 imagen(es)

Flow Shop
• 𝐹𝑚||𝐶𝑚𝑎𝑥
• No hay bloqueo: Ocurre cuando los 
productos son muy grandes y bloquean el 
trabajo en estaciones precedentes (Buffer 
limitado)
• En algunos casos, el orden de los trabajos 
en las máquinas puede cambiar. 
– Para 𝐹2||𝐶𝑚𝑎𝑥 & 𝐹3||𝐶𝑚𝑎𝑥 si hay óptimos que 
mantienen la secuencia.

### Página 5 · 1 imagen(es)

Flow Shop
• Cálculo de tiempos de terminación para una 
secuencia 𝑗1, 𝑗2, … 𝑗𝑛 dada en un conjunto de 
m máquinas
• 𝐶𝑖,𝑗1 = σ𝑙=1
𝑖
𝑝𝑙,𝑗1 
𝑖= 1, … , 𝑚
• 𝐶1,𝑗𝑘= σ𝑙=1
𝑘
𝑝1,𝑗𝑙 
𝑘= 1, … , 𝑛
• 𝐶𝑖,𝑗𝑘= max 𝐶𝑖−1,𝑗𝑘, 𝐶𝑖,𝑗𝑘−1 + 𝑝𝑖,𝑗𝑘, 
𝑘= 2, … , 𝑛; 𝑖= 2, … 𝑚

### Página 6 · 1 imagen(es)

Regla de Johnson
• Regla óptima para 𝐹2||𝐶𝑚𝑎𝑥
• Algoritmo:
– Organice los trabajos en dos grupos:
• Grupo 1: Todos los trabajos tal que 𝑝1𝑗< 𝑝2𝑗
• Grupo 2: Todos los trabajos tal que 𝑝1𝑗> 𝑝2𝑗
• Si 𝑝1𝑗= 𝑝2𝑗, asigne el trabajo a cualquier grupo.
– Los trabajos del grupo 1 se programan primero con la 
regla SPT de 𝑝1𝑗.
– Siguen los trabajos del grupo 2 con la regla LPT de 𝑝2𝑗
– Los empates se resuelven arbitrariamente.

### Página 7 · 1 imagen(es)

Ejemplo
Job
Work center A
Work center B
A
3.2
4.2
B
4.7
1.5
C
2.2
5.0
D
5.8
4.0
E
3.1
2.8

### Página 8 · 1 imagen(es)

Ejemplo
Job
Work center A
Work center B
A
3.2
4.2
B
4.7
1.5
C
2.2
5.0
D
5.8
4.0
E
3.1
2.8
GRUPO 1: A , C
GRUPO 2: B, D, E
SPT: C -> A 
LPT: D -> E -> B

### Página 9 · 1 imagen(es)

Ejemplo
Job
Work center A
Work center B
A
3.2
4.2
B
4.7
1.5
C
2.2
5.0
D
5.8
4.0
E
3.1
2.8
GRUPO 1: A , C
GRUPO 2: B, D, E
SPT: C -> A -> D -> E -> B

### Página 10 · 2 imagen(es)

Algoritmo de Johnson: Extensión a 3 
máquinas
• Con 3 o más máquinas, el algoritmo de Johnson no puede 
utilizarse. 
• Excepto en algunos casos especiales en que puede 
adaptarse 
• Para F3||Cmax, cuando la máquina intermedia está 
dominada ( Cuando el tiempo de procesamiento más largo 
de algún trabajo es menor o igual que el tiempo de 
procesamiento más corto de alguna de las otras dos 
máquinas )

### Página 11 · 3 imagen(es)

Algoritmo de Johnson: Extensión a 3 
máquinas
• Entonces, el problema F3 | | Cmax se puede transformar en 
un problema equivalente F2 | | Cmax 
• Los tiempos de proceso equivalentes son:

### Página 12 · 3 imagen(es)

Algoritmo de Johnson: Extensión a 3 
máquinas
• Entonces, el problema F3 | | Cmax se puede transformar en 
un problema equivalente F2 | | Cmax 
• Los tiempos de proceso equivalentes son:

### Página 13 · 1 imagen(es)

Algoritmo de Johnson: Extensión a 3 
máquinas
Secuenciación obtenida : ( 5, 4, 1, 2, 3 ) 
Trabajo
1
2
3
4
5
p1,j
4
9
8
6
5
p2,j
6
5
3
3
2
p3,j
8
10
6
7
11

### Página 14 · 2 imagen(es)

Algoritmo de Johnson: Extensión a 3 
máquinas
Secuenciación obtenida : ( 5, 4, 1, 2, 3 ) 
Trabajo
1
2
3
4
5
p1,j
4
9
8
6
5
p2,j
6
5
3
3
2
p3,j
8
10
6
7
11

### Página 15 · 1 imagen(es)

¿Y para el caso general?
• Programación entera mixta 
• Algoritmos heurísticos 
• Algoritmos metaheurísticos

### Página 16 · 1 imagen(es)

MIP Model: 𝐹𝑚𝑝𝑟𝑚𝑢𝐶𝑚𝑎𝑥
• Sea 𝑥𝑗𝑘= 1 si el trabajo j está en la posición k en la 
secuencia.
• Sea 𝐼𝑖𝑘 el tiempo muerto en la máquina i entre los 
trabajos de la posición k y k+1.
• Sea 𝑊𝑖𝑘 el tiempo de espera del trabajo en la 
posición k entre las máquinas i y i+1.
• Sea Δ𝑖𝑘 la diferencia entre el tiempo en que el 
trabajo de la posición k+1 inicia en la máquina i+1 y 
el trabajo en la posición k termina en la máquina i.

### Página 17 · 2 imagen(es)

MIP Model: 𝐹𝑚𝑝𝑟𝑚𝑢𝐶𝑚𝑎𝑥
Δ𝑖𝑘= 𝐼𝑖𝑘+ 𝑝𝑖(𝑘+1) + 𝑊𝑖,𝑘+1 = 𝑊𝑖𝑘+ 𝑝𝑖+1(𝑘) + 𝐼𝑖+1,𝑘

### Página 18 · 1 imagen(es)

MIP Model: 𝐹𝑚𝑝𝑟𝑚𝑢𝐶𝑚𝑎𝑥
Minimizar el makespan = minimizar el tiempo muerto 
de la última máquina.
෍
𝑖=1
𝑚−1
𝑝𝑖(1) + ෍
𝑗=1
𝑛−1
𝐼𝑚𝑗

### Página 19 · 1 imagen(es)

MIP Model: 𝐹𝑚𝑝𝑟𝑚𝑢𝐶𝑚𝑎𝑥
Usando la identidad
𝑝𝑖𝑘= ෍
𝑗=1
𝑛
𝑥𝑗𝑘𝑝𝑖𝑗

### Página 20 · 1 imagen(es)

MIP Model: 𝐹𝑚𝑝𝑟𝑚𝑢𝐶𝑚𝑎𝑥
Sujeto a:
𝐼𝑖𝑘+ ෍
𝑗=1
𝑛
𝑥𝑗𝑘+1𝑝𝑖𝑗+ 𝑊𝑖,𝑘+1 −𝑊𝑖𝑘−෍
𝑗=1
𝑛
𝑥𝑗𝑘𝑝𝑖+1𝑗−𝐼𝑖+1,𝑘= 0 
∀ 𝑘= 1, … , 𝑛−1; 𝑖= 1, … . , 𝑚−1
𝑊𝑖1 = 0 ∀ 𝑖= 1, … , 𝑚−1
𝐼1𝑘= 0 ∀ 𝑘= 1, … , 𝑛−1

### Página 21 · 1 imagen(es)

MIP Model: 𝐹𝑚𝑝𝑟𝑚𝑢𝐶𝑚𝑎𝑥
Min
෍
𝑖=1
𝑚−1
෍
𝑗=1
𝑛
𝑥𝑗𝑘𝑝𝑖𝑗+ ෍
𝑗=1
𝑛−1
𝐼𝑚𝑗
Sujeto a:
෍
𝑗=1
𝑛
𝑥𝑗𝑘= 1 ∀ 𝑘= 1, … , 𝑛
෍
𝑘=1
𝑛
𝑥𝑗𝑘= 1 ∀ 𝑗= 1, … , 𝑛
𝐼𝑖𝑘+ ෍
𝑗=1
𝑛
𝑥𝑗𝑘𝑝𝑖𝑗+ 𝑊𝑖,𝑘+1 = 𝑊𝑖𝑘+ 𝑝𝑖+1(𝑘) + 𝐼𝑖+1,𝑘

### Página 22 · 1 imagen(es)

Implementación en GAMS 
• Ver ejemplo de GAMS
• Guéret, C, Prins, C, and Sevaux, M, 
Applications of Optimization with Xpress-
MP, Translated and revised by Susanne 
Heipcke. Dash Optimization, 2002.
• Permutation flow shop: no se permiten
cambios en la secuencia

### Página 23 · 2 imagen(es)

GAMS

### Página 24 · 2 imagen(es)

Decisiones

### Página 25 · 1 imagen(es)

Problema 𝐹𝑚|| 𝐶𝑚𝑎𝑥, m>2: Heurísticos
• Un heurístico directo es forzar el problema para 
que se vea como uno de 2 máquinas y usar el 
algoritmo de Johnson. 
• El problema está en hallar las dos máquinas 
equivalentes y los tiempos de los trabajos.

### Página 26 · 1 imagen(es)

Problema 𝐹𝑚|| 𝐶𝑚𝑎𝑥, m>2: 
Heurístico CDS
• Capmbell, Dudek y Smith(1970) 
– El uso del algoritmo de Johnson para convertir un 
problema de tres máquinas en uno de dos máquinas, aún 
sin cumplir el criterio de optimalidad, brinda buenas 
soluciones como método de programación. 
CDS utiliza el anterior resultado, es decir convierte un 
problema de n trabajos con m máquinas en ( m-1 ) sub-
problemas y se selecciona el mejor programa entre éstos.

### Página 27 · 2 imagen(es)

Problema 𝐹𝑚|| 𝐶𝑚𝑎𝑥, m>2: 
Heurístico CDS
De acuerdo con el experimento realizado por 
Dannenbring (1977), el algoritmo encontró 
soluciones óptimas para el 55% de un conjunto de 
1.580 problemas.

### Página 28 · 2 imagen(es)

𝐹𝑚|| 𝐶𝑚𝑎𝑥, m>2: Ejercicio CDS
• Resolver por el método CDS

### Página 29 · 2 imagen(es)

𝐹𝑚|| 𝐶𝑚𝑎𝑥, m>2: Ejercicio CDS

### Página 30 · 1 imagen(es)

𝐹𝑚|| 𝐶𝑚𝑎𝑥, m>2: Algoritmo NEH
• Heurística de Inserción 
• Nawaz, Enscore, Ham son los autores... por eso 
el nombre 
• M. Nawaz, E. Enscore Jr. and I. Ham, A heuristic 
algorithm for the m- machine, n-job flow-shop 
sequencing problem, Omega, the International 
Journal of Management Science 11 (1983), pp. 
91–95. 
• Considerada una de las mejores heurísticas para 
el Fm//Cmax

### Página 31 · 1 imagen(es)

𝐹𝑚|| 𝐶𝑚𝑎𝑥, m>2: Algoritmo NEH
➢
Paso 1: Ordenar de los trabajos en orden no creciente de 
acuerdo a la suma de los tiempos totales de procesamiento en 
las máquinas
➢
Paso 2: Tomar los dos primeros trabajos y programarlos (F.O. 
minimizar el makespan parcial ) como si sólo se tuvieran esos 2 
trabajos 
➢
Paso3: Para k=3 hasta n, hacer el paso4 
➢
Paso 4: Insertar el k-ésimo trabajo en la posición que minimice el 
makespan parcial entre las k posibles posiciones.
Número total de secuencias =𝑛(𝑛+1)
2
−1

### Página 32 · 2 imagen(es)

𝐹𝑚|| 𝐶𝑚𝑎𝑥, m>2: Ejercicio NEH
• Resolver por el método NEH

### Página 33 · 1 imagen(es)

𝐹𝑚|| 𝐶𝑚𝑎𝑥, m>2: Ejercicio NEH
➢Paso 1: Ordenar por LPT de acuerdo a la suma de tiempos totales 
Trabajo
1
2
3
4
5
Maq.1
1
10
17
12
11
Maq.2
13
12
9
17
3
Maq.3
6
18
13
2
5
Maq.4
2
18
4
6
16
Suma
22
58
43
37
35
Orden: J2 – J3 – J4 – J5 – J1

### Página 34 · 1 imagen(es)

𝐹𝑚|| 𝐶𝑚𝑎𝑥, m>2: Ejercicio NEH
➢Paso 2: Probar con J2 y J3 y mirar con cuál programa 
J2 – J3 ó J3 – J2 se logra el mejor Cmax 
• Secuencia J2 – J3 Cmax = 62 
• Secuencia J3 – J2 Cmax = 75 
✓Escoger J2 – J3

### Página 35 · 1 imagen(es)

𝐹𝑚|| 𝐶𝑚𝑎𝑥, m>2: Ejercicio NEH
➢Paso 3: Insertar trabajos: 
- Insertar J4 y evaluar las secuencias: 
J4-J2-J3 Cmax = 81 
J2-J4-J3 Cmax = 68 
J2-J3-J4 Cmax = 68 
- Insertar J5:
J5-J2-J3-J4 Cmax = 79 
J2-J5-J3-J4 Cmax = 84 
J2-J3-J5-J4 Cmax = 84 
J2-J3-J4-J5 Cmax = 84

### Página 36 · 2 imagen(es)

𝐹𝑚|| 𝐶𝑚𝑎𝑥, m>2: Ejercicio NEH
➢Paso 3: Insertar trabajos: 
- Insertar J1 y evaluar las secuencias: 
J1-J5-J2-J3-J4 Cmax = 80 
J5-J1-J2-J3-J4 Cmax = 85 
J5-J2-J1-J3-J4 Cmax = 81 
J5-J2-J3-J1-J4 Cmax = 85 
J5-J2-J3-J4-J1 Cmax = 88

### Página 37 · 1 imagen(es)

Flexible Flow Shop
• Cada estación tiene máquinas en paralelo
• Cada trabajo se procesa en máximo una máquina
• También llamado hibrido, compuesto, o 
multiprocesadores
• NP-Hard.
• Ver regla LPT / SPT (heurística)
Maquina 1B
Maquina 2
Maquina 3C
Maquina 1A
Maquina 3B
Maquina 3A

### Página 38 · 2 imagen(es)

Flowshop flexible: FFc /𝜷/ 𝜸 
• Cada estación tiene 
máquinas en paralelo 
(pueden ser idénticas o no) 
• Cada trabajo se procesa en 
máximo una máquina
• También llamado hibrido, 
compuesto, o 
multiprocesadores
• NP-Hard. Dos problemas: 
asignación y secuenciación
• Dificil de solucionar a 
optimalidad

### Página 39 · 2 imagen(es)

Flowshop flexible: FFc /𝜷/ 𝜸

### Página 40 · 1 imagen(es)

Reglas de prioridad 
• La forma más sencilla de programar 
• Se ordenan los trabajos de acuerdo con alguna regla 
de prioridad 
• Algoritmo de lista en la primera estación de acuerdo a 
la regla elegida 
• En las demás se emplea el algoritmo de lista con la 
regla FIFO 
• ¿Garantiza el óptimo? No, pero soluciona el problema

### Página 41 · 2 imagen(es)

Ejemplo

### Página 42 · 1 imagen(es)

Gestión de Operaciones II
GENETIC ALGORITMS

### Página 43 · 1 imagen(es)

Algoritmos Genéticos
• Provienen de la familia de modelo computacional
basado en la evolución
• Introducidos por Holland en 1975
• Proveen una solución potencial a un problema
específico en una estructura tipo cromosoma y 
aplican operadores de recombinación para 
preservar la información crítica
• Cualquier modelo basado en población que usa
selección y recombinación para generar nuevos
elementos en el espacio de búsqueda

### Página 44 · 1 imagen(es)

Conceptos Básicos
• Población
– Conjunto de soluciones potenciales, donde la 
población inicial puede ser elegida
randómicamente
– Cambia con el tiempo pero su tamaño se 
mantiene
• Individuo
– Elemento de la población
– Cada individuo es representado por una cadena
de caracteres

### Página 45 · 2 imagen(es)

Conceptos básicos
• Crossover
– Dos nuevos individuos pueden ser obtenidos de 
dos padres en el mating pool, recombinando a 
ambos padres
• Mutación
– Individuos en el mating pool también pueden
cambiar a través de mutación randómica OJO 
• Resultado -> Un nueva generación
– El proceso se repite y converge a una población
con individuos muy similares entre si

### Página 46 · 2 imagen(es)

Conceptos básicos
• Crossover
– Dos nuevos individuos pueden ser obtenidos de 
dos padres en el mating pool, recombinando a 
ambos padres
• Mutación
– Individuos en el mating pool también pueden
cambiar a través de mutación randómica OJO 
• Resultado -> Un nueva generación
– El proceso se repite y converge a una población
con individuos muy similares entre si

### Página 47 · 1 imagen(es)

Conceptos Básicos
• Fitness
Función de evaluación de la calidad de una solución. Qué tan adaptado
es un individuo al medio.
Ejemplos: Makespan, Tardanza máxima, Makespan + diversidad. Fi / F
• Población inicial: 
Conjunto de soluciones que dan inicio al algoritmo. Por lo general se 
eligen de forma aleatoria
• Selección:
Forma de elegir a los individuos que pasarán de una generación a otra. 
Estrategias Elitistas, por ejemplo.

### Página 48 · 1 imagen(es)

Ejemplo
• Flow Shop:
– Representación: Orden como se asignan a 
las máquinas.
1
2
3
4
5
6
7
Maquina 1B
Maquina 2
Maquina 3C
Maquina 1A
Maquina 3B
Maquina 3A

### Página 49 · 1 imagen(es)

Ejemplo
• Población Inicial: Generada 
aleatoriamente
1
2
3
4
5
6
7
5
1
3
4
6
2
7
7
2
3
1
5
6
4

### Página 50 · 7 imagen(es)

Ejemplo
• Calculo de Fitness: Valor del makespan
1
2
3
4
5
6
7
5
1
3
4
5
2
7
7
2
3
1
5
6
4
45
50
75

### Página 51 · 5 imagen(es)

Ejemplo
• Crossover: cruce1 punto
1
2
3
4
5
6
7
5
1
3
4
6
2
7
45
50
5
1
3
4
5 (2)
6
7

### Página 52 · 2 imagen(es)

Ejemplo
• Mutación: Debe ser con baja probabilidad 
5
1
3
4
2
6
7
5
6
3
4
2
1
7

### Página 53 · 9 imagen(es)

Ejemplo
• Selección de una nueva generación
5
7
3
4
2
1
7
1
2
3
4
5
6
7
5
1
3
4
5
2
7
7
2
3
1
5
6
4
5
7
3
4
2
1
7
45
50
75
46
1
2
3
4
5
6
7
5
1
3
4
5
2
7
Repetir hasta que se cumpla algún criterio

### Página 54 · 1 imagen(es)

Algoritmo
Repetir
para cada individuo i evaluar y calcular fitness f(i)
Crear mating pool de tamaño N basado en los valores de fitness f(i)
para i=1 hasta (N/2)
quitar pares de individuos {j,k} del mating pool
recombinar usando los individuos j y k
aplicar mutación
Hasta ‘condición de parada’

### Página 55 · 1 imagen(es)

Consideraciones
• Diferentes implementaciones. Idea básica: nuevas buenas
soluciones pueden ser obtenidas a partir de bloques de 
soluciones existentes
• El tiempo de corrida va a depender de los parámetros con 
gran probabilidad de que si se deja correr por un buen tiempo
se obtenga una solución óptima o casi óptima
• Trabajan sobre toda una población otorgando mayor 
paralelismo
• Pueden trabajar sobre un problema sin conocer los detalles
del mismo con demasiada exactitud

### Página 56 · 1 imagen(es)

¡Gracias!
William Guerrero, Ph.D.

