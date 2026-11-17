<!-- fuente: corte-1-pronosticos/proyecto-thyms-pronostico/README.md -->
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

Esta entrega es el punto de partida del [proyecto del Corte 2](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/) (S&OP y gemelo digital).

### Enunciado o entregable (deducido de los archivos)

No hay enunciado escrito en la carpeta. Por lo que contienen los archivos, se pidió:
1. análisis descriptivo y gráfico de las ventas reales (histograma, dispersión, boxplot, autocorrelograma, serie de tiempo);
2. elegir y aplicar un método de pronóstico con sus medidas de error (MAD, MSE, MAPE);
3. estudio preliminar del sistema: takt time, throughput y WIP, con la ley de Little.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [`VENTAS.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/VENTAS.md) | Datos de la empresa: ventas mensuales en COP de enero a agosto de 2026 (`UNIFICADO`) y 464 facturas de mayo a julio (`MAY-JUN-JUL`), anonimizadas | Sí (1.º) |
| [`Planeacion_proyecto_corte1.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/Planeacion_proyecto_corte1.md) | Cuaderno de Colab: gráficas exploratorias de las facturas, paso a unidades (12.900 COP/tubo), takt time, throughput y WIP | Sí (2.º) |
| [`pronostico-expo-simple-ppco.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple-ppco.md) | Excel con el pronóstico SES ($\alpha$ = 0,05) de enero a julio y el pronóstico de agosto; **versión corregida y final** | Sí (3.º) |
| [`pronostico-expo-simple.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple.md) | Primera versión del mismo Excel; MAD y MAPE mal promediados (incluyen enero, con error 0) | Solo para comparar |

**Diferencia entre los dos Excel de SES:**
- Datos, $\alpha$, pronósticos, SSE y MSE: idénticos.
- La primera versión promedia el MAD y el MAPE de enero a julio (`AVERAGE(D4:D10)`, `AVERAGE(F4:F10)`), incluyendo el error 0 de enero, y obtiene **68,7 millones y 45,8 %**.
- La versión PPCO los promedia de febrero a julio, igual que el SSE y el MSE, y obtiene **80,2 millones y 53,4 %**.
- La PPCO también corrige los títulos de las columnas («Error absoluto» y «Error % absoluto (APE)» en lugar de «MAD» y «MAPE») y cambia el orden de las hojas.

## Orden de estudio sugerido

1. [`VENTAS.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/VENTAS.md): qué datos hay y qué significa cada columna.
2. [`pronostico-expo-simple-ppco.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple-ppco.md): el pronóstico y sus errores.
3. [`Planeacion_proyecto_corte1.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/Planeacion_proyecto_corte1.md): gráficas y métricas del sistema.
4. La revisión crítica de este pronóstico en el Corte 2: sección 2.1 de [`Gemelo_Digital_Thyms.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md).

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

- Suavización exponencial simple: $F_{t+1} = \alpha A_t + (1-\alpha)F_t$; un $\alpha$ pequeño hace el pronóstico casi plano y muy dependiente del arranque. Detalle en [`pronostico-expo-simple-ppco.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple-ppco.md).
- Sesgo y señal de rastreo ($e_t = A_t - F_t$): $\text{sesgo} = \frac{1}{n}\sum e_t$ y $TS = \sum e_t / MAD$. Aquí dan +63,1 M COP y 4,72 (calculados en el Corte 2).
- Takt time, throughput y ley de Little: ver [`Planeacion_proyecto_corte1.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/Planeacion_proyecto_corte1.md) y la clase [L02](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L02-introduction-to-production-systems.md).

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado principal |
|---|---|---|
| SES con $\alpha$ = 0,05 sobre 7 meses | [`pronostico-expo-simple-ppco.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple-ppco.md) | Agosto = 114,7 M COP; MAPE 53,4 % |
| Mismo SES con el error mal promediado | [`pronostico-expo-simple.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple.md) | MAD 68,7 M y MAPE 45,8 % (subestimados) |
| Exploración de 464 facturas | [`Planeacion_proyecto_corte1.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/Planeacion_proyecto_corte1.md) | Distribución sesgada a la derecha, $r_1$ ≈ 0,29 |
| Takt, throughput y WIP | [`Planeacion_proyecto_corte1.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/Planeacion_proyecto_corte1.md) | 0,69 min/tubo; 86,74 tubos/h; 304–477 tubos |

## Supuestos abiertos y advertencias

