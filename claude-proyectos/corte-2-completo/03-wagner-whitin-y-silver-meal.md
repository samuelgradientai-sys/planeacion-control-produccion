<!-- fuente: corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/README.md -->
# Wagner-Whitin y Silver-Meal (Corte 2)

## Qué cubre

Dimensionamiento de lotes (*lot sizing*) con demanda dinámica y determinística en un horizonte finito: cuánto y cuándo producir para minimizar alistamiento + producción + inventario. El algoritmo de Wagner-Whitin (1958) da el óptimo exacto como una ruta más corta / programación dinámica; la heurística de Silver-Meal da un plan rápido de bajo costo sin garantizar el óptimo. Es la técnica con la que se dimensionan las liberaciones de órdenes del MRP ([carpeta 04](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/README.md)).

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [L12-wagner-whitin-and-silver-meal.md](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/L12-wagner-whitin-and-silver-meal.md) | Presentación de clase (40 pp.): supuestos, propiedad de optimalidad, grafo de ruta más corta, recursión $Z_k$, ejemplo de 4 periodos resuelto con Wagner-Whitin y Silver-Meal. | Sí |
| [wagner_whitin.py](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/wagner_whitin.py) | Script de Python (sin gemelo `.md`; se explica abajo) que aplica la recursión de Wagner-Whitin a 10 semanas de requerimientos netos de un componente del esfero. | Después de la L12 |

### `wagner_whitin.py` en detalle

**Qué hace.** Resuelve un problema de tamaño de lote con Wagner-Whitin, imprime la recursión $Z_j$ con todos sus candidatos (marca el mínimo con `<-- min`), reconstruye el plan de producción y lo muestra con su costo por periodo. Solo usa Python estándar (sin librerías externas).

**Notación del código** (periodos indexados desde 0; el periodo $t$ del código es la semana $t+1$):

- $Z_j$: costo mínimo para cubrir la demanda de los periodos $0..j-1$; $Z_0=0$.
- $C_{ij}$: costo de producir en el periodo $i$ toda la demanda de los periodos $i..j-1$:

$$C_{ij}=\text{setup}_i+c_i\sum_{k=i}^{j-1}d_k+\sum_{k=i+1}^{j-1}d_k\sum_{s=i}^{k-1}h_s$$

  donde $d_k$ es la demanda neta del periodo $k$, $\text{setup}_i$ el costo de alistamiento, $c_i$ el costo variable unitario y $h_s$ el costo de mantener una unidad al final del periodo $s$ (la demanda del periodo $k$ se guarda desde $i$ hasta $k-1$).
- Recursión: $Z_j=\min_{i<j}\{Z_i+C_{ij}\}$, que equivale a la de la L12, $Z_k=\min_{0\le j\le k-1}[Z_j^*+C_{jk}]$, desplazada un índice.

**Entradas** (fijas en el código, "Datos del ejercicio (cuerpo)"):

| Variable | Valor | Significado |
|---|---|---|
| `demanda` | `[0, 0, 2380, 0, 2500, 0, 0, 0, 0, 0]` | Requerimientos netos de las semanas 1 a 10 |
| `setup` | `[80]*10` | \$80 por lote |
| `c_var` | `[0]*10` | Sin costo variable |
| `h` | `[0.01]*10` | \$0.01 por unidad y semana |

*Deducido:* esos requerimientos netos (2380 en la semana 3 y 2500 en la semana 5) coinciden exactamente con los de la **Tapa Arriba** en [mrp-esfero-v2](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero-v2.md) (requerimiento bruto de 2460 en la semana 3 menos las 80 unidades disponibles, y 2500 en la semana 5). El costo de mantener 0.01 es el de la Tapa Arriba en ese Excel y el alistamiento de \$80 es el del Esfero y el Cuerpo. El comentario del código dice "cuerpo". El script no maneja tiempos de entrega: dimensiona lotes sobre los requerimientos netos (producción = recepción en ese periodo).

**Funciones:**

1. `costo_lote(i, j)`: calcula $C_{ij}$ con la fórmula anterior. **Siempre suma `setup[i]`, aunque el lote sea de 0 unidades.**
2. `wagner_whitin()`: arma el diccionario de todos los $C_{ij}$ ($0\le i<j\le n$), recorre $j=1..n$, guarda $Z_j$ y el $i$ óptimo (`mejor_i`), imprime cada paso y reconstruye el plan hacia atrás: desde $j=n$, `produccion[i] = sum(demanda[i:j])` y salta a $j=i$.
3. `mostrar_plan(produccion)`: simula el inventario final de cada periodo, cobra alistamiento solo si se produce algo, costo variable y mantenimiento $h_t\cdot I_t$ con el inventario final, e imprime la tabla y el costo total.

