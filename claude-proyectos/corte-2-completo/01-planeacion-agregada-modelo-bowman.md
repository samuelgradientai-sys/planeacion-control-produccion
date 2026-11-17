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


---

<!-- fuente: corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/ejemplo-modelo-bowman.md -->
# ejemplo-modelo-bowman

> **Archivo:** [`ejemplo-modelo-bowman.xlsx`](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/ejemplo-modelo-bowman.xlsx) · **Corte 2** (el archivo estaba en la carpeta `CORTE 3/` del estudiante) · Libro de Excel con 1 hoja(s): `Hoja1`  
> **Nombre original:** `CORTE 3/Ejemplo Modelo Bowman.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Es **el mismo ejercicio** que [modelo-bowman.md](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-bowman.md): el ejemplo del modelo de Bowman de la clase [L10 – Aggregate planning](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md), pp. 55-67. Tiene los productos A y B, 4 meses y tiempo regular y extra, con capacidad de 160 h y 40 h por mes. Aquí todo está reorganizado en **una sola hoja**, `Hoja1`.

Los datos, la solución que encuentra Solver y el costo mínimo (**\$8144**) son idénticos a los de `modelo-bowman.xlsx`. No es otro ejercicio, sino una versión más ordenada:
- los costos están enlazados a celdas de parámetros;
- los rótulos de inventario inicial son correctos;
- se controla la capacidad extra del mes 1.

A cambio, introduce una fórmula rara para la demanda del inventario final (ver Observaciones).

El archivo venía de la carpeta del Corte 3 (nombre original `CORTE 3/Ejemplo Modelo Bowman.xlsx`), por eso la cabecera automática dice «Corte 3». Su tema es del Corte 2.

Con él se aprende lo mismo que con el otro libro:
1. agregar la demanda en horas y calcular la demanda neta;
2. armar la matriz de costos $C + (k-j)C_I$;
3. resolver el problema de transporte con Solver.

### Hoja `Hoja1`

**Objetivo (deducido):** minimizar el costo de producción más almacenamiento para cubrir la demanda neta agregada de los meses 1 a 4 y un inventario final de 80 h, con tiempo regular y extra.

**Datos de entrada (B2:F7)**

| Mes | Demanda Producto A | Demanda Producto B | Demanda Agregada Bruta (h), col. E | Demanda Neta (h), col. F |
|---|---|---|---|---|
| 1 | 100 | 200 | 180 | 64 |
| 2 | 90 | 190 | 166 | 158 |
| 3 | 110 | 210 | 194 | 194 |
| 4 | 100 | 200 | 180 | 180 |
| **Total (fila 7)** | 400 | 800 | – | – |

**Parámetros**

| Celda | Parámetro | Valor |
|---|---|---|
| C9 | Inventario Inicial A | 36 |
| C10 | Inventario Inicial B | 220 |
| F9 | Tiempo Producción A (h/unid.), $h_A$ | 1 |
| F10 | Tiempo Producción B (h/unid.), $h_B$ | 0.4 |
| I8 | Costo Producción Regular, $C_R$ (\$/h) | 10 |
| I9 | Costo Producción Extra, $C_O$ (\$/h) | 15 |
| I10 | Costo de Almacenamiento, $C_I$ (\$/h-mes) | 4 |
| Q15:Q18 | Capacidad regular máxima por mes (h) | 160 |
| Q22:Q25 | Capacidad extra máxima por mes (h) | 40 |

**Método paso a paso**

1. **Demanda agregada bruta** (E3:E6), `=C3*$F$9+D3*$F$10`: $D^{bruta}_t = 1{,}0\,A_t + 0{,}4\,B_t$, que da 180, 166, 194 y 180.
2. **Demanda neta** (F3:F6):
   - F3 `=(C3-C9)*F9+0*F10`, es decir $(100-36)\cdot1 + 0 = 64$. B no aporta porque su inventario de 220 cubre el mes 1.
   - F4 `=C4*F9+170*F10`, es decir $90 + 170\cdot0{,}4 = 158$. El 170 está fijo y equivale a $190-20$.
   - F5 y F6 son iguales a la bruta: 194 y 180.
3. **Matriz de costos regular** (C15:G18), con filas = mes de producción, columnas = mes de consumo 1-5 y la columna 5 como inventario final.
   - La diagonal es `=$I$8` (10).
   - Hacia la derecha cada celda es `=celda izquierda + $I$10`, o sea +4.
   - Bajo la diagonal hay un 1000 fijo (prohibido, porque no hay backlog).
   - Fórmula: $c^R_{jk} = C_R + (k-j)C_I$.

   | Producción \ Consumo | 1 | 2 | 3 | 4 | 5 |
   |---|---|---|---|---|---|
   | 1 | 10 | 14 | 18 | 22 | 26 |
   | 2 | 1000 | 10 | 14 | 18 | 22 |
   | 3 | 1000 | 1000 | 10 | 14 | 18 |
   | 4 | 1000 | 1000 | 1000 | 10 | 14 |

4. **Matriz de costos extra** (C22:G25). La diagonal es `=I9` (15) y hacia la derecha se suma `$I$10`: $c^O_{jk} = C_O + (k-j)C_I$.

   | Producción \ Consumo | 1 | 2 | 3 | 4 | 5 |
   |---|---|---|---|---|---|
   | 1 | 15 | 19 | 23 | 27 | 31 |
   | 2 | 1000 | 15 | 19 | 23 | 27 |
   | 3 | 1000 | 1000 | 15 | 19 | 23 |
   | 4 | 1000 | 1000 | 1000 | 15 | 19 |

5. **Demanda del mes 5 (inventario final)**. G19 `=SUM(G15:G18)` = 26 + 22 + 18 + 14 = **80**, con el rótulo «Costo Demanda Neta P5». La fila 28 toma ese valor en O28 `=G19`.
6. **Variables y restricciones**
   - Variables: K15:O18 (horas regulares $R_{jk}$) y K22:O25 (horas extra $O_{jk}$).
   - Horas usadas: P15 `=SUM(K15:O15)`, P16 `=SUM(L16:O16)`, P17 `=SUM(M17:O17)` y P18 `=SUM(N18:O18)`. Para el tiempo extra se usan las mismas sumas en P22:P25.
   - Demanda satisfecha: K27:O27, por ejemplo M27 `=SUM(M15:M17,M22:M24)`.
   - Demanda neta: K28:N28 `=F3`…`=F6` y O28 `=G19`.
7. **Costos**
   - K30 `=SUMPRODUCT(K15:O18,C15:G18)`: costo regular.
   - K31 `=SUMPRODUCT(K22:O25,C22:G25)`: costo extra.
   - K32 `=SUM(K30:K31)`: costo total.

**Configuración de Solver** (nombres ocultos de la hoja)

| Elemento | Valor |
|---|---|
| Objetivo | K32, minimizar (`solver_typ = 2`) |
| Celdas variables | K15:O18 y K22:O25 |
| Restricción 1 | K27:O27 = K28:O28 (demanda) |
| Restricción 2 | P15:P18 ≤ Q15:Q18 (capacidad regular) |
| Restricción 3 | P22:P25 ≤ Q22:Q25 (capacidad extra) |
| Opciones | no negativas (`solver_neg = 1`), modelo lineal (`solver_lin = 1`), motor Simplex LP (`solver_eng = 2`) |

El modelo matemático es el de Bowman (L10 p. 54):

$$\min Z=\sum_{j=1}^{4}\sum_{k=1}^{5}\left(c^R_{jk}R_{jk}+c^O_{jk}O_{jk}\right)$$

sujeto a

$$\sum_k R_{jk}\le160,\qquad \sum_k O_{jk}\le40,\qquad \sum_j (R_{jk}+O_{jk})=D_k$$

con $D=(64,158,194,180,80)$.

**Resultados**

Horas regulares (K15:O18), con «Usada» en P y «Máxima» en Q:

| Producción \ Consumo | 1 | 2 | 3 | 4 | 5 | Usada | Máxima |
|---|---|---|---|---|---|---|---|
| 1 | 64 | 0 | 0 | 12 | 40 | 116 | 160 |
| 2 | 0 | 158 | 0 | 2 | 0 | 160 | 160 |
| 3 | 0 | 0 | 154 | 6 | 0 | 160 | 160 |
| 4 | 0 | 0 | 0 | 160 | 0 | 160 | 160 |

Horas extra (K22:O25):

| Producción \ Consumo | 1 | 2 | 3 | 4 | 5 | Usada | Máxima |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 40 |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 40 |
| 3 | 0 | 0 | 40 | 0 | 0 | 40 | 40 |
| 4 | 0 | 0 | 0 | 0 | 40 | 40 | 40 |

| Fila | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Demanda Satisfecha (27) | 64 | 158 | 194 | 180 | 80 |
| Demanda Neta (28) | 64 | 158 | 194 | 180 | 80 |

Resultados de costo:
- Costo Total Hora Regular (K30) = **\$6784**.
- Costo Total Hora Extra (K31) = **\$1360**.
- **Costo Total (K32) = \$8144**.

**Gráficos:** no tiene.

**Conclusión del ejemplo:** se obtiene el mismo óptimo que en `modelo-bowman.xlsx`, celda por celda, y el mismo costo mínimo de la presentación (\$8144).

El plan consolidado es:
- tiempo regular: 116, 160, 160 y 160 h;
- tiempo extra: 0, 0, 40 y 40 h.

La asignación concreta difiere de la de L10 p. 65, pero el costo es el mismo: son óptimos alternativos. La explicación está en [modelo-bowman.md](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-bowman.md).

### Comparación con `modelo-bowman.xlsx`

| Aspecto | `modelo-bowman.xlsx` | `ejemplo-modelo-bowman.xlsx` |
|---|---|---|
| Hojas | 2 (`COSTOS`, `PRODUCCION`) | 1 (`Hoja1`) |
| Datos (demanda, tiempos, costos, capacidades) | Iguales | Iguales |
| Inventario inicial | Rótulos invertidos (dice A = 220, B = 36) | Rótulos correctos (A = 36, B = 220) |
| Costos de las matrices | Números fijos (10, 15, +4) | Enlazados a I8, I9 e I10 |
| Demanda neta en el modelo | Escrita a mano (fila 20) | Enlazada a F3:F6; el mes 5 sale de G19 |
| Capacidad extra del mes 1 | Celda con «-» (no se controla) | `=SUM(K22:O22)` (se controla) |
| Solución y costo | 6784 + 1360 = 8144 | Idéntica: 6784 + 1360 = 8144 |

**Veredicto:** es el mismo ejercicio, con los mismos datos y la misma solución. Este libro es una versión reordenada y algo más limpia del otro.

### Observaciones

- **El 80 del inventario final sale de una suma de costos.** G19 `=SUM(G15:G18)` suma los costos regulares de la columna 5 (26 + 22 + 18 + 14) y el resultado es 80 por coincidencia. En la presentación (L10 p. 62) las 80 h son un dato de demanda del «Inventario Final», no una suma de costos. El rótulo «Costo Demanda Neta P5» lo confirma. Si se cambia $C_R$ o $C_I$, la demanda del mes 5 cambiaría sin razón.
- F4 tiene el 170 escrito a mano, igual que en el otro libro. Los 1000 de las celdas prohibidas también son fijos.
- F3 `=(C3-C9)*F9+0*F10` está bien para el producto A, pero el término de B se anula a mano (`0*F10`) en lugar de calcular $\max(0, B_1 - I_B)$.
- C20 dice «Mes de Consumo Periodo Regular» encima de la matriz de costos **extra**. Debería decir «Extra». K20 sí está bien.
- La columna E no tiene total (en el otro libro E7 = 720).
- Las sumas de «Usada» excluyen las celdas bajo la diagonal. Esas celdas cuestan 1000, así que nunca se usan.
- La cabecera automática de este .md dice «Corte 3» porque el archivo estaba en esa carpeta. El contenido es del Corte 2.


---

<!-- fuente: corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-bowman.md -->
# modelo-bowman

> **Archivo:** [`modelo-bowman.xlsx`](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-bowman.xlsx) · **Corte 2** · Libro de Excel con 2 hoja(s): `COSTOS`, `PRODUCCION`  
> **Nombre original:** `CORTE 2/BOWMAN.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Este libro resuelve con Excel Solver el **ejemplo del modelo de Bowman** de la clase [L10 – Aggregate planning](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md) (pp. 55-67). El ejemplo tiene dos productos (A y B), 4 meses y dos fuentes de capacidad por mes, tiempo regular y tiempo extra. Primero se agrega la demanda en horas de trabajo y después se decide cuántas horas producir en cada mes y en cada régimen para cubrir la demanda de cada mes de consumo al menor costo de producción más almacenamiento.

