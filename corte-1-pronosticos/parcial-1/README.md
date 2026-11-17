# Parcial 1: pronóstico de una demanda con tendencia (Corte 1)

## Qué cubre

Primer parcial del curso (Entrega I). Con 48 meses de ventas de un producto se hace el análisis descriptivo completo (estadísticos, histograma, boxplot, dispersión, correlograma y Ljung-Box), se diagnostica una **tendencia lineal decreciente sin estacionalidad**, se elige el método de **Holt** y se pronostican los meses 49 a 60 con sus medidas de error. El informe cierra con recomendaciones gerenciales sobre producción e inventario.

**Enunciado (deducido de los títulos del informe):** 1) análisis descriptivo y elección del método; 2) realizar el pronóstico; 3) estimar el error; 4) conclusión gerencial.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [`parcial-1-informe.md`](./parcial-1-informe.md) | Informe en Word: diagnóstico, justificación de Holt, pronóstico, errores y conclusión gerencial | Sí (1.º) |
| [`parcial-1-calculos.md`](./parcial-1-calculos.md) | Excel con todos los cálculos: 7 hojas (datos, estadísticos, histograma, boxplot, dispersión, correlograma, Holt) | Sí (2.º) |
| [`sales_data.csv`](./sales_data.csv) | Datos del parcial (ver abajo). No tiene `.md` gemelo porque ya es texto plano | Consultar |

### `sales_data.csv`

Archivo de texto separado por comas, 48 filas más encabezado, con encabezados en inglés. Es el dato de entrada que se copió a la hoja `Datos` del Excel. Parece un conjunto de datos sintético del enunciado: el inventario no cumple el balance $I_t = I_{t-1} + P_t - D_t$.

| Columna | Significado | Mínimo | Máximo | Media |
|---|---|---|---|---|
| `Month` | «Month 1» … «Month 48» | — | — | — |
| `Actual Sales` | Demanda real (unidades) | 671 (mes 48) | 1.134 (mes 1) | 916,0 |
| `Forecasted Sales` | Pronóstico que usaba la empresa | 599 | 1.193 | 929,1 |
| `Inventory Levels` | Inventario a fin de mes | 2.089 (mes 9) | 10.622 (mes 48) | 4.629,6 |
| `Production Levels` | Producción del mes | 905 | 1.298 | 1.097,2 |

El pronóstico original tiene MAD = 100,2 y MAPE = 11,4 % frente a las ventas reales, y el inventario pasa de 2.546 (mes 1) a 10.622 (mes 48), es decir, se multiplica por 4,2.

## Orden de estudio sugerido

1. Leer el informe ([`parcial-1-informe.md`](./parcial-1-informe.md)) para ver la historia completa y las decisiones.
2. Revisar en [`parcial-1-calculos.md`](./parcial-1-calculos.md) cómo se calculó cada cosa: primero las hojas descriptivas y luego la hoja `Holt`.
3. Repasar la teoría: [L04](../03-graficas-y-autocorrelacion/L04-plotting-your-data.md) (gráficas y correlograma), [L05](../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md) (errores), [L06](../05-tendencia-suavizacion-doble-holt/L06-forecasting-data-with-trend.md) (Holt) y [L07](../06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md) (señal de rastreo y por qué no Winters).
4. Leer las observaciones al final de cada `.md` (errores y diferencias entre el informe y el Excel).

## Conceptos y fórmulas clave

- **Autocorrelación del rezago $k$** ($x_t$ = demanda, $\bar{x}$ = media, $n$ = 48):
  $$r_k = \frac{\sum_{t=1}^{n-k}(x_t-\bar{x})(x_{t+k}-\bar{x})}{\sum_{t=1}^{n}(x_t-\bar{x})^2}$$
  con límites $\pm\,t_{0{,}025;\,n-1}\cdot SE(r_k)$, donde $SE(r_k) = \sqrt{(1+2\sum_{j=1}^{k-1} r_j^2)/n}$. Detalle en [`parcial-1-calculos.md`](./parcial-1-calculos.md#hoja-descriptivo-correlograma).
- **Ljung-Box:** $Q = n(n+2)\sum_{k=1}^{h}\frac{r_k^2}{n-k}$; si $Q > \chi^2_{\alpha;\,h}$ la serie no es ruido.
- **Holt** ($D_t$ = demanda, $S_t$ = nivel, $G_t$ = tendencia, $\alpha$ y $\beta$ = constantes de suavización, $h$ = meses hacia adelante):
  $$S_t = \alpha D_t + (1-\alpha)(S_{t-1}+G_{t-1}), \quad G_t = \beta(S_t - S_{t-1}) + (1-\beta)G_{t-1}, \quad F_{t+h} = S_t + h\,G_t$$
  Aquí $\alpha$ = 0,95, $\beta$ = 0,05, $S_0$ = 1.161,45 y $G_0$ = −10,02 (intercepto y pendiente de la regresión). Detalle en [`parcial-1-calculos.md`](./parcial-1-calculos.md#hoja-holt).
- **Errores** ($e_t$ = error del mes $t$): $MAD = \frac{1}{n}\sum|e_t|$, $MAPE = \frac{1}{n}\sum|e_t|/D_t$, $MSE = \frac{1}{n}\sum e_t^2$, señal de rastreo $TS = \sum e_t/MAD$ (aceptable en ±4).
- **Regla de elección del método:** demanda estable → promedio móvil o suavización simple; tendencia → Holt o regresión; tendencia + estacionalidad → Winters. Aquí el diagnóstico da tendencia sin estacionalidad → Holt.

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado principal |
|---|---|---|
| Estadísticos descriptivos | Hoja `Descriptivo-Estadisticos` | Media 916, CV 15,4 %, caída de −40,8 %, regresión 1.161,45 − 10,02·t con $R^2$ = 0,988 |
| Histograma y boxplot | Hojas `Descriptivo-Histograma` y `Descriptivo-Boxplot` | Distribución plana; IQR = 250; 0 atípicos |
| Correlograma y Ljung-Box | Hoja `Descriptivo-Correlograma` | $r_1$ = 0,94 que decae despacio; Q = 274,4 > 21,0 |
| Pronóstico de Holt, meses 49 a 60 | Hoja `Holt` | 660,3 (mes 49) → 545,7 (mes 60); MAD 5,30; MAPE 0,60 %; MSE 40,7 |
| Recomendación gerencial | Informe | Producir 400–500 unid./mes para drenar ~10.600 unidades de inventario |

## Relación con otros temas y proyectos

- Teoría de pronósticos: [02-introduccion-a-pronosticos](../02-introduccion-a-pronosticos/), [03-graficas-y-autocorrelacion](../03-graficas-y-autocorrelacion/), [04-datos-estacionarios-promedio-movil-y-suavizacion-simple](../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/), [05-tendencia-suavizacion-doble-holt](../05-tendencia-suavizacion-doble-holt/) y [06-estacionalidad-winters-y-tracking-signal](../06-estacionalidad-winters-y-tracking-signal/).
- Práctica previa al parcial: [`practica-metodos-pronostico-parcial-1.md`](../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/practica-metodos-pronostico-parcial-1.md).
- El mismo tipo de diagnóstico se aplica en el proyecto del semestre: [proyecto-thyms-pronostico](../proyecto-thyms-pronostico/) (Corte 1) y su revisión en el [gemelo digital del Corte 2](../../corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/).
- La conclusión del parcial (bajar la producción por debajo de la demanda para drenar inventario) es una decisión de planeación agregada; ver [01-planeacion-agregada-modelo-bowman](../../corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/).
