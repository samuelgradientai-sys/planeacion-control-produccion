# instructivo-competencia-scheduling

> **Archivo:** [`instructivo-competencia-scheduling.pdf`](./instructivo-competencia-scheduling.pdf) · **Corte 3** · 4 páginas  
> **Nombre original:** `CORTE 3/PROYECTO 3/Instructivo_Competencia_Scheduling (1).pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** reglas generales de la competencia de secuenciación del Corte 3: dos retos de scheduling programados en Python y calificados automáticamente en Gradescope.

**Ideas clave**

- Se trabaja en grupos de exactamente 5 estudiantes; un solo integrante sube la entrega a Gradescope.
- Hay dos retos:
  - **Reto 01, Willy Wonka:** flow shop de 3 máquinas en serie con 15 lotes, alistamiento dependiente del tipo y prohibición de que un lote R vaya justo después de uno N. Objetivo: minimizar $C_{\max}$.
  - **Reto 02, Monstruópolis:** 3 máquinas idénticas en paralelo con 50 trabajos, fechas de liberación $r_j$, fechas de entrega $d_j$, unas 5 precedencias y sin interrupciones. Objetivo: minimizar $\sum w_jT_j$.
- **La nota** se reparte así: 60 % calidad del objetivo, 30 % tiempo de cómputo y 10 % reporte técnico (PDF de máximo 4 páginas).
- **El ranking** se calcula con el valor promedio del objetivo sobre varias instancias generadas automáticamente. El mejor equipo recibe 100 puntos y los demás se escalan en proporción.
- **Las infactibilidades** no dan cero, pero suman una penalidad proporcional al número de violaciones antes de normalizar. Una solución infactible nunca debe superar a una factible.
- **Restricciones de entrega:**
  - límite de 60 s por instancia (si se pasa, recibe el peor puntaje en esa instancia);
  - solo biblioteca estándar de Python y numpy; nada de OR-Tools, PuLP, Gurobi ni similares;
  - no se aceptan notebooks ni ZIP;
  - se permiten varias entregas y cuenta la última;
  - el código debe ser propio.
- **Formato pedido por el instructivo:** archivos `reto1.py` y `reto2.py` con una función `solve(data)` que lee `data.json`.
  - El Reto 01 devuelve `{"Cmax", "secuencia", "tiempo"}`.
  - El Reto 02 devuelve una lista de `{"job", "machine", "start", "end"}`; Gradescope calcula $C_j$ y $\sum w_jT_j$.
- **Recomendaciones del profesor:**
  - Reto 01: NEH, búsqueda local (2-opt, inserción) o recocido simulado, verificando N→R antes de calcular el $C_{\max}$.
  - Reto 02: reglas de despacho (WSPT, EDD ponderado), revisando en cada decisión qué trabajos ya tienen sus predecesores terminados.
  - Consejo general: empezar con una solución factible simple y luego mejorar; «un algoritmo rápido con solución aceptable suele ganarle a uno lento con solución teóricamente perfecta».

**Fórmulas y métodos**

- **Reto 01:** $C_{\max}=\max_j C_{j,M3}$, el instante en que el último lote sale de M3.
- **Reto 02:** $\sum_j w_jT_j$, con $T_j=\max(0,\,C_j-d_j)$, donde $w_j$ es el peso, $C_j$ el tiempo de terminación y $d_j$ la fecha de entrega.
- **Puntaje de calidad deducido de la descripción** (no hay fórmula explícita): $\text{puntaje}_e=100\cdot\dfrac{\bar z_{\text{mejor}}}{\bar z_e}$, con $\bar z_e$ el objetivo promedio del equipo $e$ más sus penalidades. No se dice cómo se puntúa el tiempo.
- **Métodos sugeridos:** NEH, búsqueda local 2-opt e inserción, simulated annealing, WSPT ($w_j/p_j$ decreciente) y EDD ponderado.

**Ejemplos resueltos:** no hay; solo ejemplos de formato. Para el Reto 01: `"Cmax": 847`, `"tiempo": 12`. Para el Reto 02: J1 en M1 de 0 a 45 y J2 en M2 de 10 a 35.

**Páginas clave**

| Página | Contenido |
|---|---|
| 1 | Los dos retos |
| 2 | Criterios, penalización, ranking, reporte y formatos de salida |
| 3 | Plantilla `solve()`, reglas y recomendación del Reto 01 |
| 4 | Recomendación del Reto 02 y consejo general |

**Relación con otros archivos del repo**

- Enunciados detallados: [reto-1-willy-wonka.md](./reto-1-willy-wonka.md) y [reto-2-monstruopolis.md](./reto-2-monstruopolis.md).
- **Plantillas del profesor:** [plantilla-reto-1-willy-wonka/reto_schedulling.py](./plantilla-reto-1-willy-wonka/reto_schedulling.py) y [plantilla-reto-2-monstruopolis/reto_schedulling.py](./plantilla-reto-2-monstruopolis/reto_schedulling.py). Usan **otro formato**, la clase `Schedulling` con `resolver_instancia()`, distinto del `solve()` de este instructivo; ver el [README del proyecto](../README.md).
- Solución del estudiante: [solucion/README.md](../solucion/README.md) e [INFORME_TECNICO.md](../solucion/INFORME_TECNICO.md).
- Teoría:
  - [L19 Flow shop](../../04-flow-shop/L19-flow-shop-scheduling.md), para el Reto 01;
  - [L18 Máquinas paralelas](../../03-maquinas-paralelas/L18-parallel-machine-scheduling.md), para el Reto 02;
  - [L17 Una máquina](../../02-una-maquina/L17-single-machine-scheduling.md), con WSPT, EDD y ATC.

**Observaciones**

- **El instructivo y las plantillas no coinciden en formato.** El instructivo pide `reto1.py`/`reto2.py` con `solve()`. Las plantillas `.py` del profesor piden un archivo `reto_schedulling.py` con la clase `Schedulling`, que además importa `pandas` aunque el instructivo solo permite la biblioteca estándar y numpy.
- Los ejemplos de salida usan comentarios `//`, que no son JSON válido; son solo ilustrativos.
- No se especifica cómo se convierte el tiempo de cómputo en el 30 % de la nota.

