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
| 01 | [`01-planeacion-agregada-modelo-bowman/`](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/README.md) | [L10](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md) | S&OP, unidades agregadas, método gráfico (persecución, nivelada, mixta), **modelo de Bowman** como PL de transporte, revenue management | Bowman en Excel/Solver (dos versiones, costo óptimo $8144) y **PL de flujo en GAMS** (z = 4.062.000) |
| 02 | [`02-agregacion-y-desagregacion/`](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/README.md) | [L11](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md) | PL con fuerza de trabajo y backlog; desagregación por **tiempo de agotamiento** y tiempo de ciclo máximo | Desagregación con Solver (T* = 1,5948), dos versiones con óptimos alternativos |
| 03 | [`03-wagner-whitin-y-silver-meal/`](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/README.md) | [L12](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/L12-wagner-whitin-and-silver-meal.md) | Tamaño de lote dinámico: **Wagner-Whitin** (programación dinámica / ruta más corta) y heurística **Silver-Meal** | `wagner_whitin.py` (ver la advertencia en su README) |
| 04 | [`04-bom-y-mrp/`](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/README.md) | [L13](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md), [L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md) | Listas de materiales (BOM), matriz BOM, demanda dependiente $dd = d\,(I-B)^{-1}$, **tabla MRP**, lotificación, nerviosismo | MRP del esfero (v1 y v2), explosión de BOM con `MMULT`/`MINVERSE` |
| 05 | [`05-mrp-ii-y-capacidad/`](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/README.md) | [L15](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md) | **MRP II**, RCCP, **CRP**, MRP de ciclo cerrado, backward/forward scheduling | Backward scheduling por centro de trabajo (lotes 300γ, 575γ, 2000β) |

## Evaluaciones y proyecto

