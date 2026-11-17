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

No hay enunciado escrito en la carpeta. Según [`CONTEXTO_GEMELO_THYMS.md`](./CONTEXTO_GEMELO_THYMS.md) y la presentación, el entregable pedía:
1. un **estudio preliminar** del sistema: WIP, takt time, throughput, cycle time y restricciones de capacidad, demanda y almacenamiento;
2. un **gemelo digital en ARENA o Python** que incluya el pronóstico, la estacionalidad y sensores virtuales;
3. la presentación del plan de ventas y operaciones (S&OP).

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [`CONTEXTO_GEMELO_THYMS.md`](./CONTEXTO_GEMELO_THYMS.md) | Documento de traspaso escrito antes de esta conversión (estado al 2026-10-05): proyecto, archivos, mapa de celdas del libro, clases del gemelo, resultados, advertencias y supuestos abiertos. Ya era Markdown; no tiene binario | Sí (1.º) |
| [`THYMS-presentacion-corte-2.md`](./THYMS-presentacion-corte-2.md) | Presentación del grupo (PDF de 9 páginas, 6 de octubre de 2026): resultados y mejoras en una vista | Sí (2.º) |
| [`Datos Thyms Completo.md`](./Datos%20Thyms%20Completo.md) | Libro de 14 hojas: parámetros, productos, tiempos, utilización, alistamientos, fallas, mano de obra, métricas, plan agregado, restricciones, proceso, facturas, clientes y ventas | Sí (3.º) |
| [`Gemelo_Digital_Thyms.md`](./Gemelo_Digital_Thyms.md) | Cuaderno base (36 celdas, con salidas): revisión del pronóstico, pronóstico a 12 meses, gemelo en SimPy, validación, métricas, restricciones, escenarios y estrés | Sí (4.º) |
| [`Gemelo_Digital_Thyms_MEJORADO.md`](./Gemelo_Digital_Thyms_MEJORADO.md) | Cuaderno principal (45 celdas): el base sin cambios + sección 4 (S&OP agregado mensual) + sección 5 (gemelo guiado por el plan frente al de punto de reorden). Las celdas nuevas no tienen salidas guardadas | Sí (5.º) |

**Base frente a MEJORADO:**
- Las celdas 0–35 son idénticas en código y salidas (comprobado comparando los dos `.ipynb`).
- MEJORADO agrega las celdas 36–44:
  - `cargar_plan_agregado()` lee la hoja `Plan Agregado`;
  - `simular_gemelo_sop()` simula mes a mes las estrategias de persecución y nivelada con demanda aleatoria y venta perdida;
  - la clase `GemeloThymsSOP` hereda del gemelo y libera lotes según el plan mensual (lazo abierto) con una demanda dada;
  - `comparar_modelos()` corre 5 modelos con la misma demanda en 30 réplicas.

## Orden de estudio sugerido

1. [`CONTEXTO_GEMELO_THYMS.md`](./CONTEXTO_GEMELO_THYMS.md): el mapa completo.
2. [`THYMS-presentacion-corte-2.md`](./THYMS-presentacion-corte-2.md): las conclusiones que se presentaron.
3. [`Datos Thyms Completo.md`](./Datos%20Thyms%20Completo.md): los datos y el plan agregado en Excel.
4. [`Gemelo_Digital_Thyms.md`](./Gemelo_Digital_Thyms.md): pronóstico y gemelo (secciones 1 a 3).
5. [`Gemelo_Digital_Thyms_MEJORADO.md`](./Gemelo_Digital_Thyms_MEJORADO.md): secciones 4 y 5.

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
- **Planeación agregada** (Excel, clases [L10](../01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md) y [L11](../02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md)):
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

