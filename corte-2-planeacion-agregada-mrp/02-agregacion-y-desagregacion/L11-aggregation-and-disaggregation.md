# L11-aggregation-and-disaggregation

> **Archivo:** [`L11-aggregation-and-disaggregation.pdf`](./L11-aggregation-and-disaggregation.pdf) · **Corte 2** · 23 páginas  
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

- [`modelo-desagregacion.md`](./modelo-desagregacion.md) y [`modelo-desagregacion-v2.md`](./modelo-desagregacion-v2.md): los Excel con Solver que resuelven el tiempo de ciclo de las pp. 15–19 (el mismo $T^* = 1{,}5948$). También desagregan mes a mes, por producto, el plan agregado del modelo de flujo en GAMS.
- [`../01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/`](../01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/) (explicado en [`../01-planeacion-agregada-modelo-bowman/README.md`](../01-planeacion-agregada-modelo-bowman/README.md)): `modelo-flujo.gms` implementa este modelo con los datos de las pp. 8–9 (demanda total por mes, costos 80 / 2,7 / 12 / 18 / 10 / 37, inventario inicial 3000 y $L_{R_1}=2880$). Le añade subcontratación a \$95, usa un costo de faltante de 10 000 en lugar de ∞ y no incluye horas de ocio ni inventario de seguridad. Por eso su solución ($z = 4\,062\,000$; producción de 2880, 2880 y luego 3000 h; subcontratación en los meses 4–11) no es la misma de la p. 11.
- [`../01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md`](../01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md): introducción a la planeación agregada y al modelo de transporte de Bowman, que la p. 21 nombra como alternativa.
- [`../parcial-2/parcial-2-solucion.md`](../parcial-2/parcial-2-solucion.md): el punto 1.4 del parcial desagrega horas agregadas con un tiempo de agotamiento común.
- [`../05-mrp-ii-y-capacidad/L15-mrp-ii.md`](../05-mrp-ii-y-capacidad/L15-mrp-ii.md): ubica el «Sistema de Agregación y Desagregación» antes del plan maestro de producción.
- [`../03-wagner-whitin-y-silver-meal/`](../03-wagner-whitin-y-silver-meal/) y [`../04-bom-y-mrp/`](../04-bom-y-mrp/): los pasos siguientes, que son el tamaño de lote por producto y el MRP.

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

## Anexo: texto extraído automáticamente del PDF

> Texto plano tal como sale del PDF, sin fórmulas ni tablas que estén como imagen. La versión fiel y completa es la sección «Contenido completo» de arriba.

### Página 1 · 2 imagen(es)

OPERATIONS 
MANAGEMENT 
Semestre 2026

### Página 2 · 1 imagen(es)

Outline
• Aggregate Planning Methods
– Model with variation of work force and 
backlogging
• Disaggregation Plan

### Página 3 · 1 imagen(es)

Aggregate planning: Model with variation of work 
force and backlogging
Objective: to determine the optimal workforce level, inventory level, and
production per period.
Parameters:
•
T set of planning periods
•
𝐷𝑡Forecast for demand at period t
•
𝐶𝑡Costo unitario de producción en el periodo t (sin nomina)
•
𝑚Horas – hombre requeridas para producir una unidad. m= 1 si la
unidad de agregación es horas- hombre
•
ℎ𝑡
Costo de almacenamiento unitario por unidad del periodo t al
periodo t+1
•
𝜋𝑡Costo unitario de pedido pendiente del periodo t al periodo t+1
•
𝐶𝑅𝑡Costo de una hora-trabajador en tiempo regular en el periodo t
•
𝐶𝑂𝑡
Costo de una hora extra-trabajador en tiempo regular en el
periodo t
•
𝑐𝑤𝑡Costo de aumentar la fuerza de trabajo en trabajador-hora del
periodo t-1 al periodo t
•
𝑐′𝑤𝑡Costo de disminuir la fuerza de trabajo en trabajador-hora del
periodo t-1 al periodo t

### Página 4 · 1 imagen(es)

Aggregate planning: Model with variation of work 
force and backlogging
Decision Variables
•
𝑃𝑡
Cantidad a producir en el periodo t
•
𝐼𝑡
Inventario on-hand al final del periodo t
•
𝑆𝑡
Cantidad pendiente al final del periodo t
•
𝐿𝑅𝑡Horas de trabajo en tiempo regular en el periodo t
•
𝐿𝑜𝑡
Horas extra programadas en el periodo t
•
𝑤𝑡
+ Aumento en el nivel de fuerza de trabajo del periodo t-
1 al periodo t
•
𝑤𝑡
−
Disminución en el nivel de fuerza de trabajo del
periodo t-1 al periodo t

