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

<!-- fuente: corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/README.md -->
# Proyecto algoritmo: competencia de secuenciación

Dos algoritmos en Python (solo biblioteca estándar) para la competencia de Gradescope:

| Reto | Problema | Algoritmo | Calidad | Tiempo prom. |
|---|---|---|---|---|
| 01 Willy Wonka | F3 \| prmu, s_ij por tipo, N→R prohibido \| Cmax | Cota inferior + heurística (NEH, bloques por tipo, búsqueda local con Taillard) + método exacto propio (programación dinámica acotada) | **Óptimo demostrado** en 30/30 instancias de la plantilla y 200/200 de prueba | ~4 ms (máx. ~60 ms) |
| 02 Monstruópolis | P3 \| r_j, prec \| Σ w_j T_j | Reglas de despacho (WSPT, ATC, cadenas, EDD) + recocido simulado con evaluación incremental | ~0,05 % sobre el mejor valor conocido (corridas 150 veces más largas), 0 violaciones | ~80 ms |

## Qué hay en la carpeta

```
reto1.py                  Reto 1, formato del instructivo: solve(data) -> {"Cmax", "secuencia", "tiempo"}
reto2.py                  Reto 2, formato del instructivo: solve(data) -> [{"job","machine","start","end"}, ...]
gradescope/
  reto1_willy_wonka/reto_schedulling.py     Reto 1 en la plantilla del profesor (clase Schedulling)
  reto2_monstruopolis/reto_schedulling.py   Reto 2 en la plantilla del profesor (clase Schedulling)
construir_plantillas.py   Regenera las dos plantillas a partir de reto1.py / reto2.py
pruebas/                  Solo para probar en local (NO se sube)
  probar_reto1.py         30 instancias de la plantilla (semilla 42), validación y comparación con el óptimo
  probar_reto2.py         30 instancias, validador independiente de factibilidad
  exacto_reto1.py         Segundo método exacto, implementado aparte, para verificar el Reto 1
  cota_reto2.py           Cota inferior lagrangiana (numpy) para medir qué tan cerca del óptimo queda el Reto 2
  generador.py            Imitación local del módulo `generador` de Gradescope (Reto 2)
  data_ejemplo_reto1.json Datos del enunciado de Willy Wonka (tablas 1 a 4)
  data_ejemplo_reto2.json Instancia de ejemplo en formato de filas (Trabajo, p_j, r_j, d_j, w_j, Predecesores)
  data_ejemplo_reto2_plantilla.json  La misma instancia en el formato de la plantilla (jobs, p, r, d, w, preds)
```

## Qué subir a Gradescope

Hay dos formatos y no está claro cuál pide el autograder:

- **Instructivo PDF**: `reto1.py` y `reto2.py` con la función `solve(data)` (lee `data.json`).
- **Plantillas .py del profesor**: un archivo `reto_schedulling.py` por reto, con la clase `Schedulling` y `resolver_instancia()`.

Subir el que pida la tarea de Gradescope. Si piden `reto_schedulling.py`, usar el de la carpeta `gradescope/` del reto correspondiente. Ambos formatos usan exactamente el mismo algoritmo.

## Cómo probar en local

Desde esta carpeta:

```
python reto1.py pruebas/data_ejemplo_reto1.json
python reto2.py pruebas/data_ejemplo_reto2.json
python pruebas/probar_reto1.py --exacto
python pruebas/probar_reto2.py
python pruebas/probar_reto2.py --holgura 0.5      (fechas de entrega más sueltas)
```

Si cambian `reto1.py` o `reto2.py`, correr `python construir_plantillas.py` para actualizar las plantillas.

## Calidad contra tiempo (parámetros al inicio de cada archivo)

El 30 % de la nota es tiempo de cómputo, por eso los parámetros están en el punto donde subir el tiempo casi no mejora la calidad. Si en Gradescope se ve que el tiempo pesa menos (o más) de lo esperado, se pueden mover:

**Reto 1** (`EXACTO_R1`, 200 instancias del generador de la plantilla):

| Configuración | Óptimas | Tiempo prom. (máx.) |
|---|---|---|
| **`EXACTO_R1 = True` (por defecto)** | 200/200, **demostradas** | ~4 ms (~60 ms) |
| `EXACTO_R1 = False` (solo heurística + Iterated Greedy) | 197/200, sin demostrar | ~2 ms (~9 ms) |

**Reto 2** (`ITER_SA_R2`, 30 instancias, brecha contra corridas largas):

| Iteraciones | Brecha (d_j ajustado) | Brecha (d_j holgado) | Tiempo |
|---|---|---|---|
| 0 (solo reglas de despacho) | 2,9 % | 18,6 % | ~2 ms |
| 5 000 | 0,17 % | 2,7 % | ~40 ms |
| **10 000 (por defecto)** | 0,05 % | 1,8 % | ~80 ms |
| 20 000 | 0,04 % | 0,7 % | ~150 ms |

## ¿Es el óptimo?

- **Reto 1: sí, demostrado.** El algoritmo termina con una prueba: o la solución iguala la cota inferior, o el método exacto revisa (podando con la cota) todas las secuencias que podrían ser mejores y no queda ninguna. Se comprobó además contra un segundo exacto implementado aparte (200/200 iguales) y en 400 instancias más difíciles que las de la plantilla (todas demostradas, peor caso ~0,3 s).
- **Reto 2: no se puede demostrar en tiempo de competencia** (50 trabajos, problema NP-difícil; un exacto en Python no terminaría). Evidencia de que estamos muy cerca: corridas 150 veces más largas solo mejoran 0,05 % en promedio, y la cota inferior lagrangiana (`pruebas/cota_reto2.py`) deja como máximo 2,4 % de brecha. Esa brecha viene sobre todo de que la cota es floja: con más iteraciones ya no sube.

Todo lo que va en la entrega usa solo la biblioteca estándar de Python, como pide el instructivo. numpy solo se usa en `pruebas/`.

Los algoritmos usan su propia semilla (`random.Random(SEMILLA)`): los resultados son reproducibles y no alteran el `random` global con el que la plantilla genera las instancias.

## Cosas a revisar antes de entregar

1. **La función `calcular_makespan_penalizado` de la plantilla del Reto 1 tiene un error.** Para buscar el tipo del lote anterior recorre toda la secuencia y toma el último lote con `fin_lote <= fin_maquina`; como los lotes aún no procesados tienen `fin_lote = 0`, casi siempre termina tomando el tipo del **último lote de la secuencia**, no el del lote anterior. Por eso da valores de 650 a 1 000 cuando el Cmax real está entre 560 y 680. Nuestro algoritmo optimiza el Cmax real (el del enunciado). Conviene preguntarle al profesor con qué función califica Gradescope; `pruebas/probar_reto1.py` muestra ambos valores (columna `plantilla`).
2. **Supuesto de alistamientos (Reto 1):** igual que en esa función de la plantilla, el alistamiento empieza cuando la máquina está libre y el lote ya llegó: `inicio = max(fin máquina, fin del lote en la máquina anterior) + alistamiento`. El primer lote no tiene alistamiento.
3. **La plantilla del Reto 1 importa `from optimizador import load_from_dict, run_ga`**, que es el ejemplo del profesor y no viene con la plantilla. Se dejó dentro de un `try/except ImportError` para que no falle si ese módulo no existe en Gradescope.
4. **Reto 2:** el módulo `generador` real está en Gradescope; el de `pruebas/` lo imita según el enunciado (d_j = tiempo mínimo teórico de finalización). Si en Gradescope los d_j resultan más holgados, el algoritmo sigue siendo factible pero queda más lejos del mejor conocido (~1,8 %); en ese caso conviene subir `ITER_SA_R2` a 20 000 (probar con `python pruebas/probar_reto2.py --holgura 0.5`).
5. **La plantilla del Reto 2 trae un ciclo que corre hasta `timelimit - 1` (29 s).** Lo reemplazamos por el recocido, que termina en ~80 ms, porque el tiempo cuenta en la nota. El tope de seguridad sigue siendo `min(5 s, timelimit - 1)`.


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

## Contenido completo (página por página)

> Documento de 4 páginas con diseño de página web impresa (encabezado oscuro, tarjetas de colores). El texto se transcribe tal cual, incluidas las palabras sin tilde del original («solucion», «tecnico», «estandar»…).

### Página 1 — Competencia de Secuenciación de Máquinas: presentación y los dos retos

**PLANEACIÓN, PROGRAMACIÓN Y CONTROL DE LAS OPERACIONES**

**Competencia de Secuenciación de Máquinas** (título principal)

Universidad de La Sabana — Facultad de Ingeniería Industrial

> [Franja de tres etiquetas de color: **Grupos de 5 estudiantes** · **2 retos de programación** · **Entrega por Gradescope**]

**¿De qué se trata la competencia?**

Cada grupo debe programar **dos algoritmos de secuenciación** en Python para resolver dos problemas clásicos de scheduling. Los algoritmos se evalúan automáticamente en **Gradescope**: el sistema prueba su código con varias instancias del problema y mide qué tan buena es la solución y qué tan rápido la encuentran. Gana el equipo que mejor combine calidad de solución y velocidad de cómputo.

**Los dos retos** (dos tarjetas lado a lado)

| | RETO 01 | RETO 02 |
|---|---|---|
| Nombre | **Fábrica de Willy Wonka** — Flow Shop con tiempos de alistamiento | **Fábrica de Monstruópolis** — Máquinas paralelas con precedencias |
| Tipo | Flow Shop de 3 máquinas en serie (M1 → M2 → M3). | 3 máquinas idénticas en paralelo (P3 \| rj, prec \| ∑WjTj). |
| Objetivo | Minimizar el Cmax (tiempo en que termina el último lote). | Minimizar la tardanza ponderada total (∑wjTj). |
| Restricciones | · Un lote Relleno (R) no puede ir inmediatamente después de un lote Nueces (N) en ninguna máquina. · Cada cambio de tipo genera un tiempo de alistamiento diferente por máquina. | · Cada trabajo tiene fecha de liberación (rj) y de entrega (dj). · Algunos trabajos tienen precedencias (i → j). No se permite interrumpir trabajos (no preemption). |
| Pie de la tarjeta | `15 lotes \| 3 máquinas en serie \| setup dependiente del tipo` | `50 trabajos \| 3 máquinas paralelas \| ~5 precedencias` |

**Criterios de evaluación y puntaje** *(el contenido sigue en la página 2)*

### Página 2 — Criterios de evaluación, penalizaciones, comparación entre equipos y formatos de entrega

> [Franja de tres bloques de color con los pesos de la nota]

| Peso | Criterio |
|---|---|
| **60 %** | Calidad de la solución (valor del objetivo obtenido) |
| **30 %** | Tiempo computacional (velocidad del algoritmo) |
| **10 %** | Reporte técnico (de los algoritmos presentados) |

**Penalizacion por restricciones violadas**

Una solucion que incumpla alguna restriccion **no recibe puntaje cero automaticamente**, pero si tendra una **penalizacion directa sobre el valor de la funcion objetivo**: se sumara una penalidad proporcional al numero de violaciones detectadas, lo que deteriorara significativamente su posicion en el ranking.

El objetivo es incentivar soluciones factibles. Una solucion infactible con buen tiempo computacional **nunca superara a una solucion factible bien construida**.

**Como se compara la calidad entre equipos**

Gradescope prueba cada algoritmo con varias instancias generadas automaticamente. El equipo con el menor valor del objetivo (Cmax en Reto 01 o ∑wjTj en Reto 02) en promedio obtiene el mayor puntaje. El ranking se normaliza: el mejor equipo obtiene 100 puntos, los demas se escalan proporcionalmente. Las penalizaciones por violaciones se suman al valor objetivo **antes** de este calculo.

**Reporte tecnico (10%):** Documento PDF de maximo 4 paginas que describe los algoritmos implementados: tipo de heuristica o metaheuristica usada, justificacion de la eleccion, analisis de resultados sobre las instancias de prueba y lecciones aprendidas. Se entrega junto con el codigo en Gradescope.

**Formatos de entrega**

**Reto 01 — Willy Wonka: salida en JSON exactamente asi:**

```
{
"Cmax": 847, // minuto en que termina el ultimo lote
"secuencia": ["L1", "L4", ..., "L15"],
"tiempo": 12 // ms que tardo el algoritmo
}
```

**Reto 02 — Monstruopolis: salida en lista JSON asi:**

```
[
{"job": "J1", "machine": "M1", "start": 0, "end": 45},
{"job": "J2", "machine": "M2", "start": 10, "end": 35},
// ... una entrada por trabajo
]
// Gradescope calcula Cj y sum(wjTj) automaticamente
```

**Template de Python — estructura esperada** *(sigue en la página 3)*

### Página 3 — Template de Python, reglas de la competencia y recomendación para el Reto 01

Cada equipo recibe **reto1.py** y **reto2.py**. Solo deben implementar el cuerpo del algoritmo dentro de la funcion **solve()**:

```python
# reto1.py — template Willy Wonka
import json, time
def solve(data: dict) -> dict:
    """
    Parametro: data — diccionario cargado desde data.json
    Retorna: {"Cmax": int, "secuencia": list[str], "tiempo": int}
    """
    start = time.time()
    # <- su algoritmo va aqui
    secuencia = [] # llenar con ['L1', 'L3', ...]
    cmax = 0 # calcular Cmax con la secuencia
    elapsed = int((time.time() - start) * 1000)
    return {"Cmax": cmax, "secuencia": secuencia, "tiempo": elapsed}
if __name__ == "__main__":
    with open("data.json") as f:
        data = json.load(f)
    print(json.dumps(solve(data), indent=2))
```

> En el PDF el código aparece sin sangría (cada línea en una franja oscura); la sangría de arriba es la que exige Python y se reconstruyó.

**Reglas de la competencia**

| Regla | Detalle |
|---|---|
| **Equipo** | Cada equipo tiene exactamente 5 integrantes. Un solo estudiante sube los archivos en Gradescope en nombre del grupo. |
| **Archivos** | Se entregan reto1.py, reto2.py y el reporte tecnico en PDF. No se aceptan notebooks (.ipynb), archivos ZIP ni dependencias no estandar. |
| **Tiempo limite** | El algoritmo tiene un limite de 60 segundos por instancia. Si supera ese limite, Gradescope lo cancela y asigna el peor puntaje en esa instancia. |
| **Librerias** | Solo se permiten librerias de la biblioteca estandar de Python (json, time, math, random, itertools, collections, heapq, etc.) y numpy. No se permite OR-Tools, PuLP, Gurobi ni similares. |
| **Entregas** | Pueden hacer multiples entregas antes de la fecha limite. Gradescope calificara automaticamente la ultima version subida. |
| **Codigo propio** | El codigo debe ser propio del equipo. Se permite inspirarse en literatura o en clase, pero no copiar codigo de otros equipos. El profesor puede solicitar explicar el algoritmo en cualquier momento. |

**Recomendaciones para el algoritmo**

**Reto 01 — Willy Wonka (Flow Shop):** Consideren heuristicas como NEH, busqueda local (2-opt, insercion), o metaheuristicas como simulated annealing. La restriccion N→R es de factibilidad: su secuencia debe verificarla antes de calcular el Cmax.

### Página 4 — Recomendación para el Reto 02 y consejo general

**Reto 02 — Monstruopolis (Paralelas):** Consideren reglas de despacho como WSPT, EDD ponderado, o prioridades adaptadas. Las precedencias implican verificar en cada momento de decision que trabajos ya tienen sus predecesores terminados.

**Consejo general:** Empiecen con una solucion factible simple para asegurarse de que el formato es correcto. Luego mejoren la calidad. Un algoritmo rapido con solucion aceptable suele ganarle a uno lento con solucion teoricamente perfecta.

*Pie de página:* Planeacion, Programacion y Control de las Operaciones · Universidad de La Sabana · Facultad de Ingenieria Industrial

(El resto de la página está en blanco.)


---

<!-- fuente: corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/plantilla-reto-1-willy-wonka/reto_schedulling.py -->
# Código: `corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/plantilla-reto-1-willy-wonka/reto_schedulling.py`

> Archivo completo: https://github.com/samuelgradientai-sys/planeacion-control-produccion/blob/main/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/plantilla-reto-1-willy-wonka/reto_schedulling.py

```python
"""
Plantilla base para GradeScope
-------------------------------------------------------
             INSTRUCCIONES IMPORTANTES
-------------------------------------------------------
1. NO cambiar el nombre de la clase ni las funciones principales.
   - Clase obligatoria: Schedulling
   - Métodos obligatorios: generar_instancia(), resolver_instancia(), ejecutar_experimentos()
2. SOLO deben modificar:
   - El contenido de generar_instancia() para crear sus propios datos.
   - El contenido de resolver_instancia() para construir su modelo de optimización.
3. NO modificar:
   - Los nombres de las funciones o variables internas del experimento.
   - El método ejecutar_experimentos() ni su estructura.
   - El nombre del archivo: debe llamarse EXACTAMENTE `reto_schedulling.py`
4. El método ejecutar_experimentos():
   - Ejecuta automáticamente 30 instancias.
   - Mide el tiempo de ejecución por instancia.
   - Devuelve un consolidado con los tiempos individuales.
   - Reporta el tiempo promedio y el total al final.

Cualquier cambio fuera de lo permitido puede causar errores de evaluación automática.
"""

# Agregar dependencias si es necesario, pero sin remover las que ya se encuentran abajo
import random
import numpy as np
import time
import pandas as pd
from optimizador import load_from_dict, run_ga
import json

class Schedulling:
    def __init__(self, n_instancias: int = 30, semilla: int = 42):
        """
        Inicializa la clase con número de instancias y semilla.
        No modificar esta función.
        """
        self.n_instancias = n_instancias
        self.semilla = semilla
        random.seed(semilla)
        np.random.seed(semilla)
        self.resultados = {"instancia": [], "valor_objetivo": [], "tiempo_seg": []}
        self.consolidado = None

    def generar_instancia(self, indice):
        """
        Genera una instancia aleatoria del problema de lotes y setups.
        Retorna un diccionario con los tiempos de procesamiento y tiempos de setup.
        """
        tipos = ["S", "N", "R"]
        lotes = [f"L{i}" for i in range(1, 16)]

        # Rangos de tiempos de procesamiento por máquina
        rangos = {
            "M1": (25, 45),
            "M2": (20, 40),
            "M3": (10, 25)
        }

        # --------------------------
        # Generar datos de los lotes
        # --------------------------
        lotes_dict = {}
        for lote in lotes:
            tipo = random.choice(tipos)
            lotes_dict[lote] = {
                "tipo": tipo,
                "M1": random.randint(*rangos["M1"]),
                "M2": random.randint(*rangos["M2"]),
                "M3": random.randint(*rangos["M3"])
            }

        # --------------------------
        # Generar tiempos de setup
        # --------------------------
        setup_dict = {}
        for maquina in ["M1", "M2", "M3"]:
            setup_dict[maquina] = {}
            for tipo_ant in tipos:
                for tipo_sig in tipos:
                    if tipo_ant == tipo_sig:
                        tiempo_setup = 0
                    else:
                        if maquina == "M1":
                            tiempo_setup = random.randint(10, 40)
                        elif maquina == "M2":
                            tiempo_setup = random.randint(5, 30)
                        else:  # M3
                            tiempo_setup = random.randint(3, 15)
                    setup_dict[maquina][f"{tipo_ant}-{tipo_sig}"] = tiempo_setup

        # --------------------------
        # Consolidar instancia
        # --------------------------
        instancia = {
            "lotes": lotes_dict,
            "setup": setup_dict
        }
        with open(f'instancia_{indice}.json', "w", encoding="utf-8") as f:
            json.dump(instancia, f, indent=4, ensure_ascii=False)

        return instancia

    def resolver_instancia(self, instancia: dict):
        data, jobs, setups = load_from_dict(instancia)
        best_seq, best_ms = run_ga(jobs, setups)
        return {
            "secuencia": [jobs[i]["id"] for i in best_seq], # pueden agregar, eliminar o agregar salidas del modelo
        }

    def ejecutar_experimentos(self):
        """
        Genera y resuelve las instancias, mide tiempos de ejecución
        y consolida los resultados.
        NO modificar esta función.
        """
        print(f"Ejecutando {self.n_instancias} instancias...\n")

        # Reinicia resultados
        self.resultados = {"instancia": [], "valor_objetivo": [], "tiempo_seg": []}

        inicio_total = time.time()

        for i in range(1, self.n_instancias + 1):
            instancia = self.generar_instancia(i)
            t0 = time.time()
            resultado = self.resolver_instancia(instancia)
            t1 = time.time()

            # Guarda resultados
            self.resultados["instancia"].append(i)
            self.resultados["valor_objetivo"].append(resultado["valor_objetivo"])
            self.resultados["tiempo_seg"].append(round(t1 - t0, 4))

            print(f"Instancia {i} optimizada en {round(t1 - t0, 4)} seg")

        # Tiempo total
        tiempo_total = time.time() - inicio_total

        # Crear DataFrame consolidado
        self.consolidado = pd.DataFrame(self.resultados)

        # Calcular promedios solo de tiempo
        promedio_tiempo = self.consolidado["tiempo_seg"].mean()

        print("\n==== REPORTE DE RENDIMIENTO ====")
        print("Tiempo promedio por instancia:", round(promedio_tiempo, 4), "seg")
        print("Tiempo total de ejecución:", round(tiempo_total, 2), "seg")

        return self.consolidado
    
    def calcular_makespan_penalizado(self , data={}, secuencia=[f'L{i}' for i in range(1,16)]):
        lotes = data["lotes"]
        setup = data["setup"]
        maquinas = ["M1", "M2", "M3"]

        # Validación: N no puede ir inmediatamente antes de R
        penalizado = False
        for i in range(1, len(secuencia)):
            tipo_anterior = lotes[secuencia[i-1]]["tipo"]
            tipo_actual = lotes[secuencia[i]]["tipo"]
            if tipo_anterior == "N" and tipo_actual == "R":
                penalizado = True
                break

        fin_maquina = {m: 0 for m in maquinas}
        fin_lote = {l: 0 for l in secuencia}

        for lote in secuencia:
            tipo_actual = lotes[lote]["tipo"]
            for m_idx, m in enumerate(maquinas):
                prev_tipo = None
                # Buscar el último tipo procesado en esta máquina
                if fin_maquina[m] > 0:
                    for l in secuencia:
                        if fin_lote[l] <= fin_maquina[m] and l != lote:
                            prev_tipo = lotes[l]["tipo"]

                t_setup = 0
                if prev_tipo is not None and prev_tipo != tipo_actual:
                    t_setup = setup[m][f"{prev_tipo}-{tipo_actual}"]

                if m_idx == 0:
                    inicio = fin_maquina[m] + t_setup
                else:
                    inicio = max(fin_maquina[m], fin_lote[lote]) + t_setup

                duracion = lotes[lote][m]
                fin = inicio + duracion

                fin_maquina[m] = fin
                fin_lote[lote] = fin

        makespan = max(fin_maquina.values())

        # Penalización si se violó la regla N → R
        if penalizado:
            makespan = float('inf')

        return makespan
# ----------------------------------------------------------
# Ejecución directa (GradeScope)
# ----------------------------------------------------------
if __name__ == "__main__":
    sch = Schedulling(30)
    df_resultados = sch.ejecutar_experimentos()
    print("\nConsolidado final:")
    print(df_resultados)
```


