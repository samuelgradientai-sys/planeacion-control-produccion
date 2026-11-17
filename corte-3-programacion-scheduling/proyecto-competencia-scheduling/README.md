# Proyecto: competencia de scheduling en Gradescope (Corte 3)

## Qué cubre

Es el proyecto final del Corte 3: una competencia por grupos de 5 en la que cada grupo programa en Python dos algoritmos de secuenciación. Gradescope los califica automáticamente con instancias aleatorias: 60 % calidad del objetivo, 30 % tiempo de cómputo y 10 % reporte técnico en PDF.

- **Reto 01, Willy Wonka:** flow shop de permutación de 3 máquinas, alistamientos según el tipo de lote y prohibición N→R; objetivo $C_{\max}$.
- **Reto 02, Monstruópolis:** 3 máquinas paralelas idénticas con fechas de liberación y precedencias; objetivo $\sum w_jT_j$.

La carpeta tiene los enunciados y las plantillas del profesor (`enunciados/`) y la solución del estudiante (`solucion/`). La solución entrega el óptimo demostrado en el Reto 1 y queda a ~0,05 % del mejor valor conocido en el Reto 2.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [enunciados/instructivo-competencia-scheduling.md](./enunciados/instructivo-competencia-scheduling.md) (gemelo del PDF, 4 págs.) | Reglas de la competencia: retos, pesos de la nota, penalizaciones, ranking, formato `solve()`, librerías permitidas, límite de 60 s | **1.º** |
| [enunciados/reto-1-willy-wonka.md](./enunciados/reto-1-willy-wonka.md) (gemelo del PDF, 4 págs.) | Enunciado del Reto 01: 15 lotes S/N/R, tiempos en M1–M3, alistamientos (Tablas 2–4), regla N→R, formato `data.json` | **2.º** |
| [enunciados/reto-2-monstruopolis.md](./enunciados/reto-2-monstruopolis.md) (gemelo del PDF, 3 págs.) | Enunciado del Reto 02: 50 trabajos, $p_j$, $r_j$, $d_j$, $w_j$, precedencias, objetivo, ejemplo de salida | **3.º** |
| [enunciados/plantilla-reto-1-willy-wonka/reto_schedulling.py](./enunciados/plantilla-reto-1-willy-wonka/reto_schedulling.py) | Plantilla del profesor para el Reto 1: clase `Schedulling`, generador aleatorio de instancias y evaluador `calcular_makespan_penalizado` (ver abajo) | 4.º |
| [enunciados/plantilla-reto-2-monstruopolis/reto_schedulling.py](./enunciados/plantilla-reto-2-monstruopolis/reto_schedulling.py) | Plantilla del profesor para el Reto 2: clase `Schedulling(GeneradorInstancias)` con un esqueleto de `resolver_instancia()` (ver abajo) | 4.º |
| [solucion/README.md](./solucion/README.md) | README de la solución, escrito por el estudiante: algoritmos, qué subir a Gradescope, cómo probar, calidad frente a tiempo, problemas abiertos | **5.º** |
| [solucion/INFORME_TECNICO.md](./solucion/INFORME_TECNICO.md) | Borrador del reporte técnico (10 % de la nota): modelo, algoritmo, justificación, resultados, lecciones y referencias | **6.º** |
| [solucion/reto1.py](./solucion/reto1.py) | Reto 1 en el formato del instructivo, `solve(data) -> {"Cmax","secuencia","tiempo"}`. Clase `WillyWonka`: cota inferior, NEH, bloques por tipo, búsqueda local con aceleración de Taillard, programación dinámica acotada e Iterated Greedy de respaldo | 7.º |
| [solucion/reto2.py](./solucion/reto2.py) | Reto 2 en el formato del instructivo, `solve(data) -> [{"job","machine","start","end"}]`. Clase `Monstruopolis`: lectura de varios formatos de entrada, decodificador de listas, 8 reglas de despacho y recocido simulado con evaluación incremental | 7.º |
| [solucion/construir_plantillas.py](./solucion/construir_plantillas.py) | Copia el bloque entre `# === INICIO ALGORITMO ===` y `# === FIN ALGORITMO ===` de `reto1.py`/`reto2.py` dentro de la plantilla del profesor y escribe los archivos de `gradescope/` | — |
| [solucion/gradescope/reto1_willy_wonka/reto_schedulling.py](./solucion/gradescope/reto1_willy_wonka/reto_schedulling.py) | Reto 1 empaquetado en la plantilla del profesor (generado; no se edita a mano). `resolver_instancia()` devuelve `secuencia`, `valor_objetivo`, `Cmax` y `tiempo`; el `import optimizador` queda en un `try/except` | — |
| [solucion/gradescope/reto2_monstruopolis/reto_schedulling.py](./solucion/gradescope/reto2_monstruopolis/reto_schedulling.py) | Reto 2 empaquetado en la plantilla del profesor (generado). `resolver_instancia()` devuelve `secuencia` (con `Cj`) y `valor_objetivo` | — |
| [solucion/pruebas/probar_reto1.py](./solucion/pruebas/probar_reto1.py) | Banco local del Reto 1: 30 instancias del generador de la plantilla (semilla 42). Valida la permutación y N→R, recalcula el $C_{\max}$ con un evaluador independiente, lo compara con la cota (y con el exacto si se usa `--exacto`) y muestra también el valor de la función defectuosa de la plantilla | — |
| [solucion/pruebas/probar_reto2.py](./solucion/pruebas/probar_reto2.py) | Banco local del Reto 2: 30 instancias. Un validador independiente revisa $r_j$, precedencias, solapes y $end=start+p_j$, y recalcula $\sum w_jT_j$. Opciones `--referencia` (corrida larga) y `--holgura` | — |
| [solucion/pruebas/exacto_reto1.py](./solucion/pruebas/exacto_reto1.py) | Segundo método exacto del Reto 1, implementado aparte para verificar el primero: programación dinámica por capas con frentes de Pareto (fin M1, M2, M3) y poda por cota | — |
| [solucion/pruebas/cota_reto2.py](./solucion/pruebas/cota_reto2.py) | Cota inferior del Reto 2 por relajación lagrangiana de la formulación indexada en el tiempo, con subgradiente y paso de Polyak (usa numpy) | — |
| [solucion/pruebas/generador.py](./solucion/pruebas/generador.py) | Imitación local del módulo `generador` que la plantilla del Reto 2 importa en Gradescope. Hace $p_j\in[10,100]$, $r_j\in[0,30]$, $w_j\in[1,5]$, 5 precedencias $i<j$ y $d_j$ igual al fin más temprano | — |
| [solucion/pruebas/data_ejemplo_reto1.json](./solucion/pruebas/data_ejemplo_reto1.json) | Datos del enunciado de Willy Wonka (Tablas 1–4) en el formato `data.json` | — |
| [solucion/pruebas/data_ejemplo_reto2.json](./solucion/pruebas/data_ejemplo_reto2.json) | Instancia de 50 trabajos en formato de filas (`Trabajo, p_j, r_j, d_j, w_j, Predecesores`), con precedencias J2→J21, J23→J27, J17→J31, J22→J36 y J3→J49 | — |
| [solucion/pruebas/data_ejemplo_reto2_plantilla.json](./solucion/pruebas/data_ejemplo_reto2_plantilla.json) | La misma instancia en el formato de la plantilla (`jobs, m, p, r, d, w, preds`) | — |

