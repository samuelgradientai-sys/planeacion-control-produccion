# parcial-1-informe

> **Archivo:** [`parcial-1-informe.docx`](./parcial-1-informe.docx) · **Corte 1** · Documento de Word  
> **Nombre original:** `CORTE 1/PARCIAL 1 PPCO.docx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

### Qué es

Informe escrito del **Parcial 1 — Entrega I** del Corte 1 (pronósticos). Analiza 48 meses de ventas de un producto ([`sales_data.csv`](./sales_data.csv)), elige el método de **Holt** (suavización exponencial doble), pronostica los meses 49 a 60, estima el error y cierra con una conclusión gerencial. Todos los números salen del libro [`parcial-1-calculos.md`](./parcial-1-calculos.md).

**Enunciado (deducido de los títulos de las secciones):** 1) análisis descriptivo de los datos y elección del método de pronóstico más adecuado; 2) realizar el pronóstico; 3) estimar el error de pronóstico; 4) conclusión gerencial.

### Estructura

| Sección | Qué hace |
|---|---|
| Portada | Logo de la Universidad de La Sabana (imagen), «PARCIAL», «ENTREGA I», miembros y «UNIVERSIDAD DE LA SABANA, CHÍA». La primera línea dice «Gerencia Financiera» (error de plantilla, ver advertencias). |
| Análisis descriptivo y elección del método | Estadísticos básicos y cinco gráficos: serie de tiempo (Fig. 1), histograma (Fig. 2), boxplot (Fig. 3), dispersión tiempo vs. demanda (Fig. 4) y correlograma (Fig. 5). Diagnóstico: tendencia decreciente fuerte, sin estacionalidad. |
| Por qué elegimos Holt | Descarta, uno por uno, el promedio móvil simple, el ponderado, la suavización exponencial simple y Winters, y justifica Holt (Fig. 6: demanda real vs. Holt). Menciona la regresión lineal como otra candidata válida. |
| Realizar el pronóstico | Explica $F_{48+h} = S_{48} + h\,G_{48}$ con $S_{48}$ = 670,7 y $G_{48}$ = −10,43 y da los pronósticos de los meses 49 a 60. |
| Estimar el error | MAD, MAPE, SSE, MSE, RMSE, sesgo, señal de rastreo e intervalo del 95 %. |
| Conclusión gerencial | Declive estructural, exceso de inventario y tres decisiones. |

Las figuras 1, 2, 4, 5 y 6 son gráficos de Word enlazados a las hojas `Datos`, `Descriptivo-Histograma`, `Descriptivo-Scatter`, `Descriptivo-Correlograma` y `Holt` del Excel; la Figura 3 es una imagen del boxplot (caja de ~789 a ~1.039, mediana ~931 en rojo, bigotes de 671 a 1.134).

### Datos que usa

`sales_data.csv`: 48 meses con ventas reales, pronóstico original de la empresa, inventario y producción (ver el [README de la carpeta](./README.md)).

### Métodos

- Estadística descriptiva: media, mediana, desviación estándar, $CV = s/\bar{x}$, cuartiles e IQR.
- Gráficas de diagnóstico (clase [L04](../03-graficas-y-autocorrelacion/L04-plotting-your-data.md)): serie, histograma, boxplot con vallas $Q_1 - 1{,}5\,IQR$ y $Q_3 + 1{,}5\,IQR$, dispersión con regresión $\hat{x}_t = a + b\,t$.
- Correlograma: $r_k = \frac{\sum_{t=1}^{n-k}(x_t-\bar{x})(x_{t+k}-\bar{x})}{\sum_{t=1}^{n}(x_t-\bar{x})^2}$ con límites de significancia al 95 %, y prueba de Ljung-Box $Q = n(n+2)\sum_{k=1}^{12}\frac{r_k^2}{n-k}$ frente a $\chi^2_{0{,}05;\,12}$.
- Holt ([L06](../05-tendencia-suavizacion-doble-holt/L06-forecasting-data-with-trend.md)): $S_t = \alpha D_t + (1-\alpha)(S_{t-1}+G_{t-1})$, $G_t = \beta(S_t - S_{t-1}) + (1-\beta)G_{t-1}$, $F_{t+h} = S_t + h\,G_t$, con $\alpha$ = 0,95 y $\beta$ = 0,05 ($S_t$ = nivel, $G_t$ = tendencia, $D_t$ = demanda, $h$ = meses hacia adelante).
- Errores ([L05](../04-datos-estacionarios-promedio-movil-y-suavizacion-simple/L05-forecasting-stationary-data-and-errors.md)): $MAD = \frac{1}{n}\sum|e_t|$, $MAPE = \frac{1}{n}\sum\frac{|e_t|}{D_t}$, $SSE = \sum e_t^2$, $MSE = SSE/n$, $RMSE = \sqrt{MSE}$, sesgo $= \frac{1}{n}\sum e_t$.
- Señal de rastreo ([L07](../06-estacionalidad-winters-y-tracking-signal/L07-forecasting-seasonality-and-tracking-signal.md)): $TS = \sum e_t / MAD$, aceptable entre −4 y +4.
- Intervalo del 95 % para el mes siguiente: $F \pm 1{,}96 \cdot RMSE$.

### Resultados clave con números

| Resultado | Valor |
|---|---|
| Media / mediana / desviación / CV | 916 / 931,5 / 141 / 15,4 % |
| Máximo (mes 1) / mínimo (mes 48) | 1.134 / 671 |
| Caída acumulada en 48 meses | −40,8 % |
| Regresión | Ventas = 1.161,45 − 10,02·t, $R^2$ = 0,988, correlación −0,994 |
| IQR / atípicos | 250 / ninguno |
| Autocorrelaciones | $r_1$ = 0,94; $r_2$ = 0,88; $r_3$ = 0,82; $r_4$ = 0,76 (los cuatro significativos); sin pico en el rezago 12 |
| Ljung-Box | Q = 274,4 frente a 21,0 → no aleatoria |
| Holt: nivel y tendencia finales | 670,7 y −10,43 unid./mes |
| Pronósticos | Mes 49 ≈ 660; mes 52 ≈ 629; mes 54 ≈ 608; mes 60 ≈ 546 |
| MAD / MAPE | 5,3 unidades / 0,59 % |
| SSE / MSE / RMSE | 1.953,7 / 40,7 / 6,4 |
| Sesgo / señal de rastreo final | 0,18 / 1,6 |
| Intervalo del 95 % (mes 49) | ±12,5 → de 648 a 673 |
| Pronóstico anterior de la empresa | MAPE 11,4 % (error promedio de ~100 unidades) |
| Producción e inventario actuales | ~1.082 unid./mes; inventario > 10.600 (≈ 16 meses de demanda; se cuadruplicó) |

### Conclusiones

1. La demanda está en **declive estructural**: cae unas 10 unidades por mes, ya perdió el 41 % y seguiría bajando hasta ~546 en el mes 60 (≈ 17 % menos en un año).
2. El problema urgente es la respuesta de la empresa: producir ~1.082 unidades/mes con un pronóstico que sobreestimaba (MAPE 11 %) infló el inventario.
3. Tres decisiones: (a) adoptar Holt como pronóstico oficial y recalibrarlo cada mes; (b) recortar la producción por debajo de la demanda, a unas **400–500 unidades/mes**, para drenar el inventario (la sección del pronóstico hablaba de planear alrededor de 600–650 «e incluso por debajo»); (c) investigar las causas del declive y decidir si se invierte en el producto o se gestiona su salida del portafolio.
4. Los primeros 6 meses del pronóstico sirven para decidir producción y compras; los meses 7 a 12 son referencia de planeación.

### Supuestos y advertencias

- **Encabezado equivocado:** la primera línea del documento dice «Gerencia Financiera» por un error de plantilla; el contenido es del curso de Planeación (pronósticos).
- **Producción promedio:** el informe dice 1.082 unidades/mes, pero el promedio de los 48 meses de `sales_data.csv` es 1.097,2 (1.081,1 es el promedio de los primeros 12 meses).
- **MAPE:** el Excel guarda 0,5976 %, que redondea a 0,60 % (el informe escribe 0,59 %).
- **Sesgo y señal de rastreo** no están calculados en el Excel. Recalculados, el sesgo es 0,18 (con error = pronóstico − real) y la señal de rastreo final vale 1,6 en valor absoluto. Pero con la definición de MAD acumulado mes a mes, la señal sale de ±4 en los meses 15, 16, 18, 19, 38 y 44, no solo «en los primeros meses» como afirma el informe.
- **«Regresión prácticamente idéntica»:** la regresión da 670,6 en el mes 49 y 560,4 en el mes 60, frente a 660,3 y 545,7 de Holt: la misma pendiente, pero una diferencia de 10 a 15 unidades.
- El «17 % menos» compara el mes 60 con el pronóstico del mes 49 (546/660 − 1 = −17,4 %); frente a la venta real del mes 48 (671) la caída sería −18,7 %.
- Los errores son **dentro de la muestra** (pronóstico a un paso con parámetros e inicialización que usan los 48 datos), así que son optimistas; el intervalo de ±12,5 solo vale para el mes inmediato.
- El supuesto de fondo es que la caída lineal continúa; el informe lo reconoce y pide recalibrar cada mes.

## Texto completo

Gerencia Financiera

PARCIAL

ENTREGA I

MIEMBROS:

Samuel Gómez Davila- 0000312349

UNIVERSIDAD DE LA SABANA, CHÍA

### Análisis descriptivo de los datos y elegir el método de pronóstico más adecuado

Empezamos por lo básico: organizar los 48 meses de ventas como una serie de tiempo, numerando cada mes del 1 al 48, y sacar los estadísticos para hacernos una primera idea de los datos. La demanda promedio del periodo fue de 916 unidades, con una mediana de 931.5, una desviación estándar de 141 unidades y un coeficiente de variación del 15.4%. Las ventas se movieron entre un máximo de 1,134 unidades al comienzo y un mínimo de 671 al final, y ese detalle, que el máximo estuviera al inicio y el mínimo al final, ya nos hacía sospechar hacia dónde iba la historia.

#### Serie de tiempo

Figura 1
Serie de tiempo de la demanda (48 meses)

Como en clase insistieron en que los promedios no cuentan toda la historia, lo siguiente fue graficar los datos desde varios ángulos. Con solo mirar la serie en la Figura 1 la sospecha se confirmó: la demanda viene cayendo sin pausa, un 40.8% acumulado en los 48 meses. Y cada gráfico que hicimos después nos fue diciendo lo mismo por caminos distintos.

#### Histograma

Figura 2
Histograma de la demanda

El histograma de la Figura 2, por ejemplo, salió plano. Si la demanda fuera estable, esperaríamos una campana concentrada alrededor de la media; en cambio, todas las clases entre 650 y 1,150 unidades tienen frecuencias muy parecidas. Al principio puede parecer raro, pero tiene todo el sentido: una serie que va cayendo no se queda oscilando en un nivel, sino que va pasando por todos los niveles en su camino hacia abajo, y eso reparte los datos por todo el rango.

#### Boxplot

Figura 3
Boxplot de la demanda

El boxplot de la Figura 3 nos dio otra pieza del rompecabezas. La caja es muy ancha, con un rango intercuartílico de 250 unidades, pero no apareció ni un solo dato atípico. Eso descarta una explicación tentadora: que la caída se debiera a uno o dos meses desastrosos por algún evento puntual. No fue así; nada se sale de lo esperado, la demanda simplemente bajó de forma gradual y sostenida. Es un problema estructural, no un accidente.

#### Scatter Plot

Figura 4
Diagrama de dispersión tiempo vs. demanda

El scatter plot de la Figura 4 fue el más contundente de todos. Los puntos forman una franja descendente casi perfecta, sin curvas ni quiebres, y la regresión que le ajustamos, Ventas = 1,161.45 − 10.02·t con un R² de 0.988, dice que el tiempo explica el 98.8% de lo que pasa con las ventas. La correlación de −0.994 lo resume bien: cada mes que pasa, se venden unas diez unidades menos, con una regularidad que casi asusta.

#### Correlograma

Figura 5
Correlograma con límites de significancia al 95%

Para cerrar el diagnóstico construimos el correlograma con sus límites de significancia, siguiendo el procedimiento de clase, y el resultado está en la Figura 5. El patrón es de libro: el coeficiente del primer rezago es altísimo (r₁ = 0.94) y los siguientes van bajando de a poquito (0.88, 0.82, 0.76…), con los primeros cuatro por encima del límite de significancia. Es exactamente la firma de una serie con tendencia. Lo que no apareció fue un pico en el rezago 12, que sería la señal de estacionalidad anual, así que la descartamos. Y por si quedaban dudas, la prueba de Ljung-Box las despejó: Q dio 274.4 contra un chi-cuadrado crítico de 21.0, o sea que los datos definitivamente no son aleatorios. Diagnóstico cerrado: tendencia decreciente fuerte, sin estacionalidad.

#### Por qué elegimos Holt

La elección no fue solo porque dio los mejores números, aunque los dio. La razón de fondo es que el método tiene que corresponder al comportamiento de los datos, y nuestra serie tiene una característica dominante: la tendencia decreciente. Con ese diagnóstico en mano, la forma más honesta de justificar la elección es mostrar por qué los demás métodos no servían para este caso.

El promedio móvil simple lo descartamos de entrada. Este método pronostica con el promedio de los últimos k periodos, lo cual funciona bien cuando la demanda es estable y oscila alrededor de un nivel constante. Pero nuestra demanda no oscila: cae. Y en una serie que cae, el pasado siempre es más alto que el presente, así que el promedio de los últimos meses queda inevitablemente por encima de la venta que viene. El resultado sería un pronóstico que sobreestima la demanda mes tras mes, de forma sistemática, que es justo el tipo de error que llevó a la empresa a acumular inventario.

El promedio móvil ponderado tampoco resuelve el problema. Es cierto que al darle más peso a los meses recientes el pronóstico reacciona más rápido, y por eso el error se reduce un poco frente al promedio simple. Pero el defecto de fondo sigue intacto: el método no tiene ninguna manera de proyectar la caída hacia adelante, porque sigue siendo un promedio de valores pasados. En el mejor de los casos persigue la tendencia siempre desde atrás, llegando tarde a cada mes. Cambiar los pesos alivia el síntoma, no cura la enfermedad.

La suavización exponencial simple fue la tercera descartada, y quizás la más ilustrativa. Es un método más refinado que los promedios móviles, porque pondera toda la historia con pesos que decaen exponencialmente. Sin embargo, su fórmula estima un solo componente: el nivel de la demanda. Al asumir que no existe tendencia, en una serie decreciente carga un sesgo positivo permanente que ningún valor de alfa puede eliminar del todo: con alfa alto se pega más al último dato, pero sigue pronosticando el pasado inmediato, no la caída que viene. De hecho, el pronóstico que la empresa venía usando cometía en esencia este mismo error, y su MAPE del 11.4% con el inventario cuadruplicado son la evidencia de lo que cuesta ignorar una tendencia.

Con Winters pasó lo contrario: lo descartamos no porque le falte algo, sino porque le sobra. El método de Winters está diseñado para series que tienen tendencia y además estacionalidad, ya que estima tres componentes (nivel, tendencia y factores estacionales). Pero nuestro análisis descriptivo fue claro en ese punto: el correlograma no mostró ningún pico en el rezago 12, que sería la firma de un patrón anual. Aplicar Winters aquí habría significado estimar un componente estacional que no existe, agregando parámetros y complejidad al modelo sin ninguna ganancia en precisión. Y en pronósticos, un modelo con parámetros de más no es más completo, es más frágil.

Figura 6
Demanda real vs. pronóstico del método de Holt

Descartadas esas cuatro alternativas, el método de Holt quedó como la elección natural, porque está diseñado exactamente para el patrón que tiene nuestra serie: tendencia sin estacionalidad. A diferencia de los anteriores, no trabaja con un solo componente sino con dos: estima el nivel de la demanda y aparte estima la pendiente, y va actualizando ambos cada mes con la información nueva que llega. Eso le permite incorporar la caída al pronóstico en lugar de perseguirla desde atrás. Los resultados lo confirmaron: obtuvo un MAD de apenas 5.3 unidades y un MAPE del 0.59%, los menores errores entre todos los métodos evaluados. La Figura 6 lo muestra bien: la línea del pronóstico se superpone casi por completo sobre la demanda real durante los 48 meses de historia y, a partir del mes 49, prolonga la caída de forma coherente hasta llegar a unas 546 unidades en el mes 60. Y tiene una ventaja adicional frente a la regresión lineal, que era la otra candidata válida: la regresión asume que la pendiente será la misma para siempre, mientras que Holt la recalcula con cada dato nuevo, así que, si el día de mañana la caída se frena o se acelera, el modelo se acomoda solo, sin que haya que rehacer nada.

### Realizar el pronóstico

Una vez elegido el método de Holt, lo aplicamos para proyectar la demanda de los próximos doce meses. El procedimiento es directo: al recorrer los 48 meses de historia, el modelo termina con dos valores estimados, el nivel de la demanda al cierre del periodo, que quedó en 670.7 unidades, y la tendencia final, que quedó en −10.43 unidades por mes. Con esos dos componentes, el pronóstico de cualquier mes futuro se calcula sumando al nivel tantas veces la tendencia como meses hacia adelante queramos ver. Por ejemplo, para el mes 49 el cálculo es 670.7 menos 10.43, que da unas 660 unidades; para el mes 50 se restan dos veces, y así sucesivamente.

Los resultados muestran una demanda que seguiría cayendo de forma gradual: alrededor de 660 unidades en el mes 49, 629 hacia el mes 52, 608 en el mes 54, y cerca de 546 al llegar al mes 60. En otras palabras, si la tendencia actual se mantiene, la empresa vendería en un año aproximadamente un 17% menos que hoy. Como verificación, corrimos el mismo pronóstico con la regresión lineal y los números resultaron prácticamente idénticos: ambos métodos coinciden en que la demanda pierde unas diez unidades cada mes, lo que nos da bastante confianza en la magnitud de la proyección.

Ahora bien, hay dos precisiones que nos parece honesto dejar por escrito. La primera es que todo pronóstico pierde confiabilidad a medida que se aleja en el tiempo: los primeros seis meses de la proyección son suficientemente sólidos para tomar decisiones de producción y compras, mientras que los meses siete a doce conviene tratarlos como una referencia de planeación, no como una cifra comprometida. La segunda es que el modelo asume que la caída continúa al ritmo actual. Esto no es un problema grave porque el método de Holt se recalibra solo, porque cada mes que entra un dato real nuevo ajusta su estimación de la tendencia, pero sí implica una disciplina: hay que actualizar el pronóstico mensualmente y estar atentos a cualquier señal de que la demanda se estabiliza o se acelera.

La conclusión práctica del pronóstico es contundente. Hoy la empresa produce en promedio 1,082 unidades al mes para una demanda que ronda las 650 y va en descenso. Esa brecha es la que infló el inventario hasta superar las 10,600 unidades, que al ritmo de ventas proyectado equivalen a unos dieciséis meses de demanda. El pronóstico indica que la producción debería planearse alrededor de las 600 a 650 unidades mensuales, e incluso por debajo de la demanda durante algunos meses, para permitir que el inventario acumulado se drene y los costos de almacenamiento bajen.

### Estimar el error de pronóstico

Elegir un método de pronóstico no basta: también hay que saber qué tanto se equivoca, porque de ese margen de error depende cuánta holgura debemos dejar en los planes de producción y de inventario. Para estimarlo, comparamos mes a mes el pronóstico de Holt contra la venta real en los 48 periodos evaluados, y a partir de esas diferencias calculamos las medidas de error habituales.

Los resultados fueron muy buenos. El error absoluto medio, o MAD, fue de apenas 5.3 unidades: en un mes típico el pronóstico se desvía unas cinco unidades de la venta real, sobre una demanda que promedia unas 900. Llevado a términos relativos, eso equivale a un MAPE del 0.59%, es decir, el modelo acierta en más del 99% de la magnitud de la demanda. Calculamos también la suma de errores al cuadrado (SSE), que dio 1,953.7, y el error cuadrático medio (MSE), que quedó en 40.7; su raíz, el RMSE, resulta en 6.4 unidades, muy cercana al MAD. Esa cercanía entre las dos medidas nos dice algo adicional: no hubo meses con errores desproporcionados, el modelo se equivoca poco y de manera pareja a lo largo de todo el periodo.

Hicimos además dos verificaciones que nos dieron tranquilidad sobre la calidad del pronóstico. La primera fue el sesgo, que mide si el modelo tiende a pronosticar sistemáticamente por encima o por debajo de la realidad. Nos dio 0.18 unidades, prácticamente cero, lo que significa que los errores hacia arriba y hacia abajo se compensan entre sí. Esto es justo lo contrario de lo que ocurría con el pronóstico anterior de la empresa, que sobreestimaba la demanda mes tras mes y por eso terminó inflando el inventario. La segunda verificación fue la señal de rastreo, un indicador que va acumulando los errores y avisa cuando un modelo empieza a desviarse de forma sostenida. La regla práctica dice que debe mantenerse entre menos cuatro y más cuatro veces el MAD, y la nuestra cerró en 1.6, cómodamente dentro de la zona de control. Vale aclarar que en los primeros meses la señal se sale de rango, pero es un efecto normal del arranque, cuando todavía hay muy pocos datos acumulados; pasado ese periodo de calentamiento, se estabiliza y ya no vuelve a salirse.

Con el RMSE pudimos, por último, ponerle una banda de confianza al pronóstico. Asumiendo que los errores se comportan de manera aproximadamente normal, el intervalo del 95% resulta de unas doce unidades y media hacia arriba o hacia abajo. En la práctica esto significa que cuando decimos que el mes 49 venderá alrededor de 660 unidades, lo razonable es esperar que la cifra real caiga entre 648 y 673. Para efectos de planeación es un margen muy manejable, aunque hay que tener presente que aplica al pronóstico del mes inmediato: a medida que proyectamos más lejos en el tiempo la incertidumbre crece, y esa es una razón más para recalibrar el modelo cada mes con el dato real que vaya llegando.

### Conclusión gerencial

El análisis deja un mensaje central que la gerencia debe asumir cuanto antes: la demanda de este producto no está pasando por un mal momento, está en declive estructural. Lleva 48 meses cayendo a un ritmo constante de unas diez unidades mensuales, ha perdido ya el 41% de su volumen inicial, y el pronóstico indica que la tendencia continuará, con ventas que bajarían de las 660 unidades actuales a cerca de 546 dentro de un año. No se trata de una proyección especulativa: el comportamiento de la serie es tan regular que dos métodos independientes llegan prácticamente a la misma cifra, y el modelo elegido demostró equivocarse en promedio apenas cinco unidades por mes.

El problema más urgente, sin embargo, no es la caída de la demanda en sí, sino la respuesta que la empresa le ha venido dando. Mientras las ventas bajaban, la producción se mantuvo alrededor de las 1,082 unidades mensuales, apoyada en un pronóstico que sobreestimaba la demanda con un error promedio del 11%. La consecuencia está a la vista: el inventario se cuadruplicó hasta superar las 10,600 unidades, que al ritmo de ventas actual representan unos dieciséis meses de demanda inmovilizados en bodega, con todo lo que eso implica en costos de almacenamiento, capital de trabajo atrapado y riesgo de obsolescencia.

De este diagnóstico se desprenden tres decisiones concretas. La primera es adoptar de inmediato el método de Holt como herramienta oficial de pronóstico, recalibrándolo cada mes con el dato real nuevo; el costo de implementarlo es mínimo y reduce el error de pronóstico de cien unidades a cinco. La segunda es recortar la producción de manera decidida: no basta con bajarla al nivel de la demanda proyectada, sino que conviene ubicarla por debajo durante varios meses, en el orden de las 400 a 500 unidades mensuales, para que el exceso de inventario se drene de forma controlada mientras las ventas se atienden desde bodega. La tercera es de más largo plazo: una demanda que cae de forma tan sostenida rara vez se revierte sola, así que la empresa debería investigar las causas del declive (competencia, sustitución del producto, cambios en el mercado) y evaluar si este producto amerita inversión comercial para recuperarlo o si lo sensato es gestionar su salida ordenada del portafolio.

En síntesis, hoy la empresa cuenta por primera vez con un pronóstico confiable, y ese pronóstico dice con claridad que el escenario es de contracción. La diferencia entre actuar ahora o dentro de seis meses se medirá en miles de unidades adicionales acumuladas en bodega. La recomendación de este informe es alinear la producción con la realidad de la demanda de inmediato, y usar el tiempo que el inventario actual concede para decidir, con datos, el futuro del producto.

