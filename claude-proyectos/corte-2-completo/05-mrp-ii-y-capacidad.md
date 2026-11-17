<!-- fuente: corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/README.md -->
# MRP II y planeación de capacidad (Corte 2)

## Qué cubre

Cómo pasar del plan de materiales (MRP I) a la verificación de capacidad del MRP II:

- planeación de capacidad global (RCCP) y planeación de requerimientos de capacidad (CRP);
- traducción de las órdenes planeadas en horas por centro de trabajo y por semana;
- backward y forward scheduling con tiempos de alistamiento y de movimiento;
- reportes de carga y qué hacer cuando el plan es infactible;
- MRP de ciclo cerrado.

Es el puente entre el MRP del Corte 2 y la programación de operaciones (*scheduling*) del Corte 3.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [`L15-mrp-ii.md`](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md) (gemelo de `L15-mrp-ii.pdf`) | Presentación de clase, 46 páginas: MRP vs. MRP II, RCCP, CRP, control de piso, ciclo cerrado, ejemplo de traducción en capacidad (A-F), backward/forward scheduling y ejemplo CRP con lotes γ y β | Sí |
| [`backward-scheduling.md`](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/backward-scheduling.md) (gemelo de `backward-scheduling.xlsx`) | Excel que rehace las tablas CRP de backward scheduling de la L15 (pp. 35-42) para los lotes 300γ, 575γ y 2000β, en minutos por semana. Estaba en la carpeta del Corte 3, pero es de este tema. Tiene errores en el lote 575γ (semana 1) y en el lote 2000β | Después de L15 |

## Orden de estudio sugerido

1. L15, pp. 1-12: conceptos de MRP II, RCCP, CRP, control de piso, sistemas de información y ciclo cerrado.
2. L15, pp. 13-21: ejemplo de traducción en capacidad. Rehaga a mano los registros MRP de A a F y sume por centro.
3. L15, pp. 22-29: qué hacer ante infactibilidad y reglas de backward/forward scheduling.
4. L15, pp. 30-43: ejemplo CRP γ/β (datos, Gantt, tablas por semana y gráfico de carga).
5. `backward-scheduling.md`: compare las celdas del Excel con las tablas de la p. 42 y ubique los errores señalados.
6. Ejercicio propuesto de la L15, p. 44: repetir con forward scheduling y doble turno en WC2.

## Conceptos y fórmulas clave

- **Requerimiento bruto de un componente** = suma de las liberaciones de órdenes planeadas (LOP) de sus padres por la cantidad por unidad:
  $$RB^{j}_t=\sum_{i\in\text{padres}(j)} q_{ij}\,LOP^{i}_t$$
  donde $q_{ij}$ = unidades de $j$ por unidad de $i$. La orden se libera $\tau$ (lead time) periodos antes del requerimiento.
- **Carga de capacidad** del centro $k$ en la semana $t$:
  $$H_{k,t}=\sum_{j}\sum_{o:\,m(j,o)=k} p_{j,o}\,LOP^{j}_{t-(o-1)}$$
  donde $p_{j,o}$ = horas/unidad de la operación $o$ del ítem $j$ y $m(j,o)$ = centro donde se hace. Detalle en [`L15-mrp-ii.md`](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md), pp. 15-21.
- **Tiempo de un lote en una estación** (L15, p. 34):
  $$T\,[\text{sem}]=\frac{S+Q\,p}{60\cdot 8\cdot 5}=\frac{S+Q\,p}{2400\ \text{min/sem}}$$
  donde $S$ = alistamiento por lote (min), $Q$ = tamaño del lote y $p$ = min/unidad. Un día de movimiento = 480 min.
- **Backward scheduling:** se programa desde la fecha de entrega hacia atrás; si la primera operación cae antes de hoy hay retraso. **Forward scheduling:** se programa desde hoy hacia adelante; si la última operación pasa la fecha de entrega hay retraso.
- **Disponible semanal:** $2400-\sum(\text{minutos de WC y de movimiento cargados})$. La carga en horas se compara con la capacidad normal (40 h) y máxima (80 h).
- **Ante infactibilidad:** horas extra, turnos adicionales, subcontratación, reasignación de trabajadores, revisar el MPS, anticipar producción y rebalancear cargas.
- **Límite del CRP:** no secuencia trabajos ni respeta precedencias en la misma máquina. Eso se resuelve con scheduling en el Corte 3.

## Ejercicios resueltos disponibles

| Ejercicio | Archivo | Resultado principal |
|---|---|---|
| Traducción en capacidad de A, B (POQ = 2), C ($\tau=2$, 2 operaciones), D, E, F | [`L15-mrp-ii.md`](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md), pp. 13-21 | WKC 100: 59.00 / 2.00 / 87.40 / 2.25 h (periodos 0-3); WKC 200: 62.00 / 54.60 / 83.80 / 70.70 / 4.50 h (periodos −2 a 2); WKC 300: 8.00 / 8.00 / 7.60 / 9.00 h (periodos −1 a 2) |
| Backward schedule por días (Gantt) de los lotes 300γ, 575γ y 2000β | [`L15-mrp-ii.md`](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md), p. 33 | 300γ y 2000β terminan en S2 día 5; 575γ en S3 día 5 |
| CRP backward en minutos por semana | [`L15-mrp-ii.md`](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md), pp. 35-42 | Disponible en S1: 600 (300γ), 250 (575γ), 170 (2000β) |
| Carga por estación | [`L15-mrp-ii.md`](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md), p. 43 | WC1 S1 = 47.75 h; WC2 S1 = 42.17 h, S2 = 83.42 h (> 80 h máx.), S3 = 12.33 h; WC4 S2 = 17.67 h, S3 = 19.67 h |
| Mismo CRP en Excel | [`backward-scheduling.md`](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/backward-scheduling.md) | 300γ correcto (S2: 1290/630/480/0; S1: 1020/300/480/600); 575γ correcto en S3-S2 y erróneo en S1 (1020/655/725 en vez de 1845/305/250); 2000β sin terminar |

## Relación con otros temas y proyectos

- MRP, BOM y registro de lotes (base de la traducción en capacidad): [`../04-bom-y-mrp/`](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/), en especial [`L14-mrp.md`](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md), que repite las diapositivas de MRP de ciclo cerrado, y [`mrp-esfero.md`](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero.md).
- Tamaños de lote (lote a lote, POQ, Wagner-Whitin, Silver-Meal): [`../03-wagner-whitin-y-silver-meal/`](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/).
- Planeación agregada y desagregación (capacidad a nivel alto y origen del MPS): [`../01-planeacion-agregada-modelo-bowman/`](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/) y [`../02-agregacion-y-desagregacion/`](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/).
- Evaluación del corte: [`../parcial-2/`](/corte-2-planeacion-agregada-mrp/parcial-2/).
- Proyecto del corte: [`../proyecto-thyms-gemelo-digital/`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/).
- Secuenciación con precedencias (lo que el CRP no resuelve): [`../../corte-3-programacion-scheduling/01-introduccion-scheduling/`](/corte-3-programacion-scheduling/01-introduccion-scheduling/), [`../../corte-3-programacion-scheduling/03-maquinas-paralelas/`](/corte-3-programacion-scheduling/03-maquinas-paralelas/) (forward scheduling con máquinas paralelas) y [`../../corte-3-programacion-scheduling/05-job-shop/`](/corte-3-programacion-scheduling/05-job-shop/).


---

<!-- fuente: corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md -->
# L15-mrp-ii

