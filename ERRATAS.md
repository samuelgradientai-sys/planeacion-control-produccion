# Erratas y errores detectados en el material

Al convertir el material a Markdown se revisó cada diapositiva y cada fórmula de Excel, y se compararon los resultados. Esta es la lista de errores encontrados, con su corrección cuando se pudo calcular. **Los archivos originales no se modificaron.** Las correcciones también están en los `.md` de cada archivo, en la sección de resumen u observaciones.

> Antes de citar un número de un Excel o de una diapositiva de esta lista, usa el valor corregido.

---

## Corte 1: Pronósticos

### L01 a L03 (introducción)
- **L01 p. 9** dice «Attend classes (20 %)», pero la tabla de notas (p. 22) no incluye la asistencia. Se deduce que es el límite de inasistencia.
- **L01 p. 24**: la columna «Term» de la tabla de proyectos solo está llena en la primera fila.
- **L01 p. 38**: ubica *production scheduling* en otro curso. Es una diapositiva desactualizada: en este curso scheduling se ve en el Corte 3.
- **L01 p. 41**: las columnas de alternativas están tapadas por rectángulos blancos. Los valores se recuperaron de la capa de texto (18.000, 12.750 y 22.500).
- **L01 p. 44**: tres líneas de la tarea están en texto blanco, invisibles en la diapositiva. Se transcribieron.
- **L02**: WIP, takt time y throughput solo se definen con palabras. En el `.md`, la ley de Little y la fórmula del takt se agregaron como complemento, marcado como tal.

### L04 y Excel de autocorrelación ([tema 03](corte-1-pronosticos/03-graficas-y-autocorrelacion/README.md))
- **L04 p. 18 (Ljung-Box)**: $Q = 2{,}9846$ solo se obtiene con la suma sin redondear.
- **`tarea-class-example-1`**:
  - la celda `D3` cuenta `C2:C1924` en lugar de `B2:B1924`, así que el límite del rezago 1 da 0,0447348 en vez de 0,0447231;
  - en la hoja de competencia, la tabla de límites está corrida una fila;
  - las fechas van en orden descendente, así que el «rezago» es en realidad el día siguiente.
- **`tarea-class-example-2`**: hay ventas negativas en el producto 2 (mínimo −30). Además, el resumen del boxplot usa QUARTILE.INC y el gráfico usa el método exclusivo.
- **`tarea-class-example-3`**: la correlación se calculó sobre `A22:V302`, rango que incluye la columna índice, así que los coeficientes de la hoja (0,964 → 0,975) están mal. **Los correctos son 0,992 → 0,776**, y están en el `.md`.

### L05 y Excel de promedios y SES ([tema 04](corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/README.md))
- **L05 p. 9**: el último término del promedio ponderado debe ser $w_nA_{t-n}$, no $w_nA_t$.
- **L05 p. 26**: el PME aparece con el error al cuadrado, $e^2/D$.
- **L05 p. 30**: el último MA(3) da 14,77, no 14,7.
- **`promedio-movil-y-suavizacion-exponencial`**: los promedios móviles se alimentan de sus propios pronósticos (varios pasos), mientras que SES usa datos reales (un paso), así que la comparación es desigual. Además, no calcula el MAPE.
- **`practica-metodos-pronostico-parcial-1`**:
  - `MA SIMPLE`: los pronósticos están corridos una fila. Da MAD 23,30; **el correcto es 28,22**.
  - `MA PONDERADO`: divide entre n aunque los pesos ya suman 1. Da 177,017; **el correcto es 531,05**.
  - `SE SIMPLE`: usa α = 0,95 en vez de 0,05.
  - Los datos salen de `RANDBETWEEN` y cambian al recalcular.

### L06 y Holt ([tema 05](corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/README.md))
- **`suavizacion-exponencial-doble-holt.xlsx`**: el Solver quedó configurado para **maximizar** el MAD. Los valores α = 0,831 y β = 0,999 maximizan el error (MAD 60,78). El mínimo está cerca de α = β = 0,01, con MAD ≈ 37,3. Además, el Excel no usa los datos del enunciado (S0 = 200, G0 = 10, α = β = 0,1); los resultados con esos datos están en el `.md`.
- **L06 p. 8**: las fórmulas rotuladas S1 son estimaciones de la pendiente.
- **L06 p. 22**: el R² = 0,0214 de un gráfico claramente creciente parece incorrecto.

