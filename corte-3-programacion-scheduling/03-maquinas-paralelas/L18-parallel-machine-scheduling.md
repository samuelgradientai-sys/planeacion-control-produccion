# L18-parallel-machine-scheduling

> **Archivo:** [`L18-parallel-machine-scheduling.pdf`](./L18-parallel-machine-scheduling.pdf) · **Corte 3** · 40 páginas  
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
| 26 | El mismo ejemplo con LFM | La diapositiva no lo resuelve. El [compendio](../00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md) obtiene $C_{max}=2$ |
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

- [lns-maquinas-paralelas.md](./lns-maquinas-paralelas.md): plantilla de Excel para asignar 15 trabajos a 3 máquinas paralelas (incompleta).
- [metodos-programacion-produccion-corte3.md](../00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md): hojas `07_Paralelas_LPT_SPT` (ejemplos de las pp. 8-14) y `08_Paralelas_Restric` (LNS/CP de la p. 19 y LFJ/LFM de las pp. 22-26).
- Fundamentos de una máquina (SPT, WSPT, EDD, cadenas): [L17](../02-una-maquina/L17-single-machine-scheduling.md).
- Notación $\alpha|\beta|\gamma$: [L16](../01-introduccion-scheduling/L16-intro-scheduling.md).
- El *flexible flow shop* generaliza las máquinas paralelas a varias etapas: [L19](../04-flow-shop/L19-flow-shop-scheduling.md), pp. 37-41.
- El reto 2 de la competencia es un problema de 3 máquinas paralelas con liberaciones y precedencias: [proyecto-competencia-scheduling](../proyecto-competencia-scheduling/).

## Contenido completo (página por página)

### Página 1 — Portada

"Programación de la Producción" (subrayado), "2026".

> [Imagen decorativa: foto del campus en tonos azules, logo "Universidad de La Sabana – Colombia" e ícono de licencia Creative Commons BY-NC-SA.]

### Página 2 — Modelos de máquinas en paralelo

- Es un caso especial del Flexible flow shop.
- Objetivos:
  - Minimizar el makespan
  - Tiempo de terminación total (tiempo de flujo)
  - Tardanza máxima
- Decisiones:
  - Asignar trabajos a las máquinas
  - Secuencia de trabajos.

### Página 3 — Supuestos y definiciones

- Existen varias máquinas/servidores
- El trabajo *j* tiene un solo proceso y puede ejecutarse en cualquiera de ellas.
- Todas las máquinas son idénticas
  - Para un trabajo, el tiempo de procesamiento es el mismo independientemente de la máquina. Ej.: máquinas de moldeo por inyección
- Máquinas no idénticas (o no homogéneas)
  - Las máquinas tienen diferentes velocidades de procesamiento y el tiempo de proceso depende de la máquina elegida. Ej.: impresoras

### Página 4 — El Pm/β/γ es una extensión del 1/β/γ

- No existen reglas de despacho que GARANTICEN la solución óptima, excepto algunos casos particulares
- Las reglas de despacho se implementan usando ALGORITMOS DE LISTA.
- Una LISTA es una secuencia de trabajos ordenados de acuerdo a la regla de despacho seleccionada.
- El programa de producción se genera asignando los trabajos en la lista a la máquina con menor carga asignada (menor tiempo de terminación).

### Página 5 — Ejemplo

> [Diagrama: arriba, una barra titulada "Trabajos" con cinco bloques de colores en orden 1 (rojo), 2 (morado), 3 (azul), 4 (azul oscuro) y 5 (verde). Las longitudes decrecen de 1 a 5, así que la lista está en orden LPT. Abajo, "Diagrama de Gantt (2 máquinas)" sin eje de tiempo: la máquina 1 procesa 1 y luego 4; la máquina 2 procesa 2, luego 3 y luego 5. La máquina 2 termina después que la máquina 1.]

La diapositiva no tiene escala de tiempo. La tabla da las posiciones medidas en el dibujo (en píxeles divididos por 10, desde el inicio de las barras), solo como referencia de proporciones:

| Máquina | Trabajo | Inicio (aprox.) | Fin (aprox.) |
|---|---|---|---|
| Máquina 1 | 1 | 0 | 25.5 |
| Máquina 1 | 4 | 25.5 | 38.7 |
| Máquina 2 | 2 | 0 | 20.8 |
| Máquina 2 | 3 | 20.8 | 36.8 |
| Máquina 2 | 5 | 36.8 | 46.2 |

El orden coincide con el algoritmo de lista: 1 → M1, 2 → M2, 3 → M2 (M2 tiene menos carga), 4 → M1 y 5 → M2.

### Página 6 — Min Makespan sin Preemptions

$Pm||C_{max}$

- Al minimizar el makespan, se balancea la carga entre las máquinas.
- Es equivalente al problema de partición

