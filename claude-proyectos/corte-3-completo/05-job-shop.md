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

## Contenido completo (página por página)

> **Notación usada en toda la presentación.** Una operación se escribe $(i,j)$: **$i$ = máquina, $j$ = trabajo** (job). $p_{ij}$ = tiempo de proceso del trabajo $j$ en la máquina $i$. $y_{ij}$ = tiempo de inicio de la operación $(i,j)$. $U$ = nodo fuente ficticio y $V$ = nodo sumidero ficticio del grafo (en la página 12 el sumidero se llama $S$).

### Página 1 — JOB SHOPS & FLEXIBLE JOB SHOPS

Portada. Título: **JOB SHOPS & FLEXIBLE JOB SHOPS**. Logo de la Universidad de La Sabana y licencia Creative Commons BY-NC-SA.

> [Imagen decorativa: foto del campus de la Universidad de La Sabana, logo institucional y logo de licencia CC BY-NC-SA]

### Página 2 — Agenda

- Job Shop
- Implementación en GAMS
- Shifting bottleneck heuristic (Cuello de botella móvil)
- Flexible Job shop
- Iterated Local Search

> Nota: aunque la agenda anuncia «Flexible Job shop» e «Iterated Local Search», el PDF **no tiene diapositivas** sobre esos dos temas: después del cuello de botella móvil (págs. 11–30) solo vienen herramientas (pág. 31), un investigador destacado (pág. 32) y el cierre (pág. 33).

### Página 3 — DEFINICIÓN: Job shop

- Cuando los trabajos pasan por un conjunto de máquinas, todos en el diferente orden (ruta)
- Máquinas en serie
- Buffer infinito entre máquinas sin recirculación.
- Min Makespan en este curso

> [Diagrama: tres cajas en fila, «Maquina 1», «Maquina 2» y «Maquina 3». Flechas de colores representan trabajos: A (amarillo), B (rojo) y C (azul). Antes de la Máquina 1 entran A y C; antes de la Máquina 2 entran A y B; antes de la Máquina 3 entran A, C y B; a la derecha de la Máquina 3 sale A. Idea: cada trabajo sigue su propia ruta por las máquinas (A pasa por 1 → 2 → 3; B aparece en 2 y 3; C aparece en 1 y 3), a diferencia del flow shop, donde todos siguen el mismo orden.]

### Página 4 — Job shop: formulación matemática

- Nombre: programación disjuntiva
- Variables de decisión:
  - $y_{ij}$ : tiempo de inicio de la operación $(i,j)$
  - $C_{max}$ : makespan

F.O: min $C_{max}$

### Página 5 — Job shop: formulación matemática

F.O: min $C_{max}$

Sujeto a:

$$y_{kj} - y_{ij} \ge p_{ij} \qquad \forall\, (i,j) \rightarrow (k,j) \in A$$

$$C_{max} - y_{ij} \ge p_{ij} \qquad \forall\, (i,j) \in N$$

$$y_{ij} - y_{il} \ge p_{il} \;\; \text{ó} \;\; y_{il} - y_{ij} \ge p_{ij} \qquad \forall\, (i,l),(i,j) \in B$$

$$y_{ij} \ge 0 \qquad \forall\, (i,j) \in N$$

Significado (los conjuntos se definen en la página 6):

- $N$: conjunto de operaciones (nodos del grafo).
- $A$: arcos conjuntivos (ruta de cada trabajo). $(i,j)\rightarrow(k,j)$ significa que el trabajo $j$ pasa de la máquina $i$ a la máquina $k$; la primera restricción obliga a que la operación siguiente empiece cuando termine la anterior.
- $B$: pares de operaciones de **trabajos distintos** ($j$ y $l$) en la **misma máquina** $i$; la restricción disyuntiva («ó») dice que una de las dos va antes que la otra (no se traslapan).
- La segunda restricción hace que $C_{max}$ sea mayor o igual que el tiempo de terminación de todas las operaciones.

### Página 6 — Job shop

- Representación en un grafo $G = \{N, A, B\}$:
  - Nodos: Representan las operaciones $(i,j)$
  - Arcos de dos tipos:
    - Solidos representan la ruta de los trabajos. Ejemplo $(i,j) \rightarrow (k,j)$ representa que el trabajo $j$ se realiza en la máquina $i$ y luego en $k$.
    - Intermitentes representan dos trabajos diferentes que se procesan en la misma máquina. Son bidireccionales. $\leftrightarrow$
    - Los arcos están asociados a la duración de la tarea del nodo de donde sale.
  - Se incluyen nodos ficticios de origen y destino.
    - El nodo de origen se conecta a los n nodos de los trabajos en su primera operación.

### Página 7 — Job shop: formulación matemática (Ejemplo)

Ejemplo:

| Job | Route | Tiempos de proceso |
|---|---|---|
| 1 | 1,2,3 | p11 = 10, p21=8, p31=4 |
| 2 | 2,1,4,3 | p22=8, p12=3, p42 = 5, p32 = 6 |
| 3 | 1,2,4 | P13=4, p23=7, p43 = 3 |

¿Cómo es el grafo del problema?