### L07 y Winters ([tema 06](corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/README.md))
- **L07 p. 5**: F11 = 67,74, no 57,21.
- **L07 p. 17**: el promedio del ciclo 1 es 210,17, no 201,16.
- **L07 p. 21**: los valores actualizados son a0 = 247,19 (no 247,93) y C = 1,00 (no 0,97).
- **L07 p. 25**: en la ecuación de tendencia del aditivo debe ir G_t a la izquierda, y la fórmula suma, no resta.
- **L07 pp. 12 y 20**: a la fórmula del pronóstico le falta el horizonte τ.
- **`metodo-winters.xlsx`**:
  - P16 promedia `P2:P13,U2:U13`, pero la columna U está vacía: debía ser la T. El MAD de 4,47 corresponde solo al año 1; **el de 24 meses es 4,23**.
  - El MAPE está vacío.
  - Noviembre del año 2 vale 208, cuando en la L07 es 209.

### L08 (ARIMA)
- La fórmula del MA(1) usa $+\theta_1 e_{t-1}$, pero los números del ejemplo salen de $-\theta_1 e_{t-1}$.
- La p. 5 pide 72 datos; la L07 dice 50 o más.

### Parcial 1 y proyecto THYMS del Corte 1
- **`parcial-1-informe`**:
  - el encabezado dice «Gerencia Financiera» (plantilla equivocada);
  - la producción promedio real es 1.097,2, no 1.082;
  - la señal de rastreo sale de ±4 en los meses 15, 16, 18, 19, 38 y 44, no solo al principio.
- **`sales_data.csv`**: el inventario no cumple el balance $I_t = I_{t-1} + P_t - D_t$.
- **`Planeacion_proyecto_corte1`**:
  - la celda 21 imprime 45.798 como «demanda diaria»; la diaria es 694;
  - julio de 2026 tiene un festivo, no dos, así que son 24 días hábiles.
- **`pronostico-expo-simple`** (primera versión): MAD y MAPE incluyen enero, que tiene error 0, así que salen demasiado bajos. La versión `-ppco` los corrige: **MAD 80,2 M COP y MAPE 53,4 %**.
- Las facturas de mayo a julio superan los totales mensuales de `UNIFICADO` en 0,7 M, 3,1 M y 1,9 M COP.

---

## Corte 2: Planeación agregada y MRP

### L10 y Bowman ([tema 01](corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/README.md))
- **L10 p. 54**: los índices deben empezar en 1 («j = 1, 2…T»).
- **L10 p. 62**: la numeración salta de 1 a 3.
- **L10 p. 41**: el eje dice «por día», pero los valores son mensuales.
- **L10 p. 65 y Excel de Bowman**: dan asignaciones distintas con el **mismo costo, $8144**; son óptimos alternativos.
- **`modelo-bowman.xlsx`**:
  - los rótulos de inventario inicial están invertidos (A = 36 y B = 220);
  - I13 tiene el texto «-», así que la capacidad extra del mes 1 no queda restringida.
- **`ejemplo-modelo-bowman.xlsx`**: la demanda final O28 = SUM(G15:G18) suma costos y da 80 por coincidencia.
- **`modelo-flujo.gms`**:
  - el inventario y las horas iniciales están fijos dentro de las ecuaciones;
  - `S(T)` modela backlog;
  - por eso su plan no coincide con L11 p. 11.

### L11 y desagregación
- **L11 p. 12**: el gráfico muestra P(1) ≈ 2280, pero la tabla dice 2880.
- **L11 p. 15**: A–E son posiciones de la secuencia, no productos.
- **`modelo-desagregacion.xlsx`**: la celda objetivo de Solver (N19) está vacía.

### L12 y Wagner-Whitin ([tema 03](corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/README.md))
- **`wagner_whitin.py`** cobra el alistamiento ($80) también en periodos con lote 0. Su plan cuesta **$207,6**; el óptimo real es **$130**: producir 4880 unidades en la semana 3. Con los datos de la L12, el script sí reproduce el 380 de clase. La corrección está en el README del tema.
- **L12 p. 36**: la fórmula $K = P/(p-t)$ de Silver-Meal divide por cero cuando $p = t$.
- **L12 p. 39**: el costo de mantener es 20 × $1, no 30 × $1.

