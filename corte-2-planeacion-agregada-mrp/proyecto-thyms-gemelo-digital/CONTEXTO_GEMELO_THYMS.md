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