## Contenido completo (página por página)

> Documento de 4 páginas con diseño de página web impresa (encabezado oscuro, tarjetas de colores). El texto se transcribe tal cual, incluidas las palabras sin tilde del original («solucion», «tecnico», «estandar»…).

### Página 1 — Competencia de Secuenciación de Máquinas: presentación y los dos retos

**PLANEACIÓN, PROGRAMACIÓN Y CONTROL DE LAS OPERACIONES**

**Competencia de Secuenciación de Máquinas** (título principal)

Universidad de La Sabana — Facultad de Ingeniería Industrial

> [Franja de tres etiquetas de color: **Grupos de 5 estudiantes** · **2 retos de programación** · **Entrega por Gradescope**]

**¿De qué se trata la competencia?**

Cada grupo debe programar **dos algoritmos de secuenciación** en Python para resolver dos problemas clásicos de scheduling. Los algoritmos se evalúan automáticamente en **Gradescope**: el sistema prueba su código con varias instancias del problema y mide qué tan buena es la solución y qué tan rápido la encuentran. Gana el equipo que mejor combine calidad de solución y velocidad de cómputo.

**Los dos retos** (dos tarjetas lado a lado)

| | RETO 01 | RETO 02 |
|---|---|---|
| Nombre | **Fábrica de Willy Wonka** — Flow Shop con tiempos de alistamiento | **Fábrica de Monstruópolis** — Máquinas paralelas con precedencias |
| Tipo | Flow Shop de 3 máquinas en serie (M1 → M2 → M3). | 3 máquinas idénticas en paralelo (P3 \| rj, prec \| ∑WjTj). |
| Objetivo | Minimizar el Cmax (tiempo en que termina el último lote). | Minimizar la tardanza ponderada total (∑wjTj). |
| Restricciones | · Un lote Relleno (R) no puede ir inmediatamente después de un lote Nueces (N) en ninguna máquina. · Cada cambio de tipo genera un tiempo de alistamiento diferente por máquina. | · Cada trabajo tiene fecha de liberación (rj) y de entrega (dj). · Algunos trabajos tienen precedencias (i → j). No se permite interrumpir trabajos (no preemption). |
| Pie de la tarjeta | `15 lotes \| 3 máquinas en serie \| setup dependiente del tipo` | `50 trabajos \| 3 máquinas paralelas \| ~5 precedencias` |

