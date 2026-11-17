# Job shop y flexible job shop (Corte 3)

## Qué cubre

Programación de talleres en los que cada trabajo sigue su propia ruta por las máquinas, con el objetivo de minimizar el makespan ($J_m \,\|\, C_{max}$). Incluye:

- la formulación disyuntiva y su grafo, donde el makespan es la ruta crítica;
- la implementación en GAMS con LogMIP;
- la heurística del cuello de botella móvil (*shifting bottleneck*), con un ejemplo de 3 trabajos × 4 máquinas resuelto paso a paso;
- el software LEKIN.

El título y la agenda anuncian también *flexible job shop* e *iterated local search*, pero la presentación no tiene diapositivas sobre esos dos temas.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [job-shop-y-flexible-job-shop.md](./job-shop-y-flexible-job-shop.md) | Gemelo de la presentación de clase (33 págs.): definición de job shop, modelo disyuntivo, grafo disyuntivo, código GAMS/LogMIP completo, cuello de botella móvil paso a paso con Gantt final, LEKIN y Rubén Ruiz | Sí (es el único archivo) |

## Orden de estudio sugerido

1. Repasar la notación $J_m$ y $FJ_c$ en [L16, págs. 21–22](../01-introduccion-scheduling/L16-intro-scheduling.md) y el problema $1\mid r_j\mid L_{max}$ en [L17](../02-una-maquina/L17-single-machine-scheduling.md).
2. Págs. 3–8 del [gemelo](./job-shop-y-flexible-job-shop.md): definición, modelo disyuntivo y grafo. Intentar escribir las restricciones del ejemplo de la pág. 7 antes de mirar la respuesta deducida.
3. Págs. 9–10: código GAMS y su explicación (con la observación de que el modelo es *no-wait* por etapas).
4. Págs. 11–13: algoritmo del cuello de botella móvil.
5. Págs. 14–30: ejemplo completo. Conviene rehacer a mano las tablas de $r_j$, $d_j$, $C_j$ y $L_j$.
6. Pág. 31: probar LEKIN para comparar heurísticas.

## Conceptos y fórmulas clave

Notación: $(i,j)$ = operación del trabajo $j$ en la máquina $i$; $p_{ij}$ = tiempo de proceso; $y_{ij}$ = inicio; $A$ = arcos de ruta; $B$ = pares de operaciones de la misma máquina; $N$ = operaciones. Detalle en el [gemelo, págs. 5, 12 y 13](./job-shop-y-flexible-job-shop.md).

**Modelo disyuntivo**

$$\min C_{max}\quad \text{s.a.}\quad y_{kj}-y_{ij}\ge p_{ij}\ \ \forall (i,j)\to(k,j)\in A;\qquad C_{max}-y_{ij}\ge p_{ij}\ \ \forall (i,j)\in N$$
$$y_{ij}-y_{il}\ge p_{il}\ \ \text{ó}\ \ y_{il}-y_{ij}\ge p_{ij}\ \ \forall (i,l),(i,j)\in B;\qquad y_{ij}\ge 0$$

**Grafo disyuntivo.** Hay que orientar los arcos de $B$ sin crear ciclos. Entonces $C_{max}$ es la ruta más larga de $U$ a $V$.

**Cuello de botella móvil.** Para cada máquina no secuenciada se resuelve $1\mid r_j\mid L_{max}$ con

$$r_{ij}=\text{ruta más larga } U\to(i,j),\qquad d_{ij}=C_{max}(M_o)-\big[\text{ruta más larga }(i,j)\to V - p_{ij}\big],\qquad L_j=C_j-d_j$$

Se fija la máquina $k$ con mayor $L_{max}$, se actualiza $C_{max}(M_o\cup\{k\})=C_{max}(M_o)+L_{max}(k)$ y se re-optimizan las máquinas ya fijadas.

## Ejercicios resueltos disponibles

| Ejemplo | Dónde | Resultado principal |
|---|---|---|
| Restricciones MIP y grafo del job shop 3 trabajos × 4 máquinas | [gemelo, págs. 7–8](./job-shop-y-flexible-job-shop.md) | 7 restricciones de ruta y 8 disyunciones (respuesta deducida). Óptimo $C_{max}^*=28$ (cálculo propio con PuLP). |
| Modelo GAMS LogMIP (ejemplo 4 del manual de LogMIP), 7 trabajos × 5 etapas | [gemelo, págs. 9–10](./job-shop-y-flexible-job-shop.md) | Código completo transcrito. El PDF no muestra el resultado; reproducido en PuLP da $MS^*=32$. |
| Cuello de botella móvil, 3 trabajos × 4 máquinas | [gemelo, págs. 14–30](./job-shop-y-flexible-job-shop.md) | $C_{max}$: 22 → 27 (fija M1: 1-2-3, $L_{max}=5$) → 28 (fija M2: 2-1-3, $L_{max}=1$) → 28 (M3 y M4 con $L_{max}=0$). Gantt final: M3 2-1 y M4 2-3. $C_{max}=28$, que es óptimo. |
| Comparación en LEKIN, instancia MT10 | [gemelo, pág. 31](./job-shop-y-flexible-job-shop.md) | $C_{max}$: Local Search 1107, SB Routine 1110, Shifting Bottleneck 1113, WSPT 1356. |

## Relación con otros temas y proyectos

- [01-introduccion-scheduling](../01-introduccion-scheduling/): notación $\alpha\mid\beta\mid\gamma$ y definiciones de $J_m$, $FJ_c$ y recirculación.
- [02-una-maquina](../02-una-maquina/): EDD y $1\mid r_j\mid L_{max}$, el subproblema del cuello de botella móvil.
- [03-maquinas-paralelas](../03-maquinas-paralelas/): las máquinas paralelas de cada etapa son las que convierten un job shop en *flexible* job shop ($FJ_c$).
- [04-flow-shop](../04-flow-shop/): caso particular en que todos los trabajos siguen la misma ruta.
- [00-compendio-metodos-scheduling](../00-compendio-metodos-scheduling/): resumen de los métodos del Corte 3.
- [proyecto-competencia-scheduling](../proyecto-competencia-scheduling/): sus retos son un flow shop de permutación y máquinas paralelas con $r_j$ y precedencias, no job shops; comparten las ideas de búsqueda local y la referencia a Ruiz y Stützle.
- [Modelo de flujo en GAMS, Corte 2](../../corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-flujo-gams/): otro modelo del curso en GAMS.
