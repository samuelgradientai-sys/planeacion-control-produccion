# L17-single-machine-scheduling

> **Archivo:** [`L17-single-machine-scheduling.pdf`](./L17-single-machine-scheduling.pdf) · **Corte 3** · 49 páginas  
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

- Excel de clase con FIFO, SPT, WSPT, EDD, MS, cadenas, preemption y una hoja para Solver: [programacion-produccion-una-maquina](./programacion-produccion-una-maquina.md). Ejemplo cotidiano con $r_j$: [ejemplo-1-programacion-produccion](./ejemplo-1-programacion-produccion.md).
- Implementación en Python del ejemplo ATC de las pp. 43-45: [atc.py](./atc.py), explicado en el [README](./README.md).
- Compendio con hojas de 1 máquina (básicas, MS/ATC, precedencia, preemption, Lawler): [metodos-programacion-produccion-corte3](../00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md).
- Notación e indicadores: [L16](../01-introduccion-scheduling/L16-intro-scheduling.md). Siguiente tema: [L18 máquinas paralelas](../03-maquinas-paralelas/L18-parallel-machine-scheduling.md).
- El reto 2 de la competencia ($P3|r_j,prec|\sum w_jT_j$) usa WSPT, ATC, cadenas y EDD: [proyecto-competencia-scheduling](../proyecto-competencia-scheduling/solucion/README.md).

**Observaciones sobre el material**

- p. 36: dice $U=\{J3,J4\}$ en $t=13$, pero J4 ya estaba programado; los pendientes son J2 y J3.
- p. 43: pregunta por el flujo **ponderado** promedio, pero las soluciones (pp. 44-45) solo calculan el flujo sin ponderar.
- p. 45: los índices ATC impresos (0.40, 0.30, 0.23, 0.13 / 0.43, 0.58 / 0.43) salen con $K=1$ y $\bar p=5.5$ fijo, el promedio de los cuatro trabajos. La definición de la p. 13 dice que $\bar p$ es el promedio de los no programados; con esa definición $I_3(5)=0.589$, y la secuencia no cambia.
- p. 28: "Añadir j\* a J (al final)" se entiende como la última posición libre: el algoritmo de Lawler construye la secuencia de atrás hacia adelante (interpretación).
- p. 48: la captura de Excel muestra una solución ($\sum w_jT_j=16822$) muy lejos del óptimo publicado (913).

## Contenido completo (página por página)

### Página 1 — Portada

**Planeación, Programación y Control de las Operaciones** — **Programación de la Producción**. Logo de la Universidad de La Sabana y licencia Creative Commons BY-NC-SA.

> [Imagen decorativa: foto de un edificio del campus en tonos azules. Las demás diapositivas llevan una franja inferior con foto del campus y logo; no se vuelve a mencionar.]

### Página 2 — Modelos de una única máquina

- Es simple, pero es el caso especial de varios problemas de scheduling.
- Fundamento para varias heurísticas
- Descomposición de problemas más complejos
  - Ejemplo: problema con un único cuello de botella.

### Página 3 — Programación de una máquina

- Problema: secuenciar *n* trabajos en la máquina de tal forma que se minimice un objetivo:

  Tiempo promedio de flujo, Tardanza Ponderada, Retardo máximo, Número de trabajos tardíos, etc.

- En general los problemas de secuenciación de trabajos en una máquina son NP-hard!!

### Página 4 — ¿Existe alguna otra forma de hallar una solución óptima al problema de una máquina?

- Supongamos que tenemos *n* trabajos para una máquina... y queremos minimizar Tardanza Ponderada Total.
- Qué se puede hacer?
- Enumeración exhaustiva: ¿Cuántas posibles **secuencias** hay??

### Página 5 — Posibles secuencias: n!

| n | Factorial (n) |
|---|---|
| 0 | 1 |
| 1 | 1 |
| 2 | 2 |
| 3 | 6 |
| 4 | 24 |
| 5 | 120 |
| 6 | 720 |
| 7 | 5040 |
| 8 | 40320 |
| 9 | 362880 |
| 10 | 3628800 |
| 11 | 39916800 |
| 12 | 479001600 |
| 13 | 6227020800 |
| 14 | 8.7178E+10 |
| 15 | 1.3077E+12 |
| 16 | 2.0923E+13 |
| 17 | 3.5569E+14 |
| 18 | 6.4024E+15 |
| 19 | 1.2165E+17 |
| 20 | 2.4329E+18 |

> [Recuadro de texto junto a la tabla:] "Es demasiado!! Un computador rápido tardaría AÑOS para el caso de 20 trabajos"

### Página 6 — Otras soluciones

- Algoritmos exactos
  - Programación Dinámica
  - Programación Entera Mixta
  - Ramificación y Acotación
- ¿Se usan los algoritmos exactos en la industria?
- Hay algunas aplicaciones, la mayoría en líneas de producción (flow shop).
- Pero en general la programación es tan compleja que no existen modelos exactos y el caso es de hallar una **"buena programación" que los encargados entiendan.**

### Página 7 — ¿Existen soluciones óptimas con reglas de despacho?

- Excepto en unos pocos casos, NO existen reglas de despacho (ej. SPT, CR, etc) que garanticen optimalidad.
- Estas son unas **excepciones**:
  - La regla WSPT minimiza el flujo promedio ponderado $1\,//\,\sum w_jC_j$
  - La regla EDD minimiza el retardo máximo $1\,//\,L_{max}$

### Página 8 — Tiempo de terminación ponderado

$1\,|\,|\,\sum w_jC_j$

- Wj puede ser el costo de almacenamiento o la prioridad del trabajo j.
- Reglas para resolverlo:
  - Tiempo de procesamiento ponderado más corto.:
  - Los trabajos se ordenan en orden decreciente de la relación: wj / pj.

### Página 9 — Tiempo de terminación ponderado

$1\,|\,|\,\sum w_jC_j$

