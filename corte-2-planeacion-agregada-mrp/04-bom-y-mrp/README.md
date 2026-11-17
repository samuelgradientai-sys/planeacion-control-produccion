# BOM y MRP (Corte 2)

## Qué cubre

Planeación de requerimientos de materiales (MRP) para productos con demanda dependiente: lista de materiales (BOM) como árbol y como matriz, niveles, explosión de partes con $dd(n)=d_n\times B$ y tabla MRP por periodo. La tabla tiene requerimientos brutos, entregas programadas, inventario esperado, requerimientos netos y liberación de órdenes desplazada por el *lead time*. También trata el dimensionamiento de lotes, el MRP de ciclo cerrado y el nerviosismo. Incluye el ejemplo de clase (productos 1 y 2) y un MRP en Excel de un esfero.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [L13-bom-intro-to-mrp.md](./L13-bom-intro-to-mrp.md) | Presentación (26 pp.): propósito y limitaciones del MRP, BOM (bolso, bicicleta, carro), matriz BOM, niveles y demanda dependiente directa. | 1.º |
| [L14-mrp.md](./L14-mrp.md) | Presentación (21 pp.): tabla MRP completa de 9 ítems y 9 semanas, *lot sizing*, MRP de ciclo cerrado y nerviosismo. | 2.º |
| [calculo-demanda-dependiente-directa.md](./calculo-demanda-dependiente-directa.md) | Excel: explosión del BOM de clase para 80 y 50 unidades, nivel por nivel (`MMULT`) y con $(I-B)^{-1}$ (`MINVERSE`). Venía de la carpeta del Corte 3. | 3.º |
| [mrp-esfero.md](./mrp-esfero.md) | Excel, 1.ª versión del MRP del esfero: producto final completo y tres borradores de componentes sin enlazar. | 4.º |
| [mrp-esfero-v2.md](./mrp-esfero-v2.md) | Excel, 2.ª versión: 6 ítems (Esfero, Cuerpo, Tapa Arriba, Tapa, Cilindro, Mina de Tinta) enlazados por el BOM, con *lead time* y costos por ítem. | 5.º |