---

<!-- fuente: corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/plantilla-reto-2-monstruopolis/reto_schedulling.py -->
# Código: `corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/plantilla-reto-2-monstruopolis/reto_schedulling.py`

> Archivo completo: https://github.com/samuelgradientai-sys/planeacion-control-produccion/blob/main/corte-3-programacion-scheduling/proyecto-competencia-scheduling/enunciados/plantilla-reto-2-monstruopolis/reto_schedulling.py

```python


# Plantilla base para GradeScope
# este archivo debe llamarse reto_schedulling.py 
# Agregar dependencias si es necesario, pero sin remover las que ya se encuentran abajo
import random
import numpy as np
import time
import pandas as pd
import json

# === Dependencias para el modelo===
from itertools import product, combinations
from generador import GeneradorInstancias

class Schedulling(GeneradorInstancias):
    def __init__(self, n_instancias: int = 30, semilla: int = 42, timelimit: int = 30):
        # reutilizamos el __init__ del generador
        super().__init__(n_instancias=n_instancias, semilla=semilla, timelimit=timelimit)
        self.timelimit = timelimit  # por claridad

    def resolver_instancia(self, instancia: dict):
        """
        Heurística mejorada para:
            P3 | r_j, prec | Σ w_j T_j
        - Usa un simulador que respeta:
            * fechas de liberación r_j
            * precedencias preds[j]
            * m máquinas paralelas sin solape
        """
        import math
        import time
        import random

        # ===================== 1. Sets y parámetros =====================
        J = instancia["jobs"]
        m = instancia["m"]
        Mset = [f"M{i+1}" for i in range(m)]

        p = instancia["p"]      # p_j tiempos de proceso
        r = instancia["r"]      # r_j tiempos de liberación
        d = instancia["d"]      # d_j due dates
        w = instancia["w"]      # w_j indices de prioridad
        preds = instancia["preds"]  # lista de predecesores por j

        # Construir lista de sucesores (para actualizar precedencias rápido)
        succs = {j: [] for j in J}
        for j in J:
            for u in preds[j]:
                succs[u].append(j)

        # --------------------- constructor de calendario ---------------------
        def build_schedule():
            """
            Construye una programación completa
            """
            secuencia_local = []
            for j in J:
                sj = start_times.get(j, 0.0)
                cj = end_times.get(j, sj + p[j])
                mm = machine_of.get(j, Mset[0])
                secuencia_local.append({
                    "job": j,
                    "machine": mm,
                    "start": round(float(sj), 6),
                    "end": round(float(cj), 6),
                    "Cj": round(float(cj), 6)
                })


		# INSERTA AQUI TU CODIGO PARA OPTIMIZAR best_val y best_seq




        best_val = float("inf")
        best_seq = None

        max_time = self.timelimit - 1.0 if self.timelimit else 29.0

        while (time.perf_counter() - start_global) < max_time:

            sec, val = build_schedule()

            if val < best_val:
                best_val = val
                best_seq = secuencia_local


        return {
            "secuencia": best_seq,
            "valor_objetivo": round(float(best_val), 4)
        }
```


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

## Contenido completo (página por página)

### Página 1 — ¡Willy Wonka está en apuros! (contexto y Tabla 1, inicio)

> [Imagen decorativa: logo de la Universidad de La Sabana, arriba a la izquierda]

**Proyecto Final Planeación, Programación y Control de las Operaciones**

**¡Willy Wonka está en apuros!**

La empresa chocolatera de Willy Wonka produce tres tipos de tabletas de chocolate diferentes: simples (S), con nueces (N) y rellenas (R). Cada lote de barras de chocolate contiene 100 tabletas y debe pasar de forma obligatoria por tres máquinas. Por razones de eficiencia operativa, todos los lotes se procesan bajo una secuencia uniforme a lo largo de las máquinas en el siguiente orden:

- **Máquina de mezclado y refinado (M1):** Se combinan los ingredientes base y se homogeneiza la mezcla con la fórmula secreta de Willy Wonka.
- **Máquina de moldeo y enfriamiento (M2):** La mezcla se vierte en moldes y se enfría en cámaras controladas para obtener la forma de tableta, conservando todo su sabor y su aroma.
- **Maquina empaquetadora (M3):** Las tabletas son empacadas y selladas individualmente, a cada una se le coloca un tiquete plateado y solo una de cada un millón de tabletas se le asignará un tiquete dorado de ganador.

El señor Willy Wonka desea con ansias acabar cuanto antes la producción de esta temporada para conocer el ganador del tiquete dorado. Por lo tanto, le ha solicitado a su equipo de ingenieros industriales que planifique la producción de este mes para terminar lo antes posible todos y cada uno de los lotes planificados para producir este mes.

El señor Wonka le ha compartido a su equipo toda la información relevante de sus operaciones en la fábrica. Lo primero que entrega el señor Wonka a su equipo es la Tabla 1, con información los lotes a fabricar en este mes de noviembre. Este es un ejemplo, pero los datos variarán de forma aleatoria.

**Tabla 1.** *Minutos de procesamiento de todos los lotes a fabricar en noviembre* (filas L1 y L2 en esta página; la tabla completa está en la página 2)

### Página 2 — Tabla 1 completa, restricción N→R y alistamientos

**Tabla 1.** Minutos de procesamiento de todos los lotes a fabricar en noviembre (tabla completa; las filas L1 y L2 vienen de la página 1)

| LOTE | TIPO | M1 | M2 | M3 |
|---|---|---|---|---|
| L1 | S | 38 | 33 | 19 |
| L2 | N | 41 | 27 | 21 |
| L3 | R | 29 | 37 | 14 |
| L4 | S | 35 | 24 | 22 |
| L5 | N | 44 | 38 | 16 |
| L6 | R | 27 | 31 | 18 |
| L7 | S | 40 | 28 | 25 |
| L8 | N | 33 | 40 | 12 |
| L9 | R | 31 | 22 | 17 |
| L10 | S | 39 | 35 | 15 |
| L11 | N | 42 | 26 | 23 |
| L12 | R | 28 | 34 | 13 |
| L13 | S | 36 | 29 | 20 |
| L14 | N | 45 | 25 | 24 |
| L15 | R | 30 | 39 | 11 |

Por políticas de seguridad alimentaria, un lote de tipo relleno (R) no puede procesarse inmediatamente después de un lote de tipo nueces (N) en ninguna máquina, para evitar contaminación por trazas de frutos secos. Debe haber al menos un lote de otro tipo entre ellos.

Asimismo, cada vez que una máquina cambia el tipo de lote a producir, se necesita un tiempo adicional de limpieza y ajuste. Los tiempos dependen del lote anterior y el tipo siguiente de lote, y son diferentes en las tres máquinas. De esta manera, se le presentó al grupo los tiempos de alistamiento en las Tablas 2, 3 y 4.

**Tabla 2.** *Minutos de alistamiento de la máquina uno según tipos de lotes.* (los valores están en la página 3)

### Página 3 — Tablas 2, 3 y 4 (alistamientos por máquina) y resultado esperado

En las tres tablas, la fila es el tipo del lote **anterior** y la columna el tipo del lote **siguiente** (de → a).

**Tabla 2.** Minutos de alistamiento de la máquina uno (M1):

| de \ a | S | N | R |
|---|---|---|---|
| **S** | 0 | 15 | 35 |
| **N** | 25 | 0 | 40 |
| **R** | 20 | 25 | 0 |

**Tabla 3.** Minutos de alistamiento de la máquina dos (M2):

| de \ a | S | N | R |
|---|---|---|---|
| **S** | 0 | 10 | 25 |
| **N** | 15 | 0 | 30 |
| **R** | 10 | 20 | 0 |

**Tabla 4.** Minutos de alistamiento de la máquina tres (M3):

| de \ a | S | N | R |
|---|---|---|---|
| **S** | 0 | 5 | 10 |
| **N** | 8 | 0 | 12 |
| **R** | 6 | 9 | 0 |

**Resultado Esperado**

Willy Wonka le solicita a su equipo que le entreguen un informe breve en donde le indiquen la secuencia en la que debe fabricar todos los lotes, además de cuánto tiempo tardarán a lo sumo para terminar de procesar todos, y cuál es la secuencia de los lotes en cada una de las máquinas. Adicionalmente, deben entregarle un algoritmo que reciba como entrada la información brindada por el señor Wonka, y la retorne en un formato especifico que se muestra a continuación: • **Entrada**

### Página 4 — Formatos de entrada (data.json) y salida, y autores

> [Captura de código con fondo oscuro. Las claves aparecen resaltadas en verde y el texto extraído las desordena; abajo se reconstruye en orden, fiel a la imagen, con los comentarios `#` originales.]

**Entrada:**

```
#  datos de entrada formato JSON (nombre del archivo debe ser data.json)
{
    "lotes" :
    {
        "L1": {"tipo": "S", "M1": 38, "M2": 33, "M3": 19}, # Información por lote
        ...,
        "L15": {"tipo": "R", "M1": 30, "M2": 39, "M3": 11} # Debe haber 15 lotes
    },

    "setup" :
    {
        "M1" :
        {
            "S-S": 0, # todas las combinaciones de tipo de lote por cada maquina
            "S-R": 15,
            "S-N": 30,
            "N-S": 25,
            "N-N": 0, # las letras iguales son 0
            "N-R": 40,
            "R-S": 20,
            "R-N": 25,
            "R-R" : 0, # 9 combinaciones posibles por maquina
        },
        ...,
        "M3" : # cada maquina debe tener sus combinaciones completas
        {
            "S-S": 0,
            ...,
            "R-R": 0,
        }
    }
}
```

> Ojo: en este ejemplo, M1 tiene `"S-R": 15` y `"S-N": 30`, pero la Tabla 2 dice S→N = 15 y S→R = 35. Los demás valores de M1 coinciden con la Tabla 2. Ver Observaciones.

**Salida:**

```
{
    "Cmax": 100, # tiempo de terminación (ej.: al minuto 100 se acaba el ultimo lote)
    "secuencia": ["L1", ..., "L15"], # secuencia ordenada por producción de los lotes
    "tiempo": 1500 # tiempo ejecución algoritmo en milisegundos
}
```

Reto diseñado por: Catalina Andrea Castro López, Isabella Sofia Endara Chitiva, Néstor Andrés Tabares David, Nicolás Joel Cáceres Parra


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

## Contenido completo (página por página)

### Página 1 — La Fábrica de Juguetes de Monstruópolis: contexto y datos del reto

> [Imagen decorativa: logo «Universidad de La Sabana › Facultad de Ingeniería», centrado arriba (se repite en las tres páginas)]

**Proyecto Final – Scheduling de Producción: “La Fábrica de Juguetes de Monstruópolis”**

$$P3 \mid r_j,\ prec \mid \sum W_jT_j$$

**1. Contexto del Problema**

La historia se desarrolla en **Monstruópolis**, la ciudad de la película *Monsters Inc.*.. Tras la transición de usar gritos a usar risas como fuente de energía, la compañía **Monsters Inc.** diversificó sus operaciones y creó una **fábrica de juguetes** que produce artículos basados en los personajes de las películas más populares de Disney-Pixar: *Toy Story*, *Cars*, *Finding Nemo*, *Inside Out* y *Monsters University*.

La fábrica cuenta con **tres máquinas idénticas en paralelo** (M1, M2, M3) que trabajan de forma continua durante el turno diurno. Cada juguete (trabajo) requiere **un solo proceso de fabricación**, pero no todas las máquinas están disponibles al mismo tiempo, ya que cada una requiere calibraciones y mantenimientos periódicos.

El gerente de planta, **Mike Wazowski**, debe decidir **en qué máquina y en qué orden** se procesarán los pedidos del día, de forma que se cumplan las prioridades, fechas de liberación y restricciones de precedencia, minimizando la tardanza ponderada total de los trabajos.

**2. Datos del Reto**

- **Número de máquinas (m):** 3 (idénticas en capacidad y velocidad)
- **Número de trabajos (n):** 50 juguetes (J1–J50)
- **Tiempos de procesamiento $p_j$:** Valores enteros generados aleatoriamente entre 10 y 100 minutos.
- **Fechas de liberación $r_j$** (momento en que cada pedido está disponible para producción): Valores enteros aleatorios entre 0 y 30 minutos desde el inicio del turno.
- **Fechas de entrega dj** Se asignan como el tiempo mínimo teórico de finalización del trabajo.
- **Prioridades $w_j$** (peso o importancia del pedido): Valores enteros aleatorios entre 1 y 5, que indican la importancia relativa de cada pedido en el objetivo ponderado.
- **Precedencias:** Generadas aleatoriamente. Algunos juguetes comparten piezas o moldes:

Se define un conjunto de relaciones (i → j) donde el trabajo j no puede comenzar hasta que el trabajo i haya terminado.

### Página 2 — Precedencias, restricciones adicionales, objetivo y formatos

El porcentaje de trabajos con precedencias puede ser del 10 % del total, es decir, aproximadamente 5 precedencias por instancia.

Se garantiza que las precedencias no formen ciclos (es decir, que sean válidas).

**Restricciones adicionales:**

- No hay tiempos de setup adicionales.
- Cada máquina puede procesar un trabajo a la vez.
- No se permite preemption (una vez iniciado un trabajo, debe finalizar).
- Las precedencias entre trabajos deben respetarse estrictamente: un trabajo sucesor solo puede comenzar cuando todos sus predecesores hayan finalizado.
- Los trabajos se asignan a una de las tres máquinas idénticas, las cuales operan de forma continua durante el turno diurno.

**3. Objetivo de Optimización**

**Minimizar la tardanza ponderada total:**

$$\min \sum_{j=1}^{n} w_j\,T_j,\qquad T_j=\max\{0,\;C_j-d_j\},$$

**donde $C_j$ es el tiempo de finalización de $J_j$**

El objetivo es **minimizar la tardanza ponderada total** ,

Esto garantiza que los trabajos con mayor prioridad presenten los menores retrasos posibles, respetando las fechas de liberación y las restricciones de precedencia establecidas.

**4. Formatos de entrada y salida:**

**Entrada:**
Archivos .json con 50 filas (una por trabajo) y las siguientes columnas:
Trabajo, p_j, r_j, d_j, w_j, Predecesores

**Salida esperada:**

- Secuencia de asignación de trabajos a las tres máquinas
- Tiempo de finalización de cada trabajo $C_j$

### Página 3 — Salida (fin), ejemplo de secuencia.json y autores

- Valor total del objetivo $\sum w_jT_j$

Ejemplo de entrada de la secuencia para una instancia (.json):

> [Captura de pantalla de un editor de código (tema oscuro), archivo `secuencia.json`, líneas 1–11:]

```json
[
  {"job": "J1", "machine": "M1", "start": 0,  "end": 45},
  {"job": "J2", "machine": "M2", "start": 10, "end": 35},
  {"job": "J3", "machine": "M3", "start": 5,  "end": 55},
  {"job": "J4", "machine": "M1", "start": 45, "end": 80},
  {"job": "J5", "machine": "M2", "start": 35, "end": 55},
  {"job": "J6", "machine": "M3", "start": 55, "end": 85},
  {"job": "J7", "machine": "M1", "start": 80, "end": 140},
  {"job": "J8", "machine": "M2", "start": 55, "end": 95}
]
```

El mismo ejemplo como Gantt:

| Máquina | Trabajo | Inicio | Fin |
|---|---|---|---|
| M1 | J1 | 0 | 45 |
| M1 | J4 | 45 | 80 |
| M1 | J7 | 80 | 140 |
| M2 | J2 | 10 | 35 |
| M2 | J5 | 35 | 55 |
| M2 | J8 | 55 | 95 |
| M3 | J3 | 5 | 55 |
| M3 | J6 | 55 | 85 |

Este reto fue diseñado por : Nicolás Ospina, Santiago Tapia, Daniela Arizmendi y Melina Kaihara


---

<!-- fuente: corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/construir_plantillas.py -->
# Código: `corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/construir_plantillas.py`

> Archivo completo: https://github.com/samuelgradientai-sys/planeacion-control-produccion/blob/main/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/construir_plantillas.py

