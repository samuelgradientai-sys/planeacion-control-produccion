# backward-scheduling

> **Archivo:** [`backward-scheduling.xlsx`](./backward-scheduling.xlsx) · **Corte 2** (el archivo estaba en la carpeta `CORTE 3/` del estudiante) · Libro de Excel con 1 hoja(s): `Hoja1`  
> **Nombre original:** `CORTE 3/Backward Scheduling.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Hoja de cálculo que rehace en Excel el **CRP con backward scheduling** del ejemplo de los productos γ y β de la clase de MRP II ([`L15-mrp-ii.md`](./L15-mrp-ii.md), pp. 30-42). Para cada lote (300γ, 575γ y 2000β) reparte por semana los minutos de alistamiento + máquina de cada centro de trabajo (WC1, WC2, WC4) y del movimiento entre estaciones, programando hacia atrás desde la fecha de entrega. Después calcula los minutos que quedan disponibles cada semana (2400 min = 40 h).

**Ubicación:** aunque el archivo original estaba en la carpeta `CORTE 3` (por eso la cabecera dice «Corte 3»), su contenido es el ejemplo de planeación de requerimientos de capacidad (CRP) de MRP II de la L15, Corte 2. Está bien ubicado en esta carpeta. No es scheduling de máquinas del Corte 3: no secuencia trabajos, solo reparte cargas por semana.

Con él se aprende a convertir cada lote en minutos por estación y semana con la fórmula $S+Q\,p$. Se respetan un día de movimiento (480 min) entre operaciones y la capacidad de 2400 min/semana, y se pasa a la semana anterior lo que no cabe.

### Hoja `Hoja1`

#### Objetivo (deducido)

Programar hacia atrás los lotes de la L15 (p. 30): 300γ y 2000β se entregan en la semana 3 y 575γ en la semana 4. Hay que obtener la carga en minutos por semana en cada centro de trabajo y el tiempo disponible restante.

#### Datos de entrada y parámetros

Tabla de parámetros de γ (rango `I2:N5`, título «γ» en `I2`):

| Centro | SU-time (min por lote) | MACH-time (min por unidad) | Celdas |
|---|---|---|---|
| WC1 | 120 | 3 | `I5`, `J5` |
| WC2 | 90 | 5 | `K5`, `L5` |
| WC4 | 30 | 2 | `M5`, `N5` |

Otros parámetros:

| Parámetro | Valor | Celda |
|---|---|---|
| Movimientos (1 día = 8 h × 60 min) | 480 min | `J7` |
| Capacidad semanal (min/semana = 60 × 8 × 5) | 2400 min | `J8` |

Segunda tabla de parámetros (rango `I10:L13`, encabezados `I11` = «WC2», `K11` = «WC4»; el título fusionado `I10:L10` está vacío):

| Centro | SU-time | MACH-time | Celdas |
|---|---|---|---|
| WC2 | 90 | 5 | `I13`, `J13` |
| WC4 | 30 | 2 | `K13`, `L13` |

Esta segunda tabla repite los valores de γ. Según la L15 (p. 31), β usa WC2 con SU = 120 y MACH = 1.8, y WC4 con SU = 30 y MACH = 0.2; esos datos **no aparecen** en el Excel.

Tamaños de lote: 300 y 575 (γ) y 2000 (β), escritos directamente dentro de las fórmulas.

#### Método paso a paso

Minutos que ocupa un lote de tamaño $Q$ en el centro $k$:

$$T_k = S_k + Q\,p_k$$

donde $S_k$ = SU-time (min por lote) y $p_k$ = MACH-time (min por unidad). Disponible de la semana $s$ para un lote:

$$\text{Disp}_s = 2400 - (\text{WC1}_s+\text{WC2}_s+\text{WC4}_s+\text{Mov}_s)$$

**Bloque 1: Lote 300γ (filas 2-6)**, entrega en la semana 3, así que se programa en las semanas 2 y 1.

| Celda | Fórmula | Significado | Valor |
|---|---|---|---|
| `E4` (S2, WC4) | `=M5+(N5*300)` | $30+2\times300$ | 630 |
| `F4` (S2, Mov.) | `=J7` | movimiento WC2→WC4 | 480 |
| `D4` (S2, WC2) | `=K5+(L5*300)-300` | $90+5\times300-300$: total de WC2 (1590) menos los 300 que se pasan a la semana 1 | 1290 |
| `G4` (S2, Disp.) | `=J8-(SUM(C4:F4))` | $2400-(1290+630+480)$ | 0 |
| `C6` (S1, WC1) | `=I5+(J5*300)` | $120+3\times300$ | 1020 |
| `D6` (S1, WC2) | 300 (valor fijo) | resto de WC2 | 300 |
| `F6` (S1, Mov.) | `=J7` | movimiento WC1→WC2 | 480 |
| `G6` (S1, Disp.) | `=J8-(SUM(C6:F6))` | $2400-(1020+300+480)$ | 600 |

**Bloque 2: Lote 575γ (filas 8-14)**, entrega en la semana 4, así que se programa en las semanas 3, 2 y 1.

| Celda | Fórmula | Significado | Valor |
|---|---|---|---|
| `E10` (S3, WC4) | `=M5+(N5*575)` | $30+2\times575$ | 1180 |
| `F10` (S3, Mov.) | `=J7` | movimiento WC2→WC4 | 480 |
| `D10` (S3, WC2) | `=K5+(L5*575)-2225` | $90+5\times575-2225=2965-2225$ | 740 |
| `G10` (S3, Disp.) | `=$J$8-SUM(C10:F10)` | $2400-(740+1180+480)$ | 0 |
| `D12` (S2, WC2) | 2225 (valor fijo) | resto de WC2 | 2225 |
| `F12` (S2, Mov.) | 175 (valor fijo) | parte del movimiento WC1→WC2 que cabe en la semana 2 | 175 |
| `G12` (S2, Disp.) | `=$J$8-(SUM(C12:F12))` | $2400-(2225+175)$ | 0 |
| `C14` (S1, WC1) | `=I5+(J5*300)` | **usa 300 en vez de 575** | 1020 |
| `F14` (S1, Mov.) | `=480+F12` | **suma en vez de restar** | 655 |
| `G14` (S1, Disp.) | `=J8-(SUM(C14:F14))` | $2400-(1020+655)$ | 725 |

**Bloque 3: Lote 2000β (filas 16-22).** Es una copia del bloque 575γ con las referencias desplazadas, sin adaptar a β.

| Celda | Fórmula | Qué calcula realmente | Valor |
|---|---|---|---|
| `D18` (S3, WC2) | `=K13+(L13*575)-2225` | $30+2\times575-2225$ (parámetros de WC4 de γ y lote 575) | −1045 |
| `E18` (S3, WC4) | `=M13+(N13*575)` | celdas vacías | 0 |
| `F18` (S3, Mov.) | `=J15` | celda vacía | 0 |
| `G18` (S3, Disp.) | `=$J$8-SUM(C18:F18)` | $2400-(-1045)$ | 3445 |
| `D20` (S2, WC2) | 2225 (valor fijo copiado) | — | 2225 |
| `F20` (S2, Mov.) | 175 (valor fijo copiado) | — | 175 |
| `G20` (S2, Disp.) | `=$J$8-(SUM(C20:F20))` | $2400-2400$ | 0 |
| `C22` (S1, WC1) | `=I13+(J13*300)` | $90+5\times300$ | 1590 |
| `F22` (S1, Mov.) | `=480+F20` | $480+175$ | 655 |
| `G22` (S1, Disp.) | `=J16-(SUM(C22:F22))` | `J16` vacía: $0-(1590+655)$ | −2245 |

#### Resultados: Excel frente a la solución de la L15 (p. 42)

| Lote | Semana | Concepto | Excel | L15 p. 42 | ¿Coincide? |
|---|---|---|---|---|---|
| 300γ | 2 | WC2 / WC4 / Mov. / Disp. | 1290 / 630 / 480 / 0 | 1290 / 630 / 480 / 0 | Sí |
| 300γ | 1 | WC1 / WC2 / Mov. / Disp. | 1020 / 300 / 480 / 600 | 1020 / 300 / 480 / 600 | Sí |
| 575γ | 3 | WC2 / WC4 / Mov. / Disp. | 740 / 1180 / 480 / 0 | 740 / 1180 / 480 / 0 | Sí |
| 575γ | 2 | WC2 / Mov. / Disp. | 2225 / 175 / 0 | 2225 / 175 / 0 | Sí |
| 575γ | 1 | WC1 / Mov. / Disp. | 1020 / 655 / 725 | 1845 / 305 / 250 | **No** |
| 2000β | 3 | WC2 / WC4 / Mov. / Disp. | −1045 / 0 / 0 / 3445 | — / — / — / 2400 (β no tiene carga en S3) | **No** |
| 2000β | 2 | WC2 / WC4 / Mov. / Disp. | 2225 / — / 175 / 0 | 1490 / 430 / 480 / 0 | **No** (solo Disp.) |
| 2000β | 1 | WC1 / WC2 / Mov. / Disp. | 1590 / — / 655 / −2245 | — / 2230 / — / 170 | **No** |

Valores correctos del lote 2000β según la L15, con ruta WC2 → WC4 y sin WC1:

- WC4: $30+2000\times0.2=430$.
- WC2: $120+2000\times1.8=3720$, repartido en $1490$ (semana 2) y $2230$ (semana 1).
- Movimiento: 480 en la semana 2.
- Disponible en la semana 1: $2400-2230=170$.

Con los valores correctos, la carga en horas es: WC1 S1 = 47.75 h; WC2 S1 = 42.17 h, S2 = 83.42 h, S3 = 12.33 h; WC4 S2 = 17.67 h, S3 = 19.67 h. Ver el gráfico de la L15, p. 43.

#### Gráficos

No hay gráficos ni imágenes en el libro. El gráfico de carga por estación está en la L15, p. 43.

#### Conclusión

El bloque del lote 300γ y las semanas 3 y 2 del lote 575γ reproducen exactamente la solución de clase. La semana 1 del lote 575γ y todo el lote 2000β están incompletos o mal copiados. Para estudiar, use las tablas de la L15 (pp. 35-42), que tienen el resultado correcto.

### Observaciones

- **Errores de fórmula:**
  - `C14` usa el lote 300 en lugar de 575: debería ser `=I5+(J5*575)` = 1845.
  - `F14` suma en lugar de restar: debería ser `=480-F12` = 305. Entonces `G14` daría 250.
- **Bloque 2000β sin terminar:** copia del bloque 575γ con referencias desplazadas (`K13`, `L13`, `M13`, `N13`, `J15`, `J16`), que dan valores negativos (−1045, −2245) y un disponible de 3445 > 2400. No usa los parámetros de β (SU 120 / MACH 1.8 en WC2; SU 30 / MACH 0.2 en WC4), que no están en la hoja. Además pone carga en WC1, centro por el que β no pasa.
- **Valores fijos:** 300 (`D6`), 2225 (`D12`, `D20`) y 175 (`F12`, `F20`) están escritos a mano, no calculados, y las cantidades de los lotes van dentro de las fórmulas.
- La segunda tabla de parámetros (`I10:L13`) repite los datos de WC2 y WC4 de γ, no los de β. Probablemente se quiso poner ahí β (deducido).
- La cabecera del gemelo dice «Corte 3» por la carpeta original; el tema es MRP II / CRP de la L15 (Corte 2).

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `Hoja1` — 22 filas × 14 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M | N |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 |  | Lote 300γ |  |  |  |  |  |  | γ |  |  |  |  |  |
| 3 |  | Semana 2 | WC 1 | WC 2 | WC 4 | Movimiento | Disponible |  | WC1 |  | WC2 |  | WC4 |  |
| 4 |  | Lote 300γ |  | 1290 | 630 | 480 | 0 |  | SU-time | MACH-time | SU-time | MACH-time | SU-time | MACH-time |
| 5 |  | Semana 1 | WC 1 | WC 2 | WC 4 | Movimiento | Disponible |  | 120 | 3 | 90 | 5 | 30 | 2 |
| 6 |  | Lote 300γ | 1020 | 300 |  | 480 | 600 |  |  |  |  |  |  |  |
| 7 |  |  |  |  |  |  |  |  | Movimientos | 480 |  |  |  |  |
| 8 |  | Lote 575γ |  |  |  |  |  |  | min/semana | 2400 |  |  |  |  |
| 9 |  | Semana 3 | WC 1 | WC 2 | WC 4 | Movimiento | Disponible |  |  |  |  |  |  |  |
| 10 |  | Lote 575γ |  | 740 | 1180 | 480 | 0 |  |  |  |  |  |  |  |
| 11 |  | Semana 2 | WC 1 | WC 2 | WC 4 | Movimiento | Disponible |  | WC2 |  | WC4 |  |  |  |
| 12 |  | Lote 575γ |  | 2225 |  | 175 | 0 |  | SU-time | MACH-time | SU-time | MACH-time |  |  |
| 13 |  | Semana 1 | WC 1 | WC 2 | WC 4 | Movimiento | Disponible |  | 90 | 5 | 30 | 2 |  |  |
| 14 |  | Lote 575γ | 1020 |  |  | 655 | 725 |  |  |  |  |  |  |  |
| 16 |  | Lote 2000β |  |  |  |  |  |  |  |  |  |  |  |  |
| 17 |  | Semana 3 | WC 1 | WC 2 | WC 4 | Movimiento | Disponible |  |  |  |  |  |  |  |
| 18 |  | Lote 2000β |  | -1045 | 0 | 0 | 3445 |  |  |  |  |  |  |  |
| 19 |  | Semana 2 | WC 1 | WC 2 | WC 4 | Movimiento | Disponible |  |  |  |  |  |  |  |
| 20 |  | Lote 2000β |  | 2225 |  | 175 | 0 |  |  |  |  |  |  |  |
| 21 |  | Semana 1 | WC 1 | WC 2 | WC 4 | Movimiento | Disponible |  |  |  |  |  |  |  |
| 22 |  | Lote 2000β | 1590 |  |  | 655 | -2245 |  |  |  |  |  |  |  |

**Fórmulas (8 patrones distintos):**

- `D4`: `=K5+(L5*300)-300`
- `E4`: `=M5+(N5*300)`
- `F4`: `=J7`
- `G4`: `=J8-(SUM(C4:F4))`
- `C6`: `=I5+(J5*300)`
- `G10`: `=$J$8-SUM(C10:F10)`
- `G12`: `=$J$8-(SUM(C12:F12))`
- `F14`: `=480+F12`

