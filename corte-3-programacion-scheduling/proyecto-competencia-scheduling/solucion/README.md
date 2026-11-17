# Proyecto algoritmo: competencia de secuenciación

Dos algoritmos en Python (solo biblioteca estándar) para la competencia de Gradescope:

| Reto | Problema | Algoritmo | Calidad | Tiempo prom. |
|---|---|---|---|---|
| 01 Willy Wonka | F3 \| prmu, s_ij por tipo, N→R prohibido \| Cmax | Cota inferior + heurística (NEH, bloques por tipo, búsqueda local con Taillard) + método exacto propio (programación dinámica acotada) | **Óptimo demostrado** en 30/30 instancias de la plantilla y 200/200 de prueba | ~4 ms (máx. ~60 ms) |
| 02 Monstruópolis | P3 \| r_j, prec \| Σ w_j T_j | Reglas de despacho (WSPT, ATC, cadenas, EDD) + recocido simulado con evaluación incremental | ~0,05 % sobre el mejor valor conocido (corridas 150 veces más largas), 0 violaciones | ~80 ms |

## Qué hay en la carpeta

```
reto1.py                  Reto 1, formato del instructivo: solve(data) -> {"Cmax", "secuencia", "tiempo"}
reto2.py                  Reto 2, formato del instructivo: solve(data) -> [{"job","machine","start","end"}, ...]
gradescope/
  reto1_willy_wonka/reto_schedulling.py     Reto 1 en la plantilla del profesor (clase Schedulling)
  reto2_monstruopolis/reto_schedulling.py   Reto 2 en la plantilla del profesor (clase Schedulling)
construir_plantillas.py   Regenera las dos plantillas a partir de reto1.py / reto2.py
pruebas/                  Solo para probar en local (NO se sube)
  probar_reto1.py         30 instancias de la plantilla (semilla 42), validación y comparación con el óptimo
  probar_reto2.py         30 instancias, validador independiente de factibilidad
  exacto_reto1.py         Segundo método exacto, implementado aparte, para verificar el Reto 1
  cota_reto2.py           Cota inferior lagrangiana (numpy) para medir qué tan cerca del óptimo queda el Reto 2
  generador.py            Imitación local del módulo `generador` de Gradescope (Reto 2)
  data_ejemplo_reto1.json Datos del enunciado de Willy Wonka (tablas 1 a 4)
  data_ejemplo_reto2.json Instancia de ejemplo en formato de filas (Trabajo, p_j, r_j, d_j, w_j, Predecesores)
  data_ejemplo_reto2_plantilla.json  La misma instancia en el formato de la plantilla (jobs, p, r, d, w, preds)
```

## Qué subir a Gradescope

Hay dos formatos y no está claro cuál pide el autograder:

- **Instructivo PDF**: `reto1.py` y `reto2.py` con la función `solve(data)` (lee `data.json`).
- **Plantillas .py del profesor**: un archivo `reto_schedulling.py` por reto, con la clase `Schedulling` y `resolver_instancia()`.

Subir el que pida la tarea de Gradescope. Si piden `reto_schedulling.py`, usar el de la carpeta `gradescope/` del reto correspondiente. Ambos formatos usan exactamente el mismo algoritmo.

## Cómo probar en local

Desde esta carpeta:

```
python reto1.py pruebas/data_ejemplo_reto1.json
python reto2.py pruebas/data_ejemplo_reto2.json
python pruebas/probar_reto1.py --exacto
python pruebas/probar_reto2.py
python pruebas/probar_reto2.py --holgura 0.5      (fechas de entrega más sueltas)
```

Si cambian `reto1.py` o `reto2.py`, correr `python construir_plantillas.py` para actualizar las plantillas.

## Calidad contra tiempo (parámetros al inicio de cada archivo)

El 30 % de la nota es tiempo de cómputo, por eso los parámetros están en el punto donde subir el tiempo casi no mejora la calidad. Si en Gradescope se ve que el tiempo pesa menos (o más) de lo esperado, se pueden mover:

**Reto 1** (`EXACTO_R1`, 200 instancias del generador de la plantilla):

