# L12-wagner-whitin-and-silver-meal

> **Archivo:** [`L12-wagner-whitin-and-silver-meal.pdf`](./L12-wagner-whitin-and-silver-meal.pdf) · **Corte 2** · 40 páginas  
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

- [`wagner_whitin.py`](./wagner_whitin.py): implementación en Python de esta misma recursión; ver [README de la carpeta](./README.md).
- [L14 MRP](../04-bom-y-mrp/L14-mrp.md): Wagner-Whitin y Silver-Meal aparecen como políticas de dimensionamiento de lotes para las liberaciones de órdenes del MRP (p. 14).
- [mrp-esfero-v2](../04-bom-y-mrp/mrp-esfero-v2.md): MRP del esfero cuyas órdenes se dimensionan a mano; sus requerimientos netos alimentan el ejemplo del `.py`.
- [Parcial 2](../parcial-2/parcial-2-solucion.md): punto 2.4, Silver-Meal contra Wagner-Whitin.
- [Presentación THYMS del corte 2](../proyecto-thyms-gemelo-digital/THYMS-presentacion-corte-2.md): propone aplicar Wagner-Whitin / Silver-Meal sobre el programa maestro como siguiente paso.

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

## Anexo: texto extraído automáticamente del PDF

> Texto plano tal como sale del PDF, sin fórmulas ni tablas que estén como imagen. La versión fiel y completa es la sección «Contenido completo» de arriba.

### Página 1 · 2 imagen(es)

Production Planning Models
Wagner Whitin Algorithm(1958)

### Página 2 · 2 imagen(es)

Planning problem
• How much to produce?
• When to produce?

### Página 3 · 1 imagen(es)