**Criterios de evaluación y puntaje** *(el contenido sigue en la página 2)*

### Página 2 — Criterios de evaluación, penalizaciones, comparación entre equipos y formatos de entrega

> [Franja de tres bloques de color con los pesos de la nota]

| Peso | Criterio |
|---|---|
| **60 %** | Calidad de la solución (valor del objetivo obtenido) |
| **30 %** | Tiempo computacional (velocidad del algoritmo) |
| **10 %** | Reporte técnico (de los algoritmos presentados) |

**Penalizacion por restricciones violadas**

Una solucion que incumpla alguna restriccion **no recibe puntaje cero automaticamente**, pero si tendra una **penalizacion directa sobre el valor de la funcion objetivo**: se sumara una penalidad proporcional al numero de violaciones detectadas, lo que deteriorara significativamente su posicion en el ranking.

El objetivo es incentivar soluciones factibles. Una solucion infactible con buen tiempo computacional **nunca superara a una solucion factible bien construida**.

**Como se compara la calidad entre equipos**

Gradescope prueba cada algoritmo con varias instancias generadas automaticamente. El equipo con el menor valor del objetivo (Cmax en Reto 01 o ∑wjTj en Reto 02) en promedio obtiene el mayor puntaje. El ranking se normaliza: el mejor equipo obtiene 100 puntos, los demas se escalan proporcionalmente. Las penalizaciones por violaciones se suman al valor objetivo **antes** de este calculo.

**Reporte tecnico (10%):** Documento PDF de maximo 4 paginas que describe los algoritmos implementados: tipo de heuristica o metaheuristica usada, justificacion de la eleccion, analisis de resultados sobre las instancias de prueba y lecciones aprendidas. Se entrega junto con el codigo en Gradescope.

**Formatos de entrega**

**Reto 01 — Willy Wonka: salida en JSON exactamente asi:**

```
{
"Cmax": 847, // minuto en que termina el ultimo lote
"secuencia": ["L1", "L4", ..., "L15"],
"tiempo": 12 // ms que tardo el algoritmo
}
```

**Reto 02 — Monstruopolis: salida en lista JSON asi:**

```
[
{"job": "J1", "machine": "M1", "start": 0, "end": 45},
{"job": "J2", "machine": "M2", "start": 10, "end": 35},
// ... una entrada por trabajo
]
// Gradescope calcula Cj y sum(wjTj) automaticamente
```

**Template de Python — estructura esperada** *(sigue en la página 3)*

### Página 3 — Template de Python, reglas de la competencia y recomendación para el Reto 01

Cada equipo recibe **reto1.py** y **reto2.py**. Solo deben implementar el cuerpo del algoritmo dentro de la funcion **solve()**:

```python
# reto1.py — template Willy Wonka
import json, time
def solve(data: dict) -> dict:
    """
    Parametro: data — diccionario cargado desde data.json
    Retorna: {"Cmax": int, "secuencia": list[str], "tiempo": int}
    """
    start = time.time()
    # <- su algoritmo va aqui
    secuencia = [] # llenar con ['L1', 'L3', ...]
    cmax = 0 # calcular Cmax con la secuencia
    elapsed = int((time.time() - start) * 1000)
    return {"Cmax": cmax, "secuencia": secuencia, "tiempo": elapsed}
if __name__ == "__main__":
    with open("data.json") as f:
        data = json.load(f)
    print(json.dumps(solve(data), indent=2))
```

> En el PDF el código aparece sin sangría (cada línea en una franja oscura); la sangría de arriba es la que exige Python y se reconstruyó.

**Reglas de la competencia**

| Regla | Detalle |
|---|---|
| **Equipo** | Cada equipo tiene exactamente 5 integrantes. Un solo estudiante sube los archivos en Gradescope en nombre del grupo. |
| **Archivos** | Se entregan reto1.py, reto2.py y el reporte tecnico en PDF. No se aceptan notebooks (.ipynb), archivos ZIP ni dependencias no estandar. |
| **Tiempo limite** | El algoritmo tiene un limite de 60 segundos por instancia. Si supera ese limite, Gradescope lo cancela y asigna el peor puntaje en esa instancia. |
| **Librerias** | Solo se permiten librerias de la biblioteca estandar de Python (json, time, math, random, itertools, collections, heapq, etc.) y numpy. No se permite OR-Tools, PuLP, Gurobi ni similares. |
| **Entregas** | Pueden hacer multiples entregas antes de la fecha limite. Gradescope calificara automaticamente la ultima version subida. |
| **Codigo propio** | El codigo debe ser propio del equipo. Se permite inspirarse en literatura o en clase, pero no copiar codigo de otros equipos. El profesor puede solicitar explicar el algoritmo en cualquier momento. |