### Página 5 · 1 imagen(es)

Objective Function
• Minimize Costs
min 𝑍=
෍
𝑡=1
𝑇
𝐶𝑡𝑃𝑡+ 𝑐𝑅𝑡𝐿𝑅𝑡+ 𝑐𝑜𝑡𝐿𝑜𝑡+ ℎ𝑡𝐼𝑡+ 𝜋𝑡𝑆𝑡
+ 𝑐𝑤𝑡𝑤𝑡
+ + 𝑐′𝑤𝑡𝑤𝑡
−

### Página 6 · 1 imagen(es)

Constraints
Consistencia de las variables periodo tras periodo:
• Variable de decisión auxiliar 
– 𝑁𝐼𝑡Inventario neto al final del periodo t
𝑁𝐼𝑡= 𝑁𝐼𝑡−1 + 𝑃𝑡−𝐷𝑡∀𝑡∈{2, … , 𝑇}
𝑁𝐼𝑡= 𝐼𝑡−𝑆𝑡
∀𝑡∈{2, … , 𝑇}

### Página 7 · 1 imagen(es)

Constraints
Consistencia en el nivel de fuerza de trabajo
𝐿𝑅𝑡= 𝐿𝑅𝑡−1 + 𝑤𝑡
+ −𝑤𝑡
−∀𝑡∈{2, … , 𝑇}
Relacionar nivel de producción y nivel de fuerza de trabajo
𝐿𝑢𝑡Horas de ocio de los trabajadores en el periodo t
𝐿𝑜𝑡−𝐿𝑢𝑡= 𝑚𝑃𝑡−𝐿𝑅𝑡
Restricciones de no-negatividad
𝑃𝑡, 𝐼𝑡, 𝑆𝑡, 𝐿𝑅𝑡, 𝐿𝑜𝑡, 𝑤𝑡
+, 𝑤𝑡
−, 𝐿𝑢𝑡≥0 ∀𝑡∈{1, , , , , 𝑇}

### Página 8 · 1 imagen(es)

Example: 5 products, 12 months
Month
A
B
C
D
E
Total
1
300
300
600
600
800
2600
2
600
600
600
800
800
3400
3
600
900
600
1000
800
3900
4
800
1500
600
1600
800
5300
5
800
600
650
1400
800
4250
6
800
600
600
1400
800
4200
7
800
100
700
1400
800
3800
8
1000
0
700
2000
800
4500
9
600
0
700
2200
800
4300
10
500
0
600
1900
800
3800
11
400
0
600
1800
800
3600
12
0
0
600
1600
800
3000
Initial
Stock
300
700
200
800
1000
3000
Demand [man-hours]

### Página 9 · 1 imagen(es)

Example: 5 products, 12 months
Cost Coefficients
𝐶𝑡 Costo unitario de producción en el periodo t (sin nomina) $80
ℎ𝑡 Costo de almacenamiento unitario por unidad del periodo t al periodo t+1 $2.70
𝜋𝑡 Costo unitario de pedido pendiente del periodo t al periodo t+1 $∞
𝐶𝑅𝑡 Costo de una hora-trabajador en tiempo regular en el periodo t $12
𝐶𝑂𝑡 Costo de una hora extra-trabajador en tiempo regular en el periodo t $18
𝑐𝑤𝑡 Costo de aumentar la fuerza de trabajo en trabajador-hora del periodo t-1 al 
periodo t $10
𝑐′𝑤𝑡 Costo de disminuir la fuerza de trabajo en trabajador-hora del periodo t-1 al 
periodo t $37

### Página 10 · 1 imagen(es)

Additional Constraints
•
Límite en la fuerza de trabajo: 26 trabajadores (4160 horas)
•
Inventario de seguridad de dos semanas del siguiente periodo
•
Limitar la capacidad de producción
•
Poner un costo fijo de producción
–
Y(t) = 1 si se produce en el periodo t, 0 de lo contrario
–
Restricción : P(t) =l= Cap*Y(t)
•
No producir en dos periodos consecutivos
–
Y(t) + Y(t+1) =l= 1; 
•
El nivel de producción no puede variar más del 20% de un mes 
al siguiente. 
–
P(t+1) =l= 1,2 * P(t) para todo t
–
P(t+1) =g= 0,8*P(t) para todo t
•
No puede despedirse más del 10% de empleados del mes 
anterior. 
–
W-(t) =l= 0,1* Lr(t-1) para todo t. 
•
Subcontratación.

### Página 11 · 1 imagen(es)