> [Diagrama: ejes de tiempo con dos filas, M1 y M2, cada una con cuatro bloques de anchos distintos. Ambas filas terminan en la misma línea vertical, marcada $C^*_{max}$: la carga queda balanceada.]

### Página 7 — Heurística de solución

- Algoritmo de lista. Regla: *Longest processing time first (LPT)*
- Asignar en paralelo los trabajos más largos primero, en la primera máquina en estar disponible.
- Teorema: Garantía de desempeño

$$\frac{C_{max}(LPT)}{C_{max}(OPT)}\le\frac{4}{3}-\frac{1}{3m}$$

### Página 8 — Ejemplo $P_3||C_{max}$

| j | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $p_j$ | 1 | 3 | 4 | 6 | 9 | 10 | 10 | 11 | 12 | 13 | 13 | 14 | 16 | 18 | 19 |

Debajo hay una tabla vacía con tres bloques (Máquina 1, Máquina 2, Máquina 3), cada uno con columnas j, pj y cj, para llenar en clase.

### Página 9 — Ejemplo $P_3||C_{max}$ (solución con LPT)

| Máquina 1: j | pj | cj | Máquina 2: j | pj | cj | Máquina 3: j | pj | cj |
|---|---|---|---|---|---|---|---|---|
| 15 | 19 | 19 | 14 | 18 | 18 | 13 | 16 | 16 |
| 10 | 13 | 32 | 11 | 13 | 31 | 12 | 14 | 30 |
| 7 | 10 | 42 | 8 | 11 | 42 | 9 | 12 | 42 |
| 6 | 10 | 52 | 5 | 9 | 51 | 4 | 6 | 48 |
| 1 | 1 | 53 | 2 | 3 | 54 | 3 | 4 | 52 |

$$C_{max}=54\qquad\sum C_j=582$$

Gantt equivalente (inicio $=c_j-p_j$):

| Máquina | Trabajo | Inicio | Fin |
|---|---|---|---|
| M1 | 15 | 0 | 19 |
| M1 | 10 | 19 | 32 |
| M1 | 7 | 32 | 42 |
| M1 | 6 | 42 | 52 |
| M1 | 1 | 52 | 53 |
| M2 | 14 | 0 | 18 |
| M2 | 11 | 18 | 31 |
| M2 | 8 | 31 | 42 |
| M2 | 5 | 42 | 51 |
| M2 | 2 | 51 | 54 |
| M3 | 13 | 0 | 16 |
| M3 | 12 | 16 | 30 |
| M3 | 9 | 30 | 42 |
| M3 | 4 | 42 | 48 |
| M3 | 3 | 48 | 52 |

(Comprobación propia: $\sum C_j=198+196+188=582$. $\sum p_j=159$, así que $C^*_{max}\ge159/3=53$; LPT queda a una unidad de esa cota.)

### Página 10 — Ejemplo: Reglas de despacho

- Calcule el makespan para LPT y SPT del siguiente ejemplo:
- $3||C_{max}$

| job | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| p(i) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |

- ¿Cuál es su cota superior?

(La diapositiva no trae la solución. Cálculo propio con algoritmo de lista y empates a la máquina de menor índice:

| Regla | Máquina 1 | Máquina 2 | Máquina 3 | $C_{max}$ |
|---|---|---|---|---|
| LPT | 10 [0-10], 5 [10-15], 4 [15-19] | 9 [0-9], 6 [9-15], 3 [15-18] | 8 [0-8], 7 [8-15], 2 [15-17], 1 [17-18] | 19 |
| SPT | 1 [0-1], 4 [1-5], 7 [5-12], 10 [12-22] | 2 [0-2], 5 [2-7], 8 [7-15] | 3 [0-3], 6 [3-9], 9 [9-18] | 22 |

$\sum p_j=55$ y $\lceil55/3\rceil=19$, así que LPT es óptimo aquí. La garantía de la p. 7 acota LPT por $\frac{11}{9}C_{max}(OPT)$.)

### Página 11 — Ejemplo: Reglas de despacho

- Asignar los trabajos en las máquinas con menos tiempo asignado de acuerdo a la regla SPT y LPT
- $P4||C_{max}$

| job | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| p(j) | 7 | 7 | 6 | 6 | 5 | 5 | 4 | 4 | 4 |

### Página 12 — LPT

> [Diagrama: captura de un programa de Gantt con fondo beige, eje superior de 1 a 15 y cuatro filas, una por máquina. Las etiquetas verdes de las filas son ilegibles; se leen como máquinas 1 a 4 de arriba abajo. Cada barra se rotula J001…J009 (trabajo 1…9).]