> **Archivo:** [`L15-mrp-ii.pdf`](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.pdf) · **Corte 2** · 46 páginas  
> **Nombre original:** `CORTE 2/Lec 15 - MRP II.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** MRP II: cómo pasar del plan de materiales (MRP I) a la verificación de capacidad (RCCP y CRP), con backward y forward scheduling y el MRP de ciclo cerrado.

**Ideas clave:**

- MRP II amplía el MRP con procesamiento de transacciones (compras, inventario, finanzas), **planeación de la capacidad global** (*rough-cut capacity planning*, RCCP), **planeación de requerimientos de capacidad** (CRP) y **control de piso** (pp. 2-5).
- RCCP es una verificación rápida de los recursos clave (horas de trabajo y de máquina, inventario, espacio) para detectar infactibilidad del plan. CRP, si el plan es factible, genera un **perfil de capacidad por recurso y por semana** (pp. 3-4, 11-12).
- El control de piso asigna trabajos a máquinas y trabajadores (tiempos muertos, tiempos de terminación, makespan) y se ajusta a diario (p. 5).
- Flujo de información: órdenes + pronóstico → agregación/desagregación → plan maestro (MPS); BOM (con cambios de ingeniería), MPS e inventario → MRP I (requerimientos brutos/netos) → MRP II (reportes de capacidad/carga, de programación y de órdenes de producción) (pp. 6-8).
- **MRP de ciclo cerrado:** cada módulo realimenta a los anteriores (p. ej., si se excede la capacidad o faltan materiales) (pp. 9-10).
- **Traducción en capacidad:** cada liberación de orden planeada (LOP) del MRP se multiplica por las horas/unidad de cada operación y se carga en el centro y la semana en que se ejecuta. Sumando por centro de trabajo se obtiene la carga semanal (pp. 13-21).
- Si la carga supera la capacidad: horas extra, subcontratar, revisar el MPS o rebalancear cargas. También se pueden añadir turnos o reasignar trabajadores. MRP II busca **reparar** planes infactibles (pp. 22-23).
- **Backward scheduling:** se programa desde la fecha de entrega hacia atrás; si la primera operación cae antes de hoy hay retraso. **Forward scheduling:** se programa desde hoy hacia adelante; si la última operación pasa la fecha de entrega hay retraso. Las máquinas paralelas pueden eliminar ese retraso. Siempre se incluyen alistamientos (*setup*) y movimientos (pp. 24-29).
- El ejemplo γ/β (pp. 30-43) muestra que el backward scheduling deja WC1 y WC2 por encima de 40 h/semana, y WC2 en la semana 2 (83.4 h) por encima incluso de la capacidad máxima de 80 h.
- Límite del CRP: no considera que dos trabajos no pueden hacerse a la vez en la misma máquina ni las precedencias; eso se resuelve con *scheduling* en el Corte 3 (p. 46).

**Fórmulas y métodos:**

- Requerimiento de un componente (registro MRP, pp. 15-20). Se escribe $RB$ = requerimiento bruto, $RP$ = recepción programada, $INV$ = inventario final, $LOP$ = liberación de orden planeada, $\tau$ = lead time y $q_{ij}$ = unidades de $j$ por unidad de su padre $i$:
  $$RB^{j}_t=\sum_{i\,\in\,\text{padres}(j)} q_{ij}\,LOP^{i}_t,\qquad LOP^{j}_{t-\tau_j}=\text{cantidad que debe llegar en } t$$
  Ejemplos: $RB^D=LOP^A+LOP^B$; $RB^E=2\,LOP^B$; $RB^F=2\,LOP^E$. B usa lote POQ = 2 (cada orden cubre 2 periodos); el resto, lote a lote.
- Carga de capacidad (formalización del ejemplo de las pp. 15-21). Se escribe $H_{k,t}$ = horas requeridas en el centro $k$ en la semana $t$, $p_{j,o}$ = horas/unidad de la operación $o$ del ítem $j$ y $m(j,o)$ = centro donde se hace:
  $$H_{k,t}=\sum_{j}\ \sum_{o:\,m(j,o)=k} p_{j,o}\;LOP^{j}_{t-(o-1)}$$
  Con una operación por semana de lead time, la operación 1 se carga en la semana de liberación y la operación 2 en la siguiente (caso C con $\tau=2$).
- Tiempo de producción de un lote en una estación (p. 34), con setup times = n.º de lotes × tiempo de setup por lote:
  $$T\,[\text{semanas}]=\frac{\text{setup times}+(\text{tamaño de lote})(\text{tiempo de máquina por unidad})}{60\,\tfrac{min}{h}\cdot 8\,\tfrac{h}{día}\cdot 5\,\tfrac{días}{sem}}=\frac{S+Q\,p}{2400\ \text{min/sem}}$$
  donde $S$ = alistamiento por lote (min), $Q$ = tamaño del lote y $p$ = min/unidad. Un día de movimiento = 480 min.
- Backward scheduling por semanas (pp. 35-42): se parte de la semana de entrega y se resta, hacia atrás, la última operación, el movimiento, la operación anterior, etc. Lo que no cabe en los 2400 min de una semana pasa a la semana anterior:
  $$\text{Disponible}_s=2400-\sum(\text{WC}+\text{movimiento cargados en } s)$$
- Carga en horas = minutos / 60, comparada con la capacidad normal (40 h) y máxima (80 h).

**Ejemplos resueltos:**

| Ejemplo | Páginas | Resultado |
|---|---|---|
| Traducción en capacidad del MRP de A, B, C, D, E, F en WKC 100/200/300 | 13-21 | Carga WKC 100: 59.00 / 2.00 / 87.40 / 2.25 h (periodos 0-3); WKC 200: 62.00 / 54.60 / 83.80 / 70.70 / 4.50 h (periodos −2 a 2); WKC 300: 8.00 / 8.00 / 7.60 / 9.00 h (periodos −1 a 2). Totales parciales: A 8.15 h, B 142.5 h, E 57 h, F 95 h |
| Backward schedule (Gantt por días) de los lotes 300γ, 575γ y 2000β | 33 | 300γ y 2000β terminan en S2 día 5; 575γ termina en S3 día 5 |
| CRP backward en minutos por semana | 35-42 | Disponible en la semana 1: 600 (300γ), 250 (575γ), 170 (2000β); semanas 2 y 3 al 100 % |
| Carga de estaciones | 43 | WC1 S1 47.75 h; WC2 S1 42.17 h, S2 83.42 h, S3 12.33 h; WC4 S2 17.67 h, S3 19.67 h; capacidad normal 40 h |
| Propuesto: repetir con forward scheduling y doble turno en WC2 | 44 | Sin solución en la presentación |

**Páginas clave:** MRP vs. MRP II (2); RCCP (3); CRP (4, 11-12); control de piso (5); sistemas de información (6-8); ciclo cerrado (9-10); ejemplo de traducción en capacidad (13-21); qué hacer ante infactibilidad (22-23); backward/forward scheduling (24-29); datos del ejemplo γ/β (30-32); Gantt backward (33); fórmula de tiempo (34); tablas CRP (35-42); gráfico de carga (43); ejercicio propuesto (44); alternativas y límites (45-46).

**Observaciones sobre el material:**

- La tabla de la p. 13 da 0.10 h/unidad para E y 0.06 h/unidad para F. La p. 14 muestra E = 0.20 y F = 0.25, y los cálculos de las pp. 19-21 usan E = 0.3 y F = 0.25. Los totales de la p. 21 son consistentes con 0.3 y 0.25.
- En la p. 14, el bloque de D bajo el producto A tiene intercambiadas las etiquetas Centro (0.10) y Tiempo (200).
- La p. 30 indica que el lote 575γ se libera en la semana 2, pero el backward schedule (pp. 33 y 39-42) lo empieza en la semana 1. Su tiempo total ($1845+480+2965+480+1180=6950$ min ≈ 2.9 semanas) no cabe en las semanas 2-3 (deducido de los datos).
- La p. 21 pregunta «Capacidad semanal?» sin dar el valor para WKC 100/200/300.
- Las pp. 9-10 (MRP de ciclo cerrado) están repetidas casi idénticas en L14 (pp. 15-16).

**Relación con otros archivos del repo:**

- [`backward-scheduling.md`](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/backward-scheduling.md): Excel que rehace en hoja de cálculo las tablas CRP de las pp. 35-42 (lotes 300γ, 575γ, 2000β).
- Registro MRP, LOP, lotes POQ y BOM: [`../04-bom-y-mrp/L14-mrp.md`](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md), [`../04-bom-y-mrp/L13-bom-intro-to-mrp.md`](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md) y [`../04-bom-y-mrp/mrp-esfero.md`](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero.md).
- Planeación agregada (nivel alto de la capacidad): [`../01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md`](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md).
- Secuenciación y precedencias que el CRP no resuelve (Corte 3): [`../../corte-3-programacion-scheduling/01-introduccion-scheduling/L16-intro-scheduling.md`](/corte-3-programacion-scheduling/01-introduccion-scheduling/L16-intro-scheduling.md), [`../../corte-3-programacion-scheduling/03-maquinas-paralelas/L18-parallel-machine-scheduling.md`](/corte-3-programacion-scheduling/03-maquinas-paralelas/L18-parallel-machine-scheduling.md) y [`../../corte-3-programacion-scheduling/05-job-shop/job-shop-y-flexible-job-shop.md`](/corte-3-programacion-scheduling/05-job-shop/job-shop-y-flexible-job-shop.md).

## Contenido completo (página por página)

### Página 1 — Portada

**Planeación, Programación y Control de las Operaciones**

> [Imagen decorativa: franja lateral con foto del campus y logo de la Universidad de La Sabana; logo de licencia Creative Commons BY-NC-SA abajo a la izquierda.]

(La franja lateral con la foto del campus y el logo de la universidad se repite en todas las diapositivas; no se vuelve a mencionar.)

### Página 2 — MRP versus MRP II

- Ventaja principal:
  - Software de procesamiento de transacciones
  - Compras, inventario, funciones financieras
- Planeación de la capacidad global (Rough-cut Capacity planning)
- Planeación de los requerimientos de capacidad
- Control de piso

### Página 3 — Planeación de la capacidad global (Rough-cut Capacity planning)

- Verificación rápida de recursos clave para implementar el plan de producción.
- Determina el impacto del plan de producción
  - Horas de trabajo
  - Horas de máquina
  - Niveles de inventario
  - Espacio de almacenamiento
  - Otros recursos
- Detecta infactibilidad

### Página 4 — Capacity Requirements Planning - CRP

- Si el plan de producción es factible.
- CRP genera perfiles de capacidad para cada recurso para cada semana

### Página 5 — Control de piso: *Shop floor control*

- Asignar los trabajos a las máquinas y trabajadores
  - Tiempos muertos
  - Tiempos esperados de terminación de labores
  - Makespan
- Se realiza diariamente para ajustar información.
- (viñeta vacía)

### Página 6 — Sistemas de información

> [Diagrama: flujo de información de la planeación.
> - Dos óvalos de entrada, **Ordenes** y **Pronóstico**, apuntan con flechas al rectángulo **Sistema de Agregación y Desagregación**.
> - **Sistema de Agregación y Desagregación** → **Plan maestro de producción** (archivo/almacén de datos).
> - El óvalo **Cambios de Ingeniería** apunta al archivo **BOM**.
> - Un tercer archivo, **Estado del Inventario**, aparece a la derecha, sin flechas.
> Los tres archivos (BOM, Plan maestro de producción, Estado del Inventario) se dibujan como almacenes de datos (rectángulos con bandas laterales).]

### Página 7 — Sistema de información MRP

> [Diagrama: los tres archivos **BOM**, **Plan maestro de producción** y **Estado del Inventario** envían flechas al módulo **MRP I**, que está dentro de un recuadro azul llamado **MRP**. **MRP I** produce el documento **Reporte de requerimientos bruto/ netos** y tiene una flecha hacia abajo al módulo **MRP II** (también dentro del recuadro MRP).]

### Página 8 — Sistema de información MRP

> [Diagrama: recuadro **MRP** con los módulos **MRP I** → **MRP II**. Salidas (documentos):
> - **MRP I** → **Reporte de requerimientos bruto/ netos**.
> - **MRP II** → **Reporte de capacidad / carga**.
> - **MRP II** → **Reporte de programación de producción**.
> - Del recuadro MRP (debajo de MRP II) → **Reporte de ordenes de producción**.]

### Página 9 — MRP de ciclo Cerrado

- Cada módulo realimenta los módulos anteriores para informar si hay ajustes por hacer.
  - Ejemplo: Se excede la capacidad de producción, faltantes de inventario.

### Página 10 — MRP de ciclo cerrado

> [Diagrama: cadena de seis flechas tipo chevrón, de izquierda a derecha: **Plan de Producción** → **Programa maestro de producción** → **Planeación de necesidades de material** → **Revisar factibilidad** → **Ejecución de planes de capacidad** → **Ejecución de planes de materiales**. Debajo, flechas curvas rojas de realimentación que vuelven a etapas anteriores:
> - Programa maestro de producción → Plan de Producción.
> - Planeación de necesidades de material → Programa maestro de producción.
> - Revisar factibilidad → Planeación de necesidades de material.
> - Revisar factibilidad → Programa maestro de producción.
> - Ejecución de planes de capacidad → Planeación de necesidades de material.
> - Ejecución de planes de materiales → Planeación de necesidades de material.]

### Página 11 — MRP II : CRP

- Capacity Requirements Planning
- Balancear la disponibilidad de maquinaria con un programa de producción que satisfaga las fechas de entrega de los trabajos.
- Capacidad fija en el corto plazo
- Evitar los tiempos muertos y sobreutilización de recursos escasos

### Página 12 — MRP II : CRP

- Traducción de los requerimientos de producción en la capacidad de los recursos necesarios
- En altos niveles está relacionado con la planeación agregada
- En niveles bajos está relacionada con la capacidad de la maquinaria de producción
- Responde a cuánta capacidad se requiere en un período dado para satisfacer la demanda

### Página 13 — Ejemplo: Plan con restricciones de capacidad

> [Diagrama: dos listas de materiales (BOM).
> - Producto **A** → componentes **C** y **D** (1 unidad de cada uno; no se indica cantidad).
> - Producto **B** → componentes **D** y **E(2)** (2 unidades de E por B).
> - **E** → **F(2)** (2 unidades de F por E).]

$\tau$ = 1 semana para cada **Operación** (palabra en rojo). Aquí $\tau$ es el tiempo de entrega (*lead time*) de cada operación.

| Producto | Operación | Máquina | Hrs/unidad |
|---|---|---|---|
| A | 1 | 100 | 0.05 |
| B | 1 | 100 | 1.50 |

| Componentes | Operación | Máquina | Hrs/unidad |
|---|---|---|---|
| C | 1 | 200 | 0.60 |
|  | 2 | 300 | 0.20 |
| D | 1 | 200 | 0.10 |
| E | 1 | 200 | 0.10 |
| F | 1 | 200 | 0.06 |

> Nota: las diapositivas 19 y 20 usan 0.3 h/unidad para E y 0.25 h/unidad para F, distintos de 0.10 y 0.06 de esta tabla (ver Observaciones en el resumen).

### Página 14 — Perfil de uso de los recursos

Perfil de cuándo y dónde se consume capacidad para entregar una unidad de A (izquierda) y de B (derecha) en la semana 3. Cada bloque indica ítem, centro de trabajo y horas por unidad.

**Producto A (semanas 1 a 3):**

| Semana | Ítem | Centro | Tiempo (h/unidad) |
|---|---|---|---|
| 1 | C | 200 | 0.60 |
| 2 | C | 300 | 0.20 |
| 2 | D | 200 | 0.10 |
| 3 | A | 100 | 0.05 |

En la diapositiva, el bloque de D (debajo de A) tiene las etiquetas intercambiadas: «Centro 0.10» y «Tiempo 200».

**Producto B (semanas 1 a 3):**

| Semana | Ítem | Centro | Tiempo (h/unidad) |
|---|---|---|---|
| 1 | F | 200 | 0.25 |
| 2 | E | 200 | 0.20 |
| 2 | D | 200 | 0.10 |
| 3 | B | 100 | 1.50 |

> [Diagrama: tabla de bloques de colores sobre un eje «Semana 1, 2, 3 | 1, 2, 3»: C en azul claro, D en azul, A en amarillo, B en naranja, F en rosa, E en verde.]

### Página 15 — Traducción en capacidad (A)

$\tau$ = 1. Tiempo de proceso: 0.05 hrs / unidad. WKC 100

Registro MRP de A (RB = requerimientos brutos, RP = recepciones programadas, INV = inventario disponible al final del periodo, LOP = liberación de órdenes planeadas):

| A | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| RB |  | 40 | 40 | 38 | 45 |
| RP |  | 0 |  |  |  |
| INV | 0 | 0 | 0 | 0 | 0 |
| LOP | 40 | 40 | 38 | 45 |  |

$\tau$ = 1

Horas-máquina ($\text{LOP}_t \times 0.05$):

| A | 0 | 1 | 2 | 3 | 4 | total hrs |
|---|---|---|---|---|---|---|
| 100 | 2.00 | 2.00 | 1.90 | 2.25 |  | 8.15 |
| 200 |  |  |  |  |  | 0.00 |
| 300 |  |  |  |  |  | 0.00 |
| **Total semana** | 2.00 | 2.00 | 1.90 | 2.25 | - |  |

Cálculo: $40\times0.05=2.00$; $40\times0.05=2.00$; $38\times0.05=1.90$; $45\times0.05=2.25$; total $8.15$ h.

### Página 16 — Traducción en capacidad (B)

$\tau$ = 1. Tiempo de proceso: 1.5 hrs / unidad. POQ= 2, WKC 100

(POQ = *periodic order quantity*: cada orden cubre los requerimientos de 2 periodos.)

| B |  | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| RB |  | 19 | 19 | 34 | 23 |
| RP |  | 0 |  |  |  |
| INV | 0 | 19 | 0 | 23 | 0 |
| LOP | 38 | 0 | 57 | 0 |  |

(La primera columna corresponde al periodo 0; en la diapositiva no tiene encabezado.)

Horas Máquina ($\text{LOP}_t \times 1.5$):

| B | 0 | 1 | 2 | 3 | 4 | total hrs |
|---|---|---|---|---|---|---|
| 100 | 57.0 |  | 85.5 |  |  | 142.5 |
| 200 |  |  |  |  |  | 0.00 |
| 300 |  |  |  |  |  | 0.00 |

Cálculo: orden en 0 por $19+19=38$ (llega en 1, sobran 19 para el periodo 2); orden en 2 por $34+23=57$ (llega en 3, sobran 23 para el periodo 4). Horas: $38\times1.5=57.0$; $57\times1.5=85.5$; total $142.5$ h.

### Página 17 — Traducción en capacidad (C)

$\tau$ = 2. Tiempo: 0.6 hrs / unidad en WKC 200 y 0.2 hrs / unidad en WKC 300

| C | -2 | -1 | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|---|
| RB |  |  | 40 | 40 | 38 | 45 |  |
| RP |  |  |  |  |  |  |  |
| INV |  | 0 | 0 | 0 | 0 | 0 |  |
| LOP | 40 | 40 | 38 | 45 |  |  |  |

$\tau$ = 2. Horas Máquina:

| C | -2 | -1 | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|---|
| 100 |  |  |  |  |  |  |  |
| 200 | 24 | 24 | 22.8 | 27 | 0 | 0 |  |
| 300 |  | 8 | 8 | 7.6 | 9 | 0 |  |

Cálculo: el RB de C es la LOP de A (40, 40, 38, 45 en los periodos 0 a 3). Con $\tau=2$ la orden se libera 2 semanas antes. La operación 1 (WKC 200) se carga en la semana de liberación: $40\times0.6=24$, $40\times0.6=24$, $38\times0.6=22.8$, $45\times0.6=27$. La operación 2 (WKC 300) se carga en la semana siguiente: $40\times0.2=8$, $40\times0.2=8$, $38\times0.2=7.6$, $45\times0.2=9$.

### Página 18 — Traducción en capacidad (D)

$\tau$ = 1. Tiempo de proceso: 0.1 hrs / unidad, WKC 200

Rótulo «A + B» sobre la columna 0: el RB de D es la suma de las LOP de A y de B.

| D | -2 | -1 | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|---|
| RB |  |  | 78 | 40 | 95 | 45 |  |
| RP |  |  |  |  |  |  |  |
| INV |  | 0 | 0 | 0 | 0 | 0 |  |
| LOP |  | 78 | 40 | 95 | 45 |  |  |

Horas máquina:

| D | -2 | -1 | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|---|
| 100 |  |  |  |  |  |  |  |
| 200 |  | 7.8 | 4 | 9.5 | 4.5 |  |  |
| 300 |  |  |  |  |  |  |  |

Cálculo: $RB_0=40+38=78$, $RB_1=40+0=40$, $RB_2=38+57=95$, $RB_3=45+0=45$. Horas: $78\times0.1=7.8$, $40\times0.1=4$, $95\times0.1=9.5$, $45\times0.1=4.5$.

### Página 19 — Traducción en capacidad (E)

$\tau$ = 1. Tiempo de proceso: 0.3 hrs / unidad, WKC 200

| E | -2 | -1 | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|---|
| RB |  |  | 76 | 0 | 114 | 0 |  |
| RP |  |  |  |  |  |  |  |
| INV |  | 0 | 0 | 0 | 0 | 0 |  |
| LOP |  | 76 | 0 | 114 | 0 |  |  |

Horas máquina:

| E | -2 | -1 | 0 | 1 | 2 | 3 | 4 | total hrs |
|---|---|---|---|---|---|---|---|---|
| 100 |  |  |  |  |  |  |  | 0.00 |
| 200 |  | 22.8 | 0 | 34.2 | 0 |  |  | 57.00 |
| 300 |  |  |  |  |  |  |  | 0.00 |

Cálculo: $RB^E_t = 2\times LOP^B_t$: $2\times38=76$ (periodo 0) y $2\times57=114$ (periodo 2). Horas: $76\times0.3=22.8$ y $114\times0.3=34.2$; total $57$ h.

### Página 20 — Traducción en capacidad (F)

$\tau$ = 1. Tiempo de proceso: 0.25 hrs / unidad, WKC 200

| F | -2 | -1 | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|---|
| RB |  | 152 | 0 | 228 | 0 |  |  |
| RP |  |  |  |  |  |  |  |
| INV |  | 0 | 0 | 0 | 0 | 0 |  |
| LOP | 152 | 0 | 228 | 0 | 0 |  |  |

Horas-Maq:

| F | -2 | -1 | 0 | 1 | 2 | 3 | 4 | total hrs |
|---|---|---|---|---|---|---|---|---|
| 100 |  |  |  |  |  |  |  | 0.00 |
| 200 | 38 | 0 | 57 | 0 |  |  |  | 95.00 |
| 300 |  |  |  |  |  |  |  | 0.00 |

Cálculo: $RB^F_t = 2\times LOP^E_t$: $2\times76=152$ (periodo −1) y $2\times114=228$ (periodo 1). Horas: $152\times0.25=38$ y $228\times0.25=57$; total $95$ h.

### Página 21 — Tiempo total por centro de trabajo

Horas por máquina:

| WKC | -2 | -1 | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|---|
| 100 | - | - | 59.00 | 2.00 | 87.40 | 2.25 | - |
| 200 | 62.00 | 54.60 | 83.80 | 70.70 | 4.50 | - | - |
| 300 | - | 8.00 | 8.00 | 7.60 | 9.00 | - | - |

**Capacidad semanal?** (pregunta en rojo; la diapositiva no da el valor).

Verificación (suma de las páginas 15 a 20):

- WKC 100: periodo 0: $2.00\,(A)+57.0\,(B)=59.00$; periodo 1: $2.00$; periodo 2: $1.90+85.5=87.40$; periodo 3: $2.25$.
- WKC 200: periodo −2: $24\,(C)+38\,(F)=62.00$; periodo −1: $24\,(C)+7.8\,(D)+22.8\,(E)+0\,(F)=54.60$; periodo 0: $22.8+4+0+57=83.80$; periodo 1: $27+9.5+34.2+0=70.70$; periodo 2: $0+4.5+0=4.50$.
- WKC 300 (solo C, operación 2): $8,\ 8,\ 7.6,\ 9$.

### Página 22 — ¿Qué hacer si el reporte de capacidad muestra infactibilidad?

- Programar horas extra
- Subcontratar
- Revisar el plan maestro de producción
- Tratar de rebalancear las cargas

### Página 23 — CRP

- Recursos disponibles: Horas extra, turnos adicionales, subcontratación, reasignación de trabajadores.
- MRP II: busca reparar planes de producción infactibles.
- Se debe calcular la cantidad total de trabajo y tiempo muerto para las ordenes de producción, usando reglas de programación sencillas.

### Página 24 — CRP

- Reglas comunes:
  - Forward scheduling: programar los trabajos desde la fecha de disponibilidad hacia adelante.
  - Backward scheduling: programar desde la fecha de entrega hacia atrás.
- Se deben incluir tiempos de alistamiento y de movimiento de los trabajos entre estaciones

### Página 25 — Backward scheduling

- Ejemplos

> [Diagrama: eje de tiempo que empieza en la «Fecha actual» y termina en la «Due date» (línea vertical). Las operaciones se colocan desde la fecha de entrega hacia atrás: **OP3** termina justo en la due date; antes de OP3 hay un hueco **Set up**; antes, **OP2**; antes, un hueco de **movimiento**; antes, **OP1**. Entre la fecha actual y el inicio de OP1 queda un espacio marcado **holgura**.]

Orden en el eje: Fecha actual → holgura → OP1 → movimiento → OP2 → Set up → OP3 → Due date. Conclusión: el trabajo cabe y sobra holgura al inicio.

### Página 26 — Backward scheduling

- Ejemplos

> [Diagrama: igual que el anterior pero con cuatro operaciones. Desde la due date hacia atrás: **OP4** (termina en la due date), **Set up**, **OP3**, **movimiento**, **OP2**, **OP1**. OP1 queda a la izquierda de la «Fecha actual», es decir, debería haber empezado en el pasado; la porción antes de la fecha actual se marca **retraso**.]

Conclusión: al programar hacia atrás, la primera operación cae antes de hoy; el plan es infactible tal como está y aparece un retraso.

### Página 27 — Forward scheduling

- Ejemplos

> [Diagrama: desde la «Fecha actual» hacia adelante: **OP1** empieza en la fecha actual, luego **movimiento**, **OP2**, **Set up**, **OP3**. OP3 termina antes de la «Due date»; el espacio entre el fin de OP3 y la due date se marca **holgura**.]

### Página 28 — Forward scheduling

- Ejemplos

> [Diagrama: desde la «Fecha actual»: **OP1**, **OP2**, **movimiento**, **OP3**, **Set up**, **OP4**. La due date cae en la mitad de OP4; la parte de OP4 después de la due date se marca **retraso**.]

### Página 29 — Forward scheduling: parallel machines

- Ejemplos

> [Diagrama: igual al de la página 28, pero **OP4** se divide en dos bloques apilados (dos máquinas en paralelo) que se procesan simultáneamente después del **Set up**. Así OP4 termina justo en la «Due date» y desaparece el retraso. Se marcan también el hueco de **movimiento** entre OP2 y OP3.]

### Página 30 — Generación de reportes de producción y capacidad

- Considere dos productos ($\gamma$ y $\beta$).

| SEMANA | γ Liberación | γ Entrega | B Liberación | B Entrega |
|---|---|---|---|---|
| 1 | 300 |  | 2000 |  |
| 2 | 575 |  |  |  |
| 3 |  | 300 |  | 2000 |
| 4 |  | 575 |  |  |

(El encabezado de la tabla escribe «B»; en el texto y en el resto del ejemplo es el producto $\beta$.)

### Página 31 — Información requerida

- PARTES: Indica el estado de las partes que componen los productos.
- WC: Work Center.

| Parte | Ruteo | SU-time (min) por lote | MACH-time (min) por unidad |
|---|---|---|---|
| γ | WC1 | 120 | 3 |
|  | WC2 | 90 | 5 |
|  | WC4 | 30 | 2 |
| α | WC3 | 120 | 3 |
|  | WC4 | 30 | 1 |
| β | WC2 | 120 | 1.8 |
|  | WC4 | 30 | 0.2 |

(SU-time = tiempo de alistamiento o *setup* por lote; MACH-time = tiempo de máquina por unidad. La parte α no tiene pedidos en la página 30.)

### Página 32 — Información requerida

- Estaciones de trabajo: (WC)
  - Capacidad dada en horas por semana.

| WC-id | Nombre | Capacidad normal | Capacidad máxima |
|---|---|---|---|
| WC1 | Torno | 40 | 80 |
| WC2 | Molino | 40 | 80 |
| WC3 | Fresa | 40 | 80 |
| WC4 | Inspección | 40 | 80 |

  - Asuma 1 día de movimiento entre operaciones.

### Página 33 — Backward Schedule

- Realizamos una gráfica para mostrar la ubicación de cada lote en la planta en el tiempo.

> [Diagrama: cuadrícula tipo Gantt vertical. Filas: Semana 1 a 4, cada una con Días 1 a 5. Columnas: «Lote de 300γ», «Lote de 575γ», «Lote de 2000β». Bloques: WC1 en amarillo, WC2 en azul, WC4 en salmón; las celdas en blanco entre bloques son días de movimiento.]

Transcripción como tabla (semana.día; los intervalos incluyen ambos días):

| Lote | Centro | Inicio | Fin |
|---|---|---|---|
| 300γ | WC1 | S1 día 2 | S1 día 3 |
| 300γ | (movimiento) | S1 día 4 | S1 día 4 |
| 300γ | WC2 | S1 día 5 | S2 día 2 |
| 300γ | (movimiento) | S2 día 3 | S2 día 3 |
| 300γ | WC4 | S2 día 4 | S2 día 5 |
| 575γ | WC1 | S1 día 2 | S1 día 5 |
| 575γ | (movimiento) | S2 día 1 | S2 día 1 |
| 575γ | WC2 | S2 día 2 | S3 día 2 |
| 575γ | (movimiento) | S3 día 3 | S3 día 3 |
| 575γ | WC4 | S3 día 4 | S3 día 5 |
| 2000β | WC2 | S1 día 2 | S2 día 3 |
| 2000β | (movimiento) | S2 día 4 | S2 día 4 |
| 2000β | WC4 | S2 día 5 | S2 día 5 |

Los lotes 300γ y 2000β terminan al final de la semana 2 (entrega en la semana 3) y el lote 575γ al final de la semana 3 (entrega en la semana 4). La semana 4 queda vacía.

### Página 34 — CRP

- Tiempo de producción en cada estación:

$$\text{Tiempo de producción [semanas]}=\frac{\text{setup times}+(\text{Tamaño lote})(\text{tiempo en máquina})}{\left(60\,\frac{min}{hr}\right)\ast\left(8\,\frac{hr}{dia}\right)\ast\left(5\,\frac{dia}{sem}\right)}$$

*Setup times = # de lotes X tiempo de setup por lote*

(El denominador vale $60\times8\times5=2400$ minutos por semana: la capacidad normal de 40 h/semana expresada en minutos. Un día de movimiento equivale a $8\times60=480$ minutos.)

### Página 35 — CRP

Tablas de carga en minutos por semana (backward scheduling). Se empieza por la semana de entrega del lote 575γ (semana 3), con 2400 min disponibles.

| Semana 3 | WC1 | WC2 | WC4 | Movimiento | Disponible |
|---|---|---|---|---|---|
| Lote de 300γ |  |  |  |  | 2400 |
| Lote de 575γ |  |  | 1180 | 480 | 740 |
| Lote de 2000β |  |  |  |  | 2400 |

| Semana 2 | WC1 | WC2 | WC4 | Movimiento |  |
|---|---|---|---|---|---|
| Lote de 300γ |  |  |  |  |  |
| Lote de 575γ |  |  |  |  |  |
| Lote de 2000β |  |  |  |  |  |

| Semana 1 | WC1 | WC2 | WC4 | Movimiento |  |
|---|---|---|---|---|---|
| Lote de 300γ |  |  |  |  |  |
| Lote de 575γ |  |  |  |  |  |
| Lote de 2000β |  |  |  |  |  |

Paso: WC4 del lote 575γ $=30+575\times2=1180$ min; movimiento WC2→WC4 $=480$ min; disponible $=2400-1180-480=740$ min.

### Página 36 — CRP

| Semana 3 | WC1 | WC2 | WC4 | Movimiento | Disponible |
|---|---|---|---|---|---|
| Lote de 300γ |  |  |  |  | 2400 |
| Lote de 575γ |  | 740 | 1180 | 480 | 0 |
| Lote de 2000β |  |  |  |  | 2400 |

| Semana 2 | WC1 | WC2 | WC4 | Movimiento |  |
|---|---|---|---|---|---|
| Lote de 300γ |  |  |  |  | 2400 |
| Lote de 575γ |  |  |  |  | 2400 |
| Lote de 2000β |  |  |  |  | 2400 |

| Semana 1 | WC1 | WC2 | WC4 | Movimiento |  |
|---|---|---|---|---|---|
| Lote de 300γ |  |  |  |  | 2400 |
| Lote de 575γ |  |  |  |  | 2400 |
| Lote de 2000β |  |  |  |  | 2400 |

Paso: los 740 min libres de la semana 3 se usan para el final de WC2 del lote 575γ; el disponible queda en 0.

### Página 37 — CRP

| Semana 3 | WC1 | WC2 | WC4 | Movimiento | Disponible |
|---|---|---|---|---|---|
| Lote de 300γ |  |  |  |  | 2400 |
| Lote de 575γ |  | 740 | 1180 | 480 | 0 |
| Lote de 2000β |  |  |  |  | 2400 |

| Semana 2 | WC1 | WC2 | WC4 | Movimiento |  |
|---|---|---|---|---|---|
| Lote de 300γ |  |  |  |  | 2400 |
| Lote de 575γ |  | 2225 |  |  | 175 |
| Lote de 2000β |  |  |  |  | 2400 |

| Semana 1 | WC1 | WC2 | WC4 | Movimiento |  |
|---|---|---|---|---|---|
| Lote de 300γ |  |  |  |  | 2400 |
| Lote de 575γ |  |  |  |  | 2400 |
| Lote de 2000β |  |  |  |  | 2400 |

Paso: WC2 total del lote 575γ $=90+575\times5=2965$ min. Ya se cargaron 740 en la semana 3, faltan $2965-740=2225$ en la semana 2; disponible $=2400-2225=175$.

### Página 38 — CRP

| Semana 3 | WC1 | WC2 | WC4 | Movimiento | Disponible |
|---|---|---|---|---|---|
| Lote de 300γ |  |  |  |  | 2400 |
| Lote de 575γ |  | 740 | 1180 | 480 | 0 |
| Lote de 2000β |  |  |  |  | 2400 |

| Semana 2 | WC1 | WC2 | WC4 | Movimiento |  |
|---|---|---|---|---|---|
| Lote de 300γ |  |  |  |  | 2400 |
| Lote de 575γ |  | 2225 |  | 175 | 0 |
| Lote de 2000β |  |  |  |  | 2400 |

| Semana 1 | WC1 | WC2 | WC4 | Movimiento |  |
|---|---|---|---|---|---|
| Lote de 300γ |  |  |  |  | 2400 |
| Lote de 575γ |  |  |  |  | 2400 |
| Lote de 2000β |  |  |  |  | 2400 |

Paso: los 175 min restantes de la semana 2 se usan como parte del movimiento WC1→WC2 (480 min).

### Página 39 — CRP

| Semana 3 | WC1 | WC2 | WC4 | Movimiento | Disponible |
|---|---|---|---|---|---|
| Lote de 300γ |  |  |  |  | 2400 |
| Lote de 575γ |  | 740 | 1180 | 480 | 0 |
| Lote de 2000β |  |  |  |  | 2400 |

| Semana 2 | WC1 | WC2 | WC4 | Movimiento |  |
|---|---|---|---|---|---|
| Lote de 300γ |  |  |  |  | 2400 |
| Lote de 575γ |  | 2225 |  | 175 | 0 |
| Lote de 2000β |  |  |  |  | 2400 |

| Semana 1 | WC1 | WC2 | WC4 | Movimiento |  |
|---|---|---|---|---|---|
| Lote de 300γ |  |  |  |  | 2400 |
| Lote de 575γ |  |  |  | 305 | 2095 |
| Lote de 2000β |  |  |  |  | 2400 |

Paso: el resto del movimiento, $480-175=305$ min, cae en la semana 1; disponible $=2400-305=2095$.

### Página 40 — CRP

| Semana 3 | WC1 | WC2 | WC4 | Movimiento | Disponible |
|---|---|---|---|---|---|
| Lote de 300γ |  |  |  |  | 2400 |
| Lote de 575γ |  | 740 | 1180 | 480 | 0 |
| Lote de 2000β |  |  |  |  | 2400 |

| Semana 2 | WC1 | WC2 | WC4 | Movimiento |  |
|---|---|---|---|---|---|
| Lote de 300γ |  |  |  |  | 2400 |
| Lote de 575γ |  | 2225 |  | 175 | 0 |
| Lote de 2000β |  |  |  |  | 2400 |

| Semana 1 | WC1 | WC2 | WC4 | Movimiento |  |
|---|---|---|---|---|---|
| Lote de 300γ |  |  |  |  | 2400 |
| Lote de 575γ | 1845 |  |  | 305 | 250 |
| Lote de 2000β |  |  |  |  | 2400 |

Paso: WC1 del lote 575γ $=120+575\times3=1845$ min; disponible $=2095-1845=250$ min. El lote 575γ queda completamente programado (empieza en la semana 1 con 250 min de holgura).

### Página 41 — CRP: *repetir el proceso para los demás pedidos*

Mismas tablas que la página 40 (solo cambia el título):

| Semana 3 | WC1 | WC2 | WC4 | Movimiento | Disponible |
|---|---|---|---|---|---|
| Lote de 300γ |  |  |  |  | 2400 |
| Lote de 575γ |  | 740 | 1180 | 480 | 0 |
| Lote de 2000β |  |  |  |  | 2400 |

| Semana 2 | WC1 | WC2 | WC4 | Movimiento |  |
|---|---|---|---|---|---|
| Lote de 300γ |  |  |  |  | 2400 |
| Lote de 575γ |  | 2225 |  | 175 | 0 |
| Lote de 2000β |  |  |  |  | 2400 |

| Semana 1 | WC1 | WC2 | WC4 | Movimiento |  |
|---|---|---|---|---|---|
| Lote de 300γ |  |  |  |  | 2400 |
| Lote de 575γ | 1845 |  |  | 305 | 250 |
| Lote de 2000β |  |  |  |  | 2400 |

### Página 42 — CRP: *repetir el proceso para los demás pedidos*

Resultado final del backward scheduling de los tres lotes (minutos):

| Semana 3 | WC1 | WC2 | WC4 | Movimiento | Disponible |
|---|---|---|---|---|---|
| Lote de 300γ |  |  |  |  | 2400 |
| Lote de 575γ |  | 740 | 1180 | 480 | 0 |
| Lote de 2000β |  |  |  |  | 2400 |

| Semana 2 | WC1 | WC2 | WC4 | Movimiento |  |
|---|---|---|---|---|---|
| Lote de 300γ |  | 1290 | 630 | 480 | 0 |
| Lote de 575γ |  | 2225 |  | 175 | 0 |
| Lote de 2000β |  | 1490 | 430 | 480 | 0 |

| Semana 1 | WC1 | WC2 | WC4 | Movimiento |  |
|---|---|---|---|---|---|
| Lote de 300γ | 1020 | 300 |  | 480 | 600 |
| Lote de 575γ | 1845 |  |  | 305 | 250 |
| Lote de 2000β |  | 2230 |  |  | 170 |

Pasos para los otros dos lotes (entregan en la semana 3, así que deben terminar en la semana 2):

- **Lote 300γ:** WC4 $=30+300\times2=630$; movimiento 480; WC2 total $=90+300\times5=1590$, de los que caben $2400-630-480=1290$ en la semana 2 y $1590-1290=300$ pasan a la semana 1. Semana 1: WC2 300 + movimiento 480 + WC1 $=120+300\times3=1020$; disponible $=2400-1800=600$.
- **Lote 2000β** (ruta WC2 → WC4, sin WC1): WC4 $=30+2000\times0.2=430$; movimiento 480; WC2 total $=120+2000\times1.8=3720$, de los que caben $2400-430-480=1490$ en la semana 2 y $3720-1490=2230$ pasan a la semana 1; disponible $=2400-2230=170$.

### Página 43 — CRP: *repetir el proceso para los demás pedidos*

> [Gráfico: barras agrupadas «Carga de las estaciones de trabajo». Eje X: WC1, WC2, WC4. Eje Y: horas, de 0 a 90. Series: Semana 1 (azul), Semana 2 (naranja), Semana 3 (gris) y una línea horizontal amarilla «Capacidad Normal» en 40 h. Valores aproximados leídos del gráfico, que coinciden con la suma de la página 42 dividida entre 60: WC1 semana 1 ≈ 47.75 h (sin carga en las semanas 2 y 3); WC2 semana 1 ≈ 42.2 h, semana 2 ≈ 83.4 h, semana 3 ≈ 12.3 h; WC4 semana 1 sin carga, semana 2 ≈ 17.7 h, semana 3 ≈ 19.7 h. WC1 en la semana 1 y WC2 en las semanas 1 y 2 superan la capacidad normal; WC2 en la semana 2 supera incluso la capacidad máxima (80 h).]

Carga calculada a partir de la página 42 (los valores del gráfico):

| Estación | Semana 1 (min → h) | Semana 2 (min → h) | Semana 3 (min → h) |
|---|---|---|---|
| WC1 | $1020+1845=2865$ → 47.75 | 0 → 0 | 0 → 0 |
| WC2 | $300+2230=2530$ → 42.17 | $1290+2225+1490=5005$ → 83.42 | 740 → 12.33 |
| WC4 | 0 → 0 | $630+430=1060$ → 17.67 | 1180 → 19.67 |

(La tabla en horas es un cálculo de esta transcripción; la diapositiva solo muestra el gráfico.)

### Página 44 — CRP

*¿Qué hubiera pasado si probamos con una regla de forward Scheduling?*

- *Realice el ejercicio*
- *Considere un doble turno en WC2*

### Página 45 — Alternativas

- El gráfico permite ver en qué periodos y estaciones se está superando la capacidad
- Anticipe la producción y balancee las cargas para reparar la solución

### Página 46 — CRP

- *ATENCION*
  - *El CRP puede tener problemas de secuenciación de los trabajos al no considerar que dos trabajos no se pueden realizar simultáneamente*
  - *Restricciones de precedencia.*
- *Lo veremos en el último tercio*


---

<!-- fuente: corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/backward-scheduling.md -->
# backward-scheduling

> **Archivo:** [`backward-scheduling.xlsx`](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/backward-scheduling.xlsx) · **Corte 2** (el archivo estaba en la carpeta `CORTE 3/` del estudiante) · Libro de Excel con 1 hoja(s): `Hoja1`  
> **Nombre original:** `CORTE 3/Backward Scheduling.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Hoja de cálculo que rehace en Excel el **CRP con backward scheduling** del ejemplo de los productos γ y β de la clase de MRP II ([`L15-mrp-ii.md`](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md), pp. 30-42). Para cada lote (300γ, 575γ y 2000β) reparte por semana los minutos de alistamiento + máquina de cada centro de trabajo (WC1, WC2, WC4) y del movimiento entre estaciones, programando hacia atrás desde la fecha de entrega. Después calcula los minutos que quedan disponibles cada semana (2400 min = 40 h).

