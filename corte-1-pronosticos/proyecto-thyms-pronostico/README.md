# Proyecto THYMS, Corte 1: pronóstico de ventas y métricas del sistema (Corte 1)

## Qué cubre

Primera entrega del proyecto del semestre sobre **THYMS Colombia S.A.S.**, que fabrica tintes para el cabello en tubos de 60 g. La empresa tiene una familia de tres productos:
- A: Kolorezza permanente;
- B: Visalia sin amoníaco;
- C: Thym's Coloring permanente.

Con las ventas reales de 2026 de **un vendedor (401) de la zona Antioquia**, el grupo:
1. exploró los datos;
2. pronosticó las ventas mensuales con **suavización exponencial simple** ($\alpha$ = 0,05);
3. calculó **takt time, throughput y WIP** de la línea de tubos.

Esta entrega es el punto de partida del [proyecto del Corte 2](../../corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/) (S&OP y gemelo digital).

### Enunciado o entregable (deducido de los archivos)

No hay enunciado escrito en la carpeta. Por lo que contienen los archivos, se pidió:
1. análisis descriptivo y gráfico de las ventas reales (histograma, dispersión, boxplot, autocorrelograma, serie de tiempo);
2. elegir y aplicar un método de pronóstico con sus medidas de error (MAD, MSE, MAPE);
3. estudio preliminar del sistema: takt time, throughput y WIP, con la ley de Little.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [`VENTAS.md`](./VENTAS.md) | Datos de la empresa: ventas mensuales en COP de enero a agosto de 2026 (`UNIFICADO`) y 464 facturas de mayo a julio (`MAY-JUN-JUL`), anonimizadas | Sí (1.º) |
| [`Planeacion_proyecto_corte1.md`](./Planeacion_proyecto_corte1.md) | Cuaderno de Colab: gráficas exploratorias de las facturas, paso a unidades (12.900 COP/tubo), takt time, throughput y WIP | Sí (2.º) |
| [`pronostico-expo-simple-ppco.md`](./pronostico-expo-simple-ppco.md) | Excel con el pronóstico SES ($\alpha$ = 0,05) de enero a julio y el pronóstico de agosto; **versión corregida y final** | Sí (3.º) |
| [`pronostico-expo-simple.md`](./pronostico-expo-simple.md) | Primera versión del mismo Excel; MAD y MAPE mal promediados (incluyen enero, con error 0) | Solo para comparar |

**Diferencia entre los dos Excel de SES:**
- Datos, $\alpha$, pronósticos, SSE y MSE: idénticos.
- La primera versión promedia el MAD y el MAPE de enero a julio (`AVERAGE(D4:D10)`, `AVERAGE(F4:F10)`), incluyendo el error 0 de enero, y obtiene **68,7 millones y 45,8 %**.
- La versión PPCO los promedia de febrero a julio, igual que el SSE y el MSE, y obtiene **80,2 millones y 53,4 %**.
- La PPCO también corrige los títulos de las columnas («Error absoluto» y «Error % absoluto (APE)» en lugar de «MAD» y «MAPE») y cambia el orden de las hojas.

## Orden de estudio sugerido

1. [`VENTAS.md`](./VENTAS.md): qué datos hay y qué significa cada columna.
2. [`pronostico-expo-simple-ppco.md`](./pronostico-expo-simple-ppco.md): el pronóstico y sus errores.
3. [`Planeacion_proyecto_corte1.md`](./Planeacion_proyecto_corte1.md): gráficas y métricas del sistema.
4. La revisión crítica de este pronóstico en el Corte 2: sección 2.1 de [`Gemelo_Digital_Thyms.md`](../../corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md).

## Datos

