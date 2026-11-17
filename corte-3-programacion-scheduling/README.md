# Corte 3: Programación de la producción (scheduling)

Tercer corte del curso (40 % de la nota final). Pasa de "qué y cuánto producir" (Cortes 1 y 2) a **en qué orden y en qué máquina**. Usa la notación de Graham $\alpha\,|\,\beta\,|\,\gamma$:

- $\alpha$: entorno de máquinas ($1$, $Pm$, $Fm$, $Jm$);
- $\beta$: restricciones ($r_j$, $prec$, $s_{ij}$, $prmu$, $pmtn$);
- $\gamma$: objetivo ($C_{max}$, $\sum w_jC_j$, $L_{max}$, $\sum w_jT_j$, $\sum U_j$).

```
Órdenes liberadas por el MRP (Corte 2)
 └─ ¿Qué entorno de máquinas?
     ├─ 1 máquina            → reglas de despacho (SPT, EDD, WSPT, MS, ATC, CR), cadenas, Lawler, Moore-Hodgson
     ├─ máquinas paralelas   → LPT, SPT, LNS/CP, LFJ
     ├─ flow shop            → Johnson (F2), Campbell–CDS, NEH
     └─ job shop             → modelo disyuntivo (GAMS), shifting bottleneck
```

## Temas (en orden de clase)

| # | Carpeta | Clase | Qué cubre | Ejercicios en la carpeta |
|---|---|---|---|---|
| 00 | [`00-compendio-metodos-scheduling/`](00-compendio-metodos-scheduling/README.md) | — | Excel de 12 hojas (índice y 11 métodos) con **todos los métodos del corte** resueltos: CRP, SPT/WSPT/EDD, MS/ATC, cadenas, preemption, Lawler, LPT/SPT, LNS/CP, LFJ/LFM, Johnson, CDS y NEH | Cada hoja enlaza con el tema correspondiente |
| 01 | [`01-introduccion-scheduling/`](01-introduccion-scheduling/README.md) | [L16](01-introduccion-scheduling/L16-intro-scheduling.md) | Notación α\|β\|γ; indicadores $C_j, L_j, T_j, U_j, E_j$; del MRP a las órdenes; anomalías en $P2\,\|\,prec\,\|\,C_{max}$; programas sin retraso y activos; complejidad | — |
| 02 | [`02-una-maquina/`](02-una-maquina/README.md) | [L17](02-una-maquina/L17-single-machine-scheduling.md) | FIFO, **SPT, EDD, WSPT**, MS, **ATC**, CR, cadenas (factor ρ), preemption, **Lawler**, **Moore-Hodgson**, Solver | Reglas de despacho, precedencias, ejemplo con $r_j$ y `atc.py` (reproduce la secuencia de clase 1-3-2-4) |
| 03 | [`03-maquinas-paralelas/`](03-maquinas-paralelas/README.md) | [L18](03-maquinas-paralelas/L18-parallel-machine-scheduling.md) | Máquinas paralelas: **LPT** para $Pm\,\|\,\|\,C_{max}$ (garantía $4/3 - 1/3m$), SPT, precedencias (CP/LNS), elegibilidad (LFJ/LFM), preemption y MIP de $Rm\,\|\,\|\,\sum C_j$ | Plantilla de paralelas (15 trabajos, 3 máquinas), con LPT, SPT y WSPT calculados en el `.md` |
| 04 | [`04-flow-shop/`](04-flow-shop/README.md) | [L19](04-flow-shop/L19-flow-shop-scheduling.md) | Flow shop de permutación: **Johnson** (F2/F3), MIP de $Fm\,\|\,prmu\,\|\,C_{max}$ en **GAMS**, **Campbell–CDS**, **NEH**, flow shop flexible y algoritmos genéticos | Excel con Johnson, Campbell, CDS (Cmax 168) y NEH |
| 05 | [`05-job-shop/`](05-job-shop/README.md) | [Job shop](05-job-shop/job-shop-y-flexible-job-shop.md) | Job shop: modelo disyuntivo, implementación en **GAMS/LogMIP**, grafo disyuntivo, **shifting bottleneck** ($1\,\|\,r_j\,\|\,L_{max}$), LEKIN | — |

## Proyecto del corte: competencia de scheduling

**[`proyecto-competencia-scheduling/`](proyecto-competencia-scheduling/README.md)** es una competencia en Gradescope. Se califica así: **calidad 60 %, tiempo de cómputo 30 % e informe 10 %** (PDF de máximo 4 páginas).

- **Reto 1, Willy Wonka:** $F3\,|\,prmu, s_{ij}\,|\,C_{max}$. Flow shop de 3 máquinas con alistamientos por tipo de lote (S, N, R) y la transición N→R prohibida.
- **Reto 2, Monstruópolis:** $P3\,|\,r_j, prec\,|\,\sum w_jT_j$. Tres máquinas paralelas con liberaciones y precedencias.

La carpeta tiene dos partes:
- `enunciados/`: instructivo, retos y plantillas del profesor.
- `solucion/`: código del estudiante. Tiene su propio [`README.md`](proyecto-competencia-scheduling/solucion/README.md) e [`INFORME_TECNICO.md`](proyecto-competencia-scheduling/solucion/INFORME_TECNICO.md).

| | Método | Resultado |
|---|---|---|
| **Reto 1** | Cota inferior, NEH, búsqueda local y programación dinámica acotada | Óptimo demostrado en 30/30 instancias de la plantilla, Cmax promedio 616,77, unos 4 ms. La primera entrega en Gradescope dio «616.7667 / 100.0». |
| **Reto 2** | WSPT/ATC y recocido simulado | 0 violaciones, unos 75–80 ms por instancia. El óptimo no se puede demostrar. |

El estudiante decidió usar solo métodos dentro del alcance del curso: sin solvers externos ni OR-Tools.

## Otros archivos

[`otros-archivos/`](otros-archivos/README.md) guarda un Excel de **otra materia (Gerencia Financiera)** que estaba en la carpeta `CORTE 3/`. Se incluyó para no omitir nada, pero **no es material de Planeación**.

## Cuidado con estos errores

- Las plantillas del profesor para la competencia tienen errores. Por ejemplo, `calcular_makespan_penalizado` del Reto 1 toma el tipo del último lote de la secuencia.
- Algunos Excel de una máquina reinician el reloj o tienen un objetivo constante.

Todos están documentados en [`../ERRATAS.md`](../ERRATAS.md).