- Teorema: la regla de WSPT es optima para el problema.
- Complejidad: $O(n\log n)$

### Página 10 — Tiempo de terminación ponderado

$1\,|\,|\,\sum w_jC_j$

- Ejemplo:

| tarea | Tiempo de proceso | Ponderación |
|---|---|---|
| A | 15 | 4 |
| B | 44 | 5 |
| C | 67 | 1 |
| D | 13 | 3 |
| E | 10 | 2 |

(La diapositiva no muestra la solución. Cálculo propio con WSPT: $w/p$ = A 0.267, D 0.231, E 0.200, B 0.114, C 0.015.)

| Posición | Tarea | $w/p$ | Inicio | Fin = $C_j$ | $w_jC_j$ |
|---|---|---|---|---|---|
| 1 | A | 0.267 | 0 | 15 | 60 |
| 2 | D | 0.231 | 15 | 28 | 84 |
| 3 | E | 0.200 | 28 | 38 | 76 |
| 4 | B | 0.114 | 38 | 82 | 410 |
| 5 | C | 0.015 | 82 | 149 | 149 |
|  |  |  |  |  | $\sum w_jC_j=779$ |

### Página 11 — Reglas de despacho (Políticas de programación)

- Son la forma más simple de programación.
- Una regla de despacho asigna prioridades de procesamiento a los trabajos que se encuentran en la cola de una máquina en un momento dado.
- Infinidad de reglas de despacho para secuenciar trabajos.
- Dos tipos de reglas: Estáticas y Dinámicas
  - Estáticas: Dependen de los parámetros de los trabajos (fecha de entrega, tiempo de proceso, etc.) pero no del tiempo o status de las máquinas.
  - Dinámicas: Dependientes del tiempo o status de las máquinas.

### Página 12 — Reglas de despacho estáticas

- FCFS (First Come First Served) o FIFO
- SPT (Shortest Processing Time) First
  $p_j\le p_{j+1}$ ($p_j$ es el tiempo de proceso del trabajo programado en la $j$-ésima posición)
- EDD (Earliest Due Date) First
  $d_j\le d_{j+1}$ ($d_j$ es la fecha de entrega del trabajo programado en la $j$-ésima posición)
- WSPT (Weighted Shortest Processing Time)
  $w_j/p_j\ge w_{j+1}/p_{j+1}$ Programa primero los trabajos con mayor prioridad y menor tiempo de proceso

### Página 13 — Reglas de despacho dinámicas

- MS (Minimum Slack)
  - El slack es el tiempo remanente para cumplir con la fecha de entrega.

$$s_j=\max(d_j-p_j-t,\ 0)$$

  Secuenciación: $s[k]\le s[k+1]$

- ATC (Aparent Tardiness Cost)

$$I_j(t)=\frac{w_j}{p_j}\,e^{\left(\frac{-\max(d_j-p_j-t,\ 0)}{K\bar p}\right)}$$

$K$: Constante a determinar

$\bar p$: Tiempo promedio de los trabajos no programados

Secuenciación $I[k]\ge I[k+1]$

### Página 14 — Restricciones de precedencia

- Supongamos restricciones de precedencia en cadena:

> [Diagrama: tres cadenas de círculos (sin etiquetas) unidos por flechas de izquierda a derecha: una cadena de 4 trabajos, otra de 3 trabajos y otra de 5 trabajos.]

### Página 15 — Restricciones de precedencia

Si el decisor debe completar la cadena, una vez iniciada, ¿cuál cadena debe hacer primero para minimizar el tiempo total?

RTA: es optimo iniciar con la cadena con mayor relación:

$$\frac{\sum w_j}{\sum p_j}$$

### Página 16 — Restricciones de precedencia

- ¿Qué pasa si la restricción no es necesaria?
- Definimos $l^*$ llamado el trabajo que determina el $\rho-factor$

$$\frac{\sum_{j=1}^{l^*}w_j}{\sum_{j=1}^{l^*}p_j}=\max_{1\le l\le k}\left(\frac{\sum_{j=1}^{l}w_j}{\sum_{j=1}^{l}p_j}\right)$$

### Página 17 — Restricciones de precedencia

Reglas de secuenciación:

- Se debe procesar una cadena de trabajos hasta $l^*$ sin interrupción.
- Seleccione la cadena que esté disponible con el mayor $\rho-factor$

### Página 18 — Ejemplo

| trabajo | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| Wj | 6 | 18 | 12 | 8 | 8 | 17 | 18 |
| pj | 3 | 6 | 6 | 5 | 4 | 8 | 10 |

Considerando las cadenas:

1 -> 2 -> 3 -> 4

5 -> 6 -> 7

### Página 19 — Ejemplo

(Misma tabla de la página 18.)

Considerando las cadenas:

- 1 -> 2 -> 3 -> 4 tiene un $\rho-factor$ = 2.66 determinado por el trabajo 2.
- 5 -> 6 -> 7 tiene un $\rho-factor$ = 2.08 determinado por el trabajo 6

(Verificación: cadena 1: $6/3=2$; $24/9=2.667$; $36/15=2.4$; $44/20=2.2$ → máximo en el trabajo 2. Cadena 2: $8/4=2$; $25/12=2.083$; $43/22=1.955$ → máximo en el trabajo 6.)

### Página 20 — Ejemplo:

Secuencia: 1-> 2 ->

Se repiten los cálculos de la cadena 1.

- 3 -> 4 tiene un $\rho-factor$ = 2 determinado por el trabajo 3.

(Como 2.08 de la cadena 5-6-7 es mayor que 2, sigue la cadena 2.)

### Página 21 — Ejemplo:

Secuencia: 1-> 2 -> 5 -> 6 ->

Se repiten los cálculos de la cadena 2.

- 7 tiene un $\rho-factor$ = 1.8

### Página 22 — Ejemplo:

Secuencia: 1-> 2 -> 5 -> 6 -> 3