| Máquina | Trabajo | Inicio | Fin |
|---|---|---|---|
| 1 | J001 | 0 | 7 |
| 1 | J007 | 7 | 11 |
| 1 | J009 | 11 | 15 |
| 2 | J002 | 0 | 7 |
| 2 | J008 | 7 | 11 |
| 3 | J003 | 0 | 6 |
| 3 | J005 | 6 | 11 |
| 4 | J004 | 0 | 6 |
| 4 | J006 | 6 | 11 |

$C_{max}(LPT)=15$. (Cálculo propio: $\sum C_j=85$.)

### Página 13 — SPT

> [Diagrama: el mismo tipo de captura, con eje de 1 a 17.]

| Máquina | Trabajo | Inicio | Fin |
|---|---|---|---|
| 1 | J007 | 0 | 4 |
| 1 | J006 | 4 | 9 |
| 1 | J002 | 9 | 16 |
| 2 | J008 | 0 | 4 |
| 2 | J003 | 4 | 10 |
| 3 | J009 | 0 | 4 |
| 3 | J004 | 4 | 10 |
| 4 | J005 | 0 | 5 |
| 4 | J001 | 5 | 12 |

$C_{max}(SPT)=16$. (Cálculo propio: $\sum C_j=74$, menor que con LPT, como se espera de SPT.)

### Página 14 — Óptimo

> [Diagrama: el mismo tipo de captura, con eje de 1 a 15. Las cuatro máquinas terminan en 12.]

| Máquina | Trabajo | Inicio | Fin |
|---|---|---|---|
| 1 | J009 | 0 | 4 |
| 1 | J008 | 4 | 8 |
| 1 | J007 | 8 | 12 |
| 2 | J003 | 0 | 6 |
| 2 | J004 | 6 | 12 |
| 3 | J002 | 0 | 7 |
| 3 | J005 | 7 | 12 |
| 4 | J001 | 0 | 7 |
| 4 | J006 | 7 | 12 |

$C^*_{max}=12=48/4$: la carga queda perfectamente balanceada. LPT/OPT $=15/12=1.25$, exactamente la garantía $4/3-1/(3\cdot4)$ (observación propia).

### Página 15 — ¿Cómo hallamos el óptimo?

- Enumeración
  - Notar que es un problema doble: Asignación y secuenciación
  - ¿Cuántas soluciones hay?
  - El número de soluciones se puede calcular así:

$$\binom{n-1}{m-1}\frac{n!}{m!}$$

- Modelo matemático Programación Mixta
- Branch & Bound

### Página 16 — Solución óptima para $Pm||\sum C_j$

- La regla SPT soluciona a optimalidad $Pm||\sum C_j$

| Job # | $p_j$ |
|---|---|
| 6 | 2 |
| 10 | 2 |
| 3 | 3 |
| 7 | 3 |
| 9 | 4 |
| 1 | 5 |
| 8 | 5 |
| 2 | 6 |
| 5 | 7 |
| 4 | 8 |

- Máquina 1: Jobs 6-7-8-4
- Máquina 2: Jobs 10-9-2
- Máquina 3: Jobs 3-1-5

$$\sum C_j=81\qquad C_{max}=18$$

Gantt calculado con los $p_j$ de la tabla:

| Máquina | Trabajo | Inicio | Fin |
|---|---|---|---|
| 1 | 6 | 0 | 2 |
| 1 | 7 | 2 | 5 |
| 1 | 8 | 5 | 10 |
| 1 | 4 | 10 | 18 |
| 2 | 10 | 0 | 2 |
| 2 | 9 | 2 | 6 |
| 2 | 2 | 6 | 12 |
| 3 | 3 | 0 | 3 |
| 3 | 1 | 3 | 8 |
| 3 | 5 | 8 | 15 |

(Comprobación: $(2+5+10+18)+(2+6+12)+(3+8+15)=35+20+26=81$.)

### Página 17 — Min *Makespan* sin *Preemptions* y restricciones de precedencia

- $Pm|prec|C_{max}$
- Fuertemente NP-hard
- Reglas aplicables:
  - Critical Path (CP)
  - Máximo número de sucesores (LNS)

### Página 18 — Critical Path

- Se le da prioridad al trabajo con la cadena más larga de trabajos en el grafo de precedencias.
- Cuando el tiempo más corto = tiempo más tarde de terminación, el nodo hace parte de la ruta crítica.
- Los empates se rompen arbitrariamente.
- E.g.:

> [Diagrama: grafo de precedencias con 7 nodos sin rótulo (círculos celestes). Llamándolos A-G de izquierda a derecha y de arriba abajo: A → B, B → C, D → C, C → G, E → F, F → G. La cadena más larga es A → B → C → G.]

### Página 19 — Comparación

- Con el siguiente ejemplo, todos los trabajos tienen una duración de 1, ¿cuál regla da un mejor Cmax?
  - LNS, CP.

> [Diagrama: grafo de 6 nodos negros numerados. Arcos: 1 → 2, 2 → 3, 4 → 3, 4 → 5, 6 → 3, 6 → 5.]

