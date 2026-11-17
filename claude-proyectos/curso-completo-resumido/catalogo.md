# Catálogo completo de archivos

Cada archivo de la carpeta original del curso, dónde quedó en este repositorio, qué es y dónde leerlo en texto.

- **Leer en .md**: versión en Markdown del archivo (resumen, contenido completo o explicación de los ejemplos, y anexo con el volcado automático).
- **Nombre original**: ruta en la carpeta de trabajo original (`CORTE 1/`, `CORTE 2/`, `CORTE 3/`).
- 🔒 = archivo con datos de clientes anonimizados (nombres → `CLIENTE ###`, documentos → `9#####`, vendedora → `VENDEDOR 401`).

Total: **83 archivos originales** copiados + versiones .md + CSV de hojas largas. Solo se omitieron 2 copias exactas (ver al final).


## Corte 1 — Pronósticos de demanda


### `01-introduccion-curso-y-sistemas-de-produccion/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `L01-introduccion-al-curso.pdf` | PDF | .md | Lec 1: presentación del curso (profesor, ABET, rúbrica, plan de estudios, reglas, evaluación 30/30/40, proyectos), qué es Operations Management y la tarea 1. | `CORTE 1/Lec 1.pdf` |
| `L02-introduction-to-production-systems.pdf` | PDF | .md | Lec 2: configuraciones de producción (flow shop, job shop, open shop), WIP, takt time, throughput, push/pull, Kanban, ConWIP. | `CORTE 1/lec 2 Introduction-to-Production-Systems.pdf` |
| `tarea-ensayo-linkedin-operations-manager.docx` | Word | .md | Tarea 1 (ensayo): compara dos ofertas de LinkedIn de Operations Manager (Lean Solutions Group y Falabella) y elige una. | `CORTE 1/TAREAS/CLASE 1 LINKEDIN/ENYAYO LIKEDIN.docx` |

### `02-introduccion-a-pronosticos/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `L03-introduction-to-forecasting.pdf` | PDF | .md | Lec 3: introducción a pronósticos: tipos y horizontes, etapas del proceso, clasificación de métodos y patrones de demanda. | `CORTE 1/Lec 3 - introduction to forecasting.pdf` |

### `03-graficas-y-autocorrelacion/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `L04-plotting-your-data.pdf` | PDF | .md | Lec 4: graficar los datos: correlograma (ACF), límites de significancia, prueba de Ljung-Box, histograma, boxplot, dispersión y PCA (15 tiendas). | `CORTE 1/Lec 4 - Plotting your data.pdf` |
| `graficas-pronosticos-ventas-autocorrelacion.xlsx` | Excel | .md | 30.000 ventas con 20 rezagos, matriz de autocorrelación y dispersión; conclusión: la serie es aleatoria. | `CORTE 1/GRAFICAS PARAA PRONOSCTICOS DE VENTAS.xlsx` |
| `tarea-class-example-1.xlsx` | Excel | .md | Tarea: ventas propias y de la competencia (1.923 días) con atípicos; ACF con límites, histograma, boxplot, dispersión. Ambas series son aleatorias. | `CORTE 1/TAREAS/PRONOSCITOS DE DEMANDAS/Class example 1.xlsx` |
| `tarea-class-example-2.xlsx` | Excel | .md | Tarea: producto 1 con fórmulas vivas: ACF hasta el rezago 88 (límites de Bartlett), histograma de 40 clases, boxplot y regresión; hay tendencia. | `CORTE 1/TAREAS/PRONOSCITOS DE DEMANDAS/Class example 2.xlsx` |
| `tarea-class-example-3.xlsx` | Excel | .md | Tarea: 301 datos con tendencia creciente. Los coeficientes de la hoja están mal (incluyen la columna índice); el .md trae los correctos. | `CORTE 1/TAREAS/PRONOSCITOS DE DEMANDAS/Class example 3.xlsx` |
| `tarea-class-example-4.xlsx` | Excel | .md | Tarea: 500 datos en zigzag; ACF de ±0,85 que alterna de signo, es decir, estacionalidad de periodo 2. | `CORTE 1/TAREAS/PRONOSCITOS DE DEMANDAS/Class example 4.xlsx` |