| Configuración | Óptimas | Tiempo prom. (máx.) |
|---|---|---|
| **`EXACTO_R1 = True` (por defecto)** | 200/200, **demostradas** | ~4 ms (~60 ms) |
| `EXACTO_R1 = False` (solo heurística + Iterated Greedy) | 197/200, sin demostrar | ~2 ms (~9 ms) |

**Reto 2** (`ITER_SA_R2`, 30 instancias, brecha contra corridas largas):

| Iteraciones | Brecha (d_j ajustado) | Brecha (d_j holgado) | Tiempo |
|---|---|---|---|
| 0 (solo reglas de despacho) | 2,9 % | 18,6 % | ~2 ms |
| 5 000 | 0,17 % | 2,7 % | ~40 ms |
| **10 000 (por defecto)** | 0,05 % | 1,8 % | ~80 ms |
| 20 000 | 0,04 % | 0,7 % | ~150 ms |

## ¿Es el óptimo?

- **Reto 1: sí, demostrado.** El algoritmo termina con una prueba: o la solución iguala la cota inferior, o el método exacto revisa (podando con la cota) todas las secuencias que podrían ser mejores y no queda ninguna. Se comprobó además contra un segundo exacto implementado aparte (200/200 iguales) y en 400 instancias más difíciles que las de la plantilla (todas demostradas, peor caso ~0,3 s).
- **Reto 2: no se puede demostrar en tiempo de competencia** (50 trabajos, problema NP-difícil; un exacto en Python no terminaría). Evidencia de que estamos muy cerca: corridas 150 veces más largas solo mejoran 0,05 % en promedio, y la cota inferior lagrangiana (`pruebas/cota_reto2.py`) deja como máximo 2,4 % de brecha. Esa brecha viene sobre todo de que la cota es floja: con más iteraciones ya no sube.

Todo lo que va en la entrega usa solo la biblioteca estándar de Python, como pide el instructivo. numpy solo se usa en `pruebas/`.

Los algoritmos usan su propia semilla (`random.Random(SEMILLA)`): los resultados son reproducibles y no alteran el `random` global con el que la plantilla genera las instancias.

## Cosas a revisar antes de entregar

1. **La función `calcular_makespan_penalizado` de la plantilla del Reto 1 tiene un error.** Para buscar el tipo del lote anterior recorre toda la secuencia y toma el último lote con `fin_lote <= fin_maquina`; como los lotes aún no procesados tienen `fin_lote = 0`, casi siempre termina tomando el tipo del **último lote de la secuencia**, no el del lote anterior. Por eso da valores de 650 a 1 000 cuando el Cmax real está entre 560 y 680. Nuestro algoritmo optimiza el Cmax real (el del enunciado). Conviene preguntarle al profesor con qué función califica Gradescope; `pruebas/probar_reto1.py` muestra ambos valores (columna `plantilla`).
2. **Supuesto de alistamientos (Reto 1):** igual que en esa función de la plantilla, el alistamiento empieza cuando la máquina está libre y el lote ya llegó: `inicio = max(fin máquina, fin del lote en la máquina anterior) + alistamiento`. El primer lote no tiene alistamiento.
3. **La plantilla del Reto 1 importa `from optimizador import load_from_dict, run_ga`**, que es el ejemplo del profesor y no viene con la plantilla. Se dejó dentro de un `try/except ImportError` para que no falle si ese módulo no existe en Gradescope.
4. **Reto 2:** el módulo `generador` real está en Gradescope; el de `pruebas/` lo imita según el enunciado (d_j = tiempo mínimo teórico de finalización). Si en Gradescope los d_j resultan más holgados, el algoritmo sigue siendo factible pero queda más lejos del mejor conocido (~1,8 %); en ese caso conviene subir `ITER_SA_R2` a 20 000 (probar con `python pruebas/probar_reto2.py --holgura 0.5`).
5. **La plantilla del Reto 2 trae un ciclo que corre hasta `timelimit - 1` (29 s).** Lo reemplazamos por el recocido, que termina en ~80 ms, porque el tiempo cuenta en la nota. El tope de seguridad sigue siendo `min(5 s, timelimit - 1)`.