(La diapositiva no indica el número de máquinas ni la respuesta. Análisis propio con $m=2$, como en la hoja `08_Paralelas_Restric` del compendio. Sucesores totales: 1 tiene 2 (2 y 3), 4 tiene 2 (3 y 5), 6 tiene 2 (3 y 5), 2 tiene 1, y 3 y 5 no tienen. Cadena más larga desde cada nodo: 1 → 3 nodos; 2, 4 y 6 → 2; 3 y 5 → 1.
- **CP:** en $t=0$ elige 1 y luego 4 o 6; en $t=1$, 2 y el otro de 4/6; en $t=2$, 3 y 5. $C_{max}=3$.
- **LNS:** en $t=0$ empatan 1, 4 y 6. Si elige 1 y 4 (o 1 y 6) obtiene $C_{max}=3$. Si elige 4 y 6, el programa queda 4,6 | 1,5 | 2 | 3 y $C_{max}=4$. Por eso CP es al menos tan buena como LNS en este ejemplo.)

### Página 20 — Restricciones de maquinaria

- $Pm|p_j=1,M_j|C_{max}$
- Es decir, el trabajo j sólo se puede procesar en el conjunto de máquinas Mj
- Regla: *Least flexible Job first* (*LFJ*).
  - Cada vez que una máquina se libera, se selecciona el trabajo que pueda ser procesado en el conjunto más pequeño de máquinas.
- Teorema: *LFJ es óptima para $Pm|p_j=1,M_j|C_{max}$ con Mj anidados*

### Página 21 — Conjuntos anidados

- Se debe cumplir una de las siguientes condiciones:
  - $M_j$ es igual a $M_k$
  - $M_j$ es un subconjunto de $M_k$
  - $M_k$ es un subconjunto de $M_j$
  - $M_j$ y $M_k$ son conjuntos disjuntos.

### Página 22 — Ejemplo

- Considere el problema $P4|p_j=1,M_j|C_{max}$ con 8 trabajos.
  - $M_1=\{1,2\}$
  - $M_2=M_3=\{1,3,4\}$
  - $M_4=\{2\}$
  - $M_5=M_6=M_7=M_8=\{3,4\}$

(Los conjuntos **no** son anidados: $M_1=\{1,2\}$ y $M_2=\{1,3,4\}$ se cruzan sin que uno contenga al otro. Por eso el teorema de la p. 20 no garantiza que LFJ sea óptima.)

### Página 23 — Una solución (paso 1, $t=0$)

- Maq1: 1
- Maq2: 4
- Maq3: 5
- Maq4: 6

### Página 24 — Una solución (paso 2, $t=1$)

- Maq1: 1-2
- Maq2: 4
- Maq3: 5-7
- Maq4: 6-8

### Página 25 — Una solución (paso 3, $t=2$)

- Maq1: 1-2
- Maq2: 4
- Maq3: 5-7-3
- Maq4: 6-8

Cmax = 3

Gantt de la solución LFJ (cada trabajo dura 1):

| Máquina | Trabajo | Inicio | Fin |
|---|---|---|---|
| 1 | 1 | 0 | 1 |
| 1 | 2 | 1 | 2 |
| 2 | 4 | 0 | 1 |
| 3 | 5 | 0 | 1 |
| 3 | 7 | 1 | 2 |
| 3 | 3 | 2 | 3 |
| 4 | 6 | 0 | 1 |
| 4 | 8 | 1 | 2 |

(Lógica de LFJ, deducida: en $t=0$ la máquina 1 toma el trabajo 1 ($|M_1|=2$) antes que el 2 o el 3 ($|M|=3$). La máquina 2 toma el 4 ($|M_4|=1$). Las máquinas 3 y 4 toman trabajos de flexibilidad 2. En $t=1$ la máquina 2 queda ociosa, porque ya no le quedan trabajos elegibles, y el trabajo 3 tiene que esperar a $t=2$. Un programa con $C_{max}=2$ existe (cálculo propio): Maq1: 2-3, Maq2: 1-4, Maq3: 5-7, Maq4: 6-8.)

### Página 26 — Least flexible machine first

- Menor Número de trabajos pendientes que una máquina puede procesar.
- Resolvamos el ejercicio anterior.

(La diapositiva no muestra la solución. En el ejemplo, las máquinas 1, 2, 3 y 4 pueden procesar 3, 2, 6 y 6 trabajos. La hoja `08_Paralelas_Restric` del [compendio](../00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md) obtiene con LFM: M1: 2-3, M2: 1-4, M3: 6-8, M4: 5-7, $C_{max}=2$.)

### Página 27 — Tarea

- Formular el modelo de programación matemática para el $Pm|M_j|C_{max}$

### Página 28 — Minimizar el Makespan con Preemptions