- **[`parcial-2/`](/corte-2-planeacion-agregada-mrp/parcial-2/README.md)**: enunciado, rúbrica y solucionario completos del parcial 2 (planeación agregada, PLE, desagregación, BOM, MRP y Silver-Meal), con verificaciones adicionales.
- **[`proyecto-thyms-gemelo-digital/`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/README.md)**: proyecto del corte sobre THYMS Colombia S.A.S. Incluye el estudio preliminar (takt, throughput, WIP, ley de Little, cuellos de botella), el gemelo digital en Python/SimPy con sensores virtuales, el S&OP y el plan agregado. Continúa el proyecto del Corte 1 ([`../corte-1-pronosticos/proyecto-thyms-pronostico/`](/corte-1-pronosticos/proyecto-thyms-pronostico/README.md)). Para retomar el trabajo, el documento de traspaso es [`CONTEXTO_GEMELO_THYMS.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/CONTEXTO_GEMELO_THYMS.md).

## Archivos que estaban en otra carpeta

Cuatro Excel de temas de este corte estaban en la carpeta `CORTE 3/` del estudiante y se movieron a su tema:

- `Ejemplo Modelo Bowman.xlsx` → [`01-.../ejemplo-modelo-bowman.md`](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/ejemplo-modelo-bowman.md)
- `Modelo de Desagregación .xlsx` → [`02-.../modelo-desagregacion-v2.md`](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion-v2.md)
- `Cálculo de Demanda Dependiente Directa.xlsx` → [`04-.../calculo-demanda-dependiente-directa.md`](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/calculo-demanda-dependiente-directa.md)
- `Backward Scheduling.xlsx` → [`05-.../backward-scheduling.md`](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/backward-scheduling.md)

## Cuidado con estos errores

- `wagner_whitin.py` cobra el alistamiento aunque el lote sea de 0 unidades, así que su plan ($207,6) no es el óptimo ($130).
- Algunas diapositivas y Excel tienen errores de cálculo.

Todos están documentados en [`../ERRATAS.md`](/ERRATAS.md).


---

<!-- fuente: corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/README.md -->
# Planeación agregada y modelo de Bowman (Corte 2)

## Qué cubre

La planeación agregada es el plan de mediano plazo (3 a 18 meses) que convierte el pronóstico de demanda en horas de producción, fuerza de trabajo, inventario, horas extra y subcontratación al menor costo.

Esta carpeta reúne cuatro cosas:
- la clase L10 (S&OP, agregación de productos, método gráfico con tres estrategias, modelo de transporte de Bowman de 1956, servicios y revenue management);
- dos libros de Excel que resuelven con Solver el ejemplo de Bowman de la clase;
- un modelo lineal en GAMS, el «modelo de flujo», con fuerza de trabajo, horas extra, faltantes y subcontratación para 12 meses;
- la salida de ese modelo en GAMS, que es el plan que luego se desagrega en la carpeta 02.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [L10-aggregate-planning.md](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md) | Presentación de la clase 10 (74 pp.). Cubre S&OP, opciones de capacidad, agregación (Nahmias), método gráfico (\$108 450 / \$105 152 / \$117 800), modelo de Bowman con ejemplo de costo mínimo \$8144, desagregación y revenue management. | **Sí (1.º)** |
| [modelo-bowman.md](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-bowman.md) | Excel con Solver (hojas `COSTOS` y `PRODUCCION`) que resuelve el ejemplo de Bowman de L10 pp. 55-67. Costo \$6784 regular + \$1360 extra = \$8144. | 2.º |
| [ejemplo-modelo-bowman.md](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/ejemplo-modelo-bowman.md) | El **mismo ejercicio** reorganizado en una sola hoja, con parámetros enlazados. Tiene la misma solución y el mismo costo de \$8144. Venía de la carpeta del Corte 3. | 3.º (o en lugar del 2.º) |
| [modelo-flujo-gams/modelo-flujo.gms](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/modelo-flujo.gms) | Código GAMS (sin gemelo `.md`; se explica y se copia completo abajo). Es un PL de planeación agregada de 12 periodos con fuerza de trabajo, horas extra, faltantes y subcontratación. | 4.º |
| [modelo-flujo-gams/modelo-flujo.lst](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/modelo-flujo.lst) | Listado de salida de GAMS: eco del código, ecuaciones generadas, estadísticas y solución óptima con valores marginales. $z = 4\,062\,000$. Se resume abajo. | Con el `.gms` |
| [modelo-flujo-gams/modelo-flujo.log](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/modelo-flujo.log) | Bitácora de la ejecución: GAMS 54.3.1, CPLEX 22.1.2.0 con licencia demo, tamaño del modelo y «Optimal solution found, Objective: 4062000». | Opcional |
| [modelo-flujo-gams/modelo-flujo.lxi](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/modelo-flujo.lxi) | Índice del `.lst` que usa el IDE de GAMS para navegar el listado. Es un archivo de texto con líneas como `D 83 FO` o `I 643 z`. No tiene información del modelo. | No |

Los binarios (`.pdf` y `.xlsx`) están al lado de cada `.md`, con el mismo nombre.

## Orden de estudio sugerido

1. **L10 pp. 1-34** ([L10](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md)): qué es la planeación agregada, la jerarquía de planes, S&OP, las opciones de capacidad y demanda, y cómo agregar productos (ejemplo de Nahmias, p. 31).
2. **L10 pp. 35-49**: el método gráfico y las tres estrategias (nivelar, subcontratar, contratar y despedir) con sus costos.
3. **L10 pp. 50-68**: la formulación de Bowman y el ejemplo completo (demanda neta agregada, matriz de costos, solución, plan consolidado, costo \$8144 y desagregación).
4. Abrir [modelo-bowman.md](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-bowman.md) y [ejemplo-modelo-bowman.md](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/ejemplo-modelo-bowman.md) para ver cómo se monta el mismo problema en Excel con Solver, y por qué su asignación difiere de la diapositiva pero cuesta lo mismo.
5. Leer [L11 pp. 3-12](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md) (modelo con fuerza de trabajo y backlog) y después la sección [Modelo de flujo en GAMS](#modelo-de-flujo-en-gams-modelo-flujo-gams) de este README, que implementa ese modelo.
6. Seguir con la desagregación del plan GAMS en [02-agregacion-y-desagregacion](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/README.md).
7. L10 pp. 69-74 (servicios y revenue management) como cierre conceptual.

## Conceptos y fórmulas clave

Todos los detalles están en el [Resumen de L10](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md).

**Producto agregado ponderado** (L10 p. 31). $D_i$ es la demanda, $h_i$ las horas-hombre por unidad y $p_i$ el precio del modelo $i$.

$$w_i=\frac{D_i}{\sum_j D_j},\qquad \bar h=\sum_i w_ih_i=5{,}06,\qquad \bar p=\sum_i w_ip_i=\$415{,}02$$

**Demanda agregada en horas** (L10 p. 56). La demanda neta es la bruta menos el inventario disponible.

$$D^{agr}_t\,[h]=1{,}0\,A^{neta}_t+0{,}4\,B^{neta}_t$$

**Método gráfico** (L10 pp. 36-49). $d_t$ son los días productivos, $r$ la tasa diaria e $I_t$ el inventario.

$$r=\frac{\sum_t D_t}{\sum_t d_t}=\frac{6200}{124}=50\ \text{unid/día},\qquad P_t=r\,d_t,\qquad I_t=I_{t-1}+P_t-D_t$$

**Modelo de Bowman** (L10 p. 54). Es un problema de transporte. La fuente $i$ es la capacidad (por ejemplo regular o extra), $j$ el periodo de producción y $k$ el periodo de consumo. $C_{ijk}$ es el costo unitario de producir en $j$ y guardar hasta $k$, $B_{ij}$ la capacidad y $D_k$ la demanda. No admite backlog ni cambios de fuerza de trabajo.

$$\min Z=\sum_{i=1}^{m}\sum_{j=1}^{T}\sum_{k=1}^{T}C_{ijk}P_{ijk}\quad\text{s.a.}\quad\sum_{k=j}^{T}P_{ijk}\le B_{ij},\qquad\sum_{i=1}^{m}\sum_{j=1}^{k}P_{ijk}=D_k,\qquad P_{ijk}\ge0$$

$$C_{R,jk}=C_R+(k-j)C_I,\qquad C_{O,jk}=C_O+(k-j)C_I\quad(k\ge j);\qquad k<j\ \text{prohibido}$$

**Modelo de flujo con fuerza de trabajo** (L11 pp. 3-7; implementado en GAMS, ver la sección siguiente):

$$\min\sum_t\left(cP_t+hI_t+c_FS_t+c_RL^R_t+c_OL^O_t+c_{W^+}W^+_t+c_{W^-}W^-_t+c_{sub}U_t\right)$$

$$NI_t=NI_{t-1}+P_t+U_t-D_t,\qquad NI_t=I_t-S_t,\qquad L^R_t=L^R_{t-1}+W^+_t-W^-_t,\qquad P_t=L^R_t+L^O_t$$

## Modelo de flujo en GAMS (`modelo-flujo-gams/`)

### Qué hace

[`modelo-flujo.gms`](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/modelo-flujo.gms) (nombre original `MODELO DE FLUJO.gms`) formula y resuelve con CPLEX un **programa lineal de planeación agregada de 12 meses**. Decide en cada mes cuánto producir, cuántas horas regulares y extra usar, cuánto contratar o despedir (en horas de fuerza de trabajo), cuánto subcontratar y cuánto inventario o faltante llevar. El objetivo es minimizar el costo total.

Es el modelo de [L11 pp. 3-9](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md) con los datos del ejemplo de 5 productos y 12 meses: la demanda en horas-hombre es la columna «Total» de L11 p. 8, el inventario inicial es 3000 y los costos son los de L11 p. 9. Le agrega subcontratación, pone una penalización finita de 10 000 por faltante en lugar de $\pi=\infty$ y no tiene variable de horas ociosas.

Es la generalización del modelo de Bowman de L10, porque añade decisiones de fuerza de trabajo, faltantes y subcontratación. La solución ($P_t$, $I_t$) es el «Plan Agregado» que se desagrega por producto en [modelo-desagregacion.md](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion.md) y [modelo-desagregacion-v2.md](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion-v2.md).

### Conjuntos

- $T=\{1,2,\dots,12\}$: periodos (meses). En GAMS: `Sets T periodos /1*12/;`.

### Parámetros y valores

Demanda $D_t$ (`Demand(T)`), en horas-hombre, que es igual a unidades porque una unidad agregada equivale a una hora:

| $t$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $D_t$ | 2600 | 3400 | 3900 | 5300 | 4250 | 4200 | 3800 | 4500 | 4300 | 3800 | 3600 | 3000 | 46 650 |

Escalares:

| GAMS | Símbolo | Significado | Valor |
|---|---|---|---|
| `c` | $c$ | Costo de producción por unidad («costo de produccion», sin nómina) | 80 |
| `h` | $h$ | Costo de mantener una unidad en inventario por periodo (el código no lo describe) | 2.7 |
| `CF` | $c_F$ | Costo por unidad faltante por periodo (penalización grande, en lugar de $\infty$) | 10 000 |
| `CR` | $c_R$ | Costo de una hora regular | 12 |
| `CO` | $c_O$ | Costo de una hora extra | 18 |
| `CWplus` | $c_{W^+}$ | Costo de aumentar la fuerza de trabajo en una hora | 10 |
| `CWminus` | $c_{W^-}$ | Costo de disminuir la fuerza de trabajo en una hora | 37 |
| `Cutso` | $c_{sub}$ | Costo de subcontratar una unidad | 95 |

Datos iniciales escritos directamente en las ecuaciones:
- inventario neto inicial $NI_0=3000$, que es el «Initial Stock» total de L11 p. 8;
- horas regulares del periodo 1, $L^R_1=2880$, que es el mismo valor de la solución de L11 p. 11. Según L11 p. 10, 26 trabajadores son 4160 h, es decir, 160 h por trabajador, así que 2880 h serían 18 trabajadores (deducido).

### Variables

| GAMS | Símbolo | Tipo | Significado |
|---|---|---|---|
| `P(T)` | $P_t$ | $\ge0$ | Producción en el periodo $t$ |
| `I(T)` | $I_t$ | $\ge0$ | Inventario a la mano |
| `S(T)` | $S_t$ | $\ge0$ | Faltantes (inventario neto negativo, es decir, backlog) |
| `LR(T)` | $L^R_t$ | $\ge0$ | Horas de trabajo en tiempo regular (nivel de fuerza de trabajo) |
| `LO(T)` | $L^O_t$ | $\ge0$ | Horas extra |
| `Wplus(T)` | $W^+_t$ | $\ge0$ | Aumento de la fuerza de trabajo (horas contratadas) |
| `Wminus(T)` | $W^-_t$ | $\ge0$ | Reducción de la fuerza de trabajo (horas despedidas) |
| `OUTSOURCE(T)` | $U_t$ | $\ge0$ | Unidades subcontratadas |
| `NI(T)` | $NI_t$ | libre | Inventario neto ($I_t-S_t$) |
| `z` | $z$ | libre | Valor de la función objetivo |

### Función objetivo y restricciones

Ecuación `FO`:

$$\min z=\sum_{t=1}^{12}\Big(c\,P_t+h\,I_t+c_F\,S_t+c_R\,L^R_t+c_O\,L^O_t+c_{W^+}W^+_t+c_{W^-}W^-_t+c_{sub}\,U_t\Big)$$

Sujeto a:

| Ecuación GAMS | Restricción | Dominio |
|---|---|---|
| `INVINICIAL` | $NI_1=3000+P_1+U_1-D_1$ | $t=1$ |
| `INVNETO1(T)` | $NI_t=NI_{t-1}+P_t+U_t-D_t$ (balance de inventario neto) | $t=2..12$ (`$(ORD(T)>1)`) |
| `INVINICIALHAND` y `INVNETO2(T)` | $NI_t=I_t-S_t$ (el neto se separa en inventario a la mano y faltante) | $t=1$ y $t=2..12$ |
| `WFINICIAL` | $L^R_1=2880$ | $t=1$ |
| `WORKFORCE(T)` | $L^R_t=L^R_{t-1}+W^+_t-W^-_t$ (conservación de la fuerza de trabajo) | $t=2..12$ |
| `PRODUCTION(T)` | $P_t=L^R_t+L^O_t$ (producción = horas regulares + horas extra) | $t=1..12$ |
| Signos | $P,I,S,L^R,L^O,W^+,W^-,U\ge0$; $NI$, $z$ libres | |

Se resuelve con `solve planeacionAgregada using LP minimizing z;` y se imprimen con `display` los valores de z, P, I, NI, LR, LO, S, Wplus, Wminus y OUTSOURCE.

### Código completo (`modelo-flujo.gms`)

```gams
Sets
T periodos /1*12/;

Parameters
Demand(T)
/
1  2600
2  3400
3  3900
4  5300
5  4250
6  4200
7  3800
8  4500
9  4300
10 3800
11 3600
12 3000
/;

scalar
c costo de produccion /80/
h /2.7/
CF /10000/
CR /12/
CO /18/
CWplus /10/
CWminus /37/
Cutso /95/;

Positive Variables
P(T) produccion en el periodo t
I(T) inventario a la mano en el periodo t
S(T) faltantes en el periodo T
LR(T) horas de trabajo en tiempo regular en el periodo T
LO(T) horas de trabajo extra en el periodo T
Wplus(T) aumento en la fuerza de trabajo en el periodo T
Wminus(T) reduccion en la fuerza de trabajo en el periodo T
OUTSOURCE(T) unidades subcontratadas en el periodo T
;

free variables
z valor de la funcion objetivo
NI(T) inventario neto
;

equations
FO definicion de la funcion objetivo para minimizar
INVNETO1(T) definicion 1 del inventario neto
INVNETO2(T) definicion 2 del inventario neto
WORKFORCE(T) conservacion de la fuerza de trabajo
PRODUCTION(T) relacion de la produccion y fuerza de trabajo
INVINICIAL inventario neto inicial
INVINICIALHAND inventario a la mano inicial
WFINICIAL fuerza de trabajo inicial
;

FO..                        z =e= SUM(T, c*P(T) + h*I(T) + CF*S(T) + CR*LR(T) + CO*LO(T) + CWplus*Wplus(T) + CWminus*Wminus(T) + Cutso*OUTSOURCE(T));
INVNETO1(T)$(ORD(T)>1)..    NI(T) =e= NI(T-1) + P(T) + OUTSOURCE(T) - Demand(T);
INVNETO2(T)$(ORD(T)>1)..    NI(T) =e= I(T) - S(T);
WORKFORCE(T)$(ORD(T)>1)..   LR(T) =e= LR(T-1) + Wplus(T) - Wminus(T);
PRODUCTION(T)..             P(T) =e= LR(T) + LO(T);
INVINICIAL..                NI("1") =e= 3000 + P("1") + OUTSOURCE("1") - Demand("1");
INVINICIALHAND..            NI("1") =e= I("1") - S("1");
WFINICIAL..                 LR("1") =e= 2880;

model planeacionAgregada /all/;
solve planeacionAgregada using LP minimizing z;
display z.l, P.l, I.l, NI.l, LR.l, LO.l, S.l, Wplus.l, Wminus.l, OUTSOURCE.l;
```

### Salida (`modelo-flujo.lst` y `modelo-flujo.log`)

**Ejecución**
- Software: GAMS 54.3.1 con CPLEX 22.1.2.0, licencia demo.
- Tamaño del modelo: 8 bloques de ecuaciones (49 ecuaciones), 10 bloques de variables (109 variables) y 261 elementos no nulos. El rango de lados derechos va de 400 a 5300; el 400 es $3000-2600$ de `INVINICIAL`. Los coeficientes van de 1 a $10^4$.
- Presolve de CPLEX: eliminó 1 fila y 29 columnas e hizo 25 sustituciones. El PL reducido quedó con 22 filas, 55 columnas y 86 no nulos.
- Resolución: 28 iteraciones y 0,016 s.
- Resultado: **SOLVER STATUS 1 Normal Completion, MODEL STATUS 1 Optimal, OBJECTIVE VALUE 4 062 000**.
- Las marcas `INFES ****` del «Equation Listing» del `.lst` no son errores. Solo indican que, con los valores iniciales en 0 antes de resolver, esas ecuaciones no se cumplen.

**Solución óptima** (niveles `.L`; los valores que el `.lst` muestra como «.» son 0):

| $t$ | $D_t$ | $P_t$ | $L^R_t$ | $L^O_t$ | $W^+_t$ | $W^-_t$ | $U_t$ (subcontr.) | $I_t$ | $NI_t$ | $S_t$ |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2600 | 2880 | 2880 | 0 | 0 | 0 | 0 | 3280 | 3280 | 0 |
| 2 | 3400 | 2880 | 2880 | 0 | 0 | 0 | 0 | 2760 | 2760 | 0 |
| 3 | 3900 | 3000 | 3000 | 0 | 120 | 0 | 0 | 1860 | 1860 | 0 |
| 4 | 5300 | 3000 | 3000 | 0 | 0 | 0 | 440 | 0 | 0 | 0 |
| 5 | 4250 | 3000 | 3000 | 0 | 0 | 0 | 1250 | 0 | 0 | 0 |
| 6 | 4200 | 3000 | 3000 | 0 | 0 | 0 | 1200 | 0 | 0 | 0 |
| 7 | 3800 | 3000 | 3000 | 0 | 0 | 0 | 800 | 0 | 0 | 0 |
| 8 | 4500 | 3000 | 3000 | 0 | 0 | 0 | 1500 | 0 | 0 | 0 |
| 9 | 4300 | 3000 | 3000 | 0 | 0 | 0 | 1300 | 0 | 0 | 0 |
| 10 | 3800 | 3000 | 3000 | 0 | 0 | 0 | 800 | 0 | 0 | 0 |
| 11 | 3600 | 3000 | 3000 | 0 | 0 | 0 | 600 | 0 | 0 | 0 |
| 12 | 3000 | 3000 | 3000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total** | 46 650 | 35 760 | 35 760 | 0 | 120 | 0 | 7890 | 7900 | | 0 |

**Desglose del costo** (cálculo propio con los niveles; la suma coincide con el `.lst`):

| Componente | Cálculo | Costo |
|---|---|---|
| Producción | $80\times35\,760$ | 2 860 800 |
| Horas regulares | $12\times35\,760$ | 429 120 |
| Subcontratación | $95\times7890$ | 749 550 |
| Inventario | $2{,}7\times7900$ | 21 330 |
| Contratación | $10\times120$ | 1 200 |
| Horas extra, despidos, faltantes | 0 | 0 |
| **Total $z$** | | **4 062 000** |

**Valores marginales de las ecuaciones** (columna `MARGINAL` del `.lst`; «EPS» es un marginal igual a 0 en una base degenerada):

| $t$ | `INVNETO1` | `INVNETO2` | `WORKFORCE` | `PRODUCTION` |
|---|---|---|---|---|
| 1 | — (ver `INVINICIAL`) | — (ver `INVINICIALHAND`) | — (ver `WFINICIAL`) | −6.9 |
| 2 | −89.6 | −2.7 | −7.6 | −9.6 |
| 3 | −92.3 | −2.7 | −10.0 | −12.3 |
| 4 | −95.0 | EPS | −9.7 | −15.0 |
| 5 | −95.0 | EPS | −6.7 | −15.0 |
| 6 | −95.0 | EPS | −3.7 | −15.0 |
| 7 | −95.0 | EPS | −0.7 | −15.0 |
| 8 | −95.0 | EPS | 2.3 | −15.0 |
| 9 | −95.0 | EPS | 5.3 | −15.0 |
| 10 | −95.0 | EPS | 8.3 | −15.0 |
| 11 | −95.0 | 17.3 | 11.3 | −15.0 |
| 12 | −77.7 | 77.7 | 14.3 | 2.3 |

Ecuaciones escalares: `FO` = 1.0; `INVINICIAL` = −86.9 (nivel 400); `INVINICIALHAND` = −2.7; `WFINICIAL` = −2.5 (nivel 2880).

**Costos reducidos de las variables** (marginales de las variables; P, LR y NI tienen marginal 0 en todos los periodos):

| $t$ | `I` | `S` | `LO` | `Wplus` | `Wminus` | `OUTSOURCE` |
|---|---|---|---|---|---|---|
| 1 | 0 | 10 002.7 | 11.1 | 10.0 | 37.0 | 8.1 |
| 2 | 0 | 10 002.7 | 8.4 | 2.4 | 44.6 | 5.4 |
| 3 | 0 | 10 002.7 | 5.7 | 0 | 47.0 | 2.7 |
| 4 | 2.7 | 10 000.0 | 3.0 | 0.3 | 46.7 | 0 |
| 5 | 2.7 | 10 000.0 | 3.0 | 3.3 | 43.7 | 0 |
| 6 | 2.7 | 10 000.0 | 3.0 | 6.3 | 40.7 | 0 |
| 7 | 2.7 | 10 000.0 | 3.0 | 9.3 | 37.7 | 0 |
| 8 | 2.7 | 10 000.0 | 3.0 | 12.3 | 34.7 | 0 |
| 9 | 2.7 | 10 000.0 | 3.0 | 15.3 | 31.7 | 0 |
| 10 | 2.7 | 10 000.0 | 3.0 | 18.3 | 28.7 | 0 |
| 11 | 20.0 | 9 982.7 | 3.0 | 21.3 | 25.7 | 0 |
| 12 | 80.4 | 9 922.3 | 20.3 | 24.3 | 22.7 | 17.3 |

**Interpretación** (deducida de la estructura de costos; un re-cálculo propio con otro solver, HiGHS, da el mismo $z=4\,062\,000$ y los mismos niveles):

- **Costo por unidad de cada fuente.** Una unidad en tiempo regular cuesta $80+12=92$, en horas extra $80+18=98$ y subcontratada $95$. Por eso nunca se usan horas extra, porque subcontratar es 3 más barato. El costo reducido de `LO` en los meses 4 a 11 es justamente 3.
- **Nivel de fuerza de trabajo.** Las horas regulares suben una sola vez, de 2880 a 3000 en el mes 3 ($W^+_3=120$), y se quedan ahí. El modelo no tiene horas ociosas ($P_t=L^R_t+L^O_t$), así que toda hora regular se convierte en producción. Con 3000 h, el mes 12 (demanda 3000) queda cubierto exactamente.
  - Tener más fuerza de trabajo en los meses 4 a 11 ahorraría solo $95-92=3$ por hora y por mes.
  - En cambio, contratar y luego despedir cuesta $10+37=47$ por hora, o bien obliga a sobreproducir en el mes 12.
  - Con 8 meses disponibles el ahorro máximo es $3\times8=24<47$, así que no conviene.
- **Excedente inicial.** El inventario inicial de 3000 más la producción forzada de 2880 en los meses 1 y 2 superan la demanda. Ese excedente se consume hasta llegar a 0 en el mes 4: $3000+2880-2600=3280$, $3280+2880-3400=2760$, $2760+3000-3900=1860$ y $1860+3000-5300=-440$, faltante que se cubre con 440 subcontratadas.
- **Subcontratación.** Del mes 4 al 11 se subcontrata exactamente $D_t-3000$, en total 7890 unidades. No hay faltantes.
- **Precios sombra de la demanda.** El marginal de `INVNETO1` (−95 en los meses 4 a 11) dice que una unidad más de demanda en esos meses cuesta 95, lo mismo que subcontratarla. En los meses 1, 2 y 3 cuesta $95-2{,}7\times(4-t)$, es decir 86.9, 89.6 y 92.3, porque se atiende con inventario que ya no hay que guardar y se subcontrata una unidad más en el mes 4.
- **Por qué contratar en el mes 3 y no en el 4.** El costo reducido de `Wplus(4)` es 0.3. Producir las 120 h en el mes 3 y guardarlas un mes cuesta $92+2{,}7=94{,}7$, frente a 95 si se subcontratan en el mes 4.

**Comparación con L11 p. 11.** La solución de la clase no tiene subcontratación. Esa solución:
- sube la fuerza de trabajo a 3700 h en el mes 2;
- usa horas extra en los meses 4 a 9 y 400 h de ocio en los meses 11 y 12;
- termina con 1800 de inventario.

El modelo GAMS da otro plan porque permite subcontratar a 95, no tiene horas de ocio ni inventario de seguridad y penaliza los faltantes con 10 000 en lugar de $\infty$. Ver [L11](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md).

**Archivos auxiliares**
- `modelo-flujo.log` es la bitácora de consola del IDE: parámetros de GAMS, licencia demo, compilación y generación del modelo, iteración del dual («Dual objective = 288126.000000»), «LP status (1): optimal» y «Objective: 4062000.000000».
- `modelo-flujo.lxi` es texto (no binario). Cada línea tiene un tipo, la línea del `.lst` donde está la sección y su nombre: B = bloque (Compilation, Equation Listing, Column Listing, Range Statistics, Model Statistics, Solution Report, Execution); D = ecuaciones del listado; E = columnas; F = ecuaciones de la solución; G = variables de la solución; I = `display`. Solo sirve para navegar el `.lst` en el IDE.

### Observaciones sobre el modelo GAMS

- El inventario inicial (3000) y las horas iniciales (2880) están escritos directamente en las ecuaciones en lugar de declararse como parámetros.
- `Wplus("1")` y `Wminus("1")` solo aparecen en la función objetivo, porque `WORKFORCE` empieza en $t=2$. Por eso valen 0.
- No hay límite superior para las horas extra ni para la subcontratación. Tampoco hay inventario final ni inventario de seguridad: las restricciones adicionales de L11 p. 10 no están implementadas.
- El escalar `h` no tiene descripción y `Cutso` es «costo outsourcing».
- `S(T)` se llama «faltantes», pero como $NI_t$ puede ser negativo y se arrastra al periodo siguiente, en realidad modela **backlog** con costo $c_F=10\,000$ por unidad y periodo.
- El `.lst` y el `.log` contienen rutas locales absolutas del equipo donde se ejecutó, así como datos de la licencia demo de GAMS.

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado principal |
|---|---|---|
| Agregación de 6 modelos (Nahmias, 2007) | [L10 pp. 30-31](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md) | Producto promedio: 5,06 h-h y \$415,02; 1168 unidades; 5910 h-h |
| Agregación de productos de cuero y de acero | L10 pp. 32-33 | Solo enunciado (sin solución) |
| Método gráfico, 6 meses, 6200 unidades en 124 días | L10 pp. 37-47 | Tasa nivelada 50 unid/día; inventario total 1850 |
| Estrategia 1: fuerza constante (10 trabajadores) | L10 pp. 45-46 | \$108 450 (91,5 % mano de obra) |
| Estrategia 2: 38/día + subcontratar 1488 | L10 p. 48 | **\$105 152** (la más barata) |
| Estrategia 3: contratar y despedir | L10 p. 49 | \$117 800 |
| Modelo de Bowman: 2 productos, 4 meses, regular 160 h y extra 40 h | L10 pp. 55-67; [modelo-bowman.md](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-bowman.md); [ejemplo-modelo-bowman.md](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/ejemplo-modelo-bowman.md) | Demanda agregada neta 64, 158, 194, 180 y 80 de inventario final. Plan de 116, 160, 200 y 200 h (extra solo en los meses 3 y 4). **Costo mínimo \$8144**. Los Excel dan una asignación distinta a la de la diapositiva con el mismo costo (óptimos alternativos). |
| Desagregación del plan de Bowman | L10 p. 68 | A = 116, 55, 98, 136; B = 0, 262, 255, 160 |
| Plan agregado de 12 meses con fuerza de trabajo y subcontratación (GAMS) | [modelo-flujo-gams/](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/) (sección anterior) | $z=4\,062\,000$. 2880 h en los meses 1-2 y 3000 h desde el mes 3; subcontrata 7890 unidades en los meses 4-11; sin horas extra ni faltantes; inventario de 3280, 2760 y 1860 en los meses 1-3 |

## Relación con otros temas y proyectos

- **Antes:** los pronósticos que alimentan el plan vienen del [Corte 1](/corte-1-pronosticos/).
- **Siguiente tema:** [02-agregacion-y-desagregacion](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/README.md).
  - [L11](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md) presenta el modelo con fuerza de trabajo y backlog que implementa el `.gms`.
  - Los Excel [modelo-desagregacion](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion.md) y [modelo-desagregacion-v2](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion-v2.md) desagregan por producto el plan que da este modelo GAMS: 2880, 2880 y luego 3000, con inventario total de 7900.
- **Después:**
  - [03-wagner-whitin-y-silver-meal](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/README.md): tamaño de lote.
  - [04-bom-y-mrp](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/): el plan maestro alimenta el MRP.
  - [05-mrp-ii-y-capacidad](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/): MRP II y capacidad.
- **Evaluación:** [parcial-2](/corte-2-planeacion-agregada-mrp/parcial-2/README.md) incluye la formulación de un modelo de planeación agregada (pregunta 1.2) y la evaluación de planes de persecución o nivelado.
- **Proyecto:** [proyecto-thyms-gemelo-digital](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/README.md). Según su presentación, aplica Bowman y el modelo de flujo al caso THYMS, aunque sus archivos no incluyen esos modelos.


---

<!-- fuente: corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md -->
# L10-aggregate-planning

> **Archivo:** [`L10-aggregate-planning.pdf`](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.pdf) · **Corte 2** · 74 páginas  
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

- [modelo-bowman.md](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-bowman.md) y [ejemplo-modelo-bowman.md](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/ejemplo-modelo-bowman.md) resuelven en Excel con Solver el ejemplo de las pp. 55-67. Llegan al mismo costo de \$8144 con una asignación distinta, pero igual de óptima.
- [modelo-flujo-gams/](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/) contiene el modelo de flujo con fuerza de trabajo, horas extra y subcontratación, que es la generalización del modelo de Bowman. Está explicado en el [README](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/README.md) de esta carpeta.
- La continuación de esta clase es [L11: agregación y desagregación](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md), con el modelo de PL con fuerza de trabajo y backlog, y la desagregación.
- El plan agregado alimenta el MRP: ver [BOM y MRP](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/) y [MRP II y capacidad](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/).
- Los pronósticos de entrada vienen del [Corte 1](/corte-1-pronosticos/).


---

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


---

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


---

<!-- fuente: corte-2-planeacion-agregada-mrp/04-bom-y-mrp/README.md -->
# BOM y MRP (Corte 2)

## Qué cubre

Planeación de requerimientos de materiales (MRP) para productos con demanda dependiente: lista de materiales (BOM) como árbol y como matriz, niveles, explosión de partes con $dd(n)=d_n\times B$ y tabla MRP por periodo. La tabla tiene requerimientos brutos, entregas programadas, inventario esperado, requerimientos netos y liberación de órdenes desplazada por el *lead time*. También trata el dimensionamiento de lotes, el MRP de ciclo cerrado y el nerviosismo. Incluye el ejemplo de clase (productos 1 y 2) y un MRP en Excel de un esfero.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [L13-bom-intro-to-mrp.md](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md) | Presentación (26 pp.): propósito y limitaciones del MRP, BOM (bolso, bicicleta, carro), matriz BOM, niveles y demanda dependiente directa. | 1.º |
| [L14-mrp.md](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md) | Presentación (21 pp.): tabla MRP completa de 9 ítems y 9 semanas, *lot sizing*, MRP de ciclo cerrado y nerviosismo. | 2.º |
| [calculo-demanda-dependiente-directa.md](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/calculo-demanda-dependiente-directa.md) | Excel: explosión del BOM de clase para 80 y 50 unidades, nivel por nivel (`MMULT`) y con $(I-B)^{-1}$ (`MINVERSE`). Venía de la carpeta del Corte 3. | 3.º |
| [mrp-esfero.md](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero.md) | Excel, 1.ª versión del MRP del esfero: producto final completo y tres borradores de componentes sin enlazar. | 4.º |
| [mrp-esfero-v2.md](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero-v2.md) | Excel, 2.ª versión: 6 ítems (Esfero, Cuerpo, Tapa Arriba, Tapa, Cilindro, Mina de Tinta) enlazados por el BOM, con *lead time* y costos por ítem. | 5.º |

**Diferencia entre las dos versiones del esfero.** Ambas tienen el mismo bloque del producto final (demanda de 10 semanas, LT = 3, liberaciones 610, 1230 y 1250 en las semanas 1, 3 y 5, costo 549.5). En la v1, los componentes son tres bloques copiados del esfero (mismo título, LT = 3, requerimientos escritos a mano) con faltantes o sin resolver. En la v2, cada componente tiene nombre, su propio *lead time* (2, 1, 0, 0, 0), requerimientos brutos calculados con el BOM (`=D7`, `=2*D7`, `=D14`) y sus propios costos. Esfero, Cuerpo y Tapa Arriba quedan factibles; Tapa, Cilindro y Mina quedan a medio resolver. Tabla comparativa completa al final de [mrp-esfero.md](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero.md#diferencias-con-mrp-esfero-v2xlsx).

## Orden de estudio sugerido

1. [L13](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md), pp. 1-12: qué es el MRP, entradas y limitaciones.
2. [L13](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md), pp. 13-26: BOM, matriz, niveles y $dd(n)=d_n\times B$.
3. [calculo-demanda-dependiente-directa](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/calculo-demanda-dependiente-directa.md): la misma explosión en Excel, hasta el último nivel.
4. [L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md), pp. 1-12: tabla MRP nivel por nivel del ejemplo de clase.
5. [mrp-esfero](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero.md) y luego [mrp-esfero-v2](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero-v2.md): la tabla MRP construida en Excel.
6. [L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md), pp. 13-21: *lot sizing*, ciclo cerrado y nerviosismo; después, [Wagner-Whitin y Silver-Meal](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/README.md).

## Conceptos y fórmulas clave

- Matriz BOM: $B=(b_{ij})$, con $b_{ij}$ = unidades del ítem $j$ para hacer **directamente** una unidad del ítem $i$ ([L13](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md), p. 13).
- Nivel de un ítem = número máximo de pasos de ensamble hasta un producto final; se planea del nivel 0 hacia abajo ([L13](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md), p. 20).
- Demanda dependiente directa: $dd(n)=d_n\times B$; demanda total $=d\,(I-B)^{-1}$ ([L13](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md), p. 23; [Excel](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/calculo-demanda-dependiente-directa.md)).
- Inventario esperado al inicio del periodo: $I_{jt}=\max\{0,\ I_{j,t-1}+S_{j,t-1}-G_{j,t-1}\}$ ([L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md), p. 5).
- Requerimiento neto: $N_{jt}=\max\{0,\ G_{jt}-S_{jt}-I_{jt}\}$ ([L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md), p. 6).
- Liberación de una orden: en $t-LT_j$ para recibir en $t$; la liberación del padre en $t$, multiplicada por la cantidad del BOM, es el requerimiento bruto del hijo en $t$.
- EOQ: $Q^*=\sqrt{2DK/h}$ ([L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md), p. 14).

Símbolos: $G$ requerimiento bruto, $S$ entregas programadas, $I$ inventario esperado, $N$ requerimiento neto, $LT$ *lead time*, $D$ demanda, $K$ costo de ordenar, $h$ costo de mantener.

### BOM del ejemplo de clase (L13 y L14)

| Ítem | Nivel | Hijos (cantidad por unidad) | Lead time | Inventario inicial |
|---|---|---|---|---|
| 1 | 0 | A (2), C (1) | 1 | 120 |
| 2 | 0 | D (1), B (1), γ (3) | 1 | 85 |
| A | 1 | B (1), α (2) | 2 | 0 |
| D | 1 | B (2), C (1) | 2 | 10 |
| B | 2 | C (2), γ (1) | 1 | 500 |
| C | 3 | α (1), β (3) | 1 | 160 |
| γ | 3 | parte | 2 | 0 |
| α | 4 | parte | 1 | 1200 |
| β | 4 | parte | 2 | 4000 |

### BOM del esfero (deducido de mrp-esfero-v2)

| Ítem | Nivel | Padre (cantidad) | Lead time | Inventario inicial |
|---|---|---|---|---|
| Esfero | 0 | producto final | 3 | 1200 (+500 programadas en la semana 1) |
| Cuerpo | 1 | Esfero (1) | 2 | 700 |
| Tapa Arriba | 1 | Esfero (2) | 1 | 1300 |
| Tapa | 1 | Esfero (1) | 0 | 0 |
| Cilindro | 2 | Cuerpo (1) | 0 | 0 |
| Mina de Tinta | 2 | Cuerpo (1) | 0 | 0 |

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado principal |
|---|---|---|
| Demanda dependiente directa con $d=(100, 200)$ | [L13](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md), pp. 24-26 | A = 200, D = 200, B = 200, C = 100, γ = 600 (primer orden) |
| Explosión completa con $d=(80, 50)$ | [calculo-demanda-dependiente-directa](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/calculo-demanda-dependiente-directa.md) | Totales: A 160, D 50, B 310, C 750, γ 460, α 1070, β 2250 |
| MRP de 9 ítems y 9 semanas | [L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md), pp. 3-12 | Liberaciones: 1 → 120 (s3, s7); 2 → 100 (s3, s7); A → 240, 240, 15 (s1, s5, s6); D → 100, 10, 100 (s1, s2, s5); B → 575 (s4), 100 (s8); C → 120, 1250, 320 (s2, s3, s6); γ → 300, 575, 300, 100 (s1, s2, s5, s6); β → 2000 (s1); α ninguna |
| Nerviosismo (A τ=0 → 2 B τ=3) | [L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md), pp. 19-20 | Subir A de 55 a 60 deja a B en −10 sin poder corregirlo, por su *lead time* de 3 |
| MRP del esfero, producto final | [mrp-esfero](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero.md) y [v2](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero-v2.md) | Liberar 610, 1230, 1250 en las semanas 1, 3, 5; costo 549.5 |
| MRP del esfero, componentes | [mrp-esfero-v2](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero-v2.md) | Cuerpo 1140 y 1250 (s1, s3), costo 195.2; Tapa Arriba 2380 y 2500 (s1, s3), costo 83.4; Tapa, Cilindro y Mina incompletos |

## Relación con otros temas y proyectos

- [03 Wagner-Whitin y Silver-Meal](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/README.md): cómo dimensionar las liberaciones de órdenes. `wagner_whitin.py` toma como demanda los requerimientos netos de la Tapa Arriba de mrp-esfero-v2 (deducido).
- [05 MRP II y capacidad](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md): agrega la verificación de capacidad (CRP) y el ciclo cerrado que el MRP no considera.
- [01 Planeación agregada](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/) y [02 Agregación y desagregación](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/): de ahí sale el programa maestro (MPS), que es la entrada del MRP.
- [Parcial 2](/corte-2-planeacion-agregada-mrp/parcial-2/parcial-2-solucion.md): punto 2.3 (matriz MRP lote a lote) y 2.4 (lot sizing).
- [Corte 3, scheduling](/corte-3-programacion-scheduling/): el MRP no programa máquinas ni horas ([L13](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md), p. 11); eso se ve en el Corte 3.


---

<!-- fuente: corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md -->
# L13-bom-intro-to-mrp

> **Archivo:** [`L13-bom-intro-to-mrp.pdf`](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.pdf) · **Corte 2** · 26 páginas  
> **Nombre original:** `CORTE 2/Lec 13 - BOM intro to MRP.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** introducción al MRP (*Material Requirements Planning*): demanda dependiente, lista de materiales (BOM), matriz BOM, asignación de niveles y cálculo de la demanda dependiente directa con $dd(n)=d_n\times B$.

### Ideas clave

- El MRP sirve para productos con cientos de componentes: reduce inventarios, evita paradas por falta de materia prima (mejor servicio al cliente, alta utilización de planta) y responde rápido a cambios del mercado (p. 2).
- **Propósito** (p. 4): calcular cuándo producir o comprar los componentes y materias primas del producto terminado para cumplir el plan de producción, minimizando el inventario en proceso (WIP).
- Es un sistema de **inventario dependiente**: más eficiente que los modelos de inventario independiente (EOQ) y reacciona mejor ante picos de demanda; evolucionó hacia los ERP (p. 5). Con puntos de reorden, los componentes y materias primas se mantienen en inventario todo el tiempo; con MRP solo aparecen justo antes de que se necesiten (p. 6).
- **Entradas** (pp. 8 y 10): programa maestro de producción (MPS: qué y cuándo), BOM, disponibilidad de inventarios, órdenes de compra en curso y *lead times*. Como cambian con frecuencia, hay que re-optimizar "moderadamente" seguido.
- **Limitaciones** (p. 11): planea materiales pero no programa (no dice en qué máquina ni a qué hora) y no considera restricciones de capacidad (eso lo agrega el MRP II, [carpeta 05](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/)).
- Tipos de ítems (p. 12): producto terminado (*e*), subensambles (*s*) y partes (*p*). La **explosión de partes** recorre la BOM de arriba hacia abajo.
- El **nivel** de un ítem es el número máximo de pasos de ensamble que lo separan de un producto final; se planea del nivel más alto (0) al más bajo (p. 20).
- Reglas para una buena BOM (p. 21): no usar unidades de volumen, peso o longitud (usar porciones), no mostrar procesos ni operaciones, no mostrar herramientas ni maquinaria, y alinear los ítems iguales en el mismo nivel.

### Fórmulas y métodos

- **Vector BOM de un ítem** (p. 13): $B^i=(b_{i1}, b_{i2}, \dots, b_{ij})$, donde $b_{ij}$ es el número de unidades del ítem $j$ requeridas para hacer **directamente** una unidad del ítem $i$.
- **Matriz BOM**: $B=\begin{pmatrix}B^1\\ B^2\\ \vdots\\ B^n\end{pmatrix}$ (fila = padre, columna = hijo).
- **Demanda dependiente directa** (p. 23): $dd(n)=d_n\times B$, donde $d_n$ es el vector (fila) de demanda en el nivel $n$ y $dd(n)$ el vector de demanda que resulta directamente en los ítems hijos. Se aplica nivel por nivel.
- *Complemento deducido, no está en las diapositivas:* la demanda total (todos los niveles) es $d\,(I+B+B^2+\dots)=d\,(I-B)^{-1}$; así lo calcula el Excel [calculo-demanda-dependiente-directa](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/calculo-demanda-dependiente-directa.md).

### BOM del ejemplo de clase (pp. 14-20)

Ítems: productos terminados 1 y 2; subensambles A, D, B y C; partes γ, α y β. Cantidades por unidad del padre (las que no llevan número son 1):

| Padre | Hijos (cantidad) | Nivel del padre |
|---|---|---|
| 1 | A (2), C (1) | 0 |
| 2 | D (1), B (1), γ (3) | 0 |
| A | B (1), α (2) | 1 |
| D | B (2), C (1) | 1 |
| B | C (2), γ (1) | 2 |
| C | α (1), β (3) | 3 |
| γ, α, β | (partes compradas) | γ: 3; α, β: 4 |

Los *lead times* y los inventarios de estos ítems aparecen en la [L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md) (p. 3).

### Ejemplos resueltos

- **Roscoe Crossbody** (p. 9): BOM en formato de tabla de un bolso, con código, parte, descripción, cantidad por unidad y especificación para tres SKU.
- **Bicicleta** (p. 18): BOM de 3 niveles (Bike → manubrio, ensamble del marco y sillín; ensamble del marco → 2 ruedas y 1 marco; rueda → 25 radios y 1 rin; marco → 3 pies de tubo de aluminio y 0.5 gal de pintura). Usa unidades de longitud y volumen, justo lo que la regla 1 de la p. 21 pide evitar.
- **Carro** (p. 22): árbol de 4 niveles (Carro → Sub2, MOT, 4 Sil; Sub2 → SUB1, C, PAI; SUB1 → CHA, 4 RUE, ELE; C → 6 MET).
- **Demanda dependiente directa** (pp. 24-26): con $d_0=(100, 200, 0,\dots,0)$ (producto 1 = 100, producto 2 = 200), $dd(0)=(0, 0, 200, 200, 200, 100, 600, 0, 0)$ en el orden (1, 2, A, D, B, C, γ, α, β): A = 200, D = 200, B = 200, C = 100, γ = 600. La p. 26 advierte que "hace falta" calcular los requerimientos de los niveles siguientes. *Deducido* con $d_0(I-B)^{-1}$, la demanda total sería A = 200, D = 200, B = 800, C = 1900, γ = 1400, α = 2300, β = 5700.

### Páginas clave

- pp. 2-5: qué es y para qué sirve el MRP; p. 6: puntos de reorden contra MRP; p. 7: ERP / SAP.
- pp. 8 y 10: entradas; p. 11: limitaciones.
- p. 9: BOM tabular (Roscoe Crossbody); p. 18: BOM de la bicicleta; p. 22: BOM del carro.
- pp. 13-20: explosión de partes, diagramas, matriz BOM y niveles.
- pp. 23-26: demanda dependiente directa y ejemplo numérico.

### Relación con otros archivos del repo

- [L14 MRP](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md): continúa con este mismo BOM (1, 2, A, D, B, C, γ, α, β), agrega inventarios, *lead times* y el MPS, y arma la tabla MRP completa.
- [calculo-demanda-dependiente-directa](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/calculo-demanda-dependiente-directa.md): Excel con la misma matriz BOM, la explosión $dd(n)$ nivel por nivel y la inversa $(I-B)^{-1}$.
- [mrp-esfero](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero.md) y [mrp-esfero-v2](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero-v2.md): MRP de un esfero hecho en clase.
- [L15 MRP II](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md): agrega la capacidad que el MRP no considera.


---

<!-- fuente: corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md -->
# L14-mrp

> **Archivo:** [`L14-mrp.pdf`](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.pdf) · **Corte 2** · 21 páginas  
> **Nombre original:** `CORTE 2/Lec 14 - MRP.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** construcción de la tabla MRP nivel por nivel para el BOM de la [L13](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md) (productos 1 y 2; ítems A, D, B, C, γ, α, β), con inventario disponible, *lead times* y MPS de 9 semanas. Luego se tratan el dimensionamiento de lotes, el MRP de ciclo cerrado y el nerviosismo del sistema.

### Ideas clave

- **Sistema MRP** (p. 2): MPS + BOM + archivo de estado del inventario → lógica MRP → programa de producción MRP.
- La tabla MRP de cada ítem tiene cinco filas por periodo: requerimientos brutos $G_{jt}$, entregas programadas $S_{jt}$, inventario esperado $I_{jt}$ (disponible al inicio del periodo), requerimientos netos $N_{jt}$ y liberación de órdenes planeadas (= recepción necesaria desplazada hacia atrás un *lead time*).
- **Procedimiento** (p. 10): (1) calcular la demanda directamente dependiente de cada periodo y cada producto con $dd(n)=d_n\times B$, usando las **liberaciones de órdenes** del nivel superior; (2) sumarla a los requerimientos brutos de los hijos (junto con su demanda independiente del MPS); (3) repetir hasta el último nivel. El requerimiento bruto de un hijo en la semana $t$ sale de las órdenes que liberan sus padres en esa semana $t$.
- Un ítem que aparece en varios niveles (B, C, γ, α) se planea **una sola vez**, en su nivel más bajo, después de todos sus padres.
- **Liberación de órdenes = problema de optimización (*lot sizing*)** (pp. 13-14): lote a lote (si ordenar cuesta poco), EOQ determinístico (supone demanda constante), Wagner-Whitin y Silver-Meal ([carpeta 03](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/README.md)).
- **MRP de ciclo cerrado** (pp. 15-16): cada módulo realimenta a los anteriores (por ejemplo, si se excede la capacidad o hay faltantes de inventario).
- **Nerviosismo** (pp. 17-21): pequeños cambios en el MPS (niveles altos) generan grandes cambios en los niveles bajos (efecto cascada). Es más sensible cuanto más cerca de la fecha actual. Se mitiga con stock de seguridad, *lead time* de seguridad o congelando el MPS, a costa de más inventario y de planes que no coinciden con lo que realmente se necesita.

### Fórmulas y métodos

Para el ítem $j$ en el periodo $t$:

- Inventario esperado al inicio del periodo (p. 5):
$$I_{jt}=\max\{0,\ I_{j,t-1}+S_{j,t-1}-G_{j,t-1}\}$$
- Requerimiento neto (p. 6):
$$N_{jt}=\max\{0,\ G_{jt}-S_{jt}-I_{jt}\}$$
- Liberación: una recepción necesaria en $t$ se libera en $t-LT_j$.
- Demanda dependiente directa (pp. 7 y 11): $dd(n)=d_n\times B$, con $d_n$ el vector de **liberaciones** del periodo y $B$ la matriz BOM de la L13.
- EOQ (p. 14): $Q^*=\sqrt{\dfrac{2DK}{h}}$, con $D$ la demanda por periodo, $K$ el costo de ordenar y $h$ el costo de mantener una unidad por periodo.

$G_{jt}$: requerimiento bruto; $S_{jt}$: entregas (recepciones) programadas; $I_{jt}$: inventario esperado al inicio de $t$; $N_{jt}$: requerimiento neto; $LT_j$: *lead time* del ítem $j$.

### Datos del ejemplo (pp. 3-4)

| Nivel | Ítem | Inventario a la mano ($t=0$) | Lead time | Padres (cantidad por padre, de la L13) |
|---|---|---|---|---|
| 0 | 1 | 120 | 1 | producto final |
| 0 | 2 | 85 | 1 | producto final |
| 1 | A | 0 | 2 | 1 (×2) |
| 1 | D | 10 | 2 | 2 (×1) |
| 2 | B | 500 | 1 | 2 (×1), A (×1), D (×2) |
| 3 | C | 160 | 1 | 1 (×1), D (×1), B (×2) |
| 3 | γ | 0 | 2 | 2 (×3), B (×1) |
| 4 | α | 1200 | 1 | A (×2), C (×1) |
| 4 | β | 4000 | 2 | C (×3) |

MPS (demanda independiente) en semanas 1 a 9: producto 1 = 50, 20, 30, 40, 40, 30, 25, 15, 30; producto 2 = 20, 30, 25, 35, 10, 35, 20, 25, 30; A = 15 en la semana 8; D = 10 en las semanas 2 y 4; B = 20 en la semana 5 y 100 en la semana 9; C = 5 en la semana 2.

### Ejemplos resueltos

- **MRP nivel 0** (pp. 5-6): producto 1, requerimientos netos 10 (sem. 8) y 30 (sem. 9), liberaciones de 120 en las semanas 3 y 7; producto 2, requerimientos netos 15 y 30, liberaciones de 100 en las semanas 3 y 7.
- **Explosión semana 7** (pp. 7-8): $dd(0)=(120, 100, 0, \dots, 0)\times B=(0, 0, 240, 100, 100, 120, 300, 0, 0)$, es decir A = 240, D = 100, B = 100, C = 120, γ = 300.
- **Explosión semana 5** (p. 11): $dd(1)=(0, 0, 240, 100, 0, \dots, 0)\times B$ da B = 440, C = 100 y α = 480.
- **MRP completo** (p. 12): liberaciones planeadas finales: 1 → 120 (s3), 120 (s7); 2 → 100 (s3), 100 (s7); A → 240 (s1), 240 (s5), 15 (s6); D → 100 (s1), 10 (s2), 100 (s5); B → 575 (s4), 100 (s8); C → 120 (s2), 1250 (s3), 320 (s6); γ → 300 (s1), 575 (s2), 300 (s5), 100 (s6); α → ninguna (el inventario alcanza, termina en 320); β → 2000 (s1).
- **Nerviosismo** (pp. 19-20): si la demanda de A en el periodo 2 sube de 55 a 60, la orden de A del periodo 1 pasa de 90 a 95. El requerimiento bruto de B sube de 180 a 190 y su inventario queda en −10 en los periodos 3 y 4. *Deducido:* B no se puede pedir porque su *lead time* es τ = 3: para recibir en el periodo 3 habría que haber pedido en el periodo 0, que ya pasó.

### Páginas clave

- p. 3: estado de inventario y *lead times*; p. 4: MPS.
- pp. 5-6: tabla MRP de nivel 0 y fórmulas $I_{jt}$, $N_{jt}$.
- pp. 7-11: explosión nivel por nivel y procedimiento.
- p. 12: **tabla MRP final de los 9 ítems**.
- pp. 13-14: *lot sizing*; pp. 15-16: ciclo cerrado; pp. 17-21: nerviosismo.

### Observaciones sobre el material

- La tabla de la p. 12 no coincide del todo con el estado de inventario de la p. 3: D empieza en 0 (no en 10) y tiene entregas programadas de 10, 100 y 10; B empieza en 0 (no en 500) con 560 programadas en la semana 1; C empieza en 0 (no en 160) con 115 programadas en la semana 1; α empieza en 3000 (no en 1200). Con los datos de la p. 3 algunos números cambiarían.
- No se dice qué regla de tamaño de lote se usa. *Deducido* de los números: A, D y γ van lote a lote; B agrupa las semanas 5-7 (460 + 15 + 100 = 575) y C agrupa 4-5 (1150 + 100 = 1250) y 7-8 (120 + 200 = 320); los productos 1 y 2 piden 120 y 100 aunque el neto sea 40 y 45; β pide 2000 para cubrir 110 + 960.
- Las recepciones de las órdenes planeadas no se suman al inventario esperado (por ejemplo, la orden de 120 del producto 1 en la semana 7 no aparece en la semana 8). Las filas de inventario y neto solo consideran las entregas programadas.
- p. 11: el vector resultado tiene 8 componentes, "(0 0 0 0 440 100 480 0)". Con los 9 ítems (1, 2, A, D, B, C, γ, α, β) es $(0, 0, 0, 0, 440, 100, 0, 480, 0)$: el 480 corresponde a α.
- p. 9 se titula "MRO hasta nivel 1" (errata de "MRP").

### Relación con otros archivos del repo

- [L13 BOM e intro al MRP](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md): matriz BOM y niveles usados aquí.
- [calculo-demanda-dependiente-directa](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/calculo-demanda-dependiente-directa.md): la misma explosión $d\times B$ en Excel.
- [mrp-esfero](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero.md) y [mrp-esfero-v2](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero-v2.md): la tabla MRP con las mismas fórmulas $I_{jt}$ y $N_{jt}$, armada en Excel ("CONSTRUIR EXCEL", p. 10).
- [Wagner-Whitin y Silver-Meal](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/L12-wagner-whitin-and-silver-meal.md): políticas de dimensionamiento de lotes.
- [L15 MRP II](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md): MRP de ciclo cerrado y capacidad.
- [Parcial 2](/corte-2-planeacion-agregada-mrp/parcial-2/parcial-2-solucion.md): punto 2.3, matriz MRP.


---

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


---

<!-- fuente: corte-2-planeacion-agregada-mrp/parcial-2/README.md -->
# Parcial 2: planeación agregada y MRP (Corte 2)

## Qué cubre

Este es el examen del Corte 2, con su rúbrica y su solucionario completo. Tiene dos puntos:

- **Punto 1, Sales and Operations Planning** (Muebles Andinos S.A.S., familia de escritorios, sillas y archivadores): agregación en horas estándar, modelo de programación lineal entera, comparación de planes de persecución y nivelado, y desagregación por igual tiempo de agotamiento.
- **Punto 2, MRP** (mesa auxiliar M): árbol de materiales y códigos de nivel bajo, demanda dependiente con netos, matrices MRP lote a lote y la heurística Silver-Meal frente a Wagner-Whitin.

El examen dura 2 horas, se hace en papel y solo admite calculadora no programable.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [parcial-2-solucion.md](/corte-2-planeacion-agregada-mrp/parcial-2/parcial-2-solucion.md) (gemelo de `parcial-2-solucion.pdf`, 13 págs.) | Enunciado (pp. 1–6), rúbrica (pp. 6–7) y solucionario (pp. 7–13), transcritos completos con todas las tablas. Incluye una verificación propia con el Plan C y el óptimo de Wagner-Whitin | Sí |

## Orden de estudio sugerido

1. Repasar los temas antes de resolver:
   - [L10](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md), planeación agregada;
   - [L11](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md), agregación y desagregación;
   - [L12](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/L12-wagner-whitin-and-silver-meal.md), Silver-Meal y Wagner-Whitin;
   - [L13](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md) y [L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md), BOM y MRP.
2. Leer el enunciado en [parcial-2-solucion.md](/corte-2-planeacion-agregada-mrp/parcial-2/parcial-2-solucion.md) (páginas 1 a 6) e intentar resolverlo sin mirar la solución.
3. Comparar con el solucionario (páginas 7 a 13) y con la sección «Verificación propia» del resumen.
4. Revisar la rúbrica (páginas 6–7). Las preguntas marcadas [Argumente] reparten el puntaje mitad cálculo y mitad argumento.

## Conceptos y fórmulas clave

El detalle está en [parcial-2-solucion.md](/corte-2-planeacion-agregada-mrp/parcial-2/parcial-2-solucion.md#resumen).

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

Todos están en [parcial-2-solucion.md](/corte-2-planeacion-agregada-mrp/parcial-2/parcial-2-solucion.md).

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

- [01-planeacion-agregada-modelo-bowman](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/): el modelo de costos y la formulación de la pregunta 1.2.
- [02-agregacion-y-desagregacion](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/): agregación en horas estándar y desagregación por tiempo de agotamiento (preguntas 1.1 y 1.4).
- [03-wagner-whitin-y-silver-meal](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/): lot sizing (pregunta 2.4); [wagner_whitin.py](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/wagner_whitin.py) sirve para comprobar el óptimo.
- [04-bom-y-mrp](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/): BOM, código de nivel bajo, demanda dependiente y matriz MRP (preguntas 2.1 a 2.3).
- [05-mrp-ii-y-capacidad](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/): MRP II y capacidad, tema posterior que no entra en este parcial.
- [proyecto-thyms-gemelo-digital](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/): el proyecto del Corte 2, que aplica planeación agregada y MRP a un caso real.


---

<!-- fuente: corte-2-planeacion-agregada-mrp/parcial-2/parcial-2-solucion.md -->
# parcial-2-solucion

> **Archivo:** [`parcial-2-solucion.pdf`](/corte-2-planeacion-agregada-mrp/parcial-2/parcial-2-solucion.pdf) · **Corte 2** · 13 páginas  
> **Nombre original:** `CORTE 2/Parcial 2 – Planeación, Programación y Control de la Producción Solucion.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** enunciado, rúbrica y solucionario completo del Parcial 2 (Corte 2): planeación agregada (S&OP), formulación lineal entera, evaluación de planes persecución/nivelado, desagregación por tiempo de agotamiento, BOM y códigos de nivel bajo, demanda dependiente, matriz MRP y dimensionamiento de lotes (Silver-Meal frente a Wagner-Whitin).

**Ideas clave**

- El parcial tiene dos puntos con datos independientes. **Punto 1** (Muebles Andinos S.A.S., familia de 3 muebles: escritorio, silla y archivador): agregación, modelo PLE, planes A/B/C y desagregación. **Punto 2** (mesa auxiliar M): BOM, demanda dependiente, MRP lote a lote y Silver-Meal.
- La unidad agregada correcta es la **hora estándar** del recurso restrictivo (mano de obra polivalente), no la suma de unidades.
- El costo regular es fijo por operario (se paga la jornada completa): $160 \times 20.000 = 3.200.000$ por operario-mes, por eso el objetivo usa $W_t$ y no $P_t$.
- La subcontratación ($38.000/h) nunca conviene porque la hora extra ($30.000/h) es más barata y su límite nunca se alcanza.
- La desagregación por **igual tiempo de agotamiento** usa los inventarios y deja a toda la familia cubierta hasta el mismo instante; repartir en proporción a la demanda deja agotamientos desiguales.
- El MRP procesa por **código de nivel bajo**: K aparece en los niveles 1 y 2 y se procesa en el 2, después de M y de S. Los requerimientos de un hijo salen de las **liberaciones planeadas** (netas) de sus padres.
- Silver-Meal es miope: se detiene en el primer mínimo local del costo por periodo. Wagner-Whitin es óptimo para un horizonte fijo, pero genera nerviosismo con horizonte rodante.
- Rúbrica con dos indicadores: (1) identifica elementos y (2) evalúa alternativas. Niveles de 100 %, 75 %, 40 % y 0–10 %. En las preguntas [Argumente], el cálculo vale el 50 % y el argumento el otro 50 %.

**Fórmulas y métodos**

- **Demanda agregada en horas estándar:** $D_t=\sum_i k_i\,d_{i,t}$, donde $k_i$ son las horas estándar por unidad del producto $i$ (2,0; 1,5; 3,0) y $d_{i,t}$ su demanda en unidades. Se usa cuando los productos comparten recursos y se mide la carga del recurso restrictivo.
- **Unidades equivalentes:** $D_t / k_{\text{ref}}$; con escritorios, $k_{\text{ref}}=2$ h.
- **Modelo de planeación agregada (PLE entera).** Los símbolos son: $W_t$ operarios; $H_t$ contratados; $F_t$ despedidos; $P_t$ horas regulares; $O_t$ horas extra; $S_t$ horas subcontratadas; $I_t$ inventario final en horas estándar; $D_t$ demanda en horas.

$$\min Z=\sum_{t=1}^{4}\left(3\,200\,000\,W_t+30\,000\,O_t+38\,000\,S_t+1\,500\,000\,H_t+2\,500\,000\,F_t+2\,000\,I_t\right)$$

  sujeto a:
  - $I_t=I_{t-1}+P_t+O_t+S_t-D_t$;
  - $W_t=W_{t-1}+H_t-F_t$;
  - $P_t\le 160W_t$;
  - $O_t\le 32W_t$;
  - $I_0=0$, $W_0=16$;
  - $P_t,O_t,S_t,I_t\ge0$ y $W_t,H_t,F_t\in\mathbb{Z}_{\ge0}$.
- **Costo de un plan:** $\sum_t\left(3\,200\,000\,W_t+30\,000\,O_t+2\,000\,I_t+1\,500\,000\,H_t+2\,500\,000\,F_t\right)$.
- **Tiempo de agotamiento común (desagregación).**
  - $T^*=\dfrac{X+\sum_i I_i}{\sum_i d_i}$.
  - $Y_i=T^*d_i-I_i$, en horas; las unidades son $Y_i/k_i$.
  - Tiempo de agotamiento de un ítem: $RO_i=(I_i+Y_i)/d_i$.
  - Símbolos: $X$ horas aprobadas para la familia; $I_i$ inventario del producto $i$ en horas; $d_i$ demanda del periodo en horas.
- **Explosión con netos (demanda dependiente):** $RB_{\text{hijo}}=\sum_{\text{padres}}q_{\text{padre,hijo}}\cdot RN_{\text{padre}}$ y $RN=\max(0,\,RB-I)$, donde $q$ es la cantidad por padre.
- **Registro MRP lote a lote.** Símbolos: $RB_t$ brutos; $RP_t$ recepciones programadas; $IP_t$ inventario proyectado; $RN_t$ netos; $ROP_t$ recepción de órdenes planeadas; $LOP_t$ liberación de órdenes planeadas; $LT$ tiempo de entrega.
  - $RN_t=\max(0,\,RB_t-IP_{t-1}-RP_t)$.
  - $ROP_t=RN_t$.
  - $IP_t=IP_{t-1}+RP_t+ROP_t-RB_t$.
  - $LOP_{t-LT}=ROP_t$.
  - Brutos del hijo: $RB^{\text{hijo}}_t=\sum q\cdot LOP^{\text{padre}}_t$.
- **Silver-Meal.** Costo por periodo de un pedido en la semana $j$ que cubre hasta la $k$:

$$C(j,k)=\frac{S+h\sum_{t=j}^{k}(t-j)\,D_t}{k-j+1}$$

  Se amplía $k$ mientras $C(j,k+1)\le C(j,k)$; cuando sube, se cierra el lote y se empieza uno nuevo en $k+1$. Aquí $S$ es el costo de ordenar, $h$ el costo de mantener por unidad y semana y $D_t$ el requerimiento neto.
- **Wagner-Whitin** (programación dinámica): $f(k)=\min_{1\le j\le k}\left\{f(j-1)+S+h\sum_{t=j}^{k}(t-j)D_t\right\}$, con $f(0)=0$. Da el óptimo para un horizonte fijo.

**Ejemplos resueltos (con su resultado)**

| Pregunta | Página(s) | Resultado |
|---|---|---|
| 1.1a Demanda agregada | 7 | 2400, 2560, 3200 y 2880 h estándar (meses 1 a 4) |
| 1.1b Escritorios equivalentes del mes 3 | 7 | 3200 / 2 = 1600 escritorios |
| 1.1c Sumar unidades | 7 | No sirve: 1550 muebles pueden ser de 2325 h a 4650 h |
| 1.2 Modelo PLE | 7–8 | Modelo completo; enteras $W_t$, $H_t$, $F_t$ |
| 1.3 Plan A (persecución) | 8 | Operarios 15, 16, 20, 18; contrata 5 y despide 3; total **$235.800.000** |
| 1.3 Plan B (nivelado, 16 operarios) | 8 | Extra 0, 0, 480 y 320 h; inventario 160, 160, 0 y 0; total **$229.440.000** |
| 1.3c Recomendación | 9 | El solucionario dice «Plan B» (ver observación 2) |
| 1.4a Desagregación de 2620 h | 9 | $T^*=1{,}2$ meses: 500 escritorios, 400 sillas y 340 archivadores |
| 1.4b Reparto proporcional | 9 | 491, 437 y 327,5 u; agotamientos de 1,18, 1,29 y 1,16 meses: se recomienda igual tiempo de agotamiento |
| 2.1 BOM y LLC | 9 | LLC: M = 0, T = 1, S = 1, K = 2, P = 2 |
| 2.2 Demanda dependiente (200 mesas) | 10 | Netos: M 180, T 150, S 130, P 420, K 380; el auxiliar compra 380 patas y 220 kits de más |
| 2.3 MRP de M | 10–11 | Liberaciones: 30 (sem. 2), 60 (sem. 4), 40 (sem. 5), 70 (sem. 7) |
| 2.3 MRP de S | 11 | Liberaciones: 20 (sem. 3), 40 (sem. 4), 70 (sem. 6) |
| 2.3 MRP de K | 12 | Brutos 0, 30, 40, 140, 40, 140, 70, 0; liberaciones: 100 (sem. 3), 40 (sem. 4), 140 (sem. 5), 70 (sem. 6) |
| 2.4 Silver-Meal | 13 | Pedidos: 310 u (sem. 1), 350 u (sem. 4) y 200 u (sem. 6); costo **$1.390.000** |

**Verificación propia de los cálculos (agregada al transcribir; no está en el PDF)**

- Rehíce todas las tablas del solucionario: agregación, planes A y B, desagregación, explosión, matrices MRP de M, S y K, y Silver-Meal. Los números coinciden.
- **Plan C (cálculo propio):** 17 operarios dan 2720 h por mes.

| Mes | Demanda (h) | Regular (h) | Extra (h) | Inventario final (h) |
|---|---|---|---|---|
| 1 | 2400 | 2720 | 0 | 320 |
| 2 | 2560 | 2720 | 0 | 480 |
| 3 | 3200 | 2720 | 0 | 0 |
| 4 | 2880 | 2720 | 160 | 0 |

  Costos del Plan C:
  - Regular: 10 880 h, $217.600.000.
  - Extra: 160 h, $4.800.000.
  - Inventario: 800 h·mes, $1.600.000.
  - Una contratación: $1.500.000.
  - **Total: $225.500.000.**

  Plan C es el más barato: $3.940.000 menos que B y $10.300.000 menos que A. Su hora extra máxima es 160 h, por debajo del límite de 544 h, así que es factible.
- **Wagner-Whitin para 2.4 (cálculo propio, en miles de pesos):** $f(1)=300$, $f(2)=380$, $f(3)=540$, $f(4)=780$, $f(5)=1080$ y $f(6)=1280$.
  - Plan óptimo: 230 u en la semana 1 (cubre 1–2), 180 u en la semana 3 (cubre 3–4) y 450 u en la semana 5 (cubre 5–6).
  - Costo: **$1.280.000**, $110.000 menos que Silver-Meal (8,6 %). Confirma la afirmación del solucionario («unir 3 con 4 y 5 con 6»).

**Observaciones (errores e inconsistencias del documento)**

1. La portada dice «Valor: 100 puntos (nota = puntos / 20)», pero la tabla de distribución suma **110 puntos**: 10 + 20 + 20 + 12 + 5 + 10 + 18 + 15.
2. **1.3c:** el solucionario dice «Se recomienda el Plan B: ahorra dinero» y lo justifica con un argumento que favorece al Plan C («contratar un operario reemplaza 640 h de extra, que costaban $19.200.000»). Tampoco calcula el costo del Plan C, que es el más barato ($225.500.000, ver arriba). Además, el argumento compara $1.500.000 de contratación con $19.200.000 de horas extra y omite la nómina adicional: 4 × $3.200.000 = $12.800.000, más $960.000 de inventario adicional. Con todo, el ahorro neto de C frente a B es de $3.940.000. Lo más probable es que la recomendación debiera ser el Plan C.
3. **2.1:** el solucionario incluye un literal c) (por qué importa el código de nivel bajo) que no aparece en el enunciado; el enunciado solo tiene a) y b).
4. **2.4:** el título y la tabla de puntos dicen «Silver-Meal vs. Wagner-Whitin», pero el enunciado solo pide calcular Silver-Meal. Wagner-Whitin aparece únicamente en el argumento b), sin números.
5. **1.4b:** las unidades se redondean de forma desigual: 491,25 → 491 y 436,7 → 437, mientras 327,5 se deja fraccional.
6. **Página 8:** las fórmulas del modelo están en el PDF como código LaTeX sin renderizar.
7. El árbol del BOM (2.1a) se pide dibujado, pero el solucionario solo da la tabla de niveles; no hay diagrama.