Con él se aprende a:
1. calcular la demanda neta agregada;
2. construir la matriz de costos producción→consumo, $C + (k-j)C_I$;
3. formular el problema de transporte en una hoja y resolverlo con Solver (Simplex LP);
4. leer el plan consolidado de horas regulares y extra.

Su nombre original era `CORTE 2/BOWMAN.xlsx`. El mismo ejercicio está reorganizado en una sola hoja en [ejemplo-modelo-bowman.md](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/ejemplo-modelo-bowman.md).

### Hoja `COSTOS`: datos, demanda agregada y matrices de costo

**Objetivo (deducido):** preparar los datos del modelo, es decir, la demanda neta en horas por mes y los costos unitarios de cada par (mes de producción, mes de consumo).

**Datos de entrada (B2:F7)**

| Mes | Producto A (unid.) | Producto B (unid.) | Demanda agregada bruta (h), col. E | Demanda neta (h), col. F |
|---|---|---|---|---|
| 1 | 100 | 200 | 180 | 64 |
| 2 | 90 | 190 | 166 | 158 |
| 3 | 110 | 210 | 194 | 194 |
| 4 | 100 | 200 | 180 | 180 |
| **Total (fila 7)** | 400 | 800 | 720 | 596 |

**Parámetros (J2:K11)**

