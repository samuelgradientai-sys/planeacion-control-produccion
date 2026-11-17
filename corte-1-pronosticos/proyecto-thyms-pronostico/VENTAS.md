# VENTAS

> **Archivo:** [`VENTAS.xls`](./VENTAS.xls) · **Corte 1** · Libro .xls con 2 hoja(s): `UNIFICADO`, `MAY-JUN-JUL`  
> **Nombre original:** `CORTE 1/PROYECTO/VENTAS.xls`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los datos

### Qué es

Datos reales de ventas de THYMS Colombia S.A.S. en 2026 que entregó la empresa para el proyecto: las ventas de **un vendedor (código 401, «VENDEDOR 401») de la zona 04, Antioquia**. Los clientes están anonimizados (CLIENTE ###, códigos 9#####). Es la fuente de todo el proyecto:
- el cuaderno [`Planeacion_proyecto_corte1.md`](./Planeacion_proyecto_corte1.md) lee la hoja `MAY-JUN-JUL`;
- los Excel de suavización exponencial ([`pronostico-expo-simple.md`](./pronostico-expo-simple.md) y [`pronostico-expo-simple-ppco.md`](./pronostico-expo-simple-ppco.md)) traen copias de las dos hojas y pronostican con `UNIFICADO`;
- en el Corte 2, el libro [`Datos Thyms Completo.md`](../../corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Datos%20Thyms%20Completo.md) las copia en sus hojas `Ventas` y `Facturas Mayo-Julio`.

### Hoja `UNIFICADO`: ventas mensuales en COP

Una fila con el total facturado por mes en 2026 (columnas F a Q) y el total del año (R).

| Mes | Ventas (COP) |
|---|---|
| Enero | 95.752.306 |
| Febrero | 153.850.391 |
| Marzo | 201.004.440 |
| Abril | 52.446.770 |
| Mayo | 197.484.330 |
| Junio | 156.580.280 |
| Julio | 230.979.600 |
| Agosto | 119.882.540 |
| Septiembre a diciembre | 0 (sin datos aún) |
| **Total** | **1.207.980.657** |

- Promedio de enero a agosto: 150.997.582 COP/mes.
- Mes más alto: julio; más bajo: abril.
- Coeficiente de variación de enero a agosto: 39,4 % (calculado en la hoja `Ventas` del libro del Corte 2).
- Con 12.900 COP/tubo, el promedio equivale a unos 11.705 tubos/mes.

### Hoja `MAY-JUN-JUL`: detalle de facturas

464 facturas (filas 2 a 465) y 18 columnas. Todas las filas en [`VENTAS-datos/MAY-JUN-JUL.csv`](./VENTAS-datos/MAY-JUN-JUL.csv).

| Columna | Significado (deducido de los valores) |
|---|---|
| `ano_doc` | Año: 2026 |
| `per_doc` | Mes: 05, 06 o 07 |
| `tip_doc` | Tipo de documento: siempre 010 (factura) |
| `num_doc` | Número de factura, de F571143 a F580175 |
| `cod_cli`, `nom_cli` | Cliente anonimizado (161 clientes distintos) |
| `valorfac` = `valordoc` | Valor facturado con IVA: exactamente 1,19 × `subdoc` |
| `valordes` | Descuento: `netdoc` − `subdoc` |
| `subdoc` | Subtotal neto (después de descuento y antes de IVA). Es el valor que usa todo el proyecto |
| `netdoc` | Valor bruto antes de descuento: `subdoc` + `valordes` |
| `codven`, `nomven` | 401, «VENDEDOR 401» |
| `devolu`, `notas` | Devoluciones y notas: siempre 0 |
| `codzona`, `nomzona` | 04, ANTIOQUIA |
| `total` | Igual a `subdoc` |

**Resumen por mes** (recalculado del CSV; las unidades se obtienen factura por factura con $\mathrm{round}(\text{subdoc}/12.900)$, como en el cuaderno):

| Mes | Facturas | `subdoc` (COP) | `valorfac` con IVA (COP) | Descuentos (COP) | `netdoc` bruto (COP) | Tubos |
|---|---|---|---|---|---|---|
| Mayo | 165 | 198.232.170 | 235.896.290 | 137.589.030 | 335.821.200 | 15.365 |
| Junio | 135 | 159.703.880 | 190.047.620 | 113.927.320 | 273.631.200 | 12.379 |
| Julio | 164 | 232.877.145 | 277.123.805 | 145.517.355 | 378.394.500 | 18.054 |
| **Total** | **464** | **590.813.195** | **703.067.715** | **397.033.705** | **987.846.900** | **45.798** |

- Por factura, `subdoc` va de 100.320 a 11.343.600 COP: media 1.273.304, mediana 1.021.820, desviación 1.157.631, $Q_1$ = 633.555 y $Q_3$ = 1.548.476.
- Distribución muy sesgada a la derecha: 21 facturas superan la valla de 1,5·IQR.
- El descuento promedio es el 40,2 % del valor bruto.
- Los 10 mayores clientes concentran el 39,0 % de las ventas y el mayor, el 13,6 % (hoja `Clientes` del libro del Corte 2).

### Observaciones

- **Las facturas no cuadran exactamente con `UNIFICADO`:** la suma de `subdoc` supera a `UNIFICADO` en 747.840 COP en mayo, 3.123.600 en junio y 1.897.545 en julio (diferencias que también calcula la hoja `Ventas` del libro del Corte 2). No se sabe qué ajuste explica la diferencia.
- Agosto aparece en `UNIFICADO` (119.882.540) pero no hay facturas de agosto. No se sabe si el mes estaba completo cuando se exportó.
- Solo hay **8 meses** de una sola zona; no alcanza para validar estacionalidad ni para representar la planta (supuesto de escala en el Corte 2).
- El CSV de este archivo conserva los ceros a la izquierda («05», «010», «04»); las copias de los Excel de pronóstico los guardan como números (5, 10, 4). Los datos son los mismos.

## Anexo: volcado de celdas por hoja

> Datos de clientes anonimizados (CLIENTE ###, códigos 9#####).

### Hoja `UNIFICADO` — 2 filas × 18 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ano_doc | codzona | codven | nomven | nomzona | enero | febrero | marzo | abril | mayo | junio | julio | agosto | septiembre | octubre | noviembre | diciembre | total |
| 2 | 2026 | 04 | 401 | VENDEDOR 401 | ANTIOQUIA | 95752306 | 153850391 | 201004440 | 52446770 | 197484330 | 156580280 | 230979600 | 119882540 | 0 | 0 | 0 | 0 | 1207980657 |

### Hoja `MAY-JUN-JUL` — 465 filas × 18 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ano_doc | per_doc | tip_doc | num_doc | cod_cli | nom_cli | valorfac | valordoc | valordes | subdoc | netdoc | codven | nomven | devolu | notas | codzona | nomzona | total |
| 2 | 2026 | 05 | 010 | F571143 | 900001 | CLIENTE 001 | 307377 | 307377 | 126000 | 258300 | 384300 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 258300 |
| 3 | 2026 | 05 | 010 | F571144 | 900002 | CLIENTE 002 | 1319972 | 1319972 | 1063980 | 1109220 | 2173200 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 1109220 |
| 4 | 2026 | 05 | 010 | F571145 | 900003 | CLIENTE 003 | 359856 | 359856 | 270300 | 302400 | 572700 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 302400 |
| 5 | 2026 | 05 | 010 | F571146 | 900004 | CLIENTE 004 | 652525 | 652525 | 97060 | 548340 | 645400 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 548340 |
| 6 | 2026 | 05 | 010 | F571149 | 900005 | CLIENTE 005 | 2110870 | 2110870 | 1475760 | 1773840 | 3249600 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 1773840 |
| 7 | 2026 | 05 | 010 | F571154 | 900006 | CLIENTE 006 | 1158536 | 1158536 | 740240 | 973560 | 1713800 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 973560 |
| 8 | 2026 | 05 | 010 | F571155 | 900005 | CLIENTE 005 | 1953504 | 1953504 | 1598400 | 1641600 | 3240000 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 1641600 |
| 9 | 2026 | 05 | 010 | F571160 | 900007 | CLIENTE 007 | 591478 | 591478 | 443760 | 497040 | 940800 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 497040 |
| 10 | 2026 | 05 | 010 | F571162 | 900008 | CLIENTE 008 | 567398 | 567398 | 332295 | 476805 | 809100 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 476805 |
| 11 | 2026 | 05 | 010 | F571164 | 900009 | CLIENTE 009 | 3427337 | 3427337 | 1680885 | 2880115 | 4561000 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 2880115 |
| 12 | 2026 | 05 | 010 | F571168 | 900010 | CLIENTE 010 | 911635 | 911635 | 518720 | 766080 | 1284800 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 766080 |
| 13 | 2026 | 05 | 010 | F571169 | 900011 | CLIENTE 011 | 3411849 | 3411849 | 1752700 | 2867100 | 4619800 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 2867100 |
| 14 | 2026 | 05 | 010 | F571170 | 900012 | CLIENTE 012 | 1709316 | 1709316 | 1398600 | 1436400 | 2835000 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 1436400 |
| 15 | 2026 | 05 | 010 | F571171 | 900007 | CLIENTE 007 | 1790712 | 1790712 | 1465200 | 1504800 | 2970000 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 1504800 |
| 16 | 2026 | 05 | 010 | F571172 | 900013 | CLIENTE 013 | 2375407 | 2375407 | 1739460 | 1996140 | 3735600 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 1996140 |
| 17 | 2026 | 05 | 010 | F571173 | 900012 | CLIENTE 012 | 2002342 | 2002342 | 1470960 | 1682640 | 3153600 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 1682640 |
| 18 | 2026 | 05 | 010 | F571174 | 900014 | CLIENTE 014 | 724424 | 724424 | 248740 | 608760 | 857500 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 608760 |
| 19 | 2026 | 05 | 010 | F571176 | 900015 | CLIENTE 015 | 755626 | 755626 | 103720 | 634980 | 738700 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 634980 |
| 20 | 2026 | 05 | 010 | F571177 | 900016 | CLIENTE 016 | 1465128 | 1465128 | 1198800 | 1231200 | 2430000 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 1231200 |
| 21 | 2026 | 05 | 010 | F571178 | 900017 | CLIENTE 017 | 1402724 | 1402724 | 874040 | 1178760 | 2052800 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 1178760 |
| 22 | 2026 | 05 | 010 | F571179 | 900012 | CLIENTE 012 | 570450 | 570450 | 60330 | 479370 | 539700 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 479370 |
| 23 | 2026 | 05 | 010 | F571180 | 900018 | CLIENTE 018 | 409693 | 409693 | 207120 | 344280 | 551400 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 344280 |
| 24 | 2026 | 05 | 010 | F571181 | 900009 | CLIENTE 009 | 1805974 | 1805974 | 248675 | 1517625 | 1766300 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 1517625 |
| 25 | 2026 | 05 | 010 | F571182 | 900019 | CLIENTE 019 | 667447 | 667447 | 490320 | 560880 | 1051200 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 560880 |
| 26 | 2026 | 05 | 010 | F571183 | 900020 | CLIENTE 020 | 325584 | 325584 | 266400 | 273600 | 540000 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 273600 |
| 27 | 2026 | 05 | 010 | F571261 | 900021 | CLIENTE 021 | 976752 | 976752 | 799200 | 820800 | 1620000 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 820800 |
| 28 | 2026 | 05 | 010 | F571262 | 900022 | CLIENTE 022 | 895356 | 895356 | 732600 | 752400 | 1485000 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 752400 |
| 29 | 2026 | 05 | 010 | F571263 | 900022 | CLIENTE 022 | 667447 | 667447 | 490320 | 560880 | 1051200 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 560880 |
| 30 | 2026 | 05 | 010 | F571264 | 900023 | CLIENTE 023 | 7686496 | 7686496 | 1835160 | 6459240 | 8294400 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 6459240 |
| 31 | 2026 | 05 | 010 | F571270 | 900024 | CLIENTE 024 | 1693376 | 1693376 | 1149595 | 1423005 | 2572600 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 1423005 |
| 32 | 2026 | 05 | 010 | F571286 | 900025 | CLIENTE 025 | 1130262 | 1130262 | 756000 | 949800 | 1705800 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 949800 |
| 33 | 2026 | 05 | 010 | F571290 | 900023 | CLIENTE 023 | 4512052 | 4512052 | 199560 | 3791640 | 3991200 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 3791640 |
| 34 | 2026 | 05 | 010 | F571291 | 900026 | CLIENTE 026 | 617705 | 617705 | 62520 | 519080 | 581600 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 519080 |
| 35 | 2026 | 05 | 010 | F571361 | 900027 | CLIENTE 027 | 333724 | 333724 | 245160 | 280440 | 525600 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 280440 |
| 36 | 2026 | 05 | 010 | F571362 | 900028 | CLIENTE 028 | 2791883 | 2791883 | 2137680 | 2346120 | 4483800 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 2346120 |
| 37 | 2026 | 05 | 010 | F571367 | 900029 | CLIENTE 029 | 451962 | 451962 | 17600 | 379800 | 397400 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 379800 |
| 38 | 2026 | 05 | 010 | F571369 | 900029 | CLIENTE 029 | 771120 | 771120 | 567000 | 648000 | 1215000 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 648000 |
| 39 | 2026 | 05 | 010 | F571392 | 900030 | CLIENTE 030 | 1002867 | 1002867 | 669955 | 842745 | 1512700 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 842745 |
| 40 | 2026 | 05 | 010 | F571393 | 900031 | CLIENTE 031 | 1465128 | 1465128 | 1198800 | 1231200 | 2430000 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 1231200 |
| 41 | 2026 | 05 | 010 | F571396 | 900031 | CLIENTE 031 | 1686254 | 1686254 | 1144980 | 1417020 | 2562000 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 1417020 |
| 42 | 2026 | 05 | 010 | F571397 | 900032 | CLIENTE 032 | 2181413 | 2181413 | 1718280 | 1833120 | 3551400 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 1833120 |
| 43 | 2026 | 05 | 010 | F571413 | 900028 | CLIENTE 028 | 2705060 | 2705060 | 1398340 | 2273160 | 3671500 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 2273160 |
| 44 | 2026 | 05 | 010 | F571414 | 900033 | CLIENTE 033 | 2192266 | 2192266 | 1537960 | 1842240 | 3380200 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 1842240 |
| 45 | 2026 | 05 | 010 | F571415 | 900033 | CLIENTE 033 | 1370166 | 1370166 | 787000 | 1151400 | 1938400 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 1151400 |
| 46 | 2026 | 05 | 010 | F571548 | 900034 | CLIENTE 034 | 2827041 | 2827041 | 1794235 | 2375665 | 4169900 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 2375665 |
| 47 | 2026 | 05 | 010 | F571551 | 900035 | CLIENTE 035 | 1256212 | 1256212 | 764360 | 1055640 | 1820000 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 1055640 |
| 48 | 2026 | 05 | 010 | F571554 | 900036 | CLIENTE 036 | 1403064 | 1403064 | 1084455 | 1179045 | 2263500 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 1179045 |
| 49 | 2026 | 05 | 010 | F571555 | 900037 | CLIENTE 037 | 1419908 | 1419908 | 919200 | 1193200 | 2112400 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 1193200 |
| 50 | 2026 | 05 | 010 | F571566 | 900038 | CLIENTE 038 | 2303507 | 2303507 | 1905480 | 1935720 | 3841200 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 1935720 |
| 51 | 2026 | 05 | 010 | F571568 | 900039 | CLIENTE 039 | 835380 | 835380 | 58500 | 702000 | 760500 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 702000 |
| 52 | 2026 | 05 | 010 | F571569 | 900040 | CLIENTE 040 | 1343034 | 1343034 | 1098900 | 1128600 | 2227500 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 1128600 |
| 53 | 2026 | 05 | 010 | F571570 | 900038 | CLIENTE 038 | 1066288 | 1066288 | 844560 | 896040 | 1740600 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 896040 |
| 54 | 2026 | 05 | 010 | F571571 | 900040 | CLIENTE 040 | 1340999 | 1340999 | 724310 | 1126890 | 1851200 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 1126890 |
| 55 | 2026 | 05 | 010 | F571572 | 900041 | CLIENTE 041 | 3339949 | 3339949 | 2599320 | 2806680 | 5406000 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 2806680 |
| 56 | 2026 | 05 | 010 | F571578 | 900042 | CLIENTE 042 | 2781369 | 2781369 | 1792215 | 2337285 | 4129500 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 2337285 |
| 57 | 2026 | 05 | 010 | F571664 | 900043 | CLIENTE 043 | 2699634 | 2699634 | 1808800 | 2268600 | 4077400 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 2268600 |
| 58 | 2026 | 05 | 010 | F571665 | 900044 | CLIENTE 044 | 2051179 | 2051179 | 1969920 | 1723680 | 3693600 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 1723680 |
| 59 | 2026 | 05 | 010 | F571666 | 900044 | CLIENTE 044 | 948603 | 948603 | 41955 | 797145 | 839100 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 797145 |
| 60 | 2026 | 05 | 010 | F571667 | 900044 | CLIENTE 044 | 3418632 | 3418632 | 2797200 | 2872800 | 5670000 | 401 | VENDEDOR 401 | 0 | 0 | 04 | ANTIOQUIA | 2872800 |

> **Hoja larga:** arriba se muestran 60 de 465 filas. **Todas las filas están en [`VENTAS-datos/MAY-JUN-JUL.csv`](./VENTAS-datos/MAY-JUN-JUL.csv)** (CSV, UTF-8).