```python
"""
Genera las versiones "plantilla Gradescope" (reto_schedulling.py) a partir de
reto1.py y reto2.py, para no mantener dos copias del algoritmo a mano.

    python construir_plantillas.py

Copia el bloque entre "# === INICIO ALGORITMO ===" y "# === FIN ALGORITMO ==="
de cada reto dentro de la plantilla del profesor (misma clase, mismos metodos
y mismo ejecutar_experimentos). Correr esto cada vez que se cambie reto1.py o
reto2.py.
"""
import os

AQUI = os.path.dirname(os.path.abspath(__file__))


def bloque(archivo):
    with open(os.path.join(AQUI, archivo), encoding="utf-8") as f:
        texto = f.read()
    ini = texto.index("# === INICIO ALGORITMO ===")
    fin = texto.index("# === FIN ALGORITMO ===") + len("# === FIN ALGORITMO ===")
    return texto[ini:fin]


# ---------------------------------------------------------------- Reto 1
PLANTILLA_R1 = '''"""
Plantilla base para GradeScope - RETO 01 Willy Wonka
-------------------------------------------------------
             INSTRUCCIONES IMPORTANTES
-------------------------------------------------------
1. NO cambiar el nombre de la clase ni las funciones principales.
   - Clase obligatoria: Schedulling
   - Metodos obligatorios: generar_instancia(), resolver_instancia(), ejecutar_experimentos()
2. SOLO deben modificar:
   - El contenido de generar_instancia() para crear sus propios datos.
   - El contenido de resolver_instancia() para construir su modelo de optimizacion.
3. NO modificar:
   - Los nombres de las funciones o variables internas del experimento.
   - El metodo ejecutar_experimentos() ni su estructura.
   - El nombre del archivo: debe llamarse EXACTAMENTE `reto_schedulling.py`
4. El metodo ejecutar_experimentos():
   - Ejecuta automaticamente 30 instancias.
   - Mide el tiempo de ejecucion por instancia.
   - Devuelve un consolidado con los tiempos individuales.
   - Reporta el tiempo promedio y el total al final.

ARCHIVO GENERADO por construir_plantillas.py a partir de reto1.py (no editar a mano).
Algoritmo: cota inferior por ordenes de tipo + heuristica (NEH, bloques por tipo,
busqueda local con aceleracion de Taillard) + programacion dinamica acotada que
encuentra y demuestra el optimo. Ver reto1.py e INFORME_TECNICO.md.
"""

# Agregar dependencias si es necesario, pero sin remover las que ya se encuentran abajo
import random
import numpy as np
import time
import pandas as pd
try:  # modulo del ejemplo del profesor; no se usa y puede no existir en Gradescope
    from optimizador import load_from_dict, run_ga  # noqa: F401
except ImportError:
    pass
import json
import itertools
import math

__ALGORITMO__


class Schedulling:
    def __init__(self, n_instancias: int = 30, semilla: int = 42):
        """
        Inicializa la clase con numero de instancias y semilla.
        No modificar esta funcion.
        """
        self.n_instancias = n_instancias
        self.semilla = semilla
        random.seed(semilla)
        np.random.seed(semilla)
        self.resultados = {"instancia": [], "valor_objetivo": [], "tiempo_seg": []}
        self.consolidado = None

    def generar_instancia(self, indice):
        """
        Genera una instancia aleatoria del problema de lotes y setups.
        Retorna un diccionario con los tiempos de procesamiento y tiempos de setup.
        """
        tipos = ["S", "N", "R"]
        lotes = [f"L{i}" for i in range(1, 16)]

        # Rangos de tiempos de procesamiento por maquina
        rangos = {
            "M1": (25, 45),
            "M2": (20, 40),
            "M3": (10, 25)
        }

        # --------------------------
        # Generar datos de los lotes
        # --------------------------
        lotes_dict = {}
        for lote in lotes:
            tipo = random.choice(tipos)
            lotes_dict[lote] = {
                "tipo": tipo,
                "M1": random.randint(*rangos["M1"]),
                "M2": random.randint(*rangos["M2"]),
                "M3": random.randint(*rangos["M3"])
            }

        # --------------------------
        # Generar tiempos de setup
        # --------------------------
        setup_dict = {}
        for maquina in ["M1", "M2", "M3"]:
            setup_dict[maquina] = {}
            for tipo_ant in tipos:
                for tipo_sig in tipos:
                    if tipo_ant == tipo_sig:
                        tiempo_setup = 0
                    else:
                        if maquina == "M1":
                            tiempo_setup = random.randint(10, 40)
                        elif maquina == "M2":
                            tiempo_setup = random.randint(5, 30)
                        else:  # M3
                            tiempo_setup = random.randint(3, 15)
                    setup_dict[maquina][f"{tipo_ant}-{tipo_sig}"] = tiempo_setup

        # --------------------------
        # Consolidar instancia
        # --------------------------
        instancia = {
            "lotes": lotes_dict,
            "setup": setup_dict
        }
        with open(f'instancia_{indice}.json', "w", encoding="utf-8") as f:
            json.dump(instancia, f, indent=4, ensure_ascii=False)

        return instancia

    def resolver_instancia(self, instancia: dict):
        inicio = time.time()
        modelo = WillyWonka(instancia)
        seq, cmax, _ = modelo.resolver()
        secuencia = [modelo.nombres[j] for j in seq]
        return {
            "secuencia": secuencia,
            "valor_objetivo": int(cmax),
            "Cmax": int(cmax),
            "tiempo": int((time.time() - inicio) * 1000),
        }

    def ejecutar_experimentos(self):
        """
        Genera y resuelve las instancias, mide tiempos de ejecucion
        y consolida los resultados.
        NO modificar esta funcion.
        """
        print(f"Ejecutando {self.n_instancias} instancias...\\n")

        # Reinicia resultados
        self.resultados = {"instancia": [], "valor_objetivo": [], "tiempo_seg": []}

        inicio_total = time.time()

        for i in range(1, self.n_instancias + 1):
            instancia = self.generar_instancia(i)
            t0 = time.time()
            resultado = self.resolver_instancia(instancia)
            t1 = time.time()

            # Guarda resultados
            self.resultados["instancia"].append(i)
            self.resultados["valor_objetivo"].append(resultado["valor_objetivo"])
            self.resultados["tiempo_seg"].append(round(t1 - t0, 4))

            print(f"Instancia {i} optimizada en {round(t1 - t0, 4)} seg")

        # Tiempo total
        tiempo_total = time.time() - inicio_total

        # Crear DataFrame consolidado
        self.consolidado = pd.DataFrame(self.resultados)

        # Calcular promedios solo de tiempo
        promedio_tiempo = self.consolidado["tiempo_seg"].mean()

        print("\\n==== REPORTE DE RENDIMIENTO ====")
        print("Tiempo promedio por instancia:", round(promedio_tiempo, 4), "seg")
        print("Tiempo total de ejecución:", round(tiempo_total, 2), "seg")

        return self.consolidado

    def calcular_makespan_penalizado(self , data={}, secuencia=[f'L{i}' for i in range(1,16)]):
        lotes = data["lotes"]
        setup = data["setup"]
        maquinas = ["M1", "M2", "M3"]

        # Validación: N no puede ir inmediatamente antes de R
        penalizado = False
        for i in range(1, len(secuencia)):
            tipo_anterior = lotes[secuencia[i-1]]["tipo"]
            tipo_actual = lotes[secuencia[i]]["tipo"]
            if tipo_anterior == "N" and tipo_actual == "R":
                penalizado = True
                break

        fin_maquina = {m: 0 for m in maquinas}
        fin_lote = {l: 0 for l in secuencia}

        for lote in secuencia:
            tipo_actual = lotes[lote]["tipo"]
            for m_idx, m in enumerate(maquinas):
                prev_tipo = None
                # Buscar el último tipo procesado en esta máquina
                if fin_maquina[m] > 0:
                    for l in secuencia:
                        if fin_lote[l] <= fin_maquina[m] and l != lote:
                            prev_tipo = lotes[l]["tipo"]

                t_setup = 0
                if prev_tipo is not None and prev_tipo != tipo_actual:
                    t_setup = setup[m][f"{prev_tipo}-{tipo_actual}"]

                if m_idx == 0:
                    inicio = fin_maquina[m] + t_setup
                else:
                    inicio = max(fin_maquina[m], fin_lote[lote]) + t_setup

                duracion = lotes[lote][m]
                fin = inicio + duracion

                fin_maquina[m] = fin
                fin_lote[lote] = fin

        makespan = max(fin_maquina.values())

        # Penalización si se violó la regla N → R
        if penalizado:
            makespan = float('inf')

        return makespan
# ----------------------------------------------------------
# Ejecución directa (GradeScope)
# ----------------------------------------------------------
if __name__ == "__main__":
    sch = Schedulling(30)
    df_resultados = sch.ejecutar_experimentos()
    print("\\nConsolidado final:")
    print(df_resultados)
'''

# ---------------------------------------------------------------- Reto 2
PLANTILLA_R2 = '''

# Plantilla base para GradeScope - RETO 02 Monstruopolis
# este archivo debe llamarse reto_schedulling.py
# ARCHIVO GENERADO por construir_plantillas.py a partir de reto2.py (no editar a mano).
# Algoritmo: reglas de despacho (WSPT, ATC, cadenas, EDD) + recocido simulado sobre
# la lista de prioridad con evaluacion incremental + busqueda local por insercion.
# Agregar dependencias si es necesario, pero sin remover las que ya se encuentran abajo
import random
import numpy as np
import time
import pandas as pd
import json

# === Dependencias para el modelo===
from itertools import product, combinations
from generador import GeneradorInstancias
import heapq
import math
import re
from bisect import bisect_right, insort

__ALGORITMO__


class Schedulling(GeneradorInstancias):
    def __init__(self, n_instancias: int = 30, semilla: int = 42, timelimit: int = 30):
        # reutilizamos el __init__ del generador
        super().__init__(n_instancias=n_instancias, semilla=semilla, timelimit=timelimit)
        self.timelimit = timelimit  # por claridad

    def resolver_instancia(self, instancia: dict):
        """
        Heuristica para:
            P3 | r_j, prec | Σ w_j T_j
        - Usa un simulador que respeta:
            * fechas de liberacion r_j
            * precedencias preds[j]
            * m maquinas paralelas sin solape
        """
        ids, p, r, d, w, preds, m = cargar_instancia(instancia)
        modelo = Monstruopolis(ids, p, r, d, w, preds, m)
        max_time = self.timelimit - 1.0 if self.timelimit else 29.0
        L, best_val, _ = modelo.resolver(tiempo_max=min(TIEMPO_MAX_R2, max_time))

        filas = {j: (k, s, c) for j, k, s, c in modelo.programa(L)}
        best_seq = []
        for j in range(len(ids)):
            k, sj, cj = filas[j]
            best_seq.append({
                "job": ids[j],
                "machine": f"M{k + 1}",
                "start": round(float(sj), 6),
                "end": round(float(cj), 6),
                "Cj": round(float(cj), 6)
            })

        return {
            "secuencia": best_seq,
            "valor_objetivo": round(float(best_val), 4)
        }
'''


def main():
    salidas = [
        (PLANTILLA_R1, "reto1.py", os.path.join("gradescope", "reto1_willy_wonka", "reto_schedulling.py")),
        (PLANTILLA_R2, "reto2.py", os.path.join("gradescope", "reto2_monstruopolis", "reto_schedulling.py")),
    ]
    for plantilla, origen, destino in salidas:
        ruta = os.path.join(AQUI, destino)
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(plantilla.replace("__ALGORITMO__", bloque(origen)))
        print("generado:", destino)


if __name__ == "__main__":
    main()
```


---

<!-- fuente: corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/INFORME_TECNICO.md -->
# Informe técnico: competencia de secuenciación de máquinas

Planeación, Programación y Control de las Operaciones. Universidad de La Sabana.
Integrantes: [nombres del grupo]

## 1. Resumen

| Reto | Problema | Método | Resultado en las instancias de prueba | Tiempo medio |
|---|---|---|---|---|
| 01 Willy Wonka | F3 \| prmu, s_ij por tipo, N→R prohibido \| Cmax | Cota inferior + heurística (NEH, bloques por tipo, búsqueda local con Taillard) + programación dinámica acotada | Óptimo **demostrado** en 30/30 instancias de la plantilla y en 200/200 de prueba | ~4 ms |
| 02 Monstruópolis | P3 \| r_j, prec \| Σ w_j T_j | Reglas de despacho + recocido simulado sobre una lista de prioridad con evaluación incremental | 0,05 % por encima del mejor valor conocido; 0 violaciones | ~80 ms |

Como el 30 % de la nota es tiempo de cómputo, en ambos retos se midió la curva calidad–tiempo y se fijaron los parámetros donde más tiempo ya casi no mejora la solución. No se usa todo el límite de 60 s.

## 2. Reto 01: Fábrica de Willy Wonka

**Modelo.** Flow shop de permutación de 3 máquinas en serie con 15 lotes. Al pasar de un lote de tipo *a* a uno de tipo *b*, la máquina *m* necesita un alistamiento s_m(a, b). Se usa la misma regla de tiempos de la plantilla: inicio(lote, M_k) = max(fin de M_k, fin del lote en M_{k−1}) + alistamiento. El primer lote no tiene alistamiento. Como la secuencia es la misma en las tres máquinas, la restricción "R no puede ir justo después de N" se revisa sobre parejas consecutivas de la secuencia.

**Algoritmo.** El algoritmo entrega el óptimo y además lo demuestra.

1. *Cota inferior (LB).* M1 nunca está ociosa, así que su tiempo total es Σ p1 más los alistamientos de M1. Para cada orden posible de los tipos de lote (un recorrido por los tipos que nunca pasa de N a R, con primer tipo *t1* y último tipo *tk*) se acota el Cmax en las tres máquinas **con ese mismo orden**:
   - B1 = Σ p1 + alistamientos en M1 + min (p2+p3) de los lotes de tipo *tk*;
   - B2 = min p1 de tipo *t1* + Σ p2 + alistamientos en M2 + min p3 de tipo *tk*;
   - B3 = min (p1+p2) de tipo *t1* + Σ p3 + alistamientos en M3.

   La LB es el mínimo, entre los órdenes posibles, de max(B1, B2, B3). Si una solución la alcanza, es óptima.
2. *Heurística rápida* para tener una buena solución. (a) NEH adaptado: lotes por tiempo total decreciente, cada uno en su mejor posición factible. (b) Secuencias por bloques de tipo: una por cada orden de bloques permitido (SRN, NSR, RSN, RNS), con los lotes de cada bloque ordenados por la regla de Johnson sobre (p1+p2, p2+p3). (c) Búsqueda local por inserción sobre la mejor, con la aceleración de Taillard adaptada a los alistamientos: al insertar *j* entre *a* y *b* solo cambian *j* y *b*, y Cmax = max_m (fin de *b* en *m* + cola de la posición siguiente en *m*). Así cada inserción cuesta O(n·m) en vez de O(n²·m).
3. *Método exacto: programación dinámica acotada* (en la línea de ramificación y acotamiento). Las secuencias se construyen lote a lote, por capas. El estado es (lotes ya programados, tipo del último). De cada estado se guardan solo los vectores (fin M1, fin M2, fin M3) no dominados y se descarta todo estado cuya cota (la misma del paso 1, desde el estado parcial) no puede mejorar la heurística. Si no sobrevive ningún estado, la heurística era óptima; si alguno sobrevive, sale la secuencia óptima. Dos detalles lo hacen rápido: los datos de los lotes que faltan se derivan del estado padre (solo se recalculan los mínimos del tipo que cambió) y los órdenes de tipos se calculan una sola vez.
4. *Respaldo.* Si el exacto llegara a su tope de seguridad (400 000 estados o 2 s), se aplica un Iterated Greedy (Ruiz y Stützle) sobre la heurística. No ocurrió en ninguna prueba.
5. *Factibilidad.* Internamente cada pareja N→R suma una penalidad de 10⁶ y el exacto nunca genera esas parejas. Las secuencias por bloques son siempre factibles.

**Justificación.** M1 es la máquina más cargada (25–45 min por lote más alistamientos de 10–40 min), así que el Cmax depende sobre todo de cuántas veces y en qué orden cambia de tipo. Por eso agrupar por tipo da buenas soluciones desde el inicio y la cota por órdenes de tipo es ajustada. Con 15 lotes y solo 3 tipos, una programación dinámica con buena cota resuelve el problema exactamente en milisegundos, así que no hace falta conformarse con una heurística.

**Resultados.** Además de la prueba que da el propio algoritmo, se comparó con un segundo método exacto implementado aparte, con una cota más simple. Ese exacto se validó contra fuerza bruta en 40 instancias de 8 lotes.

| Instancias (generador de la plantilla) | Óptimo demostrado | Tiempo medio | Mediana | Máximo |
|---|---|---|---|---|
| 30 (semilla 42, las de la plantilla) | 30/30 (12 solo con la cota) | 4,0 ms | 3,3 ms | 21 ms |
| 200 | 200/200 (115 solo con la cota) | 3,8 ms | 0,6 ms | 59 ms |
| 400 más difíciles (máquinas parejas, alistamientos de hasta 90 min) | 400/400 | 5–25 ms | | 265 ms |

| Configuración (200 instancias) | Óptimas | Tiempo medio |
|---|---|---|
| Solo NEH | 96/200 | 0,2 ms |
| NEH + bloques | 166/200 | 0,3 ms |
| + búsqueda local + Iterated Greedy corto (versión sin exacto) | 197/200, sin demostrar | 2,2 ms |
| **+ programación dinámica acotada (configuración entregada)** | **200/200, demostradas** | 3,8 ms |

El exacto pasó de 15,6 ms a 2,9 ms de costo promedio por dos cambios: la cota por órdenes de tipo (antes cada máquina usaba su mejor orden por separado) y derivar los datos de los lotes pendientes desde el estado padre. Una cota adicional de Johnson para pares de máquinas podaba más, pero costaba más de lo que ahorraba, así que se descartó.

*Ejemplo del enunciado (tablas 1 a 4).* Secuencia L9, L12, L6, L15, L3 (R) → L4, L13, L10, L1, L7 (S) → L8, L11, L5, L14, L2 (N). Cmax = 621 min, igual a la cota inferior, así que es óptimo. Se obtiene en 1 ms. Como es un flow shop de permutación, la secuencia es la misma en M1, M2 y M3. El último lote (L2) termina en M1 a los 573 min, en M2 a los 600 y en M3 a los 621.

## 3. Reto 02: Fábrica de juguetes de Monstruópolis

**Representación.** Una solución es una lista de prioridad: una permutación de los 50 trabajos donde cada predecesor va antes que sus sucesores. El decodificador programa los trabajos en ese orden, cada uno lo antes posible: listo_j = max(r_j, fin de sus predecesores). Se elige la máquina que permite empezar antes. Si varias permiten empezar en listo_j, se usa la que quedó libre más tarde (*best fit*), para no gastar las que quedaron libres antes. Toda lista así produce un programa factible, así que la búsqueda nunca genera soluciones infactibles.

**Algoritmo.**

1. *Reglas de despacho* para la lista inicial: WSPT estático y dinámico (w/p), ATC con K = 0,5, 1, 2 y 4, EDD y una razón de cadenas al estilo Sidney (un predecesor hereda la mayor razón Σw/Σp de las cadenas que salen de él, para no retrasar a un sucesor urgente). Se queda la mejor de las 8.
2. *Recocido simulado* sobre la lista: 10 000 movimientos de inserción o intercambio a distancia ≤ 20, con temperatura geométrica de 0,6 a 0,001 veces (peso medio × p medio). Para que cada vecino sea barato:
   - se guardan "fotos" del estado de las máquinas y del costo acumulado en cada posición, y se re-decodifica solo desde la primera posición que cambió;
   - el número aleatorio de Metropolis se sortea antes de evaluar, y la evaluación se corta apenas el costo supera el umbral de aceptación;
   - si después del tramo modificado las máquinas quedan igual que en la solución base (y ningún predecesor cambió su fin), el resto del programa es idéntico y su costo se toma de las fotos.

   Se verificó que esta evaluación incremental da exactamente lo mismo que decodificar todo, en unos 11 000 movimientos.