CSV con hojas completas: `graficas-pronosticos-ventas-autocorrelacion-datos/`, `tarea-class-example-1-datos/`, `tarea-class-example-2-datos/`, `tarea-class-example-3-datos/`, `tarea-class-example-4-datos/`

### `04-datos-estacionarios-promedio-movil-y-suavizacion-simple/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `L05-forecasting-stationary-data-and-errors.pdf` | PDF | .md | Lec 5: datos estacionarios: promedio móvil, promedio ponderado, suavización exponencial simple y medidas de error (MAD, SSE, MSE, MAPE, PME). | `CORTE 1/Lec 5 - forecasting stationary data and errors.pdf` |
| `practica-metodos-pronostico-parcial-1.xlsx` | Excel | .md | Práctica antes del parcial 1: MA simple, ejercicio de la diapositiva 30, MA ponderado y SES (las hojas de Holt y Winters están vacías; tiene errores). | `CORTE 1/PARICAL 1.xlsx` |
| `promedio-movil-y-suavizacion-exponencial.xlsx` | Excel | .md | Compara PM(6), PM(12), SES α=0,2 y α=0,8 en 30 días (MAD, MSE, error %); gana SES 0,2. Trae además copia de las hojas de tarea-class-example-1. | `CORTE 1/PROMEDIO MOVIL Y SUAVIZACION EXPO.xlsx` |

CSV con hojas completas: `promedio-movil-y-suavizacion-exponencial-datos/`

### `05-tendencia-suavizacion-doble-holt/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `L06-forecasting-data-with-trend.pdf` | PDF | .md | Lec 6: datos con tendencia: Holt (suavización doble), inicialización por regresión y por estaciones, regresión lineal y R². | `CORTE 1/LEc 6 - forecasting data with trend.pdf` |
| `suavizacion-exponencial-doble-holt.xlsx` | Excel | .md | Holt sobre 8 trimestres con S0/G0 por regresión, α y β con Solver, MAD, MAPE y proyección (ojo: Solver quedó en 'Máx'). | `CORTE 1/SUAVIZACION EXPONENCUAL DOBLE.xlsx` |

### `06-estacionalidad-winters-y-tracking-signal/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `L07-forecasting-seasonality-and-tracking-signal.pdf` | PDF | .md | Lec 7: Winters multiplicativo y aditivo (ejemplo de llantas), señal de rastreo, RSFE, intervalo de confianza y comparación de métodos. | `CORTE 1/Lec 7 - forecasting data with seasonality and Tracking Signal.pdf` |
| `metodo-winters.xlsx` | Excel | .md | Ejemplo de llantas de L07: regresión de 24 meses, factores estacionales normalizados, pronóstico Winters del año 3 y correlograma (19 rezagos). | `CORTE 1/METODO WINTERS.xlsx` |

### `07-arima/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `L08-forecasting-with-arima.pdf` | PDF | .md | Lec 8: metodología Box-Jenkins; AR(1), AR(2), MA(1) paso a paso y ARMA(1,1). | `CORTE 1/Lec 8 - forecasting data with ARIMA.pdf` |

### `08-metodos-cualitativos/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `L09-qualitative-forecasting-methods.pdf` | PDF | .md | Lec 9: métodos cualitativos: jurado ejecutivo, Delphi, fuerza de ventas, encuesta de mercado y diseño de cuestionarios. | `CORTE 1/Lec 9 - Qualitative methods for forecasting.pdf` |

### `parcial-1/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `parcial-1-calculos.xlsx` | Excel | .md | Cálculos del parcial 1: descriptivos, histograma, boxplot, dispersión, correlograma (Bartlett, Ljung-Box) y Holt (α=0,95, β=0,05). | `CORTE 1/PARCIAL 1 PPCO.xlsx` |
| `parcial-1-informe.docx` | Word | .md | Informe del parcial 1: diagnóstico de la serie, elección de Holt, pronóstico de los meses 49–60, errores y conclusión gerencial. | `CORTE 1/PARCIAL 1 PPCO.docx` |
| `sales_data.csv` | CSV | es texto | Datos del parcial 1: 48 meses de ventas reales, ventas pronosticadas, inventario y producción. | `CORTE 1/sales_data.csv` |

