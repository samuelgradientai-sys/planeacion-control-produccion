# otra-materia-gerencia-financiera-parcial-2do-corte

> **Archivo:** [`otra-materia-gerencia-financiera-parcial-2do-corte.xlsx`](./otra-materia-gerencia-financiera-parcial-2do-corte.xlsx) · **Corte 3** · Libro de Excel con 2 hoja(s): `TB `, `EEFF`  
> **Nombre original:** `CORTE 3/Parcial 2do Corte G. Financiera .xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

> **Aviso: este archivo NO pertenece a Planeación, Programación y Control de la Producción.** Es de otra materia, **Gerencia Financiera**. El estudiante lo tenía en la carpeta del Corte 3 (nombre original `CORTE 3/Parcial 2do Corte G. Financiera .xlsx`). Se conserva solo para no perder información; ningún tema de scheduling lo usa.

**Qué es:** un libro de Excel de un parcial del segundo corte de Gerencia Financiera. Parte de dos **balances de prueba** (trial balance, 2024 y 2025) de una empresa que comercializa vehículos nuevos («mismo caso al usado en clase», celda B2). A partir de ellos se arman los **estados financieros** con **análisis vertical** y **horizontal**.

El libro está **a medio resolver**: el estado de resultados está calculado hasta la utilidad antes de impuestos y el balance general solo hasta propiedad, planta y equipo bruto. El resto de celdas y el análisis horizontal están vacíos. Dos comentarios de celda dan las reglas para terminarlo (impuesto del 35 % y nada de impuesto si la UAI es negativa).

Se aprende a:

- clasificar las cuentas de un balance de prueba en estado de resultados y balance general;
- calcular la utilidad bruta, el EBIT, la UAI, la utilidad neta y el EBITDA;
- hacer el análisis vertical (cada partida como porcentaje de las ventas) y el horizontal (variación absoluta y porcentual entre años);
- comprobar que Activo = Pasivo + Patrimonio.

### Hoja `TB ` (balance de prueba; el nombre lleva un espacio al final)

**Enunciado (celda B2, combinada B2:H2):** «Contexto: Corresponde a una empresa que se dedica a la comercialización de vehículos nuevos, mismo caso al usado en clase.»

**Datos de entrada.** Hay dos bloques, *TRIAL BALANCE 2024* en B5:D30 y *TRIAL BALANCE 2025* en F5:H30. En cada uno van la cuenta, el saldo débito y el saldo crédito, en pesos (sin unidad indicada):

| Cuenta | 2024 Débito | 2024 Crédito | 2025 Débito | 2025 Crédito |
|---|---|---|---|---|
| Caja y Bancos | 100.000 | 0 | 308.000 | 0 |
| CxC Comerciales | 210.000 | 0 | 220.000 | 0 |
| CxC Empleados | 10.000 | 0 | 15.000 | 0 |
| CxC Socios y Accionistas | 20.000 | 0 | 25.000 | 0 |
| Anticipos de Impuestos | 10.000 | 0 | 20.000 | 0 |
| Inventarios | 200.000 | 0 | 220.000 | 0 |
| Propiedad, Planta y Equipo (Bruto) | 300.000 | 0 | 300.000 | 0 |
| Depreciación Acumulada | 0 | 40.000 | 0 | 80.000 |
| Activos Intangibles (Licencias/Soft) | 50.000 | 0 | 50.000 | 0 |
| Amortización Acumulada | 0 | 10.000 | 0 | 20.000 |
| Proveedores | 0 | 130.000 | 0 | 130.000 |
| Anticipos Recibidos de Clientes | 0 | 20.000 | 0 | 30.000 |
| Obligaciones Financieras (CP) | 0 | 25.000 | 0 | 20.000 |
| Obligaciones Financieras (LP) | 0 | 75.000 | 0 | 60.000 |
| Capital Social | 0 | 304.000 | 0 | 304.000 |
| Reservas y Utilidades Retenidas | 0 | 150.000 | 0 | 296.000 |
| Ventas (Ingresos Operacionales) | 0 | 1.000.000 | 0 | 1.200.000 |
| Costo de Ventas | 600.000 | 0 | 725.000 | 0 |
| Gastos de Administración | 100.000 | 0 | 120.000 | 0 |
| Gasto Depreciación | 40.000 | 0 | 40.000 | 0 |
| Gasto Amortización | 10.000 | 0 | 10.000 | 0 |
| Gastos de Ventas | 90.000 | 0 | 75.000 | 0 |
| Gastos Financieros (Intereses) | 14.000 | 0 | 12.000 | 0 |
| **TOTALES** (fila 30) | **1.754.000** | **1.754.000** | **2.140.000** | **2.140.000** |

**Fórmulas:** solo los totales, $\text{C30}=\sum_{\text{C7}}^{\text{C29}}$; lo mismo en D30, G30 y H30. Ambos años cuadran (débitos = créditos).

**Lectura.** Es un balance de prueba **antes del cierre**: mezcla las cuentas de balance con las de resultados del año. Las reservas pasan de 150.000 a 296.000. La diferencia, 146.000, es exactamente la utilidad de 2024 antes de impuestos con la amortización incluida: 1.000.000 − 600.000 − 100.000 − 40.000 − 10.000 − 90.000 − 14.000 = 146.000. Es decir, la utilidad de 2024 se trasladó entera a reservas (deducido).

### Hoja `EEFF` (estados financieros)

**Objetivo (deducido de la estructura):** construir el estado de resultados y el estado de situación financiera de 2024 y 2025 con análisis vertical (columnas D y F) y horizontal (G en pesos, H en porcentaje).

**Método (fórmulas de las celdas):**

- Las partidas se traen del balance de prueba: `C4='TB '!D23` (ventas 2024), `E4='TB '!H23` (ventas 2025), `C5='TB '!C24` (costo de ventas), `C7='TB '!C25` (administración), `C8='TB '!C28` (ventas), `C9='TB '!C26` (depreciación), `C11='TB '!C29` (intereses). Igual para 2025 con la columna G.
- Utilidad bruta: $UB=\text{Ventas}-\text{CV}$ (`C6=C4-C5`).
- EBIT: $UB-\text{G. adm.}-\text{G. ventas}-\text{Depreciación}$ (`C10=C6-C7-C8-C9`).
- UAI: $EBIT-\text{Intereses}-\text{Ingresos no operacionales}$ (`C13=C10-C11-C12`). El signo menos aplicado a los *ingresos* no operacionales es un error de signo; no tiene efecto porque C12 está vacía.
- Análisis vertical: $\%_i=\text{partida}_i/\text{Ventas}$ (`D4=C4/$C$4`, …, `F4=E4/$E$4`).
- Balance: activos corrientes traídos del TB (C20:C25 y E20:E25), $\text{Total activo corriente}=\sum$ (`C26=SUM(C20:C25)`) y PPE bruto (`C27='TB '!C13`).

**Resultados calculados en el archivo:**

| Partida | 2024 | A. vertical 2024 | 2025 | A. vertical 2025 |
|---|---|---|---|---|
| Ventas | 1.000.000 | 100 % | 1.200.000 | 100 % |
| Costo de ventas | 600.000 | 60,0 % | 725.000 | 60,4 % |
| Utilidad bruta | 400.000 | 40,0 % | 475.000 | 39,6 % |
| Gastos de administración | 100.000 | 10,0 % | 120.000 | 10,0 % |
| Gastos de ventas | 90.000 | 9,0 % | 75.000 | 6,25 % |
| Gasto depreciación | 40.000 | 4,0 % | 40.000 | 3,3 % |
| Utilidad operativa (EBIT) | 170.000 | 17,0 % | 240.000 | 20,0 % |
| Gastos financieros | 14.000 | 1,4 % | 12.000 | 1,0 % |
| Ingresos no operacionales | (vacío) | 0 % | (vacío) | 0 % |
| UAI | 156.000 | 15,6 % | 228.000 | 19,0 % |
| Impuesto de renta (provisión) | (vacío) | 0 % | (vacío) | 0 % |
| Utilidad neta del ejercicio | (vacío) | 0 % | (vacío) | 0 % |
| EBITDA (EBIT + Depreciación) | (vacío) | 0 % | (vacío) | 0 % |

| Balance | 2024 | 2025 |
|---|---|---|
| Caja y Bancos | 100.000 | 308.000 |
| CxC Clientes | 210.000 | 220.000 |
| CxC Empleados | 10.000 | 15.000 |
| CxC Socios y Accionistas | 20.000 | 25.000 |
| Anticipos de Impuestos | 10.000 | 20.000 |
| Inventarios | 200.000 | 220.000 |
| **Total Activo Corriente** | **550.000** | **808.000** |
| Propiedad, Planta y Equipo (Bruto) | 300.000 | 300.000 |
| Depreciación acumulada, PPE neto, total activo, todo el pasivo y el patrimonio, la comprobación (filas 28–46) y las columnas G–H | (vacías) | (vacías) |

**Comentarios de celda (las reglas del ejercicio):**

- B14 (Impuesto de renta): «IF: si la UAI es negativa no se provisiona impuesto (regla vista en clase).» La fórmula esperada es del tipo $\text{Impuesto}=\text{SI}(UAI>0;\;0{,}35\cdot UAI;\;0)$ (deducido).
- B35 (Provisión impuesto de renta del ejercicio): «El Trial Balance no trae el gasto de impuesto: la provisión del 35% se reconoce como pasivo y la utilidad del ejercicio va neta al patrimonio. Así el balance cuadra.»

**Gráficos:** no hay.

**Cómo se completaría (cálculo propio, no está en el archivo).** Si se incluye la amortización y la tasa del 35 % de los comentarios:

| Concepto | 2024 | 2025 |
|---|---|---|
| EBIT con amortización (EBIT de la hoja − 10.000) | 160.000 | 230.000 |
| UAI con amortización | 146.000 | 218.000 |
| Impuesto 35 % | 51.100 | 76.300 |
| Utilidad neta | 94.900 | 141.700 |
| EBITDA (EBIT + depreciación + amortización; da lo mismo con el EBIT de la hoja más la depreciación) | 210.000 | 280.000 |
| PPE neto (300.000 − dep. acumulada) | 260.000 | 220.000 |
| Intangibles netos (50.000 − amort. acumulada) | 40.000 | 30.000 |
| Total activo | 850.000 | 1.058.000 |
| Pasivo sin impuesto (proveedores + anticipos de clientes + oblig. CP + LP) | 250.000 | 240.000 |
| Total pasivo con provisión de impuesto | 301.100 | 316.300 |
| Patrimonio (capital + reservas + utilidad neta) | 548.900 | 741.700 |
| Pasivo + patrimonio | 850.000 | 1.058.000 |

Análisis horizontal (deducido, 2025 frente a 2024):

- Ventas: +200.000 (+20 %).
- Costo de ventas: +125.000 (+20,8 %).
- Utilidad bruta: +75.000 (+18,75 %).
- Gastos de administración: +20.000 (+20 %).
- Gastos de ventas: −15.000 (−16,7 %).
- EBIT de la hoja: +70.000 (+41,2 %).
- Intereses: −2.000 (−14,3 %).
- UAI de la hoja: +72.000 (+46,2 %).
- Caja: +208.000 (+208 %).
- Total activo corriente: +258.000 (+46,9 %).

**Conclusión:** en 2025 las ventas crecen 20 %, el margen bruto se mantiene cerca del 40 % y el margen operativo sube de 17 % a 20 %, sobre todo por menores gastos de ventas. La caja se triplica.

### Observaciones

- **Archivo de otra materia** (Gerencia Financiera); no tiene relación con planeación de la producción.
- **Libro incompleto:**
  - las filas 14–16 (impuesto, utilidad neta, EBITDA) están vacías;
  - las filas 28–46 del balance también;
  - las columnas G–H (análisis horizontal) no tienen ninguna fórmula;
  - las celdas vacías de análisis vertical muestran 0 %.
- **La plantilla EEFF omite cuentas del TB:**
  - el *Gasto Amortización* (10.000 por año) no entra en el EBIT, así que la UAI de la hoja (156.000 y 228.000) queda 10.000 por encima de la real;
  - *Activos Intangibles*, *Amortización Acumulada* y *Anticipos Recibidos de Clientes* no tienen fila en el balance.
- **La plantilla trae filas sin saldo en el TB:** *Obligaciones Laborales* e *Impuestos Corrientes por Pagar*. Si no se agregan las cuentas omitidas, la comprobación Activo − Pasivo − Patrimonio no daría cero.
- **Nombres y signos:**
  - la cuenta se llama «CxC Comerciales» en el TB y «CxC Clientes» en EEFF;
  - en C13/E13 los ingresos no operacionales se restan en vez de sumarse.
- No hay gráficos, imágenes ni hojas ocultas. La dimensión de `TB ` llega a la columna I, pero esa columna no tiene datos.

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `TB ` — 30 filas × 9 columnas

| Fila | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| 2 |  | Contexto:  Corresponde a una empresa que se dedica a la comercialización de vehículos nuevos,  mismo caso al usado en clase. |  |  |  |  |  |  |
| 5 |  | TRIAL BALANCE 2024 |  |  |  | TRIAL BALANCE 2025 |  |  |
| 6 |  | Cuenta | Saldo Débito | Saldo Crédito |  | Cuenta | Saldo Débito | Saldo Crédito |
| 7 |  | Caja y Bancos | 100000 | 0 |  | Caja y Bancos | 308000 | 0 |
| 8 |  | CxC Comerciales | 210000 | 0 |  | CxC Comerciales | 220000 | 0 |
| 9 |  | CxC Empleados | 10000 | 0 |  | CxC Empleados | 15000 | 0 |
| 10 |  | CxC Socios y Accionistas | 20000 | 0 |  | CxC Socios y Accionistas | 25000 | 0 |
| 11 |  | Anticipos de Impuestos | 10000 | 0 |  | Anticipos de Impuestos | 20000 | 0 |
| 12 |  | Inventarios | 200000 | 0 |  | Inventarios | 220000 | 0 |
| 13 |  | Propiedad, Planta y Equipo (Bruto) | 300000 | 0 |  | Propiedad, Planta y Equipo (Bruto) | 300000 | 0 |
| 14 |  | Depreciación Acumulada | 0 | 40000 |  | Depreciación Acumulada | 0 | 80000 |
| 15 |  | Activos Intangibles (Licencias/Soft) | 50000 | 0 |  | Activos Intangibles (Licencias/Soft) | 50000 | 0 |
| 16 |  | Amortización Acumulada | 0 | 10000 |  | Amortización Acumulada | 0 | 20000 |
| 17 |  | Proveedores | 0 | 130000 |  | Proveedores | 0 | 130000 |
| 18 |  | Anticipos Recibidos de Clientes | 0 | 20000 |  | Anticipos Recibidos de Clientes | 0 | 30000 |
| 19 |  | Obligaciones Financieras (CP) | 0 | 25000 |  | Obligaciones Financieras (CP) | 0 | 20000 |
| 20 |  | Obligaciones Financieras (LP) | 0 | 75000 |  | Obligaciones Financieras (LP) | 0 | 60000 |
| 21 |  | Capital Social | 0 | 304000 |  | Capital Social | 0 | 304000 |
| 22 |  | Reservas y Utilidades Retenidas | 0 | 150000 |  | Reservas y Utilidades Retenidas | 0 | 296000 |
| 23 |  | Ventas (Ingresos Operacionales) | 0 | 1000000 |  | Ventas (Ingresos Operacionales) | 0 | 1200000 |
| 24 |  | Costo de Ventas | 600000 | 0 |  | Costo de Ventas | 725000 | 0 |
| 25 |  | Gastos de Administración | 100000 | 0 |  | Gastos de Administración | 120000 | 0 |
| 26 |  | Gasto Depreciación | 40000 | 0 |  | Gasto Depreciación | 40000 | 0 |
| 27 |  | Gasto Amortización | 10000 | 0 |  | Gasto Amortización | 10000 | 0 |
| 28 |  | Gastos de Ventas | 90000 | 0 |  | Gastos de Ventas | 75000 | 0 |
| 29 |  | Gastos Financieros (Intereses) | 14000 | 0 |  | Gastos Financieros (Intereses) | 12000 | 0 |
| 30 |  | TOTALES | 1754000 | 1754000 |  | TOTALES | 2140000 | 2140000 |

**Fórmulas (4 patrones distintos):**

- `C30`: `=SUM(C7:C29)`
- `D30`: `=SUM(D7:D29)`
- `G30`: `=SUM(G7:G29)`
- `H30`: `=SUM(H7:H29)`

### Hoja `EEFF` — 46 filas × 8 columnas

| Fila | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| 3 |  | Estado de Resultados | 2024 | A. Vertical 2024 | 2025 | A. Vertical 2025 | Análisis H. $ | Análisis H. % |
| 4 |  | Ventas (Ingresos Operacionales) | 1000000 | 1 | 1200000 | 1 |  |  |
| 5 |  | Costo de Ventas | 600000 | 0.6 | 725000 | 0.604167 |  |  |
| 6 |  | Utilidad Bruta | 400000 | 0.4 | 475000 | 0.395833 |  |  |
| 7 |  | Gastos de Administración | 100000 | 0.1 | 120000 | 0.1 |  |  |
| 8 |  | Gastos de Ventas | 90000 | 0.09 | 75000 | 0.0625 |  |  |
| 9 |  | Gasto Depreciación | 40000 | 0.04 | 40000 | 0.0333333 |  |  |
| 10 |  | Utilidad Operativa (EBIT) | 170000 | 0.17 | 240000 | 0.2 |  |  |
| 11 |  | Gastos Financieros (Intereses) | 14000 | 0.014 | 12000 | 0.01 |  |  |
| 12 |  | Ingresos No Operacionales |  | 0 |  | 0 |  |  |
| 13 |  | Utilidad Antes de Impuestos (UAI) | 156000 | 0.156 | 228000 | 0.19 |  |  |
| 14 |  | Impuesto de Renta (provisión) |  | 0 |  | 0 |  |  |
| 15 |  | Utilidad Neta del Ejercicio |  | 0 |  | 0 |  |  |
| 16 |  | EBITDA (EBIT + Depreciación) |  | 0 |  | 0 |  |  |
| 17 |  |  |  | 0 |  | 0 |  |  |
| 18 |  | Estado de Situación Financiera | 2024 | A. Vertical 2024 | 2025 | A. Vertical 2025 | Análisis H. $ | Análisis H. % |
| 19 |  | ACTIVO |  |  |  |  |  |  |
| 20 |  | Caja y Bancos | 100000 |  | 308000 |  |  |  |
| 21 |  | CxC Clientes | 210000 |  | 220000 |  |  |  |
| 22 |  | CxC Empleados | 10000 |  | 15000 |  |  |  |
| 23 |  | CxC Socios y Accionistas | 20000 |  | 25000 |  |  |  |
| 24 |  | Anticipos de Impuestos | 10000 |  | 20000 |  |  |  |
| 25 |  | Inventarios | 200000 |  | 220000 |  |  |  |
| 26 |  | Total Activo Corriente | 550000 |  | 808000 |  |  |  |
| 27 |  | Propiedad, Planta y Equipo (Bruto) | 300000 |  | 300000 |  |  |  |
| 28 |  | Depreciación Acumulada |  |  |  |  |  |  |
| 29 |  | Propiedad, Planta y Equipo (Neto) |  |  |  |  |  |  |
| 30 |  | TOTAL ACTIVO |  |  |  |  |  |  |
| 31 |  | PASIVO |  |  |  |  |  |  |
| 32 |  | Proveedores |  |  |  |  |  |  |
| 33 |  | Obligaciones Laborales |  |  |  |  |  |  |
| 34 |  | Impuestos Corrientes por Pagar |  |  |  |  |  |  |
| 35 |  | Provisión Impuesto de Renta del Ejercicio |  |  |  |  |  |  |
| 36 |  | Obligaciones Financieras (CP) |  |  |  |  |  |  |
| 37 |  | Total Pasivo Corriente |  |  |  |  |  |  |
| 38 |  | Obligaciones Financieras (LP) |  |  |  |  |  |  |
| 39 |  | TOTAL PASIVO |  |  |  |  |  |  |
| 40 |  | PATRIMONIO |  |  |  |  |  |  |
| 41 |  | Capital Social |  |  |  |  |  |  |
| 42 |  | Reservas y Utilidades Retenidas |  |  |  |  |  |  |
| 43 |  | Utilidad del Ejercicio |  |  |  |  |  |  |
| 44 |  | TOTAL PATRIMONIO |  |  |  |  |  |  |
| 45 |  | TOTAL PASIVO + PATRIMONIO |  |  |  |  |  |  |
| 46 |  | Comprobación (Activo − Pasivo − Patrimonio) |  |  |  |  |  |  |

**Fórmulas (14 patrones distintos):**

- `C4`: `='TB '!D23`
- `D4`: `=C4/$C$4`
- `E4`: `='TB '!H23`
- `F4`: `=E4/$E$4`
- `C5`: `='TB '!C24`
- `E5`: `='TB '!G24`
- `C6`: `=C4-C5`
- `E6`: `=E4-E5`
- `C10`: `=C6-C7-C8-C9`
- `E10`: `=E6-E7-E8-E9`
- `C13`: `=C10-C11-C12`
- `E13`: `=E10-E11-E12`
- `C26`: `=SUM(C20:C25)`
- `E26`: `=SUM(E20:E25)`