**Páginas clave**

| Páginas | Contenido |
|---|---|
| 1–2 | Instrucciones y tabla de puntos |
| 2–3 | Datos del Punto 1 (Tablas 1 y 2) |
| 3–4 | Preguntas 1.1 a 1.4 |
| 4–6 | Punto 2: BOM, Tabla 3, MPS, Tabla 4, datos de 2.4 |
| 6–7 | Rúbrica y criterios |
| 7–13 | Solucionario: 1.1–1.2 en pp. 7–8; 1.3 en pp. 8–9; 1.4 y 2.1 en p. 9; 2.2 en p. 10; 2.3 en pp. 10–12; 2.4 en pp. 12–13 |

**Relación con otros archivos del repo**

- Planeación agregada y modelo de costos:
  - [L10 Aggregate planning](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md);
  - [modelo-bowman](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-bowman.md);
  - [ejemplo-modelo-bowman](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/ejemplo-modelo-bowman.md).
- Agregación y desagregación (tiempo de agotamiento):
  - [L11](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md);
  - [modelo-desagregacion](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion.md);
  - [modelo-desagregacion-v2](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion-v2.md).
- Silver-Meal y Wagner-Whitin:
  - [L12](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/L12-wagner-whitin-and-silver-meal.md);
  - [wagner_whitin.py](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/wagner_whitin.py).
