# reto-1-willy-wonka

> **Archivo:** [`reto-1-willy-wonka.pdf`](./reto-1-willy-wonka.pdf) · **Corte 3** · 4 páginas  
> **Nombre original:** `CORTE 3/PROYECTO 3/Reto Willy Wonka .pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** enunciado del Reto 01 de la competencia del Corte 3, un flow shop de permutación de 3 máquinas con alistamientos dependientes del tipo de lote y una restricción de secuencia (N no puede ir justo antes de R). Objetivo: minimizar el makespan.

**Ideas clave**

- **Tres tipos de lote:** simple (S), con nueces (N) y relleno (R). Hay 15 lotes (L1–L15) de 100 tabletas cada uno, y todos pasan por M1 (mezclado), M2 (moldeo) y M3 (empaque) en ese orden.
- **«Secuencia uniforme a lo largo de las máquinas»:** el orden de los lotes es el mismo en las tres máquinas, es decir, un flow shop de **permutación**.
- **Restricción de factibilidad:** un lote R no puede procesarse **inmediatamente después** de un N en ninguna máquina; debe haber al menos un lote de otro tipo entre ellos. Con la misma secuencia en las tres máquinas, basta revisar las parejas consecutivas.
- **Alistamiento:** al cambiar de tipo, cada máquina necesita un tiempo que depende del tipo anterior y del siguiente (Tablas 2–4). Es 0 entre lotes del mismo tipo.
- **Datos aleatorios:** los de las tablas son un ejemplo; en la evaluación «los datos variarán de forma aleatoria».
- **Entregables:**
  - un informe breve con la secuencia, el tiempo máximo de terminación y la secuencia en cada máquina;
  - un algoritmo que lea `data.json` (claves `lotes` y `setup`, con 9 combinaciones «X-Y» por máquina) y devuelva `{"Cmax", "secuencia", "tiempo"}`, con el tiempo en milisegundos.

**Fórmulas y métodos**

Notación de tres campos: $F3\,|\,prmu,\ s_{m}(a,b),\ \text{N}\not\to\text{R}\,|\,C_{\max}$. La forma $s_{ij}$ por tipo y la notación son del [informe técnico de la solución](../solucion/INFORME_TECNICO.md); el PDF no usa notación α|β|γ.

Para una secuencia $\pi=(\pi_1,\dots,\pi_{15})$, con $p_{m,j}$ el tiempo de proceso del lote $j$ en la máquina $m$, $\tau(j)$ su tipo y $s_m(a,b)$ el alistamiento de $m$ al pasar del tipo $a$ al $b$:

$$C_{m,\pi_k}=\max\left(C_{m,\pi_{k-1}},\,C_{m-1,\pi_k}\right)+s_m\!\left(\tau(\pi_{k-1}),\tau(\pi_k)\right)+p_{m,\pi_k}$$

con $C_{0,\cdot}=0$, $C_{m,\pi_0}=0$ y sin alistamiento para el primer lote. El objetivo es $C_{\max}=C_{3,\pi_{15}}$.

Factibilidad: $\nexists\,k:\ \tau(\pi_{k-1})=\text{N}\wedge\tau(\pi_k)=\text{R}$.

Este modelo de tiempos es un **supuesto**: el alistamiento empieza cuando la máquina está libre y el lote ya llegó. El PDF no dice si el alistamiento puede anticiparse. Es el mismo supuesto que usa la función de evaluación de la plantilla del profesor y la solución del estudiante.

**Ejemplos resueltos:** el PDF no resuelve el ejemplo. La solución del estudiante obtiene para estos datos:

- secuencia L9, L12, L6, L15, L3 | L4, L13, L10, L1, L7 | L8, L11, L5, L14, L2 (bloques R → S → N);
- **$C_{\max}=621$ min**, igual a su cota inferior, es decir, óptimo demostrado.

Ver [solucion/README.md](../solucion/README.md) e [INFORME_TECNICO.md](../solucion/INFORME_TECNICO.md).

**Páginas clave**

| Página | Contenido |
|---|---|
| 1 | Contexto y máquinas |
| 2 | Tabla 1 (tiempos), regla N→R y explicación de alistamientos |
| 3 | Tablas 2–4 (alistamientos de M1, M2 y M3) y resultado esperado |
| 4 | Formatos JSON de entrada y salida, y autores del reto |

**Relación con otros archivos del repo**

- Reglas generales y calificación: [instructivo-competencia-scheduling.md](./instructivo-competencia-scheduling.md).
- Plantilla del profesor (generador aleatorio y evaluador): [plantilla-reto-1-willy-wonka/reto_schedulling.py](./plantilla-reto-1-willy-wonka/reto_schedulling.py); explicada en el [README del proyecto](../README.md).
- Datos de este enunciado en JSON: [solucion/pruebas/data_ejemplo_reto1.json](../solucion/pruebas/data_ejemplo_reto1.json). Usa los valores de las Tablas 2–4, no los del ejemplo de la página 4.
- Teoría:
  - [L19 Flow shop](../../04-flow-shop/L19-flow-shop-scheduling.md), con NEH y Johnson;
  - [flowshop-scheduling](../../04-flow-shop/flowshop-scheduling.md), el Excel del tema;
  - [L16 Introducción a scheduling](../../01-introduccion-scheduling/L16-intro-scheduling.md), con la notación α|β|γ.

**Observaciones**

- **Inconsistencia de datos:** el ejemplo de `data.json` de la página 4 da para M1 `"S-R": 15` y `"S-N": 30`, mientras que la Tabla 2 dice S→N = 15 y S→R = 35. Los demás valores de M1 coinciden: N-S 25, N-R 40, R-S 20, R-N 25. El ejemplo parece ilustrativo; la solución del estudiante usa la Tabla 2.
- El ejemplo de entrada lleva comentarios `#`, que no son JSON válido.
- La «secuencia de los lotes en cada una de las máquinas» que pide el informe es la misma en las tres, porque la secuencia es uniforme.

