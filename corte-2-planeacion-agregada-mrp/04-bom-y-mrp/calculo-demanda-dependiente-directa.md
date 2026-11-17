# calculo-demanda-dependiente-directa

> **Archivo:** [`calculo-demanda-dependiente-directa.xlsx`](./calculo-demanda-dependiente-directa.xlsx) · **Corte 2** (el archivo estaba en la carpeta `CORTE 3/` del estudiante) · Libro de Excel con 1 hoja(s): `Hoja1`  
> **Nombre original:** `CORTE 3/Cálculo de Demanda Dependiente Directa.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Libro de una hoja que hace la **explosión de materiales** del BOM de clase (productos 1 y 2; subensambles A, D, B y C; partes γ, α y β) de la [L13](./L13-bom-intro-to-mrp.md) (pp. 13-26) con dos métodos equivalentes:

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

Árbol equivalente (cantidad por padre entre paréntesis): 1 → A (2), C (1); 2 → D (1), B (1), γ (3); A → B (1), α (2); D → B (2), C (1); B → C (2), γ (1); C → α (1), β (3). Niveles (L13, p. 20): 0 = {1, 2}; 1 = {A, D}; 2 = {B}; 3 = {C, γ}; 4 = {α, β}. Este libro no usa *lead times* (son los de la [L14](./L14-mrp.md), p. 3).

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

- La explosión no considera inventarios, recepciones ni *lead times*: son requerimientos **brutos** totales, sin fases de tiempo. La versión con tiempos es la tabla MRP de la [L14](./L14-mrp.md).
- La fila `DD(5)` sale en ceros: confirma que la BOM tiene 5 niveles (0 a 4).
- La numeración `DD (1)…DD(5)` está corrida un lugar respecto del $dd(0), dd(1),\dots$ de las diapositivas.
- El producto $d\times(I-B)^{-1}$ no está calculado en el libro.
- Archivo ubicado originalmente en el Corte 3; corresponde al tema BOM/MRP del Corte 2.

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `Hoja1` — 48 filas × 21 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | BOM | Producto Terminado |  | Sub-ensambles |  |  |  | Partes |  |  |  |  | 1 | 2 | A | D | B | C | γ | α | β |
| 3 |  | 1 | 2 | A | D | B | C | γ | α | β |  | Demanda | 80 | 50 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 4 | 1 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 5 | 2 | 0 | 0 | 0 | 1 | 1 | 0 | 3 | 0 | 0 |  | DD (1) | 0 | 0 | 160 | 50 | 50 | 80 | 150 | 0 | 0 |
| 6 | A | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 7 | D | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 |  | DD (2) | 0 | 0 | 0 | 0 | 260 | 150 | 50 | 400 | 240 |
| 8 | B | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 9 | C | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 |  | DD(3) | 0 | 0 | 0 | 0 | 0 | 520 | 260 | 150 | 450 |
| 10 | γ | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 11 | α | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | DD(4) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 520 | 1560 |
| 12 | β | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 13 |  |  |  |  |  |  |  |  |  |  |  | DD(5) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 14 | I | Producto Terminado |  | Sub-ensambles |  |  |  | Partes |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 15 |  | 1 | 2 | A | D | B | C | γ | α | β |  | DD TOTAL | 80 | 50 | 160 | 50 | 310 | 750 | 460 | 1070 | 2250 |
| 16 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 17 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 18 | A | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 19 | D | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 20 | B | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 21 | C | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 22 | γ | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 23 | α | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 24 | β | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| 26 | (I-B) | Producto Terminado |  | Sub-ensambles |  |  |  | Partes |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 27 |  | 1 | 2 | A | D | B | C | γ | α | β |  |  |  |  |  |  |  |  |  |  |  |
| 28 | 1 | 1 | 0 | -2 | 0 | 0 | -1 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 29 | 2 | 0 | 1 | 0 | -1 | -1 | 0 | -3 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 30 | A | 0 | 0 | 1 | 0 | -1 | 0 | 0 | -2 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 31 | D | 0 | 0 | 0 | 1 | -2 | -1 | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 32 | B | 0 | 0 | 0 | 0 | 1 | -2 | -1 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 33 | C | 0 | 0 | 0 | 0 | 0 | 1 | 0 | -1 | -3 |  |  |  |  |  |  |  |  |  |  |  |
| 34 | γ | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 35 | α | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 36 | β | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| 38 | (I-B)-1 | Producto Terminado |  | Sub-ensambles |  |  |  | Partes |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 39 |  | 1 | 2 | A | D | B | C | γ | α | β |  |  |  |  |  |  |  |  |  |  |  |
| 40 | 1 | 1 | 0 | 2 | 0 | 2 | 5 | 2 | 9 | 15 |  |  |  |  |  |  |  |  |  |  |  |
| 41 | 2 | 0 | 1 | 0 | 1 | 3 | 7 | 6 | 7 | 21 |  |  |  |  |  |  |  |  |  |  |  |
| 42 | A | 0 | 0 | 1 | 0 | 1 | 2 | 1 | 4 | 6 |  |  |  |  |  |  |  |  |  |  |  |
| 43 | D | 0 | 0 | 0 | 1 | 2 | 5 | 2 | 5 | 15 |  |  |  |  |  |  |  |  |  |  |  |
| 44 | B | 0 | 0 | 0 | 0 | 1 | 2 | 1 | 2 | 6 |  |  |  |  |  |  |  |  |  |  |  |
| 45 | C | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 3 |  |  |  |  |  |  |  |  |  |  |  |
| 46 | γ | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 47 | α | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 48 | β | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  |  |  |  |  |  |  |  |  |  |  |

**Fórmulas (18 patrones distintos):**

- `M15`: `=SUM(M3:M13)`
- `N15`: `=SUM(N3:N13)`
- `O15`: `=SUM(O3:O13)`
- `P15`: `=SUM(P3:P13)`
- `Q15`: `=SUM(Q3:Q13)`
- `R15`: `=SUM(R3:R13)`
- `S15`: `=SUM(S3:S13)`
- `T15`: `=SUM(T3:T13)`
- `U15`: `=SUM(U3:U13)`
- `B28`: `=B16-B4`
- `C28`: `=C16-C4`
- `D28`: `=D16-D4`
- `E28`: `=E16-E4`
- `F28`: `=F16-F4`
- `G28`: `=G16-G4`
- `H28`: `=H16-H4`
- `I28`: `=I16-I4`
- `J28`: `=J16-J4`