¿Cuáles son las restricciones del MIP?

HINT: $y_{21} - y_{11} \ge 10,\; y_{11} - y_{12} \ge 3 \text{ ó } y_{21} - y_{11} \ge 10$

> Observación: en la segunda parte del HINT la alternativa correcta de la disyunción entre $(1,1)$ y $(1,2)$ es $y_{12} - y_{11} \ge 10$ (el trabajo 1 antes que el 2 en la máquina 1); la diapositiva repite $y_{21} - y_{11} \ge 10$, que es la restricción de ruta del trabajo 1. Parece un error de digitación.

**Respuesta completa (deducida a partir de la formulación de la pág. 5; no está escrita en las diapositivas):**

Operaciones $N$: $(1,1),(2,1),(3,1)$; $(2,2),(1,2),(4,2),(3,2)$; $(1,3),(2,3),(4,3)$.

Restricciones de ruta (arcos $A$):

$$y_{21}-y_{11}\ge 10,\quad y_{31}-y_{21}\ge 8$$
$$y_{12}-y_{22}\ge 8,\quad y_{42}-y_{12}\ge 3,\quad y_{32}-y_{42}\ge 5$$
$$y_{23}-y_{13}\ge 4,\quad y_{43}-y_{23}\ge 7$$

Makespan (para todo $(i,j)\in N$; las que mandan son las de las últimas operaciones):

$$C_{max}-y_{31}\ge 4,\quad C_{max}-y_{32}\ge 6,\quad C_{max}-y_{43}\ge 3,\quad C_{max}-y_{11}\ge 10,\ \dots$$

Restricciones disyuntivas (arcos $B$):

| Máquina | Par de trabajos | Disyunción |
|---|---|---|
| 1 | 1 y 2 | $y_{11}-y_{12}\ge 3$ ó $y_{12}-y_{11}\ge 10$ |
| 1 | 1 y 3 | $y_{11}-y_{13}\ge 4$ ó $y_{13}-y_{11}\ge 10$ |
| 1 | 2 y 3 | $y_{12}-y_{13}\ge 4$ ó $y_{13}-y_{12}\ge 3$ |
| 2 | 1 y 2 | $y_{21}-y_{22}\ge 8$ ó $y_{22}-y_{21}\ge 8$ |
| 2 | 1 y 3 | $y_{21}-y_{23}\ge 7$ ó $y_{23}-y_{21}\ge 8$ |
| 2 | 2 y 3 | $y_{22}-y_{23}\ge 7$ ó $y_{23}-y_{22}\ge 8$ |
| 3 | 1 y 2 | $y_{31}-y_{32}\ge 6$ ó $y_{32}-y_{31}\ge 4$ |
| 4 | 2 y 3 | $y_{42}-y_{43}\ge 3$ ó $y_{43}-y_{42}\ge 5$ |

Más $y_{ij}\ge 0$. Para resolverlo como MIP cada «ó» se linealiza con una binaria $x$ y una constante grande $M$ (por ejemplo, la suma de todos los $p_{ij}=58$): $y_{il}-y_{ij}\ge p_{ij}-M(1-x)$ y $y_{ij}-y_{il}\ge p_{il}-Mx$. Resuelto así (cálculo propio con PuLP/CBC, no aparece en el PDF), el óptimo es $C_{max}=28$, el mismo valor al que llega el cuello de botella móvil en la página 30.

### Página 8 — Job shop: ejemplo

> [Diagrama: grafo disyuntivo del ejemplo de la página 7. Nodos negros U (fuente) y V (sumidero). Tres filas de nodos, una por trabajo:
> - Fila superior (trabajo 1): U → (1,1) → (2,1) → (3,1) → V
> - Fila central (trabajo 2): U → (2,2) → (1,2) → (4,2) → (3,2) → V
> - Fila inferior (trabajo 3): U → (1,3) → (2,3) → (4,3) → V
>
> Arcos punteados bidireccionales (disyuntivos), uno por cada par de operaciones en la misma máquina:
> - Máquina 1: (1,1)↔(1,2), (1,1)↔(1,3), (1,2)↔(1,3)
> - Máquina 2: (2,1)↔(2,2), (2,1)↔(2,3), (2,2)↔(2,3)
> - Máquina 3: (3,1)↔(3,2)
> - Máquina 4: (4,2)↔(4,3)]

*Se debe seleccionar el sentido de cada arco punteado de forma que no hayan ciclos (secuencia de trabajos en cada máquina).*

*El makespan se calcula como la ruta más larga desde U hasta V, para el conjunto de arcos punteados seleccionados. Ruta crítica.*

### Página 9 — Job shop: formulación matemática (GAMS, parte 1)

*LogMIP User's Manual Example 4 - Job Shop Scheduling (LOGMIP4,SEQ=337)*

> [Imagen: captura de pantalla del IDE de GAMS (gamside, proyecto `gmsproj.gpr`, archivo abierto `logmip4.gms`). La parte superior del archivo (el bloque de comentario `$ontext … $offtext`) no se ve; la captura empieza en `$offtext`. El borde derecho de la ventana está recortado, pero las líneas visibles están completas.]

