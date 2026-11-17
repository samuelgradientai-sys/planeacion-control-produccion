<!-- fuente: corte-3-programacion-scheduling/02-una-maquina/README.md -->
# Programación de una máquina (Corte 3)

## Qué cubre

Secuenciación de $n$ trabajos en una sola máquina ($1|\beta|\gamma$). Incluye las reglas de despacho estáticas (FIFO, SPT, EDD, WSPT) y dinámicas (holgura mínima MS, ATC, razón crítica CR), los casos con regla óptima conocida (WSPT para $\sum w_jC_j$, EDD para $L_{max}$), las precedencias en cadena con factor $\rho$, la *preemption* con liberaciones, el algoritmo de Lawler ($h_{max}$), el de Moore-Hodgson ($\sum U_j$) y el uso de Solver de Excel como método aproximado.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [L17-single-machine-scheduling.md](/corte-3-programacion-scheduling/02-una-maquina/L17-single-machine-scheduling.md) (gemelo del PDF) | Presentación "Lec 17 - Single Machine Scheduling", 49 diapositivas, con todas las secuencias y Gantt en tablas y un resumen con la comparación de reglas | **Sí (1.º)** |
| [ejemplo-1-programacion-produccion.md](/corte-3-programacion-scheduling/02-una-maquina/ejemplo-1-programacion-produccion.md) (gemelo del .xlsx) | Ejemplo cotidiano de 4 actividades con $r_j$, $p_j$, $w_j$ y $s_j$: $C_j$, flujo y $w_jC_j$ | 2.º (corto) |
| [programacion-produccion-una-maquina.md](/corte-3-programacion-scheduling/02-una-maquina/programacion-produccion-una-maquina.md) (gemelo del .xlsx) | Libro de clase con 3 hojas: reglas de despacho sobre 6 trabajos (natural, azar, SPT, WSPT, EDD, MS), cadenas y factor $\rho$, preemption (ejercicio p. 25 de L17) y una hoja para Solver | 3.º |
| [programacion-produccion-una-maquina-datos/Reglas_de_Despacho.csv](/corte-3-programacion-scheduling/02-una-maquina/programacion-produccion-una-maquina-datos/Reglas_de_Despacho.csv) | Volcado CSV completo de la hoja `Reglas de Despacho` | Solo como referencia |
| [atc.py](/corte-3-programacion-scheduling/02-una-maquina/atc.py) | Script de Python (sin gemelo) que aplica la regla ATC al ejercicio de L17 (pp. 43-45) y verifica la solución de clase. Se explica abajo | 4.º |

## `atc.py`: regla ATC (Apparent Tardiness Cost)

**Qué hace.** Construye la secuencia ATC del ejercicio de L17 (pp. 43-45), calcula $C_j$, $L_j$ y $w_jT_j$ y las medidas de desempeño, y las compara con la solución de la diapositiva 45. Solo usa la biblioteca estándar (`argparse`, `math`).

**Entradas** (fijas en el código, diccionario `TRABAJOS`):

| Trabajo | $p_j$ | $d_j$ | $w_j$ |
|---|---|---|---|
| 1 | 5 | 1 | 2 |
| 2 | 7 | 9 | 3 |
| 3 | 2 | 10 | 2 |
| 4 | 8 | 6 | 1 |

Opciones de línea de comandos:

- `--K <valor>`: constante $K$ (por defecto 1).
- `--pbar-fijo`: usa $\bar p$ de todos los trabajos (5.5) en vez de recalcularlo con los pendientes.

`ESPERADO` guarda la solución de clase: secuencia 1-3-2-4, flujo promedio 12, retardo máximo 16 y tardanza ponderada 39.

**Algoritmo** (heurística constructiva voraz):

1. $t=0$ y todos los trabajos pendientes. No hay liberaciones: todos están disponibles desde 0.
2. Se calcula $\bar p$ = promedio de $p_j$ de los pendientes, o el de todos con `--pbar-fijo`.
3. Para cada pendiente, `indice_atc` calcula

   $$I_j(t)=\frac{w_j}{p_j}\exp\!\left(-\frac{\max(d_j-p_j-t,\,0)}{K\,\bar p}\right)$$

   donde $\max(d_j-p_j-t,0)$ es la holgura del trabajo.
4. Se elige el de mayor $I_j(t)$; si hay empate, el de menor número. Se agrega a la secuencia y $t \leftarrow t+p_j$.
5. Se repite hasta programar todos.
6. `evaluar` recorre la secuencia y calcula $C_j$ (suma acumulada de $p$), $L_j=C_j-d_j$, $T_j=\max(L_j,0)$ y $w_jT_j$. Devuelve el flujo promedio $\sum C_j/n$, el flujo ponderado $\sum w_jC_j$, $L_{max}$ y $\sum w_jT_j$.
7. `imprimir_iteraciones` y `imprimir_tabla` muestran el detalle; `verificar` compara con `ESPERADO`.

**Resultado.** Corre sin instalar nada. Salida real de `python -I atc.py` (modo por defecto, $K=1$, $\bar p$ recalculado):

```
Regla ATC  |  K = 1.0  |  p_barra = trabajos no programados

Indices ATC en cada decision (* = trabajo elegido)
   t  p_barra |     I(1)     I(2)     I(3)     I(4)
----------------------------------------------------
   0    5.500 |  0.4000*  0.2979   0.2335   0.1250 
   5    5.667 |        -  0.4286   0.5890*  0.1250 
   7    7.500 |        -  0.4286*        -  0.1250 
  14    8.000 |        -        -        -  0.1250*

Programa ATC
Secuencia         1     3     2     4
pj                5     2     7     8
Cj                5     7    14    22
dj                1    10     9     6
Lj = Cj - dj      4    -3     5    16
wj                2     2     3     1
wjTj              8     0    15    16

Secuencia ATC: 1 -> 3 -> 2 -> 4
Flujo promedio          = 12
Flujo ponderado (wjCj)  = 88
Retardo maximo (Lmax)   = 16
Tardanza ponderada      = 39

Comparacion con la diapositiva 45
  Secuencia            obtenido = [1, 3, 2, 4]   esperado = [1, 3, 2, 4]   OK
  Flujo promedio       obtenido = 12.0           esperado = 12             OK
  Retardo max          obtenido = 16             esperado = 16             OK
  Tardanza ponderada   obtenido = 39             esperado = 39             OK
  Resultado: coincide con la solucion de clase
```

Comparación de modos (salidas reales):

| Modo | $\bar p$ en $t$ = 0, 5, 7, 14 | $I_3(5)$ | Secuencia | $\sum C_j/n$ | $\sum w_jC_j$ | $L_{max}$ | $\sum w_jT_j$ | ¿Coincide con la diapositiva? |
|---|---|---|---|---|---|---|---|---|
| Por defecto ($K=1$) | 5.5, 5.667, 7.5, 8 | 0.5890 | 1-3-2-4 | 12 | 88 | 16 | 39 | Sí |
| `--pbar-fijo` ($K=1$) | 5.5 siempre | 0.5796 | 1-3-2-4 | 12 | 88 | 16 | 39 | Sí, y los índices son exactamente los de la p. 45 (0.40, 0.30, 0.23, 0.13 / 0.43, 0.58 / 0.43) |
| `--K 2` | 5.5, 6.667, 6.5, 8 | — | 3-2-1-4 | 11.75 | 81 | 16 | 42 | No |