Assumptions
• No Backlogging
• Finite Planning Horizon
• Fixed and variable costs are considered
𝑘𝑝𝑡= { 
0, 𝑠𝑖 𝑝𝑡= 0 
𝐴𝑡+ 𝑐𝑝𝑡 𝑠𝑖 𝑝𝑡> 0

### Página 4 · 1 imagen(es)

Optimal solution property
• Every optimal solution satisfies that:
– 𝐼𝑡−1𝑃𝑡= 0
– 𝑃𝑡= 0, 𝐷𝑡, 𝐷𝑡+ 𝐷𝑡+1 , 𝐷𝑡+ 𝐷𝑡+1 + 𝐷𝑡+2 ,
… , σ𝑡𝐷𝑡
• La solución se traduce en decidir la 
cantidad de periodos para los 
aprovisiono el inventario en cada 
periodo.

### Página 5 · 1 imagen(es)

Graph of the problem
• Problem with 4 periods
0
1
2
3
4

### Página 6 · 1 imagen(es)

Graph of the problem
• Problem with 4 periods
• Producir en periodo 1 la demanda de periodo 1.
0
1
2
3
4

### Página 7 · 1 imagen(es)

Graph of the problem
• Problem with 4 periods
• Producir en periodo 1 la demanda de periodo 1 y 
2.
0
1
2
3
4

### Página 8 · 1 imagen(es)

Graph of the problem
• Problem with 4 periods
• Producir en periodo 1 la demanda de periodo 1, 2 
y 3.
0
1
2
3
4

### Página 9 · 1 imagen(es)

Graph of the problem
• Problem with 4 periods
• Producir en periodo 1 la demanda de periodo 1, 2, 
3 y 4.
0
1
2
3
4

### Página 10 · 1 imagen(es)

Graph of the problem
• Problem with 4 periods
• Producir en periodo 2 la demanda de periodo 2.
0
1
2
3
4

### Página 11 · 1 imagen(es)

Graph of the problem
• Problem with 4 periods
• Producir en periodo 2 la demanda de periodo 2 y 
3.
0
1
2
3
4

### Página 12 · 1 imagen(es)

Graph of the problem
• Problem with 4 periods
• Producir en periodo 2 la demanda de periodo 2, 3, 
y 4.
0
1
2
3
4

### Página 13 · 1 imagen(es)

Graph of the problem
• Problem with 4 periods
• ¡Problema de ruta más corta!
• ¡Se reducen el número de soluciones por 
explorar!
0
1
2
3
4

### Página 14 · 1 imagen(es)

Formulación
• Cjk = costo de producir y almacenar en el 
periodo j+1 para satisfacer la demanda en 
j+1,j+2,…, k
𝐶𝑗𝑘= 𝐴𝑗+1 + 𝑐𝑃𝑗+1 + ෍
𝑡=𝑗+1
𝑘−1
ℎ𝑡𝐼𝑡

### Página 15 · 1 imagen(es)

Ejemplo numérico
Periodo
Demanda
Set up [$]
c. variable
h(t)
1
10
20
3
2
2
30
40
3
2
3
30
30
3
1
4
20
50
3
1
0
1
2
3
4

### Página 16 · 1 imagen(es)

Formulación
• La solución óptima es una función 
recursiva:
𝑍𝑘=
min
0≤𝑗≤𝑘−1 𝑍𝑗
∗+ 𝐶𝑗𝑘, 𝑘= 1,2, … 𝑇
Z*0 = 0

### Página 17 · 1 imagen(es)

Ejemplo numérico
Periodo
Demanda
Set up [$]
c. variable
h(t)
1
10
20
3
2
2
30
40
3
2
3
30
30
3
1
4
20
50
3
1
0
1
2
3
4
C01 = 20 + 10*3 = 50
50

### Página 18 · 1 imagen(es)

Ejemplo numérico
Periodo
Demanda
Set up [$]
c. variable
h(t)
1
10
20
3
2
2
30
40
3
2
3
30
30
3
1
4
20
50
3
1
0
1
2
3
4
C02 = 20 + (10 + 30)*3 + 30*2 = 200
50
200

### Página 19 · 1 imagen(es)

Ejemplo numérico
Periodo
Demanda
Set up [$]
c. variable
h(t)
1
10
20
3
2
2
30
40
3
2
3
30
30
3
1
4
20
50
3
1
0
1
2
3
4
C03 = 20 + (10+30+30)*3 + 30*2 + 30*(2+2) = 410
50
200
410

### Página 20 · 1 imagen(es)

Ejemplo numérico
Periodo
Demanda
Set up [$]
c. variable
h(t)
1
10
20
3
2
2
30
40
3
2
3
30
30
3
1
4
20
50
3
1
0
1
2
3
4
C04 = 20 + (10+30+30+20)*3 + 30*2 + 30*(2+2) +20*(2+2+1) = 570
50
200
410
570

### Página 21 · 1 imagen(es)

Ejemplo numérico
Periodo
Demanda
Set up [$]
c. variable
h(t)
1
10
20
3
2
2
30
40
3
2
3
30
30
3
1
4
20
50
3
1
0
1
2
3
4
C12 = 40 + 30*3 = 130
50
200
410
570
130

### Página 22 · 1 imagen(es)

Ejemplo numérico
Periodo
Demanda
Set up [$]
c. variable
h(t)
1
10
20
3
2
2
30
40
3
2
3
30
30
3
1
4
20
50
3
1
0
1
2
3
4
C13 = 40 + (30+30)*3 + 30*2 = 280
50
200
410
570
130
280

### Página 23 · 1 imagen(es)

Ejemplo numérico
Periodo
Demanda
Set up [$]
c. variable
h(t)
1
10
20
3
2
2
30
40
3
2
3
30
30
3
1
4
20
50
3
1
0
1
2
3
4
C14 = 40 + (30+30+20)*3 + 30*2 + 20*(2+1) = 400
50
200
410
570
130
280
400

### Página 24 · 1 imagen(es)

Ejemplo numérico
Periodo
Demanda
Set up [$]
c. variable
h(t)
1
10
20
3
2
2
30
40
3
2
3
30
30
3
1
4
20
50
3
1
0
1
2
3
4
C23 = 30 + 30*3 = 120
50
200
410
570
130
280
400
120

### Página 25 · 1 imagen(es)

Ejemplo numérico
Periodo
Demanda
Set up [$]
c. variable
h(t)
1
10
20
3
2
2
30
40
3
2
3
30
30
3
1
4
20
50
3
1
0
1
2
3
4
C24 = 30 + (30+20)*3 +20*1 = 200
50
200
410
570
130
280
400
120
200

### Página 26 · 1 imagen(es)

Ejemplo numérico
Periodo
Demanda
Set up [$]
c. variable
h(t)
1
10
20
3
2
2
30
40
3
2
3
30
30
3
1
4
20
50
3
1
0
1
2
3
4
C34 = 50 + 20*3 = 110
50
200
410
570
130
280
400
120
200
110

### Página 27 · 1 imagen(es)

Ejemplo numérico
Periodo
Demanda
Set up [$]
c. variable
h(t)
1
10
20
3
2
2
30
40
3
2
3
30
30
3
1
4
20
50
3
1
Solución:
𝑍1 = 𝐶01 = 𝐴1 + 𝑐1 𝐷1 = 20 + 3 ∗10 = 50 ∗
0
1
2
3
4
50
200
410
570
130
280
400
120
200
110
Z0 = 0
Z1 = 50

### Página 28 · 1 imagen(es)

Ejemplo numérico
Periodo
Demanda
Set up [$]
c. variable
h(t)
1
10
20
3
2
2
30
40
3
2
3
30
30
3
1
4
20
50
3
1
Solución:
𝑍1 = 𝐶01 = 𝐴1 + 𝑐1 𝐷1 = 20 + 3 ∗10 = 50 ∗
0
1
2
3
4
50
200
410
570
130
280
400
120
200
110
Z0 = 0
Z1 = 50

### Página 29 · 1 imagen(es)

Ejemplo numérico
Periodo
Demanda
Set up [$]
c. variable
h(t)
1
10
20
3
2
2
30
40
3
2
3
30
30
3
1
4
20
50
3
1
Solución:
𝑍2 = ቊ𝑍0 + 𝐶02 = 𝐴1 + 𝑐1 𝐷1 + 𝐷2 + ℎ1𝐷2 = 200
𝑍1
∗+ 𝐶12 = 50 + 𝐴2 + 𝑐2𝐷2 = 180∗
0
1
2
3
4
50
200
410
570
130
280
400
120
200
110
Z0 = 0
Z1 = 50
Z2 = 180

### Página 30 · 1 imagen(es)

Ejemplo numérico
Solución:
𝑍3 = ൞
𝑍0 + 𝐶03 = 410
𝑍1
∗+ 𝐶13 = 330
𝑍2
∗+ 𝐶23 = 300∗
0
1
2
3
4
50
200
410
570
130
280
120
200
110
Z0 = 0
Z1 = 50
Z2 = 180
Z3 = 300

### Página 31 · 1 imagen(es)

Ejemplo numérico
Solución:
𝑍4 =
𝑍0 + 𝐶04 = 570
𝑍1
∗+ 𝐶14 = 450
𝑍2
∗+ 𝐶24 = 380∗
𝑍3
∗+ 𝐶34 = 410
0
1
2
3
4
50
200
410
570
130
280
120
200
110
Z0 = 0
Z1 = 50
Z2 = 180
Z3 = 300
Z4 = 380

### Página 32 · 1 imagen(es)

Ejemplo numérico
Solución:
𝑍4 =
𝑍0 + 𝐶04 = 570
𝑍1
∗+ 𝐶14 = 450
𝑍2
∗+ 𝐶24 = 380∗
𝑍3
∗+ 𝐶34 = 410
0
1
2
3
4
50
200
410
570
130
280
120
200
110
Z0 = 0
Z1 = 50
Z2 = 180
Z3 = 300
Z4 = 380

### Página 33 · 1 imagen(es)

Solución
Periodo
Demanda
Set up [$]
c. variable
h(t)
Production
1
10
20
3
2
10
2
30
40
3
2
30
3
30
30
3
1
50
4
20
50
3
1
0

### Página 34 · 1 imagen(es)

Production Planning Models:
Silver–Meal heuristic

### Página 35 · 1 imagen(es)

Silver Meal Heuristic
• Calcular los tamaños de lotes con pronósticos de 
demanda dinámica.
• No garantiza la solución óptima – si es de bajo 
costo!
• Minimiza el costo promedio de gestión de la 
producción por periodo
• Es más rápida

### Página 36 · 1 imagen(es)

Silver Meal Heuristic
• Para el periodo t desde 1 … m
o Para los periodos futuros p desde t hasta m 
o Calculo el costo promedio mensual del costo de 
producción de:
𝑃𝑡= ෍
𝑖=𝑡
𝑝
𝐷𝑖
o Costo promedio:
𝐾𝑡= 𝑃𝑡
𝑝−𝑡
Elegir el tamaño de lote de costo mínimo!!!

### Página 37 · 1 imagen(es)

Ejemplo numérico
Periodo
Demanda
Set up [$]
c. variable
h(t)
1
10
20
3
2
2
30
40
3
2
3
30
30
3
1
4
20
50
3
1
Solución para el periodo 1:
Producir en 1 D1 = $20 + $3*10 = $50 : $50/mes
Producir en 1 D1 + D2 = $20 + $3*40 + 30*$2 = $200 : $100/mes

### Página 38 · 1 imagen(es)

Ejemplo numérico
Periodo
Demanda
Set up [$]
c. variable
h(t)
1
10
20
3
2
2
30
40
3
2
3
30
30
3
1
4
20
50
3
1
Solución para el periodo 2:
Producir en 2 D2 = $40 + $3*30 = $130 : $130/mes
Producir en 2 D2 + D3 = $40 + $3*60 + 30*$2 = $280 : $140/mes

### Página 39 · 1 imagen(es)

Ejemplo numérico
Periodo
Demanda
Set up [$]
c. variable
h(t)
1
10
20
3
2
2
30
40
3
2
3
30
30
3
1
4
20
50
3
1
Solución para el periodo 3:
Producir en 3 D3 = $30 + $3*30 = $120 : $120/mes
Producir en 3 D3 + D4 = $30 + $3*50 + 30*$1 = $210: $105/mes

### Página 40 · 1 imagen(es)

¿Solución con Silver Meal?

