# L14-mrp

> **Archivo:** [`L14-mrp.pdf`](./L14-mrp.pdf) · **Corte 2** · 21 páginas  
> **Nombre original:** `CORTE 2/Lec 14 - MRP.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** construcción de la tabla MRP nivel por nivel para el BOM de la [L13](./L13-bom-intro-to-mrp.md) (productos 1 y 2; ítems A, D, B, C, γ, α, β), con inventario disponible, *lead times* y MPS de 9 semanas. Luego se tratan el dimensionamiento de lotes, el MRP de ciclo cerrado y el nerviosismo del sistema.

### Ideas clave

- **Sistema MRP** (p. 2): MPS + BOM + archivo de estado del inventario → lógica MRP → programa de producción MRP.
- La tabla MRP de cada ítem tiene cinco filas por periodo: requerimientos brutos $G_{jt}$, entregas programadas $S_{jt}$, inventario esperado $I_{jt}$ (disponible al inicio del periodo), requerimientos netos $N_{jt}$ y liberación de órdenes planeadas (= recepción necesaria desplazada hacia atrás un *lead time*).
- **Procedimiento** (p. 10): (1) calcular la demanda directamente dependiente de cada periodo y cada producto con $dd(n)=d_n\times B$, usando las **liberaciones de órdenes** del nivel superior; (2) sumarla a los requerimientos brutos de los hijos (junto con su demanda independiente del MPS); (3) repetir hasta el último nivel. El requerimiento bruto de un hijo en la semana $t$ sale de las órdenes que liberan sus padres en esa semana $t$.
- Un ítem que aparece en varios niveles (B, C, γ, α) se planea **una sola vez**, en su nivel más bajo, después de todos sus padres.
- **Liberación de órdenes = problema de optimización (*lot sizing*)** (pp. 13-14): lote a lote (si ordenar cuesta poco), EOQ determinístico (supone demanda constante), Wagner-Whitin y Silver-Meal ([carpeta 03](../03-wagner-whitin-y-silver-meal/README.md)).
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

- [L13 BOM e intro al MRP](./L13-bom-intro-to-mrp.md): matriz BOM y niveles usados aquí.
- [calculo-demanda-dependiente-directa](./calculo-demanda-dependiente-directa.md): la misma explosión $d\times B$ en Excel.
- [mrp-esfero](./mrp-esfero.md) y [mrp-esfero-v2](./mrp-esfero-v2.md): la tabla MRP con las mismas fórmulas $I_{jt}$ y $N_{jt}$, armada en Excel ("CONSTRUIR EXCEL", p. 10).
- [Wagner-Whitin y Silver-Meal](../03-wagner-whitin-y-silver-meal/L12-wagner-whitin-and-silver-meal.md): políticas de dimensionamiento de lotes.
- [L15 MRP II](../05-mrp-ii-y-capacidad/L15-mrp-ii.md): MRP de ciclo cerrado y capacidad.
- [Parcial 2](../parcial-2/parcial-2-solucion.md): punto 2.3, matriz MRP.

## Contenido completo (página por página)

> Las diapositivas llevan una franja inferior con fotos del campus y el logo de la Universidad de La Sabana (o una franja lateral derecha); no se repite en cada página. En las tablas MRP, una celda vacía es una celda vacía en la diapositiva.

### Página 1 — Introducción al MRP

Portada: "Introducción al MRP". Foto del edificio de la biblioteca, logo de la Universidad de La Sabana y licencia Creative Commons BY-NC-SA.

### Página 2 — Sistema MRP

> [Diagrama: tres círculos apilados, **MPS - master production schedule** + **BOM** + **Inventory Status file**, con una flecha hacia un círculo negro **MRP Logic** y otra flecha hacia un óvalo **MRP Production Schedule**.]

### Página 3 — Ejemplo de status de inventario

| Nivel | Item | Inventario a la mano (t=0) | Lead time |
|---|---|---|---|
| 0 | 1 | 120 | 1 |
| 0 | 2 | 85 | 1 |
| 1 | A | 0 | 2 |
| 1 | D | 10 | 2 |
| 2 | B | 500 | 1 |
| 3 | C | 160 | 1 |
| 3 | γ | 0 | 2 |
| 4 | α | 1200 | 1 |
| 4 | β | 4000 | 2 |

### Página 4 — MPS en semanas

| Item | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| **1** | 50 | 20 | 30 | 40 | 40 | 30 | 25 | 15 | 30 |
| **2** | 20 | 30 | 25 | 35 | 10 | 35 | 20 | 25 | 30 |
| **A** | | | | | | | | 15 | |
| **D** | | 10 | | 10 | | | | | |
| **B** | | | | | 20 | | | | 100 |
| **C** | | 5 | | | | | | | |
| **γ** | | | | | | | | | |
| **α** | | | | | | | | | |
| **β** | | | | | | | | | |

(Encabezado: PERIODO.)

### Página 5 — MRP – nivel 0

**Item 1, nivel 0**

| Periodo | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Requerimientos Brutos | 50 | 20 | 30 | 40 | 40 | 30 | 25 | 15 | 30 |
| Entregas programadas | | | | 120 | | | | | |
| Inventario esperado | 120 | 70 | 50 | 20 | 100 | 60 | 30 | 5 | 0 |
| Requerimientos netos | | | | | | | | 10 | 30 |
| Liberación de orden planeada | | | 120 | | | | 120 | | |

**Item 2, nivel 0**

| Periodo | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Requerimientos Brutos | 20 | 30 | 25 | 35 | 10 | 35 | 20 | 25 | 30 |
| Entregas programadas | | | | 100 | | | | | |
| Inventario esperado | 85 | 65 | 35 | 10 | 75 | 65 | 30 | 10 | 0 |
| Requerimientos netos | | | | | | | | 15 | 30 |
| Liberación de orden planeada | | | 100 | | | | 100 | | |

> [Anotación: un recuadro amarillo con la fórmula $I_{jt}=\max\{0, I_{jt-1}+S_{jt-1}-G_{jt-1}\}$ apunta a la fila "Inventario esperado"; flechas amarillas marcan $G_{jt}$ en "Requerimientos Brutos" y $S_{jt}$ en "Entregas programadas".]

### Página 6 — MRP – nivel 0

Misma tabla de la p. 5 (ítems 1 y 2, idénticos).

> [Anotación: recuadro amarillo con $N_{jt}=\max\{0, G_{jt}-S_{jt}-I_{jt}\}$; una flecha $N_{jt}$ señala la fila "Requerimientos netos".]

### Página 7 — MRP – nivel 1

- Determinación de requerimientos para la **semana 7**:
- $dd(0)=d_0 X B$
- $dd(0) = (120\ 100\ 0\dots0)\ X\ B$
- $= (0\ 0\ 240\ 100\ 100\ 120\ 300\ 0\ 0)$

### Página 8 — MRP – nivel 1

| ITEM | Desde nivel 0 | Otro | Total |
|---|---|---|---|
| A | 240 | 0 | 240 |
| D | 100 | 0 | 100 |
| B | 100 | 0 | 100 |
| C | 120 | 0 | 120 |
| γ | 300 | 0 | 300 |

### Página 9 — MRO hasta nivel 1

Ítems 1 y 2: idénticos a la p. 5. Lo nuevo:

**Item A, nivel 1**

| Periodo | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Requerimientos Brutos | 0 | 0 | 240 | 0 | 0 | 0 | 240 | 15 | 0 |
| Entregas programadas | | | 240 | | | | | | |
| Inventario esperado | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Requerimientos netos | | | | | | | 240 | 15 | |
| Liberación de orden planeada | 240 | | | | 240 | 15 | | | |

**Item D, nivel 1**

| Periodo | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Requerimientos Brutos | 0 | 10 | 100 | 10 | 0 | 0 | 100 | 0 | 0 |
| Entregas programadas | | 10 | 100 | 10 | | | | | |
| Inventario esperado | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Requerimientos netos | | | | | | | 100 | | |
| Liberación de orden planeada | 100 | 10 | | | 100 | | | | |

**Item B, nivel 2**: Requerimientos Brutos = 100 (sem. 3), 20 (sem. 5), 100 (sem. 7), 100 (sem. 9); las demás filas están vacías.

**Item C, nivel 3**: Requerimientos Brutos = 5 (sem. 2), 120 (sem. 3), 120 (sem. 7); las demás filas están vacías.

**Item γ, nivel 3**: Requerimientos Brutos = 300 (sem. 3), 300 (sem. 7) (la tabla se corta ahí).

> [Anotaciones a mano: un óvalo amarillo rodea los requerimientos brutos y la entrega programada del ítem 1; una flecha roja baja desde la liberación de 100 del ítem 2 en la semana 3, pasa por la columna 3 de A y llega al requerimiento bruto de 100 de B en la semana 3. Muestra que la orden liberada por el padre se convierte en requerimiento bruto del hijo en la misma semana.]

En esta etapa los requerimientos de B, C y γ solo incluyen lo que viene de los productos 1 y 2 y del MPS; faltan los que generan A y D.

### Página 10 — Pasos para construir un MRP completo

1. Calcule la demanda directamente dependiente para cada periodo, para cada producto.
2. Actualice los requerimientos brutos.
3. Repita el paso 1 hasta llegar al ultimo nivel.

***CONSTRUIR EXCEL***

### Página 11 — MRP Nivel 2

- $dd(1)=d_1\times B$

Usando las ordenes planeadas para la semana 5:

- $= (0\ 0\ \ 240\ 100\ 0\ 0\ 0\ 0\ 0)\times B$
- $= (0\ 0\ \ \ 0\ \ 0\ \ \ 440\ 100\ \ 480\ 0)$

### Página 12 — Al final de las iteraciones:

Tabla MRP completa (semanas 1 a 9):

**Item 1, nivel 0**

| Periodo | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Requerimientos Brutos | 50 | 20 | 30 | 40 | 40 | 30 | 25 | 15 | 30 |
| Entregas programadas | | | | 120 | | | | | |
| Inventario esperado | 120 | 70 | 50 | 20 | 100 | 60 | 30 | 5 | 0 |
| Requerimientos netos | | | | | | | | 10 | 30 |
| Liberación de orden planeada | | | 120 | | | | 120 | | |

**Item 2, nivel 0**

| Periodo | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Requerimientos Brutos | 20 | 30 | 25 | 35 | 10 | 35 | 20 | 25 | 30 |
| Entregas programadas | | | | 100 | | | | | |
| Inventario esperado | 85 | 65 | 35 | 10 | 75 | 65 | 30 | 10 | 0 |
| Requerimientos netos | | | | | | | | 15 | 30 |
| Liberación de orden planeada | | | 100 | | | | 100 | | |

**Item A, nivel 1**

| Periodo | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Requerimientos Brutos | 0 | 0 | 240 | 0 | 0 | 0 | 240 | 15 | 0 |
| Entregas programadas | | | 240 | | | | | | |
| Inventario esperado | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Requerimientos netos | | | | | | | 240 | 15 | |
| Liberación de orden planeada | 240 | | | | 240 | 15 | | | |

**Item D, nivel 1**

| Periodo | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Requerimientos Brutos | 0 | 10 | 100 | 10 | 0 | 0 | 100 | 0 | 0 |
| Entregas programadas | | 10 | 100 | 10 | | | | | |
| Inventario esperado | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Requerimientos netos | | | | | | | 100 | | |
| Liberación de orden planeada | 100 | 10 | | | 100 | | | | |

**Item B, nivel 2**

| Periodo | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Requerimientos Brutos | 440 | 20 | 100 | 0 | 460 | 15 | 100 | 0 | 100 |
| Entregas programadas | 560 | | | | | | | | |
| Inventario esperado | 0 | 120 | 100 | 0 | 0 | 0 | 0 | 0 | 0 |
| Requerimientos netos | | | | | 460 | 15 | 100 | | 100 |
| Liberación de orden planeada | | | | 575 | | | | 100 | |

**Item C, nivel 3**

| Periodo | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Requerimientos Brutos | 100 | 15 | 120 | 1150 | 100 | 0 | 120 | 200 | 0 |
| Entregas programadas | 115 | | 120 | | | | | | |
| Inventario esperado | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Requerimientos netos | | | | 1150 | 100 | | 120 | 200 | |
| Liberación de orden planeada | | 120 | 1250 | | | 320 | | | |

**Item γ, nivel 3**

| Periodo | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Requerimientos Brutos | 0 | 0 | 300 | 575 | 0 | 0 | 300 | 100 | 0 |
| Entregas programadas | | | 300 | | | | | | |
| Inventario esperado | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Requerimientos netos | | | | 575 | | | 300 | 100 | |
| Liberación de orden planeada | 300 | 575 | | | 300 | 100 | | | |

**Item α, nivel 4**

| Periodo | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Requerimientos Brutos | 480 | 120 | 1250 | 0 | 480 | 350 | 0 | 0 | 0 |
| Entregas programadas | | | | | | | | | |
| Inventario esperado | 3000 | 2520 | 2400 | 1150 | 1150 | 670 | 320 | 320 | 320 |
| Requerimientos netos | | | | | | | | | |
| Liberación de orden planeada | | | | | | | | | |

**Item β, nivel 4**

| Periodo | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Requerimientos Brutos | 0 | 360 | 3750 | 0 | 0 | 960 | 0 | 0 | 0 |
| Entregas programadas | | | | | | | | | |
| Inventario esperado | 4000 | 4000 | 3640 | 0 | 0 | 0 | 0 | 0 | 0 |
| Requerimientos netos | | | 110 | | | 960 | | | |
| Liberación de orden planeada | 2000 | | | | | | | | |

> [Anotaciones a mano: una línea amarilla subraya los requerimientos brutos del ítem 1 y una marca roja señala las filas "Requerimientos Brutos" y "Liberación de orden planeada" del ítem 1.]

De dónde salen los requerimientos brutos de los niveles bajos (verificación de esta transcripción con la matriz BOM de la L13): B en la semana 1 = 240 (A) + 2·100 (D) = 440; B en la semana 5 = 240 (A) + 2·100 (D) + 20 (MPS) = 460; C en la semana 4 = 2·575 (B) = 1150; γ en la semana 4 = 575 (B); α en la semana 3 = 1250 (C); α en la semana 6 = 2·15 (A) + 320 (C) = 350; β en la semana 3 = 3·1250 (C) = 3750; β en la semana 6 = 3·320 = 960.

### Página 13 — Determinación de liberación de ordenes programadas

- Problema de optimización
- *Lot sizing*: dimensionamiento de lotes

### Página 14 — Políticas de dimensionamiento de lotes:

- *Lote-a-lote:* ordenar lo requerido por periodo. Costo de ordenar es despreciable.
- EOQ determinístico: Asumen demanda constante.
- **Wagner-Whitin**
- **Silver Meal**

Recuadro con la fórmula:

$$Q^*=\sqrt{\frac{2DK}{h}}$$

### Página 15 — MRP de ciclo Cerrado

- Cada módulo realimenta los módulos anteriores para informar si hay ajustes por hacer.
  - Ejemplo: Se excede la capacidad de producción, faltantes de inventario.

### Página 16 — MRP de ciclo cerrado

> [Diagrama: seis flechas tipo chevrón en secuencia: **Plan de Producción** → **Programa maestro de producción** → **Planeación de necesidades de material** → **Revisar factibilidad** → **Ejecución de planes de capacidad** → **Ejecución de planes de materiales**. Debajo, flechas rojas curvas de realimentación hacia atrás: de Programa maestro a Plan de Producción; de Planeación de necesidades a Programa maestro; de Revisar factibilidad a Planeación de necesidades y a Programa maestro; de Ejecución de planes de capacidad y de Ejecución de planes de materiales a Planeación de necesidades.]

### Página 17 — NERVIOSISMO

- Ocurre cuando los requerimientos brutos de un producto varían, Esto puede ocurrir cuando las cantidades MPS se incrementan o disminuyen para reflejar cambios en las órdenes o en los pronósticos de la demanda del producto final.
- Al cambiar el MPS a causa de la incertidumbre en la demanda, el plan de producción anteriormente propuesto tendrá que ser replanteado según la nueva información disponible. Los frecuentes cambios que se hagan en el MPS provocarán a su vez efectos sobre el sistema MRP y sobre el sistema de producción, ocasionando nerviosismo en todo el sistema de planificación de producción, con sobrecostos, confusión y reducción de la productividad.

### Página 18 — NERVIOSISMO

- Nerviosismo está relacionado con pequeños cambios en los niveles altos (producto terminado) que generan grandes cambios en los niveles bajos.
- Efecto de cascada (cascading)
- Ocurre cuando se hacen cambios frecuentes en los planes de producción
- Más sensible a cambios en períodos cercanos a la fecha actual

### Página 19 — EJEMPLO

> [Diagrama: BOM de dos niveles: **A** (τ = 0) → **B (2)** (τ = 3). Cada A requiere 2 B; τ es el *lead time*.]

**A** (Pron = pronóstico, RP = recepciones programadas, INV = inventario, LOP = liberación de órdenes planeadas)

| A | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Pron | | 45 | 55 | 45 | 35 |
| RP | | | | | |
| INV | 10 | 55 | 0 | 35 | 0 |
| LOP | | 90 | | 80 | |

**B** (RB = requerimiento bruto)

| B | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| RB | | 180 | | 160 | |
| RP | | 340 | | | |
| INV | 0 | 160 | 160 | 0 | 0 |
| LOP | | | | | |

(El 55 del periodo 2 de A está encerrado en un círculo rojo.)

Supongamos que hoy es el principio del periodo 1 y se cambia el RB de A del periodo 2 a 60

### Página 20 — EJEMPLO

Mismo BOM (A τ = 0 → B (2) τ = 3). Celdas que cambian resaltadas en rojo:

| A | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Pron | | 45 | **60** | 45 | 35 |
| RP | | | | | |
| INV | 10 | 60 | 0 | 35 | 0 |
| LOP | | **95** | | 80 | |

| B | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| RB | | **190** | | 160 | |
| RP | | 340 | | | |
| INV | 0 | **150** | **150** | **-10** | **-10** |
| LOP | | | | | |

Se pueden pedir 5 unidades adicionales de A en el periodo 1 (95 en vez de 90) pero ya no se pueden pedir cantidades de B en el periodo 1 para cubrir la demanda extra ¿por qué?

### Página 21 — Soluciones al nerviosismo

- Stock de seguridad
- Tiempo de preparación (lead time) de seguridad
- Congelamiento del MPS

Sin embargo, estas alternativas ocasionan:

- Un incremento en los niveles de inventario,
- Las programación realizada no concuerda con lo que se necesita o requiere

## Anexo: texto extraído automáticamente del PDF

> Texto plano tal como sale del PDF, sin fórmulas ni tablas que estén como imagen. La versión fiel y completa es la sección «Contenido completo» de arriba.

### Página 1 · 2 imagen(es)

Introducción al MRP

### Página 2 · 3 imagen(es)

Sistema MRP
MPS- 
master 
production 
schedule
BOM 
Inventory 
Status file
MRP 
Logic
MRP 
Production 
Schedule

### Página 3 · 1 imagen(es)

Ejemplo de status de inventario
Nivel
Item
Inventario a la 
mano (t=0)
Lead time
0
1
120
1
0
2
85
1
1
A
0
2
1
D
10
2
2
B
500
1
3
C
160
1
3
γ
0
2
4
α
1200
1
4
β
4000
2

### Página 4 · 1 imagen(es)

MPS en semanas
PERIODO
Item
1
2
3
4
5
6
7
8
9
1
50
20
30
40
40
30
25
15
30
2
20
30
25
35
10
35
20
25
30
A
15
D
10
10
B
20
100
C
5
γ
α
β

### Página 5 · 1 imagen(es)

MRP – nivel 0
Periodo
1
2
3
4
5
6
7
8
9
Item 1, nivel 0
Requerimientos Brutos
50
20
30
40
40
30
25
15
30
Entregas programadas
120
Inventario esperado
120
70
50
20
100
60
30
5
0
Requerimientos netos
10
30
Liberación de orden planeada
120
120
Item 2, nivel 0
Requerimientos Brutos
20
30
25
35
10
35
20
25
30
Entregas programadas
100
Inventario esperado
85
65
35
10
75
65
30
10
0
Requerimientos netos
15
30
Liberación de orden planeada
100
100
𝐼𝑗𝑡= max{0, 𝐼𝑗𝑡−1 + 𝑆𝑗𝑡−1 −𝐺𝑗𝑡−1} 
𝑆𝑗𝑡
𝐺𝑗𝑡

### Página 6 · 1 imagen(es)

MRP – nivel 0
Periodo
1
2
3
4
5
6
7
8
9
Item 1, nivel 0
Requerimientos Brutos
50
20
30
40
40
30
25
15
30
Entregas programadas
120
Inventario esperado
120
70
50
20
100
60
30
5
0
Requerimientos netos
10
30
Liberación de orden planeada
120
120
Item 2, nivel 0
Requerimientos Brutos
20
30
25
35
10
35
20
25
30
Entregas programadas
100
Inventario esperado
85
65
35
10
75
65
30
10
0
Requerimientos netos
15
30
Liberación de orden planeada
100
100
𝑁𝑗𝑡
𝑁𝑗𝑡= max{ 0, 𝐺𝑗𝑡 −𝑆𝑗𝑡 −𝐼𝑗𝑡}

### Página 7 · 1 imagen(es)

MRP – nivel 1
• Determinación de requerimientos para la semana 
7:
• 𝑑𝑑0 = 𝑑0𝑋 𝐵
• 𝑑𝑑0 = (120 100 0…0) X B
• = ( 0 0 240 100 100 120 300 0 0)

### Página 8 · 1 imagen(es)

MRP – nivel 1
ITEM
Desde nivel 0
Otro
Total
A
240
0
240
D
100
0
100
B
100
0
100
C
120
0
120
γ
300
0
300

### Página 9 · 2 imagen(es)

MRO hasta nivel 1
Periodo
1
2
3
4
5
6
7
8
9
Item 1, nivel 0
Requerimientos Brutos
50
20
30
40
40
30
25
15
30
Entregas programadas
120
Inventario esperado
120
70
50
20
100
60
30
5
0
Requerimientos netos
10
30
Liberación de orden planeada
120
120
Item 2, nivel 0
Requerimientos Brutos
20
30
25
35
10
35
20
25
30
Entregas programadas
100
Inventario esperado
85
65
35
10
75
65
30
10
0
Requerimientos netos
15
30
Liberación de orden planeada
100
100
Item A, nivel 1
Requerimientos Brutos
0
0
240
0
0
0
240
15
0
Entregas programadas
240
Inventario esperado
0
0
0
0
0
0
0
0
0
Requerimientos netos
240
15
Liberación de orden planeada
240
240
15
Item D, nivel 1
Requerimientos Brutos
0
10
100
10
0
0
100
0
0
Entregas programadas
10
100
10
Inventario esperado
0
0
0
0
0
0
0
0
0
Requerimientos netos
100
Liberación de orden planeada
100
10
100
Item B, nivel 2
Requerimientos Brutos
100
20
100
100
Entregas programadas
Inventario esperado
Requerimientos netos
Liberación de orden planeada
Item C, nivel 3
Requerimientos Brutos
5
120
120
Entregas programadas
Inventario esperado
Requerimientos netos
Liberación de orden planeada
Item γ, nivel 3
300
300

### Página 10 · 1 imagen(es)

Pasos para construir un MRP 
completo
1. Calcule la demanda directamente 
dependiente para cada periodo, para 
cada producto.
2. Actualice los requerimientos brutos.
3. Repita el paso 1 hasta llegar al ultimo 
nivel.
CONSTRUIR EXCEL

### Página 11 · 1 imagen(es)

MRP Nivel 2
• 𝑑𝑑1 = 𝑑1 × 𝐵 
Usando las ordenes planeadas para la 
semana 5:
• = (0 0 240 100 0 0 0 0 0 ) × 𝐵 
• = (0 0 0 0 440 100 480 0 )

### Página 12 · 2 imagen(es)

Al final de las 
iteraciones:
Periodo
1
2
3
4
5
6
7
8
9
Item 1, nivel 0
Requerimientos Brutos
50
20
30
40
40
30
25
15
30
Entregas programadas
120
Inventario esperado
120
70
50
20
100
60
30
5
0
Requerimientos netos
10
30
Liberación de orden planeada
120
120
Item 2, nivel 0
Requerimientos Brutos
20
30
25
35
10
35
20
25
30
Entregas programadas
100
Inventario esperado
85
65
35
10
75
65
30
10
0
Requerimientos netos
15
30
Liberación de orden planeada
100
100
Item A, nivel 1
Requerimientos Brutos
0
0
240
0
0
0
240
15
0
Entregas programadas
240
Inventario esperado
0
0
0
0
0
0
0
0
0
Requerimientos netos
240
15
Liberación de orden planeada
240
240
15
Item D, nivel 1
Requerimientos Brutos
0
10
100
10
0
0
100
0
0
Entregas programadas
10
100
10
Inventario esperado
0
0
0
0
0
0
0
0
0
Requerimientos netos
100
Liberación de orden planeada
100
10
100
Item B, nivel 2
Requerimientos Brutos
440
20
100
0
460
15
100
0
100
Entregas programadas
560
Inventario esperado
0
120
100
0
0
0
0
0
0
Requerimientos netos
460
15
100
100
Liberación de orden planeada
575
100
Item C, nivel 3
Requerimientos Brutos
100
15
120
1150
100
0
120
200
0
Entregas programadas
115
120
Inventario esperado
0
15
0
0
0
0
0
0
0
Requerimientos netos
1150
100
120
200
Liberación de orden planeada
120
1250
320
Item γ, nivel 3
Requerimientos Brutos
0
0
300
575
0
0
300
100
0
Entregas programadas
300
Inventario esperado
0
0
0
0
0
0
0
0
0
Requerimientos netos
575
300
100
Liberación de orden planeada
300
575
300
100
Item α, nivel 4
Requerimientos Brutos
480
120
1250
0
480
350
0
0
0
Entregas programadas
Inventario esperado
3000
2520
2400
1150
1150
670
320
320
320
Requerimientos netos
Liberación de orden planeada
Item β, nivel 4
Requerimientos Brutos
0
360
3750
0
0
960
0
0
0
Entregas programadas
Inventario esperado
4000
4000
3640
0
0
0
0
0
0
Requerimientos netos
110
960
Liberación de orden planeada
2000

### Página 13 · 1 imagen(es)

Determinación de liberación de 
ordenes programadas 
• Problema de optimización
• Lot sizing: dimensionamiento de lotes

### Página 14 · 2 imagen(es)

Políticas de dimensionamiento de 
lotes:
• Lote-a-lote: ordenar lo requerido por periodo. 
Costo de ordenar es despreciable.
• EOQ determinístico: Asumen demanda constante. 
• Wagner-Whitin
• Silver Meal

### Página 15 · 1 imagen(es)

MRP de ciclo Cerrado
• Cada módulo realimenta los módulos 
anteriores para informar si hay ajustes por 
hacer. 
– Ejemplo: Se excede la capacidad de 
producción, faltantes de inventario.

### Página 16 · 7 imagen(es)

MRP de ciclo cerrado
Plan de 
Producción
Programa 
maestro de 
producción
Planeación 
de 
necesidades 
de material
Revisar 
factibilidad
Ejecución de 
planes de 
capacidad
Ejecución de 
planes de 
materiales

### Página 17 · 1 imagen(es)

NERVIOSISMO
•
Ocurre cuando los requerimientos brutos de un producto 
varían, Esto puede ocurrir cuando las cantidades MPS se 
incrementan o disminuyen para reflejar cambios en las 
órdenes o en los pronósticos de la demanda del producto 
final. 
•
Al cambiar el MPS a causa de la incertidumbre en la 
demanda, el plan de producción anteriormente propuesto 
tendrá que ser replanteado según la nueva información 
disponible. Los frecuentes cambios que se hagan en el 
MPS provocarán a su vez efectos sobre el sistema MRP y 
sobre el sistema de producción, ocasionando nerviosismo 
en todo el sistema de planificación de producción, con 
sobrecostos, confusión y reducción de la productividad.

### Página 18 · 1 imagen(es)

NERVIOSISMO
• Nerviosismo está relacionado con pequeños 
cambios en los niveles altos (producto terminado) 
que generan grandes cambios en los niveles bajos. 
• Efecto de cascada (cascading) 
• Ocurre cuando se hacen cambios frecuentes en los 
planes de producción 
• Más sensible a cambios en períodos cercanos a la 
fecha actual

### Página 19 · 3 imagen(es)

EJEMPLO
Supongamos que hoy es el principio del periodo 1 
y se cambia el RB de A del periodo 2 a 60

### Página 20 · 3 imagen(es)

EJEMPLO
Se pueden pedir 5 unidades adicionales de A en el periodo 1 
(95 en vez de 90) pero ya no se pueden pedir cantidades de B 
en el periodo 1 para cubrir la demanda extra ¿por qué?

### Página 21 · 1 imagen(es)

Soluciones al 
nerviosismo
• Stock de seguridad
• Tiempo de preparación (lead time) de seguridad 
• Congelamiento del MPS 
Sin embargo, estas alternativas ocasionan: 
• Un incremento en los niveles de inventario, 
• Las programación realizada no concuerda con lo que 
se necesita o requiere