- $Pm|prmp|C_{max}$
- Modelo de programación matemática
- Sea $X_{ij}$ = tiempo que el trabajo j pasa en la máquina i.
- Variable positiva.

### Página 29 — Minimize Cmax

- Sujeto a:

$$\sum_{i=1}^{m}x_{ij}=p_j,\qquad j=1,\dots,n$$
$$\sum_{i=1}^{m}x_{ij}\le C_{max},\qquad j=1,\dots,n$$
$$\sum_{j=1}^{n}x_{ij}\le C_{max},\qquad i=1,\dots,m$$

### Página 30 — Propiedad matemática

- La solución óptima cumple la siguiente condición:
- $C_{max}\ge\max\left(p_{max},\sum_{j=1}^{n}\frac{p_j}{m}\right)=C_{max}^*$

### Página 31 — Algoritmo

- Paso 1: Programe una máquina con todos los trabajos, en cualquier orden. Calcule m\*Cmax.
- Paso 2: Parta el programa en m partes.
- Paso 3: Asigne las partes a las máquinas.

### Página 32 — Alternativa

- Utilice la regla Longest remaining processing time first.
- Desventaja: el número de preemptions es infinito.

### Página 33 — $Pm||\sum C_j$

- SPT es la regla óptima para este problema.
- Considere dos máquinas.

| job | 1 | 2 | 3 |
|---|---|---|---|
| Pj | 1 | 1 | 3 |

(Cálculo propio: SPT pone 1 y 2 en paralelo en $[0,1]$ y el 3 en $[1,4]$; $\sum C_j=6$.)

### Página 34 — $Pm||\sum W_jC_j$

- WSPT NO es la regla óptima para este problema.
- Considere dos máquinas.

| job | 1 | 2 | 3 |
|---|---|---|---|
| Pj | 1 | 1 | 3 |
| wj | 1 | 1 | 3 |

(Cálculo propio: los tres trabajos tienen $w_j/p_j=1$, así que WSPT puede dejar el 3 de último: 1 y 2 en $[0,1]$ y 3 en $[1,4]$, con $\sum w_jC_j=1+1+12=14$. El óptimo es 3 en $[0,3]$ en una máquina y 1, 2 en $[0,1]$, $[1,2]$ en la otra: $\sum w_jC_j=9+1+2=12$.)

### Página 35 — $Pm|prec|\sum C_j$ y $Pm|M_j|\sum C_j$

$Pm|prec|\sum C_j$:
- NP-hard
- Revisar la regla de CP.

$Pm|M_j|\sum C_j$:
- NP-hard
- Revisar la regla Least flexible job

### Página 36 — $Rm||\sum C_j$

- Varias máquinas que trabajan a velocidades diferentes
- Modelo MIP
- Sea $x_{ikj}=1$ si el trabajo j se programa en la posición k de la máquina i (**de atrás hacia adelante**, en rojo), 0 d.l.c. *Ejemplo: k=1 para la última posición.*
- Sea $p_{ij}$ el tiempo de procesamiento del trabajo j en la máquina i.

### Página 37 — Modelo $Rm||\sum C_j$

$$\min\ \sum_{i=1}^{m}\sum_{j=1}^{n}\sum_{k=1}^{n}k\,p_{ij}\,x_{ikj}$$

Sujeto a:

- $\sum_{i=1}^{m}\sum_{k=1}^{n}x_{ikj}=1,\quad j=1,\dots,n$
- $\sum_{j=1}^{n}x_{ikj}\le1,\quad i=1,\dots,m,\ k=1,\dots,n$
- $x_{ikj}$ es binaria

### Página 38 — Explicación ($Rm||\sum C_j$)

- Suponga la secuencia 5-7-4

> [Diagrama: barra con tres bloques consecutivos rotulados 5, 7 y 4; el 7 es el más ancho y el 4 el más angosto.]

$$C_5=P_5$$
$$C_7=P_5+P_7$$
$$C_4=P_5+P_7+P_4$$
$$\text{F.O.}=C_5+C_7+C_4=3P_5+2P_7+P_4$$

*Como el trabajo 5 está en la posición 3 (de atrás hacia adelante), su tiempo cuenta en la F.O. tres veces.*

### Página 39 — Solver de Excel

> [Imagen: captura de Excel del libro "3.Unrelated_Parallel_Machines". Muestra las pestañas ARCHIVO, INICIO, INSERTAR, DISEÑO DE PÁGINA, FÓRMULAS, DATOS, REVISAR, VISTA y DESARROLLADOR, y dos botones de macro: "Random Assignment" y "Draw Gantt".]

Fila 1: **Unrelated parallel machines scheduling problem**. Debajo hay un gráfico de Gantt con 5 filas (máquinas 1 a 5 de arriba abajo; la numeración se deduce de la tabla).