**Resultado al ejecutarlo** (`python -I wagner_whitin.py`, Python estándar, sin instalar nada):

| $j$ | $Z_j$ | $i$ óptimo |
|---|---|---|
| 1 | 80 | 0 |
| 2 | 80.0 | 0 |
| 3 | 127.6 | 0 |
| 4 | 127.6 | 0 |
| 5 a 10 | 207.6 | 4 |

Plan que imprime (los periodos aparecen numerados del 0 al 9):

| Periodo (semana) | Demanda | Producción | Inv. final | Setup | Variable | Mantener |
|---|---|---|---|---|---|---|
| 0 (1) | 0 | 2380 | 2380 | 80 | 0 | 23.8 |
| 1 (2) | 0 | 0 | 2380 | 0 | 0 | 23.8 |
| 2 (3) | 2380 | 0 | 0 | 0 | 0 | 0.0 |
| 3 (4) | 0 | 0 | 0 | 0 | 0 | 0.0 |
| 4 (5) | 2500 | 2500 | 0 | 80 | 0 | 0.0 |
| 5-9 (6-10) | 0 | 0 | 0 | 0 | 0 | 0.0 |

**Costo total = \$207.6.** En una consola de Windows con codificación cp1252, las tildes del título ("Plan óptimo de producción") pueden verse mal; es solo un problema de visualización.

**Error del script (verificado).** Como `costo_lote` cobra el alistamiento aunque el lote sea de 0 unidades, las semanas iniciales sin demanda "obligan" a pagar \$80 ($Z_1=Z_2=80$). Por eso la recursión descarta producir en la semana 3 y el plan sale **subóptimo**. El óptimo verdadero es producir **4880 unidades en la semana 3** (2380 para esa semana + 2500 guardadas 2 semanas): $80+2500\cdot0.01\cdot2=\mathbf{\$130}$. Lo confirmé con una enumeración exhaustiva de todos los planes y con el mismo algoritmo corregido. La corrección es devolver 0 en `costo_lote` cuando `sum(demanda[i:j]) == 0`, o empezar la recursión en el primer periodo con demanda positiva. Con los datos de la L12 (demandas sin ceros), el algoritmo del script sí reproduce el resultado de la clase: $Z_4=380$ y producción 10, 30, 50, 0.

**Convenciones de costo distintas.** El script cobra el mantenimiento sobre el **inventario final** de cada periodo. Los Excel del MRP del esfero lo cobran sobre el **inventario al inicio** del periodo. Por eso los costos no son directamente comparables.

## Orden de estudio sugerido

1. [L12](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/L12-wagner-whitin-and-silver-meal.md), pp. 1-16: supuestos, propiedad $I_{t-1}P_t=0$, grafo y recursión.
2. [L12](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/L12-wagner-whitin-and-silver-meal.md), pp. 17-33: ejemplo numérico completo (costos de arco y $Z_1..Z_4$).
3. [L12](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/L12-wagner-whitin-and-silver-meal.md), pp. 34-40: Silver-Meal sobre el mismo ejemplo.
4. `wagner_whitin.py` (esta página): implementación y su error con periodos de demanda cero.
5. Aplicación en el MRP: [L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md), pp. 13-14, y [mrp-esfero-v2](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero-v2.md).

## Conceptos y fórmulas clave

- Costo de producción: $k(p_t)=0$ si $p_t=0$; $k(p_t)=A_t+c\,p_t$ si $p_t>0$ ($A_t$: alistamiento, $c$: costo variable, $p_t$: producción).
- Propiedad de optimalidad: $I_{t-1}P_t=0$, por lo que $P_t\in\{0, D_t, D_t+D_{t+1},\dots\}$.
- Costo de arco: $C_{jk}=A_{j+1}+cP_{j+1}+\sum_{t=j+1}^{k-1}h_tI_t$ (producir en $j+1$ para cubrir $j+1..k$).
- Recursión: $Z_k=\min_{0\le j\le k-1}[Z_j^*+C_{jk}]$, $Z_0^*=0$.
- Silver-Meal (forma usual, coherente con los ejemplos): $K(t,p)=\dfrac{\text{costo total del lote que cubre } t..p}{p-t+1}$; se amplía el lote mientras $K$ baje.

