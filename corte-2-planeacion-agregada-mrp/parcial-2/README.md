# Parcial 2: planeación agregada y MRP (Corte 2)

## Qué cubre

Este es el examen del Corte 2, con su rúbrica y su solucionario completo. Tiene dos puntos:

- **Punto 1, Sales and Operations Planning** (Muebles Andinos S.A.S., familia de escritorios, sillas y archivadores): agregación en horas estándar, modelo de programación lineal entera, comparación de planes de persecución y nivelado, y desagregación por igual tiempo de agotamiento.
- **Punto 2, MRP** (mesa auxiliar M): árbol de materiales y códigos de nivel bajo, demanda dependiente con netos, matrices MRP lote a lote y la heurística Silver-Meal frente a Wagner-Whitin.

El examen dura 2 horas, se hace en papel y solo admite calculadora no programable.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [parcial-2-solucion.md](./parcial-2-solucion.md) (gemelo de `parcial-2-solucion.pdf`, 13 págs.) | Enunciado (pp. 1–6), rúbrica (pp. 6–7) y solucionario (pp. 7–13), transcritos completos con todas las tablas. Incluye una verificación propia con el Plan C y el óptimo de Wagner-Whitin | Sí |

## Orden de estudio sugerido

1. Repasar los temas antes de resolver:
   - [L10](../01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md), planeación agregada;
   - [L11](../02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md), agregación y desagregación;
   - [L12](../03-wagner-whitin-y-silver-meal/L12-wagner-whitin-and-silver-meal.md), Silver-Meal y Wagner-Whitin;
   - [L13](../04-bom-y-mrp/L13-bom-intro-to-mrp.md) y [L14](../04-bom-y-mrp/L14-mrp.md), BOM y MRP.
2. Leer el enunciado en [parcial-2-solucion.md](./parcial-2-solucion.md) (páginas 1 a 6) e intentar resolverlo sin mirar la solución.
3. Comparar con el solucionario (páginas 7 a 13) y con la sección «Verificación propia» del resumen.
4. Revisar la rúbrica (páginas 6–7). Las preguntas marcadas [Argumente] reparten el puntaje mitad cálculo y mitad argumento.

## Conceptos y fórmulas clave

El detalle está en [parcial-2-solucion.md](./parcial-2-solucion.md#resumen).

- **Demanda agregada:** $D_t=\sum_i k_i d_{i,t}$, donde $k_i$ son las horas estándar por unidad y $d_{i,t}$ la demanda en unidades.
- **Modelo de planeación agregada.** Variables: $W$ operarios, $H$ contrataciones, $F$ despidos, $O$ horas extra, $S$ subcontratación, $I$ inventario, $P$ producción regular.

$$\min\sum_t\left(3.2\text{M}\,W_t+30\text{k}\,O_t+38\text{k}\,S_t+1.5\text{M}\,H_t+2.5\text{M}\,F_t+2\text{k}\,I_t\right)$$

  sujeto a:
  - $I_t=I_{t-1}+P_t+O_t+S_t-D_t$;
  - $W_t=W_{t-1}+H_t-F_t$;
  - $P_t\le160W_t$;
  - $O_t\le32W_t$.
- **Tiempo de agotamiento igual:** $T^*=\dfrac{X+\sum_i I_i}{\sum_i d_i}$ y $Y_i=T^*d_i-I_i$. Aquí $X$ son las horas aprobadas, $I_i$ el inventario en horas y $d_i$ la demanda en horas.
- **MRP lote a lote:** $RN_t=\max(0,RB_t-IP_{t-1}-RP_t)$, $LOP_{t-LT}=ROP_t=RN_t$ y $RB^{\text{hijo}}_t=\sum q\cdot LOP^{\text{padre}}_t$. Los ítems se procesan por código de nivel bajo.
- **Silver-Meal:** $C(j,k)=\dfrac{S+h\sum_{t=j}^{k}(t-j)D_t}{k-j+1}$; el lote se cierra cuando el costo por periodo sube.
- **Wagner-Whitin:** $f(k)=\min_j\{f(j-1)+S+h\sum_{t=j}^{k}(t-j)D_t\}$.

## Ejercicios resueltos disponibles

Todos están en [parcial-2-solucion.md](./parcial-2-solucion.md).

| Pregunta | Resultado principal |
|---|---|
| 1.1 Agregación | 2400, 2560, 3200 y 2880 h estándar; el mes 3 equivale a 1600 escritorios |
| 1.3 Planes | A (persecución) cuesta $235.800.000 y B (nivelado) $229.440.000. Plan C, cálculo propio: $225.500.000, el más barato, aunque el solucionario recomienda B |
| 1.4 Desagregación de 2620 h | $T^*=1{,}2$ meses: 500 escritorios, 400 sillas y 340 archivadores |
| 2.1 BOM | Códigos de nivel bajo: M = 0, T = 1, S = 1, K = 2, P = 2 |
| 2.2 Explosión de 200 mesas | Netos: M 180, T 150, S 130, P 420, K 380 |
| 2.3 MRP | Liberaciones de M en las semanas 2, 4, 5 y 7 (30, 60, 40, 70); de S en las semanas 3, 4 y 6 (20, 40, 70); de K en las semanas 3, 4, 5 y 6 (100, 40, 140, 70) |
| 2.4 Silver-Meal | Pedidos de 310, 350 y 200 u en las semanas 1, 4 y 6; costo $1.390.000. Wagner-Whitin, cálculo propio: $1.280.000 |

**Errores del documento** (detalle en el resumen del gemelo):

- La portada dice 100 puntos, pero la tabla de puntos suma 110.
- La recomendación de 1.3c contradice su propio argumento.
- El solucionario de 2.1 incluye un literal c) que el enunciado no pide.
- En 2.4 solo se pide Silver-Meal, aunque el título dice «Silver-Meal vs. Wagner-Whitin».

## Relación con otros temas y proyectos

- [01-planeacion-agregada-modelo-bowman](../01-planeacion-agregada-modelo-bowman/): el modelo de costos y la formulación de la pregunta 1.2.
- [02-agregacion-y-desagregacion](../02-agregacion-y-desagregacion/): agregación en horas estándar y desagregación por tiempo de agotamiento (preguntas 1.1 y 1.4).
- [03-wagner-whitin-y-silver-meal](../03-wagner-whitin-y-silver-meal/): lot sizing (pregunta 2.4); [wagner_whitin.py](../03-wagner-whitin-y-silver-meal/wagner_whitin.py) sirve para comprobar el óptimo.
- [04-bom-y-mrp](../04-bom-y-mrp/): BOM, código de nivel bajo, demanda dependiente y matriz MRP (preguntas 2.1 a 2.3).
- [05-mrp-ii-y-capacidad](../05-mrp-ii-y-capacidad/): MRP II y capacidad, tema posterior que no entra en este parcial.
- [proyecto-thyms-gemelo-digital](../proyecto-thyms-gemelo-digital/): el proyecto del Corte 2, que aplica planeación agregada y MRP a un caso real.