| Celda | Parámetro (rótulo de la hoja) | Valor |
|---|---|---|
| K3 | Costo hora regular (\$/hora), $C_R$ | 10 |
| K4 | Costo hora extra (\$/hora), $C_O$ | 15 |
| K5 | Costo almacenamiento (\$/unidad), $C_I$ (en realidad \$/hora-mes) | 4 |
| K6 | Capacidad regular (horas/mes) | 160 |
| K7 | Capacidad extra (horas/mes) | 40 |
| K8 | Horas por unidad – producto A, $h_A$ | 1 |
| K9 | Horas por unidad – producto B, $h_B$ | 0.4 |
| K10 | «Inventario inicial – producto A (unid.)» | 220 |
| K11 | «Inventario inicial – producto B (unid.)» | 36 |

> Los rótulos de K10 y K11 están invertidos. Según L10 p. 55 el inventario inicial es 36 de A y 220 de B, y la fórmula de F3 usa K11 = 36 para el producto A (ver Observaciones).

**Método paso a paso**

1. **Demanda agregada bruta en horas** (E3:E6), `=C3*$K$8+D3*$K$9`:
   $$D^{bruta}_t = h_A A_t + h_B B_t = 1{,}0\,A_t + 0{,}4\,B_t$$
   Da 180, 166, 194 y 180, con un total de 720 h (E7).