Detalle y símbolos en el [resumen de la L12](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/L12-wagner-whitin-and-silver-meal.md#resumen).

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado principal |
|---|---|---|
| Wagner-Whitin, 4 periodos ($D$ = 10, 30, 30, 20; setup 20, 40, 30, 50; $c=3$; $h$ = 2, 2, 1, 1) | [L12](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/L12-wagner-whitin-and-silver-meal.md), pp. 15-33 | $Z_4=380$; producir 10, 30, 50, 0 |
| Silver-Meal, mismo ejemplo | [L12](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/L12-wagner-whitin-and-silver-meal.md), pp. 37-39 | Lotes en los periodos 1, 2 y 3 (3+4); *deducido:* costo 380, igual al óptimo |
| Wagner-Whitin, 10 semanas de un componente del esfero | [wagner_whitin.py](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/wagner_whitin.py) | Imprime \$207.6 (subóptimo por el error descrito); el óptimo real es \$130 |

## Relación con otros temas y proyectos

- [04 BOM y MRP](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/README.md): el MRP calcula requerimientos netos; Wagner-Whitin y Silver-Meal deciden cómo agruparlos en lotes ([L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md), p. 14).
- [02 Agregación y desagregación](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/) y [01 Planeación agregada](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/): niveles de planeación previos que fijan el programa maestro.
- [Parcial 2](/corte-2-planeacion-agregada-mrp/parcial-2/parcial-2-solucion.md): punto 2.4, Silver-Meal contra Wagner-Whitin.
- [Proyecto THYMS, gemelo digital](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/THYMS-presentacion-corte-2.md): propone aplicar Wagner-Whitin / Silver-Meal sobre el programa maestro como siguiente paso.


---

<!-- fuente: corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/L12-wagner-whitin-and-silver-meal.md -->
# L12-wagner-whitin-and-silver-meal

> **Archivo:** [`L12-wagner-whitin-and-silver-meal.pdf`](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/L12-wagner-whitin-and-silver-meal.pdf) · **Corte 2** · 40 páginas  
> **Nombre original:** `CORTE 2/Lec 12 - Wagner Within and Silver meal heuristics.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** dimensionamiento de lotes (*lot sizing*) con demanda dinámica determinística: algoritmo exacto de Wagner-Whitin (1958) y heurística de Silver-Meal, ambos aplicados al mismo ejemplo de 4 periodos.

### Ideas clave

- El problema de planeación responde dos preguntas: **cuánto** y **cuándo** producir (p. 2).
- Supuestos de Wagner-Whitin (p. 3): no se permiten faltantes (*no backlogging*), horizonte de planeación finito y se consideran costos fijos (alistamiento, *setup*) y variables de producción, además del costo de mantener inventario.
- **Propiedad de la solución óptima** (p. 4): nunca se produce en un periodo si se llega a él con inventario ($I_{t-1}P_t=0$). Por eso cada lote cubre exactamente la demanda de un número entero de periodos consecutivos: $P_t\in\{0,\ D_t,\ D_t+D_{t+1},\ \dots\}$. Decidir el plan equivale a decidir **para cuántos periodos** se aprovisiona en cada producción.
- Esa propiedad convierte el problema en un **problema de ruta más corta** sobre un grafo acíclico con nodos $0,1,\dots,T$ (pp. 5-13): el arco $j\to k$ significa "producir en el periodo $j+1$ la demanda de los periodos $j+1,\dots,k$" y su costo es $C_{jk}$. Se reduce mucho el número de soluciones por explorar.
- La solución se obtiene con programación dinámica hacia adelante: $Z_k$ es el costo mínimo para cubrir los periodos $1..k$ (pp. 16, 27-32).
- **Silver-Meal** (pp. 34-39) es una heurística más rápida: desde el periodo $t$ va agrandando el lote mientras baje el **costo promedio por periodo**, y se detiene en el primer aumento. No garantiza el óptimo, pero da soluciones de bajo costo.

### Fórmulas y métodos

**Costo de producción en un periodo** (p. 3):

$$k(p_t)=\begin{cases}0, & \text{si } p_t=0\\ A_t+c\,p_t, & \text{si } p_t>0\end{cases}$$

donde $p_t$ es la cantidad producida en el periodo $t$, $A_t$ el costo fijo de alistamiento (*set up*) del periodo $t$ y $c$ el costo variable unitario.

**Propiedad de optimalidad** (p. 4): $I_{t-1}P_t=0$ y $P_t\in\{0,\ D_t,\ D_t+D_{t+1},\ D_t+D_{t+1}+D_{t+2},\ \dots,\ \sum_t D_t\}$, con $I_{t-1}$ el inventario al final del periodo $t-1$, $P_t$ la producción y $D_t$ la demanda del periodo $t$.

**Costo de un arco** (p. 14): $C_{jk}$ es el costo de producir (y almacenar) en el periodo $j+1$ para satisfacer la demanda de los periodos $j+1,\dots,k$:

$$C_{jk}=A_{j+1}+c\,P_{j+1}+\sum_{t=j+1}^{k-1}h_t I_t$$

con $P_{j+1}=\sum_{t=j+1}^{k}D_t$ (tamaño del lote), $I_t=\sum_{i=t+1}^{k}D_i$ (inventario al final del periodo $t$ que se arrastra para los periodos siguientes) y $h_t$ el costo de mantener una unidad al final del periodo $t$. En la práctica, la demanda del periodo $i$ paga $D_i\sum_{s=j+1}^{i-1}h_s$.

**Recursión de Wagner-Whitin** (p. 16):

$$Z_k=\min_{0\le j\le k-1}\left[Z_j^*+C_{jk}\right],\qquad k=1,2,\dots,T,\qquad Z_0^*=0$$

$Z_k$ es el costo mínimo de cubrir la demanda de los periodos $1..k$; el $j$ que da el mínimo indica que el último lote se produce en el periodo $j+1$. El plan se reconstruye hacia atrás desde $Z_T$. Se usa cuando se quiere el **óptimo exacto** con horizonte fijo y demanda conocida.

**Silver-Meal** (p. 36), tal como aparece en la diapositiva: para cada periodo $t=1,\dots,m$ y cada periodo futuro $p=t,\dots,m$:

$$P(t)=\sum_{i=t}^{p}D_i,\qquad K(t)=\frac{P(t)}{p-t}$$

"Elegir el tamaño de lote de costo mínimo". En los ejemplos (pp. 37-39) el numerador que realmente se usa es el **costo total** del lote (alistamiento + variable + mantenimiento) y el denominador es el **número de periodos cubiertos** ($p-t+1$). La forma usual, coherente con esos ejemplos, es:

$$K(t,p)=\frac{A_t+c\sum_{i=t}^{p}D_i+\sum_{i=t+1}^{p}D_i\sum_{s=t}^{i-1}h_s}{p-t+1}$$

Se aumenta $p$ mientras $K(t,p)$ disminuya; cuando aumenta, el lote se cierra en el $p$ anterior y se vuelve a empezar en el periodo siguiente. Se usa cuando se necesita rapidez o un horizonte rodante, aceptando no garantizar el óptimo.

### Ejemplos resueltos

Datos comunes (p. 15): 4 periodos, $c=3$.

| Periodo | Demanda | Set up [$] | c. variable | h(t) |
|---|---|---|---|---|
| 1 | 10 | 20 | 3 | 2 |
| 2 | 30 | 40 | 3 | 2 |
| 3 | 30 | 30 | 3 | 1 |
| 4 | 20 | 50 | 3 | 1 |

- **Wagner-Whitin** (pp. 17-33): costos de los 10 arcos $C_{01}=50$, $C_{02}=200$, $C_{03}=410$, $C_{04}=570$, $C_{12}=130$, $C_{13}=280$, $C_{14}=400$, $C_{23}=120$, $C_{24}=200$, $C_{34}=110$. Recursión: $Z_1=50$, $Z_2=180$, $Z_3=300$, $Z_4=380$. Ruta óptima $0\to1\to2\to4$: producir 10 en el periodo 1, 30 en el periodo 2, 50 en el periodo 3 y 0 en el periodo 4. **Costo mínimo = 380.**
- **Silver-Meal** (pp. 37-39): periodo 1: \$50/mes (solo D1) contra \$100/mes (D1+D2), se cierra el lote en 10; periodo 2: \$130/mes contra \$140/mes, se cierra el lote en 30; periodo 3: \$120/mes contra \$105/mes (D3+D4), se produce 50 en el periodo 3. La p. 40 deja la pregunta "¿Solución con Silver Meal?" sin respuesta. *Deducido:* el plan Silver-Meal es 10, 30, 50, 0, el mismo de Wagner-Whitin, con costo 50 + 130 + 200 = **380** (ver la observación sobre la p. 39).

### Páginas clave

- p. 3: supuestos y función de costo $k(p_t)$.
- p. 4: propiedad de la solución óptima.
- pp. 5-13: construcción del grafo de ruta más corta.
- p. 14: costo de arco $C_{jk}$; p. 16: recursión $Z_k$.
- pp. 15, 17-26: cálculo de los 10 costos de arco.
- pp. 27-32: recursión paso a paso; p. 32 marca la ruta óptima; p. 33: plan óptimo.
- pp. 34-39: Silver-Meal (definición y ejemplo); p. 40: pregunta abierta.

### Observaciones sobre el material

- p. 36: la fórmula $K(t)=P(t)/(p-t)$ se divide por cero cuando $p=t$ y define $P(t)$ como suma de demandas, aunque se usa como costo. Los ejemplos de las pp. 37-39 dividen el costo total por el número de periodos cubiertos ($p-t+1$).
- p. 39: "Producir en 3 D3 + D4 = \$30 + \$3*50 + 30*\$1 = \$210: \$105/mes". El término de mantenimiento debería ser $20\times\$1$ (se guarda $D_4=20$ un periodo), es decir, \$200 y \$100/mes (así lo calcula $C_{24}=200$ en la p. 25). La decisión no cambia.
- p. 30: en el grafo de esa diapositiva no aparece la etiqueta 400 del arco $1\to4$ (sí aparece en las pp. 23-29).

### Relación con otros archivos del repo

- [`wagner_whitin.py`](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/wagner_whitin.py): implementación en Python de esta misma recursión; ver [README de la carpeta](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/README.md).
- [L14 MRP](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md): Wagner-Whitin y Silver-Meal aparecen como políticas de dimensionamiento de lotes para las liberaciones de órdenes del MRP (p. 14).
- [mrp-esfero-v2](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero-v2.md): MRP del esfero cuyas órdenes se dimensionan a mano; sus requerimientos netos alimentan el ejemplo del `.py`.
- [Parcial 2](/corte-2-planeacion-agregada-mrp/parcial-2/parcial-2-solucion.md): punto 2.4, Silver-Meal contra Wagner-Whitin.
- [Presentación THYMS del corte 2](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/THYMS-presentacion-corte-2.md): propone aplicar Wagner-Whitin / Silver-Meal sobre el programa maestro como siguiente paso.

## Contenido completo (página por página)

> Todas las diapositivas llevan a la derecha una franja con una foto del campus y el logo de la Universidad de La Sabana; no se repite en cada página.

### Página 1 — Production Planning Models

Portada. "Production Planning Models" / "Wagner Whitin Algorithm(1958)". Licencia Creative Commons BY-NC-SA (ícono) y logo de la Universidad de La Sabana.

### Página 2 — Planning problem

- How much to produce?
- When to produce?

> [Imagen decorativa: ingeniero con casco amarillo y libreta.]

### Página 3 — Assumptions

- No Backlogging
- Finite Planning Horizon
- Fixed and variable costs are considered

$$k(p_t)=\begin{cases}0, & si\ p_t=0\\ A_t+c\,p_t, & si\ p_t>0\end{cases}$$

### Página 4 — Optimal solution property

- Every optimal solution satisfies that:
  - $I_{t-1}P_t=0$
  - $P_t=0,\ D_t,\ D_t+D_{t+1},\ D_t+D_{t+1}+D_{t+2},\ \dots,\ \sum_t D_t$
- La solución se traduce en decidir la cantidad de periodos para los aprovisiono el inventario en cada periodo.

### Página 5 — Graph of the problem

- Problem with 4 periods

> [Diagrama: cinco nodos en línea, 0, 1, 2, 3 y 4, sin arcos.]

### Página 6 — Graph of the problem

- Problem with 4 periods
- Producir en periodo 1 la demanda de periodo 1.

> [Diagrama: nodos 0-4; aparece el arco 0→1.]

### Página 7 — Graph of the problem

- Problem with 4 periods
- Producir en periodo 1 la demanda de periodo 1 y 2.

> [Diagrama: arcos 0→1 y 0→2.]

### Página 8 — Graph of the problem

- Problem with 4 periods
- Producir en periodo 1 la demanda de periodo 1, 2 y 3.

> [Diagrama: arcos 0→1, 0→2 y 0→3.]

### Página 9 — Graph of the problem

- Problem with 4 periods
- Producir en periodo 1 la demanda de periodo 1, 2, 3 y 4.

> [Diagrama: arcos 0→1, 0→2, 0→3 y 0→4.]

### Página 10 — Graph of the problem

- Problem with 4 periods
- Producir en periodo 2 la demanda de periodo 2.

> [Diagrama: arcos 0→1, 0→2, 0→3, 0→4 y 1→2.]

### Página 11 — Graph of the problem

- Problem with 4 periods
- Producir en periodo 2 la demanda de periodo 2 y 3.

> [Diagrama: se agrega el arco 1→3 (dibujado por debajo de los nodos).]

### Página 12 — Graph of the problem

- Problem with 4 periods
- Producir en periodo 2 la demanda de periodo 2, 3, y 4.

> [Diagrama: se agrega el arco 1→4.]

### Página 13 — Graph of the problem

- Problem with 4 periods
- ¡Problema de ruta más corta!
- ¡Se reducen el número de soluciones por explorar!

> [Diagrama: grafo completo con los 10 arcos $j\to k$, $j<k$: 0→1, 0→2, 0→3, 0→4, 1→2, 1→3, 1→4, 2→3, 2→4, 3→4. El arco $j\to k$ representa producir en el periodo $j+1$ la demanda de los periodos $j+1$ a $k$.]

### Página 14 — Formulación

- $C_{jk}$ = costo de producir y almacenar en el periodo $j+1$ para satisfacer la demanda en $j+1, j+2, \dots, k$

$$C_{jk}=A_{j+1}+cP_{j+1}+\sum_{t=j+1}^{k-1}h_t I_t$$

### Página 15 — Ejemplo numérico

| Periodo | Demanda | Set up [$] | c. variable | h(t) |
|---|---|---|---|---|
| 1 | 10 | 20 | 3 | 2 |
| 2 | 30 | 40 | 3 | 2 |
| 3 | 30 | 30 | 3 | 1 |
| 4 | 20 | 50 | 3 | 1 |

> [Diagrama: el grafo completo de la p. 13 (nodos 0-4, 10 arcos), todavía sin costos.]

### Página 16 — Formulación

- La solución óptima es una función recursiva:

$$Z_k=\min_{0\le j\le k-1}\left[Z_j^*+C_{jk}\right],\quad k=1,2,\dots T$$

$Z^*_0=0$

### Página 17 — Ejemplo numérico

Tabla de datos de la p. 15.

$C_{01} = 20 + 10\cdot 3 = 50$

> [Diagrama: grafo completo; el arco 0→1 tiene la etiqueta 50.]

### Página 18 — Ejemplo numérico

Tabla de datos de la p. 15.

$C_{02} = 20 + (10 + 30)\cdot 3 + 30\cdot 2 = 200$

> [Diagrama: etiquetas 0→1 = 50 y 0→2 = 200.]

### Página 19 — Ejemplo numérico

Tabla de datos de la p. 15.

$C_{03} = 20 + (10+30+30)\cdot 3 + 30\cdot 2 + 30\cdot(2+2) = 410$

> [Diagrama: etiquetas 0→1 = 50, 0→2 = 200 y 0→3 = 410.]

### Página 20 — Ejemplo numérico

Tabla de datos de la p. 15.

$C_{04} = 20 + (10+30+30+20)\cdot 3 + 30\cdot 2 + 30\cdot(2+2) + 20\cdot(2+2+1) = 570$

> [Diagrama: etiquetas 0→1 = 50, 0→2 = 200, 0→3 = 410 y 0→4 = 570.]

### Página 21 — Ejemplo numérico

Tabla de datos de la p. 15.

$C_{12} = 40 + 30\cdot 3 = 130$

> [Diagrama: se agrega la etiqueta 1→2 = 130.]

### Página 22 — Ejemplo numérico

Tabla de datos de la p. 15.

$C_{13} = 40 + (30+30)\cdot 3 + 30\cdot 2 = 280$

> [Diagrama: se agrega la etiqueta 1→3 = 280.]

### Página 23 — Ejemplo numérico

Tabla de datos de la p. 15.

$C_{14} = 40 + (30+30+20)\cdot 3 + 30\cdot 2 + 20\cdot(2+1) = 400$

> [Diagrama: se agrega la etiqueta 1→4 = 400.]

### Página 24 — Ejemplo numérico

Tabla de datos de la p. 15.

$C_{23} = 30 + 30\cdot 3 = 120$

> [Diagrama: se agrega la etiqueta 2→3 = 120.]

### Página 25 — Ejemplo numérico

Tabla de datos de la p. 15.

$C_{24} = 30 + (30+20)\cdot 3 + 20\cdot 1 = 200$

> [Diagrama: se agrega la etiqueta 2→4 = 200.]

### Página 26 — Ejemplo numérico

Tabla de datos de la p. 15.

$C_{34} = 50 + 20\cdot 3 = 110$

> [Diagrama: grafo con todos los costos de arco. Etiquetas de los arcos:]

| Arco | 0→1 | 0→2 | 0→3 | 0→4 | 1→2 | 1→3 | 1→4 | 2→3 | 2→4 | 3→4 |
|---|---|---|---|---|---|---|---|---|---|---|
| $C_{jk}$ | 50 | 200 | 410 | 570 | 130 | 280 | 400 | 120 | 200 | 110 |

### Página 27 — Ejemplo numérico

Tabla de datos de la p. 15.

**Solución:**

$$Z_1 = C_{01} = A_1 + c_1(D_1) = 20 + 3\cdot 10 = 50\ ^*$$

> [Diagrama: grafo con todos los costos; bajo los nodos, en rojo, $Z_0 = 0$ y $Z_1 = 50$.]

### Página 28 — Ejemplo numérico

Idéntica a la p. 27 (tabla de datos, $Z_1=C_{01}=A_1+c_1(D_1)=20+3\cdot10=50^*$, grafo con $Z_0=0$ y $Z_1=50$).

### Página 29 — Ejemplo numérico

Tabla de datos de la p. 15.

**Solución:**

$$Z_2=\begin{cases}Z_0+C_{02}=A_1+c_1(D_1+D_2)+h_1D_2=200\\ Z_1^*+C_{12}=50+A_2+c_2D_2=180^*\end{cases}$$

> [Diagrama: grafo con costos; etiquetas rojas $Z_0=0$, $Z_1=50$ y $Z_2=180$.]

### Página 30 — Ejemplo numérico

**Solución:**

$$Z_3=\begin{cases}Z_0+C_{03}=410\\ Z_1^*+C_{13}=330\\ Z_2^*+C_{23}=300^*\end{cases}$$

> [Diagrama: grafo con costos (en esta diapositiva no aparece la etiqueta 400 del arco 1→4); etiquetas rojas $Z_0=0$, $Z_1=50$, $Z_2=180$ y $Z_3=300$.]

### Página 31 — Ejemplo numérico

**Solución:**

$$Z_4=\begin{cases}Z_0+C_{04}=570\\ Z_1^*+C_{14}=450\\ Z_2^*+C_{24}=380^*\\ Z_3^*+C_{34}=410\end{cases}$$

> [Diagrama: grafo con costos; etiquetas rojas $Z_0=0$, $Z_1=50$, $Z_2=180$, $Z_3=300$ y $Z_4=380$.]

### Página 32 — Ejemplo numérico

Igual a la p. 31 (misma recursión de $Z_4$), pero en el grafo se resalta en rojo grueso la **ruta óptima** $0\to1$ (50), $1\to2$ (130) y $2\to4$ (200), que suma 380.

Resumen de la recursión de las pp. 27-32 (tabla agregada en esta transcripción, no está en la diapositiva):

| $k$ | Candidatos $Z_j^*+C_{jk}$ | $Z_k$ | Último lote |
|---|---|---|---|
| 1 | $0+50=50$ | 50 | periodo 1 |
| 2 | $0+200=200$; $50+130=180$ | 180 | periodo 2 |
| 3 | $0+410=410$; $50+280=330$; $180+120=300$ | 300 | periodo 3 |
| 4 | $0+570=570$; $50+400=450$; $180+200=380$; $300+110=410$ | 380 | periodo 3 (cubre 3 y 4) |

### Página 33 — Solución

| Periodo | Demanda | Set up [$] | c. variable | h(t) | Production |
|---|---|---|---|---|---|
| 1 | 10 | 20 | 3 | 2 | 10 |
| 2 | 30 | 40 | 3 | 2 | 30 |
| 3 | 30 | 30 | 3 | 1 | 50 |
| 4 | 20 | 50 | 3 | 1 | 0 |

(La columna "Production" está en rojo.)

### Página 34 — Production Planning Models: Silver–Meal heuristic

Separador: "Production Planning Models:" / "Silver–Meal heuristic". Foto del campus y logo de la Universidad de La Sabana.

### Página 35 — Silver Meal Heuristic

- Calcular los tamaños de lotes con pronósticos de demanda dinámica.
- No garantiza la solución óptima – si es de bajo costo!
- Minimiza el costo promedio de gestión de la producción por periodo
- Es más rápida

### Página 36 — Silver Meal Heuristic

- Para el periodo t desde 1 … *m*
  - Para los periodos futuros *p* desde *t* hasta *m*
  - Calculo el costo promedio mensual del costo de producción de:
    $$P(t)=\sum_{i=t}^{p}D_i$$
  - Costo promedio:
    $$K(t)=\frac{P(t)}{p-t}$$

Elegir el tamaño de lote de costo mínimo!!!

### Página 37 — Ejemplo numérico

Tabla de datos de la p. 15.

**Solución para el periodo 1:**

- Producir en 1 D1 = \$20 + \$3\*10 = \$50 : \$50/mes
- Producir en 1 D1 + D2 = \$20 + \$3\*40 + 30\*\$2 = \$200 : \$100/mes

### Página 38 — Ejemplo numérico

Tabla de datos de la p. 15.

**Solución para el periodo 2:**

- Producir en 2 D2 = \$40 + \$3\*30 = \$130 : \$130/mes
- Producir en 2 D2 + D3 = \$40 + \$3\*60 + 30\*\$2 = \$280 : \$140/mes

### Página 39 — Ejemplo numérico

Tabla de datos de la p. 15.

**Solución para el periodo 3:**

- Producir en 3 D3 = \$30 + \$3\*30 = \$120 : \$120/mes
- Producir en 3 D3 + D4 = \$30 + \$3\*50 + 30\*\$1 = \$210: \$105/mes

### Página 40 — ¿Solución con Silver Meal?

Solo el título; el resto de la diapositiva está en blanco.


---

<!-- fuente: corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/wagner_whitin.py -->
# Código: `corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/wagner_whitin.py`

> Archivo completo: https://github.com/samuelgradientai-sys/planeacion-control-produccion/blob/main/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/wagner_whitin.py

```python
"""
Algoritmo de Wagner-Whitin (tamaño de lote dinámico).

Notación (igual que en el tablero):
    Z_j  : costo mínimo hasta el momento j (demanda de los periodos 0..j-1 cubierta)
    C_ij : costo de producir en el periodo i para cubrir la demanda de i..j-1
           = setup_i + c_var_i * (d_i + ... + d_{j-1}) + costo de mantener inventario

    Z_0 = 0
    Z_j = min_{i<j} { Z_i + C_ij }
"""

# ---------------- Datos del ejercicio ----------------
# ---------------- Datos del ejercicio (cuerpo) ----------------
demanda = [0, 0, 2380, 0, 2500, 0, 0, 0, 0, 0]   # netos de las semanas 1 a 10
setup   = [80]*10
c_var   = [0]*10
h       = [0.01]*10


def costo_lote(i, j):
    """C_ij: producir en el periodo i toda la demanda de los periodos i..j-1."""
    q = sum(demanda[i:j])
    costo = setup[i] + c_var[i] * q
    # La demanda del periodo k se guarda desde el periodo i hasta el k
    for k in range(i + 1, j):
        costo += demanda[k] * sum(h[i:k])
    return costo


def wagner_whitin():
    n = len(demanda)
    C = {(i, j): costo_lote(i, j) for i in range(n) for j in range(i + 1, n + 1)}

    Z = [0] * (n + 1)
    mejor_i = [None] * (n + 1)

    print("Z_0 = $0")
    for j in range(1, n + 1):
        opciones = {i: Z[i] + C[i, j] for i in range(j)}
        i_opt = min(opciones, key=opciones.get)
        Z[j] = opciones[i_opt]
        mejor_i[j] = i_opt

        print(f"\nZ_{j} = min {{")
        for i, valor in opciones.items():
            marca = "  <-- min" if i == i_opt else ""
            print(f"    Z_{i} + C_{i}{j} = {Z[i]} + {C[i, j]} = {valor}{marca}")
        print(f"}} => ${Z[j]}")

    # Reconstrucción del plan óptimo (hacia atrás)
    produccion = [0] * n
    j = n
    while j > 0:
        i = mejor_i[j]
        produccion[i] = sum(demanda[i:j])
        j = i

    return Z, produccion


def mostrar_plan(produccion):
    print("\nPlan óptimo de producción")
    print(f"{'Periodo':>7} {'Demanda':>8} {'Produc.':>8} {'Inv.final':>10} "
          f"{'Setup':>6} {'Variable':>9} {'Mantener':>9}")
    inventario = 0
    total = 0
    for t, d in enumerate(demanda):
        inventario += produccion[t] - d
        c_setup = setup[t] if produccion[t] > 0 else 0
        c_varia = c_var[t] * produccion[t]
        c_mant = h[t] * inventario
        total += c_setup + c_varia + c_mant
        print(f"{t:>7} {d:>8} {produccion[t]:>8} {inventario:>10} "
              f"{c_setup:>6} {c_varia:>9} {c_mant:>9}")
    print(f"\nCosto total = ${total}")


if __name__ == "__main__":
    Z, produccion = wagner_whitin()
    mostrar_plan(produccion)
```
