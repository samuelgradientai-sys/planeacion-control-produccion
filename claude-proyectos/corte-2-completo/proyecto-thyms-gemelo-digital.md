<!-- fuente: corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/README.md -->
# Proyecto THYMS, Corte 2: S&OP y gemelo digital (Corte 2)

## Qué cubre

Segunda entrega del proyecto del semestre sobre **THYMS Colombia S.A.S.**, que fabrica tintes para el cabello en tubos de 60 g:
- A: Kolorezza permanente;
- B: Visalia sin amoníaco;
- C: Thym's Coloring permanente.

El grupo:
1. armó un libro con todos los parámetros de la planta, el estudio preliminar (takt, cycle time, throughput, WIP, restricciones) y el **plan agregado** de 12 meses (persecución, nivelada y mixta);
2. corrigió el pronóstico del Corte 1;
3. construyó un **gemelo digital** de la planta en Python/SimPy con sensores virtuales, escenarios y pruebas de estrés;
4. en la versión MEJORADO, conectó el gemelo con el plan agregado (S&OP).

### Enunciado o entregable (deducido de los archivos)

No hay enunciado escrito en la carpeta. Según [`CONTEXTO_GEMELO_THYMS.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/CONTEXTO_GEMELO_THYMS.md) y la presentación, el entregable pedía:
1. un **estudio preliminar** del sistema: WIP, takt time, throughput, cycle time y restricciones de capacidad, demanda y almacenamiento;
2. un **gemelo digital en ARENA o Python** que incluya el pronóstico, la estacionalidad y sensores virtuales;
3. la presentación del plan de ventas y operaciones (S&OP).

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [`CONTEXTO_GEMELO_THYMS.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/CONTEXTO_GEMELO_THYMS.md) | Documento de traspaso escrito antes de esta conversión (estado al 2026-10-05): proyecto, archivos, mapa de celdas del libro, clases del gemelo, resultados, advertencias y supuestos abiertos. Ya era Markdown; no tiene binario | Sí (1.º) |
| [`THYMS-presentacion-corte-2.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/THYMS-presentacion-corte-2.md) | Presentación del grupo (PDF de 9 páginas, 6 de octubre de 2026): resultados y mejoras en una vista | Sí (2.º) |
| [`Datos Thyms Completo.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Datos%20Thyms%20Completo.md) | Libro de 14 hojas: parámetros, productos, tiempos, utilización, alistamientos, fallas, mano de obra, métricas, plan agregado, restricciones, proceso, facturas, clientes y ventas | Sí (3.º) |
| [`Gemelo_Digital_Thyms.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md) | Cuaderno base (36 celdas, con salidas): revisión del pronóstico, pronóstico a 12 meses, gemelo en SimPy, validación, métricas, restricciones, escenarios y estrés | Sí (4.º) |
| [`Gemelo_Digital_Thyms_MEJORADO.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms_MEJORADO.md) | Cuaderno principal (45 celdas): el base sin cambios + sección 4 (S&OP agregado mensual) + sección 5 (gemelo guiado por el plan frente al de punto de reorden). Las celdas nuevas no tienen salidas guardadas | Sí (5.º) |

**Base frente a MEJORADO:**
- Las celdas 0–35 son idénticas en código y salidas (comprobado comparando los dos `.ipynb`).
- MEJORADO agrega las celdas 36–44:
  - `cargar_plan_agregado()` lee la hoja `Plan Agregado`;
  - `simular_gemelo_sop()` simula mes a mes las estrategias de persecución y nivelada con demanda aleatoria y venta perdida;
  - la clase `GemeloThymsSOP` hereda del gemelo y libera lotes según el plan mensual (lazo abierto) con una demanda dada;
  - `comparar_modelos()` corre 5 modelos con la misma demanda en 30 réplicas.

## Orden de estudio sugerido