Código visible (transcripción literal, incluida la errata `clasges` del comentario original):

```gams
$offtext


SETS  I  jobs    / A, B, C, D, E, F, G /
      J  stages  / 1*5 /;

ALIAS (I,K),(J,M);

SET L(I,K,J)  Subset to prevent clasges at stage j between stage j and k
        /A.B.3, A.B.5, A.C.1, A.D.3, A.E.3, A.E.5, A.F.1, A.F.3, A.G.5,
         B.C.2, B.D.2, B.D.3, B.E.2, B.E.3, B.E.5, B.F.3, B.G.2, B.G.5,
         C.D.2, C.D.4, C.E.2, C.F.1, C.F.4, C.G.2, C.G.4,
         D.E.2, D.E.3, D.F.3, D.F.4, D.G.2, D.G.4,
         E.F.3, E.G.2, E.G.5,
         F.G.4 /    ;

TABLE TAU(I,J) processing time of job i in stage j

          1       2       3       4       5
     A    3               5               2
     B            3       4               3
     C    6       3               6
     D            8       5       1
     E            4       6               2
     F    2               5       7
     G            8               5       4      ;


VARIABLE           MS      makespan ;
BINARY   VARIABLE  Y(I,K,J)  sequencing variable between jobs i and k ;
POSITIVE VARIABLE  T(I) ;
```

Datos de la tabla `TAU(I,J)` (tiempo de proceso del trabajo $i$ en la etapa $j$; vacío = el trabajo no pasa por esa etapa):

| Trabajo | Etapa 1 | Etapa 2 | Etapa 3 | Etapa 4 | Etapa 5 | Total |
|---|---|---|---|---|---|---|
| A | 3 | – | 5 | – | 2 | 10 |
| B | – | 3 | 4 | – | 3 | 10 |
| C | 6 | 3 | – | 6 | – | 15 |
| D | – | 8 | 5 | 1 | – | 14 |
| E | – | 4 | 6 | – | 2 | 12 |
| F | 2 | – | 5 | 7 | – | 14 |
| G | – | 8 | – | 5 | 4 | 17 |

El conjunto `L(I,K,J)` tiene 35 tripletas: son exactamente los pares de trabajos $i<k$ que comparten la etapa $j$ (comprobado contra la tabla `TAU`), es decir, los pares que podrían chocar en esa etapa.

### Página 10 — Job shop: formulación matemática (GAMS, parte 2)

> [Imagen: segunda captura del mismo archivo `logmip4.gms` en el IDE de GAMS.]

```gams
EQUATIONS
   FEAS(I)           makespan greater than all processing times
   NOCLASH1(I,K,J)   when i precedes k
   NOCLASH2(I,K,J)   when k precedes i
   DUMMY      ;

FEAS(I).. MS =G= T(I) + SUM(M, TAU(I,M))  ;

NOCLASH1(I,K,J)$((ORD(I) LT ORD(K)) AND L(I,K,J)) ..
   T(I) + SUM(M$(ORD(M) LE ORD(J)), TAU(I,M)) =L=
   T(K) + SUM(M$(ORD(M) LT ORD(J)), TAU(K,M));


NOCLASH2(I,K,J)$((ORD(I) LT ORD(K)) AND L(I,K,J)) ..
   T(K) + SUM(M$(ORD(M) LE ORD(J)), TAU(K,M)) =L=
   T(I) + SUM(M$(ORD(M) LT ORD(J)), TAU(I,M));

DUMMY..  SUM((I,K,J)$((ORD(I) LT ORD(K)) AND L(I,K,J)), Y(I,K,J)) =G= 0;

MODEL JOBSHOP / ALL / ;

*Find a quick and dirty BigM to overwrite LOGMIP's default
scalar BIGM; BIGM = SUM((I,J),TAU(I,J));

file fx /"%lm.info%"/;
putclose fx 'default bigm' BIGM 'disjunction Y NOCLASH1 else NOCLASH2';

OPTION OPTCR = 0.0, OPTCA = 0.0, EMP = LOGMIP;

SOLVE JOBSHOP MINIMIZING MS USING EMP ;

DISPLAY Y.L, T.L ;
```

**Explicación del modelo (redacción propia a partir del código):**

- Conjuntos: $i,k \in I=\{A,\dots,G\}$ (7 trabajos); $j,m \in J=\{1,\dots,5\}$ (etapas). `ALIAS` permite usar $k$ como otro trabajo y $m$ como otra etapa.
- Parámetro: $\tau_{ij}$ = `TAU(I,J)`, tiempo del trabajo $i$ en la etapa $j$.
- Variables: $MS$ = makespan; $T_i \ge 0$ = tiempo de inicio del trabajo $i$; $Y_{ikj}\in\{0,1\}$ = 1 si el trabajo $i$ va antes que el $k$ en la etapa $j$.
- `FEAS(I)`: $MS \ge T_i + \sum_{m} \tau_{im}$ (el makespan supera la terminación de cada trabajo).
- Disyunción para cada $(i,k,j)\in L$ con $i<k$ (la escribe LogMIP con la línea `disjunction Y NOCLASH1 else NOCLASH2`):

