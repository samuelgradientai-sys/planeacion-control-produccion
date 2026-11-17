<!-- fuente: corte-2-planeacion-agregada-mrp/04-bom-y-mrp/README.md -->
# BOM y MRP (Corte 2)

## Qué cubre

Planeación de requerimientos de materiales (MRP) para productos con demanda dependiente: lista de materiales (BOM) como árbol y como matriz, niveles, explosión de partes con $dd(n)=d_n\times B$ y tabla MRP por periodo. La tabla tiene requerimientos brutos, entregas programadas, inventario esperado, requerimientos netos y liberación de órdenes desplazada por el *lead time*. También trata el dimensionamiento de lotes, el MRP de ciclo cerrado y el nerviosismo. Incluye el ejemplo de clase (productos 1 y 2) y un MRP en Excel de un esfero.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [L13-bom-intro-to-mrp.md](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md) | Presentación (26 pp.): propósito y limitaciones del MRP, BOM (bolso, bicicleta, carro), matriz BOM, niveles y demanda dependiente directa. | 1.º |
| [L14-mrp.md](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md) | Presentación (21 pp.): tabla MRP completa de 9 ítems y 9 semanas, *lot sizing*, MRP de ciclo cerrado y nerviosismo. | 2.º |
| [calculo-demanda-dependiente-directa.md](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/calculo-demanda-dependiente-directa.md) | Excel: explosión del BOM de clase para 80 y 50 unidades, nivel por nivel (`MMULT`) y con $(I-B)^{-1}$ (`MINVERSE`). Venía de la carpeta del Corte 3. | 3.º |
| [mrp-esfero.md](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero.md) | Excel, 1.ª versión del MRP del esfero: producto final completo y tres borradores de componentes sin enlazar. | 4.º |
| [mrp-esfero-v2.md](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero-v2.md) | Excel, 2.ª versión: 6 ítems (Esfero, Cuerpo, Tapa Arriba, Tapa, Cilindro, Mina de Tinta) enlazados por el BOM, con *lead time* y costos por ítem. | 5.º |

