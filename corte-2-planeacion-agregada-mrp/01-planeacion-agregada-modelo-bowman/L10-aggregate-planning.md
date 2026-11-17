# L10-aggregate-planning

> **Archivo:** [`L10-aggregate-planning.pdf`](./L10-aggregate-planning.pdf) · **Corte 2** · 74 páginas  
> **Nombre original:** `CORTE 2/Lec 10 - Aggregated Planning.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** planeación agregada de la producción: qué es, el proceso S&OP, las opciones de capacidad y de demanda, cómo agregar productos, el método gráfico con tres estrategias (nivelada, subcontratar, perseguir la demanda), el modelo de transporte de Bowman (1956) con su ejemplo resuelto, la desagregación, la planeación en servicios y el revenue management.

### Ideas clave

- La demanda se mide en unidades de producto, pero el plan de operaciones se mide en horas trabajadas o recursos consumidos. El plan agregado convierte el pronóstico (unidades) en niveles de producción (horas) y en un nivel de servicio (%) (p. 3).
- Su objetivo es amortiguar las fluctuaciones de la demanda y equilibrar demanda con capacidad (pp. 4, 9). El caso Frito-Lay (pp. 6-8) muestra por qué importa la alta utilización: procesos especializados con costos fijos altos, lotes grandes y paradas de máquina muy costosas.
- Jerarquía de planes: plan trimestral → plan mensual → plan por línea de ensamble → asignación semanal de materiales y trabajadores (p. 11). Horizontes: largo plazo (> 1 año, alta gerencia: capacidad, localización, R+D+i, inversiones), mediano plazo (3-18 meses, gerentes de operaciones con el equipo S&OP: planeación agregada, contratación, inventario, tercerización) y corto plazo (< 3 meses: programación, órdenes, horas extra) (p. 13).
- S&OP es la planeación intermedia que coordina el pronóstico con las áreas funcionales (p. 14). Sus entradas son diseño de producto y capacidad, inventario y fuerza de trabajo, pronóstico de ventas, soporte de la cadena de suministro y capacidad externa (p. 15). Sus salidas son el plan agregado, que alimenta el MRP, y este al plan detallado o scheduling (p. 17). La p. 19 compara Demand Planning, S&OP y S&OE.
- Capacidad diseñada (teórica, en condiciones ideales) ≥ capacidad efectiva (con restricciones operativas) ≥ capacidad real (con todas las pérdidas) (p. 16).
- El plan agregado decide tasas de producción, niveles de fuerza de trabajo e inventario, horas extra y subcontratación. Su estructura habitual es minimizar el costo total sujeto a satisfacer la demanda, conservar el flujo de materia y respetar restricciones de cadena y presupuesto (pp. 21-22).
- Opciones de capacidad: inventario, contratar/despedir, horas extra o tiempo ocioso, subcontratar y tiempo parcial. Opciones de demanda: precios y promociones, backorders, portafolio amplio (pp. 23-27).
- Agregación: se define una unidad agregada (producto "promedio", horas-hombre, kg, materia prima principal). Según Hax y Meal (1975) se agrega por afinidad de artículos (un combo), familias (comparten un costo común) y tipos (procesos en común) (pp. 28-29, 34). Ejemplo de Nahmias: producto promedio ponderado por la demanda (p. 31).
- Método gráfico en 6 pasos (p. 36), aplicado a un ejemplo de 6 meses (pp. 37-49) con tres estrategias. La más barata del ejemplo es la 2, subcontratar (\$105 152). Le siguen la nivelada (\$108 450) y la de contratar y despedir (\$117 800).
- Modelo de Bowman: es un problema de transporte. Las fuentes son la producción regular o extra de cada periodo y los destinos son los periodos de consumo (más el inventario final). No admite backlog ni decisiones de fuerza de trabajo (pp. 50-54). Ejemplo de dos productos agregados en horas, con costo mínimo de \$8144 (pp. 55-67) y desagregación posterior a un plan maestro (p. 68).
- En servicios lo crítico es controlar el costo de mano de obra (turnos, on-call, personal flotante). El revenue management usa precios diferenciados para asignar la capacidad y maximizar la utilidad (pp. 69-74).

### Fórmulas y métodos

**1. Producto agregado ponderado (Nahmias, p. 31).** Con $D_i$ = demanda del modelo $i$, $h_i$ = horas-hombre por unidad y $p_i$ = precio de venta:

$$w_i = \frac{D_i}{\sum_j D_j},\qquad \bar h = \sum_i w_i h_i,\qquad \bar p = \sum_i w_i p_i,\qquad H = \sum_i h_i D_i$$

Resultado: $\bar h = 5{,}06$ h-h/unid., $\bar p = \$415{,}02$, $\sum D = 1168$, $H \approx 5910$ h-h. Se usa cuando las referencias son parecidas y conviene planear un "producto ficticio".

**2. Demanda agregada en horas (p. 56).** Para dos productos con tiempos 1 h y 0,4 h:

$$D^{agr}_t\,[h] = 1{,}0\,A^{neta}_t + 0{,}4\,B^{neta}_t,\qquad \text{demanda neta} = \text{demanda bruta} - \text{inventario inicial disponible}$$

**3. Método gráfico (pp. 36-49).**
- Tasa nivelada: $r = \dfrac{\sum_t D_t}{\sum_t d_t}$, donde $d_t$ son los días productivos. En el ejemplo, $6200/124 = 50$ unid/día.
- Producción del mes: $P_t = r\,d_t$.
- Inventario: $I_t = I_{t-1} + P_t - D_t$.
- Trabajadores necesarios: $W = \dfrac{r \cdot 1{,}6}{8}$, con 1,6 h por unidad y 8 h por jornada.
- Costo de mano de obra: $W \times \$80 \times \sum_t d_t$.
- Costo de inventario: $\$5 \times \sum_t I_t$.
- En la estrategia de perseguir la demanda (chase), el costo de contratar es $\$300 \times \Delta r^+$ y el de despedir es $\$600 \times \Delta r^-$.

**4. Modelo de Bowman (1956), pp. 51-54.**
- Índices: $i = 1..m$ son las fuentes (por ejemplo tiempo regular y tiempo extra), $j = 1..T$ el periodo de producción y $k = 1..T$ el periodo de consumo.
- Parámetros: $C_{ijk}$ es el costo de producir una unidad en la fuente $i$ y el periodo $j$ y guardarla hasta $k$; $B_{ij}$ es la capacidad; $D_k$ la demanda; $C_R$, $C_O$ y $C_I$ son los costos de tiempo regular, tiempo extra e inventario.
- Variable: $P_{ijk}$, las unidades de la fuente $i$ producidas en $j$ para la demanda de $k$.

$$\min Z = \sum_{i=1}^{m}\sum_{j=1}^{T}\sum_{k=1}^{T} C_{ijk}P_{ijk}$$

$$\text{s.a.}\quad \sum_{k=j}^{T} P_{ijk} \le B_{ij}\ \ \forall i, j \qquad\qquad \sum_{i=1}^{m}\sum_{j=1}^{k} P_{ijk} = D_k\ \ \forall k \qquad\qquad P_{ijk} \ge 0$$

con $C_{R,j,k} = C_R + (k-j)C_I$, $C_{O,j,k} = C_O + (k-j)C_I$ para $k \ge j$ y celdas prohibidas ("X" o "-") si $k < j$. Si $P_{ijk}$ es continua es un PL (fácil); si es entera, un PE ("difícil") (p. 53).

**5. Revenue management (pp. 71-73).** Capacidad = Demanda = $F(\text{precio})$. Sin RM el ingreso es $P^* Q^*$. Con RM se cobran varios precios ($P_1^*$, $P_2^*$) a distintos segmentos y se captura más área bajo la curva de demanda.

### Ejemplos resueltos

| Ejemplo | Páginas | Resultado |
|---|---|---|
| Agregación de 6 modelos (Nahmias, 2007) | 30-31 | Producto promedio: 5,06 h-h y \$415,02; demanda total 1168; 5910 h-h |
| Agregación de productos de cuero y de acero | 32-33 | Solo enunciado; no se resuelve en la presentación |
| Método gráfico, 6 meses (900, 700, 800, 1200, 1500, 1100; 124 días) | 37-41 | Demanda promedio 50 unid/día; inventario acumulado máx. 650 en marzo |
| Estrategia 1: fuerza de trabajo constante (50/día, 10 trabajadores) | 45-47 | Inventario total 1850; costo \$99 200 MO + \$9250 inventario = **\$108 450** |
| Estrategia 2: producir 38/día y subcontratar | 48 | 4712 propias + 1488 subcontratadas; \$75 392 + \$29 760 = **\$105 152** (la menor) |
| Estrategia 3: contratar y despedir (producción = demanda) | 49 | \$99 200 MO + \$9000 contratar + \$9600 despedir = **\$117 800** |
| Modelo de Bowman, 2 productos, 4 meses, regular 160 h y extra 40 h | 55-67 | Demanda agregada 64, 158, 194, 180 y 80 de inventario final; plan 116/160/200/200 h; **costo mínimo \$8144** |
| Desagregación del plan de Bowman | 68 | A = 116, 55, 98, 136; B = 0, 262, 255, 160 |

### Páginas clave

- Conceptos y S&OP: pp. 3-27 (jerarquía p. 11, horizontes p. 13, S&OP pp. 14-20, decisiones y estructura del modelo pp. 21-22, opciones pp. 23-27).
- Agregación: pp. 28-34.
- Método gráfico y las tres estrategias: pp. 36-49 (costos hipotéticos p. 44).
- Modelo de Bowman: pp. 50-54 (formulación p. 54); ejemplo pp. 55-68 (matriz de costos p. 61, solución p. 65, costo p. 67, desagregación p. 68).
- Servicios y revenue management: pp. 69-74.

### Relación con otros archivos del repo

- [modelo-bowman.md](./modelo-bowman.md) y [ejemplo-modelo-bowman.md](./ejemplo-modelo-bowman.md) resuelven en Excel con Solver el ejemplo de las pp. 55-67. Llegan al mismo costo de \$8144 con una asignación distinta, pero igual de óptima.
- [modelo-flujo-gams/](./modelo-flujo-gams/) contiene el modelo de flujo con fuerza de trabajo, horas extra y subcontratación, que es la generalización del modelo de Bowman. Está explicado en el [README](./README.md) de esta carpeta.
- La continuación de esta clase es [L11: agregación y desagregación](../02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md), con el modelo de PL con fuerza de trabajo y backlog, y la desagregación.
- El plan agregado alimenta el MRP: ver [BOM y MRP](../04-bom-y-mrp/) y [MRP II y capacidad](../05-mrp-ii-y-capacidad/).
- Los pronósticos de entrada vienen del [Corte 1](../../corte-1-pronosticos/).

## Contenido completo (página por página)

> Todas las diapositivas tienen la plantilla institucional de la Universidad de La Sabana: franja vertical derecha con una foto del campus (edificio de ladrillo junto a un lago) y el logo «Universidad de La Sabana» abajo. No se repite en cada página.

### Página 1 — Operations Management

**Operations Management**

Second term

> [Imagen decorativa: logo de licencia Creative Commons BY-NC-SA en la esquina inferior izquierda.]

### Página 2 — Outline

- Introduction to "Aggregate Planning"
- Aggregation Exercises
- Simple Aggregate Planning Models

### Página 3 — What is Aggregate Planning?

- Demand is measured in units of products.
- Planning of operations is measured in hours worked, resources consumed.

> [Diagrama: flujo de tres cajas conectadas con flechas, de izquierda a derecha: «Sales forecast [units]» → «Levels of production [hours]» → «Service level [%]».]

### Página 4 — What is aggregated planning made for?

- Mitigate the effects of fluctuations in demand.
  - Which are … ?

### Página 5 — Success factors for having a production system of Goods/services with high utilization

- Effective Aggregate Planning (OM1)
- Efficient production scheduling (OM2)
- Effective maintenance
- Efficient programming of personnel and resources (OM2)

Recuadro naranja: **Why have high utilization of the production system?**

### Página 6 — A Real Case: Frito-Lay

- More than three dozen brands
- 15 of them sell more than \$100 million a year.
- 7 of them sell more than \$1 billion a year.

> [Imagen decorativa: fotos de bolsas de Doritos (Nacho Cheese, Salsa Verde y otra azul) y de papas Lay's (Bar-B-Q, Classic, Salt & Vinegar).]

### Página 7 — How are these references produced?

- Specialized processes with high fixed costs.
  - Production of large batches.
- Low variable costs:
  - specialization of the team.
- Machinery downtime (idle time) generates very high costs!

### Página 8 — Supply Chain

> [Diagrama: tres bloques conectados con flechas de izquierda a derecha, cada uno con su lista:]
> - **Raw Material** → Harvest Seasons; Other seasons; Climate-controlled storage required.
> - **Production** → Different plants in different locations; Different production capacity; Produce well and fast.
> - **Planning Process** → Sales history; Forecast of new products; Innovations; Promotions.

### Página 9 — Aggregated Planning Goal

> [Diagrama: una balanza (barra inclinada) con una flecha grande hacia abajo rotulada «Demand» (arriba a la izquierda) y una flecha grande hacia arriba rotulada «Production Capacity» (abajo a la derecha). Idea: el plan agregado busca equilibrar demanda y capacidad de producción.]

### Página 10 — What are we going to do?

- Generate aggregate production plans for many plants
- In practice:
  - Large companies modify their plans every quarter.
  - What does it mean to change the plan?

### Página 11 — Aggregate Planning

> [Diagrama: embudo/triángulo invertido de tres niveles, de arriba (más ancho) a abajo (más angosto): «Quarterly Plan» → «Monthly plan» → «Production Planning per assembly line». Una flecha desde el nivel inferior apunta a un recuadro: «Allocation of raw materials and workers on a weekly basis to a production line».]

### Página 12 — Competitive Advantage

- Increase market share!
  - Have the product available when the customer wants it
  - Where the customer wants it
  - As the customer wants it
- Aggregate planning requirements

### Página 13 — Planning Process

- Long, medium and short term forecasts.

> [Diagrama: pirámide con tres niveles; a la izquierda, quién decide; a la derecha, recuadros con el horizonte y las decisiones.]

| Nivel (quién) | Horizonte | Decisiones |
|---|---|---|
| Altos ejecutivos | Planeación a largo plazo (> 1 año) | Decisiones de capacidad y localización; R+D+i; Inversiones |
| Gerentes de operaciones con equipo de S&Op | Planeación a mediano plazo (3-18 meses) | Planeación agregada; S&Op; Contratación, inventario, tercerización; Planes operativos |
| Gerentes de operaciones con equipo de supervisores y operarios | Planeación a corto plazo (< 3 meses) | Programación de producción; Ordenes; Trabajo en horas extra |

### Página 14 — S&Op Planning

- Planeación intermedia:
  - Planes operativos que coordinan los pronósticos de demanda con las áreas funcionales de la firma
- **Función:** recoger información del entorno y contexto para tomar decisiones.

### Página 15 — S &Op Inputs

> [Diagrama: nodo central rojo «Equipo de S&Op realiza el plan agregado de operaciones», unido con líneas a cinco nodos alrededor: «Diseño de producto y proceso de planeación de capacidad» (arriba, verde), «Inventario y Nivel de fuerza de trabajo» (derecha, morado), «Pronóstico de ventas» (abajo derecha, azul), «Soporte de la SC» (abajo izquierda, naranja) y «Capacidad Externa» (izquierda, rojo).]

### Página 16 — Capacity Planning

- **Capacidad diseñada**: La máxima producción teórica bajo condiciones ideales.
- **Capacidad efectiva**: La producción esperada considerando restricciones operativas.
- **Capacidad real**: La producción real considerando todas las limitaciones y tiempos improductivos (ver tiempo estándar).
### Página 17 — S&Op Outputs

> [Diagrama: tres bloques conectados con flechas de izquierda a derecha.]
> - **Plan agregado** → Cantidad a producir; Tiempos de producción; Actualizado semanal o mensualmente; Familias de productos.
> - **MRP** → Requerimientos de Materia prima.
> - **Plan detallado de trabajo** → Scheduling; Asignación de cargas de trabajo.

### Página 18 — Foco del trabajo de S&Op Team

> [Diagrama: un recuadro naranja a la izquierda, «Planeación estratégica integrada con **todas** las áreas de la firma», conectado por un arco a tres barras azules apiladas:]
> - Foco en Producción
> - Foco en Supply Chain e inventarios
> - Foco en inversiones de capacidad

### Página 19 — (infografía sin título) Demand Planning vs. S&OP vs. S&OE

> [Imagen: infografía en inglés que compara tres niveles de planeación. Al pie dice «Like, comment and follow Marcia Williams | Join my free newsletter (link in bio)». Se transcribe como tabla.]

| Aspecto | DEMAND PLANNING | S&OP (Sales & Operations Planning) | S&OE (Sales & Operations Execution) |
|---|---|---|---|
| Objective | Forecast future demand | Align demand, supply, finance, and business strategy | Ensure short-term plan execution and resolve near-term issues |
| Scope | Focuses on product/channel/market-level demand | Cross-functional: demand, supply, finance, marketing, and strategy | Tactical execution of supply and demand plans |
| Frequency | Monthly or weekly | Monthly cycle | Weekly or daily |
| Ownership | Demand Planner or Forecasting Team | S&OP Leader with cross-functional leadership | Supply Chain Execution Team (planners, schedulers, logistics) |
| Decision-Making | Data-driven, often decentralized | Cross-functional consensus and scenario-based decision making | Rapid, operational decisions with minimal escalation |
| Inputs | Historical data, market intelligence, promotions, customer input | Demand plan, supply constraints, inventory targets, financial goals | Finalized S&OP plan, current orders, inventory, supplier updates |
| Outputs | Statistical or machine learning (ML) forecast, baseline + adjustments | Balanced demand & supply plan, scenario decisions, executive consensus | Order confirmations, fulfillment plans, shipment schedules |
| Metrics | Forecast accuracy, forecast bias, WMAPE | Plan vs actual (volume/revenue), service level, inventory turns, margin impact | On-time in full (OTIF), order fill rate, schedule adherence |
| Challenges | Bias, low-quality inputs, volatility | Misalignment across functions, executive engagement, long cycle times | Firefighting, capacity bottlenecks, supply disruptions |

### Página 20 — Características de un proceso exitoso de planeación de S&Op

- Representativo
- Oportuno
- Exhaustivo
- Tiene una unidad de medida lógica
  - Kg, unidades, bytes,
- Pronostica la demanda en un tiempo intermedio razonable en unidades agregadas
- Un método para determinar los costos relevantes
- Un modelo para las decisiones de programación de producción

### Página 21 — ¿Qué decisiones toma un plan agregado?

- Tasas de producción
- Niveles de trabajo
- Niveles de inventario
- Horas extra
- Tasas de subcontratación
- Otras variables controlables…

*Para hospitales, empresas, colegios, universidades, etc…*

### Página 22 — Estructura habitual

- F. O : Minimizar el costo total
- Restricciones
  - Satisfacer la demanda
  - Conservación de la materia
  - Restricciones de la Cadena de Abastecimiento
  - Restricciones presupuestales y recursos

Recuadro **Otras estrategias:**
- Disminuir el nivel de trabajo
- Disminuir el inventario
- Alto nivel de servicio

### Página 23 — Soluciones posibles: Mitigar la fluctuación de la demanda

- Manejar altos niveles de inventario
- Variaciones dinámicas de la fuerza de trabajo
- Horas extras o tiempos muertos
- Subcontratar
- Cambiar los precios

### Página 24 — Opciones de Capacidad

- Cambiar los niveles de inventarios:
  - Aprovisionarse para periodos altos de demanda
  - Costos de almacenamiento, seguros, manejo de producto, obsolescencia, costo de capital, etc.
  - Se evita el desabastecimiento

### Página 25 — Opciones de capacidad

- Variar la fuerza de trabajo
  - Contratar o despedir personal
  - Costos de entrenamiento, contratación
  - Costos de indemnización, y bajar la moral del equipo.
- Cambiar las horas de trabajo
  - Costo extra de horas adicionales
  - Fatiga del personal.
  - Hay un límite en las horas extra.
  - Costo de mantener la fábrica abierta /cerrada

### Página 26 — Opciones de capacidad

- Subcontratar
  - Es costoso (ATENCION si no lo es!)
  - Es riesgoso
  - Es difícil hacer un contrato perfecto de subcontratación
- Usar empleados de tiempo parcial
  - Como en los restaurantes, grandes superficies, supermercados, etc.

### Página 27 — Opciones de la Demanda

- Influenciar la demanda:
  - Promociones y publicidad
- Back-ordering:
  - A veces resulta en ventas perdidas
- Tener un portafolio de productos AMPLIO
  - Producir y vender todo el año.
  - Atención al foco del mercado.

### Página 28 — Método de Agregación

- Basado en la existencia de una unidad agregada de producción.
- Artículos parecidos.
- Articulo "promedio"
- E.g.: Referencias que varían muy poco entre sí, por ejemplo, en su color.

> [Imagen decorativa: foto de un surtido grande de productos de ferretería/papelería en empaques de colores.]

### Página 29 — Principio de Jerarquía

- Según Hax et Meal (1975), la forma de agregar productos depende de:
  - Afinidad de Artículos: un combo.
  - Familias: Comparten un costo común.
  - Tipos: procesos en común.

> [Gráfico: torta ilustrativa sin título con 13 porciones. Etiquetas visibles: 51,3 % (la mayor, azul grisáceo), 13,6 % (azul), 9,6 % (naranja) y 7,1 % (verde oliva); el resto son porciones pequeñas sin etiqueta. La leyenda está cortada por el borde de la diapositiva y solo se lee el inicio de cada nombre: «Uni…», «Afg…», «Alb…», «Arm…», «Ang…», «Arg…», «Aus…», «Aus…», «Aze…», «Bos…», «Bar…», «Bel…», «Oth…» (parecen nombres de países). Es una imagen de apoyo visual; no se usa en ningún cálculo.]

### Página 30 — Ejemplo (Nahmias, 2007)

| Producto | Cantidad horas-hombre | Precio de venta |
|---|---|---|
| 1 | 4,2 | \$285 |
| 2 | 4,9 | \$345 |
| 3 | 5,1 | \$395 |
| 4 | 5,2 | \$425 |
| 5 | 5,4 | \$525 |
| 6 | 5,8 | \$725 |

- No es racional pensar en la producción de cada tipo de producto de forma independiente.
- Es mejor pensar en un producto ficticio que tiene un precio de venta ponderado y un requerimiento de horas-hombre ponderado

### Página 31 — Ejemplo (Nahmias, 2007)

| Modelo | Cantidad horas-hombre | Precio de venta | Demanda | % |
|---|---|---|---|---|
| 1 | 4,2 | \$ 285 | 120 | 10,3% |
| 2 | 4,9 | \$ 345 | 340 | 29,1% |
| 3 | 5,1 | \$ 395 | 152 | 13,0% |
| 4 | 5,2 | \$ 425 | 365 | 31,3% |
| 5 | 5,4 | \$ 525 | 102 | 8,7% |
| 6 | 5,8 | \$ 725 | 89 | 7,6% |
| **Promedio** | **5,06** | **\$415,02** | **TOTAL 1168** | |

Es decir, se requieren 5910 horas-hombre de trabajo

Cálculo implícito (verificado con los números de la tabla): la columna % es la participación de cada modelo en la demanda, $w_i = D_i / \sum_j D_j$ con $\sum_j D_j = 1168$. Los promedios son ponderados por esa participación:

$$\bar h = \sum_i w_i h_i = \frac{4{,}2(120)+4{,}9(340)+5{,}1(152)+5{,}2(365)+5{,}4(102)+5{,}8(89)}{1168} = \frac{5910{,}2}{1168} \approx 5{,}06 \text{ h-h/unidad}$$

$$\bar p = \sum_i w_i p_i = \frac{484\,740}{1168} \approx \$415{,}02$$

y las horas totales son $\sum_i h_i D_i = 5910{,}2 \approx 5910$ horas-hombre (equivale a $1168 \times 5{,}06$).

### Página 32 — Más ejercicios de Agregación

Una empresa que hace manufactura de productos de cuero tiene el siguiente pronóstico de demanda (en unidades) para cada producto de los próximos cuatro meses (ver tabla 1). Adicionalmente la tabla 2 presenta el precio promedio de venta (en dólares), el requerimiento de cuero en metros cuadrados por unidad de venta, y el número de horas-hombre requeridas para manufacturar una unidad de venta. Considerando estos datos, proponga un pronóstico AGREGADO de demanda para los meses enero-abril.

**Pronóstico de demanda [unid.]**

| Mes | Zapatos(par) | Chaqueta | Bolso | Billetera |
|---|---|---|---|---|
| Enero | 36 | 30 | 68 | 38 |
| Febrero | 2 | 61 | 53 | 52 |
| Marzo | 35 | 78 | 23 | 79 |
| Abril | 59 | 53 | 77 | 7 |

*Tabla 1: Pronóstico de demanda por referencia*

| Producto | Precio Prom. (USD) | Requerimiento cuero (m2) | Horas-hombre |
|---|---|---|---|
| Zapatos(par) | 50 | 2 | 5 |
| Chaqueta | 110 | 10 | 4 |
| Bolso | 95 | 12 | 7 |
| Billetera | 30 | 1 | 5 |

*Tabla 2: Características de producción y ventas de cada referencia*
### Página 33 — Más ejercicios de Agregación

Una empresa que hace manufactura de productos de acero tiene el siguiente pronóstico de demanda (en unidades) para cada producto de los próximos cuatro meses (ver tabla 1). Adicionalmente la tabla 2 presenta el precio promedio de venta (en dólares), el requerimiento de acero en KG por unidad de venta, y el número de horas-hombre requeridas para manufacturar una unidad de venta. Considerando estos datos, proponga un pronóstico AGREGADO de demanda para los meses enero-abril.

**Pronóstico de demanda [unid.]**

| Mes | Vigas 5 m | Láminas (5mX5m) | tornillos | Alambre(10m) |
|---|---|---|---|---|
| Enero | 36 | 30 | 68 | 38 |
| Febrero | 2 | 61 | 53 | 52 |
| Marzo | 35 | 78 | 23 | 79 |
| Abril | 59 | 53 | 77 | 7 |

*Tabla 1: Pronóstico de demanda por referencia*

| Producto | Precio Prom. (USD) | Requerimiento acero (kg) | Horas-hombre |
|---|---|---|---|
| Vigas 5 m | 50 | 2 | 5 |
| Láminas (5mX5m) | 60 | 20 | 6 |
| tornillos | 0.1 | 0.01 | 0.01 |
| Alambre(10m) | 15 | 4 | 4 |

*Tabla 2: Características de producción y ventas de cada referencia*

> Nota: la tabla 1 tiene exactamente los mismos números que la del ejercicio de cuero de la página 32; solo cambian los productos y la tabla 2. Ninguno de los dos ejercicios se resuelve en la presentación.

### Página 34 — Resumen

- Posibilidades para agregar productos:
  - Requerimientos de materia prima más importante
  - Requerimiento de horas-hombre
  - Unidades comunes: Kg, l, ton, etc.
  - Unidades (cuando tiene sentido)

### Página 35 — Modelos de Planeación Agregada

Diapositiva separadora de sección: **Modelos de Planeación Agregada**.

### Página 36 — Método gráfico (algoritmo)

1. Determine la demanda de cada periodo
2. Determine la capacidad en tiempo regular, horas extra, y subcontratación
3. Encuentre costos de mano de obra, contratación y despido, y de mantener inventario
4. Considere todas las restricciones de las políticas de los empleados
5. Encuentre la demanda promedio y grafíquela como una constante.
6. Analice y tome decisiones.

### Página 37 — Ejemplo

| Mes | Demanda esperada | Días de producción | Demanda por día |
|---|---|---|---|
| Enero | 900 | 22 | 41 |
| Febrero | 700 | 18 | 39 |
| Marzo | 800 | 21 | 38 |
| Abril | 1200 | 21 | 57 |
| Mayo | 1500 | 22 | 68 |
| Junio | 1100 | 20 | 55 |
| **Total** | **6200** | **124** | |

(Demanda por día = demanda esperada / días de producción, redondeada: p. ej. 900/22 = 40,9 ≈ 41.)

### Página 38 — Estrategia: Producir el promedio diario

- Demanda promedio diaria:

$$\frac{\text{demanda total}}{\text{días de producción}} = \frac{6200}{124} = 50\ uni/dia$$

- Estrategia: producir al día 50 unidades

### Página 39 — Método gráfico:

> [Gráfico: barras + línea, título «Comportamiento diario de la demanda por mes». Eje X «Mes de planeación»: Enero - 22 días, Febrero - 18 días, Marzo - 21 días, Abril - 21 días, Mayo - 22 días, Junio - 20 días. Eje Y «Unidades por día» de 0 a 80. Barras azules «Demanda por día en cada mes»: 41, 39, 38, 57, 68, 55. Línea roja horizontal «Demanda Promedio» en 50. Los tres primeros meses quedan por debajo del promedio y los tres últimos por encima.]

### Página 40 — Análisis

| Mes | Demanda esperada | Días de producción | Demanda por día en cada mes | Producción mensual | Exceso /faltante |
|---|---|---|---|---|---|
| Enero - 22 días | 900 | 22 | 41 | 1100 | 200 |
| Febrero - 18 días | 700 | 18 | 39 | 900 | 200 |
| Marzo - 21 días | 800 | 21 | 38 | 1050 | 250 |
| Abril - 21 días | 1200 | 21 | 57 | 1050 | -150 |
| Mayo - 22 días | 1500 | 22 | 68 | 1100 | -400 |
| Junio - 20 días | 1100 | 20 | 55 | 1000 | -100 |
| **Total** | **6200** | **124** | | | |

(Producción mensual = 50 unid/día × días del mes; Exceso/faltante = producción mensual − demanda esperada.)

### Página 41 — Método gráfico:

> [Gráfico: barras + dos líneas, título «Comportamiento del plan de producción por mes». Eje X «Mes de planeación» (Enero - 22 días … Junio - 20 días). Eje Y rotulado «Unidades por día» de 0 a 1600 (aunque los valores son mensuales). Barras azules «Demanda esperada»: 900, 700, 800, 1200, 1500, 1100. Línea roja «Producción mensual»: 1100, 900, 1050, 1050, 1100, 1000. Línea verde «Inventario Acumulado»: 200, 400, 650, 500, 100, 0 (sube hasta marzo y baja a 0 en junio).]

### Página 42 — Problema de planeación agregada

- ¿Cómo produzco 50 unidades diarias durante 6 meses?
  - Recursos (humanos, físicos, financieros y de información)
    - Contrataciones, despidos
  - Actividades a realizar:
    - Crear nuevas líneas de ensamble
  - Tercerización y gestión de proveedores

### Página 43 — Estrategias posibles

- Mantener una fuerza de trabajo constante:
  - Para producir 50 /día
  - Para producir 38 /día ( + tercerización)
- Tener una fuerza de trabajo dinámica.

### Página 44 — Costos hipotéticos

| Concepto | Costo |
|---|---|
| Costo de mantener inventario | \$5 / unid –mes |
| subcontratar | \$20 /unid |
| Salario | \$80 /día (8 horas) |
| Hora extra | \$17 /hora |
| Horas para producir una unidad | 1.6 horas |
| Costo de aumentar la producción diaria | \$300 /unid |
| Costo de disminuir la producción diaria | \$600/día |

### Página 45 — Análisis de inventario

| Mes | Demanda esperada | Producción mensual | Exceso /faltante | Inventario Acumulado |
|---|---|---|---|---|
| Enero - 22 días | 900 | 1100 | 200 | 200 |
| Febrero - 18 días | 700 | 900 | 200 | 400 |
| Marzo - 21 días | 800 | 1050 | 250 | 650 |
| Abril - 21 días | 1200 | 1050 | -150 | 500 |
| Mayo - 22 días | 1500 | 1100 | -400 | 100 |
| Junio - 20 días | 1100 | 1000 | -100 | 0 |

Recuadro: **Inventario total = 1850 unidades** (200 + 400 + 650 + 500 + 100 + 0).

Relación usada: $I_t = I_{t-1} + P_t - D_t$, con $I_0 = 0$.

### Página 46 — Análisis de Costos

- FUERZA DE TRABAJO: 50 unidades por día (8 horas)
  - 50 X 1.6 = 80 horas de trabajo al día
  - 8 horas / 1.6h/u = 5 unidades diarias por trabajador
  - Se requieren 10 trabajadores.
  - \$99200 = 10 X \$80 X 124 días
- Inventario
  - \$9250 = 1850uni X \$5/uni
- Otros costos = 0
- **TOTAL = \$108 450**
  - 91.5% son costos de mano de obra
  - 8.5% son costos de inventario

### Página 47 — (gráfico) Demanda Acumulada Vs Producción Acumulada

> [Gráfico: dos líneas, título «Demanda Acumulada Vs Producción Acumulada». Eje X: Enero - 22 días … Junio - 20 días. Eje Y de 0 a 7000. Línea azul «Demanda Acumulada»: 900, 1600, 2400, 3600, 5100, 6200. Línea verde «Producción Acumulada»: 1100, 2000, 3050, 4100, 5200, 6200. La producción acumulada va siempre por encima de la demanda acumulada (no hay faltantes); ambas terminan en 6200 en junio. La distancia vertical entre las curvas es el inventario de la página 45.]

### Página 48 — Estrategia 2: subcontratar

- Producir lo mínimo pronosticado y subcontratar el resto.
  - 38 unidades diarias
  - 4712 unidades en 124 días
  - Subcontratar 1488 unidades
- ¿Cuáles son los costos?
  - Mano de obra (7.6 trabajadores) = \$75 392
  - Subcontratar = \$29 760
  - Inventario = \$0
  - TOTAL : \$105 152
    - 71,7% mano de obra
    - 28,3% subcontratar

> Nota: en la imagen de la diapositiva un recuadro blanco tapa la respuesta (desde «Mano de obra…» hasta el final), probablemente para revelarla con animación. El texto oculto sí está en la capa de texto del PDF y es el que se transcribe arriba. Comprobación: $38 \times 124 = 4712$; $6200 - 4712 = 1488$; trabajadores $= 38 \times 1{,}6 / 8 = 7{,}6$; mano de obra $= 7{,}6 \times 80 \times 124 = 75\,392$; subcontratación $= 1488 \times 20 = 29\,760$.
### Página 49 — Estrategia 3: Contratar y despedir

- Producción = Demanda

| MES | Producción diaria | Costo de Fuerza de trabajo | Costo de contratar | Costo de despedir | Costo total |
|---|---|---|---|---|---|
| Enero | 41 | \$14 400 | \$0 | \$0 | \$14 400 |
| Febrero | 39 | \$11 200 | \$0 | \$1200 (2X600) | \$12 400 |
| Marzo | 38 | \$12 800 | \$0 | \$600 | \$13 400 |
| Abril | 57 | \$19 200 | \$5700 (19X300) | \$0 | \$24 900 |
| Mayo | 68 | \$24 000 | \$3300 (11X300) | \$0 | \$27 300 |
| Junio | 55 | \$17 600 | \$0 | \$7800 (13x600) | \$25 400 |
| **TOTAL** | | **\$99 200** | **\$9 000** | **\$9600** | **\$117 800** |

Cálculo implícito (verificado): costo de fuerza de trabajo del mes = demanda del mes × 1,6 h/unid ÷ 8 h/día × \$80/día = demanda × \$16 (p. ej. enero: $900 \times 16 = 14\,400$). Contratar cuesta \$300 por unidad diaria que sube la tasa y despedir \$600 por unidad diaria que baja (p. ej. abril: $57-38=19$ → $19\times300=5700$; junio: $68-55=13$ → $13\times600=7800$). Enero no paga contratación: se asume que la tasa inicial ya es 41.

### Página 50 — Analytic Models

- Bowman's simple net model (1956) - based on the transport problem

ASSUMPTIONS:
- ***m*** production sources.
- ***T*** planning periods.
- minimize the cost of production ***Z***
  - *Production cost*
  - *Storage cost*
- *No backlogging nor workforce level decisions.*

### Página 51 — Analytic Models

- Modelo de red simple de Bowman (1956) - basado en el problema de transporte

**NOTACIÓN (PARAMETROS):**
- $C_{ijk}$ = Costo marginal de producción de una unidad en la fuente *i*, en el periodo *j* y almacenado hasta el periodo *k*
- $B_{ij}$ = Capacidad de producción en la fuente *i* en el periodo *j*
- $D_k$ = Demanda pronosticada en el periodo *k*

### Página 52 — Analytic Models

**MAS NOTACIÓN (PARAMETROS):**
- $C_R$ = Costo de producir una unidad en tiempo regular
- $C_O$ = Costo de producir una unidad en tiempo extra
- $C_I$ = Costo de almacenar una unidad en inventario

**VARIABLES DE DECISIÓN:**

$P_{ijk}$ = Número de unidades producidas en la fuente *i*, en el periodo *j*, para satisfacer la demanda del periodo *k*

### Página 53 — Analytic Models

- $P_{ijk}$ es entera o continua depende del contexto.
  - Continua: Fácil de resolver (Programación lineal)
  - Entera: "Difícil" de resolver (Programación entera)

Tabla «Plan de Producción de la fuente i» (las X marcan combinaciones prohibidas: no se puede producir en un mes para consumir en un mes anterior, porque no hay backlog):

| Periodo de Producción \ Periodo de consumo | Enero | Febrero | Marzo | Abril | Mayo | Producción TOTAL |
|---|---|---|---|---|---|---|
| Enero | | | | | | |
| Febrero | X | | | | | |
| Marzo | X | X | | | | |
| Abril | X | X | X | | | |
| Mayo | X | X | X | X | | |
| DEMANDA TOTAL | | | | | | |

### Página 54 — Bowman Model

Minimizar Z =

$$\sum_{i=1}^{m}\sum_{j=1}^{T}\sum_{k=1}^{T} C_{ijk}P_{ijk}$$

Sujeto a:

Recuadro «Restricción de capacidad de producción»:

$$\sum_{k=j}^{T} P_{ijk} \le B_{ij},\ \forall i = 1,2\ldots m;\ j = i,2\ldots T$$

Recuadro «Restricción de satisfacción de demanda»:

$$\sum_{i=1}^{m}\sum_{j=1}^{k} P_{ijk} = D_k,\ \forall k = i,2\ldots T$$

$$P_{ijk} \ge 0$$

> Nota: en los índices de los «para todo» la diapositiva escribe «$j = i, 2 \ldots T$» y «$k = i, 2 \ldots T$»; por el contexto debe leerse $j = 1, 2, \ldots, T$ y $k = 1, 2, \ldots, T$ (errata de la diapositiva).

### Página 55 — Example

| MES | Demanda producto A | Demanda producto B |
|---|---|---|
| 1 | 100 | 200 |
| 2 | 90 | 190 |
| 3 | 110 | 210 |
| 4 | 100 | 200 |

- Inventario inicial es 36 del producto A, 220 unidades del producto B
- Hacer una unidad de producto 1 toma 1 hora.
- Hacer una unidad de producto 2 toma 0.4 horas.
- Costo de producción regular: \$10/hora
- Costo de producción extra: \$15/hora
- Costo de almacenamiento \$4/mes (productos hechos en una hora)
- Capacidad regular 160 horas/mes, extra = 40 horas /mes

(«Producto 1» y «producto 2» son los productos A y B.)

### Página 56 — Example: Aggregating Products

1. Calcular la demanda neta = demanda bruta – inventario inicial
2. Encontrar unidades agregadas. Ejemplo: usar horas de trabajo

| MES | Dem. Bruta Prod. A | Dem. Bruta Prod. B | Dem. Neta Prod. A | Dem. Neta Prod. B | Demanda AGREGADA |
|---|---|---|---|---|---|
| 1 | 100 | 200 | 64 | 0 | 64 |
| 2 | 90 | 190 | 90 | 170 | 158 |
| 3 | 110 | 210 | 110 | 210 | 194 |
| 4 | 100 | 200 | 100 | 200 | 180 |

*Demanda Agregada [h] = 1,0A + 0,4B*

(Detalle: A: $100-36=64$. B: el inventario de 220 cubre los 200 del mes 1 y sobran 20, así que la neta del mes 2 es $190-20=170$. Mes 2: $90 + 0{,}4\times170 = 158$; mes 3: $110+0{,}4\times210=194$; mes 4: $100+0{,}4\times200=180$.)

### Página 57 — Example: Cost Matrix

1. Calcular el costo unitario de producción + almacenamiento para cada combinación de periodo de producción -consumo

(Primer paso de una animación: solo está llena la primera celda.)

| Periodo de Producción | Periodo Consumo 1 | Periodo Consumo 2 | Periodo Consumo 3 | Periodo Consumo 4 | Inventario Final |
|---|---|---|---|---|---|
| 1: Tiempo Regular / Tiempo extra | $C_R$ / $C_O$ | | | | |
| 2: Tiempo Regular / Tiempo extra | - | | | | |
| 3: Tiempo Regular / Tiempo extra | - | | | | |
| 4: Tiempo Regular / Tiempo extra | - | | | | |

(En la fila 1, «Tiempo extra» está escrito en rojo.)

### Página 58 — Example: Cost Matrix

1. Calcular el costo unitario de producción + almacenamiento para cada combinación de periodo de producción -consumo

| Periodo de Producción | Periodo Consumo 1 | Periodo Consumo 2 | Periodo Consumo 3 | Periodo Consumo 4 | Inventario Final |
|---|---|---|---|---|---|
| 1: Tiempo Regular / Tiempo extra | $C_R$ / $C_O$ | $C_R+C_I$ / $C_O+C_I$ | | | |
| 2: Tiempo Regular / Tiempo extra | - | $C_R$ / $C_O$ | | | |
| 3: Tiempo Regular / Tiempo extra | - | - | | | |
| 4: Tiempo Regular / Tiempo extra | - | - | | | |

### Página 59 — Example: Cost Matrix

1. Calcular el costo unitario de producción + almacenamiento para cada combinación de periodo de producción -consumo

| Periodo de Producción | Periodo Consumo 1 | Periodo Consumo 2 | Periodo Consumo 3 | Periodo Consumo 4 | Inventario Final |
|---|---|---|---|---|---|
| 1: Tiempo Regular / Tiempo extra | $C_R$ / $C_O$ | $C_R+C_I$ / $C_O+C_I$ | $C_R+2C_I$ / $C_O+2C_I$ | | |
| 2: Tiempo Regular / Tiempo extra | - | $C_R$ / $C_O$ | $C_R+C_I$ / $C_O+C_I$ | | |
| 3: Tiempo Regular / Tiempo extra | - | - | $C_R$ / $C_O$ | | |
| 4: Tiempo Regular / Tiempo extra | - | - | - | | |

### Página 60 — Example: Cost Matrix

1. Calcular el costo unitario de producción + almacenamiento para cada combinación de periodo de producción -consumo

| Periodo de Producción | Periodo Consumo 1 | Periodo Consumo 2 | Periodo Consumo 3 | Periodo Consumo 4 | Inventario Final |
|---|---|---|---|---|---|
| 1: Tiempo Regular / Tiempo extra | $C_R$ / $C_O$ | $C_R+C_I$ / $C_O+C_I$ | $C_R+2C_I$ / $C_O+2C_I$ | $C_R+3C_I$ / $C_O+3C_I$ | $C_R+4C_I$ / $C_O+4C_I$ |
| 2: Tiempo Regular / Tiempo extra | - | $C_R$ / $C_O$ | $C_R+C_I$ / $C_O+C_I$ | $C_R+2C_I$ / $C_O+2C_I$ | $C_R+3C_I$ / $C_O+3C_I$ |
| 3: Tiempo Regular / Tiempo extra | - | - | $C_R$ / $C_O$ | $C_R+C_I$ / $C_O+C_I$ | $C_R+2C_I$ / $C_O+2C_I$ |
| 4: Tiempo Regular / Tiempo extra | - | - | - | $C_R$ / $C_O$ | $C_R+C_I$ / $C_O+C_I$ |

Regla general: producir en $j$ para consumir en $k \ge j$ cuesta $C_R + (k-j)C_I$ en tiempo regular y $C_O + (k-j)C_I$ en tiempo extra; la columna «Inventario Final» se trata como un periodo 5.

### Página 61 — Example: Cost Matrix

1. Calcular el costo unitario de producción + almacenamiento para cada combinación de periodo de producción -consumo

| Periodo de Producción | Periodo Consumo 1 | Periodo Consumo 2 | Periodo Consumo 3 | Periodo Consumo 4 | Inventario Final |
|---|---|---|---|---|---|
| 1: Tiempo Regular | $C_R$ = \$10 | $C_R+C_I$ = \$14 | $C_R+2C_I$ = \$18 | $C_R+3C_I$ = \$22 | $C_R+4C_I$ = \$26 |
| 1: Tiempo extra | $C_O$ = \$15 | $C_O+C_I$ = \$19 | $C_O+2C_I$ = \$23 | $C_O+3C_I$ = \$27 | $C_O+4C_I$ = \$31 |
| 2: Tiempo Regular | - | $C_R$ = \$10 | $C_R+C_I$ = \$14 | $C_R+2C_I$ = \$18 | $C_R+3C_I$ = \$22 |
| 2: Tiempo extra | - | $C_O$ = \$15 | $C_O+C_I$ = \$19 | $C_O+2C_I$ = \$23 | $C_O+3C_I$ = \$27 |
| 3: Tiempo Regular | - | - | $C_R$ = \$10 | $C_R+C_I$ = \$14 | $C_R+2C_I$ = \$18 |
| 3: Tiempo extra | - | - | $C_O$ = \$15 | $C_O+C_I$ = \$19 | $C_O+2C_I$ = \$23 |
| 4: Tiempo Regular | - | - | - | $C_R$ = \$10 | $C_R+C_I$ = \$14 |
| 4: Tiempo extra | - | - | - | $C_O$ = \$15 | $C_O+C_I$ = \$19 |

### Página 62 — Example: Cost Matrix

3. Calcular el costo unitario de producción + almacenamiento para cada combinación de periodo de producción -consumo

(La numeración salta de 1 a 3 en la diapositiva.)

| Periodo de Producción | Periodo Consumo 1 | Periodo Consumo 2 | Periodo Consumo 3 | Periodo Consumo 4 | Inventario Final | Capacidad |
|---|---|---|---|---|---|---|
| 1: Tiempo Regular / Tiempo extra | $C_R$ / $C_O$ | $C_R+C_I$ / $C_O+C_I$ | $C_R+2C_I$ / $C_O+2C_I$ | $C_R+3C_I$ / $C_O+3C_I$ | $C_R+4C_I$ / $C_O+4C_I$ | 160 / 40 |
| 2: Tiempo Regular / Tiempo extra | - | $C_R$ / $C_O$ | $C_R+C_I$ / $C_O+C_I$ | $C_R+2C_I$ / $C_O+2C_I$ | $C_R+3C_I$ / $C_O+3C_I$ | 160 / 40 |
| 3: Tiempo Regular / Tiempo extra | - | - | $C_R$ / $C_O$ | $C_R+C_I$ / $C_O+C_I$ | $C_R+2C_I$ / $C_O+2C_I$ | 160 / 40 |
| 4: Tiempo Regular / Tiempo extra | - | - | - | $C_R$ / $C_O$ | $C_R+C_I$ / $C_O+C_I$ | 160 / 40 |
| **Demanda** | 64 | 158 | 194 | 180 | 80 | |

(La demanda del «Inventario Final» es 80 horas; la presentación no explica de dónde sale ese valor, se da como dato.)

### Página 63 — Example: Solución (Usando PL)

4. Calcular la solución usando métodos de programación matemática

(Primer paso de la animación que va llenando la solución.)

| Periodo de Producción | Periodo Consumo 1 | Periodo Consumo 2 | Periodo Consumo 3 | Periodo Consumo 4 | Inventario Final | Capacidad |
|---|---|---|---|---|---|---|
| 1: Tiempo Regular / Tiempo extra | 64 / 0 | | | | | 160 / 40 |
| 2: Tiempo Regular / Tiempo extra | X | | | | | 160 / 40 |
| 3: Tiempo Regular / Tiempo extra | X | X | | | | 160 / 40 |
| 4: Tiempo Regular / Tiempo extra | X | X | X | | | 160 / 40 |
| **Demanda** | 64 | 158 | 194 | 180 | 80 | |

### Página 64 — Example: Solución (Usando PL)

4. Calcular la solución usando métodos de programación matemática

| Periodo de Producción | Periodo Consumo 1 | Periodo Consumo 2 | Periodo Consumo 3 | Periodo Consumo 4 | Inventario Final | Capacidad |
|---|---|---|---|---|---|---|
| 1: Tiempo Regular / Tiempo extra | 64 / 0 | 0 | | | | 160 / 40 |
| 2: Tiempo Regular / Tiempo extra | X | 158 / 0 | | | | 160 / 40 |
| 3: Tiempo Regular / Tiempo extra | X | X | | | | 160 / 40 |
| 4: Tiempo Regular / Tiempo extra | X | X | X | | | 160 / 40 |
| **Demanda** | 64 | 158 | 194 | 180 | 80 | |

### Página 65 — Example: Solución (Usando PL)

4. Calcular la solución usando métodos de programación matemática

| Periodo de Producción | Periodo Consumo 1 | Periodo Consumo 2 | Periodo Consumo 3 | Periodo Consumo 4 | Inventario Final | Capacidad |
|---|---|---|---|---|---|---|
| 1: Tiempo Regular | 64 | 0 | 0 | 0 | 52 | 160 |
| 1: Tiempo extra | 0 | | | | 0 | 40 |
| 2: Tiempo Regular | X | 158 | 2 | 0 | 0 | 160 |
| 2: Tiempo extra | X | 0 | 0 | | | 40 |
| 3: Tiempo Regular | X | X | 160 | 0 | 0 | 160 |
| 3: Tiempo extra | X | X | 32 | 8 | | 40 |
| 4: Tiempo Regular | X | X | X | 160 | 0 | 160 |
| 4: Tiempo extra | X | X | X | 12 | 28 | 40 |
| **Demanda** | 64 | 158 | 194 | 180 | 80 | |

(Las celdas vacías de tiempo extra están en blanco en la diapositiva; equivalen a 0.) Comprobación: consumo 3 = 2 + 160 + 32 = 194; consumo 4 = 8 + 160 + 12 = 180; inventario final = 52 + 28 = 80. Costo regular = $64(10)+52(26)+158(10)+2(14)+160(10)+160(10)=6800$; costo extra = $32(15)+8(19)+12(15)+28(19)=1344$; total \$8144.

### Página 66 — Example: Solución (Usando PL)

5. Consolidar plan de producción

| Periodo de Producción | Horas Regulares | Horas Extras | Horas totales |
|---|---|---|---|
| 1 | 116 | 0 | 116 |
| 2 | 160 | 0 | 160 |
| 3 | 160 | 40 | 200 |
| 4 | 160 | 40 | 200 |

### Página 67 — Example: Solución (Usando PL)

6. Calculo del costo mínimo: Multiplicación de matriz de costos y de solución

$$\sum_{i=1}^{m}\sum_{j=1}^{T}\sum_{k=1}^{T} C_{ijk}P_{ijk} = \$8144$$

### Página 68 — Example: Método de desagregación

7. Calcular el programa maestro (*master schedule*) si la demanda de cada referencia es estable.

- Se buscará minimizar los costos de set-up
- Producir A hasta que se acaba el inventario de B, luego cambiar la producción
- *¡Es fácil para dos referencias!*

| Producto | Mes 1 | Mes 2 | Mes 3 | Mes 4 |
|---|---|---|---|---|
| A | 116 | 55 | 98 | 136 |
| B | 0 | 262 | 255 | 160 |

(Verificación propia: horas = A + 0,4B → mes 1: 116; mes 2: $55+104{,}8=159{,}8\approx160$; mes 3: $98+102=200$; mes 4: $136+64=200$, que coincide con el plan consolidado de la página 66. Inventarios al cierre: A = 52, 17, 5, 41; B = 20, 92, 137, 97. Inventario final en horas $= 41 + 0{,}4\times97 = 79{,}8 \approx 80$.)

### Página 69 — Aggregated Planning in Services

- Controlar los costos de mano de obra es critico.
- Requerimientos:
  - Programar las horas de trabajo
  - Modalidad "on-call"
  - Relocalización de personal capacitado
  - Flexibilidad para cambiar las velocidades de trabajo para satisfacer la demanda

> [Imagen decorativa: foto de una oficina abierta con puestos de trabajo y foto de cuatro profesionales de la salud con bata.]

### Página 70 — Examples

- Restaurant: forecast for periods of time in an interval of 10 minutes
- Hospitals: Floating Nurses Between Units
- Airlines: Subcontracting services in cases of lack of personnel

> [Imagen decorativa: fachada de un restaurante con letrero «RESTAURANT», un edificio de hospital con una cruz roja y un avión de pasajeros en vuelo.]

### Página 71 — Revenue Management

- Changing product prices is possible
- Capacity = Demand = *F*(*price*)

*Revenue Management is an aggregated planning process of allocating company resources to customers at prices that maximize profit.*

### Página 72 — Revenue Management Examples

- Tiquetes aéreos
- Reservas de hoteles y vehículos
- UBER

> [Gráfico: curva de demanda lineal decreciente (línea roja). Eje Y «Cantidad demandada», eje X «Precio». Rótulo «Ejemplo SIN *RM*». Un único precio $P^*$ con cantidad $Q^*$; el rectángulo azul bajo la curva entre 0 y $P^*$ (altura $Q^*$) se rotula «Ventas» (ingreso = $P^* \times Q^*$).]

### Página 73 — Revenue Management Examples

- Tiquetes aéreos
- Reservas de hoteles y vehículos
- UBER

> [Gráfico: la misma curva de demanda, rótulo «Ejemplo CON *RM*». Ahora hay dos precios, $P_1^*$ y $P_2^* > P_1^*$. Un rectángulo «Ventas1» de altura $Q^*$ hasta $P_1^*$ y un segundo rectángulo «Ventas 2», más bajo, entre $P_1^*$ y $P_2^*$. Idea: con precios diferenciados se captura más área bajo la curva de demanda (más ingreso) que con un solo precio.]

### Página 74 — Pay attention !

- RM requires:
  - Differentiated pricing structures - fair to the customer
  - Demand curve forecasts
  - Attention to changes in demand: Offering different prices changes consumer behavior.

## Anexo: texto extraído automáticamente del PDF

> Texto plano tal como sale del PDF, sin fórmulas ni tablas que estén como imagen. La versión fiel y completa es la sección «Contenido completo» de arriba.

### Página 1 · 2 imagen(es)

Operations Management
Second term

### Página 2 · 1 imagen(es)

Outline
• Introduction to "Aggregate Planning"
• Aggregation Exercises
• Simple Aggregate Planning Models

### Página 3 · 6 imagen(es)

What is Aggregate
Planning?
• Demand is measured in units of 
products.
• Planning of operations is measured 
in hours worked, resources 
consumed. 
Sales 
forecast
[units]
Levels of 
production
[hours]
Service level
[%]

### Página 4 · 1 imagen(es)

What is aggregated 
planning made for?
• Mitigate the effects of fluctuations in 
demand.
– Which are … ?

### Página 5 · 2 imagen(es)

Success factors for having a 
production system of Goods/services 
with high utilization
• Effective Aggregate Planning (OM1)
• Efficient production scheduling (OM2)
• Effective maintenance
• Efficient programming of personnel and 
resources (OM2)
Why have high utilization of the production 
system?

### Página 6 · 3 imagen(es)

A Real Case: Frito-Lay
• More than three dozen brands
• 15 of them sell more than $100 million a 
year. 
• 7 of them sell more than $1 billion a year.

### Página 7 · 1 imagen(es)

How are these references 
produced?
• Specialized processes with high 
fixed costs. 
– Production of large batches.
• Low variable costs:
– specialization of the team.
• Machinery downtime (idle time) 
generates very high costs!

### Página 8 · 1 imagen(es)

Supply Chain
Raw Material 
• Harvest 
Seasons
• Other 
seasons
• Climate-
controlled 
storage 
required
Production
• Different 
plants in 
different 
locations
• Different 
production 
capacity
• Produce 
well and 
fast.
Planning 
Process
• Sales 
history
• Forecast of 
new 
products
• Innovations
• Promotions

### Página 9 · 1 imagen(es)

Aggregated Planning Goal
Demand
Production 
Capacity

### Página 10 · 1 imagen(es)

What are we going to do?
• Generate aggregate production 
plans for many plants
• In practice:
– Large companies modify their plans 
every quarter.
– What does it mean to change the plan?

### Página 11 · 1 imagen(es)

Aggregate Planning
Quarterly Plan
Monthly plan
Production 
Planning per 
assembly 
line
Allocation of raw 
materials and 
workers on a 
weekly basis to 
a production line

### Página 12 · 1 imagen(es)

Competitive Advantage
• Increase market share!
– Have the product available when the 
customer wants it
– Where the customer wants it
– As the customer wants it
• Aggregate planning requirements

### Página 13 · 1 imagen(es)

Planning Process
•
Long, medium and short term forecasts.
Planeación a largo plazo ( > 1 
año) 
•Decisiones de capacidad y localización
•R+D+i
•Inversiones
Planeación a mediano plazo (3-
18meses)
•Planeación agregada
•S&Op
•Contratación, inventario, tercerización
•Planes operativos
Planeación a corto plazo (< 3 
meses)
•Programación de producción
•Ordenes
•Trabajo en horas extra
Altos ejecutivos
Gerentes de 
operaciones con 
equipo de S&Op
Gerentes de operaciones 
con equipo de 
supervisores y operarios

### Página 14 · 1 imagen(es)

S&Op Planning
• Planeación intermedia:
– Planes operativos que coordinan los 
pronósticos de demanda con las áreas 
funcionales de la firma
• Función: recoger información del 
entorno y contexto para tomar decisiones.

### Página 15 · 1 imagen(es)

S &Op Inputs
Equipo de 
S&Op realiza 
el plan 
agregado de 
operaciones
Diseño de producto y 
proceso de 
planeación de 
capacidad
Inventario 
y Nivel de 
fuerza de 
trabajo
Pronóstico 
de ventas
Soporte 
de la 
SC
Capacidad 
Externa

### Página 16 · 1 imagen(es)

Capacity Planning
• Capacidad diseñada: La máxima 
producción teórica bajo condiciones 
ideales.
• Capacidad efectiva: La producción 
esperada considerando restricciones 
operativas.
• Capacidad real: La producción real 
considerando todas las limitaciones 
y tiempos improductivos (ver tiempo 
estándar).

### Página 17 · 1 imagen(es)

S&Op Outputs
Plan agregado
• Cantidad a producir 
• Tiempos de 
producción
• Actualizado semanal 
o mensualmente
• Familias de 
productos
MRP
• Requerimientos 
de Materia 
prima
Plan detallado de 
trabajo
• Scheduling
• Asignación de 
cargas de 
trabajo

### Página 18 · 1 imagen(es)

Foco del trabajo de S&Op 
Team
Foco en Producción
Foco en Supply Chain e 
inventarios
Foco en inversiones de 
capacidad
Planeación 
estratégica 
integrada 
con todas 
las áreas 
de la firma

### Página 19 · 2 imagen(es)

_(sin texto: página solo con imágenes)_

### Página 20 · 1 imagen(es)

Características de un proceso 
exitoso de planeación de S&Op
• Representativo
• Oportuno
• Exhaustivo
• Tiene una unidad de medida lógica
– Kg, unidades, bytes,
• Pronostica la demanda en un tiempo intermedio 
razonable en unidades agregadas
• Un método para determinar los costos relevantes
• Un modelo para las decisiones de programación 
de producción

### Página 21 · 1 imagen(es)

¿Qué decisiones toma un 
plan agregado?
• Tasas de producción
• Niveles de trabajo
• Niveles de inventario
• Horas extra
• Tasas de subcontratación
• Otras variables controlables…
Para hospitales, empresas, colegios, 
universidades, etc…

### Página 22 · 1 imagen(es)

Estructura habitual
• F. O : Minimizar el costo total
• Restricciones
– Satisfacer la demanda
– Conservación de la materia
– Restricciones de la Cadena de Abastecimiento
– Restricciones presupuestales y recursos
Otras estrategias:
•
Disminuir el nivel de trabajo
•
Disminuir el inventario
•
Alto nivel de servicio

### Página 23 · 1 imagen(es)

Soluciones posibles:
Mitigar la fluctuación de la demanda
• Manejar altos niveles de inventario
• Variaciones dinámicas de la fuerza 
de trabajo
• Horas extras o tiempos muertos
• Subcontratar
• Cambiar los precios

### Página 24 · 1 imagen(es)

Opciones de Capacidad
• Cambiar los niveles de inventarios:
– Aprovisionarse para periodos altos de 
demanda
– Costos de almacenamiento, seguros, 
manejo de producto, obsolescencia, 
costo de capital, etc.
– Se evita el desabastecimiento

### Página 25 · 1 imagen(es)

Opciones de capacidad
• Variar la fuerza de trabajo
– Contratar o despedir personal
– Costos de entrenamiento, contratación
– Costos de indemnización, y bajar la moral del 
equipo.
• Cambiar las horas de trabajo
– Costo extra de horas adicionales
– Fatiga del personal. 
– Hay un límite en las horas extra.
– Costo de mantener la fábrica abierta /cerrada

### Página 26 · 1 imagen(es)

Opciones de capacidad
• Subcontratar
– Es costoso (ATENCION si no lo es!)
– Es riesgoso 
– Es difícil hacer un contrato perfecto de 
subcontratación
• Usar empleados de tiempo parcial
– Como en los restaurantes, grandes 
superficies, supermercados, etc.

### Página 27 · 1 imagen(es)

Opciones de la Demanda
• Influenciar la demanda:
– Promociones y publicidad
• Back-ordering:
– A veces resulta en ventas perdidas
• Tener un portafolio de productos 
AMPLIO
– Producir y vender todo el año.
– Atención al foco del mercado.

### Página 28 · 2 imagen(es)

• Basado en la existencia de una
unidad agregada de producción.
• Artículos parecidos.
• Articulo “promedio”
• E.g.: Referencias que varían 
muy poco entre sí, por ejemplo, 
en su color.
Método de Agregación

### Página 29 · 2 imagen(es)

• Según Hax et Meal (1975), la forma de
agregar productos depende de:
– Afinidad de Artículos: un combo.
– Familias: Comparten un costo común.
– Tipos: procesos en común.
Principio de Jerarquía

### Página 30 · 1 imagen(es)

Ejemplo (Nahmias, 2007)
•
No es racional pensar en la producción de cada tipo de 
producto de forma independiente.
•
Es mejor pensar en un producto ficticio que tiene un precio de
venta ponderado y un requerimiento de horas-hombre
ponderado
Producto
Cantidad horas-
hombre
Precio de venta
1
4,2
$285
2
4,9
$345
3
5,1
$395
4
5,2
$425
5
5,4
$525
6
5,8
$725

### Página 31 · 1 imagen(es)

Ejemplo (Nahmias, 2007)
Modelo
Cantidad
horas-hombre
Precio de
venta
Demanda
%
1
4,2
$ 285
120
10,3%
2
4,9
$ 345
340
29,1%
3
5,1
$ 395
152
13,0%
4
5,2
$ 425
365
31,3%
5
5,4
$ 525
102
8,7%
6
5,8
$ 725
89
7,6%
Promedio
5,06
$415,02
TOTAL 
1168
Es decir, se requieren 5910 horas-hombre de trabajo

### Página 32 · 1 imagen(es)

Más ejercicios de 
Agregación
Una empresa que hace manufactura de productos de cuero tiene el siguiente pronóstico de demanda (en 
unidades) para cada producto de los próximos cuatro meses (ver tabla 1). Adicionalmente la tabla 2 presenta 
el precio promedio de venta (en dólares), el requerimiento de cuero en metros cuadrados por unidad de 
venta, y el número de horas-hombre requeridas para manufacturar una unidad de venta. Considerando 
estos datos, proponga un pronóstico AGREGADO de demanda para los meses enero-abril. 
Pronóstico de demanda [unid.] 
Mes 
Zapatos(par) 
Chaqueta 
Bolso 
Billetera 
Enero 
36 
30 
68 
38 
Febrero 
2 
61 
53 
52 
Marzo 
35 
78 
23 
79 
Abril 
59 
53 
77 
7 
Tabla 1: Pronóstico de demanda por referencia 
Producto 
Precio Prom. (USD) 
Requerimiento cuero (m2) 
Horas-hombre 
Zapatos(par) 
50 
2 
5 
Chaqueta 
110 
10 
4 
Bolso 
95 
12 
7 
Billetera 
30 
1 
5 
Tabla 2: Características de producción y ventas de cada referencia

### Página 33 · 1 imagen(es)

Más ejercicios de 
Agregación
Una empresa que hace manufactura de productos de acero tiene el siguiente pronóstico de demanda (en 
unidades) para cada producto de los próximos cuatro meses (ver tabla 1). Adicionalmente la tabla 2 presenta 
el precio promedio de venta (en dólares), el requerimiento de acero en KG por unidad de venta, y el número 
de horas-hombre requeridas para manufacturar una unidad de venta. Considerando estos datos, proponga 
un pronóstico AGREGADO de demanda para los meses enero-abril. 
Pronóstico de demanda [unid.] 
Mes 
Vigas 5 m 
Láminas (5mX5m) 
tornillos 
Alambre(10m) 
Enero 
36 
30 
68 
38 
Febrero 
2 
61 
53 
52 
Marzo 
35 
78 
23 
79 
Abril 
59 
53 
77 
7 
Tabla 1: Pronóstico de demanda por referencia 
Producto 
Precio Prom. (USD) 
Requerimiento acero (kg) 
Horas-hombre 
Vigas 5 m 
50 
2 
5 
Láminas (5mX5m) 
60 
20 
6 
tornillos 
0.1 
0.01 
0.01 
Alambre(10m) 
15 
4 
4 
Tabla 2: Características de producción y ventas de cada referencia

### Página 34 · 1 imagen(es)

Resumen
• Posibilidades para agregar productos:
– Requerimientos de materia prima más 
importante
– Requerimiento de horas-hombre
– Unidades comunes: Kg, l, ton, etc.
– Unidades (cuando tiene sentido)

### Página 35 · 1 imagen(es)

Modelos de Planeación 
Agregada

### Página 36 · 1 imagen(es)

Método gráfico (algoritmo)
1.
Determine la demanda de cada periodo
2.
Determine la capacidad en tiempo regular, 
horas extra, y subcontratación
3.
Encuentre costos de mano de obra, 
contratación y despido, y de mantener 
inventario
4.
Considere todas las restricciones de las 
políticas de los empleados
5.
Encuentre la demanda promedio y grafíquela 
como una constante.
6.
Analice y tome decisiones.

### Página 37 · 1 imagen(es)

Ejemplo
Mes
Demanda 
esperada
Días de 
producción
Demanda por 
día
Enero
900
22
41
Febrero
700
18
39
Marzo
800
21
38
Abril
1200
21
57
Mayo
1500
22
68
Junio
1100
20
55
Total
6200
124

### Página 38 · 1 imagen(es)

Estrategia: Producir el 
promedio diario
• Demanda promedio diaria:
–
𝑑𝑒𝑚𝑎𝑛𝑑𝑎 𝑡𝑜𝑡𝑎𝑙
𝑑í𝑎𝑠 𝑑𝑒 𝑝𝑟𝑜𝑑𝑢𝑐𝑐𝑖ó𝑛=
6200
124 = 50 𝑢𝑛𝑖/𝑑𝑖𝑎
• Estrategia: producir al día 50 
unidades

### Página 39 · 2 imagen(es)

Método gráfico:
0
10
20
30
40
50
60
70
80
Enero - 22 días
Febrero - 18 días
Marzo - 21 días
Abril - 21 días
Mayo - 22 días
Junio - 20 días
Unidades por día
Mes de planeación
Comportamiento diario de la demanda por mes
Demanda por día en
cada mes
Demanda Promedio

### Página 40 · 1 imagen(es)

Análisis
Mes
Demanda 
esperada
Días de 
producción
Demanda 
por día en 
cada mes
Producción 
mensual
Exceso 
/faltante
Enero - 
22 días
900
22
41
1100
200
Febrer
o - 18 
días
700
18
39
900
200
Marzo 
- 21 
días
800
21
38
1050
250
Abril - 
21 días 
1200
21
57
1050
-150
Mayo - 
22 días
1500
22
68
1100
-400
Junio - 
20 días
1100
20
55
1000
-100
Total
6200
124

### Página 41 · 2 imagen(es)

Método gráfico:
0
200
400
600
800
1000
1200
1400
1600
Enero - 22 días
Febrero - 18
días
Marzo - 21 días
Abril - 21 días
Mayo - 22 días
Junio - 20 días
Unidades por día
Mes de planeación
Comportamiento del plan de producción por mes
Demanda esperada
Producción mensual
Inventario Acumulado

### Página 42 · 1 imagen(es)

Problema de planeación 
agregada
• ¿Cómo produzco 50 unidades 
diarias durante 6 meses?
– Recursos (humanos, físicos, 
financieros y de información)
• Contrataciones, despidos
– Actividades a realizar:
• Crear nuevas líneas de ensamble
– Tercerización y gestión de proveedores

### Página 43 · 1 imagen(es)

Estrategias posibles
• Mantener una fuerza de trabajo 
constante:
– Para producir 50 /día
– Para producir 38 /día ( + tercerización)
• Tener una fuerza de trabajo 
dinámica.

### Página 44 · 1 imagen(es)

Costos hipotéticos
Costo de mantener inventario
$5 / unid –mes
subcontratar
$20 /unid
Salario
$80 /día (8 horas)
Hora extra
$17 /hora
Horas para producir una unidad
1.6 horas
Costo de aumentar la producción 
diaria
$300 /unid
Costo de disminuir la producción 
diaria
$600/día

### Página 45 · 1 imagen(es)

Análisis de inventario
Mes
Demanda 
esperada
Producción 
mensual
Exceso 
/faltante
Inventario 
Acumulado
Enero - 
22 días
900
1100
200
200
Febrero 
- 18 
días
700
900
200
400
Marzo - 
21 días
800
1050
250
650
Abril - 
21 días 
1200
1050
-150
500
Mayo - 
22 días
1500
1100
-400
100
Junio - 
20 días
1100
1000
-100
0
Inventario total = 1850 unidades

### Página 46 · 1 imagen(es)

Análisis de Costos
• FUERZA DE TRABAJO: 50 unidades por día (8 
horas)
– 50 X 1.6 = 80 horas de trabajo al día
– 8 horas / 1.6h/u = 5 unidades diarias por trabajador
– Se requieren 10 trabajadores.
– $99200 = 10 X $80 X 124 días
• Inventario
– $9250 = 1850uni X $5/uni
• Otros costos = 0
• TOTAL = $108 450 
– 91.5% son costos de mano de obra
– 8.5% son costos de inventario

### Página 47 · 2 imagen(es)

_(sin texto: página solo con imágenes)_

### Página 48 · 1 imagen(es)

Estrategia 2: subcontratar
• Producir lo mínimo pronosticado y 
subcontratar el resto.
– 38 unidades diarias
– 4712 unidades en 124 días
– Subcontratar 1488 unidades
• ¿Cuáles son los costos?
– Mano de obra (7.6 trabajadores) = $75 392
– Subcontratar = $29 760
– Inventario = $0
– TOTAL : $105 152
• 71,7% mano de obra
• 28,3% subcontratar

### Página 49 · 1 imagen(es)

Estrategia 3: Contratar y 
despedir
• Producción = Demanda
MES
Producción 
diaria
Costo de Fuerza 
de trabajo
Costo de 
contratar
Costo de 
despedir
Costo 
total
Enero
41
$14 400
$0
$0
$14 400
Febrero
39
$11 200
$0
$1200 (2X600)
$12 400 
Marzo
38
$12 800
$0
$600
$13 400
Abril
57
$19 200
$5700 (19X300)
$0
$24 900
Mayo
68
$24 000
$3300 (11X300)
$0
$27 300
Junio
55
$17 600
$0 $7800 (13x600)
$25 400
TOTAL
$99 200
$9 000
$9600
$117 800

### Página 50 · 1 imagen(es)

Analytic Models
• Bowman's simple net model (1956) - based on the 
transport problem
ASSUMPTIONS:
• m production sources.
• T planning periods.
• minimize the cost of production Z
– Production cost
– Storage cost
• No backlogging nor workforce level decisions.

### Página 51 · 1 imagen(es)

Analytic Models
• Modelo de red simple de Bowman (1956) - 
basado en el problema de transporte
NOTACIÓN (PARAMETROS):
• 𝐶𝑖𝑗𝑘= Costo marginal de producción de una 
unidad en la fuente i, en el periodo j y almacenado 
hasta el periodo k
• 𝐵𝑖𝑗 = Capacidad de producción en la fuente i en el 
periodo j
• 𝐷𝑘= Demanda pronosticada en el periodo k

### Página 52 · 1 imagen(es)

Analytic Models
MAS NOTACIÓN (PARAMETROS):
• 𝐶𝑅= Costo de producir una unidad en tiempo 
regular
• 𝐶𝑂= Costo de producir una unidad en tiempo 
extra
• 𝐶𝐼= Costo de almacenar una unidad en inventario
VARIABLES DE DECISIÓN:
𝑃𝑖𝑗𝑘= Número de unidades producidas en la fuente 
i, en el periodo j, para satisfacer la demanda del 
periodo k

### Página 53 · 1 imagen(es)

Analytic Models
• 𝑃𝑖𝑗𝑘 es entera o continua depende del contexto.
– Continua: Fácil de resolver (Programación lineal)
– Entera: “Difícil” de resolver (Programación entera)
Plan de Producción 
de la fuente i
Periodo de consumo
Producción 
TOTAL
Enero
Febrero
Marzo
Abril 
Mayo
Periodo de 
Producción
Enero
Febrero
X
Marzo
X
X
Abril 
X
X
X
Mayo
X
X
X
X
DEMANDA TOTAL

### Página 54 · 5 imagen(es)

Bowman Model
Minimizar Z = 
෍
𝑖=1
𝑚
෍
𝑗=1
𝑇
෍
𝑘=1
𝑇
𝐶𝑖𝑗𝑘𝑃𝑖𝑗𝑘
Sujeto a:
෍
𝑘=𝑗
𝑇
𝑃𝑖𝑗𝑘≤𝐵𝑖𝑗, ∀𝑖= 1,2 … 𝑚; 𝑗= 𝑖, 2 … 𝑇
෍
𝑖=1
𝑚
෍
𝑗=1
𝑘
𝑃𝑖𝑗𝑘= 𝐷𝑘, ∀𝑘= 𝑖, 2 … 𝑇
𝑃𝑖𝑗𝑘≥0
Restricción de 
capacidad de 
producción
Restricción de 
satisfacción de 
demanda

### Página 55 · 1 imagen(es)

Example
MES
Demanda producto A
Demanda producto B
1
100
200
2
90
190
3
110
210
4
100
200
•
Inventario inicial es 36 del producto A, 220 unidades del producto B
•
Hacer una unidad de producto 1 toma 1 hora.
•
Hacer una unidad de producto 2 toma 0.4 horas.
•
Costo de producción regular: $10/hora
•
Costo de producción extra: $15/hora
•
Costo de almacenamiento $4/mes (productos hechos en una hora)
•
Capacidad regular 160 horas/mes, extra = 40 horas /mes

### Página 56 · 1 imagen(es)

Example: 
Aggregating Products
1.
Calcular la demanda neta = demanda bruta – inventario inicial
2.
Encontrar unidades agregadas. Ejemplo: usar horas de trabajo
Demanda Agregada [h] = 1,0A + 0,4B
MES
Dem. 
Bruta 
Prod. A
Dem. 
Bruta 
Prod. B
Dem. Neta 
Prod. A
Dem. Neta 
Prod. B
Demanda 
AGREGADA
1
100
200
64
0
64
2
90
190
90
170
158
3
110
210
110
210
194
4
100
200
100
200
180

### Página 57 · 1 imagen(es)

Example: 
Cost Matrix
1.
Calcular el costo unitario de producción + almacenamiento 
para cada combinación de periodo de producción -consumo
Periodo de 
Producción
Periodo 
Consumo 1 
Periodo 
Consumo 2 
Periodo 
Consumo 3 
Periodo 
Consumo 4 
Inventario Final
1: Tiempo 
Regular
Tiempo extra
𝐶𝑅
𝐶𝑂
2: Tiempo 
Regular
Tiempo extra
-
3: Tiempo 
Regular
Tiempo extra
-
4: Tiempo 
Regular
Tiempo extra
-

### Página 58 · 1 imagen(es)

Example: 
Cost Matrix
1.
Calcular el costo unitario de producción + almacenamiento 
para cada combinación de periodo de producción -consumo
Periodo de 
Producción
Periodo 
Consumo 1 
Periodo 
Consumo 2 
Periodo 
Consumo 3 
Periodo 
Consumo 4 
Inventario Final
1: Tiempo 
Regular
Tiempo extra
𝐶𝑅
𝐶𝑂
𝐶𝑅+ 𝐶𝐼
𝐶𝑂+ 𝐶𝐼
2: Tiempo 
Regular
Tiempo extra
-
𝐶𝑅
𝐶𝑂
3: Tiempo 
Regular
Tiempo extra
-
-
4: Tiempo 
Regular
Tiempo extra
-
-

### Página 59 · 1 imagen(es)

Example: 
Cost Matrix
1.
Calcular el costo unitario de producción + almacenamiento 
para cada combinación de periodo de producción -consumo
Periodo de 
Producción
Periodo 
Consumo 1 
Periodo 
Consumo 2 
Periodo 
Consumo 3 
Periodo 
Consumo 4 
Inventario Final
1: Tiempo 
Regular
Tiempo extra
𝐶𝑅
𝐶𝑂
𝐶𝑅+ 𝐶𝐼
𝐶𝑂+ 𝐶𝐼
𝐶𝑅+ 2𝐶𝐼
𝐶𝑂+ 2𝐶𝐼
2: Tiempo 
Regular
Tiempo extra
-
𝐶𝑅
𝐶𝑂
𝐶𝑅+ 𝐶𝐼
𝐶𝑂+ 𝐶𝐼
3: Tiempo 
Regular
Tiempo extra
-
-
𝐶𝑅
𝐶𝑂
4: Tiempo 
Regular
Tiempo extra
-
-
-

### Página 60 · 1 imagen(es)

Example: 
Cost Matrix
1.
Calcular el costo unitario de producción + almacenamiento 
para cada combinación de periodo de producción -consumo
Periodo de 
Producción
Periodo 
Consumo 1 
Periodo 
Consumo 2 
Periodo 
Consumo 3 
Periodo 
Consumo 4 
Inventario Final
1: Tiempo 
Regular
Tiempo extra
𝐶𝑅
𝐶𝑂
𝐶𝑅+ 𝐶𝐼
𝐶𝑂+ 𝐶𝐼
𝐶𝑅+ 2𝐶𝐼
𝐶𝑂+ 2𝐶𝐼
𝐶𝑅+ 3𝐶𝐼
𝐶𝑂+ 3𝐶𝐼
𝐶𝑅+ 4𝐶𝐼
𝐶𝑂+ 4𝐶𝐼
2: Tiempo 
Regular
Tiempo extra
-
𝐶𝑅
𝐶𝑂
𝐶𝑅+ 𝐶𝐼
𝐶𝑂+ 𝐶𝐼
𝐶𝑅+ 2𝐶𝐼
𝐶𝑂+ 2𝐶𝐼
𝐶𝑅+ 3𝐶𝐼
𝐶𝑂+ 3𝐶𝐼
3: Tiempo 
Regular
Tiempo extra
-
-
𝐶𝑅
𝐶𝑂
𝐶𝑅+ 𝐶𝐼
𝐶𝑂+ 𝐶𝐼
𝐶𝑅+ 2𝐶𝐼
𝐶𝑂+ 2𝐶𝐼
4: Tiempo 
Regular
Tiempo extra
-
-
-
𝐶𝑅
𝐶𝑂
𝐶𝑅+ 𝐶𝐼
𝐶𝑂+ 𝐶𝐼

### Página 61 · 1 imagen(es)

Example: 
Cost Matrix
1.
Calcular el costo unitario de producción + almacenamiento 
para cada combinación de periodo de producción -consumo
Periodo de 
Producción
Periodo 
Consumo 1 
Periodo 
Consumo 2 
Periodo 
Consumo 3 
Periodo 
Consumo 4 
Inventario Final
1: Tiempo 
Regular
Tiempo extra
𝐶𝑅 = $10
𝐶𝑂= $15 
𝐶𝑅+ 𝐶𝐼 = 
$14
𝐶𝑂+ 𝐶𝐼
= $19
𝐶𝑅+ 2𝐶𝐼
= $18
𝐶𝑂+ 2𝐶𝐼
= $23
𝐶𝑅+ 3𝐶𝐼
= $22
𝐶𝑂+ 3𝐶𝐼
= $27
𝐶𝑅+ 4𝐶𝐼
= $26
𝐶𝑂+ 4𝐶𝐼
= $31
2: Tiempo 
Regular
Tiempo extra
-
𝐶𝑅 = $10
𝐶𝑂= $15 
𝐶𝑅+ 𝐶𝐼 = 
$14
𝐶𝑂+ 𝐶𝐼
= $19
𝐶𝑅+ 2𝐶𝐼
= $18
𝐶𝑂+ 2𝐶𝐼
= $23
𝐶𝑅+ 3𝐶𝐼
= $22
𝐶𝑂+ 3𝐶𝐼
= $27
3: Tiempo 
Regular
Tiempo extra
-
-
𝐶𝑅 = $10
𝐶𝑂= $15 
𝐶𝑅+ 𝐶𝐼 = 
$14
𝐶𝑂+ 𝐶𝐼
= $19
𝐶𝑅+ 2𝐶𝐼
= $18
𝐶𝑂+ 2𝐶𝐼
= $23
4: Tiempo 
Regular
Tiempo extra
-
-
-
𝐶𝑅 = $10
𝐶𝑂= $15 
𝐶𝑅+ 𝐶𝐼 = 
$14
𝐶𝑂+ 𝐶𝐼
= $19

### Página 62 · 1 imagen(es)

Example: 
Cost Matrix
3.
Calcular el costo unitario de producción + almacenamiento 
para cada combinación de periodo de producción -consumo
Periodo de 
Producción
Periodo 
Consumo 1 
Periodo 
Consumo 2 
Periodo 
Consumo 3 
Periodo 
Consumo 4 
Inventario Final
Capacidad
1: Tiempo 
Regular
Tiempo extra
𝐶𝑅
𝐶𝑂
𝐶𝑅+ 𝐶𝐼
𝐶𝑂+ 𝐶𝐼
𝐶𝑅+ 2𝐶𝐼
𝐶𝑂+ 2𝐶𝐼
𝐶𝑅+ 3𝐶𝐼
𝐶𝑂+ 3𝐶𝐼
𝐶𝑅+ 4𝐶𝐼
𝐶𝑂+ 4𝐶𝐼
160
40
2: Tiempo 
Regular
Tiempo extra
-
𝐶𝑅
𝐶𝑂
𝐶𝑅+ 𝐶𝐼
𝐶𝑂+ 𝐶𝐼
𝐶𝑅+ 2𝐶𝐼
𝐶𝑂+ 2𝐶𝐼
𝐶𝑅+ 3𝐶𝐼
𝐶𝑂+ 3𝐶𝐼
160
40
3: Tiempo 
Regular
Tiempo extra
-
-
𝐶𝑅
𝐶𝑂
𝐶𝑅+ 𝐶𝐼
𝐶𝑂+ 𝐶𝐼
𝐶𝑅+ 2𝐶𝐼
𝐶𝑂+ 2𝐶𝐼
160
40
4: Tiempo 
Regular
Tiempo extra
-
-
-
𝐶𝑅
𝐶𝑂
𝐶𝑅+ 𝐶𝐼
𝐶𝑂+ 𝐶𝐼
160
40
Demanda
64
158
194
180
80

### Página 63 · 1 imagen(es)

Example: 
Solución (Usando PL)
4. Calcular la solución usando métodos de programación matemática
Periodo de 
Producción
Periodo 
Consumo 1 
Periodo 
Consumo 2 
Periodo 
Consumo 3 
Periodo 
Consumo 4 
Inventario Final
Capacidad
1: Tiempo 
Regular
Tiempo extra
64
0
160
40
2: Tiempo 
Regular
Tiempo extra
X
160
40
3: Tiempo 
Regular
Tiempo extra
X
X
160
40
4: Tiempo 
Regular
Tiempo extra
X
X
X
160
40
Demanda
64
158
194
180
80

### Página 64 · 1 imagen(es)

Example: 
Solución (Usando PL)
4. Calcular la solución usando métodos de programación matemática
Periodo de 
Producción
Periodo 
Consumo 1 
Periodo 
Consumo 2 
Periodo 
Consumo 3 
Periodo 
Consumo 4 
Inventario Final
Capacidad
1: Tiempo 
Regular
Tiempo extra
64
0
0
160
40
2: Tiempo 
Regular
Tiempo extra
X
158
0
160
40
3: Tiempo 
Regular
Tiempo extra
X
X
160
40
4: Tiempo 
Regular
Tiempo extra
X
X
X
160
40
Demanda
64
158
194
180
80

### Página 65 · 1 imagen(es)

Example: 
Solución (Usando PL)
4. Calcular la solución usando métodos de programación matemática
Periodo de 
Producción
Periodo 
Consumo 1 
Periodo 
Consumo 2 
Periodo 
Consumo 3 
Periodo 
Consumo 4 
Inventario Final
Capacidad
1: Tiempo 
Regular
Tiempo extra
64
0
0
0
0
52
0
160
40
2: Tiempo 
Regular
Tiempo extra
X
158
0
2
0
0
0
160
40
3: Tiempo 
Regular
Tiempo extra
X
X
160
32
0
8
0
160
40
4: Tiempo 
Regular
Tiempo extra
X
X
X
160
12
0
28
160
40
Demanda
64
158
194
180
80

### Página 66 · 1 imagen(es)

5. Consolidar plan de producción 
Example: 
Solución (Usando PL)
Periodo de 
Producción
Horas 
Regulares
Horas 
Extras
Horas 
totales
1
116
0
116
2
160
0
160
3
160
40
200
4
160
40
200

### Página 67 · 1 imagen(es)

6. Calculo del costo mínimo: Multiplicación de matriz de 
costos y de solución 
෍
𝑖=1
𝑚
෍
𝑗=1
𝑇
෍
𝑘=1
𝑇
𝐶𝑖𝑗𝑘𝑃𝑖𝑗𝑘= $8144
Example: 
Solución (Usando PL)

### Página 68 · 1 imagen(es)

7. Calcular el programa maestro (master schedule) si la 
demanda de cada referencia es estable. 
•
Se buscará minimizar los costos de set-up
•
Producir A hasta que se acaba el inventario de B, luego 
cambiar la producción
•
¡Es fácil para dos referencias!
Example: 
Método de desagregación
Producto
Mes 1
Mes 2
Mes 3
Mes 4
A
116
55
98
136
B
0
262
255
160

### Página 69 · 3 imagen(es)

Aggregated Planning in 
Services
• Controlar los costos de mano de 
obra es critico.
• Requerimientos:
– Programar las horas de trabajo
– Modalidad “on-call”
– Relocalización de personal capacitado
– Flexibilidad para cambiar las 
velocidades de trabajo para satisfacer 
la demanda

### Página 70 · 4 imagen(es)

Examples
• Restaurant: forecast for 
periods of time in an 
interval of 10 minutes
• Hospitals: Floating 
Nurses Between Units
• Airlines: Subcontracting 
services in cases of lack 
of personnel

### Página 71 · 1 imagen(es)

Revenue Management
• Changing product prices is possible
• Capacity = Demand = F(price)
Revenue Management is an aggregated 
planning process of allocating company 
resources to customers at prices that 
maximize profit.

### Página 72 · 1 imagen(es)

Revenue Management 
Examples
• Tiquetes aéreos
• Reservas de hoteles y vehículos
• UBER
Precio 
Cantidad 
demandada 
Ventas
P*
Q*
Ejemplo SIN RM

### Página 73 · 1 imagen(es)

Revenue Management 
Examples
• Tiquetes aéreos
• Reservas de hoteles y vehículos
• UBER
Precio 
Cantidad 
demandada 
Ventas1
P1*
Q*
Ejemplo CON RM
Ventas 2
P2*

### Página 74 · 1 imagen(es)

Pay attention !
• RM requires:
– Differentiated pricing structures - fair to 
the customer
– Demand curve forecasts
– Attention to changes in demand: 
Offering different prices changes 
consumer behavior.