- **Escala zona → planta:** los datos son de un solo vendedor. En el Corte 2 se calcula que esta serie (~11.705 tubos/mes) es el **11,7 %** de la demanda de la planta (100.000 tubos/mes), y se escala por 8,54. Falta confirmarlo con la empresa.
- **Jornada:** aquí se supone 1 turno de 8 h de lunes a sábado; el libro del Corte 2 usa 2 turnos de 7 h de lunes a viernes.
- **Precio único** de 12.900 COP/tubo para los tres productos, aunque los descuentos de las facturas promedian el 40 % del valor bruto.
- **$\alpha$ = 0,05 sin justificación escrita**: es el que minimiza el MAPE, pero no el MAD ni el MSE. El arranque $F_1 = A_1$ (enero, mes bajo) sesga el pronóstico hacia abajo.
- **Julio de 2026:** el cuaderno resta 2 festivos, pero con el calendario oficial solo hay uno (20 de julio); serían 24 días hábiles y no 23.
- Error de impresión en la celda 21 del cuaderno (muestra 45.798 como «demanda diaria»; el valor usado es 694).
- Solo 8 meses de datos: no se puede validar estacionalidad.

## Cómo se conecta con el Corte 2

El [proyecto del Corte 2](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/) parte de estos archivos:

1. **Mismos datos.** El libro [`Datos Thyms Completo.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Datos%20Thyms%20Completo.md) copia las ventas mensuales (hoja `Ventas`) y las 464 facturas (hoja `Facturas Mayo-Julio`), y calcula los índices estacionales con ellas (julio 1,53; abril 0,35).
2. **Revisión del pronóstico.** La sección 2.1 del gemelo reproduce este SES (MAD 80,2 M, MAPE 53,4 %) y muestra que está **sesgado**: sesgo +63,1 M COP y señal de rastreo 4,72. Agosto: 114,7 M pronosticado frente a 119,9 M real.
3. **Corrección.** Con origen móvil se comparan 7 métodos y gana el mismo SES con $\alpha$ = 0,05 pero con **nivel inicial = promedio de los 3 primeros meses**: sesgo 44,6 M → 2,4 M y RMSE 76,8 M → 63,6 M (−17 %). El nivel resultante, 151,06 M COP/mes, se convierte en **100.038 tubos/mes de planta** con los mismos 12.900 COP/tubo y la escala de 8,54.
4. **Métricas.** El takt (41,5 s), el throughput (86,7 tubos/h) y el WIP (304–477 tubos) de este cuaderno se comparan en la sección 3.5 del gemelo con los del libro (11,1 s; 325 tubos/h; 8.500 tubos) y los del gemelo (10,3 s; 352 tubos/h; 5.308 tubos). No son comparables en magnitud porque aquí se mide la zona con jornada de 8 h.
5. **Tamaño de pedido.** Las 464 facturas alimentan la distribución lognormal del tamaño de pedido del gemelo: 1.273.304 COP ≈ 99 tubos por pedido.

## Relación con otros temas y proyectos

- Teoría: [L03](/corte-1-pronosticos/02-introduccion-a-pronosticos/L03-introduction-to-forecasting.md), [L04](/corte-1-pronosticos/03-graficas-y-autocorrelacion/L04-plotting-your-data.md), [L05](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md) (SES y errores) y [L07](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md) (señal de rastreo y estacionalidad).
- Mismo tipo de análisis con datos de clase: [parcial-1](/corte-1-pronosticos/parcial-1/).
- Continuación: [proyecto-thyms-gemelo-digital](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/), con el documento de traspaso [`CONTEXTO_GEMELO_THYMS.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/CONTEXTO_GEMELO_THYMS.md).


---

<!-- fuente: corte-1-pronosticos/proyecto-thyms-pronostico/Planeacion_proyecto_corte1.md -->
# Planeacion_proyecto_corte1

> **Archivo:** [`Planeacion_proyecto_corte1.ipynb`](/corte-1-pronosticos/proyecto-thyms-pronostico/Planeacion_proyecto_corte1.ipynb) · **Corte 1** · Cuaderno Jupyter con 34 celdas  
> **Nombre original:** `CORTE 1/PROYECTO/Planeacion_proyecto_corte1.ipynb`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

### Qué es