**Diferencia entre las dos versiones del esfero.** Ambas tienen el mismo bloque del producto final (demanda de 10 semanas, LT = 3, liberaciones 610, 1230 y 1250 en las semanas 1, 3 y 5, costo 549.5). En la v1, los componentes son tres bloques copiados del esfero (mismo título, LT = 3, requerimientos escritos a mano) con faltantes o sin resolver. En la v2, cada componente tiene nombre, su propio *lead time* (2, 1, 0, 0, 0), requerimientos brutos calculados con el BOM (`=D7`, `=2*D7`, `=D14`) y sus propios costos. Esfero, Cuerpo y Tapa Arriba quedan factibles; Tapa, Cilindro y Mina quedan a medio resolver. Tabla comparativa completa al final de [mrp-esfero.md](./mrp-esfero.md#diferencias-con-mrp-esfero-v2xlsx).

## Orden de estudio sugerido

1. [L13](./L13-bom-intro-to-mrp.md), pp. 1-12: qué es el MRP, entradas y limitaciones.
2. [L13](./L13-bom-intro-to-mrp.md), pp. 13-26: BOM, matriz, niveles y $dd(n)=d_n\times B$.
3. [calculo-demanda-dependiente-directa](./calculo-demanda-dependiente-directa.md): la misma explosión en Excel, hasta el último nivel.
4. [L14](./L14-mrp.md), pp. 1-12: tabla MRP nivel por nivel del ejemplo de clase.
5. [mrp-esfero](./mrp-esfero.md) y luego [mrp-esfero-v2](./mrp-esfero-v2.md): la tabla MRP construida en Excel.
6. [L14](./L14-mrp.md), pp. 13-21: *lot sizing*, ciclo cerrado y nerviosismo; después, [Wagner-Whitin y Silver-Meal](../03-wagner-whitin-y-silver-meal/README.md).

## Conceptos y fórmulas clave

- Matriz BOM: $B=(b_{ij})$, con $b_{ij}$ = unidades del ítem $j$ para hacer **directamente** una unidad del ítem $i$ ([L13](./L13-bom-intro-to-mrp.md), p. 13).
- Nivel de un ítem = número máximo de pasos de ensamble hasta un producto final; se planea del nivel 0 hacia abajo ([L13](./L13-bom-intro-to-mrp.md), p. 20).
- Demanda dependiente directa: $dd(n)=d_n\times B$; demanda total $=d\,(I-B)^{-1}$ ([L13](./L13-bom-intro-to-mrp.md), p. 23; [Excel](./calculo-demanda-dependiente-directa.md)).
- Inventario esperado al inicio del periodo: $I_{jt}=\max\{0,\ I_{j,t-1}+S_{j,t-1}-G_{j,t-1}\}$ ([L14](./L14-mrp.md), p. 5).
- Requerimiento neto: $N_{jt}=\max\{0,\ G_{jt}-S_{jt}-I_{jt}\}$ ([L14](./L14-mrp.md), p. 6).
- Liberación de una orden: en $t-LT_j$ para recibir en $t$; la liberación del padre en $t$, multiplicada por la cantidad del BOM, es el requerimiento bruto del hijo en $t$.
- EOQ: $Q^*=\sqrt{2DK/h}$ ([L14](./L14-mrp.md), p. 14).

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
| Demanda dependiente directa con $d=(100, 200)$ | [L13](./L13-bom-intro-to-mrp.md), pp. 24-26 | A = 200, D = 200, B = 200, C = 100, γ = 600 (primer orden) |
| Explosión completa con $d=(80, 50)$ | [calculo-demanda-dependiente-directa](./calculo-demanda-dependiente-directa.md) | Totales: A 160, D 50, B 310, C 750, γ 460, α 1070, β 2250 |
| MRP de 9 ítems y 9 semanas | [L14](./L14-mrp.md), pp. 3-12 | Liberaciones: 1 → 120 (s3, s7); 2 → 100 (s3, s7); A → 240, 240, 15 (s1, s5, s6); D → 100, 10, 100 (s1, s2, s5); B → 575 (s4), 100 (s8); C → 120, 1250, 320 (s2, s3, s6); γ → 300, 575, 300, 100 (s1, s2, s5, s6); β → 2000 (s1); α ninguna |
| Nerviosismo (A τ=0 → 2 B τ=3) | [L14](./L14-mrp.md), pp. 19-20 | Subir A de 55 a 60 deja a B en −10 sin poder corregirlo, por su *lead time* de 3 |
| MRP del esfero, producto final | [mrp-esfero](./mrp-esfero.md) y [v2](./mrp-esfero-v2.md) | Liberar 610, 1230, 1250 en las semanas 1, 3, 5; costo 549.5 |
| MRP del esfero, componentes | [mrp-esfero-v2](./mrp-esfero-v2.md) | Cuerpo 1140 y 1250 (s1, s3), costo 195.2; Tapa Arriba 2380 y 2500 (s1, s3), costo 83.4; Tapa, Cilindro y Mina incompletos |

## Relación con otros temas y proyectos

- [03 Wagner-Whitin y Silver-Meal](../03-wagner-whitin-y-silver-meal/README.md): cómo dimensionar las liberaciones de órdenes. `wagner_whitin.py` toma como demanda los requerimientos netos de la Tapa Arriba de mrp-esfero-v2 (deducido).
- [05 MRP II y capacidad](../05-mrp-ii-y-capacidad/L15-mrp-ii.md): agrega la verificación de capacidad (CRP) y el ciclo cerrado que el MRP no considera.
- [01 Planeación agregada](../01-planeacion-agregada-modelo-bowman/) y [02 Agregación y desagregación](../02-agregacion-y-desagregacion/): de ahí sale el programa maestro (MPS), que es la entrada del MRP.
- [Parcial 2](../parcial-2/parcial-2-solucion.md): punto 2.3 (matriz MRP lote a lote) y 2.4 (lot sizing).
- [Corte 3, scheduling](../../corte-3-programacion-scheduling/): el MRP no programa máquinas ni horas ([L13](./L13-bom-intro-to-mrp.md), p. 11); eso se ve en el Corte 3.