CSV con hojas completas: `parcial-1-calculos-datos/`

### `proyecto-thyms-pronostico/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `Planeacion_proyecto_corte1.ipynb` 🔒 | Cuaderno Jupyter | .md | Colab del proyecto C1: gráficas de las 464 facturas, conversión a tubos, takt (0,69 min), throughput (86,74 tubos/h) y WIP (Little). | `CORTE 1/PROYECTO/Planeacion_proyecto_corte1.ipynb` |
| `VENTAS.xls` 🔒 | Excel (.xls) | .md | Ventas 2026 del vendedor 401 (Antioquia): totales mensuales y 464 facturas de mayo a julio (anonimizadas). | `CORTE 1/PROYECTO/VENTAS.xls` |
| `pronostico-expo-simple-ppco.xlsx` 🔒 | Excel | .md | Versión corregida del SES: MAD 80,2 M COP, MAPE 53,4 %, pronóstico de agosto 114,7 M COP. | `CORTE 1/PROYECTO/PRONOSTICO EXPO SIMPLE PPCO.xlsx` |
| `pronostico-expo-simple.xlsx` 🔒 | Excel | .md | Primera versión del pronóstico SES (α=0,05) de las ventas; su MAD/MAPE incluye enero (error 0) y sale demasiado bajo. | `CORTE 1/PROYECTO/PRONOSTICO EXPO SIMPLE.xlsx` |

CSV con hojas completas: `VENTAS-datos/`, `pronostico-expo-simple-datos/`, `pronostico-expo-simple-ppco-datos/`

## Corte 2 — Planeación agregada, tamaño de lote y MRP


### `01-planeacion-agregada-modelo-bowman/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `L10-aggregate-planning.pdf` | PDF | .md | Lec 10: S&OP y planeación agregada: unidades agregadas, método gráfico (3 estrategias), modelo de Bowman (PL de transporte, ejemplo con costo $8144), desagregación y revenue management. | `CORTE 2/Lec 10 - Aggregated Planning.pdf` |
| `ejemplo-modelo-bowman.xlsx` | Excel | .md | El mismo ejercicio de Bowman en una sola hoja con parámetros enlazados; misma solución ($8144). Estaba en la carpeta CORTE 3. | `CORTE 3/Ejemplo Modelo Bowman.xlsx` |
| `modelo-bowman.xlsx` | Excel | .md | Ejemplo de Bowman de L10 (pp. 55–67) con Solver: matrices de costo y asignación regular/extra; costo $6784 + $1360 = $8144. | `CORTE 2/BOWMAN.xlsx` |
| `modelo-flujo-gams/modelo-flujo.gms` | GAMS (modelo) | es texto | Modelo LP de planeación agregada (flujo) en GAMS: horas, inventario, contratación/despido, horas extra y subcontratación. | `CORTE 2/MODELO DE FLUJO.gms` |
| `modelo-flujo-gams/modelo-flujo.log` | GAMS (log) | es texto | Log de la ejecución de GAMS (licencia demo). | `CORTE 2/MODELO DE FLUJO.log` |
| `modelo-flujo-gams/modelo-flujo.lst` | GAMS (salida) | es texto | Salida de GAMS/CPLEX con la solución: z = 4.062.000, 2880 h y luego 3000 h, 7890 unidades subcontratadas, sin horas extra. | `CORTE 2/MODELO DE FLUJO.lst` |
| `modelo-flujo-gams/modelo-flujo.lxi` | GAMS (índice IDE) | — | Índice de texto del .lst que usa el IDE de GAMS. | `CORTE 2/MODELO DE FLUJO.lxi` |