$$\left[\,Y_{ikj}:\; T_i + \sum_{m\le j}\tau_{im} \;\le\; T_k + \sum_{m<j}\tau_{km}\,\right] \;\vee\; \left[\,\neg Y_{ikj}:\; T_k + \sum_{m\le j}\tau_{km} \;\le\; T_i + \sum_{m<j}\tau_{im}\,\right]$$

  El lado izquierdo de `NOCLASH1` es la hora en que $i$ **termina** la etapa $j$; el derecho, la hora en que $k$ **empieza** la etapa $j$. `NOCLASH2` es el caso contrario.
- `DUMMY`: $\sum Y_{ikj} \ge 0$; restricción trivial que solo sirve para que las $Y$ aparezcan en el modelo.
- LogMIP reformula la disyunción con big-M, con $M$ = `BIGM` $=\sum_{i,j}\tau_{ij} = 92$:

$$T_i + \sum_{m\le j}\tau_{im} \le T_k + \sum_{m<j}\tau_{km} + M(1-Y_{ikj}),\qquad T_k + \sum_{m\le j}\tau_{km} \le T_i + \sum_{m<j}\tau_{im} + M\,Y_{ikj}$$

- `OPTCR = 0`, `OPTCA = 0`: exige el óptimo exacto (brecha relativa y absoluta cero). Se resuelve como modelo EMP con LogMIP y se muestran `Y.L` (secuencias) y `T.L` (inicios).

> Observaciones (deducidas):
> - El modelo tiene **un solo tiempo de inicio por trabajo**, $T_i$, y la etapa $j$ empieza en $T_i+\sum_{m<j}\tau_{im}$. Eso supone que todos los trabajos recorren las etapas en el orden 1 → 5 (saltándose las que no usan) y **sin esperas entre etapas** (*no-wait*). En rigor es un taller de flujo multietapa *no-wait* con etapas omitidas, no un job shop general con rutas distintas como el de la página 7.
> - Las diapositivas no muestran el resultado. Al reproducir el modelo en Python (PuLP/CBC) con los mismos datos y el mismo big-M se obtiene $MS^* = 32$; una solución óptima es $T_B=0$, $T_C=1$, $T_E=3$, $T_A=10$, $T_G=10$, $T_F=16$, $T_D=18$ (puede haber óptimos alternativos).

### Página 11 — Job shop: Cuello de botella móvil

*M: conjunto de máquinas*

*Mo: conjunto de máquinas con las operaciones ya programadas.*

*En cada iteración, se adiciona una máquina al conjunto Mo.*

*Idea básica: ¿Cuál es la máquina que genera el tiempo muerto total más grande ?*

### Página 12 — Job shop: Cuello de botella móvil (Algoritmo, pasos 1–3)

*Algoritmo*

1. $M_o = \{\}$. $G$ contiene todos los arcos continuos, $C_{max}(M_o)$ = ruta más larga del grafo.
2. Para cada máquina sin programar:
   - Genere una instancia de $1 \mid r_j \mid L_{max}$
   - $r_j$ es el tiempo más largo desde $U$ hasta $(i,j)$
   - $d_j$ se determina con el tiempo más largo desde $(i,j)$ hasta $(S)$ menos $p(i,j)$
     - $d_j = C_{max}$ – ruta desde $(i,j)$ hasta $(S)$ menos $p(i,j)$
   - Resolver cada problema:
   - $L_{max}(i)$ = mínimo $L_{max}$ de la máquina $i$.
3. Selección de cuello de botella

En fórmulas (con $(S)$ = sumidero $V$):

$$r_{ij} = \text{longitud de la ruta más larga de } U \text{ a } (i,j)$$

$$q_{ij} = \big(\text{ruta más larga de } (i,j) \text{ a } V\big) - p_{ij}, \qquad d_{ij} = C_{max}(M_o) - q_{ij}$$

$$L_j = C_j - d_j, \qquad L_{max}(i) = \min_{\text{secuencias de } i}\; \max_j L_j$$

donde $q_{ij}$ («cola») es el tiempo mínimo que falta después de terminar $(i,j)$ y $C_j$ es la terminación de $j$ en el problema de una máquina.

### Página 13 — Job shop: Cuello de botella móvil (Algoritmo, pasos 3–5)

*Algoritmo*

3. Selección de cuello de botella
   - Seleccione la máquina $k$ con el máximo $L_{max}(i)$
   - Secuencie la máquina correspondiente.
   - Inserte los arcos discontinuos en el grafo $G$
   - Inserte la máquina $k$ en $M_o$
4. Para cada máquina en $M_o$, excepto $k$:
   - Borre los arcos discontinuos del grafo $G$,
   - Formule el problema de una única máquina $1 \mid r_j \mid L_{max}$
   - Inserte los arcos discontinuos correspondientes a la secuencia
5. Pare cuando todas las máquinas hayan sido secuenciadas.

En el ejemplo, el nuevo makespan se actualiza como $C_{max}(M_o \cup \{k\}) = C_{max}(M_o) + L_{max}(k)$ (págs. 24 y 28).