- **Ley de Little:** $WIP = TH \times CT$, donde $TH$ es el throughput y $CT$ el tiempo de flujo. Se usa para validar el gemelo. Detalle en [`Gemelo_Digital_Thyms.md`](./Gemelo_Digital_Thyms.md).
- **Takt time:** $T_{takt} = T_{disponible}/D$. Ver la hoja `Métricas` en [`Datos Thyms Completo.md`](./Datos%20Thyms%20Completo.md#hoja-métricas).
- **Capacidad efectiva con mezcla:** $\bar{c} = OEE \cdot \left(\sum_p w_p/c_p\right)^{-1}$ = 1.675,47 tubos/h, donde $w_p$ es la participación del producto y $c_p$ su capacidad de llenado.
- **Estrategias de plan agregado:** persecución, nivelada y mixta, con inventario $I_t = I_{t-1}+P_t-D_t$. Ver [`Datos Thyms Completo.md`](./Datos%20Thyms%20Completo.md#hoja-plan-agregado).
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

Pendientes de confirmar con la empresa (ver también la sección 9 de [`CONTEXTO_GEMELO_THYMS.md`](./CONTEXTO_GEMELO_THYMS.md)):
- **Escala zona → planta:** los índices estacionales y el nivel salen de un solo vendedor (11,7 % de la planta).
- **Jornada:** 1 turno de 8 h de lunes a sábado en el Corte 1, frente a 2 turnos de 7 h de lunes a viernes en el libro (el gemelo usa el libro).
- **Índices de septiembre a diciembre = 1** (no hay datos).
- **Materia prima en tránsito al inicio:** el stock cubre ~13 días frente a 40 de lead time; el gemelo supone pedidos ya en camino.
- **Supuestos propios del gemelo:** choque mensual del 10 %, CV de reparación de 0,5, sublotes de 600, revisión de compras cada 5 días; OEE de pesaje, control de calidad y empaque supuestos.
- **No modelado:** mano de obra, tubos vacíos y cartón, capacidad de bodega impuesta, reprocesos y estrategia mixta en simulación.
- Las secciones 4 y 5 leen valores calculados del Excel (rompen la regla de «solo datos de entrada») y no tienen salidas guardadas.
- Los resultados de Bowman, flujo en red, MILP de turnos y programa maestro que muestra la presentación (páginas 6–7) no están en ningún archivo de esta carpeta.

## Cómo se conecta con el Corte 1

| Corte 1 ([proyecto-thyms-pronostico](../../corte-1-pronosticos/proyecto-thyms-pronostico/)) | Corte 2 (esta carpeta) |
|---|---|
| `VENTAS.xls`: ventas mensuales de 2026 y 464 facturas | Copiadas en las hojas `Ventas` y `Facturas Mayo-Julio`; dan los índices estacionales y la distribución del tamaño de pedido |
| SES α = 0,05 con $F_1$ = enero: MAD 80,2 M, MAPE 53,4 %, agosto 114,7 M | Sección 2.1: se reproduce y se muestra el sesgo (+63,1 M, señal de rastreo 4,72); la sección 2.2 lo corrige con nivel inicial = promedio de 3 meses |
| 12.900 COP/tubo | Se mantiene (`PRECIO_UND`) para pasar de COP a tubos y escalar a la planta (×8,54) |
| Takt 0,69 min (41,5 s), throughput 86,7 tubos/h, WIP 304–477 (zona, 8 h/día) | Sección 3.5: comparados con el libro (11,1 s; 325; 8.500) y el gemelo (10,3 s; 352; 5.308) |
| Tiempo de ciclo de 3,5–5,5 h (dato de la empresa) | Coherente con pesaje + mezcla + control de calidad = 3,9–5,0 h por lote |
| Días hábiles con festivos (cuaderno de Colab) | Calendario de festivos de Colombia programado (`festivos_colombia()`) |

## Relación con otros temas y proyectos

- Planeación agregada y modelo de Bowman (la presentación dice haberlo aplicado a THYMS): [01-planeacion-agregada-modelo-bowman](../01-planeacion-agregada-modelo-bowman/).
- Agregación y desagregación (tubos, kg, horas-hombre; plan por producto): [02-agregacion-y-desagregacion](../02-agregacion-y-desagregacion/).
- Siguiente paso propuesto (dimensionar lotes del programa maestro): [03-wagner-whitin-y-silver-meal](../03-wagner-whitin-y-silver-meal/).
- Materia prima con lead time y MRP: [04-bom-y-mrp](../04-bom-y-mrp/) y [05-mrp-ii-y-capacidad](../05-mrp-ii-y-capacidad/).
- Pronósticos (SES, señal de rastreo, estacionalidad): [04-datos-estacionarios-promedio-movil-y-suavizacion-simple](../../corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/) y [06-estacionalidad-winters-y-tracking-signal](../../corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/).
- Métricas de desempeño (takt, throughput, WIP, Little): [L02](../../corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L02-introduction-to-production-systems.md).