Se repiten los cálculos de la cadena 1.

- 4 tiene un $\rho-factor$ = 1.6

### Página 23 — Ejemplo:

Secuencia: 1-> 2 -> 5 -> 6 -> 3 -> 7 -> 4

(Tabla calculada a partir de los datos; la diapositiva solo da la secuencia.)

| Posición | Trabajo | $p_j$ | $w_j$ | Inicio | Fin = $C_j$ | $w_jC_j$ |
|---|---|---|---|---|---|---|
| 1 | 1 | 3 | 6 | 0 | 3 | 18 |
| 2 | 2 | 6 | 18 | 3 | 9 | 162 |
| 3 | 5 | 4 | 8 | 9 | 13 | 104 |
| 4 | 6 | 8 | 17 | 13 | 21 | 357 |
| 5 | 3 | 6 | 12 | 21 | 27 | 324 |
| 6 | 7 | 10 | 18 | 27 | 37 | 666 |
| 7 | 4 | 5 | 8 | 37 | 42 | 336 |
|  |  |  |  |  |  | $\sum w_jC_j=1967$ |

### Página 24 — tiempos de liberación

$1\,|\,r_j,prmp\,|\,\sum w_jC_j$

Considerando *preemption*

Regla de secuenciación:

En cualquier momento del tiempo, el trabajo con la mayor tasa de prioridad sobre tiempo de trabajo faltante se selecciona.

- No necesariamente es óptimo.

### Página 25 — Ejercicio

Implemente la regla mostrada para este ejercicio:

| trabajo | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| pj | 6 | 18 | 12 | 10 | 10 | 17 | 16 |
| rj | 0 | 0 | 0 | 14 | 25 | 25 | 50 |

(La diapositiva no da pesos ni solución. El Excel [programacion-produccion-una-maquina](./programacion-produccion-una-maquina.md), hoja `Restricciones de Precedencia`, lo resuelve con $w_j=1$; ver el resumen.)

### Página 26 — Reglas de despacho cuando los trabajos no están todos disponibles en todo momento

- Idea: En el tiempo *t* ordenar los trabajos de la cola de la máquina de acuerdo a un criterio (regla), seleccionar algún trabajo (digamos *j\**) y programarlo.
- Una vez programado el trabajo *j\**, actualizar el tiempo *t* (se actualiza por eventos) y seleccionar el siguiente trabajo a programar. Repetir hasta que no haya nuevos trabajos que programar.
- Los eventos pueden ser la llegada de nuevos trabajos o la liberación de la máquina.

### Página 27 — Tardanza máxima

- $1\,|\,prec\,|\,L_{max}$ es un caso especial de $1\,|\,prec\,|\,h_{max}$
- $h_{max}=f(C_j)$
- La función objetivo está parametrizada en términos de Cj

### Página 28 — Tardanza máxima

- $1\,|\,prec\,|\,h_{max}$
- Algoritmo:
  1. Conjunto J = {}, Jc = {todos los trabajos}, J' = {trabajos sin sucesor}
  2. Elija el trabajo j*