**Justificación.** El enunciado define d_j como el tiempo mínimo teórico de finalización. Entonces C_j ≥ d_j para todo trabajo, T_j = C_j − d_j y Σ w_j T_j = Σ w_j C_j − constante. El problema equivale a minimizar el tiempo de finalización ponderado, donde la regla de Smith (WSPT) es la referencia. Con esas fechas, ATC coincide con WSPT porque la holgura nunca es positiva. Las listas de prioridad con decodificador son la forma natural de manejar r_j y precedencias sin infactibilidades. El recocido supera a una búsqueda local por inserción completa porque, a igual tiempo, prueba muchos más vecinos.

**Resultados.** El generador de Gradescope no está disponible, así que se imitó según el enunciado (p_j 10–100, r_j 0–30, w_j 1–5, unas 5 precedencias sin ciclos, d_j = tiempo mínimo teórico). Cada instancia se comparó con el mejor valor de 3 corridas de 500 000 iteraciones (150 veces más largas). Todas las soluciones se revisaron con un validador independiente (r_j, precedencias, solapes, duraciones): 0 violaciones.

| Configuración (30 instancias) | Brecha media (máx.) | Tiempo medio |
|---|---|---|
| Solo reglas de despacho | 2,94 % (6,9 %) | 2 ms |
| Recocido 5 000 iteraciones | 0,17 % (1,0 %) | 37 ms |
| **Recocido 10 000 iteraciones (configuración entregada)** | 0,046 % (0,46 %) | 79 ms |
| Recocido 20 000 iteraciones | 0,042 % (0,56 %) | 151 ms |

La mejor regla inicial fue la razón de cadenas en 19 de 30 instancias, y WSPT dinámico (igual a ATC) en las otras 11. *Robustez:* si las fechas de entrega fueran holgadas (margen aleatorio de hasta media carga por máquina), el algoritmo sigue siendo factible y pasa de 18,6 % (reglas) a 1,8 % de brecha en el mismo tiempo; con 20 000 iteraciones baja a ~0,7 %.

*¿Qué tan lejos del óptimo?* Con 50 trabajos no es posible demostrar el óptimo en tiempo de competencia. Para acotar la distancia se calculó una cota inferior por relajación lagrangiana de la formulación indexada en el tiempo: cada trabajo elige su inicio pagando su tardanza más unos multiplicadores por usar cada instante, y la capacidad de 3 máquinas se relaja; los multiplicadores se ajustan por subgradiente. Nuestras soluciones quedan, en promedio, como máximo 2,4 % por encima de esa cota. Como la cota ya no sube con más iteraciones y las corridas 150 veces más largas solo mejoran 0,05 %, esa brecha refleja sobre todo la debilidad de la cota y no la del algoritmo.

En la evaluación de vecinos se agruparon los datos de cada trabajo en una tupla, lo que redujo ~10 % el tiempo sin cambiar resultados. También se probó asignar cada trabajo a la máquina que se libera primero (en vez de *best fit*): con esa regla el programa es monótono y permite cortar antes la evaluación, pero la calidad empeoró (0,19 % frente a 0,05 %) y el corte casi no se activaba, así que se descartó.

## 4. Lecciones aprendidas

- **Una buena cota convierte una heurística en un método exacto.** En el Reto 1 la heurística ya acertaba el óptimo en 97 % de los casos; con la cota por órdenes de tipo, la programación dinámica acotada lo demuestra (o lo encuentra) en todos los casos, a un costo de ~1,6 ms adicionales en promedio.
- **En Python, lo que cuesta evaluar un vecino decide cuánto se puede buscar.** La aceleración de Taillard, las fotos del estado, el umbral sorteado antes de evaluar y el corte por convergencia permitieron soluciones casi óptimas en milisegundos.
- **Medir antes de agregar complejidad.** Varias ideas razonables no sirvieron al medirlas: la cota de Johnson en el Reto 1 y la regla de máquina que se libera primero en el Reto 2 costaban más de lo que aportaban. En el Reto 2, pasar de 10 000 a 20 000 iteraciones duplica el tiempo y casi no cambia la brecha.
- **Es mejor garantizar la factibilidad por construcción que repararla después**: decodificador con listas topológicas en el Reto 2, y en el Reto 1 una solución inicial factible más una penalización.
- **Hay que validar la función de evaluación.** La función `calcular_makespan_penalizado` de la plantilla toma como "tipo anterior" el del último lote de la secuencia (los lotes sin procesar tienen fin 0), por eso da valores mayores que el Cmax real. Nuestro algoritmo optimiza el Cmax del enunciado.

## Referencias

Johnson, S. M. (1954). Optimal two- and three-stage production schedules with setup times included. *Naval Research Logistics Quarterly*, 1(1), 61–68.
Kirkpatrick, S., Gelatt, C. D., & Vecchi, M. P. (1983). Optimization by simulated annealing. *Science*, 220(4598), 671–680.
Nawaz, M., Enscore, E. E., & Ham, I. (1983). A heuristic algorithm for the m-machine, n-job flow-shop sequencing problem. *Omega*, 11(1), 91–95.
Pinedo, M. L. (2016). *Scheduling: Theory, algorithms, and systems* (5.ª ed.). Springer.
Ruiz, R., & Stützle, T. (2007). A simple and effective iterated greedy algorithm for the permutation flowshop scheduling problem. *European Journal of Operational Research*, 177(3), 2033–2049.
Ruiz, R., & Stützle, T. (2008). An iterated greedy heuristic for the sequence dependent setup times flowshop problem with makespan and weighted tardiness objectives. *European Journal of Operational Research*, 187(3), 1143–1159.
Sidney, J. B. (1975). Decomposition algorithms for single-machine sequencing with precedence relations and deferral costs. *Operations Research*, 23(2), 283–298.
Smith, W. E. (1956). Various optimizers for single-stage production. *Naval Research Logistics Quarterly*, 3(1–2), 59–66.
Taillard, E. (1990). Some efficient heuristic methods for the flow shop sequencing problem. *European Journal of Operational Research*, 47(1), 65–74.
Vepsalainen, A. P. J., & Morton, T. E. (1987). Priority rules for job shops with weighted tardiness costs. *Management Science*, 33(8), 1035–1047.


---

<!-- fuente: corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/cota_reto2.py -->
# Código: `corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/cota_reto2.py`

> Archivo completo: https://github.com/samuelgradientai-sys/planeacion-control-produccion/blob/main/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/cota_reto2.py

```python
"""
Cota inferior fuerte para el RETO 02 (solo para medir que tan cerca del optimo
estamos; no se sube). Usa numpy.

Formulacion indexada en el tiempo: cada trabajo j escoge un inicio s >= e_j
(e_j = inicio mas temprano por r_j y precedencias) y paga w_j * max(0, s + p_j - d_j).
La restriccion "a lo sumo m trabajos a la vez" se relaja con multiplicadores
lambda_t >= 0 (relajacion lagrangiana):

    L(lambda) = sum_j min_s [ w_j T_j(s) + sum_{t=s}^{s+p_j-1} lambda_t ] - m * sum_t lambda_t

Para cualquier lambda >= 0, L(lambda) <= optimo. Se busca el mejor lambda con
subgradiente (paso de Polyak). Se ignoran las precedencias entre trabajos salvo
el inicio mas temprano, asi que es una cota valida.

    python pruebas/cota_reto2.py          -> brecha de reto2.py contra la cota en 30 instancias
"""
import os
import random
import sys

import numpy as np

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))
sys.path.insert(0, AQUI)


def cota_lagrangiana(inst, ub, iteraciones=800):
    jobs, m = inst["jobs"], inst["m"]
    p = np.array([inst["p"][j] for j in jobs])
    w = np.array([inst["w"][j] for j in jobs], dtype=float)
    d = np.array([inst["d"][j] for j in jobs])
    # inicio mas temprano por liberacion y precedencias (CPM)
    e = {}
    for j in jobs:                                   # los predecesores van antes en la lista
        e[j] = max([inst["r"][j]] + [e[i] + inst["p"][i] for i in inst["preds"][j]])
    pend = [j for j in jobs if any(i not in e for i in inst["preds"][j])]
    assert not pend
    e = np.array([e[j] for j in jobs])
    n = len(jobs)
    T = int(e.max() + p.sum())                       # horizonte seguro
    S = np.arange(T)
    fin = S[None, :] + p[:, None]                    # n x T
    valido = (S[None, :] >= e[:, None]) & (fin <= T)
    tard = w[:, None] * np.maximum(0, fin - d[:, None])
    fin_c = np.minimum(fin, T)
    lam = np.zeros(T)
    mejor = 0.0
    mu = 2.0
    sin_mejora = 0
    filas = np.arange(n)
    for _ in range(iteraciones):
        Lc = np.concatenate(([0.0], np.cumsum(lam)))   # Lc[t] = sum lam[0..t-1]
        costo = tard + Lc[fin_c] - Lc[S][None, :]
        costo[~valido] = np.inf
        s = costo.argmin(axis=1)
        valor = costo[filas, s].sum() - m * lam.sum()
        if valor > mejor + 1e-9:
            mejor, sin_mejora = valor, 0
        else:
            sin_mejora += 1
            if sin_mejora >= 25:
                mu, sin_mejora = mu / 2, 0
                if mu < 1e-4:
                    break
        uso = np.zeros(T + 1)
        np.add.at(uso, s, 1)
        np.add.at(uso, s + p, -1)
        g = np.cumsum(uso)[:T] - m
        norma = float((g * g).sum())
        if norma == 0:
            break
        lam = np.maximum(0.0, lam + mu * (ub - valor) / norma * g)
    return mejor


if __name__ == "__main__":
    import time
    import statistics
    import reto2
    from generador import generar
    holgura = float(sys.argv[1]) if len(sys.argv) > 1 else 0.0
    rng = random.Random(42)
    instancias = [generar(rng, holgura=holgura) for _ in range(30)]
    brechas = []
    for k, inst in enumerate(instancias, 1):
        ub = reto2.tardanza_ponderada(inst, reto2.solve(inst))
        t0 = time.perf_counter()
        lb = cota_lagrangiana(inst, ub)
        brechas.append(100 * (ub - lb) / ub)
        print(f"inst {k:>2}: nuestra {ub:>7}  cota {lb:9.1f}  brecha <= {brechas[-1]:.2f}%  ({time.perf_counter() - t0:.1f} s)")
    print(f"\nbrecha promedio contra la cota: {statistics.mean(brechas):.2f}%  (max {max(brechas):.2f}%)")
```


---

<!-- fuente: corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/data_ejemplo_reto1.json -->
# Código: `corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/data_ejemplo_reto1.json`

> Archivo completo: https://github.com/samuelgradientai-sys/planeacion-control-produccion/blob/main/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/data_ejemplo_reto1.json

```json
{
  "lotes": {
    "L1": {
      "tipo": "S",
      "M1": 38,
      "M2": 33,
      "M3": 19
    },
    "L2": {
      "tipo": "N",
      "M1": 41,
      "M2": 27,
      "M3": 21
    },
    "L3": {
      "tipo": "R",
      "M1": 29,
      "M2": 37,
      "M3": 14
    },
    "L4": {
      "tipo": "S",
      "M1": 35,
      "M2": 24,
      "M3": 22
    },
    "L5": {
      "tipo": "N",
      "M1": 44,
      "M2": 38,
      "M3": 16
    },
    "L6": {
      "tipo": "R",
      "M1": 27,
      "M2": 31,
      "M3": 18
    },
    "L7": {
      "tipo": "S",
      "M1": 40,
      "M2": 28,
      "M3": 25
    },
    "L8": {
      "tipo": "N",
      "M1": 33,
      "M2": 40,
      "M3": 12
    },
    "L9": {
      "tipo": "R",
      "M1": 31,
      "M2": 22,
      "M3": 17
    },
    "L10": {
      "tipo": "S",
      "M1": 39,
      "M2": 35,
      "M3": 15
    },
    "L11": {
      "tipo": "N",
      "M1": 42,
      "M2": 26,
      "M3": 23
    },
    "L12": {
      "tipo": "R",
      "M1": 28,
      "M2": 34,
      "M3": 13
    },
    "L13": {
      "tipo": "S",
      "M1": 36,
      "M2": 29,
      "M3": 20
    },
    "L14": {
      "tipo": "N",
      "M1": 45,
      "M2": 25,
      "M3": 24
    },
    "L15": {
      "tipo": "R",
      "M1": 30,
      "M2": 39,
      "M3": 11
    }
  },
  "setup": {
    "M1": {
      "S-S": 0,
      "S-N": 15,
      "S-R": 35,
      "N-S": 25,
      "N-N": 0,
      "N-R": 40,
      "R-S": 20,
      "R-N": 25,
      "R-R": 0
    },
    "M2": {
      "S-S": 0,
      "S-N": 10,
      "S-R": 25,
      "N-S": 15,
      "N-N": 0,
      "N-R": 30,
      "R-S": 10,
      "R-N": 20,
      "R-R": 0
    },
    "M3": {
      "S-S": 0,
      "S-N": 5,
      "S-R": 10,
      "N-S": 8,
      "N-N": 0,
      "N-R": 12,
      "R-S": 6,
      "R-N": 9,
      "R-R": 0
    }
  }
}
```


---

<!-- fuente: corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/data_ejemplo_reto2.json -->
# Código: `corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/data_ejemplo_reto2.json`

> Archivo completo: https://github.com/samuelgradientai-sys/planeacion-control-produccion/blob/main/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/data_ejemplo_reto2.json

```json
[
 {
  "Trabajo": "J1",
  "p_j": 16,
  "r_j": 20,
  "d_j": 36,
  "w_j": 3,
  "Predecesores": ""
 },
 {
  "Trabajo": "J2",
  "p_j": 44,
  "r_j": 16,
  "d_j": 60,
  "w_j": 1,
  "Predecesores": ""
 },
 {
  "Trabajo": "J3",
  "p_j": 21,
  "r_j": 18,
  "d_j": 39,
  "w_j": 2,
  "Predecesores": ""
 },
 {
  "Trabajo": "J4",
  "p_j": 62,
  "r_j": 25,
  "d_j": 87,
  "w_j": 5,
  "Predecesores": ""
 },
 {
  "Trabajo": "J5",
  "p_j": 44,
  "r_j": 30,
  "d_j": 74,
  "w_j": 1,
  "Predecesores": ""
 },
 {
  "Trabajo": "J6",
  "p_j": 23,
  "r_j": 10,
  "d_j": 33,
  "w_j": 3,
  "Predecesores": ""
 },
 {
  "Trabajo": "J7",
  "p_j": 14,
  "r_j": 0,
  "d_j": 14,
  "w_j": 1,
  "Predecesores": ""
 },
 {
  "Trabajo": "J8",
  "p_j": 58,
  "r_j": 12,
  "d_j": 70,
  "w_j": 3,
  "Predecesores": ""
 },
 {
  "Trabajo": "J9",
  "p_j": 78,
  "r_j": 28,
  "d_j": 106,
  "w_j": 2,
  "Predecesores": ""
 },
 {
  "Trabajo": "J10",
  "p_j": 81,
  "r_j": 24,
  "d_j": 105,
  "w_j": 4,
  "Predecesores": ""
 },
 {
  "Trabajo": "J11",
  "p_j": 52,
  "r_j": 20,
  "d_j": 72,
  "w_j": 5,
  "Predecesores": ""
 },
 {
  "Trabajo": "J12",
  "p_j": 53,
  "r_j": 16,
  "d_j": 69,
  "w_j": 5,
  "Predecesores": ""
 },
 {
  "Trabajo": "J13",
  "p_j": 16,
  "r_j": 13,
  "d_j": 29,
  "w_j": 1,
  "Predecesores": ""
 },
 {
  "Trabajo": "J14",
  "p_j": 30,
  "r_j": 21,
  "d_j": 51,
  "w_j": 3,
  "Predecesores": ""
 },
 {
  "Trabajo": "J15",
  "p_j": 27,
  "r_j": 17,
  "d_j": 44,
  "w_j": 4,
  "Predecesores": ""
 },
 {
  "Trabajo": "J16",
  "p_j": 53,
  "r_j": 20,
  "d_j": 73,
  "w_j": 2,
  "Predecesores": ""
 },
 {
  "Trabajo": "J17",
  "p_j": 81,
  "r_j": 25,
  "d_j": 106,
  "w_j": 5,
  "Predecesores": ""
 },
 {
  "Trabajo": "J18",
  "p_j": 52,
  "r_j": 21,
  "d_j": 73,
  "w_j": 4,
  "Predecesores": ""
 },
 {
  "Trabajo": "J19",
  "p_j": 99,
  "r_j": 19,
  "d_j": 118,
  "w_j": 2,
  "Predecesores": ""
 },
 {
  "Trabajo": "J20",
  "p_j": 41,
  "r_j": 28,
  "d_j": 69,
  "w_j": 2,
  "Predecesores": ""
 },
 {
  "Trabajo": "J21",
  "p_j": 30,
  "r_j": 26,
  "d_j": 90,
  "w_j": 5,
  "Predecesores": "J2"
 },
 {
  "Trabajo": "J22",
  "p_j": 10,
  "r_j": 15,
  "d_j": 25,
  "w_j": 4,
  "Predecesores": ""
 },
 {
  "Trabajo": "J23",
  "p_j": 65,
  "r_j": 16,
  "d_j": 81,
  "w_j": 4,
  "Predecesores": ""
 },
 {
  "Trabajo": "J24",
  "p_j": 21,
  "r_j": 21,
  "d_j": 42,
  "w_j": 4,
  "Predecesores": ""
 },
 {
  "Trabajo": "J25",
  "p_j": 86,
  "r_j": 13,
  "d_j": 99,
  "w_j": 1,
  "Predecesores": ""
 },
 {
  "Trabajo": "J26",
  "p_j": 58,
  "r_j": 11,
  "d_j": 69,
  "w_j": 1,
  "Predecesores": ""
 },
 {
  "Trabajo": "J27",
  "p_j": 18,
  "r_j": 16,
  "d_j": 99,
  "w_j": 2,
  "Predecesores": "J23"
 },
 {
  "Trabajo": "J28",
  "p_j": 10,
  "r_j": 1,
  "d_j": 11,
  "w_j": 4,
  "Predecesores": ""
 },
 {
  "Trabajo": "J29",
  "p_j": 50,
  "r_j": 27,
  "d_j": 77,
  "w_j": 2,
  "Predecesores": ""
 },
 {
  "Trabajo": "J30",
  "p_j": 67,
  "r_j": 24,
  "d_j": 91,
  "w_j": 1,
  "Predecesores": ""
 },
 {
  "Trabajo": "J31",
  "p_j": 23,
  "r_j": 20,
  "d_j": 129,
  "w_j": 3,
  "Predecesores": "J17"
 },
 {
  "Trabajo": "J32",
  "p_j": 15,
  "r_j": 5,
  "d_j": 20,
  "w_j": 3,
  "Predecesores": ""
 },
 {
  "Trabajo": "J33",
  "p_j": 21,
  "r_j": 23,
  "d_j": 44,
  "w_j": 3,
  "Predecesores": ""
 },
 {
  "Trabajo": "J34",
  "p_j": 95,
  "r_j": 26,
  "d_j": 121,
  "w_j": 4,
  "Predecesores": ""
 },
 {
  "Trabajo": "J35",
  "p_j": 28,
  "r_j": 2,
  "d_j": 30,
  "w_j": 4,
  "Predecesores": ""
 },
 {
  "Trabajo": "J36",
  "p_j": 26,
  "r_j": 29,
  "d_j": 55,
  "w_j": 1,
  "Predecesores": "J22"
 },
 {
  "Trabajo": "J37",
  "p_j": 12,
  "r_j": 15,
  "d_j": 27,
  "w_j": 1,
  "Predecesores": ""
 },
 {
  "Trabajo": "J38",
  "p_j": 47,
  "r_j": 21,
  "d_j": 68,
  "w_j": 5,
  "Predecesores": ""
 },
 {
  "Trabajo": "J39",
  "p_j": 65,
  "r_j": 8,
  "d_j": 73,
  "w_j": 1,
  "Predecesores": ""
 },
 {
  "Trabajo": "J40",
  "p_j": 83,
  "r_j": 5,
  "d_j": 88,
  "w_j": 5,
  "Predecesores": ""
 },
 {
  "Trabajo": "J41",
  "p_j": 71,
  "r_j": 10,
  "d_j": 81,
  "w_j": 3,
  "Predecesores": ""
 },
 {
  "Trabajo": "J42",
  "p_j": 43,
  "r_j": 10,
  "d_j": 53,
  "w_j": 1,
  "Predecesores": ""
 },
 {
  "Trabajo": "J43",
  "p_j": 70,
  "r_j": 17,
  "d_j": 87,
  "w_j": 1,
  "Predecesores": ""
 },
 {
  "Trabajo": "J44",
  "p_j": 14,
  "r_j": 12,
  "d_j": 26,
  "w_j": 4,
  "Predecesores": ""
 },
 {
  "Trabajo": "J45",
  "p_j": 49,
  "r_j": 28,
  "d_j": 77,
  "w_j": 1,
  "Predecesores": ""
 },
 {
  "Trabajo": "J46",
  "p_j": 53,
  "r_j": 2,
  "d_j": 55,
  "w_j": 5,
  "Predecesores": ""
 },
 {
  "Trabajo": "J47",
  "p_j": 76,
  "r_j": 23,
  "d_j": 99,
  "w_j": 4,
  "Predecesores": ""
 },
 {
  "Trabajo": "J48",
  "p_j": 71,
  "r_j": 14,
  "d_j": 85,
  "w_j": 1,
  "Predecesores": ""
 },
 {
  "Trabajo": "J49",
  "p_j": 36,
  "r_j": 12,
  "d_j": 75,
  "w_j": 5,
  "Predecesores": "J3"
 },
 {
  "Trabajo": "J50",
  "p_j": 87,
  "r_j": 18,
  "d_j": 105,
  "w_j": 4,
  "Predecesores": ""
 }
]
```