### Página 14 — Job shop: Cuello de botella móvil (datos del ejemplo)

*Algoritmo*

| Jobs | Ruta | Tiempos de proceso |
|---|---|---|
| 1 | 1-2-3 | P11=10, p21=8, p31=4 |
| 2 | 2-1-4-3 | P22=8, p12 = 3, p42=5, p32=6 |
| 3 | 1-2-4 | P13=4, p23=7, p43=3 |

(Es la misma instancia de la página 7: 3 trabajos y 4 máquinas.)

### Página 15 — Job shop: Cuello de botella móvil (Iteración 1, grafo)

*Algoritmo — Iteración 1*

- $M_o = \{\}$
- Makespan = 22 (trabajos 1 y 2)

> [Diagrama: grafo solo con los arcos conjuntivos (continuos), cada uno con el tiempo de proceso del nodo de donde sale:
> - U → (1,1) →[10] (2,1) →[8] (3,1) →[4] V
> - U → (2,2) →[8] (1,2) →[3] (4,2) →[5] (3,2) →[6] V
> - U → (1,3) →[4] (2,3) →[7] (4,3) →[3] V
>
> Longitud de cada ruta: trabajo 1 = 10+8+4 = 22; trabajo 2 = 8+3+5+6 = 22; trabajo 3 = 4+7+3 = 14. La ruta más larga es 22.]

### Página 16 — Job shop: Cuello de botella móvil (Iteración 1, ruta crítica)

Mismo grafo y mismo texto de la página 15 (Mo = {}, Makespan = 22 (trabajos 1 y 2)).

> [Diagrama: igual al de la página 15, con las rutas críticas resaltadas en rojo: U → (1,1) → (2,1) → (3,1) → V y U → (2,2) → (1,2) → (4,2) → (3,2). El arco (3,2) → V aparece en negro, aunque también forma parte de la ruta del trabajo 2 de longitud 22. La ruta del trabajo 3 queda en negro.]

### Página 17 — Job shop: Cuello de botella móvil (Iteración 1, máquina 1)

*Algoritmo — Iteración 1*

- $M_o = \{\}$
- Makespan = 22 (trabajos 1 y 2)
- Resolver el problema $1 \mid r_j \mid L_{max}$ (sobre la máquina 1):

| jobs | 1 | 2 | 3 |
|---|---|---|---|
| P1j | 10 | 3 | 4 |
| R1j | 0 | 8 | 0 |
| d1j | 22-12=10 | 11 | 12 |

Recuadros explicativos (con flechas hacia la tabla):

- «Camino más corto desde (U) hasta (1,2)» → apunta a $R_{12}=8$.
- «Makespan – camino más largo desde (1,2) hasta (V)» → apunta a $d_{12}=11$.

> Observación: el recuadro dice «camino más corto», pero según el algoritmo (pág. 12) $r_j$ es la ruta **más larga** desde U. Aquí da lo mismo porque a (1,2) solo llega una ruta (U → (2,2) → (1,2), longitud 8).

Cálculo de cada valor (deducido de los números de la tabla): $d_{11}=22-(8+4)=10$; $d_{12}=22-(5+6)=11$; $d_{13}=22-(7+3)=12$; $r_{11}=r_{13}=0$ porque son primeras operaciones; $r_{12}=p_{22}=8$.

### Página 18 — Job shop: Cuello de botella móvil (Iteración 1, secuencia de la máquina 1)

- $M_o = \{\}$
- Makespan = 22 (trabajos 1 y 2)
- Secuencia de la máquina 1

> [Diagrama: el grafo de la página 16 (rutas críticas en rojo, pesos de los arcos visibles) con los tres nodos de la máquina 1, (1,1), (1,2) y (1,3), resaltados en amarillo: son las operaciones que forman el subproblema de una máquina.]

### Página 19 — Job shop: Cuello de botella móvil (Iteración 1, solución de la máquina 1)

- Resolver el problema $1 \mid r_j \mid L_{max}$ (sobre la máquina 1):

| jobs | 1 | 2 | 3 |
|---|---|---|---|
| P1j | 10 | 3 | 4 |
| R1j | 0 | 8 | 0 |
| d1j | 10 | 11 | 12 |

→ **RTA: 1-2-3**

### Página 20 — Job shop: Cuello de botella móvil (Iteración 1, Lmax de la máquina 1)

| jobs | 1 | 2 | 3 |
|---|---|---|---|
| P1j | 10 | 3 | 4 |
| R1j | 0 | 8 | 0 |
| d1j | 10 | 11 | 12 |
| C1j | 10 | 13 | 17 |
| Lj | =10-10=0 | =13-11=2 | =17-12=5 |

→ **RTA: 1-2-3, $L_{max} = 5$**

(Trabajo 1 de 0 a 10; trabajo 2 de 10 a 13, pues aunque llega en 8 la máquina está ocupada; trabajo 3 de 13 a 17.)

### Página 21 — Job shop: Cuello de botella móvil (Iteración 1, máquina 2)

- Resolver el problema $1 \mid r_j \mid L_{max}$ (sobre la máquina 2):

