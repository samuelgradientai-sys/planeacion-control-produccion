<!-- fuente: corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/README.md -->
# Agregación y desagregación (Corte 2)

## Qué cubre

- El modelo lineal de planeación agregada con variación de la fuerza de trabajo y pedidos pendientes (backlog), aplicado a 5 productos y 12 meses con la demanda en horas-hombre, y las restricciones que se le pueden añadir.
- Cómo pasar del plan agregado a cantidades por producto (desagregación) de tres maneras:
  - tiempo de agotamiento y tiempo de ciclo máximo en una sola línea;
  - reparto mensual que minimiza el inventario, resuelto con Solver;
  - modelo con costos de set-up.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [`L11-aggregation-and-disaggregation.md`](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md) | Presentación de la clase 11 (23 diapositivas): modelo agregado con fuerza de trabajo y backlog, ejemplo de 5 productos y 12 meses con su solución, tiempo de ciclo máximo y modelo de set-up. | **Sí (1.º)** |
| [`modelo-desagregacion.md`](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion.md) | Excel con Solver. `EJEMPLO 1`: tiempo de ciclo máximo, $T^*=1{,}5948$. `EJEMPLO 2`: desagregación mensual del plan GAMS, inventario total de 7900. La celda objetivo de Solver de `EJEMPLO 2` está vacía. | 2.º |
| [`modelo-desagregacion-v2.md`](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion-v2.md) | Otra versión del mismo libro, que estaba en la carpeta del Corte 3: rótulos corregidos, Solver bien configurado y otro reparto óptimo con el mismo 7900. Incluye la tabla comparativa con la versión anterior. | 3.º (o en lugar del 2.º) |
| `README.md` | Esta guía. | — |

Los binarios (`.pdf` y `.xlsx`) están al lado de cada `.md`, con el mismo nombre.

## Orden de estudio sugerido

1. Repasar el problema de planeación agregada y el modelo de Bowman en [`../01-planeacion-agregada-modelo-bowman/README.md`](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/README.md).
2. Leer [L11, pp. 3–12](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md): el modelo con fuerza de trabajo y backlog, y el ejemplo de 5 productos.
3. Ver cómo ese modelo está programado en GAMS en [`../01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/`](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/) (explicado en el README de la carpeta 01). El plan que produce es la entrada de la desagregación mensual.
4. Leer L11, pp. 13–20 (tiempo de agotamiento y tiempo de ciclo) y luego la hoja `EJEMPLO 1` o `Para una línea de producción` de los Excel.
5. Estudiar la desagregación mensual en la hoja `Modelo` de [`modelo-desagregacion-v2.md`](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion-v2.md) y compararla con `EJEMPLO 2` de [`modelo-desagregacion.md`](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion.md).
6. Cerrar con L11, pp. 21–22 (proceso completo y modelo de set-up) y practicar con el punto 1.4 de [`../parcial-2/parcial-2-solucion.md`](/corte-2-planeacion-agregada-mrp/parcial-2/parcial-2-solucion.md).

## Conceptos y fórmulas clave

Todos los detalles y la definición de cada símbolo están en el [Resumen de L11](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md).

**Modelo agregado con fuerza de trabajo y backlog** (L11 pp. 3–7). Variables: $P_t$ producción; $I_t$ inventario; $S_t$ pendientes; $L_{R_t}, L_{o_t}, L_{u_t}$ horas regulares, extra y de ocio; $w_t^{\pm}$ contratación y despido en horas; $m$ horas por unidad.

