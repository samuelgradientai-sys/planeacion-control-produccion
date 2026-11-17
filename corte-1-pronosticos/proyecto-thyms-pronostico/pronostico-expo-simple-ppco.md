# pronostico-expo-simple-ppco

> **Archivo:** [`pronostico-expo-simple-ppco.xlsx`](./pronostico-expo-simple-ppco.xlsx) · **Corte 1** · Libro de Excel con 3 hoja(s): `UNIFICADO`, `MAY-JUN-JUL`, `PRONOSTICO SES`  
> **Nombre original:** `CORTE 1/PROYECTO/PRONOSTICO EXPO SIMPLE PPCO.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Versión **corregida y final** del pronóstico del proyecto del Corte 1 (THYMS Colombia): suavización exponencial simple (SES) con $\alpha$ = 0,05 sobre las ventas mensuales en COP del vendedor 401 (zona Antioquia), de enero a julio de 2026, para pronosticar agosto. «PPCO» es, por deducción, la sigla del curso (Planeación, Programación y Control de la Producción); el parcial también se llamaba «PARCIAL 1 PPCO». Aplica la clase [L05](../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md).

Comparte datos, fórmulas del pronóstico y resultados con [`pronostico-expo-simple.md`](./pronostico-expo-simple.md); la diferencia está en el MAD y el MAPE (ver «Diferencia con la primera versión» más abajo). Esta es la versión cuyas cifras (MAD 80,2 millones, MAPE 53,4 %) reproduce el Corte 2.

### Hojas `UNIFICADO` y `MAY-JUN-JUL`

Copias exactas de las hojas de [`VENTAS.xls`](./VENTAS.md): ventas mensuales en COP de 2026 (enero a agosto) y las 464 facturas de mayo a julio. `MAY-JUN-JUL` no la usa ninguna fórmula.

### Hoja `PRONOSTICO SES`

**Objetivo (deducido):** pronosticar las ventas de agosto de 2026 y medir el error del método de febrero a julio.

**Datos de entrada:** B4:B10 = `UNIFICADO!F2:L2` (ventas de enero a julio, en COP).

**Parámetros:** $\alpha$ = 0,05 (H4). Pronóstico inicial $F_1 = A_1$ (C4 = B4).

**Método paso a paso** ($A_t$ = venta real del mes $t$, $F_t$ = pronóstico):
- C5 a C11 (`=$H$4*B4+(1-$H$4)*C4`): $F_{t+1} = \alpha A_t + (1-\alpha)F_t$. C11 es el pronóstico de agosto.
- D «Error absoluto»: $|A_t - F_t|$.
- E «SSE (error²)»: $(A_t - F_t)^2$.
- F «Error % absoluto (APE)»: $|A_t - F_t|/A_t$.
- Resumen (fila 14), todo de febrero a julio ($n$ = 6):
  - $MAD = \frac{1}{6}\sum_{t=2}^{7}|A_t - F_t|$;
  - $SSE = \sum_{t=2}^{7}(A_t - F_t)^2$;
  - $MSE = SSE/6$;
  - $MAPE = \frac{1}{6}\sum_{t=2}^{7}\frac{|A_t - F_t|}{A_t}$.

**Resultados:**

| Mes | Venta real $A_t$ (COP) | Pronóstico $F_t$ (COP) | Error absoluto | Error² | APE |
|---|---|---|---|---|---|
| Enero | 95.752.306 | 95.752.306 | 0 | 0 | 0,0 % |
| Febrero | 153.850.391 | 95.752.306 | 58.098.085 | 3,375 × 10¹⁵ | 37,8 % |
| Marzo | 201.004.440 | 98.657.210 | 102.347.230 | 1,047 × 10¹⁶ | 50,9 % |
| Abril | 52.446.770 | 103.774.572 | 51.327.802 | 2,635 × 10¹⁵ | 97,9 % |
| Mayo | 197.484.330 | 101.208.182 | 96.276.148 | 9,269 × 10¹⁵ | 48,8 % |
| Junio | 156.580.280 | 106.021.989 | 50.558.291 | 2,556 × 10¹⁵ | 32,3 % |
| Julio | 230.979.600 | 108.549.904 | 122.429.696 | 1,499 × 10¹⁶ | 53,0 % |
| **Agosto (pronóstico)** | — | **114.671.388** | — | — | — |

| Medida (febrero a julio) | Valor |
|---|---|
| MAD | 80.172.875 COP |
| SSE | 4,330 × 10¹⁶ |
| MSE | 7,217 × 10¹⁵ (RMSE ≈ 84,9 millones COP) |
| MAPE | 53,4 % |

- **Pronóstico de agosto:** 114.671.388 COP, unos 8.889 tubos para la zona con 12.900 COP/tubo (conversión que no hace el libro).
- **Sesgo** (calculado en el Corte 2 con los mismos números, error = real − pronóstico): +63.063.608 COP/mes. La señal de rastreo es 4,72, fuera del límite de ±4: el método **subestima** sistemáticamente.

**Gráfico:** líneas sin título; ventas reales (B4:B10) y pronóstico (C4:C11, con agosto). El pronóstico es una línea casi plana entre 96 y 115 millones; las ventas oscilan entre 52 y 231 millones.

**Conclusión:** el error relativo del 53 % y el sesgo positivo muestran que SES con $\alpha$ = 0,05 arrancando en enero no sigue el nivel real (promedio de enero a julio: 155,4 millones). En el Corte 2 se mantuvieron el método y el $\alpha$, pero el arranque se cambió por el promedio de los 3 primeros meses; en la evaluación de origen móvil, eso baja el sesgo de 44,6 a 2,4 millones COP y el RMSE de 76,8 a 63,6 millones.

### Diferencia con la primera versión

| Aspecto | [`pronostico-expo-simple`](./pronostico-expo-simple.md) | Esta versión (PPCO) |
|---|---|---|
| Orden de las hojas | `UNIFICADO`, `PRONOSTICO_SES`, `MAY-JUN-JUL` | `UNIFICADO`, `MAY-JUN-JUL`, `PRONOSTICO SES` |
| Títulos | «MAD» y «MAPE» en las columnas de cada mes; «($)» en los encabezados | «Error absoluto» y «Error % absoluto (APE)» |
| MAD | `AVERAGE(D4:D10)` = 68,7 millones (incluye el error 0 de enero) | `AVERAGE(D5:D10)` = 80,2 millones |
| MAPE | `AVERAGE(F4:F10)` = 45,8 % | `AVERAGE(F5:F10)` = 53,4 % |
| Pronósticos, α, SSE y MSE | Iguales | Iguales |

### Observaciones

- **α sin justificación en el libro.** Recalculado de febrero a julio, $\alpha$ = 0,05 es el que da el menor MAPE (53,43 % frente a 53,59 % con 0,10), pero no el menor MAD (≈ $\alpha$ = 0,5, con 69,2 millones) ni el menor MSE (≈ $\alpha$ = 0,3).
- El dato real de agosto (119.882.540 COP, `UNIFICADO!M2`) no se usa para validar. Frente a él, el pronóstico falla por 5,2 millones (4,3 %).
- No se calcula sesgo ni señal de rastreo, que habrían mostrado la subestimación.
- Todo está en COP de **una sola zona**; el paso a tubos de planta se hace en el Corte 2 ([`Gemelo_Digital_Thyms.md`](../../corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md)).
- La hoja `MAY-JUN-JUL` no se usa.

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `UNIFICADO` — 2 filas × 18 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ano_doc | codzona | codven | nomven | nomzona | enero | febrero | marzo | abril | mayo | junio | julio | agosto | septiembre | octubre | noviembre | diciembre | total |
| 2 | 2026 | 4 | 401 | VENDEDOR 401 | ANTIOQUIA | 95752306 | 153850391 | 201004440 | 52446770 | 197484330 | 156580280 | 230979600 | 119882540 | 0 | 0 | 0 | 0 | 1207980657 |

### Hoja `MAY-JUN-JUL` — 465 filas × 18 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ano_doc | per_doc | tip_doc | num_doc | cod_cli | nom_cli | valorfac | valordoc | valordes | subdoc | netdoc | codven | nomven | devolu | notas | codzona | nomzona | total |
| 2 | 2026 | 5 | 10 | F571143 | 900001 | CLIENTE 001 | 307377 | 307377 | 126000 | 258300 | 384300 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 258300 |
| 3 | 2026 | 5 | 10 | F571144 | 900002 | CLIENTE 002 | 1319972 | 1319972 | 1063980 | 1109220 | 2173200 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 1109220 |
| 4 | 2026 | 5 | 10 | F571145 | 900003 | CLIENTE 003 | 359856 | 359856 | 270300 | 302400 | 572700 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 302400 |
| 5 | 2026 | 5 | 10 | F571146 | 900004 | CLIENTE 004 | 652525 | 652525 | 97060 | 548340 | 645400 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 548340 |
| 6 | 2026 | 5 | 10 | F571149 | 900005 | CLIENTE 005 | 2110870 | 2110870 | 1475760 | 1773840 | 3249600 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 1773840 |
| 7 | 2026 | 5 | 10 | F571154 | 900006 | CLIENTE 006 | 1158536 | 1158536 | 740240 | 973560 | 1713800 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 973560 |
| 8 | 2026 | 5 | 10 | F571155 | 900005 | CLIENTE 005 | 1953504 | 1953504 | 1598400 | 1641600 | 3240000 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 1641600 |
| 9 | 2026 | 5 | 10 | F571160 | 900007 | CLIENTE 007 | 591478 | 591478 | 443760 | 497040 | 940800 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 497040 |
| 10 | 2026 | 5 | 10 | F571162 | 900008 | CLIENTE 008 | 567398 | 567398 | 332295 | 476805 | 809100 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 476805 |
| 11 | 2026 | 5 | 10 | F571164 | 900009 | CLIENTE 009 | 3427337 | 3427337 | 1680885 | 2880115 | 4561000 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 2880115 |
| 12 | 2026 | 5 | 10 | F571168 | 900010 | CLIENTE 010 | 911635 | 911635 | 518720 | 766080 | 1284800 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 766080 |
| 13 | 2026 | 5 | 10 | F571169 | 900011 | CLIENTE 011 | 3411849 | 3411849 | 1752700 | 2867100 | 4619800 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 2867100 |
| 14 | 2026 | 5 | 10 | F571170 | 900012 | CLIENTE 012 | 1709316 | 1709316 | 1398600 | 1436400 | 2835000 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 1436400 |
| 15 | 2026 | 5 | 10 | F571171 | 900007 | CLIENTE 007 | 1790712 | 1790712 | 1465200 | 1504800 | 2970000 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 1504800 |
| 16 | 2026 | 5 | 10 | F571172 | 900013 | CLIENTE 013 | 2375407 | 2375407 | 1739460 | 1996140 | 3735600 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 1996140 |
| 17 | 2026 | 5 | 10 | F571173 | 900012 | CLIENTE 012 | 2002342 | 2002342 | 1470960 | 1682640 | 3153600 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 1682640 |
| 18 | 2026 | 5 | 10 | F571174 | 900014 | CLIENTE 014 | 724424 | 724424 | 248740 | 608760 | 857500 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 608760 |
| 19 | 2026 | 5 | 10 | F571176 | 900015 | CLIENTE 015 | 755626 | 755626 | 103720 | 634980 | 738700 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 634980 |
| 20 | 2026 | 5 | 10 | F571177 | 900016 | CLIENTE 016 | 1465128 | 1465128 | 1198800 | 1231200 | 2430000 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 1231200 |
| 21 | 2026 | 5 | 10 | F571178 | 900017 | CLIENTE 017 | 1402724 | 1402724 | 874040 | 1178760 | 2052800 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 1178760 |
| 22 | 2026 | 5 | 10 | F571179 | 900012 | CLIENTE 012 | 570450 | 570450 | 60330 | 479370 | 539700 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 479370 |
| 23 | 2026 | 5 | 10 | F571180 | 900018 | CLIENTE 018 | 409693 | 409693 | 207120 | 344280 | 551400 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 344280 |
| 24 | 2026 | 5 | 10 | F571181 | 900009 | CLIENTE 009 | 1805974 | 1805974 | 248675 | 1517625 | 1766300 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 1517625 |
| 25 | 2026 | 5 | 10 | F571182 | 900019 | CLIENTE 019 | 667447 | 667447 | 490320 | 560880 | 1051200 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 560880 |
| 26 | 2026 | 5 | 10 | F571183 | 900020 | CLIENTE 020 | 325584 | 325584 | 266400 | 273600 | 540000 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 273600 |
| 27 | 2026 | 5 | 10 | F571261 | 900021 | CLIENTE 021 | 976752 | 976752 | 799200 | 820800 | 1620000 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 820800 |
| 28 | 2026 | 5 | 10 | F571262 | 900022 | CLIENTE 022 | 895356 | 895356 | 732600 | 752400 | 1485000 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 752400 |
| 29 | 2026 | 5 | 10 | F571263 | 900022 | CLIENTE 022 | 667447 | 667447 | 490320 | 560880 | 1051200 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 560880 |
| 30 | 2026 | 5 | 10 | F571264 | 900023 | CLIENTE 023 | 7686496 | 7686496 | 1835160 | 6459240 | 8294400 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 6459240 |
| 31 | 2026 | 5 | 10 | F571270 | 900024 | CLIENTE 024 | 1693376 | 1693376 | 1149595 | 1423005 | 2572600 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 1423005 |
| 32 | 2026 | 5 | 10 | F571286 | 900025 | CLIENTE 025 | 1130262 | 1130262 | 756000 | 949800 | 1705800 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 949800 |
| 33 | 2026 | 5 | 10 | F571290 | 900023 | CLIENTE 023 | 4512052 | 4512052 | 199560 | 3791640 | 3991200 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 3791640 |
| 34 | 2026 | 5 | 10 | F571291 | 900026 | CLIENTE 026 | 617705 | 617705 | 62520 | 519080 | 581600 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 519080 |
| 35 | 2026 | 5 | 10 | F571361 | 900027 | CLIENTE 027 | 333724 | 333724 | 245160 | 280440 | 525600 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 280440 |
| 36 | 2026 | 5 | 10 | F571362 | 900028 | CLIENTE 028 | 2791883 | 2791883 | 2137680 | 2346120 | 4483800 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 2346120 |
| 37 | 2026 | 5 | 10 | F571367 | 900029 | CLIENTE 029 | 451962 | 451962 | 17600 | 379800 | 397400 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 379800 |
| 38 | 2026 | 5 | 10 | F571369 | 900029 | CLIENTE 029 | 771120 | 771120 | 567000 | 648000 | 1215000 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 648000 |
| 39 | 2026 | 5 | 10 | F571392 | 900030 | CLIENTE 030 | 1002867 | 1002867 | 669955 | 842745 | 1512700 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 842745 |
| 40 | 2026 | 5 | 10 | F571393 | 900031 | CLIENTE 031 | 1465128 | 1465128 | 1198800 | 1231200 | 2430000 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 1231200 |
| 41 | 2026 | 5 | 10 | F571396 | 900031 | CLIENTE 031 | 1686254 | 1686254 | 1144980 | 1417020 | 2562000 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 1417020 |
| 42 | 2026 | 5 | 10 | F571397 | 900032 | CLIENTE 032 | 2181413 | 2181413 | 1718280 | 1833120 | 3551400 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 1833120 |
| 43 | 2026 | 5 | 10 | F571413 | 900028 | CLIENTE 028 | 2705060 | 2705060 | 1398340 | 2273160 | 3671500 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 2273160 |
| 44 | 2026 | 5 | 10 | F571414 | 900033 | CLIENTE 033 | 2192266 | 2192266 | 1537960 | 1842240 | 3380200 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 1842240 |
| 45 | 2026 | 5 | 10 | F571415 | 900033 | CLIENTE 033 | 1370166 | 1370166 | 787000 | 1151400 | 1938400 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 1151400 |
| 46 | 2026 | 5 | 10 | F571548 | 900034 | CLIENTE 034 | 2827041 | 2827041 | 1794235 | 2375665 | 4169900 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 2375665 |
| 47 | 2026 | 5 | 10 | F571551 | 900035 | CLIENTE 035 | 1256212 | 1256212 | 764360 | 1055640 | 1820000 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 1055640 |
| 48 | 2026 | 5 | 10 | F571554 | 900036 | CLIENTE 036 | 1403064 | 1403064 | 1084455 | 1179045 | 2263500 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 1179045 |
| 49 | 2026 | 5 | 10 | F571555 | 900037 | CLIENTE 037 | 1419908 | 1419908 | 919200 | 1193200 | 2112400 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 1193200 |
| 50 | 2026 | 5 | 10 | F571566 | 900038 | CLIENTE 038 | 2303507 | 2303507 | 1905480 | 1935720 | 3841200 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 1935720 |
| 51 | 2026 | 5 | 10 | F571568 | 900039 | CLIENTE 039 | 835380 | 835380 | 58500 | 702000 | 760500 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 702000 |
| 52 | 2026 | 5 | 10 | F571569 | 900040 | CLIENTE 040 | 1343034 | 1343034 | 1098900 | 1128600 | 2227500 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 1128600 |
| 53 | 2026 | 5 | 10 | F571570 | 900038 | CLIENTE 038 | 1066288 | 1066288 | 844560 | 896040 | 1740600 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 896040 |
| 54 | 2026 | 5 | 10 | F571571 | 900040 | CLIENTE 040 | 1340999 | 1340999 | 724310 | 1126890 | 1851200 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 1126890 |
| 55 | 2026 | 5 | 10 | F571572 | 900041 | CLIENTE 041 | 3339949 | 3339949 | 2599320 | 2806680 | 5406000 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 2806680 |
| 56 | 2026 | 5 | 10 | F571578 | 900042 | CLIENTE 042 | 2781369 | 2781369 | 1792215 | 2337285 | 4129500 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 2337285 |
| 57 | 2026 | 5 | 10 | F571664 | 900043 | CLIENTE 043 | 2699634 | 2699634 | 1808800 | 2268600 | 4077400 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 2268600 |
| 58 | 2026 | 5 | 10 | F571665 | 900044 | CLIENTE 044 | 2051179 | 2051179 | 1969920 | 1723680 | 3693600 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 1723680 |
| 59 | 2026 | 5 | 10 | F571666 | 900044 | CLIENTE 044 | 948603 | 948603 | 41955 | 797145 | 839100 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 797145 |
| 60 | 2026 | 5 | 10 | F571667 | 900044 | CLIENTE 044 | 3418632 | 3418632 | 2797200 | 2872800 | 5670000 | 401 | VENDEDOR 401 | 0 | 0 | 4 | ANTIOQUIA | 2872800 |

> **Hoja larga:** arriba se muestran 60 de 465 filas con datos. **Todos los valores de la hoja están en [`pronostico-expo-simple-ppco-datos/MAY-JUN-JUL.csv`](./pronostico-expo-simple-ppco-datos/MAY-JUN-JUL.csv)** (CSV, UTF-8).

### Hoja `PRONOSTICO SES` — 26 filas × 8 columnas · 1 gráfico(s)

**Gráficos en esta hoja:**

- Gráfico de líneas — título «(sin título)»
  - Series: 'PRONOSTICO SES'!$B$3: y = `'PRONOSTICO SES'!$B$4:$B$10`; 'PRONOSTICO SES'!$C$3: y = `'PRONOSTICO SES'!$C$4:$C$11`

| Fila | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| 3 | Mes | Ventas reales A(t) | Pronóstico F(t) | Error absoluto | SSE (error²) | Error % absoluto (APE) |  |  |
| 4 | Enero | 95752306 | 95752306 | 0 | 0 | 0 | Alpha (α): | 0.05 |
| 5 | Febrero | 153850391 | 95752306 | 58098085 | 3375387480667225 | 0.377627 |  |  |
| 6 | Marzo | 201004440 | 9.86572e+07 | 1.02347e+08 | 1.0475e+16 | 0.509179 |  |  |
| 7 | Abril | 52446770 | 1.03775e+08 | 5.13278e+07 | 2.63454e+15 | 0.978665 |  |  |
| 8 | Mayo | 197484330 | 1.01208e+08 | 9.62761e+07 | 9269096740990864 | 0.487513 |  |  |
| 9 | Junio | 156580280 | 1.06022e+08 | 5.05583e+07 | 2.55614e+15 | 0.322891 |  |  |
| 10 | Julio | 230979600 | 1.0855e+08 | 1.2243e+08 | 1.4989e+16 | 0.530045 |  |  |
| 11 | AGOSTO (PRONÓSTICO) |  | 1.14671e+08 |  |  |  |  |  |
| 13 |  | MAD | SSE | MSE | MAPE |  |  |  |
| 14 |  | 8.01729e+07 | 4.32992e+16 | 7216525704886031 | 0.53432 |  |  |  |

**Fórmulas (16 patrones distintos):**

- `B4`: `=UNIFICADO!F$2`
- `C4`: `=B4`
- `D4`: `=ABS(B4-C4)`
- `E4`: `=D4^2`
- `F4`: `=D4/B4`
- `B5`: `=UNIFICADO!G$2`
- `C5`: `=$H$4*B4+(1-$H$4)*C4`
- `B6`: `=UNIFICADO!H$2`
- `B7`: `=UNIFICADO!I$2`
- `B8`: `=UNIFICADO!J$2`
- `B9`: `=UNIFICADO!K$2`
- `B10`: `=UNIFICADO!L$2`
- `B14`: `=AVERAGE(D5:D10)`
- `C14`: `=SUM(E5:E10)`
- `D14`: `=AVERAGE(E5:E10)`
- `E14`: `=AVERAGE(F5:F10)`