### `02-agregacion-y-desagregacion/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `L11-aggregation-and-disaggregation.pdf` | PDF | .md | Lec 11: PL con fuerza de trabajo y backlog; desagregación por tiempo de agotamiento, tiempo de ciclo máximo y alistamientos. | `CORTE 2/Lec 11 - Agregration and dissagregation.pdf` |
| `modelo-desagregacion-v2.xlsx` | Excel | .md | Versión corregida del mismo libro de desagregación; otro reparto óptimo con el mismo 7900. Estaba en la carpeta CORTE 3. | `CORTE 3/Modelo de Desagregación .xlsx` |
| `modelo-desagregacion.xlsx` | Excel | .md | Desagregación con Solver: T* = 1,5948 y reparto del plan agregado de GAMS (inventario 7900). | `CORTE 2/MODELO DE DESAGREGACION.xlsx` |

### `03-wagner-whitin-y-silver-meal/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `L12-wagner-whitin-and-silver-meal.pdf` | PDF | .md | Lec 12: tamaño de lote dinámico; Wagner-Whitin como ruta más corta (ejemplo de 4 periodos, costo óptimo 380) y heurística Silver-Meal. | `CORTE 2/Lec 12 - Wagner Within and Silver meal heuristics.pdf` |
| `wagner_whitin.py` | Python | es texto | Wagner-Whitin en Python para 10 semanas de un componente del esfero. Ojo: cobra alistamiento en lotes de 0 y da $207,6; el óptimo es $130 (ver README). | `CORTE 2/wagner_whitin.py` |

### `04-bom-y-mrp/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `L13-bom-intro-to-mrp.pdf` | PDF | .md | Lec 13: propósito del MRP, listas de materiales (bolso, bicicleta, carro, ejemplo de clase), matriz BOM, niveles y demanda dependiente dd(n)=d·B. | `CORTE 2/Lec 13 - BOM intro to MRP.pdf` |
| `L14-mrp.pdf` | PDF | .md | Lec 14: tabla MRP (9 ítems × 9 semanas), requerimientos netos, tamaño de lote, MRP de ciclo cerrado y nerviosismo. | `CORTE 2/Lec 14 - MRP.pdf` |
| `calculo-demanda-dependiente-directa.xlsx` | Excel | .md | Explosión de la BOM de clase para demandas de 80 y 50 unidades con MMULT y la matriz (I−B)⁻¹ (MINVERSE). | `CORTE 3/Cálculo de Demanda Dependiente Directa.xlsx` |
| `mrp-esfero-v2.xlsx` | Excel | .md | MRP del esfero, versión 2 (reemplaza a la 1): 6 ítems enlazados por la BOM, lead times 3/2/1/0/0/0 y costos por ítem. | `CORTE 2/MRP 2.xlsx` |
| `mrp-esfero.xlsx` | Excel | .md | MRP del esfero, versión 1: producto final resuelto y tres bloques de componentes incompletos. | `CORTE 2/MRP.xlsx` |

### `05-mrp-ii-y-capacidad/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `L15-mrp-ii.pdf` | PDF | .md | Lec 15: MRP II, planeación aproximada de capacidad (RCCP), CRP, MRP de ciclo cerrado, backward/forward scheduling con el ejemplo γ/β. | `CORTE 2/Lec 15 - MRP II.pdf` |
| `backward-scheduling.xlsx` | Excel | .md | CRP con backward scheduling de L15 (pp. 35–42): lotes 300γ, 575γ y 2000β por centro de trabajo, en minutos por semana. Estaba en la carpeta CORTE 3. | `CORTE 3/Backward Scheduling.xlsx` |

### `parcial-2/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `parcial-2-solucion.pdf` | PDF | .md | Parcial 2 con enunciado, rúbrica y solucionario: planeación agregada, PLE, desagregación, BOM, MRP y Silver-Meal. | `CORTE 2/Parcial 2 – Planeación, Programación y Control de la Producción Solucion.pdf` |

