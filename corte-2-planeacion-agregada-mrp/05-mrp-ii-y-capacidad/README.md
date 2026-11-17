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
| [`L15-mrp-ii.md`](./L15-mrp-ii.md) (gemelo de `L15-mrp-ii.pdf`) | Presentación de clase, 46 páginas: MRP vs. MRP II, RCCP, CRP, control de piso, ciclo cerrado, ejemplo de traducción en capacidad (A-F), backward/forward scheduling y ejemplo CRP con lotes γ y β | Sí |
| [`backward-scheduling.md`](./backward-scheduling.md) (gemelo de `backward-scheduling.xlsx`) | Excel que rehace las tablas CRP de backward scheduling de la L15 (pp. 35-42) para los lotes 300γ, 575γ y 2000β, en minutos por semana. Estaba en la carpeta del Corte 3, pero es de este tema. Tiene errores en el lote 575γ (semana 1) y en el lote 2000β | Después de L15 |

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
  donde $p_{j,o}$ = horas/unidad de la operación $o$ del ítem $j$ y $m(j,o)$ = centro donde se hace. Detalle en [`L15-mrp-ii.md`](./L15-mrp-ii.md), pp. 15-21.
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
| Traducción en capacidad de A, B (POQ = 2), C ($\tau=2$, 2 operaciones), D, E, F | [`L15-mrp-ii.md`](./L15-mrp-ii.md), pp. 13-21 | WKC 100: 59.00 / 2.00 / 87.40 / 2.25 h (periodos 0-3); WKC 200: 62.00 / 54.60 / 83.80 / 70.70 / 4.50 h (periodos −2 a 2); WKC 300: 8.00 / 8.00 / 7.60 / 9.00 h (periodos −1 a 2) |
| Backward schedule por días (Gantt) de los lotes 300γ, 575γ y 2000β | [`L15-mrp-ii.md`](./L15-mrp-ii.md), p. 33 | 300γ y 2000β terminan en S2 día 5; 575γ en S3 día 5 |
| CRP backward en minutos por semana | [`L15-mrp-ii.md`](./L15-mrp-ii.md), pp. 35-42 | Disponible en S1: 600 (300γ), 250 (575γ), 170 (2000β) |
| Carga por estación | [`L15-mrp-ii.md`](./L15-mrp-ii.md), p. 43 | WC1 S1 = 47.75 h; WC2 S1 = 42.17 h, S2 = 83.42 h (> 80 h máx.), S3 = 12.33 h; WC4 S2 = 17.67 h, S3 = 19.67 h |
| Mismo CRP en Excel | [`backward-scheduling.md`](./backward-scheduling.md) | 300γ correcto (S2: 1290/630/480/0; S1: 1020/300/480/600); 575γ correcto en S3-S2 y erróneo en S1 (1020/655/725 en vez de 1845/305/250); 2000β sin terminar |

## Relación con otros temas y proyectos

- MRP, BOM y registro de lotes (base de la traducción en capacidad): [`../04-bom-y-mrp/`](../04-bom-y-mrp/), en especial [`L14-mrp.md`](../04-bom-y-mrp/L14-mrp.md), que repite las diapositivas de MRP de ciclo cerrado, y [`mrp-esfero.md`](../04-bom-y-mrp/mrp-esfero.md).
- Tamaños de lote (lote a lote, POQ, Wagner-Whitin, Silver-Meal): [`../03-wagner-whitin-y-silver-meal/`](../03-wagner-whitin-y-silver-meal/).
- Planeación agregada y desagregación (capacidad a nivel alto y origen del MPS): [`../01-planeacion-agregada-modelo-bowman/`](../01-planeacion-agregada-modelo-bowman/) y [`../02-agregacion-y-desagregacion/`](../02-agregacion-y-desagregacion/).
- Evaluación del corte: [`../parcial-2/`](../parcial-2/).
- Proyecto del corte: [`../proyecto-thyms-gemelo-digital/`](../proyecto-thyms-gemelo-digital/).
- Secuenciación con precedencias (lo que el CRP no resuelve): [`../../corte-3-programacion-scheduling/01-introduccion-scheduling/`](../../corte-3-programacion-scheduling/01-introduccion-scheduling/), [`../../corte-3-programacion-scheduling/03-maquinas-paralelas/`](../../corte-3-programacion-scheduling/03-maquinas-paralelas/) (forward scheduling con máquinas paralelas) y [`../../corte-3-programacion-scheduling/05-job-shop/`](../../corte-3-programacion-scheduling/05-job-shop/).