---

<!-- fuente: corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/data_ejemplo_reto2_plantilla.json -->
# Código: `corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/data_ejemplo_reto2_plantilla.json`

> Archivo completo: https://github.com/samuelgradientai-sys/planeacion-control-produccion/blob/main/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/data_ejemplo_reto2_plantilla.json

```json
{
 "jobs": [
  "J1",
  "J2",
  "J3",
  "J4",
  "J5",
  "J6",
  "J7",
  "J8",
  "J9",
  "J10",
  "J11",
  "J12",
  "J13",
  "J14",
  "J15",
  "J16",
  "J17",
  "J18",
  "J19",
  "J20",
  "J21",
  "J22",
  "J23",
  "J24",
  "J25",
  "J26",
  "J27",
  "J28",
  "J29",
  "J30",
  "J31",
  "J32",
  "J33",
  "J34",
  "J35",
  "J36",
  "J37",
  "J38",
  "J39",
  "J40",
  "J41",
  "J42",
  "J43",
  "J44",
  "J45",
  "J46",
  "J47",
  "J48",
  "J49",
  "J50"
 ],
 "m": 3,
 "p": {
  "J1": 16,
  "J2": 44,
  "J3": 21,
  "J4": 62,
  "J5": 44,
  "J6": 23,
  "J7": 14,
  "J8": 58,
  "J9": 78,
  "J10": 81,
  "J11": 52,
  "J12": 53,
  "J13": 16,
  "J14": 30,
  "J15": 27,
  "J16": 53,
  "J17": 81,
  "J18": 52,
  "J19": 99,
  "J20": 41,
  "J21": 30,
  "J22": 10,
  "J23": 65,
  "J24": 21,
  "J25": 86,
  "J26": 58,
  "J27": 18,
  "J28": 10,
  "J29": 50,
  "J30": 67,
  "J31": 23,
  "J32": 15,
  "J33": 21,
  "J34": 95,
  "J35": 28,
  "J36": 26,
  "J37": 12,
  "J38": 47,
  "J39": 65,
  "J40": 83,
  "J41": 71,
  "J42": 43,
  "J43": 70,
  "J44": 14,
  "J45": 49,
  "J46": 53,
  "J47": 76,
  "J48": 71,
  "J49": 36,
  "J50": 87
 },
 "r": {
  "J1": 20,
  "J2": 16,
  "J3": 18,
  "J4": 25,
  "J5": 30,
  "J6": 10,
  "J7": 0,
  "J8": 12,
  "J9": 28,
  "J10": 24,
  "J11": 20,
  "J12": 16,
  "J13": 13,
  "J14": 21,
  "J15": 17,
  "J16": 20,
  "J17": 25,
  "J18": 21,
  "J19": 19,
  "J20": 28,
  "J21": 26,
  "J22": 15,
  "J23": 16,
  "J24": 21,
  "J25": 13,
  "J26": 11,
  "J27": 16,
  "J28": 1,
  "J29": 27,
  "J30": 24,
  "J31": 20,
  "J32": 5,
  "J33": 23,
  "J34": 26,
  "J35": 2,
  "J36": 29,
  "J37": 15,
  "J38": 21,
  "J39": 8,
  "J40": 5,
  "J41": 10,
  "J42": 10,
  "J43": 17,
  "J44": 12,
  "J45": 28,
  "J46": 2,
  "J47": 23,
  "J48": 14,
  "J49": 12,
  "J50": 18
 },
 "d": {
  "J1": 36,
  "J2": 60,
  "J3": 39,
  "J4": 87,
  "J5": 74,
  "J6": 33,
  "J7": 14,
  "J8": 70,
  "J9": 106,
  "J10": 105,
  "J11": 72,
  "J12": 69,
  "J13": 29,
  "J14": 51,
  "J15": 44,
  "J16": 73,
  "J17": 106,
  "J18": 73,
  "J19": 118,
  "J20": 69,
  "J21": 90,
  "J22": 25,
  "J23": 81,
  "J24": 42,
  "J25": 99,
  "J26": 69,
  "J27": 99,
  "J28": 11,
  "J29": 77,
  "J30": 91,
  "J31": 129,
  "J32": 20,
  "J33": 44,
  "J34": 121,
  "J35": 30,
  "J36": 55,
  "J37": 27,
  "J38": 68,
  "J39": 73,
  "J40": 88,
  "J41": 81,
  "J42": 53,
  "J43": 87,
  "J44": 26,
  "J45": 77,
  "J46": 55,
  "J47": 99,
  "J48": 85,
  "J49": 75,
  "J50": 105
 },
 "w": {
  "J1": 3,
  "J2": 1,
  "J3": 2,
  "J4": 5,
  "J5": 1,
  "J6": 3,
  "J7": 1,
  "J8": 3,
  "J9": 2,
  "J10": 4,
  "J11": 5,
  "J12": 5,
  "J13": 1,
  "J14": 3,
  "J15": 4,
  "J16": 2,
  "J17": 5,
  "J18": 4,
  "J19": 2,
  "J20": 2,
  "J21": 5,
  "J22": 4,
  "J23": 4,
  "J24": 4,
  "J25": 1,
  "J26": 1,
  "J27": 2,
  "J28": 4,
  "J29": 2,
  "J30": 1,
  "J31": 3,
  "J32": 3,
  "J33": 3,
  "J34": 4,
  "J35": 4,
  "J36": 1,
  "J37": 1,
  "J38": 5,
  "J39": 1,
  "J40": 5,
  "J41": 3,
  "J42": 1,
  "J43": 1,
  "J44": 4,
  "J45": 1,
  "J46": 5,
  "J47": 4,
  "J48": 1,
  "J49": 5,
  "J50": 4
 },
 "preds": {
  "J1": [],
  "J2": [],
  "J3": [],
  "J4": [],
  "J5": [],
  "J6": [],
  "J7": [],
  "J8": [],
  "J9": [],
  "J10": [],
  "J11": [],
  "J12": [],
  "J13": [],
  "J14": [],
  "J15": [],
  "J16": [],
  "J17": [],
  "J18": [],
  "J19": [],
  "J20": [],
  "J21": [
   "J2"
  ],
  "J22": [],
  "J23": [],
  "J24": [],
  "J25": [],
  "J26": [],
  "J27": [
   "J23"
  ],
  "J28": [],
  "J29": [],
  "J30": [],
  "J31": [
   "J17"
  ],
  "J32": [],
  "J33": [],
  "J34": [],
  "J35": [],
  "J36": [
   "J22"
  ],
  "J37": [],
  "J38": [],
  "J39": [],
  "J40": [],
  "J41": [],
  "J42": [],
  "J43": [],
  "J44": [],
  "J45": [],
  "J46": [],
  "J47": [],
  "J48": [],
  "J49": [
   "J3"
  ],
  "J50": []
 }
}
```


---

<!-- fuente: corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/exacto_reto1.py -->
# Código: `corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/exacto_reto1.py`

> Archivo completo: https://github.com/samuelgradientai-sys/planeacion-control-produccion/blob/main/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/exacto_reto1.py

```python
"""
Metodo exacto para verificar el RETO 01: programacion dinamica por capas con
frentes de Pareto y poda por cota. Solo para pruebas (no se sube).

Estado: (lotes ya programados, tipo del ultimo lote). Para cada estado se
guardan los vectores (fin M1, fin M2, fin M3) no dominados. Un estado se poda
si su cota inferior ya no puede mejorar la mejor solucion conocida (UB).
Si nada sobrevive, la UB es optima.
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))

import reto1  # noqa: E402


def optimo_exacto(data, ub, limite_estados=3_000_000):
    """Devuelve (Cmax optimo, estados explorados). Busca algo estrictamente menor que ub."""
    m = reto1.WillyWonka(data)
    n = m.n
    tipos = sorted(set(m.tipo))
    k = len(tipos)
    ti = [tipos.index(t) for t in m.tipo]
    ini = k                                   # tipo virtual "sin anterior"
    prohibido = [[tipos[a] == "N" and tipos[b] == "R" for b in range(k)] for a in range(k)] + [[False] * k]
    ST = []
    for maq in reto1.MAQUINAS_R1:
        ST.append([[m.st[maq, tipos[a], tipos[b]] for b in range(k)] for a in range(k)] + [[0] * k])
    P1, P2, P3 = m.P1, m.P2, m.P3
    INF = float("inf")

    # W[maq][inicio][conjunto de tipos] = recorrido minimo que cubre el conjunto
    def recorridos(s):
        W = [[INF] * (1 << k) for _ in range(k + 1)]
        for a in range(k + 1):
            dist = {}
            base = 0 if a == ini else (1 << a)
            dist[(base, a)] = 0
            cambio = True
            while cambio:
                cambio = False
                for (mask, u), du in list(dist.items()):
                    for b in range(k):
                        if b == u or prohibido[u][b]:
                            continue
                        clave = (mask | (1 << b), b)
                        nd = du + s[u][b]
                        if nd < dist.get(clave, INF):
                            dist[clave] = nd
                            cambio = True
            for (mask, u), du in dist.items():
                for sub in range(1 << k):
                    if sub & ~mask == 0 and du < W[a][sub]:
                        W[a][sub] = du
        return W

    W1, W2, W3 = (recorridos(s) for s in ST)

    cache = {}

    def datos_resto(mask):
        r = cache.get(mask)
        if r is None:
            resto = [j for j in range(n) if not mask >> j & 1]
            tmask = 0
            for j in resto:
                tmask |= 1 << ti[j]
            r = (resto, tmask, sum(P1[j] for j in resto), sum(P2[j] for j in resto),
                 sum(P3[j] for j in resto), min(P2[j] + P3[j] for j in resto),
                 min(P1[j] for j in resto), min(P3[j] for j in resto),
                 min(P1[j] + P2[j] for j in resto), min(P2[j] for j in resto))
            cache[mask] = r
        return r

    capa = {(0, ini): [(0, 0, 0)]}
    explorados = 0
    for _ in range(n):
        nueva = {}
        for (mask, lt), frente in capa.items():
            resto = datos_resto(mask)[0]
            for j in resto:
                tj = ti[j]
                if lt != ini and prohibido[lt][tj]:
                    continue
                nmask = mask | (1 << j)
                s1, s2, s3 = ST[0][lt][tj], ST[1][lt][tj], ST[2][lt][tj]
                ultimo = nmask == (1 << n) - 1
                if not ultimo:
                    _, tm, sp1, sp2, sp3, m23, mp1, mp3, m12, mp2 = datos_resto(nmask)
                for c1, c2, c3 in frente:
                    n1 = c1 + s1 + P1[j]
                    n2 = (c2 if c2 > n1 else n1) + s2 + P2[j]
                    n3 = (c3 if c3 > n2 else n2) + s3 + P3[j]
                    if ultimo:
                        cota = n3
                    else:
                        cota = max(n1 + sp1 + W1[tj][tm] + m23,
                                   max(n2, n1 + mp1) + sp2 + W2[tj][tm] + mp3,
                                   max(n3, n2 + mp2, n1 + m12) + sp3 + W3[tj][tm])
                    if cota >= ub:
                        continue
                    explorados += 1
                    clave = (nmask, tj)
                    lst = nueva.get(clave)
                    if lst is None:
                        nueva[clave] = [(n1, n2, n3)]
                        continue
                    dominado = False
                    for e in lst:
                        if e[0] <= n1 and e[1] <= n2 and e[2] <= n3:
                            dominado = True
                            break
                    if not dominado:
                        lst[:] = [e for e in lst if not (n1 <= e[0] and n2 <= e[1] and n3 <= e[2])]
                        lst.append((n1, n2, n3))
            if explorados > limite_estados:
                return None, explorados
        capa = nueva
        if not capa:
            return ub, explorados            # nada mejora la UB: es optima
    mejor = min(f[2] for frente in capa.values() for f in frente)
    return mejor, explorados


if __name__ == "__main__":
    import random
    import time
    from probar_reto1 import generar_instancia_plantilla

    random.seed(42)
    instancias = [generar_instancia_plantilla() for _ in range(30)]
    tot = 0
    for i, data in enumerate(instancias, 1):
        res = reto1.solve(data)
        t0 = time.perf_counter()
        opt, est = optimo_exacto(data, res["Cmax"])
        dt = time.perf_counter() - t0
        marca = "" if opt == res["Cmax"] else f"  <-- optimo {opt}, heuristica {res['Cmax']}"
        tot += opt == res["Cmax"]
        print(f"inst {i:>2}: heuristica {res['Cmax']:>4}  exacto {opt}  estados {est:>8}  {dt*1000:8.1f} ms{marca}")
    print(f"\nheuristica optima en {tot}/30 instancias")
```


---

<!-- fuente: corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/generador.py -->
# Código: `corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/generador.py`

> Archivo completo: https://github.com/samuelgradientai-sys/planeacion-control-produccion/blob/main/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/generador.py

```python
"""
Version LOCAL del modulo `generador` que importa la plantilla del Reto 2
(`from generador import GeneradorInstancias`). El real esta en Gradescope y no
lo tenemos: este lo imita segun el enunciado para poder probar. NO SE SUBE.

Instancia (mismas claves que usa la plantilla):
    {"jobs": ["J1", ...], "m": 3, "p": {j: pj}, "r": {j: rj}, "d": {j: dj},
     "w": {j: wj}, "preds": {j: [predecesores]}}
  * p_j entre 10 y 100, r_j entre 0 y 30, w_j entre 1 y 5
  * ~10 % de los trabajos con precedencia (unas 5 parejas i -> j con i < j: sin ciclos)
  * d_j = tiempo minimo teorico de finalizacion = max(r_j, d de sus predecesores) + p_j
    (con holgura > 0 se le suma un margen aleatorio, para probar fechas mas sueltas)
"""
import random
import time

import numpy as np


def generar(rng, n=50, m=3, n_prec=5, holgura=0.0):
    jobs = [f"J{i}" for i in range(1, n + 1)]
    p = {j: rng.randint(10, 100) for j in jobs}
    r = {j: rng.randint(0, 30) for j in jobs}
    w = {j: rng.randint(1, 5) for j in jobs}
    preds = {j: [] for j in jobs}
    parejas = set()
    while len(parejas) < n_prec:
        a, b = sorted(rng.sample(range(n), 2))
        parejas.add((a, b))
    for a, b in sorted(parejas):
        preds[jobs[b]].append(jobs[a])
    # tiempo minimo teorico de finalizacion (CPM hacia adelante; i < j, sin ciclos)
    emin = {}
    for j in jobs:
        emin[j] = max([r[j]] + [emin[i] for i in preds[j]]) + p[j]
    carga = sum(p.values()) / m
    d = {j: emin[j] + (int(rng.uniform(0, holgura) * carga) if holgura > 0 else 0) for j in jobs}
    return {"jobs": jobs, "m": m, "p": p, "r": r, "d": d, "w": w, "preds": preds}


class GeneradorInstancias:
    def __init__(self, n_instancias: int = 30, semilla: int = 42, timelimit: int = 30, holgura=0.0):
        self.n_instancias = n_instancias
        self.semilla = semilla
        self.timelimit = timelimit
        self.holgura = holgura
        random.seed(semilla)
        np.random.seed(semilla)
        self._rng = random.Random(semilla)
        self.resultados = {"instancia": [], "valor_objetivo": [], "tiempo_seg": []}

    def generar_instancia(self, indice):
        return generar(self._rng, holgura=self.holgura)

    def resolver_instancia(self, instancia):
        raise NotImplementedError

    def ejecutar_experimentos(self):
        import pandas as pd
        print(f"Ejecutando {self.n_instancias} instancias...\n")
        inicio = time.time()
        for i in range(1, self.n_instancias + 1):
            inst = self.generar_instancia(i)
            t0 = time.time()
            res = self.resolver_instancia(inst)
            t1 = time.time()
            self.resultados["instancia"].append(i)
            self.resultados["valor_objetivo"].append(res["valor_objetivo"])
            self.resultados["tiempo_seg"].append(round(t1 - t0, 4))
            print(f"Instancia {i}: sum wjTj = {res['valor_objetivo']}  ({round(t1 - t0, 4)} s)")
        df = pd.DataFrame(self.resultados)
        print("\nTiempo promedio:", round(df["tiempo_seg"].mean(), 4), "s",
              "| total:", round(time.time() - inicio, 2), "s")
        return df
```


---

<!-- fuente: corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/probar_reto1.py -->
# Código: `corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/probar_reto1.py`

> Archivo completo: https://github.com/samuelgradientai-sys/planeacion-control-produccion/blob/main/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/probar_reto1.py