## Contenido completo (página por página)

### Página 1 — ¡Willy Wonka está en apuros! (contexto y Tabla 1, inicio)

> [Imagen decorativa: logo de la Universidad de La Sabana, arriba a la izquierda]

**Proyecto Final Planeación, Programación y Control de las Operaciones**

**¡Willy Wonka está en apuros!**

La empresa chocolatera de Willy Wonka produce tres tipos de tabletas de chocolate diferentes: simples (S), con nueces (N) y rellenas (R). Cada lote de barras de chocolate contiene 100 tabletas y debe pasar de forma obligatoria por tres máquinas. Por razones de eficiencia operativa, todos los lotes se procesan bajo una secuencia uniforme a lo largo de las máquinas en el siguiente orden:

- **Máquina de mezclado y refinado (M1):** Se combinan los ingredientes base y se homogeneiza la mezcla con la fórmula secreta de Willy Wonka.
- **Máquina de moldeo y enfriamiento (M2):** La mezcla se vierte en moldes y se enfría en cámaras controladas para obtener la forma de tableta, conservando todo su sabor y su aroma.
- **Maquina empaquetadora (M3):** Las tabletas son empacadas y selladas individualmente, a cada una se le coloca un tiquete plateado y solo una de cada un millón de tabletas se le asignará un tiquete dorado de ganador.

El señor Willy Wonka desea con ansias acabar cuanto antes la producción de esta temporada para conocer el ganador del tiquete dorado. Por lo tanto, le ha solicitado a su equipo de ingenieros industriales que planifique la producción de este mes para terminar lo antes posible todos y cada uno de los lotes planificados para producir este mes.

El señor Wonka le ha compartido a su equipo toda la información relevante de sus operaciones en la fábrica. Lo primero que entrega el señor Wonka a su equipo es la Tabla 1, con información los lotes a fabricar en este mes de noviembre. Este es un ejemplo, pero los datos variarán de forma aleatoria.

