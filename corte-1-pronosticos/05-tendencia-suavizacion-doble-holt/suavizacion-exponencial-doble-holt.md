# suavizacion-exponencial-doble-holt

> **Archivo:** [`suavizacion-exponencial-doble-holt.xlsx`](./suavizacion-exponencial-doble-holt.xlsx) · **Corte 1** · Libro de Excel con 1 hoja(s): `Hoja1`  
> **Nombre original:** `CORTE 1/SUAVIZACION EXPONENCUAL DOBLE.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Libro de una sola hoja (`Hoja1`) que aplica la **suavización exponencial doble de Holt** a la demanda trimestral del ejemplo de la página 6 de [`L06-forecasting-data-with-trend.md`](./L06-forecasting-data-with-trend.md). Los valores iniciales $S_0$ y $G_0$ se obtienen por **regresión lineal**, el método 1 de la clase. Calcula el pronóstico a un periodo, el error de cada periodo, MAD y MAPE, y proyecta 4 periodos hacia adelante. Las constantes $\alpha$ y $\beta$ se calcularon con Solver (la configuración está guardada en el libro; ver **Observaciones**). Sirve para ver cómo se implementa Holt en Excel y cómo cambian los errores según $\alpha$ y $\beta$.

### Hoja `Hoja1`

**Objetivo (deducido del ejercicio de la p. 6 de L06):** pronosticar un periodo adelante la demanda de 8 trimestres con Holt, calcular el error y compararlo; además, proyectar los trimestres 9 a 12.

**Datos de entrada** (tabla de Excel `Tabla1`, rango B2:I15; los encabezados B2 y C2 quedaron con los nombres por defecto «Columna1» y «Columna2», y los rótulos reales «Periodo» y «Demanda» están en B3 y C3):

| Periodo (B) | Demanda (C) |
|---|---|
| 1 | 200 |
| 2 | 250 |
| 3 | 175 |
| 4 | 186 |
| 5 | 225 |
| 6 | 285 |
| 7 | 305 |
| 8 | 190 |

**Parámetros:**

| Parámetro | Celda | Valor |
|---|---|---|
| $\alpha$ (rotulado «Aplha») | L2 | 0,830999 (0,8309987851) |
| $\beta$ | L3 | 0,999 |
| $S_0$ (intercepto de la regresión) | D3 | 196,25 = `INTERCEPT(C4:C11,B4:B11)` |
| $G_0$ (pendiente de la regresión) | E3 | 6,83333 = `SLOPE(C4:C11,B4:B11)` |

**Método paso a paso** (fila $t+3$ = periodo $t$):

1. Inicialización por regresión de la demanda contra el periodo (1 a 8): $S_0=a=196{,}25$, $G_0=b=6{,}8333$.
2. Pronóstico a un periodo (columna F, `=D3+E3`, `=D4+E4`, …): $F_t=S_{t-1}+G_{t-1}$.
3. Nivel (columna D, `=$L$2*C4+(1-$L$2)*(D3+E3)`): $S_t=\alpha D_t+(1-\alpha)(S_{t-1}+G_{t-1})$, con $\alpha$ en L2.
4. Tendencia (columna E, `=$L$3*(D4-D3)+(1-$L$3)*E3`): $G_t=\beta(S_t-S_{t-1})+(1-\beta)G_{t-1}$, con $\beta$ en L3.
5. Error absoluto (columna G, rotulada «MAD»): $|F_t-D_t|$.
6. Residual (columna H): $e_t=F_t-D_t$ (pronóstico menos real).
7. Error relativo (columna I): $|F_t-D_t|/D_t$.
8. Proyección desde el último dato (F12:F15): $F_{8+\tau}=S_8+\tau G_8$ con $\tau=1,2,3,4$ (`=D11+E11`, `=$D$11+2*$E$11`, `=$D$11+3*$E$11`, `=$D$11+4*$E$11`).
9. Indicadores: $MAD=\frac{1}{8}\sum|F_t-D_t|$ (G20) y $MAPE=\frac{1}{8}\sum\frac{|F_t-D_t|}{D_t}$ (I20).

**Resultados:**

| t | $D_t$ | $S_t$ | $G_t$ | $F_t$ | $\|F_t-D_t\|$ | $F_t-D_t$ | Error relativo |
|---|---|---|---|---|---|---|---|
| 0 | | 196,250 | 6,833 | | | | |
| 1 | 200 | 200,521 | 4,274 | 203,083 | 3,083 | 3,083 | 0,0154 |
| 2 | 250 | 242,360 | 41,802 | 204,795 | 45,205 | −45,205 | 0,1808 |
| 3 | 175 | 193,448 | −48,821 | 284,162 | 109,162 | 109,162 | 0,6238 |
| 4 | 186 | 179,008 | −14,475 | 144,627 | 41,373 | −41,373 | 0,2224 |
| 5 | 225 | 214,781 | 35,723 | 164,533 | 60,467 | −60,467 | 0,2687 |
| 6 | 285 | 279,170 | 64,360 | 250,504 | 34,496 | −34,496 | 0,1210 |
| 7 | 305 | 311,512 | 32,374 | 343,531 | 38,531 | 38,531 | 0,1263 |
| 8 | 190 | 216,007 | −95,377 | 343,885 | 153,885 | 153,885 | 0,8099 |
| 9 | | | | 120,630 | | | |
| 10 | | | | 25,253 | | | |
| 11 | | | | −70,124 | | | |
| 12 | | | | −165,501 | | | |

- **MAD = 60,7752** (G20)
- **MAPE = 0,296061 = 29,6 %** (I20)

**Gráficos:** dos gráficos de líneas sin título, superpuestos en la misma posición (M2:S15).
- Gráfico 1: demanda (C4:C11, 8 puntos) y pronóstico $F_t$ (F4:F15, 12 puntos, incluida la proyección 9–12).
- Gráfico 2: demanda (C4:C11) y pronóstico F4:F12 (9 puntos).

Con $\beta=0{,}999$, la pendiente salta de un periodo a otro (+41,8; −48,8; +64,4; −95,4) y el pronóstico oscila con fuerza.

**Conclusión del ejemplo:** con estas constantes el pronóstico es muy inestable. Con $\beta\approx1$ la tendencia se vuelve la última diferencia de niveles, y como el último trimestre cayó (305 → 190), la proyección se desploma hasta valores **negativos** en los periodos 11 y 12 (−70 y −166), lo cual no tiene sentido para una demanda. La serie (200 a 305 con caídas) no tiene una tendencia lineal limpia; la regresión da una pendiente de solo 6,8 por trimestre.

### Observaciones

- **Solver configurado para maximizar.** El libro guarda un modelo de Solver con estos datos: objetivo `G20` (MAD), tipo `solver_typ = 1` (**maximizar**), celdas variables L2 y L3, motor evolutivo (`solver_eng = 3`), restricciones $0{,}01\le\alpha,\beta\le0{,}999$ y una restricción trivial L2 ≥ L2. Los valores guardados ($\alpha=0{,}831$, $\beta=0{,}999$) son justamente los que **maximizan** el MAD.
  - Cálculo propio: con $\beta=0{,}999$ fijo, el MAD máximo sobre $\alpha$ es 60,775 en $\alpha=0{,}831$, el mismo valor del libro.
  - Si se minimiza, como se pretendía, la búsqueda en malla da el MAD más bajo en la cota inferior, $\alpha=\beta=0{,}01$, con MAD ≈ 37,32. Con $\alpha=\beta=0{,}1$, los parámetros de la clase, el MAD es ≈ 38,58 con estos mismos $S_0$ y $G_0$.
  - Para corregirlo hay que cambiar Solver a «Mín».
- **Diferencias con el enunciado de la p. 6 de L06.** El ejercicio dice $\alpha=\beta=0{,}1$, $S_0=200$ y $G_0=10$, y el Excel usa la regresión ($S_0=196{,}25$, $G_0=6{,}83$) y los parámetros del Solver.
  - Cálculo propio con los datos del enunciado: pronósticos $F_1\ldots F_8$ = 210,0; 218,9; 232,2; 236,1; 240,3; 247,7; 260,8; 275,0, con MAD ≈ 41,28 y pronóstico del periodo 9 ≈ 275,5.
- **Nombres de columnas.** La columna G se rotula «MAD», pero contiene el error absoluto de cada periodo; el MAD propiamente dicho está en G20. Error de tipeo: «Aplha» en K2.
- **Signo del error.** El residual se define como $F_t-D_t$ (pronóstico menos real), como en los ejemplos de la p. 11 y la p. 15 de L06. En la señal de rastreo de L07 se usa real menos pronóstico.
- **Inicialización con los mismos datos.** $S_0$ y $G_0$ se calculan con los mismos 8 datos que luego se pronostican; la clase recomienda reservar periodos base para inicializar.

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `Hoja1` — 20 filas × 12 columnas · 2 gráfico(s)

**Gráficos en esta hoja:**

- Gráfico de líneas — título «(sin título)»
  - Series: (serie): y = `Hoja1!$C$4:$C$11`; (serie): y = `Hoja1!$F$4:$F$15`
- Gráfico de líneas — título «(sin título)»
  - Series: (serie): y = `Hoja1!$C$4:$C$11`; (serie): y = `Hoja1!$F$4:$F$12`

| Fila | A | B | C | D | E | F | G | H | I | J | K | L |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 |  | Columna1 | Columna2 | S(t) | G(t) | F(t) | MAD | RESIDUALES | ERROR RELATIVO |  | Aplha | 0.830999 |
| 3 |  | Periodo | Demanda | 196.25 | 6.83333 |  |  |  |  |  | Beta | 0.999 |
| 4 |  | 1 | 200 | 200.521 | 4.27365 | 203.083 | 3.08333 | 3.08333 | 0.0154167 |  |  |  |
| 5 |  | 2 | 250 | 242.36 | 41.8016 | 204.795 | 45.2053 | -45.2053 | 0.180821 |  |  |  |
| 6 |  | 3 | 175 | 193.448 | -48.8211 | 284.162 | 109.162 | 109.162 | 0.623782 |  |  |  |
| 7 |  | 4 | 186 | 179.008 | -14.4749 | 144.627 | 41.3726 | -41.3726 | 0.222433 |  |  |  |
| 8 |  | 5 | 225 | 214.781 | 35.7228 | 164.533 | 60.4669 | -60.4669 | 0.268742 |  |  |  |
| 9 |  | 6 | 285 | 279.17 | 64.3604 | 250.504 | 34.4962 | -34.4962 | 0.121039 |  |  |  |
| 10 |  | 7 | 305 | 311.512 | 32.3736 | 343.531 | 38.5305 | 38.5305 | 0.12633 |  |  |  |
| 11 |  | 8 | 190 | 216.007 | -95.377 | 343.885 | 153.885 | 153.885 | 0.809923 |  |  |  |
| 12 |  | 9 |  |  |  | 120.63 |  |  |  |  |  |  |
| 13 |  | 10 |  |  |  | 25.2528 |  |  |  |  |  |  |
| 14 |  | 11 |  |  |  | -70.1242 |  |  |  |  |  |  |
| 15 |  | 12 |  |  |  | -165.501 |  |  |  |  |  |  |
| 19 |  |  |  |  |  |  | MAD |  | MAPE |  |  |  |
| 20 |  |  |  |  |  |  | 60.7752 |  | 0.296061 |  |  |  |

**Fórmulas (12 patrones distintos):**

- `D3`: `=INTERCEPT(C4:C11,B4:B11)`
- `E3`: `=SLOPE(C4:C11,B4:B11)`
- `D4`: `=$L$2*C4+(1-$L$2)*(D3+E3)`
- `E4`: `=$L$3*(D4-D3)+(1-$L$3)*E3`
- `F4`: `=D3+E3`
- `G4`: `=ABS(Tabla1[[#This Row],[F(t)]]-Tabla1[[#This Row],[Columna2]])`
- `H4`: `=Tabla1[[#This Row],[F(t)]]-Tabla1[[#This Row],[Columna2]]`
- `I4`: `=Tabla1[[#This Row],[MAD]]/Tabla1[[#This Row],[Columna2]]`
- `D5`: `=C5*$L$2+(1-$L$2)*(D4+E4)`
- `F13`: `=$D$11+2*$E$11`
- `G20`: `=AVERAGE(G4:G11)`
- `I20`: `=AVERAGE(I4:I11)`