```python
"""
Banco de pruebas local del RETO 01 (Willy Wonka). No se sube a Gradescope.

Uso (desde la carpeta PROYECTO ALGORITMO):
    python pruebas/probar_reto1.py               -> 30 instancias de la plantilla (semilla 42)
    python pruebas/probar_reto1.py --exacto      -> ademas calcula el optimo exacto de cada instancia
    python pruebas/probar_reto1.py --n 100 --semilla 7

Que revisa:
  * que la secuencia sea una permutacion de los 15 lotes y no tenga N -> R;
  * recalcula el Cmax con un evaluador independiente (sencillo y legible);
  * compara con la cota inferior (LB) y, opcional, con el optimo exacto;
  * muestra tambien lo que daria la funcion calcular_makespan_penalizado de la
    plantilla, que tiene un error en como busca el tipo anterior (ver README).
"""
import argparse
import os
import random
import statistics
import sys
import time

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))
sys.path.insert(0, AQUI)

import reto1  # noqa: E402
from exacto_reto1 import optimo_exacto  # noqa: E402


# --------------------------------------------------------------- generador
def generar_instancia_plantilla():
    """Copia exacta de generar_instancia() de la plantilla (sin escribir archivos).
    Usa el random GLOBAL en el mismo orden, asi con random.seed(42) salen las
    mismas instancias que genera la plantilla."""
    tipos = ["S", "N", "R"]
    lotes = [f"L{i}" for i in range(1, 16)]
    rangos = {"M1": (25, 45), "M2": (20, 40), "M3": (10, 25)}
    lotes_dict = {}
    for lote in lotes:
        tipo = random.choice(tipos)
        lotes_dict[lote] = {
            "tipo": tipo,
            "M1": random.randint(*rangos["M1"]),
            "M2": random.randint(*rangos["M2"]),
            "M3": random.randint(*rangos["M3"]),
        }
    setup_dict = {}
    for maquina in ["M1", "M2", "M3"]:
        setup_dict[maquina] = {}
        for tipo_ant in tipos:
            for tipo_sig in tipos:
                if tipo_ant == tipo_sig:
                    tiempo_setup = 0
                elif maquina == "M1":
                    tiempo_setup = random.randint(10, 40)
                elif maquina == "M2":
                    tiempo_setup = random.randint(5, 30)
                else:
                    tiempo_setup = random.randint(3, 15)
                setup_dict[maquina][f"{tipo_ant}-{tipo_sig}"] = tiempo_setup
    return {"lotes": lotes_dict, "setup": setup_dict}


# --------------------------------------------------------------- evaluadores
def cmax_independiente(data, secuencia):
    """Evaluador simple: misma regla de tiempos, escrito sin optimizaciones."""
    lotes, setup = data["lotes"], data["setup"]
    fin = {"M1": 0, "M2": 0, "M3": 0}
    anterior = None
    for lote in secuencia:
        llegada = 0
        for m in ("M1", "M2", "M3"):
            s = 0 if anterior is None else setup[m][f"{lotes[anterior]['tipo']}-{lotes[lote]['tipo']}"]
            inicio = max(fin[m], llegada) + s
            fin[m] = inicio + lotes[lote][m]
            llegada = fin[m]
        anterior = lote
    return fin["M3"]


def violaciones(data, secuencia):
    t = [data["lotes"][x]["tipo"] for x in secuencia]
    return sum(1 for a, b in zip(t, t[1:]) if a == "N" and b == "R")


def cmax_plantilla(data, secuencia):
    """Copia textual de calcular_makespan_penalizado() de la plantilla."""
    lotes = data["lotes"]
    setup = data["setup"]
    maquinas = ["M1", "M2", "M3"]
    penalizado = False
    for i in range(1, len(secuencia)):
        if lotes[secuencia[i - 1]]["tipo"] == "N" and lotes[secuencia[i]]["tipo"] == "R":
            penalizado = True
            break
    fin_maquina = {m: 0 for m in maquinas}
    fin_lote = {l: 0 for l in secuencia}
    for lote in secuencia:
        tipo_actual = lotes[lote]["tipo"]
        for m_idx, m in enumerate(maquinas):
            prev_tipo = None
            if fin_maquina[m] > 0:
                for l in secuencia:
                    if fin_lote[l] <= fin_maquina[m] and l != lote:
                        prev_tipo = lotes[l]["tipo"]
            t_setup = 0
            if prev_tipo is not None and prev_tipo != tipo_actual:
                t_setup = setup[m][f"{prev_tipo}-{tipo_actual}"]
            if m_idx == 0:
                inicio = fin_maquina[m] + t_setup
            else:
                inicio = max(fin_maquina[m], fin_lote[lote]) + t_setup
            fin = inicio + lotes[lote][m]
            fin_maquina[m] = fin
            fin_lote[lote] = fin
    makespan = max(fin_maquina.values())
    return float("inf") if penalizado else makespan


# --------------------------------------------------------------- chequeos
def chequear_insercion(n_pruebas=300):
    """Compara la insercion acelerada (Taillard) contra evaluar todas las posiciones."""
    rng = random.Random(1)
    estado = random.getstate()
    random.seed(99)
    for _ in range(n_pruebas):
        modelo = reto1.WillyWonka(generar_instancia_plantilla())
        seq = list(range(modelo.n))
        rng.shuffle(seq)
        j = seq.pop(rng.randrange(len(seq)))
        val, pos = modelo.mejor_insercion(seq, j)
        bruto = min(modelo.evaluar(seq[:i] + [j] + seq[i:]) for i in range(len(seq) + 1))
        assert val == bruto, (val, bruto)
    random.setstate(estado)
    print(f"[ok] insercion acelerada = fuerza bruta en {n_pruebas} casos")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=30, help="numero de instancias")
    ap.add_argument("--semilla", type=int, default=42, help="semilla del generador (plantilla = 42)")
    ap.add_argument("--exacto", action="store_true",
                    help="calcula el optimo con programacion dinamica (pruebas/exacto_reto1.py)")
    args = ap.parse_args()

    chequear_insercion()
    random.seed(args.semilla)
    instancias = [generar_instancia_plantilla() for _ in range(args.n)]

    filas = []
    print(f"\n{'inst':>4} {'LB':>5} {'inicial':>7} {'Cmax':>5} {'optimo':>6} {'gapLB%':>6} "
          f"{'iter':>4} {'ms':>6} {'plantilla':>9}  estado")
    for k, data in enumerate(instancias, 1):
        t0 = time.perf_counter()
        res = reto1.solve(data)
        ms = (time.perf_counter() - t0) * 1000

        seq = res["secuencia"]
        assert sorted(seq) == sorted(data["lotes"]), "la secuencia no es una permutacion"
        v = violaciones(data, seq)
        c_ind = cmax_independiente(data, seq)
        assert c_ind == res["Cmax"], f"Cmax reportado {res['Cmax']} != recalculado {c_ind}"

        _, _, info = reto1.WillyWonka(data).resolver()
        opt = None
        if args.exacto:
            opt = optimo_exacto(data, res["Cmax"])[0]
        gap = 100 * (res["Cmax"] - info["lb"]) / info["lb"]
        estado = "optimo demostrado" if info["optimo_probado"] else ""
        if opt is not None and not info["optimo_probado"]:
            estado = "optimo" if opt == res["Cmax"] else f"a {res['Cmax'] - opt} del optimo"
        if v:
            estado = f"INFACTIBLE ({v} N->R)"
        filas.append({"lb": info["lb"], "cmax": res["Cmax"], "ms": ms, "ini": info["inicial"],
                      "opt": opt, "lbopt": info["optimo_probado"], "gap": gap})
        print(f"{k:>4} {info['lb']:>5} {info['inicial']:>7} {res['Cmax']:>5} "
              f"{opt if opt is not None else '-':>6} {gap:>6.2f} {info['iteraciones']:>4} "
              f"{ms:>6.1f} {cmax_plantilla(data, seq):>9}  {estado}")

    print("\n==== RESUMEN RETO 1 ====")
    print(f"instancias:                  {len(filas)}")
    print(f"optimo demostrado:           {sum(f['lbopt'] for f in filas)}/{len(filas)}")
    if args.exacto:
        nopt = sum(f["cmax"] == f["opt"] for f in filas)
        brecha = statistics.mean(100 * (f["cmax"] - f["opt"]) / f["opt"] for f in filas)
        print(f"optimas (metodo exacto):     {nopt}/{len(filas)}   brecha promedio {brecha:.4f}%")
    print(f"Cmax promedio:               {statistics.mean(f['cmax'] for f in filas):.2f}")
    print(f"brecha promedio vs LB:       {statistics.mean(f['gap'] for f in filas):.3f}%")
    print(f"mejora vs mejor inicial:     "
          f"{statistics.mean(100 * (f['ini'] - f['cmax']) / f['ini'] for f in filas):.3f}%")
    print(f"tiempo promedio:             {statistics.mean(f['ms'] for f in filas):.2f} ms"
          f"  (max {max(f['ms'] for f in filas):.1f} ms)")


if __name__ == "__main__":
    main()
```


---

<!-- fuente: corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/probar_reto2.py -->
# Código: `corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/probar_reto2.py`

> Archivo completo: https://github.com/samuelgradientai-sys/planeacion-control-produccion/blob/main/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/pruebas/probar_reto2.py

```python
"""
Banco de pruebas local del RETO 02 (Monstruopolis). No se sube a Gradescope.

Uso (desde la carpeta PROYECTO ALGORITMO):
    python pruebas/probar_reto2.py                 -> 30 instancias (semilla 42)
    python pruebas/probar_reto2.py --referencia    -> ademas una corrida larga para medir la brecha
    python pruebas/probar_reto2.py --holgura 0.5   -> fechas de entrega mas sueltas

Que revisa (con un validador independiente del algoritmo):
  * una entrada por trabajo, maquina valida, end = start + p_j;
  * start >= r_j, predecesores terminados antes de empezar, sin solapes por maquina;
  * recalcula sum w_j T_j.
"""
import argparse
import os
import random
import statistics
import sys
import time

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))
sys.path.insert(0, AQUI)

import reto2  # noqa: E402
from generador import generar  # noqa: E402


def validar(inst, salida):
    """Devuelve (sum wjTj, lista de violaciones)."""
    errores = []
    jobs = inst["jobs"]
    maquinas = {f"M{k + 1}" for k in range(inst["m"])}
    por_job = {}
    for f in salida:
        if f["job"] in por_job:
            errores.append(f"{f['job']} repetido")
        por_job[f["job"]] = f
    for j in jobs:
        if j not in por_job:
            errores.append(f"{j} falta")
            continue
        f = por_job[j]
        if f["machine"] not in maquinas:
            errores.append(f"{j} maquina {f['machine']}")
        if f["end"] - f["start"] != inst["p"][j]:
            errores.append(f"{j} duracion")
        if f["start"] < inst["r"][j]:
            errores.append(f"{j} empieza antes de r_j")
        for i in inst["preds"][j]:
            if por_job[i]["end"] > f["start"]:
                errores.append(f"{i}->{j} precedencia")
    for mq in maquinas:
        tareas = sorted((f["start"], f["end"], f["job"]) for f in salida if f["machine"] == mq)
        for (s1, e1, j1), (s2, e2, j2) in zip(tareas, tareas[1:]):
            if s2 < e1:
                errores.append(f"solape {j1}/{j2} en {mq}")
    total = sum(inst["w"][j] * max(0, por_job[j]["end"] - inst["d"][j]) for j in jobs if j in por_job)
    return total, errores


def cota_inferior(inst):
    """sum wT >= sum wC - sum wd, con sum wC acotado por Eastman-Even-Isaacs
    (sin liberaciones ni precedencias) y por sum w_j (r_j + p_j)."""
    jobs, m = inst["jobs"], inst["m"]
    p, w, d, r = inst["p"], inst["w"], inst["d"], inst["r"]
    orden = sorted(jobs, key=lambda j: -w[j] / p[j])
    acum, eei = 0, 0
    for j in orden:
        acum += p[j]
        eei += w[j] * acum / m
    eei += (m - 1) / (2 * m) * sum(w[j] * p[j] for j in jobs)
    lb_wc = max(eei, sum(w[j] * (r[j] + p[j]) for j in jobs))
    return max(0.0, lb_wc - sum(w[j] * d[j] for j in jobs))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=30)
    ap.add_argument("--semilla", type=int, default=42)
    ap.add_argument("--holgura", type=float, default=0.0)
    ap.add_argument("--referencia", action="store_true")
    args = ap.parse_args()

    rng = random.Random(args.semilla)
    instancias = [generar(rng, holgura=args.holgura) for _ in range(args.n)]

    filas = []
    print(f"{'inst':>4} {'LB':>7} {'regla':>7} {'final':>7} {'ref':>7} "
          f"{'gap%':>6} {'ms':>7}  estado")
    for k, inst in enumerate(instancias, 1):
        t0 = time.perf_counter()
        salida = reto2.solve(inst)
        ms = (time.perf_counter() - t0) * 1000
        total, errores = validar(inst, salida)

        modelo = reto2.Monstruopolis(*reto2.cargar_instancia(inst))
        _, costo, info = modelo.resolver()
        assert costo == total, (costo, total)
        ref = None
        if args.referencia:
            ref = min([total] + [modelo.resolver(tiempo_max=60, semilla=s, iteraciones=400000)[1]
                                 for s in (11, 22)])
        lb = cota_inferior(inst)
        gap = 100 * (total - ref) / ref if ref else 0.0
        estado = "OK" if not errores else "ERRORES: " + "; ".join(errores[:3])
        filas.append({"tot": total, "ref": ref, "ms": ms, "ini": info["inicial"], "gap": gap})
        print(f"{k:>4} {lb:>7.0f} {info['inicial']:>7} {total:>7} "
              f"{ref if ref is not None else '-':>7} {gap:>6.2f} {ms:>7.1f}  {estado}")

    print("\n==== RESUMEN RETO 2 ====")
    print(f"instancias:              {len(filas)}")
    print(f"sum wjTj promedio:       {statistics.mean(f['tot'] for f in filas):.1f}")
    print(f"mejora vs mejor regla:   "
          f"{statistics.mean(100 * (f['ini'] - f['tot']) / f['ini'] for f in filas if f['ini']):.2f}%")
    if args.referencia:
        print(f"brecha vs corrida larga: {statistics.mean(f['gap'] for f in filas):.3f}%  "
              f"(iguales: {sum(f['tot'] == f['ref'] for f in filas)})")
    print(f"tiempo promedio:         {statistics.mean(f['ms'] for f in filas):.1f} ms"
          f"  (max {max(f['ms'] for f in filas):.1f} ms)")


if __name__ == "__main__":
    main()
```


---

<!-- fuente: corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/reto1.py -->
# Código: `corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/reto1.py`

> Archivo completo: https://github.com/samuelgradientai-sys/planeacion-control-produccion/blob/main/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/reto1.py

