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
| [`L11-aggregation-and-disaggregation.md`](./L11-aggregation-and-disaggregation.md) | Presentación de la clase 11 (23 diapositivas): modelo agregado con fuerza de trabajo y backlog, ejemplo de 5 productos y 12 meses con su solución, tiempo de ciclo máximo y modelo de set-up. | **Sí (1.º)** |
| [`modelo-desagregacion.md`](./modelo-desagregacion.md) | Excel con Solver. `EJEMPLO 1`: tiempo de ciclo máximo, $T^*=1{,}5948$. `EJEMPLO 2`: desagregación mensual del plan GAMS, inventario total de 7900. La celda objetivo de Solver de `EJEMPLO 2` está vacía. | 2.º |
| [`modelo-desagregacion-v2.md`](./modelo-desagregacion-v2.md) | Otra versión del mismo libro, que estaba en la carpeta del Corte 3: rótulos corregidos, Solver bien configurado y otro reparto óptimo con el mismo 7900. Incluye la tabla comparativa con la versión anterior. | 3.º (o en lugar del 2.º) |
| `README.md` | Esta guía. | — |

Los binarios (`.pdf` y `.xlsx`) están al lado de cada `.md`, con el mismo nombre.

## Orden de estudio sugerido

1. Repasar el problema de planeación agregada y el modelo de Bowman en [`../01-planeacion-agregada-modelo-bowman/README.md`](../01-planeacion-agregada-modelo-bowman/README.md).
2. Leer [L11, pp. 3–12](./L11-aggregation-and-disaggregation.md): el modelo con fuerza de trabajo y backlog, y el ejemplo de 5 productos.
3. Ver cómo ese modelo está programado en GAMS en [`../01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/`](../01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/) (explicado en el README de la carpeta 01). El plan que produce es la entrada de la desagregación mensual.
4. Leer L11, pp. 13–20 (tiempo de agotamiento y tiempo de ciclo) y luego la hoja `EJEMPLO 1` o `Para una línea de producción` de los Excel.
5. Estudiar la desagregación mensual en la hoja `Modelo` de [`modelo-desagregacion-v2.md`](./modelo-desagregacion-v2.md) y compararla con `EJEMPLO 2` de [`modelo-desagregacion.md`](./modelo-desagregacion.md).
6. Cerrar con L11, pp. 21–22 (proceso completo y modelo de set-up) y practicar con el punto 1.4 de [`../parcial-2/parcial-2-solucion.md`](../parcial-2/parcial-2-solucion.md).

## Conceptos y fórmulas clave

Todos los detalles y la definición de cada símbolo están en el [Resumen de L11](./L11-aggregation-and-disaggregation.md).

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
| Plan agregado de 5 productos y 12 meses (demanda total 46 650 h-h, inventario inicial 3000) | [L11 pp. 8–12](./L11-aggregation-and-disaggregation.md) | Contratar 820 h en el mes 2 (de 2880 a 3700 h/mes); horas extra en los meses 4–9 (345 a 700 h); 400 h de ocio en los meses 11–12; inventario final de 1800. |
| Inventario en meses con demanda mensual | L11 p. 14 | A 1; B 1,66; C 0,33; D 1,25; E 1,25 meses |
| Tiempo de ciclo máximo (secuencia C→A→B→D→E, $P=3700$) | L11 pp. 15–20; hoja `EJEMPLO 1` de [`modelo-desagregacion.md`](./modelo-desagregacion.md); hoja `Para una línea de producción` de [`modelo-desagregacion-v2.md`](./modelo-desagregacion-v2.md) | $T^*=1{,}5948$ meses; inicios 0; 0,2586; 0,5172; 0,9052; 1,25; inventario total constante de 3000. |
| Desagregación mensual del plan GAMS (2880, 2880 y luego 3000) | Hoja `EJEMPLO 2` de [`modelo-desagregacion.md`](./modelo-desagregacion.md) y hoja `Modelo` de [`modelo-desagregacion-v2.md`](./modelo-desagregacion-v2.md) | Inventario total de 7900 (3280 + 2760 + 1860). Desde el mes 5 la producción es igual a la demanda. Los dos libros dan repartos distintos con el mismo óptimo. |

## Relación con otros temas y proyectos

- **Antes:**
  - [`../01-planeacion-agregada-modelo-bowman/`](../01-planeacion-agregada-modelo-bowman/README.md): planeación agregada (L10), modelo de Bowman y modelo de flujo en GAMS. El `modelo-flujo.gms` implementa el modelo de L11 pp. 3–9, con subcontratación a \$95, y su solución ($z = 4\,062\,000$) es el «Plan Agregado» que se desagrega en los Excel de esta carpeta.
  - [`../../corte-1-pronosticos/`](../../corte-1-pronosticos/): de ahí salen los pronósticos $D_t$ que alimentan el plan.
- **Después:**
  - [`../03-wagner-whitin-y-silver-meal/`](../03-wagner-whitin-y-silver-meal/): tamaño de lote por producto con costos de set-up.
  - [`../04-bom-y-mrp/`](../04-bom-y-mrp/): el plan desagregado (plan maestro) alimenta el MRP.
  - [`../05-mrp-ii-y-capacidad/L15-mrp-ii.md`](../05-mrp-ii-y-capacidad/L15-mrp-ii.md): muestra el «Sistema de Agregación y Desagregación» antes del plan maestro de producción.
- **Evaluación y proyecto:**
  - [`../parcial-2/parcial-2-solucion.md`](../parcial-2/parcial-2-solucion.md): el punto 1.4 desagrega 2620 horas con un tiempo de agotamiento común.
  - [`../proyecto-thyms-gemelo-digital/`](../proyecto-thyms-gemelo-digital/): el gemelo digital de THYMS también desagrega por producto el plan de la estrategia elegida.
- **Scheduling:** las «restricciones de secuenciación» que L11 p. 13 da como razón para desagregar se estudian en el Corte 3, en [`../../corte-3-programacion-scheduling/`](../../corte-3-programacion-scheduling/).