2. **Demanda neta en horas** (F3:F6):
   - F3 `=C3-$K$11*$K$8+0*$K$9`, es decir $(100-36)\cdot 1 + 0 \cdot 0{,}4 = 64$. A se descuenta su inventario de 36. B no aporta nada porque su inventario (220) cubre los 200 del mes 1 y sobran 20.
   - F4 `=C4*$K$8+170*$K$9`, es decir $90 + 170 \cdot 0{,}4 = 158$. El 170 está escrito a mano y equivale a $190 - 20$, la demanda de B del mes 2 menos lo que sobró del inventario.
   - F5 y F6 son iguales a la bruta (194 y 180), porque ya no queda inventario.
   - Total neto: 596 h (F7).
3. **Matriz de costos en tiempo regular** (C12:G15). Las filas son el mes de producción $j$ (1-4) y las columnas el mes de consumo $k$ (1-5). La columna 5 es el **inventario final** de L10 p. 62.
   - En la diagonal hay un 10 escrito a mano. A la derecha, cada celda vale la de su izquierda + 4 (`=C12+4`, `=D12+4`, …; G15 `=10+4`).
   - Debajo de la diagonal hay un 1000, que funciona como "M grande" para prohibir producir después del mes de consumo (no hay backlog).
   - Fórmula: $c^R_{jk} = C_R + (k-j)\,C_I$ si $k \ge j$, y $1000$ si $k < j$.

   | Producción \ Consumo | 1 | 2 | 3 | 4 | 5 (inv. final) |
   |---|---|---|---|---|---|
   | 1 | 10 | 14 | 18 | 22 | 26 |
   | 2 | 1000 | 10 | 14 | 18 | 22 |
   | 3 | 1000 | 1000 | 10 | 14 | 18 |
   | 4 | 1000 | 1000 | 1000 | 10 | 14 |

4. **Matriz de costos en tiempo extra** (C20:G23). Se arma igual, partiendo de 15 en la diagonal: $c^O_{jk} = C_O + (k-j)\,C_I$.

   | Producción \ Consumo | 1 | 2 | 3 | 4 | 5 (inv. final) |
   |---|---|---|---|---|---|
   | 1 | 15 | 19 | 23 | 27 | 31 |
   | 2 | 1000 | 15 | 19 | 23 | 27 |
   | 3 | 1000 | 1000 | 15 | 19 | 23 |
   | 4 | 1000 | 1000 | 1000 | 15 | 19 |