```python
"""
RETO 01 - Fabrica de Willy Wonka
================================
Flow shop de permutacion con 3 maquinas en serie (M1 -> M2 -> M3), tiempos de
alistamiento que dependen del tipo del lote anterior y del siguiente (distintos
en cada maquina) y una restriccion de factibilidad: un lote R (relleno) no puede
ir inmediatamente despues de un lote N (nueces).
Objetivo: minimizar Cmax.

Algoritmo (entrega el OPTIMO y lo demuestra)
--------------------------------------------
1. Cota inferior (LB): para cada orden posible de los tipos de lote se acota el
   Cmax en las tres maquinas con ese mismo orden; la LB es el minimo entre
   ordenes. Si una solucion la alcanza, es optima y se para.
2. Heuristica rapida para tener una buena solucion (cota superior):
   - NEH adaptado: inserta cada lote en la mejor posicion FACTIBLE, y
   - secuencias por bloques de tipo: cada orden de tipos permitido, con los
     lotes de cada bloque ordenados por la regla de Johnson;
   - busqueda local por insercion sobre la mejor, con la aceleracion de
     Taillard (cabezas y colas: todas las posiciones en O(n*m)).
3. Metodo exacto (programacion dinamica acotada, tipo ramificacion y
   acotamiento): arma las secuencias lote a lote, guarda por estado solo los
   tiempos no dominados y descarta lo que, segun la cota, no puede mejorar la
   heuristica. Si no sobrevive nada, la heuristica era optima; si sobrevive
   algo, sale la secuencia optima.
4. Respaldo: Iterated Greedy (Ruiz y Stutzle), solo si el exacto se apaga o
   llega a su tope de seguridad.

Modelo de tiempos (el mismo de la funcion de evaluacion de la plantilla):
    inicio(lote, Mk) = max(fin de Mk, fin del lote en Mk-1) + alistamiento
    El primer lote no tiene alistamiento y M1 arranca en 0.
"""
import itertools
import json
import math
import random
import sys
import time

# === INICIO ALGORITMO ===
# ---------------------------------------------------------------- parametros
# Con 200 instancias del generador de la plantilla: optimo demostrado en 200/200,
# ~3,5 ms en promedio (mediana ~0,4 ms, peor caso ~60 ms).
TIEMPO_MAX_R1 = 2.0      # tope de seguridad (segundos) por instancia
MAX_ITER_R1 = 1500       # iteraciones maximas del Iterated Greedy
MAX_SIN_MEJORA_R1 = 5    # (respaldo) para si el mejor no cambia en estas iteraciones
D_DESTRUCCION_R1 = 4     # lotes que se retiran en cada destruccion
EXACTO_R1 = True         # demostrar/encontrar el optimo con el metodo exacto
MAX_ESTADOS_R1 = 400000  # tope de seguridad del exacto (si se pasa, queda la heuristica)
T_ACEPTACION_R1 = 0.4    # constante de temperatura de Ruiz y Stutzle
SEMILLA_R1 = 2026        # semilla propia: no altera el random global
PENAL_R1 = 10 ** 6       # penalidad interna por cada pareja N -> R

MAQUINAS_R1 = ("M1", "M2", "M3")


class WillyWonka:
    """Datos de una instancia y los procedimientos del algoritmo."""

    def __init__(self, data):
        lotes = data["lotes"]
        setup = data["setup"]
        self.nombres = list(lotes)
        n = self.n = len(self.nombres)
        self.tipo = [str(lotes[x]["tipo"]).strip().upper() for x in self.nombres]
        self.P1 = [lotes[x]["M1"] for x in self.nombres]
        self.P2 = [lotes[x]["M2"] for x in self.nombres]
        self.P3 = [lotes[x]["M3"] for x in self.nombres]

        # alistamiento por maquina y pareja de tipos (anterior, siguiente)
        tipos = sorted(set(self.tipo))
        self.st = {}
        for m in MAQUINAS_R1:
            tabla = setup.get(m, {})
            for a in tipos:
                for b in tipos:
                    v = tabla.get(f"{a}-{b}")
                    if v is None and isinstance(tabla.get(a), dict):
                        v = tabla[a].get(b)
                    self.st[m, a, b] = v if v is not None else 0

        # matrices lote x lote; la fila n es el "inicio" (sin lote anterior)
        t = self.tipo
        self.S1, self.S2, self.S3 = (
            [[self.st[m, t[i], t[j]] for j in range(n)] for i in range(n)] + [[0] * n]
            for m in MAQUINAS_R1
        )
        self.PROH = [[1 if (t[i] == "N" and t[j] == "R") else 0 for j in range(n)]
                     for i in range(n)] + [[0] * n]
        self._preparar_tipos()

    # ------------------------------------------------------------ evaluacion
    def evaluar(self, seq):
        """Cmax de la secuencia + PENAL por cada pareja N -> R."""
        P1, P2, P3 = self.P1, self.P2, self.P3
        S1, S2, S3, PROH = self.S1, self.S2, self.S3, self.PROH
        c1 = c2 = c3 = 0
        viol = 0
        a = self.n
        for x in seq:
            c1 += S1[a][x] + P1[x]
            if c1 > c2:
                c2 = c1
            c2 += S2[a][x] + P2[x]
            if c2 > c3:
                c3 = c2
            c3 += S3[a][x] + P3[x]
            viol += PROH[a][x]
            a = x
        return c3 + PENAL_R1 * viol

    def mejor_insercion(self, pi, j):
        """Mejor posicion para insertar el lote j en la secuencia parcial pi.

        Aceleracion de Taillard adaptada a alistamientos:
          e[k]  = fin del lote pi[k-1] en cada maquina (cabezas)
          q[k]  = camino mas largo desde el lote pi[k] hasta el final (colas)
        Al insertar j entre a = pi[i-1] y b = pi[i] se recalculan solo j y b
        (b cambia de alistamiento porque ahora su anterior es j):
          Cmax = max_m ( fin de b en m + q[i+1][m] )
        Devuelve (valor penalizado, posicion).
        """
        P1, P2, P3 = self.P1, self.P2, self.P3
        S1, S2, S3, PROH = self.S1, self.S2, self.S3, self.PROH
        ini = self.n
        L = len(pi)

        # cabezas
        e1 = [0] * (L + 1)
        e2 = [0] * (L + 1)
        e3 = [0] * (L + 1)
        c1 = c2 = c3 = 0
        viol = 0
        a = ini
        for k in range(L):
            x = pi[k]
            c1 += S1[a][x] + P1[x]
            if c1 > c2:
                c2 = c1
            c2 += S2[a][x] + P2[x]
            if c2 > c3:
                c3 = c2
            c3 += S3[a][x] + P3[x]
            e1[k + 1] = c1
            e2[k + 1] = c2
            e3[k + 1] = c3
            viol += PROH[a][x]
            a = x

        # colas
        q1 = [0] * (L + 1)
        q2 = [0] * (L + 1)
        q3 = [0] * (L + 1)
        t1 = t2 = t3 = 0
        for k in range(L - 1, -1, -1):
            x = pi[k]
            a = pi[k - 1] if k else ini
            t3 = t3 + S3[a][x] + P3[x]
            t2 = (t2 if t2 > t3 else t3) + S2[a][x] + P2[x]
            t1 = (t1 if t1 > t2 else t2) + S1[a][x] + P1[x]
            q1[k] = t1
            q2[k] = t2
            q3[k] = t3

        # todas las posiciones de insercion
        p1j, p2j, p3j = P1[j], P2[j], P3[j]
        mejor = float("inf")
        mejor_pos = 0
        for i in range(L + 1):
            a = pi[i - 1] if i else ini
            f1 = e1[i] + S1[a][j] + p1j
            f2 = (e2[i] if e2[i] > f1 else f1) + S2[a][j] + p2j
            f3 = (e3[i] if e3[i] > f2 else f2) + S3[a][j] + p3j
            v = viol + PROH[a][j]
            if i < L:
                b = pi[i]
                v += PROH[j][b] - PROH[a][b]
                g1 = f1 + S1[j][b] + P1[b]
                g2 = (f2 if f2 > g1 else g1) + S2[j][b] + P2[b]
                g3 = (f3 if f3 > g2 else g2) + S3[j][b] + P3[b]
                c = g1 + q1[i + 1]
                t = g2 + q2[i + 1]
                if t > c:
                    c = t
                t = g3 + q3[i + 1]
                if t > c:
                    c = t
            else:
                c = f3
            val = c + PENAL_R1 * v
            if val < mejor:
                mejor = val
                mejor_pos = i
        return mejor, mejor_pos

    # ------------------------------------------------- cotas y metodo exacto
    def _preparar_tipos(self):
        """Tablas por TIPO de lote (no por lote), que usan la cota y el exacto."""
        tipos = sorted(set(self.tipo))
        k = self.k = len(tipos)
        self.ti = [tipos.index(t) for t in self.tipo]
        # fila k = inicio (sin lote anterior): alistamiento 0 y nada prohibido
        self.PT = [[tipos[a] == "N" and tipos[b] == "R" for b in range(k)] for a in range(k)] + [[False] * k]
        self.STT = [[[self.st[m, tipos[a], tipos[b]] if a < k else 0 for b in range(k)]
                     for a in range(k + 1)] for m in MAQUINAS_R1]
        self.lotes_tipo = [[j for j in range(self.n) if self.ti[j] == t] for t in range(k)]
        self._caminos = {}
        self._resto = {}

    def caminos(self, lt, S):
        """Ordenes de tipos posibles para lo que falta: recorridos que salen del
        tipo lt, pasan por todos los tipos del conjunto S (mascara de bits) y
        nunca van de N a R. Devuelve la lista de (alist. M1, alist. M2, alist. M3,
        primer tipo, ultimo tipo) no dominados. Se calcula una vez y se guarda."""
        clave0 = (lt, S)
        res = self._caminos.get(clave0)
        if res is not None:
            return res
        k, PT = self.k, self.PT
        A, B, C = self.STT
        est = {}
        cola = []

        def agregar(clave, v):
            lst = est.setdefault(clave, [])
            for u in lst:
                if u[0] <= v[0] and u[1] <= v[1] and u[2] <= v[2]:
                    return
            lst[:] = [u for u in lst if not (v[0] <= u[0] and v[1] <= u[1] and v[2] <= u[2])]
            lst.append(v)
            cola.append((clave, v))

        for t1 in range(k):
            if S >> t1 & 1 and not PT[lt][t1]:
                agregar((1 << t1, t1, t1), (A[lt][t1], B[lt][t1], C[lt][t1]))
        while cola:
            (cub, act, t1), v = cola.pop()
            if v not in est[(cub, act, t1)]:
                continue
            for b in range(k):
                if b != act and S >> b & 1 and not PT[act][b]:
                    agregar((cub | 1 << b, b, t1), (v[0] + A[act][b], v[1] + B[act][b], v[2] + C[act][b]))
        res = [(v[0], v[1], v[2], t1, act) for (cub, act, t1), lst in est.items() if cub == S for v in lst]
        self._caminos[clave0] = res
        return res

    def datos_resto(self, mask):
        """Datos de los lotes que faltan (los que no estan en mask): sumas de
        tiempos, tipos presentes y minimos por tipo. Se guardan por mascara."""
        d = self._resto.get(mask)
        if d is None:
            k, ti = self.k, self.ti
            P1, P2, P3 = self.P1, self.P2, self.P3
            INF = float("inf")
            sp1 = sp2 = sp3 = S = 0
            mp1 = [INF] * k
            mp2 = [INF] * k
            mp12 = [INF] * k
            mp3 = [INF] * k
            m23 = [INF] * k
            resto = []
            for j in range(self.n):
                if mask >> j & 1:
                    continue
                resto.append(j)
                t = ti[j]
                S |= 1 << t
                a, b, c = P1[j], P2[j], P3[j]
                sp1 += a
                sp2 += b
                sp3 += c
                if a < mp1[t]:
                    mp1[t] = a
                if b < mp2[t]:
                    mp2[t] = b
                if a + b < mp12[t]:
                    mp12[t] = a + b
                if c < mp3[t]:
                    mp3[t] = c
                if b + c < m23[t]:
                    m23[t] = b + c
            d = (resto, sp1, sp2, sp3, S, mp1, mp2, mp12, mp3, m23)
            self._resto[mask] = d
        return d

    def resto_sin(self, d, j, nmask):
        """datos_resto(nmask) a partir de los datos d del estado padre, donde
        nmask = padre + lote j: se resta j y solo se recalculan los minimos de
        su tipo (mucho mas barato que recorrer todos los lotes)."""
        r = self._resto.get(nmask)
        if r is not None:
            return r
        resto, sp1, sp2, sp3, S, mp1, mp2, mp12, mp3, m23 = d
        P1, P2, P3 = self.P1, self.P2, self.P3
        t = self.ti[j]
        mp1, mp2, mp12, mp3, m23 = mp1[:], mp2[:], mp12[:], mp3[:], m23[:]
        INF = float("inf")
        a1 = a2 = a12 = a3 = a23 = INF
        for x in self.lotes_tipo[t]:
            if nmask >> x & 1:
                continue
            a, b, c = P1[x], P2[x], P3[x]
            if a < a1:
                a1 = a
            if b < a2:
                a2 = b
            if a + b < a12:
                a12 = a + b
            if c < a3:
                a3 = c
            if b + c < a23:
                a23 = b + c
        mp1[t], mp2[t], mp12[t], mp3[t], m23[t] = a1, a2, a12, a3, a23
        if a1 == INF:                       # ya no quedan lotes de ese tipo
            S &= ~(1 << t)
        r = ([x for x in resto if x != j], sp1 - P1[j], sp2 - P2[j], sp3 - P3[j], S,
             mp1, mp2, mp12, mp3, m23)
        self._resto[nmask] = r
        return r

    def cota(self, c1, c2, c3, lt, d, tope=float("inf")):
        """Cota inferior del Cmax desde un estado parcial: maquinas libres en
        (c1, c2, c3), ultimo tipo lt y lotes restantes descritos por d.

        Para cada orden de tipos posible (ver caminos) con primer tipo t1 y
        ultimo tipo tk, y alistamientos w1, w2, w3 en cada maquina:
          B1 = c1 + sum p1 + w1 + min (p2+p3) de los lotes de tipo tk
          B2 = max(c2, c1 + s1 + min p1 de tipo t1) + sum p2 + w2 + min p3 de tipo tk
          B3 = max(c3, llegada a M3 del primer lote) + sum p3 + w3
        La cota es el minimo, entre los ordenes, de max(B1, B2, B3): las tres
        maquinas tienen que usar el MISMO orden de tipos."""
        _, sp1, sp2, sp3, S, mp1, mp2, mp12, mp3, m23 = d
        A, B, _ = self.STT
        mejor = tope
        a1 = c1 + sp1
        for w1, w2, w3, t1, tk in self.caminos(lt, S):
            b = a1 + w1 + m23[tk]
            if b >= mejor:
                continue
            s1f = A[lt][t1]
            x = c1 + s1f + mp1[t1]
            b2 = (c2 if c2 > x else x) + sp2 + w2 + mp3[tk]
            if b2 > b:
                b = b2
                if b >= mejor:
                    continue
            s2f = B[lt][t1]
            y = c2 + s2f + mp2[t1]
            z = c1 + s1f + s2f + mp12[t1]
            if z > y:
                y = z
            if c3 > y:
                y = c3
            b3 = y + sp3 + w3
            if b3 > b:
                b = b3
            if b < mejor:
                mejor = b
        return mejor

    def cota_inferior(self):
        """Cota inferior del Cmax de toda la instancia."""
        return self.cota(0, 0, 0, self.k, self.datos_resto(0))

    def exacto(self, ub, limite):
        """Programacion dinamica acotada (tipo ramificacion y acotamiento).

        Construye las secuencias lote a lote, por capas. Estado: (lotes ya
        programados, tipo del ultimo). De cada estado se guardan solo los
        vectores (fin M1, fin M2, fin M3) no dominados, y se descarta todo
        estado cuya cota ya no puede mejorar ub (la mejor solucion conocida).
        Devuelve (secuencia o None, valor, completo): si completo es True y la
        secuencia es None, ub era optimo; si hay secuencia, es la optima."""
        n, k = self.n, self.k
        P1, P2, P3, ti, PT = self.P1, self.P2, self.P3, self.ti, self.PT
        A, B, C = self.STT
        cota, resto_sin = self.cota, self.resto_sin
        lleno = (1 << n) - 1
        capa = {(0, k): [(0, 0, 0, None)]}
        estados = 0
        for _ in range(n):
            nueva = {}
            for (mask, lt), frente in capa.items():
                d = self.datos_resto(mask)
                for j in d[0]:
                    tj = ti[j]
                    if PT[lt][tj]:
                        continue
                    nmask = mask | (1 << j)
                    s1, s2, s3 = A[lt][tj], B[lt][tj], C[lt][tj]
                    p1, p2, p3 = P1[j], P2[j], P3[j]
                    ultimo = nmask == lleno
                    if not ultimo:
                        dn = resto_sin(d, j, nmask)
                    clave = (nmask, tj)
                    for ent in frente:
                        n1 = ent[0] + s1 + p1
                        n2 = (ent[1] if ent[1] > n1 else n1) + s2 + p2
                        n3 = (ent[2] if ent[2] > n2 else n2) + s3 + p3
                        if ultimo:
                            if n3 >= ub:
                                continue
                        elif cota(n1, n2, n3, tj, dn, ub) >= ub:
                            continue
                        lst = nueva.get(clave)
                        if lst is None:
                            nueva[clave] = [(n1, n2, n3, (j, ent))]
                            estados += 1
                            continue
                        dominado = False
                        for e in lst:
                            if e[0] <= n1 and e[1] <= n2 and e[2] <= n3:
                                dominado = True
                                break
                        if dominado:
                            continue
                        lst[:] = [e for e in lst if not (n1 <= e[0] and n2 <= e[1] and n3 <= e[2])]
                        lst.append((n1, n2, n3, (j, ent)))
                        estados += 1
                if estados > MAX_ESTADOS_R1 or time.perf_counter() > limite:
                    return None, ub, False
            capa = nueva
            if not capa:
                return None, ub, True
        fin = min((e for lst in capa.values() for e in lst), key=lambda e: e[2])
        seq = []
        e = fin
        while e[3] is not None:
            j, e = e[3]
            seq.append(j)
        return seq[::-1], fin[2], True

    # -------------------------------------------------------- constructivos
    def neh(self):
        """NEH: lotes por tiempo total decreciente, cada uno a su mejor posicion."""
        P1, P2, P3 = self.P1, self.P2, self.P3
        orden = sorted(range(self.n), key=lambda j: -(P1[j] + P2[j] + P3[j]))
        seq = [orden[0]]
        for j in orden[1:]:
            _, i = self.mejor_insercion(seq, j)
            seq.insert(i, j)
        return seq

    def por_bloques(self):
        """Una secuencia por cada orden de bloques de tipo que no ponga N antes de R.
        Dentro del bloque: regla de Johnson con A = p1+p2 y B = p2+p3."""
        P1, P2, P3 = self.P1, self.P2, self.P3
        presentes = list(dict.fromkeys(self.tipo))
        salida = []
        for orden in itertools.permutations(presentes):
            if any(orden[k] == "N" and orden[k + 1] == "R" for k in range(len(orden) - 1)):
                continue
            seq = []
            for t in orden:
                grupo = [j for j in range(self.n) if self.tipo[j] == t]
                g1 = sorted((j for j in grupo if P1[j] + P2[j] < P2[j] + P3[j]),
                            key=lambda j: P1[j] + P2[j])
                g2 = sorted((j for j in grupo if P1[j] + P2[j] >= P2[j] + P3[j]),
                            key=lambda j: -(P2[j] + P3[j]))
                seq += g1 + g2
            salida.append(seq)
        return salida

    # --------------------------------------------------------- mejora
    def busqueda_local(self, seq, val, rng):
        """Insercion: saca cada lote y lo pone en su mejor posicion, hasta que nada mejore."""
        mejora = True
        while mejora:
            mejora = False
            orden = seq[:]
            rng.shuffle(orden)
            for j in orden:
                k = seq.index(j)
                pi = seq[:k] + seq[k + 1:]
                v, i = self.mejor_insercion(pi, j)
                if v < val:
                    pi.insert(i, j)
                    seq, val = pi, v
                    mejora = True
        return seq, val

    def resolver(self, tiempo_max=TIEMPO_MAX_R1, semilla=SEMILLA_R1,
                 max_iter=MAX_ITER_R1, max_sin_mejora=MAX_SIN_MEJORA_R1, exacto=EXACTO_R1):
        """Devuelve (secuencia de indices, Cmax, info)."""
        t0 = time.perf_counter()
        limite = t0 + tiempo_max
        n = self.n
        if n == 0:
            return [], 0, {"lb": 0, "iteraciones": 0, "optimo_probado": True}
        rng = random.Random(semilla)
        lb = self.cota_inferior()

        # 1) soluciones iniciales (NEH + bloques) y busqueda local, empezando por
        #    la mejor. Con el exacto activo basta con la mejor (el exacto hace el
        #    resto); sin el, se aplica a todas. Se para si alguna llega a la cota.
        candidatos = [self.neh()] + self.por_bloques()
        valores = [self.evaluar(s) for s in candidatos]
        orden = sorted(range(len(candidatos)), key=valores.__getitem__)
        mejor, mejor_val = candidatos[orden[0]], valores[orden[0]]
        inicial = mejor_val
        for k in (orden[:1] if exacto else orden):
            if mejor_val <= lb:
                break
            s, v = self.busqueda_local(candidatos[k], valores[k], rng)
            if v < mejor_val:
                mejor, mejor_val = s, v
        heuristica = mejor_val
        probado = mejor_val <= lb

        # 2) metodo exacto: encuentra una secuencia mejor o demuestra que no existe
        if not probado and exacto and mejor_val < PENAL_R1:
            seq, val, completo = self.exacto(mejor_val, limite)
            if seq is not None:
                mejor, mejor_val = seq, val
            probado = completo

        # 3) Iterated Greedy: solo si no se demostro el optimo (exacto apagado o
        #    se llego a su tope de seguridad)
        actual, actual_val = mejor[:], mejor_val
        temp = T_ACEPTACION_R1 * (sum(self.P1) + sum(self.P2) + sum(self.P3)) / (n * 3 * 10)
        d = min(D_DESTRUCCION_R1, n - 1)
        it = sin_mejora = 0
        while (not probado and mejor_val > lb and it < max_iter and sin_mejora < max_sin_mejora
               and time.perf_counter() < limite):
            it += 1
            pi = actual[:]
            quitados = [pi.pop(rng.randrange(len(pi))) for _ in range(d)]
            val = None
            for j in quitados:
                val, i = self.mejor_insercion(pi, j)
                pi.insert(i, j)
            pi, val = self.busqueda_local(pi, val, rng)
            if val < actual_val:
                actual, actual_val = pi, val
                if val < mejor_val:
                    mejor, mejor_val = pi[:], val
                    sin_mejora = 0
                    continue
            elif rng.random() < math.exp(-(val - actual_val) / temp):
                actual, actual_val = pi, val
            sin_mejora += 1

        cmax = mejor_val % PENAL_R1 if mejor_val >= PENAL_R1 else mejor_val
        info = {"lb": lb, "inicial": inicial, "heuristica": heuristica, "iteraciones": it,
                "factible": mejor_val < PENAL_R1, "optimo_probado": probado or mejor_val <= lb}
        return mejor, cmax, info
# === FIN ALGORITMO ===


def solve(data: dict) -> dict:
    """
    Parametro: data - diccionario cargado desde data.json
    Retorna: {"Cmax": int, "secuencia": list[str], "tiempo": int}
    """
    start = time.time()
    modelo = WillyWonka(data)
    seq, cmax, _ = modelo.resolver()
    secuencia = [modelo.nombres[j] for j in seq]
    elapsed = int((time.time() - start) * 1000)
    return {"Cmax": int(cmax), "secuencia": secuencia, "tiempo": elapsed}


if __name__ == "__main__":
    ruta = sys.argv[1] if len(sys.argv) > 1 else "data.json"
    with open(ruta, encoding="utf-8") as f:
        data = json.load(f)
    print(json.dumps(solve(data), indent=2))
```


---

<!-- fuente: corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/reto2.py -->
# Código: `corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/reto2.py`

> Archivo completo: https://github.com/samuelgradientai-sys/planeacion-control-produccion/blob/main/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/reto2.py

