# Planeación, Programación y Control de la Producción

Material completo del curso de **Ingeniería Industrial, VII semestre, Universidad de La Sabana, 2026-2** (prof. William J. Guerrero), organizado por **corte** y, dentro de cada corte, por **tema**. Contiene presentaciones de clase, ejercicios en Excel, código, tareas, parciales resueltos y los proyectos del semestre.

Cada archivo está en su formato original y además en **Markdown**, para poder leerlo, buscarlo y entenderlo sin abrir el PDF o el Excel. El repositorio está pensado para usarse con Claude: la guía para la IA está en **[`CLAUDE.md`](CLAUDE.md)**.

## Mapa del curso

### [Corte 1: Pronósticos de demanda](corte-1-pronosticos/README.md) (30 %)
| Tema | Clase |
|---|---|
| [01 · Introducción al curso y sistemas de producción](corte-1-pronosticos/01-introduccion-curso-y-sistemas-de-produccion/README.md) | L01, L02 |
| [02 · Introducción a pronósticos](corte-1-pronosticos/02-introduccion-a-pronosticos/README.md) | L03 |
| [03 · Gráficas y autocorrelación](corte-1-pronosticos/03-graficas-y-autocorrelacion/README.md) | L04 |
| [04 · Datos estacionarios: promedio móvil y suavización simple](corte-1-pronosticos/04-datos-estacionarios-promedio-movil-y-suavizacion-simple/README.md) | L05 |
| [05 · Tendencia: suavización doble (Holt)](corte-1-pronosticos/05-tendencia-suavizacion-doble-holt/README.md) | L06 |
| [06 · Estacionalidad: Winters y señal de rastreo](corte-1-pronosticos/06-estacionalidad-winters-y-tracking-signal/README.md) | L07 |
| [07 · ARIMA](corte-1-pronosticos/07-arima/README.md) | L08 |
| [08 · Métodos cualitativos](corte-1-pronosticos/08-metodos-cualitativos/README.md) | L09 |
| [Parcial 1](corte-1-pronosticos/parcial-1/README.md) · [Proyecto THYMS: pronóstico](corte-1-pronosticos/proyecto-thyms-pronostico/README.md) | |

### [Corte 2: Planeación agregada, tamaño de lote y MRP](corte-2-planeacion-agregada-mrp/README.md) (30 %)
| Tema | Clase |
|---|---|
| [01 · Planeación agregada y modelo de Bowman](corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/README.md) | L10 |
| [02 · Agregación y desagregación](corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/README.md) | L11 |
| [03 · Wagner-Whitin y Silver-Meal](corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/README.md) | L12 |
| [04 · BOM y MRP](corte-2-planeacion-agregada-mrp/04-bom-y-mrp/README.md) | L13, L14 |
| [05 · MRP II y planeación de capacidad](corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/README.md) | L15 |
| [Parcial 2](corte-2-planeacion-agregada-mrp/parcial-2/README.md) · [Proyecto THYMS: S&OP y gemelo digital](corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/README.md) | |

### [Corte 3: Programación de la producción (scheduling)](corte-3-programacion-scheduling/README.md) (40 %)
| Tema | Clase |
|---|---|
| [00 · Compendio de métodos de scheduling](corte-3-programacion-scheduling/00-compendio-metodos-scheduling/README.md) | Excel resumen |
| [01 · Introducción a scheduling](corte-3-programacion-scheduling/01-introduccion-scheduling/README.md) | L16 |
| [02 · Una máquina](corte-3-programacion-scheduling/02-una-maquina/README.md) | L17 |
| [03 · Máquinas paralelas](corte-3-programacion-scheduling/03-maquinas-paralelas/README.md) | L18 |
| [04 · Flow shop](corte-3-programacion-scheduling/04-flow-shop/README.md) | L19 |
| [05 · Job shop](corte-3-programacion-scheduling/05-job-shop/README.md) | Job shop |
| [Proyecto: competencia de scheduling (Willy Wonka y Monstruópolis)](corte-3-programacion-scheduling/proyecto-competencia-scheduling/README.md) · [Otros archivos](corte-3-programacion-scheduling/otros-archivos/README.md) | |

## Usarlo en un Proyecto de claude.ai

Un Proyecto tiene un límite de tamaño y el repositorio completo no cabe (ocupa unas 5 veces el límite). Por eso existe la carpeta **[`claude-proyectos/`](claude-proyectos/README.md)**, con paquetes que sí caben. En «Añadir contenido desde GitHub», desmarca todo y marca **solo una** de estas carpetas:

| Carpeta | Qué contiene | Uso aprox. |
|---|---|---|
| `claude-proyectos/corte-1-completo/` | Corte 1 con todo el detalle | ~62 % |
| `claude-proyectos/corte-2-completo/` | Corte 2 con todo el detalle | ~73 % |
| `claude-proyectos/corte-3-completo/` | Corte 3 con todo el detalle, código incluido | ~67 % |
| `claude-proyectos/curso-completo-resumido/` | Los tres cortes resumidos: índices, fórmulas, ejemplos, erratas | ~68 % |

Para tener todo el detalle, crea un Proyecto por corte. Para un solo Proyecto, usa el resumido.

## Cómo está organizado

```
README.md      ← este mapa
CLAUDE.md      ← guía para la IA: cómo leer el repo y dónde buscar cada cosa
CATALOGO.md    ← todos los archivos: ruta nueva, nombre original y descripción
ERRATAS.md     ← errores detectados en diapositivas, Excel y código, con su corrección
claude-proyectos/  ← paquetes generados para Proyectos de claude.ai (no editar a mano)
herramientas/      ← script que genera esos paquetes
corte-N-…/
  README.md            ← temas del corte en orden de clase
  NN-tema/
    README.md          ← qué cubre, archivos, orden de estudio, fórmulas clave, ejercicios
    L##-clase.pdf  +  L##-clase.md        ← presentación + conversión completa
    ejercicio.xlsx +  ejercicio.md        ← Excel + explicación de sus ejemplos
    ejercicio-datos/*.csv                 ← hojas largas completas (si las hay)
```

- **PDF → `.md`**: resumen con todas las fórmulas en LaTeX y transcripción página por página, con tablas, ejemplos numéricos, gráficos y diagramas descritos.
- **Excel → `.md`**: explicación de cada ejemplo (datos, método paso a paso, resultados) y volcado de valores, fórmulas y gráficos.
- **Cuadernos y Word → `.md`**: resumen y contenido completo.

## Notas

- **No se omitió ningún material.** Todo lo que había en las carpetas `CORTE 1`, `CORTE 2` y `CORTE 3` está aquí. Solo quedaron fuera dos copias exactas, cuyo contenido ya está en el repo; ver [`CATALOGO.md`](CATALOGO.md).
- Algunos archivos estaban en la carpeta de otro corte: cuatro Excel de temas del Corte 2 que estaban en `CORTE 3/`. Se ubicaron en su tema. El Excel de otra materia (Gerencia Financiera) que estaba en `CORTE 3/` quedó en [`otros-archivos/`](corte-3-programacion-scheduling/otros-archivos/README.md).
- Los nombres, documentos de identidad y códigos de **clientes de THYMS están anonimizados** (`CLIENTE ###`). Las cifras de ventas no se modificaron.