- BOM, LLC y MRP:
  - [L13](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md);
  - [L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md);
  - [calculo-demanda-dependiente-directa](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/calculo-demanda-dependiente-directa.md);
  - [mrp-esfero](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero.md).
- MRP II (capacidad), tema posterior que no entra en el parcial: [L15](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md).


---

<!-- fuente: corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/README.md -->
# Proyecto THYMS, Corte 2: S&OP y gemelo digital (Corte 2)

## Qué cubre

Segunda entrega del proyecto del semestre sobre **THYMS Colombia S.A.S.**, que fabrica tintes para el cabello en tubos de 60 g:
- A: Kolorezza permanente;
- B: Visalia sin amoníaco;
- C: Thym's Coloring permanente.

El grupo:
1. armó un libro con todos los parámetros de la planta, el estudio preliminar (takt, cycle time, throughput, WIP, restricciones) y el **plan agregado** de 12 meses (persecución, nivelada y mixta);
2. corrigió el pronóstico del Corte 1;
3. construyó un **gemelo digital** de la planta en Python/SimPy con sensores virtuales, escenarios y pruebas de estrés;
4. en la versión MEJORADO, conectó el gemelo con el plan agregado (S&OP).

### Enunciado o entregable (deducido de los archivos)

No hay enunciado escrito en la carpeta. Según [`CONTEXTO_GEMELO_THYMS.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/CONTEXTO_GEMELO_THYMS.md) y la presentación, el entregable pedía:
1. un **estudio preliminar** del sistema: WIP, takt time, throughput, cycle time y restricciones de capacidad, demanda y almacenamiento;
2. un **gemelo digital en ARENA o Python** que incluya el pronóstico, la estacionalidad y sensores virtuales;
3. la presentación del plan de ventas y operaciones (S&OP).

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [`CONTEXTO_GEMELO_THYMS.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/CONTEXTO_GEMELO_THYMS.md) | Documento de traspaso escrito antes de esta conversión (estado al 2026-10-05): proyecto, archivos, mapa de celdas del libro, clases del gemelo, resultados, advertencias y supuestos abiertos. Ya era Markdown; no tiene binario | Sí (1.º) |
| [`THYMS-presentacion-corte-2.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/THYMS-presentacion-corte-2.md) | Presentación del grupo (PDF de 9 páginas, 6 de octubre de 2026): resultados y mejoras en una vista | Sí (2.º) |
| [`Datos Thyms Completo.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Datos%20Thyms%20Completo.md) | Libro de 14 hojas: parámetros, productos, tiempos, utilización, alistamientos, fallas, mano de obra, métricas, plan agregado, restricciones, proceso, facturas, clientes y ventas | Sí (3.º) |
| [`Gemelo_Digital_Thyms.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md) | Cuaderno base (36 celdas, con salidas): revisión del pronóstico, pronóstico a 12 meses, gemelo en SimPy, validación, métricas, restricciones, escenarios y estrés | Sí (4.º) |
| [`Gemelo_Digital_Thyms_MEJORADO.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms_MEJORADO.md) | Cuaderno principal (45 celdas): el base sin cambios + sección 4 (S&OP agregado mensual) + sección 5 (gemelo guiado por el plan frente al de punto de reorden). Las celdas nuevas no tienen salidas guardadas | Sí (5.º) |

