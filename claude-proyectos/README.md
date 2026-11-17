# Paquetes para Proyectos de claude.ai

Un Proyecto de claude.ai tiene un límite de tamaño (≈ su ventana de contexto). El repositorio completo ocupa unas 5 veces ese límite: sus PDF, Excel, CSV y anexos repiten mucho contenido. Estas carpetas se **generan automáticamente** con [`herramientas/generar_paquetes_claude.py`](https://github.com/samuelgradientai-sys/planeacion-control-produccion/blob/main/herramientas/generar_paquetes_claude.py) y caben en un Proyecto.

| Carpeta | Tamaño (caracteres) | Uso estimado de un Proyecto |
|---|---|---|
| `corte-1-completo/` | 470 mil | ≈ 62 % |
| `corte-2-completo/` | 557 mil | ≈ 73 % |
| `corte-3-completo/` | 510 mil | ≈ 67 % |
| `curso-completo-resumido/` | 517 mil | ≈ 68 % |

El porcentaje es una estimación; el diálogo «Añadir contenido desde GitHub» muestra el valor real.

## Cómo usarlos

En el Proyecto: **Añadir contenido desde GitHub** → repositorio `planeacion-control-produccion` → desmarca todo → marca **solo una** de estas carpetas.

- **Opción A, un Proyecto por corte, con todo el detalle:** crea tres Proyectos (Corte 1, Corte 2, Corte 3) y carga en cada uno su carpeta `corte-N-completo/`.
- **Opción B, un solo Proyecto con todo el curso resumido:** carga `curso-completo-resumido/`.

Los tres paquetes completos juntos no caben en un solo Proyecto. Puedes combinar `curso-completo-resumido/` con el paquete completo de **un** corte si el diálogo lo permite (ver el porcentaje).

No edites estos archivos a mano. Si cambia el material, vuelve a correr `python -I herramientas/generar_paquetes_claude.py .` desde la raíz del repositorio.