**Tabla 1.** *Minutos de procesamiento de todos los lotes a fabricar en noviembre* (filas L1 y L2 en esta página; la tabla completa está en la página 2)

### Página 2 — Tabla 1 completa, restricción N→R y alistamientos

**Tabla 1.** Minutos de procesamiento de todos los lotes a fabricar en noviembre (tabla completa; las filas L1 y L2 vienen de la página 1)

| LOTE | TIPO | M1 | M2 | M3 |
|---|---|---|---|---|
| L1 | S | 38 | 33 | 19 |
| L2 | N | 41 | 27 | 21 |
| L3 | R | 29 | 37 | 14 |
| L4 | S | 35 | 24 | 22 |
| L5 | N | 44 | 38 | 16 |
| L6 | R | 27 | 31 | 18 |
| L7 | S | 40 | 28 | 25 |
| L8 | N | 33 | 40 | 12 |
| L9 | R | 31 | 22 | 17 |
| L10 | S | 39 | 35 | 15 |
| L11 | N | 42 | 26 | 23 |
| L12 | R | 28 | 34 | 13 |
| L13 | S | 36 | 29 | 20 |
| L14 | N | 45 | 25 | 24 |
| L15 | R | 30 | 39 | 11 |

Por políticas de seguridad alimentaria, un lote de tipo relleno (R) no puede procesarse inmediatamente después de un lote de tipo nueces (N) en ninguna máquina, para evitar contaminación por trazas de frutos secos. Debe haber al menos un lote de otro tipo entre ellos.

Asimismo, cada vez que una máquina cambia el tipo de lote a producir, se necesita un tiempo adicional de limpieza y ajuste. Los tiempos dependen del lote anterior y el tipo siguiente de lote, y son diferentes en las tres máquinas. De esta manera, se le presentó al grupo los tiempos de alistamiento en las Tablas 2, 3 y 4.

**Tabla 2.** *Minutos de alistamiento de la máquina uno según tipos de lotes.* (los valores están en la página 3)

### Página 3 — Tablas 2, 3 y 4 (alistamientos por máquina) y resultado esperado

En las tres tablas, la fila es el tipo del lote **anterior** y la columna el tipo del lote **siguiente** (de → a).

**Tabla 2.** Minutos de alistamiento de la máquina uno (M1):

| de \ a | S | N | R |
|---|---|---|---|
| **S** | 0 | 15 | 35 |
| **N** | 25 | 0 | 40 |
| **R** | 20 | 25 | 0 |

**Tabla 3.** Minutos de alistamiento de la máquina dos (M2):

| de \ a | S | N | R |
|---|---|---|---|
| **S** | 0 | 10 | 25 |
| **N** | 15 | 0 | 30 |
| **R** | 10 | 20 | 0 |

**Tabla 4.** Minutos de alistamiento de la máquina tres (M3):

| de \ a | S | N | R |
|---|---|---|---|
| **S** | 0 | 5 | 10 |
| **N** | 8 | 0 | 12 |
| **R** | 6 | 9 | 0 |

**Resultado Esperado**

Willy Wonka le solicita a su equipo que le entreguen un informe breve en donde le indiquen la secuencia en la que debe fabricar todos los lotes, además de cuánto tiempo tardarán a lo sumo para terminar de procesar todos, y cuál es la secuencia de los lotes en cada una de las máquinas. Adicionalmente, deben entregarle un algoritmo que reciba como entrada la información brindada por el señor Wonka, y la retorne en un formato especifico que se muestra a continuación: • **Entrada**

### Página 4 — Formatos de entrada (data.json) y salida, y autores

> [Captura de código con fondo oscuro. Las claves aparecen resaltadas en verde y el texto extraído las desordena; abajo se reconstruye en orden, fiel a la imagen, con los comentarios `#` originales.]

**Entrada:**