**Base frente a MEJORADO:**
- Las celdas 0–35 son idénticas en código y salidas (comprobado comparando los dos `.ipynb`).
- MEJORADO agrega las celdas 36–44:
  - `cargar_plan_agregado()` lee la hoja `Plan Agregado`;
  - `simular_gemelo_sop()` simula mes a mes las estrategias de persecución y nivelada con demanda aleatoria y venta perdida;
  - la clase `GemeloThymsSOP` hereda del gemelo y libera lotes según el plan mensual (lazo abierto) con una demanda dada;
  - `comparar_modelos()` corre 5 modelos con la misma demanda en 30 réplicas.

## Orden de estudio sugerido

1. [`CONTEXTO_GEMELO_THYMS.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/CONTEXTO_GEMELO_THYMS.md): el mapa completo.
2. [`THYMS-presentacion-corte-2.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/THYMS-presentacion-corte-2.md): las conclusiones que se presentaron.
3. [`Datos Thyms Completo.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Datos%20Thyms%20Completo.md): los datos y el plan agregado en Excel.
4. [`Gemelo_Digital_Thyms.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md): pronóstico y gemelo (secciones 1 a 3).
5. [`Gemelo_Digital_Thyms_MEJORADO.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms_MEJORADO.md): secciones 4 y 5.

## Datos

- **Planta** (libro, hojas `Parámetros` a `Mano de Obra`):
  - 22 días hábiles al mes, 2 turnos de 7 h de lunes a viernes;
  - lotes de 500 kg que rinden 7.800 tubos; 24 tubos por caja;
  - demanda base de 100.000 tubos/mes (A 48.000, B 30.000, C 22.000);
  - stock de producto terminado 29.500, bodega 58.000, puntos de reorden 8.000/5.500/4.500, lotes 15.600/7.800/15.600;
  - 6 estaciones con tiempos normales truncados;
  - OEE: llenadora 0,74, mezcla 0,85, encartonado 0,83 y supuestos de 0,88–0,90 para las demás;
  - alistamientos de 70, 155 y 300 min según el cambio;
  - MTBF/MTTR de 5 equipos;
  - 34 operarios.
- **Materia prima:** 3.600 kg de base y colorantes importados (lead time de 40 días) y 60.000 tubos vacíos.
- **Ventas reales** (del Corte 1): ventas mensuales de enero a agosto de 2026 en COP, de las que salen los índices estacionales (julio 1,53; abril 0,35), y 464 facturas de mayo a julio de 161 clientes, de las que sale el tamaño de pedido lognormal (media de 1,27 M COP ≈ 99 tubos).

## Métodos

- **Estudio preliminar** (Excel; $D_p$ = demanda mensual del producto $p$):
  - takt $= 308 \cdot 3.600 / D_p$;
  - utilización $= \sum_p D_p/(y_p\,\text{cap}_{e,p}) / (308 \cdot OEE_e)$;
  - ley de Little: tiempo de flujo = WIP / throughput.
- **Planeación agregada** (Excel, clases [L10](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md) y [L11](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md)):
  - demanda $D_t = 100.000\,s_t$;
  - persecución: $P_t = D_t$; nivelada: $P_t = \bar{D}$; mixta: $P_t = \alpha D_t + (1-\alpha)\bar{D}$;
  - inventario $I_t = I_{t-1} + P_t - D_t$;
  - capacidad $K_t = n_t \cdot 14 \cdot 1.675{,}47$;
  - desagregación 48/30/22 % y lotes $\lceil P_t/7.800 \rceil$.
- **Pronóstico** (cuaderno):
  - SES con origen móvil y $\alpha$ elegido por RMSE;
  - nivel inicial = promedio de 3 meses;
  - pronóstico de planta $N \cdot s_m$ con intervalo del 80 %.
- **Gemelo digital** (SimPy):
  - demanda Poisson + lognormal con choque mensual;
  - punto de reorden con revisión diaria;
  - recorrido del lote por 6 estaciones con 2 reactores;
  - fallas exponenciales en horas de marcha con reparación lognormal;
  - alistamientos dependientes de la secuencia;
  - pérdida de velocidad $OEE/A$;
  - rendimiento binomial;
  - materia prima con revisión periódica;
  - calendario con festivos de Colombia;
  - 16 sensores virtuales;
  - 30 réplicas con números aleatorios comunes.
- **S&OP + gemelo** (MEJORADO):
  - modelo agregado mensual con venta perdida;
  - gemelo que libera lotes según la cuota diaria del plan;
  - comparación con la misma demanda.

## Resultados principales

| Tema | Resultado |
|---|---|
| Escala | La serie de ventas real (~11.705 tubos/mes) es el **11,7 %** de la planta |
| Pronóstico del Corte 1 | Sesgo +63,1 M COP, señal de rastreo 4,72: subestima |
| Pronóstico corregido | SES α = 0,05 con nivel inicial = promedio de 3 meses: RMSE 63,6 M frente a 76,8 M (−17 %), sesgo 2,4 M frente a 44,6 M; nivel de **100.038 tubos/mes**, error mensual ±42 % |
| Utilización (libro) | Llenadora 28,3 % (cuello de botella); demás estaciones de 3 % a 14 % |
| Takt / throughput / flujo / WIP | Libro: 11,1 s; 325 tubos/h; 12,7–14,5 h; 8.500 tubos. Gemelo: 10,3 s; 352 tubos/h; 16,9 h; 5.308 tubos |
| Validación del gemelo | Balance de masa exacto; Little 5.472 = 366 × 14,95; horas de equipo dentro de ±0,7 % |
| Restricciones (gemelo) | Llenadora al 28,9 %; servicio 99,99 %; **C sobre su bodega el 32,3 % de los días**; materia prima mínima de 800 kg |
| Escenarios | Lote de C de 7.800 → 0 % de días sobre la bodega e inventario −10,3 %; un turno → 97,97 % de servicio; compras sin estacionalidad → 6 de 30 réplicas con faltante |
| Estrés | Servicio 99,4 % con 2× la demanda, 93,9 % con 2,5×, 70,8 % con 3×; el libro dice 3,37× porque no ve colas |
| Plan agregado (Excel) | Solo **persecución** es factible: costo de mantener 29,6 M COP; la nivelada excede la bodega 5 meses (pico de 96.346), la mixta 1 mes |
| Materia prima | Cobertura de 13 días frente a 55 requeridos; faltan **11.665 kg** |
| S&OP en el gemelo (MEJORADO) | Con la misma demanda: punto de reorden 99,99 % de servicio; plan de persecución a lazo abierto **79,42 %**; plan nivelado 84,99 % |

## Conceptos y fórmulas clave

- **Ley de Little:** $WIP = TH \times CT$, donde $TH$ es el throughput y $CT$ el tiempo de flujo. Se usa para validar el gemelo. Detalle en [`Gemelo_Digital_Thyms.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md).
- **Takt time:** $T_{takt} = T_{disponible}/D$. Ver la hoja `Métricas` en [`Datos Thyms Completo.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Datos%20Thyms%20Completo.md#hoja-métricas).
- **Capacidad efectiva con mezcla:** $\bar{c} = OEE \cdot \left(\sum_p w_p/c_p\right)^{-1}$ = 1.675,47 tubos/h, donde $w_p$ es la participación del producto y $c_p$ su capacidad de llenado.
- **Estrategias de plan agregado:** persecución, nivelada y mixta, con inventario $I_t = I_{t-1}+P_t-D_t$. Ver [`Datos Thyms Completo.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Datos%20Thyms%20Completo.md#hoja-plan-agregado).
- **Disponibilidad:** $A = MTBF/(MTBF+MTTR)$. La pérdida de velocidad que completa el OEE es $OEE/A$.
- **Pronosticador del gemelo:** $N \leftarrow \alpha\,D^{real}_m/s_m + (1-\alpha)N$ (SES sobre la demanda desestacionalizada; $N$ = nivel, $s_m$ = índice del mes).

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado principal |
|---|---|---|
| Utilización y cuello de botella | `Datos Thyms Completo`, hoja `Utilizacion` | Llenadora 28,3 % |
| Takt, cycle time, throughput y Little | Hoja `Métricas` | Takt de la familia 11,09 s; flujo 26,2 h; eficiencia de flujo 51 % |
| Plan agregado de 3 estrategias | Hoja `Plan Agregado` | Persecución factible, 29,6 M COP; nivelada 45,3 M y no factible |
| Revisión y elección del pronóstico | `Gemelo_Digital_Thyms`, sección 2 | SES α = 0,05 con nivel promedio; 100.038 tubos/mes |
| Gemelo base, escenarios y estrés | `Gemelo_Digital_Thyms`, sección 3 | Lote de C de 7.800 recomendado; aguanta ~2× la demanda |
| Plan agregado dentro del gemelo | `Gemelo_Digital_Thyms_MEJORADO`, secciones 4 y 5 | Lazo abierto da 79 % de servicio; debe liberar el punto de reorden |

## Supuestos abiertos

Pendientes de confirmar con la empresa (ver también la sección 9 de [`CONTEXTO_GEMELO_THYMS.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/CONTEXTO_GEMELO_THYMS.md)):
- **Escala zona → planta:** los índices estacionales y el nivel salen de un solo vendedor (11,7 % de la planta).
- **Jornada:** 1 turno de 8 h de lunes a sábado en el Corte 1, frente a 2 turnos de 7 h de lunes a viernes en el libro (el gemelo usa el libro).
- **Índices de septiembre a diciembre = 1** (no hay datos).
- **Materia prima en tránsito al inicio:** el stock cubre ~13 días frente a 40 de lead time; el gemelo supone pedidos ya en camino.
- **Supuestos propios del gemelo:** choque mensual del 10 %, CV de reparación de 0,5, sublotes de 600, revisión de compras cada 5 días; OEE de pesaje, control de calidad y empaque supuestos.
- **No modelado:** mano de obra, tubos vacíos y cartón, capacidad de bodega impuesta, reprocesos y estrategia mixta en simulación.
- Las secciones 4 y 5 leen valores calculados del Excel (rompen la regla de «solo datos de entrada») y no tienen salidas guardadas.
- Los resultados de Bowman, flujo en red, MILP de turnos y programa maestro que muestra la presentación (páginas 6–7) no están en ningún archivo de esta carpeta.

## Cómo se conecta con el Corte 1

| Corte 1 ([proyecto-thyms-pronostico](/corte-1-pronosticos/proyecto-thyms-pronostico/)) | Corte 2 (esta carpeta) |
|---|---|
| `VENTAS.xls`: ventas mensuales de 2026 y 464 facturas | Copiadas en las hojas `Ventas` y `Facturas Mayo-Julio`; dan los índices estacionales y la distribución del tamaño de pedido |
| SES α = 0,05 con $F_1$ = enero: MAD 80,2 M, MAPE 53,4 %, agosto 114,7 M | Sección 2.1: se reproduce y se muestra el sesgo (+63,1 M, señal de rastreo 4,72); la sección 2.2 lo corrige con nivel inicial = promedio de 3 meses |
| 12.900 COP/tubo | Se mantiene (`PRECIO_UND`) para pasar de COP a tubos y escalar a la planta (×8,54) |
| Takt 0,69 min (41,5 s), throughput 86,7 tubos/h, WIP 304–477 (zona, 8 h/día) | Sección 3.5: comparados con el libro (11,1 s; 325; 8.500) y el gemelo (10,3 s; 352; 5.308) |
| Tiempo de ciclo de 3,5–5,5 h (dato de la empresa) | Coherente con pesaje + mezcla + control de calidad = 3,9–5,0 h por lote |
| Días hábiles con festivos (cuaderno de Colab) | Calendario de festivos de Colombia programado (`festivos_colombia()`) |

## Relación con otros temas y proyectos

- Planeación agregada y modelo de Bowman (la presentación dice haberlo aplicado a THYMS): [01-planeacion-agregada-modelo-bowman](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/).
- Agregación y desagregación (tubos, kg, horas-hombre; plan por producto): [02-agregacion-y-desagregacion](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/).
- Siguiente paso propuesto (dimensionar lotes del programa maestro): [03-wagner-whitin-y-silver-meal](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/).
- Materia prima con lead time y MRP: [04-bom-y-mrp](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/) y [05-mrp-ii-y-capacidad](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/).
- Pronósticos (SES, señal de rastreo, estacionalidad): [04-datos-estacionarios-promedio-movil-y-suavizacion-simple](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/) y [06-estacionalidad-winters-y-tracking-signal](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/).
- Métricas de desempeño (takt, throughput, WIP, Little): [L02](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L02-introduction-to-production-systems.md).


---

<!-- fuente: corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md -->
# Gemelo_Digital_Thyms

> **Archivo:** [`Gemelo_Digital_Thyms.ipynb`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.ipynb) · **Corte 2** · Cuaderno Jupyter con 36 celdas  
> **Nombre original:** `CORTE 2/Gemelo_Digital_Thyms.ipynb`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

### Qué es

Cuaderno **base** del proyecto del Corte 2 sobre THYMS Colombia S.A.S. (creado el 2026-10-01; 36 celdas, todas ejecutadas con salidas guardadas, Python 3.12). Hace tres cosas:
1. revisa y corrige el pronóstico del Corte 1;
2. construye un pronóstico de planta a 12 meses con estacionalidad;
3. implementa un **gemelo digital** de la planta como simulación de eventos discretos en **SimPy**, con sensores virtuales, validación, métricas de eficiencia, restricciones y escenarios.

Lee **solo datos de entrada** de [`Datos Thyms Completo.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Datos%20Thyms%20Completo.md) y recalcula en Python lo que en el libro son fórmulas.

La versión [`Gemelo_Digital_Thyms_MEJORADO.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms_MEJORADO.md) tiene estas mismas 36 celdas (código y salidas idénticos) y agrega las secciones 4 y 5. El documento de traspaso [`CONTEXTO_GEMELO_THYMS.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/CONTEXTO_GEMELO_THYMS.md) describe el cuaderno con más detalle (mapa de celdas, clases y funciones).

### Estructura

| Celdas | Sección | Qué hace |
|---|---|---|
| 0–2 | Título · 1. Configuración y datos | Librerías: math, datetime, numpy, pandas, matplotlib, scipy.stats, openpyxl, simpy |
| 3 | Configuración | Supuestos editables, colores, estilo de gráficos y funciones `es()` (números en formato español) y `tabla()` |
| 4–5 | Carga | `cargar_datos()` lee del libro parámetros, productos, tiempos, OEE, alistamientos, fallas, ventas y facturas, y muestra la tabla de productos |
| 6 | Escala | Compara la venta real promedio con la demanda de planta → escala zona → planta |
| 7–8 | 2.1 Revisión del Corte 1 | `ses()` y `metricas()` (MAD, RMSE, MAPE, sesgo, señal de rastreo); reproduce el SES del Corte 1 |
| 9–11 | 2.2 Elección del método | Prueba de tendencia; 7 métodos comparados con **origen móvil**; búsqueda de $\alpha$ por RMSE |
| 12–14 | 2.3 Pronóstico a 12 meses | Nivel × índice estacional, intervalo del 80 %, tabla y gráfica |
| 15–16 | 2.4 Pronosticador del gemelo | Clase `Pronosticador` y parámetros lognormales del tamaño de pedido |
| 17 | 3.1 Qué representa | Diagrama del flujo y tabla de cómo se modela cada elemento |
| 18 | Calendario | `pascua()`, `festivos_colombia()` (con ley Emiliani), `dias_habiles()` |
| 19–20 | 3.2 El modelo | `CFG_BASE`, `lognormal_media()`, clases `Maquina` y `GemeloThyms`, función `replicar()` |
| 21–22 | 3.3 Validación | Balance de masa, ley de Little y horas de equipo frente al libro |
| 23–28 | 3.4 Corrida base con sensores | Telemetría horaria, modo «en vivo», gráfica de inventario y gráfica de una semana de la llenadora |
| 29–30 | 3.5 Métricas de eficiencia | Takt, throughput, tiempo de flujo y WIP: Corte 1 frente a libro frente a gemelo |
| 31–32 | 3.6 Restricciones | Capacidad, demanda, almacenamiento y materia prima, con intervalo del 95 % |
| 33–35 | 3.7 Escenarios | 6 escenarios y prueba de estrés con factor de demanda de 1 a 3,5 |

### Datos que usa

- **Libro `Datos Thyms Completo.xlsx`:**
  - parámetros (22 días/mes, 2 turnos de 7 h, 7.800 tubos/lote, 24 tubos/caja);
  - productos (demanda 48.000/30.000/22.000, rendimiento, stock, bodega, punto de reorden, lote, materia prima);
  - lead time de la materia prima (40 días);
  - tiempos (promedio, desviación y rango);
  - OEE, alistamientos, MTBF/MTTR;
  - ventas de enero a agosto de 2026 en COP;
  - las 464 facturas (COP por pedido).
- **Supuestos de la celda 3:**
  - `PRECIO_UND` = 12.900 COP/tubo;
  - índices de septiembre a diciembre = 1;
  - `CV_CHOQUE_MENSUAL` = 0,10;
  - horizonte de septiembre de 2026 a agosto de 2027 (`INICIO`, `MESES` = 12);
  - `SUBLOTE` = 600 tubos;
  - `KG_LOTE` = 500;
  - `CV_MTTR` = 0,5;
  - `SS_MP_DIAS` = 15;
  - `REVISION_MP_DIAS` = 5;
  - `N_REP` = 30 réplicas, `SEMILLA` = 2026.

### Métodos

**Pronóstico.**
- SES: $F_{t+1} = \alpha y_t + (1-\alpha)F_t$, donde $y_t$ es la venta del mes $t$.
- Métricas ($e_t = y_t - F_t$): MAD, $RMSE = \sqrt{\frac{1}{n}\sum e_t^2}$, MAPE, sesgo $= \bar{e}$ y señal de rastreo $TS = \sum e_t/MAD$.
- Tendencia: regresión lineal con valor p (`scipy.stats.linregress`).
- **Origen móvil:** con los meses $1..k$ se pronostica el mes $k+1$, para $k = 3..7$ (5 pronósticos fuera de muestra).
- $\alpha$: rejilla de 0,05 a 0,95 minimizando el RMSE.
- Pronóstico de planta: $\hat{D}_m = N \cdot s_m$, con nivel $N$ en tubos de planta e índice $s_m = y_m/\bar{y}$ (meses 1 a 8; 1 en los demás).
- Intervalo del 80 %: $\hat{D}_m (1 \pm z_{0{,}90}\,\sigma_{rel})$, con $\sigma_{rel}$ = RMSE fuera de muestra / nivel.
- Escala: $\text{ESCALA} = 100.000 / (\bar{y}/12.900)$.

**Pronosticador dentro del gemelo.**
- Índice: $s'_m = 1 + w(s_m - 1)$, donde $w$ es el peso estacional.
- Actualización mensual: $N \leftarrow \alpha\,D^{real}_m/s'_m + (1-\alpha)N$.
- Tamaño de pedido: lognormal ajustada al logaritmo de las facturas.

**Gemelo digital** (eventos discretos; el reloj avanza en horas de turno, 1 día hábil = 14 h, de lunes a viernes sin festivos de Colombia).
- **Demanda.** Cada mes la tasa diaria es demanda base × factor × índice × choque lognormal (CV 10 %) / días hábiles. Cada día:
  - número de pedidos ~ Poisson(tasa / pedido medio);
  - tamaño ~ lognormal (de las facturas) / 12.900;
  - lo que no hay en bodega queda pendiente (backorder).
- **Producción.**
  - Política de punto de reorden con revisión diaria: si la posición (PT + en proceso − pendientes) ≤ punto de reorden, se lanzan lotes de 7.800 tubos (A y C: 2 lotes; B: 1).
  - Recorrido del lote: materia prima (500 kg) → pesaje → reactor (2 en paralelo, con alistamiento según el cambio: tono, A↔C o con B) → mezcla → control de calidad → llenadora en 13 sublotes de 600 tubos → encartonado → empaque → tubos buenos ~ Binomial(600, rendimiento).
- **Tiempos:** normal truncada entre mínimo y máximo.
- **Máquinas** (clase `Maquina`):
  - estados libre, marcha, alistamiento y falla;
  - vida ~ Exponencial(MTBF), consumida solo en marcha;
  - reparación lognormal con media MTTR y CV 0,5;
  - pérdida de velocidad $= OEE / A$, con $A = MTBF/(MTBF+MTTR)$, para completar el OEE del libro.
- **Materia prima:**
  - revisión cada 5 días hábiles;
  - se pide hasta cubrir el consumo pronosticado en (lead time + 5 + 15) días hábiles, en múltiplos de 500 kg;
  - lead time de 40 días calendario ≈ 29 días hábiles;
  - se supone que al inicio ya hay pedidos en tránsito.
- **Sensores virtuales:** `lectura()` devuelve 16 variables (estado y velocidad de la llenadora con ruido del 1 %, contadores, estados de reactores, encartonadora y empaque, PT por producto, WIP, pendientes y materia prima). Se toma una lectura cada hora y también se puede avanzar paso a paso (`iniciar()` + `env.run`).
- **Réplicas:** 30 por escenario con números aleatorios comunes (semillas 2026 + i), con intervalo del 95 % $\pm t_{0{,}975;\,29}\,s/\sqrt{30}$.

### Resultados clave con números

**Escala (celda 6):** la venta real promedio es de 150.997.582 COP/mes = 11.705 tubos/mes, es decir, el **11,7 %** de la planta (100.000 tubos/mes); la escala es de unas 8,54 veces.

**2.1 Revisión del SES del Corte 1** ($\alpha$ = 0,05, arranca en enero, evaluado de febrero a julio):
- MAD = 80.172.875 COP;
- MAPE = 53,4 %;
- **sesgo = +63.063.608 COP** (subestima);
- **señal de rastreo = 4,72** (fuera de ±4);
- agosto: 114.671.388 pronosticado frente a 119.882.540 real.

**2.2 Comparación por origen móvil** (MAD, RMSE y sesgo en millones de COP). Tendencia: 6.741.938 COP/mes con valor p = 0,51, no significativa.

| Método | MAD | RMSE | MAPE | Sesgo | Señal de rastreo |
|---|---|---|---|---|---|
| **SES α = 0,05, nivel inicial = promedio de 3 meses (elegido)** | 54,7 | **63,6** | 56,3 % | 2,4 | 0,22 |
| Promedio histórico | 61,9 | 69,3 | 60,2 % | 8,6 | 0,69 |
| Promedio móvil (3) | 67,3 | 75,1 | 65,1 % | −1,9 | −0,14 |
| SES del Corte 1 (arranca en enero) | 65,2 | 76,8 | 47,3 % | 44,6 | 3,42 |
| Regresión lineal | 92,6 | 111,6 | 109,4 % | −31,8 | −1,72 |
| Ingenuo (último mes) | 104,0 | 111,9 | 101,5 % | −16,2 | −0,78 |
| Holt (α = 0,3; β = 0,3) | 106,7 | 127,5 | 126,1 % | −106,7 | −5,00 |

**2.3 Pronóstico a 12 meses.** Nivel = 151.055.237 COP/mes = **100.038 tubos/mes de planta**; error típico de un mes = 42 %.

| Mes | Índice | Pronóstico | Límite inferior (80 %) | Límite superior (80 %) |
|---|---|---|---|---|
| Sep, Oct, Nov y Dic 2026 | 1,00 | 100.038 | 46.038 | 154.038 |
| Ene 2027 | 0,63 | 63.437 | 29.194 | 97.681 |
| Feb 2027 | 1,02 | 101.928 | 46.908 | 156.949 |
| Mar 2027 | 1,33 | 133.168 | 61.285 | 205.052 |
| Abr 2027 | 0,35 | 34.747 | 15.991 | 53.503 |
| May 2027 | 1,31 | 130.836 | 60.212 | 201.461 |
| Jun 2027 | 1,04 | 103.737 | 47.740 | 159.733 |
| Jul 2027 | 1,53 | 153.027 | 70.424 | 235.631 |
| Ago 2027 | 0,79 | 79.424 | 36.551 | 122.297 |

El gráfico de la celda 14 muestra la venta real escalada a planta (gris, enero a agosto de 2026), el pronóstico estacional (azul) con su banda del 80 % y el nivel plano de 100.038 (línea naranja).

**2.4 Pedido promedio:** 1.273.304 COP ≈ 99 tubos.

**3.3 Validación** (demanda plana, sin choques ni materia prima):
- **balance de masa:** 29.500 + 1.234.289 − 1.224.545 = 39.244 = inventario final − pendientes;
- **ley de Little:** WIP de 5.472 = 366 tubos/h × 14,95 h;
- **horas de equipo**, libro frente a gemelo: pesaje 124/123 (−0,6 %), mezcla 494/496 (+0,5 %), control de calidad 188/188 (0,0 %), llenado 748/743 (−0,7 %), encartonado 504/502 (−0,4 %), empaque 541/544 (+0,7 %).

**3.4 Corrida base:**
- 3.431 lecturas horarias de 16 variables.
- En el modo en vivo, la llenadora arranca el 2026-09-02 a las 13:00 y llena un lote de B a ~1.420–1.560 tubos/h; el WIP baja de 7.800 a 0 hacia las 19:00.
- Gráfica de inventario (celda 27): A oscila entre ~7.000 y ~22.000 (bodega 26.000); B entre ~4.000 y ~13.000 (bodega 18.000); **C hace un diente de sierra que sube hasta ~19.000, por encima de su bodega de 14.000**, cada vez que entra un lote doble de 15.600.
- Gráfica de una semana de la llenadora (celda 28, desde el 09/09/2026): hay tramos de marcha a ~1.450–1.950 tubos/h, alistamientos antes de cada lote y una falla de ~3 h en la mitad de la semana; el resto del tiempo la máquina está libre.

**3.5 Métricas de eficiencia** (30 réplicas):

| | Corte 1 (zona, 8 h/día) | Libro (planta) | Gemelo (planta, 12 meses) |
|---|---|---|---|
| Takt time | 41,5 s/tubo (0,69 min) | 11,1 s/tubo | 10,3 s/tubo |
| Throughput | 86,7 tubos/h | 325 tubos/h | 352 tubos/h |
| Tiempo de ciclo (flujo) | 3,5 a 5,5 h (dato de la empresa) | 12,7 a 14,5 h por lote | 16,9 h por lote |
| WIP promedio | 304 a 477 tubos | 8.500 tubos | 5.308 tubos |

Pesaje + mezcla + control de calidad según el libro: 3,9 a 5,0 h por lote, coherente con las 3,5 a 5,5 h que dio la empresa.

**3.6 Restricciones** (promedio ± intervalo del 95 %):

| Tipo | Indicador | Valor |
|---|---|---|
| Capacidad | Ocupación de la llenadora (cuello de botella) | 28,9 % ± 0,4 |
| Capacidad | Ocupación de los reactores | 10,5 % ± 0,1 |
| Capacidad | Ocupación de la encartonadora | 16,0 % ± 0,2 |
| Capacidad | Ocupación del empaque | 15,4 % ± 0,2 |
| Demanda | Nivel de servicio (despacho inmediato) | 99,99 % ± 0,02 |
| Demanda | Mayor acumulado de pendientes | 0 tubos |
| Almacenamiento | Inventario total máximo | 49.226 ± 627 tubos (bodega de 58.000) |
| Almacenamiento | Días con la bodega total sobre su capacidad | 0,0 % |
| Almacenamiento | **Días con C sobre su bodega** | **32,3 % ± 1,1** |
| Materia prima | Menor existencia de base y colorantes | 800 ± 152 kg |

La causa del problema de C es que su punto de reorden + lote (20.100) es mayor que su bodega (14.000). En 3 de 30 réplicas algún lote esperó materia prima.

**3.7 Escenarios** (mismas semillas):

| Escenario | Servicio | Inventario promedio | Días C sobre bodega | Llenadora | Flujo por lote | Réplicas con faltante de MP |
|---|---|---|---|---|---|---|
| Base: política del libro | 99,99 % | 34.697 | 32,3 % | 28,9 % | 16,9 h | 3 |
| Sin estacionalidad | 100,00 % | 34.724 | 32,3 % | 29,0 % | 16,8 h | 0 |
| Punto de reorden ajustado con el pronóstico | 99,97 % | 36.740 | 36,9 % | 28,7 % | 17,1 h | 1 |
| Compras con pronóstico sin estacionalidad | 99,85 % | 34.627 | 32,1 % | 28,9 % | 16,9 h | 6 |
| **Lote de C de 7.800 tubos** | 99,96 % | **31.108** | **0,0 %** | 29,5 % | 16,1 h | 1 |
| Un solo turno | 97,97 % | 28.240 | 19,9 % | 57,5 % | 18,3 h | 1 |

**Prueba de estrés** (celda 35, punto de reorden ajustado con el pronóstico, sin materia prima; valores leídos de la gráfica):

| Factor de demanda | 1,0 | 1,5 | 2,0 | 2,5 | 3,0 | 3,5 |
|---|---|---|---|---|---|---|
| Ocupación de la llenadora | 28,7 % | 43,3 % | 57,9 % | 72,2 % | 85,9 % | 94,3 % |
| Nivel de servicio | 100,0 % | 99,9 % | 99,4 % | 93,9 % | 70,8 % | 43,9 % |

### Conclusiones

1. El SES del Corte 1 estaba **sesgado** por arrancar en enero. Con el nivel inicial igual al promedio de 3 meses (mismo $\alpha$ = 0,05), el sesgo baja de 44,6 a 2,4 millones COP y el RMSE un 17 %. La demanda de planta queda en ~100.000 tubos/mes, sin tendencia y con ±42 % de error mensual.
2. El gemelo está **validado**: cuadran el balance de masa y la ley de Little, y las horas de equipo quedan dentro de ±0,7 % del libro.
3. **La capacidad sobra:** la llenadora (cuello de botella) trabaja al ~29 %. La planta aguanta unas 2 veces la demanda con ≥ 99 % de servicio; el libro calcula 3,37 veces porque no considera colas ni variabilidad.
4. El problema real es la **bodega de C**. Bajar su lote a 7.800 tubos elimina los días sobre la bodega y reduce el inventario promedio un 10,3 %.
5. Las compras de materia prima deben usar el pronóstico **con** estacionalidad: sin ella, los faltantes de materia prima pasan de 3 a 6 réplicas.

### Supuestos y advertencias

- **Escala zona → planta** (11,7 %): los índices estacionales salen de un solo vendedor y se aplican a toda la planta.
- **Jornada:** el gemelo usa los 2 turnos de 7 h de lunes a viernes del libro; el Corte 1 suponía 1 turno de 8 h de lunes a sábado.
- **Índices de septiembre a diciembre = 1** (supuesto), y la estacionalidad se trata como escenario porque no se puede validar con un año incompleto.
- **El $\alpha$ óptimo (0,05) quedó en el extremo inferior de la rejilla:** el SES se comporta casi como el promedio histórico.
- Se supone que al inicio **ya hay materia prima en tránsito** (el stock de 3.600 kg cubre unos 13 días frente a 40 de lead time).
- Supuestos propios del gemelo: choque mensual del 10 %, CV de reparación de 0,5, sublotes de 600 tubos, revisión de compras cada 5 días.
- **No se modelan:**
  - mano de obra;
  - tubos vacíos ni cartón;
  - reprocesos (los defectuosos se descartan).
- La bodega **se mide, no se impone**: el inventario puede pasar la capacidad.
- La llenadora libera la máquina entre sublotes, pero la prioridad por orden de llegada hace que cada lote se llene completo antes del siguiente.
- La tabla de la celda 30 escribe a mano los valores del Corte 1 (41,5 s, 86,7 tubos/h, 304–477), no los recalcula.
- La prueba de estrés solo tiene salida gráfica; los números de arriba se leyeron de las etiquetas del gráfico.
- Para correrlo, el libro debe estar en la misma carpeta con el nombre `Datos Thyms Completo.xlsx` (ruta relativa en `ARCHIVO`).


---

<!-- fuente: corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms_MEJORADO.md -->
# Gemelo_Digital_Thyms_MEJORADO

> **Archivo:** [`Gemelo_Digital_Thyms_MEJORADO.ipynb`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms_MEJORADO.ipynb) · **Corte 2** · Cuaderno Jupyter con 45 celdas  
> **Nombre original:** `CORTE 2/Gemelo_Digital_Thyms MEJORADO.ipynb`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

### Qué es

**Cuaderno principal** del proyecto del Corte 2 sobre THYMS Colombia S.A.S. (45 celdas). Es el cuaderno base [`Gemelo_Digital_Thyms.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md) más dos secciones nuevas que conectan el gemelo digital con la **planeación agregada (S&OP)** de la hoja `Plan Agregado` de [`Datos Thyms Completo.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Datos%20Thyms%20Completo.md).

**Qué agrega exactamente frente al base:**
- Las **celdas 0 a 35 son idénticas** al cuaderno base: mismo código y mismas salidas guardadas (comprobado comparando el JSON de los dos `.ipynb`). Todo lo de las secciones 1 a 3 (pronóstico, gemelo, validación, métricas, restricciones, escenarios y estrés) está explicado en el resumen de [`Gemelo_Digital_Thyms.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md) y no se repite aquí.
- Las **celdas 36 a 44 son nuevas** (2 de Markdown y 7 de código):
  - la **sección 4** simula mes a mes el plan agregado de persecución y el nivelado con demanda aleatoria;
  - la **sección 5** mete ese plan dentro del gemelo detallado (liberación de lotes según el plan, a lazo abierto) y lo compara con el gemelo de punto de reorden, con **exactamente la misma demanda**.
- **Las celdas 36 a 44 no tienen salidas guardadas** (nunca se ejecutaron en el archivo). Los números de abajo vienen de una corrida aparte documentada en [`CONTEXTO_GEMELO_THYMS.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/CONTEXTO_GEMELO_THYMS.md), sección 7; la presentación [`THYMS-presentacion-corte-2.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/THYMS-presentacion-corte-2.md) (página 6) muestra los mismos resultados principales.
- Ninguna celda anterior cambia: la clase `GemeloThyms` se reutiliza por herencia.

### Estructura de las secciones nuevas

| Celda | Sección | Qué hace |
|---|---|---|
| 36 | 4. Gemelo digital guiado por el Plan Agregado (S&OP) | Markdown: se simulan persecución y nivelada con la misma semilla, es decir, con la misma demanda real |
| 37 | Carga del plan | `_norm()` quita tildes. `cargar_plan_agregado()` lee la hoja `Plan Agregado` con `pd.read_excel(header=None)`, busca los parámetros por texto en la columna A (inventario inicial, bodega, capacidad de la llenadora, horas por día, costo de mantener), ubica la fila «Mes» y las columnas de cada estrategia. Devuelve `df_plan` (Mes, Días hábiles, Demanda Plan, Prod persecucion, Prod nivelada, Prod mixta) y `PRM_SOP` |
| 38 | Simulación agregada | `simular_gemelo_sop(df_plan, estrategia, variabilidad_demanda=0.05, seed=42)`: un paso de SimPy por mes (ver métodos) |
| 39 | Corrida | `ESTRATEGIAS_SOP = ["Persecucion", "Nivelada"]`; tabla mensual de cada una y resumen anual |
| 40 | Gráfica | Inventario final de cada mes frente al límite de bodega (58.000), con los meses que la saturan marcados en rojo |
| 41 | 5. Comparación con la misma demanda | Markdown: tabla de los 5 modelos y supuestos (reparto 48/30/22 %, pedidos reescalados al total del mes, plan dividido por el rendimiento, calendario de enero a diciembre de 2026) |
| 42 | Gemelo guiado por el plan | `INICIO_PLAN` = 2026-01-01; clase `GemeloThymsSOP(GemeloThyms)`; funciones `kpis_gemelo()` y `kpis_agregado()`; lista `KPIS` |
| 43 | Comparación | `comparar_modelos(df_plan, n_rep=30)`, aviso de diferencia de días hábiles, tabla de promedio ± intervalo del 95 % y tabla «Mejor modelo» por KPI |
| 44 | Gráfica | (a) Inventario a fin de mes, promedio de réplicas, de los 5 modelos con el límite de bodega; (b) barras del costo anual de inventario de los 3 gemelos con su nivel de servicio |

### Datos que usa

- Todo lo de las secciones 1 a 3 (libro de Excel, pronóstico `PRON` y clase `GemeloThyms`).
- Hoja **`Plan Agregado`**, leída con `pd.read_excel`, es decir, los **valores calculados que Excel guardó** de las fórmulas:
  - demanda mensual de 63.413 a 152.969 (1.200.000 al año);
  - producción de persecución (= demanda) y nivelada (100.000/mes);
  - días hábiles por mes (246 al año);
  - inventario inicial 29.500, bodega 58.000, llenadora 1.675,47 tubos/h, 14 h/día, costo de mantener 83,56 COP/tubo-mes.

### Métodos

**Sección 4: modelo agregado mensual** (`simular_gemelo_sop`). Para cada mes $t$:
- demanda real: $\tilde{D}_t \sim \mathcal{N}(D_t, (0{,}05\,D_t)^2)$ truncada en 0;
- capacidad: $K_t = n_t \cdot 14 \cdot 1.675{,}47$;
- producción real: $P^{real}_t = \min(P^{plan}_t, K_t)$;
- inventario: $I_t = \max(0,\ I_{t-1} + P^{real}_t - \tilde{D}_t)$, es decir, **la venta no atendida se pierde**;
- desabastecimiento: $\max(0,\ \tilde{D}_t - I_{t-1} - P^{real}_t)$;
- saturación de bodega si $I_t > 58.000$;
- costo: $I_t \cdot 83{,}56$.

**Sección 5: gemelo guiado por el plan** (`GemeloThymsSOP`, que hereda de `GemeloThyms`):
- **Calendario:** pone la variable global `INICIO` en 2026-01-01 mientras se construye el objeto y la restaura con `try/finally`.
- **Demanda dada:**
  - la demanda mensual de la réplica se reparte en A, B y C (48/30/22 %);
  - se generan pedidos diarios con Poisson + lognormal (con su propio generador, semilla + 20.000) y se reescalan para que cada mes sume exactamente esa demanda;
  - sobrescribe `_demanda_del_dia`.
- **Producción:**
  - sin plan (`plan_prod=None`), usa el punto de reorden de siempre (lazo cerrado);
  - con plan, la cuota diaria es $P^{plan}_t \cdot w_p / n_t / y_p$ ($w_p$ = participación, $y_p$ = rendimiento). Se acumula en un crédito y se lanza un lote de 7.800 cada vez que el crédito lo alcanza (**lazo abierto**: no mira el inventario).
- **`comparar_modelos`:** en cada réplica $i$ (semilla 2026 + $i$, 30 réplicas) corre los dos modelos agregados. Su demanda, idéntica en ambos, alimenta tres gemelos: punto de reorden, plan de persecución y plan nivelado.
- **KPI:** demanda, producción, nivel de servicio, no atendido, inventario a fin de mes (promedio y máximo), meses y días sobre la bodega, costo anual = $\sum_t I^{fin}_t \cdot 83{,}56$ y ocupación de la llenadora. Intervalo del 95 %: $t_{0{,}975;\,29}\,s/\sqrt{30}$.
- **Tabla «Mejor modelo»:** para cada KPI elige el mejor de los 3 gemelos y dice si la diferencia con el segundo es significativa (brecha mayor que la suma de las semiamplitudes).

### Resultados clave con números

> Las celdas 36 a 44 no tienen salidas en el `.ipynb`. Estos números son de la corrida documentada en [`CONTEXTO_GEMELO_THYMS.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/CONTEXTO_GEMELO_THYMS.md) (sección 7); los de nivel de servicio e inventario coinciden con la página 6 de la presentación.

**Sección 4** (semilla 42, variabilidad del 5 %):

| | Persecución | Nivelada |
|---|---|---|
| Inventario final máximo | 28.455 | 86.700 |
| Meses sobre la bodega | 0 | 4 (enero, febrero, abril y mayo) |
| Desabastecimiento | 0 | 7.799 (julio) |
| Costo de inventario al año | 18,72 M COP | 38,30 M COP |

**Sección 5** (30 réplicas, ± intervalo del 95 %, misma demanda en los 5 modelos). Días hábiles: el plan cuenta 246 y el calendario del gemelo 243. Meses distintos (plan/gemelo): abril 21/20, mayo 21/19, junio 20/19, agosto 20/19, octubre 20/21, noviembre 20/19, diciembre 19/21.

| KPI | Gemelo con punto de reorden | Gemelo + persecución | Gemelo + nivelada | Agregado persecución | Agregado nivelada |
|---|---|---|---|---|---|
| Demanda anual | 1.204.081 | igual | igual | igual | igual |
| Producción anual | 1.210.571 | 1.188.007 | 1.187.973 | 1.200.000 | 1.200.000 |
| Nivel de servicio | **99,99 %** | **79,42 % ± 5,76** | 84,99 % ± 4,46 | 99,99 % | 99,79 % |
| No atendido de inmediato | 115 | 249.252 | 182.005 | 145 | 2.546 |
| Inventario promedio a fin de mes | 35.341 | 14.643 | 29.867 | 26.379 | 43.234 |
| Inventario máximo a fin de mes | 43.802 | 24.371 | 78.098 | 36.472 | 94.865 |
| Meses sobre la bodega (de 12) | 0,0 | 0,0 | 1,5 | 0,1 | 3,9 |
| Días sobre la bodega | 0,0 % | 0,0 % | 9,7 % | — | — |
| Costo de inventario al año | 35,44 M | 14,68 M | 29,95 M | 26,45 M | 43,35 M |
| Ocupación de la llenadora | 29,4 % | 30,1 % | 30,1 % | 20,7 % | 20,8 % |

**Gráfica de la celda 44.** Una versión parecida está en la página 6 de la presentación, cuyo panel (b) muestra el inventario promedio en lugar del costo. Lo que se ve:
- el gemelo con punto de reorden se mantiene entre ~32.000 y ~38.000 tubos todo el año;
- el gemelo con persecución queda entre ~9.000 y ~17.000;
- el gemelo nivelado sube a ~78.000 en abril (sobre la bodega) y cae a casi 0 en julio;
- los modelos agregados (líneas punteadas) van por encima de sus gemelos.

**Por qué la persecución da 79 % en el gemelo** (diagnóstico de una réplica, según CONTEXTO):
1. el plan es fijo (1,2 M) y no corrige cuando la demanda real sale mayor;
2. al cierre quedan ~12.000 tubos de crédito sin lanzar, por el redondeo a lotes completos;
3. se producen ~1,19 M frente a ~1,20–1,22 M demandados, y el inventario se drena de 29.500 a casi 0;
4. con poco colchón y lotes que llegan a saltos de 7.800, hay quiebres dentro del mes.

El modelo agregado no lo ve porque mira solo el cierre del mes y da por perdida la venta no atendida.

### Conclusiones

1. El plan agregado de **persecución** es el factible (la nivelada no cabe en la bodega), y sirve para fijar volúmenes de capacidad y compras.
2. Ejecutarlo **a lazo abierto** dentro del gemelo da solo **79,4 %** de servicio, frente al 99,99 % del punto de reorden. La liberación diaria de lotes debe reaccionar al inventario: el plan fija los volúmenes y el punto de reorden libera los lotes (la presentación lo resume como «79,4 % → 99,99 %, por validar»).
3. Las cifras del modelo agregado (99,99 % de servicio en persecución) son optimistas frente al detallado, porque ignoran fallas, alistamientos, rendimiento y el día a día del inventario.

### Supuestos y advertencias

- **La tabla «Mejor modelo» engaña:** declara a la persecución mejor en inventario y costo, pero sale barata porque está desabastecida (79 % de servicio). Habría que comparar al mismo nivel de servicio o sumar un costo de faltante.
- **El agregado y el detallado miden distinto:**
  - el agregado pierde las ventas y mide a fin de mes; el gemelo acumula pendientes y mide a diario;
  - la ocupación del agregado es producción/capacidad (promedio de los meses), y la del gemelo, horas de marcha + alistamiento + falla.
- **Rompe la regla de «solo datos de entrada»:** las secciones 4 y 5 leen resultados de fórmulas del Excel (valores guardados). Si el libro se edita sin recalcular en Excel, leerán valores viejos o vacíos.
- **La estrategia mixta** se carga pero no se simula.
- **Calendario:** 246 días hábiles en el plan frente a 243 en el gemelo; además, `GemeloThymsSOP` modifica temporalmente la variable global `INICIO` (funciona, pero es frágil).
- La celda 37 vuelve a importar `scipy.stats`. En la tabla «Mejor modelo», «Días sobre bodega» puede declarar ganador con una ventaja de 0,0 en lugar de empate, porque la brecha se compara con `> 0` antes de redondear.
- Supuestos de la sección 5: demanda mensual con CV del 5 %, reparto fijo 48/30/22 % y plan dividido por el rendimiento para cubrir tubos buenos.
- Para reproducir los números hay que ejecutar el cuaderno completo (la sección 5 tarda ~10 s; las réplicas de la sección 3 son lo más lento).


---

<!-- fuente: corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/THYMS-presentacion-corte-2.md -->
# THYMS-presentacion-corte-2

> **Archivo:** [`THYMS-presentacion-corte-2.pdf`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/THYMS-presentacion-corte-2.pdf) · **Corte 2** · 9 páginas  
> **Nombre original:** `CORTE 2/THYMS Presentacion Corte 2.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** presentación del grupo con el entregable del Corte 2 sobre THYMS Colombia S.A.S. (6 de octubre de 2026): S&OP apoyado en un gemelo digital de la planta de tintes.

**Ideas clave:**
- **La capacidad no es el problema:** la llenadora (cuello de botella) trabaja al 29 % y la demanda podría crecer 3,37 veces (según el libro) antes de saturarla. Las restricciones reales son:
  - la bodega de producto terminado;
  - la bahía del producto C (punto de reorden + lote = 20.100 frente a 14.000);
  - la materia prima importada (13 días de cobertura frente a 55 requeridos).
- **El pronóstico del Corte 1 estaba sesgado;** corregido, el sesgo baja de 29.600 a 1.600 tubos/mes y el RMSE un 17 %.
- **Gemelo digital en SimPy:**
  - 6 estaciones;
  - demanda de facturas reales, fallas, alistamientos y OEE;
  - 16 sensores virtuales;
  - validado con balance de masa, ley de Little y horas de equipo (±0,7 %).
- **Escenarios:** bajar el lote de C a 7.800 elimina los días sobre la bahía; con un solo turno el servicio cae al 97,97 %; el servicio se mantiene ≥ 99,4 % hasta 2 veces la demanda.
- **Optimización** (Bowman = flujo en red, MILP de turnos): la persecución es óptima. Pero ejecutada a lazo abierto en el gemelo da 79,4 % de servicio frente al 99,99 % del modelo agregado; el plan debe fijar volúmenes y el punto de reorden liberar los lotes.

**Fórmulas y métodos** (los detalles están en los cuadernos):
- Suavización exponencial simple $F_{t+1} = \alpha y_t + (1-\alpha)F_t$, con $\alpha$ = 0,05 y nivel inicial = promedio de 3 meses ($y_t$ = venta del mes $t$, $F_t$ = pronóstico).
- Sesgo $\bar{e}$, señal de rastreo $\sum e_t / MAD$ y RMSE.
- Índices estacionales $s_m = y_m/\bar{y}$ con intervalo del 80 %.
- Ley de Little $WIP = TH \times$ tiempo de flujo; takt time = tiempo disponible / demanda.
- Modelo de transporte de Bowman y modelo de flujo en red para el plan agregado; MILP para los turnos.
- Simulación de eventos discretos con 30 réplicas, números aleatorios comunes e intervalo del 95 %.

**Resultados presentados:**

| Resultado | Valor | Página |
|---|---|---|
| Ocupación de la llenadora | 29 % (28,9 %) | 2, 5 |
| Factor de demanda antes de saturar | 3,37× | 2 |
| Tiempo de flujo por lote / takt / throughput / WIP | 16,9 h / 11,1 s/tubo / 352 frente a 325 tubos/h / 5.308 | 2 |
| Cobertura de materia prima | 13 frente a 55 días | 2 |
| Sesgo del pronóstico | 44,6 M → 2,4 M COP (29.600 → 1.600 tubos/mes) | 3, 7 |
| Señal de rastreo | 3,42 → 0,22 | 3 |
| RMSE | 76,8 M → 63,6 M COP (50.800 → 42.100 tubos/mes) | 3 |
| Prueba de estrés | ≥ 99,4 % hasta 2,0×; 93,9 % con 2,5×; 70,8 % con 3,0× | 5 |
| Lote de C de 7.800 | días sobre la bahía 32,3 % → 0 %; inventario −10,3 % | 5, 7 |
| Persecución frente a nivelado | inventario promedio 45.100 → 29.500 (−35 %); meses sobre la bodega 5 → 0 | 6, 7 |
| Servicio del plan a lazo abierto | 79,42 % (persecución) y 84,99 % (nivelado), frente a 99,99 % con punto de reorden | 6 |
| Un turno en enero, abril y agosto | −8.300 horas-hombre/año; −114,5 M COP/año | 6, 7 |
| Compras estacionales (+11.665 kg) | espera de materia prima 44,8 h → 9,3 h | 7 |
| Programa maestro | 156 lotes/año (−0,36 % frente al plan); alistamientos = 27,9 % del tiempo de la llenadora | 7 |

**Páginas clave:**
- p. 2: estudio preliminar;
- p. 3: pronóstico;
- p. 4: diseño y validación del gemelo;
- p. 5: escenarios;
- p. 6: optimización y comparación plan frente a gemelo (gráficos);
- p. 7: tabla de mejoras;
- p. 8: conclusiones.

**Relación con otros archivos del repo:**
- Estudio preliminar y plan agregado: [`Datos Thyms Completo.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Datos%20Thyms%20Completo.md).
- Pronóstico, gemelo, escenarios y estrés: [`Gemelo_Digital_Thyms.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md).
- Gemelo guiado por el plan (79,42 %, 84,99 %, 99,99 %): [`Gemelo_Digital_Thyms_MEJORADO.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms_MEJORADO.md).
- Resumen completo del trabajo: [`CONTEXTO_GEMELO_THYMS.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/CONTEXTO_GEMELO_THYMS.md).
- Pronóstico del Corte 1 que se corrige: [proyecto-thyms-pronostico](/corte-1-pronosticos/proyecto-thyms-pronostico/).
- Teoría del modelo de Bowman y del flujo en red: [01-planeacion-agregada-modelo-bowman](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/).
- Siguiente paso propuesto (Wagner–Whitin / Silver–Meal): [03-wagner-whitin-y-silver-meal](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/).

**Advertencias:**
- Los resultados de **Bowman, flujo en red, MILP de turnos y programa maestro** (página 6 y parte de la 7) **no están en los archivos de esta carpeta**: no hay un libro ni un cuaderno de THYMS con esos modelos. Los archivos de [01-planeacion-agregada-modelo-bowman](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/) son ejemplos de clase con otros datos.
- Tampoco salen de estos archivos:
  - el «26 % de uso de mano de obra en el mes pico» (p. 2);
  - las horas de espera de materia prima 44,8 h → 9,3 h y el «×5» (pp. 5 y 7): el cuaderno solo reporta réplicas con faltante, 3 frente a 6;
  - los −114,5 M COP de mano de obra.
- Los «61 g/tubo» (p. 2) equivalen a 6.106 kg de materia prima por 100.000 tubos (hoja `Restricciones`).
- La página 7 no explica qué significa «(sin cambio)»; podría referirse a que el servicio no cambia [interpretación no confirmada]. «(por validar)» se entiende porque el plan + punto de reorden todavía no se había simulado: es el «siguiente paso» de la página 8.