### L13, L14 y MRP ([tema 04](corte-2-planeacion-agregada-mrp/04-bom-y-mrp/README.md))
- **L14 p. 12 (tabla final)**:
  - no coincide con el inventario de la p. 3 (D, B, C y α);
  - no dice qué regla de lote usa;
  - las recepciones no se suman al inventario.
- **L14 p. 11**: el vector tiene 8 componentes, no 9.
- **L14 p. 9**: dice «MRO» donde debería decir «MRP».
- **`mrp-esfero-v2.xlsx`**:
  - las «X» de texto generan `#VALUE!` en las semanas 8 a 10;
  - en la semana 1 se ocultan faltantes de 610 y 1140 unidades;
  - la Tapa Arriba se libera un periodo antes de lo necesario.
- **`mrp-esfero.xlsx`** (v1): los componentes están incompletos y todos usan lead time 3.
- **`calculo-demanda-dependiente-directa.xlsx`**: la numeración DD(n) está corrida un lugar respecto de las diapositivas.

### L15 y MRP II ([tema 05](corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/README.md))
- **L15**:
  - los tiempos de E y F no coinciden entre la p. 13 (0,10/0,06), la p. 14 (0,20/0,25) y las pp. 19–21 (0,3/0,25);
  - la p. 30 da otra semana de liberación para el lote 575γ.
- **`backward-scheduling.xlsx`**:
  - C14 usa 300 donde debería ir 575;
  - F14 suma donde debería restar;
  - el bloque 2000β está copiado del 575γ sin adaptar.

### Parcial 2 ([carpeta](corte-2-planeacion-agregada-mrp/parcial-2/README.md))
- La portada dice 100 puntos, pero la tabla suma 110.
- **1.3c**: recomienda el Plan B sin calcular el C. **El Plan C cuesta $225.500.000**, menos que el B ($229.440.000) y el A ($235.800.000).
- **2.4**: solo pide Silver-Meal ($1.390.000). El óptimo de Wagner-Whitin es **$1.280.000**.

### Proyecto THYMS del Corte 2
- **`Datos Thyms Completo.xlsx`**:
  - el rótulo «(celda B9)» debe decir B10;
  - `Restricciones` mezcla días calendario y días hábiles;
  - unas hojas usan 22 días/mes y otras 246 días/año.
- **`Gemelo_Digital_Thyms_MEJORADO`**:
  - las celdas 36–44 no tienen salidas guardadas;
  - la tabla «Mejor modelo» da como mejor la persecución, que queda desabastecida.
- **Presentación del Corte 2**: los resultados de Bowman/flujo, el MILP de turnos y el programa maestro (pp. 6–7) **no están en ningún archivo del repo**.

---

## Corte 3: Programación de la producción

### L16 y L17 ([temas 01](corte-3-programacion-scheduling/01-introduccion-scheduling/README.md) y [02](corte-3-programacion-scheduling/02-una-maquina/README.md))
- **L16 p. 43**: el trabajo 9 está dibujado de 6 a 15, aunque p₉ = 8; el Cmax de 36 no cambia.
- **L16**: la p. 7 y la p. 13 indexan $p$ en orden distinto.
- **L17 p. 36**: dice U = {J3, J4}, pero los pendientes son J2 y J3.
- **L17 p. 43**: pregunta por el flujo ponderado y responde con el no ponderado.
- **L17 p. 45**: el ATC usa p̄ fijo (5,5), mientras la p. 13 lo define con los trabajos no programados.
- **`programacion-produccion-una-maquina.xlsx`**:
  - `Reglas de Despacho`:
    - J21 da 28,8 y debería dar 26;
    - E49 y E74 reinician el reloj, así que en EDD el flujo promedio sale 14 y debería salir 23,33, y ΣwC sale 123 y debería salir 179;
    - los setups s_j no se usan.
  - `Restricciones de Precedencia`:
    - la cadena aparece como C-A-B en un lado y C-B-A en otro;
    - «3*=12−8=2» debería dar 4;
    - t = 18 debería ser 28, y t = 38 debería ser 50.
  - `Tardanza Máxima`:
    - el objetivo `SUMPRODUCT(p,w)` = 20197 es constante; el ΣwC real es 192388 y el óptimo con WSPT es 151038;
    - `RANDBETWEEN` cambia los datos al recalcular.