```
#  datos de entrada formato JSON (nombre del archivo debe ser data.json)
{
    "lotes" :
    {
        "L1": {"tipo": "S", "M1": 38, "M2": 33, "M3": 19}, # Información por lote
        ...,
        "L15": {"tipo": "R", "M1": 30, "M2": 39, "M3": 11} # Debe haber 15 lotes
    },

    "setup" :
    {
        "M1" :
        {
            "S-S": 0, # todas las combinaciones de tipo de lote por cada maquina
            "S-R": 15,
            "S-N": 30,
            "N-S": 25,
            "N-N": 0, # las letras iguales son 0
            "N-R": 40,
            "R-S": 20,
            "R-N": 25,
            "R-R" : 0, # 9 combinaciones posibles por maquina
        },
        ...,
        "M3" : # cada maquina debe tener sus combinaciones completas
        {
            "S-S": 0,
            ...,
            "R-R": 0,
        }
    }
}
```

> Ojo: en este ejemplo, M1 tiene `"S-R": 15` y `"S-N": 30`, pero la Tabla 2 dice S→N = 15 y S→R = 35. Los demás valores de M1 coinciden con la Tabla 2. Ver Observaciones.

**Salida:**

```
{
    "Cmax": 100, # tiempo de terminación (ej.: al minuto 100 se acaba el ultimo lote)
    "secuencia": ["L1", ..., "L15"], # secuencia ordenada por producción de los lotes
    "tiempo": 1500 # tiempo ejecución algoritmo en milisegundos
}
```

Reto diseñado por: Catalina Andrea Castro López, Isabella Sofia Endara Chitiva, Néstor Andrés Tabares David, Nicolás Joel Cáceres Parra

## Anexo: texto extraído automáticamente del PDF

> Texto plano tal como sale del PDF, sin fórmulas ni tablas que estén como imagen. La versión fiel y completa es la sección «Contenido completo» de arriba.

### Página 1 · 1 imagen(es)

Proyecto Final Planeación, Programación y Control de las Operaciones 
¡Willy Wonka está en apuros! 
La empresa chocolatera de Willy Wonka produce tres tipos de tabletas de chocolate diferentes: simples 
(S), con nueces (N) y rellenas (R). Cada lote de barras de chocolate contiene 100 tabletas y debe pasar de 
forma obligatoria por tres máquinas. Por razones de eficiencia operativa, todos los lotes se procesan bajo 
una secuencia uniforme a lo largo de las máquinas en el siguiente orden: 
• 
Máquina de mezclado y refinado (M1): Se combinan los ingredientes base y se homogeneiza la 
mezcla con la fórmula secreta de Willy Wonka. 
• 
Máquina de moldeo y enfriamiento (M2): La mezcla se vierte en moldes y se enfría en cámaras 
controladas para obtener la forma de tableta, conservando todo su sabor y su aroma. 
• 
Maquina empaquetadora (M3): Las tabletas son empacadas y selladas individualmente, a cada una 
se le coloca un tiquete plateado y solo una de cada un millón de tabletas se le asignará un tiquete 
dorado de ganador. 
El señor Willy Wonka desea con ansias acabar cuanto antes la producción de esta temporada para 
conocer el ganador del tiquete dorado. Por lo tanto, le ha solicitado a su equipo de ingenieros industriales 
que planifique la producción de este mes para terminar lo antes posible todos y cada uno de los lotes 
planificados para producir este mes. 
El señor Wonka le ha compartido a su equipo toda la información relevante de sus operaciones en la 
fábrica. Lo primero que entrega el señor Wonka a su equipo es la Tabla 1, con información los lotes a 
fabricar en este mes de noviembre. Este es un ejemplo, pero los datos variarán de forma aleatoria. 
Tabla 1. 
Minutos de procesamiento de todos los lotes a fabricar en noviembre 
LOTE 
TIPO 
M1 
M2 
M3 
L1 
S 
38 
33 
19 
L2 
N 
41 
27 
21

