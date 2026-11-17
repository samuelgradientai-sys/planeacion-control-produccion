# practica-metodos-pronostico-parcial-1

> **Archivo:** [`practica-metodos-pronostico-parcial-1.xlsx`](./practica-metodos-pronostico-parcial-1.xlsx) · **Corte 1** · Libro de Excel con 6 hoja(s): `MA SIMPLE`, `EJERCICIO DIAPO`, `MA PONDERADO`, `SE SIMPLE`, `SE DOBLE HOLT`, `SE TRIPLE WINTERS`  
> **Nombre original:** `CORTE 1/PARICAL 1.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Libro de práctica preparado antes del primer parcial (nombre original `CORTE 1/PARICAL 1.xlsx`). Repasa en Excel los métodos de la [Lección 5 — Forecasting stationary data and errors](./L05-forecasting-stationary-data-and-errors.md): promedio móvil simple con sus medidas de error (MAD, SSE, MSE, MAPE), el ejercicio de la diapositiva 30 (¿MA de 3 o de 5?), promedio móvil ponderado y suavización exponencial simple. Tiene además dos hojas reservadas para Holt y Winters que quedaron **vacías**. Varias hojas tienen errores de fórmula (ver cada hoja y Observaciones).

**Advertencia general:** las demandas de `MA SIMPLE`, `MA PONDERADO` y `SE SIMPLE` se generan con `=RANDBETWEEN(480,600)`, que cambia cada vez que Excel recalcula. Los números de abajo son los que quedaron guardados en el archivo; al abrirlo se verán otros.

### Hoja `MA SIMPLE` — promedio móvil simple con n = 3

**Objetivo (deducido):** pronosticar con un promedio móvil de 3 periodos, calcular el pronóstico del periodo 22 y medir el error, como en el ejemplo de la p. 6 de la L05 pero con datos aleatorios.

**Datos de entrada** (periodos en `B2:B13`, demanda `D()` en `C2:C13`, generada con `RANDBETWEEN(480,600)`):

| Periodo | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Demanda | 504 | 598 | 553 | 531 | 540 | 569 | 587 | 505 | 570 | 583 | 537 | 540 |

**Parámetros:** $n=3$ (`B1` «n=3» y `C15`).

**Método (tal como está en la hoja)**

- `F()` (columna D, filas 5–13): `D5 = AVERAGE(C3:C5)`, … , `D13 = AVERAGE(C11:C13)`; es decir, en la fila del periodo $t$ se pone $\frac{1}{3}(D_{t-2}+D_{t-1}+D_t)$, que incluye la demanda del propio periodo.
- `MAD` (columna E): `=ABS(C5-D5)` → $|D_t-F|$; `SSE` (columna F): `=E5^2`; `MAPE` (columna G): `=E5/C5` → $|e|/D_t$.
- `F22` (`C16`): `=AVERAGE(C11:C13)` $=\frac{583+537+540}{3}=553{,}333$ (promedio de los periodos 19, 20 y 21).
- Resumen: MAD `E18 = AVERAGE(E5:E13)`; SSE `E19 = SUM(F5:F13)`; MSE `E20 = AVERAGE(F5:F13)`; MAPE `E21 = AVERAGE(G5:G13)`.

**Resultados guardados**

| Periodo | D() | F() | Error abs. | Error² | Error % |
|---|---|---|---|---|---|
| 13 | 531 | 560,667 | 29,667 | 880,111 | 5,59 % |
| 14 | 540 | 541,333 | 1,333 | 1,778 | 0,25 % |
| 15 | 569 | 546,667 | 22,333 | 498,778 | 3,93 % |
| 16 | 587 | 565,333 | 21,667 | 469,444 | 3,69 % |
| 17 | 505 | 553,667 | 48,667 | 2.368,44 | 9,64 % |
| 18 | 570 | 554,000 | 16,000 | 256,000 | 2,81 % |
| 19 | 583 | 552,667 | 30,333 | 920,111 | 5,20 % |
| 20 | 537 | 563,333 | 26,333 | 693,444 | 4,90 % |
| 21 | 540 | 553,333 | 13,333 | 177,778 | 2,47 % |

| F22 | MAD | SSE | MSE | MAPE |
|---|---|---|---|---|
| 553,333 | 23,2963 | 6.265,89 | 696,21 | 0,0427443 (4,27 %) |

**Error de alineación:** cada valor de `F()` está una fila más arriba de donde debería; el número de la fila del periodo $t$ es en realidad el pronóstico del periodo $t+1$ (por ejemplo, 560,667 es $F_{14}=\frac{598+553+531}{3}$, no $F_{13}$). Al compararlo con $D_t$, la demanda que se quiere pronosticar entra en su propio pronóstico y el error sale menor. Con la alineación correcta, $F_t=\frac{D_{t-1}+D_{t-2}+D_{t-3}}{3}$ (cálculo propio con los mismos datos):

| Periodo | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |
|---|---|---|---|---|---|---|---|---|---|---|
| $F_t$ correcto | 551,67 | 560,67 | 541,33 | 546,67 | 565,33 | 553,67 | 554,00 | 552,67 | 563,33 | 553,33 |

MAD = 28,22; SSE = 8.784,22; MSE = 976,02; MAPE = 5,16 %. El pronóstico $F_{22}=553{,}33$ de la hoja sí es correcto.

### Hoja `EJERCICIO DIAPO` — ejercicio de la diapositiva 30

**Enunciado** (imagen pegada en la hoja, igual a la p. 30 de la L05): «Exercise — For the next set of data, and their forecasts, say which method is best.»

> [Imagen: captura de la diapositiva «Exercise» con la tabla Data / MA n = 3 / MA n = 5 que se transcribe abajo.]

**Datos y método:** demandas en `B3:B12` (y repetidas en `B15:B24`); pronósticos copiados de la diapositiva como valores (`C6:C12` para MA n = 3 y `C20:C24` para MA n = 5). Error absoluto `D = ABS(B−C)`, error al cuadrado `E = D^2`, error relativo `F = D/B`. Resumen: MAD = promedio de D; SSE = suma de E; MSE = promedio de E; MAPE = promedio de F.

| Dato | MA n = 3 | Error abs. | Error² | Error % | MA n = 5 | Error abs. | Error² | Error % |
|---|---|---|---|---|---|---|---|---|
| 13,9 | | | | | | | | |
| 13,4 | | | | | | | | |
| 16,4 | | | | | | | | |
| 14,1 | 14,6 | 0,5 | 0,25 | 3,55 % | | | | |
| 8,8 | 14,6 | 5,8 | 33,64 | 65,91 % | | | | |
| 15,8 | 13,1 | 2,7 | 7,29 | 17,09 % | 13,3 | 2,5 | 6,25 | 15,82 % |
| 15,2 | 12,9 | 2,3 | 5,29 | 15,13 % | 13,7 | 1,5 | 2,25 | 9,87 % |
| 15,2 | 13,3 | 1,9 | 3,61 | 12,50 % | 14,1 | 1,1 | 1,21 | 7,24 % |
| 13,9 | 15,4 | 1,5 | 2,25 | 10,79 % | 13,8 | 0,1 | 0,01 | 0,72 % |
| 17,3 | 14,7 | 2,6 | 6,76 | 15,03 % | 13,8 | 3,5 | 12,25 | 20,23 % |

| Medida | MA n = 3 (`I3:I6`) | MA n = 5 (`I15:I18`) |
|---|---|---|
| MAD | 2,47143 | **1,74** |
| SSE | 59,09 | **21,97** |
| MSE | 8,44143 | **4,394** |
| MAPE | 0,199994 (20,0 %) | **0,107757 (10,8 %)** |

**Conclusión:** el promedio móvil de 5 periodos es mejor en las cuatro medidas. Comprobación propia: si se compara solo en los 5 periodos que ambos pronostican (sin el atípico 8,8), MA n = 3 da MAD 2,2, SSE 25,2, MSE 5,04 y MAPE 14,1 %, y MA n = 5 sigue siendo mejor.

### Hoja `MA PONDERADO` — promedio móvil ponderado

**Objetivo (deducido):** pronosticar el periodo 22 con $n=3$ y pesos $w_0=0{,}75$, $w_1=0{,}15$, $w_2=0{,}1$, como en el ejemplo de la p. 11 de la L05.

**Datos de entrada** (`C2:C13`, `RANDBETWEEN(480,600)`):

| Periodo | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Demanda | 545 | 585 | 506 | 533 | 544 | 529 | 487 | 501 | 529 | 590 | 522 | 525 |

**Parámetros:** `W0` = 0,75 (`C16`), `W2` = 0,15 (`C17`), `W3` = 0,1 (`C18`), `n=` 3 (`C20`).

**Método:** `F22` (`C21`) `=(((C13*C16)+(C17*C12)+(C18*C11))/C20)`, es decir
$$F_{22}=\frac{w_0D_{21}+w_1D_{20}+w_2D_{19}}{n}=\frac{0{,}75(525)+0{,}15(522)+0{,}1(590)}{3}=\frac{531{,}05}{3}=177{,}017.$$

**Resultado guardado:** F22 = 177,017.

**Error:** como los pesos ya suman 1, no se debe dividir entre $n$. El pronóstico correcto es $F_{22}=531{,}05$. Además, los rótulos `W2` y `W3` corresponden a $w_1$ y $w_2$, y la hoja solo calcula un pronóstico (no hay errores ni serie de pronósticos).

### Hoja `SE SIMPLE` — suavización exponencial simple

**Objetivo (deducido):** aplicar la suavización exponencial simple con pronóstico inicial 540, como en el ejemplo de la p. 16 de la L05.

**Datos de entrada** (`C2:C13`, `RANDBETWEEN(480,600)`):

| Periodo | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Demanda | 533 | 545 | 537 | 514 | 552 | 592 | 524 | 492 | 550 | 549 | 480 | 537 |

**Parámetros:** pronóstico inicial 540 (`D1`); `ALFA` = 0,95 (`C17`); `ALFA-1` = `=1-C17` = 0,05 (`C18`), que es $1-\alpha$.

**Método:** `F10` (`C19`) `=(C17*C2)+(C18*D1)`, es decir
$$F=\alpha D_{10}+(1-\alpha)F_{10}=0{,}95(533)+0{,}05(540)=533{,}35.$$

**Resultado guardado:** 533,35 (rotulado «F10»).

**Observaciones de la hoja:** solo se calcula un paso (falta continuar hasta $F_{22}$); con la convención de la L05 ($F_t=\alpha D_{t-1}+(1-\alpha)F_{t-1}$) el valor calculado es el pronóstico del periodo 11, no el del 10; y el ejemplo de la diapositiva usa $\alpha=0{,}05$, mientras que aquí el peso 0,95 se aplica al dato (α efectivo = 0,95), es decir, los pesos están invertidos respecto al ejemplo.

### Hojas `SE DOBLE HOLT` y `SE TRIPLE WINTERS`

Vacías. Estaban reservadas para la suavización doble de Holt (tema [05](../05-tendencia-suavizacion-doble-holt/)) y el método de Winters (tema [06](../06-estacionalidad-winters-y-tracking-signal/)).

### Observaciones

- Datos aleatorios (`RANDBETWEEN`) en tres hojas: los valores cambian al recalcular; no son los datos de las diapositivas (482, 474, 523, …).
- `MA SIMPLE`: pronósticos desalineados una fila (el error sale subestimado: MAD 23,30 en vez de 28,22).
- `MA PONDERADO`: división entre $n$ sobrante (177,017 en vez de 531,05) y rótulos de pesos `W0`, `W2`, `W3`.
- `SE SIMPLE`: un solo paso, rótulo «F10» y α = 0,95 en lugar de 0,05.
- `EJERCICIO DIAPO`: `I16 = SUM(E19:E24)` incluye la celda vacía `E19`, sin efecto. El último pronóstico MA n = 3 de la diapositiva (14,7) es en rigor 14,77 ≈ 14,8.
- Las hojas de Holt y Winters están vacías.
- Por su contenido (MA, WMA y SES), el archivo encaja en esta carpeta; las hojas vacías de Holt y Winters pertenecen a los temas 05 y 06.

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `MA SIMPLE` — 21 filas × 7 columnas

| Fila | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| 1 |  | n=3 | D() | F() | MAD | SSE | MAPE |
| 2 |  | 10 | 504 |  |  |  |  |
| 3 |  | 11 | 598 |  |  |  |  |
| 4 |  | 12 | 553 |  |  |  |  |
| 5 |  | 13 | 531 | 560.667 | 29.6667 | 880.111 | 0.0558694 |
| 6 |  | 14 | 540 | 541.333 | 1.33333 | 1.77778 | 0.00246914 |
| 7 |  | 15 | 569 | 546.667 | 22.3333 | 498.778 | 0.0392501 |
| 8 |  | 16 | 587 | 565.333 | 21.6667 | 469.444 | 0.0369108 |
| 9 |  | 17 | 505 | 553.667 | 48.6667 | 2368.44 | 0.0963696 |
| 10 |  | 18 | 570 | 554 | 16 | 256 | 0.0280702 |
| 11 |  | 19 | 583 | 552.667 | 30.3333 | 920.111 | 0.0520297 |
| 12 |  | 20 | 537 | 563.333 | 26.3333 | 693.444 | 0.0490379 |
| 13 |  | 21 | 540 | 553.333 | 13.3333 | 177.778 | 0.0246914 |
| 15 |  | n= | 3 |  |  |  |  |
| 16 |  | F22 | 553.333 |  |  |  |  |
| 18 |  |  |  | MAD | 23.2963 |  |  |
| 19 |  |  |  | SSE | 6265.89 |  |  |
| 20 |  |  |  | MSE | 696.21 |  |  |
| 21 |  |  |  | MAPE | 0.0427443 |  |  |

**Fórmulas (9 patrones distintos):**

- `C2`: `=RANDBETWEEN(480,600)`
- `D5`: `=AVERAGE(C3:C5)`
- `E5`: `=ABS(C5-D5)`
- `F5`: `=E5^2`
- `G5`: `=E5/C5`
- `E18`: `=AVERAGE(E5:E13)`
- `E19`: `=SUM(F5:F13)`
- `E20`: `=AVERAGE(F5:F13)`
- `E21`: `=AVERAGE(G5:G13)`

### Hoja `EJERCICIO DIAPO` — 24 filas × 9 columnas · 1 imagen(es)

| Fila | A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|---|
| 2 |  | Data | MA n = 3 | MAD | SSE | MAPE |  |  |  |
| 3 |  | 13.9 |  |  |  |  |  | MAD | 2.47143 |
| 4 |  | 13.4 |  |  |  |  |  | SSE | 59.09 |
| 5 |  | 16.4 |  |  |  |  |  | MSE | 8.44143 |
| 6 |  | 14.1 | 14.6 | 0.5 | 0.25 | 0.035461 |  | MAPE | 0.199994 |
| 7 |  | 8.8 | 14.6 | 5.8 | 33.64 | 0.659091 |  |  |  |
| 8 |  | 15.8 | 13.1 | 2.7 | 7.29 | 0.170886 |  |  |  |
| 9 |  | 15.2 | 12.9 | 2.3 | 5.29 | 0.151316 |  |  |  |
| 10 |  | 15.2 | 13.3 | 1.9 | 3.61 | 0.125 |  |  |  |
| 11 |  | 13.9 | 15.4 | 1.5 | 2.25 | 0.107914 |  |  |  |
| 12 |  | 17.3 | 14.7 | 2.6 | 6.76 | 0.150289 |  |  |  |
| 14 |  | Data | MA n = 5 | MAD | SSE | MAPE |  |  |  |
| 15 |  | 13.9 |  |  |  |  |  | MAD | 1.74 |
| 16 |  | 13.4 |  |  |  |  |  | SSE | 21.97 |
| 17 |  | 16.4 |  |  |  |  |  | MSE | 4.394 |
| 18 |  | 14.1 |  |  |  |  |  | MAPE | 0.107757 |
| 19 |  | 8.8 |  |  |  |  |  |  |  |
| 20 |  | 15.8 | 13.3 | 2.5 | 6.25 | 0.158228 |  |  |  |
| 21 |  | 15.2 | 13.7 | 1.5 | 2.25 | 0.0986842 |  |  |  |
| 22 |  | 15.2 | 14.1 | 1.1 | 1.21 | 0.0723684 |  |  |  |
| 23 |  | 13.9 | 13.8 | 0.1 | 0.01 | 0.00719424 |  |  |  |
| 24 |  | 17.3 | 13.8 | 3.5 | 12.25 | 0.202312 |  |  |  |

**Fórmulas (7 patrones distintos):**

- `I3`: `=AVERAGE(D6:D12)`
- `I4`: `=SUM(E6:E12)`
- `I5`: `=AVERAGE(E6:E12)`
- `D6`: `=ABS(B6-C6)`
- `E6`: `=D6^ 2`
- `F6`: `=D6/B6`
- `I6`: `=AVERAGE(F6:F12)`

### Hoja `MA PONDERADO` — 21 filas × 3 columnas

| Fila | A | B | C |
|---|---|---|---|
| 2 |  | 10 | 545 |
| 3 |  | 11 | 585 |
| 4 |  | 12 | 506 |
| 5 |  | 13 | 533 |
| 6 |  | 14 | 544 |
| 7 |  | 15 | 529 |
| 8 |  | 16 | 487 |
| 9 |  | 17 | 501 |
| 10 |  | 18 | 529 |
| 11 |  | 19 | 590 |
| 12 |  | 20 | 522 |
| 13 |  | 21 | 525 |
| 16 |  | W0 | 0.75 |
| 17 |  | W2 | 0.15 |
| 18 |  | W3 | 0.1 |
| 20 |  | n= | 3 |
| 21 |  | F22 | 177.017 |

**Fórmulas (2 patrones distintos):**

- `C2`: `=RANDBETWEEN(480,600)`
- `C21`: `=(((C13*C16)+(C17*C12)+(C18*C11))/C20)`

### Hoja `SE SIMPLE` — 19 filas × 4 columnas

| Fila | A | B | C | D |
|---|---|---|---|---|
| 1 |  |  |  | 540 |
| 2 |  | 10 | 533 |  |
| 3 |  | 11 | 545 |  |
| 4 |  | 12 | 537 |  |
| 5 |  | 13 | 514 |  |
| 6 |  | 14 | 552 |  |
| 7 |  | 15 | 592 |  |
| 8 |  | 16 | 524 |  |
| 9 |  | 17 | 492 |  |
| 10 |  | 18 | 550 |  |
| 11 |  | 19 | 549 |  |
| 12 |  | 20 | 480 |  |
| 13 |  | 21 | 537 |  |
| 17 |  | ALFA | 0.95 |  |
| 18 |  | ALFA-1 | 0.05 |  |
| 19 |  | F10 | 533.35 |  |

**Fórmulas (3 patrones distintos):**

- `C2`: `=RANDBETWEEN(480,600)`
- `C18`: `=1-C17`
- `C19`: `=(C17*C2)+(C18*D1)`

### Hoja `SE DOBLE HOLT` — 1 filas × 1 columnas

_(hoja vacía)_

### Hoja `SE TRIPLE WINTERS` — 1 filas × 1 columnas

_(hoja vacía)_