Conclusión: con $K=1$ la secuencia de clase (1-3-2-4, $\sum w_jT_j=39$) sale igual con $\bar p$ fijo o recalculado; la diapositiva usó $\bar p$ fijo. Con $K=2$ la holgura pesa menos, el índice se acerca a WSPT ($w_j/p_j$) y la secuencia pasa a 3-2-1-4: mejor $\sum w_jC_j$ (81, el óptimo WSPT) pero peor tardanza ponderada (42). $K$ es un parámetro que hay que calibrar.

**Advertencias.** El docstring llama al archivo `atc_lec17.py`, pero se llama `atc.py`. El script no maneja liberaciones $r_j$ ni setups, y los datos están fijos en el código.

## Orden de estudio sugerido

1. [L17](/corte-3-programacion-scheduling/02-una-maquina/L17-single-machine-scheduling.md), pp. 2-13: motivación ($n!$), WSPT, reglas estáticas y dinámicas (MS, ATC).
2. [ejemplo-1](/corte-3-programacion-scheduling/02-una-maquina/ejemplo-1-programacion-produccion.md): calcular $C_j$ con liberaciones.
3. [programacion-produccion-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/programacion-produccion-una-maquina.md), hoja `Reglas de Despacho`: comparar las reglas sobre 6 trabajos.
4. L17, pp. 14-26, y la hoja `Restricciones de Precedencia`: cadenas, factor $\rho$ y preemption.
5. L17, pp. 27-42: Lawler, EDD, CR paso a paso, Moore-Hodgson y la regla para $\sum T_j$.
6. L17, pp. 43-45, y `atc.py`: ejercicio FIFO/SPT/EDD/ATC.
7. L17, pp. 46-48, y la hoja `Tardanza Máxima`: métodos exactos y Solver.

## Conceptos y fórmulas clave

