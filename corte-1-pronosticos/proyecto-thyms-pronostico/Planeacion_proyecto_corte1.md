# Planeacion_proyecto_corte1

> **Archivo:** [`Planeacion_proyecto_corte1.ipynb`](./Planeacion_proyecto_corte1.ipynb) · **Corte 1** · Cuaderno Jupyter con 34 celdas  
> **Nombre original:** `CORTE 1/PROYECTO/Planeacion_proyecto_corte1.ipynb`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

### Qué es

Cuaderno de Google Colab del **proyecto del Corte 1** sobre THYMS Colombia S.A.S. (tintes para el cabello en tubo de 60 g). Usa las 464 facturas de mayo a julio de 2026 de un vendedor de la zona Antioquia ([`VENTAS.md`](./VENTAS.md), hoja `MAY-JUN-JUL`) para:
1. explorar los datos con histograma, gráfico de retardo, boxplot, autocorrelograma y serie de tiempo;
2. pasar las ventas de pesos a tubos y calcular **takt time**, **throughput** y **WIP** (ley de Little).

El pronóstico de suavización exponencial simple del proyecto **no está en este cuaderno**: está en los Excel [`pronostico-expo-simple.md`](./pronostico-expo-simple.md) y [`pronostico-expo-simple-ppco.md`](./pronostico-expo-simple-ppco.md).

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

- `VENTAS.xls`, hoja `MAY-JUN-JUL`: 464 facturas (165 en mayo, 135 en junio, 164 en julio), columna `subdoc` = subtotal neto en COP (después de descuento y antes de IVA). Descripción completa en [`VENTAS.md`](./VENTAS.md).
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
- **Días hábiles de julio:** el cuaderno resta 2 festivos en julio de 2026. Según el calendario de festivos de Colombia que usa el gemelo del Corte 2 (celda 18 de [`Gemelo_Digital_Thyms.md`](../../corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md)), julio de 2026 solo tiene el 20 de julio. Con un festivo serían 24 días, 67 en total, y el takt quedaría en ~0,70 min/tubo.
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