$$
\min Z=\sum_{t=1}^{T}\left(C_tP_t + c_{R_t}L_{R_t} + c_{o_t}L_{o_t} + h_tI_t + \pi_tS_t + c_{w_t}w_t^+ + c'_{w_t}w_t^-\right)
$$

$$
NI_t = NI_{t-1}+P_t-D_t,\qquad NI_t = I_t - S_t,\qquad L_{R_t}=L_{R_{t-1}}+w_t^+-w_t^-,\qquad L_{o_t}-L_{u_t}=mP_t-L_{R_t}
$$

Costos del ejemplo: $C_t=80$, $h_t=2{,}70$, $\pi_t=\infty$, $c_R=12$, $c_o=18$, $c_w=10$, $c'_w=37$.

**Tiempo de agotamiento:**

$$
r_i = \frac{I_{0,i}}{d_i}
$$

$I_{0,i}$ es el inventario inicial y $d_i$ la tasa de demanda. Se produce en orden creciente de $r_i$.

**Tiempo de ciclo máximo** (L11 p. 17). $t_{[i]}$ es el inicio del producto en la posición $i$ y $P$ la tasa de producción de la línea.

$$
\max T\quad\text{s.a.}\quad t_{[i]}\le r_{[i]},\qquad (t_{[i+1]}-t_{[i]})\frac{P}{D_{[i]}}\ge T,\qquad (T-t_{[n]})\frac{P}{D_{[n]}}\ge T
$$

**Desagregación mensual** (Excel). $Y_{j,t}$ es la producción del producto $j$ en el mes $t$ y $X^*_t$ el plan agregado.

$$
\min\sum_t\sum_j I_{j,t}\quad\text{s.a.}\quad I_{j,t}=I_{j,t-1}+Y_{j,t}-D_{j,t}\ge 0,\qquad \sum_j Y_{j,t}\ge X^*_t
$$

**Desagregación con set-up** (L11 p. 22). $K_j$ es el costo de set-up y $\lambda_j$ la tasa de demanda.

$$
\min\sum_j \frac{K_j\lambda_j}{Y_j}\quad\text{s.a.}\quad\sum_j Y_j=X^*,\qquad a_j\le Y_j\le b_j
$$

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado principal |
|---|---|---|
| Plan agregado de 5 productos y 12 meses (demanda total 46 650 h-h, inventario inicial 3000) | [L11 pp. 8–12](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md) | Contratar 820 h en el mes 2 (de 2880 a 3700 h/mes); horas extra en los meses 4–9 (345 a 700 h); 400 h de ocio en los meses 11–12; inventario final de 1800. |
| Inventario en meses con demanda mensual | L11 p. 14 | A 1; B 1,66; C 0,33; D 1,25; E 1,25 meses |
| Tiempo de ciclo máximo (secuencia C→A→B→D→E, $P=3700$) | L11 pp. 15–20; hoja `EJEMPLO 1` de [`modelo-desagregacion.md`](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion.md); hoja `Para una línea de producción` de [`modelo-desagregacion-v2.md`](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion-v2.md) | $T^*=1{,}5948$ meses; inicios 0; 0,2586; 0,5172; 0,9052; 1,25; inventario total constante de 3000. |
| Desagregación mensual del plan GAMS (2880, 2880 y luego 3000) | Hoja `EJEMPLO 2` de [`modelo-desagregacion.md`](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion.md) y hoja `Modelo` de [`modelo-desagregacion-v2.md`](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion-v2.md) | Inventario total de 7900 (3280 + 2760 + 1860). Desde el mes 5 la producción es igual a la demanda. Los dos libros dan repartos distintos con el mismo óptimo. |

## Relación con otros temas y proyectos

- **Antes:**
  - [`../01-planeacion-agregada-modelo-bowman/`](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/README.md): planeación agregada (L10), modelo de Bowman y modelo de flujo en GAMS. El `modelo-flujo.gms` implementa el modelo de L11 pp. 3–9, con subcontratación a \$95, y su solución ($z = 4\,062\,000$) es el «Plan Agregado» que se desagrega en los Excel de esta carpeta.
  - [`../../corte-1-pronosticos/`](/corte-1-pronosticos/): de ahí salen los pronósticos $D_t$ que alimentan el plan.
- **Después:**
  - [`../03-wagner-whitin-y-silver-meal/`](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/): tamaño de lote por producto con costos de set-up.
  - [`../04-bom-y-mrp/`](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/): el plan desagregado (plan maestro) alimenta el MRP.
  - [`../05-mrp-ii-y-capacidad/L15-mrp-ii.md`](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md): muestra el «Sistema de Agregación y Desagregación» antes del plan maestro de producción.
- **Evaluación y proyecto:**
  - [`../parcial-2/parcial-2-solucion.md`](/corte-2-planeacion-agregada-mrp/parcial-2/parcial-2-solucion.md): el punto 1.4 desagrega 2620 horas con un tiempo de agotamiento común.
  - [`../proyecto-thyms-gemelo-digital/`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/): el gemelo digital de THYMS también desagrega por producto el plan de la estrategia elegida.
- **Scheduling:** las «restricciones de secuenciación» que L11 p. 13 da como razón para desagregar se estudian en el Corte 3, en [`../../corte-3-programacion-scheduling/`](/corte-3-programacion-scheduling/).


---

<!-- fuente: corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md -->
# L11-aggregation-and-disaggregation

> **Archivo:** [`L11-aggregation-and-disaggregation.pdf`](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.pdf) · **Corte 2** · 23 páginas  
> **Nombre original:** `CORTE 2/Lec 11 - Agregration and dissagregation.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** el modelo lineal de planeación agregada con variación de la fuerza de trabajo y pedidos pendientes (5 productos, 12 meses), y cómo desagregar el plan agregado en producción por producto: tiempo de ciclo con producción y demanda constantes, y el modelo con costos de set-up.

### Ideas clave

- La planeación agregada busca el nivel óptimo de fuerza de trabajo, inventario y producción por periodo, con la demanda en una unidad común (aquí, horas-hombre, así que $m = 1$).
- El modelo es un PL que minimiza los costos de producción, de mano de obra regular y extra, de inventario, de pedidos pendientes y de contratar o despedir. Lo amarran tres grupos de restricciones: balance del inventario neto, continuidad de la fuerza de trabajo y relación entre producción y horas disponibles (horas extra y horas de ocio).
- Restricciones que se pueden añadir (p. 10): tope de fuerza de trabajo (26 trabajadores = 4160 h), inventario de seguridad de dos semanas, capacidad, costo fijo con binaria $Y_t$, no producir en dos periodos seguidos, variación de la producción de ±20 % entre meses, despidos de máximo 10 % y subcontratación.
- En la solución del ejemplo (p. 11) se contrata una sola vez (820 h en el mes 2) y la plantilla queda en 3700 h/mes. Los picos se cubren con horas extra (meses 4–9) y el valle con horas de ocio (400 h en los meses 11–12), en vez de despedir.
- ¿Por qué no planear producto por producto desde el inicio? Porque se volvería un problema de optimización entera, el pronóstico por producto tiene más error y aparecerían restricciones de secuenciación (p. 13).
- Desagregación con producción y demanda constantes: los productos se ordenan por tiempo de agotamiento creciente y se busca el **tiempo de ciclo máximo** $T$, porque un ciclo más largo significa menos set-ups. En el ejemplo, $T^* = 1{,}5948$ meses con la secuencia C → A → B → D → E.
- El proceso completo (p. 21) es: agregar las unidades → planear la producción (Bowman o el modelo de flujo en GAMS) → desagregar en cantidades por referencia.
- Otra forma de desagregar (p. 22) es repartir la producción agregada $X^*$ entre productos minimizando el costo de set-up $\sum K_j\lambda_j/Y_j$, con cotas $a_j \le Y_j \le b_j$.

### Fórmulas y métodos

**1. Modelo de planeación agregada con variación de fuerza de trabajo y backlog (pp. 3–7).** Es un PL que se usa para fijar la plantilla, la producción y el inventario de cada periodo.

$$
\min Z = \sum_{t=1}^{T}\left(C_tP_t + c_{R_t}L_{R_t} + c_{o_t}L_{o_t} + h_tI_t + \pi_tS_t + c_{w_t}w_t^+ + c'_{w_t}w_t^-\right)
$$

$$
NI_t = NI_{t-1} + P_t - D_t,\qquad NI_t = I_t - S_t \qquad \forall t\in\{2,\dots,T\}
$$

$$
L_{R_t} = L_{R_{t-1}} + w_t^+ - w_t^- \qquad \forall t\in\{2,\dots,T\}
$$

$$
L_{o_t} - L_{u_t} = mP_t - L_{R_t},\qquad P_t, I_t, S_t, L_{R_t}, L_{o_t}, w_t^+, w_t^-, L_{u_t}\ge 0
$$

Símbolos:

- $D_t$: demanda pronosticada.
- $P_t$: producción.
- $I_t$: inventario a la mano al final de $t$.
- $S_t$: pendientes (backlog) al final de $t$.
- $NI_t$: inventario neto, que es libre de signo.
- $L_{R_t}$, $L_{o_t}$, $L_{u_t}$: horas regulares, extra y de ocio.
- $w_t^\pm$: aumento y disminución de la fuerza de trabajo, en horas.
- $m$: horas-hombre por unidad.
- Costos: $C_t$ = 80 (producción sin nómina), $h_t$ = 2,70, $\pi_t = \infty$, $c_R$ = 12, $c_o$ = 18, $c_w$ = 10, $c'_w$ = 37.
- Datos del ejemplo: inventario inicial agregado 3000 h; $L_{R_1} = 2880$, según la solución de la p. 11.

**2. Restricciones adicionales (p. 10)**, en forma algebraica:

- $L_{R_t}\le 4160$.
- $P_t \le \text{Cap}\,Y_t$ con $Y_t\in\{0,1\}$ (costo fijo).
- $Y_t + Y_{t+1}\le 1$.
- $0{,}8P_t \le P_{t+1}\le 1{,}2P_t$.
- $w_t^- \le 0{,}1\,L_{R_{t-1}}$.
- Subcontratación.

**3. Inventario en meses o tiempo de agotamiento (pp. 14–15).** Para el producto $i$, con inventario inicial $I_{0,i}$ y demanda constante $D_i$:

$$
r_i = \frac{I_{0,i}}{D_i}
$$

Si la demanda cambia de mes a mes (p. 14), primero se cubre el mes 1 y el sobrante se divide por la demanda del mes 2: $r_i = 1 + (I_{0,i}-D_{i1})/D_{i2}$ cuando $I_{0,i} > D_{i1}$. Los productos se ordenan por $r_i$ creciente, y ese es el orden de producción.

**4. Tiempo de ciclo máximo con producción y demanda constantes (pp. 16–17).** Es un PL que da el tiempo de inicio de cada producto en una línea única. Aplica cuando la tasa de producción $P$ alcanza para todos ($P = \sum_i D_i$ en el ejemplo).

$$
\max\ T \quad \text{s.a.}\quad t_{[i]}\le r_{[i]}\ \forall [i];\qquad (t_{[i+1]}-t_{[i]})\frac{P_t}{D_{[i]t}}\ge T\ \ \forall [i]=1,\dots,n-1;\qquad (T-t_{[n]})\frac{P_t}{D_{[n]t}}\ge T
$$

Símbolos:

- $T$: tiempo de ciclo (una rotación completa de los $n$ productos).
- $t_{[i]}$: instante en que empieza a producirse el producto en la posición $i$.
- $r_{[i]}$: su tiempo de agotamiento.
- $D_{[i]t}$: su tasa de demanda.
- $P_t$: tasa de producción de la línea.

**Formulación extensa del ejemplo**, la que pide la p. 18. Es deducida de las pp. 15, 17 y 19 y coincide con el Solver del Excel. Con la secuencia C, A, B, D, E y $P = 3700$:

$$
\begin{aligned}
\max\ & T\\
\text{s.a. } & t_C \le \tfrac{200}{600},\quad t_A \le \tfrac{300}{600},\quad t_B \le \tfrac{700}{900},\quad t_D \le \tfrac{800}{800},\quad t_E \le \tfrac{1000}{800}\\
& (t_A - t_C)\tfrac{3700}{600} \ge T,\quad (t_B - t_A)\tfrac{3700}{600} \ge T,\quad (t_D - t_B)\tfrac{3700}{900} \ge T\\
& (t_E - t_D)\tfrac{3700}{800} \ge T,\quad (T - t_E)\tfrac{3700}{800} \ge T,\qquad T, t_i \ge 0
\end{aligned}
$$

Comprobación propia: en el óptimo todas las restricciones de demanda quedan activas y $t_E = r_E = 1{,}25$. Por eso

$$
T^* = \frac{r_E\,P}{\sum_{i\ne E} D_i} = \frac{1{,}25\cdot 3700}{2900} = 1{,}5948
$$

**5. Desagregación con costos de set-up (p. 22).** Es un problema no lineal convexo que reparte la producción agregada de un periodo entre productos con costos de alistamiento distintos.

$$
\min \sum_{j=1}^{J}\frac{K_j\lambda_j}{Y_j}\quad\text{s.a.}\quad \sum_{j=1}^{J}Y_j = X^*,\qquad a_j\le Y_j\le b_j
$$

Símbolos:

- $K_j$: costo de set-up.
- $\lambda_j$: tasa de demanda.
- $X^*$: producción agregada.
- $Y_j$: producción desagregada del producto $j$.
- $a_j$, $b_j$: cotas inferior y superior.

En GAMS se pone `y.lo(j) = 1;` para evitar dividir por cero. Nota de contexto, no está en la diapositiva: en la literatura este modelo se asocia a la desagregación jerárquica de Bitran y Hax.

### Ejemplos resueltos

| Ejemplo | Páginas | Resultado |
|---|---|---|
| Plan agregado de 5 productos y 12 meses (demanda en horas-hombre, total 46 650 h; inventario inicial 3000 h) | 8–12 | Plantilla de 2880 h → contratar 820 h en el mes 2 → 3700 h/mes; horas extra de 345, 525, 300, 450, 700 y 350 en los meses 4–9; 400 h de ocio en los meses 11 y 12; inventario final de 1800. No se reporta el costo total. |
| Inventario en meses con demanda mensual (A–E) | 14 | 1; 1,66; 0,33; 1,25; 1,25 meses |
| Tiempos de agotamiento con tasas constantes | 15 | 0,33; 0,5; 0,78; 1; 1,25 (orden C, A, B, D, E) |
| Tiempo de ciclo máximo | 17–19 | $T^* = 1{,}5948$; $t_C = 0$, $t_A = 0{,}2586$, $t_B = 0{,}5172$, $t_D = 0{,}9052$, $t_E = 1{,}25$ |
| Simulación del ciclo | 20 | El inventario total se mantiene en 3000. Los picos son C = 1002, A = 947, B = 1320, D = 1076 y E = 1000. E llega a 0 en $t=1{,}25$. Al final del ciclo los inventarios vuelven a 200, 300, 700, 800 y 1000. |

### Páginas clave

- p. 3–7: parámetros, variables, función objetivo y restricciones del modelo agregado.
- p. 8–9: datos del ejemplo (demanda por producto y costos).
- p. 10: restricciones adicionales.
- p. 11–12: solución del ejemplo, en tabla y gráfico.
- p. 13–15: por qué desagregar, inventario en meses y tiempos de agotamiento.
- p. 16–20: modelo de tiempo de ciclo máximo, su solución y la simulación.
- p. 21: diagrama del proceso agregar → planear → desagregar.
- p. 22: modelo de desagregación con costos de set-up.

### Relación con otros archivos del repo

- [`modelo-desagregacion.md`](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion.md) y [`modelo-desagregacion-v2.md`](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion-v2.md): los Excel con Solver que resuelven el tiempo de ciclo de las pp. 15–19 (el mismo $T^* = 1{,}5948$). También desagregan mes a mes, por producto, el plan agregado del modelo de flujo en GAMS.
- [`../01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/`](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/) (explicado en [`../01-planeacion-agregada-modelo-bowman/README.md`](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/README.md)): `modelo-flujo.gms` implementa este modelo con los datos de las pp. 8–9 (demanda total por mes, costos 80 / 2,7 / 12 / 18 / 10 / 37, inventario inicial 3000 y $L_{R_1}=2880$). Le añade subcontratación a \$95, usa un costo de faltante de 10 000 en lugar de ∞ y no incluye horas de ocio ni inventario de seguridad. Por eso su solución ($z = 4\,062\,000$; producción de 2880, 2880 y luego 3000 h; subcontratación en los meses 4–11) no es la misma de la p. 11.
- [`../01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md`](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md): introducción a la planeación agregada y al modelo de transporte de Bowman, que la p. 21 nombra como alternativa.
- [`../parcial-2/parcial-2-solucion.md`](/corte-2-planeacion-agregada-mrp/parcial-2/parcial-2-solucion.md): el punto 1.4 del parcial desagrega horas agregadas con un tiempo de agotamiento común.
- [`../05-mrp-ii-y-capacidad/L15-mrp-ii.md`](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md): ubica el «Sistema de Agregación y Desagregación» antes del plan maestro de producción.
- [`../03-wagner-whitin-y-silver-meal/`](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/) y [`../04-bom-y-mrp/`](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/): los pasos siguientes, que son el tamaño de lote por producto y el MRP.

## Contenido completo (página por página)

> [Imagen decorativa: todas las diapositivas, salvo la 22, llevan a la derecha una franja con una foto del campus de la Universidad de La Sabana (edificio de ladrillo junto a un lago) y el logo «Universidad de La Sabana». No se repite en cada página.]

### Página 1 — Operations Management (portada)

**OPERATIONS MANAGEMENT**

Semestre 2026

> [Imagen decorativa: logo de licencia Creative Commons BY-NC-SA en la esquina inferior izquierda.]

### Página 2 — Outline

- Aggregate Planning Methods
  - Model with variation of work force and backlogging
- Disaggregation Plan

### Página 3 — Aggregate planning: Model with variation of work force and backlogging (parámetros)

**Objective:** to determine the optimal workforce level, inventory level, and production per period.

**Parameters:**

- $T$ set of planning periods
- $D_t$ Forecast for demand at period t
- $C_t$ Costo unitario de producción en el periodo t (sin nomina)
- $m$ Horas – hombre requeridas para producir una unidad. m= 1 si la unidad de agregación es horas- hombre
- $h_t$ Costo de almacenamiento unitario por unidad del periodo t al periodo t+1
- $\pi_t$ Costo unitario de pedido pendiente del periodo t al periodo t+1
- $C_{R_t}$ Costo de una hora-trabajador en tiempo regular en el periodo t
- $C_{O_t}$ Costo de una hora extra-trabajador en tiempo regular en el periodo t *(sic: la diapositiva dice «en tiempo regular», pero se refiere a la hora extra)*
- $c_{w_t}$ Costo de aumentar la fuerza de trabajo en trabajador-hora del periodo t-1 al periodo t
- $c'_{w_t}$ Costo de disminuir la fuerza de trabajo en trabajador-hora del periodo t-1 al periodo t

### Página 4 — Aggregate planning: Model with variation of work force and backlogging (variables)

**Decision Variables**

- $P_t$ Cantidad a producir en el periodo t
- $I_t$ Inventario on-hand al final del periodo t
- $S_t$ Cantidad pendiente al final del periodo t
- $L_{R_t}$ Horas de trabajo en tiempo regular en el periodo t
- $L_{o_t}$ Horas extra programadas en el periodo t
- $w_t^+$ Aumento en el nivel de fuerza de trabajo del periodo t-1 al periodo t
- $w_t^-$ Disminución en el nivel de fuerza de trabajo del periodo t-1 al periodo t

### Página 5 — Objective Function

- Minimize Costs

$$
\min Z = \sum_{t=1}^{T} C_tP_t + c_{R_t}L_{R_t} + c_{o_t}L_{o_t} + h_tI_t + \pi_tS_t + c_{w_t}w_t^+ + c'_{w_t}w_t^-
$$

(La sumatoria abarca todos los términos; en la diapositiva la expresión está partida en dos renglones.)

### Página 6 — Constraints (inventario neto)

Consistencia de las variables periodo tras periodo:

- Variable de decisión auxiliar
  - $NI_t$ Inventario neto al final del periodo t

$$
NI_t = NI_{t-1} + P_t - D_t \qquad \forall\, t \in \{2,\dots,T\}
$$

$$
NI_t = I_t - S_t \qquad \forall\, t \in \{2,\dots,T\}
$$

### Página 7 — Constraints (fuerza de trabajo y no negatividad)

Consistencia en el nivel de fuerza de trabajo

$$
L_{R_t} = L_{R_{t-1}} + w_t^+ - w_t^- \qquad \forall\, t \in \{2,\dots,T\}
$$

Relacionar nivel de producción y nivel de fuerza de trabajo

$L_{u_t}$ Horas de ocio de los trabajadores en el periodo t

$$
L_{o_t} - L_{u_t} = mP_t - L_{R_t}
$$

Restricciones de no-negatividad

$$
P_t,\ I_t,\ S_t,\ L_{R_t},\ L_{o_t},\ w_t^+,\ w_t^-,\ L_{u_t} \ge 0 \qquad \forall\, t \in \{1,\dots,T\}
$$

(La diapositiva escribe el conjunto como «{1, , , , , T}».)

### Página 8 — Example: 5 products, 12 months (demanda)

Demand [man-hours]

| Month | A | B | C | D | E | Total |
|---|---|---|---|---|---|---|
| 1 | 300 | 300 | 600 | 600 | 800 | 2600 |
| 2 | 600 | 600 | 600 | 800 | 800 | 3400 |
| 3 | 600 | 900 | 600 | 1000 | 800 | 3900 |
| 4 | 800 | 1500 | 600 | 1600 | 800 | 5300 |
| 5 | 800 | 600 | 650 | 1400 | 800 | 4250 |
| 6 | 800 | 600 | 600 | 1400 | 800 | 4200 |
| 7 | 800 | 100 | 700 | 1400 | 800 | 3800 |
| 8 | 1000 | 0 | 700 | 2000 | 800 | 4500 |
| 9 | 600 | 0 | 700 | 2200 | 800 | 4300 |
| 10 | 500 | 0 | 600 | 1900 | 800 | 3800 |
| 11 | 400 | 0 | 600 | 1800 | 800 | 3600 |
| 12 | 0 | 0 | 600 | 1600 | 800 | 3000 |
| Initial Stock | 300 | 700 | 200 | 800 | 1000 | 3000 |

### Página 9 — Example: 5 products, 12 months (costos)

Cost Coefficients

| Símbolo | Descripción (texto de la diapositiva) | Valor |
|---|---|---|
| $C_t$ | Costo unitario de producción en el periodo t (sin nomina) | \$80 |
| $h_t$ | Costo de almacenamiento unitario por unidad del periodo t al periodo t+1 | \$2.70 |
| $\pi_t$ | Costo unitario de pedido pendiente del periodo t al periodo t+1 | \$∞ |
| $C_{R_t}$ | Costo de una hora-trabajador en tiempo regular en el periodo t | \$12 |
| $C_{O_t}$ | Costo de una hora extra-trabajador en tiempo regular en el periodo t | \$18 |
| $c_{w_t}$ | Costo de aumentar la fuerza de trabajo en trabajador-hora del periodo t-1 al periodo t | \$10 |
| $c'_{w_t}$ | Costo de disminuir la fuerza de trabajo en trabajador-hora del periodo t-1 al periodo t | \$37 |

Con $\pi_t = \infty$ no se permiten pedidos pendientes (backlog).

### Página 10 — Additional Constraints

- Límite en la fuerza de trabajo: 26 trabajadores (4160 horas)
- Inventario de seguridad de dos semanas del siguiente periodo
- Limitar la capacidad de producción
- Poner un costo fijo de producción
  - Y(t) = 1 si se produce en el periodo t, 0 de lo contrario
  - Restricción : P(t) =l= Cap\*Y(t)
- No producir en dos periodos consecutivos
  - Y(t) + Y(t+1) =l= 1;
- El nivel de producción no puede variar más del 20% de un mes al siguiente.
  - P(t+1) =l= 1,2 \* P(t) para todo t
  - P(t+1) =g= 0,8\*P(t) para todo t
- No puede despedirse más del 10% de empleados del mes anterior.
  - W-(t) =l= 0,1\* Lr(t-1) para todo t.
- Subcontratación.

Las restricciones escritas en sintaxis GAMS (`=l=` es $\le$, `=g=` es $\ge$) equivalen a:

$$
L_{R_t} \le 4160;\qquad P_t \le \text{Cap}\cdot Y_t,\ Y_t\in\{0,1\};\qquad Y_t + Y_{t+1} \le 1
$$

$$
P_{t+1} \le 1{,}2\,P_t;\qquad P_{t+1} \ge 0{,}8\,P_t;\qquad w_t^- \le 0{,}1\,L_{R_{t-1}}
$$

(26 trabajadores × 160 h = 4160 h/mes. La traducción de «inventario de seguridad de dos semanas» sería $I_t \ge 0{,}5\,D_{t+1}$ si el mes tiene unas cuatro semanas; esa forma algebraica es deducida, no aparece en la diapositiva.)

### Página 11 — Solution (tabla)

| Mes | I(t) | P(t) | D(t) | L(RT) | L(OT) | L(UT) | w(t)+ | w(t)- |
|---|---|---|---|---|---|---|---|---|
| 1 | 3280 | 2880 | 2600 | 2880 | 0 | 0 | 0 | 0 |
| 2 | 3580 | 3700 | 3400 | 3700 | 0 | 0 | 820 | 0 |
| 3 | 3380 | 3700 | 3900 | 3700 | 0 | 0 | 0 | 0 |
| 4 | 2125 | 4045 | 5300 | 3700 | 345 | 0 | 0 | 0 |
| 5 | 2100 | 4225 | 4250 | 3700 | 525 | 0 | 0 | 0 |
| 6 | 1900 | 4000 | 4200 | 3700 | 300 | 0 | 0 | 0 |
| 7 | 2250 | 4150 | 3800 | 3700 | 450 | 0 | 0 | 0 |
| 8 | 2150 | 4400 | 4500 | 3700 | 700 | 0 | 0 | 0 |
| 9 | 1900 | 4050 | 4300 | 3700 | 350 | 0 | 0 | 0 |
| 10 | 1800 | 3700 | 3800 | 3700 | 0 | 0 | 0 | 0 |
| 11 | 1500 | 3300 | 3600 | 3700 | 0 | 400 | 0 | 0 |
| 12 | 1800 | 3300 | 3000 | 3700 | 0 | 400 | 0 | 0 |

La diapositiva no muestra el costo total ni dice qué restricciones adicionales de la página 10 se activaron. Comprobación propia: el balance $I_t = I_{t-1} + P_t - D_t$ con $I_0 = 3000$ cuadra en los 12 meses (p. ej. $3000 + 2880 - 2600 = 3280$), y $L_{OT} - L_{UT} = P_t - L_{RT}$ (con $m=1$) también cuadra. Del mes 4 al 11 el inventario es exactamente la mitad de la demanda del mes siguiente ($2125 = 4250/2$, $2100 = 4200/2$, …, $1500 = 3000/2$), lo que sugiere que se resolvió con el inventario de seguridad de dos semanas (deducido).

### Página 12 — Solution (gráfico)

> [Gráfico: líneas, título «COMPORTAMIENTO DE LA PRODUCCIÓN Y DEMANDA». Eje X: «MES DEL AÑO» 1 a 12; eje Y: «HORAS-HOMBRE» de 0 a 6000. Series: I(t) (naranja), P(t) (gris), D(t) (amarillo), L(RT) (azul), L(OT) (verde), L(UT) (azul oscuro), w(t)+ (marrón), w(t)- (gris oscuro). Valores visibles: D(t) sube de 2600 a un pico de 5300 en el mes 4 y baja a 3000 en el mes 12; L(RT) sube de 2880 a 3700 en el mes 2 y queda plana; P(t) sigue a la demanda por encima de 3700 entre los meses 3 y 9 y baja a 3300 en los meses 11–12; I(t) sube de unos 3280 a 3580 (mes 2) y luego baja a unos 2100–2250 en los meses 4–8, 1500 en el mes 11 y 1800 en el mes 12; w(t)+ tiene un solo pico de 820 en el mes 2; L(OT) va de 0 (mes 3) a unos 345–700 en los meses 4–9 y vuelve a 0 en el mes 10; L(UT) pasa de 0 a 400 en los meses 11–12; w(t)- es 0 todo el año. Ojo: en el gráfico P(t) del mes 1 aparece cerca de 2280, mientras que la tabla de la página 11 dice 2880.]

### Página 13 — Disaggregating aggregate plans (por qué desagregar)

- ¿Por qué no formular una planeación multi-producto desde el inicio?
  - Optimización entera
  - Errores más altos del pronóstico
  - Restricciones de secuenciación

### Página 14 — Disaggregating aggregate plans (inventario en meses)

- Para el caso de producción y demanda constante

| | A | B | C | D | E |
|---|---|---|---|---|---|
| Inventario Inicial | 300 | 700 | 200 | 800 | 1000 |
| Demanda Mes 1 | 300 | 300 | 600 | 600 | 800 |
| Demanda Mes 2 | 600 | 600 | 600 | 800 | 800 |
| Inventario en meses | 1 | 1,66 | 0,33 | 1,25 | 1,25 |

(Cómo sale la última fila, deducido: el inventario inicial cubre la demanda del mes 1 y lo que sobra se divide por la demanda del mes 2. B: $1 + (700-300)/600 = 1{,}66$; D: $1 + (800-600)/800 = 1{,}25$; E: $1 + (1000-800)/800 = 1{,}25$; A: $300/300 = 1$; C: $200/600 = 0{,}33$.)

### Página 15 — Disaggregating aggregate plans (tasas constantes)

- Para el caso de producción y demanda constante

| | Inventario Inicial | Demanda Mes | tasa de Producción/mes | Inventario en meses |
|---|---|---|---|---|
| A | 200 | 600 | 3700 | 0,33 |
| B | 300 | 600 | 3700 | 0,5 |
| C | 700 | 900 | 3700 | 0,78 |
| D | 800 | 800 | 3700 | 1 |
| E | 1000 | 800 | 3700 | 1,25 |

Aquí «Inventario en meses» = Inventario Inicial / Demanda Mes, y las filas están ordenadas de menor a mayor. Ojo con las etiquetas: por los inventarios iniciales (200, 300, 700, 800, 1000), estas filas A–E son en realidad los productos C, A, B, D y E de la página 8, que es el orden que usan las páginas 19 y 20 (deducido). Las cinco tasas de demanda suman $600+600+900+800+800 = 3700$, igual a la tasa de producción.

### Página 16 — Optimization Problem

- $T$ Tiempo de ciclo para una rotación completa de n productos

*El numero de set-ups se minimiza cuando el tiempo de ciclo es máximo.*

- $r_{[i]}$ Tiempo hasta agotar el producto en la i-esima posición de producción.
- $t_{[i]}$ Tiempo en que inicia el producto de la i-esima posición de producción
- $D_{[i]t}$ Tasa de demanda en el periodo t para i-esima posición de producción

### Página 17 — Mathematical Formulation

$$
\text{Maximize } T
$$

- Sujet to:

Avoid shortage:

$$
t_{[i]} \le r_{[i]} \qquad \forall\, [i]
$$

Satisfy the demand:

$$
\left(t_{[i+1]} - t_{[i]}\right)\frac{P_t}{D_{[i]t}} \ge T \qquad \forall\, [i] = \{1,\dots,n-1\}
$$

Restart the cicle in moment T:

$$
\left(T - t_{[n]}\right)\frac{P_t}{D_{[n]t}} \ge T
$$

Aquí $P_t$ es la tasa de producción de la línea (3700 h/mes en el ejemplo). La condición de demanda dice que lo producido mientras la línea está en el producto $[i]$, $(t_{[i+1]}-t_{[i]})P_t$, debe cubrir su demanda durante todo el ciclo, $T\,D_{[i]t}$.

### Página 18 — What is the extensive formulation of the problem?

Diapositiva con solo la pregunta «What is the extensive formulation of the problem?». No trae respuesta. (La formulación extensa del ejemplo, deducida de las páginas 15, 17 y 19 y del Excel, está en el Resumen.)

### Página 19 — Optimal solution

- T\* = 1.5948
- tc = 0
- ta = 0.2586
- tb = 0.5172
- td = 0.9052
- te = 1.25

Secuencia de producción: C → A → B → D → E, y vuelve a empezar en $T^* = 1{,}5948$ meses.

### Página 20 — Simulating the solution

| Time | C | A | B | D | E | Inv Total |
|---|---|---|---|---|---|---|
| 0 | 200 | 300 | 700 | 800 | 1000 | 3000 |
| 0.2586 | **1002** | 145 | 467 | 593 | 793 | 3000 |
| 0.5172 | 847 | **947** | 234 | 386 | 586 | 3000 |
| 0.9052 | 614 | 714 | **1320** | 76 | 276 | 3000 |
| 1.25 | 407 | 507 | 1010 | **1076** | 0 | 3000 |
| 1.59 | 200 | 300 | 700 | 800 | **1000** | 3000 |

En la diapositiva, los valores en **negrita** aquí están en rojo: son el inventario máximo del producto que se acaba de fabricar en ese intervalo. Cada producto se consume a su tasa de demanda y, mientras se fabrica, crece a la tasa $3700 - D_i$. El inventario total queda constante en 3000 porque la tasa de producción es igual a la suma de las tasas de demanda. E llega exactamente a 0 en $t = 1{,}25$, justo cuando empieza su producción. Al cerrar el ciclo, en 1.59, todos los inventarios vuelven a los valores iniciales.

### Página 21 — Proceso de Planeación Agregada

> [Diagrama: flujo de tres bloques conectados por flechas, de izquierda a derecha.]
>
> 1. **Agregar las unidades** → Identificar la unidad de agregación correcta.
> 2. **Planear la producción** → Saber Horas de trabajo, niveles de inventario y de producción; Bowman; Modelo en GAMS de flujo.
> 3. **Desagregar** → Saber la cantidad a producir de cada referencia o tipo de producto.

### Página 22 — Mathematical Model (desagregación con costos de set-up)

- Minimize $\displaystyle\sum_{j=1}^{J} K_j\lambda_j / Y_j$
- Subject to:
  - $\displaystyle\sum_{j=1}^{J} Y_j = X^*$
  - $a_j \le Y_j \le b_j$ for all product j
- $K_j$ : Set-up cost
- $\lambda_j$: Demand rate
- $X^*$: Aggregated production
- $Y_j$: Disaggregated production
- En GAMS: `y.lo(j) = 1;`

(Es la única diapositiva sin la franja lateral de fotos. La instrucción `y.lo(j) = 1;` pone una cota inferior de 1 a $Y_j$ para que el solver no divida por cero en la función objetivo; esta interpretación es deducida.)

### Página 23 — ¡THANKS!

William Guerrero, Ph.D.

**¡THANKS!**


---

<!-- fuente: corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion-v2.md -->
# modelo-desagregacion-v2

> **Archivo:** [`modelo-desagregacion-v2.xlsx`](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion-v2.xlsx) · **Corte 2** (el archivo estaba en la carpeta `CORTE 3/` del estudiante) · Libro de Excel con 2 hoja(s): `Para una línea de producción`, `Modelo`  
> **Nombre original:** `CORTE 3/Modelo de Desagregación .xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Es otra versión del mismo libro de desagregación de la clase L11 ([`L11-aggregation-and-disaggregation.md`](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md)). Estaba en la carpeta del Corte 3, pero el tema es del Corte 2 (desagregación del plan agregado) y por eso vive aquí. Se creó el 2026-09-10, el mismo día que [`modelo-desagregacion.xlsx`](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion.md), en Excel para Mac, y se modificó por última vez el 2026-09-11. Resuelve con **Solver (Simplex LP)** los dos mismos ejemplos:

1. **`Para una línea de producción`**: tiempo de ciclo máximo de una línea con 5 productos, con producción y demanda constantes (L11, pp. 15–20). Resultado: $T^* = 1{,}5948$ meses.
2. **`Modelo`**: desagregación mensual, por producto, del plan agregado de 12 meses del modelo de flujo en GAMS ([`../01-planeacion-agregada-modelo-bowman/README.md`](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/README.md)), minimizando el inventario total. Resultado: 7900 horas-mes.

**¿Mismo ejercicio que `modelo-desagregacion.xlsx`?** Sí: mismos datos, mismo método y mismos resultados en el objetivo. Las diferencias, detalladas al final, son de presentación y de configuración de Solver (aquí el objetivo sí está bien puesto), más un reparto distinto por producto en los meses 1–4 que tiene el mismo inventario total. Ese reparto es un óptimo alternativo.

---

### Hoja `Para una línea de producción`: tiempo de ciclo máximo

**Objetivo (deducido de L11, pp. 16–19).** Hallar los tiempos de inicio $t_i$ de cada producto y el ciclo completo $T$ más largo posible, sin que ningún producto se agote, en una línea que produce 3700 h/mes y fabrica los productos uno tras otro en orden creciente de tiempo de agotamiento.

**Datos de entrada** (filas 5–9; encabezado «Parámetros del Modelo» en B3:D3):

| Fila | Producto (posición) | Inventario Inicial (B) | Demanda Mes $d_i$ (C) | tasa de producción/mes $P$ (D) |
|---|---|---|---|---|
| 5 | A | 200 | 600 | 3700 |
| 6 | B | 300 | 600 | 3700 |
| 7 | C | 700 | 900 | 3700 |
| 8 | D | 800 | 800 | 3700 |
| 9 | E | 1000 | 800 | 3700 |

Las letras A–E son **posiciones** en la secuencia, no los productos de la tabla de demanda. Por los inventarios iniciales, son los productos C, A, B, D y E de la hoja `Modelo` y de L11 p. 8 (deducido). Las tasas de demanda suman 3700, igual a $P$.

**Parámetros:** $P = 3700$ h/mes en D5:D9. No hay costos.

**Método paso a paso:**

1. **Inventario en meses** (E, «ordenar creciente»): `E5 = +B5/C5`, es decir, $r_i = I_{0,i}/d_i$, que da 0,3333; 0,5; 0,7778; 1; 1,25.
2. **Variables** («Variable de decisión», F): F5:F9 son los inicios $t_i$ y F10 es $T$ («T (duración del ciclo)»).
3. **Producción total** (G): `G5 = +(F6-F5)*D5`, es decir, $G_i = (t_{i+1}-t_i)P$. La última fila usa F10: $G_5 = (T-t_5)P$.
4. **Demanda total** (H): `H5 = +$F$10*C5`, es decir, $H_i = T\,d_i$.
5. **Solver** (nombres `solver_*`):
   - **Maximizar** F10.
   - Celdas variables: F5:F10.
   - Restricción F5:F9 ≤ E5:E9 ($t_i \le r_i$).
   - Restricción G5:G9 ≥ H5:H9 (lo producido cubre la demanda del ciclo).
   - No negatividad; motor Simplex LP, con la opción «asumir modelo lineal» activada (`solver_lin = 1`).

$$
\max T\quad\text{s.a.}\quad t_i\le r_i,\qquad (t_{i+1}-t_i)P\ge T d_i\ (i=1,\dots,4),\qquad (T-t_5)P\ge T d_5
$$

**Resultados:**

| Posición | Producto real (deducido) | $r_i$ | Inicio $t_i$ | Producción en el ciclo (G) | Demanda en el ciclo (H) |
|---|---|---|---|---|---|
| A | C | 0,3333 | 0 | 956,90 | 956,90 |
| B | A | 0,5 | 0,258621 | 956,90 | 956,90 |
| C | B | 0,7778 | 0,517241 | 1435,34 | 1435,34 |
| D | D | 1 | 0,905172 | 1275,86 | 1275,86 |
| E | E | 1,25 | 1,25 | 1275,86 | 1275,86 |
| | | | **$T^*$ = 1,5948276** (F10) | | |

Todas las restricciones de demanda están activas y el producto E arranca justo cuando se agota ($t_5 = r_5 = 1{,}25$). Comprobación propia: $T^* = 1{,}25\cdot 3700/2900 = 1{,}594828$.

**Gráficos:** ninguno.

**Conclusión.** El resultado es el mismo de L11 p. 19: rotación de 1,5948 meses con la secuencia C (0) → A (0,2586) → B (0,5172) → D (0,9052) → E (1,25).

---

### Hoja `Modelo`: desagregación mensual del plan agregado

**Objetivo (deducido).** Repartir cada mes la producción agregada entre los productos A–E. Cada mes la producción total debe ser al menos la del plan agregado, sin inventarios negativos por producto, y se minimiza el inventario total.

**Datos de entrada:**

- **Pronóstico de la Demanda** (B3:F14, total en G; título en A1:G1). Es la tabla de L11 p. 8, en horas-hombre, por mes:
  - A: 300, 600, 600, 800, 800, 800, 800, 1000, 600, 500, 400, 0.
  - B: 300, 600, 900, 1500, 600, 600, 100, 0, 0, 0, 0, 0.
  - C: 600, 600, 600, 600, 650, 600, 700, 700, 700, 600, 600, 600.
  - D: 600, 800, 1000, 1600, 1400, 1400, 1400, 2000, 2200, 1900, 1800, 1600.
  - E: 800 todos los meses.
  - Totales: 2600, 3400, 3900, 5300, 4250, 4200, 3800, 4500, 4300, 3800, 3600, 3000.
- **Initial Stock** (fila 19): A 300, B 700, C 200, D 800, E 1000; total 3000.
- **Plan Agregado** (P3:P14, valores fijos): 2880, 2880 y luego 3000 en los meses 3–12. Es la producción $P_t$ del modelo de flujo en GAMS ([`../01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/modelo-flujo.lst`](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/modelo-flujo.lst)).

**Parámetros:** no hay costos.

**Método paso a paso:**

1. **Variables:** J3:N14 = $Y_{j,t}$, la producción por producto y mes (bloque «Producción», I1:P1).
2. **Total:** `O3 = SUM(J3:N3)`, es decir, $P_t=\sum_j Y_{j,t}$.
3. **Inventarios** (bloque «Inventarios», filas 21–32). El mes 1 sale de `B21 = $B$19+J3-B3` y los siguientes de `B22 = B21+J4-B4`; es decir, $I_{j,t} = I_{j,t-1}+Y_{j,t}-D_{j,t}$. El total por mes es `G21 = SUM(B21:F21)`.
4. **Inventario Total:** `J18 = SUM(B21:F32)`.
5. **Solver:**
   - **Minimizar J18** (`solver_typ = 2`).
   - Variables J3:N14, no negativas.
   - Restricción B21:F32 ≥ 0.
   - Restricción O3:O14 ≥ P3:P14.
   - Simplex LP, con «asumir modelo lineal».

$$
\min \sum_{t=1}^{12}\sum_{j} I_{j,t}\quad\text{s.a.}\quad I_{j,t} = I_{j,t-1}+Y_{j,t}-D_{j,t}\ge 0,\qquad \sum_j Y_{j,t}\ge X^*_t,\qquad Y_{j,t}\ge 0
$$

**Resultados.** Producción por producto (J3:P14):

| Mes | A | B | C | D | E | Total (O) | Plan Agregado (P) |
|---|---|---|---|---|---|---|---|
| 1 | 280 | 0 | 400 | 0 | 2200 | 2880 | 2880 |
| 2 | 920 | 760 | 600 | 600 | 0 | 2880 | 2880 |
| 3 | 0 | 340 | 600 | 2060 | 0 | 3000 | 3000 |
| 4 | 800 | 1500 | 600 | 540 | 0 | 3440 | 3000 |
| 5 | 800 | 600 | 650 | 1400 | 800 | 4250 | 3000 |
| 6 | 800 | 600 | 600 | 1400 | 800 | 4200 | 3000 |
| 7 | 800 | 100 | 700 | 1400 | 800 | 3800 | 3000 |
| 8 | 1000 | 0 | 700 | 2000 | 800 | 4500 | 3000 |
| 9 | 600 | 0 | 700 | 2200 | 800 | 4300 | 3000 |
| 10 | 500 | 0 | 600 | 1900 | 800 | 3800 | 3000 |
| 11 | 400 | 0 | 600 | 1800 | 800 | 3600 | 3000 |
| 12 | 0 | 0 | 600 | 1600 | 800 | 3000 | 3000 |

Inventario al final de cada mes (B19:G32):

| Mes | A | B | C | D | E | Total |
|---|---|---|---|---|---|---|
| Inicial | 300 | 700 | 200 | 800 | 1000 | 3000 |
| 1 | 280 | 400 | 0 | 200 | 2400 | 3280 |
| 2 | 600 | 560 | 0 | 0 | 1600 | 2760 |
| 3 | 0 | 0 | 0 | 1060 | 800 | 1860 |
| 4–12 | 0 | 0 | 0 | 0 | 0 | 0 |

- **Inventario Total (J18) = 7900.**
- Del mes 4 al 11, el exceso de la producción sobre el plan (440, 1250, 1200, 800, 1500, 1300, 800, 600) es igual a la subcontratación `OUTSOURCE(t)` del modelo GAMS (deducido). Los inventarios totales mensuales (3280, 2760, 1860) son los `I(t)` de la solución GAMS.

**Gráficos:** ninguno.

**Conclusión.** En esta solución el inventario de los primeros meses se acumula sobre todo en E (2400 en el mes 1) y luego en D (1060 en el mes 3). Hace falta para cubrir el pico de demanda del mes 4 (5300) con un plan agregado de 3000. Desde el mes 5 cada producto se fabrica igual a su demanda.

---

### Comparación con [`modelo-desagregacion.xlsx`](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion.md)

| Aspecto | `modelo-desagregacion.xlsx` (Corte 2) | `modelo-desagregacion-v2.xlsx` (este) |
|---|---|---|
| Hojas | `EJEMPLO 1`, `EJEMPLO 2` | `Para una línea de producción`, `Modelo` |
| Posición de las tablas | Filas 2–8; bloque mensual desde la columna B | Filas 3–10; bloque mensual desde la columna A |
| Rótulos | Con errores («ORDERAR CRECIETE», «VAIRBLE DE DECISIÓN», «Fase Produccion Mes») | Corregidos («ordenar creciente», «Variable de decisión», «tasa de producción/mes») |
| Fórmulas | `=B3/C3`, `=(F4-F3)*D3` | Las mismas con prefijo `=+` (`=+B5/C5`); el mes 1 de inventario usa referencia absoluta `$B$19`; total mensual con `SUM(B21:F21)` en vez del balance agregado |
| Objetivo de Solver (mensual) | `N19`, celda **vacía** (error) | `J18`, el inventario total (correcto) |
| Imagen | Captura de la tabla de demanda de L11 p. 8 | No tiene |
| Fila extra | Fila 30 «Initial Stock» con fórmulas que apuntan a una fila vacía | No tiene |
| $T^*$ y tiempos de inicio | 1,594828; 0; 0,258621; 0,517241; 0,905172; 1,25 | Idénticos (diferencias a partir del 11.º decimal) |
| Producción meses 1–4 | A 600/0/600/800; B 0/2600/0/0; C 1000/0/600/600; D 600/0/1000/1600; E 680/280/800/440 | A 280/920/0/800; B 0/760/340/1500; C 400/600/600/600; D 0/600/2060/540; E 2200/0/0/0 |
| Producción meses 5–12 | Igual a la demanda | Igual a la demanda |
| Inventario total | 7900 (3280 + 2760 + 1860) | 7900 (3280 + 2760 + 1860) |

**Conclusión de la comparación:** es el mismo ejercicio. La hoja de una línea da exactamente los mismos resultados en los dos libros. La hoja mensual tiene **óptimos alternativos**: el inventario total queda fijado por el plan agregado (en los meses 1–3 la producción tiene que ser igual al plan y desde el mes 4 no conviene guardar nada). Por eso los dos repartos por producto son distintos pero igual de buenos. Esta versión v2 es la mejor configurada, porque su Solver tiene la celda objetivo correcta.

### Observaciones

- El encabezado automático dice «Corte 3» porque el archivo original estaba en `CORTE 3/`, pero el contenido es del Corte 2 (L11, desagregación).
- La restricción «producción ≥ plan agregado» deja que la producción supere el plan del mes 4 en adelante. Esa diferencia representa la subcontratación del modelo GAMS (deducido); la hoja no la rotula.
- Las letras A–E de la hoja `Para una línea de producción` son posiciones de la secuencia (la A es el producto C), no los mismos productos de la hoja `Modelo`.
- Las demandas de la hoja de una línea (600, 600, 900, 800, 800) son tasas constantes elegidas para que sumen 3700. No corresponden a un mes concreto del pronóstico.


---

<!-- fuente: corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion.md -->
# modelo-desagregacion

> **Archivo:** [`modelo-desagregacion.xlsx`](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion.xlsx) · **Corte 2** · Libro de Excel con 2 hoja(s): `EJEMPLO 1`, `EJEMPLO 2`  
> **Nombre original:** `CORTE 2/MODELO DE DESAGREGACION.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Es el libro de Excel de la clase de desagregación ([`L11-aggregation-and-disaggregation.md`](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md)). Resuelve con **Solver (motor Simplex LP)** los dos pasos de la desagregación del ejemplo de 5 productos (A–E) y 12 meses:

1. **`EJEMPLO 1`**: el tiempo de ciclo máximo de una línea que fabrica los 5 productos en rotación, con producción y demanda constantes (L11, pp. 15–20). Resultado: $T^* = 1{,}5948$ meses.
2. **`EJEMPLO 2`**: desagrega mes a mes, en producción por producto, el plan agregado de 12 meses que sale del modelo de flujo en GAMS de la carpeta hermana ([`../01-planeacion-agregada-modelo-bowman/README.md`](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/README.md)). Busca el menor inventario sin faltantes. Resultado: inventario total de 7900 horas-mes.

Con estos ejemplos se aprende a pasar de un plan en horas-hombre a cantidades por producto. Hay dos maneras: ordenar por tiempo de agotamiento y fijar los tiempos de inicio dentro de un ciclo, o repartir cada mes la producción agregada sin que ningún producto se quede sin inventario. El libro se creó el 2026-09-10, el mismo día en que se corrió el modelo GAMS de la carpeta 01.

---

### Hoja `EJEMPLO 1`: tiempo de ciclo máximo en una línea

**Objetivo (deducido de L11, pp. 16–19).** Una sola línea produce 3700 h/mes y fabrica los productos uno tras otro, en orden creciente de tiempo de agotamiento. Hay que hallar cuándo empieza cada producto ($t_i$) y la duración máxima del ciclo completo ($T$) sin que ningún producto se agote. Un ciclo más largo implica menos set-ups.

**Datos de entrada** (filas 3–7):

| Fila | Producto (posición) | Inventario inicial $I_{0,i}$ (B) | Demanda/mes $d_i$ (C) | Tasa de producción $P$ (D, «Fase Produccion Mes») |
|---|---|---|---|---|
| 3 | A | 200 | 600 | 3700 |
| 4 | B | 300 | 600 | 3700 |
| 5 | C | 700 | 900 | 3700 |
| 6 | D | 800 | 800 | 3700 |
| 7 | E | 1000 | 800 | 3700 |

Ojo con las letras. Aquí A–E son las **posiciones** en la secuencia (ya ordenadas, como en la p. 15 de L11). Por los inventarios iniciales, corresponden a los productos C, A, B, D y E de la tabla de demanda (L11 p. 8 y hoja `EJEMPLO 2`), que es la secuencia de la p. 19 (deducido). Las tasas de demanda suman $600+600+900+800+800 = 3700 = P$, de modo que la línea produce justo lo que se consume.

**Parámetros:**

- Tasa de producción $P = 3700$ h/mes en D3:D7. Coincide con la plantilla regular de la solución de L11 p. 11.
- No hay costos: el modelo solo maximiza $T$.

**Método paso a paso:**

1. **Tiempo de agotamiento** (columna E, rotulada «INV En Meses» y «ORDERAR CRECIETE» en E1): `E3 = B3/C3`, es decir, $r_i = I_{0,i}/d_i$. Da 0,3333; 0,5; 0,7778; 1; 1,25. Los productos ya vienen ordenados de forma creciente.
2. **Variables de decisión** (columna F, «VAIRBLE DE DECISIÓN» en F1): F3:F7 son los tiempos de inicio $t_i$ y F8 es $T$ («T (Duracion del ciclo)»).
3. **Producción del producto $i$ en el ciclo** (columna G, «Produccion Total»): `G3 = (F4-F3)*D3`, es decir, $G_i = (t_{i+1}-t_i)\,P$. Para el último, `G7 = (F8-F7)*D7`, es decir, $G_5 = (T - t_5)\,P$ (reinicio del ciclo).
4. **Demanda del producto durante el ciclo** (columna H, «Demanda Total»): `H3 = $F$8*C3`, es decir, $H_i = T\,d_i$.
5. **Solver** (guardado en los nombres `solver_*` de la hoja):
   - Objetivo: **maximizar** F8 (`solver_typ = 1`).
   - Celdas variables: F3:F8.
   - Restricción 1: F3:F7 ≤ E3:E7, es decir, $t_i \le r_i$ (que no haya faltantes antes del primer lote).
   - Restricción 2: G3:G7 ≥ H3:H7, es decir, $(t_{i+1}-t_i)P \ge T d_i$ (lo producido cubre la demanda del ciclo). La nota en G12, «PRODUCCION TIENE QUE SER MAYOR O IGUAL», recuerda esta restricción.
   - Variables no negativas (`solver_neg = 1`); motor Simplex LP (`solver_eng = 2`).

Es la formulación de L11 p. 17 multiplicada por $d_i$:

$$
\max T\quad\text{s.a.}\quad t_i \le r_i,\qquad (t_{i+1}-t_i)P \ge T\,d_i\ (i=1,\dots,4),\qquad (T-t_5)P \ge T\,d_5,\qquad t_i, T\ge 0
$$

**Resultados** (valores guardados):

| Posición | Producto real (deducido) | $r_i$ (E) | Inicio $t_i$ (F) | Duración del lote $t_{i+1}-t_i$ | Producción en el ciclo (G) | Demanda en el ciclo (H) |
|---|---|---|---|---|---|---|
| A | C | 0,3333 | 0 | 0,2586 | 956,90 | 956,90 |
| B | A | 0,5 | 0,258621 | 0,2586 | 956,90 | 956,90 |
| C | B | 0,7778 | 0,517241 | 0,3879 | 1435,34 | 1435,34 |
| D | D | 1 | 0,905172 | 0,3448 | 1275,86 | 1275,86 |
| E | E | 1,25 | 1,25 | 0,3448 | 1275,86 | 1275,86 |
| | | | **$T^*$ = 1,594828** (F8) | | Σ = 5900,86 | Σ = 5900,86 |

- Todas las restricciones G ≥ H quedan activas (G = H), y la del último producto también: $t_5 = r_5 = 1{,}25$.
- Comprobación propia: $T^* = r_5 P / (d_1+d_2+d_3+d_4) = 1{,}25 \cdot 3700/2900 = 1{,}594828$, igual que en F8.
- Las duraciones de la tabla no están en el Excel: son diferencias entre las celdas de la columna F.

**Gráficos:** ninguno.

**Conclusión.** La rotación óptima dura 1,5948 meses: C desde 0, A desde 0,2586, B desde 0,5172, D desde 0,9052 y E desde 1,25. Lo que limita el ciclo es el producto E, que se agota exactamente cuando empieza a fabricarse. Los resultados coinciden con L11 pp. 19–20.

---

### Hoja `EJEMPLO 2`: desagregación mensual del plan agregado

**Objetivo (deducido).** Repartir cada mes la producción agregada entre los productos A–E. Cada mes la producción total debe ser al menos la del plan agregado, y ningún producto puede tener inventario negativo. Se busca el menor inventario total.

**Datos de entrada:**

- **Pronóstico** (C3:G14, totales en H; título «Pronostico» en D1:F1). Es la demanda en horas-hombre de L11 p. 8:

| Mes | A | B | C | D | E | Total |
|---|---|---|---|---|---|---|
| 1 | 300 | 300 | 600 | 600 | 800 | 2600 |
| 2 | 600 | 600 | 600 | 800 | 800 | 3400 |
| 3 | 600 | 900 | 600 | 1000 | 800 | 3900 |
| 4 | 800 | 1500 | 600 | 1600 | 800 | 5300 |
| 5 | 800 | 600 | 650 | 1400 | 800 | 4250 |
| 6 | 800 | 600 | 600 | 1400 | 800 | 4200 |
| 7 | 800 | 100 | 700 | 1400 | 800 | 3800 |
| 8 | 1000 | 0 | 700 | 2000 | 800 | 4500 |
| 9 | 600 | 0 | 700 | 2200 | 800 | 4300 |
| 10 | 500 | 0 | 600 | 1900 | 800 | 3800 |
| 11 | 400 | 0 | 600 | 1800 | 800 | 3600 |
| 12 | 0 | 0 | 600 | 1600 | 800 | 3000 |

- **Inventario inicial** (fila 17, «Initial Stock»): A 300, B 700, C 200, D 800, E 1000; total 3000.
- **Plan agregado** (Q3:Q14, valores fijos): 2880, 2880 y luego 3000 en los meses 3 a 12. Es exactamente la producción $P_t$ de la solución del modelo de flujo en GAMS ([`../01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/modelo-flujo.lst`](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/modelo-flujo.lst)).
- **Imagen:** en T1, a la derecha de las tablas, hay una captura de la tabla «Month / A–E / Total / Initial Stock» de L11 p. 8. Repite los mismos datos del pronóstico y del inventario inicial.

**Parámetros:** no hay costos. Las únicas constantes son el pronóstico, el inventario inicial y el plan agregado.

**Método paso a paso:**

1. **Variables de decisión:** K3:O14 = $Y_{j,t}$, la producción del producto $j$ en el mes $t$ (bloque «Produccion», título en L1:N1).
2. **Producción total:** `P3 = SUM(K3:O3)`, es decir, $P_t = \sum_j Y_{j,t}$.
3. **Inventario por producto** (bloque «inventarios», filas 18–29): `C18 = C17+K3-C3`, es decir, $I_{j,t} = I_{j,t-1} + Y_{j,t} - D_{j,t}$. La columna H usa el mismo balance con los totales: `H18 = H17+P3-H3`.
4. **Inventario total:** `K17 = SUM(C18:G29)`, es decir, $\sum_{t=1}^{12}\sum_j I_{j,t}$.
5. **Solver** (nombres `solver_*` de la hoja):
   - **Minimizar** (`solver_typ = 2`) la celda `N19`.
   - Variables K3:O14, no negativas.
   - Restricción 1: C18:G29 ≥ 0 (sin faltantes por producto).
   - Restricción 2: P3:P14 ≥ Q3:Q14 (producción ≥ plan agregado).
   - Motor Simplex LP.
   - La celda objetivo N19 está **vacía**: la que debería ir es K17 (deducido; la versión v2 usa la celda equivalente).

Formulación (deducida):

$$
\min \sum_{t=1}^{12}\sum_{j=A}^{E} I_{j,t}\quad\text{s.a.}\quad I_{j,t} = I_{j,t-1} + Y_{j,t} - D_{j,t}\ge 0,\qquad \sum_j Y_{j,t} \ge X_t^*,\qquad Y_{j,t}\ge 0
$$

donde $X_t^*$ es el plan agregado del mes $t$ (columna Q).

**Resultados.** Producción por producto (K3:P14):

| Mes | A | B | C | D | E | Total (P) | Plan agregado (Q) | Exceso sobre el plan |
|---|---|---|---|---|---|---|---|---|
| 1 | 600 | 0 | 1000 | 600 | 680 | 2880 | 2880 | 0 |
| 2 | 0 | 2600 | 0 | 0 | 280 | 2880 | 2880 | 0 |
| 3 | 600 | 0 | 600 | 1000 | 800 | 3000 | 3000 | 0 |
| 4 | 800 | 0 | 600 | 1600 | 440 | 3440 | 3000 | 440 |
| 5 | 800 | 600 | 650 | 1400 | 800 | 4250 | 3000 | 1250 |
| 6 | 800 | 600 | 600 | 1400 | 800 | 4200 | 3000 | 1200 |
| 7 | 800 | 100 | 700 | 1400 | 800 | 3800 | 3000 | 800 |
| 8 | 1000 | 0 | 700 | 2000 | 800 | 4500 | 3000 | 1500 |
| 9 | 600 | 0 | 700 | 2200 | 800 | 4300 | 3000 | 1300 |
| 10 | 500 | 0 | 600 | 1900 | 800 | 3800 | 3000 | 800 |
| 11 | 400 | 0 | 600 | 1800 | 800 | 3600 | 3000 | 600 |
| 12 | 0 | 0 | 600 | 1600 | 800 | 3000 | 3000 | 0 |

La última columna es cálculo propio (P − Q). Ese exceso coincide unidad por unidad con la **subcontratación** `OUTSOURCE(t)` de la solución GAMS (440, 1250, 1200, 800, 1500, 1300, 800 y 600 en los meses 4–11). Es decir, la columna P es la producción propia más la subcontratada (deducido).

Inventario al final de cada mes (C17:H29):

| Mes | A | B | C | D | E | Total |
|---|---|---|---|---|---|---|
| Inicial | 300 | 700 | 200 | 800 | 1000 | 3000 |
| 1 | 600 | 400 | 600 | 800 | 880 | 3280 |
| 2 | 0 | 2400 | 0 | 0 | 360 | 2760 |
| 3 | 0 | 1500 | 0 | 0 | 360 | 1860 |
| 4–12 | 0 | 0 | 0 | 0 | 0 | 0 |

- **Inventario total (K17) = 7900** = 3280 + 2760 + 1860. Coincide con la suma de `I(t)` de la solución GAMS (3280, 2760 y 1860 en los meses 1–3).
- En el mes 4 se consumen los últimos inventarios: B usa sus 1500 y no produce, y E usa 360 y produce 440. Desde el mes 5 la producción de cada producto es igual a su demanda.

**Gráficos:** ninguno (solo la imagen de la tabla de demanda).

**Conclusión.** En los meses 1–3 el plan agregado (2880, 2880 y 3000) se reparte de modo que todo producto llegue sin faltantes al mes 4. En el mes 1 el inventario queda repartido entre los cinco productos. En los meses 2–3 se concentra en B (2400 y 1500) y E (360), y a partir del mes 4 es cero. El total de 7900 queda fijado por el plan agregado. Cualquier reparto que cumpla las restricciones con P = Q en los meses 1–3 da el mismo total, así que hay **óptimos alternativos**: la versión v2 llega a otro reparto con el mismo 7900.

---

### Observaciones

- **Celda objetivo vacía en `EJEMPLO 2`:** Solver apunta a `N19`, que no tiene nada. Con esa configuración solo se obtiene una solución factible. El objetivo correcto sería K17 (inventario total), como en la hoja `Modelo` de [`modelo-desagregacion-v2.md`](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion-v2.md).
- **Fila 30 sobrante:** dice «Initial Stock», pero sus fórmulas (`C30 = C29+K15-C15`) apuntan a la fila 15, que está vacía. Es un arrastre de fórmulas y solo repite el inventario del mes 12 (0).
- **Errores de rótulo:** «ORDERAR CRECIETE» (ordenar creciente), «VAIRBLE DE DECISIÓN» (variable de decisión) y «Fase Produccion Mes» (debería ser «tasa de producción/mes»).
- **Letras A–E en `EJEMPLO 1`:** no son los productos de `EJEMPLO 2` sino posiciones en la secuencia (la A de `EJEMPLO 1` es el producto C). Mismo problema que la p. 15 de L11.
- La restricción es «producción ≥ plan agregado», no «=». Por eso, del mes 4 en adelante, la producción por producto supera el plan; esa diferencia corresponde a la subcontratación del modelo GAMS.
- Las demandas de `EJEMPLO 1` (600, 600, 900, 800, 800) no salen de un mes concreto del pronóstico. Son tasas constantes que suman 3700, igual a la tasa de producción.
- Comparación con [`modelo-desagregacion-v2.xlsx`](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion-v2.md): es el **mismo ejercicio**. `EJEMPLO 1` da los mismos resultados que la hoja `Para una línea de producción`. `EJEMPLO 2` corresponde a la hoja `Modelo`, con otro reparto por producto en los meses 1–4, el mismo inventario total (7900) y el objetivo de Solver bien configurado en v2. El detalle está en el .md de la v2.
