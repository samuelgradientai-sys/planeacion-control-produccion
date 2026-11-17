# Guía del paquete «corte-1-completo»

Este paquete contiene **todo el material del Corte 1: Pronósticos de demanda**: el README de cada tema; el resumen y el contenido completo, página por página, de cada presentación; la explicación de cada Excel; los cuadernos, documentos Word y código. Solo se omitieron los anexos automáticos (repiten el contenido) y los CSV de datos largos, que están en el repositorio.

**Repositorio completo** (archivos originales PDF/Excel, anexos con todas las celdas y CSV de datos): https://github.com/samuelgradientai-sys/planeacion-control-produccion

## Archivos de este paquete

- `00-README-del-corte.md`: temas del corte en orden de clase.
- `01-introduccion-curso-y-sistemas-de-produccion.md`: todo el contenido de la carpeta `corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/`.
- `02-introduccion-a-pronosticos.md`: todo el contenido de la carpeta `corte-1-pronosticos/02-introduccion-a-pronosticos/`.
- `03-graficas-y-autocorrelacion.md`: todo el contenido de la carpeta `corte-1-pronosticos/03-graficas-y-autocorrelacion/`.
- `04-datos-estacionarios-promedio-movil-y-suavizacion-simple.md`: todo el contenido de la carpeta `corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/`.
- `05-tendencia-suavizacion-doble-holt.md`: todo el contenido de la carpeta `corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/`.
- `06-estacionalidad-winters-y-tracking-signal.md`: todo el contenido de la carpeta `corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/`.
- `07-arima.md`: todo el contenido de la carpeta `corte-1-pronosticos/07-arima/`.
- `08-metodos-cualitativos.md`: todo el contenido de la carpeta `corte-1-pronosticos/08-metodos-cualitativos/`.
- `parcial-1.md`: todo el contenido de la carpeta `corte-1-pronosticos/parcial-1/`.
- `proyecto-thyms-pronostico.md`: todo el contenido de la carpeta `corte-1-pronosticos/proyecto-thyms-pronostico/`.
- `ERRATAS.md`: errores detectados en todo el material, con su corrección.

## Paquetes disponibles

- `claude-proyectos/corte-1-completo/`: Corte 1 con todo el detalle.
- `claude-proyectos/corte-2-completo/`: Corte 2 con todo el detalle.
- `claude-proyectos/corte-3-completo/`: Corte 3 con todo el detalle, código incluido.
- `claude-proyectos/curso-completo-resumido/`: los tres cortes en versión resumida.

En los paquetes, cada archivo original empieza con un comentario `<!-- fuente: ruta -->`. Los enlaces son rutas desde la raíz del repositorio: `/ruta/archivo.md` corresponde a `https://github.com/samuelgradientai-sys/planeacion-control-produccion/blob/main/ruta/archivo.md`.

---

# Guía general del repositorio (CLAUDE.md)

## Qué es

Este repositorio tiene **todo el material** del curso **Planeación, Programación y Control de la Producción** (en los nombres de archivo aparece como "PPCO"), de Ingeniería Industrial, VII semestre, Universidad de La Sabana (Chía, Colombia), semestre 2026-2. El profesor es William J. Guerrero.

Incluye:
- las presentaciones de clase (L01 a L19 y job shop);
- los Excel trabajados en clase;
- las tareas;
- los parciales;
- los proyectos del estudiante: THYMS en los Cortes 1 y 2, y la competencia de scheduling en el Corte 3.

El dueño del repositorio es el estudiante. Lo usa para estudiar, resolver ejercicios y avanzar sus proyectos con ayuda de Claude.

## Regla principal: lee los `.md`, no los binarios

Cada **PDF, Excel, Word y cuaderno** tiene al lado un `.md` con el **mismo nombre**: `L07-….pdf` tiene su `L07-….md`, y `metodo-winters.xlsx` tiene su `metodo-winters.md`. El `.md` contiene todo lo que hay en el archivo, así que no hace falta abrir el binario.

| Tipo | Secciones del `.md` |
|---|---|
| **PDF** (clases, enunciados, parciales) | `## Resumen`: tema, ideas clave, todas las fórmulas en LaTeX, ejemplos y páginas clave.<br>`## Contenido completo (página por página)`: transcripción fiel de cada diapositiva, con fórmulas, tablas con todos los números, gráficos y diagramas descritos y Gantt en tablas.<br>`## Anexo`: texto extraído automáticamente. |
| **Excel** | `## Explicación de los ejemplos`: enunciado, datos, parámetros, método paso a paso (las fórmulas de celda pasadas a notación matemática), resultados, gráficos y observaciones.<br>`## Anexo: volcado de celdas por hoja`: valores, **todas** las fórmulas y gráficos con sus rangos. |
| **Hojas largas de Excel** | CSV completos en la carpeta `<nombre>-datos/`, junto al `.md`. |
| **Cuaderno (.ipynb)** | `## Resumen` y `## Contenido del cuaderno`: todas las celdas con su código y sus salidas de texto. |
| **Word** | `## Resumen` y `## Texto completo`. |