### L18 y máquinas paralelas ([tema 03](corte-3-programacion-scheduling/03-maquinas-paralelas/README.md))
- **`lns-maquinas-paralelas.xlsx`**:
  - es una plantilla incompleta: las fórmulas de la máquina 2 están mal copiadas y la máquina 3 no tiene fórmulas;
  - el nombre («LNS») y el de la hoja («LFJ») no corresponden al contenido.
  - El `.md` trae LPT, SPT y WSPT calculados (cálculo propio).
- **L18 pp. 12–14**: las etiquetas de máquina no se leen; se tomaron como 1–4 de arriba abajo.

### L19 y flow shop ([tema 04](corte-3-programacion-scheduling/04-flow-shop/README.md))
- **L19 p. 21**: la función objetivo escribe $x_{jk}$ donde debería ir $x_{j1}$, y una restricción escribe $x_{jk}$ donde la p. 20 tiene $x_{j,k+1}$.
- **L19 p. 24 (GAMS)**: los nombres `onmachrel` y `permachrel` están cruzados con su descripción, y `totwait` es en realidad el makespan.
- **L19 p. 14**: el eje del Gantt llega a 48, pero el Cmax es 49.
- **L19 pp. 50 y 53**: los cromosomas tienen genes repetidos.
- **`flowshop-scheduling.xlsx`**:
  - hoja `Campbell`: las iteraciones 2 y 3 están rotas (suman tiempos de terminación, la columna M1 está vacía y el trabajo 5 queda en el grupo equivocado). **Los valores correctos son 85 y 85**, como en la L19.
  - hoja `CDS`: las fórmulas `C74` y `C75` toman la referencia equivocada; los errores se compensan y el Cmax de 168 no cambia.
  - hoja `NEH`: algunos `MIN` no incluyen todas las opciones; el resultado no cambia.

### Compendio ([tema 00](corte-3-programacion-scheduling/00-compendio-metodos-scheduling/README.md))
- **Hoja `07`**: usa $p_1 = 3$, pero L18 p. 8 dice 1. Por eso da Cmax 55 y ΣCj 584; **los correctos son 54 y 582**.
- **Hoja `08`**: la solución LFJ omite un trabajo y reporta Cmax = 2; **el correcto es 3** (L18 p. 25).
- **Hoja `03`**: el encabezado «t=30» de la tabla MS debería ser t=34.
- **Hoja `01` (CRP, tema del Corte 2)**:
  - los rótulos «Producto Y/B» deberían ser γ;
  - el backward scheduling está simplificado frente al de la L15.
- Las citas «PDF p. X» no corresponden a las páginas de los PDF del repo. El `.md` trae una tabla con las fuentes reales.

### Job shop ([tema 05](corte-3-programacion-scheduling/05-job-shop/README.md))
- El título anuncia flexible job shop e iterated local search, pero no hay diapositivas de esos temas.
- **p. 7**: dice y21; debería ser y12.
- **p. 17**: dice «camino más corto», pero el método usa la ruta más larga.
- **p. 29**: un arco sale del nodo equivocado.
- El modelo GAMS usa un solo inicio por trabajo, así que en realidad modela un job shop sin esperas.

### Competencia de scheduling ([proyecto](corte-3-programacion-scheduling/proyecto-competencia-scheduling/README.md))
- **Reto 1**: el `data.json` de ejemplo dice S-R = 15 y S-N = 30 en M1, pero la Tabla 2 dice S-N = 15 y S-R = 35.
- **Reto 2**:
  - el ejemplo de «entrada» es en realidad una salida;
  - no da datos de disponibilidad de máquinas;
  - $d_j$ es ambiguo.
- **El instructivo y las plantillas no coinciden**: el instructivo pide la función `solve()` y las plantillas la clase `Schedulling`; además, las plantillas importan pandas.
- **Plantilla del Reto 1**:
  - falta el módulo `optimizador`;
  - no devuelve `valor_objetivo`;
  - `calcular_makespan_penalizado` toma el tipo del **último lote de la secuencia**, así que da 651–1003 cuando el Cmax real está entre 566 y 678.
- **Plantilla del Reto 2**: el esqueleto no corre tal cual (falta `generador` y hay variables sin definir) y deja un ciclo de 29 s por instancia.