### `proyecto-thyms-gemelo-digital/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `CONTEXTO_GEMELO_THYMS.md` | Markdown | es texto | Documento de traspaso del proyecto C2: datos, mapa de celdas del Excel, resultados y advertencias. | `CORTE 2/CONTEXTO_GEMELO_THYMS.md` |
| `Datos Thyms Completo.xlsx` 🔒 | Excel | .md | Libro base del proyecto C2 (14 hojas): parámetros de planta, productos, tiempos, utilización, alistamientos, fallas, métricas, plan agregado, restricciones y ventas. | `CORTE 2/Datos Thyms Completo.xlsx` |
| `Gemelo_Digital_Thyms.ipynb` | Cuaderno Jupyter | .md | Cuaderno base: revisión del pronóstico, gemelo digital en SimPy con sensores virtuales, validación, métricas, restricciones y escenarios. | `CORTE 2/Gemelo_Digital_Thyms.ipynb` |
| `Gemelo_Digital_Thyms_MEJORADO.ipynb` | Cuaderno Jupyter | .md | Igual al base (celdas 0–35) más las secciones 4–5: S&OP agregado y gemelo guiado por el plan frente al de punto de reorden. | `CORTE 2/Gemelo_Digital_Thyms MEJORADO.ipynb` |
| `THYMS-presentacion-corte-2.pdf` | PDF | .md | Presentación del grupo (9 págs.): estudio preliminar, pronóstico, gemelo digital, plan agregado y KPI. | `CORTE 2/THYMS Presentacion Corte 2.pdf` |

CSV con hojas completas: `Datos Thyms Completo-datos/`

## Corte 3 — Programación de la producción (scheduling)


### `00-compendio-metodos-scheduling/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `metodos-programacion-produccion-corte3.xlsx` | Excel | .md | Compendio de 12 hojas con todos los métodos del corte resueltos: CRP, SPT/WSPT/EDD, MS/ATC, cadenas, preemption, Lawler, LPT/SPT, LNS/CP, LFJ/LFM, Johnson, CDS y NEH. | `CORTE 3/Metodos_Programacion_Produccion_Corte3.xlsx` |

### `01-introduccion-scheduling/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `L16-intro-scheduling.pdf` | PDF | .md | Lec 16: introducción a scheduling: notación α|β|γ, indicadores C_j, L_j, T_j, U_j, E_j, de MRP a órdenes, anomalías en P2|prec|Cmax, programas sin retrasos/activos, complejidad. | `CORTE 3/Lec 16 - intro Scheduling.pdf` |

### `02-una-maquina/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `L17-single-machine-scheduling.pdf` | PDF | .md | Lec 17: una máquina: FIFO, SPT, EDD, WSPT, MS, ATC, CR, cadenas (factor ρ), preemption, Lawler, Moore-Hodgson y Solver. | `CORTE 3/Lec 17 - Single Machine Scheduling.pdf` |
| `atc.py` | Python | es texto | Regla ATC (Apparent Tardiness Cost) voraz sobre el ejercicio de L17 pp. 43–45; reproduce la secuencia de clase 1-3-2-4 (ΣwT = 39). | `CORTE 3/atc.py` |
| `ejemplo-1-programacion-produccion.xlsx` | Excel | .md | Ejemplo de 4 actividades con tiempos de liberación r_j: programa, C_j y tiempo de flujo (igual a filas 3–8 de 'Reglas de Despacho'). | `CORTE 3/Ejemplo 1 Programación de Producción .xlsx` |
| `programacion-produccion-una-maquina.xlsx` | Excel | .md | Reglas de despacho con 6 trabajos, cadenas de precedencia, preemption con r_j y modelo en Solver (tiene errores de fórmula documentados). | `CORTE 3/Programación de Producción.xlsx` |

CSV con hojas completas: `programacion-produccion-una-maquina-datos/`

### `03-maquinas-paralelas/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `L18-parallel-machine-scheduling.pdf` | PDF | .md | Lec 18: máquinas paralelas: Pm||Cmax con LPT (garantía 4/3−1/3m), SPT, CP/LNS con precedencias, LFJ/LFM, preemption y MIP de Rm||ΣCj. | `CORTE 3/Lec 18 - Parallel Machine Scheduling.pdf` |
| `lns-maquinas-paralelas.xlsx` | Excel | .md | Plantilla incompleta de máquinas paralelas (15 trabajos, 3 máquinas); el .md trae LPT/SPT/WSPT calculados. El nombre 'LNS' no refleja el contenido. | `CORTE 3/LNS.xlsx` |