Los archivos `.py`, `.gms`, `.lst`, `.csv`, `.json` y `.md` ya son texto: léelos directamente. El `README.md` de cada tema explica qué hacen.

Marcas que vas a encontrar en los `.md`:
- `[ilegible]`: el original no se lee.
- «deducido»: inferido, no está escrito en el original.
- «cálculo propio»: calculado durante la conversión; no está en el material.

## Cómo navegar

1. [`README.md`](/README.md): mapa general del curso.
2. `corte-N-…/README.md`: los temas del corte, en orden de clase.
3. `corte-N-…/<tema>/README.md`: qué hay en la carpeta, orden de estudio, fórmulas clave y ejercicios resueltos.
4. El `.md` de cada archivo, para el detalle.

Además:
- [`CATALOGO.md`](/CATALOGO.md): **todos** los archivos, con su ruta nueva, su nombre original en la carpeta del estudiante y una descripción.
- [`ERRATAS.md`](/ERRATAS.md): **errores conocidos** de diapositivas, Excel y código, con su corrección. **Revísalo antes de citar una cifra.**
- [`claude-proyectos/`](/claude-proyectos/README.md): **copias generadas** de este mismo material, empaquetadas para que quepan en un Proyecto de claude.ai (un paquete completo por corte y uno resumido de todo el curso).
  - Si estás leyendo el repositorio completo, ignora esa carpeta: repite lo que ya está en `corte-N-…/`.
  - Se regenera con [`herramientas/generar_paquetes_claude.py`](/herramientas/generar_paquetes_claude.py).

## Dónde buscar

| Si preguntan por… | Ve a |
|---|---|
| Evaluación, porcentajes, reglas, programa del curso | [`corte-1-pronosticos/01-…/L01-introduccion-al-curso.md`](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L01-introduccion-al-curso.md) |
| WIP, takt, throughput, push/pull, Kanban | [`corte-1-pronosticos/01-…/L02`](/corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/L02-introduction-to-production-systems.md) |
| Autocorrelación, correlograma, Ljung-Box | [`corte-1-pronosticos/03-graficas-y-autocorrelacion/`](/corte-1-pronosticos/03-graficas-y-autocorrelacion/README.md) |
| Promedio móvil, SES, MAD/MSE/MAPE | [`corte-1-pronosticos/04-…/`](/corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/README.md) |
| Holt | [`corte-1-pronosticos/05-…/`](/corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/README.md) |
| Winters, señal de rastreo | [`corte-1-pronosticos/06-…/`](/corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/README.md) |
| ARIMA | [`corte-1-pronosticos/07-arima/`](/corte-1-pronosticos/07-arima/README.md) |
| Métodos cualitativos (Delphi…) | [`corte-1-pronosticos/08-metodos-cualitativos/`](/corte-1-pronosticos/08-metodos-cualitativos/README.md) |
| Planeación agregada, Bowman, PL de flujo (GAMS) | [`corte-2-…/01-planeacion-agregada-modelo-bowman/`](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/README.md) |
| Desagregación, tiempo de agotamiento | [`corte-2-…/02-agregacion-y-desagregacion/`](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/README.md) |
| Tamaño de lote: Wagner-Whitin, Silver-Meal | [`corte-2-…/03-wagner-whitin-y-silver-meal/`](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/README.md) |
| BOM, explosión de materiales, tabla MRP | [`corte-2-…/04-bom-y-mrp/`](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/README.md) |
| MRP II, RCCP, CRP, backward scheduling | [`corte-2-…/05-mrp-ii-y-capacidad/`](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/README.md) |
| Notación α\|β\|γ, métricas de scheduling | [`corte-3-…/01-introduccion-scheduling/`](/corte-3-programacion-scheduling/01-introduccion-scheduling/README.md) |
| Una máquina: SPT, EDD, WSPT, ATC, Lawler, Moore | [`corte-3-…/02-una-maquina/`](/corte-3-programacion-scheduling/02-una-maquina/README.md) |
| Máquinas paralelas: LPT, LNS, LFJ | [`corte-3-…/03-maquinas-paralelas/`](/corte-3-programacion-scheduling/03-maquinas-paralelas/README.md) |
| Flow shop: Johnson, CDS, NEH | [`corte-3-…/04-flow-shop/`](/corte-3-programacion-scheduling/04-flow-shop/README.md) |
| Job shop, shifting bottleneck | [`corte-3-…/05-job-shop/`](/corte-3-programacion-scheduling/05-job-shop/README.md) |
| Resumen de todos los métodos de scheduling | [`corte-3-…/00-compendio-metodos-scheduling/`](/corte-3-programacion-scheduling/00-compendio-metodos-scheduling/README.md) |
| Parciales resueltos | [`corte-1-…/parcial-1/`](/corte-1-pronosticos/parcial-1/README.md), [`corte-2-…/parcial-2/`](/corte-2-planeacion-agregada-mrp/parcial-2/README.md) |
| Proyecto THYMS | [Corte 1: pronóstico](/corte-1-pronosticos/proyecto-thyms-pronostico/README.md) → [Corte 2: gemelo digital](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/README.md) (traspaso: [`CONTEXTO_GEMELO_THYMS.md`](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/CONTEXTO_GEMELO_THYMS.md)) |
| Competencia de scheduling (Gradescope) | [`corte-3-…/proyecto-competencia-scheduling/`](/corte-3-programacion-scheduling/proyecto-competencia-scheduling/README.md) |