**Ubicación:** aunque el archivo original estaba en la carpeta `CORTE 3` (por eso la cabecera dice «Corte 3»), su contenido es el ejemplo de planeación de requerimientos de capacidad (CRP) de MRP II de la L15, Corte 2. Está bien ubicado en esta carpeta. No es scheduling de máquinas del Corte 3: no secuencia trabajos, solo reparte cargas por semana.

Con él se aprende a convertir cada lote en minutos por estación y semana con la fórmula $S+Q\,p$. Se respetan un día de movimiento (480 min) entre operaciones y la capacidad de 2400 min/semana, y se pasa a la semana anterior lo que no cabe.

### Hoja `Hoja1`

#### Objetivo (deducido)

Programar hacia atrás los lotes de la L15 (p. 30): 300γ y 2000β se entregan en la semana 3 y 575γ en la semana 4. Hay que obtener la carga en minutos por semana en cada centro de trabajo y el tiempo disponible restante.

#### Datos de entrada y parámetros

Tabla de parámetros de γ (rango `I2:N5`, título «γ» en `I2`):

| Centro | SU-time (min por lote) | MACH-time (min por unidad) | Celdas |
|---|---|---|---|
| WC1 | 120 | 3 | `I5`, `J5` |
| WC2 | 90 | 5 | `K5`, `L5` |
| WC4 | 30 | 2 | `M5`, `N5` |