**Recomendaciones para el algoritmo**

**Reto 01 — Willy Wonka (Flow Shop):** Consideren heuristicas como NEH, busqueda local (2-opt, insercion), o metaheuristicas como simulated annealing. La restriccion N→R es de factibilidad: su secuencia debe verificarla antes de calcular el Cmax.

### Página 4 — Recomendación para el Reto 02 y consejo general

**Reto 02 — Monstruopolis (Paralelas):** Consideren reglas de despacho como WSPT, EDD ponderado, o prioridades adaptadas. Las precedencias implican verificar en cada momento de decision que trabajos ya tienen sus predecesores terminados.

**Consejo general:** Empiecen con una solucion factible simple para asegurarse de que el formato es correcto. Luego mejoren la calidad. Un algoritmo rapido con solucion aceptable suele ganarle a uno lento con solucion teoricamente perfecta.

*Pie de página:* Planeacion, Programacion y Control de las Operaciones · Universidad de La Sabana · Facultad de Ingenieria Industrial

(El resto de la página está en blanco.)

## Anexo: texto extraído automáticamente del PDF

> Texto plano tal como sale del PDF, sin fórmulas ni tablas que estén como imagen. La versión fiel y completa es la sección «Contenido completo» de arriba.

### Página 1

PLANEACIÓN, PROGRAMACIÓN Y CONTROL DE LAS OPERACIONES
Competencia de Secuenciación de Máquinas
Universidad de La Sabana — Facultad de Ingeniería Industrial
Grupos de 5 estudiantes
2 retos de programación
Entrega por Gradescope
¿De qué se trata la competencia?
Cada grupo debe programar dos algoritmos de secuenciación en Python para resolver dos problemas clásicos
de scheduling. Los algoritmos se evalúan automáticamente en Gradescope: el sistema prueba su código con
varias instancias del problema y mide qué tan buena es la solución y qué tan rápido la encuentran. Gana el equipo
que mejor combine calidad de solución y velocidad de cómputo.
Los dos retos
RETO 01
Fábrica de Willy Wonka
Flow Shop con tiempos de alistamiento
Tipo: Flow Shop de 3 máquinas en serie (M1 → M2 →
M3).
Objetivo: Minimizar el Cmax (tiempo en que termina el
último lote).
Restricciones:
· Un lote Relleno (R) no puede ir inmediatamente
después de un lote Nueces (N) en ninguna máquina.
· Cada cambio de tipo genera un tiempo de
alistamiento diferente por máquina.
15 lotes | 3 máquinas en serie | setup
dependiente del tipo
RETO 02
Fábrica de Monstruópolis
Máquinas paralelas con precedencias
Tipo: 3 máquinas idénticas en paralelo (P3 | rj, prec |
∑WjTj).
Objetivo: Minimizar la tardanza ponderada total
(∑wjTj).
Restricciones:
· Cada trabajo tiene fecha de liberación (rj) y de entrega
(dj).
· Algunos trabajos tienen precedencias (i → j). No se
permite interrumpir trabajos (no preemption).
50 trabajos | 3 máquinas paralelas | ~5
precedencias
Criterios de evaluación y puntaje

### Página 2