### Hoja `PRODUCCION`: modelo de transporte y solución con Solver

**Objetivo:** encontrar las horas $R_{jk}$ (regulares) y $O_{jk}$ (extra) producidas en el mes $j$ para el mes de consumo $k$ que minimizan el costo total.

**Estructura de la hoja**

| Rango | Contenido |
|---|---|
| D5:H8 | Variables $R_{jk}$: horas regulares (filas = mes de producción 1-4, columnas = mes de consumo 1-5) |
| D13:H16 | Variables $O_{jk}$: horas extra |
| I5:I8 | Horas regulares usadas: I5 `=SUM(D5:H5)`, I6 `=SUM(E6:H6)`, I7 `=SUM(F7:H7)`, I8 `=SUM(G8:H8)`. Solo suman desde la diagonal |
| J5:J8 | Capacidad regular: 160 |
| I13:I16 | Horas extra usadas: I13 tiene el **texto «-»**, I14 `=SUM(E14:H14)`, I15 `=SUM(F15:H15)`, I16 `=SUM(G16:H16)` |
| J13:J16 | Capacidad extra: 40 |
| D19:H19 | Demanda satisfecha: $\sum_{j \le k}(R_{jk}+O_{jk})$, p. ej. F19 `=SUM(F5:F7,F13:F15)` |
| D20:H20 | «Demanda Neta», escrita a mano: 64, 158, 194, 180, 80 (el 80 es el inventario final) |
| C23 | `=SUMPRODUCT(COSTOS!C12:G15,D5:H8)`: costo regular |
| C24 | `=SUMPRODUCT(COSTOS!C20:G23,D13:H16)`: costo extra |
| C25 | `=SUM(C23:C24)`: costo total (celda objetivo) |
| L5 | «investiario total» `=SUM(E5:H5,E13:H13)` = 52: horas producidas en el mes 1 para meses posteriores, es decir, el inventario que sale del mes 1 |

**Configuración de Solver** (guardada en los nombres ocultos de la hoja)

| Elemento | Valor |
|---|---|
| Objetivo | C25, minimizar (`solver_typ = 2`) |
| Celdas variables | D5:H8 y D13:H16 |
| Restricción 1 | D19:H19 = D20:H20 (satisfacer la demanda) |
| Restricción 2 | I13:I16 ≤ J13:J16 (capacidad extra) |
| Restricción 3 | I5:I8 ≤ J5:J8 (capacidad regular) |
| No negatividad | sí (`solver_neg = 1`) |
| Motor | Simplex LP (`solver_eng = 2`) |

**Modelo matemático equivalente** (Bowman, L10 p. 54):

$$\min Z = \sum_{j=1}^{4}\sum_{k=1}^{5}\left(c^R_{jk}R_{jk} + c^O_{jk}O_{jk}\right)$$

$$\text{s.a.}\quad \sum_{k} R_{jk} \le 160,\qquad \sum_{k} O_{jk} \le 40 \quad \forall j;\qquad \sum_{j=1}^{4}\left(R_{jk}+O_{jk}\right) = D_k \quad \forall k;\qquad R_{jk}, O_{jk} \ge 0$$

con $D = (64, 158, 194, 180, 80)$.

**Resultados (solución guardada)**

Horas en tiempo regular $R_{jk}$:

| Producción \ Consumo | 1 | 2 | 3 | 4 | 5 (inv. final) | Usadas | Capacidad |
|---|---|---|---|---|---|---|---|
| 1 | 64 | 0 | 0 | 12 | 40 | 116 | 160 |
| 2 | 0 | 158 | 0 | 2 | 0 | 160 | 160 |
| 3 | 0 | 0 | 154 | 6 | 0 | 160 | 160 |
| 4 | 0 | 0 | 0 | 160 | 0 | 160 | 160 |

Horas en tiempo extra $O_{jk}$:

| Producción \ Consumo | 1 | 2 | 3 | 4 | 5 (inv. final) | Usadas | Capacidad |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 0 | 0 | «-» | 40 |
| 2 | 0 | 0 | 0 | 0 | 0 | 0 | 40 |
| 3 | 0 | 0 | 40 | 0 | 0 | 40 | 40 |
| 4 | 0 | 0 | 0 | 0 | 40 | 40 | 40 |

| Concepto | Mes 1 | Mes 2 | Mes 3 | Mes 4 | Mes 5 (inv. final) |
|---|---|---|---|---|---|
| Demanda satisfecha (fila 19) | 64 | 158 | 194 | 180 | 80 |
| Demanda neta (fila 20) | 64 | 158 | 194 | 180 | 80 |