**Diferencia entre las dos versiones del esfero.** Ambas tienen el mismo bloque del producto final (demanda de 10 semanas, LT = 3, liberaciones 610, 1230 y 1250 en las semanas 1, 3 y 5, costo 549.5). En la v1, los componentes son tres bloques copiados del esfero (mismo título, LT = 3, requerimientos escritos a mano) con faltantes o sin resolver. En la v2, cada componente tiene nombre, su propio *lead time* (2, 1, 0, 0, 0), requerimientos brutos calculados con el BOM (`=D7`, `=2*D7`, `=D14`) y sus propios costos. Esfero, Cuerpo y Tapa Arriba quedan factibles; Tapa, Cilindro y Mina quedan a medio resolver. Tabla comparativa completa al final de [mrp-esfero.md](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero.md#diferencias-con-mrp-esfero-v2xlsx).

## Orden de estudio sugerido

1. [L13](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md), pp. 1-12: qué es el MRP, entradas y limitaciones.
2. [L13](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md), pp. 13-26: BOM, matriz, niveles y $dd(n)=d_n\times B$.
3. [calculo-demanda-dependiente-directa](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/calculo-demanda-dependiente-directa.md): la misma explosión en Excel, hasta el último nivel.
4. [L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md), pp. 1-12: tabla MRP nivel por nivel del ejemplo de clase.
5. [mrp-esfero](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero.md) y luego [mrp-esfero-v2](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero-v2.md): la tabla MRP construida en Excel.
6. [L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md), pp. 13-21: *lot sizing*, ciclo cerrado y nerviosismo; después, [Wagner-Whitin y Silver-Meal](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/README.md).

## Conceptos y fórmulas clave

- Matriz BOM: $B=(b_{ij})$, con $b_{ij}$ = unidades del ítem $j$ para hacer **directamente** una unidad del ítem $i$ ([L13](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md), p. 13).
- Nivel de un ítem = número máximo de pasos de ensamble hasta un producto final; se planea del nivel 0 hacia abajo ([L13](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md), p. 20).
- Demanda dependiente directa: $dd(n)=d_n\times B$; demanda total $=d\,(I-B)^{-1}$ ([L13](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md), p. 23; [Excel](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/calculo-demanda-dependiente-directa.md)).
- Inventario esperado al inicio del periodo: $I_{jt}=\max\{0,\ I_{j,t-1}+S_{j,t-1}-G_{j,t-1}\}$ ([L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md), p. 5).
- Requerimiento neto: $N_{jt}=\max\{0,\ G_{jt}-S_{jt}-I_{jt}\}$ ([L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md), p. 6).
- Liberación de una orden: en $t-LT_j$ para recibir en $t$; la liberación del padre en $t$, multiplicada por la cantidad del BOM, es el requerimiento bruto del hijo en $t$.
- EOQ: $Q^*=\sqrt{2DK/h}$ ([L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md), p. 14).

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
| Demanda dependiente directa con $d=(100, 200)$ | [L13](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md), pp. 24-26 | A = 200, D = 200, B = 200, C = 100, γ = 600 (primer orden) |
| Explosión completa con $d=(80, 50)$ | [calculo-demanda-dependiente-directa](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/calculo-demanda-dependiente-directa.md) | Totales: A 160, D 50, B 310, C 750, γ 460, α 1070, β 2250 |
| MRP de 9 ítems y 9 semanas | [L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md), pp. 3-12 | Liberaciones: 1 → 120 (s3, s7); 2 → 100 (s3, s7); A → 240, 240, 15 (s1, s5, s6); D → 100, 10, 100 (s1, s2, s5); B → 575 (s4), 100 (s8); C → 120, 1250, 320 (s2, s3, s6); γ → 300, 575, 300, 100 (s1, s2, s5, s6); β → 2000 (s1); α ninguna |
| Nerviosismo (A τ=0 → 2 B τ=3) | [L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md), pp. 19-20 | Subir A de 55 a 60 deja a B en −10 sin poder corregirlo, por su *lead time* de 3 |
| MRP del esfero, producto final | [mrp-esfero](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero.md) y [v2](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero-v2.md) | Liberar 610, 1230, 1250 en las semanas 1, 3, 5; costo 549.5 |
| MRP del esfero, componentes | [mrp-esfero-v2](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero-v2.md) | Cuerpo 1140 y 1250 (s1, s3), costo 195.2; Tapa Arriba 2380 y 2500 (s1, s3), costo 83.4; Tapa, Cilindro y Mina incompletos |

## Relación con otros temas y proyectos

- [03 Wagner-Whitin y Silver-Meal](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/README.md): cómo dimensionar las liberaciones de órdenes. `wagner_whitin.py` toma como demanda los requerimientos netos de la Tapa Arriba de mrp-esfero-v2 (deducido).
- [05 MRP II y capacidad](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md): agrega la verificación de capacidad (CRP) y el ciclo cerrado que el MRP no considera.
- [01 Planeación agregada](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/) y [02 Agregación y desagregación](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/): de ahí sale el programa maestro (MPS), que es la entrada del MRP.
- [Parcial 2](/corte-2-planeacion-agregada-mrp/parcial-2/parcial-2-solucion.md): punto 2.3 (matriz MRP lote a lote) y 2.4 (lot sizing).
- [Corte 3, scheduling](/corte-3-programacion-scheduling/): el MRP no programa máquinas ni horas ([L13](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md), p. 11); eso se ve en el Corte 3.


---

<!-- fuente: corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md -->
# L13-bom-intro-to-mrp

> **Archivo:** [`L13-bom-intro-to-mrp.pdf`](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.pdf) · **Corte 2** · 26 páginas  
> **Nombre original:** `CORTE 2/Lec 13 - BOM intro to MRP.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** introducción al MRP (*Material Requirements Planning*): demanda dependiente, lista de materiales (BOM), matriz BOM, asignación de niveles y cálculo de la demanda dependiente directa con $dd(n)=d_n\times B$.

### Ideas clave

- El MRP sirve para productos con cientos de componentes: reduce inventarios, evita paradas por falta de materia prima (mejor servicio al cliente, alta utilización de planta) y responde rápido a cambios del mercado (p. 2).
- **Propósito** (p. 4): calcular cuándo producir o comprar los componentes y materias primas del producto terminado para cumplir el plan de producción, minimizando el inventario en proceso (WIP).
- Es un sistema de **inventario dependiente**: más eficiente que los modelos de inventario independiente (EOQ) y reacciona mejor ante picos de demanda; evolucionó hacia los ERP (p. 5). Con puntos de reorden, los componentes y materias primas se mantienen en inventario todo el tiempo; con MRP solo aparecen justo antes de que se necesiten (p. 6).
- **Entradas** (pp. 8 y 10): programa maestro de producción (MPS: qué y cuándo), BOM, disponibilidad de inventarios, órdenes de compra en curso y *lead times*. Como cambian con frecuencia, hay que re-optimizar "moderadamente" seguido.
- **Limitaciones** (p. 11): planea materiales pero no programa (no dice en qué máquina ni a qué hora) y no considera restricciones de capacidad (eso lo agrega el MRP II, [carpeta 05](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/)).
- Tipos de ítems (p. 12): producto terminado (*e*), subensambles (*s*) y partes (*p*). La **explosión de partes** recorre la BOM de arriba hacia abajo.
- El **nivel** de un ítem es el número máximo de pasos de ensamble que lo separan de un producto final; se planea del nivel más alto (0) al más bajo (p. 20).
- Reglas para una buena BOM (p. 21): no usar unidades de volumen, peso o longitud (usar porciones), no mostrar procesos ni operaciones, no mostrar herramientas ni maquinaria, y alinear los ítems iguales en el mismo nivel.

### Fórmulas y métodos

- **Vector BOM de un ítem** (p. 13): $B^i=(b_{i1}, b_{i2}, \dots, b_{ij})$, donde $b_{ij}$ es el número de unidades del ítem $j$ requeridas para hacer **directamente** una unidad del ítem $i$.
- **Matriz BOM**: $B=\begin{pmatrix}B^1\\ B^2\\ \vdots\\ B^n\end{pmatrix}$ (fila = padre, columna = hijo).
- **Demanda dependiente directa** (p. 23): $dd(n)=d_n\times B$, donde $d_n$ es el vector (fila) de demanda en el nivel $n$ y $dd(n)$ el vector de demanda que resulta directamente en los ítems hijos. Se aplica nivel por nivel.
- *Complemento deducido, no está en las diapositivas:* la demanda total (todos los niveles) es $d\,(I+B+B^2+\dots)=d\,(I-B)^{-1}$; así lo calcula el Excel [calculo-demanda-dependiente-directa](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/calculo-demanda-dependiente-directa.md).

### BOM del ejemplo de clase (pp. 14-20)

Ítems: productos terminados 1 y 2; subensambles A, D, B y C; partes γ, α y β. Cantidades por unidad del padre (las que no llevan número son 1):

| Padre | Hijos (cantidad) | Nivel del padre |
|---|---|---|
| 1 | A (2), C (1) | 0 |
| 2 | D (1), B (1), γ (3) | 0 |
| A | B (1), α (2) | 1 |
| D | B (2), C (1) | 1 |
| B | C (2), γ (1) | 2 |
| C | α (1), β (3) | 3 |
| γ, α, β | (partes compradas) | γ: 3; α, β: 4 |

Los *lead times* y los inventarios de estos ítems aparecen en la [L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md) (p. 3).

### Ejemplos resueltos

- **Roscoe Crossbody** (p. 9): BOM en formato de tabla de un bolso, con código, parte, descripción, cantidad por unidad y especificación para tres SKU.
- **Bicicleta** (p. 18): BOM de 3 niveles (Bike → manubrio, ensamble del marco y sillín; ensamble del marco → 2 ruedas y 1 marco; rueda → 25 radios y 1 rin; marco → 3 pies de tubo de aluminio y 0.5 gal de pintura). Usa unidades de longitud y volumen, justo lo que la regla 1 de la p. 21 pide evitar.
- **Carro** (p. 22): árbol de 4 niveles (Carro → Sub2, MOT, 4 Sil; Sub2 → SUB1, C, PAI; SUB1 → CHA, 4 RUE, ELE; C → 6 MET).
- **Demanda dependiente directa** (pp. 24-26): con $d_0=(100, 200, 0,\dots,0)$ (producto 1 = 100, producto 2 = 200), $dd(0)=(0, 0, 200, 200, 200, 100, 600, 0, 0)$ en el orden (1, 2, A, D, B, C, γ, α, β): A = 200, D = 200, B = 200, C = 100, γ = 600. La p. 26 advierte que "hace falta" calcular los requerimientos de los niveles siguientes. *Deducido* con $d_0(I-B)^{-1}$, la demanda total sería A = 200, D = 200, B = 800, C = 1900, γ = 1400, α = 2300, β = 5700.

### Páginas clave

- pp. 2-5: qué es y para qué sirve el MRP; p. 6: puntos de reorden contra MRP; p. 7: ERP / SAP.
- pp. 8 y 10: entradas; p. 11: limitaciones.
- p. 9: BOM tabular (Roscoe Crossbody); p. 18: BOM de la bicicleta; p. 22: BOM del carro.
- pp. 13-20: explosión de partes, diagramas, matriz BOM y niveles.
- pp. 23-26: demanda dependiente directa y ejemplo numérico.

### Relación con otros archivos del repo

- [L14 MRP](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md): continúa con este mismo BOM (1, 2, A, D, B, C, γ, α, β), agrega inventarios, *lead times* y el MPS, y arma la tabla MRP completa.
- [calculo-demanda-dependiente-directa](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/calculo-demanda-dependiente-directa.md): Excel con la misma matriz BOM, la explosión $dd(n)$ nivel por nivel y la inversa $(I-B)^{-1}$.
- [mrp-esfero](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero.md) y [mrp-esfero-v2](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero-v2.md): MRP de un esfero hecho en clase.
- [L15 MRP II](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md): agrega la capacidad que el MRP no considera.

## Contenido completo (página por página)

> La mayoría de las diapositivas lleva una franja inferior con fotos del campus y el logo de la Universidad de La Sabana (o una franja lateral derecha con foto del campus); no se repite en cada página.

### Página 1 — Operations Management: Material Requirements Planning (MRP)

Portada: "Operations Management" / "Material Requirements Planning (MRP)". Foto del edificio de la biblioteca y logo de la Universidad de La Sabana.

### Página 2 — MRP

- Productos con cientos de componentes
- Reducción de niveles de inventario
- Minimizar las paradas de producción por falta de materia prima
  - Mejor nivel de satisfacción de cliente
  - Alta utilización de planta
- Rápida respuesta a cambios del mercado

### Página 3 — Software disponible

> [Imagen: collage de logos de software MRP/ERP: The E2 Shop System ("The Authority on Shop Control Software"), Fishbowl, IQMS Manufacturing ERP, statii, JobBOSS ("Shop management solutions"), mie solutions ("Integrated Data. Informed Decisions."), Microsoft Dynamics GP, Deltek ("Know more. Do more."), Oracle JD Edwards, SAP Business One, McGladrey, polygon software y SAP.]

### Página 4 — MRP: Propósito

- Calcula el tiempo de producción/compra de componentes y materias primas de producto terminado, requerido para satisfacer el plan de producción.
- Minimizando el inventario de producto en proceso (WIP).

### Página 5 — MRP

- Sistema de inventario dependiente:
  - Componentes.
  - Más eficiente que modelos de inventario independiente (*EOQ*)
  - Mejor reacción ante picos de demanda
- Ha evolucionado a sistemas ERP
  - Enterprise Resource Planning.

### Página 6 — Sistema de Puntos de Reorden Vs Sistema MRP

> [Gráfico: dos columnas de tres gráficas escalonadas de inventario contra tiempo (*Time*): *End item* arriba, *Component* en medio y *Raw material* abajo.
> **Izquierda (puntos de reorden):** el inventario del producto final baja en escalones y, al cruzar el nivel de reorden R (línea punteada), se pide un lote que llega después de un *lead time* LT y lo repone (diente de sierra). Flechas punteadas muestran que cada pedido del producto final retira de golpe un lote del inventario de componentes; el componente tiene su propio R y LT, y su pedido a su vez retira materia prima, que también tiene R y LT. El componente y la materia prima **mantienen inventario alto casi todo el tiempo**.
> **Derecha (MRP):** el producto final tiene el mismo diente de sierra con R, pero el componente solo aparece como **pulsos rectangulares cortos** justo antes de cada pedido del producto final, y la materia prima como pulsos justo antes de los del componente. El resto del tiempo su inventario es cero.]

### Página 7 — ERP

> [Diagrama: círculo grande con el logo de SAP conectado a cinco módulos: **FI** (Bank accounts, Pricing strategy), **HR** (Salary infos, PII, SSN), **BW** (Vendors, Strategy details), **CRM** (Customer info, Credit cards) y **SRM** (RfPs, bids; Business negotiations; Supplier info).]

Título a la derecha: **SAP**.

> [Imagen: captura de pantalla de SAP Solution Manager (pestaña *Root Cause Analysis*, "Detailed Selection", "Change Reporting", lista *Store List* con entradas como ABAP_COMP_RELEASE, ABAP_NOTES, ABAP_PACKAGES, ABAP_TRANSPORTS). La letra pequeña es en su mayoría [ilegible].]

### Página 8 — Modelos de inventario dependiente

Se debe saber:

1. *Master production schedule*: Qué y cuándo producir.
2. Lista de materiales: BOM- bill of materials
3. Disponibilidad de inventarios
4. Ordenes de compra en curso.
5. Lead times.

### Página 9 — BOM

Encabezado del documento:

| Roscoe Crossbody | |
|---|---|
| Version: | FINAL |
| Date: | 10/13/12 |
| Drawn By: | MB |
| Page: | 3 of 3 |

| Code | Part | Description | #/Unit | RC3613 | RC4113 | RC3013 |
|---|---|---|---|---|---|---|
| A | Exterior Fabric | see SKU detail | | Feathers print 600x 300D Poly PU Coated | Stripes print 600x 300D Poly PU Coated | Umber color 12 oz. canvas Wax coating |
| B | Lining Fabric | 420D PU Coated Nylon | | Pink | Pink | Olive |
| C | Rectangle Ring | 1.5" Nickel | 1 | Nickel | Nickel | Nickel |
| D | Tri-glide | 1.5" Nickel | 1 | Nickel | Nickel | Nickel |
| E | Wire Hook | 45mm | 1 | Nickel | Nickel | Nickel |
| F | Zipper Pull | #5 Round Zipper Pull | 1 | Nickel | Nickel | Nickel |
| G | Accent Fabric | 12 oz. Wax Canvas | | Umber | Umber | Umber |
| H | Logo | Woven Logo | 1 | n/a | n/a | n/a |
| I | Zipper | #5 Nylon Coil Chain | 1 | Tan | Tan | Tan |
| J | Hidden Magnet | 18mm | 1 | n/a | n/a | n/a |
| K | Webbing | 1.5" PP | 1 | Tan | Tan | Tan |
| L | Webbing | .5" Gros Grain | 1 | Warm Gray | Warm Gray | Warm Gray |
| M | Elastic | 1" Braided Elastic | 1 | Pink, matches lining | Pink, matches lining | Olive, matches lining |
| N | Reflective Tape | .75" | 2 | Silver | Silver | Silver |
| O | Zipper | #3 Nylon Coil Chain | 1 | Tan | Tan | Tan |
| P | Zipper Pull | #3 Round Zipper Pull | 1 | Nickel | Nickel | Nickel |
| Q | Internal Fabric | 600x 300D Poly PVC Backed .55mm Neutral Color | | n/a | n/a | n/a |
| | Ball Chain | #3 | 1 | n/a | n/a | n/a |
| | Printed Tag Set S[ilegible, texto cortado] | 2"x4" Tags (2 in set) | 1 | n/a | n/a | n/a |
| | Country of Origin Label | Made in China | 1 | | | |

### Página 10 — Dinámica del MRP

- Los Inputs:
  - Plan maestro de producción
  - BOM
  - Lead times
  - Compras actuales
  - Inventario
- Estos datos cambian con frecuencia: re-optimizar frecuentemente. Moderadamente

### Página 11 — Limitaciones del MRP

- MRP realiza la planeación de los materiales, pero no programa.
  - NO dice la máquina en que debe procesarse un material, ni la hora.
- No considera restricciones de capacidad

### Página 12 — ¿Cuándo producir/comprar los componentes?

- Conozco el plan de producción
- Explosión de requerimientos/partes
- Tipos de ítems:
  - Producto terminado (*e*)
  - Subensambles (*s*)
  - Partes (*p*)

### Página 13 — Explosión de partes

- Sea $B^i = (b_{i1}, b_{i2},\dots, b_{ij})$,

*Donde* $b_{ij}$ = numero de unidades del ítem *j* requeridas para hacer directamente una unidad de ítem *i*.

$$\textit{Matriz BOM: } B=\begin{pmatrix}B^1\\ B^2\\ \cdots\\ B^n\end{pmatrix}$$

### Página 14 — Materials Requirement Diagram

> [Diagrama: dos árboles de un nivel. **1** → A **(2)** y C. **2** → B, γ **(3)** y D. Un recuadro naranja "Cantidad requerida" señala el número entre paréntesis (2) junto a A; los hijos sin número llevan cantidad 1.]

### Página 15 — (sin título)

> [Diagrama: **A** → B y α **(2)**. **B** → γ y C **(2)**.]

### Página 16 — (sin título)

> [Diagrama: **C** → β **(3)** y α. **D** → B **(2)** y C.]

### Página 17 — (sin título)

> [Diagrama: árbol completo del producto 1, sin cantidades. Nivel 1: 1 → A, C. Bajo A: B, α. Bajo B: γ, C. Bajo esa C: β, α. Bajo la C de primer nivel: β, α.]

Es decir:

- 1
  - A
    - B
      - γ
      - C
        - β
        - α
    - α
  - C
    - β
    - α

### Página 18 — Example of a BOM

> [Diagrama: BOM de una bicicleta con íconos (bicicleta, sillín, rueda, marco).]

- Bike (1)
  - Handlebars (1)
  - Frame assembly (1)
    - Wheel (2)
      - Spokes (25)
      - Tire Rims (1)
    - Frame (1)
      - Aluminum Tubing (3 feet)
      - Paint (0.5 gal)
  - Seat (1)

### Página 19 — Matriz BOM

Fila = ítem padre, columna = ítem hijo, celda = unidades del hijo por unidad del padre (las celdas vacías son 0).

| B | 1 | 2 | A | D | B | C | γ | α | β |
|---|---|---|---|---|---|---|---|---|---|
| **1** | | | 2 | | | 1 | | | |
| **2** | | | | 1 | 1 | | 3 | | |
| **A** | | | | | 1 | | | 2 | |
| **D** | | | | | 2 | 1 | | | |
| **B** | | | | | | 2 | 1 | | |
| **C** | | | | | | | | 1 | 3 |
| **γ** | | | | | | | | | |
| **α** | | | | | | | | | |
| **β** | | | | | | | | | |

Grupos de columnas: Producto Terminado (1, 2); Sub-ensambles (A, D, B, C); Partes (γ, α, β).

### Página 20 — Asignación de niveles en MRP

| NIVEL 0 | NIVEL 1 | NIVEL 2 | NIVEL 3 | NIVEL 4 |
|---|---|---|---|---|
| 1 | A | B | C | α |
| 2 | D | | γ | β |

El nivel es el número máximo de pasos de ensamblado requeridos para llegar a un producto final.

Se inicia a planear los requerimientos del nivel más alto al más bajo.

### Página 21 — Rules to build a good BOM

1. Don't use volumen, weight or lenght units -> use portions
2. Don't show processes or operations in the diagram
3. Don't show tools or machinery
4. Align equal ítems at the same level.

### Página 22 — (sin título): BOM de un carro

> [Diagrama de árbol: Carro → Sub2, MOT, 4 Sil. Sub2 → SUB1, C, PAI. SUB1 → CHA, 4 RUE, ELE. C → 6 MET. El número delante del nombre es la cantidad (4 Sil, 4 RUE, 6 MET); los demás son 1. Las abreviaturas no se definen en la diapositiva.]

- Carro (nivel 0)
  - Sub2
    - SUB1
      - CHA
      - 4 RUE
      - ELE
    - C
      - 6 MET
    - PAI
  - MOT
  - 4 Sil

### Página 23 — Cálculo de Demanda dependiente directa

- Considere: $d_n$ = vector de demanda en el nivel n.
- $dd(n)$ = vector de demanda dependiente directamente resultante en el nivel n.

Entonces:

$$dd(n)=d_n\times B$$

### Página 24 — Ejemplo numérico

- Usando la matriz mostrada previamente, y una demanda del producto 1 = 100, y producto 2 = 200. Calcule la demanda dependiente directa.

### Página 25 — Ejemplo numérico (solución)

$$dd(0)=d_0\times B=$$

$$=(100, 200, 0,\dots,0)\times B=$$

$$=(0,\ 0,\ 200,\ 200,\ 200,\ 100,\ 600,\ 0,\ 0)$$

(Orden de los componentes: 1, 2, A, D, B, C, γ, α, β. A = 2·100; D = 1·200; B = 1·200; C = 1·100; γ = 3·200.)

### Página 26 — Ejemplo numérico (solución)

Requerimientos de primer orden

| Item | Demanda |
|---|---|
| A | 200 |
| D | 200 |
| B | 200 |
| C | 100 |
| γ | 600 |

Hace falta los requerimientos para este plan de producción. (en rojo)


---

<!-- fuente: corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md -->
# L14-mrp

> **Archivo:** [`L14-mrp.pdf`](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.pdf) · **Corte 2** · 21 páginas  
> **Nombre original:** `CORTE 2/Lec 14 - MRP.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** construcción de la tabla MRP nivel por nivel para el BOM de la [L13](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md) (productos 1 y 2; ítems A, D, B, C, γ, α, β), con inventario disponible, *lead times* y MPS de 9 semanas. Luego se tratan el dimensionamiento de lotes, el MRP de ciclo cerrado y el nerviosismo del sistema.

### Ideas clave

- **Sistema MRP** (p. 2): MPS + BOM + archivo de estado del inventario → lógica MRP → programa de producción MRP.
- La tabla MRP de cada ítem tiene cinco filas por periodo: requerimientos brutos $G_{jt}$, entregas programadas $S_{jt}$, inventario esperado $I_{jt}$ (disponible al inicio del periodo), requerimientos netos $N_{jt}$ y liberación de órdenes planeadas (= recepción necesaria desplazada hacia atrás un *lead time*).
- **Procedimiento** (p. 10): (1) calcular la demanda directamente dependiente de cada periodo y cada producto con $dd(n)=d_n\times B$, usando las **liberaciones de órdenes** del nivel superior; (2) sumarla a los requerimientos brutos de los hijos (junto con su demanda independiente del MPS); (3) repetir hasta el último nivel. El requerimiento bruto de un hijo en la semana $t$ sale de las órdenes que liberan sus padres en esa semana $t$.
- Un ítem que aparece en varios niveles (B, C, γ, α) se planea **una sola vez**, en su nivel más bajo, después de todos sus padres.
- **Liberación de órdenes = problema de optimización (*lot sizing*)** (pp. 13-14): lote a lote (si ordenar cuesta poco), EOQ determinístico (supone demanda constante), Wagner-Whitin y Silver-Meal ([carpeta 03](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/README.md)).
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

- [L13 BOM e intro al MRP](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md): matriz BOM y niveles usados aquí.
- [calculo-demanda-dependiente-directa](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/calculo-demanda-dependiente-directa.md): la misma explosión $d\times B$ en Excel.
- [mrp-esfero](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero.md) y [mrp-esfero-v2](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero-v2.md): la tabla MRP con las mismas fórmulas $I_{jt}$ y $N_{jt}$, armada en Excel ("CONSTRUIR EXCEL", p. 10).
- [Wagner-Whitin y Silver-Meal](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/L12-wagner-whitin-and-silver-meal.md): políticas de dimensionamiento de lotes.
- [L15 MRP II](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md): MRP de ciclo cerrado y capacidad.
- [Parcial 2](/corte-2-planeacion-agregada-mrp/parcial-2/parcial-2-solucion.md): punto 2.3, matriz MRP.

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


---

<!-- fuente: corte-2-planeacion-agregada-mrp/04-bom-y-mrp/calculo-demanda-dependiente-directa.md -->
# calculo-demanda-dependiente-directa

> **Archivo:** [`calculo-demanda-dependiente-directa.xlsx`](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/calculo-demanda-dependiente-directa.xlsx) · **Corte 2** (el archivo estaba en la carpeta `CORTE 3/` del estudiante) · Libro de Excel con 1 hoja(s): `Hoja1`  
> **Nombre original:** `CORTE 3/Cálculo de Demanda Dependiente Directa.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Libro de una hoja que hace la **explosión de materiales** del BOM de clase (productos 1 y 2; subensambles A, D, B y C; partes γ, α y β) de la [L13](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md) (pp. 13-26) con dos métodos equivalentes:

1. la demanda dependiente directa nivel por nivel, $dd(n)=d_n\times B$, con `MMULT`;
2. la matriz de requerimientos totales $(I-B)^{-1}$, con `MINVERSE`.

Estaba en la carpeta del Corte 3 (nombre original `CORTE 3/Cálculo de Demanda Dependiente Directa.xlsx`, por eso la cabecera dice "Corte 3"), pero el tema es BOM/MRP del Corte 2. Se aprende a pasar de la demanda de productos terminados a la demanda total de cada componente, sumando todos los niveles.

### Datos de entrada

**Matriz BOM $B$** (A2:J12; fila = padre, columna = hijo, valor = unidades del hijo por unidad del padre). Es la misma matriz de la L13, p. 19:

| B | 1 | 2 | A | D | B | C | γ | α | β |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 | 1 | 1 | 0 | 3 | 0 | 0 |
| A | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 0 |
| D | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 |
| B | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 |
| C | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 |
| γ | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| α | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| β | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Grupos: Producto Terminado (1, 2), Sub-ensambles (A, D, B, C), Partes (γ, α, β).

Árbol equivalente (cantidad por padre entre paréntesis): 1 → A (2), C (1); 2 → D (1), B (1), γ (3); A → B (1), α (2); D → B (2), C (1); B → C (2), γ (1); C → α (1), β (3). Niveles (L13, p. 20): 0 = {1, 2}; 1 = {A, D}; 2 = {B}; 3 = {C, γ}; 4 = {α, β}. Este libro no usa *lead times* (son los de la [L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md), p. 3).

**Demanda de productos terminados** (fila 3, M3:U3): producto 1 = **80**, producto 2 = **50**, los demás 0. Es distinta de la del ejemplo de la L13 (100 y 200).

**Matriz identidad $I$** (A14:J24): identidad 9×9 escrita a mano.

### Método paso a paso

1. **Demanda dependiente directa nivel por nivel** (fórmulas matriciales):
   - `M5:U5 = MMULT(M3:U3, B4:J12)`, es decir $DD(1)=d\,B$.
   - `M7:U7 = MMULT(M5:U5, B4:J12)`, es decir $DD(2)=DD(1)\,B=d\,B^2$.
   - `M9:U9`, `M11:U11` y `M13:U13` repiten el producto: $DD(3)=d\,B^3$, $DD(4)=d\,B^4$, $DD(5)=d\,B^5$.
   - `M15:U15 = SUM(M3:M13)` (una por columna): **demanda total** $=d+DD(1)+\dots+DD(5)=d\,(I+B+B^2+B^3+B^4+B^5)$.

   La numeración del libro está corrida un lugar respecto de la L13: el $dd(0)=d_0\times B$ de las diapositivas es el "DD (1)" del Excel.

2. **Matriz de requerimientos totales:**
   - `B28:J36`: $(I-B)$, celda a celda (`B28 = B16-B4`, etc.).
   - `B40:J48 = MINVERSE(B28:J36)`, es decir $(I-B)^{-1}$. Como la BOM no tiene ciclos, $B^5=0$ y $(I-B)^{-1}=I+B+B^2+B^3+B^4$. Cada fila dice cuántas unidades de cada ítem requiere, en total, una unidad del ítem de esa fila.

### Resultados

**Explosión nivel por nivel** (orden de columnas: 1, 2, A, D, B, C, γ, α, β):

| Fila | 1 | 2 | A | D | B | C | γ | α | β |
|---|---|---|---|---|---|---|---|---|---|
| Demanda $d$ | 80 | 50 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| DD (1) | 0 | 0 | 160 | 50 | 50 | 80 | 150 | 0 | 0 |
| DD (2) | 0 | 0 | 0 | 0 | 260 | 150 | 50 | 400 | 240 |
| DD(3) | 0 | 0 | 0 | 0 | 0 | 520 | 260 | 150 | 450 |
| DD(4) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 520 | 1560 |
| DD(5) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **DD TOTAL** | **80** | **50** | **160** | **50** | **310** | **750** | **460** | **1070** | **2250** |

De dónde sale, por ejemplo: DD (1): A = 2·80, D = 1·50, B = 1·50, C = 1·80, γ = 3·50. DD (2): B = 1·160 (de A) + 2·50 (de D) = 260; C = 1·50 (de D) + 2·50 (de B) = 150; γ = 1·50 (de B); α = 2·160 (de A) + 1·80 (de C) = 400; β = 3·80 = 240. DD(3): C = 2·260 = 520; γ = 260; α = 150; β = 3·150 = 450. DD(4): α = 520; β = 3·520 = 1560.

**Matriz $(I-B)$** (B28:J36):

| (I-B) | 1 | 2 | A | D | B | C | γ | α | β |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 0 | -2 | 0 | 0 | -1 | 0 | 0 | 0 |
| 2 | 0 | 1 | 0 | -1 | -1 | 0 | -3 | 0 | 0 |
| A | 0 | 0 | 1 | 0 | -1 | 0 | 0 | -2 | 0 |
| D | 0 | 0 | 0 | 1 | -2 | -1 | 0 | 0 | 0 |
| B | 0 | 0 | 0 | 0 | 1 | -2 | -1 | 0 | 0 |
| C | 0 | 0 | 0 | 0 | 0 | 1 | 0 | -1 | -3 |
| γ | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| α | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| β | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |

**Matriz de requerimientos totales $(I-B)^{-1}$** (B40:J48):

| (I-B)⁻¹ | 1 | 2 | A | D | B | C | γ | α | β |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | 0 | 2 | 0 | 2 | 5 | 2 | 9 | 15 |
| 2 | 0 | 1 | 0 | 1 | 3 | 7 | 6 | 7 | 21 |
| A | 0 | 0 | 1 | 0 | 1 | 2 | 1 | 4 | 6 |
| D | 0 | 0 | 0 | 1 | 2 | 5 | 2 | 5 | 15 |
| B | 0 | 0 | 0 | 0 | 1 | 2 | 1 | 2 | 6 |
| C | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 3 |
| γ | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| α | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| β | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |

Lectura: una unidad del producto 1 necesita en total 2 A, 2 B, 5 C, 2 γ, 9 α y 15 β; una unidad del producto 2 necesita 1 D, 3 B, 7 C, 6 γ, 7 α y 21 β.

**Verificación (hecha en esta explicación, no está en el libro):** $d\,(I-B)^{-1}=80\cdot\text{fila}_1+50\cdot\text{fila}_2=(80, 50, 160, 50, 310, 750, 460, 1070, 2250)$, igual a la fila DD TOTAL. Los dos métodos coinciden.

### Gráficos

No hay.

### Conclusión

Para 80 unidades del producto 1 y 50 del producto 2 se necesitan en total 160 A, 50 D, 310 B, 750 C, 460 γ, 1070 α y 2250 β. La matriz $(I-B)^{-1}$ da el mismo resultado en un solo paso y sirve para cualquier otro vector de demanda. Con la demanda de la L13 (100 y 200) daría A = 200, D = 200, B = 800, C = 1900, γ = 1400, α = 2300 y β = 5700 (deducido).

### Observaciones

- La explosión no considera inventarios, recepciones ni *lead times*: son requerimientos **brutos** totales, sin fases de tiempo. La versión con tiempos es la tabla MRP de la [L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md).
- La fila `DD(5)` sale en ceros: confirma que la BOM tiene 5 niveles (0 a 4).
- La numeración `DD (1)…DD(5)` está corrida un lugar respecto del $dd(0), dd(1),\dots$ de las diapositivas.
- El producto $d\times(I-B)^{-1}$ no está calculado en el libro.
- Archivo ubicado originalmente en el Corte 3; corresponde al tema BOM/MRP del Corte 2.


---

<!-- fuente: corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero-v2.md -->
# mrp-esfero-v2

> **Archivo:** [`mrp-esfero-v2.xlsx`](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero-v2.xlsx) · **Corte 2** · Libro de Excel con 1 hoja(s): `Hoja1`  
> **Nombre original:** `CORTE 2/MRP 2.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Segunda versión, corregida y ampliada, del MRP del **esfero** de [mrp-esfero](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero.md). Una hoja (`Hoja1`) con 6 tablas MRP de 10 semanas, una por ítem del BOM, enlazadas con fórmulas: el requerimiento bruto de cada componente sale de las liberaciones de órdenes de su padre multiplicadas por la cantidad del BOM. Cada ítem tiene su *lead time* y sus costos de ordenar y de mantener. Aplica la explosión nivel por nivel de la [L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md) (pp. 7-12) y la idea de la [L13](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md) de que la demanda de los componentes es dependiente.

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

Idéntico al bloque 1 de [mrp-esfero](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero.md).

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

*Deducido:* liberando en las semanas 2 y 4 (justo a tiempo con LT = 1), el costo de mantener bajaría a $0.01\times(1300+80+80)=14.6$ y el total a 34.6. Los requerimientos netos de este ítem (2380 en la semana 3 y 2500 en la semana 5) son exactamente la demanda que usa [`wagner_whitin.py`](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/README.md).

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
- Diferencias con la primera versión: ver la tabla al final de [mrp-esfero](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero.md#diferencias-con-mrp-esfero-v2xlsx).


---

<!-- fuente: corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero.md -->
# mrp-esfero

> **Archivo:** [`mrp-esfero.xlsx`](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero.xlsx) · **Corte 2** · Libro de Excel con 1 hoja(s): `Hoja1`  
> **Nombre original:** `CORTE 2/MRP.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Primera versión del MRP de un **esfero** (bolígrafo) hecha en Excel en clase, siguiendo el "CONSTRUIR EXCEL" de la [L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md) (p. 10) con las mismas fórmulas de inventario esperado y requerimiento neto. Tiene una sola hoja (`Hoja1`) con cuatro bloques MRP de 10 semanas. Solo el primero (el esfero, producto final) está completo y es factible; los otros tres son borradores de los componentes: todos se titulan "item, final: esfero", tienen valores escritos a mano y no están enlazados por fórmulas. La versión corregida y completa es [mrp-esfero-v2](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero-v2.md); las diferencias están al final.

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

| Aspecto | mrp-esfero (esta versión) | [mrp-esfero-v2](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero-v2.md) |
|---|---|---|
| Bloques | 4, todos titulados "esfero" | 6 con nombre: Esfero, Cuerpo, Tapa Arriba, Tapa, Cilindro, Mina de Tinta |
| *Lead times* | 3 en todos | 3, 2, 1, 0, 0, 0 |
| Requerimientos brutos de componentes | Escritos a mano | Fórmulas que implementan el BOM: `=D7` (1 por esfero), `=2*D7` (2 tapas arriba por esfero), `=D14` (1 por cuerpo) |
| Costos | Bloques 1 y 2 (\$80 por orden; \$0.05 por unidad-periodo) | Uno por ítem, con tarifas distintas (80/0.05, 80/0.04, 10/0.01, 50 y 1500 escritos a mano, 5/0.01, 4/0.01) |
| Factibilidad | Solo el esfero; los demás bloques tienen faltantes | Esfero, Cuerpo y Tapa Arriba factibles; Tapa sin resolver; Cilindro y Mina con el faltante del periodo 1 oculto |
| Bloque del esfero | Igual | Igual (mismos datos, fórmulas y costo 549.5) |
| Periodos 8-10 | "x" en la liberación, sin errores | Las "X" se propagan como `#VALUE!` en los componentes |
