# Corte 1: Introducción y pronósticos de demanda

Primer corte del curso (30 % de la nota final). Empieza con la presentación del curso y los sistemas de producción. Luego cubre los **métodos de pronóstico**: primero graficar y diagnosticar la serie (autocorrelación), después elegir un método según el patrón de la serie y, por último, medir el error.

```
¿Qué patrón tiene la serie?  (graficar, correlograma, Ljung-Box)
 ├─ estacionaria / aleatoria → promedio móvil, promedio ponderado, SES
 ├─ con tendencia            → Holt (suavización doble), regresión
 ├─ con estacionalidad       → Winters (multiplicativo / aditivo)
 ├─ estructura autorregresiva → ARIMA (Box-Jenkins)
 └─ sin datos históricos     → métodos cualitativos (Delphi, jurado, fuerza de ventas)
Control del pronóstico: MAD, MSE, MAPE, señal de rastreo
```

## Temas (en orden de clase)

| # | Carpeta | Clase | Qué cubre | Ejercicios en la carpeta |
|---|---|---|---|---|
| 01 | [`01-introduccion-curso-y-sistemas-de-produccion/`](01-introduccion-curso-y-sistemas-de-produccion/README.md) | [L01](01-introduccion-curso-y-sistemas-de-produccion/L01-introduccion-al-curso.md), [L02](01-introduccion-curso-y-sistemas-de-produccion/L02-introduction-to-production-systems.md) | **Programa del curso, evaluación y reglas**; qué es Operations Management; flow shop, job shop y open shop; WIP, takt, throughput; push/pull, Kanban, ConWIP | Tarea 1: ensayo sobre ofertas de LinkedIn |
| 02 | [`02-introduccion-a-pronosticos/`](02-introduccion-a-pronosticos/README.md) | [L03](02-introduccion-a-pronosticos/L03-introduction-to-forecasting.md) | Tipos y horizontes de pronóstico, etapas, clasificación de métodos, patrones de demanda | — |
| 03 | [`03-graficas-y-autocorrelacion/`](03-graficas-y-autocorrelacion/README.md) | [L04](03-graficas-y-autocorrelacion/L04-plotting-your-data.md) | Correlograma (ACF) y límites de significancia, **Ljung-Box**, histograma, boxplot, dispersión, PCA | Excel de 30.000 ventas con rezagos y 4 tareas "Class example" (aleatoria, tendencia, estacionalidad de periodo 2) |
| 04 | [`04-datos-estacionarios-promedio-movil-y-suavizacion-simple/`](04-datos-estacionarios-promedio-movil-y-suavizacion-simple/README.md) | [L05](04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md) | **Promedio móvil**, promedio ponderado, **SES** y medidas de error (MAD, SSE, MSE, MAPE, PME) | Comparación PM(6)/PM(12)/SES(0,2)/SES(0,8) y la práctica del parcial 1 |
| 05 | [`05-tendencia-suavizacion-doble-holt/`](05-tendencia-suavizacion-doble-holt/README.md) | [L06](05-tendencia-suavizacion-doble-holt/L06-forecasting-data-with-trend.md) | **Holt**, inicialización (regresión o estaciones), regresión lineal y R² | Holt con Solver sobre 8 trimestres |
| 06 | [`06-estacionalidad-winters-y-tracking-signal/`](06-estacionalidad-winters-y-tracking-signal/README.md) | [L07](06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md) | **Winters** multiplicativo y aditivo, **señal de rastreo**, RSFE, intervalo de confianza, comparación de métodos | Ejemplo de llantas con Winters y correlograma |
| 07 | [`07-arima/`](07-arima/README.md) | [L08](07-arima/L08-forecasting-with-arima.md) | Box-Jenkins: AR(1), AR(2), MA(1), ARMA(1,1) | — |
| 08 | [`08-metodos-cualitativos/`](08-metodos-cualitativos/README.md) | [L09](08-metodos-cualitativos/L09-qualitative-forecasting-methods.md) | Jurado ejecutivo, Delphi, fuerza de ventas, encuesta de mercado, cuestionarios | — |

## Evaluaciones y proyecto

- **[`parcial-1/`](parcial-1/README.md)**: datos del parcial (48 meses), Excel de cálculos (descriptivos, correlograma, Holt) e informe Word con la elección del método y el pronóstico de los meses 49 a 60. La práctica previa está en el tema 04.
- **[`proyecto-thyms-pronostico/`](proyecto-thyms-pronostico/README.md)**: proyecto del corte sobre THYMS Colombia S.A.S. (tintes en tubo de 60 g). Toma las ventas reales de un vendedor de la zona Antioquia, anonimizadas, y hace un pronóstico con SES (α = 0,05). Calcula además takt time, throughput y WIP. Continúa en el Corte 2 con el gemelo digital: [`../corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/`](../corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/README.md).

## Cómo se evalúa el curso

Según la [L01](01-introduccion-curso-y-sistemas-de-produccion/L01-introduccion-al-curso.md):

- Los cortes pesan **30 % / 30 % / 40 %**.
- Dentro de cada corte: **examen 60 %**, **actividades de clase 10 %** y **proyecto 30 %**.

La rúbrica completa y las reglas del curso están en la L01.

## Cuidado con estos errores

Varios Excel de clase tienen errores de fórmula. Los más importantes:
- el Solver del Excel de Holt quedó en «maximizar» el MAD;
- el MAD del Excel de Winters solo promedia el año 1;
- los coeficientes de `tarea-class-example-3` están mal calculados.

Algunas diapositivas también tienen erratas numéricas. Todo está documentado, con la corrección, en [`../ERRATAS.md`](../ERRATAS.md).