| jobs | 1 | 2 | 3 |
|---|---|---|---|
| P2j | 8 | 8 | 7 |
| R2j | 10 | 0 | 4 |
| d2j | 18 | 8 | 19 |

→ **RTA: 2-3-1**

(Deducido: $r_{21}=p_{11}=10$, $r_{22}=0$, $r_{23}=p_{13}=4$; $d_{21}=22-4=18$, $d_{22}=22-(3+5+6)=8$, $d_{23}=22-3=19$.)

### Página 22 — Job shop: Cuello de botella móvil (Iteración 1, Lmax de la máquina 2)

| jobs | 1 | 2 | 3 |
|---|---|---|---|
| P2j | 8 | 8 | 7 |
| R2j | 10 | 0 | 4 |
| d2j | 18 | 8 | 19 |
| Cj | 23 | 8 | 15 |
| Lj | 5 | 0 | -4 |

→ **RTA: 2-3-1, $L_{max} = 5$**

(Trabajo 2 de 0 a 8; trabajo 3 de 8 a 15; trabajo 1 de 15 a 23.)

### Página 23 — Job shop: Cuello de botella móvil (Iteración 1, máquinas 3 y 4)

- $M_o = \{\}$
- Makespan = 22 (trabajos 1 y 2)
- Resolver el problema $1 \mid r_j \mid L_{max}$:
  - Para la máquina 3, $L_{max} = 4$
  - Para la máquina 4, $L_{max} = 0$
- Se selecciona la máquina 1 o 2. (cuellos de botella)

Datos de esos dos subproblemas (deducidos del grafo; las diapositivas solo dan el $L_{max}$):

| Máquina | Trabajo | $p$ | $r$ | $d$ | Mejor secuencia | $C_j$ | $L_j$ |
|---|---|---|---|---|---|---|---|
| 3 | 1 | 4 | 18 | 22 | 2-1 | 26 | 4 |
| 3 | 2 | 6 | 16 | 22 | 2-1 | 22 | 0 |
| 4 | 2 | 5 | 11 | 16 | 2-3 | 16 | 0 |
| 4 | 3 | 3 | 11 | 22 | 2-3 | 19 | -3 |

Resumen de la iteración 1: $L_{max}(1)=5$, $L_{max}(2)=5$, $L_{max}(3)=4$, $L_{max}(4)=0$. Hay empate entre las máquinas 1 y 2.

### Página 24 — Job shop: Cuello de botella móvil (Iteración 1, máquina 1 fijada)

- Se selecciona la máquina 1 (cuellos de botella)
- $C_{max} = 22+5\,(L_{max}) = 27$

> [Diagrama: grafo con los arcos conjuntivos y, ahora, los arcos de la secuencia 1-2-3 de la máquina 1 dibujados como arcos continuos: (1,1) → (1,2) y (1,2) → (1,3). Los demás arcos disyuntivos ya no aparecen. Sin etiquetas de peso; por la regla de la pág. 6 sus pesos son $p_{11}=10$ y $p_{12}=3$.]

Comprobación (deducida): con esos arcos, la ruta U → (1,1) → (1,2) → (1,3) → (2,3) → (4,3) → V mide $10+3+4+7+3 = 27$.

### Página 25 — Job shop: Cuello de botella móvil (Iteración 1, repetida)

Diapositiva idéntica a la página 24 (mismo texto, mismo grafo y $C_{max} = 22+5\,(L_{max}) = 27$).

### Página 26 — Job shop: Cuello de botella móvil (Iteración 2, grafo)

*Iteración 2, $M_o = \{1\}$*

- Resolver el problema $1 \mid r_j \mid L_{max}$ para las máquinas 2,3,4

> [Diagrama: el mismo grafo de la página 24 (arcos de ruta más los arcos (1,1) → (1,2) y (1,2) → (1,3) de la máquina 1).]

### Página 27 — Job shop: Cuello de botella móvil (Iteración 2, subproblemas)

*Iteración 2, $M_o = \{1\}$* — Resolver el problema $1 \mid r_j \mid L_{max}$ para las máquinas 2,3,4

**Maquina 2**

| Job | 1 | 2 | 3 |
|---|---|---|---|
| P2j | 8 | 8 | 7 |
| R2j | 10 | 0 | 17 |
| D2j | 23 | 10 | 24 |

RTA: 2-1-3, $L_{max} = 1$

**Maquina 3**

| Job | 1 | 2 |
|---|---|---|
| P3j | 4 | 6 |
| R3j | 18 | 18 |
| D3j | 27 | 27 |

RTA: $L_{max}=1$ con cualquier secuencia.

**Escogemos la máquina 2.**

Detalle (deducido):