$$h_{j^*}\left(\sum_{j\in J^c}p_j\right)=\min_{j\in J'}\left(h_j\left(\sum_{k\in J^c}p_k\right)\right)$$

  Añadir j* a J (al final), borrar j* de Jc, modificar J'

  3. Parar cuando no haya más trabajos. Regrese a 2 d.l.c.

### Página 29 — Tardanza máxima

- Ejemplo.

| job | 1 | 2 | 3 |
|---|---|---|---|
| pj | 2 | 3 | 5 |
| hj(cj) | 1+C1 | 1.2C2 | 10 |

- Makespan = 10

### Página 30 — Tardanza máxima

- Ejemplo. (Misma tabla.)
- Makespan = 10
- $h_3(10)=10<h_1(10)=11<h_2(10)=12$
- 3 es el último trabajo.
- Inicia su procesamiento en t = 5

### Página 31 — Tardanza máxima

- Ejemplo. (Misma tabla.)
- T = 5
- $h_1(5)=6,\ h_2(5)=6$
- Elegir cualquiera:
- 1-2-3 y 2-1-3 son secuencias optimas.

(Tablas calculadas a partir de los datos para comprobar que ambas dan $h_{max}=10$.)

| Secuencia 1-2-3 | Inicio | Fin = $C_j$ | $h_j(C_j)$ |
|---|---|---|---|
| 1 | 0 | 2 | 3 |
| 2 | 2 | 5 | 6 |
| 3 | 5 | 10 | 10 |

| Secuencia 2-1-3 | Inicio | Fin = $C_j$ | $h_j(C_j)$ |
|---|---|---|---|
| 2 | 0 | 3 | 3.6 |
| 1 | 3 | 5 | 6 |
| 3 | 5 | 10 | 10 |

### Página 32 — Tardanza máxima

- Para el caso de $1||L_{max}$
- La función de costos $h_j=C_j-d_j$
- La regla óptima para programar es *Earliest Due Date First*
- La generalización $1\,|\,r_j\,|\,L_{max}$ es NP-hard
- Procedimientos de enumeración como Branch-and-bound

### Página 33 — Regla de la razón crítica (CR)

$$CR=\frac{\textit{Tiempo que resta hasta la fecha de entrega}}{\textit{Tiempo de procesamiento restante}}$$

$$CR_j=\frac{\max(d_j-t,\ 0)}{p_j}$$

- Secuenciar el trabajo con min CR.
- Desempate por *SPT*

Leyenda de colores: j1 amarillo, j2 rojo oscuro, j3 rojo, j4 verde.

| j | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| pj | 5 | 7 | 2 | 8 |
| dj | 1 | 9 | 10 | 6 |
| wj | 2 | 3 | 2 | 1 |

### Página 34 — Regla de la razón crítica (CR)

> [Diagrama: Gantt en una fila de celdas numeradas 1 a 25; las celdas 1-5 están en amarillo con "1".]

$t=0$, $U=\{J1,J2,J3,J4\}$

- $CR1=\max(d_1-t,0)/p_1=1/5=0.2$
- $CR2=\max(d_2-t,0)/p_2=9/7=1.29$
- $CR3=\max(d_3-t,0)/p_3=10/2=5$
- $CR4=\max(d_4-t,0)/p_4=6/8=0.75$

Secuenciar J1 y eliminarlo de $U$

| Trabajo | Inicio | Fin |
|---|---|---|
| 1 | 0 | 5 |

### Página 35 — Regla de la razón crítica (CR)

> [Diagrama: Gantt; celdas 1-5 amarillas ("1") y 6-13 verdes ("4").]

$t=5=0+p_1$. $U=\{J2,J3,J4\}$

- $CR2=\max(d_2-t,0)/p_2=4/7=0.57$
- $CR3=\max(d_3-t,0)/p_3=5/2=2.5$
- $CR4=\max(d_4-t,0)/p_4=1/8=0.125$

Secuenciar J4 y eliminarlo de U

| Trabajo | Inicio | Fin |
|---|---|---|
| 1 | 0 | 5 |
| 4 | 5 | 13 |

### Página 36 — Regla de la razón crítica (CR)

> [Diagrama: Gantt; celdas 1-5 amarillas ("1"), 6-13 verdes ("4"), 14-15 rojas ("3"), 16-22 rojo oscuro ("2").]

$t=13=(5+p_4)$ $U=\{J3, J4\}$ (así está escrito en la diapositiva; los trabajos pendientes en $t=13$ son J2 y J3)

- $CR2=\max(d_2-t,0)/p_2=0$
- $CR3=\max(d_3-t,0)/p_3=0$
- Desempatar por SPT

Secuenciar primero J3 y luego J2

| Trabajo | Inicio | Fin |
|---|---|---|
| 1 | 0 | 5 |
| 4 | 5 | 13 |
| 3 | 13 | 15 |
| 2 | 15 | 22 |

### Página 37 — Regla de la razón crítica (CR)

> [Diagrama: el mismo Gantt final de la página 36, con la leyenda de colores y la tabla de datos.]

- Tiempo de Flujo Promedio $=55/4=13.75$
- Retraso Máximo $=\max(5-1,\ 22-9,\ 15-10,\ 13-6)=13$
- Tardanza Ponderada Total $=64$

**Regla CR = 1-4-3-2**

| Trabajo | Inicio | Fin = $C_j$ | $d_j$ | $L_j$ | $T_j$ | $w_j$ | $w_jT_j$ |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 5 | 1 | 4 | 4 | 2 | 8 |
| 4 | 5 | 13 | 6 | 7 | 7 | 1 | 7 |
| 3 | 13 | 15 | 10 | 5 | 5 | 2 | 10 |
| 2 | 15 | 22 | 9 | 13 | 13 | 3 | 39 |
| Total |  | $\sum C_j=55$ |  | $L_{max}=13$ |  |  | 64 |

### Página 38 — Número de trabajos Tardíos

$$1||\sum U_j$$

Algoritmo de solución (forward):

Definir

- J = {trabajos programados}
- Jd = {trabajos que no cumplirán su due date}
- Jc = {trabajos pendientes por programar}

### Página 39 — Número de trabajos Tardíos

Algoritmo de solución (forward):

1. J = {}, Jd = {}, Jc = {1, …, n}
2. Calcular j*
   $$d_{j^*}=\min_{j\in J^c}(d_j)$$
   Añadir j* a J; Borrar j* de Jc; Paso 3.
3. Si $\sum_{j\in J}p_j\le d_{j^*}$ ir al paso 4.
   Si no, defina k* tal que
   $$p_{k^*}=\max_{j\in J}(p_j)$$
   Borrar k* de J; Añadir k* a Jd
4. Si Jc = { } Parar. Si no, regresar a 2.

### Página 40 — Número de trabajos Tardíos

Ejemplo:

| job | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| pj | 7 | 8 | 4 | 6 | 6 |
| dj | 9 | 17 | 18 | 19 | 21 |

### Página 41 — Número de trabajos Tardíos

Ejemplo: (misma tabla)

Respuesta:

1-2-3.
Se borra el trabajo 2 (más largo)
1-3-4-5
Se borra el trabajo 1 (el más largo
3-4-5-1-2 ( ΣU =2)

(Programa final calculado a partir de los datos:)

| Trabajo | Inicio | Fin = $C_j$ | $d_j$ | $T_j$ | $U_j$ |
|---|---|---|---|---|---|
| 3 | 0 | 4 | 18 | 0 | 0 |
| 4 | 4 | 10 | 19 | 0 | 0 |
| 5 | 10 | 16 | 21 | 0 | 0 |
| 1 | 16 | 23 | 9 | 14 | 1 |
| 2 | 23 | 31 | 17 | 14 | 1 |
| Total |  |  |  |  | $\sum U_j=2$ |

### Página 42 — Tardanza total

$$1||\sum T_j$$

Problema NP-hard

**Reglas:**

Si hay dos trabajos j y k tal que $p_j\le p_k$ & $d_j\le d_k$, existe entonces una secuencia optima en donde j se programa ANTES de K.

### Página 43 — Ejercicios

Se tienen los siguientes trabajos $1//\gamma$:

Trabajos

| j | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| pj | 5 | 7 | 2 | 8 |
| dj | 1 | 9 | 10 | 6 |
| wj | 2 | 3 | 2 | 1 |

Programe los trabajos con FIFO, SPT, EDD y ATC

- ¿Cuál regla minimiza el flujo ponderado promedio?
- ¿Cuál regla minimiza el retardo máximo?
- ¿Cuál regla minimiza la tardanza ponderada?

### Página 44 — Solución ejercicio reglas de despacho

**FIFO**

| Secuencia | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| pj | 5 | 7 | 2 | 8 |
| Cj | 5 | 12 | 14 | 22 |
| dj | 1 | 9 | 10 | 6 |
| cj - dj = Lj | 4 | 3 | 4 | 16 |
| wj | 2 | 3 | 2 | 1 |
| wjTj | 8 | 9 | 8 | 16 |

Flujo Promedio 13,25 · Retardo Max 16 · Tardanza Ponderada 41

**SPT**

| Secuencia | 3 | 1 | 2 | 4 |
|---|---|---|---|---|
| pj | 2 | 5 | 7 | 8 |
| Cj | 2 | 7 | 14 | 22 |
| dj | 10 | 1 | 9 | 6 |
| cj - dj = Lj | -8 | 6 | 5 | 16 |
| wj | 2 | 2 | 3 | 1 |
| wjTj | 0 | 12 | 15 | 16 |

Flujo Promedio 11,25 · Retardo Max 16 · Tardanza Ponderada 43

(Inicio de cada trabajo = $C_j-p_j$. FIFO: 1 [0,5], 2 [5,12], 3 [12,14], 4 [14,22]. SPT: 3 [0,2], 1 [2,7], 2 [7,14], 4 [14,22].)

### Página 45 — Solución ejercicio reglas de despacho

**EDD**

| Secuencia | 1 | 4 | 2 | 3 |
|---|---|---|---|---|
| pj | 5 | 8 | 7 | 2 |
| Cj | 5 | 13 | 20 | 22 |
| dj | 1 | 6 | 9 | 10 |
| cj - dj = Lj | 4 | 7 | 11 | 12 |
| wj | 2 | 1 | 3 | 2 |
| wjTj | 8 | 7 | 33 | 24 |

Flujo Promedio 15 · Retardo Max 12 · Tardanza Ponderada 72

**ATC**

| Secuencia | 1 | 3 | 2 | 4 |
|---|---|---|---|---|
| pj | 5 | 2 | 7 | 8 |
| Cj | 5 | 7 | 14 | 22 |
| dj | 1 | 10 | 9 | 6 |
| cj - dj = Lj | 4 | -3 | 5 | 16 |
| wj | 2 | 2 | 3 | 1 |
| wjTj | 8 | 0 | 15 | 16 |

Flujo Promedio 12 · Retardo Max 16 · Tardanza Ponderada 39

Índices ATC en cada decisión (resaltado en amarillo el elegido):

| | I (1) | I (2) | I (3) | I (4) |
|---|---|---|---|---|
| t=0 | **0,40** | 0,30 | 0,23 | 0,13 |
| t=5 |  | 0,43 | **0,58** | 0,13 |
| t=7 |  | **0,43** |  | 0,13 |

(Inicio de cada trabajo = $C_j-p_j$. EDD: 1 [0,5], 4 [5,13], 2 [13,20], 3 [20,22]. ATC: 1 [0,5], 3 [5,7], 2 [7,14], 4 [14,22]. Los índices coinciden con $K=1$ y $\bar p=5.5$, el promedio de los cuatro trabajos sin recalcular; con $\bar p$ recalculado, $I_3(5)=0.589$. Ver [atc.py](./atc.py).)

### Página 46 — Soluciones exactas

- Programación matemática
- Branch and Bound
- Programación Dinámica
- Enumeración exhaustiva!

### Página 47 — Tarea

- Presente en PAPEL un modelo de programación matemática para el problema de

$$1\,|\,r_j\,|\,\sum W_jC_j$$

### Página 48 — Solver de Excel

> [Imagen: captura de Excel del archivo "2.Single_Machine_TWT", hoja "Single Machine", junto al cuadro "Parámetros de Solver".]

Contenido legible de la hoja de Excel:

- Título: **Single machine total weighted tardiness scheduling problem**.
- Gantt de colores con 40 trabajos, en este orden: 1, 39, 19, 8, 7, 5, 32, 24, 33, 2, 31, 35, 11, 25, 21, 10, 20, 18, 38, 22, 40, 27, 28, 13, 26, 12, 14, 9, 16, 30, 3, 17, 34, 23, 4, 36, 37, 6, 15, 29 (18, 38, 27 y 9 son barras muy angostas; su lectura es dudosa).
- Makespan (Cmax) = **2065**; Tot Tardiness = **2637**; Tot Weigh. tardiness = **16822**.
- Nota: "(instance wt40_1 of OR_Library, http://people.brunel.ac.uk/~mastjjb/jeb/orlib/files/wt40.txt. Optimum TWT value=913)".
- Botones "Random Order" y "Draw Gantt".

Tabla "Job data" (filas visibles, trabajos 1-15):

| Job ID | Proc Time | Weight | Due Date |
|---|---|---|---|
| 1 | 26 | 1 | 1588 |
| 2 | 24 | 10 | 1620 |
| 3 | 79 | 9 | 1731 |
| 4 | 46 | 10 | 1773 |
| 5 | 32 | 10 | 1694 |
| 6 | 35 | 4 | 1487 |
| 7 | 73 | 3 | 1566 |
| 8 | 74 | 2 | 1844 |
| 9 | 14 | 10 | 1727 |
| 10 | 67 | 3 | 1636 |
| 11 | 86 | 7 | 1599 |
| 12 | 46 | 3 | 1539 |
| 13 | 78 | 1 | 1855 |
| 14 | 40 | 3 | 1645 |
| 15 | 29 | 10 | 1709 |

Tablas "GENETIC ALGORITHM ORDER" y "Machine 1" (filas visibles, primeras 15 posiciones):

| tasks | Proc Time | Weight | Due Date | Start | Completion | Tardiness | W.Tardiness |
|---|---|---|---|---|---|---|---|
| 1 | 26 | 1 | 1588 | 0 | 26 | 0 | 0 |
| 39 | 49 | 1 | 1579 | 26 | 75 | 0 | 0 |
| 19 | 90 | 4 | 1484 | 75 | 165 | 0 | 0 |
| 8 | 74 | 2 | 1844 | 165 | 239 | 0 | 0 |
| 7 | 73 | 3 | 1566 | 239 | 312 | 0 | 0 |
| 5 | 32 | 10 | 1694 | 312 | 344 | 0 | 0 |
| 32 | 28 | 4 | 1833 | 344 | 372 | 0 | 0 |
| 24 | 69 | 4 | 1795 | 372 | 441 | 0 | 0 |
| 33 | 39 | 9 | 1627 | 441 | 480 | 0 | 0 |
| 2 | 24 | 10 | 1620 | 480 | 504 | 0 | 0 |
| 31 | 44 | 7 | 1650 | 504 | 548 | 0 | 0 |
| 35 | 30 | 7 | 1541 | 548 | 578 | 0 | 0 |
| 11 | 86 | 7 | 1599 | 578 | 664 | 0 | 0 |
| 25 | 85 | 9 | 1522 | 664 | 749 | 0 | 0 |
| 21 | 35 | 5 | 1772 | 749 | 784 | 0 | 0 |

Cuadro **Parámetros de Solver**:

- Establecer objetivo: `$Q$16`
- Para: **Mín**
- Cambiando las celdas de variables: `TaskOrder`
- Sujeto a las restricciones: `TaskOrder = Todos diferentes`
- [x] Convertir variables sin restricciones en no negativas
- Método de resolución: **Evolutionary**

### Página 49 — ¡Gracias!

**¡Gracias!** — William Guerrero, Ph.D.

## Anexo: texto extraído automáticamente del PDF

> Texto plano tal como sale del PDF, sin fórmulas ni tablas que estén como imagen. La versión fiel y completa es la sección «Contenido completo» de arriba.

### Página 1 · 2 imagen(es)

Planeación, Programación y 
Control de las Operaciones
Programación de la 
Producción

### Página 2 · 1 imagen(es)

Modelos de una única máquina
• Es simple, pero es el caso especial de 
varios problemas de scheduling.
• Fundamento para varias heurísticas
• Descomposición de problemas más 
complejos
– Ejemplo: problema con un único cuello de 
botella.

### Página 3 · 1 imagen(es)

Programación de una máquina
• Problema: secuenciar n trabajos en la máquina 
de tal forma que se minimice un objetivo: 
Tiempo promedio de flujo, Tardanza Ponderada, 
Retardo máximo, Número de trabajos tardíos, etc. 
• En general los problemas de secuenciación de 
trabajos en una máquina son NP-hard!!

### Página 4 · 1 imagen(es)

¿Existe alguna otra forma de hallar una 
solución óptima al problema de una 
máquina?
• Supongamos que tenemos n trabajos para una 
máquina... y queremos minimizar Tardanza 
Ponderada Total. 
• Qué se puede hacer? 
• Enumeración exhaustiva: ¿Cuántas posibles 
secuencias hay??

### Página 5 · 2 imagen(es)

Posibles secuencias: n!

### Página 6 · 1 imagen(es)

Otras soluciones
• Algoritmos exactos
– Programación Dinámica
– Programación Entera Mixta 
 – Ramificación y Acotación 
• ¿Se usan los algoritmos exactos en la industria? 
• Hay algunas aplicaciones, la mayoría en líneas de 
producción (flow shop) . 
• Pero en general la programación es tan compleja que no 
existen modelos exactos y el caso es de hallar una 
“buena programación” que los encargados 
entiendan.

### Página 7 · 1 imagen(es)

¿Existen soluciones óptimas con reglas 
de despacho?
• Excepto en unos pocos casos, NO existen reglas 
de despacho (ej. SPT, CR, etc) que garanticen 
optimalidad. 
• Estas son unas excepciones: 
– La regla WSPT minimiza el flujo promedio ponderado 
1 // ΣwjCj
– La regla EDD minimiza el retardo máximo 1// Lmax

### Página 8 · 1 imagen(es)

Tiempo de terminación 
ponderado
1 | | ∑𝑤𝑗𝐶𝑗
• Wj puede ser el costo de almacenamiento o la 
prioridad del trabajo j.
• Reglas para resolverlo:
– Tiempo de procesamiento ponderado más corto.:
– Los trabajos se ordenan en orden decreciente de la 
relación: wj / pj.

### Página 9 · 1 imagen(es)

Tiempo de terminación 
ponderado
1 | | ∑𝑤𝑗𝐶𝑗
• Teorema: la regla de WSPT es optima para el 
problema. 
• Complejidad: O(n log n)

### Página 10 · 1 imagen(es)

Tiempo de terminación 
ponderado
1 | | ∑𝑤𝑗𝐶𝑗
• Ejemplo:
tarea
Tiempo de 
proceso
Ponderación
A
15
4
B
44
5
C
67
1
D
13
3
E
10
2

### Página 11 · 1 imagen(es)

Reglas de despacho 
(Políticas de programación)
• Son la forma más simple de programación. 
• Una regla de despacho asigna prioridades de 
procesamiento a los trabajos que se encuentran en la 
cola de una máquina en un momento dado. 
• Infinidad de reglas de despacho para secuenciar 
trabajos. 
• Dos tipos de reglas: Estáticas y Dinámicas 
• Estáticas: Dependen de los parámetros de los trabajos (fecha 
de entrega, tiempo de proceso, etc.) pero no del tiempo o status 
de las máquinas. 
• Dinámicas: Dependientes del tiempo o status de las máquinas.

### Página 12 · 1 imagen(es)

Reglas de despacho estáticas
• FCFS (First Come First Served) o FIFO
• SPT (Shortest Processing Time) First 
pj ≤ pj+1 (pj es el tiempo de proceso del trabajo programado en la 
j-ésima posición) 
• EDD (Earliest Due Date) First
 dj ≤ dj+1 (dj es la fecha de entrega del trabajo programado en la j-
ésima posición)
• WSPT (Weighted Shortest Processing Time) 
wj / pj ≥ wj+1 / pj+1 Programa primero los trabajos con mayor 
prioridad y menor tiempo de proceso

### Página 13 · 1 imagen(es)

Reglas de despacho dinámicas
• MS (Minimum Slack)
– El slack es el tiempo remanente para cumplir con la 
fecha de entrega. 
sj = max(dj – pj – t, 0) 
Secuenciación: s[k] ≤ s[k+1] 
• ATC (Aparent Tardiness Cost) 
𝐼𝑗𝑡= 𝑤𝑗
𝑝𝑗
𝑒
−max(𝑑𝑗−𝑝𝑗−𝑡,0)
𝐾 ҧ𝑝
K: Constante a determinar 
ҧ𝑝 : Tiempo promedio de los trabajos no programados 
Secuenciación I[k] ≥ I[k+1]

### Página 14 · 1 imagen(es)

Restricciones de precedencia
• Supongamos restricciones de precedencia 
en cadena:

### Página 15 · 1 imagen(es)

Restricciones de precedencia
Si el decisor debe completar la cadena, una vez 
iniciada, ¿cuál cadena debe hacer primero para 
minimizar el tiempo total?
RTA: es optimo iniciar con la cadena con mayor 
relación: 
∑𝑤𝑗
∑𝑝𝑗

### Página 16 · 1 imagen(es)

Restricciones de precedencia
• ¿Qué pasa si la restricción no es necesaria?
• Definimos 𝑙∗ llamado el trabajo que determina el 
𝜌−𝑓𝑎𝑐𝑡𝑜𝑟
∑𝑗=1
𝑙∗
𝑤𝑗
∑𝑗=1
𝑙∗
𝑝𝑗
= max
1≤𝑙≤𝑘
∑𝑗=1
𝑙
𝑤𝑗
∑𝑗=1
𝑙
𝑝𝑗

### Página 17 · 1 imagen(es)

Restricciones de precedencia
Reglas de secuenciación:
• Se debe procesar una cadena de trabajos hasta 𝑙∗ sin 
interrupción.
• Seleccione la cadena que esté disponible con el mayor 
𝜌−𝑓𝑎𝑐𝑡𝑜𝑟

### Página 18 · 1 imagen(es)

Ejemplo
Considerando las cadenas:
1 -> 2 -> 3 -> 4
5 -> 6 -> 7
trabajo
1
2
3
4
5
6
7
Wj
6
18
12
8
8
17
18
pj
3
6
6
5
4
8
10

### Página 19 · 1 imagen(es)

Ejemplo
Considerando las cadenas:
1 -> 2 -> 3 -> 4 tiene un 𝜌−𝑓𝑎𝑐𝑡𝑜𝑟 = 2.66 determinado por el trabajo 2.
5 -> 6 -> 7 tiene un 𝜌−𝑓𝑎𝑐𝑡𝑜𝑟 = 2.08 determinado por el trabajo 6
trabajo
1
2
3
4
5
6
7
Wj
6
18
12
8
8
17
18
pj
3
6
6
5
4
8
10

### Página 20 · 1 imagen(es)

Ejemplo:
Secuencia: 1-> 2 ->
Se repiten los cálculos de la cadena 1.
• 3 -> 4 tiene un 𝜌−𝑓𝑎𝑐𝑡𝑜𝑟 = 2 determinado por 
el trabajo 3.

### Página 21 · 1 imagen(es)

Ejemplo:
Secuencia: 1-> 2 -> 5 -> 6 -> 
Se repiten los cálculos de la cadena 2.
• 7 tiene un 𝜌−𝑓𝑎𝑐𝑡𝑜𝑟 = 1.8

### Página 22 · 1 imagen(es)

Ejemplo:
Secuencia: 1-> 2 -> 5 -> 6 -> 3
Se repiten los cálculos de la cadena 1.
• 4 tiene un 𝜌−𝑓𝑎𝑐𝑡𝑜𝑟 = 1.6

### Página 23 · 1 imagen(es)

Ejemplo:
Secuencia: 1-> 2 -> 5 -> 6 -> 3 -> 7 -> 4

### Página 24 · 1 imagen(es)

tiempos de liberación
1 | 𝑟𝑗, 𝑝𝑟𝑚𝑝 | ∑𝑤𝑗𝐶𝑗
Considerando preemption
Regla de secuenciación:
En cualquier momento del tiempo, el trabajo con la 
mayor tasa de prioridad sobre tiempo de trabajo 
faltante se selecciona. 
• No necesariamente es óptimo.

### Página 25 · 1 imagen(es)

Ejercicio
Implemente la regla mostrada para este ejercicio:
trabajo
1
2
3
4
5
6
7
pj
6
18
12
10
10
17
16
rj
0
0
0
14
25
25
50

### Página 26 · 1 imagen(es)

Reglas de despacho cuando los trabajos no 
están todos disponibles en todo momento
• Idea: En el tiempo t ordenar los trabajos de la cola de la 
máquina de acuerdo a un criterio (regla), seleccionar 
algún trabajo (digamos j*) y programarlo. 
• Una vez programado el trabajo j*, actualizar el tiempo t 
(se actualiza por eventos) y seleccionar el siguiente 
trabajo a programar. Repetir hasta que no haya nuevos 
trabajos que programar. 
• Los eventos pueden ser la llegada de nuevos trabajos o 
la liberación de la máquina.

### Página 27 · 1 imagen(es)

Tardanza máxima
• 1| prec | Lmax es un caso especial de 1| prec | h max
• h max = f ( Cj )
• La función objetivo está parametrizada en términos de 
Cj

### Página 28 · 1 imagen(es)

Tardanza máxima
• 1| prec | h max
• Algoritmo:
1. Conjunto J = {}, Jc = {todos los trabajos}, J’ = {trabajos 
sin sucesor}
2. Elija el trabajo j*
ℎ𝑗∗
 ෍
𝑗∈𝐽𝑐
𝑝𝑗
= min
𝑗∈𝐽′
ℎ𝑗
෍
𝑘∈𝐽𝑐
𝑝𝑘
Añadir j* a J (al final), borrar j* de Jc, modificar J’
3. Parar cuando no haya más trabajos. Regrese a 2 d.l.c.

### Página 29 · 1 imagen(es)

Tardanza máxima
• Ejemplo.
• Makespan = 10 
job
1
2
3
pj
2
3
5
hj(cj)
1+C1
1.2C2
10

### Página 30 · 1 imagen(es)

Tardanza máxima
• Ejemplo.
• Makespan = 10
• ℎ3 10 = 10 < ℎ1 10 = 11 < ℎ2 10 = 12 
• 3 es el último trabajo.
• Inicia su procesamiento en t = 5
job
1
2
3
pj
2
3
5
hj(cj)
1+C1
1.2C2
10

### Página 31 · 1 imagen(es)

Tardanza máxima
• Ejemplo.
• T = 5
• ℎ1 5 = 6, ℎ2 5 = 6 
• Elegir cualquiera:
• 1-2-3 y 2-1-3 son secuencias optimas.
job
1
2
3
pj
2
3
5
hj(cj)
1+C1
1.2C2
10

### Página 32 · 1 imagen(es)

Tardanza máxima
• Para el caso de 1|| L max
• La función de costos ℎ𝑗= 𝐶𝑗−𝑑𝑗
• La regla óptima para programar es Earliest Due Date First
• La generalización 1| 𝑟𝑗 | Lmax es NP-hard
• Procedimientos de enumeración como Branch-and-bound

### Página 33 · 2 imagen(es)

Regla de la razón crítica (CR)
𝐶𝑅= 𝑇𝑖𝑒𝑚𝑝𝑜 𝑞𝑢𝑒 𝑟𝑒𝑠𝑡𝑎 ℎ𝑎𝑠𝑡𝑎 𝑙𝑎 𝑓𝑒𝑐ℎ𝑎 𝑑𝑒 𝑒𝑛𝑡𝑟𝑒𝑔𝑎
𝑇𝑖𝑒𝑚𝑝𝑜 𝑑𝑒 𝑝𝑟𝑜𝑐𝑒𝑠𝑎𝑚𝑖𝑒𝑛𝑡𝑜 𝑟𝑒𝑠𝑡𝑎𝑛𝑡𝑒
𝐶𝑅𝑗= max(𝑑𝑗−𝑡, 0)
𝑝𝑗
•
Secuenciar el trabajo con min CR.
•
Desempate por SPT

### Página 34 · 5 imagen(es)

Regla de la razón crítica (CR)

### Página 35 · 5 imagen(es)

Regla de la razón crítica (CR)

### Página 36 · 5 imagen(es)

Regla de la razón crítica (CR)

### Página 37 · 5 imagen(es)

Regla de la razón crítica (CR)

### Página 38 · 1 imagen(es)

Número de trabajos Tardíos 
1|| ෍𝑈𝑗
Algoritmo de solución (forward):
Definir 
• J = {trabajos programados}
• Jd = {trabajos que no cumplirán su due date}
• Jc = {trabajos pendientes por programar}

### Página 39 · 1 imagen(es)

Número de trabajos Tardíos 
Algoritmo de solución (forward):
1.
J = {}, Jd = {}, Jc = {1, …, n}
2.
Calcular j*
𝑑𝑗∗= min
𝑗∈𝐽𝑐𝑑𝑗
Añadir j* a J
Borrar j* de Jc
Paso 3.
3.
Si ∑𝑗∈𝐽𝑝𝑗≤𝑑𝑗∗ir al paso 4.
Si no, defina k* tal que 
𝑝𝑘∗= max
𝑗∈𝐽(𝑝𝑗)
Borrar k* de J
Añadir k* a Jd
 4. Si Jc = { } Parar. Si no, regresar a 2.

### Página 40 · 1 imagen(es)

Número de trabajos Tardíos 
Ejemplo:
job
1
2
3
4
5
pj
7
8
4
6
6
dj
9
17
18
19
21

### Página 41 · 1 imagen(es)

Número de trabajos Tardíos 
Ejemplo:
Respuesta:
1-2-3. 
Se borra el trabajo 2 (más largo)
1-3-4-5
Se borra el trabajo 1 (el más largo
3-4-5-1-2 ( ΣU =2)
job
1
2
3
4
5
pj
7
8
4
6
6
dj
9
17
18
19
21

### Página 42 · 1 imagen(es)

Tardanza total
1|| ෍𝑇𝑗
Problema NP-hard
Reglas: 
Si hay dos trabajos j y k tal que 𝑝𝑗≤𝑝𝑘 & 𝑑𝑗≤𝑑𝑘, existe entonces una 
secuencia optima en donde j se programa ANTES de K.

### Página 43 · 2 imagen(es)

Ejercicios 
Se tienen los siguientes trabajos 1// 𝛾:
Programe los trabajos con FIFO, SPT, EDD y ATC 
• ¿Cuál regla minimiza el flujo ponderado promedio? 
• ¿Cuál regla minimiza el retardo máximo?
• ¿Cuál regla minimiza la tardanza ponderada?

### Página 44 · 2 imagen(es)

Solución ejercicio reglas de despacho

### Página 45 · 3 imagen(es)

Solución ejercicio reglas de despacho

### Página 46 · 1 imagen(es)

Soluciones exactas
• Programación matemática 
• Branch and Bound 
• Programación Dinámica 
• Enumeración exhaustiva!

### Página 47 · 1 imagen(es)

Tarea
• Presente en PAPEL un modelo de programación 
matemática para el problema de 
1 𝑟𝑗∑𝑊𝑗𝐶𝑗

### Página 48 · 3 imagen(es)

Solver de Excel

### Página 49 · 1 imagen(es)

¡Gracias!
William Guerrero, Ph.D.

