# reto-2-monstruopolis

> **Archivo:** [`reto-2-monstruopolis.pdf`](./reto-2-monstruopolis.pdf) · **Corte 3** · 3 páginas  
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
- **Salida:** la asignación y secuencia por máquina, $C_j$ de cada trabajo y $\sum w_jT_j$. El ejemplo `secuencia.json` usa una lista de `{"job","machine","start","end"}`, el mismo formato del [instructivo](./instructivo-competencia-scheduling.md).

**Fórmulas y métodos**

$$\min\ \sum_{j=1}^{n}w_jT_j,\qquad T_j=\max\{0,\;C_j-d_j\},\qquad C_j=S_j+p_j$$

Restricciones, con $S_j$ el inicio de $j$ y $\mu(j)$ su máquina:

- $S_j\ge r_j$;
- $S_j\ge C_i$ para todo $i\to j$;
- si dos trabajos van en la misma máquina, $\mu(i)=\mu(j)$, sus intervalos $[S_i,C_i)$ y $[S_j,C_j)$ no se solapan.

**Interpretación de $d_j$ (deducida).** El «tiempo mínimo teórico de finalización» se entiende como el fin más temprano posible ignorando la capacidad:

$$d_j=\max\!\left(r_j,\ \max_{i\to j}d_i\right)+p_j$$

Con esa definición, $C_j\ge d_j$ siempre, así que $T_j=C_j-d_j$. Minimizar $\sum w_jT_j$ equivale entonces a minimizar $\sum w_jC_j$ (la constante $\sum w_jd_j$ no cambia la solución). Por eso la regla WSPT ($w_j/p_j$ decreciente) es la referencia natural. Esta interpretación es la del generador local de la solución, [solucion/pruebas/generador.py](../solucion/pruebas/generador.py).

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

- Reglas generales: [instructivo-competencia-scheduling.md](./instructivo-competencia-scheduling.md).
- Plantilla del profesor: [plantilla-reto-2-monstruopolis/reto_schedulling.py](./plantilla-reto-2-monstruopolis/reto_schedulling.py), explicada en el [README del proyecto](../README.md).
- Instancia de ejemplo en el formato de filas de este enunciado: [solucion/pruebas/data_ejemplo_reto2.json](../solucion/pruebas/data_ejemplo_reto2.json).
- Teoría:
  - [L18 Máquinas paralelas](../../03-maquinas-paralelas/L18-parallel-machine-scheduling.md);
  - [lns-maquinas-paralelas](../../03-maquinas-paralelas/lns-maquinas-paralelas.md);
  - [L17 Una máquina](../../02-una-maquina/L17-single-machine-scheduling.md), con WSPT, EDD y ATC;
  - [atc.py](../../02-una-maquina/atc.py).

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

## Anexo: texto extraído automáticamente del PDF

> Texto plano tal como sale del PDF, sin fórmulas ni tablas que estén como imagen. La versión fiel y completa es la sección «Contenido completo» de arriba.

### Página 1 · 1 imagen(es)

Proyecto Final – Scheduling de Producción: “La Fábrica de Juguetes de 
Monstruópolis” 
𝑷𝟑 ∣ 𝒓𝒋, 𝒑𝒓𝒆𝒄 ∣ ∑𝑾𝒋𝑻𝒋 
1. Contexto del Problema 
La historia se desarrolla en Monstruópolis, la ciudad de la película Monsters Inc... Tras la transición 
de usar gritos a usar risas como fuente de energía, la compañía Monsters Inc. diversificó sus 
operaciones y creó una fábrica de juguetes que produce artículos basados en los personajes de las 
películas más populares de Disney-Pixar: Toy Story, Cars, Finding Nemo, Inside Out y Monsters 
University. 
La fábrica cuenta con tres máquinas idénticas en paralelo (M1, M2, M3) que trabajan de forma 
continua durante el turno diurno. Cada juguete (trabajo) requiere un solo proceso de fabricación, 
pero no todas las máquinas están disponibles al mismo tiempo, ya que cada una requiere 
calibraciones y mantenimientos periódicos. 
El gerente de planta, Mike Wazowski, debe decidir en qué máquina y en qué orden se procesarán 
los pedidos del día, de forma que se cumplan las prioridades, fechas de liberación y restricciones de 
precedencia, minimizando la tardanza ponderada total de los trabajos. 
2. Datos del Reto 
• 
Número de máquinas (m): 3 (idénticas en capacidad y velocidad) 
• 
Número de trabajos (n): 50 juguetes (J1–J50) 
• 
Tiempos de procesamiento 𝑝𝑗 : Valores enteros generados aleatoriamente entre 10 y 100 
minutos. 
• 
Fechas de liberación 𝑟𝑗(momento en que cada pedido está disponible para producción): 
Valores enteros aleatorios entre 0 y 30 minutos desde el inicio del turno. 
• 
Fechas de entrega dj Se asignan como el tiempo mínimo teórico de finalización del 
trabajo. 
• 
Prioridades 𝑤𝑗(peso o importancia del pedido): Valores enteros aleatorios entre 1 y 5, que 
indican la importancia relativa de cada pedido en el objetivo ponderado. 
• 
Precedencias: 
Generadas aleatoriamente. Algunos juguetes comparten piezas o moldes: 
Se define un conjunto de relaciones (i → j) donde el trabajo j no puede comenzar hasta que el 
trabajo i haya terminado.

### Página 2 · 1 imagen(es)

El porcentaje de trabajos con precedencias puede ser del 10 % del total, es decir, aproximadamente 5 
precedencias por instancia. 
Se garantiza que las precedencias no formen ciclos (es decir, que sean válidas). 
Restricciones adicionales: 
o 
No hay tiempos de setup adicionales. o Cada máquina puede procesar un trabajo a 
la vez. 
o 
No se permite preemption (una vez iniciado un trabajo, debe finalizar). 
o 
Las precedencias entre trabajos deben respetarse estrictamente: un trabajo sucesor 
solo puede comenzar cuando todos sus predecesores hayan finalizado. 
o 
Los trabajos se asignan a una de las tres máquinas idénticas, las cuales operan de 
forma continua durante el turno diurno. 
3. Objetivo de Optimización 
Minimizar la tardanza ponderada total: 
𝒏 
𝐦𝐢 𝐧 ∑ 
𝒘𝒋 𝑻𝒋, 𝑻𝒋 = 𝐦𝐚𝐱 {𝟎, 𝑪𝒋 − 𝒅𝒋}, 
𝒋=𝟏 
donde 𝑪𝒋es el tiempo de finalización de 𝑱𝒋 
El objetivo es minimizar la tardanza ponderada total , 
Esto garantiza que los trabajos con mayor prioridad presenten los menores retrasos posibles, 
respetando las fechas de liberación y las restricciones de precedencia establecidas. 
4. Formatos de entrada y salida: 
Entrada: 
 Archivos .json con 50 filas (una por trabajo) y las siguientes columnas: 
Trabajo, p_j, r_j, d_j, w_j, Predecesores 
Salida esperada: 
• 
Secuencia de asignación de trabajos a las tres máquinas 
• 
Tiempo de finalización de cada trabajo Cj

### Página 3 · 2 imagen(es)

• 
Valor total del objetivo ∑wjTj 
Ejemplo de entrada de la secuencia para una instancia (.json): 
Este reto fue diseñado por : Nicolás Ospina, Santiago Tapia, Daniela Arizmendi y Melina Kaihara