### `04-flow-shop/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `L19-flow-shop-scheduling.pdf` | PDF | .md | Lec 19: flow shop: Johnson F2/F3, MIP Fm|prmu|Cmax con código GAMS, Campbell–CDS, NEH, flow shop flexible y algoritmos genéticos. | `CORTE 3/Lec 19 - flow shop scheduling.pdf` |
| `flowshop-scheduling.xlsx` | Excel | .md | Johnson, Campbell, CDS (Cmax 168) y NEH en Excel; la hoja Campbell tiene las iteraciones 2 y 3 rotas (ver ERRATAS). | `CORTE 3/Flowshop Schedulling .xlsx` |

CSV con hojas completas: `flowshop-scheduling-datos/`

### `05-job-shop/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `job-shop-y-flexible-job-shop.pdf` | PDF | .md | Job shop: modelo disyuntivo, implementación en GAMS/LogMIP, grafo disyuntivo, shifting bottleneck (1|r_j|Lmax) y LEKIN. | `CORTE 3/job shop.pdf` |

### `otros-archivos/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `otra-materia-gerencia-financiera-parcial-2do-corte.xlsx` | Excel | .md | OTRA MATERIA (Gerencia Financiera): balances de prueba 2024–2025 y estados financieros con análisis vertical y horizontal. No es de Planeación. | `CORTE 3/Parcial 2do Corte G. Financiera .xlsx` |

### `proyecto-competencia-scheduling/`