### Página 2

L3 
R 
29 
37 
14 
L4 
S 
35 
24 
22 
L5 
N 
44 
38 
16 
L6 
R 
27 
31 
18 
L7 
S 
40 
28 
25 
L8 
N 
33 
40 
12 
L9 
R 
31 
22 
17 
L10 
S 
39 
35 
15 
L11 
N 
42 
26 
23 
L12 
R 
28 
34 
13 
L13 
S 
36 
29 
20 
L14 
N 
45 
25 
24 
L15 
R 
30 
39 
11 
Por políticas de seguridad alimentaria, un lote de tipo relleno (R) no puede procesarse inmediatamente 
después de un lote de tipo nueces (N) en ninguna máquina, para evitar contaminación por trazas de 
frutos secos. Debe haber al menos un lote de otro tipo entre ellos. 
Asimismo, cada vez que una máquina cambia el tipo de lote a producir, se necesita un tiempo adicional 
de limpieza y ajuste. Los tiempos dependen del lote anterior y el tipo siguiente de lote, y son diferentes 
en las tres máquinas. De esta manera, se le presentó al grupo los tiempos de alistamiento en las Tablas 
2, 3 y 4. 
Tabla 2. 
Minutos de alistamiento de la máquina uno según tipos de lotes.

### Página 3

S 
N 
R 
S 
0 
15 
35 
N 
25 
0 
40 
R 
20 
25 
0 
Tabla 3. 
Minutos de alistamiento de la máquina dos según tipos de lotes. 
S 
N 
R 
S 
0 
10 
25 
N 
15 
0 
30 
R 
10 
20 
0 
Tabla 4. 
Minutos de alistamiento de la máquina tres según tipos de lotes. 
S 
N 
R 
S 
0 
5 
10 
N 
8 
0 
12 
R 
6 
9 
0 
Resultado Esperado 
Willy Wonka le solicita a su equipo que le entreguen un informe breve en donde le indiquen la secuencia 
en la que debe fabricar todos los lotes, además de cuánto tiempo tardarán a lo sumo para terminar de 
procesar todos, y cuál es la secuencia de los lotes en cada una de las máquinas. Adicionalmente, deben 
entregarle un algoritmo que reciba como entrada la información brindada por el señor Wonka, y la 
retorne en un formato especifico que se muestra a continuación: • Entrada

### Página 4

# 
datos de entrada formato JSON (nombre del archivo debe ser 
data.json) { 
 : 
{ 
: 19}, # Información por lote 
 ..., 
: 11} # Debe haber 15 lotes 
 }, 
 : 
 { 
 : 
{ 
: 0, # todas las combinaciones de tipo de lote por cada maquina 
: 15, 
: 30, 
: 25, 
: 0, # las letras iguales son 0 
: 40, 
: 20, 
: 25, 
 : 0, # 9 combinaciones posibles por maquina 
}, 
..., 
: # cada maquina debe tener sus combinaciones completas 
 { 
: 0, 
 ..., 
: 0, 
 } 
 } 
} 
"lotes" 
"L1": {"tipo" : "S", "M1" : 38, "M2" : 33, "M3"
"L15": {"tipo": "R", "M1": 30, "M2" : 39, "M3"
"setup" 
"M1"
"S-S"
"S-R"
"S-N"
"N-S"
"N-N"
"N-R"
"R-S"
"R-N"
"R-R"
"M3"
"S-S"
"R-R"
• Salida 
{ 
 "Cmax": 100, # 
tiempo de terminación (ej.: al minuto 100 se acaba el ultimo 
lote) 
 "secuencia": [ 
], # secuencia ordenada por producción de los lotes 
 "tiempo": 1500 # tiempo ejecución algoritmo en milisegundos } 
"L1", ..., "L15" 
Reto diseñado por: Catalina Andrea Castro López, Isabella Sofia Endara Chitiva, Néstor Andrés Tabares 
David , Nicolás Joel Cáceres Parra

