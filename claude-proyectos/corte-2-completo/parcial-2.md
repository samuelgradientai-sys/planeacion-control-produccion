<!-- fuente: corte-2-planeacion-agregada-mrp/parcial-2/README.md -->
# Parcial 2: planeación agregada y MRP (Corte 2)

## Qué cubre

Este es el examen del Corte 2, con su rúbrica y su solucionario completo. Tiene dos puntos:

- **Punto 1, Sales and Operations Planning** (Muebles Andinos S.A.S., familia de escritorios, sillas y archivadores): agregación en horas estándar, modelo de programación lineal entera, comparación de planes de persecución y nivelado, y desagregación por igual tiempo de agotamiento.
- **Punto 2, MRP** (mesa auxiliar M): árbol de materiales y códigos de nivel bajo, demanda dependiente con netos, matrices MRP lote a lote y la heurística Silver-Meal frente a Wagner-Whitin.

El examen dura 2 horas, se hace en papel y solo admite calculadora no programable.

## Archivos de esta carpeta

| Archivo | Qué es | Leer primero |
|---|---|---|
| [parcial-2-solucion.md](/corte-2-planeacion-agregada-mrp/parcial-2/parcial-2-solucion.md) (gemelo de `parcial-2-solucion.pdf`, 13 págs.) | Enunciado (pp. 1–6), rúbrica (pp. 6–7) y solucionario (pp. 7–13), transcritos completos con todas las tablas. Incluye una verificación propia con el Plan C y el óptimo de Wagner-Whitin | Sí |

## Orden de estudio sugerido

1. Repasar los temas antes de resolver:
   - [L10](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md), planeación agregada;
   - [L11](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md), agregación y desagregación;
   - [L12](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/L12-wagner-whitin-and-silver-meal.md), Silver-Meal y Wagner-Whitin;
   - [L13](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md) y [L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md), BOM y MRP.
2. Leer el enunciado en [parcial-2-solucion.md](/corte-2-planeacion-agregada-mrp/parcial-2/parcial-2-solucion.md) (páginas 1 a 6) e intentar resolverlo sin mirar la solución.
3. Comparar con el solucionario (páginas 7 a 13) y con la sección «Verificación propia» del resumen.
4. Revisar la rúbrica (páginas 6–7). Las preguntas marcadas [Argumente] reparten el puntaje mitad cálculo y mitad argumento.

## Conceptos y fórmulas clave

El detalle está en [parcial-2-solucion.md](/corte-2-planeacion-agregada-mrp/parcial-2/parcial-2-solucion.md#resumen).

- **Demanda agregada:** $D_t=\sum_i k_i d_{i,t}$, donde $k_i$ son las horas estándar por unidad y $d_{i,t}$ la demanda en unidades.
- **Modelo de planeación agregada.** Variables: $W$ operarios, $H$ contrataciones, $F$ despidos, $O$ horas extra, $S$ subcontratación, $I$ inventario, $P$ producción regular.

$$\min\sum_t\left(3.2\text{M}\,W_t+30\text{k}\,O_t+38\text{k}\,S_t+1.5\text{M}\,H_t+2.5\text{M}\,F_t+2\text{k}\,I_t\right)$$

  sujeto a:
  - $I_t=I_{t-1}+P_t+O_t+S_t-D_t$;
  - $W_t=W_{t-1}+H_t-F_t$;
  - $P_t\le160W_t$;
  - $O_t\le32W_t$.
- **Tiempo de agotamiento igual:** $T^*=\dfrac{X+\sum_i I_i}{\sum_i d_i}$ y $Y_i=T^*d_i-I_i$. Aquí $X$ son las horas aprobadas, $I_i$ el inventario en horas y $d_i$ la demanda en horas.
- **MRP lote a lote:** $RN_t=\max(0,RB_t-IP_{t-1}-RP_t)$, $LOP_{t-LT}=ROP_t=RN_t$ y $RB^{\text{hijo}}_t=\sum q\cdot LOP^{\text{padre}}_t$. Los ítems se procesan por código de nivel bajo.
- **Silver-Meal:** $C(j,k)=\dfrac{S+h\sum_{t=j}^{k}(t-j)D_t}{k-j+1}$; el lote se cierra cuando el costo por periodo sube.
- **Wagner-Whitin:** $f(k)=\min_j\{f(j-1)+S+h\sum_{t=j}^{k}(t-j)D_t\}$.

## Ejercicios resueltos disponibles

Todos están en [parcial-2-solucion.md](/corte-2-planeacion-agregada-mrp/parcial-2/parcial-2-solucion.md).

| Pregunta | Resultado principal |
|---|---|
| 1.1 Agregación | 2400, 2560, 3200 y 2880 h estándar; el mes 3 equivale a 1600 escritorios |
| 1.3 Planes | A (persecución) cuesta $235.800.000 y B (nivelado) $229.440.000. Plan C, cálculo propio: $225.500.000, el más barato, aunque el solucionario recomienda B |
| 1.4 Desagregación de 2620 h | $T^*=1{,}2$ meses: 500 escritorios, 400 sillas y 340 archivadores |
| 2.1 BOM | Códigos de nivel bajo: M = 0, T = 1, S = 1, K = 2, P = 2 |
| 2.2 Explosión de 200 mesas | Netos: M 180, T 150, S 130, P 420, K 380 |
| 2.3 MRP | Liberaciones de M en las semanas 2, 4, 5 y 7 (30, 60, 40, 70); de S en las semanas 3, 4 y 6 (20, 40, 70); de K en las semanas 3, 4, 5 y 6 (100, 40, 140, 70) |
| 2.4 Silver-Meal | Pedidos de 310, 350 y 200 u en las semanas 1, 4 y 6; costo $1.390.000. Wagner-Whitin, cálculo propio: $1.280.000 |

**Errores del documento** (detalle en el resumen del gemelo):

- La portada dice 100 puntos, pero la tabla de puntos suma 110.
- La recomendación de 1.3c contradice su propio argumento.
- El solucionario de 2.1 incluye un literal c) que el enunciado no pide.
- En 2.4 solo se pide Silver-Meal, aunque el título dice «Silver-Meal vs. Wagner-Whitin».

## Relación con otros temas y proyectos