| Fuente | Contenido | Cifras |
|---|---|---|
| `VENTAS.xls` → `UNIFICADO` | Ventas mensuales de 2026 en COP | Ene 95,8 M; Feb 153,9 M; Mar 201,0 M; Abr 52,4 M; May 197,5 M; Jun 156,6 M; Jul 231,0 M; Ago 119,9 M; promedio 151,0 M/mes |
| `VENTAS.xls` → `MAY-JUN-JUL` | 464 facturas, 161 clientes | `subdoc` total 590,8 M COP = 45.798 tubos (May 15.365; Jun 12.379; Jul 18.054) |

## Métodos

- **Pronóstico SES** ($A_t$ = venta real, $F_t$ = pronóstico): $F_{t+1} = \alpha A_t + (1-\alpha)F_t$, con $\alpha$ = 0,05 y $F_1 = A_1$.
- **Errores** ($n$ = 6, de febrero a julio): $MAD = \frac{1}{n}\sum|A_t - F_t|$, $MSE = \frac{1}{n}\sum(A_t-F_t)^2$, $MAPE = \frac{1}{n}\sum\frac{|A_t-F_t|}{A_t}$.
- **Conversión a unidades:** tubos = round(COP / 12.900).
- **Takt time:** $T_{takt} = T_{disponible}/\bar{d}$, con 480 min/día y $\bar{d}$ = demanda diaria.
- **Throughput:** $TH = \text{unidades}/\text{tiempo disponible}$.
- **Ley de Little:** $WIP = TH \times CT$, donde $CT$ = tiempo de ciclo.

## Resultados principales

| Resultado | Valor | Archivo |
|---|---|---|
| Pronóstico SES de agosto de 2026 | 114.671.388 COP (≈ 8.889 tubos de la zona) | `pronostico-expo-simple-ppco` |
| MAD / MAPE (feb–jul) | 80.172.875 COP / 53,4 % | `pronostico-expo-simple-ppco` |
| SSE / MSE | 4,33 × 10¹⁶ / 7,22 × 10¹⁵ (RMSE ≈ 84,9 M) | ambos Excel |
| Venta real de agosto (no usada para validar) | 119.882.540 COP (error de 4,3 %) | `UNIFICADO` |
| Días hábiles may–jul | 22 + 21 + 23 = 66 | cuaderno |
| Demanda diaria | 694 tubos/día | cuaderno |
| Takt time | 0,69 min/tubo ≈ 41,5 s | cuaderno |
| Throughput | 86,74 tubos/h (528 h disponibles) | cuaderno |
| WIP | 303,6 a 477,1 tubos (CT de 3,5 a 5,5 h) | cuaderno |

## Conceptos y fórmulas clave

- Suavización exponencial simple: $F_{t+1} = \alpha A_t + (1-\alpha)F_t$; un $\alpha$ pequeño hace el pronóstico casi plano y muy dependiente del arranque. Detalle en [`pronostico-expo-simple-ppco.md`](./pronostico-expo-simple-ppco.md).
- Sesgo y señal de rastreo ($e_t = A_t - F_t$): $\text{sesgo} = \frac{1}{n}\sum e_t$ y $TS = \sum e_t / MAD$. Aquí dan +63,1 M COP y 4,72 (calculados en el Corte 2).
- Takt time, throughput y ley de Little: ver [`Planeacion_proyecto_corte1.md`](./Planeacion_proyecto_corte1.md) y la clase [L02](../01-introduccion-curso-y-sistemas-de-produccion/L02-introduction-to-production-systems.md).

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado principal |
|---|---|---|
| SES con $\alpha$ = 0,05 sobre 7 meses | [`pronostico-expo-simple-ppco.md`](./pronostico-expo-simple-ppco.md) | Agosto = 114,7 M COP; MAPE 53,4 % |
| Mismo SES con el error mal promediado | [`pronostico-expo-simple.md`](./pronostico-expo-simple.md) | MAD 68,7 M y MAPE 45,8 % (subestimados) |
| Exploración de 464 facturas | [`Planeacion_proyecto_corte1.md`](./Planeacion_proyecto_corte1.md) | Distribución sesgada a la derecha, $r_1$ ≈ 0,29 |
| Takt, throughput y WIP | [`Planeacion_proyecto_corte1.md`](./Planeacion_proyecto_corte1.md) | 0,69 min/tubo; 86,74 tubos/h; 304–477 tubos |