Otros parámetros:

| Parámetro | Valor | Celda |
|---|---|---|
| Movimientos (1 día = 8 h × 60 min) | 480 min | `J7` |
| Capacidad semanal (min/semana = 60 × 8 × 5) | 2400 min | `J8` |

Segunda tabla de parámetros (rango `I10:L13`, encabezados `I11` = «WC2», `K11` = «WC4»; el título fusionado `I10:L10` está vacío):

| Centro | SU-time | MACH-time | Celdas |
|---|---|---|---|
| WC2 | 90 | 5 | `I13`, `J13` |
| WC4 | 30 | 2 | `K13`, `L13` |

Esta segunda tabla repite los valores de γ. Según la L15 (p. 31), β usa WC2 con SU = 120 y MACH = 1.8, y WC4 con SU = 30 y MACH = 0.2; esos datos **no aparecen** en el Excel.

Tamaños de lote: 300 y 575 (γ) y 2000 (β), escritos directamente dentro de las fórmulas.

#### Método paso a paso

Minutos que ocupa un lote de tamaño $Q$ en el centro $k$:

$$T_k = S_k + Q\,p_k$$

donde $S_k$ = SU-time (min por lote) y $p_k$ = MACH-time (min por unidad). Disponible de la semana $s$ para un lote:

$$\text{Disp}_s = 2400 - (\text{WC1}_s+\text{WC2}_s+\text{WC4}_s+\text{Mov}_s)$$

**Bloque 1: Lote 300γ (filas 2-6)**, entrega en la semana 3, así que se programa en las semanas 2 y 1.

| Celda | Fórmula | Significado | Valor |
|---|---|---|---|
| `E4` (S2, WC4) | `=M5+(N5*300)` | $30+2\times300$ | 630 |
| `F4` (S2, Mov.) | `=J7` | movimiento WC2→WC4 | 480 |
| `D4` (S2, WC2) | `=K5+(L5*300)-300` | $90+5\times300-300$: total de WC2 (1590) menos los 300 que se pasan a la semana 1 | 1290 |
| `G4` (S2, Disp.) | `=J8-(SUM(C4:F4))` | $2400-(1290+630+480)$ | 0 |
| `C6` (S1, WC1) | `=I5+(J5*300)` | $120+3\times300$ | 1020 |
| `D6` (S1, WC2) | 300 (valor fijo) | resto de WC2 | 300 |
| `F6` (S1, Mov.) | `=J7` | movimiento WC1→WC2 | 480 |
| `G6` (S1, Disp.) | `=J8-(SUM(C6:F6))` | $2400-(1020+300+480)$ | 600 |