## Contexto de los proyectos

### THYMS Colombia S.A.S. (Cortes 1 y 2)
- **Empresa:** tintes para el cabello en tubo de 60 g, productos A, B y C.
- **Corte 1:** pronóstico de las ventas reales de un vendedor de la zona Antioquia con SES (α = 0,05), a 12.900 COP por unidad.
- **Corte 2:** estudio preliminar (takt, throughput, WIP, restricciones), S&OP y plan agregado, y gemelo digital en Python/SimPy con sensores virtuales.
- **Supuestos que el grupo aún debe confirmar con la empresa:**
  - la escala zona → planta (la serie real equivale a ≈ 11,7 % de la planta);
  - la jornada (1 turno de 8 h L-S en el Corte 1, frente a 2 turnos de 7 h L-V en el libro de datos);
  - los índices estacionales de septiembre a diciembre (= 1);
  - los pedidos de materia prima en tránsito.

### Competencia de scheduling (Corte 3)
- **Retos:**
  - Reto 1, Willy Wonka: $F3\,|\,prmu, s_{ij}\,|\,C_{max}$, con alistamientos por tipo y la transición N→R prohibida.
  - Reto 2, Monstruópolis: $P3\,|\,r_j, prec\,|\,\sum w_jT_j$.
- **Calificación:** calidad 60 %, tiempo de cómputo 30 % e informe 10 %.
- **Restricción del estudiante:** solo usa métodos dentro del alcance del curso; nada de solvers externos ni OR-Tools, ni siquiera para verificar.
- **Primera entrega del Reto 1 en Gradescope:** «616.7667 / 100.0», que es el Cmax promedio óptimo de las 30 instancias de la plantilla con semilla 42.
- **Dudas abiertas:**
  - si Gradescope pide `solve()` o la clase `Schedulling`;
  - con qué función califica, porque la de la plantilla tiene un error;
  - la fórmula exacta del puntaje de tiempo.

## Convenciones

- **Lecciones:** L01 a L19 en orden de clase; `job-shop-y-flexible-job-shop` no tiene número y va después de L19.
- **Idioma:** las diapositivas se transcribieron en su idioma original (casi siempre inglés); resúmenes y explicaciones están en español.
- **Notación de pronósticos:**
  - $D_t$ o $A_t$: demanda real;
  - $F_t$: pronóstico;
  - $\alpha, \beta, \gamma$: constantes de suavización;
  - $S_t$ y $G_t$: nivel y tendencia en Holt;
  - $c_t$: factor estacional.
- **Notación de scheduling:** de Graham, $\alpha\,|\,\beta\,|\,\gamma$; $p_j, r_j, d_j, w_j, C_j, L_j, T_j, U_j$.
- **Moneda:** COP en el proyecto THYMS; los ejemplos de clase usan dólares o unidades genéricas.
- **Datos de clientes de THYMS anonimizados:** `CLIENTE ###`, códigos `9#####` y `VENDEDOR 401`. Las cifras de ventas son las reales.

## Al responder

- Cita el archivo y la página o celda (p. ej. «L07 p. 21» o «`metodo-winters.xlsx`, celda P16»).
- Si un número del material está en [`ERRATAS.md`](/ERRATAS.md), usa el valor corregido y avisa del error.
- No inventes datos que no estén en el material. Si algo no está, dilo; por ejemplo, la presentación del Corte 2 cita resultados de Bowman y de un MILP que no están en ningún archivo.
- Los archivos originales se conservan sin cambios (salvo la anonimización), así que una fórmula se puede verificar en el `.xlsx`.