- Con la máquina 1 fijada, $r_{23}=r_{13}+p_{13}=13+4=17$ (el trabajo 3 ahora espera a los trabajos 1 y 2 en la máquina 1) y los $d$ se calculan con $C_{max}=27$: $d_{21}=27-4=23$, $d_{22}=27-(3+14)=10$, $d_{23}=27-3=24$.
- Máquina 2, secuencia 2-1-3: trabajo 2 de 0 a 8 ($L=-2$), trabajo 1 de 10 a 18 ($L=-5$), trabajo 3 de 18 a 25 ($L=1$). $L_{max}=1$.
- Máquina 3: cualquiera de las dos secuencias termina en 28, así que $L_{max}=28-27=1$.
- Máquina 4 (no aparece en la diapositiva): trabajo 2 con $p=5$, $r=13$, $d=21$; trabajo 3 con $p=3$, $r=24$, $d=27$. Con la secuencia 2-3, $L_{max}=0$.
- Las máquinas 2 y 3 empatan con $L_{max}=1$; se escoge la 2.

### Página 28 — Job shop: Cuello de botella móvil (Iteración 2, resultado)

*Iteración 2, $M_o = \{1,2\}$*

$C_{max} = 27+1\,(L_{max}) = 28$

- Se debe intentar rehacer la secuencia de la máquina 1. (Paso 4 del algoritmo.)
- En este caso no se encuentran mejoras.

### Página 29 — Job shop: Cuello de botella móvil (Iteración 3, grafo)

*Iteración 3, $M_o = \{1,2\}$*

> [Diagrama: grafo con los arcos de ruta, los arcos de la máquina 1, (1,1) → (1,2) y (1,2) → (1,3), y los de la máquina 2: (2,1) → (2,3) y un arco que llega a (2,1) desde (4,2).]

*Resolver los problemas de tardanza máxima para maquinas 3,4*

> Observación: la secuencia escogida para la máquina 2 es 2-1-3, así que los arcos deberían ser (2,2) → (2,1) y (2,1) → (2,3). El arco que llega a (2,1) sale de (4,2), un nodo de la máquina 4; parece un error de dibujo y debería salir de (2,2).

Detalle (deducido): con $C_{max}=28$, la máquina 3 tiene $r_{31}=r_{32}=18$ y $d_{31}=d_{32}=28$; la máquina 4 tiene trabajo 2 ($r=13$, $d=22$) y trabajo 3 ($r=25$, $d=28$). En ambas máquinas $L_{max}=0$.

### Página 30 — Job shop: Cuello de botella móvil (Iteración 3, programa final)

*Iteración 3, $M_o = \{1,2\}$*

**El resultado debe ser que ambas máquinas 3 y 4 tienen tardanza = 0. ¡No son cuello de botella!** (texto en rojo)

> [Gantt: cuatro filas (Machine 1 a Machine 4) y eje horizontal de periodos numerados 1 a 30; una barra que ocupa las casillas 1 a 10 corresponde al intervalo de tiempo de 0 a 10. Colores: trabajo 1 amarillo, trabajo 2 azul, trabajo 3 naranja. Makespan = 28.]

| Máquina | Trabajo | Inicio | Fin |
|---|---|---|---|
| Machine 1 | 1 | 0 | 10 |
| Machine 1 | 2 | 10 | 13 |
| Machine 1 | 3 | 13 | 17 |
| Machine 2 | 2 | 0 | 8 |
| Machine 2 | 1 | 10 | 18 |
| Machine 2 | 3 | 18 | 25 |
| Machine 3 | 2 | 18 | 24 |
| Machine 3 | 1 | 24 | 28 |
| Machine 4 | 2 | 13 | 18 |
| Machine 4 | 3 | 25 | 28 |

Secuencias finales: M1: 1-2-3; M2: 2-1-3; M3: 2-1; M4: 2-3. $C_{max}=28$. La Máquina 2 está ociosa de 8 a 10. Comprobación por trabajo: trabajo 1 = M1 (0–10) → M2 (10–18) → M3 (24–28); trabajo 2 = M2 (0–8) → M1 (10–13) → M4 (13–18) → M3 (18–24); trabajo 3 = M1 (13–17) → M2 (18–25) → M4 (25–28). Todas las rutas se respetan. El MIP disyuntivo de la página 5 resuelto con este mismo ejemplo también da 28 (cálculo propio), así que este programa es óptimo.

### Página 31 — Herramientas informáticas

*Revisar el sitio web para propósitos académicos:*

http://web-static.stern.nyu.edu/om/software/lekin/

> [Imagen: captura del software **LEKIN – flexible job-shop scheduling system** (menús Workspace, File, Schedule, Log, Sort, Tools, Window, Help) con la instancia `MT10`. Tiene cuatro ventanas:
> 1. **Gantt Chart – MT10.seq (WSPT)**: diagrama de Gantt con eje de tiempo de 100 a 1300 y 10 filas de máquinas con barras de colores (una por trabajo).
> 2. **Sequence – MT10.seq (WSPT)**: secuencia por máquina (tabla abajo).
> 3. **Log Book – MT10.seq**: comparación de reglas y heurísticas (tabla abajo).
> 4. **Job Pool – MT10.job (Job Shop)**: datos y resultados por trabajo (tabla abajo).]

Ventana *Sequence – MT10.seq (WSPT)*:

| Mc/Job | Setup | Start | Stop | Pr.tm |
|---|---|---|---|---|
| W01 | 0 | | | 493 |
| W02 | 0 | | | 548 |
| └ J07 | 0 | 0 | 46 | 46 |
| └ J01 | 0 | 46 | 124 | 78 |
| └ J05 | 0 | 124 | 146 | 22 |
| └ J06 | 0 | 146 | 148 | 2 |
| └ J10 | 0 | 148 | 233 | 85 |
| └ J09 | 0 | 233 | 302 | 69 |
| └ J03 | 0 | 302 | 393 | 91 |
| └ J02 | 0 | 457 | 485 | 28 |
| └ J08 | 0 | 564 | 610 | 46 |
| └ J04 | 0 | 610 | 691 | 81 |
| W03 | 0 | | | 556 |

Ventana *Log Book – MT10.seq*:

| Schedule | Time | $C_{max}$ | $T_{max}$ | $\sum U_j$ | $\sum C_j$ | $\sum T_j$ | $\sum w_jC_j$ | $\sum w_jT_j$ |
|---|---|---|---|---|---|---|---|---|
| General SB Routine / sum | 24 | 1110 | 1110 | 10 | 8676 | 8676 | 8676 | 8676 |
| Local Search / sum(wT) | 23 | 1107 | 1107 | 10 | 7488 | 7488 | 7488 | 7488 |
| Shifting Bottleneck / sum | 24 | 1113 | 1113 | 10 | 7551 | 7551 | 7551 | 7551 |
| WSPT | 1 | 1356 | 1356 | 10 | 8538 | 8538 | 8538 | 8538 |

Ventana *Job Pool – MT10.job (Job Shop)*:

| ID | Wght | Rls | Due | Pr.tm. | Stat. | Bgn | End | T | wT |
|---|---|---|---|---|---|---|---|---|---|
| J01 | 1 | 0 | 0 | 395 | | 0 | 531 | 531 | 531 |
| J02 | 1 | 0 | 0 | 510 | | 83 | 679 | 679 | 679 |
| J03 | 1 | 0 | 0 | 568 | | 302 | 1082 | 1082 | 1082 |
| J04 | 1 | 0 | 0 | 655 | | 610 | 1356 | 1356 | 1356 |
| └ W02 | | | | 81 | A | 610 | 691 | | |
| └ W03 | | | | [ilegible, fila cortada] | A | [ilegible] | [ilegible] | | |

Lectura: como todos los trabajos tienen peso 1 y fecha de entrega 0, $T_j=C_j$, así que $T_{max}=C_{max}$ y $\sum T_j=\sum C_j=\sum w_jC_j=\sum w_jT_j$. En $C_{max}$, la búsqueda local (1107), la rutina general SB (1110) y el shifting bottleneck (1113) mejoran mucho la regla WSPT (1356). Nota externa (no está en la diapositiva): MT10 es la instancia clásica de Muth y Thompson de 10 trabajos × 10 máquinas.

### Página 32 — Investigadores destacados: Rubén Ruiz, Ph.D.

*Rubén Ruiz, Ph.D.*

https://scholar.google.com.co/citations?user=aTVU3eoAAAAJ&hl=en

> [Imagen: captura del perfil de Google Scholar de Rubén Ruiz: «Unknown affiliation», «Verified email at eio.upv.es», con foto de perfil (decorativa).]

Índices de citación:

| | All | Since 2012 |
|---|---|---|
| Citations | 5459 | 3762 |
| h-index | 34 | 32 |
| i10-index | 57 | 51 |

> [Gráfico: barras de citas por año, 2009 a 2017. Crecen de 2009 a un máximo en 2014, bajan un poco en 2015 y 2016 y caen en 2017 (año incompleto). Sin valores numéricos visibles.]

Publicaciones visibles (Title 1–20):

| Título | Autores | Revista | Cited by | Year |
|---|---|---|---|---|
| A simple and effective iterated greedy algorithm for the permutation flowshop scheduling problem | R Ruiz, T Stützle | European Journal of Operational Research 177 (3), 2033-2049 | 543 | 2007 |
| A comprehensive review and evaluation of permutation flowshop heuristics | R Ruiz, C Maroto | European Journal of Operational Research 165 (2), 479-494 | 470 | 2005 |
| The hybrid flow shop scheduling problem | R Ruiz, JA Vázquez-Rodríguez | European Journal of Operational Research 205 (1), 1-18 | 413 | 2010 |
| A genetic algorithm for hybrid flowshops with sequence dependent setup times and machine eligibility | R Ruiz, C Maroto | European Journal of Operational Research 169 (3), 781-800 | 322 | 2006 |
| Two new robust genetic algorithms for the flowshop scheduling problem | [cortado] | [cortado] | 304 | 2006 |

Co-authors (columna derecha): Javier Alcaraz, Thomas Stützle, Quan-ke pan, Michele Ciavotta, Bahman Naderi, Angel A. Juan, Ali Allahverdi, Jose M Framiñán, Alejandro Rodríguez Villalobos, Javier Faulin, [la lista sigue cortada].

### Página 33 — ¡Gracias!

¡Gracias! — William Guerrero, Ph.D.

> [Imagen decorativa: franja con foto del campus y logo de la Universidad de La Sabana]