| Archivo | Tipo | Leer en .md | Qué es | Nombre original |
|---|---|---|---|---|
| `enunciados/instructivo-competencia-scheduling.pdf` | PDF | .md | Reglas de la competencia en Gradescope: calidad 60 %, tiempo 30 %, informe 10 %; penalizaciones, ranking, función solve(), límite 60 s, librerías. | `CORTE 3/PROYECTO 3/Instructivo_Competencia_Scheduling (1).pdf` |
| `enunciados/plantilla-reto-1-willy-wonka/reto_schedulling.py` | Python | es texto | Plantilla del profesor para el Reto 1 (clase Schedulling). Importa un módulo 'optimizador' que no viene incluido. | `CORTE 3/PROYECTO 3/reto_schedulling (2).py` |
| `enunciados/plantilla-reto-2-monstruopolis/reto_schedulling.py` | Python | es texto | Plantilla del profesor para el Reto 2 (clase Schedulling con generador de instancias y timelimit). | `CORTE 3/PROYECTO 3/reto_schedulling.py` |
| `enunciados/reto-1-willy-wonka.pdf` | PDF | .md | Reto 1 (Willy Wonka): flow shop de 3 máquinas con setups por tipo y regla N→R prohibida, F3|prmu,s_ij|Cmax; formato JSON. | `CORTE 3/PROYECTO 3/Reto Willy Wonka .pdf` |
| `enunciados/reto-2-monstruopolis.pdf` | PDF | .md | Reto 2 (Monstruópolis): 3 máquinas paralelas con liberaciones y precedencias, P3|r_j,prec|Σw_jT_j. | `CORTE 3/PROYECTO 3/Planteamiento proyecto Monstruópolis.pdf` |
| `solucion/INFORME_TECNICO.md` | Markdown | es texto | Borrador del informe técnico de la competencia (máx. 4 páginas). | `CORTE 3/PROYECTO ALGORITMO/INFORME_TECNICO.md` |
| `solucion/README.md` | Markdown | es texto | README de la solución del estudiante: algoritmos, resultados, cómo correr y dudas abiertas sobre Gradescope. | `CORTE 3/PROYECTO ALGORITMO/README.md` |
| `solucion/construir_plantillas.py` | Python | es texto | Genera los dos reto_schedulling.py de gradescope/ a partir de reto1.py y reto2.py. | `CORTE 3/PROYECTO ALGORITMO/construir_plantillas.py` |
| `solucion/gradescope/reto1_willy_wonka/reto_schedulling.py` | Python | es texto | Reto 1 empaquetado en la plantilla del profesor (clase Schedulling), listo para subir a Gradescope. | `CORTE 3/PROYECTO ALGORITMO/gradescope/reto1_willy_wonka/reto_schedulling.py` |
| `solucion/gradescope/reto2_monstruopolis/reto_schedulling.py` | Python | es texto | Reto 2 empaquetado en la plantilla del profesor (clase Schedulling), listo para subir a Gradescope. | `CORTE 3/PROYECTO ALGORITMO/gradescope/reto2_monstruopolis/reto_schedulling.py` |
| `solucion/pruebas/cota_reto2.py` | Python | es texto | Cota inferior lagrangiana del Reto 2 (deja una brecha ≤ 2,4 %). | `CORTE 3/PROYECTO ALGORITMO/pruebas/cota_reto2.py` |
| `solucion/pruebas/data_ejemplo_reto1.json` | JSON | es texto | Instancia de ejemplo del enunciado del Reto 1. | `CORTE 3/PROYECTO ALGORITMO/pruebas/data_ejemplo_reto1.json` |
| `solucion/pruebas/data_ejemplo_reto2.json` | JSON | es texto | Instancia de ejemplo del Reto 2. | `CORTE 3/PROYECTO ALGORITMO/pruebas/data_ejemplo_reto2.json` |
| `solucion/pruebas/data_ejemplo_reto2_plantilla.json` | JSON | es texto | La misma instancia del Reto 2 en el formato de la plantilla (jobs, p, r, d, w, preds). | `CORTE 3/PROYECTO ALGORITMO/pruebas/data_ejemplo_reto2_plantilla.json` |
| `solucion/pruebas/exacto_reto1.py` | Python | es texto | Segundo método exacto, independiente, para verificar el Reto 1. | `CORTE 3/PROYECTO ALGORITMO/pruebas/exacto_reto1.py` |
| `solucion/pruebas/generador.py` | Python | es texto | Generador de instancias compatible con la plantilla. | `CORTE 3/PROYECTO ALGORITMO/pruebas/generador.py` |
| `solucion/pruebas/probar_reto1.py` | Python | es texto | Prueba el Reto 1 con las 30 instancias de la plantilla (semilla 42): validación y comparación con el óptimo. | `CORTE 3/PROYECTO ALGORITMO/pruebas/probar_reto1.py` |
| `solucion/pruebas/probar_reto2.py` | Python | es texto | Prueba el Reto 2: validez (precedencias, liberaciones), ΣwT y tiempo por instancia. | `CORTE 3/PROYECTO ALGORITMO/pruebas/probar_reto2.py` |
| `solucion/reto1.py` | Python | es texto | Solución del Reto 1 (F3|prmu,s_ij|Cmax): cota inferior, NEH, bloques por tipo, búsqueda local con aceleración de Taillard y programación dinámica acotada que demuestra el óptimo. | `CORTE 3/PROYECTO ALGORITMO/reto1.py` |
| `solucion/reto2.py` | Python | es texto | Solución del Reto 2 (P3|r_j,prec|Σw_jT_j): construcción WSPT/ATC respetando precedencias y recocido simulado. | `CORTE 3/PROYECTO ALGORITMO/reto2.py` |

## Archivos de la carpeta original que no se copiaron

Solo copias exactas; su contenido está completo en el archivo indicado.

| Nombre original | Motivo |
|---|---|
| `CORTE 3/Lec 17 - Single Machine Scheduling (1).pdf` | Copia byte a byte (mismo hash MD5) de `CORTE 3/Lec 17 - Single Machine Scheduling.pdf`, que sí está en el repo. |
| `CORTE 3/VENTAS.xls` | Mismas celdas que `CORTE 1/PROYECTO/VENTAS.xls` (comparadas una a una; solo cambian metadatos del archivo), que sí está en el repo. |