Detalle en el [resumen de L17](/corte-3-programacion-scheduling/02-una-maquina/L17-single-machine-scheduling.md#resumen).

- **WSPT** (óptima para $1||\sum w_jC_j$): ordenar por $w_j/p_j$ decreciente. **SPT** minimiza $\sum C_j/n$. **EDD** (óptima para $1||L_{max}$): ordenar por $d_j$ creciente.
- **Holgura mínima:** $s_j=\max(d_j-p_j-t,0)$, menor primero.
- **ATC:** $I_j(t)=\dfrac{w_j}{p_j}\exp\!\left(-\dfrac{\max(d_j-p_j-t,0)}{K\bar p}\right)$, mayor primero. $K$ es una constante de escala y $\bar p$ el promedio de $p$ de los no programados.
- **Razón crítica:** $CR_j=\dfrac{\max(d_j-t,0)}{p_j}$, menor primero; empate por SPT.
- **Cadenas:** si no se pueden interrumpir, mayor $\sum w/\sum p$ primero. Si se pueden cortar, factor $\rho=\max_{l}\dfrac{\sum_{j\le l}w_j}{\sum_{j\le l}p_j}$, procesando hasta $l^*$.
- **Preemption** ($1|r_j,prmp|\sum w_jC_j$): en cada evento, mayor $w_j/p_j^{\text{restante}}$.
- **Lawler** ($1|prec|h_{max}$): de atrás hacia adelante, se pone de último el trabajo elegible con menor $h_j\!\left(\sum_{k\in J^c}p_k\right)$.
- **Moore-Hodgson** ($1||\sum U_j$): orden EDD; si alguno llega tarde, se saca el más largo de los programados.
- **$1||\sum T_j$:** si $p_j\le p_k$ y $d_j\le d_k$, existe un óptimo con $j$ antes que $k$.

## Ejercicios resueltos disponibles

| Ejercicio | Archivo | Resultado principal |
|---|---|---|
| FIFO, SPT, EDD y ATC con 4 trabajos ($p$ = 5, 7, 2, 8; $d$ = 1, 9, 10, 6; $w$ = 2, 3, 2, 1) | [L17](/corte-3-programacion-scheduling/02-una-maquina/L17-single-machine-scheduling.md) pp. 43-45; [atc.py](/corte-3-programacion-scheduling/02-una-maquina/atc.py) | FIFO: 13.25 / 16 / 41; SPT: **11.25** / 16 / 43; EDD: 15 / **12** / 72; ATC: 12 / 16 / **39** (flujo promedio / $L_{max}$ / $\sum w_jT_j$) |
| Razón crítica con los mismos 4 trabajos | L17 pp. 33-37 | 1-4-3-2: flujo 13.75, $L_{max}=13$, $\sum w_jT_j=64$ |
| Cadenas 1→2→3→4 y 5→6→7 (factor $\rho$) | L17 pp. 18-23 | 1-2-5-6-3-7-4 |
| Lawler con $h_1=1+C_1$, $h_2=1.2C_2$, $h_3=10$ | L17 pp. 29-31 | 1-2-3 o 2-1-3, $h_{max}=10$ |
| Moore-Hodgson, 5 trabajos | L17 pp. 40-41 | 3-4-5-1-2, $\sum U_j=2$ |
| WSPT, tareas A-E | L17 p. 10 (resuelto en el .md) | A-D-E-B-C, $\sum w_jC_j=779$ |
| 6 trabajos con natural, azar, SPT, WSPT, EDD y MS | [programacion-produccion-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/programacion-produccion-una-maquina.md) | WSPT 6-5-2-4-1-3 da el menor $\sum w_jC_j$ (161); SPT el menor $\sum C_j/n$ (16); EDD el menor $L_{max}$ (7); MS da $\sum T_j=16$ |
| Cadenas A-F (sin y con interrupción) | ídem, hoja `Restricciones de Precedencia` | Sin romper: C-B-A-E-F-D; con $\rho$: $l^*$ = A (0.35) y E (0.38) |
| Preemption con $r_j$ (L17 p. 25), $w_j=1$ | ídem, hoja `Restricciones de Precedencia` | 1, 3, 4, 5, 6, 7, 2; $C_{max}=89$, $\sum C_j=305$ |
| 4 actividades cotidianas con $r_j$ | [ejemplo-1](/corte-3-programacion-scheduling/02-una-maquina/ejemplo-1-programacion-produccion.md) | Flujo promedio 35.165 h |
| Solver Evolutionary para $1\|\|\sum w_jT_j$ (wt40_1) | L17 p. 48; hoja `Tardanza Máxima` | Captura: $\sum w_jT_j=16822$ (óptimo conocido 913) |

Varias hojas del Excel tienen errores de fórmula (reloj reiniciado en EDD, rango mal tomado en un promedio, objetivo constante en `Tardanza Máxima`). Están señalados y corregidos en [programacion-produccion-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/programacion-produccion-una-maquina.md#observaciones).

## Relación con otros temas y proyectos

- Antes: [01-introduccion-scheduling](/corte-3-programacion-scheduling/01-introduccion-scheduling/README.md), con la notación $\alpha|\beta|\gamma$ y los indicadores.
- Después: [03-maquinas-paralelas](/corte-3-programacion-scheduling/03-maquinas-paralelas/) (extiende SPT/LPT a $Pm$), [04-flow-shop](/corte-3-programacion-scheduling/04-flow-shop/) y [05-job-shop](/corte-3-programacion-scheduling/05-job-shop/).
- Compendio con hojas `02_1Maq_Basicos`, `03_1Maq_MS_ATC`, `04_1Maq_Precedencia`, `05_1Maq_Preemption` y `06_1Maq_Lawler`: [metodos-programacion-produccion-corte3](/corte-3-programacion-scheduling/00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md).
- Proyecto: el reto 2 de la [competencia](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/README.md) ($P3|r_j,prec|\sum w_jT_j$) usa WSPT, ATC, cadenas y EDD como reglas de arranque.
- Corte 2: la regla de "inicio en $\max(r_j, C_{\text{anterior}})$" se parece al backward/forward scheduling de [05-mrp-ii-y-capacidad](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/).


---

<!-- fuente: corte-3-programacion-scheduling/02-una-maquina/L17-single-machine-scheduling.md -->
# L17-single-machine-scheduling

> **Archivo:** [`L17-single-machine-scheduling.pdf`](/corte-3-programacion-scheduling/02-una-maquina/L17-single-machine-scheduling.pdf) · **Corte 3** · 49 páginas  
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

- Excel de clase con FIFO, SPT, WSPT, EDD, MS, cadenas, preemption y una hoja para Solver: [programacion-produccion-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/programacion-produccion-una-maquina.md). Ejemplo cotidiano con $r_j$: [ejemplo-1-programacion-produccion](/corte-3-programacion-scheduling/02-una-maquina/ejemplo-1-programacion-produccion.md).
- Implementación en Python del ejemplo ATC de las pp. 43-45: [atc.py](/corte-3-programacion-scheduling/02-una-maquina/atc.py), explicado en el [README](/corte-3-programacion-scheduling/02-una-maquina/README.md).
- Compendio con hojas de 1 máquina (básicas, MS/ATC, precedencia, preemption, Lawler): [metodos-programacion-produccion-corte3](/corte-3-programacion-scheduling/00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md).
- Notación e indicadores: [L16](/corte-3-programacion-scheduling/01-introduccion-scheduling/L16-intro-scheduling.md). Siguiente tema: [L18 máquinas paralelas](/corte-3-programacion-scheduling/03-maquinas-paralelas/L18-parallel-machine-scheduling.md).
- El reto 2 de la competencia ($P3|r_j,prec|\sum w_jT_j$) usa WSPT, ATC, cadenas y EDD: [proyecto-competencia-scheduling](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/README.md).

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

(La diapositiva no da pesos ni solución. El Excel [programacion-produccion-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/programacion-produccion-una-maquina.md), hoja `Restricciones de Precedencia`, lo resuelve con $w_j=1$; ver el resumen.)

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

(Inicio de cada trabajo = $C_j-p_j$. EDD: 1 [0,5], 4 [5,13], 2 [13,20], 3 [20,22]. ATC: 1 [0,5], 3 [5,7], 2 [7,14], 4 [14,22]. Los índices coinciden con $K=1$ y $\bar p=5.5$, el promedio de los cuatro trabajos sin recalcular; con $\bar p$ recalculado, $I_3(5)=0.589$. Ver [atc.py](/corte-3-programacion-scheduling/02-una-maquina/atc.py).)

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


---

<!-- fuente: corte-3-programacion-scheduling/02-una-maquina/atc.py -->
# Código: `corte-3-programacion-scheduling/02-una-maquina/atc.py`

> Archivo completo: https://github.com/samuelgradientai-sys/planeacion-control-produccion/blob/main/corte-3-programacion-scheduling/02-una-maquina/atc.py

```python
"""
Regla de despacho ATC (Apparent Tardiness Cost) para una maquina.
Ejemplo de la Lec 17 (diapositivas 43-45).

    I_j(t) = (w_j / p_j) * exp( -max(d_j - p_j - t, 0) / (K * p_barra) )

    K       : constante a determinar (en el ejemplo K = 1)
    p_barra : tiempo promedio de los trabajos no programados

En cada instante t se programa el trabajo con MAYOR indice I_j(t)
(secuenciacion I[k] >= I[k+1]); luego t avanza en p_j y se repite.

Uso:
    python atc_lec17.py              -> p_barra se recalcula con los trabajos pendientes
    python atc_lec17.py --pbar-fijo  -> p_barra fijo con todos los trabajos (asi salen
                                        exactamente los indices de la diapositiva 45)
    python atc_lec17.py --K 2        -> cambiar la constante K
"""

import argparse
import math

# Datos del ejemplo (diapositiva 43)
TRABAJOS = {
    1: {"p": 5, "d": 1, "w": 2},
    2: {"p": 7, "d": 9, "w": 3},
    3: {"p": 2, "d": 10, "w": 2},
    4: {"p": 8, "d": 6, "w": 1},
}

# Solucion ATC de la diapositiva 45, para verificar
ESPERADO = {
    "secuencia": [1, 3, 2, 4],
    "flujo_promedio": 12,
    "retardo_max": 16,
    "tardanza_ponderada": 39,
}


def indice_atc(trabajo, t, K, p_barra):
    """I_j(t) = (w_j/p_j) * exp(-max(d_j - p_j - t, 0) / (K * p_barra))"""
    holgura = max(trabajo["d"] - trabajo["p"] - t, 0)
    return (trabajo["w"] / trabajo["p"]) * math.exp(-holgura / (K * p_barra))


def programar_atc(trabajos, K=1.0, pbar_fijo=False):
    """Construye la secuencia ATC. Devuelve la secuencia y el detalle de cada iteracion."""
    pendientes = sorted(trabajos)
    p_barra_total = sum(trabajos[j]["p"] for j in pendientes) / len(pendientes)

    t = 0
    secuencia = []
    iteraciones = []

    while pendientes:
        if pbar_fijo:
            p_barra = p_barra_total
        else:
            p_barra = sum(trabajos[j]["p"] for j in pendientes) / len(pendientes)

        indices = {j: indice_atc(trabajos[j], t, K, p_barra) for j in pendientes}

        # Mayor indice; si hay empate, el trabajo de menor numero
        elegido = max(pendientes, key=lambda j: (indices[j], -j))

        iteraciones.append({"t": t, "p_barra": p_barra, "indices": indices, "elegido": elegido})
        secuencia.append(elegido)
        pendientes.remove(elegido)
        t += trabajos[elegido]["p"]

    return secuencia, iteraciones


def evaluar(secuencia, trabajos):
    """Calcula Cj, Lj, wjTj y las medidas de desempeno de una secuencia."""
    t = 0
    filas = []
    for j in secuencia:
        tr = trabajos[j]
        t += tr["p"]
        L = t - tr["d"]
        T = max(L, 0)
        filas.append({"j": j, "p": tr["p"], "C": t, "d": tr["d"], "L": L, "w": tr["w"], "wT": tr["w"] * T})

    n = len(filas)
    medidas = {
        "flujo_promedio": sum(f["C"] for f in filas) / n,
        "flujo_ponderado": sum(f["w"] * f["C"] for f in filas),
        "retardo_max": max(f["L"] for f in filas),
        "tardanza_ponderada": sum(f["wT"] for f in filas),
    }
    return filas, medidas


def imprimir_iteraciones(iteraciones, trabajos):
    ids = sorted(trabajos)
    print("Indices ATC en cada decision (* = trabajo elegido)")
    print(f"{'t':>4} {'p_barra':>8} | " + " ".join(f"{'I(' + str(j) + ')':>8}" for j in ids))
    print("-" * (16 + 9 * len(ids)))
    for it in iteraciones:
        celdas = []
        for j in ids:
            if j in it["indices"]:
                marca = "*" if j == it["elegido"] else " "
                celdas.append(f"{it['indices'][j]:7.4f}{marca}")
            else:
                celdas.append(f"{'-':>8}")
        print(f"{it['t']:>4} {it['p_barra']:>8.3f} | " + " ".join(celdas))
    print()


def imprimir_tabla(filas):
    print("Programa ATC")
    etiquetas = [("Secuencia", "j"), ("pj", "p"), ("Cj", "C"), ("dj", "d"),
                 ("Lj = Cj - dj", "L"), ("wj", "w"), ("wjTj", "wT")]
    for nombre, clave in etiquetas:
        print(f"{nombre:<13}" + "".join(f"{f[clave]:>6}" for f in filas))
    print()


def verificar(secuencia, medidas):
    print("Comparacion con la diapositiva 45")
    checks = [
        ("Secuencia", secuencia, ESPERADO["secuencia"]),
        ("Flujo promedio", medidas["flujo_promedio"], ESPERADO["flujo_promedio"]),
        ("Retardo max", medidas["retardo_max"], ESPERADO["retardo_max"]),
        ("Tardanza ponderada", medidas["tardanza_ponderada"], ESPERADO["tardanza_ponderada"]),
    ]
    todo_ok = True
    for nombre, obtenido, esperado in checks:
        ok = obtenido == esperado
        todo_ok &= ok
        print(f"  {nombre:<20} obtenido = {str(obtenido):<14} esperado = {str(esperado):<14} {'OK' if ok else 'DIFERENTE'}")
    print("  Resultado:", "coincide con la solucion de clase" if todo_ok else "NO coincide")


def main():
    parser = argparse.ArgumentParser(description="Regla ATC - ejemplo Lec 17")
    parser.add_argument("--K", type=float, default=1.0, help="constante K (por defecto 1)")
    parser.add_argument("--pbar-fijo", action="store_true",
                        help="usar p_barra de todos los trabajos en vez de solo los pendientes")
    args = parser.parse_args()

    modo = "fijo (todos los trabajos)" if args.pbar_fijo else "trabajos no programados"
    print(f"Regla ATC  |  K = {args.K}  |  p_barra = {modo}\n")

    secuencia, iteraciones = programar_atc(TRABAJOS, K=args.K, pbar_fijo=args.pbar_fijo)
    filas, medidas = evaluar(secuencia, TRABAJOS)

    imprimir_iteraciones(iteraciones, TRABAJOS)
    imprimir_tabla(filas)

    print("Secuencia ATC:", " -> ".join(map(str, secuencia)))
    print(f"Flujo promedio          = {medidas['flujo_promedio']:g}")
    print(f"Flujo ponderado (wjCj)  = {medidas['flujo_ponderado']:g}")
    print(f"Retardo maximo (Lmax)   = {medidas['retardo_max']:g}")
    print(f"Tardanza ponderada      = {medidas['tardanza_ponderada']:g}")
    print()

    verificar(secuencia, medidas)


if __name__ == "__main__":
    main()
```


---

<!-- fuente: corte-3-programacion-scheduling/02-una-maquina/ejemplo-1-programacion-produccion.md -->
# ejemplo-1-programacion-produccion

> **Archivo:** [`ejemplo-1-programacion-produccion.xlsx`](/corte-3-programacion-scheduling/02-una-maquina/ejemplo-1-programacion-produccion.xlsx) · **Corte 3** · Libro de Excel con 1 hoja(s): `Hoja1`  
> **Nombre original:** `CORTE 3/Ejemplo 1 Programación de Producción .xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Ejemplo introductorio de **programación de una máquina con tiempos de liberación** ($1|r_j|\cdot$), con actividades de la vida diaria. La "máquina" es la persona que hace las tareas. Usa los parámetros de [L16](/corte-3-programacion-scheduling/01-introduccion-scheduling/L16-intro-scheduling.md) ($r_j$, $d_j$, $p_j$, $w_j$, setup $s_j$) y los indicadores $C_j$, $C_j-r_j$ y $w_jC_j$ de [L17](/corte-3-programacion-scheduling/02-una-maquina/L17-single-machine-scheduling.md). Sirve para ver que un trabajo no puede empezar antes de su $r_j$ y cómo se calcula el tiempo de flujo.

Es **idéntico** al bloque de las filas 3-8 de la hoja `Reglas de Despacho` de [programacion-produccion-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/programacion-produccion-una-maquina.md): mismos valores y mismas fórmulas.

### Hoja `Hoja1`

**Objetivo (deducido):** secuenciar 4 actividades, con el tiempo en horas desde un instante 0, y calcular cuándo termina cada una, su tiempo de flujo y su costo ponderado.

**Datos de entrada** (columnas B-H, filas 4-7). La columna N es la **posición** en la secuencia; las filas no están en ese orden.

| N (posición) | Trabajo | $r_j$ (h) | $d_j$ (como está escrito) | $p_j$ | $w_j$ | $s_j$ (setup) |
|---|---|---|---|---|---|---|
| 2 | Proyecto | 24 | "24 h + 30 días" (texto) | 10 h | 5 | 3 h |
| 4 | Seminario | 0 | 19-oct (celda con fecha, formato d-mmm) | 2 h | 2 | 0 h |
| 1 | Pago Factura | 50 | 19-oct (celda con fecha, formato d-mmm) | 20 min | 3 | 30 min |
| 3 | Entrevista de Trabajo | 100 | "100 h + 2 h" (texto) | 1 h | 4 | 0 h |

$p_j$, $s_j$ y casi todos los $d_j$ son texto, así que no entran en fórmulas; los $C_j$ se escribieron con números a mano.

**Método (fórmulas traducidas):**

- Pago Factura (posición 1): `I6 = 50+0.33`, es decir $C=r_j+p_j=50+0.33$ (nota J6: "20 min = 0,33 h").
- Proyecto (posición 2): `I4 = I6+10`, es decir $C=C_{\text{anterior}}+p_j$ (ya pasó su $r=24$).
- Entrevista (posición 3): `I7 = 100+1`. Nota J7: "si r_j es > c_j del anterior, inicia en r_j", o sea $\text{inicio}_j=\max(r_j,\ C_{\text{anterior}})$.
- Seminario (posición 4): `I5 = I7+2`.
- `K = I − D`: tiempo de flujo $F_j=C_j-r_j$. `L = G·I`: $w_jC_j$.
- `K8 = AVERAGE(K4:K7)` = flujo promedio $\bar F$. `L8 = AVERAGE(L4:L7)` = promedio de $w_jC_j$.

**Resultados (programa en orden de ejecución):**

| Posición | Trabajo | $r_j$ | Inicio | Fin = $C_j$ | $C_j-r_j$ | $w_jC_j$ |
|---|---|---|---|---|---|---|
| 1 | Pago Factura | 50 | 50 | 50.33 | 0.33 | 150.99 |
| 2 | Proyecto | 24 | 50.33 | 60.33 | 36.33 | 301.65 |
| — | (ocioso) | | 60.33 | 100 | | |
| 3 | Entrevista de Trabajo | 100 | 100 | 101 | 1 | 404 |
| 4 | Seminario | 0 | 101 | 103 | 103 | 206 |
| | **"Tiempo de Flujo"** (promedios) | | | | **35.165** | **265.66** |

Cálculo propio: $\sum w_jC_j=1062.64$ y $C_{max}=103$ h. La Entrevista ($d$ = "100 h + 2 h" = 102 h, interpretación) termina en 101, a tiempo.

**Gráficos:** no hay.

**Conclusión:** el ejemplo muestra cómo las liberaciones fuerzan esperas: la Entrevista no puede empezar antes de $t=100$, y el orden elegido deja al Seminario de último con un flujo de 103 h.

### Observaciones

- **Duplicado:** es igual al bloque A de la hoja `Reglas de Despacho` de [programacion-produccion-una-maquina](/corte-3-programacion-scheduling/02-una-maquina/programacion-produccion-una-maquina.md).
- Los tiempos de alistamiento $s_j$ (3 h para Proyecto y 30 min para Pago Factura) no se suman en ningún $C_j$.
- Las fechas de entrega mezclan texto ("24 h + 30 días", "100 h + 2 h") y fechas de calendario (19-oct), así que no se calculan $L_j$ ni $T_j$.
- La secuencia no es un programa sin retrasos (*non-delay*): de 0 a 50 no se hace nada aunque el Seminario ($r=0$) y el Proyecto ($r=24$) ya están disponibles. Programar el Seminario en $[0,2]$ y el Proyecto en $[24,34]$ bajaría el flujo (deducido).
- La fila 8 dice "Tiempo de Flujo", pero L8 es un promedio de $w_jC_j$, no un tiempo de flujo.


---

<!-- fuente: corte-3-programacion-scheduling/02-una-maquina/programacion-produccion-una-maquina.md -->
# programacion-produccion-una-maquina

> **Archivo:** [`programacion-produccion-una-maquina.xlsx`](/corte-3-programacion-scheduling/02-una-maquina/programacion-produccion-una-maquina.xlsx) · **Corte 3** · Libro de Excel con 3 hoja(s): `Reglas de Despacho`, `Restricciones de Precedencia`, `Tardanza Máxima`  
> **Nombre original:** `CORTE 3/Programación de Producción.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Libro de trabajo de clase para el tema **programación de una máquina** ([L17](/corte-3-programacion-scheduling/02-una-maquina/L17-single-machine-scheduling.md)). Tiene tres hojas:

1. `Reglas de Despacho`: un ejemplo cotidiano con $r_j$ (el mismo de [ejemplo-1-programacion-produccion](/corte-3-programacion-scheduling/02-una-maquina/ejemplo-1-programacion-produccion.md)) y el "ejemplo clase 20/10": 6 trabajos secuenciados con orden natural, al azar, SPT, WSPT, EDD y holgura mínima (MS), con $\sum C_j/n$, $\sum w_jT_j$, número de tardíos y $\sum w_jC_j$.
2. `Restricciones de Precedencia`: cadenas que no se pueden romper (razón $\sum w/\sum p$), cadenas que sí (factor $\rho$) y el ejercicio de *preemption* de la p. 25 de L17, con un Gantt dibujado a mano.
3. `Tardanza Máxima`: 20 trabajos y una secuencia evaluada con `VLOOKUP`; parece preparada para optimizar con Solver, como en la p. 48 de L17 (deducido).

Se aprende a calcular $C_j$, $T_j$, $L_j$ y $U_j$ a partir de una secuencia, a comparar reglas de despacho y a aplicar las reglas de cadenas y de *preemption*.

No hay gráficos de Excel. La hoja 2 tiene una imagen (un Gantt a mano).

Notación de las fórmulas: $[k]$ es el trabajo en la posición $k$; $C_{[k]}=C_{[k-1]}+p_{[k]}$; $T_j=\max(C_j-d_j,0)$; $L_j=C_j-d_j$.

---

### Hoja `Reglas de Despacho`

#### Bloque A (filas 3-8): ejemplo cotidiano con liberaciones

**Objetivo (deducido):** programar cuatro actividades personales en un solo "recurso" (la persona), respetando la hora en que cada una está disponible ($r_j$), y medir el tiempo de flujo. Es idéntico a [ejemplo-1-programacion-produccion](/corte-3-programacion-scheduling/02-una-maquina/ejemplo-1-programacion-produccion.md); ahí está explicado en detalle.

| N (posición) | Trabajo | $r_j$ (h) | $d_j$ | $p_j$ | $w_j$ | $s_j$ | $c_j$ | $c_j-r_j$ | $w_jc_j$ |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Pago Factura | 50 | 19-oct (fecha) | 20 min | 3 | 30 min | 50.33 | 0.33 | 150.99 |
| 2 | Proyecto | 24 | "24 h + 30 días" | 10 h | 5 | 3 h | 60.33 | 36.33 | 301.65 |
| 3 | Entrevista de Trabajo | 100 | "100 h + 2 h" | 1 h | 4 | 0 h | 101 | 1 | 404 |
| 4 | Seminario | 0 | 19-oct (fecha) | 2 h | 2 | 0 h | 103 | 103 | 206 |

(En la hoja las filas aparecen en el orden 2, 4, 1, 3; la columna N da la posición en la secuencia.)

- Fórmulas: `I6 = 50+0.33` ($C=r+p$, con 20 min = 0.33 h); `I4 = I6+10`; `I7 = 100+1` (nota J7: "si r_j es > c_j del anterior, inicia en r_j"); `I5 = I7+2`; `K = I−D` ($C_j-r_j$); `L = G·I` ($w_jC_j$).
- Resultados: `K8 = AVERAGE(K4:K7)` = **35.165** h ("Tiempo de Flujo" promedio $\bar F=\frac1n\sum(C_j-r_j)$); `L8 = AVERAGE(L4:L7)` = **265.66** (promedio de $w_jC_j$; la suma sería 1062.64).

#### Bloque B (filas 10-18): "ejemplo clase 20/10", orden natural

**Datos de entrada** (los mismos en todos los bloques que siguen):

| Trabajo | $p_j$ | $d_j$ | $w_j$ | $w_j/p_j$ |
|---|---|---|---|---|
| 1 | 6 | 36 | 1 | 0.1667 |
| 2 | 4 | 21 | 1 | 0.25 |
| 3 | 7 | 18 | 1 | 0.1429 |
| 4 | 12 | 15 | 3 | 0.25 |
| 5 | 5 | 1 | 2 | 0.4 |
| 6 | 2 | 32 | 1 | 0.5 |

**Método:** `E13 = C13`, `E14 = E13+C14` → $C_{[k]}=C_{[k-1]}+p_{[k]}$; `F = IF(E<D,0,E−D)` → $T_j=\max(C_j-d_j,0)$; `G = IF(F>0,F,E−D)` → $L_j=C_j-d_j$; `J12 = AVERAGE(E13:E18)` → $\sum C_j/n$; `J13 = {SUM(H13:H18*F13:F18)}` (fórmula matricial) → $\sum w_jT_j$; `J14` = número de tardíos, escrito a mano.

Secuencia 1-2-3-4-5-6 (orden natural, FIFO):

| Trabajo | Inicio | $C_j$ | $d_j$ | $T_j$ | $L_j$ | $w_j$ |
|---|---|---|---|---|---|---|
| 1 | 0 | 6 | 36 | 0 | −30 | 1 |
| 2 | 6 | 10 | 21 | 0 | −11 | 1 |
| 3 | 10 | 17 | 18 | 0 | −1 | 1 |
| 4 | 17 | 29 | 15 | 14 | 14 | 3 |
| 5 | 29 | 34 | 1 | 33 | 33 | 2 |
| 6 | 34 | 36 | 32 | 4 | 4 | 1 |

$\sum C_j/n=22$; $\sum w_jT_j=112$; tardíos = 3.

#### Bloque C (filas 20-27): "Secuencia elegida al azar"

| Trabajo | Inicio | $C_j$ | $d_j$ | $T_j$ | $L_j$ | $w_j$ | $w_jC_j$ |
|---|---|---|---|---|---|---|---|
| 4 | 0 | 12 | 15 | 0 | −3 | 3 | 36 |
| 3 | 12 | 19 | 18 | 1 | 1 | 1 | 19 |
| 1 | 19 | 25 | 36 | 0 | −11 | 1 | 25 |
| 5 | 25 | 30 | 1 | 29 | 29 | 2 | 60 |
| 2 | 30 | 34 | 21 | 13 | 13 | 1 | 34 |
| 6 | 34 | 36 | 32 | 4 | 4 | 1 | 36 |

$\sum C_j/n$ = **28.8** en la hoja (ver Observaciones; el valor correcto es 26); $\sum w_jT_j=76$; tardíos = 4; `K27 = SUM` → $\sum w_jC_j=210$.

#### Bloque D (filas 28-35): "Secuencia organizada desde el más corto" (SPT)

| Trabajo | Inicio | $C_j$ | $d_j$ | $T_j$ | $L_j$ | $w_j$ | $w_j/p_j$ | Prioridad WSPT | $w_jC_j$ |
|---|---|---|---|---|---|---|---|---|---|
| 6 | 0 | 2 | 32 | 0 | −30 | 1 | 0.5 | 1 | 2 |
| 2 | 2 | 6 | 21 | 0 | −15 | 1 | 0.25 | 3 | 6 |
| 5 | 6 | 11 | 1 | 10 | 10 | 2 | 0.4 | 2 | 22 |
| 1 | 11 | 17 | 36 | 0 | −19 | 1 | 0.1667 | 5 | 17 |
| 3 | 17 | 24 | 18 | 6 | 6 | 1 | 0.1429 | 6 | 24 |
| 4 | 24 | 36 | 15 | 21 | 21 | 3 | 0.25 | 4 | 108 |

$\sum C_j/n=16$; $\sum w_jT_j=89$; tardíos = 3; $\sum w_jC_j=179$. Las columnas K (`=H/C`, $w_j/p_j$) y L (prioridad de mayor a menor, escrita a mano) preparan el bloque WSPT.

#### Bloque E (filas 36-43): "Secuencia por prioridad WSPT"

| Trabajo | Inicio | $C_j$ | $d_j$ | $T_j$ | $L_j$ | $w_j$ | $w_jC_j$ |
|---|---|---|---|---|---|---|---|
| 6 | 0 | 2 | 32 | 0 | −30 | 1 | 2 |
| 5 | 2 | 7 | 1 | 6 | 6 | 2 | 14 |
| 2 | 7 | 11 | 21 | 0 | −10 | 1 | 11 |
| 4 | 11 | 23 | 15 | 8 | 8 | 3 | 69 |
| 1 | 23 | 29 | 36 | 0 | −7 | 1 | 29 |
| 3 | 29 | 36 | 18 | 18 | 18 | 1 | 36 |

$\sum C_j/n=18$; $\sum w_jT_j=54$; tardíos = 3; **$\sum w_jC_j=161$**, el mínimo de todo el libro, como garantiza el teorema de WSPT. Los trabajos 2 y 4 empatan en $w/p=0.25$; cualquier orden entre ellos da 161.

#### Bloque F (filas 44-51): "Secuencia por tiempo de terminación EDD"

Secuencia 5-4-3-2-6-1. Valores que guardó la hoja:

| Trabajo | $C_j$ (hoja) | $C_j$ correcto | $d_j$ | $T_j$ | $L_j$ correcto | $w_j$ | $w_jC_j$ (hoja) |
|---|---|---|---|---|---|---|---|
| 5 | 5 | 5 | 1 | 4 | 4 | 2 | 10 |
| 4 | 17 | 17 | 15 | 2 | 2 | 3 | 51 |
| 3 | 24 | 24 | 18 | 6 | 6 | 1 | 24 |
| 2 | 28 | 28 | 21 | 7 | 7 | 1 | 28 |
| 6 | **2** | 30 | 32 | 0 | −2 | 1 | 2 |
| 1 | **8** | 36 | 36 | 0 | 0 | 1 | 8 |

Hoja: $\sum C_j/n=14$, $\sum w_jT_j=27$, tardíos = 4, $\sum w_jC_j=123$. Corregido (cálculo propio): $\sum C_j/n=23.33$, $\sum w_jT_j=27$ (no cambia), $\sum w_jC_j=179$, $L_{max}=7$ (el menor de todas las reglas, como garantiza EDD).

#### Bloque G (filas 52-68): "Secuencia por holgura mínima MS"

**Método:** holgura $s_j(t)=\max(d_j-p_j-t,0)$. Las fórmulas son `E53 = IF(D−C>0,D−C,0)` para $t=0$ y `F53 = IF(D−C−$E$59>0, D−C−$E$59, 0)` para los demás instantes. La fila 59 ("Menor Holgura") guarda el reloj $t$ después de cada trabajo elegido: `E59 = C57` (=5), `F59 = C56+E59` (=17), `G59 = C54+F59` (=21), `H59 = C55+G59` (=28). Las celdas de los trabajos ya programados quedan vacías.

| Trabajo | $p_j$ | $d_j$ | $s_j(0)$ | $s_j(5)$ | $s_j(17)$ | $s_j(21)$ | $s_j(28)$ |
|---|---|---|---|---|---|---|---|
| 1 | 6 | 36 | 30 | 25 | 13 | 9 | 2 |
| 2 | 4 | 21 | 17 | 12 | **0** | | |
| 3 | 7 | 18 | 11 | 6 | 0 | **0** | |
| 4 | 12 | 15 | 3 | **0** | | | |
| 5 | 5 | 1 | **0** | | | | |
| 6 | 2 | 32 | 30 | 25 | 13 | 9 | **2** |
| Elegido → nuevo $t$ | | | 5 → 5 | 4 → 17 | 2 → 21 | 3 → 28 | 6 → 30, luego 1 → 36 |

En $t=17$ empatan 2 y 3 (holgura 0) y en $t=28$ empatan 1 y 6 (holgura 2). La hoja elige 2 y 6, los de menor $p_j$; el desempate por SPT es deducido, la hoja no lo dice.

Resultado (filas 61-68):

| Trabajo | Inicio | $C_j$ | $d_j$ | $T_j$ |
|---|---|---|---|---|
| 5 | 0 | 5 | 1 | 4 |
| 4 | 5 | 17 | 15 | 2 |
| 2 | 17 | 21 | 21 | 0 |
| 3 | 21 | 28 | 18 | 10 |
| 6 | 28 | 30 | 32 | 0 |
| 1 | 30 | 36 | 36 | 0 |

`F68 = SUM(F62:F67)` → $\sum T_j=16$. Cálculo propio: $\sum w_jT_j=24$, $\sum C_j/n=22.83$, $\sum w_jC_j=176$, tardíos = 3.

#### Bloque H (filas 70-77): sin rótulo

Secuencia 5-4-2-6-3-1. La hoja no dice qué regla aplica. No coincide con MS ni con EDD, y tampoco con ATC ($K=1$) ni CR calculadas con estos datos (cálculo propio; deducido).

| Trabajo | $C_j$ (hoja) | $C_j$ correcto | $d_j$ | $T_j$ (hoja) | $T_j$ correcto | $w_j$ |
|---|---|---|---|---|---|---|
| 5 | 5 | 5 | 1 | 4 | 4 | 2 |
| 4 | 17 | 17 | 15 | 2 | 2 | 3 |
| 2 | 21 | 21 | 21 | 0 | 0 | 1 |
| 6 | **2** | 23 | 32 | 0 | 0 | 1 |
| 3 | **9** | 30 | 18 | 0 | **12** | 1 |
| 1 | **15** | 36 | 36 | 0 | 0 | 1 |

Hoja: $\sum C_j/n=11.5$, $\sum w_jT_j=14$, tardíos = 3, $\sum w_jC_j=108$. Corregido: $\sum C_j/n=22$, $\sum w_jT_j=26$, $\sum w_jC_j=171$, tardíos = 3.

#### Resumen comparativo del ejemplo 20/10

Valores corregidos donde la hoja tiene errores; $L_{max}$ y las celdas marcadas con \* son cálculo propio.

| Regla | Secuencia | $\sum C_j/n$ | $\sum w_jT_j$ | Tardíos | $\sum w_jC_j$ | $L_{max}$ |
|---|---|---|---|---|---|---|
| Orden natural | 1-2-3-4-5-6 | 22 | 112 | 3 | 224\* | 33 |
| Al azar | 4-3-1-5-2-6 | 26 (hoja: 28.8) | 76 | 4 | 210 | 29 |
| SPT | 6-2-5-1-3-4 | **16** | 89 | 3 | 179 | 21 |
| WSPT | 6-5-2-4-1-3 | 18 | 54 | 3 | **161** | 18 |
| EDD | 5-4-3-2-6-1 | 23.33 (hoja: 14) | 27 | 4 | 179 (hoja: 123) | **7** |
| MS | 5-4-2-3-6-1 | 22.83\* | **24\*** | 3 | 176\* | 10 |
| Sin rótulo | 5-4-2-6-3-1 | 22 (hoja: 11.5) | 26 (hoja: 14) | 3 | 171 (hoja: 108) | 12 |

**Conclusión:** SPT minimiza el flujo promedio, WSPT minimiza $\sum w_jC_j$ y EDD minimiza $L_{max}$, como dice la teoría de L17. Para la tardanza ponderada, las reglas orientadas a fechas (MS, EDD) son mucho mejores que FIFO o SPT.

---

### Hoja `Restricciones de Precedencia`

#### Bloque 1 (filas 1-13): "1|Prec|ΣCj — Si, NO se pueden romper las cadenas"

**Datos:**

| Job | $P_j$ | $W_j$ |
|---|---|---|
| A | 2 | 1 |
| B | 4 | 2 |
| C | 11 | 3 |
| D | 30 | 2 |
| E | 13 | 5 |
| F | 20 | 1 |

Cadenas (columna "Prec"): `C-A-B`, `E-F` y `D` (trabajo suelto).

**Método:** si una cadena debe terminarse una vez iniciada, se programa primero la de mayor $\sum W_j/\sum P_j$ (L17, p. 15).

| Cadena | Fórmula | $\sum W/\sum P$ |
|---|---|---|
| C-B-A | `=(C5+C4+C3)/(B5+B4+B3)` = 6/17 | 0.3529 |
| E-F | `=(C7+C8)/(B7+B8)` = 6/33 | 0.1818 |
| D | `=C6/B6` = 2/30 | 0.0667 |

"Se inicia con la cadena que tiene la mayor relación" → **Respuesta: C-B-A-E-F-D**.

#### Bloque 2 (filas 15-29): "Si SI se pueden romper las cadenas" (factor $\rho$)

| Cadena | Prefijo | Fórmula | Valor |
|---|---|---|---|
| C-B-A | hasta C | `=C19/B19` = 3/11 | 0.2727 |
| C-B-A | hasta B | `=(C19+C18)/(B19+B18)` = 5/15 | 0.3333 |
| C-B-A | hasta A | `=(C19+C18+C17)/(B19+B18+B17)` = 6/17 | **0.3529** → $l^*=A$, "ρ-factor = 0,35" |
| E-F | hasta E | `=C21/B21` = 5/13 | **0.3846** → $l^*=E$, "ρ-factor = 0,38" |
| E-F | hasta F (rotulado "l=E") | `=(C21+C22)/(B21+B22)` = 6/33 | 0.1818 |

La hoja no escribe la secuencia final. Continuación propia con la regla de L17 (p. 17): primero E ($\rho=0.385$); luego C-B-A completa ($\rho=0.353$ frente a F $=1/20=0.05$ y D $=0.067$); luego D ($0.067>0.05$) y al final F. Secuencia deducida: **E-C-B-A-D-F**.

#### Bloque 3 (filas 31-54): "1|Prec|ΣCj/ΣWj*Cj", preemption con liberaciones

Es el ejercicio de L17, p. 25 ($1|r_j,prmp|\sum w_jC_j$), con **$W_j=1$** para todos (celda `J32`). Entonces la regla "mayor $w_j$ / tiempo restante" equivale a escoger el menor tiempo restante.

| Trabajo | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| $P_j$ | 6 | 18 | 12 | 10 | 10 | 17 | 16 |
| $R_j$ | 0 | 0 | 0 | 14 | 25 | 25 | 50 |
| $W_j/P_j$ (`L33:L39 = J32/P`) | 0.1667 | 0.0556 | 0.0833 | 0.1 | 0.1 | 0.0588 | 0.0625 |

Decisiones por evento (columna B = `MAX` de las razones de los disponibles; C = elegido):

| $t$ | Disponibles | Máx. $W/P$ | Elegido | Nota de la hoja |
|---|---|---|---|---|
| 0 | 1, 2, 3 | 0.1667 | 1 | "se mueve el reloj t"; termina en t=6 |
| 6 | 2, 3 | 0.0833 | 3 | "el 3 no se termina (interrumpido por la llegada del 4)"; "3\*=12-8=2" |
| 14 | 2, 3\*, 4 | 0.5 | 3\* | termina en t=18; próxima llegada t=25 |
| 18 | 2, 4 | 0.1 | 4 | "el 4 no se termina (interrumpido por la llegada del 5 y 6)"; "4\*=10-7=3" |
| 25 | 2, 4\*, 5, 6 | 0.3333 | 4\* | (texto: "Terminación del trabajo (t=18)") |
| 28 | 2, 5, 6 | 0.1 | 5 | termina en t=38 |
| 38 | 2, 6 | 0.0588 | 6 | "el 6 no se termina (interrumpido por la llegada del 7)"; "6\*=17-12" |
| 50 (la hoja dice "t=38") | 2, 6\*, 7 | 0.2 | 6\* | |
| 55 | 2, 7 | 0.0625 | 7 | |
| (71) | 2 | — | 2 | celda `C54` = 2 |

**Imagen (Gantt a mano, anclado cerca de G40:S50):** una barra horizontal con eje 0 a 71, más una segunda fila para el trabajo 2. Notas: "si o si tiene que iniciar actividad 4" en t=14, "actividad 5,6" en t=25 y "actividad 7" en t=50. Unas llaves marcan que el trabajo 3 avanza 8 unidades (6→14) y el 4 avanza 7 (18→25).

| Trabajo | Inicio | Fin |
|---|---|---|
| 1 | 0 | 6 |
| 3 | 6 | 14 |
| 3\* (resto) | 14 | 18 |
| 4 | 18 | 25 |
| 4\* (resto) | 25 | 28 |
| 5 | 28 | 38 |
| 6 | 38 | 50 |
| 6\* (resto) | 50 | 55 |
| 7 | 55 | 71 |
| 2 | 71 | 89 (dibujado en otra fila, sin escala) |

**Resultados (cálculo propio, la hoja no los totaliza):** $C_1=6$, $C_3=18$, $C_4=28$, $C_5=38$, $C_6=55$, $C_7=71$, $C_2=89$. $\sum C_j=\sum w_jC_j=305$; tiempo de flujo total $\sum(C_j-r_j)=191$; $C_{max}=89$.

**Conclusión:** el trabajo más largo (2, con $p=18$ y $r=0$) queda de último porque siempre aparece otro con menor tiempo restante. En las tres llegadas ($t=14$, 25 y 50) se revisa la prioridad, pero el trabajo en proceso sigue: le queda poco y su razón es la mayor. Por eso, en este caso, la *preemption* no llega a cambiar de trabajo.

---

### Hoja `Tardanza Máxima`

**Objetivo (deducido):** evaluar una permutación de 20 trabajos para optimizarla después con Solver Evolutionary y la restricción "todos diferentes", como en la p. 48 de L17. El nombre de la hoja dice "Tardanza Máxima", pero no hay fechas de entrega: lo que se calcula es un "Tiempo de Flujo Ponderado".

**Datos** (columnas A-C). $P_j$ y $W_j$ de los trabajos 17-20 son `=RANDBETWEEN(10,50)`: cambian en cada recálculo; los valores de abajo son los que guardó Excel. Los trabajos 1-16 son valores fijos.

| Trabajo | $P_j$ | $W_j$ | | Trabajo | $P_j$ | $W_j$ |
|---|---|---|---|---|---|---|
| 1 | 10 | 12 | | 11 | 15 | 33 |
| 2 | 36 | 22 | | 12 | 41 | 44 |
| 3 | 36 | 23 | | 13 | 21 | 17 |
| 4 | 26 | 11 | | 14 | 24 | 36 |
| 5 | 48 | 40 | | 15 | 24 | 31 |
| 6 | 11 | 46 | | 16 | 14 | 22 |
| 7 | 23 | 37 | | 17 | 42 | 45 |
| 8 | 49 | 48 | | 18 | 46 | 36 |
| 9 | 21 | 24 | | 19 | 38 | 24 |
| 10 | 47 | 16 | | 20 | 48 | 47 |

**Secuencia** (F2:F21): 18, 19, 7, 2, 14, 17, 16, 5, 11, 6, 4, 8, 15, 20, 1, 13, 9, 3, 12, 10.

**Método:** `G = VLOOKUP(ROUND(F,0), A:B, 2)` trae el $P_j$ del trabajo en esa posición; la columna se rotula "Cj", pero no es un tiempo de terminación. `H = VLOOKUP(ROUND(F,0), A:C, 3)` trae $W_j$. `J3 = SUMPRODUCT(G2:G21, H2:H21)` = **20197**, rotulado "Tiempo de Flujo Ponderado". El `ROUND` sugiere que la secuencia la escriben variables continuas de Solver (deducido).

**Resultado y corrección (cálculo propio):**

- $20197=\sum_j p_jw_j$ es una constante: no depende de la secuencia, así que Solver no puede mejorarla.
- El $\sum w_jC_j$ real de la secuencia guardada, con $C_{[k]}=\sum_{i\le k}p_{[i]}$, es **192388** ($C_{max}=620$).
- El óptimo para $1||\sum w_jC_j$ (WSPT) es **151038**, con el orden 6, 11, 7, 16, 14, 15, 1, 9, 12, 17, 8, 20, 5, 13, 18, 3, 19, 2, 4, 10.

---

### Observaciones

- **`Reglas de Despacho`, J21:** `=AVERAGE(E22:E27)` omite la fila 21 e incluye la 27, que está vacía. Da 28.8; el promedio correcto de $C_j$ es 26.
- **`Reglas de Despacho`, E49 y E74:** `=C49` y `=C74` reinician el reloj en el trabajo 6. Probablemente se copió la fila de un bloque donde el 6 iba primero (SPT/WSPT; deducido). Esto altera $C_j$, $\sum C_j/n$, $\sum w_jC_j$ y, en el bloque H, la tardanza del trabajo 3. Ver las tablas corregidas arriba.
- **Número de tardíos** (J14, J23, J31, J39, J47, J73): escrito a mano, no calculado. Los valores coinciden con los programas correctos.
- **Bloque A:** los setups $s_j$ (3 h y 30 min) no se usan en los $C_j$. Las fechas de entrega están en texto o como fecha (19-oct), así que no se calcula tardanza. La máquina queda ociosa de 0 a 50 aunque Seminario ($r=0$) y Proyecto ($r=24$) estaban disponibles: no es un programa sin retrasos. El "Tiempo de Flujo" de la columna L es un promedio de $w_jC_j$, no una suma.
- **`Restricciones de Precedencia`:** la cadena se escribe `C-A-B` en los datos y `C-B-A` en los cálculos y la respuesta. La razón de la cadena completa no cambia, pero el orden interno sí. F26 se rotula "l=E" cuando es el prefijo hasta F. El título "1|Prec|ΣCj" usa pesos, así que en realidad es $\sum w_jC_j$. El bloque 3 se titula "1|Prec|…" pero es $1|r_j,prmp|\sum w_jC_j$.
- **Bloque 3, errores de texto:** "3\*=12-8=2" debería ser 4 (y `B40` usa $1/2=0.5$ en vez de $1/4$; la decisión no cambia). "Terminación del trabajo (t=18)" en E45 debería ser t=28. "en t=38" en D50 debería ser t=50, y E51 debería decir t=55.
- **`Tardanza Máxima`:** el nombre no corresponde al cálculo. La fórmula objetivo es invariante a la secuencia. `RANDBETWEEN` hace que los trabajos 17-20 cambien al recalcular.
- No hay hojas vacías ni gráficos de Excel.
