# L16-intro-scheduling

> **Archivo:** [`L16-intro-scheduling.pdf`](./L16-intro-scheduling.pdf) · **Corte 3** · 49 páginas  
> **Nombre original:** `CORTE 3/Lec 16 - intro Scheduling.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** introducción a la programación de la producción (*scheduling*): dónde encaja en la jerarquía de planeación, sus elementos, sus indicadores, la notación $\alpha|\beta|\gamma$ de Graham et al. (1979) y algunas propiedades (programas sin retrasos, programas activos, anomalías y jerarquía de complejidad).

**Ideas clave**

- El scheduling es el último eslabón de la jerarquía: Pronósticos → Planeación agregada → Plan maestro → MRP → **Programación detallada**. Recibe las órdenes que libera el MRP y entrega un programa al despacho y al taller (pp. 3-4, 15-16).
- Elementos: trabajos (disponibilidad $r_j$, fecha de entrega $d_j$, tiempo de proceso $p_{ij}$, prioridad $w_j$, setup, ruta) y máquinas (configuración y capacidad) (pp. 11, 13).
- Objetivos típicos: cumplir fechas, bajar el WIP y el tiempo de flujo, usar bien las máquinas, reducir setups y costos (p. 12).
- Notación $\alpha|\beta|\gamma$: $\alpha$ = ambiente de máquinas, $\beta$ = restricciones, $\gamma$ = función objetivo (pp. 18-31).
- El orden de los trabajos cambia el resultado: en el ejemplo de dos trabajos y dos máquinas, A-B da $C_{max}=25$ y B-A da $C_{max}=22$ (pp. 7-9).
- **Anomalías** en $P2|prec|C_{max}$: el óptimo es 31; si se reducen todos los tiempos en una unidad, la programación sin esperas da 32, y con 3 máquinas da 36. Más recursos o tiempos más cortos no garantizan un mejor makespan (pp. 40-43).
- Programación sin retrasos (*non-delay*): no se deja una máquina ociosa si hay trabajos esperando. Programa activo: ninguna operación puede adelantarse a un hueco sin retrasar otra (pp. 39, 44).
- Hay $n!$ secuencias posibles en una máquina; la mayoría de los problemas son NP-hard, pero $1||\sum w_jC_j$ se resuelve en tiempo polinomial (p. 46).
- En la vida real hay reglas implícitas, fechas y prioridades flexibles y objetivos no clásicos; existe software comercial como Siemens Preactor (pp. 47-48).

**Fórmulas y métodos**

Parámetros (p. 13): $n$ trabajos indexados en $j$, $m$ máquinas indexadas en $i$; $p_{ij}$ tiempo de proceso del trabajo $j$ en la máquina $i$; $r_j$ liberación; $d_j$ fecha de entrega; $w_j$ prioridad o peso.

Indicadores (p. 14), con $C_j$ = instante en que termina el trabajo $j$:

$$C_{max}=\max_j C_j \qquad \bar F=\frac{1}{n}\sum_j (C_j-r_j)$$

$$L_j=C_j-d_j \qquad T_j=\max(L_j,0) \qquad E_j=\max(-L_j,0)=\max(0,d_j-C_j)$$

$$U_j=\begin{cases}1 & T_j>0\\ 0 & \text{en otro caso}\end{cases}\qquad \bar T=\frac{1}{n}\sum_j T_j \qquad \sum_j w_jT_j \qquad \sum_j U_j$$

Funciones objetivo $\gamma$ (pp. 27-31):

- $C_{max}=\max\{C_1,\dots,C_N\}$: al minimizarlo se suele maximizar la utilización.
- $L_{max}=\max\{L_1,\dots,L_N\}$: mide la peor violación de la fecha de entrega.
- $\sum w_jC_j$: tiempo ponderado total de terminación (*weighted flow time*); representa el costo de mantener inventario.
- $\sum w_j(1-e^{-rC_j})$: tiempo ponderado descontado, con $r$ = tasa de descuento (p. ej. 10 %); costo marginal de terminación decreciente.
- $\sum w_jT_j$: tardanza ponderada total; $\sum w_jE_j$: anticipo ponderado total.

Ambientes $\alpha$ (pp. 19-22):

| Símbolo | Ambiente | Descripción |
|---|---|---|
| 1 | Una máquina | Un solo recurso. |
| $Pm$ | Máquinas idénticas en paralelo | Cada trabajo necesita una operación en cualquiera de las $m$ máquinas. |
| $Qm$ | Paralelas uniformes | La máquina $i$ tiene velocidad $v_i$; tiempo $p_j/v_i$. |
| $Rm$ | Paralelas no relacionadas | La velocidad $v_{ij}$ depende de la máquina y del trabajo. |
| $Fm$ | Flow shop | $m$ máquinas en serie; todos los trabajos siguen la misma ruta. |
| $FFc$ | Flow shop flexible | $c$ etapas con máquinas paralelas idénticas en cada una. |
| $Jm$ | Job shop | Cada trabajo tiene su propia ruta. |
| $FJc$ | Job shop flexible | $c$ etapas con máquinas paralelas; ruta propia por trabajo. |
| $Om$ | Open shop | Todos pasan por todas las máquinas, sin ruta fija. |

Restricciones $\beta$ (pp. 23-26): $r_j$ (liberación), $s_{jk}$ (setups dependientes de la secuencia; $s_{0k}$ inicio, $s_{j0}$ limpieza final, $s_{ijk}$ dependiente de la máquina), *prmp* (interrupciones), *prec* (precedencias: cadenas, intree, outtree), *brkdwn* (fallas), $M_j$ (elegibilidad de máquinas), *prmu* (misma secuencia en todas las máquinas), *block* (buffer limitado), *nwt* (sin espera) y *recrc* (recirculación).

Jerarquía de complejidad (pp. 45-46): $A\propto B$ significa que $A$ es un caso especial de $B$ (un algoritmo para $B$ resuelve $A$):

$$1||\sum C_j\ \propto\ 1||\sum w_jC_j\ \propto\ Pm||\sum w_jC_j\ \propto\ Qm|prec|\sum w_jC_j$$

**Ejemplos resueltos**

| Página | Ejemplo | Resultado |
|---|---|---|
| 7-9 | 2 trabajos en 2 máquinas en serie (A: 8 y 5; B: 7 y 10) | A-B: $C_{max}=25$; B-A: $C_{max}=22$ |
| 15-16 | Registros MRP de 2 productos → 4 órdenes de producción | Órdenes 0001-0004 con $p$ = 0.4, 0.6, 0.5 y 0.7 semanas ($p$ = lote × factor) |
| 17 | Gantt de las 4 órdenes en una máquina | La orden 0004 termina en 4.2 con $d=4$: tardanza de 0.2 semanas |
| 40-41 | $P2\|prec\|C_{max}$ con 10 trabajos | Solución óptima $C_{max}=31$ |
| 42 | Mismo problema con $p_j-1$ | Programa sin esperas con $C_{max}=32$ (empeora) |
| 43 | Mismo problema con 3 máquinas | $C_{max}=36$ (empeora) |
| 32-36 | Lectura de la notación | $FFc\|r_j\|\sum w_jT_j$ (fábrica de papel), $Pm\|r_j,M_j\|\sum w_jT_j$ (puertas de aeropuerto), $P\infty\|prec\|C_{max}$ (proyecto) |

**Páginas clave**

- Contexto y jerarquía: pp. 3-6.
- Ejemplo introductorio de secuenciación: pp. 7-9.
- Elementos, objetivos, parámetros e indicadores: pp. 11-14.
- Del MRP a las órdenes y al Gantt: pp. 15-17.
- Notación $\alpha|\beta|\gamma$: pp. 18-31; ejemplos de notación: pp. 32-36.
- Tipos de programación, sin retrasos, anomalías y programa activo: pp. 37-44.
- Complejidad y realidad industrial: pp. 45-48.

**Relación con otros archivos del repo**

- Siguiente tema, una máquina (reglas de despacho, WSPT, EDD, ATC, CR, Moore): [L17](../02-una-maquina/L17-single-machine-scheduling.md) y su [README](../02-una-maquina/README.md).
- Máquinas en paralelo ($Pm$): [L18](../03-maquinas-paralelas/L18-parallel-machine-scheduling.md). Flow shop ($Fm$; el ejemplo de las pp. 7-9 es un flow shop de 2 máquinas, y la secuencia B-A coincide con la que da la regla de Johnson, cosa que la diapositiva no dice): [L19](../04-flow-shop/L19-flow-shop-scheduling.md). Job shop: [job-shop-y-flexible-job-shop](../05-job-shop/job-shop-y-flexible-job-shop.md).
- Compendio de métodos del corte 3: [metodos-programacion-produccion-corte3](../00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md).
- Los registros MRP de la p. 15 vienen del corte 2: [L14 MRP](../../corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md) y [L15 MRP II](../../corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md).
- La notación se aplica en la competencia: [proyecto-competencia-scheduling](../proyecto-competencia-scheduling/solucion/README.md) ($F3|prmu,s_{ij}|C_{max}$ y $P3|r_j,prec|\sum w_jT_j$).

**Observaciones sobre el material**

- En la p. 7 los subíndices de $p$ van como (trabajo, máquina): $p_{11}=8$ es A en M1 y $p_{12}=5$ es A en M2. En la p. 13, en cambio, $p_{ij}$ es el trabajo $j$ en la máquina $i$.
- En el Gantt de la p. 43, el trabajo 9 se dibuja de 6 a 15 (9 unidades) aunque $p_9=8$. El makespan (36) no cambia.
- En la p. 17 hay un bloque azul claro sin rótulo entre 2.0 y 2.2; no se explica qué representa.
- La p. 46 dice "Estos problemas se conocen como NP-Hard" justo antes de aclarar que $1||\sum w_jC_j$ es polinomial. Lo NP-hard son los problemas más generales de la cadena, como $Pm||\sum w_jC_j$; esta lectura es deducida.

## Contenido completo (página por página)

### Página 1 — Programación de la Producción (portada)

Portada: **Programación de la Producción**. Logo de la Universidad de La Sabana y licencia Creative Commons BY-NC-SA.

> [Imagen decorativa: foto de un edificio del campus en tonos azules.]

### Página 2 — Actividades recomendadas

- Lectura:
  - Shaikh, N., Prabhu, V., Abril, D., Sánchez, D., Arias, J., Rodríguez, E., & Riaño, G. (2011). *Kimberly-Clark Latin America builds an optimization-based system for machine scheduling*. Interfaces, 41(5), 455-465.
  - CAP. 19. Pinedo, M. L. (2016). *Scheduling: theory, algorithms, and systems*. Springer.

> [Imagen decorativa: franja inferior con foto del campus y logo de la Universidad de La Sabana; se repite en casi todas las diapositivas y no se vuelve a mencionar.]

### Página 3 — Flujo de información en una empresa

> [Diagrama: seis bloques en fila, unidos por flechas curvas de izquierda a derecha. Cada bloque tiene una etiqueta (título) y unas viñetas con su salida.]

| Orden | Bloque (etiqueta) | Contenido / salida |
|---|---|---|
| 1 | Planeación de la Producción | • Pronóstico de la demanda • Cantidades y fechas |
| 2 | MRP (CRP) | • Ordenes de compra • Liberación de ordenes |
| 3 | Scheduling and Rescheduling | • Programa de producción |
| 4 | Dispatching | (sin viñetas) |
| 5 | Shopfloor management | • Recolección de información |
| 6 | Shopfloor | • Ejecución de tareas |

### Página 4 — Jerarquía de la Planeación de Producción

> [Diagrama: cinco cajas apiladas, unidas por flechas hacia abajo.]

Pronósticos → Planeación Agregada → Plan Maestro de Producción → M.R.P. → Programación Detallada

### Página 5 — Aplicaciones de programación

- Programación de Proyectos
- Programación de Operarios
- Programación de Tripulaciones
- Programación de Producción
- Este curso se concentra en **programación de producción**.

### Página 6 — Machine Scheduling

- Programar la secuencia de las operaciones
- Sistemas de manufactura
- Ambientes de procesamiento de información
- Sistemas de prestación de servicios: asignación de puertas en un aeropuerto.

### Página 7 — Ejemplo

- Haga la secuenciación de estos dos trabajos:
  - Respetando la secuencia M1 – M2

$$p_{11}=8,\qquad p_{12}=5,\qquad p_{21}=7,\qquad p_{22}=10$$

(Aquí el primer subíndice es el trabajo y el segundo la máquina: trabajo 1 = Job A, trabajo 2 = Job B; ver la tabla de la página 8.)

### Página 8 — Ejemplo (secuencia A-B)

- Haga la secuenciación de estos dos trabajos:
  - Respetando la secuencia M1 – M2

| Tiempo de proceso | M1 | M2 |
|---|---|---|
| Job A | 8 | 5 |
| Job B | 7 | 10 |

**Programando A-B: Cmax = 25**

> [Diagrama: Gantt de 2 máquinas (M1, M2) con eje "tiempo" de 1 a 25. En M1: A y luego B (B sombreado gris). En M2: A y luego B.]

| Máquina | Trabajo | Inicio | Fin |
|---|---|---|---|
| M1 | A | 0 | 8 |
| M1 | B | 8 | 15 |
| M2 | A | 8 | 13 |
| M2 | B | 15 | 25 |

M2 queda ociosa de 13 a 15 esperando a que B salga de M1. $C_{max}=25$.

### Página 9 — Ejemplo (secuencia B-A)

Misma tabla de tiempos que la página 8.

**Programando B-A: Cmax = 22**

> [Diagrama: Gantt de 2 máquinas con eje "tiempo" de 1 a 25.]

| Máquina | Trabajo | Inicio | Fin |
|---|---|---|---|
| M1 | B | 0 | 7 |
| M1 | A | 7 | 15 |
| M2 | B | 7 | 17 |
| M2 | A | 17 | 22 |

$C_{max}=22$: el orden de los trabajos cambia el makespan aunque los tiempos sean los mismos.

### Página 10 — Tipos de modelos de scheduling

- Determinísticos
  - Una máquina
  - Máquinas en paralelo
  - Flow shops y flexible flow shops
  - Job shops
  - Open shops
- Estocásticos (*llegadas de trabajos, tiempos de procesamiento, etc.*)
  - No en este curso

### Página 11 — Elementos de la programación de producción

- Trabajos
  - Disponibilidad
  - Fecha de entrega
  - Tiempo de proceso
  - Prioridad
  - Tiempo de alistamiento (setup)
  - Ruta de proceso
- Máquinas
  - Configuración
  - Capacidad

> [Diagrama: Gantt de proyecto con barras rojas; eje superior de fechas 07/01, 26/02, 17/04, 06/06 (unos 50 días entre marcas). La duración (en días) va escrita dentro de cada barra. Inicio y fin son aproximados, leídos de la posición de las barras.]

| Actividad | Duración (días) | Inicio aprox. | Fin aprox. |
|---|---|---|---|
| Proceso de Marco Legal | 21 | 07/01 | ~28/01 |
| Renta y Acondicionamiento del lugar de trabajo | 60 | 07/01 | ~08/03 |
| Selección de Proveedor | 30 | ~04/02 | ~06/03 |
| Compra De Maquinarias y Equipos | 40 | ~25/02 | ~06/04 |
| Selección y Contratación de Personal | 30 | ~19/03 | ~18/04 |
| Registro Planta y Aprobación del MAGFOR | 21 | ~25/03 | ~15/04 |
| Capacitación del Personal | 15 | ~22/04 | ~07/05 |
| Inicio de Operaciones | (sin número; barra de unos 60 días) | ~13/05 | ~mediados de julio (más allá del 06/06) |

### Página 12 — Objetivos de la programación

- Cumplir fechas de entrega
- Minimizar el trabajo en proceso (WIP).
- Minimizar el tiempo de flujo
- Garantizar alta utilización de la maquinaria
- Reducir demora por tiempos de alistamiento
- Minimizar costos de producción

### Página 13 — Definiciones básicas (parámetros)

- Todos los problemas de scheduling consideran:
  - N trabajos indexado en j
  - M máquinas indexado en i

1. $p_{ij}$: Tiempo de proceso del trabajo $j$ en la máquina $i$
2. $r_j$: Tiempo de disponibilidad (release) del trabajo $j$
3. $d_j$: Fecha de entrega del trabajo $j$
4. $w_j$: Prioridad del trabajo $j$

### Página 14 — Definiciones básicas (indicadores)

- Fecha de terminación (trabajo j): $C_j$
- Makespan: $C_{max}=\max(C_j)$
- Tiempo Flujo Promedio: $\sum (C_j-r_j)/n$ (número de trabajos)
- Retardo $L_j$ (trabajo $j$): $C_j-d_j$
- Tardanza $T_j$ (trabajo $j$): $\max(L_j,0)$
- Trabajo Tardío $U_j$ (trabajo $j$): $U_j\in\{0,1\}$. $U_j=1$ si $T_j>0$; 0 dlc.
- Tardanza Media: $\sum T_j/n$
- Tardanza Ponderada Total: $\sum w_jT_j$
- Total Trabajos Tardíos: $\sum U_j$
- Anticipo $=\max(-L_j,0)$

### Página 15 — Registros del MRP generan órdenes en planta

Dos registros MRP (periodos 0 a 5, tiempo de entrega $L=1$):

**Producto 1**

| Producto 1 | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Requerimientos Brutos |  | 50 | 60 | 40 | 60 | 40 |
| Recepciones Programadas |  |  |  |  |  |  |
| Inventario Proyectado | 70 | 20 | 40 | 0 | 40 | 0 |
| Colocación de órdenes |  | 80 |  | 100 |  |  |

L = 1

**Producto 2**

| Producto 2 | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Requerimientos Brutos |  | 30 | 30 | 30 | 40 | 30 |
| Recepciones Programadas |  |  |  |  |  |  |
| Inventario Proyectado | 30 | 0 | 30 | 0 | 30 | 0 |
| Colocación de órdenes |  | 60 |  | 70 |  |  |

L = 1

Tiempo de proceso:

| Producto | Fórmula | Factor | Unidad |
|---|---|---|---|
| producto 1 | tamaño lote x | 0.005 | semanas |
| producto 2 | tamaño lote x | 0.01 | semanas |

### Página 16 — Generación de órdenes

Se generan 4 órdenes de producción

| Orden | Producto | Disponibilidad | Tiempo proceso | Fecha de entrega |
|---|---|---|---|---|
| 0001 | 1 | 1 | 0.4 | 2 |
| 0002 | 2 | 1 | 0.6 | 2 |
| 0003 | 1 | 3 | 0.5 | 4 |
| 0004 | 2 | 3 | 0.7 | 4 |

> [Flecha desde el 0.4 de la orden 0001 hacia la nota:] tamaño de lote x 0.005 → $80\times0.005=0.4$ semanas

(Disponibilidad = periodo en que se coloca la orden en el MRP; fecha de entrega = disponibilidad + $L$. Los demás tiempos salen igual: $60\times0.01=0.6$; $100\times0.005=0.5$; $70\times0.01=0.7$.)

### Página 17 — Visualización Gantt

> [Diagrama: Gantt de una máquina sobre una rejilla; eje "t" en semanas con marcas 1, 1.5, 2, 2.5, 3, 3.5, 4 (cada celda = 0.1 semana). Bloques de colores: 0001 azul oscuro, 0002 naranja, un bloque azul claro sin rótulo, 0003 blanco, 0004 rojo.]

| Orden | Inicio (semana) | Fin = $C_j$ | Fecha de entrega $d_j$ | $L_j$ | $T_j$ |
|---|---|---|---|---|---|
| 0001 | 1.0 | 1.4 | 2 | −0.6 | 0 |
| 0002 | 1.4 | 2.0 | 2 | 0 | 0 |
| (bloque azul claro sin rótulo) | 2.0 | 2.2 | — | — | — |
| (máquina ociosa) | 2.2 | 3.0 | — | — | — |
| 0003 | 3.0 | 3.5 | 4 | −0.5 | 0 |
| 0004 | 3.5 | 4.2 | 4 | +0.2 | 0.2 |

\*\* ¿Qué ocurre?

(Lectura del Gantt: las órdenes 0003 y 0004 solo están disponibles en la semana 3, así que la máquina espera; la orden 0004 termina en 4.2 y llega 0.2 semanas tarde. Los valores $L_j$ y $T_j$ de la tabla se calcularon con los datos de la página 16; no están escritos en la diapositiva.)

### Página 18 — Clasificación de los problemas de Scheduling (Notación)

- Esta es la notación de Graham et al (1979)
  Tripleta: $\alpha\,|\,\beta\,|\,\gamma$

Donde:

- $\alpha$: ambiente de las máquinas (Framework)
- $\beta$: características del procesamiento (Restricciones)
- $\gamma$: objetivo a optimizar (Función Objetivo)

### Página 19 — Ambientes de las máquinas

Se debe saber:

- *Única máquina (1)*
- *Máquinas en paralelo (Pm):* Los trabajos pasan por alguna de las máquinas (son idénticas) requieren una única operación.
  - Si hay máquinas que no pueden realizar un trabajo, se especifica en el campo $\beta$.
- *Máquinas en paralelo con diferentes velocidades (Qm).* Cada velocidad es $v_i$. Tiempo de proceso $p_j/v_i$. También llamado maquinas uniformes.

### Página 20 — Ambientes de las máquinas

Se debe saber:

- *Máquinas no relacionadas en paralelo (Rm):* La velocidad de la máquina depende del trabajo a realizar. Entiéndase $v_{ij}$.
- *Flow shop (Fm):* m máquinas en serie. Cada trabajo tiene que pasar por cada una de las máquinas. Todos los trabajos siguen la misma ruta. Los trabajos esperan en cola de cada estación. FIFO.
  *También llamado permutation flow shop.* Poner en $\beta$ **prmu**

> [Diagrama: tres cajas M1 → M2 → M3 unidas por flechas (máquinas en serie).]

### Página 21 — Ambientes de las máquinas

Se debe saber:

- *Flow shop flexible (FFc):* sistema con c etapas, cada una con máquinas en paralelo idénticas. Los trabajos se procesan en cada etapa en el mismo orden. Cada trabajo sólo requiere un proceso por estación. Las estaciones pueden o no operar con la regla FIFO.
- *Job shop (Jm):* m máquinas. Cada trabajo tiene su propia ruta predeterminada. Poner en $\beta$ **recrc** cuando hay recirculación (se visita una máquina más de una vez).

### Página 22 — Ambientes de las máquinas

Se debe saber:

- *Job shop flexible (FJc):* sistema con c etapas, cada una con máquinas en paralelo idénticas. Cada trabajo tiene su propia ruta. Cada trabajo sólo requiere un proceso por estación. Puede haber recirculación.
- *Open shop (Om):* m máquinas. Cada trabajo debe pasar por todas las máquinas. Algunos tiempos de proceso son cero. No hay rutas predeterminadas y pueden variar entre trabajos.

### Página 23 — $\beta$: características del procesamiento

- Tiempos de liberación $r_j$. Si se omite, el trabajo puede iniciar en el tiempo cero. Los tiempos de entrega no se consideran en la notación (aparecen en la función objetivo).
- Tiempos de set-up dependientes de la secuencia ($s_{jk}$).
  - $s_{0k}$: Tiempo de inicio
  - $s_{j0}$: Tiempo de limpieza al final
  - $s_{ijk}$: Tiempos dependientes de la máquina
  - Si se omite, se suman al tiempo de proceso.

### Página 24 — $\beta$: características del procesamiento

- Preemptions (prmp): Se puede pausar la ejecución de una tarea, en una máquina, para hacer otro trabajo prioritario. El trabajo realizado no se pierde. Se puede cambiar de máquina. Interrupciones
- Restricciones de precedencia (*prec*): Uno o más trabajos se deben completar antes de iniciar otro.
  - Cadenas: Un trabajo sólo tiene máximo un sucesor y un predecesor.
  - Intree: los trabajos tienen máximo un sucesor.
  - outtree: los trabajos tienen máximo un predecesor.

### Página 25 — $\beta$: características del procesamiento

- Fallas (brkdwn): Las máquinas no están disponibles de forma continua.
- Restricciones de elección de máquina ($M_j$): $M_j$ es el conjunto de máquinas en paralelo que pueden procesar el trabajo $j$
- Permutaciones (*prmu*): Todas las máquinas tienen la misma secuencia de trabajos
- Bloqueo (*block*): En flow shops. Buffer limitado entre dos máquinas sucesivas. Un trabajo no puede continuar hacia la siguiente máquina a menos que ésta se encuentre vacía.

### Página 26 — $\beta$: características del procesamiento

- No-wait (*nwt*): Flow shops. Un trabajo una vez inicia su proceso, nunca espera en cola.
- Recirculación (*recrc*): En job shops. Un trabajo puede visitar varias veces la misma máquina.

### Página 27 — $\gamma$: Función Objetivo

- Tardanza Ponderada Total $\sum w_jT_j$
- Makespan
- Retardo Máximo
- Tiempo (ponderado) de Flujo Total
- Anticipo Ponderado Total (Earliness)

$$E_j=\max(0,\ d_j-C_j)$$

### Página 28 — $\gamma$: Función Objetivo

- Makespan ($C_{max}$)

$$C_{max}=\max\{C_1,C_2,\dots,C_N\}$$

- Al minimizar el makespan, usualmente se obtiene la máxima utilización en el sistema.

### Página 29 — $\gamma$: Función Objetivo

- Retraso máximo ($L_{max}$)

$$L_{max}=\max\{L_1,L_2,\dots,L_N\}$$

- Al minimizar el retraso máximo, se mide la peor violación de la fecha de entrega.

### Página 30 — $\gamma$: Función Objetivo

- Tiempo ponderado total de terminación

$$\sum w_jC_j$$

- Costo total de almacenamiento de inventario por la programación
- También llamado *weighted Flow time.*

### Página 31 — $\gamma$: Función Objetivo

- Tiempo ponderado descontado total de terminación

$$\sum w_j\left(1-e^{-rC_j}\right)$$

- Costo de terminación marginal decreciente. R es un valor de descuento 10%

### Página 32 — Ejemplos

- $FFc\,|\,r_j\,|\,\sum w_jT_j$

### Página 33 — Ejemplos

- $FFc\,|\,r_j\,|\,\sum w_jT_j$

Flexible flow shop con trabajos que tienen fecha de liberación r(j) y se busca la minimización de la tardanza ponderada.

E.g.: Fábrica de papel.

### Página 34 — Ejemplos

- $Pm\,|\,r_j,M_j\,|\,\sum w_jT_j$

### Página 35 — Ejemplos

- $Pm\,|\,r_j,M_j\,|\,\sum w_jT_j$

Sistema con m maquinas en paralelo. Hay fechas de liberación de trabajos y fechas de entrega. El trabajo j se realiza solamente en el conjunto de máquinas Mj.

Ejemplo: asignación de puertas en aeropuerto.

### Página 36 — Ejemplos

- $P\infty\,|\,prec\,|\,C_{max}$

N trabajos con restricciones de precedencia y máquinas ilimitadas en paralelo. Minimización del makespan. Ejemplo: un proyecto.

### Página 37 — Tipos de programación

- Secuencia
- Programación
- Política de programación

### Página 38 — Tipos de programación

- Secuencia: permutación de trabajos en una máquina.
- Programación: incluye la asignación de trabajos a máquinas con o sin preemption.
- Política de programación: describe las acciones a tomar en ciertos estados del sistema (*stochastic scheduling*)

### Página 39 — Programación sin retrasos

- Ninguna máquina se deja sin utilizar cuando hay trabajos esperando.
- Es equivalente a prohibir tiempos muertos no forzosos.
- Condición de optimalidad!

### Página 40 — Casos particulares

Considere el siguiente $P2\,|\,prec\,|\,C_{max}$

| trabajo | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Pj | 8 | 7 | 7 | 2 | 3 | 2 | 2 | 8 | 8 | 15 |

Restricciones de Precedencia:

> [Diagrama: red de precedencias con 10 nodos (círculos) y flechas.]

| Arco (predecesor → sucesor) |
|---|
| 1 → 2 |
| 1 → 3 |
| 2 → 10 |
| 3 → 10 |
| 4 → 5 |
| 4 → 6 |
| 5 → 3 |
| 5 → 8 |
| 5 → 9 |
| 6 → 7 |
| 7 → 8 |
| 7 → 9 |

Predecesores de cada trabajo: 2 ← {1}; 3 ← {1, 5}; 5 ← {4}; 6 ← {4}; 7 ← {6}; 8 ← {5, 7}; 9 ← {5, 7}; 10 ← {2, 3}; 1 y 4 no tienen predecesores.

### Página 41 — Solución Optima

> [Diagrama: Gantt de 2 máquinas (M1, M2), eje "tiempo" de 1 a 31.]

| Máquina | Trabajo | Inicio | Fin |
|---|---|---|---|
| M1 | 1 | 0 | 8 |
| M1 | 2 | 8 | 15 |
| M1 | 8 | 15 | 23 |
| M1 | 9 | 23 | 31 |
| M2 | 4 | 0 | 2 |
| M2 | 6 | 2 | 4 |
| M2 | 5 | 4 | 7 |
| M2 | 7 | 7 | 9 |
| M2 | 3 | 9 | 16 |
| M2 | 10 | 16 | 31 |

$C_{max}=31$. Ninguna máquina queda ociosa.

### Página 42 — ¿Qué pasa si reducimos los tiempos de proceso en una unidad?

- Sistema sin esperas!

> [Diagrama: Gantt de 2 máquinas, eje "tiempo" de 1 a 32. Todos los tiempos de proceso son $p_j-1$: 7, 6, 6, 1, 2, 1, 1, 7, 7, 14.]

| Máquina | Trabajo | Inicio | Fin |
|---|---|---|---|
| M1 | 1 | 0 | 7 |
| M1 | 2 | 7 | 13 |
| M1 | 9 | 13 | 20 |
| M1 | (ociosa) | 20 | 32 |
| M2 | 4 | 0 | 1 |
| M2 | 6 | 1 | 2 |
| M2 | 5 | 2 | 4 |
| M2 | 7 | 4 | 5 |
| M2 | 8 | 5 | 12 |
| M2 | 3 | 12 | 18 |
| M2 | 10 | 18 | 32 |

- En contra de la intuición, el makespan aumentó! ($C_{max}=32>31$)

### Página 43 — ¿Qué pasa si usamos 3 máquinas?

> [Diagrama: Gantt de 3 máquinas (M1, M2, M3), eje "tiempo" de 1 a 36, con los tiempos originales. En M2 hay una celda amarilla vacía entre 5 y 6 (tiempo muerto).]

| Máquina | Trabajo | Inicio | Fin |
|---|---|---|---|
| M1 | 1 | 0 | 8 |
| M1 | 2 | 8 | 15 |
| M1 | (ociosa) | 15 | 36 |
| M2 | 4 | 0 | 2 |
| M2 | 5 | 2 | 5 |
| M2 | (ociosa, celda amarilla) | 5 | 6 |
| M2 | 8 | 6 | 14 |
| M2 | 3 | 14 | 21 |
| M2 | 10 | 21 | 36 |
| M3 | (ociosa) | 0 | 2 |
| M3 | 6 | 2 | 4 |
| M3 | 7 | 4 | 6 |
| M3 | 9 | 6 | 15 (así se dibuja; con $p_9=8$ terminaría en 14) |

$C_{max}=36$: con una máquina más, el makespan empeora (de 31 a 36).

### Página 44 — Active Schedule

- Es una programación factible, para la cual no es posible construir otra programación cambiando el orden y tener una operación que termine más pronto y otra operación que termina más tarde.
- Ninguna operación puede ponerse en un hueco más temprano, manteniendo factibilidad.

### Página 45 — Jerarquía de complejidad

- Cuando un algoritmo puede ser usado para resolver otros problemas:
- Ejemplo:
  - $1||\sum C_j$ es un caso especial de $1||\sum w_jC_j$

$$1||\sum C_j\ \propto\ 1||\sum w_jC_j$$

### Página 46 — Jerarquía de complejidad

$$1||\sum C_j\ \propto\ 1||\sum w_jC_j\ \propto\ Pm||\sum w_jC_j\ \propto\ Qm|prec|\sum w_jC_j$$

Estos problemas se conocen como NP-Hard

$1||\sum w_jC_j$ se resuelve en tiempo polinomial.

El número de secuencias posibles para una máquina es n!

### Página 47 — Problemática de la programación de la producción en la vida real

- Los ambientes reales son muy difíciles de modelar
- Hay innumerables reglas implícitas de programación en las industrias
- Las fechas de entrega y las prioridades son variables (no son "hard constraints").
- Las funciones objetivo industriales no corresponden a las clásicas usadas en programación de producción

### Página 48 — Siemens Preactor Software

- https://www.youtube.com/watch?v=klL9IctdADg

> [Imagen decorativa: foto de una persona frente a un monitor con un diagrama de Gantt de colores del software Preactor.]

### Página 49 — ¡Gracias!

Diapositiva de cierre: **¡Gracias!**

## Anexo: texto extraído automáticamente del PDF

> Texto plano tal como sale del PDF, sin fórmulas ni tablas que estén como imagen. La versión fiel y completa es la sección «Contenido completo» de arriba.

### Página 1 · 2 imagen(es)

Programación de la 
Producción

### Página 2 · 1 imagen(es)

Actividades recomendadas
• Lectura:
– Shaikh, N., Prabhu, V., Abril, D., Sánchez, D., Arias, 
J., Rodríguez, E., & Riaño, G. (2011). Kimberly-Clark 
Latin America builds an optimization-based system for 
machine scheduling. Interfaces, 41(5), 455-465.
– CAP. 19. Pinedo, M. L. (2016). Scheduling: 
theory, algorithms, and systems. Springer.

### Página 3 · 1 imagen(es)

Flujo de información en una 
empresa
•Pronóstico de 
la demanda
•Cantidades y 
fechas
Planeación de 
la Producción
•Ordenes de 
compra
•Liberación de 
ordenes
MRP (CRP)
•Programa de 
producción
Scheduling and 
Rescheduling
Dispatching
•Recolección de 
información
Shopfloor 
management
•Ejecución de 
tareas
Shopfloor

### Página 4 · 2 imagen(es)

Jerarquía de la Planeación de 
Producción

### Página 5 · 1 imagen(es)

Aplicaciones de programación
• Programación de Proyectos 
• Programación de Operarios 
• Programación de Tripulaciones 
• Programación de Producción 
• Este curso se concentra en programación 
de producción.

### Página 6 · 1 imagen(es)

Machine Scheduling
• Programar la secuencia de las 
operaciones
• Sistemas de manufactura
• Ambientes de procesamiento de 
información
• Sistemas de prestación de servicios: 
asignación de puertas en un aeropuerto.

### Página 7 · 1 imagen(es)

Ejemplo
• Haga la secuenciación de estos dos trabajos:
– Respetando la secuencia M1 – M2
p11 = 8
p12 = 5
p21 = 7
p22 = 10

### Página 8 · 1 imagen(es)

Ejemplo
• Haga la secuenciación de estos dos trabajos:
– Respetando la secuencia M1 – M2
Programando A-B: Cmax = 25
Tiempo de 
proceso
M1
M2
Job A
8
5
Job B
7
10
M1
M2
tiempo
1
2
3
4
5
6
7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
A
B
A
B

### Página 9 · 1 imagen(es)

Ejemplo
• Haga la secuenciación de estos dos trabajos:
– Respetando la secuencia M1 – M2
Programando B-A: Cmax = 22
Tiempo de 
proceso
M1
M2
Job A
8
5
Job B
7
10
M1
M2
tiempo
1
2
3
4
5
6
7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
A
B
A
B

### Página 10 · 1 imagen(es)

Tipos de modelos de scheduling
• Determinísticos
– Una máquina
– Máquinas en paralelo
– Flow shops y flexible flow shops
– Job shops
– Open shops
• Estocásticos (llegadas de trabajos, tiempos de procesamiento, etc.)
– No en este curso

### Página 11 · 2 imagen(es)

Elementos de la programación de producción
• Trabajos
– Disponibilidad 
– Fecha de entrega
– Tiempo de proceso
– Prioridad
– Tiempo de alistamiento (setup)
– Ruta de proceso 
• Máquinas
– Configuración 
– Capacidad

### Página 12 · 1 imagen(es)

Objetivos de la programación
• Cumplir fechas de entrega 
• Minimizar el trabajo en proceso (WIP). 
• Minimizar el tiempo de flujo 
• Garantizar alta utilización de la maquinaria 
• Reducir demora por tiempos de alistamiento 
• Minimizar costos de producción

### Página 13 · 1 imagen(es)

Definiciones básicas (parámetros)
• Todos los problemas de scheduling consideran:
– N trabajos indexado en j 
– M máquinas indexado en i
1. pij: Tiempo de proceso del trabajo j en la máquina i 
2. rj: Tiempo de disponibilidad (release) del trabajo j 
3. dj: Fecha de entrega del trabajo j 
4. wj: Prioridad del trabajo j

### Página 14 · 1 imagen(es)

Definiciones básicas (indicadores)
• Fecha de terminación (trabajo j): Cj 
• Makespan: Cmax = Max (Cj) 
• Tiempo Flujo Promedio: ∑(Cj - rj) / n (número de trabajos) 
• Retardo Lj (trabajo j): Cj - dj 
• Tardanza Tj (trabajo j): Max (Lj, 0) 
• Trabajo Tardío Uj (trabajo j): Uj 𝜖 {0,1}. Uj = 1 si Tj >0; 0 dlc. 
• Tardanza Media: ∑ Tj / n 
• Tardanza Ponderada Total: ∑ wjTj 
• Total Trabajos Tardíos: ∑ Uj 
• Anticipo = Max (-Lj, 0)

### Página 15 · 2 imagen(es)

Registros del MRP generan órdenes en 
planta

### Página 16 · 3 imagen(es)

Generación de órdenes

### Página 17 · 2 imagen(es)

Visualización Gantt
** ¿Qué ocurre?

### Página 18 · 1 imagen(es)

Clasificación de los problemas de 
Scheduling (Notación)
• Esta es la notación de Graham et al (1979) 
Tripleta: 𝛼 𝛽 𝛾
Donde :
• 𝛼: ambiente de las máquinas (Framework)
• 𝛽: características del procesamiento 
(Restricciones)
• 𝛾: objetivo a optimizar (Función Objetivo)

### Página 19 · 1 imagen(es)

Ambientes de las máquinas
Se debe saber:
• Única máquina (1) 
• Máquinas en paralelo (Pm): Los trabajos pasan por 
alguna de las máquinas (son idénticas) requieren una 
única operación. 
– Si hay máquinas que no pueden realizar un trabajo, se 
especifica en el campo 𝛽.
• Máquinas en paralelo con diferentes velocidades (Qm). 
Cada velocidad es vi. Tiempo de proceso pj/vi. También 
llamado maquinas uniformes.

### Página 20 · 1 imagen(es)

Ambientes de las máquinas
Se debe saber:
•
Máquinas no relacionadas en paralelo (Rm): La velocidad de la 
máquina depende del trabajo a realizar. Entiéndase 𝑣𝑖𝑗.
•
Flow shop (Fm): m máquinas en serie. Cada trabajo tiene que pasar 
por cada una de las máquinas. Todos los trabajos siguen la misma 
ruta. Los trabajos esperan en cola de cada estación. FIFO. 
También llamado permutation flow shop. Poner en 𝛽 prmu
M1
M2
M3

### Página 21 · 1 imagen(es)

Ambientes de las máquinas
Se debe saber:
•
Flow shop flexible (FFc): sistema con c etapas, cada una con 
máquinas en paralelo idénticas. Los trabajos se procesan en cada 
etapa en el mismo orden. Cada trabajo sólo requiere un proceso por 
estación. Las estaciones pueden o no operar con la regla FIFO. 
•
Job shop (Jm): m máquinas. Cada trabajo tiene su propia ruta 
predeterminada. Poner en 𝛽 recrc cuando hay recirculación (se 
visita una máquina más de una vez).

### Página 22 · 1 imagen(es)

Ambientes de las máquinas
Se debe saber:
•
Job shop flexible (FJc): sistema con c etapas, cada una con 
máquinas en paralelo idénticas. Cada trabajo tiene su propia ruta. 
Cada trabajo sólo requiere un proceso por estación. Puede haber 
recirculación.
•
Open shop (Om): m máquinas. Cada trabajo debe pasar por todas 
las máquinas. Algunos tiempos de proceso son cero. No hay rutas 
predeterminadas y pueden variar entre trabajos.

### Página 23 · 1 imagen(es)

𝛽: características del procesamiento
• Tiempos de liberación 𝑟𝑗. Si se omite, el trabajo puede 
iniciar en el tiempo cero. Los tiempos de entrega no se 
consideran en la notación (aparecen en la función 
objetivo).
• Tiempos de set-up dependientes de la secuencia (𝑠𝑗𝑘).
– 𝑠0𝑘: Tiempo de inicio
– 𝑠𝑗0: Tiempo de limpieza al final
– 𝑠𝑗𝑖𝑘: Tiempos dependientes de la máquina
– Si se omite, se suman al tiempo de proceso.

### Página 24 · 1 imagen(es)

𝛽: características del 
procesamiento
• Preemptions (prmp): Se puede pausar la ejecución de 
una tarea, en una máquina, para hacer otro trabajo 
prioritario. El trabajo realizado no se pierde. Se puede 
cambiar de máquina. Interrupciones
• Restricciones de precedencia (prec): Uno o más trabajos 
se deben completar antes de iniciar otro. 
– Cadenas: Un trabajo sólo tiene máximo un sucesor y un 
predecesor.
– Intree: los trabajos tienen máximo un sucesor.
– outtree: los trabajos tienen máximo un predecesor.

### Página 25 · 1 imagen(es)

• Fallas (brkdwn): Las máquinas no están disponibles de 
forma continua. 
• Restricciones de elección de máquina (Mj): Mj es el 
conjunto de máquinas en paralelo que pueden procesar 
el trabajo j 
• Permutaciones (prmu): Todas las máquinas tienen la 
misma secuencia de trabajos 
• Bloqueo (block): En flow shops. Buffer limitado entre dos 
máquinas sucesivas. Un trabajo no puede continuar 
hacia la siguiente máquina a menos que ésta se 
encuentre vacía. 
𝛽: características del procesamiento

### Página 26 · 1 imagen(es)

• No-wait (nwt): Flow shops. Un trabajo una vez inicia su 
proceso, nunca espera en cola. 
• Recirculación (recrc): En job shops. Un trabajo puede 
visitar varias veces la misma máquina. 
𝛽: características del procesamiento

### Página 27 · 1 imagen(es)

𝛾: Función Objetivo
– Tardanza Ponderada Total ∑𝑤𝑗𝑇𝑗
– Makespan
– Retardo Máximo
– Tiempo (ponderado) de Flujo Total
– Anticipo Ponderado Total (Earliness)
 𝐸𝑗= max(0, 𝑑𝑗−𝐶𝑗)

### Página 28 · 1 imagen(es)

• Makespan (𝐶𝑚𝑎𝑥)
𝐶𝑚𝑎𝑥= max{𝐶1, 𝐶2, … , 𝐶𝑁}
• Al minimizar el makespan, usualmente se 
obtiene la máxima utilización en el 
sistema.
𝛾: Función Objetivo

### Página 29 · 1 imagen(es)

• Retraso máximo (𝐿𝑚𝑎𝑥)
𝐿𝑚𝑎𝑥= max{𝐿1, 𝐿2, … , 𝐿𝑁}
• Al minimizar el retraso máximo, se mide la 
peor violación de la fecha de entrega.
𝛾: Función Objetivo

### Página 30 · 1 imagen(es)

• Tiempo ponderado total de terminación 
෍𝑤𝑗𝐶𝑗
• Costo total de almacenamiento de 
inventario por la programación
• También llamado weighted Flow time.
𝛾: Función Objetivo

### Página 31 · 1 imagen(es)

• Tiempo ponderado descontado total de 
terminación 
෍𝑤𝑗(1 −𝑒−𝑟𝐶𝑗)
• Costo de terminación marginal decreciente. 
R es un valor de descuento 10%
𝛾: Función Objetivo

### Página 32 · 1 imagen(es)

Ejemplos
• 𝐹𝐹𝑐 𝑟𝑗 ∑𝑤𝑗𝑇𝑗

### Página 33 · 1 imagen(es)

Ejemplos
• 𝐹𝐹𝑐 𝑟𝑗 ∑𝑤𝑗𝑇𝑗
Flexible flow shop con trabajos que tienen 
fecha de liberación r(j) y se busca la 
minimización de la tardanza ponderada.
E.g.: Fábrica de papel.

### Página 34 · 1 imagen(es)

Ejemplos
• 𝑃𝑚 𝑟𝑗, 𝑀𝑗 ∑𝑤𝑗𝑇𝑗

### Página 35 · 1 imagen(es)

Ejemplos
• 𝑃𝑚 𝑟𝑗, 𝑀𝑗 ∑𝑤𝑗𝑇𝑗
Sistema con m maquinas en paralelo. Hay 
fechas de liberación de trabajos y fechas de 
entrega. El trabajo j se realiza solamente en 
el conjunto de máquinas Mj.
Ejemplo: asignación de puertas en aeropuerto.

### Página 36 · 1 imagen(es)

Ejemplos
• 𝑃∞ 𝑝𝑟𝑒𝑐 𝐶𝑚𝑎𝑥
N trabajos con restricciones de precedencia 
y máquinas ilimitadas en paralelo. 
Minimización del makespan. Ejemplo: un 
proyecto.

### Página 37 · 1 imagen(es)

Tipos de programación
• Secuencia
• Programación
• Política de programación

### Página 38 · 1 imagen(es)

Tipos de programación
• Secuencia: permutación de trabajos en 
una máquina.
• Programación: incluye la asignación de 
trabajos a máquinas con o sin preemption.
• Política de programación: describe las 
acciones a tomar en ciertos estados del 
sistema (stochastic scheduling)

### Página 39 · 1 imagen(es)

Programación sin retrasos
• Ninguna máquina se deja sin utilizar 
cuando hay trabajos esperando.
• Es equivalente a prohibir tiempos muertos 
no forzosos. 
• Condición de optimalidad!

### Página 40 · 1 imagen(es)

Casos particulares
Considere el siguiente 𝑃2 𝑝𝑟𝑒𝑐𝐶𝑚𝑎𝑥
Restricciones de 
Precedencia:
trabajo
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
Pj
8
7
7
2
3
2
2
8
8
15
4
5
6
7
9
8
3
1
10
2

### Página 41 · 1 imagen(es)

Solución Optima
1
2
3
4
5
6
7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
10
M1: 
M2:
1
2
8
9
tiempo
4
6
5
7
3

### Página 42 · 1 imagen(es)

¿Qué pasa si reducimos los tiempos de 
proceso en una unidad?
• Sistema sin esperas!
• En contra de la intuición, el makespan 
aumentó!
4
6
7
1
2
3
4
5
6
7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32
8
3
10
M1: 
M2:
tiempo
1
2
9
5

### Página 43 · 1 imagen(es)

¿Qué pasa si usamos 3 
máquinas?
1
2
3
4
5
6
7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
5
8
3
10
9
7
6
M1: 
M2:
tiempo
M3:
1
2
4

### Página 44 · 1 imagen(es)

Active Schedule
• Es una programación factible, para la cual 
no es posible construir otra programación 
cambiando el orden y tener una operación 
que termine más pronto y otra operación 
que termina más tarde. 
• Ninguna operación puede ponerse en un 
hueco más temprano, manteniendo 
factibilidad.

### Página 45 · 1 imagen(es)

Jerarquía de complejidad
• Cuando un algoritmo puede ser usado 
para resolver otros problemas:
• Ejemplo:
– 1|| ∑𝐶𝑗 es un caso especial de 1|| ∑𝑤𝑗𝐶𝑗
1|| ෍𝐶𝑗 ∝1|| ෍𝑤𝑗𝐶𝑗

### Página 46 · 1 imagen(es)

Jerarquía de complejidad
1|| ෍𝐶𝑗 ∝1|| ෍𝑤𝑗𝐶𝑗∝𝑃𝑚|| ෍𝑤𝑗𝐶𝑗∝𝑄𝑚|𝑝𝑟𝑒𝑐| ෍𝑤𝑗𝐶𝑗
Estos problemas se conocen como NP-Hard
1|| ∑𝑤𝑗𝐶𝑗 se resuelve en tiempo polinomial. 
El número de secuencias posibles para una máquina es n!

### Página 47 · 1 imagen(es)

Problemática de la programación 
de la producción en la vida real
• Los ambientes reales son muy difíciles de modelar 
• Hay innumerables reglas implícitas de programación 
en las industrias 
• Las fechas de entrega y las prioridades son variables 
(no son “hard constraints”). 
• Las funciones objetivo industriales no corresponden a 
las clásicas usadas en programación de producción

### Página 48 · 1 imagen(es)

Siemens Preactor Software
• https://www.youtube.com/watch?v=klL9Ict
dADg

### Página 49 · 1 imagen(es)

¡Gracias!

