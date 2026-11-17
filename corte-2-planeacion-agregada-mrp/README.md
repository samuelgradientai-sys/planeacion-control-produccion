# Corte 2: Planeación agregada, tamaño de lote y MRP

Segundo corte del curso (30 % de la nota final). Va de la planeación de **mediano plazo**, agregada y por familias, a la planeación **detallada de materiales y capacidad**:

```
Pronóstico (Corte 1) → S&OP / plan agregado (Bowman, PL de flujo)
                     → desagregación por producto
                     → tamaño de lote (Wagner-Whitin, Silver-Meal)
                     → BOM y MRP (explosión de materiales)
                     → MRP II (RCCP, CRP, backward scheduling)
                     → programación detallada (Corte 3)
```

## Temas (en orden de clase)

| # | Carpeta | Clase | Qué cubre | Ejercicios en la carpeta |
|---|---|---|---|---|
| 01 | [`01-planeacion-agregada-modelo-bowman/`](01-planeacion-agregada-modelo-bowman/README.md) | [L10](01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md) | S&OP, unidades agregadas, método gráfico (persecución, nivelada, mixta), **modelo de Bowman** como PL de transporte, revenue management | Bowman en Excel/Solver (dos versiones, costo óptimo $8144) y **PL de flujo en GAMS** (z = 4.062.000) |
| 02 | [`02-agregacion-y-desagregacion/`](02-agregacion-y-desagregacion/README.md) | [L11](02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md) | PL con fuerza de trabajo y backlog; desagregación por **tiempo de agotamiento** y tiempo de ciclo máximo | Desagregación con Solver (T* = 1,5948), dos versiones con óptimos alternativos |
| 03 | [`03-wagner-whitin-y-silver-meal/`](03-wagner-whitin-y-silver-meal/README.md) | [L12](03-wagner-whitin-y-silver-meal/L12-wagner-whitin-and-silver-meal.md) | Tamaño de lote dinámico: **Wagner-Whitin** (programación dinámica / ruta más corta) y heurística **Silver-Meal** | `wagner_whitin.py` (ver la advertencia en su README) |
| 04 | [`04-bom-y-mrp/`](04-bom-y-mrp/README.md) | [L13](04-bom-y-mrp/L13-bom-intro-to-mrp.md), [L14](04-bom-y-mrp/L14-mrp.md) | Listas de materiales (BOM), matriz BOM, demanda dependiente $dd = d\,(I-B)^{-1}$, **tabla MRP**, lotificación, nerviosismo | MRP del esfero (v1 y v2), explosión de BOM con `MMULT`/`MINVERSE` |
| 05 | [`05-mrp-ii-y-capacidad/`](05-mrp-ii-y-capacidad/README.md) | [L15](05-mrp-ii-y-capacidad/L15-mrp-ii.md) | **MRP II**, RCCP, **CRP**, MRP de ciclo cerrado, backward/forward scheduling | Backward scheduling por centro de trabajo (lotes 300γ, 575γ, 2000β) |

## Evaluaciones y proyecto

- **[`parcial-2/`](parcial-2/README.md)**: enunciado, rúbrica y solucionario completos del parcial 2 (planeación agregada, PLE, desagregación, BOM, MRP y Silver-Meal), con verificaciones adicionales.
- **[`proyecto-thyms-gemelo-digital/`](proyecto-thyms-gemelo-digital/README.md)**: proyecto del corte sobre THYMS Colombia S.A.S. Incluye el estudio preliminar (takt, throughput, WIP, ley de Little, cuellos de botella), el gemelo digital en Python/SimPy con sensores virtuales, el S&OP y el plan agregado. Continúa el proyecto del Corte 1 ([`../corte-1-pronosticos/proyecto-thyms-pronostico/`](../corte-1-pronosticos/proyecto-thyms-pronostico/README.md)). Para retomar el trabajo, el documento de traspaso es [`CONTEXTO_GEMELO_THYMS.md`](proyecto-thyms-gemelo-digital/CONTEXTO_GEMELO_THYMS.md).

## Archivos que estaban en otra carpeta

Cuatro Excel de temas de este corte estaban en la carpeta `CORTE 3/` del estudiante y se movieron a su tema:

- `Ejemplo Modelo Bowman.xlsx` → [`01-.../ejemplo-modelo-bowman.md`](01-planeacion-agregada-modelo-bowman/ejemplo-modelo-bowman.md)
- `Modelo de Desagregación .xlsx` → [`02-.../modelo-desagregacion-v2.md`](02-agregacion-y-desagregacion/modelo-desagregacion-v2.md)
- `Cálculo de Demanda Dependiente Directa.xlsx` → [`04-.../calculo-demanda-dependiente-directa.md`](04-bom-y-mrp/calculo-demanda-dependiente-directa.md)
- `Backward Scheduling.xlsx` → [`05-.../backward-scheduling.md`](05-mrp-ii-y-capacidad/backward-scheduling.md)

## Cuidado con estos errores

- `wagner_whitin.py` cobra el alistamiento aunque el lote sea de 0 unidades, así que su plan ($207,6) no es el óptimo ($130).
- Algunas diapositivas y Excel tienen errores de cálculo.

Todos están documentados en [`../ERRATAS.md`](../ERRATAS.md).