Solution 
Mes
I(t)
P(t)
D(t)
L(RT)
L(OT)
L(UT)
w(t)+
w(t)-
1
3280
2880
2600
2880
0
0
0
0
2
3580
3700
3400
3700
0
0
820
0
3
3380
3700
3900
3700
0
0
0
0
4
2125
4045
5300
3700
345
0
0
0
5
2100
4225
4250
3700
525
0
0
0
6
1900
4000
4200
3700
300
0
0
0
7
2250
4150
3800
3700
450
0
0
0
8
2150
4400
4500
3700
700
0
0
0
9
1900
4050
4300
3700
350
0
0
0
10
1800
3700
3800
3700
0
0
0
0
11
1500
3300
3600
3700
0
400
0
0
12
1800
3300
3000
3700
0
400
0
0

### Página 12 · 2 imagen(es)

Solution

### Página 13 · 1 imagen(es)

Disaggregating aggregate 
plans
• ¿Por qué no formular una 
planeación multi-producto desde el 
inicio?
– Optimización entera
– Errores más altos del pronóstico
– Restricciones de secuenciación

### Página 14 · 1 imagen(es)

Disaggregating aggregate 
plans
• Para el caso de producción y 
demanda constante
A
B
C
D
E
Inventario Inicial
300
700
200
800
1000
Demanda Mes 1
300
300
600
600
800
Demanda Mes 2
600
600
600
800
800
Inventario en 
meses
1
1,66
0,33
1,25
1,25

### Página 15 · 1 imagen(es)

Disaggregating aggregate 
plans
• Para el caso de producción y 
demanda constante
Inventario 
Inicial
Demanda 
Mes
tasa de 
Producción/mes
Inventario en 
meses
A
200
600
3700
0,33
B
300
600
3700
0,5
C
700
900
3700
0,78
D
800
800
3700
1
E
1000
800
3700
1,25

### Página 16 · 1 imagen(es)

Optimization Problem
• 𝑇 Tiempo de ciclo para una rotación completa de 
n productos
El numero de set-ups se minimiza cuando el tiempo 
de ciclo es máximo.
• 𝑟𝑖 Tiempo hasta agotar el producto en la i-esima 
posición de producción.
• 𝑡𝑖 Tiempo en que inicia el producto de la i-esima 
posición de producción
• 𝐷𝑖𝑡 Tasa de demanda en el periodo t para i-
esima posición de producción

### Página 17 · 1 imagen(es)

Mathematical Formulation
Maximize T
• Sujet to:
Avoid shortage: 𝑡𝑖≤𝑟𝑖 ∀𝑖
Satisfy the demand:
(𝑡𝑖+1 −𝑡𝑖) 𝑃𝑡/𝐷𝑖𝑡≥𝑇 ∀𝑖= {1, … , 𝑛−1}
Restart the cicle in moment T:
𝑇−𝑡𝑛
𝑃𝑡
𝐷𝑛𝑡≥𝑇

### Página 18 · 1 imagen(es)

What is the extensive 
formulation of the problem?

### Página 19 · 1 imagen(es)

Optimal solution
• T* = 1.5948
• tc = 0
• ta = 0.2586
• tb = 0.5172
• td = 0.9052
• te = 1.25

### Página 20 · 1 imagen(es)

Simulating the solution
Time
C
A
B
D
E
Inv 
Total
0
200
300
700
800
1000
3000
0.2586
1002
145
467
593
793
3000
0.5172
847
947
234
386
586
3000
0.9052
614
714
1320
76
276
3000
1.25
407
507
1010
1076
0
3000
1.59
200
300
700
800
1000
3000

### Página 21 · 1 imagen(es)

Proceso de Planeación
Agregada
Agregar las 
unidades
• Identificar 
la unidad 
de 
agregación 
correcta
Planear la 
producción
• Saber 
Horas de 
trabajo, 
niveles de 
inventario y 
de 
producción
• Bowman
• Modelo en 
GAMS de 
flujo
Desagregar
• Saber la 
cantidad a 
producir de 
cada 
referencia 
o tipo de 
producto.

### Página 22

Mathematical Model
• Minimize σ𝑗=1
𝐽
𝐾𝑗𝜆𝑗/𝑌𝑗
• Subject to:
o σ𝑗=1
𝐽
𝑌𝑗= 𝑋∗
o 𝑎𝑗≤𝑌𝑗≤𝑏𝑗for all product j
•
𝐾𝑗: Set-up cost
•
𝜆𝑗: Demand rate
•
𝑋∗: Aggregated production
•
𝑌𝑗: Disaggregated production
•
En GAMS: y.lo(j) = 1;

### Página 23 · 1 imagen(es)

¡THANKS!
William Guerrero, Ph.D.