- [01-planeacion-agregada-modelo-bowman](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/): el modelo de costos y la formulación de la pregunta 1.2.
- [02-agregacion-y-desagregacion](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/): agregación en horas estándar y desagregación por tiempo de agotamiento (preguntas 1.1 y 1.4).
- [03-wagner-whitin-y-silver-meal](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/): lot sizing (pregunta 2.4); [wagner_whitin.py](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/wagner_whitin.py) sirve para comprobar el óptimo.
- [04-bom-y-mrp](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/): BOM, código de nivel bajo, demanda dependiente y matriz MRP (preguntas 2.1 a 2.3).
- [05-mrp-ii-y-capacidad](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/): MRP II y capacidad, tema posterior que no entra en este parcial.
- [proyecto-thyms-gemelo-digital](/corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/): el proyecto del Corte 2, que aplica planeación agregada y MRP a un caso real.


---

<!-- fuente: corte-2-planeacion-agregada-mrp/parcial-2/parcial-2-solucion.md -->
# parcial-2-solucion

> **Archivo:** [`parcial-2-solucion.pdf`](/corte-2-planeacion-agregada-mrp/parcial-2/parcial-2-solucion.pdf) · **Corte 2** · 13 páginas  
> **Nombre original:** `CORTE 2/Parcial 2 – Planeación, Programación y Control de la Producción Solucion.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** enunciado, rúbrica y solucionario completo del Parcial 2 (Corte 2): planeación agregada (S&OP), formulación lineal entera, evaluación de planes persecución/nivelado, desagregación por tiempo de agotamiento, BOM y códigos de nivel bajo, demanda dependiente, matriz MRP y dimensionamiento de lotes (Silver-Meal frente a Wagner-Whitin).

**Ideas clave**

- El parcial tiene dos puntos con datos independientes. **Punto 1** (Muebles Andinos S.A.S., familia de 3 muebles: escritorio, silla y archivador): agregación, modelo PLE, planes A/B/C y desagregación. **Punto 2** (mesa auxiliar M): BOM, demanda dependiente, MRP lote a lote y Silver-Meal.
- La unidad agregada correcta es la **hora estándar** del recurso restrictivo (mano de obra polivalente), no la suma de unidades.
- El costo regular es fijo por operario (se paga la jornada completa): $160 \times 20.000 = 3.200.000$ por operario-mes, por eso el objetivo usa $W_t$ y no $P_t$.
- La subcontratación ($38.000/h) nunca conviene porque la hora extra ($30.000/h) es más barata y su límite nunca se alcanza.
- La desagregación por **igual tiempo de agotamiento** usa los inventarios y deja a toda la familia cubierta hasta el mismo instante; repartir en proporción a la demanda deja agotamientos desiguales.
- El MRP procesa por **código de nivel bajo**: K aparece en los niveles 1 y 2 y se procesa en el 2, después de M y de S. Los requerimientos de un hijo salen de las **liberaciones planeadas** (netas) de sus padres.
- Silver-Meal es miope: se detiene en el primer mínimo local del costo por periodo. Wagner-Whitin es óptimo para un horizonte fijo, pero genera nerviosismo con horizonte rodante.
- Rúbrica con dos indicadores: (1) identifica elementos y (2) evalúa alternativas. Niveles de 100 %, 75 %, 40 % y 0–10 %. En las preguntas [Argumente], el cálculo vale el 50 % y el argumento el otro 50 %.

**Fórmulas y métodos**

- **Demanda agregada en horas estándar:** $D_t=\sum_i k_i\,d_{i,t}$, donde $k_i$ son las horas estándar por unidad del producto $i$ (2,0; 1,5; 3,0) y $d_{i,t}$ su demanda en unidades. Se usa cuando los productos comparten recursos y se mide la carga del recurso restrictivo.
- **Unidades equivalentes:** $D_t / k_{\text{ref}}$; con escritorios, $k_{\text{ref}}=2$ h.
- **Modelo de planeación agregada (PLE entera).** Los símbolos son: $W_t$ operarios; $H_t$ contratados; $F_t$ despedidos; $P_t$ horas regulares; $O_t$ horas extra; $S_t$ horas subcontratadas; $I_t$ inventario final en horas estándar; $D_t$ demanda en horas.

$$\min Z=\sum_{t=1}^{4}\left(3\,200\,000\,W_t+30\,000\,O_t+38\,000\,S_t+1\,500\,000\,H_t+2\,500\,000\,F_t+2\,000\,I_t\right)$$

  sujeto a:
  - $I_t=I_{t-1}+P_t+O_t+S_t-D_t$;
  - $W_t=W_{t-1}+H_t-F_t$;
  - $P_t\le 160W_t$;
  - $O_t\le 32W_t$;
  - $I_0=0$, $W_0=16$;
  - $P_t,O_t,S_t,I_t\ge0$ y $W_t,H_t,F_t\in\mathbb{Z}_{\ge0}$.
- **Costo de un plan:** $\sum_t\left(3\,200\,000\,W_t+30\,000\,O_t+2\,000\,I_t+1\,500\,000\,H_t+2\,500\,000\,F_t\right)$.
- **Tiempo de agotamiento común (desagregación).**
  - $T^*=\dfrac{X+\sum_i I_i}{\sum_i d_i}$.
  - $Y_i=T^*d_i-I_i$, en horas; las unidades son $Y_i/k_i$.
  - Tiempo de agotamiento de un ítem: $RO_i=(I_i+Y_i)/d_i$.
  - Símbolos: $X$ horas aprobadas para la familia; $I_i$ inventario del producto $i$ en horas; $d_i$ demanda del periodo en horas.
- **Explosión con netos (demanda dependiente):** $RB_{\text{hijo}}=\sum_{\text{padres}}q_{\text{padre,hijo}}\cdot RN_{\text{padre}}$ y $RN=\max(0,\,RB-I)$, donde $q$ es la cantidad por padre.
- **Registro MRP lote a lote.** Símbolos: $RB_t$ brutos; $RP_t$ recepciones programadas; $IP_t$ inventario proyectado; $RN_t$ netos; $ROP_t$ recepción de órdenes planeadas; $LOP_t$ liberación de órdenes planeadas; $LT$ tiempo de entrega.
  - $RN_t=\max(0,\,RB_t-IP_{t-1}-RP_t)$.
  - $ROP_t=RN_t$.
  - $IP_t=IP_{t-1}+RP_t+ROP_t-RB_t$.
  - $LOP_{t-LT}=ROP_t$.
  - Brutos del hijo: $RB^{\text{hijo}}_t=\sum q\cdot LOP^{\text{padre}}_t$.
- **Silver-Meal.** Costo por periodo de un pedido en la semana $j$ que cubre hasta la $k$:

$$C(j,k)=\frac{S+h\sum_{t=j}^{k}(t-j)\,D_t}{k-j+1}$$

  Se amplía $k$ mientras $C(j,k+1)\le C(j,k)$; cuando sube, se cierra el lote y se empieza uno nuevo en $k+1$. Aquí $S$ es el costo de ordenar, $h$ el costo de mantener por unidad y semana y $D_t$ el requerimiento neto.
- **Wagner-Whitin** (programación dinámica): $f(k)=\min_{1\le j\le k}\left\{f(j-1)+S+h\sum_{t=j}^{k}(t-j)D_t\right\}$, con $f(0)=0$. Da el óptimo para un horizonte fijo.

**Ejemplos resueltos (con su resultado)**

| Pregunta | Página(s) | Resultado |
|---|---|---|
| 1.1a Demanda agregada | 7 | 2400, 2560, 3200 y 2880 h estándar (meses 1 a 4) |
| 1.1b Escritorios equivalentes del mes 3 | 7 | 3200 / 2 = 1600 escritorios |
| 1.1c Sumar unidades | 7 | No sirve: 1550 muebles pueden ser de 2325 h a 4650 h |
| 1.2 Modelo PLE | 7–8 | Modelo completo; enteras $W_t$, $H_t$, $F_t$ |
| 1.3 Plan A (persecución) | 8 | Operarios 15, 16, 20, 18; contrata 5 y despide 3; total **$235.800.000** |
| 1.3 Plan B (nivelado, 16 operarios) | 8 | Extra 0, 0, 480 y 320 h; inventario 160, 160, 0 y 0; total **$229.440.000** |
| 1.3c Recomendación | 9 | El solucionario dice «Plan B» (ver observación 2) |
| 1.4a Desagregación de 2620 h | 9 | $T^*=1{,}2$ meses: 500 escritorios, 400 sillas y 340 archivadores |
| 1.4b Reparto proporcional | 9 | 491, 437 y 327,5 u; agotamientos de 1,18, 1,29 y 1,16 meses: se recomienda igual tiempo de agotamiento |
| 2.1 BOM y LLC | 9 | LLC: M = 0, T = 1, S = 1, K = 2, P = 2 |
| 2.2 Demanda dependiente (200 mesas) | 10 | Netos: M 180, T 150, S 130, P 420, K 380; el auxiliar compra 380 patas y 220 kits de más |
| 2.3 MRP de M | 10–11 | Liberaciones: 30 (sem. 2), 60 (sem. 4), 40 (sem. 5), 70 (sem. 7) |
| 2.3 MRP de S | 11 | Liberaciones: 20 (sem. 3), 40 (sem. 4), 70 (sem. 6) |
| 2.3 MRP de K | 12 | Brutos 0, 30, 40, 140, 40, 140, 70, 0; liberaciones: 100 (sem. 3), 40 (sem. 4), 140 (sem. 5), 70 (sem. 6) |
| 2.4 Silver-Meal | 13 | Pedidos: 310 u (sem. 1), 350 u (sem. 4) y 200 u (sem. 6); costo **$1.390.000** |

**Verificación propia de los cálculos (agregada al transcribir; no está en el PDF)**

- Rehíce todas las tablas del solucionario: agregación, planes A y B, desagregación, explosión, matrices MRP de M, S y K, y Silver-Meal. Los números coinciden.
- **Plan C (cálculo propio):** 17 operarios dan 2720 h por mes.

| Mes | Demanda (h) | Regular (h) | Extra (h) | Inventario final (h) |
|---|---|---|---|---|
| 1 | 2400 | 2720 | 0 | 320 |
| 2 | 2560 | 2720 | 0 | 480 |
| 3 | 3200 | 2720 | 0 | 0 |
| 4 | 2880 | 2720 | 160 | 0 |

  Costos del Plan C:
  - Regular: 10 880 h, $217.600.000.
  - Extra: 160 h, $4.800.000.
  - Inventario: 800 h·mes, $1.600.000.
  - Una contratación: $1.500.000.
  - **Total: $225.500.000.**

  Plan C es el más barato: $3.940.000 menos que B y $10.300.000 menos que A. Su hora extra máxima es 160 h, por debajo del límite de 544 h, así que es factible.
- **Wagner-Whitin para 2.4 (cálculo propio, en miles de pesos):** $f(1)=300$, $f(2)=380$, $f(3)=540$, $f(4)=780$, $f(5)=1080$ y $f(6)=1280$.
  - Plan óptimo: 230 u en la semana 1 (cubre 1–2), 180 u en la semana 3 (cubre 3–4) y 450 u en la semana 5 (cubre 5–6).
  - Costo: **$1.280.000**, $110.000 menos que Silver-Meal (8,6 %). Confirma la afirmación del solucionario («unir 3 con 4 y 5 con 6»).

**Observaciones (errores e inconsistencias del documento)**

1. La portada dice «Valor: 100 puntos (nota = puntos / 20)», pero la tabla de distribución suma **110 puntos**: 10 + 20 + 20 + 12 + 5 + 10 + 18 + 15.
2. **1.3c:** el solucionario dice «Se recomienda el Plan B: ahorra dinero» y lo justifica con un argumento que favorece al Plan C («contratar un operario reemplaza 640 h de extra, que costaban $19.200.000»). Tampoco calcula el costo del Plan C, que es el más barato ($225.500.000, ver arriba). Además, el argumento compara $1.500.000 de contratación con $19.200.000 de horas extra y omite la nómina adicional: 4 × $3.200.000 = $12.800.000, más $960.000 de inventario adicional. Con todo, el ahorro neto de C frente a B es de $3.940.000. Lo más probable es que la recomendación debiera ser el Plan C.
3. **2.1:** el solucionario incluye un literal c) (por qué importa el código de nivel bajo) que no aparece en el enunciado; el enunciado solo tiene a) y b).
4. **2.4:** el título y la tabla de puntos dicen «Silver-Meal vs. Wagner-Whitin», pero el enunciado solo pide calcular Silver-Meal. Wagner-Whitin aparece únicamente en el argumento b), sin números.
5. **1.4b:** las unidades se redondean de forma desigual: 491,25 → 491 y 436,7 → 437, mientras 327,5 se deja fraccional.
6. **Página 8:** las fórmulas del modelo están en el PDF como código LaTeX sin renderizar.
7. El árbol del BOM (2.1a) se pide dibujado, pero el solucionario solo da la tabla de niveles; no hay diagrama.

**Páginas clave**

| Páginas | Contenido |
|---|---|
| 1–2 | Instrucciones y tabla de puntos |
| 2–3 | Datos del Punto 1 (Tablas 1 y 2) |
| 3–4 | Preguntas 1.1 a 1.4 |
| 4–6 | Punto 2: BOM, Tabla 3, MPS, Tabla 4, datos de 2.4 |
| 6–7 | Rúbrica y criterios |
| 7–13 | Solucionario: 1.1–1.2 en pp. 7–8; 1.3 en pp. 8–9; 1.4 y 2.1 en p. 9; 2.2 en p. 10; 2.3 en pp. 10–12; 2.4 en pp. 12–13 |

**Relación con otros archivos del repo**

- Planeación agregada y modelo de costos:
  - [L10 Aggregate planning](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/L10-aggregate-planning.md);
  - [modelo-bowman](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/modelo-bowman.md);
  - [ejemplo-modelo-bowman](/corte-2-planeacion-agregada-mrp/01-planeacion-agregada-modelo-bowman/ejemplo-modelo-bowman.md).
- Agregación y desagregación (tiempo de agotamiento):
  - [L11](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/L11-aggregation-and-disaggregation.md);
  - [modelo-desagregacion](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion.md);
  - [modelo-desagregacion-v2](/corte-2-planeacion-agregada-mrp/02-agregacion-y-desagregacion/modelo-desagregacion-v2.md).
- Silver-Meal y Wagner-Whitin:
  - [L12](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/L12-wagner-whitin-and-silver-meal.md);
  - [wagner_whitin.py](/corte-2-planeacion-agregada-mrp/03-wagner-whitin-y-silver-meal/wagner_whitin.py).
- BOM, LLC y MRP:
  - [L13](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md);
  - [L14](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L14-mrp.md);
  - [calculo-demanda-dependiente-directa](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/calculo-demanda-dependiente-directa.md);
  - [mrp-esfero](/corte-2-planeacion-agregada-mrp/04-bom-y-mrp/mrp-esfero.md).
- MRP II (capacidad), tema posterior que no entra en el parcial: [L15](/corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md).

## Contenido completo (página por página)

> Convención numérica del documento: el punto separa miles y la coma separa decimales (2.400 = 2400; 1,5 = 1.5; $3.200.000 = 3 200 000 pesos colombianos). Se conserva tal cual en la transcripción. El documento es un Word convertido a PDF (no son diapositivas): el enunciado ocupa las páginas 1 a 7 y el **Solucionario**, de la página 7 a la 13.

### Página 1 — Parcial 2: instrucciones generales y distribución de puntos

**Parcial 2 – Planeación, Programación y Control de la Producción**

**Instrucciones generales**

Ingeniería Industrial · VII semestre · Duración: 2 horas · Valor: 100 puntos (nota = puntos / 20).

Nombre: ______________________________ Código: ____________ Fecha: ____________

1. El parcial se resuelve en papel, con lápiz o esfero. Se permite calculadora no programable; no se permiten celulares ni computador.
2. Todo resultado numérico debe ir acompañado del procedimiento. Un número sin procedimiento no suma puntos.
3. Las preguntas marcadas con **[Argumente]** exigen una justificación escrita de 3 a 6 líneas: qué decidió, por qué y qué supuesto usó.
4. Si considera que falta un dato, declare explícitamente el supuesto que adopta y continúe.
5. Los datos de cada punto son independientes: un error en una pregunta no se arrastra a la siguiente cuando esta trae sus propios datos.

**Distribución de puntos y competencia evaluada**

Competencia: habilidad para identificar, formular y resolver problemas complejos de ingeniería aplicando principios de ingeniería, ciencias y matemáticas.

| Pregunta | Tema | Puntos | Indicador 1: identifica elementos | Indicador 2: evalúa alternativas |
|---|---|---|---|---|
| 1.1 | Métodos de agregación | 10 | X | |
| 1.2 | Formulación de planeación agregada con programación matemática | 20 | X | |
| 1.3 | Evaluación de planes agregados alternativos | 20 | | X |
| 1.4 | Desagregación (tiempo de agotamiento igual) | 12 | X | X |

### Página 2 — Distribución de puntos (continuación), Punto 1 y Tablas 1 y 2

| Pregunta | Tema | Puntos | Indicador 1: identifica elementos | Indicador 2: evalúa alternativas |
|---|---|---|---|---|
| 2.1 | Bill of materials y códigos de nivel bajo | 5 | X | |
| 2.2 | Demanda dependiente directa | 10 | X | |
| 2.3 | Matriz MRP | 18 | X | |
| 2.4 | Lot sizing: Silver-Meal vs. Wagner-Whitin | 15 | | X |
| **Total** | | **110** | | |

**Punto 1. Sales and Operations Planning**

**Muebles Andinos S.A.S.** fabrica en una misma planta una familia de muebles de oficina. Los tres productos comparten la línea de corte, ensamble y pintura, y la mano de obra es polivalente. El comité de S&OP debe aprobar el plan de producción de los próximos cuatro meses.

**Tabla 1. Pronóstico de demanda (unidades) y tiempo estándar**

| Producto | Horas estándar por unidad | Mes 1 | Mes 2 | Mes 3 | Mes 4 |
|---|---|---|---|---|---|
| Escritorio (E) | 2,0 | 450 | 500 | 550 | 480 |
| Silla (S) | 1,5 | 400 | 440 | 600 | 520 |
| Archivador (A) | 3,0 | 300 | 300 | 400 | 380 |

**Tabla 2. Parámetros de capacidad y costos** (primera parte)

| Parámetro | Valor |
|---|---|
| Operarios al inicio del mes 1 | 16 |
| Horas regulares por operario al mes | 160 h |
| Costo de hora regular (se paga toda la jornada, se use o no) | $20.000 / h |
| Costo de hora extra | $30.000 / h |
| Límite de horas extra | 20 % de las horas regulares del mes |
| Costo de subcontratación | $38.000 / hora estándar |

### Página 3 — Tabla 2 (fin) y preguntas 1.1, 1.2 y 1.3

**Tabla 2** (continuación)

| Parámetro | Valor |
|---|---|
| Costo de contratar un operario | $1.500.000 |
| Costo de despedir un operario | $2.500.000 |
| Costo de mantener inventario | $2.000 / hora estándar / mes (sobre inventario final del mes) |
| Inventario inicial de la familia | 0 horas estándar |
| Faltantes (backorders) | No permitidos |

**1.1 Métodos de agregación (10 puntos)**

a) Calcule la demanda agregada de la familia para cada mes usando el método apropiado. (4 pts)

b) Exprese la demanda del mes 3 en **escritorios equivalentes** (unidad agregada = un escritorio). (2 pts)

c) **[Argumente]** Un analista propone agregar sumando unidades: "el mes 3 tiene 1.550 muebles". Explique si esta unidad de agregación es adecuada para este problema y qué condiciones deben cumplir los productos para que una agregación sea válida. (4 pts)

**1.2 Formulación del modelo de planeación agregada (20 puntos)**

Formule un modelo de **programación lineal entera** que minimice el costo total del horizonte de 4 meses. Su formulación debe incluir:

a) Conjuntos, parámetros y variables de decisión, indicando unidades de cada una. (5 pts)

b) Función objetivo. (3 pts)

c) Restricciones de: balance de inventario, balance de fuerza laboral, capacidad regular, límite de horas extra, y naturaleza de las variables. (10 pts)

d) **[Argumente]** ¿Qué variables deben ser enteras? ¿Qué pasaría con la solución si se relaja la integralidad y luego se redondea? (2 pts)

**1.3 Evaluación de planes alternativos (20 puntos)**

El comité recibió dos propuestas:

- **Plan A (persecución):** ajustar cada mes el número de operarios para producir exactamente la demanda en tiempo regular, sin horas extra ni inventario. Operarios por mes: 15, 16, 20, 18.
- **Plan B (nivelado):** mantener 16 operarios los cuatro meses; el excedente de un mes se guarda en inventario y el faltante se cubre primero con inventario y luego con horas extra.

a) Construya la tabla mes a mes de cada plan (producción regular, horas extra, inventario final, contrataciones, despidos) y verifique que ambos sean factibles frente a las restricciones de la Tabla 2. (5 pts)

b) Calcule el costo total de cada plan, discriminado por rubro. (5 pts)

c) **[Argumente]** Una tercera propuesta (Plan C) consiste en contratar **un** operario al inicio del mes 1 y mantener 17 operarios constantes, con la misma lógica del Plan B. Sin resolver el modelo de la 1.2, evalúe el Plan C, compárelo con A y B, y recomiende un plan al comité. Incluya en su argumento al *(continúa en la página 4)*

### Página 4 — 1.3c (fin), 1.4 Desagregación y Punto 2 (MRP): BOM, Tabla 3, 2.1 y 2.2

*(continuación de 1.3c)* menos un factor no monetario y explique por qué la subcontratación no aparece en ninguno de los planes. (10 pts)

**1.4 Desagregación (12 puntos)**

Para el mes 1 el comité aprobó **2.620 horas estándar** de producción para la familia. Los inventarios iniciales por producto son: Escritorios 40 u, Sillas 80 u, Archivadores 20 u. Use la demanda del mes 1 de la Tabla 1.

a) Desagregue las 2.620 horas en unidades a producir de cada producto. (7 pts)

b) **[Argumente]** Otro analista propone repartir las 2.620 horas en proporción a la demanda del mes, ignorando los inventarios. Explique cuál de los dos criterios recomienda y por qué. (5 pts)

**Punto 2. Material Requirements Planning**

La misma empresa lanza la **Mesa auxiliar (M)**. Su lista de materiales, descrita por el área de ingeniería, es:

- Cada mesa M se arma con 1 tablero (T), 1 estructura (S) y 1 kit de herrajes (K) que se empaca suelto en la caja.
- Cada estructura S se arma con 4 patas (P) y 2 kits de herrajes (K).
- T, P y K se compran a proveedores.

**Tabla 3. Datos de los ítems**

| Ítem | Tiempo de entrega (semanas) | Tamaño de lote |
|---|---|---|
| M | 1 | Lote a lote |
| T | 2 | Lote a lote |
| S | 1 | Lote a lote |
| P | 1 | Lote a lote |
| K | 1 | Lote a lote |

**2.1 Bill of materials (5 puntos)**

a) Dibuje el árbol de estructura del producto M indicando niveles y cantidades por padre. (4 pts)

b) Asigne el código de nivel bajo (low-level code) de cada ítem. (1 pts)

**2.2 Cálculo de demanda dependiente directa (10 puntos)**

Se recibe un pedido de **200 mesas**. Los inventarios disponibles son: M = 20, T = 30, S = 50, P = 100, K = 60. No hay recepciones programadas. Ignore los tiempos de entrega.

a) Calcule los requerimientos brutos y netos de cada ítem (M, T, S, P, K). (6 pts)

b) **[Argumente]** Un auxiliar calculó las patas como 4 × 200 = 800 y los kits como 200 + 2 × 200 = 600. Explique qué omitió, cuántas unidades de más compraría en cada caso y qué impacto tiene esto en el costo. (4 pts)

### Página 5 — 2.3 Matriz MRP (datos y formato) y 2.4 (inicio)

**2.3 Matriz MRP (18 puntos)**

El plan maestro de producción (MPS) de la mesa M para las próximas 8 semanas es:

| Semana | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| MPS de M (unidades) | 0 | 0 | 50 | 0 | 60 | 40 | 0 | 70 |

| Ítem | Inventario inicial | Recepciones programadas | Stock de seguridad |
|---|---|---|---|
| M | 20 | Ninguna | 0 |
| S | 30 | 40 u en la semana 2 | 0 |
| K | 50 | 60 u en la semana 1 | 0 |

a) Construya la matriz MRP de M, S y K para las 8 semanas, con lote a lote y los tiempos de entrega de la Tabla 3. Use el formato de la Tabla 4 (una matriz por ítem). (14 pts)

b) **[Argumente]** Explique de dónde provienen los requerimientos brutos de K en la semana 4 y qué órdenes debe liberar el planeador en las semanas 1 y 2. (4 pts)

**Tabla 4. Formato de matriz MRP (reproduzca en su hoja para M, S y K)** (plantilla vacía)

| Ítem: ___ LT: ___ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Requerimientos brutos | | | | | | | | |
| Recepciones programadas | | | | | | | | |
| Inventario proyectado (inicial: ___ ) | | | | | | | | |
| Requerimientos netos | | | | | | | | |
| Recepción de órdenes planeadas | | | | | | | | |
| Liberación de órdenes planeadas | | | | | | | | |

**2.4 Lot sizing: Silver-Meal y Wagner-Whitin (15 puntos)**

Para el tablero T (ítem comprado) se tienen los siguientes requerimientos netos: *(tabla en la página 6)*

### Página 6 — 2.4 (datos y preguntas) y rúbrica de calificación

| Semana | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Requerimientos netos (u) | 150 | 80 | 80 | 100 | 250 | 200 |

Costo de ordenar S = $300.000 por pedido. Costo de mantener h = $1.000 por unidad por semana. Un pedido llega al inicio de la semana en que se coloca; las unidades de la semana k pedidas en la semana j pagan (k − j) semanas de mantenimiento.

a) Determine el plan de pedidos con la heurística de **Silver-Meal** y su costo total. Muestre el costo por periodo en cada iteración. (10 pts)

b) **[Argumente]** ¿Por qué Silver-Meal no garantiza el óptimo en este caso? ¿En qué situación práctica preferiría Silver-Meal aunque no garantice el óptimo? (5 pts)

**Rúbrica de calificación por indicador**

Cada pregunta se califica asignando el porcentaje del nivel alcanzado sobre su puntaje. Los cálculos pesan la mitad del puntaje y el argumento la otra mitad en las preguntas marcadas **[Argumente]**.

| Indicador | Excelente (100 %) | Satisfactorio (75 %) | En desarrollo (40 %) | Insuficiente (0–10 %) |
|---|---|---|---|---|
| **1. Identifica los elementos del problema** | Distingue datos, parámetros, variables de decisión y restricciones; usa unidades coherentes (horas estándar, unidades por nivel); la estructura (modelo, BOM, matriz) es completa y correcta. | Estructura completa con un error menor de cálculo o de unidades que no altera la lógica. | Omite un elemento clave (una restricción, un nivel del BOM, el inventario de un nivel intermedio) o confunde parámetro con variable. | No identifica la estructura del problema o presenta resultados sin procedimiento. |
| **2. Evalúa soluciones alternativas** | Calcula correctamente el costo o desempeño de todas las alternativas, compara con un criterio explícito, recomienda y reconoce limitaciones o factores no monetarios. *(la frase termina en la página 7)* | Compara correctamente y recomienda, pero el argumento no discute limitaciones o supuestos. | Calcula las alternativas pero no las compara con un criterio claro, o la recomendación no se sigue de los cálculos. | Elige una alternativa sin cálculos ni justificación. |

### Página 7 — Rúbrica (fin), criterios para argumentos y Solucionario 1.1 y 1.2 (inicio)

*(Última celda de la rúbrica, indicador 2, nivel Excelente: "… limitaciones o factores no monetarios.")*

**Criterios para los argumentos escritos**

- Afirma una conclusión concreta (no "depende") y la respalda con al menos un número calculado.
- Hace explícito el supuesto o la condición bajo la cual su conclusión es válida.
- Usa el vocabulario técnico correcto (tiempo de agotamiento, código de nivel bajo, horizonte rodante, etc.).

**Consideración de error arrastrado:** si un resultado previo está mal pero el estudiante lo usa con procedimiento correcto en la pregunta siguiente, se otorga el puntaje de procedimiento de esa pregunta.

**Solucionario** (título de sección en el PDF)

Retire esta sección antes de imprimir el parcial. Montos en pesos colombianos; todos los cálculos fueron verificados.

**1.1 Agregación**

a) Demanda agregada en horas estándar = Σ (unidades × horas por unidad):

| Mes | Escritorios (h) | Sillas (h) | Archivadores (h) | Total (h estándar) |
|---|---|---|---|---|
| 1 | 900 | 600 | 900 | 2.400 |
| 2 | 1.000 | 660 | 900 | 2.560 |
| 3 | 1.100 | 900 | 1.200 | 3.200 |
| 4 | 960 | 780 | 1.140 | 2.880 |

(Ej.: mes 1 = 450 × 2,0 + 400 × 1,5 + 300 × 3,0 = 900 + 600 + 900 = 2.400 h.)

b) Mes 3: 3.200 h ÷ 2 h/escritorio = **1.600 escritorios equivalentes**.

c) Sumar unidades supone que un archivador (3 h) consume lo mismo que una silla (1,5 h); con otra mezcla, 1.550 muebles pueden requerir desde 2.325 h hasta 4.650 h. La unidad agregada debe medir el recurso restrictivo (horas de mano de obra). Condiciones: procesos y recursos compartidos, estructura de costos similar y una mezcla de productos relativamente estable.

(2.325 h = 1.550 × 1,5 si todos fueran sillas; 4.650 h = 1.550 × 3 si todos fueran archivadores.)

**1.2 Formulación**

Conjuntos: t = 1,…,4. Parámetros: D_t (Tabla de 1.1a, en h), W_0 = 16, I_0 = 0, 160 h/operario. Variables (t = 1,…,4): W_t operarios; H_t contratados; F_t despedidos; P_t horas regulares producidas; O_t horas extra; S_t horas subcontratadas; I_t inventario final (h estándar).

### Página 8 — Solucionario 1.2 (modelo), 1.2d y 1.3 (tablas de los planes A y B)

> En el PDF las dos fórmulas aparecen como **código LaTeX sin renderizar** (texto monoespaciado sobre fondo gris). Aquí se muestran renderizadas, con el mismo contenido.

$$\min Z=\sum_{t=1}^{4}\left(3.200.000\,W_t+30.000\,O_t+38.000\,S_t+1.500.000\,H_t+2.500.000\,F_t+2.000\,I_t\right)$$

$$
\begin{aligned}
& I_t = I_{t-1}+P_t+O_t+S_t-D_t && \forall t \\
& W_t = W_{t-1}+H_t-F_t && \forall t \\
& P_t \le 160\,W_t && \forall t \\
& O_t \le 0{,}2\cdot 160\,W_t = 32\,W_t && \forall t \\
& I_0=0,\; W_0=16 \\
& P_t,O_t,S_t,I_t \ge 0;\quad W_t,H_t,F_t \in \mathbb{Z}_{\ge 0} && \forall t
\end{aligned}
$$

Donde: $W_t$ operarios en el mes $t$; $H_t$ operarios contratados y $F_t$ despedidos al inicio del mes $t$; $P_t$ horas estándar producidas en tiempo regular; $O_t$ horas extra; $S_t$ horas estándar subcontratadas; $I_t$ inventario final (horas estándar); $D_t$ demanda agregada (horas estándar).

Nota: el costo regular es 160 h × $20.000 = $3.200.000 por operario-mes porque la jornada se paga completa. I_t ≥ 0 impide faltantes.

d) Deben ser enteras W_t, H_t y F_t (personas). Las horas pueden ser continuas. Redondear hacia abajo puede volver infactible el plan (capacidad insuficiente); redondear hacia arriba lo vuelve factible pero no necesariamente óptimo.

**1.3 Evaluación de planes**

| Mes | Demanda (h) | Plan A: operarios | Plan A: contrata / despide | Plan B: regular (h) | Plan B: extra (h) | Plan B: inventario final (h) |
|---|---|---|---|---|---|---|
| 1 | 2.400 | 15 | despide 1 | 2.560 | 0 | 160 |
| 2 | 2.560 | 16 | contrata 1 | 2.560 | 0 | 160 |
| 3 | 3.200 | 20 | contrata 4 | 2.560 | 480 | 0 |
| 4 | 2.880 | 18 | despide 2 | 2.560 | 320 | 0 |

Factibilidad: el límite de horas extra del Plan B es 0,2 × 2.560 = 512 h/mes; el máximo usado es 480 h (mes 3), así que es factible. El Plan A produce exactamente la demanda en tiempo regular.

| Rubro | Plan A | Plan B |
|---|---|---|
| Tiempo regular | 11.040 h → $220.800.000 | 10.240 h → $204.800.000 |
| Horas extra | $0 | 800 h → $24.000.000 |
| Inventario | $0 | 320 h·mes → $640.000 |
| Contrataciones | 5 → $7.500.000 | $0 |
| Despidos | 3 → $7.500.000 | $0 |
| **Total** | **$235.800.000** | **$229.440.000** |

(La tabla del PDF tiene una cuarta columna vacía, sin encabezado.)

### Página 9 — Solucionario 1.3c, 1.4 Desagregación y 2.1 BOM

c) Se recomienda el Plan B: ahorra dinero. Contratar un operario ($1.500.000) reemplaza 640 h de extra, que costaban $19.200.000. Factores no monetarios: estabilidad laboral y clima, costo de curva de aprendizaje de los contratados en el Plan A, y el riesgo de depender de horas extra si el pronóstico falla. La subcontratación ($38.000/h) es más cara que la hora extra ($30.000/h) y el límite de horas extra nunca se alcanza, así que nunca conviene.

> Nota del transcriptor: el texto dice «Se recomienda el Plan B», pero el argumento que sigue (contratar un operario reemplaza 640 h extra) es el del Plan C, y el solucionario no calcula el costo del Plan C. Ver la verificación en el Resumen: el Plan C cuesta $225.500.000 (cálculo propio) y es el más barato.

**1.4 Desagregación**

a) Tiempo de agotamiento común:

$$T^{*}=\frac{X+\sum_i I_i}{\sum_i d_i}=\frac{2620+(80+120+60)}{900+600+900}=\frac{2880}{2400}=1{,}2\ \text{meses}$$

($X$ = horas agregadas a producir; $I_i$ = inventario inicial del producto $i$ en horas estándar: 40 u × 2 = 80 h, 80 u × 1,5 = 120 h, 20 u × 3 = 60 h; $d_i$ = demanda del mes 1 en horas estándar.)

Producción de cada ítem, Y_i = T* × d_i − I_i (en horas), luego se divide por las horas por unidad:

| Producto | Inventario (h) | Demanda mes 1 (h) | Y_i (h) | Unidades a producir |
|---|---|---|---|---|
| Escritorio | 80 | 900 | 1.000 | 500 |
| Silla | 120 | 600 | 600 | 400 |
| Archivador | 60 | 900 | 1.020 | 340 |
| Total | 260 | 2.400 | 2.620 | — |

(Escritorio: 1,2 × 900 − 80 = 1.000 h ÷ 2 = 500 u; Silla: 1,2 × 600 − 120 = 600 h ÷ 1,5 = 400 u; Archivador: 1,2 × 900 − 60 = 1.020 h ÷ 3 = 340 u.)

b) Reparto proporcional a la demanda: Escritorios 982,5 h (491 u), Sillas 655 h (437 u), Archivadores 982,5 h (327,5 u). Tiempos de agotamiento: Escritorio (80 + 982,5)/900 = 1,18 meses; Silla (120 + 655)/600 = 1,29; Archivador (60 + 982,5)/900 = 1,16. Los archivadores se agotan primero mientras las sillas acumulan inventario. Se recomienda igual tiempo de agotamiento porque usa los inventarios existentes y deja toda la familia cubierta hasta el mismo instante. Limitación esperada en el argumento: no considera costos de alistamiento ni tamaños mínimos de lote.

**2.1 Bill of materials**

| Nivel | Ítem | Cantidad por padre | Padre | Código de nivel bajo |
|---|---|---|---|---|
| 0 | M | — | — | 0 |
| 1 | T | 1 | M | 1 |
| 1 | S | 1 | M | 1 |
| 1 | K | 1 | M | 2 |
| 2 | P | 4 | S | 2 |
| 2 | K | 2 | S | 2 |

> [Diagrama deducido de la tabla (el PDF no dibuja el árbol): M (nivel 0) → T ×1, S ×1, K ×1 (nivel 1); S → P ×4, K ×2 (nivel 2). K aparece en los niveles 1 y 2, por eso su código de nivel bajo es 2.]

c) MRP procesa cada ítem una sola vez, después de todos sus padres. Si K se procesara en el nivel 1, se neteraría contra el inventario solo con la demanda que viene de M, antes de conocer la que viene de S. *(continúa en la página 10)*

### Página 10 — Solucionario 2.1c (fin), 2.2 y 2.3 (matriz de M)

*(continuación)* El inventario se asignaría mal, se omitirían los requerimientos de S o K tendría que recalcularse, generando órdenes duplicadas o faltantes.

**2.2 Demanda dependiente directa**

| Ítem | Requerimiento bruto | Inventario | Requerimiento neto |
|---|---|---|---|
| M | 200 | 20 | 180 |
| T | 1 × 180 = 180 | 30 | 150 |
| S | 1 × 180 = 180 | 50 | 130 |
| P | 4 × 130 = 520 | 100 | 420 |
| K | 1 × 180 + 2 × 130 = 440 | 60 | 380 |

b) El auxiliar explotó el requerimiento bruto y no el neto de cada padre, e ignoró los inventarios. Patas: 800 − 420 = 380 u de más. Kits: 600 − 380 = 220 u de más. Eso infla compras, capital inmovilizado y costo de mantener.

**2.3 Matriz MRP**

| M (LT 1, inicial 20) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Requerimientos brutos | 0 | 0 | 50 | 0 | 60 | 40 | 0 | 70 |
| Recepciones programadas | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Inventario proyectado | 20 | 20 | 0 | 0 | 0 | 0 | 0 | 0 |
| Requerimientos netos | 0 | 0 | 30 | 0 | 60 | 40 | 0 | 70 |
| Recepción de órdenes planeadas | 0 | 0 | 30 | 0 | 60 | 40 | 0 | 70 |

*(La fila «Liberación de órdenes planeadas» de M está en la página 11.)*

### Página 11 — Solucionario 2.3 (liberaciones de M y matriz de S)

| M (LT 1, inicial 20) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Liberación de órdenes planeadas | 0 | 30 | 0 | 60 | 40 | 0 | 70 | 0 |

| S (LT 1, inicial 30) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Requerimientos brutos | 0 | 30 | 0 | 60 | 40 | 0 | 70 | 0 |
| Recepciones programadas | 0 | 40 | 0 | 0 | 0 | 0 | 0 | 0 |
| Inventario proyectado | 30 | 40 | 40 | 0 | 0 | 0 | 0 | 0 |
| Requerimientos netos | 0 | 0 | 0 | 20 | 40 | 0 | 70 | 0 |
| Recepción de órdenes planeadas | 0 | 0 | 0 | 20 | 40 | 0 | 70 | 0 |
| Liberación de órdenes planeadas | 0 | 0 | 20 | 40 | 0 | 70 | 0 | 0 |

(Brutos de S = liberaciones de M × 1. Semana 2: 30 + 40 − 30 = 40; semana 4: 40 − 60 → neto 20.)

### Página 12 — Solucionario 2.3 (matriz de K y 2.3b) y 2.4 (inicio)

| K (LT 1, inicial 50) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Requerimientos brutos | 0 | 30 | 40 | 140 | 40 | 140 | 70 | 0 |
| Recepciones programadas | 60 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Inventario proyectado | 110 | 80 | 40 | 0 | 0 | 0 | 0 | 0 |
| Requerimientos netos | 0 | 0 | 0 | 100 | 40 | 140 | 70 | 0 |
| Recepción de órdenes planeadas | 0 | 0 | 0 | 100 | 40 | 140 | 70 | 0 |
| Liberación de órdenes planeadas | 0 | 0 | 100 | 40 | 140 | 70 | 0 | 0 |

Brutos de K = liberaciones de M × 1 + liberaciones de S × 2.

(Semana 2: 30 de M; semana 3: 2 × 20 de S = 40; semana 4: 60 + 2 × 40 = 140; semana 5: 40 de M; semana 6: 2 × 70 = 140; semana 7: 70 de M.)

b) Semana 4 de K: 60 (liberación de M en la semana 4, × 1) + 80 (liberación de S de 40 en la semana 4, × 2) = 140. Semana 1: no se libera ninguna orden nueva; se recibe la orden abierta de 60 kits. Semana 2: liberar la orden de 30 mesas M. Puntaje adicional si el estudiante nota que la recepción de 40 estructuras en la semana 2 no se consume hasta la semana 4, por lo que podría reprogramarse (mensaje de acción de aplazar).

**2.4 Lot sizing**

a) Silver-Meal (costos en miles de pesos; costo por periodo = costo acumulado ÷ semanas cubiertas): *(tabla en la página 13)*

### Página 13 — Solucionario 2.4 (tabla Silver-Meal y argumento)

| Inicio | Semanas cubiertas | Costo acumulado | Costo por periodo | Decisión |
|---|---|---|---|---|
| Semana 1 | 1 | 300 | 300 | sigue |
| Semana 1 | 1–2 | 300 + 80 = 380 | 190 | sigue |
| Semana 1 | 1–3 | 380 + 160 = 540 | 180 | sigue |
| Semana 1 | 1–4 | 540 + 300 = 840 | 210 | sube: lote 1–3 |
| Semana 4 | 4 | 300 | 300 | sigue |
| Semana 4 | 4–5 | 300 + 250 = 550 | 275 | sigue |
| Semana 4 | 4–6 | 550 + 400 = 950 | 316,7 | sube: lote 4–5 |
| Semana 6 | 6 | 300 | 300 | fin |

(Los incrementos son h × (k − j) × D_k en miles: 80 × 1 = 80; 80 × 2 = 160; 100 × 3 = 300; 250 × 1 = 250; 200 × 2 = 400.)

Plan Silver-Meal: 310 u en la semana 1, 350 u en la semana 4 y 200 u en la semana 6. Costo total = 540 + 550 + 300 = **$1.390.000**.

b) Silver-Meal es miope: cierra el lote en el primer mínimo local del costo por periodo. Al unir la semana 3 con 1–2 obliga a pedir en la semana 4 y termina uniendo 4 con 5, cuando lo óptimo es unir 3 con 4 y 5 con 6. Se preferiría Silver-Meal con horizonte rodante y demanda que se actualiza cada semana, pues el óptimo de Wagner-Whitin solo vale para un horizonte fijo y conocido, cambia al llegar nueva información y genera nerviosismo en el plan; además, es fácil de calcular y explicar a planta.
