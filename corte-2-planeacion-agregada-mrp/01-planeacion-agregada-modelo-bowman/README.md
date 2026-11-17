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
| [L10-aggregate-planning.md](./L10-aggregate-planning.md) | Presentación de la clase 10 (74 pp.). Cubre S&OP, opciones de capacidad, agregación (Nahmias), método gráfico (\$108 450 / \$105 152 / \$117 800), modelo de Bowman con ejemplo de costo mínimo \$8144, desagregación y revenue management. | **Sí (1.º)** |
| [modelo-bowman.md](./modelo-bowman.md) | Excel con Solver (hojas `COSTOS` y `PRODUCCION`) que resuelve el ejemplo de Bowman de L10 pp. 55-67. Costo \$6784 regular + \$1360 extra = \$8144. | 2.º |
| [ejemplo-modelo-bowman.md](./ejemplo-modelo-bowman.md) | El **mismo ejercicio** reorganizado en una sola hoja, con parámetros enlazados. Tiene la misma solución y el mismo costo de \$8144. Venía de la carpeta del Corte 3. | 3.º (o en lugar del 2.º) |
| [modelo-flujo-gams/modelo-flujo.gms](./modelo-flujo-gams/modelo-flujo.gms) | Código GAMS (sin gemelo `.md`; se explica y se copia completo abajo). Es un PL de planeación agregada de 12 periodos con fuerza de trabajo, horas extra, faltantes y subcontratación. | 4.º |
| [modelo-flujo-gams/modelo-flujo.lst](./modelo-flujo-gams/modelo-flujo.lst) | Listado de salida de GAMS: eco del código, ecuaciones generadas, estadísticas y solución óptima con valores marginales. $z = 4\,062\,000$. Se resume abajo. | Con el `.gms` |
| [modelo-flujo-gams/modelo-flujo.log](./modelo-flujo-gams/modelo-flujo.log) | Bitácora de la ejecución: GAMS 54.3.1, CPLEX 22.1.2.0 con licencia demo, tamaño del modelo y «Optimal solution found, Objective: 4062000». | Opcional |
| [modelo-flujo-gams/modelo-flujo.lxi](./modelo-flujo-gams/modelo-flujo.lxi) | Índice del `.lst` que usa el IDE de GAMS para navegar el listado. Es un archivo de texto con líneas como `D 83 FO` o `I 643 z`. No tiene información del modelo. | No |

Los binarios (`.pdf` y `.xlsx`) están al lado de cada `.md`, con el mismo nombre.

## Orden de estudio sugerido