**Bloque 2: Lote 575γ (filas 8-14)**, entrega en la semana 4, así que se programa en las semanas 3, 2 y 1.

| Celda | Fórmula | Significado | Valor |
|---|---|---|---|
| `E10` (S3, WC4) | `=M5+(N5*575)` | $30+2\times575$ | 1180 |
| `F10` (S3, Mov.) | `=J7` | movimiento WC2→WC4 | 480 |
| `D10` (S3, WC2) | `=K5+(L5*575)-2225` | $90+5\times575-2225=2965-2225$ | 740 |
| `G10` (S3, Disp.) | `=$J$8-SUM(C10:F10)` | $2400-(740+1180+480)$ | 0 |
| `D12` (S2, WC2) | 2225 (valor fijo) | resto de WC2 | 2225 |
| `F12` (S2, Mov.) | 175 (valor fijo) | parte del movimiento WC1→WC2 que cabe en la semana 2 | 175 |
| `G12` (S2, Disp.) | `=$J$8-(SUM(C12:F12))` | $2400-(2225+175)$ | 0 |
| `C14` (S1, WC1) | `=I5+(J5*300)` | **usa 300 en vez de 575** | 1020 |
| `F14` (S1, Mov.) | `=480+F12` | **suma en vez de restar** | 655 |
| `G14` (S1, Disp.) | `=J8-(SUM(C14:F14))` | $2400-(1020+655)$ | 725 |

