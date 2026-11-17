# mrp-esfero

> **Archivo:** [`mrp-esfero.xlsx`](./mrp-esfero.xlsx) · **Corte 2** · Libro de Excel con 1 hoja(s): `Hoja1`  
> **Nombre original:** `CORTE 2/MRP.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Primera versión del MRP de un **esfero** (bolígrafo) hecha en Excel en clase, siguiendo el "CONSTRUIR EXCEL" de la [L14](./L14-mrp.md) (p. 10) con las mismas fórmulas de inventario esperado y requerimiento neto. Tiene una sola hoja (`Hoja1`) con cuatro bloques MRP de 10 semanas. Solo el primero (el esfero, producto final) está completo y es factible; los otros tres son borradores de los componentes: todos se titulan "item, final: esfero", tienen valores escritos a mano y no están enlazados por fórmulas. La versión corregida y completa es [mrp-esfero-v2](./mrp-esfero-v2.md); las diferencias están al final.

Se aprende: cómo se encadenan las filas de una tabla MRP, cómo el *lead time* desplaza las recepciones, que el requerimiento neto debe quedar en 0 si el plan es factible ("Idealmente debe de ser 0 en todos los periodos", celda N6) y cómo se costea un plan (ordenar + mantener).

### Fórmulas comunes a todos los bloques

En cada bloque, con $t$ = periodo (columnas D a M = periodos 1 a 10):

- Inventario esperado (disponible al inicio de la semana), p. ej. `E5 = MAX(0,D5+D4-D3)`:
$$I_t=\max\{0,\ I_{t-1}+S_{t-1}-G_{t-1}\}$$
- Requerimiento neto ("demanda que no se ha satisfecho"), p. ej. `D6 = MAX(0,D3-D4-D5)`:
$$N_t=\max\{0,\ G_t-S_t-I_t\}$$
- Entregas programadas ("lotes listos al inicio de la semana"): desde el periodo 4 son la liberación de 3 periodos antes, p. ej. `G4 = D7`, es decir $S_t=L_{t-3}$ (LT = 3; nota en D9: "Lo que yo pida en el periodo 1 llega en el periodo 4"). Los periodos 1 a 3 se escriben a mano.
- Liberación de órdenes ("Pedidos realizados a la fábrica (LEAD TIME = 3)"): **variable de decisión** escrita a mano (N7) para los periodos 1-7. Los periodos 8-10 llevan "x", porque lo que se pidiera ahí llegaría después del horizonte.
- Costos (solo bloques 1 y 2):
  - Costo de ordenar, `P3 = 80*COUNTIF(D7:J7,">0")`: \$80 por cada orden liberada en los periodos 1-7.
  - Costo de inventario, `P4 = 0.05*SUM(D5:M5)`: \$0.05 por unidad y periodo, sobre el inventario **al inicio** de cada periodo.
  - Costo total, `P5 = SUM(P3:P4)`.

$G_t$: requerimiento bruto; $S_t$: entregas programadas; $I_t$: inventario esperado al inicio de $t$; $N_t$: requerimiento neto; $L_t$: liberación de órdenes.

### Bloque 1 (filas 2-7): esfero, producto final

**Objetivo:** liberar órdenes de fabricación del esfero (LT = 3 semanas) de modo que nunca falte producto frente a la demanda final, con pocas órdenes.

**Datos de entrada:** demanda final (requerimiento bruto) de 10 semanas; inventario inicial 1200 (D5); recepción ya programada de 500 en la semana 1 (D4).

| Fila | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 | P10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Requerimiento bruto (fila 3) | 300 | 400 | 500 | 550 | 560 | 700 | 530 | 550 | 400 | 300 |
| Entregas programadas (fila 4) | 500 | 0 | 0 | 610 | 0 | 1230 | 0 | 1250 | 0 | 0 |
| *Recepción de órdenes planeadas (derivada = liberación de 3 periodos antes)* | | | | 610 | 0 | 1230 | 0 | 1250 | 0 | 0 |
| Inventario esperado (fila 5) | 1200 | 1400 | 1000 | 500 | 560 | 0 | 530 | 0 | 700 | 300 |
| Requerimiento neto (fila 6) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Liberación de órdenes (fila 7) | 610 | 0 | 1230 | 0 | 1250 | 0 | 0 | x | x | x |

**Lógica del plan:** la orden de 610 (semana 1, llega en la 4) cubre las semanas 4 y 5 ($550+560-500$ disponibles $=610$). La de 1230 (semana 3, llega en la 6) cubre las semanas 6 y 7 ($700+530$). La de 1250 (semana 5, llega en la 8) cubre las semanas 8, 9 y 10 ($550+400+300$). El inventario final después de la semana 10 es $300-300=0$.

**Resultados:** requerimiento neto 0 en todas las semanas (plan factible). Costo de ordenar = $80\times3=240$; costo de inventario = $0.05\times(1200+1400+1000+500+560+0+530+0+700+300)=0.05\times6190=309.5$; **costo total = 549.5** (celdas P3:P5).

**Conclusión:** plan factible del producto final con 3 órdenes; sus liberaciones (610, 1230 y 1250 en las semanas 1, 3 y 5) son los requerimientos brutos de los componentes.

### Bloque 2 (filas 16-21): primer componente (sin nombre; *deducido:* el cuerpo)

**Objetivo (deducido):** planear el componente cuyo requerimiento bruto son las liberaciones del esfero (610, 0, 1230, 0, 1250), escritas a mano. Usa LT = 3 (`G18 = D21`) e inventario inicial 700.

| Fila | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 | P10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Requerimiento bruto (fila 17) | 610 | 0 | 1230 | 0 | 1250 | 0 | 0 | | | |
| Entregas programadas (fila 18) | 0 | 0 | 0 | 1140 | 0 | 1250 | 0 | 0 | 0 | 0 |
| Inventario esperado (fila 19) | 700 | 90 | 90 | 0 | 1140 | 0 | 1250 | 1250 | 1250 | 1250 |
| Requerimiento neto (fila 20) | 0 | 0 | **1140** | 0 | **110** | 0 | 0 | 0 | 0 | 0 |
| Liberación de órdenes (fila 21) | 1140 | 0 | 1250 | 0 | 0 | 0 | 0 | x | x | x |

**Resultados:** costo de ordenar $80\times2=160$ (P17), inventario $0.05\times7020=351$ (P18), total **511** (P19). **Plan no factible**: con LT = 3 la orden de 1140 llega en la semana 4, pero se necesita en la 3 (faltan 1140). En la semana 5 faltan 110, y la orden de 1250 llega en la 6, cuando ya no hay demanda, por lo que quedan 1250 unidades sobrantes hasta el final.

**Conclusión:** muestra que, con LT = 3, el componente no se puede abastecer a tiempo. En la v2 este bloque es el **Cuerpo** con LT = 2, y el mismo plan (1140 en la semana 1 y 1250 en la 3) sí es factible.

### Bloque 3 (filas 23-28): segundo componente (sin nombre)

Requerimiento bruto escrito a mano = liberaciones del bloque 2 (1140, 0, 1250); inventario inicial 1300; LT = 3 (`G25 = D28`).

| Fila | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 | P10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Requerimiento bruto (fila 24) | 1140 | 0 | 1250 | 0 | 0 | 0 | 0 | | | |
| Entregas programadas (fila 25) | 0 | 0 | 0 | 2380 | 0 | 2500 | 0 | 0 | 0 | 0 |
| Inventario esperado (fila 26) | 1300 | 160 | 160 | 0 | 2380 | 2380 | 4880 | 4880 | 4880 | 4880 |
| Requerimiento neto (fila 27) | 0 | 0 | **1090** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Liberación de órdenes (fila 28) | 2380 | 0 | 2500 | 0 | 0 | 0 | 0 | x | x | x |

**Resultados:** sin fórmulas de costo. No factible: en la semana 3 faltan 1090. Las órdenes de 2380 y 2500 llegan en las semanas 4 y 6 y dejan 4880 unidades sin uso. *Deducido:* 2380 y 2500 son las cantidades que en la v2 se liberan para la **Tapa Arriba** (2 por esfero), pero aquí se mezclaron con el requerimiento bruto de otro componente.

### Bloque 4 (filas 30-35): tercer componente (sin resolver)

Requerimiento bruto escrito a mano = liberaciones del bloque 3 (2380, 0, 2500); inventario inicial 0; LT = 3; ninguna liberación.

| Fila | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 | P10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Requerimiento bruto (fila 31) | 2380 | 0 | 2500 | 0 | 0 | 0 | 0 | | | |
| Entregas programadas (fila 32) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Inventario esperado (fila 33) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Requerimiento neto (fila 34) | **2380** | 0 | **2500** | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Liberación de órdenes (fila 35) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | x | x | x |

**Conclusión:** bloque sin resolver. Los requerimientos netos muestran lo que faltaría cubrir y, con LT = 3, ya no se podría cubrir a tiempo.

### Observaciones

- Los bloques 2-4 se copiaron del bloque 1: conservan el título "item, final: esfero", la descripción "demanda final" y el rótulo "LEAD TIME = 3". Sus requerimientos brutos están escritos a mano, no enlazados con fórmulas a las liberaciones del padre, y no tienen cantidades por unidad del BOM.
- Las celdas de los periodos 1-3 de "Entregas programadas" se escriben a mano (500, 0, 0 en el bloque 1; 0 en los demás).
- Los costos solo se calculan para los bloques 1 y 2, y el costo de mantener se cobra sobre el inventario al **inicio** de cada periodo.
- La tabla no tiene una fila separada de "recepción de órdenes planeadas": va dentro de "Entregas programadas" (la fila derivada del bloque 1 es solo una ayuda de lectura).
- No hay gráficos ni otras hojas.
- Erratas de los rótulos originales: "Entrega Pogramadas", "invetario disponible al incio de semana", "demanda que no se ha satifceho", "Pedidos Relizados", "peridodo", "peridos".

### Diferencias con `mrp-esfero-v2.xlsx`

| Aspecto | mrp-esfero (esta versión) | [mrp-esfero-v2](./mrp-esfero-v2.md) |
|---|---|---|
| Bloques | 4, todos titulados "esfero" | 6 con nombre: Esfero, Cuerpo, Tapa Arriba, Tapa, Cilindro, Mina de Tinta |
| *Lead times* | 3 en todos | 3, 2, 1, 0, 0, 0 |
| Requerimientos brutos de componentes | Escritos a mano | Fórmulas que implementan el BOM: `=D7` (1 por esfero), `=2*D7` (2 tapas arriba por esfero), `=D14` (1 por cuerpo) |
| Costos | Bloques 1 y 2 (\$80 por orden; \$0.05 por unidad-periodo) | Uno por ítem, con tarifas distintas (80/0.05, 80/0.04, 10/0.01, 50 y 1500 escritos a mano, 5/0.01, 4/0.01) |
| Factibilidad | Solo el esfero; los demás bloques tienen faltantes | Esfero, Cuerpo y Tapa Arriba factibles; Tapa sin resolver; Cilindro y Mina con el faltante del periodo 1 oculto |
| Bloque del esfero | Igual | Igual (mismos datos, fórmulas y costo 549.5) |
| Periodos 8-10 | "x" en la liberación, sin errores | Las "X" se propagan como `#VALUE!` en los componentes |

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `Hoja1` — 35 filas × 16 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 |  | item, final: esfero | descripcion | periodo 1 | periodo 2 | periodo 3 | periodo 4 | periodo 5 | periodo 6 | periodo 7 | periodo 8 | periodo 9 | periodo 10 |  | Costos |  |
| 3 |  | Requerimiento Bruto | demanda final | 300 | 400 | 500 | 550 | 560 | 700 | 530 | 550 | 400 | 300 |  | Costos De Ordenar | 240 |
| 4 |  | Entrega Pogramadas | Lotes Listos al inicio de la semana | 500 | 0 | 0 | 610 | 0 | 1230 | 0 | 1250 | 0 | 0 |  | Costos De Inventario | 309.5 |
| 5 |  | inventario Esperado | invetario disponible al incio de semana | 1200 | 1400 | 1000 | 500 | 560 | 0 | 530 | 0 | 700 | 300 |  | Costos Totales | 549.5 |
| 6 |  | requerimiento neto | demanda que no se ha satifceho | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | Idealmente debe de ser 0 en todos los peridos |  |  |
| 7 |  | Liberacion De Ordenes | Pedidos Relizados a la fabrica (LEAD TIME = 3) | 610 | 0 | 1230 | 0 | 1250 | 0 | 0 | x | x | x | Variable De Decisión |  |  |
| 9 |  |  |  | Lo que yo pida en el peridodo 1 llega en el periodo 4 |  |  |  |  |  |  |  |  |  |  |  |  |
| 16 |  | item, final: esfero | descripcion | periodo 1 | periodo 2 | periodo 3 | periodo 4 | periodo 5 | periodo 6 | periodo 7 | periodo 8 | periodo 9 | periodo 10 |  | Costos |  |
| 17 |  | Requerimiento Bruto | demanda final | 610 | 0 | 1230 | 0 | 1250 | 0 | 0 |  |  |  |  | Costos De Ordenar | 160 |
| 18 |  | Entrega Pogramadas | Lotes Listos al inicio de la semana | 0 | 0 | 0 | 1140 | 0 | 1250 | 0 | 0 | 0 | 0 |  | Costos De Inventario | 351 |
| 19 |  | inventario Esperado | invetario disponible al incio de semana | 700 | 90 | 90 | 0 | 1140 | 0 | 1250 | 1250 | 1250 | 1250 |  | Costos Totales | 511 |
| 20 |  | requerimiento neto | demanda que no se ha satifceho | 0 | 0 | 1140 | 0 | 110 | 0 | 0 | 0 | 0 | 0 |  |  |  |
| 21 |  | Liberacion De Ordenes | Pedidos Relizados a la fabrica (LEAD TIME = 3) | 1140 | 0 | 1250 | 0 | 0 | 0 | 0 | x | x | x |  |  |  |
| 23 |  | item, final: esfero | descripcion | periodo 1 | periodo 2 | periodo 3 | periodo 4 | periodo 5 | periodo 6 | periodo 7 | periodo 8 | periodo 9 | periodo 10 |  |  |  |
| 24 |  | Requerimiento Bruto | demanda final | 1140 | 0 | 1250 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |
| 25 |  | Entrega Pogramadas | Lotes Listos al inicio de la semana | 0 | 0 | 0 | 2380 | 0 | 2500 | 0 | 0 | 0 | 0 |  |  |  |
| 26 |  | inventario Esperado | invetario disponible al incio de semana | 1300 | 160 | 160 | 0 | 2380 | 2380 | 4880 | 4880 | 4880 | 4880 |  |  |  |
| 27 |  | requerimiento neto | demanda que no se ha satifceho | 0 | 0 | 1090 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |
| 28 |  | Liberacion De Ordenes | Pedidos Relizados a la fabrica (LEAD TIME = 3) | 2380 | 0 | 2500 | 0 | 0 | 0 | 0 | x | x | x |  |  |  |
| 30 |  | item, final: esfero | descripcion | periodo 1 | periodo 2 | periodo 3 | periodo 4 | periodo 5 | periodo 6 | periodo 7 | periodo 8 | periodo 9 | periodo 10 |  |  |  |
| 31 |  | Requerimiento Bruto | demanda final | 2380 | 0 | 2500 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |
| 32 |  | Entrega Pogramadas | Lotes Listos al inicio de la semana | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |
| 33 |  | inventario Esperado | invetario disponible al incio de semana | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |
| 34 |  | requerimiento neto | demanda que no se ha satifceho | 2380 | 0 | 2500 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |
| 35 |  | Liberacion De Ordenes | Pedidos Relizados a la fabrica (LEAD TIME = 3) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | x | x | x |  |  |  |

**Fórmulas (29 patrones distintos):**

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