1. **L10 pp. 1-34** ([L10](./L10-aggregate-planning.md)): qué es la planeación agregada, la jerarquía de planes, S&OP, las opciones de capacidad y demanda, y cómo agregar productos (ejemplo de Nahmias, p. 31).
2. **L10 pp. 35-49**: el método gráfico y las tres estrategias (nivelar, subcontratar, contratar y despedir) con sus costos.
3. **L10 pp. 50-68**: la formulación de Bowman y el ejemplo completo (demanda neta agregada, matriz de costos, solución, plan consolidado, costo \$8144 y desagregación).
4. Abrir [modelo-bowman.md](./modelo-bowman.md) y [ejemplo-modelo-bowman.md](./ejemplo-modelo-bowman.md) para ver cómo se monta el mismo problema en Excel con Solver, y por qué su asignación difiere de la diapositiva pero cuesta lo mismo.
5. Leer [L11 pp. 3-12](../02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md) (modelo con fuerza de trabajo y backlog) y después la sección [Modelo de flujo en GAMS](#modelo-de-flujo-en-gams-modelo-flujo-gams) de este README, que implementa ese modelo.
6. Seguir con la desagregación del plan GAMS en [02-agregacion-y-desagregacion](../02-agregacion-y-desagregacion/README.md).
7. L10 pp. 69-74 (servicios y revenue management) como cierre conceptual.

## Conceptos y fórmulas clave

Todos los detalles están en el [Resumen de L10](./L10-aggregate-planning.md).

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

[`modelo-flujo.gms`](./modelo-flujo-gams/modelo-flujo.gms) (nombre original `MODELO DE FLUJO.gms`) formula y resuelve con CPLEX un **programa lineal de planeación agregada de 12 meses**. Decide en cada mes cuánto producir, cuántas horas regulares y extra usar, cuánto contratar o despedir (en horas de fuerza de trabajo), cuánto subcontratar y cuánto inventario o faltante llevar. El objetivo es minimizar el costo total.

Es el modelo de [L11 pp. 3-9](../02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md) con los datos del ejemplo de 5 productos y 12 meses: la demanda en horas-hombre es la columna «Total» de L11 p. 8, el inventario inicial es 3000 y los costos son los de L11 p. 9. Le agrega subcontratación, pone una penalización finita de 10 000 por faltante en lugar de $\pi=\infty$ y no tiene variable de horas ociosas.

Es la generalización del modelo de Bowman de L10, porque añade decisiones de fuerza de trabajo, faltantes y subcontratación. La solución ($P_t$, $I_t$) es el «Plan Agregado» que se desagrega por producto en [modelo-desagregacion.md](../02-agregacion-y-desagregacion/modelo-desagregacion.md) y [modelo-desagregacion-v2.md](../02-agregacion-y-desagregacion/modelo-desagregacion-v2.md).

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

El modelo GAMS da otro plan porque permite subcontratar a 95, no tiene horas de ocio ni inventario de seguridad y penaliza los faltantes con 10 000 en lugar de $\infty$. Ver [L11](../02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md).

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
| Agregación de 6 modelos (Nahmias, 2007) | [L10 pp. 30-31](./L10-aggregate-planning.md) | Producto promedio: 5,06 h-h y \$415,02; 1168 unidades; 5910 h-h |
| Agregación de productos de cuero y de acero | L10 pp. 32-33 | Solo enunciado (sin solución) |
| Método gráfico, 6 meses, 6200 unidades en 124 días | L10 pp. 37-47 | Tasa nivelada 50 unid/día; inventario total 1850 |
| Estrategia 1: fuerza constante (10 trabajadores) | L10 pp. 45-46 | \$108 450 (91,5 % mano de obra) |
| Estrategia 2: 38/día + subcontratar 1488 | L10 p. 48 | **\$105 152** (la más barata) |
| Estrategia 3: contratar y despedir | L10 p. 49 | \$117 800 |
| Modelo de Bowman: 2 productos, 4 meses, regular 160 h y extra 40 h | L10 pp. 55-67; [modelo-bowman.md](./modelo-bowman.md); [ejemplo-modelo-bowman.md](./ejemplo-modelo-bowman.md) | Demanda agregada neta 64, 158, 194, 180 y 80 de inventario final. Plan de 116, 160, 200 y 200 h (extra solo en los meses 3 y 4). **Costo mínimo \$8144**. Los Excel dan una asignación distinta a la de la diapositiva con el mismo costo (óptimos alternativos). |
| Desagregación del plan de Bowman | L10 p. 68 | A = 116, 55, 98, 136; B = 0, 262, 255, 160 |
| Plan agregado de 12 meses con fuerza de trabajo y subcontratación (GAMS) | [modelo-flujo-gams/](./modelo-flujo-gams/) (sección anterior) | $z=4\,062\,000$. 2880 h en los meses 1-2 y 3000 h desde el mes 3; subcontrata 7890 unidades en los meses 4-11; sin horas extra ni faltantes; inventario de 3280, 2760 y 1860 en los meses 1-3 |

## Relación con otros temas y proyectos

- **Antes:** los pronósticos que alimentan el plan vienen del [Corte 1](../../corte-1-pronosticos/).
- **Siguiente tema:** [02-agregacion-y-desagregacion](../02-agregacion-y-desagregacion/README.md).
  - [L11](../02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md) presenta el modelo con fuerza de trabajo y backlog que implementa el `.gms`.
  - Los Excel [modelo-desagregacion](../02-agregacion-y-desagregacion/modelo-desagregacion.md) y [modelo-desagregacion-v2](../02-agregacion-y-desagregacion/modelo-desagregacion-v2.md) desagregan por producto el plan que da este modelo GAMS: 2880, 2880 y luego 3000, con inventario total de 7900.
- **Después:**
  - [03-wagner-whitin-y-silver-meal](../03-wagner-whitin-y-silver-meal/README.md): tamaño de lote.
  - [04-bom-y-mrp](../04-bom-y-mrp/): el plan maestro alimenta el MRP.
  - [05-mrp-ii-y-capacidad](../05-mrp-ii-y-capacidad/): MRP II y capacidad.
- **Evaluación:** [parcial-2](../parcial-2/README.md) incluye la formulación de un modelo de planeación agregada (pregunta 1.2) y la evaluación de planes de persecución o nivelado.
- **Proyecto:** [proyecto-thyms-gemelo-digital](../proyecto-thyms-gemelo-digital/README.md). Según su presentación, aplica Bowman y el modelo de flujo al caso THYMS, aunque sus archivos no incluyen esos modelos.