**Bloque 3: Lote 2000β (filas 16-22).** Es una copia del bloque 575γ con las referencias desplazadas, sin adaptar a β.

| Celda | Fórmula | Qué calcula realmente | Valor |
|---|---|---|---|
| `D18` (S3, WC2) | `=K13+(L13*575)-2225` | $30+2\times575-2225$ (parámetros de WC4 de γ y lote 575) | −1045 |
| `E18` (S3, WC4) | `=M13+(N13*575)` | celdas vacías | 0 |
| `F18` (S3, Mov.) | `=J15` | celda vacía | 0 |
| `G18` (S3, Disp.) | `=$J$8-SUM(C18:F18)` | $2400-(-1045)$ | 3445 |
| `D20` (S2, WC2) | 2225 (valor fijo copiado) | — | 2225 |
| `F20` (S2, Mov.) | 175 (valor fijo copiado) | — | 175 |
| `G20` (S2, Disp.) | `=$J$8-(SUM(C20:F20))` | $2400-2400$ | 0 |
| `C22` (S1, WC1) | `=I13+(J13*300)` | $90+5\times300$ | 1590 |
| `F22` (S1, Mov.) | `=480+F20` | $480+175$ | 655 |
| `G22` (S1, Disp.) | `=J16-(SUM(C22:F22))` | `J16` vacía: $0-(1590+655)$ | −2245 |

