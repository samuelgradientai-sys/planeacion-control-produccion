# Programación de una máquina (Corte 3)

## Qué cubre

Secuenciación de $n$ trabajos en una sola máquina ($1|\beta|\gamma$). Incluye las reglas de despacho estáticas (FIFO, SPT, EDD, WSPT) y dinámicas (holgura mínima MS, ATC, razón crítica CR), los casos con regla óptima conocida (WSPT para $\sum w_jC_j$, EDD para $L_{max}$), las precedencias en cadena con factor $\rho$, la *preemption* con liberaciones, el algoritmo de Lawler ($h_{max}$), el de Moore-Hodgson ($\sum U_j$) y el uso de Solver de Excel como método aproximado.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [L17-single-machine-scheduling.md](./L17-single-machine-scheduling.md) (gemelo del PDF) | Presentación "Lec 17 - Single Machine Scheduling", 49 diapositivas, con todas las secuencias y Gantt en tablas y un resumen con la comparación de reglas | **Sí (1.º)** |
| [ejemplo-1-programacion-produccion.md](./ejemplo-1-programacion-produccion.md) (gemelo del .xlsx) | Ejemplo cotidiano de 4 actividades con $r_j$, $p_j$, $w_j$ y $s_j$: $C_j$, flujo y $w_jC_j$ | 2.º (corto) |
| [programacion-produccion-una-maquina.md](./programacion-produccion-una-maquina.md) (gemelo del .xlsx) | Libro de clase con 3 hojas: reglas de despacho sobre 6 trabajos (natural, azar, SPT, WSPT, EDD, MS), cadenas y factor $\rho$, preemption (ejercicio p. 25 de L17) y una hoja para Solver | 3.º |
| [programacion-produccion-una-maquina-datos/Reglas_de_Despacho.csv](./programacion-produccion-una-maquina-datos/Reglas_de_Despacho.csv) | Volcado CSV completo de la hoja `Reglas de Despacho` | Solo como referencia |
| [atc.py](./atc.py) | Script de Python (sin gemelo) que aplica la regla ATC al ejercicio de L17 (pp. 43-45) y verifica la solución de clase. Se explica abajo | 4.º |

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

1. [L17](./L17-single-machine-scheduling.md), pp. 2-13: motivación ($n!$), WSPT, reglas estáticas y dinámicas (MS, ATC).
2. [ejemplo-1](./ejemplo-1-programacion-produccion.md): calcular $C_j$ con liberaciones.
3. [programacion-produccion-una-maquina](./programacion-produccion-una-maquina.md), hoja `Reglas de Despacho`: comparar las reglas sobre 6 trabajos.
4. L17, pp. 14-26, y la hoja `Restricciones de Precedencia`: cadenas, factor $\rho$ y preemption.
5. L17, pp. 27-42: Lawler, EDD, CR paso a paso, Moore-Hodgson y la regla para $\sum T_j$.
6. L17, pp. 43-45, y `atc.py`: ejercicio FIFO/SPT/EDD/ATC.
7. L17, pp. 46-48, y la hoja `Tardanza Máxima`: métodos exactos y Solver.

## Conceptos y fórmulas clave

Detalle en el [resumen de L17](./L17-single-machine-scheduling.md#resumen).

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
| FIFO, SPT, EDD y ATC con 4 trabajos ($p$ = 5, 7, 2, 8; $d$ = 1, 9, 10, 6; $w$ = 2, 3, 2, 1) | [L17](./L17-single-machine-scheduling.md) pp. 43-45; [atc.py](./atc.py) | FIFO: 13.25 / 16 / 41; SPT: **11.25** / 16 / 43; EDD: 15 / **12** / 72; ATC: 12 / 16 / **39** (flujo promedio / $L_{max}$ / $\sum w_jT_j$) |
| Razón crítica con los mismos 4 trabajos | L17 pp. 33-37 | 1-4-3-2: flujo 13.75, $L_{max}=13$, $\sum w_jT_j=64$ |
| Cadenas 1→2→3→4 y 5→6→7 (factor $\rho$) | L17 pp. 18-23 | 1-2-5-6-3-7-4 |
| Lawler con $h_1=1+C_1$, $h_2=1.2C_2$, $h_3=10$ | L17 pp. 29-31 | 1-2-3 o 2-1-3, $h_{max}=10$ |
| Moore-Hodgson, 5 trabajos | L17 pp. 40-41 | 3-4-5-1-2, $\sum U_j=2$ |
| WSPT, tareas A-E | L17 p. 10 (resuelto en el .md) | A-D-E-B-C, $\sum w_jC_j=779$ |
| 6 trabajos con natural, azar, SPT, WSPT, EDD y MS | [programacion-produccion-una-maquina](./programacion-produccion-una-maquina.md) | WSPT 6-5-2-4-1-3 da el menor $\sum w_jC_j$ (161); SPT el menor $\sum C_j/n$ (16); EDD el menor $L_{max}$ (7); MS da $\sum T_j=16$ |
| Cadenas A-F (sin y con interrupción) | ídem, hoja `Restricciones de Precedencia` | Sin romper: C-B-A-E-F-D; con $\rho$: $l^*$ = A (0.35) y E (0.38) |
| Preemption con $r_j$ (L17 p. 25), $w_j=1$ | ídem, hoja `Restricciones de Precedencia` | 1, 3, 4, 5, 6, 7, 2; $C_{max}=89$, $\sum C_j=305$ |
| 4 actividades cotidianas con $r_j$ | [ejemplo-1](./ejemplo-1-programacion-produccion.md) | Flujo promedio 35.165 h |
| Solver Evolutionary para $1\|\|\sum w_jT_j$ (wt40_1) | L17 p. 48; hoja `Tardanza Máxima` | Captura: $\sum w_jT_j=16822$ (óptimo conocido 913) |

Varias hojas del Excel tienen errores de fórmula (reloj reiniciado en EDD, rango mal tomado en un promedio, objetivo constante en `Tardanza Máxima`). Están señalados y corregidos en [programacion-produccion-una-maquina](./programacion-produccion-una-maquina.md#observaciones).

## Relación con otros temas y proyectos

- Antes: [01-introduccion-scheduling](../01-introduccion-scheduling/README.md), con la notación $\alpha|\beta|\gamma$ y los indicadores.
- Después: [03-maquinas-paralelas](../03-maquinas-paralelas/) (extiende SPT/LPT a $Pm$), [04-flow-shop](../04-flow-shop/) y [05-job-shop](../05-job-shop/).
- Compendio con hojas `02_1Maq_Basicos`, `03_1Maq_MS_ATC`, `04_1Maq_Precedencia`, `05_1Maq_Preemption` y `06_1Maq_Lawler`: [metodos-programacion-produccion-corte3](../00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md).
- Proyecto: el reto 2 de la [competencia](../proyecto-competencia-scheduling/solucion/README.md) ($P3|r_j,prec|\sum w_jT_j$) usa WSPT, ATC, cadenas y EDD como reglas de arranque.
- Corte 2: la regla de "inicio en $\max(r_j, C_{\text{anterior}})$" se parece al backward/forward scheduling de [05-mrp-ii-y-capacidad](../../corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/).