Cuaderno de Google Colab del **proyecto del Corte 1** sobre THYMS Colombia S.A.S. (tintes para el cabello en tubo de 60 g). Usa las 464 facturas de mayo a julio de 2026 de un vendedor de la zona Antioquia ([`VENTAS.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/VENTAS.md), hoja `MAY-JUN-JUL`) para:
1. explorar los datos con histograma, gráfico de retardo, boxplot, autocorrelograma y serie de tiempo;
2. pasar las ventas de pesos a tubos y calcular **takt time**, **throughput** y **WIP** (ley de Little).

El pronóstico de suavización exponencial simple del proyecto **no está en este cuaderno**: está en los Excel [`pronostico-expo-simple.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple.md) y [`pronostico-expo-simple-ppco.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple-ppco.md).

### Estructura

| Celdas | Sección | Qué hace |
|---|---|---|
| 0 | Librerías | seaborn, matplotlib, pandas, numpy y `plot_acf` de statsmodels |
| 1–2 | Carga | Sube `VENTAS.xls` a Colab (`files.upload()`) y lee la segunda hoja (`sheet_name=1`, `MAY-JUN-JUL`) |
| 3–4 | Revisión | `df.head()` (primeras 5 facturas) y conteo de vacíos en `subdoc`: 0 |
| 5–6 | Histograma | Histograma con curva de densidad de `subdoc` (COP por factura) |
| 7–8 | Gráfico de retardo | $x_t$ frente a $x_{t-1}$ (factura actual frente a la anterior) |
| 9–10 | Boxplot | Boxplot de `subdoc` |
| 11–12 | Autocorrelograma | ACF de `subdoc` con 20 rezagos y bandas de confianza |
| 13–14 | Serie de tiempo | `subdoc` en el orden de las facturas (índice 0 a 463) |
| 15–17 | Takt time, paso 1 | Demanda en unidades: `Demanda_unitaria = round(subdoc / 12900)` |
| 18–21 | Demanda diaria | Días hábiles reales de mayo, junio y julio; demanda total y diaria |
| 22–23 | Takt time, paso 2 | Tiempo disponible = 8 h = 480 min por jornada |
| 24–25 | Takt time, paso 3 | Takt = tiempo disponible / demanda diaria |
| 26–29 | Throughput | Unidades / tiempo total disponible del trimestre |
| 30–33 | WIP | Ley de Little con el tiempo de ciclo que dio la empresa (3,5 a 5,5 h) |

### Datos que usa

- `VENTAS.xls`, hoja `MAY-JUN-JUL`: 464 facturas (165 en mayo, 135 en junio, 164 en julio), columna `subdoc` = subtotal neto en COP (después de descuento y antes de IVA). Descripción completa en [`VENTAS.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/VENTAS.md).
- Precio supuesto: **12.900 COP por tubo** (para pasar de pesos a unidades).
- Datos de la empresa citados en el texto: 2 días de parada programada al mes; descansos escalonados que no detienen la planta; tiempo de ciclo de un tubo de 3,5 a 5,5 h.

### Métodos

- **Conversión a unidades:** $u_i = \mathrm{round}(\text{subdoc}_i / 12.900)$ por factura $i$.
- **Días hábiles reales:** días del mes − domingos − 2 días de parada − festivos de Colombia 2026:
  - mayo: 31 − 5 − 2 − 2 = 22;
  - junio: 30 − 4 − 2 − 3 = 21;
  - julio: 31 − 4 − 2 − 2 = 23;
  - total: 66 días (se trabaja de lunes a sábado).
- **Demanda diaria:** $\bar{d} = \sum u_i / \sum \text{días hábiles} = 45.798 / 66 \approx 694$ tubos/día.
- **Takt time:** $T_{takt} = \dfrac{T_{disponible}}{\bar{d}} = \dfrac{480 \text{ min}}{694 \text{ tubos}}$.
- **Throughput:** $TH = \dfrac{\text{unidades}}{\text{tiempo total}}$, con tiempo total $= (480/60)\cdot 66 = 528$ h.
- **WIP (ley de Little):** $WIP = TH \times CT$, donde $CT$ = tiempo de ciclo (3,5 a 5,5 h).

### Resultados clave con números

| Indicador | Valor |
|---|---|
| Facturas | 464, sin vacíos en `subdoc` |
| Demanda del trimestre (may–jul) | 45.798 tubos (mayo 15.365; junio 12.379; julio 18.054, recalculado con la misma regla) |
| Días hábiles | 22 + 21 + 23 = 66 |
| Demanda diaria promedio | 694 tubos/día |
| Takt time | 0,69 min/tubo (≈ 41,5 s/tubo) |
| Tiempo total disponible | 528 h |
| Throughput | 86,74 tubos/h |
| WIP | 303,59 tubos (CT = 3,5 h) a 477,06 tubos (CT = 5,5 h) |

**Gráficos** (marcados como `[gráfico]` abajo):
- **Histograma:** muy sesgado a la derecha. La mayoría de las facturas está por debajo de 2 millones de COP, con un pico de ~78 facturas cerca de 0,8 millones y una cola hasta 11,3 millones.
- **Gráfico de retardo:** nube concentrada cerca del origen, sin una recta clara; unos pocos pedidos grandes quedan aislados.
- **Boxplot:** mediana ~1,02 millones, caja de ~0,63 a ~1,55 millones y muchos atípicos por encima de ~2,9 millones (21 facturas, el mayor de 11,34 millones).
- **Autocorrelograma:** $r_1$ ≈ 0,29 fuera de la banda (±0,09); los demás rezagos están dentro o rozan la banda.
- **Serie de tiempo:** valores de factura en orden de emisión, en general bajo 3 millones, con picos de hasta ~11,3 millones (facturas grandes de un mismo cliente, cerca de la factura 350 y de la 435).

### Conclusiones

El cuaderno termina con: «El nivel de inventario en proceso (WIP) para la línea de tubos de tinte se sitúa entre 303.59 y 477.06 unidades, en función del tiempo de ciclo real de cada unidad dentro del rango de 3.5 a 5.5 horas.» El takt de 0,69 min/tubo y el throughput de 86,7 tubos/h describen el ritmo que exige la demanda **de esta zona**, no de la planta completa.

### Supuestos y advertencias

- **Error de impresión (celda 21):** el mensaje dice «La demanda diaria promedio es:45798.0 unidades», pero imprime `Dem_hist` (la demanda del trimestre). El valor diario correcto, `Dem_diaria_prom`, es 694, y es el que se usa en el takt.
- **Días hábiles de julio:** el cuaderno resta 2 festivos en julio de 2026. Según el calendario de festivos de Colombia que usa el gemelo del Corte 2 (celda 18 de [`Gemelo_Digital_Thyms.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md)), julio de 2026 solo tiene el 20 de julio. Con un festivo serían 24 días, 67 en total, y el takt quedaría en ~0,70 min/tubo.
- **Escala:** son las ventas de **un solo vendedor (401) de una zona**. En el Corte 2 se calcula que la venta promedio de esta serie (~11.705 tubos/mes) es solo el 11,7 % de la demanda de la planta (100.000 tubos/mes).
- **Jornada:** 1 turno de 8 h de lunes a sábado. El libro de datos del Corte 2 usa 2 turnos de 7 h de lunes a viernes.
- **Throughput = demanda:** se supone que se produjo exactamente lo vendido (no hay datos de producción).
- **Precio único** de 12.900 COP/tubo para los tres productos y para todos los clientes, aunque los descuentos de las facturas varían.
- Las gráficas exploratorias se hacen sobre **facturas individuales en orden de emisión**, no sobre una serie mensual; la autocorrelación del rezago 1 refleja facturas seguidas del mismo cliente más que un patrón de demanda en el tiempo.
- Depende de Colab (`google.colab.files`); para correrlo en local hay que reemplazar la celda 1 por la ruta del archivo.

## Contenido del cuaderno

> Todas las celdas con su código y sus salidas de texto. Los gráficos (imágenes) se marcan como `[gráfico]`; el .ipynb conserva las imágenes.

<!-- celda 0 · código -->
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf
```

<!-- celda 1 · código -->
```python
from google.colab import files
uploaded = files.upload()
```

Salida:
```text
<IPython.core.display.HTML object>
Saving VENTAS.xls to VENTAS.xls
```

<!-- celda 2 · código -->
```python
df = pd.read_excel("VENTAS.xls",sheet_name=1)
```

<!-- celda 3 · código -->
```python
df.head()
```

Salida:
```text
ano_doc  per_doc  tip_doc  num_doc     cod_cli  \
0     2026        5       10  F571143    900001   
1     2026        5       10  F571144    900002   
2     2026        5       10  F571145    900003   
3     2026        5       10  F571146  900004   
4     2026        5       10  F571149    900005   

                                          nom_cli  valorfac  valordoc  \
0                      CLIENTE 001    307377    307377   
1                 CLIENTE 002   1319972   1319972   
2         CLIENTE 003    359856    359856   
3                         CLIENTE 004    652525    652525   
4  CLIENTE 005   2110870   2110870   

   valordes   subdoc   netdoc  codven                 nomven  devolu  notas  \
0    126000   258300   384300     401  VENDEDOR 401       0      0   
1   1063980  1109220  2173200     401  VENDEDOR 401       0      0   
2    270300   302400   572700     401  VENDEDOR 401       0      0   
3     97060   548340   645400     401  VENDEDOR 401       0      0   
4   1475760  1773840  3249600     401  VENDEDOR 401       0      0   

   codzona    nomzona    total  
0        4  ANTIOQUIA   258300  
1        4  ANTIOQUIA  1109220  
2        4  ANTIOQUIA   302400  
3        4  ANTIOQUIA   548340  
4        4  ANTIOQUIA  1773840
```

<!-- celda 4 · código -->
```python
x=df["subdoc"]
x.isna().sum()
```

Salida:
```text
np.int64(0)
```

<!-- celda 5 · markdown -->
**Histograma**

<!-- celda 6 · código -->
```python
plt.figure(figsize=(6, 4))
sns.histplot(x, kde=True, color="skyblue")
plt.title("Histograma")
plt.xlabel("x")
plt.ylabel("Frecuencia")
plt.show()
```

Salida:
```text
[gráfico]
```

<!-- celda 7 · markdown -->
**Scatterplot**

<!-- celda 8 · código -->
```python
x_lag1 = x.shift(1)

plt.figure(figsize=(6, 5))
sns.scatterplot(x=x_lag1, y=x, color="coral", alpha=0.7)

plt.title("Scatterplot de Retardo: $x_t$ vs $x_{t-1}$")
plt.xlabel("$x_{t-1}$ (Valor anterior)")
plt.ylabel("$x_t$ (Valor actual)")
plt.grid(True, linestyle="--", alpha=0.5)

plt.show()
```

Salida:
```text
[gráfico]
```

<!-- celda 9 · markdown -->
**Boxplot**

<!-- celda 10 · código -->
```python
plt.figure(figsize=(6, 4))
sns.boxplot(y=x, color="lightgreen")
plt.title("Boxplot de ventas")
plt.ylabel("x")
plt.show()
```

Salida:
```text
[gráfico]
```

<!-- celda 11 · markdown -->
**Autocorrelograma**

<!-- celda 12 · código -->
```python
# Opción recomendada con bandas de confianza (statsmodels)
fig, ax = plt.subplots(figsize=(7, 4))
plot_acf(x, lags=20, ax=ax)
plt.title("Autocorrelograma (ACF)")
plt.xlabel("Lags")
plt.ylabel("Autocorrelación")
plt.show()
```

Salida:
```text
[gráfico]
```

<!-- celda 13 · markdown -->
**Serie de tiempo**

<!-- celda 14 · código -->
```python
plt.figure(figsize=(8, 4))
sns.lineplot(x=range(len(x)), y=x, color="purple", marker="o")
plt.title("Serie de Tiempo de ventas")
plt.xlabel("Tiempo / Período")
plt.ylabel("x")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()
```

Salida:
```text
[gráfico]
```

<!-- celda 15 · markdown -->
**Calculo de Takt time**

<!-- celda 16 · markdown -->
1. calcular la demanda en unidades debido a que se encuentra en valor monetario actualmente

<!-- celda 17 · código -->
```python
df["Demanda_unitaria"]=round(df["subdoc"]/12900,0)
```

<!-- celda 18 · markdown -->
**Calculo aproximado de la demanda diaria**

 El cálculo de la demanda diaria se realiza indexando los días hábiles reales mediante la siguiente fórmula:

$$\text{Demanda Diaria Promedio} = \frac{\sum \text{Demanda Histórica (May + Jun + Jul)}}{\sum \text{Días Hábiles Reales (May + Jun + Jul)}}$$

Donde los **Días Hábiles Reales** se calculan dinámicamente para cada mes restando del calendario:
* Los días de descanso dominical obligatorio (Artículo 171 del Código Sustantivo del Trabajo).
* Los días festivos oficiales de Colombia del año 2026.
* Los días de parada programada de planta (mantenimiento preventivo), en este caso 2 dias al mes según la información brindada por la empresa.

En este caso los días hábiles reales para los meses disponibles son:
* $\text{Dias_Disp_Mayo} = 31\ \text{Días_Calendario} \ - 5\ \text{Días_Descanso_Dominical}\ - 2\ \text{Días_Parada_Programada}\ - 2\ \text{Días_Festivos} = 22 \ \text{Días_Hábiles_Reales}$

* $\text{Dias_Disp_Junio} = 30\ \text{Días_Calendario} \ - 4\ \text{Días_Descanso_Dominical}\ - 2\ \text{Días_Parada_Programada}- 3\ \text{Días_Festivos} = 21 \ \text{Días_Hábiles_Reales}$

* $\text{Dias_Disp_Julio} = 31\ \text{Días_Calendario} \ - 4\ \text{Días_Descanso_Dominical}\ - 2\ \text{Días_Parada_Programada}- 2\ \text{Días_Festivos} = 23 \ \text{Días_Hábiles_Reales}$

<!-- celda 19 · código -->
```python
Dias_Disp_Mayo=22
Dias_Disp_Junio=21
Dias_Disp_Julio=23
total_dias_hab= Dias_Disp_Mayo+Dias_Disp_Junio+Dias_Disp_Julio
print(f"El número de días habiles reales en los tres meses es: {total_dias_hab} Días")
```

Salida:
```text
El número de días habiles reales en los tres meses es: 66 Días
```

<!-- celda 20 · código -->
```python
Dem_hist= df["Demanda_unitaria"].sum()
Dem_hist
```

Salida:
```text
np.float64(45798.0)
```

<!-- celda 21 · código -->
```python
Dem_diaria_prom = round(Dem_hist/total_dias_hab,0)
print(f"La demanda diaria promedio es:{Dem_hist} unidades")
```

Salida:
```text
La demanda diaria promedio es:45798.0 unidades
```

<!-- celda 22 · markdown -->
2. calcular el tiempo disponible.

**Justificación del tiempo disponible:** Se considera una jornada laboral de
8 horas diarias, equivalentes a 480 minutos de operación. Según la información brindada por la empresa,
 los descansos del personal se gestionan mediante horarios
escalonados, de manera que los trabajadores toman sus pausas en diferentes
momentos y se garantiza la continuidad de las actividades productivas. Por lo
tanto, los períodos de descanso del personal no representan una interrupción de
la operación de la planta y no se descuentan del tiempo disponible para la
producción.

En consecuencia, el tiempo disponible considerado para el cálculo del **Takt
Time** es:

$
T_{\text{disponible}} = 8 \text{ horas} = 480 \text{ minutos por jornada}.
$

<!-- celda 23 · código -->
```python
t_disponible=480
```

<!-- celda 24 · markdown -->
3.Calcular **Takt time** usando la formula $$Takt\  time\ =\frac{tiempo \ disponible}{demanda}$$

<!-- celda 25 · código -->
```python
takt_time = t_disponible/Dem_diaria_prom
print(f"El takt time calculado es: {round(takt_time,2)} minutos/unidad")
```

Salida:
```text
El takt time calculado es: 0.69 minutos/unidad
```

<!-- celda 26 · markdown -->
**Cálculo de Throughput**

<!-- celda 27 · markdown -->
El throughput mide la cantidad de unidades producidas por unidad de tiempo, usando la fórmula:

$$Throughput = \frac{Unidades\ producidas}{Tiempo\ total}$$

Las unidades producidas corresponden a la demanda histórica total del periodo (May + Jun + Jul), ya calculada como `Dem_hist`. El tiempo total corresponde al tiempo disponible de planta acumulado en los días hábiles reales del mismo periodo, expresado en horas:

$$Tiempo\ total = \left(\frac{t_{disponible}}{60}\right) \times total\_dias\_hab$$

Con $t_{disponible}=480$ minutos/día (8 horas) y $total\_dias\_hab=66$ días, el tiempo total disponible en el periodo es de 528 horas.

<!-- celda 28 · código -->
```python
t_disponible_horas = t_disponible/60
tiempo_total = t_disponible_horas*total_dias_hab
print(f"El tiempo total disponible en el periodo es: {tiempo_total} horas")
```

Salida:
```text
El tiempo total disponible en el periodo es: 528.0 horas
```

<!-- celda 29 · código -->
```python
throughput = Dem_hist/tiempo_total
print(f"El throughput calculado es: {round(throughput,2)} unidades/hora")
```

Salida:
```text
El throughput calculado es: 86.74 unidades/hora
```

<!-- celda 30 · markdown -->
**Cálculo de WIP (Work In Process)**

<!-- celda 31 · markdown -->
El WIP se calcula mediante:

$$WIP = Throughput \times Tiempo\ de\ ciclo$$

El tiempo de ciclo compartido por la empresa para un tubo de tinte es de 3.5 a 5.5 horas. Con este rango, el WIP se calcula en su valor mínimo y máximo, usando el throughput de 86.74 unidades/hora obtenido en el paso anterior.

<!-- celda 32 · código -->
```python
tiempo_ciclo_min = 3.5
tiempo_ciclo_max = 5.5

WIP_min = throughput*tiempo_ciclo_min
WIP_max = throughput*tiempo_ciclo_max

print(f"El WIP mínimo es: {round(WIP_min,2)} unidades")
print(f"El WIP máximo es: {round(WIP_max,2)} unidades")
```

Salida:
```text
El WIP mínimo es: 303.59 unidades
El WIP máximo es: 477.06 unidades
```

<!-- celda 33 · markdown -->
El nivel de inventario en proceso (WIP) para la línea de tubos de tinte se sitúa entre 303.59 y 477.06 unidades, en función del tiempo de ciclo real de cada unidad dentro del rango de 3.5 a 5.5 horas.



---

<!-- fuente: corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple-ppco.md -->
# pronostico-expo-simple-ppco

> **Archivo:** [`pronostico-expo-simple-ppco.xlsx`](/corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple-ppco.xlsx) · **Corte 1** · Libro de Excel con 3 hoja(s): `UNIFICADO`, `MAY-JUN-JUL`, `PRONOSTICO SES`  
> **Nombre original:** `CORTE 1/PROYECTO/PRONOSTICO EXPO SIMPLE PPCO.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Versión **corregida y final** del pronóstico del proyecto del Corte 1 (THYMS Colombia): suavización exponencial simple (SES) con $\alpha$ = 0,05 sobre las ventas mensuales en COP del vendedor 401 (zona Antioquia), de enero a julio de 2026, para pronosticar agosto. «PPCO» es, por deducción, la sigla del curso (Planeación, Programación y Control de la Producción); el parcial también se llamaba «PARCIAL 1 PPCO». Aplica la clase [L05](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md).

Comparte datos, fórmulas del pronóstico y resultados con [`pronostico-expo-simple.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple.md); la diferencia está en el MAD y el MAPE (ver «Diferencia con la primera versión» más abajo). Esta es la versión cuyas cifras (MAD 80,2 millones, MAPE 53,4 %) reproduce el Corte 2.

### Hojas `UNIFICADO` y `MAY-JUN-JUL`

Copias exactas de las hojas de [`VENTAS.xls`](/corte-1-pronosticos/proyecto-thyms-pronostico/VENTAS.md): ventas mensuales en COP de 2026 (enero a agosto) y las 464 facturas de mayo a julio. `MAY-JUN-JUL` no la usa ninguna fórmula.

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

| Aspecto | [`pronostico-expo-simple`](/corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple.md) | Esta versión (PPCO) |
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
- Todo está en COP de **una sola zona**; el paso a tubos de planta se hace en el Corte 2 ([`Gemelo_Digital_Thyms.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md)).
- La hoja `MAY-JUN-JUL` no se usa.


---

<!-- fuente: corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple.md -->
# pronostico-expo-simple

> **Archivo:** [`pronostico-expo-simple.xlsx`](/corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple.xlsx) · **Corte 1** · Libro de Excel con 3 hoja(s): `UNIFICADO`, `PRONOSTICO_SES`, `MAY-JUN-JUL`  
> **Nombre original:** `CORTE 1/PROYECTO/PRONOSTICO EXPO SIMPLE.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Primera versión del **pronóstico del proyecto del Corte 1** (THYMS Colombia): suavización exponencial simple (SES) sobre las ventas mensuales en COP del vendedor 401 (zona Antioquia), de enero a julio de 2026, para pronosticar agosto. Aplica la clase [L05](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md) y el Excel de clase [`promedio-movil-y-suavizacion-exponencial.md`](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/promedio-movil-y-suavizacion-exponencial.md).

Existe una versión corregida, [`pronostico-expo-simple-ppco.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple-ppco.md), con los mismos datos y pronósticos pero con el MAD y el MAPE calculados de forma consistente (ver «Diferencia con la versión PPCO» más abajo).

### Hojas `UNIFICADO` y `MAY-JUN-JUL`

Copias exactas de las hojas de [`VENTAS.xls`](/corte-1-pronosticos/proyecto-thyms-pronostico/VENTAS.md): ventas mensuales en COP de 2026 y las 464 facturas de mayo a julio. `MAY-JUN-JUL` no la usa ninguna fórmula.

### Hoja `PRONOSTICO_SES`

**Objetivo (deducido):** pronosticar las ventas de agosto de 2026 con SES y medir el error del método en los meses anteriores.

**Datos de entrada:** B4:B10 = `UNIFICADO!F2:L2` (enero a julio, en COP).

**Parámetros:** $\alpha$ = 0,05 (H4). Pronóstico inicial $F_1 = A_1$ (C4 = B4).

**Método paso a paso** ($A_t$ = venta real del mes $t$, $F_t$ = pronóstico del mes $t$):
- C5 a C11 (`=$H$4*B4+(1-$H$4)*C4`): $F_{t+1} = \alpha A_t + (1-\alpha) F_t$.
- D: error absoluto $|A_t - F_t|$ (columna titulada «MAD»).
- E: error al cuadrado $(A_t - F_t)^2$.
- F: error porcentual absoluto $|A_t - F_t|/A_t$ (columna titulada «MAPE»).
- Resumen (fila 14):
  - B14 = `AVERAGE(D4:D10)`: MAD de enero a julio, **incluye enero**, cuyo error es 0 por construcción;
  - C14 = `SUM(E5:E10)`: SSE de febrero a julio;
  - D14 = `AVERAGE(E5:E10)`: MSE de febrero a julio;
  - E14 = `AVERAGE(F4:F10)`: MAPE de enero a julio, **incluye enero**.

**Resultados:**

| Mes | Venta real $A_t$ (COP) | Pronóstico $F_t$ (COP) | Error absoluto | Error² | Error % |
|---|---|---|---|---|---|
| Enero | 95.752.306 | 95.752.306 | 0 | 0 | 0,0 % |
| Febrero | 153.850.391 | 95.752.306 | 58.098.085 | 3,375 × 10¹⁵ | 37,8 % |
| Marzo | 201.004.440 | 98.657.210 | 102.347.230 | 1,047 × 10¹⁶ | 50,9 % |
| Abril | 52.446.770 | 103.774.572 | 51.327.802 | 2,635 × 10¹⁵ | 97,9 % |
| Mayo | 197.484.330 | 101.208.182 | 96.276.148 | 9,269 × 10¹⁵ | 48,8 % |
| Junio | 156.580.280 | 106.021.989 | 50.558.291 | 2,556 × 10¹⁵ | 32,3 % |
| Julio | 230.979.600 | 108.549.904 | 122.429.696 | 1,499 × 10¹⁶ | 53,0 % |
| **Agosto (pronóstico)** | — | **114.671.388** | — | — | — |

| Medida | Valor | Meses que promedia |
|---|---|---|
| MAD | 68.719.607 COP | 7 (enero a julio) |
| SSE | 4,330 × 10¹⁶ | 6 (febrero a julio) |
| MSE | 7,217 × 10¹⁵ (RMSE ≈ 84,9 millones) | 6 (febrero a julio) |
| MAPE | 45,8 % | 7 (enero a julio) |

En unidades (con los 12.900 COP/tubo del cuaderno), el pronóstico de agosto equivale a unos 8.889 tubos para esta zona; el libro no hace esa conversión.

**Gráfico:** líneas sin título ni ejes rotulados; una serie con las ventas reales (B4:B10, 7 puntos) y otra con el pronóstico (C4:C11, 8 puntos incluido agosto). El pronóstico es casi plano, entre 96 y 115 millones, mientras las ventas saltan entre 52 y 231 millones.

**Conclusión:** con $\alpha$ = 0,05 el pronóstico apenas se mueve del valor de enero, que fue un mes bajo. Todos los pronósticos (95,8 a 114,7 millones) quedan por debajo del promedio real de enero a julio (155,4 millones), y el pronóstico solo supera a la venta real en abril.

### Diferencia con la versión PPCO

| Aspecto | Esta versión | [`pronostico-expo-simple-ppco`](/corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple-ppco.md) |
|---|---|---|
| Orden de las hojas | `UNIFICADO`, `PRONOSTICO_SES`, `MAY-JUN-JUL` | `UNIFICADO`, `MAY-JUN-JUL`, `PRONOSTICO SES` |
| Títulos de columnas | «Ventas reales A(t) ($)», «Pronóstico SES F(t) ($)», «MAD», «SSE (error²)», «MAPE» | «Ventas reales A(t)», «Pronóstico F(t)», «Error absoluto», «SSE (error²)», «Error % absoluto (APE)» |
| MAD | `AVERAGE(D4:D10)` = 68.719.607 (incluye enero) | `AVERAGE(D5:D10)` = 80.172.875 |
| MAPE | `AVERAGE(F4:F10)` = 45,8 % (incluye enero) | `AVERAGE(F5:F10)` = 53,4 % |
| SSE, MSE, pronósticos, α | Iguales | Iguales |

### Observaciones

- **Error de cálculo:** el MAD y el MAPE promedian 7 meses e incluyen enero, cuyo error es 0 porque $F_1 = A_1$. Eso subestima el error (68,7 millones y 45,8 % en lugar de 80,2 millones y 53,4 %) y es inconsistente con el SSE y el MSE, que sí empiezan en febrero. La versión PPCO lo corrige.
- Los títulos «MAD» y «MAPE» de las columnas D y F son en realidad el error absoluto y el error porcentual de cada mes.
- **α sin justificación en el libro:** no hay Solver ni tabla de búsqueda. Recalculado con el MAD y el MAPE de febrero a julio, $\alpha$ = 0,05 es el que da el menor MAPE (53,43 % frente a 53,59 % con 0,10). No minimiza el MAD (el mínimo está cerca de $\alpha$ = 0,5, con 69,2 millones) ni el MSE (cerca de $\alpha$ = 0,3).
- **Arranque sesgado:** $F_1 = A_1$ ancla el pronóstico en enero (95,8 millones, el segundo mes más bajo). El Corte 2 mide ese sesgo: +63,1 millones COP/mes y señal de rastreo de 4,72 (fuera de ±4). Ver [`Gemelo_Digital_Thyms.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md), sección 2.1.
- El dato real de agosto (119.882.540 COP) ya está en `UNIFICADO!M2`, pero el libro no lo usa para validar. Frente a él, el pronóstico falla por 5,2 millones (4,3 %).
- La hoja `MAY-JUN-JUL` no se usa en ningún cálculo.


---

<!-- fuente: corte-1-pronosticos/proyecto-thyms-pronostico/VENTAS.md -->
# VENTAS

> **Archivo:** [`VENTAS.xls`](/corte-1-pronosticos/proyecto-thyms-pronostico/VENTAS.xls) · **Corte 1** · Libro .xls con 2 hoja(s): `UNIFICADO`, `MAY-JUN-JUL`  
> **Nombre original:** `CORTE 1/PROYECTO/VENTAS.xls`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los datos

### Qué es

Datos reales de ventas de THYMS Colombia S.A.S. en 2026 que entregó la empresa para el proyecto: las ventas de **un vendedor (código 401, «VENDEDOR 401») de la zona 04, Antioquia**. Los clientes están anonimizados (CLIENTE ###, códigos 9#####). Es la fuente de todo el proyecto:
- el cuaderno [`Planeacion_proyecto_corte1.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/Planeacion_proyecto_corte1.md) lee la hoja `MAY-JUN-JUL`;
- los Excel de suavización exponencial ([`pronostico-expo-simple.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple.md) y [`pronostico-expo-simple-ppco.md`](/corte-1-pronosticos/proyecto-thyms-pronostico/pronostico-expo-simple-ppco.md)) traen copias de las dos hojas y pronostican con `UNIFICADO`;
- en el Corte 2, el libro [`Datos Thyms Completo.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Datos%20Thyms%20Completo.md) las copia en sus hojas `Ventas` y `Facturas Mayo-Julio`.

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

464 facturas (filas 2 a 465) y 18 columnas. Todas las filas en [`VENTAS-datos/MAY-JUN-JUL.csv`](/corte-1-pronosticos/proyecto-thyms-pronostico/VENTAS-datos/MAY-JUN-JUL.csv).

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