60%
Calidad de la solución
(valor del objetivo obtenido)
30%
Tiempo computacional
(velocidad del algoritmo)
10%
Reporte técnico
(de los algoritmos presentados)
Penalizacion por restricciones violadas
Una solucion que incumpla alguna restriccion no recibe puntaje cero automaticamente, pero si tendra una
penalizacion directa sobre el valor de la funcion objetivo: se sumara una penalidad proporcional al numero de
violaciones detectadas, lo que deteriorara significativamente su posicion en el ranking.
El objetivo es incentivar soluciones factibles. Una solucion infactible con buen tiempo computacional nunca
superara a una solucion factible bien construida.
Como se compara la calidad entre equipos
Gradescope prueba cada algoritmo con varias instancias generadas automaticamente. El equipo con el menor
valor del objetivo (Cmax en Reto 01 o ∑wjTj en Reto 02) en promedio obtiene el mayor puntaje. El ranking se
normaliza: el mejor equipo obtiene 100 puntos, los demas se escalan proporcionalmente. Las penalizaciones por
violaciones se suman al valor objetivo antes de este calculo.
Reporte tecnico (10%): Documento PDF de maximo 4 paginas que describe los algoritmos implementados: tipo
de heuristica o metaheuristica usada, justificacion de la eleccion, analisis de resultados sobre las instancias de
prueba y lecciones aprendidas. Se entrega junto con el codigo en Gradescope.
Formatos de entrega
Reto 01 — Willy Wonka: salida en JSON exactamente asi:
{
"Cmax": 847, // minuto en que termina el ultimo lote
"secuencia": ["L1", "L4", ..., "L15"],
"tiempo": 12 // ms que tardo el algoritmo
}
Reto 02 — Monstruopolis: salida en lista JSON asi:
[
{"job": "J1", "machine": "M1", "start": 0, "end": 45},
{"job": "J2", "machine": "M2", "start": 10, "end": 35},
// ... una entrada por trabajo
]
// Gradescope calcula Cj y sum(wjTj) automaticamente
Template de Python — estructura esperada

### Página 3

Cada equipo recibe reto1.py y reto2.py. Solo deben implementar el cuerpo del algoritmo dentro de la funcion solve():
# reto1.py — template Willy Wonka
import json, time
def solve(data: dict) -> dict:
"""
Parametro: data — diccionario cargado desde data.json
Retorna: {"Cmax": int, "secuencia": list[str], "tiempo": int}
"""
start = time.time()
# <- su algoritmo va aqui
secuencia = [] # llenar con ['L1', 'L3', ...]
cmax = 0 # calcular Cmax con la secuencia
elapsed = int((time.time() - start) * 1000)
return {"Cmax": cmax, "secuencia": secuencia, "tiempo": elapsed}
if __name__ == "__main__":
with open("data.json") as f:
data = json.load(f)
print(json.dumps(solve(data), indent=2))
Reglas de la competencia
Equipo
Cada equipo tiene exactamente 5 integrantes. Un solo estudiante sube los archivos en
Gradescope en nombre del grupo.
Archivos
Se entregan reto1.py, reto2.py y el reporte tecnico en PDF. No se aceptan notebooks (.ipynb),
archivos ZIP ni dependencias no estandar.
Tiempo limite
El algoritmo tiene un limite de 60 segundos por instancia. Si supera ese limite, Gradescope lo
cancela y asigna el peor puntaje en esa instancia.
Librerias
Solo se permiten librerias de la biblioteca estandar de Python (json, time, math, random, itertools,
collections, heapq, etc.) y numpy. No se permite OR-Tools, PuLP, Gurobi ni similares.
Entregas
Pueden hacer multiples entregas antes de la fecha limite. Gradescope calificara automaticamente
la ultima version subida.
Codigo propio
El codigo debe ser propio del equipo. Se permite inspirarse en literatura o en clase, pero no copiar
codigo de otros equipos. El profesor puede solicitar explicar el algoritmo en cualquier momento.
Recomendaciones para el algoritmo
Reto 01 — Willy Wonka (Flow Shop): Consideren heuristicas como NEH, busqueda local (2-opt, insercion), o
metaheuristicas como simulated annealing. La restriccion N→R es de factibilidad: su secuencia debe verificarla
antes de calcular el Cmax.

### Página 4

Reto 02 — Monstruopolis (Paralelas): Consideren reglas de despacho como WSPT, EDD ponderado, o
prioridades adaptadas. Las precedencias implican verificar en cada momento de decision que trabajos ya tienen
sus predecesores terminados.
Consejo general: Empiecen con una solucion factible simple para asegurarse de que el formato es correcto.
Luego mejoren la calidad. Un algoritmo rapido con solucion aceptable suele ganarle a uno lento con solucion
teoricamente perfecta.
Planeacion, Programacion y Control de las Operaciones · Universidad de La Sabana · Facultad de Ingenieria Industrial

