# ejemplo-1-programacion-produccion

> **Archivo:** [`ejemplo-1-programacion-produccion.xlsx`](./ejemplo-1-programacion-produccion.xlsx) · **Corte 3** · Libro de Excel con 1 hoja(s): `Hoja1`  
> **Nombre original:** `CORTE 3/Ejemplo 1 Programación de Producción .xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Ejemplo introductorio de **programación de una máquina con tiempos de liberación** ($1|r_j|\cdot$), con actividades de la vida diaria. La "máquina" es la persona que hace las tareas. Usa los parámetros de [L16](../01-introduccion-scheduling/L16-intro-scheduling.md) ($r_j$, $d_j$, $p_j$, $w_j$, setup $s_j$) y los indicadores $C_j$, $C_j-r_j$ y $w_jC_j$ de [L17](./L17-single-machine-scheduling.md). Sirve para ver que un trabajo no puede empezar antes de su $r_j$ y cómo se calcula el tiempo de flujo.

Es **idéntico** al bloque de las filas 3-8 de la hoja `Reglas de Despacho` de [programacion-produccion-una-maquina](./programacion-produccion-una-maquina.md): mismos valores y mismas fórmulas.

### Hoja `Hoja1`

**Objetivo (deducido):** secuenciar 4 actividades, con el tiempo en horas desde un instante 0, y calcular cuándo termina cada una, su tiempo de flujo y su costo ponderado.

**Datos de entrada** (columnas B-H, filas 4-7). La columna N es la **posición** en la secuencia; las filas no están en ese orden.

| N (posición) | Trabajo | $r_j$ (h) | $d_j$ (como está escrito) | $p_j$ | $w_j$ | $s_j$ (setup) |
|---|---|---|---|---|---|---|
| 2 | Proyecto | 24 | "24 h + 30 días" (texto) | 10 h | 5 | 3 h |
| 4 | Seminario | 0 | 19-oct (celda con fecha, formato d-mmm) | 2 h | 2 | 0 h |
| 1 | Pago Factura | 50 | 19-oct (celda con fecha, formato d-mmm) | 20 min | 3 | 30 min |
| 3 | Entrevista de Trabajo | 100 | "100 h + 2 h" (texto) | 1 h | 4 | 0 h |

$p_j$, $s_j$ y casi todos los $d_j$ son texto, así que no entran en fórmulas; los $C_j$ se escribieron con números a mano.

**Método (fórmulas traducidas):**

- Pago Factura (posición 1): `I6 = 50+0.33`, es decir $C=r_j+p_j=50+0.33$ (nota J6: "20 min = 0,33 h").
- Proyecto (posición 2): `I4 = I6+10`, es decir $C=C_{\text{anterior}}+p_j$ (ya pasó su $r=24$).
- Entrevista (posición 3): `I7 = 100+1`. Nota J7: "si r_j es > c_j del anterior, inicia en r_j", o sea $\text{inicio}_j=\max(r_j,\ C_{\text{anterior}})$.
- Seminario (posición 4): `I5 = I7+2`.
- `K = I − D`: tiempo de flujo $F_j=C_j-r_j$. `L = G·I`: $w_jC_j$.
- `K8 = AVERAGE(K4:K7)` = flujo promedio $\bar F$. `L8 = AVERAGE(L4:L7)` = promedio de $w_jC_j$.

**Resultados (programa en orden de ejecución):**

| Posición | Trabajo | $r_j$ | Inicio | Fin = $C_j$ | $C_j-r_j$ | $w_jC_j$ |
|---|---|---|---|---|---|---|
| 1 | Pago Factura | 50 | 50 | 50.33 | 0.33 | 150.99 |
| 2 | Proyecto | 24 | 50.33 | 60.33 | 36.33 | 301.65 |
| — | (ocioso) | | 60.33 | 100 | | |
| 3 | Entrevista de Trabajo | 100 | 100 | 101 | 1 | 404 |
| 4 | Seminario | 0 | 101 | 103 | 103 | 206 |
| | **"Tiempo de Flujo"** (promedios) | | | | **35.165** | **265.66** |

Cálculo propio: $\sum w_jC_j=1062.64$ y $C_{max}=103$ h. La Entrevista ($d$ = "100 h + 2 h" = 102 h, interpretación) termina en 101, a tiempo.

**Gráficos:** no hay.

**Conclusión:** el ejemplo muestra cómo las liberaciones fuerzan esperas: la Entrevista no puede empezar antes de $t=100$, y el orden elegido deja al Seminario de último con un flujo de 103 h.

### Observaciones

- **Duplicado:** es igual al bloque A de la hoja `Reglas de Despacho` de [programacion-produccion-una-maquina](./programacion-produccion-una-maquina.md).
- Los tiempos de alistamiento $s_j$ (3 h para Proyecto y 30 min para Pago Factura) no se suman en ningún $C_j$.
- Las fechas de entrega mezclan texto ("24 h + 30 días", "100 h + 2 h") y fechas de calendario (19-oct), así que no se calculan $L_j$ ni $T_j$.
- La secuencia no es un programa sin retrasos (*non-delay*): de 0 a 50 no se hace nada aunque el Seminario ($r=0$) y el Proyecto ($r=24$) ya están disponibles. Programar el Seminario en $[0,2]$ y el Proyecto en $[24,34]$ bajaría el flujo (deducido).
- La fila 8 dice "Tiempo de Flujo", pero L8 es un promedio de $w_jC_j$, no un tiempo de flujo.

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `Hoja1` — 8 filas × 12 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K | L |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 |  | N | Trabajo | r_j | d_j | p_j | w_j | s_j | c_j |  | c_j - r_j | w_j * c_j |
| 4 |  | 2 | Proyecto | 24 | 24 h + 30 días | 10 h | 5 | 3 h | 60.33 |  | 36.33 | 301.65 |
| 5 |  | 4 | Seminario | 0 | 2026-10-19 | 2 h | 2 | 0 h | 103 |  | 103 | 206 |
| 6 |  | 1 | Pago Factura | 50 | 2026-10-19 | 20 min | 3 | 30 min | 50.33 | 20 min = 0,33 h | 0.33 | 150.99 |
| 7 |  | 3 | Entrevista de Trabajo | 100 | 100 h + 2 h | 1 h | 4 | 0 h | 101 | si r_j es > c_j del anterior, inicia en r_j | 1 | 404 |
| 8 |  |  |  |  |  |  |  |  |  | Tiempo de Flujo | 35.165 | 265.66 |

**Fórmulas (7 patrones distintos):**

- `I4`: `=I6+10`
- `K4`: `=I4-D4`
- `L4`: `=G4*I4`
- `I6`: `=50+0.33`
- `I7`: `=100+1`
- `K8`: `=AVERAGE(K4:K7)`
- `L8`: `=AVERAGE(L4:L7)`