## Orden de estudio sugerido

1. Leer las reglas en el [instructivo](./enunciados/instructivo-competencia-scheduling.md) y los dos enunciados.
2. Repasar la teoría:
   - notación α|β|γ en [01-introduccion-scheduling](../01-introduccion-scheduling/);
   - WSPT y ATC en [02-una-maquina](../02-una-maquina/);
   - máquinas paralelas en [03-maquinas-paralelas](../03-maquinas-paralelas/);
   - Johnson y NEH en [04-flow-shop](../04-flow-shop/).
3. Leer la sección «Plantillas del profesor» de este README: las plantillas usan un formato distinto del instructivo y tienen errores.
4. Leer el [informe técnico](./solucion/INFORME_TECNICO.md) y luego el [README de la solución](./solucion/README.md).
5. Ejecutar los ejemplos (ver «Cómo ejecutar») y revisar el código de `reto1.py` y `reto2.py`.

## Enunciado en resumen

**Reglas comunes** (detalle en el [instructivo](./enunciados/instructivo-competencia-scheduling.md)):

- Grupos de 5; un integrante sube la entrega.
- Límite de 60 s por instancia; si se pasa, recibe el peor puntaje en esa instancia.
- Solo biblioteca estándar y numpy; nada de OR-Tools, PuLP ni Gurobi.
- Varias entregas permitidas; cuenta la última.
- El ranking usa el objetivo promedio más las penalidades por violación: el mejor equipo recibe 100 y los demás se escalan en proporción.
- Reporte técnico en PDF de máximo 4 páginas.

**Reto 01, Willy Wonka** ([enunciado](./enunciados/reto-1-willy-wonka.md)):

