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
