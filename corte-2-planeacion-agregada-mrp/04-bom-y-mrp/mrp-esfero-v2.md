# mrp-esfero-v2

> **Archivo:** [`mrp-esfero-v2.xlsx`](./mrp-esfero-v2.xlsx) · **Corte 2** · Libro de Excel con 1 hoja(s): `Hoja1`  
> **Nombre original:** `CORTE 2/MRP 2.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Segunda versión, corregida y ampliada, del MRP del **esfero** de [mrp-esfero](./mrp-esfero.md). Una hoja (`Hoja1`) con 6 tablas MRP de 10 semanas, una por ítem del BOM, enlazadas con fórmulas: el requerimiento bruto de cada componente sale de las liberaciones de órdenes de su padre multiplicadas por la cantidad del BOM. Cada ítem tiene su *lead time* y sus costos de ordenar y de mantener. Aplica la explosión nivel por nivel de la [L14](./L14-mrp.md) (pp. 7-12) y la idea de la [L13](./L13-bom-intro-to-mrp.md) de que la demanda de los componentes es dependiente.

Se aprende: cómo la liberación del padre se convierte en requerimiento bruto del hijo, cómo cambia la fecha de recepción según el *lead time* (3, 2, 1 o 0 semanas) y cómo verificar la factibilidad (requerimiento neto = 0).

### BOM y parámetros (deducidos de las fórmulas y rótulos)

Árbol del producto (cantidad por unidad del padre, *lead time*, inventario inicial):

- **Esfero** (nivel 0; LT = 3; inventario 1200; recepción programada de 500 en la semana 1)
  - **Cuerpo** ×1 (nivel 1; LT = 2; inventario 700): `D10 = D7`
    - **Cilindro** ×1 (nivel 2; LT = 0; inventario 0): `D31 = D14`
    - **Mina de Tinta** ×1 (nivel 2; LT = 0; inventario 0): `D38 = D14`
  - **Tapa Arriba** ×2 (nivel 1; LT = 1; inventario 1300): `D17 = 2*D7`
  - **Tapa** ×1 (nivel 1; LT = 0; inventario 0): `D24 = D7`

| Ítem | Filas | LT | Inv. inicial | Recepción = liberación de… | Costo de ordenar (celda) | Costo de mantener (celda) |
|---|---|---|---|---|---|---|
| Esfero | 2-7 | 3 | 1200 (D5) | 3 periodos antes (`G4 = D7`) | `P3 = 80*COUNTIF(D7:J7,">0")` | `P4 = 0.05*SUM(D5:M5)` |
| Cuerpo | 9-14 | 2 | 700 (D12) | 2 periodos antes (`F11 = D14`) | `P10 = 80*COUNTIF(D14:J14,">0")` | `P11 = 0.04*SUM(D12:K12)` |
| Tapa Arriba | 16-21 | 1 | 1300 (D19) | 1 periodo antes (`E18 = D21`) | `P17 = 10*COUNTIF(D21:J21,">0")` | `P18 = 0.01*SUM(D19:K19)` |
| Tapa | 23-28 | 0 | 0 (D26) | mismo periodo (`D25 = D28`) | P24 = 50 (escrito a mano) | P25 = 1500 (escrito a mano) |
| Cilindro | 30-35 | 0 | 0 (D33) | mismo periodo (`D32 = D35`) | `P31 = 5*COUNTIF(D35:J35,">0")` | `P32 = 0.01*SUM(D33:K33)` |
| Mina de Tinta | 37-42 | 0 | 0 (D40) | mismo periodo (`D39 = D42`) | `P38 = 4*COUNTIF(D42:J42,">0")` | `P39 = 0.01*SUM(D40:K40)` |

En cada bloque: costo total = suma de las dos celdas de costo (P5, P12, P19, P26, P33, P40).

### Método (igual en los 6 bloques)

Con $t$ = periodo (columnas D a M = semanas 1 a 10):

- Inventario esperado al inicio de la semana: $I_t=\max\{0, I_{t-1}+S_{t-1}-G_{t-1}\}$ (p. ej. `E12 = MAX(0,D12+D11-D10)`).
- Requerimiento neto: $N_t=\max\{0, G_t-S_t-I_t\}$ (p. ej. `E13 = MAX(0,E10-E11-E12)`).
- Entregas programadas: $S_t=L_{t-LT}$; los periodos anteriores al primer arribo posible valen 0 (salvo el 500 del esfero).
- Requerimiento bruto de un hijo: $G^{hijo}_t=q\cdot L^{padre}_t$, con $q$ la cantidad del BOM.
- Liberación de órdenes $L_t$: **variable de decisión** escrita a mano en los periodos 1-7; "X" en los periodos 8-10.
- Costo de ordenar = tarifa × número de liberaciones $>0$ en los periodos 1-7; costo de mantener = tarifa × suma del inventario esperado (al inicio de cada periodo).

### Bloque Esfero (filas 2-7), LT = 3

Idéntico al bloque 1 de [mrp-esfero](./mrp-esfero.md).

| Fila | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 | P10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Requerimiento bruto | 300 | 400 | 500 | 550 | 560 | 700 | 530 | 550 | 400 | 300 |
| Entregas programadas | 500 | 0 | 0 | 610 | 0 | 1230 | 0 | 1250 | 0 | 0 |
| *Recepción de órdenes planeadas (derivada)* | | | | 610 | 0 | 1230 | 0 | 1250 | 0 | 0 |
| Inventario esperado | 1200 | 1400 | 1000 | 500 | 560 | 0 | 530 | 0 | 700 | 300 |
| Requerimiento neto | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Liberación de órdenes planeadas | 610 | 0 | 1230 | 0 | 1250 | 0 | 0 | X | X | X |

Costos: ordenar $80\times3=240$; mantener $0.05\times6190=309.5$; **total 549.5**. Factible.

### Bloque Cuerpo (filas 9-14), LT = 2, 1 por esfero

| Fila | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 | P10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Requerimiento bruto (= liberación del esfero) | 610 | 0 | 1230 | 0 | 1250 | 0 | 0 | X | X | X |
| Entregas programadas | 0 | 0 | 1140 | 0 | 1250 | 0 | 0 | 0 | 0 | X |
| Inventario esperado | 700 | 90 | 90 | 0 | 0 | 0 | 0 | 0 | #VALUE! | #VALUE! |
| Requerimiento neto | 0 | 0 | 0 | 0 | 0 | 0 | 0 | #VALUE! | #VALUE! | #VALUE! |
| Liberación de órdenes planeadas | 1140 | 0 | 1250 | 0 | 0 | 0 | 0 | X | X | X |

Lógica: las 700 unidades cubren la semana 1 (sobran 90). La orden de 1140 de la semana 1 llega en la 3 y, con las 90, cubre exactamente 1230. La orden de 1250 de la semana 3 llega en la 5. Costos: ordenar $80\times2=160$; mantener $0.04\times(700+90+90)=35.2$; **total 195.2**. Factible (neto 0 en las semanas 1-7) y sin inventario sobrante.

### Bloque Tapa Arriba (filas 16-21), LT = 1, 2 por esfero

| Fila | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 | P10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Requerimiento bruto (= 2 × liberación del esfero) | 1220 | 0 | 2460 | 0 | 2500 | 0 | 0 | #VALUE! | #VALUE! | #VALUE! |
| Entregas programadas | 0 | 2380 | 0 | 2500 | 0 | 0 | 0 | 0 | X | X |
| Inventario esperado | 1300 | 80 | 2460 | 0 | 2500 | 0 | 0 | 0 | #VALUE! | #VALUE! |
| Requerimiento neto | 0 | 0 | 0 | 0 | 0 | 0 | 0 | #VALUE! | #VALUE! | #VALUE! |
| Liberación de órdenes planeadas | 2380 | 0 | 2500 | 0 | 0 | 0 | 0 | X | X | X |

Lógica: 1300 en inventario cubren las 1220 de la semana 1 (sobran 80). Se necesitan $2460-80=2380$ para la semana 3 y 2500 para la semana 5. Las órdenes se liberan en las semanas 1 y 3 y llegan en la 2 y la 4, **un periodo antes de lo necesario**. Costos: ordenar $10\times2=20$; mantener $0.01\times(1300+80+2460+0+2500)=63.4$; **total 83.4**. Factible.

*Deducido:* liberando en las semanas 2 y 4 (justo a tiempo con LT = 1), el costo de mantener bajaría a $0.01\times(1300+80+80)=14.6$ y el total a 34.6. Los requerimientos netos de este ítem (2380 en la semana 3 y 2500 en la semana 5) son exactamente la demanda que usa [`wagner_whitin.py`](../03-wagner-whitin-y-silver-meal/README.md).

### Bloque Tapa (filas 23-28), LT = 0, 1 por esfero (sin resolver)

| Fila | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 | P10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Requerimiento bruto (= liberación del esfero) | 610 | 0 | 1230 | 0 | 1250 | 0 | 0 | X | X | X |
| Entregas programadas (= liberación del mismo periodo) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | X | X | X |
| Inventario esperado | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | #VALUE! | #VALUE! |
| Requerimiento neto | 0 | 0 | **1230** | 0 | **1250** | 0 | 0 | #VALUE! | #VALUE! | #VALUE! |
| Liberación de órdenes planeadas | 0 | 0 | 0 | 0 | 0 | 0 | 0 | X | X | X |

No hay órdenes, así que faltan 610 (semana 1, oculto, ver observaciones), 1230 y 1250. Costos escritos a mano: ordenar 50, mantener 1500, **total 1550**. *Deducido:* con LT = 0, el plan lote a lote sería liberar 610, 1230 y 1250 en las semanas 1, 3 y 5.

### Bloque Cilindro (filas 30-35), LT = 0, 1 por cuerpo

| Fila | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 | P10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Requerimiento bruto (= liberación del cuerpo) | 1140 | 0 | 1250 | 0 | 0 | 0 | 0 | X | X | X |
| Entregas programadas | 0 | 0 | 1250 | 0 | 0 | 0 | 0 | X | X | X |
| Inventario esperado | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | #VALUE! | #VALUE! |
| Requerimiento neto | 0 | 0 | 0 | 0 | 0 | 0 | 0 | #VALUE! | #VALUE! | #VALUE! |
| Liberación de órdenes planeadas | 0 | 0 | 1250 | 0 | 0 | 0 | 0 | X | X | X |

Costos: ordenar $5\times1=5$; mantener $0.01\times0=0$; **total 5**. El requerimiento de 1140 de la semana 1 **no se cubre**, pero el neto aparece en 0 porque `D34 = D35` en lugar de la fórmula de neto.

### Bloque Mina de Tinta (filas 37-42), LT = 0, 1 por cuerpo

| Fila | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 | P10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Requerimiento bruto (= liberación del cuerpo) | 1140 | 0 | 1250 | 0 | 0 | 0 | 0 | X | X | X |
| Entregas programadas | 0 | 0 | 1250 | 0 | 0 | 0 | 0 | X | X | X |
| Inventario esperado | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | #VALUE! | #VALUE! |
| Requerimiento neto | 0 | 0 | 0 | 0 | 0 | 0 | 0 | #VALUE! | #VALUE! | #VALUE! |
| Liberación de órdenes planeadas | 0 | 0 | 1250 | 0 | 0 | 0 | 0 | X | X | X |

Costos: ordenar $4\times1=4$; mantener 0; **total 4**. Mismo problema que el cilindro: la semana 1 (1140) queda sin cubrir y el neto se ve en 0 por `D41 = D42`.

### Resultados globales

| Ítem | Liberaciones (semana: cantidad) | ¿Factible? | Costo total |
|---|---|---|---|
| Esfero | 1: 610; 3: 1230; 5: 1250 | Sí | 549.5 |
| Cuerpo | 1: 1140; 3: 1250 | Sí | 195.2 |
| Tapa Arriba | 1: 2380; 3: 2500 | Sí (con inventario de más) | 83.4 |
| Tapa | ninguna | No (faltan 610, 1230, 1250) | 1550 (escrito a mano) |
| Cilindro | 3: 1250 | No (faltan 1140 en la semana 1) | 5 |
| Mina de Tinta | 3: 1250 | No (faltan 1140 en la semana 1) | 4 |

*Deducido:* la suma de los costos totales es 2387.1; el archivo no la calcula.

**Conclusión:** el libro implementa bien la explosión del BOM y el desfase por *lead time* para el esfero, el cuerpo y la tapa arriba. Los tres ítems de LT = 0 quedaron a medio resolver.

### Observaciones

- **Errores de fórmula:** las "X" de texto en las liberaciones de los periodos 8-10 entran en las fórmulas de los hijos y generan `#VALUE!` en los requerimientos brutos (Tapa Arriba), inventarios y netos de las semanas 8-10. No afectan los costos, porque las sumas de inventario de los componentes llegan solo hasta la columna K (semana 8), donde todavía no hay errores, y `COUNTIF` solo mira las columnas D:J.
- **Neto del periodo 1 mal formulado** en Tapa (`D27 = D28`), Cilindro (`D34 = D35`) y Mina (`D41 = D42`): muestra la liberación en lugar de $\max\{0, G_1-S_1-I_1\}$ y oculta faltantes de 610 y 1140.
- Los costos de la Tapa (50 y 1500) son números escritos a mano, no fórmulas; no se puede saber cómo se obtuvieron.
- El rango de inventario del costo cambia: el esfero suma D:M (10 periodos), los demás D:K (8 periodos).
- Los títulos dicen "Item Final" para todos los ítems, aunque solo el esfero es producto final.
- Las tarifas de costo (80 y 0.05, 80 y 0.04, 10 y 0.01, 5 y 0.01, 4 y 0.01) no se explican en la hoja; se toman como datos del ejercicio.
- Diferencias con la primera versión: ver la tabla al final de [mrp-esfero](./mrp-esfero.md#diferencias-con-mrp-esfero-v2xlsx).

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `Hoja1` — 42 filas × 16 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 |  | Item Final: Esfero | Descripción | Periodo 1 | Periodo 2 | Periodo 3 | Periodo 4 | Periodo 5 | Periodo 6 | Periodo 7 | Periodo 8 | Periodo 9 | Periodo 10 |  | Costos |  |
| 3 |  | Requerimiento Bruto | Demanda Final | 300 | 400 | 500 | 550 | 560 | 700 | 530 | 550 | 400 | 300 |  | Costos Ordenar | 240 |
| 4 |  | Entregas Programadas | Lotes Listos al Inicio de la Semana | 500 | 0 | 0 | 610 | 0 | 1230 | 0 | 1250 | 0 | 0 |  | Costos Inventario | 309.5 |
| 5 |  | Inventario Esperado | Inventario Disponible al Inicio de la Semana | 1200 | 1400 | 1000 | 500 | 560 | 0 | 530 | 0 | 700 | 300 |  | Costos Totales | 549.5 |
| 6 |  | Requerimiento Neto | Demanda que no se ha Satisfecho | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |
| 7 | Variable de Decisión | Liberación de Órdenes Planeadas | Pedidos Realizados a la Fábrica (LT=3) | 610 | 0 | 1230 | 0 | 1250 | 0 | 0 | X | X | X |  |  |  |
| 9 |  | Item Final: Cuerpo | Descripción | Periodo 1 | Periodo 2 | Periodo 3 | Periodo 4 | Periodo 5 | Periodo 6 | Periodo 7 | Periodo 8 | Periodo 9 | Periodo 10 |  | Costos |  |
| 10 |  | Requerimiento Bruto | Demanda Final | 610 | 0 | 1230 | 0 | 1250 | 0 | 0 | X | X | X |  | Costos Ordenar | 160 |
| 11 |  | Entregas Programadas | Lotes Listos al Inicio de la Semana | 0 | 0 | 1140 | 0 | 1250 | 0 | 0 | 0 | 0 | X |  | Costos Inventario | 35.2 |
| 12 |  | Inventario Esperado | Inventario Disponible al Inicio de la Semana | 700 | 90 | 90 | 0 | 0 | 0 | 0 | 0 | #VALUE! | #VALUE! |  | Costos Totales | 195.2 |
| 13 |  | Requerimiento Neto | Demanda que no se ha Satisfecho | 0 | 0 | 0 | 0 | 0 | 0 | 0 | #VALUE! | #VALUE! | #VALUE! |  |  |  |
| 14 |  | Liberación de Órdenes Planeadas | Pedidos Realizados a la Fábrica (LT=2) | 1140 | 0 | 1250 | 0 | 0 | 0 | 0 | X | X | X |  |  |  |
| 16 |  | Item Final: Tapa Arriba | Descripción | Periodo 1 | Periodo 2 | Periodo 3 | Periodo 4 | Periodo 5 | Periodo 6 | Periodo 7 | Periodo 8 | Periodo 9 | Periodo 10 |  | Costos |  |
| 17 |  | Requerimiento Bruto | Demanda Final | 1220 | 0 | 2460 | 0 | 2500 | 0 | 0 | #VALUE! | #VALUE! | #VALUE! |  | Costos Ordenar | 20 |
| 18 |  | Entregas Programadas | Lotes Listos al Inicio de la Semana | 0 | 2380 | 0 | 2500 | 0 | 0 | 0 | 0 | X | X |  | Costos Inventario | 63.4 |
| 19 |  | Inventario Esperado | Inventario Disponible al Inicio de la Semana | 1300 | 80 | 2460 | 0 | 2500 | 0 | 0 | 0 | #VALUE! | #VALUE! |  | Costos Totales | 83.4 |
| 20 |  | Requerimiento Neto | Demanda que no se ha Satisfecho | 0 | 0 | 0 | 0 | 0 | 0 | 0 | #VALUE! | #VALUE! | #VALUE! |  |  |  |
| 21 |  | Liberación de Órdenes Planeadas | Pedidos Realizados a la Fábrica (LT=1) | 2380 | 0 | 2500 | 0 | 0 | 0 | 0 | X | X | X |  |  |  |
| 23 |  | Item Final: Tapa | Descripción | Periodo 1 | Periodo 2 | Periodo 3 | Periodo 4 | Periodo 5 | Periodo 6 | Periodo 7 | Periodo 8 | Periodo 9 | Periodo 10 |  | Costos |  |
| 24 |  | Requerimiento Bruto | Demanda Final | 610 | 0 | 1230 | 0 | 1250 | 0 | 0 | X | X | X |  | Costos Ordenar | 50 |
| 25 |  | Entregas Programadas | Lotes Listos al Inicio de la Semana | 0 | 0 | 0 | 0 | 0 | 0 | 0 | X | X | X |  | Costos Inventario | 1500 |
| 26 |  | Inventario Esperado | Inventario Disponible al Inicio de la Semana | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | #VALUE! | #VALUE! |  | Costos Totales | 1550 |
| 27 |  | Requerimiento Neto | Demanda que no se ha Satisfecho | 0 | 0 | 1230 | 0 | 1250 | 0 | 0 | #VALUE! | #VALUE! | #VALUE! |  |  |  |
| 28 |  | Liberación de Órdenes Planeadas | Pedidos Realizados a la Fábrica (LT=0) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | X | X | X |  |  |  |
| 30 |  | Item Final: Cilindro | Descripción | Periodo 1 | Periodo 2 | Periodo 3 | Periodo 4 | Periodo 5 | Periodo 6 | Periodo 7 | Periodo 8 | Periodo 9 | Periodo 10 |  | Costos |  |
| 31 |  | Requerimiento Bruto | Demanda Final | 1140 | 0 | 1250 | 0 | 0 | 0 | 0 | X | X | X |  | Costos Ordenar | 5 |
| 32 |  | Entregas Programadas | Lotes Listos al Inicio de la Semana | 0 | 0 | 1250 | 0 | 0 | 0 | 0 | X | X | X |  | Costos Inventario | 0 |
| 33 |  | Inventario Esperado | Inventario Disponible al Inicio de la Semana | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | #VALUE! | #VALUE! |  | Costos Totales | 5 |
| 34 |  | Requerimiento Neto | Demanda que no se ha Satisfecho | 0 | 0 | 0 | 0 | 0 | 0 | 0 | #VALUE! | #VALUE! | #VALUE! |  |  |  |
| 35 |  | Liberación de Órdenes Planeadas | Pedidos Realizados a la Fábrica (LT=0) | 0 | 0 | 1250 | 0 | 0 | 0 | 0 | X | X | X |  |  |  |
| 37 |  | Item Final: Mina de Tinta | Descripción | Periodo 1 | Periodo 2 | Periodo 3 | Periodo 4 | Periodo 5 | Periodo 6 | Periodo 7 | Periodo 8 | Periodo 9 | Periodo 10 |  | Costos |  |
| 38 |  | Requerimiento Bruto | Demanda Final | 1140 | 0 | 1250 | 0 | 0 | 0 | 0 | X | X | X |  | Costos Ordenar | 4 |
| 39 |  | Entregas Programadas | Lotes Listos al Inicio de la Semana | 0 | 0 | 1250 | 0 | 0 | 0 | 0 | X | X | X |  | Costos Inventario | 0 |
| 40 |  | Inventario Esperado | Inventario Disponible al Inicio de la Semana | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | #VALUE! | #VALUE! |  | Costos Totales | 4 |
| 41 |  | Requerimiento Neto | Demanda que no se ha Satisfecho | 0 | 0 | 0 | 0 | 0 | 0 | 0 | #VALUE! | #VALUE! | #VALUE! |  |  |  |
| 42 |  | Liberación de Órdenes Planeadas | Pedidos Realizados a la Fábrica (LT=0) | 0 | 0 | 1250 | 0 | 0 | 0 | 0 | X | X | X |  |  |  |

**Fórmulas (43 patrones distintos):**

- `P3`: `=80*COUNTIF(D7:J7,">0")`
- `G4`: `=D7`
- `H4`: `=E7`
- `I4`: `=F7`
- `J4`: `=G7`
- `K4`: `=H7`
- `L4`: `=I7`
- `M4`: `=J7`
- `P4`: `=0.05*SUM(D5:M5)`
- `E5`: `=MAX(0,D5+D4-D3)`
- `F5`: `=MAX(0,E5+E4-E3)`
- `G5`: `=MAX(0,F5+F4-F3)`
- `H5`: `=MAX(0,G5+G4-G3)`
- `I5`: `=MAX(0,H5+H4-H3)`
- `J5`: `=MAX(0,I5+I4-I3)`
- `K5`: `=MAX(0,J5+J4-J3)`
- `L5`: `=MAX(0,K5+K4-K3)`
- `M5`: `=MAX(0,L5+L4-L3)`
- `P5`: `=SUM(P3:P4)`
- `D6`: `=MAX(0,D3-D4-D5)`
- `E6`: `=MAX(0,E3-E4-E5)`
- `F6`: `=MAX(0,F3-F4-F5)`
- `G6`: `=MAX(0,G3-G4-G5)`
- `H6`: `=MAX(0,H3-H4-H5)`
- `I6`: `=MAX(0,I3-I4-I5)`
- `J6`: `=MAX(0,J3-J4-J5)`
- `K6`: `=MAX(0,K3-K4-K5)`
- `L6`: `=MAX(0,L3-L4-L5)`
- `M6`: `=MAX(0,M3-M4-M5)`
- `K10`: `=K7`
- `L10`: `=L7`
- `M10`: `=M7`
- `P11`: `=0.04*SUM(D12:K12)`
- `D17`: `=2*D7`
- `E17`: `=2*E7`
- `F17`: `=2*F7`
- `G17`: `=2*G7`
- `H17`: `=2*H7`
- `I17`: `=2*I7`
- `J17`: `=2*J7`
- `K17`: `=2*K7`
- `L17`: `=2*L7`
- `M17`: `=2*M7`