#### Resultados: Excel frente a la solución de la L15 (p. 42)

| Lote | Semana | Concepto | Excel | L15 p. 42 | ¿Coincide? |
|---|---|---|---|---|---|
| 300γ | 2 | WC2 / WC4 / Mov. / Disp. | 1290 / 630 / 480 / 0 | 1290 / 630 / 480 / 0 | Sí |
| 300γ | 1 | WC1 / WC2 / Mov. / Disp. | 1020 / 300 / 480 / 600 | 1020 / 300 / 480 / 600 | Sí |
| 575γ | 3 | WC2 / WC4 / Mov. / Disp. | 740 / 1180 / 480 / 0 | 740 / 1180 / 480 / 0 | Sí |
| 575γ | 2 | WC2 / Mov. / Disp. | 2225 / 175 / 0 | 2225 / 175 / 0 | Sí |
| 575γ | 1 | WC1 / Mov. / Disp. | 1020 / 655 / 725 | 1845 / 305 / 250 | **No** |
| 2000β | 3 | WC2 / WC4 / Mov. / Disp. | −1045 / 0 / 0 / 3445 | — / — / — / 2400 (β no tiene carga en S3) | **No** |
| 2000β | 2 | WC2 / WC4 / Mov. / Disp. | 2225 / — / 175 / 0 | 1490 / 430 / 480 / 0 | **No** (solo Disp.) |
| 2000β | 1 | WC1 / WC2 / Mov. / Disp. | 1590 / — / 655 / −2245 | — / 2230 / — / 170 | **No** |

Valores correctos del lote 2000β según la L15, con ruta WC2 → WC4 y sin WC1:

- WC4: $30+2000\times0.2=430$.
- WC2: $120+2000\times1.8=3720$, repartido en $1490$ (semana 2) y $2230$ (semana 1).
- Movimiento: 480 en la semana 2.
- Disponible en la semana 1: $2400-2230=170$.

Con los valores correctos, la carga en horas es: WC1 S1 = 47.75 h; WC2 S1 = 42.17 h, S2 = 83.42 h, S3 = 12.33 h; WC4 S2 = 17.67 h, S3 = 19.67 h. Ver el gráfico de la L15, p. 43.

#### Gráficos

No hay gráficos ni imágenes en el libro. El gráfico de carga por estación está en la L15, p. 43.

#### Conclusión

El bloque del lote 300γ y las semanas 3 y 2 del lote 575γ reproducen exactamente la solución de clase. La semana 1 del lote 575γ y todo el lote 2000β están incompletos o mal copiados. Para estudiar, use las tablas de la L15 (pp. 35-42), que tienen el resultado correcto.

### Observaciones

- **Errores de fórmula:**
  - `C14` usa el lote 300 en lugar de 575: debería ser `=I5+(J5*575)` = 1845.
  - `F14` suma en lugar de restar: debería ser `=480-F12` = 305. Entonces `G14` daría 250.
- **Bloque 2000β sin terminar:** copia del bloque 575γ con referencias desplazadas (`K13`, `L13`, `M13`, `N13`, `J15`, `J16`), que dan valores negativos (−1045, −2245) y un disponible de 3445 > 2400. No usa los parámetros de β (SU 120 / MACH 1.8 en WC2; SU 30 / MACH 0.2 en WC4), que no están en la hoja. Además pone carga en WC1, centro por el que β no pasa.
- **Valores fijos:** 300 (`D6`), 2225 (`D12`, `D20`) y 175 (`F12`, `F20`) están escritos a mano, no calculados, y las cantidades de los lotes van dentro de las fórmulas.
- La segunda tabla de parámetros (`I10:L13`) repite los datos de WC2 y WC4 de γ, no los de β. Probablemente se quiso poner ahí β (deducido).
- La cabecera del gemelo dice «Corte 3» por la carpeta original; el tema es MRP II / CRP de la L15 (Corte 2).