**Makespan (Cmax) = 39** (recuadro rojo) · **Lower Bound = 30**

**Job data – Processing Times** (filas 10-15 visibles; los trabajos 7-10 quedan fuera de la captura):

| Job ID | Máq. 1 | Máq. 2 | Máq. 3 | Máq. 4 | Máq. 5 |
|---|---|---|---|---|---|
| 1 | 47 | 15 | 38 | 10 | 38 |
| 2 | 23 | 20 | 39 | 46 | 24 |
| 3 | 38 | 10 | 26 | 36 | 40 |
| 4 | 27 | 27 | 29 | 27 | 17 |
| 5 | 12 | 31 | 35 | 40 | 49 |
| 6 | 22 | 47 | 31 | 23 | 21 |

**GENETIC ALGORITHM ORDER:**

| Job ID | Assigned Machine | Proc Time |
|---|---|---|
| 1 | 4 | 10 |
| 2 | 3 | 39 |
| 3 | 2 | 10 |
| 4 | 2 | 27 |
| 5 | 1 | 12 |
| 6 | 5 | 21 |

**Machine 1-5 (Start / Completion)** por trabajo; las demás celdas valen 0:

| Job ID | Máquina | Start | Completion |
|---|---|---|---|
| 1 | 4 | 0 | 10 |
| 2 | 3 | 0 | 39 |
| 3 | 2 | 0 | 10 |
| 4 | 2 | 10 | 37 |
| 5 | 1 | 0 | 12 |
| 6 | 5 | 0 | 21 |

Gantt del gráfico. Los trabajos 1-6 salen de la tabla; los 7-10 se estiman con la escala del dibujo, en la que el trabajo 2 ocupa de 0 a 39:

| Máquina | Trabajo | Inicio | Fin |
|---|---|---|---|
| 1 | 5 | 0 | 12 |
| 1 | 10 | 12 | ≈27 |
| 2 | 3 | 0 | 10 |
| 2 | 4 | 10 | 37 |
| 3 | 2 | 0 | 39 |
| 4 | 1 | 0 | 10 |
| 4 | 7 | 10 | ≈26 |
| 4 | 9 | ≈26 | ≈39 |
| 5 | 6 | 0 | 21 |
| 5 | 8 | 21 | ≈34 |

### Página 40 — ¡Gracias!

William Guerrero, Ph.D.

## Anexo: texto extraído automáticamente del PDF

> Texto plano tal como sale del PDF, sin fórmulas ni tablas que estén como imagen. La versión fiel y completa es la sección «Contenido completo» de arriba.

### Página 1 · 2 imagen(es)

Programación de la 
Producción
2026

### Página 2 · 1 imagen(es)

Modelos de máquinas en paralelo
• Es un caso especial del Flexible flow 
shop.
• Objetivos:
– Minimizar el makespan
– Tiempo de terminación total (tiempo de flujo)
– Tardanza máxima 
• Decisiones:
– Asignar trabajos a las máquinas
– Secuencia de trabajos.

### Página 3 · 1 imagen(es)

Supuestos y definiciones
• Existen varias máquinas/servidores 
• El trabajo j tiene un solo proceso y puede ejecutarse en 
cualquiera de ellas. 
• Todas las máquinas son idénticas 
– Para un trabajo, el tiempo de procesamiento es el mismo 
independientemente de la máquina. 
Ej.:máquinas de moldeo por inyección
• Máquinas no idénticas (o no homogéneas) 
– Las máquinas tienen diferentes velocidades de procesamiento y el 
tiempo de proceso depende de la máquina elegida. 
Ej.:impresoras

### Página 4 · 1 imagen(es)

El Pm/β/γ es una extensión del 1/β/γ
• No existen reglas de despacho que GARANTICEN la 
solución óptima, excepto algunos casos particulares 
• Las reglas de despacho se implementan usando 
ALGORITMOS DE LISTA. 
• Una LISTA es una secuencia de trabajos ordenados de 
acuerdo a la regla de despacho seleccionada. 
• El programa de producción se genera asignando los 
trabajos en la lista a la máquina con menor carga 
asignada (menor tiempo de terminación).

### Página 5 · 4 imagen(es)

Ejemplo

### Página 6 · 2 imagen(es)

Min Makespan sin Preemptions
𝑃𝑚||𝐶𝑚𝑎𝑥
• Al minimizar el makespan, se balancea la 
carga entre las máquinas.
• Es equivalente al problema de partición

### Página 7 · 1 imagen(es)

Heurística de solución 
• Algoritmo de lista. Regla: Longest 
processing time first (LPT)
• Asignar en paralelo los trabajos más 
largos primero, en la primera máquina en 
estar disponible. 
• Teorema: Garantía de desempeño
𝐶𝑚𝑎𝑥𝐿𝑃𝑇
𝐶𝑚𝑎𝑥𝑂𝑃𝑇≤4
3 −1
3𝑚

