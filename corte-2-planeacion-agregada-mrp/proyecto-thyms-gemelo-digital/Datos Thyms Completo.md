# Datos Thyms Completo

> **Archivo:** [`Datos Thyms Completo.xlsx`](./Datos%20Thyms%20Completo.xlsx) · **Corte 2** · Libro de Excel con 14 hoja(s): `Parámetros`, `Productos`, `Tiempos`, `Utilizacion`, `Alistamiento`, `Fallas`, `Mano de Obra`, `Métricas`, `Plan Agregado`, `Restricciones`, `Proceso Planeación Agregada`, `Facturas Mayo-Julio`, `Clientes`, `Ventas`  
> **Nombre original:** `CORTE 2/Datos Thyms Completo.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Libro de datos del **proyecto del Corte 2** sobre THYMS Colombia S.A.S. (tintes en tubo de 60 g, productos A, B y C). Reúne en 14 hojas los parámetros de la planta (turnos, productos, tiempos, OEE, alistamientos, fallas, mano de obra), el **estudio preliminar** del sistema (utilización, takt time, cycle time, throughput, WIP y ley de Little), la **planeación agregada** de 12 meses (persecución, nivelada y mixta, con su desagregación por producto), las restricciones de capacidad, demanda y almacenamiento, y los datos reales de ventas del Corte 1.

Es la **única fuente de datos** de los cuadernos [`Gemelo_Digital_Thyms.md`](./Gemelo_Digital_Thyms.md) y [`Gemelo_Digital_Thyms_MEJORADO.md`](./Gemelo_Digital_Thyms_MEJORADO.md); el mapa de las celdas que leen está en [`CONTEXTO_GEMELO_THYMS.md`](./CONTEXTO_GEMELO_THYMS.md). Aplica las clases [L02](../../corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L02-introduction-to-production-systems.md) (métricas de desempeño), [L10](../01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md) (planeación agregada) y [L11](../02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md) (agregación y desagregación).

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

464 facturas reales de mayo a julio de 2026 (filas 5 a 468), con columnas mes, factura, código de cliente, cliente (anonimizado) y ventas en COP. Las ventas son el `subdoc` de [`VENTAS.xls`](../../corte-1-pronosticos/proyecto-thyms-pronostico/VENTAS.md). Todas las filas en [`Datos Thyms Completo-datos/Facturas_Mayo-Julio.csv`](./Datos%20Thyms%20Completo-datos/Facturas_Mayo-Julio.csv). Los cuadernos solo leen la columna E, para ajustar la distribución del tamaño de pedido.

### Hoja `Clientes`

Concentración de ventas por cliente; cada fila suma con `SUMIF` las facturas del cliente. Todas las filas en [`Datos Thyms Completo-datos/Clientes.csv`](./Datos%20Thyms%20Completo-datos/Clientes.csv).
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

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `Parámetros` — 14 filas × 3 columnas

| Fila | A | B | C |
|---|---|---|---|
| 1 | THYMS Colombia S.A.S. - Parámetros generales |  |  |
| 3 | Parámetro | Valor | Unidad / nota |
| 4 | Días hábiles por mes | 22 | días |
| 5 | Turnos por día | 2 | turnos (6:00-14:00 y 14:00-22:00, L-V) |
| 6 | Horas efectivas por turno | 7 | h (8 h menos descansos) |
| 7 | Horas disponibles por mes | 308 | h por recurso |
| 8 | Factor de demanda (escenarios) | 1 | 1 = demanda base; subir para estresar el sistema |
| 9 | Tubos por lote de 500 kg | 7800 | und (rendimiento aprox. con mermas) |
| 10 | Unidades por caja master | 24 | und |
| 11 | Tasa anual de costo de mantener inventario | 0.22 | sobre costo unitario |
| 12 | Cambios de tono por mes | 26 | ≈ 6 por semana |
| 13 | Alistamiento promedio en llenadora | 0.75 | h por cambio (supuesto: mezcla de cambios de tono y de fórmula) |
| 14 | Contenido de producto por tubo | 60 | g de base y colorantes por tubo (para consumo de materia prima) |

**Fórmulas (1 patrones distintos):**

- `B7`: `=B4*B5*B6`

### Hoja `Productos` — 16 filas × 15 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Productos e inventario |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2 | Tubo de 60 g de tinte permanente. Demanda de escenario = base x factor (hoja Parametros). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 | Producto | Código | Demanda base (und/mes) | Demanda escenario (und/mes) | Yield de calidad | Costo unitario (COP) | Holding (COP/und-mes) | Costo por alistamiento (COP) | Stock PT (und) | Cobertura PT (días) | Capacidad máx. PT (und) | Punto de reorden (und) | Lote de producción (und) | WIP (tubos) | Materia prima (kg) |
| 5 | A. Kolorezza permanente 60 g | THY-KZ060 | 48000 | 48000 | 0.985 | 4300 | 78.8333 | 320000 | 14000 | 6.41667 | 26000 | 8000 | 15600 | 4000 | 1600 |
| 6 | B. Visalia sin amoníaco 60 g | THY-VS060 | 30000 | 30000 | 0.975 | 5600 | 102.667 | 520000 | 8500 | 6.23333 | 18000 | 5500 | 7800 | 2500 | 1100 |
| 7 | C. Thym's Coloring permanente 60 g | THY-TC060 | 22000 | 22000 | 0.988 | 3700 | 67.8333 | 300000 | 7000 | 7 | 14000 | 4500 | 15600 | 2000 | 900 |
| 8 | Total |  | 100000 | 100000 |  |  |  |  | 29500 |  | 58000 | 18000 | 39000 | 8500 | 3600 |
| 10 | Materias primas y materiales |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 11 | Ítem | Origen | Stock actual | Unidad | Lead time (días) | Política |  |  |  |  |  |  |  |  |  |
| 12 | Base y colorantes | Importado | 3600 | kg | 40 | Stock de seguridad de 3 semanas (lead time de 40 días) |  |  |  |  |  |  |  |  |  |
| 13 | Tubos vacíos | Nacional | 60000 | und | 12 | ≈ 10 días de producción |  |  |  |  |  |  |  |  |  |
| 14 | Tapas, cartones e instructivos | Nacional |  | und | 12 | Sin dato de stock |  |  |  |  |  |  |  |  |  |

**Fórmulas (12 patrones distintos):**

- `D5`: `=C5*Parámetros!$B$8`
- `G5`: `=F5*Parámetros!$B$11/12`
- `J5`: `=I5/(D5/Parámetros!$B$4)`
- `C8`: `=SUM(C5:C7)`
- `D8`: `=SUM(D5:D7)`
- `I8`: `=SUM(I5:I7)`
- `K8`: `=SUM(K5:K7)`
- `L8`: `=SUM(L5:L7)`
- `M8`: `=SUM(M5:M7)`
- `N8`: `=SUM(N5:N7)`
- `O8`: `=SUM(O5:O7)`
- `C12`: `=O8`

### Hoja `Tiempos` — 24 filas × 10 columnas

| Fila | A | B | C | D | E | F | G | H | I | J |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Tiempos de procesamiento y capacidad nominal |  |  |  |  |  |  |  |  |  |
| 2 | Distribución normal |  |  |  |  |  |  |  |  |  |
| 4 | Estación | Producto | Unidad | Promedio | Desv. est. | Mínimo | Máximo | Recursos | Rango ±% | Capacidad nominal (und/h) |
| 5 | Pesaje | A | min/lote | 40 | 4 | 36 | 44 | 1 | 0.1 | 11700 |
| 6 | Pesaje | B | min/lote | 45 | 4 | 40.5 | 49.5 | 1 | 0.1 | 10400 |
| 7 | Pesaje | C | min/lote | 40 | 4 | 36 | 44 | 1 | 0.1 | 11700 |
| 8 | Mezcla y emulsión | A | min/lote | 150 | 12 | 120 | 180 | 2 | 0.2 | 6240 |
| 9 | Mezcla y emulsión | B | min/lote | 180 | 12 | 144 | 216 | 2 | 0.2 | 5200 |
| 10 | Mezcla y emulsión | C | min/lote | 140 | 12 | 112 | 168 | 2 | 0.2 | 6685.71 |
| 11 | Control de calidad de lote | A | min/lote | 60 | 8 | 52.2 | 67.8 | 1 | 0.13 | 7800 |
| 12 | Control de calidad de lote | B | min/lote | 75 | 8 | 65.25 | 84.75 | 1 | 0.13 | 6240 |
| 13 | Control de calidad de lote | C | min/lote | 55 | 8 | 47.85 | 62.15 | 1 | 0.13 | 8509.09 |
| 14 | Llenado y sellado | A | tubos/h | 2400 | 150 | 2112 | 2688 | 1 | 0.12 | 2400 |
| 15 | Llenado y sellado | B | tubos/h | 2000 | 150 | 1760 | 2240 | 1 | 0.12 | 2000 |
| 16 | Llenado y sellado | C | tubos/h | 2400 | 150 | 2112 | 2688 | 1 | 0.12 | 2400 |
| 17 | Encartonado | A | tubos/h | 3000 | 200 | 2790 | 3210 | 1 | 0.07 | 3000 |
| 18 | Encartonado | B | tubos/h | 3000 | 200 | 2790 | 3210 | 1 | 0.07 | 3000 |
| 19 | Encartonado | C | tubos/h | 3000 | 200 | 2790 | 3210 | 1 | 0.07 | 3000 |
| 20 | Empaque caja master | A | cajas/h | 110 | 10 | 100.1 | 119.9 | 1 | 0.09 | 2640 |
| 21 | Empaque caja master | B | cajas/h | 110 | 10 | 100.1 | 119.9 | 1 | 0.09 | 2640 |
| 22 | Empaque caja master | C | cajas/h | 110 | 10 | 100.1 | 119.9 | 1 | 0.09 | 2640 |

**Fórmulas (5 patrones distintos):**

- `F5`: `=D5*(1-I5)`
- `G5`: `=D5*(1+I5)`
- `J5`: `=Parámetros!$B$9*60/D5*H5`
- `J14`: `=D14*H14`
- `J20`: `=D20*Parámetros!$B$10*H20`

### Hoja `Utilizacion` — 22 filas × 9 columnas

| Fila | A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Capacidad, utilización y cuello de botella |  |  |  |  |  |  |  |  |
| 4 | Estación | Capacidad A (und/h) | Capacidad B (und/h) | Capacidad C (und/h) | OEE | Horas de alistamiento/mes | Horas requeridas/mes | Horas disponibles efectivas/mes | Utilización |
| 5 | Pesaje | 11700 | 10400 | 11700 | 0.9 | 0 | 9.0268 | 277.2 | 0.0325642 |
| 6 | Mezcla y emulsión | 6240 | 5200 | 6685.71 | 0.85 | 0 | 17.0572 | 261.8 | 0.0651535 |
| 7 | Control de calidad de lote | 7800 | 6240 | 8509.09 | 0.9 | 0 | 13.7954 | 277.2 | 0.049767 |
| 8 | Llenado y sellado | 2400 | 2000 | 2400 | 0.74 | 19.5 | 64.4672 | 227.92 | 0.28285 |
| 9 | Encartonado | 3000 | 3000 | 3000 | 0.83 | 0 | 33.9225 | 255.64 | 0.132696 |
| 10 | Empaque caja master | 2640 | 2640 | 2640 | 0.88 | 0 | 38.5483 | 271.04 | 0.142224 |
| 12 | Cuello de botella por producto (menor capacidad) |  |  |  |  |  |  |  |  |
| 13 | Producto | Estación limitante | Capacidad (und/h) |  |  |  |  |  |  |
| 14 | A | Llenado y sellado | 2400 |  |  |  |  |  |  |
| 15 | B | Llenado y sellado | 2000 |  |  |  |  |  |  |
| 16 | C | Llenado y sellado | 2400 |  |  |  |  |  |  |
| 18 | Estación más utilizada | Llenado y sellado | 0.28285 |  |  |  |  |  |  |
| 20 | OEE: llenadora 74 %, encartonadora 83 % y reactores 85 % son del ejercicio; pesaje (90 %), control de calidad (90 %) y empaque (88 %) son supuestos. |  |  |  |  |  |  |  |  |
| 21 | Horas requeridas = demanda de escenario / yield / capacidad, sumando los tres productos, más horas de alistamiento (solo llenadora). |  |  |  |  |  |  |  |  |
| 22 | Con factor de demanda 1 la utilización es baja; súbelo en la hoja Parametros para simular picos y ver cuándo se satura la llenadora. |  |  |  |  |  |  |  |  |

**Fórmulas (13 patrones distintos):**

- `B5`: `=Tiempos!J5`
- `G5`: `=Productos!$D$5/Productos!$E$5/B5+Productos!$D$6/Productos!$E$6/C5+Productos!$D$7/Productos!$E$7/D5+F5`
- `H5`: `=Parámetros!$B$7*E5`
- `I5`: `=G5/H5`
- `F8`: `=Parámetros!B12*Parámetros!B13`
- `B14`: `=INDEX($A$5:$A$10,MATCH(MIN(B5:B10),B5:B10,0))`
- `C14`: `=MIN(B5:B10)`
- `B15`: `=INDEX($A$5:$A$10,MATCH(MIN(C5:C10),C5:C10,0))`
- `C15`: `=MIN(C5:C10)`
- `B16`: `=INDEX($A$5:$A$10,MATCH(MIN(D5:D10),D5:D10,0))`
- `C16`: `=MIN(D5:D10)`
- `B18`: `=INDEX($A$5:$A$10,MATCH(MAX(I5:I10),I5:I10,0))`
- `C18`: `=MAX(I5:I10)`

### Hoja `Alistamiento` — 7 filas × 6 columnas

| Fila | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 1 | Tiempos de alistamiento (cambio de referencia) |  |  |  |  |  |
| 4 | Cambio | Limpieza de reactor (min) | Limpieza y ajuste de llenadora (min) | Ajuste de encartonadora (min) | Total (min) | Total (h) |
| 5 | Mismo producto, distinto tono | 25 | 35 | 10 | 70 | 1.16667 |
| 6 | A ↔ C (ambos con amoníaco) | 60 | 75 | 20 | 155 | 2.58333 |
| 7 | A/C ↔ B (con amoníaco a sin amoníaco) | 120 | 150 | 30 | 300 | 5 |

**Fórmulas (2 patrones distintos):**

- `E5`: `=SUM(B5:D5)`
- `F5`: `=E5/60`

### Hoja `Fallas` — 9 filas × 4 columnas

| Fila | A | B | C | D |
|---|---|---|---|---|
| 1 | Fallas y reparaciones (MTBF / MTTR) |  |  |  |
| 2 | Tiempo entre fallas: exponencial. Tiempo de reparación: lognormal. |  |  |  |
| 4 | Recurso | MTBF (h) | MTTR (h) | Disponibilidad por fallas |
| 5 | Reactor 1 | 180 | 3 | 0.983607 |
| 6 | Reactor 2 | 160 | 3.5 | 0.978593 |
| 7 | Llenadora de tubos | 70 | 2 | 0.972222 |
| 8 | Encartonadora | 120 | 1.5 | 0.987654 |
| 9 | Línea de empaque | 200 | 1 | 0.995025 |

**Fórmulas (1 patrones distintos):**

- `D5`: `=B5/(B5+C5)`

### Hoja `Mano de Obra` — 28 filas × 5 columnas

| Fila | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | Capacidad y mano de obra |  |  |  |  |
| 4 | Área | Operarios por turno |  |  |  |
| 5 | Pesaje | 2 |  |  |  |
| 6 | Mezcla | 2 |  |  |  |
| 7 | Control de calidad (laboratorio) | 2 |  |  |  |
| 8 | Llenado y sellado | 3 |  |  |  |
| 9 | Encartonado | 2 |  |  |  |
| 10 | Empaque caja master | 4 |  |  |  |
| 11 | Bodega y montacargas | 2 |  |  |  |
| 12 | Total por turno | 17 |  |  |  |
| 13 | Total operarios (todos los turnos) | 34 |  |  |  |
| 15 | Costo de mano de obra | COP/hora |  |  |  |
| 16 | Hora ordinaria | 13800 |  |  |  |
| 17 | Extra diurna (x1,25) | 17250 |  |  |  |
| 18 | Extra nocturna (x1,75) | 24150 |  |  |  |
| 20 | Horas extra | Valor |  |  |  |
| 21 | Límite legal por día (h) | 2 |  |  |  |
| 22 | Límite legal por semana (h) | 12 |  |  |  |
| 23 | Uso actual (h extra/mes, llenado y empaque) | 150 |  |  |  |
| 24 | Costo mensual aprox. con tarifa diurna (COP) | 2587500 |  |  |  |
| 26 | Subcontratación | Costo (COP) | Capacidad (und/mes) | Lead time (días) | Condiciones |
| 27 | Maquila de llenado de tubos | 380 | 20000 | 5 | Costo por tubo; solo fórmulas con amoníaco (A y C) |
| 28 | Empaque externo | 210 | 500 | 2 | Costo por caja master; capacidad en cajas/mes |

**Fórmulas (4 patrones distintos):**

- `B12`: `=SUM(B5:B11)`
- `B13`: `=B12*Parámetros!B5`
- `B17`: `=B16*1.25`
- `B24`: `=B23*B17`

### Hoja `Métricas` — 53 filas × 5 columnas

| Fila | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | Métricas de eficiencia: Takt time, Cycle time, Throughput y WIP |  |  |  |  |
| 4 | 1. Takt time |  |  |  |  |
| 5 | Producto | Demanda (und/mes) | Tiempo disponible (s/mes) | Takt time (s/und) | Takt time (min por lote de tubos) |
| 6 | A | 48000 | 1108800 | 23.1 | 3003 |
| 7 | B | 30000 | 1108800 | 36.96 | 4804.8 |
| 8 | C | 22000 | 1108800 | 50.4 | 6552 |
| 9 | Familia (total) | 100000 | 1108800 | 11.088 | 1441.44 |
| 12 | 2. Cycle time por estación (s/und a capacidad nominal) |  |  |  |  |
| 13 | Estación | A | B | C |  |
| 14 | Pesaje | 0.307692 | 0.346154 | 0.307692 |  |
| 15 | Mezcla y emulsión | 0.576923 | 0.692308 | 0.538462 |  |
| 16 | Control de calidad de lote | 0.461538 | 0.576923 | 0.423077 |  |
| 17 | Llenado y sellado | 1.5 | 1.8 | 1.5 |  |
| 18 | Encartonado | 1.2 | 1.2 | 1.2 |  |
| 19 | Empaque caja master | 1.36364 | 1.36364 | 1.36364 |  |
| 20 | Cycle time del cuello de botella (s/und) | 1.5 | 1.8 | 1.5 |  |
| 21 | Cycle time efectivo con OEE (s/und) | 2.02703 | 2.43243 | 2.02703 |  |
| 22 | Takt time (s/und) | 23.1 | 36.96 | 50.4 |  |
| 23 | Takt / cycle time efectivo (x) | 11.396 | 15.1947 | 24.864 |  |
| 26 | 3. Tiempo de proceso por lote (min, sin esperas) |  |  |  |  |
| 27 | Estación | A | B | C |  |
| 28 | Pesaje | 40 | 45 | 40 |  |
| 29 | Mezcla y emulsión | 150 | 180 | 140 |  |
| 30 | Control de calidad de lote | 60 | 75 | 55 |  |
| 31 | Llenado y sellado | 195 | 234 | 195 |  |
| 32 | Encartonado | 156 | 156 | 156 |  |
| 33 | Empaque caja master | 177.273 | 177.273 | 177.273 |  |
| 34 | Tiempo total de proceso por lote (min) | 778.273 | 867.273 | 763.273 |  |
| 35 | Tiempo total de proceso por lote (h) | 12.9712 | 14.4545 | 12.7212 |  |
| 38 | 4. Throughput, WIP y tiempo de flujo (Ley de Little: WIP = throughput x tiempo de flujo) |  |  |  |  |
| 39 | Indicador | A | B | C | Total |
| 40 | Throughput requerido (und/h) | 155.844 | 97.4026 | 71.4286 | 324.675 |
| 41 | Throughput máximo: cuello de botella x OEE (und/h) | 1776 | 1480 | 1776 | — |
| 42 | Holgura de throughput (x) | 11.396 | 15.1947 | 24.864 | — |
| 43 | Lotes por mes | 6.15385 | 3.84615 | 2.82051 | 12.8205 |
| 44 | WIP actual (tubos) | 4000 | 2500 | 2000 | 8500 |
| 45 | Tiempo de flujo por Little (h) | 25.6667 | 25.6667 | 28 | 26.18 |
| 46 | Tiempo de flujo (días hábiles) | 1.83333 | 1.83333 | 2 | 1.87 |
| 47 | Tiempo de proceso por lote (h) | 12.9712 | 14.4545 | 12.7212 | 13.3612 |
| 48 | Eficiencia de flujo (tiempo de proceso / tiempo de flujo) | 0.505372 | 0.563164 | 0.454329 | 0.51036 |
| 49 | WIP crítico con solo tiempo de proceso (tubos) | 2021.49 | 1407.91 | 908.658 | 4338.06 |
| 50 | WIP actual / WIP crítico (x) | 1.97874 | 1.77568 | 2.20105 | 1.9594 |

**Fórmulas (43 patrones distintos):**

- `B6`: `=Productos!D5`
- `C6`: `=Parámetros!$B$7*3600`
- `D6`: `=C6/B6`
- `E6`: `=D6*Parámetros!$B$9/60`
- `B14`: `=3600/Utilizacion!B5`
- `C14`: `=3600/Utilizacion!C5`
- `D14`: `=3600/Utilizacion!D5`
- `B20`: `=MAX(B14:B19)`
- `C20`: `=MAX(C14:C19)`
- `D20`: `=MAX(D14:D19)`
- `B21`: `=B20/INDEX(Utilizacion!$E$5:$E$10,MATCH(B20,B14:B19,0))`
- `C21`: `=C20/INDEX(Utilizacion!$E$5:$E$10,MATCH(C20,C14:C19,0))`
- `D21`: `=D20/INDEX(Utilizacion!$E$5:$E$10,MATCH(D20,D14:D19,0))`
- `B22`: `=D6`
- `B23`: `=B22/B21`
- `C23`: `=C22/C21`
- `D23`: `=D22/D21`
- `B28`: `=Tiempos!D5`
- `B31`: `=Parámetros!$B$9/Tiempos!D14*60`
- `B33`: `=Parámetros!$B$9/(Tiempos!D20*Parámetros!$B$10)*60`
- `B34`: `=SUM(B28:B33)`
- `C34`: `=SUM(C28:C33)`
- `D34`: `=SUM(D28:D33)`
- `B35`: `=B34/60`
- `C35`: `=C34/60`
- `D35`: `=D34/60`
- `B40`: `=Productos!D5/Parámetros!$B$7`
- `E40`: `=SUM(B40:D40)`
- `B41`: `=MIN(Utilizacion!B5:B10)*INDEX(Utilizacion!$E$5:$E$10,MATCH(MIN(Utilizacion!B5:B10),Utilizacion!B5:B10,0))`
- `C41`: `=MIN(Utilizacion!C5:C10)*INDEX(Utilizacion!$E$5:$E$10,MATCH(MIN(Utilizacion!C5:C10),Utilizacion!C5:C10,0))`
- `D41`: `=MIN(Utilizacion!D5:D10)*INDEX(Utilizacion!$E$5:$E$10,MATCH(MIN(Utilizacion!D5:D10),Utilizacion!D5:D10,0))`
- `B44`: `=Productos!N5`
- `E45`: `=E44/E40`
- `B46`: `=B45/(Parámetros!$B$5*Parámetros!$B$6)`
- `C46`: `=C45/(Parámetros!$B$5*Parámetros!$B$6)`
- `D46`: `=D45/(Parámetros!$B$5*Parámetros!$B$6)`
- `E46`: `=E45/(Parámetros!$B$5*Parámetros!$B$6)`
- `B47`: `=B35`
- `C47`: `=C35`
- `E47`: `=SUMPRODUCT(B47:D47,B40:D40)/E40`
- `B49`: `=B40*B47`
- `C49`: `=C40*C47`
- `D49`: `=D40*D47`

### Hoja `Plan Agregado` — 60 filas × 15 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Planeación agregada de la familia de tintes (12 meses, unidades = tubos) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 2 | Compara tres estrategias con la misma demanda: persecución, producción nivelada y mixta. Azul = dato editable. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 4 | α: peso de la demanda del mes en la estrategia mixta (1 = persecución, 0 = nivelada) | 0.5 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 5 | Inventario inicial de producto terminado (und) | 29500 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 6 | Capacidad de almacenamiento de PT (und) | 58000 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 7 | Capacidad efectiva de la llenadora con la mezcla de productos (und/h) | 1675.47 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 8 | Horas efectivas por día | 14 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 9 | Costo de mantener inventario, promedio ponderado (COP/und-mes) | 83.5633 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 10 | Estrategia seleccionada (1 persecución, 2 nivelada, 3 mixta) | 1 | Persecución |  |  |  |  |  |  |  |  |  |  |  |  |
| 12 |  |  |  |  |  | Persecución |  |  | Nivelada |  |  | Mixta |  |  |  |
| 13 | Mes | Días hábiles | Índice estacional | Demanda (und) | Capacidad regular llenadora (und) | Producción | Inventario final | Utilización | Producción | Inventario final | Utilización | Producción | Inventario final | Utilización | Holgura de capacidad (x) |
| 14 | Enero | 20 | 0.634131 | 63413.1 | 469132 | 63413.1 | 29500 | 0.135171 | 100000 | 66086.9 | 0.21316 | 81706.6 | 47793.4 | 0.174165 | 7.39803 |
| 15 | Febrero | 20 | 1.01889 | 101889 | 469132 | 101889 | 29500 | 0.217187 | 100000 | 64197.6 | 0.21316 | 100945 | 46848.8 | 0.215173 | 4.60433 |
| 16 | Marzo | 21 | 1.33118 | 133118 | 492589 | 133118 | 29500 | 0.270241 | 100000 | 31079.9 | 0.203009 | 116559 | 30289.9 | 0.236625 | 3.7004 |
| 17 | Abril | 21 | 0.347335 | 34733.5 | 492589 | 34733.5 | 29500 | 0.0705122 | 100000 | 96346.4 | 0.203009 | 67366.8 | 62923.2 | 0.136761 | 14.1819 |
| 18 | Mayo | 21 | 1.30786 | 130786 | 492589 | 130786 | 29500 | 0.265508 | 100000 | 65560 | 0.203009 | 115393 | 47530 | 0.234259 | 3.76636 |
| 19 | Junio | 20 | 1.03697 | 103697 | 469132 | 103697 | 29500 | 0.221041 | 100000 | 61862.8 | 0.21316 | 101849 | 45681.4 | 0.2171 | 4.52406 |
| 20 | Julio | 22 | 1.52969 | 152969 | 516045 | 152969 | 29500 | 0.296426 | 100000 | 8893.68 | 0.193781 | 126485 | 19196.8 | 0.245104 | 3.37353 |
| 21 | Agosto | 20 | 0.793937 | 79393.7 | 469132 | 79393.7 | 29500 | 0.169235 | 100000 | 29500 | 0.21316 | 89696.8 | 29500 | 0.191197 | 5.90893 |
| 22 | Septiembre | 22 | 1 | 100000 | 516045 | 100000 | 29500 | 0.193781 | 100000 | 29500 | 0.193781 | 100000 | 29500 | 0.193781 | 5.16045 |
| 23 | Octubre | 20 | 1 | 100000 | 469132 | 100000 | 29500 | 0.21316 | 100000 | 29500 | 0.21316 | 100000 | 29500 | 0.21316 | 4.69132 |
| 24 | Noviembre | 20 | 1 | 100000 | 469132 | 100000 | 29500 | 0.21316 | 100000 | 29500 | 0.21316 | 100000 | 29500 | 0.21316 | 4.69132 |
| 25 | Diciembre | 19 | 1 | 100000 | 445675 | 100000 | 29500 | 0.224379 | 100000 | 29500 | 0.224379 | 100000 | 29500 | 0.224379 | 4.45675 |
| 26 | Total | 246 |  | 1200000 | 5.77032e+06 | 1200000 |  |  | 1200000 |  |  | 1200000 |  |  |  |
| 29 | Comparación de estrategias |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 30 | Indicador | Persecución | Nivelada | Mixta |  |  |  |  |  |  |  |  |  |  |  |
| 31 | Producción anual (und) | 1200000 | 1200000 | 1200000 |  |  |  |  |  |  |  |  |  |  |  |
| 32 | Inventario promedio (und) | 29500 | 45127.3 | 37313.6 |  |  |  |  |  |  |  |  |  |  |  |
| 33 | Inventario máximo (und) | 29500 | 96346.4 | 62923.2 |  |  |  |  |  |  |  |  |  |  |  |
| 34 | Inventario mínimo (und) | 29500 | 8893.68 | 19196.8 |  |  |  |  |  |  |  |  |  |  |  |
| 35 | Meses con desabastecimiento (inventario < 0) | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 36 | Meses sobre la capacidad de almacenamiento | 0 | 5 | 1 |  |  |  |  |  |  |  |  |  |  |  |
| 37 | Utilización máxima de la llenadora | 0.296426 | 0.224379 | 0.245104 |  |  |  |  |  |  |  |  |  |  |  |
| 38 | Horas extra requeridas (h/año) | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 39 | Costo anual de mantener inventario (COP) | 29581420 | 4.52518e+07 | 3.74166e+07 |  |  |  |  |  |  |  |  |  |  |  |
| 40 | Costo de horas extra (COP) | 0 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |
| 41 | Variación de producción entre meses (máx - mín, und) | 118236 | 0 | 59117.8 |  |  |  |  |  |  |  |  |  |  |  |
| 42 | Costo total estimado (COP) | 29581420 | 4.52518e+07 | 3.74166e+07 |  |  |  |  |  |  |  |  |  |  |  |
| 43 | ¿Plan factible? | Sí | No | No |  |  |  |  |  |  |  |  |  |  |  |
| 46 | Desagregación: plan por producto de la estrategia seleccionada (celda B9) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| 47 | Mes | Producción total (und) | Lotes de 500 kg | Producto A (und) | Producto B (und) | Producto C (und) | Inventario final PT (und) |  |  |  |  |  |  |  |  |
| 48 | Enero | 63413.1 | 9 | 30438.3 | 19023.9 | 13950.9 | 29500 |  |  |  |  |  |  |  |  |
| 49 | Febrero | 101889 | 14 | 48906.9 | 30566.8 | 22415.6 | 29500 |  |  |  |  |  |  |  |  |
| 50 | Marzo | 133118 | 18 | 63896.5 | 39935.3 | 29285.9 | 29500 |  |  |  |  |  |  |  |  |
| 51 | Abril | 34733.5 | 5 | 16672.1 | 10420.1 | 7641.37 | 29500 |  |  |  |  |  |  |  |  |
| 52 | Mayo | 130786 | 17 | 62777.5 | 39235.9 | 28773 | 29500 |  |  |  |  |  |  |  |  |
| 53 | Junio | 103697 | 14 | 49774.7 | 31109.2 | 22813.4 | 29500 |  |  |  |  |  |  |  |  |
| 54 | Julio | 152969 | 20 | 73425.2 | 45890.7 | 33653.2 | 29500 |  |  |  |  |  |  |  |  |
| 55 | Agosto | 79393.7 | 11 | 38109 | 23818.1 | 17466.6 | 29500 |  |  |  |  |  |  |  |  |
| 56 | Septiembre | 100000 | 13 | 48000 | 30000 | 22000 | 29500 |  |  |  |  |  |  |  |  |
| 57 | Octubre | 100000 | 13 | 48000 | 30000 | 22000 | 29500 |  |  |  |  |  |  |  |  |
| 58 | Noviembre | 100000 | 13 | 48000 | 30000 | 22000 | 29500 |  |  |  |  |  |  |  |  |
| 59 | Diciembre | 100000 | 13 | 48000 | 30000 | 22000 | 29500 |  |  |  |  |  |  |  |  |

**Fórmulas (68 patrones distintos):**

- `B5`: `=Productos!I8`
- `B6`: `=Productos!K8`
- `B7`: `=1/(Productos!D5/Productos!D8/Utilizacion!B8+Productos!D6/Productos!D8/Utilizacion!C8+Productos!D7/Productos!D8/Utilizacion!D8)*Utilizacion!E8`
- `B8`: `=Parámetros!B5*Parámetros!B6`
- `B9`: `=SUMPRODUCT(Productos!G5:G7,Productos!D5:D7)/Productos!D8`
- `C10`: `=CHOOSE(B10,"Persecución","Nivelada","Mixta")`
- `C14`: `=Ventas!C5`
- `D14`: `=Productos!$D$8*C14`
- `E14`: `=B14*$B$8*$B$7`
- `F14`: `=D14`
- `G14`: `=$B$5+F14-D14`
- `H14`: `=F14/E14`
- `I14`: `=AVERAGE($D$14:$D$25)`
- `J14`: `=$B$5+I14-D14`
- `K14`: `=I14/E14`
- `L14`: `=$B$4*D14+(1-$B$4)*AVERAGE($D$14:$D$25)`
- `M14`: `=$B$5+L14-D14`
- `N14`: `=L14/E14`
- `O14`: `=E14/D14`
- `G15`: `=G14+F15-D15`
- `J15`: `=J14+I15-D15`
- `M15`: `=M14+L15-D15`
- `B26`: `=SUM(B14:B25)`
- `D26`: `=SUM(D14:D25)`
- `E26`: `=SUM(E14:E25)`
- `F26`: `=SUM(F14:F25)`
- `I26`: `=SUM(I14:I25)`
- `L26`: `=SUM(L14:L25)`
- `B32`: `=AVERAGE(G14:G25)`
- `C32`: `=AVERAGE(J14:J25)`
- `D32`: `=AVERAGE(M14:M25)`
- `B33`: `=MAX(G14:G25)`
- `C33`: `=MAX(J14:J25)`
- `D33`: `=MAX(M14:M25)`
- `B34`: `=MIN(G14:G25)`
- `C34`: `=MIN(J14:J25)`
- `D34`: `=MIN(M14:M25)`
- `B35`: `=COUNTIF(G14:G25,"<0")`
- `C35`: `=COUNTIF(J14:J25,"<0")`
- `D35`: `=COUNTIF(M14:M25,"<0")`
- `B36`: `=COUNTIF(G14:G25,">"&$B$6)`
- `C36`: `=COUNTIF(J14:J25,">"&$B$6)`
- `D36`: `=COUNTIF(M14:M25,">"&$B$6)`
- `B37`: `=MAX(H14:H25)`
- `C37`: `=MAX(K14:K25)`
- `D37`: `=MAX(N14:N25)`
- `B38`: `=SUMPRODUCT((F14:F25>$E$14:$E$25)*(F14:F25-$E$14:$E$25))/$B$7`
- `C38`: `=SUMPRODUCT((I14:I25>$E$14:$E$25)*(I14:I25-$E$14:$E$25))/$B$7`
- `D38`: `=SUMPRODUCT((L14:L25>$E$14:$E$25)*(L14:L25-$E$14:$E$25))/$B$7`
- `B39`: `=SUM(G14:G25)*$B$9`
- `C39`: `=SUM(J14:J25)*$B$9`
- `D39`: `=SUM(M14:M25)*$B$9`
- `B40`: `=B38*'Mano de Obra'!$B$12*'Mano de Obra'!$B$17`
- `C40`: `=C38*'Mano de Obra'!$B$12*'Mano de Obra'!$B$17`
- `D40`: `=D38*'Mano de Obra'!$B$12*'Mano de Obra'!$B$17`
- `B41`: `=MAX(F14:F25)-MIN(F14:F25)`
- `C41`: `=MAX(I14:I25)-MIN(I14:I25)`
- `D41`: `=MAX(L14:L25)-MIN(L14:L25)`
- `B42`: `=B39+B40`
- `C42`: `=C39+C40`
- `D42`: `=D39+D40`
- `B43`: `=IF(AND(B35=0,B36=0,B38=0),"Sí","No")`
- `C43`: `=IF(AND(C35=0,C36=0,C38=0),"Sí","No")`
- `D43`: `=IF(AND(D35=0,D36=0,D38=0),"Sí","No")`
- `B48`: `=CHOOSE($B$10,F14,I14,L14)`
- `C48`: `=ROUNDUP(B48/Parámetros!$B$9,0)`
- `D48`: `=B48*Productos!$D$5/Productos!$D$8`
- `G48`: `=CHOOSE($B$10,G14,J14,M14)`

### Hoja `Restricciones` — 24 filas × 7 columnas

| Fila | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| 1 | Restricciones de capacidad, demanda y almacenamiento |  |  |  |  |  |  |
| 4 | Tipo | Recurso o tema | Indicador | Valor | Referencia | Estado | Qué significa |
| 5 | Capacidad | Llenadora de tubos | Utilización pico mensual (estrategia persecución) | 0.296426 | 1 | Holgura | Qué tan cerca está la llenadora de su límite en el mes de mayor demanda. |
| 6 | Capacidad | Llenadora de tubos | Factor de demanda máximo antes de saturarse | 3.37353 | 1 | Holgura | Cuántas veces se puede multiplicar la demanda base antes de que el mes pico supere la capacidad. |
| 7 | Capacidad | Reactores de mezcla | Utilización mensual con demanda base | 0.0651535 | 1 | Holgura | Uso de los 2 reactores con el promedio mensual de demanda. |
| 8 | Capacidad | Horas extra | Horas extra requeridas al año (persecución) | 0 | 624 | Holgura | Referencia: límite legal de 12 h extra por semana durante 52 semanas. |
| 9 | Demanda | Estacionalidad | Pico / promedio del índice estacional | 1.52969 | 1.25 | Alerta | Referencia de alerta (supuesto): picos de 25 % sobre el promedio exigen anticipar inventario. |
| 10 | Demanda | Mes pico | Mes de mayor demanda | Julio | — | Informativo | Mes donde el inventario debe estar listo con anticipación. |
| 11 | Demanda | Mezcla de productos | Participación de Visalia (B) en la demanda | 0.3 | — | Informativo | Visalia exige cambios largos de fórmula (sin amoníaco) y la mezcla más lenta. |
| 12 | Almacenamiento | Producto terminado | Cobertura máxima que permite la bodega (días) | 12.76 | 6.49 | Holgura | Referencia: cobertura actual. Muestra cuánto inventario adicional cabe en bodega. |
| 13 | Almacenamiento | Producto terminado | Inventario máximo de la estrategia nivelada / capacidad de bodega (x) | 1.66114 | 1 | Crítica | Mayor que 1 significa que producir parejo durante el año no cabe en la bodega. |
| 14 | Almacenamiento | Materia prima importada | Cobertura actual de base y colorantes (días hábiles) | 12.9708 | 55 | Crítica | Referencia: lead time de importación + stock de seguridad de 3 semanas. |
| 15 | Almacenamiento | Tubos vacíos | Cobertura actual (días hábiles) | 13.2 | 12 | Alerta | Referencia: lead time del proveedor nacional. |
| 16 | Demanda | Clientes | Participación de los 10 mayores clientes en las ventas (may-jul) | 0.39036 | — | Informativo | Datos reales: pocos clientes concentran gran parte de las ventas, lo que aumenta el riesgo de demanda. |
| 18 | Cálculos de apoyo: materia prima |  |  |  |  |  |  |
| 19 | Concepto | Valor | Unidad |  |  |  |  |
| 20 | Consumo de base y colorantes | 6106.04 | kg/mes |  |  |  |  |
| 21 | Consumo diario | 277.547 | kg/día hábil |  |  |  |  |
| 22 | Stock de seguridad | 15 | días hábiles (3 semanas; supuesto) |  |  |  |  |
| 23 | Stock requerido (lead time + seguridad) | 15265.1 | kg |  |  |  |  |
| 24 | Faltante frente al stock actual | 11665.1 | kg |  |  |  |  |

**Fórmulas (27 patrones distintos):**

- `D5`: `='Plan Agregado'!B37`
- `E5`: `=1`
- `F5`: `=IF(D5>=E5,"Crítica",IF(D5>=0.85,"Alerta","Holgura"))`
- `D6`: `=Parámetros!B8*MIN('Plan Agregado'!O14:O25)`
- `E6`: `=Parámetros!B8`
- `F6`: `=IF(D6/E6<1,"Crítica",IF(D6/E6<1.5,"Alerta","Holgura"))`
- `D7`: `=Utilizacion!I6`
- `E8`: `='Mano de Obra'!B22*52`
- `F8`: `=IF(D8>E8,"Crítica",IF(D8>0,"Alerta","Holgura"))`
- `D9`: `=MAX('Plan Agregado'!C14:C25)/AVERAGE('Plan Agregado'!C14:C25)`
- `F9`: `=IF(D9>=E9,"Alerta","Holgura")`
- `D10`: `=INDEX('Plan Agregado'!A14:A25,MATCH(MAX('Plan Agregado'!C14:C25),'Plan Agregado'!C14:C25,0))`
- `D11`: `=Productos!D6/Productos!D8`
- `D12`: `=Productos!K8/(Productos!D8/Parámetros!B4)`
- `E12`: `=Productos!I8/(Productos!D8/Parámetros!B4)`
- `D13`: `='Plan Agregado'!C33/'Plan Agregado'!B6`
- `F13`: `=IF(D13>E13,"Crítica",IF(D13>0.9,"Alerta","Holgura"))`
- `D14`: `=Productos!C12/B21`
- `E14`: `=Productos!E12+B22`
- `F14`: `=IF(D14<E14,"Crítica",IF(D14<E14*1.25,"Alerta","Holgura"))`
- `D15`: `=Productos!C13/(Productos!D8/Parámetros!B4)`
- `E15`: `=Productos!E13`
- `D16`: `=Clientes!C7`
- `B20`: `=(Productos!D5/Productos!E5+Productos!D6/Productos!E6+Productos!D7/Productos!E7)*Parámetros!B14/1000`
- `B21`: `=B20/Parámetros!B4`
- `B23`: `=B21*(Productos!E12+B22)`
- `B24`: `=MAX(0,B23-Productos!C12)`

### Hoja `Proceso Planeación Agregada` — 16 filas × 4 columnas

| Fila | A | B | C |
|---|---|---|---|
| 1 | Proceso de planeación agregada propuesto |  |  |
| 2 | Pasos que sigue THYMS cada mes para fijar producción, inventario y recursos de la familia de tintes. |  |  |
| 4 | Paso | ¿Qué se hace? | Insumo |
| 5 | 1 | Pronosticar la demanda de la familia por mes y aplicar la estacionalidad. | Demanda base por producto e índice estacional calculado con ventas reales 2026 |
| 6 | 2 | Expresar la demanda en una unidad común (tubos de 60 g) y en horas del cuello de botella. | Capacidad de la llenadora y OEE |
| 7 | 3 | Medir la eficiencia del sistema actual con Takt time, Cycle time, Throughput y WIP. | Tiempos, WIP y demanda |
| 8 | 4 | Identificar restricciones de capacidad, demanda y almacenamiento. | Capacidad, bodega, lead times |
| 9 | 5 | Construir las estrategias: persecución, nivelada y mixta (α ajustable). | Demanda mensual, inventario inicial |
| 10 | 6 | Evaluar cada estrategia: inventario, desabastecimiento, bodega, horas extra y costo. | Costos de holding y mano de obra |
| 11 | 7 | Seleccionar la estrategia factible de menor costo y desagregarla por producto y por lote. | Mezcla de demanda, tamaño de lote |
| 12 | 8 | Revisar cada mes con la demanda real y ajustar materia prima y alistamientos. | Ventas reales, lead times |

### Hoja `Facturas Mayo-Julio` — 468 filas × 5 columnas

| Fila | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | Facturas de mayo a julio de 2026 (datos reales) |  |  |  |  |
| 4 | Mes | Factura | Código cliente | Cliente | Ventas (COP) |
| 5 | 5 | F571143 | 900001 | CLIENTE 001 | 258300 |
| 6 | 5 | F571144 | 900002 | CLIENTE 002 | 1109220 |
| 7 | 5 | F571145 | 900003 | CLIENTE 003 | 302400 |
| 8 | 5 | F571146 | 900004 | CLIENTE 004 | 548340 |
| 9 | 5 | F571149 | 900005 | CLIENTE 005 | 1773840 |
| 10 | 5 | F571154 | 900006 | CLIENTE 006 | 973560 |
| 11 | 5 | F571155 | 900005 | CLIENTE 005 | 1641600 |
| 12 | 5 | F571160 | 900007 | CLIENTE 007 | 497040 |
| 13 | 5 | F571162 | 900008 | CLIENTE 008 | 476805 |
| 14 | 5 | F571164 | 900009 | CLIENTE 009 | 2880115 |
| 15 | 5 | F571168 | 900010 | CLIENTE 010 | 766080 |
| 16 | 5 | F571169 | 900011 | CLIENTE 011 | 2867100 |
| 17 | 5 | F571170 | 900012 | CLIENTE 012 | 1436400 |
| 18 | 5 | F571171 | 900007 | CLIENTE 007 | 1504800 |
| 19 | 5 | F571172 | 900013 | CLIENTE 013 | 1996140 |
| 20 | 5 | F571173 | 900012 | CLIENTE 012 | 1682640 |
| 21 | 5 | F571174 | 900014 | CLIENTE 014 | 608760 |
| 22 | 5 | F571176 | 900015 | CLIENTE 015 | 634980 |
| 23 | 5 | F571177 | 900016 | CLIENTE 016 | 1231200 |
| 24 | 5 | F571178 | 900017 | CLIENTE 017 | 1178760 |
| 25 | 5 | F571179 | 900012 | CLIENTE 012 | 479370 |
| 26 | 5 | F571180 | 900018 | CLIENTE 018 | 344280 |
| 27 | 5 | F571181 | 900009 | CLIENTE 009 | 1517625 |
| 28 | 5 | F571182 | 900019 | CLIENTE 019 | 560880 |
| 29 | 5 | F571183 | 900020 | CLIENTE 020 | 273600 |
| 30 | 5 | F571261 | 900021 | CLIENTE 021 | 820800 |
| 31 | 5 | F571262 | 900022 | CLIENTE 022 | 752400 |
| 32 | 5 | F571263 | 900022 | CLIENTE 022 | 560880 |
| 33 | 5 | F571264 | 900023 | CLIENTE 023 | 6459240 |
| 34 | 5 | F571270 | 900024 | CLIENTE 024 | 1423005 |
| 35 | 5 | F571286 | 900025 | CLIENTE 025 | 949800 |
| 36 | 5 | F571290 | 900023 | CLIENTE 023 | 3791640 |
| 37 | 5 | F571291 | 900026 | CLIENTE 026 | 519080 |
| 38 | 5 | F571361 | 900027 | CLIENTE 027 | 280440 |
| 39 | 5 | F571362 | 900028 | CLIENTE 028 | 2346120 |
| 40 | 5 | F571367 | 900029 | CLIENTE 029 | 379800 |
| 41 | 5 | F571369 | 900029 | CLIENTE 029 | 648000 |
| 42 | 5 | F571392 | 900030 | CLIENTE 030 | 842745 |
| 43 | 5 | F571393 | 900031 | CLIENTE 031 | 1231200 |
| 44 | 5 | F571396 | 900031 | CLIENTE 031 | 1417020 |
| 45 | 5 | F571397 | 900032 | CLIENTE 032 | 1833120 |
| 46 | 5 | F571413 | 900028 | CLIENTE 028 | 2273160 |
| 47 | 5 | F571414 | 900033 | CLIENTE 033 | 1842240 |
| 48 | 5 | F571415 | 900033 | CLIENTE 033 | 1151400 |
| 49 | 5 | F571548 | 900034 | CLIENTE 034 | 2375665 |
| 50 | 5 | F571551 | 900035 | CLIENTE 035 | 1055640 |
| 51 | 5 | F571554 | 900036 | CLIENTE 036 | 1179045 |
| 52 | 5 | F571555 | 900037 | CLIENTE 037 | 1193200 |
| 53 | 5 | F571566 | 900038 | CLIENTE 038 | 1935720 |
| 54 | 5 | F571568 | 900039 | CLIENTE 039 | 702000 |
| 55 | 5 | F571569 | 900040 | CLIENTE 040 | 1128600 |
| 56 | 5 | F571570 | 900038 | CLIENTE 038 | 896040 |
| 57 | 5 | F571571 | 900040 | CLIENTE 040 | 1126890 |
| 58 | 5 | F571572 | 900041 | CLIENTE 041 | 2806680 |
| 59 | 5 | F571578 | 900042 | CLIENTE 042 | 2337285 |
| 60 | 5 | F571664 | 900043 | CLIENTE 043 | 2268600 |
| 61 | 5 | F571665 | 900044 | CLIENTE 044 | 1723680 |
| 62 | 5 | F571666 | 900044 | CLIENTE 044 | 797145 |

> **Hoja larga:** arriba se muestran 60 de 466 filas con datos. **Todos los valores de la hoja están en [`Datos Thyms Completo-datos/Facturas_Mayo-Julio.csv`](./Datos%20Thyms%20Completo-datos/Facturas_Mayo-Julio.csv)** (CSV, UTF-8).

### Hoja `Clientes` — 171 filas × 5 columnas

| Fila | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | Concentración de ventas por cliente (mayo a julio de 2026) |  |  |  |  |
| 4 | Clientes distintos |  | 161 |  |  |
| 5 | Ventas totales del detalle (COP) |  | 590813195 |  |  |
| 6 | Participación del mayor cliente |  | 0.136134 |  |  |
| 7 | Participación de los 10 mayores clientes |  | 0.39036 |  |  |
| 8 | Participación del 20 % de clientes con más ventas |  | 0.639388 |  |  |
| 10 | Código cliente | Cliente | Ventas (COP) | % del total | % acumulado |
| 11 | 900023 | CLIENTE 023 | 80429530 | 0.136134 | 0.136134 |
| 12 | 900028 | CLIENTE 028 | 40026160 | 0.0677476 | 0.203881 |
| 13 | 900033 | CLIENTE 033 | 21855890 | 0.0369929 | 0.240874 |
| 14 | 900038 | CLIENTE 038 | 15120865 | 0.0255933 | 0.266467 |
| 15 | 900044 | CLIENTE 044 | 14766705 | 0.0249939 | 0.291461 |
| 16 | 900009 | CLIENTE 009 | 13768540 | 0.0233044 | 0.314766 |
| 17 | 900011 | CLIENTE 011 | 12135585 | 0.0205405 | 0.335306 |
| 18 | 900022 | CLIENTE 022 | 11139700 | 0.0188549 | 0.354161 |
| 19 | 900062 | CLIENTE 062 | 11139700 | 0.0188549 | 0.373016 |
| 20 | 900072 | CLIENTE 072 | 10246890 | 0.0173437 | 0.39036 |
| 21 | 900066 | CLIENTE 066 | 9952200 | 0.0168449 | 0.407204 |
| 22 | 900080 | CLIENTE 080 | 9756120 | 0.016513 | 0.423717 |
| 23 | 900015 | CLIENTE 015 | 8966100 | 0.0151759 | 0.438893 |
| 24 | 900042 | CLIENTE 042 | 8174655 | 0.0138363 | 0.45273 |
| 25 | 900005 | CLIENTE 005 | 8114520 | 0.0137345 | 0.466464 |
| 26 | 900047 | CLIENTE 047 | 6979840 | 0.011814 | 0.478278 |
| 27 | 900096 | CLIENTE 096 | 6953810 | 0.0117699 | 0.490048 |
| 28 | 900012 | CLIENTE 012 | 6927970 | 0.0117262 | 0.501774 |
| 29 | 900016 | CLIENTE 016 | 6714600 | 0.011365 | 0.513139 |
| 30 | 900032 | CLIENTE 032 | 6334980 | 0.0107225 | 0.523862 |
| 31 | 900128 | CLIENTE 128 | 6314460 | 0.0106877 | 0.534549 |
| 32 | 900049 | CLIENTE 049 | 6252900 | 0.0105835 | 0.545133 |
| 33 | 900024 | CLIENTE 024 | 6215185 | 0.0105197 | 0.555653 |
| 34 | 900134 | CLIENTE 134 | 5986140 | 0.010132 | 0.565785 |
| 35 | 900031 | CLIENTE 031 | 5958780 | 0.0100857 | 0.57587 |
| 36 | 900110 | CLIENTE 110 | 5889240 | 0.00996802 | 0.585838 |
| 37 | 900081 | CLIENTE 081 | 5549520 | 0.00939302 | 0.595231 |
| 38 | 900095 | CLIENTE 095 | 5459555 | 0.00924075 | 0.604472 |
| 39 | 900057 | CLIENTE 057 | 5307840 | 0.00898396 | 0.613456 |
| 40 | 900075 | CLIENTE 075 | 5238870 | 0.00886722 | 0.622323 |
| 41 | 900061 | CLIENTE 061 | 5046780 | 0.00854209 | 0.630865 |
| 42 | 900043 | CLIENTE 043 | 5035380 | 0.0085228 | 0.639388 |
| 43 | 900074 | CLIENTE 074 | 5022840 | 0.00850157 | 0.64789 |
| 44 | 900034 | CLIENTE 034 | 4870555 | 0.00824382 | 0.656134 |
| 45 | 900008 | CLIENTE 008 | 4658325 | 0.0078846 | 0.664018 |
| 46 | 900021 | CLIENTE 021 | 4379880 | 0.00741331 | 0.671432 |
| 47 | 900058 | CLIENTE 058 | 4163280 | 0.00704669 | 0.678478 |
| 48 | 900041 | CLIENTE 041 | 4092600 | 0.00692706 | 0.685405 |
| 49 | 900122 | CLIENTE 122 | 4020780 | 0.0068055 | 0.692211 |
| 50 | 900056 | CLIENTE 056 | 3958935 | 0.00670082 | 0.698912 |
| 51 | 900013 | CLIENTE 013 | 3728370 | 0.00631057 | 0.705222 |
| 52 | 900076 | CLIENTE 076 | 3658925 | 0.00619303 | 0.711415 |
| 53 | 900123 | CLIENTE 123 | 3636600 | 0.00615525 | 0.71757 |
| 54 | 900040 | CLIENTE 040 | 3523170 | 0.00596326 | 0.723534 |
| 55 | 900067 | CLIENTE 067 | 3487925 | 0.0059036 | 0.729437 |
| 56 | 900135 | CLIENTE 135 | 3486975 | 0.00590199 | 0.735339 |
| 57 | 900085 | CLIENTE 085 | 3440520 | 0.00582336 | 0.741163 |
| 58 | 900079 | CLIENTE 079 | 3203120 | 0.00542154 | 0.746584 |
| 59 | 900064 | CLIENTE 064 | 3014920 | 0.005103 | 0.751687 |
| 60 | 900053 | CLIENTE 053 | 2981100 | 0.00504576 | 0.756733 |
| 61 | 900069 | CLIENTE 069 | 2979960 | 0.00504383 | 0.761777 |
| 62 | 900086 | CLIENTE 086 | 2895600 | 0.00490104 | 0.766678 |
| 63 | 900002 | CLIENTE 002 | 2853990 | 0.00483061 | 0.771508 |

> **Hoja larga:** arriba se muestran 60 de 168 filas con datos. **Todos los valores de la hoja están en [`Datos Thyms Completo-datos/Clientes.csv`](./Datos%20Thyms%20Completo-datos/Clientes.csv)** (CSV, UTF-8).

**Fórmulas (8 patrones distintos):**

- `C4`: `=COUNTA(A11:A171)`
- `C5`: `=SUM(C11:C171)`
- `C6`: `=C11/C5`
- `C7`: `=SUM(C11:C20)/C5`
- `C8`: `=SUM(C11:INDEX(C11:C171,ROUND(0.2*C4,0)))/C5`
- `C11`: `=SUMIF('Facturas Mayo-Julio'!$C$5:$C$468,A11,'Facturas Mayo-Julio'!$E$5:$E$468)`
- `D11`: `=C11/$C$5`
- `E11`: `=SUM($D$11:D11)`

### Hoja `Ventas` — 28 filas × 7 columnas

| Fila | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| 1 | Ventas 2026 y estacionalidad observada |  |  |  |  |  |  |
| 4 | Mes | Ventas UNIFICADO (COP) | Índice estacional (promedio ene-ago = 1) | Ventas según facturas (COP) | Facturas (#) | Ticket promedio (COP) | Diferencia facturas - UNIFICADO (COP) |
| 5 | Enero | 95752306 | 0.634131 | — | — | — | — |
| 6 | Febrero | 153850391 | 1.01889 | — | — | — | — |
| 7 | Marzo | 201004440 | 1.33118 | — | — | — | — |
| 8 | Abril | 52446770 | 0.347335 | — | — | — | — |
| 9 | Mayo | 197484330 | 1.30786 | 198232170 | 165 | 1.20141e+06 | 747840 |
| 10 | Junio | 156580280 | 1.03697 | 159703880 | 135 | 1.18299e+06 | 3123600 |
| 11 | Julio | 230979600 | 1.52969 | 232877145 | 164 | 1.41998e+06 | 1897545 |
| 12 | Agosto | 119882540 | 0.793937 | — | — | — | — |
| 13 | Septiembre | 0 | 1 | — | — | — | — |
| 14 | Octubre | 0 | 1 | — | — | — | — |
| 15 | Noviembre | 0 | 1 | — | — | — | — |
| 16 | Diciembre | 0 | 1 | — | — | — | — |
| 17 | Total | 1207980657 |  | 590813195 | 464 |  |  |
| 19 | Promedio mensual ene-ago (COP) | 1.50998e+08 |  |  |  |  |  |
| 20 | Mes de mayores ventas | Julio |  |  |  |  |  |
| 21 | Mes de menores ventas | Abril |  |  |  |  |  |
| 22 | Máximo / promedio (ene-ago) | 1.52969 |  |  |  |  |  |
| 23 | Mínimo / promedio (ene-ago) | 0.347335 |  |  |  |  |  |
| 24 | Coeficiente de variación mensual (ene-ago) | 0.394434 |  |  |  |  |  |

**Fórmulas (14 patrones distintos):**

- `C5`: `=B5/$B$19`
- `D9`: `=SUMIFS('Facturas Mayo-Julio'!$E$5:$E$468,'Facturas Mayo-Julio'!$A$5:$A$468,5)`
- `E9`: `=COUNTIFS('Facturas Mayo-Julio'!$A$5:$A$468,5)`
- `F9`: `=D9/E9`
- `G9`: `=D9-B9`
- `B17`: `=SUM(B5:B16)`
- `D17`: `=SUM(D9:D11)`
- `E17`: `=SUM(E9:E11)`
- `B19`: `=AVERAGE(B5:B12)`
- `B20`: `=INDEX(A5:A12,MATCH(MAX(B5:B12),B5:B12,0))`
- `B21`: `=INDEX(A5:A12,MATCH(MIN(B5:B12),B5:B12,0))`
- `B22`: `=MAX(B5:B12)/B19`
- `B23`: `=MIN(B5:B12)/B19`
- `B24`: `=STDEV(B5:B12)/B19`