Plan consolidado (deducido de las tablas): regulares 116, 160, 160 y 160 h; extra 0, 0, 40 y 40 h; totales 116, 160, 200 y 200 h. Es el mismo plan de L10 p. 66.

Costos: **regular \$6784** (C23) + **extra \$1360** (C24) = **costo total \$8144** (C25).
- Detalle regular: $64(10)+12(22)+40(26)+158(10)+2(18)+154(10)+6(14)+160(10) = 6784$.
- Detalle extra: $40(15)+40(19) = 1360$.

**Gráficos:** el libro no tiene gráficos.

**Conclusión del ejemplo:** el costo mínimo coincide con el de la presentación (\$8144, L10 p. 67). El plan usa todo el tiempo regular de los meses 2 a 4 y deja libres 44 h regulares en el mes 1. Usa además todo el tiempo extra de los meses 3 y 4. Las 80 h de inventario final se cubren con 40 h regulares del mes 1 (a \$26) y 40 h extra del mes 4 (a \$19).

La asignación celda por celda **no es la misma** de L10 p. 65. La presentación pone, por ejemplo, 52 h regulares del mes 1 al inventario final, y 32 + 8 h extra en el mes 3. Ambas son **óptimos alternativos**, porque tienen el mismo costo y las mismas horas por mes y por régimen.

Esto pasa porque el costo de almacenar depende solo de cuántas horas-mes se guardan en total. Ese total queda fijo con la producción de cada mes, sin importar a qué mes de consumo se asigne cada hora. Un re-cálculo propio con PL (HiGHS) también da \$8144, con una tercera asignación distinta.

### Observaciones

- **Rótulos invertidos de inventario inicial.** K10 dice «producto A» = 220 y K11 «producto B» = 36, pero los datos de L10 p. 55 son A = 36 y B = 220. La fórmula F3 usa K11 = 36 para A, así que el cálculo está bien y solo están mal los rótulos.
- **Fórmulas con números escritos a mano.**
  - F4 tiene el 170 fijo, que equivale a $190-(220-200)$.
  - Las matrices de costo usan 10, 15 y "+4" fijos en lugar de referenciar K3, K4 y K5.
  - La fila 20 (demanda neta) está escrita a mano en vez de enlazar con `COSTOS!F3:F6`.
  - Si cambian los parámetros, el modelo no se actualiza.
- **F3 mezcla unidades.** `=C3-$K$11*$K$8` resta "inventario × horas por unidad" a una demanda en unidades. Funciona solo porque $h_A = 1$. La forma general sería $(A_1 - I_A)\,h_A + \max(0, B_1 - I_B)\,h_B$.
- **I13 contiene el texto «-»** en lugar de `=SUM(D13:H13)`. Por eso la restricción de capacidad extra del mes 1 no controla nada. No afecta a la solución porque esas celdas valen 0.
- Las sumas de capacidad (I6:I8, I14:I16) excluyen las celdas bajo la diagonal. Esas celdas son variables, pero su costo de 1000 impide que se usen.
- El «mes 5» de las tablas es el **inventario final** de 80 h que da la presentación (L10 p. 62). Ni la hoja ni la presentación explican de dónde sale ese valor.
- «Costo almacenamiento (\$/unidad)» es en realidad \$4 por hora agregada y por mes (L10 p. 55: «productos hechos en una hora»).
- Erratas en los rótulos: «Capaciad de horas», «investiario total», «costo total horaExtra».
- No hay hojas vacías ni gráficos.


---

<!-- fuente: corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/modelo-flujo.gms -->
# Código: `corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/modelo-flujo.gms`

> Archivo completo: https://github.com/samuelgradientai-sys/planeacion-control-produccion/blob/main/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/modelo-flujo.gms

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


---

**Archivos de esta carpeta que no se copiaron en el paquete** (están completos en el repositorio):

- `corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/modelo-flujo.log` (ver en el repositorio: https://github.com/samuelgradientai-sys/planeacion-control-produccion/blob/main/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/modelo-flujo.log)
- `corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/modelo-flujo.lst` (ver en el repositorio: https://github.com/samuelgradientai-sys/planeacion-control-produccion/blob/main/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/modelo-flujo.lst)
- `corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/modelo-flujo.lxi` (ver en el repositorio: https://github.com/samuelgradientai-sys/planeacion-control-produccion/blob/main/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/modelo-flujo.lxi)