### Página 8 · 1 imagen(es)

Ejemplo P3 | | Cmax
j
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
pj
1
3
4
6
9
10
10
11
12
13
13
14
16
18
19
Máquina 1
Máquina 2
Máquina 3
j
pj
cj
j
pj
cj
j
pj
cj

### Página 9 · 1 imagen(es)

Ejemplo P3 | | Cmax
Máquina 1
Máquina 2
Máquina 3
j
pj
cj
j
pj
cj
j
pj
cj
15
19
19
14
18
18
13
16
16
10
13
32
11
13
31
12
14
30
7
10
42
8
11
42
9
12
42
6
10
52
5
9
51
4
6
48
1
1
53
2
3
54
3
4
52
Cmax = 54
෍𝐶𝑗= 582

### Página 10 · 1 imagen(es)

Ejemplo: Reglas de despacho
• Calcule el makespan para LPT y SPT del 
siguiente ejemplo:
• 3||Cmax
• ¿Cuál es su cota superior?
job
1
2
3
4
5
6
7
8
9
10
p(i)
1
2
3
4
5
6
7
8
9
10

### Página 11 · 1 imagen(es)

Ejemplo: Reglas de despacho
• Asignar los trabajos en las máquinas con 
menos tiempo asignado de acuerdo a la 
regla SPT y LPT
• P4||Cmax
job
1
2
3
4
5
6
7
8
9
p(j)
7
7
6
6
5
5
4
4
4

### Página 12 · 2 imagen(es)

LPT

### Página 13 · 2 imagen(es)

SPT

### Página 14 · 2 imagen(es)

Óptimo

### Página 15 · 2 imagen(es)

¿Cómo hallamos el óptimo?
• Enumeración
– Notar que es un problema doble: Asignación y 
secuenciación 
– ¿Cuántas soluciones hay?
– El número de soluciones se puede calcular asi:
• Modelo matemático Programación Mixta 
• Branch & Bound

### Página 16 · 3 imagen(es)

Solución óptima para Pm | | ∑Cj
• La regla SPT soluciona a optimalidad Pm | | ∑Cj

### Página 17 · 1 imagen(es)

Min Makespan sin Preemptions y 
restricciones de precedencia
• 𝑃𝑚|𝑝𝑟𝑒𝑐|𝐶𝑚𝑎𝑥
• Fuertemente NP-hard
• Reglas aplicables:
– Critical Path (CP)
– Máximo numero de sucesores (LNS)

### Página 18 · 1 imagen(es)

Critical Path
• Se le da prioridad al trabajo con la cadena más larga de 
trabajos en el grafo de precedencias.
• Cuando el tiempo más corto = tiempo más tarde de 
terminación, el nodo hace parte de la ruta crítica.
• Los empates se rompen arbitrariamente.
• E.g.:

### Página 19 · 1 imagen(es)

Comparación
• Con el siguiente ejemplo, todos los 
trabajos tienen una duración de 1, ¿cuál 
regla da un mejor Cmax?
– LNS, CP.
1
2
3
4
5
6

### Página 20 · 1 imagen(es)

Restricciones de maquinaria
• 𝑃𝑚|𝑝𝑗= 1, 𝑀𝑗|𝐶𝑚𝑎𝑥
• Es decir, el trabajo j sólo se puede procesar en el 
conjunto de máquinas Mj
• Regla: Least flexible Job first (LFJ).
– Cada vez que una máquina se libera, se selecciona el 
trabajo que pueda ser procesado en el conjunto más 
pequeño de máquinas. 
• Teorema: LFJ es optima para 𝑃𝑚|𝑝𝑗= 1, 𝑀𝑗|𝐶𝑚𝑎𝑥 
con Mj anidados

### Página 21 · 1 imagen(es)

Conjuntos anidados
• Se debe cumplir una de las siguientes 
condiciones:
– Mj es igual a Mk
– Mj es un subconjunto de Mk
– Mk es un subconjunto de Mj
– Mj y Mk son conjuntos disjuntos.

### Página 22 · 1 imagen(es)

Ejemplo
• Considere el problema 𝑃4|𝑝𝑗= 1, 𝑀𝑗|𝐶𝑚𝑎𝑥 
con 8 trabajos.
– M1 = {1,2}
– M2 = M3 = {1, 3 , 4}
– M4 = {2}
– M5 = M6 = M7 = M8 = {3,4}

### Página 23 · 1 imagen(es)

Una solución
• Maq1: 
– 1
• Maq2:
– 4
• Maq3:
– 5
• Maq4: 
– 6

### Página 24 · 1 imagen(es)

Una solución
• Maq1: 
– 1-2
• Maq2:
– 4
• Maq3:
– 5-7
• Maq4: 
– 6-8

### Página 25 · 1 imagen(es)