- 15 lotes de tres tipos (S simple, N nueces, R relleno) pasan por M1 (mezclado), M2 (moldeo) y M3 (empaque) en el mismo orden en las tres máquinas.
- Los tiempos de ejemplo están entre 27 y 45 min en M1, entre 22 y 40 en M2 y entre 11 y 25 en M3.
- Al cambiar de tipo hay un alistamiento por máquina, por ejemplo N→R: 40, 30 y 12 min en M1, M2 y M3.
- Un lote R no puede ir justo después de uno N.
- Se minimiza el tiempo en que termina el último lote.

**Reto 02, Monstruópolis** ([enunciado](./enunciados/reto-2-monstruopolis.md)):

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

### Plantilla del Reto 1 ([código](./enunciados/plantilla-reto-1-willy-wonka/reto_schedulling.py))

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

### Plantilla del Reto 2 ([código](./enunciados/plantilla-reto-2-monstruopolis/reto_schedulling.py))

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

Detalle completo en el [informe técnico](./solucion/INFORME_TECNICO.md). Lo que va en la entrega usa solo la biblioteca estándar; numpy aparece solo en `pruebas/`. Cada reto usa su propia semilla (`random.Random(2026)`), así que no altera el `random` global con el que la plantilla genera las instancias.

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

- **Notación α|β|γ:** α es el entorno de máquinas (F3, P3), β las restricciones (prmu, $s_{ij}$, $r_j$, prec) y γ el objetivo ($C_{\max}$, $\sum w_jT_j$). Ver [L16](../01-introduccion-scheduling/L16-intro-scheduling.md).
- **Flow shop con alistamiento:** $C_{m,\pi_k}=\max(C_{m,\pi_{k-1}},C_{m-1,\pi_k})+s^m_{\tau(\pi_{k-1})\tau(\pi_k)}+p_{m,\pi_k}$. Ver [reto-1](./enunciados/reto-1-willy-wonka.md).
- **NEH y Johnson:** en [L19](../04-flow-shop/L19-flow-shop-scheduling.md). La regla de Johnson para tres máquinas usa $(p_1+p_2,\ p_2+p_3)$.
- **Tardanza:** $T_j=\max(0,C_j-d_j)$.
- **WSPT:** ordenar por $w_j/p_j$ decreciente.
- **ATC:** $I_j(t)=\frac{w_j}{p_j}e^{-\max(d_j-p_j-t,0)/(K\bar p)}$. Ver [L17](../02-una-maquina/L17-single-machine-scheduling.md) y [atc.py](../02-una-maquina/atc.py).
- **Recocido simulado:** se acepta un vecino peor con probabilidad $e^{-\Delta/T}$, con $T$ que decrece geométricamente.
- **Iterated Greedy:** destruir $d$ lotes, reinsertarlos con NEH y aceptar con temperatura constante.

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado |
|---|---|---|
| Willy Wonka con los datos del enunciado | [solucion/reto1.py](./solucion/reto1.py) con [data_ejemplo_reto1.json](./solucion/pruebas/data_ejemplo_reto1.json); explicado en el [informe](./solucion/INFORME_TECNICO.md) | $C_{\max}=621$ (óptimo), bloques R → S → N |
| 30 instancias de la plantilla del Reto 1 | [probar_reto1.py](./solucion/pruebas/probar_reto1.py) | 30/30 óptimas, $C_{\max}$ promedio 616,77 |
| Monstruópolis, instancia de ejemplo | [solucion/reto2.py](./solucion/reto2.py) con [data_ejemplo_reto2.json](./solucion/pruebas/data_ejemplo_reto2.json) | $\sum w_jT_j=27\,683$ |
| 30 instancias del Reto 2 | [probar_reto2.py](./solucion/pruebas/probar_reto2.py) | Promedio 38 182; ~0,05 % del mejor conocido; 0 violaciones |

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

- [01-introduccion-scheduling](../01-introduccion-scheduling/): notación α|β|γ y medidas de desempeño.
- [02-una-maquina](../02-una-maquina/): WSPT, EDD y ATC, la base de las reglas de despacho del Reto 2; [atc.py](../02-una-maquina/atc.py).
- [03-maquinas-paralelas](../03-maquinas-paralelas/): máquinas paralelas y LNS, el entorno del Reto 2.
- [04-flow-shop](../04-flow-shop/): Johnson y NEH, la base de la heurística del Reto 1.
- [05-job-shop](../05-job-shop/): búsqueda local y la referencia de Ruiz y Stützle (iterated greedy); ninguno de los retos es un job shop.
- [00-compendio-metodos-scheduling](../00-compendio-metodos-scheduling/): compendio de los métodos del corte.
- [otros-archivos](../otros-archivos/): no tiene relación (material de otra materia).