1. [`CONTEXTO_GEMELO_THYMS.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/CONTEXTO_GEMELO_THYMS.md): el mapa completo.
2. [`THYMS-presentacion-corte-2.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/THYMS-presentacion-corte-2.md): las conclusiones que se presentaron.
3. [`Datos Thyms Completo.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Datos%20Thyms%20Completo.md): los datos y el plan agregado en Excel.
4. [`Gemelo_Digital_Thyms.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md): pronóstico y gemelo (secciones 1 a 3).
5. [`Gemelo_Digital_Thyms_MEJORADO.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms_MEJORADO.md): secciones 4 y 5.

## Datos

- **Planta** (libro, hojas `Parámetros` a `Mano de Obra`):
  - 22 días hábiles al mes, 2 turnos de 7 h de lunes a viernes;
  - lotes de 500 kg que rinden 7.800 tubos; 24 tubos por caja;
  - demanda base de 100.000 tubos/mes (A 48.000, B 30.000, C 22.000);
  - stock de producto terminado 29.500, bodega 58.000, puntos de reorden 8.000/5.500/4.500, lotes 15.600/7.800/15.600;
  - 6 estaciones con tiempos normales truncados;
  - OEE: llenadora 0,74, mezcla 0,85, encartonado 0,83 y supuestos de 0,88–0,90 para las demás;
  - alistamientos de 70, 155 y 300 min según el cambio;
  - MTBF/MTTR de 5 equipos;
  - 34 operarios.
- **Materia prima:** 3.600 kg de base y colorantes importados (lead time de 40 días) y 60.000 tubos vacíos.
- **Ventas reales** (del Corte 1): ventas mensuales de enero a agosto de 2026 en COP, de las que salen los índices estacionales (julio 1,53; abril 0,35), y 464 facturas de mayo a julio de 161 clientes, de las que sale el tamaño de pedido lognormal (media de 1,27 M COP ≈ 99 tubos).

## Métodos

- **Estudio preliminar** (Excel; $D_p$ = demanda mensual del producto $p$):
  - takt $= 308 \cdot 3.600 / D_p$;
  - utilización $= \sum_p D_p/(y_p\,\text{cap}_{e,p}) / (308 \cdot OEE_e)$;
  - ley de Little: tiempo de flujo = WIP / throughput.
- **Planeación agregada** (Excel, clases [L10](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md) y [L11](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md)):
  - demanda $D_t = 100.000\,s_t$;
  - persecución: $P_t = D_t$; nivelada: $P_t = \bar{D}$; mixta: $P_t = \alpha D_t + (1-\alpha)\bar{D}$;
  - inventario $I_t = I_{t-1} + P_t - D_t$;
  - capacidad $K_t = n_t \cdot 14 \cdot 1.675{,}47$;
  - desagregación 48/30/22 % y lotes $\lceil P_t/7.800 \rceil$.
- **Pronóstico** (cuaderno):
  - SES con origen móvil y $\alpha$ elegido por RMSE;
  - nivel inicial = promedio de 3 meses;
  - pronóstico de planta $N \cdot s_m$ con intervalo del 80 %.
- **Gemelo digital** (SimPy):
  - demanda Poisson + lognormal con choque mensual;
  - punto de reorden con revisión diaria;
  - recorrido del lote por 6 estaciones con 2 reactores;
  - fallas exponenciales en horas de marcha con reparación lognormal;
  - alistamientos dependientes de la secuencia;
  - pérdida de velocidad $OEE/A$;
  - rendimiento binomial;
  - materia prima con revisión periódica;
  - calendario con festivos de Colombia;
  - 16 sensores virtuales;
  - 30 réplicas con números aleatorios comunes.
- **S&OP + gemelo** (MEJORADO):
  - modelo agregado mensual con venta perdida;
  - gemelo que libera lotes según la cuota diaria del plan;
  - comparación con la misma demanda.

## Resultados principales

| Tema | Resultado |
|---|---|
| Escala | La serie de ventas real (~11.705 tubos/mes) es el **11,7 %** de la planta |
| Pronóstico del Corte 1 | Sesgo +63,1 M COP, señal de rastreo 4,72: subestima |
| Pronóstico corregido | SES α = 0,05 con nivel inicial = promedio de 3 meses: RMSE 63,6 M frente a 76,8 M (−17 %), sesgo 2,4 M frente a 44,6 M; nivel de **100.038 tubos/mes**, error mensual ±42 % |
| Utilización (libro) | Llenadora 28,3 % (cuello de botella); demás estaciones de 3 % a 14 % |
| Takt / throughput / flujo / WIP | Libro: 11,1 s; 325 tubos/h; 12,7–14,5 h; 8.500 tubos. Gemelo: 10,3 s; 352 tubos/h; 16,9 h; 5.308 tubos |
| Validación del gemelo | Balance de masa exacto; Little 5.472 = 366 × 14,95; horas de equipo dentro de ±0,7 % |
| Restricciones (gemelo) | Llenadora al 28,9 %; servicio 99,99 %; **C sobre su bodega el 32,3 % de los días**; materia prima mínima de 800 kg |
| Escenarios | Lote de C de 7.800 → 0 % de días sobre la bodega e inventario −10,3 %; un turno → 97,97 % de servicio; compras sin estacionalidad → 6 de 30 réplicas con faltante |
| Estrés | Servicio 99,4 % con 2× la demanda, 93,9 % con 2,5×, 70,8 % con 3×; el libro dice 3,37× porque no ve colas |
| Plan agregado (Excel) | Solo **persecución** es factible: costo de mantener 29,6 M COP; la nivelada excede la bodega 5 meses (pico de 96.346), la mixta 1 mes |
| Materia prima | Cobertura de 13 días frente a 55 requeridos; faltan **11.665 kg** |
| S&OP en el gemelo (MEJORADO) | Con la misma demanda: punto de reorden 99,99 % de servicio; plan de persecución a lazo abierto **79,42 %**; plan nivelado 84,99 % |

## Conceptos y fórmulas clave

- **Ley de Little:** $WIP = TH \times CT$, donde $TH$ es el throughput y $CT$ el tiempo de flujo. Se usa para validar el gemelo. Detalle en [`Gemelo_Digital_Thyms.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md).
- **Takt time:** $T_{takt} = T_{disponible}/D$. Ver la hoja `Métricas` en [`Datos Thyms Completo.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Datos%20Thyms%20Completo.md#hoja-métricas).
- **Capacidad efectiva con mezcla:** $\bar{c} = OEE \cdot \left(\sum_p w_p/c_p\right)^{-1}$ = 1.675,47 tubos/h, donde $w_p$ es la participación del producto y $c_p$ su capacidad de llenado.
- **Estrategias de plan agregado:** persecución, nivelada y mixta, con inventario $I_t = I_{t-1}+P_t-D_t$. Ver [`Datos Thyms Completo.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Datos%20Thyms%20Completo.md#hoja-plan-agregado).
- **Disponibilidad:** $A = MTBF/(MTBF+MTTR)$. La pérdida de velocidad que completa el OEE es $OEE/A$.
- **Pronosticador del gemelo:** $N \leftarrow \alpha\,D^{real}_m/s_m + (1-\alpha)N$ (SES sobre la demanda desestacionalizada; $N$ = nivel, $s_m$ = índice del mes).

## Ejercicios resueltos disponibles

| Ejercicio | Dónde | Resultado principal |
|---|---|---|
| Utilización y cuello de botella | `Datos Thyms Completo`, hoja `Utilizacion` | Llenadora 28,3 % |
| Takt, cycle time, throughput y Little | Hoja `Métricas` | Takt de la familia 11,09 s; flujo 26,2 h; eficiencia de flujo 51 % |
| Plan agregado de 3 estrategias | Hoja `Plan Agregado` | Persecución factible, 29,6 M COP; nivelada 45,3 M y no factible |
| Revisión y elección del pronóstico | `Gemelo_Digital_Thyms`, sección 2 | SES α = 0,05 con nivel promedio; 100.038 tubos/mes |
| Gemelo base, escenarios y estrés | `Gemelo_Digital_Thyms`, sección 3 | Lote de C de 7.800 recomendado; aguanta ~2× la demanda |
| Plan agregado dentro del gemelo | `Gemelo_Digital_Thyms_MEJORADO`, secciones 4 y 5 | Lazo abierto da 79 % de servicio; debe liberar el punto de reorden |

## Supuestos abiertos

Pendientes de confirmar con la empresa (ver también la sección 9 de [`CONTEXTO_GEMELO_THYMS.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/CONTEXTO_GEMELO_THYMS.md)):
- **Escala zona → planta:** los índices estacionales y el nivel salen de un solo vendedor (11,7 % de la planta).
- **Jornada:** 1 turno de 8 h de lunes a sábado en el Corte 1, frente a 2 turnos de 7 h de lunes a viernes en el libro (el gemelo usa el libro).
- **Índices de septiembre a diciembre = 1** (no hay datos).
- **Materia prima en tránsito al inicio:** el stock cubre ~13 días frente a 40 de lead time; el gemelo supone pedidos ya en camino.
- **Supuestos propios del gemelo:** choque mensual del 10 %, CV de reparación de 0,5, sublotes de 600, revisión de compras cada 5 días; OEE de pesaje, control de calidad y empaque supuestos.
- **No modelado:** mano de obra, tubos vacíos y cartón, capacidad de bodega impuesta, reprocesos y estrategia mixta en simulación.
- Las secciones 4 y 5 leen valores calculados del Excel (rompen la regla de «solo datos de entrada») y no tienen salidas guardadas.
- Los resultados de Bowman, flujo en red, MILP de turnos y programa maestro que muestra la presentación (páginas 6–7) no están en ningún archivo de esta carpeta.

## Cómo se conecta con el Corte 1

| Corte 1 ([proyecto-thyms-pronostico](/corte-1-pronosticos/proyecto-thyms-pronostico/)) | Corte 2 (esta carpeta) |
|---|---|
| `VENTAS.xls`: ventas mensuales de 2026 y 464 facturas | Copiadas en las hojas `Ventas` y `Facturas Mayo-Julio`; dan los índices estacionales y la distribución del tamaño de pedido |
| SES α = 0,05 con $F_1$ = enero: MAD 80,2 M, MAPE 53,4 %, agosto 114,7 M | Sección 2.1: se reproduce y se muestra el sesgo (+63,1 M, señal de rastreo 4,72); la sección 2.2 lo corrige con nivel inicial = promedio de 3 meses |
| 12.900 COP/tubo | Se mantiene (`PRECIO_UND`) para pasar de COP a tubos y escalar a la planta (×8,54) |
| Takt 0,69 min (41,5 s), throughput 86,7 tubos/h, WIP 304–477 (zona, 8 h/día) | Sección 3.5: comparados con el libro (11,1 s; 325; 8.500) y el gemelo (10,3 s; 352; 5.308) |
| Tiempo de ciclo de 3,5–5,5 h (dato de la empresa) | Coherente con pesaje + mezcla + control de calidad = 3,9–5,0 h por lote |
| Días hábiles con festivos (cuaderno de Colab) | Calendario de festivos de Colombia programado (`festivos_colombia()`) |

## Relación con otros temas y proyectos

- Planeación agregada y modelo de Bowman (la presentación dice haberlo aplicado a THYMS): [01-planeacion-agregada-modelo-bowman](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/).
- Agregación y desagregación (tubos, kg, horas-hombre; plan por producto): [02-agregacion-y-desagregacion](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/).
- Siguiente paso propuesto (dimensionar lotes del programa maestro): [03-wagner-whitin-y-silver-meal](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/).
- Materia prima con lead time y MRP: [04-bom-y-mrp](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/) y [05-mrp-ii-y-capacidad](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/).
- Pronósticos (SES, señal de rastreo, estacionalidad): [04-datos-estacionarios-promedio-movil-y-suavizacion-simple](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/) y [06-estacionalidad-winters-y-tracking-signal](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/).
- Métricas de desempeño (takt, throughput, WIP, Little): [L02](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L02-introduction-to-production-systems.md).


---

<!-- fuente: corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/CONTEXTO_GEMELO_THYMS.md -->
# Contexto completo: pronóstico y gemelo digital de THYMS Colombia

Documento de traspaso para un agente que va a continuar este trabajo. Estado al 2026-10-05.

---

## 1. El proyecto

- **Curso:** Planeación y Control de la Producción, 7.º semestre.
- **Empresa:** THYMS Colombia S.A.S., que fabrica tintes para el cabello en tubos de 60 g. Hay tres productos de una misma familia:

  | Código | Producto | Nota |
  |---|---|---|
  | A | Kolorezza permanente 60 g (THY-KZ060) | Con amoníaco |
  | B | Visalia sin amoníaco 60 g (THY-VS060) | Sin amoníaco; cambiar a B o desde B exige la limpieza más larga |
  | C | Thym's Coloring permanente 60 g (THY-TC060) | Con amoníaco |

- **Entregable del Corte 2:**
  - Estudio preliminar del sistema: WIP, takt time, throughput, cycle time y restricciones de capacidad, demanda y almacenamiento.
  - **Gemelo digital** en ARENA o Python, que incluya el pronóstico, la estacionalidad y sensores virtuales.
- **Idioma:** todo el trabajo es en **español**: código, comentarios, textos del cuaderno y respuestas al usuario.

---

## 2. Archivos

Carpeta raíz: `C:\Users\samue\Desktop\U\S7\PLEANCION\`

### Corte 2 (`CORTE 2/`): la base actual

| Archivo | Qué es | Estado |
|---|---|---|
| `Gemelo_Digital_Thyms MEJORADO.ipynb` | **Cuaderno principal.** Secciones 1 a 5 | Revisado a fondo. Llegó sin la extensión `.ipynb` y se le agregó el 2026-10-05 |
| `Gemelo_Digital_Thyms.ipynb` | Versión anterior (2026-10-01). Sus celdas 0–35 son **idénticas** a las celdas 0–35 de la versión MEJORADO | Revisado |
| `Datos Thyms Completo.xlsx` | Libro con todos los parámetros de la planta. Es la **única fuente de datos** del cuaderno | Revisado |
| `BOWMAN.xlsx`, `MODELO DE DESAGREGACION.xlsx`, `MRP.xlsx`, `MRP 2.xlsx`, `wagner_whitin.py`, `MODELO DE FLUJO.gms` (GAMS, con sus `.log`, `.lst` y `.lxi`) | Otros trabajos del corte | **No revisados** |

### Corte 1 (`CORTE 1/PROYECTO/`)

| Archivo | Qué es |
|---|---|
| `Planeacion_proyecto_corte1.ipynb`, `PRONOSTICO EXPO SIMPLE.xlsx`, `PRONOSTICO EXPO SIMPLE PPCO.xlsx`, `VENTAS.xls` | Pronóstico del Corte 1 (no revisados en detalle) |

Lo que se sabe del Corte 1:
- Usó las ventas reales de un solo vendedor (código 401, zona Antioquia): 8 meses de 2026 en COP y 464 facturas de mayo a julio.
- Pronosticó con suavización exponencial simple, α = 0,05.
- Pasó de pesos a tubos con 12.900 COP por tubo.
- Supuso 1 turno de 8 h de lunes a sábado.

---

## 3. El libro de Excel: `Datos Thyms Completo.xlsx`

Hojas: Parámetros, Productos, Tiempos, Utilizacion, Alistamiento, Fallas, Mano de Obra, Métricas, Plan Agregado, Restricciones, Proceso Planeación Agregada, Facturas Mayo-Julio, Clientes, Ventas.

> **Privacidad:** las hojas `Facturas Mayo-Julio` y `Clientes` tienen nombres y cédulas de clientes reales. **No las reproduzcas** en documentos ni salidas. El cuaderno solo usa el valor en COP de cada factura (columna E).

### Celdas que lee `cargar_datos()`

Solo se leen **datos de entrada**; las fórmulas se recalculan en Python.

| Hoja | Celdas | Dato |
|---|---|---|
| Parámetros | B4, B5, B6, B9, B10 | Días hábiles por mes, turnos, horas por turno, tubos por lote, unidades por caja |
| Productos | Filas 5–7. Columnas: A (nombre), C (demanda), E (rendimiento), I (stock), K (bodega), L (punto de reorden), M (lote), N (WIP), O (kg de materia prima) | Datos de cada producto. Hay un `assert` que exige que L4 empiece por "Punto de reorden" |
| Productos | E12 | Tiempo de entrega de la materia prima (días calendario) |
| Tiempos | Filas 5–22. Columnas: A (estación), B (producto), C (unidad), D (promedio), E (desviación), I (rango ±%) | Tiempos de proceso |
| Utilizacion | A5:A10 y E5:E10 | OEE de cada estación |
| Alistamiento | B5:D7 (en minutos) | Filas: cambio de tono, A↔C, A/C↔B. Columnas: reactor, llenadora, encartonadora |
| Fallas | A5:C9 | MTBF y MTTR de cada equipo |
| Ventas | B5:B12 | Ventas en COP de enero a agosto de 2026 |
| Facturas Mayo-Julio | Columna E, desde la fila 5 hasta que la columna A quede vacía | COP de cada uno de los 464 pedidos |

### Valores clave

**Parámetros generales**
- 22 días hábiles al mes.
- 2 turnos de 7 h (de 6:00 a 14:00 y de 14:00 a 22:00, lunes a viernes), es decir, 14 h por día.
- Un lote de 500 kg rinde 7.800 tubos.
- 24 tubos por caja master.

**Productos**

| Producto | Demanda (tubos/mes) | Rendimiento | Stock de PT | Bodega | Punto de reorden | Lote | WIP | Materia prima (kg) | Costo de mantener (COP por tubo al mes) |
|---|---|---|---|---|---|---|---|---|---|
| A | 48.000 | 0,985 | 14.000 | 26.000 | 8.000 | 15.600 | 4.000 | 1.600 | 78,83 |
| B | 30.000 | 0,975 | 8.500 | 18.000 | 5.500 | 7.800 | 2.500 | 1.100 | 102,67 |
| C | 22.000 | 0,988 | 7.000 | 14.000 | 4.500 | 15.600 | 2.000 | 900 | 67,83 |
| **Total** | **100.000** | | **29.500** | **58.000** | | | **8.500** | **3.600** | |

**Materias primas**
- Base y colorantes: importados, 3.600 kg en stock, tiempo de entrega de 40 días calendario. El cuaderno lo pasa a unos 29 días hábiles.
- Tubos vacíos: 60.000 en stock, tiempo de entrega de 12 días. **El gemelo no los modela.**

**Tiempos promedio**

| Estación | Unidad | A | B | C |
|---|---|---|---|---|
| Pesaje | min/lote | 40 | 45 | 40 |
| Mezcla | min/lote | 150 | 180 | 140 |
| Control de calidad | min/lote | 60 | 75 | 55 |
| Llenado | tubos/h | 2.400 | 2.000 | 2.400 |
| Encartonado | tubos/h | 3.000 | 3.000 | 3.000 |
| Empaque | cajas/h | 110 | 110 | 110 |

**OEE por estación:** pesaje 0,90 · mezcla 0,85 · control de calidad 0,90 · **llenado 0,74** · encartonado 0,83 · empaque 0,88.

**Fallas (MTBF / MTTR, en horas)**

| Equipo | MTBF | MTTR |
|---|---|---|
| Reactor 1 | 180 | 3 |
| Reactor 2 | 160 | 3,5 |
| Llenadora | 70 | 2 |
| Encartonadora | 120 | 1,5 |
| Empaque | 200 | 1 |

**Alistamiento (minutos, reactor / llenadora / encartonadora)**

| Tipo de cambio | Reactor | Llenadora | Encartonadora |
|---|---|---|---|
| Solo cambia el tono | 25 | 35 | 10 |
| A ↔ C | 60 | 75 | 20 |
| A/C ↔ B | 120 | 150 | 30 |

**Ventas de 2026 (COP)**

| Mes | Ene | Feb | Mar | Abr | May | Jun | Jul | Ago |
|---|---|---|---|---|---|---|---|---|
| Ventas | 95.752.306 | 153.850.391 | 201.004.440 | 52.446.770 | 197.484.330 | 156.580.280 | 230.979.600 | 119.882.540 |
| Índice estacional | 0,63 | 1,02 | 1,33 | 0,35 | 1,31 | 1,04 | 1,53 | 0,79 |

Septiembre a diciembre no tienen datos; su índice está puesto en 1.

**Mano de obra:** 17 operarios por turno, 34 en total. La hora ordinaria cuesta 13.800 COP. **El gemelo no la modela.**

**Hoja `Plan Agregado`** (todo son fórmulas, salvo B4 y B10)
- Parámetros:
  - B4 = α de la estrategia mixta (0,5).
  - B5 = inventario inicial (29.500).
  - B6 = bodega (58.000).
  - B7 = capacidad efectiva de la llenadora (1.675,47 tubos/h).
  - B8 = 14 h efectivas por día.
  - B9 = costo de mantener ponderado (83,56 COP por tubo al mes).
  - B10 = estrategia elegida (1 = persecución, 2 = nivelada, 3 = mixta).
- Tabla mensual en las filas 14–25 (enero a diciembre):
  - Columnas A–E: mes, días hábiles (246 en total), índice, demanda y capacidad.
  - Producción: persecución en F, nivelada en I, mixta en L.
- Comparación en las filas 31–43. Según el Excel, solo persecución es factible: nivelada pasa 5 meses sobre la bodega y mixta 1.

**Hoja `Restricciones`**
- Factor de demanda máximo antes de saturar la llenadora: 3,37.
- Stock de seguridad de materia prima: 15 días hábiles.
- Faltante de materia prima frente al stock requerido: 11.665 kg.

---

## 4. El cuaderno `Gemelo_Digital_Thyms MEJORADO.ipynb`

Tiene 45 celdas. Se ejecuta desde la carpeta `CORTE 2/`, porque lee `ARCHIVO = "Datos Thyms Completo.xlsx"` con ruta relativa.

### Mapa de celdas

| Celdas | Sección | Contenido |
|---|---|---|
| 0–1 | Título · 1. Configuración y datos | Markdown |
| 2 | | Librerías: math, datetime, numpy, pandas, matplotlib, scipy.stats, openpyxl, simpy |
| 3 | **Configuración** | Todos los supuestos editables (ver abajo) y las funciones de formato `es()` y `tabla()` |
| 4–5 | | `cargar_datos(ruta)` devuelve el diccionario `D` (`par`, `prod`, `mp`, `tiempos`, `oee`, `alist`, `fallas`, `ventas`, `facturas`) |
| 6 | | Escala de la zona a la planta: `ESCALA = 100.000 / (venta promedio / 12.900)`, que da unos 8,54 |
| 7–8 | 2.1 Revisión del pronóstico del Corte 1 | `ses()` y `metricas()` |
| 9–11 | 2.2 Elección del método | Prueba de tendencia, `origen_movil()`, 7 métodos comparados, búsqueda de `ALPHA` |
| 12–14 | 2.3 Pronóstico a 12 meses | `NIVEL_PLANTA`, `INDICES`, `pron12` con intervalo del 80 % y su gráfica |
| 15–16 | 2.4 Pronosticador del gemelo | Clase `Pronosticador` y diccionario `PRON` (nivel, α, índices, parámetros lognormales del tamaño de pedido) |
| 17 | 3.1 Qué representa | Diagrama y tabla de cómo se modela cada elemento |
| 18 | | Calendario: `pascua()`, `festivos_colombia()` (con ley Emiliani), `dias_habiles()` |
| 19–20 | 3.2 El modelo | `CFG_BASE`, `lognormal_media()`, clases `Maquina` y `GemeloThyms`, función `replicar()` |
| 21–22 | 3.3 Validación | Balance de masa, ley de Little, horas de equipo frente al libro |
| 23–28 | 3.4 Corrida base con sensores | Telemetría, modo en vivo, gráfica de inventario y gráfica de una semana de la llenadora |
| 29–30 | 3.5 Métricas de eficiencia | Takt, throughput, flujo y WIP: Corte 1 frente a libro frente a gemelo |
| 31–32 | 3.6 Restricciones | Capacidad, demanda, almacenamiento y materia prima, con intervalo del 95 % |
| 33–35 | 3.7 Escenarios | 6 escenarios y prueba de estrés con factor de demanda de 1 a 3,5 |
| 36–40 | **4. S&OP agregado** (nuevo) | `cargar_plan_agregado()`, `simular_gemelo_sop()`, persecución frente a nivelada y gráfica |
| 41–44 | **5. Comparación con la misma demanda** (nuevo) | Clase `GemeloThymsSOP`, `kpis_gemelo()`, `kpis_agregado()`, `comparar_modelos()`, tablas y gráfica |

### Configuración (celda 3)

| Parámetro | Valor | Significado |
|---|---|---|
| `PRECIO_UND` | 12.900 | COP por tubo (del Corte 1) |
| `INDICE_SUPUESTO` | {9: 1, 10: 1, 11: 1, 12: 1} | Índice estacional de septiembre a diciembre (supuesto) |
| `CV_CHOQUE_MENSUAL` | 0,10 | Choque mensual de la demanda (supuesto) |
| `INICIO`, `MESES` | 2026-09-01, 12 | Horizonte: septiembre de 2026 a agosto de 2027 |
| `SUBLOTE` | 600 | Tubos que pasan juntos de llenado a encartonado (25 cajas) |
| `KG_LOTE` | 500 | kg de materia prima por lote |
| `CV_MTTR` | 0,5 | Variación del tiempo de reparación (supuesto) |
| `SS_MP_DIAS` | 15 | Stock de seguridad de materia prima en días hábiles |
| `REVISION_MP_DIAS` | 5 | Periodo de revisión de compras |
| `N_REP`, `SEMILLA` | 30, 2026 | Réplicas por escenario y semilla base |

**Estilo:**
- `MES`, `PRODS = ["A","B","C"]`.
- `COLOR = {A: #2a78d6, B: #eb6834, C: #1baf7a, gris: #898781}`.
- `rcParams`: sin bordes superior ni derecho, rejilla `#e1e0d9` y títulos en negrita alineados a la izquierda.
- `es(x, d)` formatea números en español (1.234.567,8).
- `tabla(df, dec)` aplica `es()` a todas las columnas numéricas de un DataFrame.

---

## 5. Sección 2: pronóstico

### 2.1 Revisión del Corte 1
SES con α = 0,05 y nivel inicial igual a la venta de enero. Se evalúa de febrero a julio.

| Métrica | Valor |
|---|---|
| MAD | 80,2 M COP |
| MAPE | 53,4 % |
| Sesgo | **+63,1 M COP** (subestima) |
| Señal de rastreo | **4,72**, fuera del límite de ±4 |
| Agosto | Pronóstico de 114,7 M frente a 119,9 M reales |

Causa: enero fue un mes bajo y, con α pequeño, el nivel casi no se mueve desde ese arranque.

### 2.2 Elección del método
- **Tendencia:** regresión lineal con pendiente de 6,74 M COP/mes y valor p = 0,51. No es significativa.
- **Comparación:** origen móvil (con los meses 1..k se pronostica el mes k+1, para k ≥ 3).
- **α:** se busca en una rejilla de 0,05 a 0,95 minimizando el RMSE. El óptimo es α = 0,05, el extremo inferior de la rejilla.

| Método | MAD | RMSE | MAPE | Sesgo | Señal de rastreo |
|---|---|---|---|---|---|
| **SES α=0,05, nivel inicial = promedio de 3 meses (ELEGIDO)** | 54,7 | **63,6** | 56,3 % | 2,4 | 0,22 |
| Promedio histórico | 61,9 | 69,3 | 60,2 % | 8,6 | 0,69 |
| Promedio móvil (3) | 67,3 | 75,1 | 65,1 % | −1,9 | −0,14 |
| SES del Corte 1 | 65,2 | 76,8 | 47,3 % | 44,6 | 3,42 |
| Regresión lineal | 92,6 | 111,6 | 109,4 % | −31,8 | −1,72 |
| Ingenuo | 104,0 | 111,9 | 101,5 % | −16,2 | −0,78 |
| Holt (0,3; 0,3) | 106,7 | 127,5 | 126,1 % | −106,7 | −5,00 |

MAD, RMSE y sesgo están en millones de COP.

### 2.3 Pronóstico a 12 meses
- **Nivel:** `NIVEL_COP` = 151,06 M COP/mes, que da `NIVEL_PLANTA` = **100.038 tubos/mes**.
- **Error típico de un mes** (fuera de muestra): `SIGMA_REL` = 42 %.
- **Intervalo del 80 %:** ±1,2816 × 42 %.
- **Pronóstico de cada mes** = nivel × índice. Por ejemplo, julio de 2027 da 153.027 tubos (de 70.424 a 235.631).
- La estacionalidad se trata como **escenario**: con un solo año incompleto no se puede validar.

### 2.4 Pronosticador
- `Pronosticador(nivel, alpha, indices, peso_estacional)` tiene los métodos `.pronostico(mes)` y `.actualizar(mes, demanda_real)`. El segundo aplica SES sobre la demanda desestacionalizada.
- **Tamaño de pedido:** lognormal ajustada a las 464 facturas. Promedio de 1.273.304 COP, unos 99 tubos.

---

## 6. Sección 3: el gemelo digital (núcleo del cuaderno)

Simulación de eventos discretos con **SimPy**. El reloj está en **horas de turno**: 1 día hábil = `H` = turnos × horas por turno = 14 h. Los días son de lunes a viernes, sin festivos de Colombia. Septiembre de 2026 a agosto de 2027 son 245 días hábiles.

### `CFG_BASE`: interruptores de los escenarios

```python
turnos=None                 # None = los del libro (2)
factor_demanda=1.0
peso_estacional_real=1.0    # 0 = demanda plana
peso_estacional_pron=1.0    # cuánta estacionalidad conoce el planeador
cv_choque_mensual=CV_CHOQUE_MENSUAL
politica="rop_fijo"         # o "rop_pronostico" (el punto de reorden se escala con la demanda diaria pronosticada)
lote=None                   # dict por producto para cambiar el lote del libro
modelar_mp=True
sensores=False, dt_sensor=1.0
```

### Clase `Maquina`
- **Estados:** libre, marcha, alistamiento, falla. Acumula `horas[estado]`.
- **Fallas por horas de marcha:**
  - `vida` ~ Exponencial(MTBF) y solo se consume en marcha.
  - Al agotarse, la máquina pasa a falla; la reparación dura una lognormal con media MTTR y CV = `CV_MTTR`.
  - Luego se sortea una vida nueva y el trabajo continúa.
- **Desempeño:** `desempeno = OEE / disponibilidad`, con disponibilidad = MTBF/(MTBF+MTTR). Esta pérdida de velocidad completa el OEE del libro.
- **Métodos:** `alistar(horas)` y `operar(horas, velocidad)` son generadores; se usan con `yield from`.

### Clase `GemeloThyms(D, PRON, cfg, semilla)`

**Recursos**
- Pesaje, Control de calidad, Encartonadora y Empaque: `simpy.Resource(1)`.
- Llenadora: `PriorityResource(1)`, con prioridad = orden de llegada del lote. Así un lote se llena completo antes de que entre otro.
- Reactores: `simpy.Store` con 2 máquinas.

**Ciclo diario `_dias()`.** Cada día hábil:
1. **`_abrir_mes`**, si cambia el mes:
   - el pronóstico se actualiza con la demanda que el gemelo midió el mes anterior;
   - `tasa_dia[p]` = demanda base × factor × índice (con peso real) × choque lognormal(1, CV) / días hábiles del mes;
   - con `rop_pronostico`, el punto de reorden se escala por la relación entre la demanda diaria pronosticada y la del libro.
2. **`_demanda_del_dia`:**
   - número de pedidos ~ Poisson(tasa / pedido medio);
   - tamaño ~ lognormal de las facturas, dividido por 12.900;
   - se despacha desde la bodega (`pt`) y lo que no alcanza queda en `pendiente` (**backorders**).
3. **`_revisar_produccion`:**
   - posición = `pt + en_proceso − pendiente`;
   - mientras posición ≤ punto de reorden, se lanzan `round(Q/7.800)` lotes de 7.800 tubos (A y C: 2 lotes; B: 1) y la posición sube en Q.
4. **Cada 5 días, `_revisar_mp(d)`:**
   - objetivo = consumo pronosticado en (tiempo de entrega + 5 + 15) días hábiles;
   - se pide el objetivo − (existencia + en tránsito), redondeado hacia arriba a múltiplos de 500 kg;
   - el pedido llega después del tiempo de entrega.
5. **Registro:** se guarda en `diario` la materia prima, `pt_A/B/C` y `pend_A/B/C`.

**Materia prima inicial.** Hay 3.600 kg en stock, y se **supone** que ya hay pedidos en tránsito: lo que falta para el objetivo se reparte en `lt_mp // 5` pedidos que llegan escalonados.

**Recorrido de un lote, `_lote()`:**
1. `mp.get(500)`; la espera se acumula en `espera_mp`.
2. Pesaje.
3. Reactor libre del Store, con alistamiento según el cambio de producto: el mismo producto o el primero cuenta como "tono"; si interviene B, "B"; si no, "AC".
4. Mezcla.
5. Control de calidad.
6. Llenadora: 13 sublotes de 600 tubos, con alistamiento solo en el primero. La velocidad real es el tiempo muestreado × desempeño.
7. Cada sublote lanza `_sublote()`.

**`_sublote()`:**
1. Encartonadora, con alistamiento si cambia el lote.
2. Empaque (la velocidad en cajas/h se multiplica por 24).
3. Tubos buenos ~ Binomial(600, rendimiento).
4. Los buenos atienden primero los pendientes y el resto va a `pt`.
5. Se registran el flujo del sublote y el flujo del lote (en el último sublote).

**Tiempos:** `_muestra(estacion, p)` sortea una normal (promedio, desviación) y la repite hasta que cae entre el mínimo y el máximo.

**Sensores virtuales: `lectura()`** devuelve 16 variables:
- `t_h` y `momento` (fecha y hora real);
- estado y velocidad de la llenadora (con ruido del 1 %);
- contadores de llenado y de empaque;
- estados de los reactores 1 y 2, la encartonadora y el empaque;
- `pt_A/B/C`, `wip_tubos`, `pendiente_und` y `mp_kg`.

Con `sensores=True` se toma una lectura cada `dt_sensor` horas y se guarda en `tele`.

**Uso:**
- `iniciar()` registra los procesos y permite avanzar paso a paso con `env.run(until=...)` (modo en vivo).
- `correr()` simula el año completo.

**`kpis()`** devuelve:
- `nivel_servicio_%` (despacho inmediato), `pendiente_max_und`, `pt_prom_und`, `pt_max_und`;
- `dias_sobre_bodega_%` y `dias_{A,B,C}_sobre_bodega_%`;
- `takt_s_und`, `throughput_und_h`, `flujo_lote_h`, `flujo_tubo_h`, `wip_prom_tubos` (área bajo la curva / T), `lotes`;
- `ocup_{pesaje,mezcla,calidad,llenadora,encartonadora,empaque}_%`, que suman marcha + alistamiento + falla;
- `mp_min_kg` y `espera_mp_h`.

**Réplicas:** `replicar(cfg, n=30, semilla=2026)` usa las semillas 2026 + i. Los flujos aleatorios son tres: `rng` (semilla), `rng_sensor` (semilla + 10.000) y, en la sección 5, la demanda (semilla + 20.000).

### Resultados (salidas guardadas en el cuaderno)

**3.3 Validación** (demanda plana, sin choques, sin materia prima)
- Balance de masa: 29.500 + 1.234.289 − 1.224.545 = 39.244, que es igual a inventario final − pendientes. ✔
- Ley de Little: WIP de 5.472 = 366 tubos/h × 14,95 h. ✔
- Horas de equipo, gemelo frente a libro (unidades / capacidad / OEE): diferencias de −0,7 % a +0,7 % en las 6 estaciones. ✔

**3.4 Corrida base**
- 3.431 lecturas horarias de 16 variables.
- Gráfica de inventario: C hace un diente de sierra que llega a unos 19.000 tubos con una bodega de 14.000.

**3.5 Métricas de eficiencia** (30 réplicas)

| | Corte 1 (zona, 8 h/día) | Libro | Gemelo |
|---|---|---|---|
| Takt time | 41,5 s/tubo | 11,1 s/tubo | 10,3 s/tubo |
| Throughput | 86,7 tubos/h | 325 tubos/h | 352 tubos/h |
| Tiempo de flujo | 3,5 a 5,5 h | 12,7 a 14,5 h por lote | 16,9 h por lote |
| WIP | 304 a 477 tubos | 8.500 tubos | 5.308 tubos |

Pesaje + mezcla + control de calidad según el libro: 3,9 a 5,0 h por lote, coherente con las 3,5–5,5 h que reportó la empresa.

**3.6 Restricciones** (promedio ± intervalo del 95 %)
- Ocupación: llenadora **28,9 % ± 0,4** (cuello de botella), reactores 10,5 %, encartonadora 16,0 %, empaque 15,4 %.
- Nivel de servicio: 99,99 %. Pedidos pendientes máximos: unos 0.
- Inventario total máximo: 49.226 frente a una bodega de 58.000.
- **Días con C sobre su bodega: 32,3 % ± 1,1.** Causa: punto de reorden + lote de C = 20.100, mayor que su bodega de 14.000.
- Materia prima mínima: 800 kg ± 152. En 3 de 30 réplicas algún lote esperó materia prima.

**3.7 Escenarios** (mismas semillas)

| Escenario | Servicio | Inventario promedio | Días con C sobre su bodega | Llenadora | Flujo por lote | Réplicas con faltante de MP |
|---|---|---|---|---|---|---|
| Base (política del libro) | 99,99 % | 34.697 | 32,3 % | 28,9 % | 16,9 h | 3 |
| Sin estacionalidad | 100,00 % | 34.724 | 32,3 % | 29,0 % | 16,8 h | 0 |
| Punto de reorden ajustado con el pronóstico | 99,97 % | 36.740 | 36,9 % | 28,7 % | 17,1 h | 1 |
| Compras con pronóstico sin estacionalidad | 99,85 % | 34.627 | 32,1 % | 28,9 % | 16,9 h | **6** |
| **Lote de C de 7.800** | 99,96 % | **31.108** | **0,0 %** | 29,5 % | 16,1 h | 1 |
| Un solo turno | 97,97 % | 28.240 | 19,9 % | 57,5 % | 18,3 h | 1 |

**Prueba de estrés** (`rop_pronostico`, sin materia prima)

| Factor de demanda | 1,0 | 1,5 | 2,0 | 2,5 | 3,0 | 3,5 |
|---|---|---|---|---|---|---|
| Ocupación de la llenadora | 28,7 % | 43,3 % | 57,9 % | 72,2 % | 85,9 % | 94,3 % |
| Nivel de servicio | 100,0 % | 99,9 % | 99,4 % | 93,9 % | 70,8 % | 43,9 % |

En la práctica la planta aguanta unas 2 veces la demanda actual con un servicio de al menos 99 %. El Excel calcula 3,37 veces porque no considera colas ni variabilidad.

### Qué NO modela el gemelo
- Mano de obra (se supone que siempre hay operarios).
- Tubos vacíos y cartón.
- La capacidad de la bodega se **mide**, no se impone.
- Reprocesos: los tubos defectuosos se descartan.

---

## 7. Secciones 4 y 5 (agregadas en la versión MEJORADO)

> **Estado:** al 2026-10-05 las celdas 36–44 **no tenían salidas guardadas**. Se ejecutaron en una copia aparte: corren sin errores y la sección 5 tarda unos 10 s. Los números de abajo vienen de esa corrida. Si el usuario ya ejecutó el cuaderno, verifica contra sus salidas.

### Sección 4: S&OP agregado
- **`cargar_plan_agregado(ruta=None, hoja="Plan Agregado")`:**
  - lee la hoja con `pd.read_excel(header=None)` y busca los parámetros por texto en la columna A, normalizando tildes con `_norm()`;
  - ubica la fila "Mes" y saca los nombres de las estrategias de la fila anterior;
  - devuelve `df_plan` con las columnas Mes, Días hábiles, Demanda Plan, Prod persecucion, Prod nivelada y Prod mixta, y `PRM_SOP` (inv_inicial, cap_bodega, vel_llenadora, horas_dia, costo_hold).
- **`simular_gemelo_sop(df_plan, estrategia, variabilidad_demanda=0.05, seed=42)`** avanza 1 paso por mes en SimPy:
  - demanda ~ normal truncada en 0, con σ = 5 % de la media;
  - producción = mín(plan, días × 14 h × 1.675 tubos/h);
  - inventario final = máx(0, inicial + producción − demanda): la venta no atendida **se pierde**;
  - marca los meses sobre la bodega y calcula el costo = inventario final × 83,56.

**Resultado con semilla 42**

| | Persecución | Nivelada |
|---|---|---|
| Inventario final máximo | 28.455 | 86.700 |
| Meses sobre la bodega | 0 | 4 (enero, febrero, abril, mayo) |
| Desabastecimiento | 0 | 7.799 (julio) |
| Costo de inventario al año | 18,72 M COP | 38,30 M COP |

### Sección 5: el plan dentro del gemelo detallado, con la misma demanda
**`GemeloThymsSOP(D, PRON, cfg, semilla, demanda_mes, plan_prod=None, compensar_rend=True)`** hereda de `GemeloThyms` y cambia lo siguiente:
- **Calendario:** pone temporalmente la variable global `INICIO = INICIO_PLAN` (2026-01-01) durante `super().__init__` y la restaura con try/finally.
- **Demanda dada:** reparte la demanda mensual dada en A/B/C (48/30/22 %) y en pedidos diarios (Poisson + lognormal, con su propio rng = semilla + 20.000), reescalados para que cada mes sume exactamente. Sobrescribe `_demanda_del_dia`.
- **Producción:**
  - sin `plan_prod`, usa el punto de reorden normal;
  - con `plan_prod`, la cuota diaria es plan × participación / días hábiles / rendimiento. Se acumula en `credito` y se lanza un lote de 7.800 cada vez que el crédito lo alcanza (lazo abierto).

**`comparar_modelos(df_plan, n_rep=30)`:** en cada réplica corre las simulaciones agregadas de persecución y nivelada. Su demanda alimenta los 3 gemelos: punto de reorden, plan de persecución y plan nivelado.

**Días hábiles:** el plan cuenta 246 y el calendario del gemelo 243. Meses con diferencia (plan / gemelo): abril 21/20, mayo 21/19, junio 20/19, agosto 20/19, octubre 20/21, noviembre 20/19, diciembre 19/21.

**Resultados** (30 réplicas, ± intervalo del 95 %)

| KPI | Gemelo con punto de reorden | Gemelo + Persecución | Gemelo + Nivelada | Agregado Persecución | Agregado Nivelada |
|---|---|---|---|---|---|
| Demanda anual | 1.204.081 | = | = | = | = |
| Producción anual | 1.210.571 | 1.188.007 | 1.187.973 | 1.200.000 | 1.200.000 |
| Nivel de servicio | **99,99 %** | **79,42 % ± 5,76** | 84,99 % ± 4,46 | 99,99 % | 99,79 % |
| No atendido de inmediato | 115 | 249.252 | 182.005 | 145 | 2.546 |
| Inventario promedio a fin de mes | 35.341 | 14.643 | 29.867 | 26.379 | 43.234 |
| Inventario máximo a fin de mes | 43.802 | 24.371 | 78.098 | 36.472 | 94.865 |
| Meses sobre la bodega (de 12) | 0,0 | 0,0 | 1,5 | 0,1 | 3,9 |
| Días sobre la bodega | 0,0 % | 0,0 % | 9,7 % | — | — |
| Costo de inventario al año | 35,44 M | 14,68 M | 29,95 M | 26,45 M | 43,35 M |
| Ocupación de la llenadora | 29,4 % | 30,1 % | 30,1 % | 20,7 % | 20,8 % |

**Por qué persecución da 79 % en el gemelo** (comprobado con un diagnóstico de una réplica):
1. El plan es fijo en 1,2 M y no corrige cuando la demanda real sale mayor.
2. Al cierre del año quedan unos 12.000 tubos de crédito sin lanzar, por el redondeo a lotes completos.
3. Se producen unos 1,19 M frente a una demanda de unos 1,20–1,22 M, y el inventario se drena de 29.500 hasta casi 0.
4. Con poco colchón y lotes de 7.800 que llegan a saltos, hay quiebres frecuentes dentro del mes.

El modelo agregado no lo ve porque solo mira el cierre de cada mes y da por perdida la venta no atendida.

---

## 8. Advertencias y deuda técnica conocida

1. **La tabla "Mejor modelo" de la sección 5 engaña:** declara a persecución la mejor en inventario y costo, pero sale barata porque está desabastecida (79 % de servicio). Hay que comparar con el mismo nivel de servicio o agregar un costo de faltante.
2. **El agregado y el detallado miden distinto:**
   - el agregado da por perdidas las ventas y mide a fin de mes; el gemelo usa pendientes y mide a diario;
   - la ocupación del agregado es producción / capacidad, mientras que la del gemelo son horas de marcha + alistamiento + falla.
3. **Las secciones 4 y 5 rompen la regla "solo datos de entrada":** leen resultados de fórmulas del Excel (los valores cacheados de `pd.read_excel`). Si el libro se modifica sin recalcular en Excel, leerán valores viejos o `NaN`.
4. **La estrategia mixta** se carga, pero no se simula (`ESTRATEGIAS_SOP = ["Persecucion", "Nivelada"]`).
5. **Calendario:** la diferencia de días hábiles entre el plan (246) y el gemelo (243).
6. **Código:**
   - la celda 37 reimporta `scipy.stats`;
   - `GemeloThymsSOP` modifica la global `INICIO`; funciona, pero es frágil;
   - `kpis_agregado` usa la utilización promedio, no la máxima;
   - en la tabla "Mejor modelo", "Días sobre bodega" puede declarar ganador con una ventaja de 0,0 en vez de empate.
7. **El α óptimo quedó en el extremo de la rejilla (0,05):** el SES se comporta casi como el promedio histórico.

## 9. Supuestos abiertos (confirmar con la empresa)

- Escala de la zona a la planta: la serie real es el 11,7 % de la planta.
- Jornada: 1 turno de 8 h de lunes a sábado en el Corte 1, frente a 2 turnos de 7 h de lunes a viernes en el libro. El gemelo usa el libro.
- Índices estacionales de septiembre a diciembre = 1.
- Pedidos de materia prima en tránsito al inicio: el stock actual cubre unos 13 días frente a 40 de tiempo de entrega.
- Supuestos propios del gemelo: choque mensual del 10 %, CV de reparación de 0,5, sublotes de 600, revisión de compras cada 5 días.

## 10. Conclusiones vigentes

1. El pronóstico del Corte 1 estaba sesgado. Corregido (SES con α = 0,05 y nivel inicial = promedio de 3 meses), la demanda queda en unos 100.000 tubos/mes, sin tendencia y con ±42 % de error mensual.
2. El gemelo está validado: cuadran el balance de masa, la ley de Little y las horas frente al libro (±1 %).
3. Sobra capacidad: la llenadora trabaja al 29 % y la planta aguanta unas 2 veces la demanda con un servicio de al menos 99 %.
4. El problema real es la bodega de C. **Recomendación: bajar el lote de C a 7.800 tubos.**
5. Las compras de materia prima deben usar el pronóstico con estacionalidad.
6. Plan agregado:
   - la nivelada no cabe en la bodega;
   - la de persecución sirve para planear capacidad y compras;
   - la liberación diaria de lotes debe reaccionar al inventario (lazo cerrado), porque seguir el plan a ciegas da 79 % de servicio.

## 11. Cómo ejecutar y convenciones de trabajo

- **Entorno:**
  - Python 3.12.10 en `C:\Users\samue\AppData\Local\Programs\Python\Python312`.
  - Versiones: numpy 2.4.4 · pandas 3.0.2 · matplotlib 3.10.9 · scipy 1.17.1 · openpyxl 3.1.5 · simpy 4.1.2.
  - `jupyter` **no** está en el PATH. El usuario abre el cuaderno en VS Code (Windows 11) y usa Run All.
  - Para ejecutar fuera de VS Code: cargar el JSON del cuaderno y ejecutar las celdas en orden con `exec` en un espacio de nombres compartido, con `matplotlib.use("Agg")` y `display` redefinido.
- **Duración:** lo más lento son las réplicas de la sección 3 (escenarios y estrés); la sección 5 tarda unos 10 s.
- **Convenciones que hay que respetar:**
  - Todo en español.
  - Números con `es()` y `tabla()` (punto de miles, coma decimal).
  - Colores de `COLOR` y estilo de `rcParams`.
  - Todo supuesto nuevo va en la celda de **Configuración**.
  - Leer del Excel solo datos de entrada; recalcular las fórmulas en Python.
  - Comparar escenarios con las mismas semillas.
  - Reportar promedio ± intervalo del 95 % con `N_REP` réplicas.
  - Imitar la densidad de comentarios y el estilo del código existente: nombres en español, funciones cortas, comentarios al final de la línea.
- **No reproducir datos personales** de clientes (hojas `Facturas Mayo-Julio` y `Clientes`).
- **Ideas pendientes** (no pedidas aún por el usuario):
  - simular la estrategia mixta;
  - agregar un costo de faltante o comparar con el mismo nivel de servicio;
  - calcular en Python el Plan Agregado en vez de leer las fórmulas;
  - imponer la capacidad de bodega en el gemelo;
  - modelar tubos vacíos y mano de obra;
  - ejecutar y guardar las salidas de las celdas 36–44.


---

<!-- fuente: corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Datos Thyms Completo.md -->
# Datos Thyms Completo

> **Archivo:** [`Datos Thyms Completo.xlsx`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Datos%20Thyms%20Completo.xlsx) · **Corte 2** · Libro de Excel con 14 hoja(s): `Parámetros`, `Productos`, `Tiempos`, `Utilizacion`, `Alistamiento`, `Fallas`, `Mano de Obra`, `Métricas`, `Plan Agregado`, `Restricciones`, `Proceso Planeación Agregada`, `Facturas Mayo-Julio`, `Clientes`, `Ventas`  
> **Nombre original:** `CORTE 2/Datos Thyms Completo.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Libro de datos del **proyecto del Corte 2** sobre THYMS Colombia S.A.S. (tintes en tubo de 60 g, productos A, B y C). Reúne en 14 hojas los parámetros de la planta (turnos, productos, tiempos, OEE, alistamientos, fallas, mano de obra), el **estudio preliminar** del sistema (utilización, takt time, cycle time, throughput, WIP y ley de Little), la **planeación agregada** de 12 meses (persecución, nivelada y mixta, con su desagregación por producto), las restricciones de capacidad, demanda y almacenamiento, y los datos reales de ventas del Corte 1.

Es la **única fuente de datos** de los cuadernos [`Gemelo_Digital_Thyms.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md) y [`Gemelo_Digital_Thyms_MEJORADO.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms_MEJORADO.md); el mapa de las celdas que leen está en [`CONTEXTO_GEMELO_THYMS.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/CONTEXTO_GEMELO_THYMS.md). Aplica las clases [L02](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L02-introduction-to-production-systems.md) (métricas de desempeño), [L10](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md) (planeación agregada) y [L11](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md) (agregación y desagregación).

Las celdas en azul son datos editables (según la nota de la hoja `Plan Agregado`); el resto son fórmulas.

### Hoja `Parámetros`

**Objetivo:** parámetros generales de la planta.

| Parámetro | Celda | Valor |
|---|---|---|
| Días hábiles por mes | B4 | 22 |
| Turnos por día | B5 | 2 (6:00–14:00 y 14:00–22:00, de lunes a viernes) |
| Horas efectivas por turno | B6 | 7 (8 h menos descansos) |
| Horas disponibles por mes y recurso | B7 = B4·B5·B6 | 308 |
| Factor de demanda (escenarios) | B8 | 1 |
| Tubos por lote de 500 kg | B9 | 7.800 (rendimiento aproximado, con mermas) |
| Unidades por caja master | B10 | 24 |
| Tasa anual de costo de mantener | B11 | 0,22 sobre el costo unitario |
| Cambios de tono por mes | B12 | 26 (≈ 6 por semana) |
| Alistamiento promedio en la llenadora | B13 | 0,75 h por cambio (supuesto) |
| Contenido por tubo | B14 | 60 g de base y colorantes |

### Hoja `Productos`

**Objetivo:** datos de cada producto e inventario, y materias primas.

**Fórmulas:**
- demanda de escenario: $D_p = D^{base}_p \cdot f$, con $f$ = `Parámetros!B8`;
- costo de mantener mensual: $h_p = c_p \cdot 0{,}22/12$;
- cobertura de producto terminado en días: $\text{Stock}_p / (D_p/22)$.

| Producto | Código | Demanda (tubos/mes) | Rendimiento | Costo unitario (COP) | $h_p$ (COP/tubo-mes) | Costo de alistamiento (COP) | Stock PT | Cobertura (días) | Bodega máx. | Punto de reorden | Lote | WIP | MP (kg) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A. Kolorezza permanente 60 g | THY-KZ060 | 48.000 | 0,985 | 4.300 | 78,83 | 320.000 | 14.000 | 6,42 | 26.000 | 8.000 | 15.600 | 4.000 | 1.600 |
| B. Visalia sin amoníaco 60 g | THY-VS060 | 30.000 | 0,975 | 5.600 | 102,67 | 520.000 | 8.500 | 6,23 | 18.000 | 5.500 | 7.800 | 2.500 | 1.100 |
| C. Thym's Coloring permanente 60 g | THY-TC060 | 22.000 | 0,988 | 3.700 | 67,83 | 300.000 | 7.000 | 7,00 | 14.000 | 4.500 | 15.600 | 2.000 | 900 |
| **Total** | | **100.000** | | | | | **29.500** | | **58.000** | **18.000** | **39.000** | **8.500** | **3.600** |

**Materias primas y materiales:**

| Ítem | Origen | Stock | Lead time (días) | Política |
|---|---|---|---|---|
| Base y colorantes | Importado | 3.600 kg (= suma de la columna O) | 40 | Stock de seguridad de 3 semanas |
| Tubos vacíos | Nacional | 60.000 und | 12 | ≈ 10 días de producción |
| Tapas, cartones e instructivos | Nacional | sin dato | 12 | Sin dato de stock |

**Lectura útil:** punto de reorden + lote = 23.600 en A (bodega de 26.000), 13.300 en B (18.000) y **20.100 en C, más que su bodega de 14.000**. Ese es el problema de almacenamiento que detecta el gemelo.

### Hoja `Tiempos`

**Objetivo:** tiempos de proceso por estación y producto. La hoja indica «Distribución normal».

**Fórmulas:**
- mínimo y máximo: $\mu(1 \mp r)$, donde $\mu$ es el promedio y $r$ el rango ±% (columna I);
- capacidad nominal en tubos/h (columna J), con $R$ = número de recursos:
  - estaciones en min/lote: $7.800 \cdot 60/\mu \cdot R$;
  - estaciones en tubos/h: $\mu \cdot R$;
  - empaque, en cajas/h: $\mu \cdot 24 \cdot R$.

| Estación | Unidad | A | B | C | Desv. | Recursos | Rango ± | Capacidad A / B / C (tubos/h) |
|---|---|---|---|---|---|---|---|---|
| Pesaje | min/lote | 40 | 45 | 40 | 4 | 1 | 10 % | 11.700 / 10.400 / 11.700 |
| Mezcla y emulsión | min/lote | 150 | 180 | 140 | 12 | 2 | 20 % | 6.240 / 5.200 / 6.685,7 |
| Control de calidad de lote | min/lote | 60 | 75 | 55 | 8 | 1 | 13 % | 7.800 / 6.240 / 8.509,1 |
| Llenado y sellado | tubos/h | 2.400 | 2.000 | 2.400 | 150 | 1 | 12 % | 2.400 / 2.000 / 2.400 |
| Encartonado | tubos/h | 3.000 | 3.000 | 3.000 | 200 | 1 | 7 % | 3.000 / 3.000 / 3.000 |
| Empaque caja master | cajas/h | 110 | 110 | 110 | 10 | 1 | 9 % | 2.640 / 2.640 / 2.640 |

Ejemplos de límites: mezcla A va de 120 a 180 min; llenado A, de 2.112 a 2.688 tubos/h.

### Hoja `Utilizacion`

**Objetivo:** utilización de cada estación con la demanda base y cuello de botella.

**Método** ($e$ = estación, $p$ = producto, $y_p$ = rendimiento, $\text{cap}_{e,p}$ = capacidad nominal, $S_e$ = horas de alistamiento):
- horas requeridas al mes: $H^{req}_e = \sum_p \frac{D_p}{y_p\,\text{cap}_{e,p}} + S_e$; solo la llenadora tiene alistamiento, $S$ = 26 × 0,75 = 19,5 h;
- horas efectivas: $H^{ef}_e = 308 \cdot OEE_e$;
- utilización: $U_e = H^{req}_e / H^{ef}_e$.

| Estación | OEE | Alistamiento (h/mes) | Horas requeridas | Horas efectivas | Utilización |
|---|---|---|---|---|---|
| Pesaje | 0,90 | 0 | 9,03 | 277,2 | 3,3 % |
| Mezcla y emulsión | 0,85 | 0 | 17,06 | 261,8 | 6,5 % |
| Control de calidad | 0,90 | 0 | 13,80 | 277,2 | 5,0 % |
| **Llenado y sellado** | **0,74** | **19,5** | **64,47** | **227,92** | **28,3 %** |
| Encartonado | 0,83 | 0 | 33,92 | 255,64 | 13,3 % |
| Empaque caja master | 0,88 | 0 | 38,55 | 271,04 | 14,2 % |

El cuello de botella de los tres productos es **llenado y sellado** (menor capacidad: 2.400, 2.000 y 2.400 tubos/h), y es también la estación más utilizada (28,3 %).

Notas de la hoja:
- los OEE de la llenadora (74 %), la encartonadora (83 %) y los reactores (85 %) son del ejercicio; los de pesaje (90 %), control de calidad (90 %) y empaque (88 %) son supuestos;
- con factor de demanda 1 la utilización es baja; se sube en `Parámetros` para estresar el sistema.

### Hoja `Alistamiento`

| Cambio | Reactor (min) | Llenadora (min) | Encartonadora (min) | Total (min) | Total (h) |
|---|---|---|---|---|---|
| Mismo producto, distinto tono | 25 | 35 | 10 | 70 | 1,17 |
| A ↔ C (ambos con amoníaco) | 60 | 75 | 20 | 155 | 2,58 |
| A/C ↔ B (de con amoníaco a sin amoníaco) | 120 | 150 | 30 | 300 | 5,00 |

### Hoja `Fallas`

Tiempo entre fallas exponencial y reparación lognormal. Disponibilidad por fallas $A = MTBF/(MTBF + MTTR)$.

| Recurso | MTBF (h) | MTTR (h) | Disponibilidad |
|---|---|---|---|
| Reactor 1 | 180 | 3 | 0,9836 |
| Reactor 2 | 160 | 3,5 | 0,9786 |
| Llenadora de tubos | 70 | 2 | 0,9722 |
| Encartonadora | 120 | 1,5 | 0,9877 |
| Línea de empaque | 200 | 1 | 0,9950 |

### Hoja `Mano de Obra`

- **Operarios por turno:** pesaje 2, mezcla 2, control de calidad 2, llenado y sellado 3, encartonado 2, empaque 4, bodega y montacargas 2 = **17 por turno**; con 2 turnos, **34 en total**.
- **Costo por hora:** ordinaria 13.800 COP; extra diurna (×1,25) 17.250; extra nocturna (×1,75) 24.150.
- **Horas extra:**
  - límite legal: 2 h por día y 12 h por semana;
  - uso actual: 150 h/mes en llenado y empaque;
  - costo aproximado: 150 × 17.250 = 2.587.500 COP/mes.
- **Subcontratación:**
  - maquila de llenado: 380 COP/tubo, 20.000 tubos/mes, 5 días, solo A y C;
  - empaque externo: 210 COP/caja, 500 cajas/mes, 2 días.

### Hoja `Métricas`

**Objetivo:** takt time, cycle time, throughput, WIP y ley de Little ($D_p$ = demanda del producto, $T$ = 308 h/mes).

**1. Takt time.** $T_{takt,p} = \dfrac{308 \cdot 3.600 \text{ s}}{D_p}$; en minutos por lote: $T_{takt,p} \cdot 7.800/60$.

| | A | B | C | Familia |
|---|---|---|---|---|
| Takt (s/tubo) | 23,10 | 36,96 | 50,40 | 11,088 |
| Takt (min por lote) | 3.003 | 4.804,8 | 6.552 | 1.441,4 |

**2. Cycle time por estación** = 3.600 / capacidad nominal (s/tubo):

| Estación | A | B | C |
|---|---|---|---|
| Pesaje | 0,308 | 0,346 | 0,308 |
| Mezcla | 0,577 | 0,692 | 0,538 |
| Control de calidad | 0,462 | 0,577 | 0,423 |
| Llenado | 1,5 | 1,8 | 1,5 |
| Encartonado | 1,2 | 1,2 | 1,2 |
| Empaque | 1,364 | 1,364 | 1,364 |
| Cuello de botella (máx.) | 1,5 | 1,8 | 1,5 |
| Efectivo con OEE (÷ 0,74) | 2,027 | 2,432 | 2,027 |
| Takt / cycle time efectivo | 11,40× | 15,19× | 24,86× |

**3. Tiempo de proceso por lote, sin esperas** (min):
- estaciones de lote: el tiempo del lote;
- llenado: $7.800/\text{tubos/h} \cdot 60$;
- empaque: $7.800/(110 \cdot 24) \cdot 60$.

| Estación | A | B | C |
|---|---|---|---|
| Pesaje | 40 | 45 | 40 |
| Mezcla | 150 | 180 | 140 |
| Control de calidad | 60 | 75 | 55 |
| Llenado | 195 | 234 | 195 |
| Encartonado | 156 | 156 | 156 |
| Empaque | 177,3 | 177,3 | 177,3 |
| **Total** | **778,3 min = 12,97 h** | **867,3 min = 14,45 h** | **763,3 min = 12,72 h** |

**4. Throughput, WIP y ley de Little** ($WIP = TH \times$ tiempo de flujo):

| Indicador | Fórmula | A | B | C | Total |
|---|---|---|---|---|---|
| Throughput requerido (tubos/h) | $D_p/308$ | 155,84 | 97,40 | 71,43 | 324,68 |
| Throughput máximo (tubos/h) | cap. mínima × OEE | 1.776 | 1.480 | 1.776 | — |
| Holgura de throughput | máx./requerido | 11,40× | 15,19× | 24,86× | — |
| Lotes por mes | $D_p/7.800$ | 6,15 | 3,85 | 2,82 | 12,82 |
| WIP actual (tubos) | dato | 4.000 | 2.500 | 2.000 | 8.500 |
| Tiempo de flujo por Little (h) | WIP/TH | 25,67 | 25,67 | 28,00 | 26,18 |
| Tiempo de flujo (días hábiles) | ÷ 14 h/día | 1,83 | 1,83 | 2,00 | 1,87 |
| Tiempo de proceso por lote (h) | sección 3 | 12,97 | 14,45 | 12,72 | 13,36 (ponderado por TH) |
| Eficiencia de flujo | proceso/flujo | 50,5 % | 56,3 % | 45,4 % | 51,0 % |
| WIP crítico (tubos) | TH × tiempo de proceso | 2.021 | 1.408 | 909 | 4.338 |
| WIP actual / crítico | | 1,98× | 1,78× | 2,20× | 1,96× |

**Conclusión:** la planta tiene mucha holgura de capacidad (11 a 25 veces el ritmo que exige la demanda en la llenadora) y casi el doble del WIP mínimo necesario.

### Hoja `Plan Agregado`

**Objetivo:** plan agregado de 12 meses (enero a diciembre) para la familia, en tubos, comparando tres estrategias con la misma demanda.

**Parámetros:**
- B4: $\alpha$ de la estrategia mixta = 0,5 (dato).
- B5: inventario inicial $I_0$ = 29.500 (`Productos!I8`).
- B6: bodega = 58.000 (`Productos!K8`).
- B7: capacidad efectiva de la llenadora con la mezcla de productos, $\bar{c} = OEE_{lle} \cdot \left(\sum_p \frac{w_p}{c_p}\right)^{-1}$, con $w_p = D_p/\sum D$ y $c_p$ = capacidad nominal de llenado → 0,74 × 2.264,15 = **1.675,47 tubos/h**.
- B8: horas efectivas por día = 2 × 7 = 14.
- B9: costo de mantener ponderado, $\bar{h} = \sum_p h_p D_p / \sum D$ = **83,56 COP/tubo-mes**.
- B10: estrategia elegida (1 persecución, 2 nivelada, 3 mixta) = **1**; C10 muestra «Persecución».

**Fórmulas mensuales** ($t$ = mes; $n_t$ = días hábiles, dato; $s_t$ = índice estacional, de `Ventas!C`):
- demanda: $D_t = 100.000 \cdot s_t$;
- capacidad: $K_t = n_t \cdot 14 \cdot \bar{c}$;
- persecución: $P_t = D_t$;
- nivelada: $P_t = \bar{D} = \frac{1}{12}\sum D_t$ = 100.000;
- mixta: $P_t = \alpha D_t + (1-\alpha)\bar{D}$;
- inventario de cada estrategia: $I_t = I_{t-1} + P_t - D_t$;
- utilización: $P_t/K_t$;
- holgura: $K_t/D_t$.

| Mes | Días | Índice | Demanda | Capacidad | Util. persecución | Inv. nivelada | Prod. mixta | Inv. mixta | Holgura |
|---|---|---|---|---|---|---|---|---|---|
| Enero | 20 | 0,634 | 63.413 | 469.132 | 13,5 % | 66.087 | 81.707 | 47.793 | 7,40 |
| Febrero | 20 | 1,019 | 101.889 | 469.132 | 21,7 % | 64.198 | 100.945 | 46.849 | 4,60 |
| Marzo | 21 | 1,331 | 133.118 | 492.589 | 27,0 % | 31.080 | 116.559 | 30.290 | 3,70 |
| Abril | 21 | 0,347 | 34.734 | 492.589 | 7,1 % | **96.346** | 67.367 | **62.923** | 14,18 |
| Mayo | 21 | 1,308 | 130.786 | 492.589 | 26,6 % | 65.560 | 115.393 | 47.530 | 3,77 |
| Junio | 20 | 1,037 | 103.697 | 469.132 | 22,1 % | 61.863 | 101.849 | 45.681 | 4,52 |
| Julio | 22 | 1,530 | 152.969 | 516.045 | **29,6 %** | 8.894 | 126.485 | 19.197 | **3,37** |
| Agosto | 20 | 0,794 | 79.394 | 469.132 | 16,9 % | 29.500 | 89.697 | 29.500 | 5,91 |
| Septiembre | 22 | 1 | 100.000 | 516.045 | 19,4 % | 29.500 | 100.000 | 29.500 | 5,16 |
| Octubre | 20 | 1 | 100.000 | 469.132 | 21,3 % | 29.500 | 100.000 | 29.500 | 4,69 |
| Noviembre | 20 | 1 | 100.000 | 469.132 | 21,3 % | 29.500 | 100.000 | 29.500 | 4,69 |
| Diciembre | 19 | 1 | 100.000 | 445.675 | 22,4 % | 29.500 | 100.000 | 29.500 | 4,46 |
| **Total** | **246** | | **1.200.000** | **5.770.325** | | | **1.200.000** | | |

En persecución, la producción es igual a la demanda y el inventario se queda en 29.500 todos los meses. En nivelada, la producción es de 100.000 al mes, con utilización del 19,4 % al 22,4 %.

**Comparación (filas 31 a 43):**
- horas extra: $HE = \sum_t \max(0, P_t - K_t)/\bar{c}$;
- costo de mantener: $\sum_t I_t \cdot \bar{h}$;
- costo de horas extra: $HE \cdot 17 \text{ operarios} \cdot 17.250$;
- factible si no hay meses con $I_t < 0$, ni meses con $I_t > 58.000$, ni horas extra.

| Indicador | Persecución | Nivelada | Mixta |
|---|---|---|---|
| Producción anual | 1.200.000 | 1.200.000 | 1.200.000 |
| Inventario promedio | 29.500 | 45.127 | 37.314 |
| Inventario máximo | 29.500 | 96.346 | 62.923 |
| Inventario mínimo | 29.500 | 8.894 | 19.197 |
| Meses con desabastecimiento | 0 | 0 | 0 |
| Meses sobre la bodega | 0 | **5** (ene, feb, abr, may, jun) | **1** (abr) |
| Utilización máxima de la llenadora | 29,6 % | 22,4 % | 24,5 % |
| Horas extra (h/año) | 0 | 0 | 0 |
| Costo anual de mantener (COP) | 29.581.420 | 45.251.809 | 37.416.615 |
| Costo de horas extra | 0 | 0 | 0 |
| Variación de la producción (máx. − mín.) | 118.236 | 0 | 59.118 |
| Costo total (COP) | 29.581.420 | 45.251.809 | 37.416.615 |
| ¿Factible? | **Sí** | No | No |

**Desagregación de la estrategia elegida** (filas 47 a 59):
- producción: `CHOOSE(B10, F, I, L)`;
- lotes: $\lceil P_t/7.800 \rceil$;
- por producto: $P_t \cdot D_p/\sum D$, es decir, 48 % A, 30 % B y 22 % C.

Con persecución:

| Mes | Producción | Lotes de 500 kg | A | B | C |
|---|---|---|---|---|---|
| Enero | 63.413 | 9 | 30.438 | 19.024 | 13.951 |
| Febrero | 101.889 | 14 | 48.907 | 30.567 | 22.416 |
| Marzo | 133.118 | 18 | 63.896 | 39.935 | 29.286 |
| Abril | 34.734 | 5 | 16.672 | 10.420 | 7.641 |
| Mayo | 130.786 | 17 | 62.777 | 39.236 | 28.773 |
| Junio | 103.697 | 14 | 49.775 | 31.109 | 22.813 |
| Julio | 152.969 | 20 | 73.425 | 45.891 | 33.653 |
| Agosto | 79.394 | 11 | 38.109 | 23.818 | 17.467 |
| Sep a dic (cada mes) | 100.000 | 13 | 48.000 | 30.000 | 22.000 |

En total son 160 lotes al año; el inventario final de producto terminado es de 29.500 todos los meses.

**Conclusión:** solo la persecución es factible. La nivelada no cabe en la bodega (pico de 96.346, 1,66 veces la capacidad) y la mixta la excede en abril. La capacidad sobra en todos los casos (la llenadora no pasa del 30 %).

### Hoja `Restricciones`

**Objetivo:** tablero de restricciones con su estado. El estado se calcula con reglas `IF` sobre el valor y la referencia (Holgura, Alerta o Crítica).

| Tipo | Indicador | Valor | Referencia | Estado |
|---|---|---|---|---|
| Capacidad | Utilización pico de la llenadora (persecución) | 29,6 % | 100 % | Holgura |
| Capacidad | Factor de demanda máximo antes de saturar la llenadora = $f \cdot \min_t (K_t/D_t)$ | 3,37 | 1 | Holgura |
| Capacidad | Utilización de los reactores | 6,5 % | 100 % | Holgura |
| Capacidad | Horas extra al año (persecución) | 0 | 624 (12 h × 52 semanas) | Holgura |
| Demanda | Pico / promedio del índice estacional | 1,53 | 1,25 | Alerta |
| Demanda | Mes pico | Julio | — | Informativo |
| Demanda | Participación de B (cambios largos, mezcla más lenta) | 30 % | — | Informativo |
| Almacenamiento | Cobertura máxima que permite la bodega = 58.000/(100.000/22) | 12,76 días | 6,49 (cobertura actual) | Holgura |
| Almacenamiento | Inventario máximo de la nivelada / bodega | 1,66 | 1 | **Crítica** |
| Almacenamiento | Cobertura de base y colorantes = 3.600/277,5 | 12,97 días | 55 (lead time + seguridad) | **Crítica** |
| Almacenamiento | Cobertura de tubos vacíos | 13,2 días | 12 | Alerta |
| Demanda | Participación de los 10 mayores clientes (may–jul) | 39,0 % | — | Informativo |

**Cálculos de materia prima** (filas 19 a 24):
- consumo: $\sum_p \frac{D_p}{y_p} \cdot 60 \text{ g} / 1.000$ = **6.106 kg/mes** (unos 61 g por tubo bueno);
- consumo diario: 6.106/22 = 277,5 kg/día hábil;
- stock de seguridad: 15 días hábiles (supuesto);
- stock requerido: 277,5 × (40 + 15) = 15.265 kg;
- **faltante frente a los 3.600 kg actuales: 11.665 kg.**

### Hoja `Proceso Planeación Agregada`

Pasos que seguiría THYMS cada mes:
1. pronosticar la demanda de la familia y aplicar la estacionalidad (demanda base e índices de las ventas reales de 2026);
2. expresar la demanda en tubos y en horas del cuello de botella (capacidad de la llenadora y OEE);
3. medir la eficiencia con takt, cycle time, throughput y WIP;
4. identificar restricciones de capacidad, demanda y almacenamiento;
5. construir las estrategias persecución, nivelada y mixta (con $\alpha$ ajustable);
6. evaluar inventario, desabastecimiento, bodega, horas extra y costo;
7. elegir la estrategia factible de menor costo y desagregarla por producto y lote;
8. revisar cada mes con la demanda real y ajustar materia prima y alistamientos.

### Hoja `Facturas Mayo-Julio`

464 facturas reales de mayo a julio de 2026 (filas 5 a 468), con columnas mes, factura, código de cliente, cliente (anonimizado) y ventas en COP. Las ventas son el `subdoc` de [`VENTAS.xls`](/corte-1-pronosticos/proyecto-thyms-pronostico/VENTAS.md). Todas las filas en [`Datos Thyms Completo-datos/Facturas_Mayo-Julio.csv`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Datos%20Thyms%20Completo-datos/Facturas_Mayo-Julio.csv). Los cuadernos solo leen la columna E, para ajustar la distribución del tamaño de pedido.

### Hoja `Clientes`

Concentración de ventas por cliente; cada fila suma con `SUMIF` las facturas del cliente. Todas las filas en [`Datos Thyms Completo-datos/Clientes.csv`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Datos%20Thyms%20Completo-datos/Clientes.csv).
- **161 clientes distintos**, con ventas por 590.813.195 COP.
- El mayor cliente (CLIENTE 023, 80.429.530 COP) concentra el **13,6 %**.
- Los 10 mayores concentran el **39,0 %**.
- El 20 % de clientes con más ventas (32 clientes) concentra el **63,9 %**.

### Hoja `Ventas`

Ventas de 2026 en COP (de `UNIFICADO`) e índice estacional $s_m = V_m / \bar{V}$, donde $V_m$ son las ventas del mes $m$ y $\bar{V}$ = 150.997.582 es el promedio de enero a agosto.

| Mes | Ventas (COP) | Índice | Ventas según facturas | Facturas | Ticket promedio | Facturas − UNIFICADO |
|---|---|---|---|---|---|---|
| Enero | 95.752.306 | 0,634 | — | — | — | — |
| Febrero | 153.850.391 | 1,019 | — | — | — | — |
| Marzo | 201.004.440 | 1,331 | — | — | — | — |
| Abril | 52.446.770 | 0,347 | — | — | — | — |
| Mayo | 197.484.330 | 1,308 | 198.232.170 | 165 | 1.201.407 | 747.840 |
| Junio | 156.580.280 | 1,037 | 159.703.880 | 135 | 1.182.992 | 3.123.600 |
| Julio | 230.979.600 | 1,530 | 232.877.145 | 164 | 1.419.983 | 1.897.545 |
| Agosto | 119.882.540 | 0,794 | — | — | — | — |
| Sep a dic | 0 | 1 (supuesto) | — | — | — | — |
| **Total** | **1.207.980.657** | | **590.813.195** | **464** | | |

Mes de mayores ventas: julio (1,53 veces el promedio); de menores: abril (0,35). Coeficiente de variación mensual: 39,4 %.

### Observaciones

- **Error de rótulo:** la fila 46 de `Plan Agregado` dice «estrategia seleccionada (celda B9)», pero el selector está en **B10** (B9 es el costo de mantener).
- **Unidades mezcladas:** en `Restricciones` el lead time de la materia prima (40 días **calendario**) se suma a 15 días **hábiles** y se compara con una cobertura en días hábiles. El cuaderno del gemelo convierte los 40 días calendario a unos 29 hábiles.
- **Días hábiles distintos:** `Parámetros`, `Utilizacion` y `Métricas` usan 22 días/mes (308 h), mientras que `Plan Agregado` usa días por mes escritos a mano (246 al año, 20,5 en promedio). El calendario con festivos del gemelo da 243 días para 2026.
- **Índices de septiembre a diciembre = 1** (supuesto, no hay datos). Además, los índices salen de **una sola zona de ventas** (≈ 11,7 % de la planta) y se aplican a toda la planta.
- La persecución mantiene los 29.500 tubos iniciales todo el año, así que su costo de mantener no es 0 (29,6 millones COP). El plan no reduce el inventario inicial.
- El costo de horas extra supone que los 17 operarios de un turno hacen las horas extra.
- El costo de alistamiento por producto (`Productos!H`) y la maquila no entran en el costo de ninguna estrategia.
- Los nombres de los clientes ya están anonimizados (CLIENTE ###).
- No hay hojas vacías ni gráficos.


---

<!-- fuente: corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md -->
# Gemelo_Digital_Thyms

> **Archivo:** [`Gemelo_Digital_Thyms.ipynb`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.ipynb) · **Corte 2** · Cuaderno Jupyter con 36 celdas  
> **Nombre original:** `CORTE 2/Gemelo_Digital_Thyms.ipynb`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

### Qué es

Cuaderno **base** del proyecto del Corte 2 sobre THYMS Colombia S.A.S. (creado el 2026-10-01; 36 celdas, todas ejecutadas con salidas guardadas, Python 3.12). Hace tres cosas:
1. revisa y corrige el pronóstico del Corte 1;
2. construye un pronóstico de planta a 12 meses con estacionalidad;
3. implementa un **gemelo digital** de la planta como simulación de eventos discretos en **SimPy**, con sensores virtuales, validación, métricas de eficiencia, restricciones y escenarios.

Lee **solo datos de entrada** de [`Datos Thyms Completo.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Datos%20Thyms%20Completo.md) y recalcula en Python lo que en el libro son fórmulas.

La versión [`Gemelo_Digital_Thyms_MEJORADO.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms_MEJORADO.md) tiene estas mismas 36 celdas (código y salidas idénticos) y agrega las secciones 4 y 5. El documento de traspaso [`CONTEXTO_GEMELO_THYMS.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/CONTEXTO_GEMELO_THYMS.md) describe el cuaderno con más detalle (mapa de celdas, clases y funciones).

### Estructura

| Celdas | Sección | Qué hace |
|---|---|---|
| 0–2 | Título · 1. Configuración y datos | Librerías: math, datetime, numpy, pandas, matplotlib, scipy.stats, openpyxl, simpy |
| 3 | Configuración | Supuestos editables, colores, estilo de gráficos y funciones `es()` (números en formato español) y `tabla()` |
| 4–5 | Carga | `cargar_datos()` lee del libro parámetros, productos, tiempos, OEE, alistamientos, fallas, ventas y facturas, y muestra la tabla de productos |
| 6 | Escala | Compara la venta real promedio con la demanda de planta → escala zona → planta |
| 7–8 | 2.1 Revisión del Corte 1 | `ses()` y `metricas()` (MAD, RMSE, MAPE, sesgo, señal de rastreo); reproduce el SES del Corte 1 |
| 9–11 | 2.2 Elección del método | Prueba de tendencia; 7 métodos comparados con **origen móvil**; búsqueda de $\alpha$ por RMSE |
| 12–14 | 2.3 Pronóstico a 12 meses | Nivel × índice estacional, intervalo del 80 %, tabla y gráfica |
| 15–16 | 2.4 Pronosticador del gemelo | Clase `Pronosticador` y parámetros lognormales del tamaño de pedido |
| 17 | 3.1 Qué representa | Diagrama del flujo y tabla de cómo se modela cada elemento |
| 18 | Calendario | `pascua()`, `festivos_colombia()` (con ley Emiliani), `dias_habiles()` |
| 19–20 | 3.2 El modelo | `CFG_BASE`, `lognormal_media()`, clases `Maquina` y `GemeloThyms`, función `replicar()` |
| 21–22 | 3.3 Validación | Balance de masa, ley de Little y horas de equipo frente al libro |
| 23–28 | 3.4 Corrida base con sensores | Telemetría horaria, modo «en vivo», gráfica de inventario y gráfica de una semana de la llenadora |
| 29–30 | 3.5 Métricas de eficiencia | Takt, throughput, tiempo de flujo y WIP: Corte 1 frente a libro frente a gemelo |
| 31–32 | 3.6 Restricciones | Capacidad, demanda, almacenamiento y materia prima, con intervalo del 95 % |
| 33–35 | 3.7 Escenarios | 6 escenarios y prueba de estrés con factor de demanda de 1 a 3,5 |

### Datos que usa

- **Libro `Datos Thyms Completo.xlsx`:**
  - parámetros (22 días/mes, 2 turnos de 7 h, 7.800 tubos/lote, 24 tubos/caja);
  - productos (demanda 48.000/30.000/22.000, rendimiento, stock, bodega, punto de reorden, lote, materia prima);
  - lead time de la materia prima (40 días);
  - tiempos (promedio, desviación y rango);
  - OEE, alistamientos, MTBF/MTTR;
  - ventas de enero a agosto de 2026 en COP;
  - las 464 facturas (COP por pedido).
- **Supuestos de la celda 3:**
  - `PRECIO_UND` = 12.900 COP/tubo;
  - índices de septiembre a diciembre = 1;
  - `CV_CHOQUE_MENSUAL` = 0,10;
  - horizonte de septiembre de 2026 a agosto de 2027 (`INICIO`, `MESES` = 12);
  - `SUBLOTE` = 600 tubos;
  - `KG_LOTE` = 500;
  - `CV_MTTR` = 0,5;
  - `SS_MP_DIAS` = 15;
  - `REVISION_MP_DIAS` = 5;
  - `N_REP` = 30 réplicas, `SEMILLA` = 2026.

### Métodos

**Pronóstico.**
- SES: $F_{t+1} = \alpha y_t + (1-\alpha)F_t$, donde $y_t$ es la venta del mes $t$.
- Métricas ($e_t = y_t - F_t$): MAD, $RMSE = \sqrt{\frac{1}{n}\sum e_t^2}$, MAPE, sesgo $= \bar{e}$ y señal de rastreo $TS = \sum e_t/MAD$.
- Tendencia: regresión lineal con valor p (`scipy.stats.linregress`).
- **Origen móvil:** con los meses $1..k$ se pronostica el mes $k+1$, para $k = 3..7$ (5 pronósticos fuera de muestra).
- $\alpha$: rejilla de 0,05 a 0,95 minimizando el RMSE.
- Pronóstico de planta: $\hat{D}_m = N \cdot s_m$, con nivel $N$ en tubos de planta e índice $s_m = y_m/\bar{y}$ (meses 1 a 8; 1 en los demás).
- Intervalo del 80 %: $\hat{D}_m (1 \pm z_{0{,}90}\,\sigma_{rel})$, con $\sigma_{rel}$ = RMSE fuera de muestra / nivel.
- Escala: $\text{ESCALA} = 100.000 / (\bar{y}/12.900)$.

**Pronosticador dentro del gemelo.**
- Índice: $s'_m = 1 + w(s_m - 1)$, donde $w$ es el peso estacional.
- Actualización mensual: $N \leftarrow \alpha\,D^{real}_m/s'_m + (1-\alpha)N$.
- Tamaño de pedido: lognormal ajustada al logaritmo de las facturas.

**Gemelo digital** (eventos discretos; el reloj avanza en horas de turno, 1 día hábil = 14 h, de lunes a viernes sin festivos de Colombia).
- **Demanda.** Cada mes la tasa diaria es demanda base × factor × índice × choque lognormal (CV 10 %) / días hábiles. Cada día:
  - número de pedidos ~ Poisson(tasa / pedido medio);
  - tamaño ~ lognormal (de las facturas) / 12.900;
  - lo que no hay en bodega queda pendiente (backorder).
- **Producción.**
  - Política de punto de reorden con revisión diaria: si la posición (PT + en proceso − pendientes) ≤ punto de reorden, se lanzan lotes de 7.800 tubos (A y C: 2 lotes; B: 1).
  - Recorrido del lote: materia prima (500 kg) → pesaje → reactor (2 en paralelo, con alistamiento según el cambio: tono, A↔C o con B) → mezcla → control de calidad → llenadora en 13 sublotes de 600 tubos → encartonado → empaque → tubos buenos ~ Binomial(600, rendimiento).
- **Tiempos:** normal truncada entre mínimo y máximo.
- **Máquinas** (clase `Maquina`):
  - estados libre, marcha, alistamiento y falla;
  - vida ~ Exponencial(MTBF), consumida solo en marcha;
  - reparación lognormal con media MTTR y CV 0,5;
  - pérdida de velocidad $= OEE / A$, con $A = MTBF/(MTBF+MTTR)$, para completar el OEE del libro.
- **Materia prima:**
  - revisión cada 5 días hábiles;
  - se pide hasta cubrir el consumo pronosticado en (lead time + 5 + 15) días hábiles, en múltiplos de 500 kg;
  - lead time de 40 días calendario ≈ 29 días hábiles;
  - se supone que al inicio ya hay pedidos en tránsito.
- **Sensores virtuales:** `lectura()` devuelve 16 variables (estado y velocidad de la llenadora con ruido del 1 %, contadores, estados de reactores, encartonadora y empaque, PT por producto, WIP, pendientes y materia prima). Se toma una lectura cada hora y también se puede avanzar paso a paso (`iniciar()` + `env.run`).
- **Réplicas:** 30 por escenario con números aleatorios comunes (semillas 2026 + i), con intervalo del 95 % $\pm t_{0{,}975;\,29}\,s/\sqrt{30}$.

### Resultados clave con números

**Escala (celda 6):** la venta real promedio es de 150.997.582 COP/mes = 11.705 tubos/mes, es decir, el **11,7 %** de la planta (100.000 tubos/mes); la escala es de unas 8,54 veces.

**2.1 Revisión del SES del Corte 1** ($\alpha$ = 0,05, arranca en enero, evaluado de febrero a julio):
- MAD = 80.172.875 COP;
- MAPE = 53,4 %;
- **sesgo = +63.063.608 COP** (subestima);
- **señal de rastreo = 4,72** (fuera de ±4);
- agosto: 114.671.388 pronosticado frente a 119.882.540 real.

**2.2 Comparación por origen móvil** (MAD, RMSE y sesgo en millones de COP). Tendencia: 6.741.938 COP/mes con valor p = 0,51, no significativa.

| Método | MAD | RMSE | MAPE | Sesgo | Señal de rastreo |
|---|---|---|---|---|---|
| **SES α = 0,05, nivel inicial = promedio de 3 meses (elegido)** | 54,7 | **63,6** | 56,3 % | 2,4 | 0,22 |
| Promedio histórico | 61,9 | 69,3 | 60,2 % | 8,6 | 0,69 |
| Promedio móvil (3) | 67,3 | 75,1 | 65,1 % | −1,9 | −0,14 |
| SES del Corte 1 (arranca en enero) | 65,2 | 76,8 | 47,3 % | 44,6 | 3,42 |
| Regresión lineal | 92,6 | 111,6 | 109,4 % | −31,8 | −1,72 |
| Ingenuo (último mes) | 104,0 | 111,9 | 101,5 % | −16,2 | −0,78 |
| Holt (α = 0,3; β = 0,3) | 106,7 | 127,5 | 126,1 % | −106,7 | −5,00 |

**2.3 Pronóstico a 12 meses.** Nivel = 151.055.237 COP/mes = **100.038 tubos/mes de planta**; error típico de un mes = 42 %.

| Mes | Índice | Pronóstico | Límite inferior (80 %) | Límite superior (80 %) |
|---|---|---|---|---|
| Sep, Oct, Nov y Dic 2026 | 1,00 | 100.038 | 46.038 | 154.038 |
| Ene 2027 | 0,63 | 63.437 | 29.194 | 97.681 |
| Feb 2027 | 1,02 | 101.928 | 46.908 | 156.949 |
| Mar 2027 | 1,33 | 133.168 | 61.285 | 205.052 |
| Abr 2027 | 0,35 | 34.747 | 15.991 | 53.503 |
| May 2027 | 1,31 | 130.836 | 60.212 | 201.461 |
| Jun 2027 | 1,04 | 103.737 | 47.740 | 159.733 |
| Jul 2027 | 1,53 | 153.027 | 70.424 | 235.631 |
| Ago 2027 | 0,79 | 79.424 | 36.551 | 122.297 |

El gráfico de la celda 14 muestra la venta real escalada a planta (gris, enero a agosto de 2026), el pronóstico estacional (azul) con su banda del 80 % y el nivel plano de 100.038 (línea naranja).

**2.4 Pedido promedio:** 1.273.304 COP ≈ 99 tubos.

**3.3 Validación** (demanda plana, sin choques ni materia prima):
- **balance de masa:** 29.500 + 1.234.289 − 1.224.545 = 39.244 = inventario final − pendientes;
- **ley de Little:** WIP de 5.472 = 366 tubos/h × 14,95 h;
- **horas de equipo**, libro frente a gemelo: pesaje 124/123 (−0,6 %), mezcla 494/496 (+0,5 %), control de calidad 188/188 (0,0 %), llenado 748/743 (−0,7 %), encartonado 504/502 (−0,4 %), empaque 541/544 (+0,7 %).

**3.4 Corrida base:**
- 3.431 lecturas horarias de 16 variables.
- En el modo en vivo, la llenadora arranca el 2026-09-02 a las 13:00 y llena un lote de B a ~1.420–1.560 tubos/h; el WIP baja de 7.800 a 0 hacia las 19:00.
- Gráfica de inventario (celda 27): A oscila entre ~7.000 y ~22.000 (bodega 26.000); B entre ~4.000 y ~13.000 (bodega 18.000); **C hace un diente de sierra que sube hasta ~19.000, por encima de su bodega de 14.000**, cada vez que entra un lote doble de 15.600.
- Gráfica de una semana de la llenadora (celda 28, desde el 09/09/2026): hay tramos de marcha a ~1.450–1.950 tubos/h, alistamientos antes de cada lote y una falla de ~3 h en la mitad de la semana; el resto del tiempo la máquina está libre.

**3.5 Métricas de eficiencia** (30 réplicas):

| | Corte 1 (zona, 8 h/día) | Libro (planta) | Gemelo (planta, 12 meses) |
|---|---|---|---|
| Takt time | 41,5 s/tubo (0,69 min) | 11,1 s/tubo | 10,3 s/tubo |
| Throughput | 86,7 tubos/h | 325 tubos/h | 352 tubos/h |
| Tiempo de ciclo (flujo) | 3,5 a 5,5 h (dato de la empresa) | 12,7 a 14,5 h por lote | 16,9 h por lote |
| WIP promedio | 304 a 477 tubos | 8.500 tubos | 5.308 tubos |

Pesaje + mezcla + control de calidad según el libro: 3,9 a 5,0 h por lote, coherente con las 3,5 a 5,5 h que dio la empresa.

**3.6 Restricciones** (promedio ± intervalo del 95 %):

| Tipo | Indicador | Valor |
|---|---|---|
| Capacidad | Ocupación de la llenadora (cuello de botella) | 28,9 % ± 0,4 |
| Capacidad | Ocupación de los reactores | 10,5 % ± 0,1 |
| Capacidad | Ocupación de la encartonadora | 16,0 % ± 0,2 |
| Capacidad | Ocupación del empaque | 15,4 % ± 0,2 |
| Demanda | Nivel de servicio (despacho inmediato) | 99,99 % ± 0,02 |
| Demanda | Mayor acumulado de pendientes | 0 tubos |
| Almacenamiento | Inventario total máximo | 49.226 ± 627 tubos (bodega de 58.000) |
| Almacenamiento | Días con la bodega total sobre su capacidad | 0,0 % |
| Almacenamiento | **Días con C sobre su bodega** | **32,3 % ± 1,1** |
| Materia prima | Menor existencia de base y colorantes | 800 ± 152 kg |

La causa del problema de C es que su punto de reorden + lote (20.100) es mayor que su bodega (14.000). En 3 de 30 réplicas algún lote esperó materia prima.

**3.7 Escenarios** (mismas semillas):

| Escenario | Servicio | Inventario promedio | Días C sobre bodega | Llenadora | Flujo por lote | Réplicas con faltante de MP |
|---|---|---|---|---|---|---|
| Base: política del libro | 99,99 % | 34.697 | 32,3 % | 28,9 % | 16,9 h | 3 |
| Sin estacionalidad | 100,00 % | 34.724 | 32,3 % | 29,0 % | 16,8 h | 0 |
| Punto de reorden ajustado con el pronóstico | 99,97 % | 36.740 | 36,9 % | 28,7 % | 17,1 h | 1 |
| Compras con pronóstico sin estacionalidad | 99,85 % | 34.627 | 32,1 % | 28,9 % | 16,9 h | 6 |
| **Lote de C de 7.800 tubos** | 99,96 % | **31.108** | **0,0 %** | 29,5 % | 16,1 h | 1 |
| Un solo turno | 97,97 % | 28.240 | 19,9 % | 57,5 % | 18,3 h | 1 |

**Prueba de estrés** (celda 35, punto de reorden ajustado con el pronóstico, sin materia prima; valores leídos de la gráfica):

| Factor de demanda | 1,0 | 1,5 | 2,0 | 2,5 | 3,0 | 3,5 |
|---|---|---|---|---|---|---|
| Ocupación de la llenadora | 28,7 % | 43,3 % | 57,9 % | 72,2 % | 85,9 % | 94,3 % |
| Nivel de servicio | 100,0 % | 99,9 % | 99,4 % | 93,9 % | 70,8 % | 43,9 % |

### Conclusiones

1. El SES del Corte 1 estaba **sesgado** por arrancar en enero. Con el nivel inicial igual al promedio de 3 meses (mismo $\alpha$ = 0,05), el sesgo baja de 44,6 a 2,4 millones COP y el RMSE un 17 %. La demanda de planta queda en ~100.000 tubos/mes, sin tendencia y con ±42 % de error mensual.
2. El gemelo está **validado**: cuadran el balance de masa y la ley de Little, y las horas de equipo quedan dentro de ±0,7 % del libro.
3. **La capacidad sobra:** la llenadora (cuello de botella) trabaja al ~29 %. La planta aguanta unas 2 veces la demanda con ≥ 99 % de servicio; el libro calcula 3,37 veces porque no considera colas ni variabilidad.
4. El problema real es la **bodega de C**. Bajar su lote a 7.800 tubos elimina los días sobre la bodega y reduce el inventario promedio un 10,3 %.
5. Las compras de materia prima deben usar el pronóstico **con** estacionalidad: sin ella, los faltantes de materia prima pasan de 3 a 6 réplicas.

### Supuestos y advertencias

- **Escala zona → planta** (11,7 %): los índices estacionales salen de un solo vendedor y se aplican a toda la planta.
- **Jornada:** el gemelo usa los 2 turnos de 7 h de lunes a viernes del libro; el Corte 1 suponía 1 turno de 8 h de lunes a sábado.
- **Índices de septiembre a diciembre = 1** (supuesto), y la estacionalidad se trata como escenario porque no se puede validar con un año incompleto.
- **El $\alpha$ óptimo (0,05) quedó en el extremo inferior de la rejilla:** el SES se comporta casi como el promedio histórico.
- Se supone que al inicio **ya hay materia prima en tránsito** (el stock de 3.600 kg cubre unos 13 días frente a 40 de lead time).
- Supuestos propios del gemelo: choque mensual del 10 %, CV de reparación de 0,5, sublotes de 600 tubos, revisión de compras cada 5 días.
- **No se modelan:**
  - mano de obra;
  - tubos vacíos ni cartón;
  - reprocesos (los defectuosos se descartan).
- La bodega **se mide, no se impone**: el inventario puede pasar la capacidad.
- La llenadora libera la máquina entre sublotes, pero la prioridad por orden de llegada hace que cada lote se llene completo antes del siguiente.
- La tabla de la celda 30 escribe a mano los valores del Corte 1 (41,5 s, 86,7 tubos/h, 304–477), no los recalcula.
- La prueba de estrés solo tiene salida gráfica; los números de arriba se leyeron de las etiquetas del gráfico.
- Para correrlo, el libro debe estar en la misma carpeta con el nombre `Datos Thyms Completo.xlsx` (ruta relativa en `ARCHIVO`).

> **Contenido completo omitido en este paquete:** Las celdas 0–35 de este cuaderno son idénticas (código y salidas) a las de `Gemelo_Digital_Thyms_MEJORADO`, cuyo contenido completo sí está en este paquete.


---

<!-- fuente: corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms_MEJORADO.md -->
# Gemelo_Digital_Thyms_MEJORADO

> **Archivo:** [`Gemelo_Digital_Thyms_MEJORADO.ipynb`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms_MEJORADO.ipynb) · **Corte 2** · Cuaderno Jupyter con 45 celdas  
> **Nombre original:** `CORTE 2/Gemelo_Digital_Thyms MEJORADO.ipynb`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

### Qué es

**Cuaderno principal** del proyecto del Corte 2 sobre THYMS Colombia S.A.S. (45 celdas). Es el cuaderno base [`Gemelo_Digital_Thyms.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md) más dos secciones nuevas que conectan el gemelo digital con la **planeación agregada (S&OP)** de la hoja `Plan Agregado` de [`Datos Thyms Completo.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Datos%20Thyms%20Completo.md).

**Qué agrega exactamente frente al base:**
- Las **celdas 0 a 35 son idénticas** al cuaderno base: mismo código y mismas salidas guardadas (comprobado comparando el JSON de los dos `.ipynb`). Todo lo de las secciones 1 a 3 (pronóstico, gemelo, validación, métricas, restricciones, escenarios y estrés) está explicado en el resumen de [`Gemelo_Digital_Thyms.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md) y no se repite aquí.
- Las **celdas 36 a 44 son nuevas** (2 de Markdown y 7 de código):
  - la **sección 4** simula mes a mes el plan agregado de persecución y el nivelado con demanda aleatoria;
  - la **sección 5** mete ese plan dentro del gemelo detallado (liberación de lotes según el plan, a lazo abierto) y lo compara con el gemelo de punto de reorden, con **exactamente la misma demanda**.
- **Las celdas 36 a 44 no tienen salidas guardadas** (nunca se ejecutaron en el archivo). Los números de abajo vienen de una corrida aparte documentada en [`CONTEXTO_GEMELO_THYMS.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/CONTEXTO_GEMELO_THYMS.md), sección 7; la presentación [`THYMS-presentacion-corte-2.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/THYMS-presentacion-corte-2.md) (página 6) muestra los mismos resultados principales.
- Ninguna celda anterior cambia: la clase `GemeloThyms` se reutiliza por herencia.

### Estructura de las secciones nuevas

| Celda | Sección | Qué hace |
|---|---|---|
| 36 | 4. Gemelo digital guiado por el Plan Agregado (S&OP) | Markdown: se simulan persecución y nivelada con la misma semilla, es decir, con la misma demanda real |
| 37 | Carga del plan | `_norm()` quita tildes. `cargar_plan_agregado()` lee la hoja `Plan Agregado` con `pd.read_excel(header=None)`, busca los parámetros por texto en la columna A (inventario inicial, bodega, capacidad de la llenadora, horas por día, costo de mantener), ubica la fila «Mes» y las columnas de cada estrategia. Devuelve `df_plan` (Mes, Días hábiles, Demanda Plan, Prod persecucion, Prod nivelada, Prod mixta) y `PRM_SOP` |
| 38 | Simulación agregada | `simular_gemelo_sop(df_plan, estrategia, variabilidad_demanda=0.05, seed=42)`: un paso de SimPy por mes (ver métodos) |
| 39 | Corrida | `ESTRATEGIAS_SOP = ["Persecucion", "Nivelada"]`; tabla mensual de cada una y resumen anual |
| 40 | Gráfica | Inventario final de cada mes frente al límite de bodega (58.000), con los meses que la saturan marcados en rojo |
| 41 | 5. Comparación con la misma demanda | Markdown: tabla de los 5 modelos y supuestos (reparto 48/30/22 %, pedidos reescalados al total del mes, plan dividido por el rendimiento, calendario de enero a diciembre de 2026) |
| 42 | Gemelo guiado por el plan | `INICIO_PLAN` = 2026-01-01; clase `GemeloThymsSOP(GemeloThyms)`; funciones `kpis_gemelo()` y `kpis_agregado()`; lista `KPIS` |
| 43 | Comparación | `comparar_modelos(df_plan, n_rep=30)`, aviso de diferencia de días hábiles, tabla de promedio ± intervalo del 95 % y tabla «Mejor modelo» por KPI |
| 44 | Gráfica | (a) Inventario a fin de mes, promedio de réplicas, de los 5 modelos con el límite de bodega; (b) barras del costo anual de inventario de los 3 gemelos con su nivel de servicio |

### Datos que usa

- Todo lo de las secciones 1 a 3 (libro de Excel, pronóstico `PRON` y clase `GemeloThyms`).
- Hoja **`Plan Agregado`**, leída con `pd.read_excel`, es decir, los **valores calculados que Excel guardó** de las fórmulas:
  - demanda mensual de 63.413 a 152.969 (1.200.000 al año);
  - producción de persecución (= demanda) y nivelada (100.000/mes);
  - días hábiles por mes (246 al año);
  - inventario inicial 29.500, bodega 58.000, llenadora 1.675,47 tubos/h, 14 h/día, costo de mantener 83,56 COP/tubo-mes.

### Métodos

**Sección 4: modelo agregado mensual** (`simular_gemelo_sop`). Para cada mes $t$:
- demanda real: $\tilde{D}_t \sim \mathcal{N}(D_t, (0{,}05\,D_t)^2)$ truncada en 0;
- capacidad: $K_t = n_t \cdot 14 \cdot 1.675{,}47$;
- producción real: $P^{real}_t = \min(P^{plan}_t, K_t)$;
- inventario: $I_t = \max(0,\ I_{t-1} + P^{real}_t - \tilde{D}_t)$, es decir, **la venta no atendida se pierde**;
- desabastecimiento: $\max(0,\ \tilde{D}_t - I_{t-1} - P^{real}_t)$;
- saturación de bodega si $I_t > 58.000$;
- costo: $I_t \cdot 83{,}56$.

**Sección 5: gemelo guiado por el plan** (`GemeloThymsSOP`, que hereda de `GemeloThyms`):
- **Calendario:** pone la variable global `INICIO` en 2026-01-01 mientras se construye el objeto y la restaura con `try/finally`.
- **Demanda dada:**
  - la demanda mensual de la réplica se reparte en A, B y C (48/30/22 %);
  - se generan pedidos diarios con Poisson + lognormal (con su propio generador, semilla + 20.000) y se reescalan para que cada mes sume exactamente esa demanda;
  - sobrescribe `_demanda_del_dia`.
- **Producción:**
  - sin plan (`plan_prod=None`), usa el punto de reorden de siempre (lazo cerrado);
  - con plan, la cuota diaria es $P^{plan}_t \cdot w_p / n_t / y_p$ ($w_p$ = participación, $y_p$ = rendimiento). Se acumula en un crédito y se lanza un lote de 7.800 cada vez que el crédito lo alcanza (**lazo abierto**: no mira el inventario).
- **`comparar_modelos`:** en cada réplica $i$ (semilla 2026 + $i$, 30 réplicas) corre los dos modelos agregados. Su demanda, idéntica en ambos, alimenta tres gemelos: punto de reorden, plan de persecución y plan nivelado.
- **KPI:** demanda, producción, nivel de servicio, no atendido, inventario a fin de mes (promedio y máximo), meses y días sobre la bodega, costo anual = $\sum_t I^{fin}_t \cdot 83{,}56$ y ocupación de la llenadora. Intervalo del 95 %: $t_{0{,}975;\,29}\,s/\sqrt{30}$.
- **Tabla «Mejor modelo»:** para cada KPI elige el mejor de los 3 gemelos y dice si la diferencia con el segundo es significativa (brecha mayor que la suma de las semiamplitudes).

### Resultados clave con números

> Las celdas 36 a 44 no tienen salidas en el `.ipynb`. Estos números son de la corrida documentada en [`CONTEXTO_GEMELO_THYMS.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/CONTEXTO_GEMELO_THYMS.md) (sección 7); los de nivel de servicio e inventario coinciden con la página 6 de la presentación.

**Sección 4** (semilla 42, variabilidad del 5 %):

| | Persecución | Nivelada |
|---|---|---|
| Inventario final máximo | 28.455 | 86.700 |
| Meses sobre la bodega | 0 | 4 (enero, febrero, abril y mayo) |
| Desabastecimiento | 0 | 7.799 (julio) |
| Costo de inventario al año | 18,72 M COP | 38,30 M COP |

**Sección 5** (30 réplicas, ± intervalo del 95 %, misma demanda en los 5 modelos). Días hábiles: el plan cuenta 246 y el calendario del gemelo 243. Meses distintos (plan/gemelo): abril 21/20, mayo 21/19, junio 20/19, agosto 20/19, octubre 20/21, noviembre 20/19, diciembre 19/21.

| KPI | Gemelo con punto de reorden | Gemelo + persecución | Gemelo + nivelada | Agregado persecución | Agregado nivelada |
|---|---|---|---|---|---|
| Demanda anual | 1.204.081 | igual | igual | igual | igual |
| Producción anual | 1.210.571 | 1.188.007 | 1.187.973 | 1.200.000 | 1.200.000 |
| Nivel de servicio | **99,99 %** | **79,42 % ± 5,76** | 84,99 % ± 4,46 | 99,99 % | 99,79 % |
| No atendido de inmediato | 115 | 249.252 | 182.005 | 145 | 2.546 |
| Inventario promedio a fin de mes | 35.341 | 14.643 | 29.867 | 26.379 | 43.234 |
| Inventario máximo a fin de mes | 43.802 | 24.371 | 78.098 | 36.472 | 94.865 |
| Meses sobre la bodega (de 12) | 0,0 | 0,0 | 1,5 | 0,1 | 3,9 |
| Días sobre la bodega | 0,0 % | 0,0 % | 9,7 % | — | — |
| Costo de inventario al año | 35,44 M | 14,68 M | 29,95 M | 26,45 M | 43,35 M |
| Ocupación de la llenadora | 29,4 % | 30,1 % | 30,1 % | 20,7 % | 20,8 % |

**Gráfica de la celda 44.** Una versión parecida está en la página 6 de la presentación, cuyo panel (b) muestra el inventario promedio en lugar del costo. Lo que se ve:
- el gemelo con punto de reorden se mantiene entre ~32.000 y ~38.000 tubos todo el año;
- el gemelo con persecución queda entre ~9.000 y ~17.000;
- el gemelo nivelado sube a ~78.000 en abril (sobre la bodega) y cae a casi 0 en julio;
- los modelos agregados (líneas punteadas) van por encima de sus gemelos.

**Por qué la persecución da 79 % en el gemelo** (diagnóstico de una réplica, según CONTEXTO):
1. el plan es fijo (1,2 M) y no corrige cuando la demanda real sale mayor;
2. al cierre quedan ~12.000 tubos de crédito sin lanzar, por el redondeo a lotes completos;
3. se producen ~1,19 M frente a ~1,20–1,22 M demandados, y el inventario se drena de 29.500 a casi 0;
4. con poco colchón y lotes que llegan a saltos de 7.800, hay quiebres dentro del mes.

El modelo agregado no lo ve porque mira solo el cierre del mes y da por perdida la venta no atendida.

### Conclusiones

1. El plan agregado de **persecución** es el factible (la nivelada no cabe en la bodega), y sirve para fijar volúmenes de capacidad y compras.
2. Ejecutarlo **a lazo abierto** dentro del gemelo da solo **79,4 %** de servicio, frente al 99,99 % del punto de reorden. La liberación diaria de lotes debe reaccionar al inventario: el plan fija los volúmenes y el punto de reorden libera los lotes (la presentación lo resume como «79,4 % → 99,99 %, por validar»).
3. Las cifras del modelo agregado (99,99 % de servicio en persecución) son optimistas frente al detallado, porque ignoran fallas, alistamientos, rendimiento y el día a día del inventario.

### Supuestos y advertencias

- **La tabla «Mejor modelo» engaña:** declara a la persecución mejor en inventario y costo, pero sale barata porque está desabastecida (79 % de servicio). Habría que comparar al mismo nivel de servicio o sumar un costo de faltante.
- **El agregado y el detallado miden distinto:**
  - el agregado pierde las ventas y mide a fin de mes; el gemelo acumula pendientes y mide a diario;
  - la ocupación del agregado es producción/capacidad (promedio de los meses), y la del gemelo, horas de marcha + alistamiento + falla.
- **Rompe la regla de «solo datos de entrada»:** las secciones 4 y 5 leen resultados de fórmulas del Excel (valores guardados). Si el libro se edita sin recalcular en Excel, leerán valores viejos o vacíos.
- **La estrategia mixta** se carga pero no se simula.
- **Calendario:** 246 días hábiles en el plan frente a 243 en el gemelo; además, `GemeloThymsSOP` modifica temporalmente la variable global `INICIO` (funciona, pero es frágil).
- La celda 37 vuelve a importar `scipy.stats`. En la tabla «Mejor modelo», «Días sobre bodega» puede declarar ganador con una ventaja de 0,0 en lugar de empate, porque la brecha se compara con `> 0` antes de redondear.
- Supuestos de la sección 5: demanda mensual con CV del 5 %, reparto fijo 48/30/22 % y plan dividido por el rendimiento para cubrir tubos buenos.
- Para reproducir los números hay que ejecutar el cuaderno completo (la sección 5 tarda ~10 s; las réplicas de la sección 3 son lo más lento).

## Contenido del cuaderno

> Todas las celdas con su código y sus salidas de texto. Los gráficos (imágenes) se marcan como `[gráfico]`; el .ipynb conserva las imágenes.

<!-- celda 0 · markdown -->
# THYMS Colombia — Pronóstico de demanda y gemelo digital de la planta



**Para correrlo:** el archivo `Datos Thyms Completo.xlsx` debe estar en la misma carpeta. Todos
los supuestos están en la celda *Configuración*.

<!-- celda 1 · markdown -->
## 1. Configuración y datos

<!-- celda 2 · código -->
```python
import math
import datetime as dt

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import openpyxl
import simpy                 # si falta: pip install simpy
```

<!-- celda 3 · código -->
```python
# ---------------- Configuración (supuestos editables) ----------------
ARCHIVO = "Datos Thyms Completo.xlsx"

PRECIO_UND = 12_900          # COP por tubo; el valor que se usó en el Corte 1 para pasar de pesos a unidades
INDICE_SUPUESTO = {9: 1.0, 10: 1.0, 11: 1.0, 12: 1.0}   # índice estacional de los meses SIN datos (sep-dic)
CV_CHOQUE_MENSUAL = 0.10     # variación mensual de la demanda que el pronóstico no explica (supuesto)

INICIO = dt.date(2026, 9, 1) # primer mes sin datos reales
MESES = 12

SUBLOTE = 600                # tubos que pasan juntos de llenado a encartonado y empaque (25 cajas master)
KG_LOTE = 500                # kg de base y colorantes por lote
CV_MTTR = 0.5                # dispersión del tiempo de reparación; el libro solo da el promedio
SS_MP_DIAS = 15              # stock de seguridad de materia prima, días hábiles (hoja Restricciones)
REVISION_MP_DIAS = 5         # cada cuánto se revisa el pedido de materia prima

N_REP = 30                   # réplicas por escenario
SEMILLA = 2026

MES = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
PRODS = ["A", "B", "C"]
COLOR = {"A": "#2a78d6", "B": "#eb6834", "C": "#1baf7a", "gris": "#898781"}
plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.grid": True, "grid.color": "#e1e0d9", "axes.titleweight": "bold",
                     "axes.titlelocation": "left", "legend.frameon": False})

def es(x, d=0):
    """Número con formato en español: 1.234.567,8"""
    return f"{x:,.{d}f}".replace(",", "§").replace(".", ",").replace("§", ".")

def tabla(df, dec=0):
    """La misma tabla con los números en formato español (dec: decimales, o dict por columna)."""
    out = df.copy()
    for col in out.select_dtypes("number").columns:
        d = dec.get(col, 0) if isinstance(dec, dict) else dec
        out[col] = out[col].map(lambda v, d=d: es(v, d))
    return out
```

<!-- celda 4 · markdown -->
Del libro solo se leen **datos de entrada**; lo que allí es fórmula se calcula aquí.

<!-- celda 5 · código -->
```python
def cargar_datos(ruta):
    wb = openpyxl.load_workbook(ruta)
    v = lambda hoja, ref: wb[hoja][ref].value
    assert str(v("Productos", "L4")).startswith("Punto de reorden"), "Cambió la hoja Productos"

    D = {"par": dict(dias_mes=v("Parámetros", "B4"), turnos=v("Parámetros", "B5"), horas_turno=v("Parámetros", "B6"),
                     tubos_lote=v("Parámetros", "B9"), und_caja=v("Parámetros", "B10"))}
    D["prod"] = pd.DataFrame([dict(p=v("Productos", f"A{r}")[0], nombre=v("Productos", f"A{r}")[3:],
                                   demanda=v("Productos", f"C{r}"), rend=v("Productos", f"E{r}"),
                                   stock=v("Productos", f"I{r}"), bodega=v("Productos", f"K{r}"),
                                   rop=v("Productos", f"L{r}"), lote=v("Productos", f"M{r}"),
                                   wip=v("Productos", f"N{r}"), mp_kg=v("Productos", f"O{r}"))
                              for r in (5, 6, 7)]).set_index("p")
    D["mp"] = dict(stock_kg=float(D["prod"].mp_kg.sum()), lead_time=v("Productos", "E12"))

    T = pd.DataFrame([dict(estacion=v("Tiempos", f"A{r}"), p=v("Tiempos", f"B{r}"), unidad=v("Tiempos", f"C{r}"),
                           prom=v("Tiempos", f"D{r}"), desv=v("Tiempos", f"E{r}"), rango=v("Tiempos", f"I{r}"))
                      for r in range(5, 23)])
    T["minimo"], T["maximo"] = T.prom * (1 - T.rango), T.prom * (1 + T.rango)
    D["tiempos"] = T.set_index(["estacion", "p"])

    D["oee"] = pd.Series({v("Utilizacion", f"A{r}"): v("Utilizacion", f"E{r}") for r in range(5, 11)})
    D["alist"] = pd.DataFrame({equipo: [v("Alistamiento", f"{col}{r}") for r in (5, 6, 7)]
                               for equipo, col in (("reactor", "B"), ("llenadora", "C"), ("encartonadora", "D"))},
                              index=["tono", "AC", "B"])                                    # minutos
    D["fallas"] = pd.DataFrame({"mtbf": [v("Fallas", f"B{r}") for r in range(5, 10)],
                                "mttr": [v("Fallas", f"C{r}") for r in range(5, 10)]},
                               index=[v("Fallas", f"A{r}") for r in range(5, 10)])
    D["ventas"] = np.array([v("Ventas", f"B{r}") for r in range(5, 13)], dtype=float)       # COP, ene-ago 2026
    ws, r, cop = wb["Facturas Mayo-Julio"], 5, []
    while ws[f"A{r}"].value is not None:
        cop.append(float(ws[f"E{r}"].value)); r += 1
    D["facturas"] = np.array(cop)                                                           # COP por pedido
    return D

D = cargar_datos(ARCHIVO)
prod, par = D["prod"], D["par"]
prod[["nombre", "demanda", "rend", "stock", "bodega", "rop", "lote"]]
```

Salida:
```text
nombre  demanda   rend  stock  bodega   rop   lote
p                                                                             
A        Kolorezza permanente 60 g    48000  0.985  14000   26000  8000  15600
B        Visalia sin amoníaco 60 g    30000  0.975   8500   18000  5500   7800
C  Thym's Coloring permanente 60 g    22000  0.988   7000   14000  4500  15600
```

<!-- celda 6 · código -->
```python
y = D["ventas"]                            # COP por mes, ene-ago 2026
DEMANDA_PLANTA = float(prod.demanda.sum()) # tubos por mes en el libro
ESCALA = DEMANDA_PLANTA / (y.mean() / PRECIO_UND)
print(f"Venta real promedio: {es(y.mean())} COP/mes = {es(y.mean()/PRECIO_UND)} tubos/mes "
      f"-> equivale al {es(100/ESCALA, 1)} % de la planta ({es(DEMANDA_PLANTA)} tubos/mes)")
```

Salida:
```text
Venta real promedio: 150.997.582 COP/mes = 11.705 tubos/mes -> equivale al 11,7 % de la planta (100.000 tubos/mes)
```

<!-- celda 7 · markdown -->
## 2. Pronóstico de demanda

### 2.1 Revisión del pronóstico del Corte 1

Suavización exponencial simple con α = 0,05, arrancando en la venta de enero, sobre enero a julio.

<!-- celda 8 · código -->
```python
def ses(serie, alpha, nivel0):
    """Suavización exponencial simple. Devuelve (pronósticos a un paso, pronóstico del mes siguiente)."""
    F, nivel = np.empty(len(serie)), nivel0
    for t, valor in enumerate(serie):
        F[t] = nivel
        nivel = alpha * valor + (1 - alpha) * nivel
    return F, nivel

def metricas(real, pron):
    e = np.asarray(real) - np.asarray(pron)
    mad = np.abs(e).mean()
    return dict(MAD=mad, RMSE=np.sqrt((e ** 2).mean()), MAPE=(np.abs(e) / real).mean(),
                sesgo=e.mean(), senal_rastreo=e.sum() / mad)

F_c1, pron_ago_c1 = ses(y[:7], 0.05, y[0])
m_c1 = metricas(y[1:7], F_c1[1:])          # igual que en el Corte 1: febrero a julio
print(f"MAD = {es(m_c1['MAD'])} COP | MAPE = {es(100*m_c1['MAPE'], 1)} %")
print(f"Sesgo (error promedio) = {es(m_c1['sesgo'])} COP | Señal de rastreo = {es(m_c1['senal_rastreo'], 2)} (límite usual: ±4)")
print(f"Agosto: pronóstico {es(pron_ago_c1)} vs real {es(y[7])} COP")
```

Salida:
```text
MAD = 80.172.875 COP | MAPE = 53,4 %
Sesgo (error promedio) = 63.063.608 COP | Señal de rastreo = 4,72 (límite usual: ±4)
Agosto: pronóstico 114.671.388 vs real 119.882.540 COP
```

<!-- celda 9 · markdown -->
### 2.2 Elección del método

La serie no tiene tendencia significativa: se comporta como un nivel estable más variación. Los
métodos se comparan con **origen móvil**: con los primeros 3 meses se pronostica el 4.º, con los
primeros 4 el 5.º, y así hasta agosto.

<!-- celda 10 · código -->
```python
tend = stats.linregress(np.arange(len(y)), y)
print(f"Tendencia: {es(tend.slope)} COP/mes, valor p = {es(tend.pvalue, 2)} (no significativa)")

def p_holt(alpha, beta):
    def f(h):
        nivel, tend = h[0], h[1] - h[0]
        for valor in h[1:]:
            nuevo = alpha * valor + (1 - alpha) * (nivel + tend)
            tend, nivel = beta * (nuevo - nivel) + (1 - beta) * tend, nuevo
        return nivel + tend
    return f
p_ses = lambda alpha: (lambda h: ses(h, alpha, h[:3].mean())[1])     # nivel inicial = promedio de 3 meses

def origen_movil(modelo, minimo=3):
    """Métricas de pronosticar cada mes solo con los meses anteriores."""
    return metricas(y[minimo:], np.array([modelo(y[:i]) for i in range(minimo, len(y))]))

ALPHA = float(min(np.round(np.arange(0.05, 1.0, 0.05), 2), key=lambda a: origen_movil(p_ses(a))["RMSE"]))
ELEGIDO = f"SES (α={es(ALPHA, 2)}; nivel inicial promedio)"
modelos = {"Ingenuo (último mes)": lambda h: h[-1],
           "Promedio histórico": lambda h: h.mean(),
           "Promedio móvil (3)": lambda h: h[-3:].mean(),
           "SES del Corte 1 (α=0,05; arranca en enero)": lambda h: ses(h, 0.05, h[0])[1],
           ELEGIDO: p_ses(ALPHA),
           "Holt (α=0,3; β=0,3)": p_holt(0.3, 0.3),
           "Regresión lineal": lambda h: np.polyval(np.polyfit(np.arange(len(h)), h, 1), len(h))}
cv = pd.DataFrame({nombre: origen_movil(f) for nombre, f in modelos.items()}).T.sort_values("RMSE")
vista = cv.assign(MAD=cv.MAD / 1e6, RMSE=cv.RMSE / 1e6, MAPE=cv.MAPE * 100, sesgo=cv.sesgo / 1e6)
tabla(vista.rename(columns={"MAD": "MAD (M COP)", "RMSE": "RMSE (M COP)", "MAPE": "MAPE (%)",
                            "sesgo": "Sesgo (M COP)", "senal_rastreo": "Señal de rastreo"}),
      {"MAD (M COP)": 1, "RMSE (M COP)": 1, "MAPE (%)": 1, "Sesgo (M COP)": 1, "Señal de rastreo": 2})
```

Salida:
```text
Tendencia: 6.741.938 COP/mes, valor p = 0,51 (no significativa)

                                           MAD (M COP) RMSE (M COP) MAPE (%)  \
SES (α=0,05; nivel inicial promedio)              54,7         63,6     56,3   
Promedio histórico                                61,9         69,3     60,2   
Promedio móvil (3)                                67,3         75,1     65,1   
SES del Corte 1 (α=0,05; arranca en enero)        65,2         76,8     47,3   
Regresión lineal                                  92,6        111,6    109,4   
Ingenuo (último mes)                             104,0        111,9    101,5   
Holt (α=0,3; β=0,3)                              106,7        127,5    126,1   

                                           Sesgo (M COP) Señal de rastreo  
SES (α=0,05; nivel inicial promedio)                 2,4             0,22  
Promedio histórico                                   8,6             0,69  
Promedio móvil (3)                                  -1,9            -0,14  
SES del Corte 1 (α=0,05; arranca en enero)          44,6             3,42  
Regresión lineal                                   -31,8            -1,72  
Ingenuo (último mes)                               -16,2            -0,78  
Holt (α=0,3; β=0,3)                               -106,7            -5,00
```

<!-- celda 11 · markdown -->
Gana la **suavización exponencial simple con α bajo y nivel inicial igual al promedio de los
primeros meses**: el mismo método del Corte 1, corregido en el arranque. Tiene el menor RMSE y casi
no tiene sesgo; los métodos con tendencia y el ingenuo quedan muy por encima.

El MAPE del Corte 1 sale mejor porque el MAPE premia a los pronósticos bajos; para planear
producción pesa más el sesgo. Con α tan bajo el resultado es casi el promedio histórico, y el error
de un mes cualquiera es grande: por eso el pronóstico se entrega con intervalo.

<!-- celda 12 · markdown -->
### 2.3 Pronóstico a 12 meses con estacionalidad

Con un solo año incompleto no se puede validar un modelo estacional. El patrón observado se usa
como **escenario**: de enero a agosto, índice = venta del mes / promedio; de septiembre a
diciembre, el valor de `INDICE_SUPUESTO`. El pronóstico de un mes es `nivel × índice`.

<!-- celda 13 · código -->
```python
NIVEL_COP = ses(y, ALPHA, y[:3].mean())[1]                 # nivel con los 8 meses
SIGMA_REL = cv.loc[ELEGIDO, "RMSE"] / NIVEL_COP            # error típico de un mes, medido fuera de muestra
NIVEL_PLANTA = NIVEL_COP / PRECIO_UND * ESCALA             # tubos de planta por mes
INDICES = {m: y[m - 1] / y.mean() for m in range(1, 9)} | INDICE_SUPUESTO
Z = stats.norm.ppf(0.90)                                   # intervalo del 80 %

def meses_desde(inicio, k):
    return [((inicio.year + (inicio.month - 1 + i) // 12), (inicio.month - 1 + i) % 12 + 1) for i in range(k)]

pron12 = pd.DataFrame([{"Mes": f"{MES[m-1]} {a}", "Índice": INDICES[m], "Pronóstico (und)": NIVEL_PLANTA * INDICES[m]}
                       for a, m in meses_desde(INICIO, MESES)])
pron12["Límite inferior"] = pron12["Pronóstico (und)"] * (1 - Z * SIGMA_REL)
pron12["Límite superior"] = pron12["Pronóstico (und)"] * (1 + Z * SIGMA_REL)
print(f"Nivel: {es(NIVEL_COP)} COP/mes = {es(NIVEL_PLANTA)} tubos/mes de planta | error típico de un mes: {es(100*SIGMA_REL)} %")
tabla(pron12, {"Índice": 2})
```

Salida:
```text
Nivel: 151.055.237 COP/mes = 100.038 tubos/mes de planta | error típico de un mes: 42 %

         Mes Índice Pronóstico (und) Límite inferior Límite superior
0   Sep 2026   1,00          100.038          46.038         154.038
1   Oct 2026   1,00          100.038          46.038         154.038
2   Nov 2026   1,00          100.038          46.038         154.038
3   Dic 2026   1,00          100.038          46.038         154.038
4   Ene 2027   0,63           63.437          29.194          97.681
5   Feb 2027   1,02          101.928          46.908         156.949
6   Mar 2027   1,33          133.168          61.285         205.052
7   Abr 2027   0,35           34.747          15.991          53.503
8   May 2027   1,31          130.836          60.212         201.461
9   Jun 2027   1,04          103.737          47.740         159.733
10  Jul 2027   1,53          153.027          70.424         235.631
11  Ago 2027   0,79           79.424          36.551         122.297
```

<!-- celda 14 · código -->
```python
fig, ax = plt.subplots(figsize=(9, 3.6))
ax.plot([f"{MES[m]} 2026" for m in range(8)], y / PRECIO_UND * ESCALA, marker="o", color=COLOR["gris"], label="Venta real (escala planta)")
ax.fill_between(pron12.Mes, pron12["Límite inferior"], pron12["Límite superior"], color=COLOR["A"], alpha=0.15, linewidth=0, label="Intervalo del 80 %")
ax.plot(pron12.Mes, pron12["Pronóstico (und)"], marker="o", color=COLOR["A"], label="Pronóstico estacional")
ax.axhline(NIVEL_PLANTA, color=COLOR["B"], linewidth=1.5, label="Nivel (pronóstico plano)")
ax.set_ylabel("Tubos por mes"); ax.set_ylim(0, None); ax.tick_params(axis="x", labelrotation=60)
ax.yaxis.set_major_formatter(lambda v, _: es(v)); ax.legend(ncols=2, loc="upper left")
ax.set_title("Pronóstico de demanda de planta, septiembre de 2026 a agosto de 2027")
plt.show()
```

Salida:
```text
[gráfico]
```

<!-- celda 15 · markdown -->
### 2.4 El pronosticador que usa el gemelo

El gemelo consulta el pronóstico para planear y lo **actualiza cada mes** con la demanda que mide.
El tamaño de los pedidos sale de las facturas reales (lognormal).

<!-- celda 16 · código -->
```python
class Pronosticador:
    """Suavización exponencial simple sobre la demanda desestacionalizada (tubos de planta por mes)."""

    def __init__(self, nivel, alpha, indices, peso_estacional=1.0):
        self.nivel, self.alpha, self.indices, self.peso = nivel, alpha, indices, peso_estacional

    def indice(self, mes):
        return 1 + self.peso * (self.indices[mes] - 1)

    def pronostico(self, mes):
        return self.nivel * self.indice(mes)

    def actualizar(self, mes, demanda_real):
        self.nivel = self.alpha * demanda_real / self.indice(mes) + (1 - self.alpha) * self.nivel

log_ped = np.log(D["facturas"])
PRON = dict(nivel_planta=NIVEL_PLANTA, alpha=ALPHA, indices=INDICES,
            mu_pedido=log_ped.mean(), sg_pedido=log_ped.std(ddof=1))
print(f"Pedido promedio: {es(D['facturas'].mean())} COP = {es(D['facturas'].mean()/PRECIO_UND)} tubos")
```

Salida:
```text
Pedido promedio: 1.273.304 COP = 99 tubos
```

<!-- celda 17 · markdown -->
## 3. Gemelo digital de la planta

### 3.1 Qué representa

```
Pedidos de clientes ──> Producto terminado (A, B, C) ──> despacho o pendiente
                             ▲                 │ revisión diaria: ¿posición ≤ punto de reorden?
                             │                 ▼
  Materia prima ──> Pesaje ──> Mezcla (2 reactores) ──> Control de calidad
  (500 kg/lote)                                                 │
       Empaque caja master <── Encartonado <── Llenado y sellado ┘   (por sublotes de 600 tubos)
```

| Elemento | Cómo se modela | Fuente |
|---|---|---|
| Demanda | Pedidos diarios: llegadas Poisson, tamaño lognormal; nivel mensual = base × índice estacional × choque aleatorio | Facturas reales y sección 2 |
| Tiempos de proceso | Normal truncada entre mínimo y máximo, por estación y producto | Hoja `Tiempos` |
| Fallas | Tiempo entre fallas exponencial (en horas de marcha), reparación lognormal | Hoja `Fallas` |
| Alistamientos | Cambio de tono, A↔C o A/C↔B en reactor, llenadora y encartonadora | Hoja `Alistamiento` |
| OEE | Las fallas explican una parte; el resto se aplica como pérdida de velocidad | Hojas `Utilizacion` y `Fallas` |
| Calidad | Rendimiento por producto, al final de la línea | Hoja `Productos` |
| Control de producción | Punto de reorden y lote por producto, revisión diaria | Hoja `Productos` |
| Materia prima | Revisión semanal; se pide hasta cubrir lead time + seguridad según el pronóstico | Hojas `Productos` y `Restricciones` |
| Calendario | Lunes a viernes sin festivos de Colombia; el reloj avanza solo en horas de turno | Hoja `Parámetros` |


<!-- celda 18 · código -->
```python
def pascua(a):
    """Domingo de Pascua (algoritmo de Meeus)."""
    g, c, k = a % 19, a // 100, a % 100
    h = (19 * g + c - c // 4 - (c - (c + 8) // 25 + 1) // 3 + 15) % 30
    i = (32 + 2 * (c % 4) + 2 * (k // 4) - h - k % 4) % 7
    mes, dia = divmod(h + i - 7 * ((g + 11 * h + 22 * i) // 451) + 114, 31)
    return dt.date(a, mes, dia + 1)

def festivos_colombia(a):
    lunes = lambda d: d + dt.timedelta(days=(7 - d.weekday()) % 7)      # ley Emiliani
    p = pascua(a)
    fijos = [(1, 1), (5, 1), (7, 20), (8, 7), (12, 8), (12, 25)]
    trasladables = [(1, 6), (3, 19), (6, 29), (8, 15), (10, 12), (11, 1), (11, 11)]
    f = {dt.date(a, m, d) for m, d in fijos} | {lunes(dt.date(a, m, d)) for m, d in trasladables}
    return f | {p - dt.timedelta(3), p - dt.timedelta(2)} | {p + dt.timedelta(k) for k in (43, 64, 71)}

def dias_habiles(a, m):
    fest = festivos_colombia(a)
    ultimo = (dt.date(a + m // 12, m % 12 + 1, 1) - dt.timedelta(1)).day
    return [d for d in (dt.date(a, m, k) for k in range(1, ultimo + 1)) if d.weekday() < 5 and d not in fest]
```

<!-- celda 19 · markdown -->
### 3.2 El modelo

<!-- celda 20 · código -->
```python
E_PES, E_MEZ, E_QC = "Pesaje", "Mezcla y emulsión", "Control de calidad de lote"
E_LLE, E_ENC, E_EMP = "Llenado y sellado", "Encartonado", "Empaque caja master"

CFG_BASE = dict(
    turnos=None,                    # None = los del libro
    factor_demanda=1.0,             # multiplica la demanda de planta
    peso_estacional_real=1.0,       # cuánta estacionalidad ocurre de verdad (0 = demanda plana)
    peso_estacional_pron=1.0,       # cuánta estacionalidad conoce el planeador
    cv_choque_mensual=CV_CHOQUE_MENSUAL,
    politica="rop_fijo",            # "rop_fijo" (libro) o "rop_pronostico" (se ajusta con el pronóstico)
    lote=None,                      # dict por producto para cambiar el lote del libro
    modelar_mp=True,
    sensores=False, dt_sensor=1.0)  # sensores: una lectura cada dt_sensor horas

def lognormal_media(rng, media, cv):
    s2 = math.log(1 + cv ** 2)
    return rng.lognormal(math.log(media) - s2 / 2, math.sqrt(s2))


class Maquina:
    """Equipo con estados (libre, marcha, alistamiento, falla) y fallas según horas de marcha."""

    def __init__(self, env, oee, rng, mtbf=None, mttr=None):
        self.env, self.rng, self.mtbf, self.mttr = env, rng, mtbf, mttr
        disponibilidad = mtbf / (mtbf + mttr) if mtbf else 1.0
        self.desempeno = oee / disponibilidad          # pérdida de velocidad que completa el OEE del libro
        self.vida = rng.exponential(mtbf) if mtbf else math.inf
        self.estado, self.t_cambio = "libre", 0.0
        self.horas = dict(libre=0.0, marcha=0.0, alistamiento=0.0, falla=0.0)
        self.ultimo_producto = self.ultimo_lote = None
        self.velocidad = 0.0

    def _pasar_a(self, estado):
        self.horas[self.estado] += self.env.now - self.t_cambio
        self.estado, self.t_cambio = estado, self.env.now

    def alistar(self, horas):
        if horas > 0:
            self._pasar_a("alistamiento")
            yield self.env.timeout(horas)
        self._pasar_a("libre")

    def operar(self, horas, velocidad=0.0):
        restante = horas
        while restante > 1e-12:
            tramo = min(restante, self.vida)
            self._pasar_a("marcha"); self.velocidad = velocidad
            yield self.env.timeout(tramo)
            restante -= tramo; self.vida -= tramo
            if self.vida <= 1e-12:                       # falla: se repara y el trabajo continúa
                self._pasar_a("falla"); self.velocidad = 0.0
                yield self.env.timeout(lognormal_media(self.rng, self.mttr, CV_MTTR))
                self.vida = self.rng.exponential(self.mtbf)
        self._pasar_a("libre"); self.velocidad = 0.0


class GemeloThyms:
    def __init__(self, D, PRON, cfg=None, semilla=1):
        c = self.c = {**CFG_BASE, **(cfg or {})}
        self.D, self.rng, self.rng_sensor = D, np.random.default_rng(semilla), np.random.default_rng(semilla + 10_000)
        env = self.env = simpy.Environment()
        par, prod = D["par"], D["prod"]

        # --- calendario: el reloj avanza en horas de turno ---
        self.H = (c["turnos"] or par["turnos"]) * par["horas_turno"]
        todos = meses_desde(INICIO, MESES + 4)                       # 4 meses extra para mirar hacia adelante
        self.habiles = {am: dias_habiles(*am) for am in todos}
        self.dias = [d for am in todos[:MESES] for d in self.habiles[am]]
        self.dias_ext = [d for am in todos for d in self.habiles[am]]
        self.T = len(self.dias) * self.H

        # --- política, pronóstico y datos del libro ---
        self.Q = {p: (c["lote"] or {}).get(p, prod.lote[p]) for p in PRODS}
        self.rop_base = prod.rop.to_dict()
        self.rop = dict(self.rop_base)
        self.pron = Pronosticador(PRON["nivel_planta"] * c["factor_demanda"], PRON["alpha"], PRON["indices"],
                                  c["peso_estacional_pron"])
        self.pedido_medio = math.exp(PRON["mu_pedido"] + PRON["sg_pedido"] ** 2 / 2) / PRECIO_UND   # tubos
        self.tiempos = {clave: (r.prom, r.desv, r.minimo, r.maximo) for clave, r in D["tiempos"].iterrows()}
        self.alist = {(tipo, equipo): D["alist"].loc[tipo, equipo] / 60 for tipo in D["alist"].index for equipo in D["alist"].columns}   # horas
        self.rend, self.dem_base = prod.rend.to_dict(), prod.demanda.to_dict()
        self.n_lote, self.und_caja = par["tubos_lote"], par["und_caja"]

        # --- equipos ---
        oee, fa = D["oee"], D["fallas"]
        nueva = lambda est, falla=None: Maquina(env, oee[est], self.rng, *(fa.loc[falla] if falla else (None, None)))
        self.maq = {"Pesaje": nueva(E_PES), "Control de calidad": nueva(E_QC),
                    "Reactor 1": nueva(E_MEZ, "Reactor 1"), "Reactor 2": nueva(E_MEZ, "Reactor 2"),
                    "Llenadora": nueva(E_LLE, "Llenadora de tubos"),
                    "Encartonadora": nueva(E_ENC, "Encartonadora"), "Empaque": nueva(E_EMP, "Línea de empaque")}
        self.res = {k: simpy.Resource(env, 1) for k in ("Pesaje", "Control de calidad", "Encartonadora", "Empaque")}
        self.res_llenadora = simpy.PriorityResource(env, 1)
        self.reactores = simpy.Store(env)
        self.reactores.items = [self.maq["Reactor 1"], self.maq["Reactor 2"]]

        # --- estado ---
        self.pt = {p: float(prod.stock[p]) for p in PRODS}
        self.pendiente = dict.fromkeys(PRODS, 0.0)
        self.en_proceso = dict.fromkeys(PRODS, 0.0)       # tubos lanzados que aún no llegan a bodega
        self.wip, self.wip_area, self.wip_t = 0.0, 0.0, 0.0
        self.dem_total, self.a_tiempo = dict.fromkeys(PRODS, 0.0), dict.fromkeys(PRODS, 0.0)
        self.lotes = dict.fromkeys(PRODS, 0)
        self.cont_llenado = self.cont_empacado = self.cont_bueno = 0.0
        self.flujo_lote, self.flujo_sub, self.espera_mp = [], [], 0.0
        self.sec_lote = self.sec_llenadora = 0
        self.mes_actual, self.dem_mes = None, 0.0
        self.diario, self.tele = [], []

        # --- materia prima ---
        rend_medio = float((prod.demanda / prod.demanda.sum() * prod.rend).sum())
        self.kg_tubo = KG_LOTE / (par["tubos_lote"] * rend_medio)    # kg de materia prima por tubo bueno
        self.lt_mp = round(D["mp"]["lead_time"] * 5 / 7)             # días calendario -> días hábiles
        if c["modelar_mp"]:
            self.mp, self.mp_transito = simpy.Container(env, init=D["mp"]["stock_kg"]), 0.0
            # Se supone que compras venía pidiendo bien: lo que falta para el objetivo ya está en tránsito
            falta = max(0.0, self._consumo_pron(0, self.lt_mp + REVISION_MP_DIAS + SS_MP_DIAS) - self.mp.level)
            k = max(1, self.lt_mp // REVISION_MP_DIAS)
            for i in range(1, k + 1):
                self._pedir_mp(math.ceil(falta / k / KG_LOTE) * KG_LOTE, i * self.lt_mp / k * self.H)

    # ------------------------------------------------------------------ utilidades
    def _muestra(self, estacion, p):
        prom, desv, minimo, maximo = self.tiempos[(estacion, p)]
        while True:
            x = self.rng.normal(prom, desv)
            if minimo <= x <= maximo:
                return x

    def _cambio(self, previo, nuevo):
        if previo is None or previo == nuevo:
            return "tono"
        return "B" if "B" in (previo, nuevo) else "AC"

    def _mover_wip(self, delta):
        self.wip_area += self.wip * (self.env.now - self.wip_t)
        self.wip, self.wip_t = self.wip + delta, self.env.now

    def _consumo_pron(self, d0, n):
        """Materia prima (kg) que el pronóstico espera consumir en n días hábiles desde el día d0."""
        tubos = sum(self.pron.pronostico(f.month) / len(self.habiles[(f.year, f.month)]) for f in self.dias_ext[d0:d0 + n])
        return tubos * self.kg_tubo

    # ------------------------------------------------------------------ materia prima
    def _pedir_mp(self, kg, espera_h):
        self.mp_transito += kg
        self.env.process(self._llegada_mp(kg, espera_h))

    def _llegada_mp(self, kg, espera_h):
        yield self.env.timeout(espera_h)
        yield self.mp.put(kg)
        self.mp_transito -= kg

    def _revisar_mp(self, d):
        objetivo = self._consumo_pron(d, self.lt_mp + REVISION_MP_DIAS + SS_MP_DIAS)
        pedir = objetivo - (self.mp.level + self.mp_transito)
        if pedir > 0:
            self._pedir_mp(math.ceil(pedir / KG_LOTE) * KG_LOTE, self.lt_mp * self.H)

    # ------------------------------------------------------------------ demanda y planeación
    def _abrir_mes(self, clave):
        if self.mes_actual is not None:
            self.pron.actualizar(self.mes_actual[1], self.dem_mes)   # el pronóstico aprende de lo que midió el gemelo
        c = self.c
        self.mes_actual, mes, n = clave, clave[1], len(self.habiles[clave])
        indice = 1 + c["peso_estacional_real"] * (self.pron.indices[mes] - 1)
        choque = lognormal_media(self.rng, 1.0, c["cv_choque_mensual"]) if c["cv_choque_mensual"] > 0 else 1.0
        self.tasa_dia = {p: self.dem_base[p] * c["factor_demanda"] * indice * choque / n for p in PRODS}
        self.dem_mes = 0.0
        if c["politica"] == "rop_pronostico":      # el punto de reorden sigue a la demanda diaria pronosticada
            relacion = (self.pron.pronostico(mes) / n) / (sum(self.dem_base.values()) / self.D["par"]["dias_mes"])
            self.rop = {p: self.rop_base[p] * relacion for p in PRODS}

    def _demanda_del_dia(self):
        for p in PRODS:
            k = self.rng.poisson(self.tasa_dia[p] / self.pedido_medio)
            q = float(np.round(self.rng.lognormal(PRON["mu_pedido"], PRON["sg_pedido"], k) / PRECIO_UND).sum())
            despacho = min(q, self.pt[p])
            self.pt[p] -= despacho; self.pendiente[p] += q - despacho
            self.dem_total[p] += q; self.a_tiempo[p] += despacho; self.dem_mes += q

    def _revisar_produccion(self):
        for p in PRODS:
            posicion = self.pt[p] + self.en_proceso[p] - self.pendiente[p]
            while posicion <= self.rop[p]:
                for _ in range(max(1, round(self.Q[p] / self.n_lote))):
                    self.sec_lote += 1
                    self.en_proceso[p] += self.n_lote
                    self.env.process(self._lote(dict(id=self.sec_lote, p=p)))
                posicion += self.Q[p]

    # ------------------------------------------------------------------ producción
    def _lote(self, lote):
        env, p, alist, n_lote = self.env, lote["p"], self.alist, self.n_lote
        if self.c["modelar_mp"]:
            t0 = env.now
            yield self.mp.get(KG_LOTE)
            self.espera_mp += env.now - t0
        lote["inicio"] = env.now; self.lotes[p] += 1; self._mover_wip(n_lote)

        with self.res["Pesaje"].request() as turno:
            yield turno
            m = self.maq["Pesaje"]
            yield from m.operar(self._muestra(E_PES, p) / 60 / m.desempeno)

        reactor = yield self.reactores.get()
        yield from reactor.alistar(alist[(self._cambio(reactor.ultimo_producto, p), "reactor")])
        yield from reactor.operar(self._muestra(E_MEZ, p) / 60 / reactor.desempeno)
        reactor.ultimo_producto = p
        yield self.reactores.put(reactor)

        with self.res["Control de calidad"].request() as turno:
            yield turno
            m = self.maq["Control de calidad"]
            yield from m.operar(self._muestra(E_QC, p) / 60 / m.desempeno)

        self.sec_llenadora += 1
        orden, m, n_sub = self.sec_llenadora, self.maq["Llenadora"], n_lote // SUBLOTE
        for k in range(n_sub):                       # el lote se llena completo antes de dar paso a otro
            with self.res_llenadora.request(priority=orden) as turno:
                yield turno
                if k == 0:
                    yield from m.alistar(alist[(self._cambio(m.ultimo_producto, p), "llenadora")])
                    m.ultimo_producto = p
                vel = self._muestra(E_LLE, p) * m.desempeno          # tubos/h reales
                yield from m.operar(SUBLOTE / vel, velocidad=vel)
                self.cont_llenado += SUBLOTE
            env.process(self._sublote(lote, ultimo=(k == n_sub - 1)))

    def _sublote(self, lote, ultimo):
        p = lote["p"]
        with self.res["Encartonadora"].request() as turno:
            yield turno
            m = self.maq["Encartonadora"]
            if m.ultimo_lote != lote["id"]:
                yield from m.alistar(self.alist[(self._cambio(m.ultimo_producto, p), "encartonadora")])
                m.ultimo_lote, m.ultimo_producto = lote["id"], p
            yield from m.operar(SUBLOTE / (self._muestra(E_ENC, p) * m.desempeno))
        with self.res["Empaque"].request() as turno:
            yield turno
            m = self.maq["Empaque"]
            yield from m.operar(SUBLOTE / (self._muestra(E_EMP, p) * self.und_caja * m.desempeno))
        buenos = float(self.rng.binomial(SUBLOTE, self.rend[p]))
        self.cont_empacado += SUBLOTE; self.cont_bueno += buenos
        self.en_proceso[p] -= SUBLOTE; self._mover_wip(-SUBLOTE)
        atender = min(buenos, self.pendiente[p])                     # primero los pedidos pendientes
        self.pendiente[p] -= atender; self.pt[p] += buenos - atender
        self.flujo_sub.append(self.env.now - lote["inicio"])
        if ultimo:
            self.flujo_lote.append(self.env.now - lote["inicio"])

    # ------------------------------------------------------------------ reloj diario y sensores
    def _dias(self):
        for d, fecha in enumerate(self.dias):
            if (fecha.year, fecha.month) != self.mes_actual:
                self._abrir_mes((fecha.year, fecha.month))
            self._demanda_del_dia()
            self._revisar_produccion()
            if self.c["modelar_mp"] and d % REVISION_MP_DIAS == 0:
                self._revisar_mp(d)
            yield self.env.timeout(self.H)
            self.diario.append(dict(fecha=fecha, mp_kg=self.mp.level if self.c["modelar_mp"] else np.nan,
                                    **{f"pt_{p}": self.pt[p] for p in PRODS},
                                    **{f"pend_{p}": self.pendiente[p] for p in PRODS}))

    def lectura(self):
        """Lo que reportan los sensores virtuales en este instante."""
        d = min(int(self.env.now // self.H), len(self.dias) - 1)
        m, vel = self.maq, self.maq["Llenadora"].velocidad
        return {"t_h": round(self.env.now, 2),
                "momento": dt.datetime.combine(self.dias[d], dt.time(6)) + dt.timedelta(hours=self.env.now - d * self.H),
                "llenadora_estado": m["Llenadora"].estado,
                "llenadora_vel_und_h": round(vel * (1 + self.rng_sensor.normal(0, 0.01))) if vel else 0,
                "llenadora_contador": self.cont_llenado, "empaque_contador": self.cont_empacado,
                "reactor1_estado": m["Reactor 1"].estado, "reactor2_estado": m["Reactor 2"].estado,
                "encartonadora_estado": m["Encartonadora"].estado, "empaque_estado": m["Empaque"].estado,
                **{f"pt_{p}": self.pt[p] for p in PRODS}, "wip_tubos": self.wip,
                "pendiente_und": sum(self.pendiente.values()),
                "mp_kg": self.mp.level if self.c["modelar_mp"] else np.nan}

    def _sensores(self):
        while True:
            self.tele.append(self.lectura())
            yield self.env.timeout(self.c["dt_sensor"])

    def iniciar(self):
        self._proc = self.env.process(self._dias())
        if self.c["sensores"]:
            self.env.process(self._sensores())
        return self

    def correr(self):
        self.iniciar()
        self.env.run(until=self._proc)
        self._mover_wip(0)
        for m in self.maq.values():
            m._pasar_a(m.estado)
        return self

    # ------------------------------------------------------------------ resultados
    def kpis(self):
        d, prod, T, m = pd.DataFrame(self.diario), self.D["prod"], self.T, self.maq
        dem = sum(self.dem_total.values())
        pt_total = d[[f"pt_{p}" for p in PRODS]].sum(axis=1)
        ocup = lambda *eq: 100 * sum(m[x].horas["marcha"] + m[x].horas["alistamiento"] + m[x].horas["falla"] for x in eq) / T / len(eq)
        return {"nivel_servicio_%": 100 * sum(self.a_tiempo.values()) / dem,
                "pendiente_max_und": d[[f"pend_{p}" for p in PRODS]].sum(axis=1).max(),
                "pt_prom_und": pt_total.mean(), "pt_max_und": pt_total.max(),
                "dias_sobre_bodega_%": 100 * (pt_total > prod.bodega.sum()).mean(),
                **{f"dias_{p}_sobre_bodega_%": 100 * (d[f"pt_{p}"] > prod.bodega[p]).mean() for p in PRODS},
                "takt_s_und": T * 3600 / dem, "throughput_und_h": self.cont_bueno / T,
                "flujo_lote_h": np.mean(self.flujo_lote), "flujo_tubo_h": np.mean(self.flujo_sub),
                "wip_prom_tubos": self.wip_area / T, "lotes": len(self.flujo_lote),
                "ocup_pesaje_%": ocup("Pesaje"), "ocup_mezcla_%": ocup("Reactor 1", "Reactor 2"),
                "ocup_calidad_%": ocup("Control de calidad"), "ocup_llenadora_%": ocup("Llenadora"),
                "ocup_encartonadora_%": ocup("Encartonadora"), "ocup_empaque_%": ocup("Empaque"),
                "mp_min_kg": d.mp_kg.min(), "espera_mp_h": self.espera_mp}


def replicar(cfg=None, n=N_REP, semilla=SEMILLA):
    return pd.DataFrame([GemeloThyms(D, PRON, cfg, semilla + i).correr().kpis() for i in range(n)])
```

<!-- celda 21 · markdown -->
### 3.3 Validación

Con demanda plana, el gemelo se compara con cuentas que se pueden hacer a mano: balance de masa,
horas de equipo según el libro (unidades / capacidad nominal / OEE) y ley de Little.

<!-- celda 22 · código -->
```python
cfg_val = dict(peso_estacional_real=0, peso_estacional_pron=0, cv_choque_mensual=0, modelar_mp=False)
g = GemeloThyms(D, PRON, cfg_val, SEMILLA).correr()
k = g.kpis()
dem = sum(g.dem_total.values())
print(f"Balance de masa: inicial {es(prod.stock.sum())} + producción {es(g.cont_bueno)} - demanda {es(dem)} = "
      f"{es(prod.stock.sum() + g.cont_bueno - dem)} | inventario final - pendientes = {es(sum(g.pt.values()) - sum(g.pendiente.values()))}")
print(f"Ley de Little: WIP medido = {es(k['wip_prom_tubos'])} tubos | tasa × tiempo de flujo = "
      f"{es(g.cont_empacado / g.T)} × {es(k['flujo_tubo_h'], 2)} = {es(g.cont_empacado / g.T * k['flujo_tubo_h'])} tubos")

EQUIPOS = {E_PES: ["Pesaje"], E_MEZ: ["Reactor 1", "Reactor 2"], E_QC: ["Control de calidad"],
           E_LLE: ["Llenadora"], E_ENC: ["Encartonadora"], E_EMP: ["Empaque"]}
def horas_nominales_lote(est, p):
    r = D["tiempos"].loc[(est, p)]
    if r.unidad == "min/lote":
        return r.prom / 60
    return par["tubos_lote"] / (r.prom * (par["und_caja"] if r.unidad == "cajas/h" else 1))

val = pd.DataFrame({
    "Horas según el libro": {e: sum(g.lotes[p] * horas_nominales_lote(e, p) for p in PRODS) / D["oee"][e] for e in EQUIPOS},
    "Horas en el gemelo": {e: sum(g.maq[x].horas["marcha"] + g.maq[x].horas["falla"] for x in eq) for e, eq in EQUIPOS.items()}})
val["Diferencia (%)"] = 100 * (val["Horas en el gemelo"] / val["Horas según el libro"] - 1)
tabla(val, {"Diferencia (%)": 1})
```

Salida:
```text
Balance de masa: inicial 29.500 + producción 1.234.289 - demanda 1.224.545 = 39.244 | inventario final - pendientes = 39.244
Ley de Little: WIP medido = 5.472 tubos | tasa × tiempo de flujo = 366 × 14,95 = 5.472 tubos

                           Horas según el libro Horas en el gemelo  \
Pesaje                                      124                123   
Mezcla y emulsión                           494                496   
Control de calidad de lote                  188                188   
Llenado y sellado                           748                743   
Encartonado                                 504                502   
Empaque caja master                         541                544   

                           Diferencia (%)  
Pesaje                               -0,6  
Mezcla y emulsión                     0,5  
Control de calidad de lote           -0,0  
Llenado y sellado                    -0,7  
Encartonado                          -0,4  
Empaque caja master                   0,7
```

<!-- celda 23 · markdown -->
### 3.4 Corrida base con sensores virtuales

Doce meses con la política actual del libro (punto de reorden y lote fijos) y la demanda
estacional. Los sensores toman una lectura cada hora de turno.

<!-- celda 24 · código -->
```python
base = GemeloThyms(D, PRON, dict(sensores=True), SEMILLA).correr()
tele, diario = pd.DataFrame(base.tele), pd.DataFrame(base.diario)
print(f"Lecturas de sensores: {es(len(tele))} | variables por lectura: {tele.shape[1]}")
tele.iloc[30:35]
```

Salida:
```text
Lecturas de sensores: 3.431 | variables por lectura: 16


     t_h             momento llenadora_estado  llenadora_vel_und_h  \
30  30.0 2026-09-03 08:00:00            libre                    0   
31  31.0 2026-09-03 09:00:00            libre                    0   
32  32.0 2026-09-03 10:00:00            libre                    0   
33  33.0 2026-09-03 11:00:00     alistamiento                    0   
34  34.0 2026-09-03 12:00:00     alistamiento                    0   

    llenadora_contador  empaque_contador reactor1_estado reactor2_estado  \
30              7800.0            7800.0    alistamiento          marcha   
31              7800.0            7800.0    alistamiento          marcha   
32              7800.0            7800.0          marcha    alistamiento   
33              7800.0            7800.0          marcha          marcha   
34              7800.0            7800.0          marcha          marcha   

   encartonadora_estado empaque_estado    pt_A     pt_B    pt_C  wip_tubos  \
30                libre          libre  7328.0  12033.0  4033.0    31200.0   
31                libre          libre  7328.0  12033.0  4033.0    31200.0   
32                libre          libre  7328.0  12033.0  4033.0    31200.0   
33                libre          libre  7328.0  12033.0  4033.0    31200.0   
34                libre          libre  7328.0  12033.0  4033.0    31200.0   

    pendiente_und   mp_kg  
30            0.0  1100.0  
31            0.0  1100.0  
32            0.0  1100.0  
33            0.0  1100.0  
34            0.0  1100.0
```

<!-- celda 25 · markdown -->
**En tiempo real.** El gemelo también se puede avanzar paso a paso y leer en cualquier momento,
que es como se conectaría a un tablero. Aquí se avanza hora por hora desde que la llenadora
recibe su primer lote.

<!-- celda 26 · código -->
```python
vivo = GemeloThyms(D, PRON, None, SEMILLA).iniciar()
while vivo.maq["Llenadora"].estado == "libre":
    vivo.env.run(until=vivo.env.now + 1)
for _ in range(8):
    s = vivo.lectura()
    print(f"{s['momento']:%Y-%m-%d %H:%M} | llenadora: {s['llenadora_estado']:<7} {es(s['llenadora_vel_und_h']):>5} und/h | "
          f"WIP {es(s['wip_tubos']):>5} | PT A/B/C {es(s['pt_A'])}/{es(s['pt_B'])}/{es(s['pt_C'])} | MP {es(s['mp_kg'])} kg")
    vivo.env.run(until=vivo.env.now + 1)
```

Salida:
```text
2026-09-02 13:00 | llenadora: marcha  1.555 und/h | WIP 7.800 | PT A/B/C 9.170/5.225/6.065 | MP 3.100 kg
2026-09-02 14:00 | llenadora: marcha  1.446 und/h | WIP 7.200 | PT A/B/C 9.170/5.813/6.065 | MP 3.100 kg
2026-09-02 15:00 | llenadora: marcha  1.542 und/h | WIP 6.000 | PT A/B/C 9.170/6.987/6.065 | MP 3.100 kg
2026-09-02 16:00 | llenadora: marcha  1.493 und/h | WIP 4.200 | PT A/B/C 9.170/8.743/6.065 | MP 3.100 kg
2026-09-02 17:00 | llenadora: marcha  1.417 und/h | WIP 2.400 | PT A/B/C 9.170/10.495/6.065 | MP 3.100 kg
2026-09-02 18:00 | llenadora: marcha  1.514 und/h | WIP 1.200 | PT A/B/C 9.170/11.663/6.065 | MP 3.100 kg
2026-09-02 19:00 | llenadora: libre       0 und/h | WIP     0 | PT A/B/C 9.170/12.833/6.065 | MP 3.100 kg
2026-09-03 06:00 | llenadora: libre       0 und/h | WIP     0 | PT A/B/C 9.170/12.833/6.065 | MP 3.100 kg
```

<!-- celda 27 · código -->
```python
# Inventario de producto terminado, con el punto de reorden y la capacidad de bodega de cada producto
fig, axs = plt.subplots(3, 1, figsize=(9, 6.4), sharex=True)
for ax, p in zip(axs, PRODS):
    ax.plot(diario.fecha, diario[f"pt_{p}"], color=COLOR[p], linewidth=1.5)
    for valor, texto in ((prod.bodega[p], "Capacidad de bodega"), (prod.rop[p], "Punto de reorden")):
        ax.axhline(valor, color=COLOR["gris"], linewidth=1)
        ax.annotate(texto, (1, valor), xycoords=ax.get_yaxis_transform(), xytext=(5, 0),
                    textcoords="offset points", va="center", fontsize=8, annotation_clip=False)
    ax.set_title(f"Producto {p}: {prod.nombre[p]}", fontsize=10); ax.set_ylim(0, None)
    ax.yaxis.set_major_formatter(lambda v, _: es(v))
axs[1].set_ylabel("Tubos en bodega al cierre del día")
fig.tight_layout(rect=(0, 0, 0.87, 1)); plt.show()
```

Salida:
```text
[gráfico]
```

<!-- celda 28 · código -->
```python
# Una semana de la llenadora vista por sus sensores (se busca una semana con falla, si la hay)
falla = tele.t_h[tele.llenadora_estado == "falla"]
t0 = max(0, int(falla.iloc[0] // base.H) - 2) * base.H if len(falla) else 10 * base.H
semana = tele[(tele.t_h >= t0) & (tele.t_h < t0 + 5 * base.H)].assign(h=lambda x: x.t_h - t0)
color_estado = {"libre": "#e1e0d9", "marcha": COLOR["A"], "alistamiento": "#eda100", "falla": "#d03b3b"}
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 4), sharex=True, height_ratios=[3, 1])
ax1.step(semana.h, semana.llenadora_vel_und_h, where="post", color=COLOR["A"], linewidth=1.5)
ax1.set_ylabel("Velocidad (und/h)"); ax1.yaxis.set_major_formatter(lambda v, _: es(v))
ax1.set_title(f"Llenadora: lecturas horarias de una semana (desde el {semana.momento.iloc[0]:%d/%m/%Y})")
for estado, col in color_estado.items():
    ax2.broken_barh([(t, 1) for t in semana.h[semana.llenadora_estado == estado]], (0, 1), color=col, label=estado.capitalize())
ax2.set_yticks([]); ax2.grid(False); ax2.set_xlabel(f"Horas de turno ({es(base.H)} h = 1 día)")
ax2.legend(ncols=4, loc="upper center", bbox_to_anchor=(0.5, -0.9))
plt.show()
```

Salida:
```text
[gráfico]
```

<!-- celda 29 · markdown -->
### 3.5 Métricas de eficiencia

Takt time, tiempo de ciclo, throughput y WIP medidos en el gemelo (promedio de las réplicas). Los
del Corte 1 están a escala de la zona y con jornada de 8 h, por eso no son comparables en magnitud.

<!-- celda 30 · código -->
```python
rep_base = replicar()
kb = rep_base.mean()
horas_dia = par["turnos"] * par["horas_turno"]
proceso = {p: sum(horas_nominales_lote(e, p) for e in EQUIPOS) for p in PRODS}                 # h por lote, todas las estaciones
fabricacion = {p: sum(horas_nominales_lote(e, p) for e in (E_PES, E_MEZ, E_QC)) for p in PRODS}
display(pd.DataFrame({
    "Corte 1 (zona, 8 h/día)": ["41,5 s/und (0,69 min)", "86,7 und/h", "3,5 a 5,5 h (dato de la empresa)", "304 a 477 und"],
    "Libro (planta)": [f"{es(par['dias_mes']*horas_dia*3600/DEMANDA_PLANTA, 1)} s/und",
                       f"{es(DEMANDA_PLANTA/(par['dias_mes']*horas_dia))} und/h",
                       f"{es(min(proceso.values()), 1)} a {es(max(proceso.values()), 1)} h por lote",
                       f"{es(prod.wip.sum())} tubos"],
    "Gemelo (planta, 12 meses)": [f"{es(kb['takt_s_und'], 1)} s/und", f"{es(kb['throughput_und_h'])} und/h",
                                  f"{es(kb['flujo_lote_h'], 1)} h por lote", f"{es(kb['wip_prom_tubos'])} tubos"]},
    index=["Takt time", "Throughput", "Tiempo de ciclo (flujo)", "WIP promedio"]))
print(f"Pesaje + mezcla + control de calidad según el libro: {es(min(fabricacion.values()), 1)} a {es(max(fabricacion.values()), 1)} h por lote")
```

Salida:
```text
Corte 1 (zona, 8 h/día)  \
Takt time                           41,5 s/und (0,69 min)   
Throughput                                     86,7 und/h   
Tiempo de ciclo (flujo)  3,5 a 5,5 h (dato de la empresa)   
WIP promedio                                304 a 477 und   

                                 Libro (planta) Gemelo (planta, 12 meses)  
Takt time                            11,1 s/und                10,3 s/und  
Throughput                            325 und/h                 352 und/h  
Tiempo de ciclo (flujo)  12,7 a 14,5 h por lote           16,9 h por lote  
WIP promedio                        8.500 tubos               5.308 tubos  
Pesaje + mezcla + control de calidad según el libro: 3,9 a 5,0 h por lote
```

<!-- celda 31 · markdown -->
### 3.6 Restricciones: capacidad, demanda y almacenamiento

<!-- celda 32 · código -->
```python
semiancho = stats.t.ppf(0.975, N_REP - 1) * rep_base.std(ddof=1) / math.sqrt(N_REP)     # intervalo del 95 %
filas = [("Capacidad", "Ocupación de la llenadora (cuello de botella)", "ocup_llenadora_%", "%", 1),
         ("Capacidad", "Ocupación de los reactores", "ocup_mezcla_%", "%", 1),
         ("Capacidad", "Ocupación de la encartonadora", "ocup_encartonadora_%", "%", 1),
         ("Capacidad", "Ocupación del empaque", "ocup_empaque_%", "%", 1),
         ("Demanda", "Nivel de servicio (despacho inmediato)", "nivel_servicio_%", "%", 2),
         ("Demanda", "Mayor acumulado de pedidos pendientes", "pendiente_max_und", "tubos", 0),
         ("Almacenamiento", "Inventario total máximo", "pt_max_und", "tubos", 0),
         ("Almacenamiento", "Días con la bodega total sobre su capacidad", "dias_sobre_bodega_%", "%", 1),
         ("Almacenamiento", "Días con el producto C sobre su bodega", "dias_C_sobre_bodega_%", "%", 1),
         ("Materia prima", "Menor existencia de base y colorantes", "mp_min_kg", "kg", 0)]
display(pd.DataFrame([{"Tipo": tipo, "Indicador": texto, "Promedio": es(kb[col], d), "± (95 %)": es(semiancho[col], d), "Unidad": und}
                      for tipo, texto, col, und, d in filas]))
print(f"Bodega total: {es(prod.bodega.sum())} tubos | bodega de C: {es(prod.bodega['C'])} | punto de reorden + lote de C: {es(prod.rop['C'] + prod.lote['C'])}")
print(f"Réplicas en las que algún lote esperó materia prima: {(rep_base.espera_mp_h > 0).sum()} de {N_REP}")
```

Salida:
```text
Tipo                                      Indicador Promedio  \
0       Capacidad  Ocupación de la llenadora (cuello de botella)     28,9   
1       Capacidad                     Ocupación de los reactores     10,5   
2       Capacidad                  Ocupación de la encartonadora     16,0   
3       Capacidad                          Ocupación del empaque     15,4   
4         Demanda         Nivel de servicio (despacho inmediato)    99,99   
5         Demanda          Mayor acumulado de pedidos pendientes        0   
6  Almacenamiento                        Inventario total máximo   49.226   
7  Almacenamiento    Días con la bodega total sobre su capacidad      0,0   
8  Almacenamiento         Días con el producto C sobre su bodega     32,3   
9   Materia prima          Menor existencia de base y colorantes      800   

  ± (95 %) Unidad  
0      0,4      %  
1      0,1      %  
2      0,2      %  
3      0,2      %  
4     0,02      %  
5        0  tubos  
6      627  tubos  
7      0,0      %  
8      1,1      %  
9      152     kg  
Bodega total: 58.000 tubos | bodega de C: 14.000 | punto de reorden + lote de C: 20.100
Réplicas en las que algún lote esperó materia prima: 3 de 30
```

<!-- celda 33 · markdown -->
### 3.7 Escenarios

Todos se corren con las mismas semillas, así las diferencias se deben a la decisión y no al azar.

<!-- celda 34 · código -->
```python
escenarios = {
    "Base: política del libro": {},
    "Sin estacionalidad (demanda plana)": dict(peso_estacional_real=0, peso_estacional_pron=0),
    "Punto de reorden ajustado con el pronóstico": dict(politica="rop_pronostico"),
    "Compras con pronóstico sin estacionalidad": dict(peso_estacional_pron=0),
    "Lote de C de 7.800 tubos": dict(lote={"C": 7800}),
    "Un solo turno": dict(turnos=1),
}
res = {nombre: (rep_base if not cfg else replicar(cfg)) for nombre, cfg in escenarios.items()}
cols = {"nivel_servicio_%": "Nivel de servicio (%)", "pt_prom_und": "Inventario promedio (tubos)",
        "dias_C_sobre_bodega_%": "Días C sobre su bodega (%)", "ocup_llenadora_%": "Ocupación llenadora (%)",
        "flujo_lote_h": "Flujo por lote (h)"}
comp = pd.DataFrame({nombre: df.mean()[list(cols)] for nombre, df in res.items()}).T.rename(columns=cols)
comp["Réplicas con faltante de materia prima"] = [int((df.espera_mp_h > 0).sum()) for df in res.values()]
tabla(comp, {"Nivel de servicio (%)": 2, "Días C sobre su bodega (%)": 1, "Ocupación llenadora (%)": 1, "Flujo por lote (h)": 1})
```

Salida:
```text
Nivel de servicio (%)  \
Base: política del libro                                    99,99   
Sin estacionalidad (demanda plana)                         100,00   
Punto de reorden ajustado con el pronóstico                 99,97   
Compras con pronóstico sin estacionalidad                   99,85   
Lote de C de 7.800 tubos                                    99,96   
Un solo turno                                               97,97   

                                            Inventario promedio (tubos)  \
Base: política del libro                                         34.697   
Sin estacionalidad (demanda plana)                               34.724   
Punto de reorden ajustado con el pronóstico                      36.740   
Compras con pronóstico sin estacionalidad                        34.627   
Lote de C de 7.800 tubos                                         31.108   
Un solo turno                                                    28.240   

                                            Días C sobre su bodega (%)  \
Base: política del libro                                          32,3   
Sin estacionalidad (demanda plana)                                32,3   
Punto de reorden ajustado con el pronóstico                       36,9   
Compras con pronóstico sin estacionalidad                         32,1   
Lote de C de 7.800 tubos                                           0,0   
Un solo turno                                                     19,9   

                                            Ocupación llenadora (%)  \
Base: política del libro                                       28,9   
Sin estacionalidad (demanda plana)                             29,0   
Punto de reorden ajustado con el pronóstico                    28,7   
Compras con pronóstico sin estacionalidad                      28,9   
Lote de C de 7.800 tubos                                       29,5   
Un solo turno                                                  57,5   

                                            Flujo por lote (h)  \
Base: política del libro                                  16,9   
Sin estacionalidad (demanda plana)                        16,8   
Punto de reorden ajustado con el pronóstico               17,1   
Compras con pronóstico sin estacionalidad                 16,9   
Lote de C de 7.800 tubos                                  16,1   
Un solo turno                                             18,3   

                                            Réplicas con faltante de materia prima  
Base: política del libro                                                         3  
Sin estacionalidad (demanda plana)                                               0  
Punto de reorden ajustado con el pronóstico                                      1  
Compras con pronóstico sin estacionalidad                                        6  
Lote de C de 7.800 tubos                                                         1  
Un solo turno                                                                    1
```

<!-- celda 35 · código -->
```python
factores = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
estres = pd.DataFrame({f: replicar(dict(factor_demanda=f, politica="rop_pronostico", modelar_mp=False)).mean() for f in factores}).T

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3.2))
for ax, col, titulo in ((ax1, "ocup_llenadora_%", "Ocupación de la llenadora (%)"), (ax2, "nivel_servicio_%", "Nivel de servicio (%)")):
    ax.plot(estres.index, estres[col], marker="o", color=COLOR["A"])
    for f, valor in estres[col].items():
        ax.annotate(es(valor, 1), (f, valor), xytext=(0, 7), textcoords="offset points", ha="center", fontsize=8)
    ax.set_title(titulo); ax.set_xlabel("Factor de demanda"); ax.set_ylim(0, 115)
    ax.xaxis.set_major_formatter(lambda v, _: es(v, 1))
fig.tight_layout(); plt.show()
```

Salida:
```text
[gráfico]
```

<!-- celda 36 · markdown -->
## 4. Gemelo digital guiado por el Plan Agregado (S&OP)

Se simula el plan de la hoja `Plan Agregado` (persecución y nivelada) con demanda estocástica, capacidad de llenadora, bodega y costo de inventario. Ambas estrategias comparten la misma semilla, así que enfrentan **la misma demanda real**.

<!-- celda 37 · código -->
```python
import os, unicodedata
from scipy import stats

def _norm(t):
    return unicodedata.normalize("NFKD", str(t)).encode("ascii", "ignore").decode().strip().lower()

def cargar_plan_agregado(ruta=None, hoja="Plan Agregado"):
    """Lee la hoja del plan agregado. Devuelve (df_plan, parametros)."""
    ruta = ruta or ARCHIVO
    if not os.path.exists(ruta) and os.path.exists(ruta.replace(" ", "_")):
        ruta = ruta.replace(" ", "_")
    raw = pd.read_excel(ruta, sheet_name=hoja, header=None)
    col0 = raw[0].map(_norm)

    def parametro(texto):
        return float(raw.loc[col0.str.contains(_norm(texto), regex=False), 1].iloc[0])

    prm = dict(inv_inicial=parametro("Inventario inicial"),
               cap_bodega=parametro("Capacidad de almacenamiento"),
               vel_llenadora=parametro("Capacidad efectiva de la llenadora"),
               horas_dia=parametro("Horas efectivas por dia"),
               costo_hold=parametro("Costo de mantener inventario"))

    i_enc = col0[col0 == "mes"].index[0]                     # fila de encabezados de la tabla mensual
    estrategias = {_norm(n): c for c, n in raw.iloc[i_enc - 1].items() if c > 0 and pd.notna(n)}
    cuerpo = raw.iloc[i_enc + 1: i_enc + 13]
    df = pd.DataFrame({"Mes": cuerpo[0].values,
                       "Días hábiles": cuerpo[1].astype(float).values,
                       "Demanda Plan": cuerpo[3].astype(float).values})
    for nombre in ("persecucion", "nivelada", "mixta"):
        if nombre in estrategias:
            df[f"Prod {nombre}"] = cuerpo[estrategias[nombre]].astype(float).values
    assert len(df) == 12 and df["Mes"].notna().all(), "No se encontraron los 12 meses del plan"
    df.attrs["parametros"] = prm
    return df, prm

df_plan, PRM_SOP = cargar_plan_agregado()
print(f"Inventario inicial: {es(PRM_SOP['inv_inicial'])} | Bodega PT: {es(PRM_SOP['cap_bodega'])} und | "
      f"Llenadora: {es(PRM_SOP['vel_llenadora'], 2)} und/h x {es(PRM_SOP['horas_dia'])} h/día | "
      f"Holding: {es(PRM_SOP['costo_hold'], 2)} COP/und-mes")
tabla(df_plan, 0)
```

<!-- celda 38 · código -->
```python
def simular_gemelo_sop(df_plan, estrategia="Persecucion", variabilidad_demanda=0.05, seed=42):
    """Simula 12 meses del plan agregado con demanda Normal truncada en 0 (SimPy, un paso por mes).
    estrategia: 'Persecucion', 'Nivelada' o 'Mixta'. Parámetros de bodega, llenadora y costo salen de df_plan.attrs."""
    prm = df_plan.attrs["parametros"]
    col_plan = f"Prod {_norm(estrategia)}"
    if col_plan not in df_plan:
        raise ValueError(f"Estrategia '{estrategia}' no está en el plan: {[c[5:] for c in df_plan if c.startswith('Prod ')]}")
    rng = np.random.default_rng(seed)
    env = simpy.Environment()
    estado, filas = {"inv": prm["inv_inicial"]}, []

    def demanda_real(media):
        sigma = variabilidad_demanda * media
        if sigma <= 0:
            return media
        return float(stats.truncnorm.rvs((0 - media) / sigma, np.inf, loc=media, scale=sigma, random_state=rng))

    def proceso_mensual(env):
        for _, r in df_plan.iterrows():
            dem = demanda_real(r["Demanda Plan"])
            cap_max = r["Días hábiles"] * prm["horas_dia"] * prm["vel_llenadora"]       # horas efectivas x tubos/h
            prod_real = min(r[col_plan], cap_max)
            inv_ini = estado["inv"]
            disponible = inv_ini + prod_real
            inv_fin = max(0.0, disponible - dem)
            filas.append({"Mes": r["Mes"], "Demanda Real": dem, "Plan Producción": r[col_plan],
                          "Producción Real": prod_real, "Inv. Inicial": inv_ini, "Inv. Final": inv_fin,
                          "Utilización Llenadora": prod_real / cap_max,
                          "Desabastecimiento": max(0.0, dem - disponible),
                          "Satura Bodega": inv_fin > prm["cap_bodega"],
                          "Costo Inventario (COP)": inv_fin * prm["costo_hold"]})
            estado["inv"] = inv_fin
            yield env.timeout(1)                                                       # 1 paso = 1 mes

    env.process(proceso_mensual(env))
    env.run()
    return pd.DataFrame(filas)
```

<!-- celda 39 · código -->
```python
ESTRATEGIAS_SOP = ["Persecucion", "Nivelada"]
sim_sop = {e: simular_gemelo_sop(df_plan, e, variabilidad_demanda=0.05, seed=42) for e in ESTRATEGIAS_SOP}

for e, s in sim_sop.items():
    print(f"\n{e}")
    display(tabla(s.assign(**{"Utilización Llenadora": s["Utilización Llenadora"] * 100}), {"Utilización Llenadora": 1}))

resumen_sop = pd.DataFrame({e: {"Demanda real anual (und)": s["Demanda Real"].sum(),
                                "Producción real anual (und)": s["Producción Real"].sum(),
                                "Inventario final máximo (und)": s["Inv. Final"].max(),
                                "Meses sobre bodega": int(s["Satura Bodega"].sum()),
                                "Desabastecimiento total (und)": s["Desabastecimiento"].sum(),
                                "Utilización máxima llenadora (%)": 100 * s["Utilización Llenadora"].max(),
                                "Costo inventario anual (COP)": s["Costo Inventario (COP)"].sum()}
                               for e, s in sim_sop.items()})
tabla(resumen_sop, 0)
```

<!-- celda 40 · código -->
```python
fig, ax = plt.subplots(figsize=(9, 4))
estilo = {"Persecucion": (COLOR["A"], "Persecución"), "Nivelada": (COLOR["B"], "Nivelada")}
for e, s in sim_sop.items():
    col, etiqueta = estilo[e]
    ax.plot(s["Mes"], s["Inv. Final"], marker="o", color=col, label=etiqueta)
    sat = s[s["Satura Bodega"]]
    ax.scatter(sat["Mes"], sat["Inv. Final"], s=90, facecolors="none", edgecolors="#d03b3b", linewidths=2, zorder=5)
ax.axhline(PRM_SOP["cap_bodega"], color="#d03b3b", linestyle="--", linewidth=1.3, label=f"Límite de bodega ({es(PRM_SOP['cap_bodega'])} und)")
ax.scatter([], [], s=90, facecolors="none", edgecolors="#d03b3b", linewidths=2, label="Mes que satura la bodega")
ax.set_ylabel("Inventario final de PT (und)"); ax.set_ylim(0, None); ax.tick_params(axis="x", labelrotation=45)
ax.yaxis.set_major_formatter(lambda v, _: es(v))
ax.set_title("Inventario final vs. capacidad de bodega: persecución vs. nivelada")
ax.legend(ncols=2, loc="upper left", bbox_to_anchor=(0, -0.2))
plt.show()
```

<!-- celda 41 · markdown -->
## 5. Comparación con la misma demanda: gemelo normal vs. gemelo guiado por el plan agregado

Se comparan cinco modelos bajo **exactamente la misma demanda mensual** (la que genera el modelo de la sección 4 en cada réplica):

| Modelo | Cómo decide la producción |
|---|---|
| Gemelo normal (punto de reorden) | Sección 3 sin cambios: punto de reorden y lote por producto, revisión diaria (lazo cerrado). |
| Gemelo con plan Persecución | Mismo gemelo detallado, pero libera lotes según la producción mensual del plan (lazo abierto). |
| Gemelo con plan Nivelada | Ídem, con la producción nivelada del plan. |
| S&OP agregado Persecución / Nivelada | Modelo mensual de la sección 4 (sin fallas, alistamientos ni rendimiento); sirve de referencia. |

Supuestos: la demanda mensual se reparte entre A, B y C según la demanda base del libro; los pedidos diarios se generan como en la sección 3 (Poisson y lognormal) y se reescalan para que cada mes sume exactamente la demanda dada; el plan se libera en partes iguales por día hábil, en lotes de 7.800 tubos con arrastre del sobrante, y se divide por el rendimiento de cada producto para que el plan cubra tubos buenos. El calendario es enero a diciembre de 2026, con los festivos de Colombia del gemelo; el plan cuenta algunos días hábiles de más (la celda de resultados muestra la diferencia).

<!-- celda 42 · código -->
```python
INICIO_PLAN = dt.date(2026, 1, 1)      # los 12 meses de la hoja Plan Agregado son enero a diciembre de 2026
COSTO_HOLD, CAP_BODEGA = PRM_SOP["costo_hold"], PRM_SOP["cap_bodega"]


class GemeloThymsSOP(GemeloThyms):
    """Gemelo detallado de la sección 3 con dos cambios, sin tocar la clase original:
    1) la demanda mensual viene dada (misma para todos los modelos que se comparan);
    2) si plan_prod no es None, los lotes se liberan según el plan mensual y no por punto de reorden."""

    def __init__(self, D, PRON, cfg, semilla, demanda_mes, plan_prod=None, compensar_rend=True):
        global INICIO
        previo, INICIO = INICIO, INICIO_PLAN                       # el calendario del gemelo arranca en enero
        try:
            super().__init__(D, PRON, cfg, semilla)
        finally:
            INICIO = previo
        self.plan_prod, self.credito, self._i_dia = plan_prod, dict.fromkeys(PRODS, 0.0), 0
        share = (D["prod"].demanda / D["prod"].demanda.sum()).to_dict()
        rng = np.random.default_rng(semilla + 20_000)              # flujo propio: la demanda no depende de la política

        def pedidos_mes(objetivo, n):
            k = rng.poisson(objetivo / n / self.pedido_medio, n)   # pedidos por día
            tam = rng.lognormal(PRON["mu_pedido"], PRON["sg_pedido"], int(k.sum()))
            dia = np.repeat(np.arange(n), k)
            if len(tam) == 0:                                      # mes sin pedidos: todo en un día al azar
                dia, tam = np.array([rng.integers(n)]), np.array([1.0])
            return np.bincount(dia, weights=tam * objetivo / tam.sum(), minlength=n)   # el mes suma exactamente la demanda dada

        self.pedidos, self.liberar = [], []
        for m, am in enumerate(meses_desde(INICIO_PLAN, MESES)):
            n = len(self.habiles[am])
            ped = {p: pedidos_mes(demanda_mes[m] * share[p], n) for p in PRODS}
            for d in range(n):
                self.pedidos.append({p: ped[p][d] for p in PRODS})
                self.liberar.append({p: 0.0 if plan_prod is None else
                                     plan_prod[m] * share[p] / n / (self.rend[p] if compensar_rend else 1.0) for p in PRODS})

    def _demanda_del_dia(self):
        q = self.pedidos[self._i_dia]; self._i_dia += 1
        for p in PRODS:
            despacho = min(q[p], self.pt[p])
            self.pt[p] -= despacho; self.pendiente[p] += q[p] - despacho
            self.dem_total[p] += q[p]; self.a_tiempo[p] += despacho; self.dem_mes += q[p]

    def _revisar_produccion(self):
        if self.plan_prod is None:                                 # gemelo normal: punto de reorden
            return super()._revisar_produccion()
        lib = self.liberar[self._i_dia - 1]                        # plan: cuota diaria, con arrastre del sobrante
        for p in PRODS:
            self.credito[p] += lib[p]
            while self.credito[p] >= self.n_lote:
                self.credito[p] -= self.n_lote
                self.sec_lote += 1; self.en_proceso[p] += self.n_lote
                self.env.process(self._lote(dict(id=self.sec_lote, p=p)))


KPIS = ["Demanda anual (und)", "Producción anual (und)", "Nivel de servicio (%)", "No atendido de inmediato (und)",
        "Inventario promedio fin de mes (und)", "Inventario máximo fin de mes (und)", "Meses sobre bodega (de 12)",
        "Días sobre bodega (%)", "Costo inventario anual (COP)", "Ocupación llenadora (%)"]

def kpis_gemelo(g):
    d = pd.DataFrame(g.diario)
    d["tot"] = d[[f"pt_{p}" for p in PRODS]].sum(axis=1)
    fin = d.groupby(d.fecha.map(lambda f: (f.year, f.month)), sort=False)["tot"].last().to_numpy()
    dem, atendido = sum(g.dem_total.values()), sum(g.a_tiempo.values())
    return dict(zip(KPIS, [dem, g.cont_bueno, 100 * atendido / dem, dem - atendido, fin.mean(), fin.max(),
                           int((fin > CAP_BODEGA).sum()), 100 * (d.tot > CAP_BODEGA).mean(),
                           fin.sum() * COSTO_HOLD, g.kpis()["ocup_llenadora_%"]])), fin

def kpis_agregado(s):
    dem = s["Demanda Real"].sum()
    fin = s["Inv. Final"].to_numpy()
    return dict(zip(KPIS, [dem, s["Producción Real"].sum(), 100 * (1 - s["Desabastecimiento"].sum() / dem),
                           s["Desabastecimiento"].sum(), fin.mean(), fin.max(), int(s["Satura Bodega"].sum()),
                           np.nan, s["Costo Inventario (COP)"].sum(), 100 * s["Utilización Llenadora"].mean()])), fin
```

<!-- celda 43 · código -->
```python
N_REP_COMP = N_REP
MODELOS = ["Gemelo normal (punto de reorden)", "Gemelo con plan Persecución", "Gemelo con plan Nivelada",
           "S&OP agregado Persecución", "S&OP agregado Nivelada"]
GEMELOS = MODELOS[:3]

def comparar_modelos(df_plan, n_rep=N_REP_COMP, variabilidad_demanda=0.05, semilla=SEMILLA):
    """Misma demanda mensual en los 5 modelos dentro de cada réplica. Devuelve (KPIs por réplica, inventario fin de mes)."""
    filas, inv = [], {m: [] for m in MODELOS}
    for i in range(n_rep):
        s = semilla + i
        agg = {e: simular_gemelo_sop(df_plan, e, variabilidad_demanda, s) for e in ("Persecucion", "Nivelada")}
        dem = agg["Persecucion"]["Demanda Real"].to_numpy()               # idéntica en Persecución y Nivelada
        corridas = {MODELOS[0]: GemeloThymsSOP(D, PRON, {}, s, dem, None),
                    MODELOS[1]: GemeloThymsSOP(D, PRON, {}, s, dem, df_plan["Prod persecucion"].to_numpy()),
                    MODELOS[2]: GemeloThymsSOP(D, PRON, {}, s, dem, df_plan["Prod nivelada"].to_numpy())}
        resultados = {m: kpis_gemelo(g.correr()) for m, g in corridas.items()}
        resultados[MODELOS[3]], resultados[MODELOS[4]] = kpis_agregado(agg["Persecucion"]), kpis_agregado(agg["Nivelada"])
        for m, (k, fin) in resultados.items():
            filas.append({"Modelo": m, "rep": i, **k}); inv[m].append(fin)
    return pd.DataFrame(filas), {m: np.array(v) for m, v in inv.items()}

# El plan y el gemelo no cuentan igual los días hábiles: se avisa la diferencia (el gemelo usa los festivos de Colombia)
dias_gemelo = [len(dias_habiles(a, m)) for a, m in meses_desde(INICIO_PLAN, MESES)]
dif = [(mes[:3], int(p), n) for mes, p, n in zip(df_plan["Mes"], df_plan["Días hábiles"], dias_gemelo) if int(p) != n]
print(f"Días hábiles: plan {int(df_plan['Días hábiles'].sum())} | calendario del gemelo {sum(dias_gemelo)}. "
      f"Meses distintos (mes, plan, gemelo): {dif}\n")

res_comp, inv_comp = comparar_modelos(df_plan)
g_ = res_comp.groupby("Modelo")[KPIS]
media = g_.mean().loc[MODELOS].T
semi = (stats.t.ppf(0.975, N_REP_COMP - 1) * g_.std(ddof=1) / math.sqrt(N_REP_COMP)).loc[MODELOS].T     # intervalo del 95 %

DEC = {"Nivel de servicio (%)": 2, "Meses sobre bodega (de 12)": 1, "Días sobre bodega (%)": 1, "Ocupación llenadora (%)": 1}
fmt = lambda k, m, h: "—" if np.isnan(m) else f"{es(m, DEC.get(k, 0))} ± {es(h, DEC.get(k, 0))}"
print(f"Promedio de {N_REP_COMP} réplicas ± intervalo del 95 %, con la misma demanda en los 5 modelos\n")
display(pd.DataFrame({m: [fmt(k, media.loc[k, m], semi.loc[k, m]) for k in KPIS] for m in MODELOS}, index=KPIS))

# Mejor modelo por KPI entre los tres gemelos detallados (el agregado no tiene fallas ni alistamientos: es solo referencia)
SENTIDO = {"Nivel de servicio (%)": 1, "No atendido de inmediato (und)": -1, "Inventario promedio fin de mes (und)": -1,
           "Inventario máximo fin de mes (und)": -1, "Meses sobre bodega (de 12)": -1, "Días sobre bodega (%)": -1,
           "Costo inventario anual (COP)": -1}
filas = []
for k, sg in SENTIDO.items():
    orden = sorted(GEMELOS, key=lambda m: -sg * media.loc[k, m])
    a, b = orden[0], orden[1]
    brecha = abs(media.loc[k, a] - media.loc[k, b])
    filas.append({"KPI": k, "Mejor modelo": a if brecha > 0 else "Empate", "Ventaja sobre el segundo": es(brecha, DEC.get(k, 0)),
                  "¿Diferencia significativa?": "Sí" if brecha > semi.loc[k, a] + semi.loc[k, b] else "No"})
display(pd.DataFrame(filas).set_index("KPI"))
```

<!-- celda 44 · código -->
```python
mes_lbl = [m[:3] for m in df_plan["Mes"]]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4), gridspec_kw={"width_ratios": [1.6, 1]})
estilo = {MODELOS[0]: (COLOR["gris"], "-"), MODELOS[1]: (COLOR["A"], "-"), MODELOS[2]: (COLOR["B"], "-"),
          MODELOS[3]: (COLOR["A"], ":"), MODELOS[4]: (COLOR["B"], ":")}
for m, (col, ls) in estilo.items():
    ax1.plot(mes_lbl, inv_comp[m].mean(axis=0), color=col, linestyle=ls, marker="o" if ls == "-" else None,
             linewidth=2 if ls == "-" else 1.5, label=m)
ax1.axhline(CAP_BODEGA, color="#d03b3b", linestyle="--", linewidth=1.3, label=f"Límite de bodega ({es(CAP_BODEGA)} und)")
ax1.set_ylim(0, None); ax1.set_ylabel("Inventario total fin de mes (und)")
ax1.yaxis.set_major_formatter(lambda v, _: es(v)); ax1.set_title("Inventario fin de mes (promedio de réplicas)")
ax1.legend(fontsize=7, loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=2)

k = "Costo inventario anual (COP)"
ax2.bar(range(3), [media.loc[k, m] / 1e6 for m in GEMELOS], yerr=[semi.loc[k, m] / 1e6 for m in GEMELOS],
        color=[COLOR["gris"], COLOR["A"], COLOR["B"]], capsize=4)
for i, m in enumerate(GEMELOS):
    ax2.annotate(f"Servicio {es(media.loc['Nivel de servicio (%)', m], 1)} %", (i, media.loc[k, m] / 1e6 / 2), ha="center", fontsize=8, color="white")
ax2.set_xticks(range(3), ["Normal\n(reorden)", "Plan\nPersecución", "Plan\nNivelada"])
ax2.set_ylabel("Millones de COP por año"); ax2.set_title("Costo anual y servicio")
fig.tight_layout(); plt.show()
```



---

<!-- fuente: corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/THYMS-presentacion-corte-2.md -->
# THYMS-presentacion-corte-2

> **Archivo:** [`THYMS-presentacion-corte-2.pdf`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/THYMS-presentacion-corte-2.pdf) · **Corte 2** · 9 páginas  
> **Nombre original:** `CORTE 2/THYMS Presentacion Corte 2.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** presentación del grupo con el entregable del Corte 2 sobre THYMS Colombia S.A.S. (6 de octubre de 2026): S&OP apoyado en un gemelo digital de la planta de tintes.

**Ideas clave:**
- **La capacidad no es el problema:** la llenadora (cuello de botella) trabaja al 29 % y la demanda podría crecer 3,37 veces (según el libro) antes de saturarla. Las restricciones reales son:
  - la bodega de producto terminado;
  - la bahía del producto C (punto de reorden + lote = 20.100 frente a 14.000);
  - la materia prima importada (13 días de cobertura frente a 55 requeridos).
- **El pronóstico del Corte 1 estaba sesgado;** corregido, el sesgo baja de 29.600 a 1.600 tubos/mes y el RMSE un 17 %.
- **Gemelo digital en SimPy:**
  - 6 estaciones;
  - demanda de facturas reales, fallas, alistamientos y OEE;
  - 16 sensores virtuales;
  - validado con balance de masa, ley de Little y horas de equipo (±0,7 %).
- **Escenarios:** bajar el lote de C a 7.800 elimina los días sobre la bahía; con un solo turno el servicio cae al 97,97 %; el servicio se mantiene ≥ 99,4 % hasta 2 veces la demanda.
- **Optimización** (Bowman = flujo en red, MILP de turnos): la persecución es óptima. Pero ejecutada a lazo abierto en el gemelo da 79,4 % de servicio frente al 99,99 % del modelo agregado; el plan debe fijar volúmenes y el punto de reorden liberar los lotes.

**Fórmulas y métodos** (los detalles están en los cuadernos):
- Suavización exponencial simple $F_{t+1} = \alpha y_t + (1-\alpha)F_t$, con $\alpha$ = 0,05 y nivel inicial = promedio de 3 meses ($y_t$ = venta del mes $t$, $F_t$ = pronóstico).
- Sesgo $\bar{e}$, señal de rastreo $\sum e_t / MAD$ y RMSE.
- Índices estacionales $s_m = y_m/\bar{y}$ con intervalo del 80 %.
- Ley de Little $WIP = TH \times$ tiempo de flujo; takt time = tiempo disponible / demanda.
- Modelo de transporte de Bowman y modelo de flujo en red para el plan agregado; MILP para los turnos.
- Simulación de eventos discretos con 30 réplicas, números aleatorios comunes e intervalo del 95 %.

**Resultados presentados:**

| Resultado | Valor | Página |
|---|---|---|
| Ocupación de la llenadora | 29 % (28,9 %) | 2, 5 |
| Factor de demanda antes de saturar | 3,37× | 2 |
| Tiempo de flujo por lote / takt / throughput / WIP | 16,9 h / 11,1 s/tubo / 352 frente a 325 tubos/h / 5.308 | 2 |
| Cobertura de materia prima | 13 frente a 55 días | 2 |
| Sesgo del pronóstico | 44,6 M → 2,4 M COP (29.600 → 1.600 tubos/mes) | 3, 7 |
| Señal de rastreo | 3,42 → 0,22 | 3 |
| RMSE | 76,8 M → 63,6 M COP (50.800 → 42.100 tubos/mes) | 3 |
| Prueba de estrés | ≥ 99,4 % hasta 2,0×; 93,9 % con 2,5×; 70,8 % con 3,0× | 5 |
| Lote de C de 7.800 | días sobre la bahía 32,3 % → 0 %; inventario −10,3 % | 5, 7 |
| Persecución frente a nivelado | inventario promedio 45.100 → 29.500 (−35 %); meses sobre la bodega 5 → 0 | 6, 7 |
| Servicio del plan a lazo abierto | 79,42 % (persecución) y 84,99 % (nivelado), frente a 99,99 % con punto de reorden | 6 |
| Un turno en enero, abril y agosto | −8.300 horas-hombre/año; −114,5 M COP/año | 6, 7 |
| Compras estacionales (+11.665 kg) | espera de materia prima 44,8 h → 9,3 h | 7 |
| Programa maestro | 156 lotes/año (−0,36 % frente al plan); alistamientos = 27,9 % del tiempo de la llenadora | 7 |

**Páginas clave:**
- p. 2: estudio preliminar;
- p. 3: pronóstico;
- p. 4: diseño y validación del gemelo;
- p. 5: escenarios;
- p. 6: optimización y comparación plan frente a gemelo (gráficos);
- p. 7: tabla de mejoras;
- p. 8: conclusiones.

**Relación con otros archivos del repo:**
- Estudio preliminar y plan agregado: [`Datos Thyms Completo.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Datos%20Thyms%20Completo.md).
- Pronóstico, gemelo, escenarios y estrés: [`Gemelo_Digital_Thyms.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md).
- Gemelo guiado por el plan (79,42 %, 84,99 %, 99,99 %): [`Gemelo_Digital_Thyms_MEJORADO.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms_MEJORADO.md).
- Resumen completo del trabajo: [`CONTEXTO_GEMELO_THYMS.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/CONTEXTO_GEMELO_THYMS.md).
- Pronóstico del Corte 1 que se corrige: [proyecto-thyms-pronostico](/corte-1-pronosticos/proyecto-thyms-pronostico/).
- Teoría del modelo de Bowman y del flujo en red: [01-planeacion-agregada-modelo-bowman](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/).
- Siguiente paso propuesto (Wagner–Whitin / Silver–Meal): [03-wagner-whitin-y-silver-meal](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/).

**Advertencias:**
- Los resultados de **Bowman, flujo en red, MILP de turnos y programa maestro** (página 6 y parte de la 7) **no están en los archivos de esta carpeta**: no hay un libro ni un cuaderno de THYMS con esos modelos. Los archivos de [01-planeacion-agregada-modelo-bowman](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/) son ejemplos de clase con otros datos.
- Tampoco salen de estos archivos:
  - el «26 % de uso de mano de obra en el mes pico» (p. 2);
  - las horas de espera de materia prima 44,8 h → 9,3 h y el «×5» (pp. 5 y 7): el cuaderno solo reporta réplicas con faltante, 3 frente a 6;
  - los −114,5 M COP de mano de obra.
- Los «61 g/tubo» (p. 2) equivalen a 6.106 kg de materia prima por 100.000 tubos (hoja `Restricciones`).
- La página 7 no explica qué significa «(sin cambio)»; podría referirse a que el servicio no cambia [interpretación no confirmada]. «(por validar)» se entiende porque el plan + punto de reorden todavía no se había simulado: es el «siguiente paso» de la página 8.

## Contenido completo (página por página)

### Página 1 — S&OP con Gemelo Digital (portada)

> [Imagen decorativa: fondo negro con una foto de cabello castaño ondulado, de espaldas.]
> [Imagen decorativa: logo dorado «THYM'S ACADEMIC» arriba al centro.]

- **S&OP con Gemelo Digital**
- **Thyms Colombia S.A.S**
- Proyecto C2 · Planeación, Programación y Control de la Producción · Universidad de La Sabana
- Prof. William J. Guerrero · 6 de octubre de 2026

### Página 2 — 1. Estudio preliminar: la capacidad no es el problema

> [Imagen decorativa: logo «THYM'S ACADEMIC» arriba a la izquierda; aparece igual en las páginas 2 a 8.]

Cuatro indicadores destacados en círculos:

| Valor | Indicador |
|---|---|
| 29% | Ocupación de la llenadora |
| 3,37× | Demanda antes de saturar la llenadora |
| 16,9 h | Tiempo de flujo por lote (gemelo) |
| 13 vs 55 | Cobertura de materia prima (días) |

- Takt 11,1 s/tubo · throughput 352 vs 325 tubos/h requeridos · WIP 5.308 (Ley de Little verificada)
- Restricciones críticas: almacenamiento de PT (plan nivelado = 1,66× la bodega), bahía del producto C (20.100 vs 14.000), materia prima importada
- Agregación en tres unidades: tubos · kg (61 g/tubo) · horas-hombre (26% de uso de mano de obra en el mes pico)

### Página 3 — 2. Pronóstico: mejor que el Corte 1

> [Gráfico: líneas; eje Y «Tubos / mes» de 0 a 200k; eje X de ene-26 a ago-27.
> - «Ventas reales (escala planta)» (gris), de ene-26 a ago-26: ≈ 63k, 102k, 133k, 35k, 131k, 104k, 153k, 79k.
> - «Pronóstico SES estacional» (marrón), de sep-26 a ago-27: ≈ 100k en sep, oct, nov y dic, luego 63k, 102k, 133k, 35k, 131k, 104k, 153k, 79k.
> - «Intervalo de predicción 80%» (banda rosada): de ≈ 46k a 154k en sep–dic, hasta ≈ 235k en jul-27.
> - «Nivel SES (100.038 tubos/mes)» (línea discontinua horizontal en ≈ 100k).]

- Sesgo del Corte 1: 44,6M → 2,4 M COP
  - 29.600 → 1.600 tubos/mes
- Señal de rastreo: 3,42 → 0,22
- RMSE −17% (63,6M vs 76,8M)
  - 50.800 → 42.100 tubos/mes
- El pronóstico se actualiza dentro del gemelo cada mes
- El MAPE del Corte 1 es menor solo porque premia pronósticos bajos: para planear importa más el sesgo
- Índices estacionales (julio 1,53; abril 0,35) + intervalo del 80%

### Página 4 — 3. Gemelo digital: diseño y validación

Lista numerada:
1. Modelo de eventos discretos en SimPy · 6 estaciones · parámetros leídos del libro de 14 hojas
2. Demanda estocástica (facturas reales), fallas (MTBF/MTTR), alistamientos dependientes de la secuencia, OEE, plazo de la materia prima, festivos colombianos
3. 16 sensores virtuales por hora · consultas en vivo paso a paso (gancho para tablero)
4. Validación: balance de masa exacto · Ley de Little · horas de equipo dentro de ±0,7%
5. 30 réplicas, números aleatorios comunes, IC del 95%

### Página 5 — 4. Escenarios what-if: cuellos de botella

Lista numerada:
1. Llenadora 28,9% vs reactores 10,5%, encartonadora 16,0%, empaque 15,4%
2. Prueba de estrés: servicio ≥ 99,4% hasta 2,0× la demanda; 93,9% con 2,5×; 70,8% con 3,0×
3. Lote de C 15.600 → 7.800: días sobre la bahía 32,3% → 0%, inventario −10,3%
4. Compras sin estacionalidad: espera de materia prima ×5, servicio 99,85%
5. Un solo turno: servicio 97,97%, llenadora 57,5%

### Página 6 — 5. Optimización: Bowman, flujo y MILP

- Mismo problema de dos formas: transporte de Bowman = flujo en red → persecución, con inventario promedio de 29.500 tubos (nivelado: 45.100)
- Recursos en orden: inventario → horas extra → maquila → ventas perdidas (≥ 3,4× la demanda)
- Turnos con MILP: un turno basta en meses bajos (ene, abr, ago): −8.300 horas-hombre/año

> [Gráfico (a): «Inventario de PT a fin de mes, promedio de 30 réplicas»; eje Y «Inventario PT (tubos)» de 0 a 80k+; eje X de Ene a Dic. Valores aproximados leídos del gráfico:
>
> | Serie | Ene | Feb | Mar | Abr | May | Jun | Jul | Ago | Sep | Oct | Nov | Dic |
> |---|---|---|---|---|---|---|---|---|---|---|---|---|
> | Gemelo – punto de reorden (actual) | 32k | 38k | 36k | 35k | 36k | 35k | 36k | 38k | 32k | 36k | 33k | 36k |
> | Gemelo – plan de persecución | 12k | 15,5k | 13k | 16,5k | 14k | 17k | 16,5k | 9,5k | 15k | 16k | 15,5k | 14k |
> | Gemelo – plan nivelado | 50k | 46k | 13k | 78k | 52k | 48k | 1k | 9,5k | 15k | 16k | 15k | 14k |
> | Agregado – persecución (punteado) | 29k | 27,5k | 28k | 28k | 25,5k | 25k | 24k | 25k | 25k | 26k | 26k | 25,5k |
> | Agregado – nivelado (punteado) | 66k | 62k | 29k | 95k | 61k | 57k | 7k | 27,5k | 27,5k | 29k | 29k | 28k |
>
> Línea roja discontinua: «Capacidad de bodega (58k)». El gemelo nivelado y el agregado nivelado pasan la bodega en abril (y el agregado también en enero y febrero).]

> [Gráfico (b): barras «Inventario promedio y servicio», eje Y «Inventario promedio de fin de mes (tubos)» de 0 a 40.000, con barras de error:
> - Punto de reorden ≈ 35.300 (NS 99,99%);
> - Plan de persecución ≈ 14.600 (NS 79,42%), con barra de error de ≈ 11.800 a 17.400;
> - Plan nivelado ≈ 29.900 (NS 84,99%), con barra de error de ≈ 27.300 a 32.400.]

Recuadro inferior: **Mismo plan: 99,99% de servicio en el modelo agregado, 79,4% ejecutado a lazo abierto en el gemelo**

### Página 7 — 6. Mejoras e impacto en los KPI

| Mejora | KPI | Antes → Después |
|---|---|---|
| Corrección del pronóstico | Sesgo (tubos/mes) | 29.600 → 1.600 |
| Persecución en lugar de nivelado | Inventario promedio (tubos) / meses sobre bodega | 45.100 → 29.500 (−35 %) / 5 → 0 |
| Lote de C 15.600 → 7.800 | Días de C sobre la bahía · Inventario PT | 32,3 % → 0 % · −10,3 % *(sin cambio)* |
| Compras estacionales + 11.665 kg | Espera de materia prima | 44,8 h → 9,3 h *(sin cambio)* |
| El plan fija volúmenes, el ROP libera | Servicio | 79,4 % → 99,99 % (por validar) |
| Un turno en ene/abr/ago | Costo de mano de obra | −114,5 M COP/año (≈ −8.300 h-h) |

Nota al pie: *Programa maestro: 156 lotes/año, −0,36% vs plan · alistamientos = 27,9% del tiempo de la llenadora*

### Página 8 — 7. Conclusiones

- La capacidad es abundante: el foco está en almacenamiento, cobertura de materia prima y reglas de ejecución
- Persecución es óptima (Bowman = flujo), pero debe ejecutarse a lazo cerrado para mantener el servicio ≈ 100%
- Limitaciones: una zona de ventas, 8 meses de datos y algunos supuestos de costos
- Siguiente paso: simular plan + punto de reorden juntos; Wagner–Whitin / Silver–Meal sobre el programa maestro

### Página 9 — ¡Gracias!

«¡Gracias!» sobre fondo negro, con el logo «THYM'S ACADEMIC» (imagen decorativa).