Una solución
• Maq1: 
– 1-2
• Maq2:
– 4
• Maq3: 
Cmax = 3
– 5-7-3
• Maq4: 
– 6-8

### Página 26 · 1 imagen(es)

Least flexible machine first
• Menor Número de trabajos pendientes 
que una máquina puede procesar. 
• Resolvamos el ejercicio anterior.

### Página 27 · 1 imagen(es)

Tarea
• Formular el modelo de programación
matemática para el 𝑃𝑚|𝑀𝑗|𝐶𝑚𝑎𝑥

### Página 28 · 1 imagen(es)

Minimizar el Makespan con 
Preemptions
• 𝑃𝑚|𝑝𝑟𝑚𝑝|𝐶𝑚𝑎𝑥
• Modelo de programación matemática
• Sea Xij = tiempo que el trabajo j pasa en 
la máquina i.
• Variable positiva.

### Página 29 · 1 imagen(es)

Minimize Cmax
• Sujeto a:
෍
𝑖=1
𝑚
𝑥𝑖𝑗= 𝑝𝑗,
 𝑗= 1, … , 𝑛
෍
𝑖=1
𝑚
𝑥𝑖𝑗≤𝐶𝑚𝑎𝑥, 𝑗= 1, … , 𝑛
෍
𝑗=1
𝑛
𝑥𝑖𝑗≤𝐶𝑚𝑎𝑥, 𝑖= 1, … , 𝑚

### Página 30 · 1 imagen(es)

Propiedad matemática
• La solución óptima cumple la siguiente 
condición:
• 𝐶𝑚𝑎𝑥≥max 𝑝𝑚𝑎𝑥, σ𝑗=1
𝑛
𝑝𝑗
𝑚
= 𝐶𝑚𝑎𝑥∗

### Página 31 · 1 imagen(es)

Algoritmo
• Paso 1: Programe una máquina con todos 
los trabajos, en cualquier orden. Calcule 
m*Cmax.
• Paso 2: Parta el programa en m partes. 
• Paso 3: Asigne las partes a las máquinas.

### Página 32 · 1 imagen(es)

Alternativa
• Utilice la regla Longest remaining 
processing time first. 
• Desventaja: el número de preemptions es 
infinito.

### Página 33 · 1 imagen(es)

𝑃𝑚|| ෍𝐶𝑗
• SPT es la regla óptima para este problema. 
• Considere dos máquinas.
job
1
2
3
Pj
1
1
3

### Página 34 · 1 imagen(es)

𝑃𝑚|| ෍𝑊𝑗𝐶𝑗
• WSPT NO es la regla optima para este 
problema. 
• Considere dos máquinas.
job
1
2
3
Pj
1
1
3
wj
1
1
3

### Página 35 · 1 imagen(es)

𝑃𝑚|𝑝𝑟𝑒𝑐| ෍𝐶𝑗
• NP-hard
• Revisar la regla de CP.
• NP-hard
• Revisar la regla Least flexible job
𝑃𝑚|𝑀𝑗| ෍𝐶𝑗

### Página 36 · 1 imagen(es)

𝑅𝑚|| ෍𝐶𝑗
• Varias máquinas que trabajan a velocidades 
diferentes
• Modelo MIP
• Sea 𝑥𝑖𝑘𝑗= 1 si el trabajo j se programa en la 
posición k de la máquina i (de atrás hacia adelante)., 
0 d.l.c. Ejemplo: k=1 para la última posición. 
• Sea 𝑝𝑖𝑗 el tiempo de procesamiento del trabajo j en 
la máquina i.

### Página 37 · 1 imagen(es)

Min σ𝑖=1
𝑚σ𝑗=1
𝑛
σ𝑘=1
𝑛
𝑘𝑝𝑖𝑗𝑥𝑖𝑘𝑗
Sujeto a:
• σ𝑖=1
𝑚σ𝑘=1
𝑛
𝑥𝑖𝑘𝑗= 1 , 𝑗= 1, … , 𝑛
• σ𝑗=1
𝑛
𝑥𝑖𝑘𝑗≤1 , 𝑖= 1, … , 𝑚, 𝑘= 1, … , 𝑛
• 𝑥𝑖𝑘𝑗 es binaria

### Página 38

Explicación
• Suponga la secuencia 5-7-4
C5 = P5
C7 = P5 + P7
C4 = P5 + P7 + P4
F.O. = C5+C7+C4 = 3*P5 + 2*P7+ P4
Como el trabajo 5 está en la posición 3 (de atrás hacia 
adelante, su tiempo cuenta en la F.O. Tres veces.
5
7
4
𝑅𝑚|| ෍𝐶𝑗

### Página 39 · 2 imagen(es)

Solver de Excel

### Página 40 · 1 imagen(es)

¡Gracias!
William Guerrero, Ph.D.

