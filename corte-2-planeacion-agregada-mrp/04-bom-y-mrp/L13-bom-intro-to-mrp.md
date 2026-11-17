# L13-bom-intro-to-mrp

> **Archivo:** [`L13-bom-intro-to-mrp.pdf`](./L13-bom-intro-to-mrp.pdf) · **Corte 2** · 26 páginas  
> **Nombre original:** `CORTE 2/Lec 13 - BOM intro to MRP.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** introducción al MRP (*Material Requirements Planning*): demanda dependiente, lista de materiales (BOM), matriz BOM, asignación de niveles y cálculo de la demanda dependiente directa con $dd(n)=d_n\times B$.

### Ideas clave

- El MRP sirve para productos con cientos de componentes: reduce inventarios, evita paradas por falta de materia prima (mejor servicio al cliente, alta utilización de planta) y responde rápido a cambios del mercado (p. 2).
- **Propósito** (p. 4): calcular cuándo producir o comprar los componentes y materias primas del producto terminado para cumplir el plan de producción, minimizando el inventario en proceso (WIP).
- Es un sistema de **inventario dependiente**: más eficiente que los modelos de inventario independiente (EOQ) y reacciona mejor ante picos de demanda; evolucionó hacia los ERP (p. 5). Con puntos de reorden, los componentes y materias primas se mantienen en inventario todo el tiempo; con MRP solo aparecen justo antes de que se necesiten (p. 6).
- **Entradas** (pp. 8 y 10): programa maestro de producción (MPS: qué y cuándo), BOM, disponibilidad de inventarios, órdenes de compra en curso y *lead times*. Como cambian con frecuencia, hay que re-optimizar "moderadamente" seguido.
- **Limitaciones** (p. 11): planea materiales pero no programa (no dice en qué máquina ni a qué hora) y no considera restricciones de capacidad (eso lo agrega el MRP II, [carpeta 05](../05-mrp-ii-y-capacidad/)).
- Tipos de ítems (p. 12): producto terminado (*e*), subensambles (*s*) y partes (*p*). La **explosión de partes** recorre la BOM de arriba hacia abajo.
- El **nivel** de un ítem es el número máximo de pasos de ensamble que lo separan de un producto final; se planea del nivel más alto (0) al más bajo (p. 20).
- Reglas para una buena BOM (p. 21): no usar unidades de volumen, peso o longitud (usar porciones), no mostrar procesos ni operaciones, no mostrar herramientas ni maquinaria, y alinear los ítems iguales en el mismo nivel.

### Fórmulas y métodos

- **Vector BOM de un ítem** (p. 13): $B^i=(b_{i1}, b_{i2}, \dots, b_{ij})$, donde $b_{ij}$ es el número de unidades del ítem $j$ requeridas para hacer **directamente** una unidad del ítem $i$.
- **Matriz BOM**: $B=\begin{pmatrix}B^1\\ B^2\\ \vdots\\ B^n\end{pmatrix}$ (fila = padre, columna = hijo).
- **Demanda dependiente directa** (p. 23): $dd(n)=d_n\times B$, donde $d_n$ es el vector (fila) de demanda en el nivel $n$ y $dd(n)$ el vector de demanda que resulta directamente en los ítems hijos. Se aplica nivel por nivel.
- *Complemento deducido, no está en las diapositivas:* la demanda total (todos los niveles) es $d\,(I+B+B^2+\dots)=d\,(I-B)^{-1}$; así lo calcula el Excel [calculo-demanda-dependiente-directa](./calculo-demanda-dependiente-directa.md).

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

Los *lead times* y los inventarios de estos ítems aparecen en la [L14](./L14-mrp.md) (p. 3).

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

- [L14 MRP](./L14-mrp.md): continúa con este mismo BOM (1, 2, A, D, B, C, γ, α, β), agrega inventarios, *lead times* y el MPS, y arma la tabla MRP completa.
- [calculo-demanda-dependiente-directa](./calculo-demanda-dependiente-directa.md): Excel con la misma matriz BOM, la explosión $dd(n)$ nivel por nivel y la inversa $(I-B)^{-1}$.
- [mrp-esfero](./mrp-esfero.md) y [mrp-esfero-v2](./mrp-esfero-v2.md): MRP de un esfero hecho en clase.
- [L15 MRP II](../05-mrp-ii-y-capacidad/L15-mrp-ii.md): agrega la capacidad que el MRP no considera.

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

## Anexo: texto extraído automáticamente del PDF

> Texto plano tal como sale del PDF, sin fórmulas ni tablas que estén como imagen. La versión fiel y completa es la sección «Contenido completo» de arriba.

### Página 1 · 1 imagen(es)

Operations Management
Material Requirements 
Planning (MRP)

### Página 2 · 1 imagen(es)

MRP
• Productos con cientos de componentes
• Reducción de niveles de inventario
• Minimizar las paradas de producción por 
falta de materia prima
– Mejor nivel de satisfacción de cliente
– Alta utilización de planta
• Rápida respuesta a cambios del mercado

### Página 3 · 14 imagen(es)

Software disponible

### Página 4 · 1 imagen(es)

MRP: Propósito
• Calcula el tiempo de 
producción/compra de componentes 
y materias primas de producto 
terminado, requerido para satisfacer 
el plan de producción.
• Minimizando el inventario de 
producto en proceso (WIP).

### Página 5 · 1 imagen(es)

MRP
• Sistema de inventario dependiente:
– Componentes.
– Más eficiente que modelos de 
inventario independiente (EOQ)
– Mejor reacción ante picos de demanda
• Ha evolucionado a sistemas ERP
– Enterprise Resource Planning.

### Página 6 · 3 imagen(es)

Sistema de Puntos de 
Reorden Vs Sistema MRP

### Página 7 · 3 imagen(es)

ERP
SAP

### Página 8 · 1 imagen(es)

Modelos de inventario 
dependiente
Se debe saber:
1. Master production schedule: Qué y cuándo 
producir.
2. Lista de materiales: BOM- bill of materials
3. Disponibilidad de inventarios
4. Ordenes de compra en curso. 
5. Lead times.

### Página 9 · 2 imagen(es)

BOM

### Página 10 · 1 imagen(es)

Dinámica del MRP
• Los Inputs: 
– Plan maestro de producción
– BOM
– Lead times
– Compras actuales
– Inventario
• Estos datos cambian con frecuencia: re-optimizar 
frecuentemente. Moderadamente

### Página 11 · 1 imagen(es)

Limitaciones del MRP
• MRP realiza la planeación de los 
materiales, pero no programa.
– NO dice la máquina en que debe 
procesarse un material, ni la hora.
• No considera restricciones de 
capacidad

### Página 12 · 1 imagen(es)

¿Cuándo 
producir/comprar los 
componentes?
• Conozco el plan de producción
• Explosión de requerimientos/partes
• Tipos de ítems:
– Producto terminado (e)
– Subensambles (s)
– Partes (p)

### Página 13 · 1 imagen(es)

Explosión de partes
• Sea Bi = (bi1, bi2,…, bij),
Donde bij = numero de unidades del ítem j 
requeridas para hacer directamente una 
unidad de ítem i. 
Matriz BOM: 𝐵=
𝐵1
𝐵2
…
𝐵𝑛

### Página 14 · 3 imagen(es)

Materials Requirement 
Diagram
1
A
C
(2)
2
B
γ 
D
(3)
Cantidad 
requerida

### Página 15 · 3 imagen(es)

A
B
α
(2)
B
γ 
C
(2)

### Página 16 · 3 imagen(es)

C
β
α
(3)
D
B
C
(2)

### Página 17 · 1 imagen(es)

1
A
B
γ 
C
β 
α
α
C
β 
α

### Página 18 · 2 imagen(es)

Example of a BOM

### Página 19 · 1 imagen(es)

Matriz BOM
B
Producto 
Terminado
Sub-ensambles
Partes
1
2
A
D
B
C
γ
α
β
1
2
1
2
1
1
3
A
1
2
D
2
1
B
2
1
C
1
3
γ
α
β

### Página 20 · 1 imagen(es)

Asignación de niveles en 
MRP
NIVEL
0
1
2
3
4
1
A
B
C
α
2
D
γ
β
El nivel es el número máximo de pasos de ensamblado requeridos para 
llegar a un producto final.
Se inicia a planear los requerimientos del nivel más alto al más bajo.

### Página 21 · 1 imagen(es)

Rules to build a 
good BOM
1. Don’t use volumen, weight or lenght 
units -> use portions
2. Don’t show processes or operations 
in the diagram
3. Don’t show tools or machinery
4. Align equal ítems at the same level.

### Página 22 · 1 imagen(es)

Carro
Sub2
SUB1
CHA
4 RUE
ELE
C
6 MET
PAI
MOT
4 Sil

### Página 23 · 1 imagen(es)

Cálculo de Demanda 
dependiente directa
• Considere: 𝑑𝑛= vector de demanda 
en el nivel n.
• 𝑑𝑑𝑛= vector de demanda 
dependiente directamente resultante 
en el nivel n.
Entonces: 
𝑑𝑑𝑛= 𝑑𝑛 × 𝐵

### Página 24 · 1 imagen(es)

Ejemplo numérico
• Usando la matriz mostrada 
previamente, y una demanda del 
producto 1 = 100, y producto 2 = 
200. Calcule la demanda 
dependiente directa.

### Página 25 · 1 imagen(es)

Ejemplo numérico 
(solución)
𝑑𝑑0 = 𝑑𝑜 × 𝐵= 
= (100, 200, 0,…0) × 𝐵 = 
= (0, 0, 200, 200, 200, 100, 600, 0, 0)

### Página 26 · 2 imagen(es)

Item
Demanda
A
200
D
200
B
200
C
100
γ
600
Requerimientos de primer orden
Hace falta los requerimientos para este plan de producción.