## Supuestos abiertos y advertencias

- **Escala zona → planta:** los datos son de un solo vendedor. En el Corte 2 se calcula que esta serie (~11.705 tubos/mes) es el **11,7 %** de la demanda de la planta (100.000 tubos/mes), y se escala por 8,54. Falta confirmarlo con la empresa.
- **Jornada:** aquí se supone 1 turno de 8 h de lunes a sábado; el libro del Corte 2 usa 2 turnos de 7 h de lunes a viernes.
- **Precio único** de 12.900 COP/tubo para los tres productos, aunque los descuentos de las facturas promedian el 40 % del valor bruto.
- **$\alpha$ = 0,05 sin justificación escrita**: es el que minimiza el MAPE, pero no el MAD ni el MSE. El arranque $F_1 = A_1$ (enero, mes bajo) sesga el pronóstico hacia abajo.
- **Julio de 2026:** el cuaderno resta 2 festivos, pero con el calendario oficial solo hay uno (20 de julio); serían 24 días hábiles y no 23.
- Error de impresión en la celda 21 del cuaderno (muestra 45.798 como «demanda diaria»; el valor usado es 694).
- Solo 8 meses de datos: no se puede validar estacionalidad.

## Cómo se conecta con el Corte 2

El [proyecto del Corte 2](../../corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/) parte de estos archivos:

1. **Mismos datos.** El libro [`Datos Thyms Completo.md`](../../corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Datos%20Thyms%20Completo.md) copia las ventas mensuales (hoja `Ventas`) y las 464 facturas (hoja `Facturas Mayo-Julio`), y calcula los índices estacionales con ellas (julio 1,53; abril 0,35).
2. **Revisión del pronóstico.** La sección 2.1 del gemelo reproduce este SES (MAD 80,2 M, MAPE 53,4 %) y muestra que está **sesgado**: sesgo +63,1 M COP y señal de rastreo 4,72. Agosto: 114,7 M pronosticado frente a 119,9 M real.
3. **Corrección.** Con origen móvil se comparan 7 métodos y gana el mismo SES con $\alpha$ = 0,05 pero con **nivel inicial = promedio de los 3 primeros meses**: sesgo 44,6 M → 2,4 M y RMSE 76,8 M → 63,6 M (−17 %). El nivel resultante, 151,06 M COP/mes, se convierte en **100.038 tubos/mes de planta** con los mismos 12.900 COP/tubo y la escala de 8,54.
4. **Métricas.** El takt (41,5 s), el throughput (86,7 tubos/h) y el WIP (304–477 tubos) de este cuaderno se comparan en la sección 3.5 del gemelo con los del libro (11,1 s; 325 tubos/h; 8.500 tubos) y los del gemelo (10,3 s; 352 tubos/h; 5.308 tubos). No son comparables en magnitud porque aquí se mide la zona con jornada de 8 h.
5. **Tamaño de pedido.** Las 464 facturas alimentan la distribución lognormal del tamaño de pedido del gemelo: 1.273.304 COP ≈ 99 tubos por pedido.

## Relación con otros temas y proyectos

- Teoría: [L03](../02-introduccion-a-pronosticos/L03-introduction-to-forecasting.md), [L04](../03-graficas-y-autocorrelacion/L04-plotting-your-data.md), [L05](../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md) (SES y errores) y [L07](../06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md) (señal de rastreo y estacionalidad).
- Mismo tipo de análisis con datos de clase: [parcial-1](../parcial-1/).
- Continuación: [proyecto-thyms-gemelo-digital](../../corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/), con el documento de traspaso [`CONTEXTO_GEMELO_THYMS.md`](../../corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/CONTEXTO_GEMELO_THYMS.md).
