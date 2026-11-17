# Wagner-Whitin y Silver-Meal (Corte 2)

## Qué cubre

Dimensionamiento de lotes (*lot sizing*) con demanda dinámica y determinística en un horizonte finito: cuánto y cuándo producir para minimizar alistamiento + producción + inventario. El algoritmo de Wagner-Whitin (1958) da el óptimo exacto como una ruta más corta / programación dinámica; la heurística de Silver-Meal da un plan rápido de bajo costo sin garantizar el óptimo. Es la técnica con la que se dimensionan las liberaciones de órdenes del MRP ([carpeta 04](../04-bom-y-mrp/README.md)).

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [L12-wagner-whitin-and-silver-meal.md](./L12-wagner-whitin-and-silver-meal.md) | Presentación de clase (40 pp.): supuestos, propiedad de optimalidad, grafo de ruta más corta, recursión $Z_k$, ejemplo de 4 periodos resuelto con Wagner-Whitin y Silver-Meal. | Sí |
| [wagner_whitin.py](./wagner_whitin.py) | Script de Python (sin gemelo `.md`; se explica abajo) que aplica la recursión de Wagner-Whitin a 10 semanas de requerimientos netos de un componente del esfero. | Después de la L12 |

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

*Deducido:* esos requerimientos netos (2380 en la semana 3 y 2500 en la semana 5) coinciden exactamente con los de la **Tapa Arriba** en [mrp-esfero-v2](../04-bom-y-mrp/mrp-esfero-v2.md) (requerimiento bruto de 2460 en la semana 3 menos las 80 unidades disponibles, y 2500 en la semana 5). El costo de mantener 0.01 es el de la Tapa Arriba en ese Excel y el alistamiento de \$80 es el del Esfero y el Cuerpo. El comentario del código dice "cuerpo". El script no maneja tiempos de entrega: dimensiona lotes sobre los requerimientos netos (producción = recepción en ese periodo).

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

1. [L12](./L12-wagner-whitin-and-silver-meal.md), pp. 1-16: supuestos, propiedad $I_{t-1}P_t=0$, grafo y recursión.
2. [L12](./L12-wagner-whitin-and-silver-meal.md), pp. 17-33: ejemplo numérico completo (costos de arco y $Z_1..Z_4$).
3. [L12](./L12-wagner-whitin-and-silver-meal.md), pp. 34-40: Silver-Meal sobre el mismo ejemplo.
4. `wagner_whitin.py` (esta página): implementación y su error con periodos de demanda cero.
5. Aplicación en el MRP: [L14](../04-bom-y-mrp/L14-mrp.md), pp. 13-14, y [mrp-esfero-v2](../04-bom-y-mrp/mrp-esfero-v2.md).

## Conceptos y fórmulas clave

- Costo de producción: $k(p_t)=0$ si $p_t=0$; $k(p_t)=A_t+c\,p_t$ si $p_t>0$ ($A_t$: alistamiento, $c$: costo variable, $p_t$: producción).
- Propiedad de optimalidad: $I_{t-1}P_t=0$, por lo que $P_t\in\{0, D_t, D_t+D_{t+1},\dots\}$.
- Costo de arco: $C_{jk}=A_{j+1}+cP_{j+1}+\sum_{t=j+1}^{k-1}h_tI_t$ (producir en $j+1$ para cubrir $j+1..k$).
- Recursión: $Z_k=\min_{0\le j\le k-1}[Z_j^*+C_{jk}]$, $Z_0^*=0$.
- Silver-Meal (forma usual, coherente con los ejemplos): $K(t,p)=\dfrac{\text{costo total del lote que cubre } t..p}{p-t+1}$; se amplía el lote mientras $K$ baje.

Detalle y símbolos en el [resumen de la L12](./L12-wagner-whitin-and-silver-meal.md#resumen).

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado principal |
|---|---|---|
| Wagner-Whitin, 4 periodos ($D$ = 10, 30, 30, 20; setup 20, 40, 30, 50; $c=3$; $h$ = 2, 2, 1, 1) | [L12](./L12-wagner-whitin-and-silver-meal.md), pp. 15-33 | $Z_4=380$; producir 10, 30, 50, 0 |
| Silver-Meal, mismo ejemplo | [L12](./L12-wagner-whitin-and-silver-meal.md), pp. 37-39 | Lotes en los periodos 1, 2 y 3 (3+4); *deducido:* costo 380, igual al óptimo |
| Wagner-Whitin, 10 semanas de un componente del esfero | [wagner_whitin.py](./wagner_whitin.py) | Imprime \$207.6 (subóptimo por el error descrito); el óptimo real es \$130 |

## Relación con otros temas y proyectos

- [04 BOM y MRP](../04-bom-y-mrp/README.md): el MRP calcula requerimientos netos; Wagner-Whitin y Silver-Meal deciden cómo agruparlos en lotes ([L14](../04-bom-y-mrp/L14-mrp.md), p. 14).
- [02 Agregación y desagregación](../02-agregacion-y-desagregacion/) y [01 Planeación agregada](../01-planeacion-agregada-modelo-bowman/): niveles de planeación previos que fijan el programa maestro.
- [Parcial 2](../parcial-2/parcial-2-solucion.md): punto 2.4, Silver-Meal contra Wagner-Whitin.
- [Proyecto THYMS, gemelo digital](../proyecto-thyms-gemelo-digital/THYMS-presentacion-corte-2.md): propone aplicar Wagner-Whitin / Silver-Meal sobre el programa maestro como siguiente paso.