```python
"""
RETO 02 - Fabrica de juguetes de Monstruopolis
==============================================
P3 | r_j, prec | sum w_j T_j : 3 maquinas identicas en paralelo, fechas de
liberacion, precedencias (i -> j: j empieza cuando i termino), sin interrupciones.
Objetivo: minimizar la tardanza ponderada total.

Representacion
--------------
Una lista de prioridad: permutacion de los trabajos en la que cada predecesor
aparece antes que sus sucesores. El decodificador programa los trabajos en el
orden de la lista, cada uno lo antes posible:
    listo_j = max(r_j, fin de sus predecesores)
    maquina = la que permite empezar antes; si varias permiten empezar en
              listo_j se usa la que quedo libre mas tarde ("best fit"), asi las
              que quedaron libres antes siguen disponibles para otros trabajos.
Cualquier lista asi da un programa factible (respeta r_j, precedencias y no
hay solapes), por eso la busqueda nunca produce soluciones infactibles.

Algoritmo
---------
1. Reglas de despacho: WSPT (w/p), ATC con varios K, razon de cadenas (para que
   un predecesor "herede" la prioridad de su sucesor) y EDD. Se queda la mejor.
2. Recocido simulado sobre la lista con movimientos de insercion e intercambio
   en una ventana. Para que cada vecino sea barato de evaluar:
   - se re-decodifica solo desde la primera posicion que cambio (se guardan
     "fotos" del estado de las maquinas en cada posicion);
   - se corta apenas el costo supera el umbral de aceptacion (el numero
     aleatorio de Metropolis se sortea ANTES de evaluar);
   - si despues del tramo modificado las maquinas quedan igual que en la
     solucion base, el resto del programa es identico y no se recalcula.
"""
import heapq
import json
import math
import random
import re
import sys
import time
from bisect import bisect_right, insort

# === INICIO ALGORITMO ===
# ---------------------------------------------------------------- parametros
# Calibrados con 30 instancias contra corridas largas (3 x 500 000 iteraciones):
#   d_j ajustado (enunciado): 10 000 iter -> brecha ~0,05 % en ~0,09 s
#                             20 000 iter -> ~0,04 % en ~0,18 s
#                             0 iter (solo reglas de despacho) -> ~2,9 % en ~2 ms
#   d_j holgado (prueba de robustez): 10 000 iter -> ~1,8 %; 20 000 -> ~0,7 %
TIEMPO_MAX_R2 = 5.0       # tope de seguridad (segundos) por instancia
ITER_SA_R2 = 10000        # iteraciones del recocido simulado
VENTANA_R2 = 20           # distancia maxima de un movimiento en la lista
T_INI_R2 = 0.6            # temperatura inicial  (x peso medio x p medio)
T_FIN_R2 = 0.001          # temperatura final    (x peso medio x p medio)
SEMILLA_R2 = 2026         # semilla propia: no altera el random global


# ------------------------------------------------------- lectura de datos
_ALIAS = {
    "id": ("job", "trabajo", "id", "j", "nombre", "name"),
    "p": ("p_j", "p", "pj", "proc", "procesamiento", "tiempo_procesamiento"),
    "r": ("r_j", "r", "rj", "release", "liberacion"),
    "d": ("d_j", "d", "dj", "due", "entrega", "fecha_entrega"),
    "w": ("w_j", "w", "wj", "peso", "prioridad", "weight"),
    "pred": ("predecesores", "preds", "pred", "predecessors", "precedencias"),
}


def _campo(fila, clave):
    bajas = {str(k).strip().lower(): v for k, v in fila.items()}
    for alias in _ALIAS[clave]:
        if alias in bajas:
            return bajas[alias]
    return None


def _numero(x):
    if isinstance(x, (int, float)):
        return x
    v = float(str(x).strip())
    return int(v) if v.is_integer() else v


def _lista(x):
    """Predecesores como lista: acepta lista, None, '', '-', 'J1, J3', '[J1;J3]'."""
    if x is None or (isinstance(x, float) and x != x):
        return []
    if isinstance(x, (list, tuple, set)):
        return list(x)
    s = str(x).strip().strip("[]")
    if s.lower() in ("", "-", "none", "nan", "ninguno", "null"):
        return []
    return [t.strip().strip("'\"") for t in re.split(r"[,;\s]+", s) if t.strip().strip("'\"")]


def cargar_instancia(data):
    """Convierte la entrada (varios formatos posibles) a listas internas.

    Formatos aceptados:
      * plantilla Gradescope: {"jobs": [...], "m": 3, "p": {j: pj}, "r": {...},
        "d": {...}, "w": {...}, "preds": {j: [i, ...]}}
      * lista de filas: [{"Trabajo": "J1", "p_j": 45, "r_j": 3, "d_j": 60,
        "w_j": 2, "Predecesores": ["J3"]}, ...]  (o {"jobs"/"trabajos": [filas]})
    """
    m = 3
    filas = None
    if isinstance(data, list):
        filas = data
    else:
        if "m" in data:
            m = int(data["m"])
        for k in ("jobs", "trabajos", "Trabajos", "instancia", "data"):
            v = data.get(k)
            if isinstance(v, list) and v and isinstance(v[0], dict):
                filas = v
                break

    if filas is not None:
        ids = [_campo(f, "id") for f in filas]
        if any(i is None for i in ids):
            ids = [f"J{k + 1}" for k in range(len(filas))]
        p = [_numero(_campo(f, "p")) for f in filas]
        r = [_numero(_campo(f, "r") or 0) for f in filas]
        d = [_numero(_campo(f, "d")) for f in filas]
        w = [_numero(_campo(f, "w") if _campo(f, "w") is not None else 1) for f in filas]
        preds_raw = [_lista(_campo(f, "pred")) for f in filas]
    else:
        ids = list(data["jobs"]) if "jobs" in data else list(data["p"])

        def valor(campo, k, j, defecto=None):
            v = data.get(campo, defecto)
            if isinstance(v, dict):
                v = v.get(j, v.get(str(j), defecto))
            elif isinstance(v, list):
                v = v[k]
            return defecto if v is None else _numero(v)

        p = [valor("p", k, j) for k, j in enumerate(ids)]
        r = [valor("r", k, j, 0) for k, j in enumerate(ids)]
        d = [valor("d", k, j) for k, j in enumerate(ids)]
        w = [valor("w", k, j, 1) for k, j in enumerate(ids)]
        pr = data.get("preds", data.get("predecesores", {}))
        if isinstance(pr, dict):
            preds_raw = [_lista(pr.get(j, pr.get(str(j)))) for j in ids]
        elif isinstance(pr, list) and len(pr) == len(ids) and all(
                isinstance(x, (list, tuple)) or x is None for x in pr):
            preds_raw = [_lista(x) for x in pr]
        else:
            preds_raw = [[] for _ in ids]
        # precedencias como lista de parejas [i, j]
        for par in data.get("precedencias", data.get("prec", [])) or []:
            if isinstance(par, dict):
                par = (par.get("i", par.get("pred")), par.get("j", par.get("succ")))
            i_, j_ = par
            preds_raw[[str(x) for x in ids].index(str(j_))].append(i_)

    # nombres de predecesores -> indices (tolera "J3", 3 o "3")
    indice = {}
    for k, j in enumerate(ids):
        indice[str(j)] = k
        num = re.sub(r"\D", "", str(j))
        if num:
            indice.setdefault(num, k)
    preds = []
    for k, lst in enumerate(preds_raw):
        idx = []
        for x in lst:
            s = str(x).strip()
            pos = indice.get(s, indice.get(re.sub(r"\D", "", s)))
            if pos is not None and pos != k and pos not in idx:
                idx.append(pos)
        preds.append(tuple(idx))
    if d and any(v is None for v in d):
        raise ValueError("faltan fechas de entrega d_j")
    return ids, p, r, d, w, preds, m


class Monstruopolis:
    """Datos de una instancia y los procedimientos del algoritmo."""

    def __init__(self, ids, p, r, d, w, preds, m=3):
        self.ids, self.p, self.r, self.d, self.w = ids, p, r, d, w
        self.preds = preds
        self.m = m
        n = self.n = len(ids)
        succs = [[] for _ in range(n)]
        for j in range(n):
            for i in preds[j]:
                succs[i].append(j)
        self.succs = [tuple(s) for s in succs]
        self.con_suc = [bool(s) for s in succs]
        # datos de cada trabajo en una tupla: se leen de una vez en el decodificador
        self.datos = [(r[j], p[j], d[j], w[j], preds[j], self.con_suc[j]) for j in range(n)]

    # ------------------------------------------------------------ decodificador
    def decodificar(self, L):
        """Programa completo de la lista L. Devuelve (costo, C, f_av, f_costo):
        f_av[k] = tiempos en que quedan libres las maquinas (ordenados) y
        f_costo[k] = costo acumulado, ANTES de programar L[k] ("fotos")."""
        n = self.n
        f_av = [None] * (n + 1)
        f_costo = [0] * (n + 1)
        f_av[0] = (0,) * self.m
        costo, C, _ = self.evaluar_desde(L, 0, n, float("inf"), [0] * n, f_av, f_costo, f_av, f_costo)
        return costo, C, f_av, f_costo

    def evaluar_desde(self, L, lo, hi, umbral, C_base, f_av, f_costo, tmp_av, tmp_costo):
        """Re-decodifica L desde la posicion lo partiendo de las fotos del
        programa base (f_av[lo], f_costo[lo]); L solo cambio entre lo y hi.

        - Si el costo supera el umbral corta y devuelve None (vecino rechazado).
        - Convergencia: pasada la posicion hi, si las maquinas quedan igual que
          en el programa base, el resto del programa es identico y su costo se
          toma de f_costo sin recalcularlo.
        Devuelve (costo, C, k) con k = posicion hasta la que se recalculo."""
        if self.m != 3:
            return self._evaluar_general(L, lo, hi, umbral, C_base, f_av, f_costo, tmp_av, tmp_costo)
        datos = self.datos
        n = self.n
        a0, a1, a2 = f_av[lo]          # maquinas libres en a0 <= a1 <= a2
        costo = f_costo[lo]
        C = C_base[:]
        sucio = False                  # algun predecesor termino distinto que en la base
        k1 = lo                        # k1 = posicion del trabajo + 1
        for j in L[lo:]:
            k1 += 1
            t, pj, dj, wj, pr, cs = datos[j]
            for i in pr:
                if C[i] > t:
                    t = C[i]
            # best fit: la maquina libre mas tarde que no haga esperar a j
            if t >= a2:
                c = t + pj
                a2 = c
            elif t >= a1:
                c = t + pj
                if c <= a2:
                    a1 = c
                else:
                    a1, a2 = a2, c
            else:
                if t < a0:
                    t = a0
                c = t + pj
                if c <= a1:
                    a0 = c
                elif c <= a2:
                    a0, a1 = a1, c
                else:
                    a0, a1, a2 = a1, a2, c
            if cs and c != C_base[j]:
                sucio = True
            C[j] = c
            if c > dj:
                costo += wj * (c - dj)
                if costo > umbral:
                    return None
            est = (a0, a1, a2)
            tmp_av[k1] = est
            tmp_costo[k1] = costo
            if k1 > hi and not sucio and est == f_av[k1]:
                costo += f_costo[n] - f_costo[k1]
                return (costo, C, k1) if costo <= umbral else None
        return costo, C, n

    def _evaluar_general(self, L, lo, hi, umbral, C_base, f_av, f_costo, tmp_av, tmp_costo):
        """Igual que evaluar_desde pero para cualquier numero de maquinas."""
        p, r, d, w, preds, con_suc = self.p, self.r, self.d, self.w, self.preds, self.con_suc
        n = self.n
        av = list(f_av[lo])
        costo = f_costo[lo]
        C = C_base[:]
        sucio = False
        for k in range(lo, n):
            j = L[k]
            t = r[j]
            for i in preds[j]:
                if C[i] > t:
                    t = C[i]
            idx = bisect_right(av, t) - 1
            if idx < 0:
                idx = 0
                t = av[0]
            c = t + p[j]
            del av[idx]
            insort(av, c)
            if con_suc[j] and c != C_base[j]:
                sucio = True
            C[j] = c
            c -= d[j]
            if c > 0:
                costo += w[j] * c
                if costo > umbral:
                    return None
            est = tuple(av)
            tmp_av[k + 1] = est
            tmp_costo[k + 1] = costo
            if k >= hi and not sucio and est == f_av[k + 1]:
                costo += f_costo[n] - f_costo[k + 1]
                return (costo, C, k + 1) if costo <= umbral else None
        return costo, C, n

    def aceptar(self, f_av, f_costo, tmp_av, tmp_costo, lo, kc):
        """Actualiza las fotos del programa base con las del vecino aceptado."""
        if kc < self.n:
            delta = tmp_costo[kc] - f_costo[kc]
            if delta:
                for q in range(kc + 1, self.n + 1):
                    f_costo[q] += delta
        f_av[lo + 1:kc + 1] = tmp_av[lo + 1:kc + 1]
        f_costo[lo + 1:kc + 1] = tmp_costo[lo + 1:kc + 1]

    def programa(self, L):
        """Programa con nombre de maquina: lista de (j, maquina, inicio, fin)."""
        p, r, preds = self.p, self.r, self.preds
        libre = [0] * self.m
        C = [0] * self.n
        salida = []
        for j in L:
            t = r[j]
            for i in preds[j]:
                if C[i] > t:
                    t = C[i]
            aptas = [k for k in range(self.m) if libre[k] <= t]
            if aptas:   # best fit: la que quedo libre mas tarde sin pasarse de t
                k = max(aptas, key=lambda q: (libre[q], -q))
            else:
                k = min(range(self.m), key=lambda q: (libre[q], q))
                t = libre[k]
            C[j] = t + p[j]
            libre[k] = C[j]
            salida.append((j, k, t, C[j]))
        return salida

    # --------------------------------------------------------- reglas iniciales
    def lista_topologica(self, clave):
        """Ordena por clave (menor primero) respetando precedencias (Kahn)."""
        n = self.n
        faltan = [len(self.preds[j]) for j in range(n)]
        heap = [(clave[j], j) for j in range(n) if faltan[j] == 0]
        heapq.heapify(heap)
        L = []
        while heap:
            _, j = heapq.heappop(heap)
            L.append(j)
            for s in self.succs[j]:
                faltan[s] -= 1
                if faltan[s] == 0:
                    heapq.heappush(heap, (clave[s], s))
        if len(L) < n:   # ciclo en precedencias (no deberia pasar)
            vistos = set(L)
            L += [j for j in sorted(range(n), key=clave.__getitem__) if j not in vistos]
        return L

    def razon_cadena(self):
        """rho_j = max(w/p) de las cadenas que salen de j (estilo Sidney):
        un predecesor de un trabajo urgente sube su prioridad."""
        n, p, w = self.n, self.p, self.w
        orden = self.lista_topologica(list(range(n)))
        mejor = [(w[j], p[j]) for j in range(n)]
        for j in reversed(orden):
            for s in self.succs[j]:
                ws, ps = mejor[s]
                cand = (w[j] + ws, p[j] + ps)
                if cand[0] * mejor[j][1] > mejor[j][0] * cand[1]:
                    mejor[j] = cand
        return [a / b for a, b in mejor]

    def despacho(self, indice):
        """Despacho dinamico: cuando se libera una maquina elige, entre los
        trabajos listos, el de mayor indice(j, t, p_medio)."""
        n, m = self.n, self.m
        p, r, preds = self.p, self.r, self.preds
        faltan = [len(preds[j]) for j in range(n)]
        listo = list(r)
        disponibles = {j for j in range(n) if faltan[j] == 0}
        av = [0] * m
        resto_p = sum(p)
        L = []
        while disponibles:
            t = av[0]
            cand = [j for j in disponibles if listo[j] <= t]
            if not cand:
                t = min(listo[j] for j in disponibles)
                cand = [j for j in disponibles if listo[j] <= t]
            pm = resto_p / (n - len(L))
            j = max(cand, key=lambda q: (indice(q, t, pm), -q))
            s = listo[j]
            idx = bisect_right(av, s) - 1
            if idx < 0:
                idx = 0
                s = av[0]
            c = s + p[j]
            del av[idx]
            insort(av, c)
            L.append(j)
            disponibles.discard(j)
            resto_p -= p[j]
            for q in self.succs[j]:
                if c > listo[q]:
                    listo[q] = c
                faltan[q] -= 1
                if faltan[q] == 0:
                    disponibles.add(q)
        return L

    def listas_iniciales(self):
        p, d, w = self.p, self.d, self.w
        listas = [
            self.lista_topologica([-w[j] / p[j] for j in range(self.n)]),     # WSPT
            self.lista_topologica([-x for x in self.razon_cadena()]),        # cadenas
            self.lista_topologica([d[j] for j in range(self.n)]),            # EDD
            self.despacho(lambda j, t, pm: w[j] / p[j]),                      # WSPT dinamico
        ]
        for K in (0.5, 1.0, 2.0, 4.0):                                       # ATC
            listas.append(self.despacho(
                lambda j, t, pm, K=K: w[j] / p[j] * math.exp(-max(d[j] - p[j] - t, 0) / (K * pm))))
        return listas

    # ------------------------------------------------------------- busqueda
    def recocido(self, L, rng, iteraciones, limite):
        """Recocido simulado sobre la lista. Devuelve (mejor lista, mejor costo)."""
        n = self.n
        preds, succs = self.preds, self.succs
        pos = [0] * n
        for k, j in enumerate(L):
            pos[j] = k
        costo, C, f_av, f_costo = self.decodificar(L)
        mejor, mejor_costo = L[:], costo
        if costo == 0 or iteraciones <= 0 or n < 2:
            return mejor, mejor_costo
        tmp_av = f_av[:]
        tmp_costo = f_costo[:]
        escala = (sum(self.w) / n) * (sum(self.p) / n)
        T = T_INI_R2 * escala
        factor = (T_FIN_R2 / T_INI_R2) ** (1.0 / iteraciones)
        W = VENTANA_R2
        ancho = 2 * W + 1
        log = math.log
        azar = rng.random            # random() es mucho mas rapido que randint()
        for it in range(iteraciones):
            if (it & 511) == 0 and time.perf_counter() > limite:
                break
            T *= factor
            a = int(azar() * n)
            b = a + int(azar() * ancho) - W
            if b < 0 or b >= n or b == a:
                continue
            x = L[a]
            if azar() < 0.5:
                # insercion: x pasa de la posicion a a la b
                if b < a:
                    if preds[x] and any(pos[i] >= b for i in preds[x]):
                        continue
                    lo, hi = b, a
                else:
                    if succs[x] and any(pos[s] <= b for s in succs[x]):
                        continue
                    lo, hi = a, b
                nueva = L[:]
                del nueva[a]
                nueva.insert(b, x)
            else:
                # intercambio de las posiciones lo y hi
                lo, hi = (a, b) if a < b else (b, a)
                y1, y2 = L[lo], L[hi]
                if ((succs[y1] and any(pos[s] <= hi for s in succs[y1]))
                        or (preds[y2] and any(pos[i] >= lo for i in preds[y2]))):
                    continue
                nueva = L[:]
                nueva[lo], nueva[hi] = y2, y1
            u = azar()
            umbral = costo - T * log(u) if u > 0.0 else float("inf")
            res = self.evaluar_desde(nueva, lo, hi, umbral, C, f_av, f_costo, tmp_av, tmp_costo)
            if res is None:
                continue
            costo, C, kc = res
            L = nueva
            self.aceptar(f_av, f_costo, tmp_av, tmp_costo, lo, kc)
            for k in range(lo, hi + 1):
                pos[L[k]] = k
            if costo < mejor_costo:
                mejor, mejor_costo = L[:], costo
                if costo == 0:
                    break
        return mejor, mejor_costo

    def resolver(self, tiempo_max=TIEMPO_MAX_R2, semilla=SEMILLA_R2, iteraciones=ITER_SA_R2):
        """Devuelve (lista, costo, info)."""
        t0 = time.perf_counter()
        limite = t0 + tiempo_max
        rng = random.Random(semilla)
        listas = self.listas_iniciales()
        costos = [self.decodificar(L)[0] for L in listas]
        k = min(range(len(listas)), key=costos.__getitem__)
        L, costo = listas[k], costos[k]
        info = {"inicial": costo, "regla": k}
        L, costo = self.recocido(L, rng, iteraciones, limite)
        info["tiempo"] = time.perf_counter() - t0
        return L, costo, info
# === FIN ALGORITMO ===


def solve(data):
    """
    Parametro: data - diccionario (o lista) cargado desde data.json
    Retorna: lista con un diccionario por trabajo
             [{"job": "J1", "machine": "M1", "start": 0, "end": 45}, ...]
    """
    ids, p, r, d, w, preds, m = cargar_instancia(data)
    modelo = Monstruopolis(ids, p, r, d, w, preds, m)
    L, _, _ = modelo.resolver()
    filas = {j: (k, s, c) for j, k, s, c in modelo.programa(L)}
    return [{"job": ids[j], "machine": f"M{filas[j][0] + 1}",
             "start": filas[j][1], "end": filas[j][2]} for j in range(len(ids))]


def tardanza_ponderada(data, salida):
    """sum w_j * max(0, C_j - d_j) de una salida de solve()."""
    ids, p, r, d, w, preds, m = cargar_instancia(data)
    fin = {str(f["job"]): f["end"] for f in salida}
    return sum(w[k] * max(0, fin[str(j)] - d[k]) for k, j in enumerate(ids))


if __name__ == "__main__":
    ruta = sys.argv[1] if len(sys.argv) > 1 else "data.json"
    with open(ruta, encoding="utf-8") as f:
        data = json.load(f)
    t0 = time.time()
    salida = solve(data)
    print(json.dumps(salida, indent=2))
    print(f"// sum wjTj = {tardanza_ponderada(data, salida)}  |  "
          f"tiempo = {int((time.time() - t0) * 1000)} ms", file=sys.stderr)
```


---

**Archivos de esta carpeta que no se copiaron en el paquete** (están completos en el repositorio):

- `corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/gradescope/reto1_willy_wonka/reto_schedulling.py`: copia generada de `solucion/reto1.py` dentro de la plantilla (ver `construir_plantillas.py`).
- `corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/gradescope/reto2_monstruopolis/reto_schedulling.py`: copia generada de `solucion/reto2.py` dentro de la plantilla (ver `construir_plantillas.py`).
