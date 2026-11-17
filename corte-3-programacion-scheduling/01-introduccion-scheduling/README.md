# Introducción a la programación de la producción: scheduling (Corte 3)

## Qué cubre

Abre el corte 3. Ubica la programación detallada (*scheduling*) al final de la jerarquía Pronósticos → Planeación agregada → Plan maestro → MRP. Define los parámetros ($p_{ij}$, $r_j$, $d_j$, $w_j$) y los indicadores ($C_j$, $C_{max}$, $L_j$, $T_j$, $U_j$, $E_j$) y presenta la notación $\alpha|\beta|\gamma$ de Graham et al. (1979) para clasificar problemas. Termina con propiedades generales: programas sin retrasos, programas activos, anomalías del makespan en máquinas paralelas y jerarquía de complejidad.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [L16-intro-scheduling.md](./L16-intro-scheduling.md) (gemelo de `L16-intro-scheduling.pdf`) | Presentación "Lec 16 - intro Scheduling", 49 diapositivas, transcritas página por página con los Gantt en tablas | Sí (único archivo) |

## Orden de estudio sugerido

1. Contexto (pp. 3-6): de dónde vienen las órdenes (MRP) y qué es el machine scheduling.
2. Ejemplo de dos trabajos en dos máquinas (pp. 7-9): el orden cambia el makespan.
3. Elementos, objetivos, parámetros e indicadores (pp. 11-14). Conviene aprenderlos de memoria, porque se usan en todo el corte.
4. Del MRP a las órdenes y al Gantt (pp. 15-17).
5. Notación $\alpha|\beta|\gamma$ (pp. 18-31) y ejemplos de lectura (pp. 32-36).
6. Tipos de programación, programas sin retrasos y activos, y anomalías en $P2|prec|C_{max}$ (pp. 37-44).
7. Complejidad y realidad industrial (pp. 45-48).
8. Después, seguir con [02-una-maquina](../02-una-maquina/README.md).

## Conceptos y fórmulas clave

Detalle completo en el [resumen de L16](./L16-intro-scheduling.md#resumen).

- Indicadores, con $C_j$ = instante en que termina el trabajo $j$, $r_j$ = liberación, $d_j$ = fecha de entrega, $w_j$ = peso y $n$ = número de trabajos:

$$C_{max}=\max_j C_j\qquad \bar F=\frac1n\sum_j(C_j-r_j)\qquad L_j=C_j-d_j\qquad T_j=\max(L_j,0)$$

$$E_j=\max(0,\,d_j-C_j)\qquad U_j=\mathbb 1[T_j>0]\qquad \sum w_jT_j,\ \sum U_j,\ L_{max}=\max_j L_j,\ \sum w_jC_j,\ \sum w_j(1-e^{-rC_j})$$

- Notación $\alpha|\beta|\gamma$:
  - $\alpha$ (ambiente): $1$, $Pm$, $Qm$, $Rm$, $Fm$, $FFc$, $Jm$, $FJc$, $Om$.
  - $\beta$ (restricciones): $r_j$, $s_{jk}$, *prmp*, *prec*, *brkdwn*, $M_j$, *prmu*, *block*, *nwt*, *recrc*.
  - $\gamma$ (objetivo): $C_{max}$, $L_{max}$, $\sum w_jC_j$, $\sum w_jT_j$, $\sum U_j$…
- Programa **sin retrasos** (*non-delay*): ninguna máquina queda ociosa si hay trabajos esperando. Programa **activo**: ninguna operación puede adelantarse sin retrasar otra.
- Hay $n!$ secuencias posibles en una máquina. $1||\sum C_j \propto 1||\sum w_jC_j \propto Pm||\sum w_jC_j \propto Qm|prec|\sum w_jC_j$ ($\propto$ = "es caso especial de").

## Ejercicios resueltos disponibles

Todos están en [L16-intro-scheduling.md](./L16-intro-scheduling.md).

| Ejercicio | Páginas | Resultado principal |
|---|---|---|
| 2 trabajos, 2 máquinas en serie (A: 8/5, B: 7/10) | 7-9 | A-B: $C_{max}=25$; B-A: $C_{max}=22$ |
| Registros MRP de 2 productos → 4 órdenes | 15-16 | $p$ = lote × factor: 0.4, 0.6, 0.5 y 0.7 semanas |
| Gantt de las 4 órdenes | 17 | La orden 0004 termina en 4.2 con $d=4$ (0.2 semanas tarde) |
| $P2\|prec\|C_{max}$, 10 trabajos | 40-41 | Óptimo $C_{max}=31$ |
| El mismo con $p_j-1$ | 42 | $C_{max}=32$: el makespan sube (anomalía) |
| El mismo con 3 máquinas | 43 | $C_{max}=36$: el makespan sube (anomalía) |
| Lectura de notación | 32-36 | $FFc\|r_j\|\sum w_jT_j$, $Pm\|r_j,M_j\|\sum w_jT_j$, $P\infty\|prec\|C_{max}$ |

## Relación con otros temas y proyectos

- Antes, en el corte 2, el MRP genera las órdenes que aquí se programan: [04-bom-y-mrp](../../corte-2-planeacion-agregada-mrp/04-bom-y-mrp/), y [05-mrp-ii-y-capacidad](../../corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/) para la capacidad (CRP) y el backward scheduling.
- Después: [02-una-maquina](../02-una-maquina/README.md) (reglas de despacho, WSPT, EDD, ATC, CR, Moore, Lawler), [03-maquinas-paralelas](../03-maquinas-paralelas/), [04-flow-shop](../04-flow-shop/) y [05-job-shop](../05-job-shop/).
- Compendio de métodos del corte: [00-compendio-metodos-scheduling](../00-compendio-metodos-scheduling/metodos-programacion-produccion-corte3.md).
- Proyecto del corte: [proyecto-competencia-scheduling](../proyecto-competencia-scheduling/solucion/README.md), que plantea dos problemas en esta notación: $F3|prmu,s_{ij}|C_{max}$ y $P3|r_j,prec|\sum w_jT_j$.
