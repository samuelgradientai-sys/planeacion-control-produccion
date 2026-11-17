# L02-introduction-to-production-systems

> **Archivo:** [`L02-introduction-to-production-systems.pdf`](./L02-introduction-to-production-systems.pdf) · **Corte 1** · 22 páginas  
> **Nombre original:** `CORTE 1/lec 2 Introduction-to-Production-Systems.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** configuraciones de los sistemas de producción (flowshop, jobshop y openshop), sus medidas de desempeño y las estrategias de control de piso (push, pull, Kanban y ConWIP). Es la Lecture 2 del corte 1; las diapositivas se hicieron con Gamma.

**Ideas clave:**

- Un sistema de producción es el conjunto de procesos y recursos que crean bienes o servicios. La configuración determina cómo fluyen los productos entre estaciones.
- **Flowshop:** todos los productos siguen la misma secuencia fija de estaciones (p. ej., una línea de ensamble de autos). Sirve para alto volumen de productos estandarizados. Es eficiente y tiene poca variabilidad, pero poca flexibilidad.
- **Jobshop:** cada referencia tiene su propia ruta. En el ejemplo, la ref 1 va A→C, la ref 2 va B→A→C y la ref 3 va C→A→B. Es flexible, admite productos personalizados y lotes pequeños (muebles a medida, herramientas especiales). Su programación es compleja.
- **Openshop:** la ruta no es estricta, porque cualquier máquina puede hacer cualquier operación y el orden de visita es libre. Es muy variable y difícil de programar y gestionar.
- **Medidas de desempeño:** WIP (trabajo promedio en proceso), *takt time* (ritmo al que hay que terminar un producto para cumplir la demanda), *throughput* (tasa de salida de producto terminado), *cycle time* (tiempo de inicio a fin de un producto), *lead time* (tiempo hasta entregar al cliente) y eficiencia (qué tan bien se usan los recursos).
- **Control de piso:** son los métodos para gestionar el flujo de trabajo en planta. Buscan eficiencia, menos retrasos y cumplir la demanda.
  - **Push:** produce según un programa o pronóstico predeterminado, sin importar la demanda real. Genera más WIP e inventario, y aparecen cuellos de botella si el programa no se alinea con la demanda.
  - **Pull:** produce solo cuando la demanda real lo pide. Está ligado a *lean manufacturing*, reduce desperdicio e inventario y responde mejor a los cambios.
  - **Kanban** («letrero» o «tarjeta» en japonés): nació en el sistema de producción de Toyota en los años 1940. Usa tarjetas o tableros como señales visuales, de modo que cada estación «jala» trabajo solo cuando está lista. Reduce el WIP, deja ver los cuellos de botella y promueve la mejora continua.
  - **ConWIP** (solo en el diagrama de la página 19): una única tarjeta va del final de la línea al inicio y limita el WIP total de la línea.
- Cuándo usar cada estrategia: push para alto volumen, productos estándar y demanda estable; pull para demanda variable cuando se busca reducir desperdicio; Kanban es versátil y se adapta a muchos entornos.
- La página 1 trae reglas de debate (Musgrave, 1957) para una actividad en clase, y la página 2 recomienda leer el capítulo 1 de *Factory Physics* (Hopp & Spearman, 2001, 2.ª ed.).

**Fórmulas y métodos:**

La presentación no trae fórmulas: las medidas de desempeño se definen solo con palabras (páginas 8–9). Como **complemento que no aparece en las diapositivas**, estas son las relaciones estándar que suelen acompañar esas definiciones (por ejemplo, en *Factory Physics*, el libro recomendado):

- Takt time: $\text{Takt} = \dfrac{\text{tiempo disponible de producción en el periodo}}{\text{demanda del cliente en el periodo}}$.
- Ley de Little: $WIP = TH \times CT$, donde $WIP$ es el inventario promedio en proceso (unidades), $TH$ el *throughput* (unidades por unidad de tiempo) y $CT$ el *cycle time* promedio.

Métodos que sí presenta: la clasificación de configuraciones (flowshop, jobshop, openshop) y las estrategias de control de piso (push, pull, Kanban y ConWIP), con su comparación (páginas 10, 17 y 22) y el diagrama de flujo de información (página 19).

**Ejemplos resueltos:** no hay ejercicios numéricos. Ejemplos ilustrativos:

- Página 4: flujo lineal Station 1→2→3 (flowshop).
- Página 5: tabla de rutas de 3 referencias en 3 estaciones (jobshop).
- Página 7: rutas «Not strict» (openshop).
- Página 19: diagrama Push / Kanban / ConWIP.

**Páginas clave:**

- Reglas del debate: página 1.
- Lectura recomendada: página 2.
- Flowshop: páginas 4 y 13.
- Jobshop: páginas 5–6.
- Openshop: página 7.
- Medidas de desempeño: páginas 8–9.
- Comparación de configuraciones: página 10.
- Control de piso: página 14.
- Push: página 15.
- Pull: página 16.
- Push vs. pull: página 17.
- Kanban: páginas 18, 20 y 21.
- Diagrama Push/Kanban/ConWIP: página 19.
- Conclusión: página 22.

**Relación con otros archivos del repo:**

- Las configuraciones de esta clase son los problemas de programación del corte 3:
  - [introducción a scheduling](../../corte-3-programacion-scheduling/01-introduccion-scheduling/L16-intro-scheduling.md)
  - [flow shop](../../corte-3-programacion-scheduling/04-flow-shop/L19-flow-shop-scheduling.md) y su Excel [flowshop-scheduling](../../corte-3-programacion-scheduling/04-flow-shop/flowshop-scheduling.md)
  - [job shop](../../corte-3-programacion-scheduling/05-job-shop/job-shop-y-flexible-job-shop.md)
- La lógica push (producir según un pronóstico o un plan) es la del pronóstico (corte 1) → planeación agregada → MRP (corte 2):
  - [L13 BOM e introducción a MRP](../../corte-2-planeacion-agregada-mrp/04-bom-y-mrp/L13-bom-intro-to-mrp.md)
  - [L15 MRP II](../../corte-2-planeacion-agregada-mrp/05-mrp-ii-y-capacidad/L15-mrp-ii.md)
- Presentación anterior del curso: [L01 introducción al curso](./L01-introduccion-al-curso.md).

## Contenido completo (página por página)

### Página 1 — Debate Rules

Condensed from *Competitive Debate: Rules and Techniques*, by George McCoy Musgrave. New York: H.W. Wilson, 1957)

1. There are two teams.
2. Each team has two constructive speeches (1 minute), and one rebuttal speech (40 seconds). The affirmative gives the first constructive speech, and the rebuttals alternate: negative, affirmative, negative, affirmative. The affirmative has both the first and last speeches of the debate.
3. The affirmative must advocate everything required by the topic itself. No revision of position of a team is permitted during the debate.
4. He who asserts must prove. In order to establish an assertion, the team must support it with enough evidence and logic to convince an intelligent but previously uninformed person that it is more reasonable to believe the assertion than to disbelieve it. Facts must be accurate. Visual materials are not permissible, and if introduced, they become available for the opponents' use if desired.
5. The judge must base his decision entirely on the material presented, without regard for other material which he may happen to possess.

> Nota (deducido): la diapositiva no dice el tema del debate. Por el resto de la presentación, probablemente se debatía entre configuraciones de producción o entre estrategias *push* y *pull*.

### Página 2 — Recommended Reading: term 1

- **Cap 1**, from the book:
  J.. Hopp, & Mark L.. Spearman. (2001). Factory Physics: Foundations of Manufacturing Management. Irwin/McGraw-Hill.Ed. 2.

> [Imagen: portada del libro *Factory Physics, Second Edition*: un científico de pelo blanco escribiendo en un tablero y un operario recostado sobre un engranaje.]

### Página 3 — Introduction to Production Systems

Production systems refer to the processes and resources used to create goods or services. Different configurations exist, each with unique characteristics and applications. This presentation will explore flowshop, jobshop, and openshop configurations, along with key performance measures.

> [Imagen decorativa: logo de la Universidad de La Sabana sobre la foto de una planta industrial con maquinaria azul.]

### Página 4 — Flowshop Configuration

> [Diagrama: flujo lineal **→ STATION 1 → STATION 2 → STATION 3 →** con flechas amarillas. Todos los productos entran por la estación 1 y salen por la 3 en el mismo orden. Íconos: STATION 1 con una hoja de sierra (corte), STATION 2 con una brocha (pintura), STATION 3 con una carretilla (despacho/transporte).]

| Characteristics | Example | Advantages |
|---|---|---|
| In a flowshop, products follow a fixed sequence of operations. This configuration is suitable for **high-volume production** of **standardized** products, such as automobiles or electronics. | Imagine a car assembly line where each station performs a specific task in a predetermined order. This represents a flowshop system. | Flowshops are known for their efficiency, due to streamlined operations and minimal process variability. |

### Página 5 — Jobshop Configuration

| Product Reference | Production Route |
|---|---|
| Product ref 1, | Station A – station C |
| Product ref 2 | Station B – station A – station C |
| Product ref 3 | Station C – station A – station B |

> [Diagrama: tres cajas separadas, **STATION A** (ícono de sierra), **STATION B** (ícono de brocha) y **STATION C** (ícono de carretilla), sin flechas entre ellas: cada producto sigue su propia ruta, dada en la tabla.]

> [Imagen decorativa: foto de un taller industrial (marca de agua de Alamy) y sello «Made with Gamma».]

### Página 6 — Jobshop Configuration

1. **Flexibility** — Jobshops are highly flexible, allowing for the production of **customized products** with varying production sequences.
2. **Variety** — This configuration handles a wide range of products and orders, making it ideal for small batch production or unique projects.
3. **Examples** — Examples include custom furniture manufacturing or specialized tool fabrication, where each product has a unique production route.
4. **Scheduling Complexity** — Jobshops present challenges in scheduling due to the variability in product orders and routes.

> [Imagen decorativa: la misma foto del taller industrial.]

### Página 7 — Openshop Configuration

| Product Reference | Production Route |
|---|---|
| Product ref 1 | Not strict |
| Product ref 2 | Not strict |
| Product ref 3 | Not strict |

> [Diagrama: tres cajas, **STATION 1**, **STATION 2** y **STATION 3**, sin flechas: el orden de visita no es fijo.]

- **Machine Flexibility** — In an openshop, machines can handle any type of operation, allowing for greater flexibility in production routes.
- **Unpredictable Routing** — Product orders can be processed in any order, resulting in unpredictable production routes. This can lead to challenges in scheduling and resource allocation.
- **Example** — Imagine a workshop where various machines can perform different operations on any product, allowing for a wide range of production possibilities.
- **High Variability** — Openshops are characterized by high variability in product orders and production sequences, making them challenging to manage.

> [Imagen decorativa: foto de brazos robóticos industriales amarillos en una celda de manufactura.]

### Página 8 — Performance Measures: WIP, Takt Time, and Throughput

1. **Work-in-Progress (WIP)** — Measures the average amount of work that is currently in progress within a production system.
2. **Takt Time** — Represents the rate at which a product needs to be completed to meet customer demand.
3. **Throughput** — Indicates the rate at which a production system produces finished goods or services over a given period.

> [Imagen decorativa: captura de un tablero de producción genérico: «Quick Stats» 99,474 Production Volume, 45 Active Machines, 77,662 Quantity Ordered, 1.12M Sales Revenue; «Downtime» 4.45 %; «Top 5 Products»; «Production Volume by Top 5 Machines» (9 %, 7 %, 5 %, 4 %…); «Returned Items by Reason». Es una imagen de ejemplo, no son datos del curso.]

### Página 9 — Other Performance Measures

| Measure | Definition |
|---|---|
| Cycle Time | The total time it takes to complete a product from start to finish. |
| Lead Time | The time it takes to deliver a finished product to the customer. |
| Efficiency | Measures how well resources are utilized and how effectively products are produced. |

> [Imagen decorativa: operario con casco rojo en una planta; sello «Made with Gamma».]

### Página 10 — Comparison of Production System Configurations

| 1. Flowshop | 2. Jobshop | 3. Openshop |
|---|---|---|
| High volume, standardized products, efficient operations, low flexibility. | Customizable products, flexible operations, complex scheduling, lower volume. | High variability, flexible machines, unpredictable routing, challenging to manage. |

> [Imagen decorativa: banda superior con una línea de brazos robóticos naranjas a ambos lados de un transportador; sello «Made with Gamma».]

### Página 11 — Conclusion and Key Takeaways

Production system configurations offer different advantages and challenges depending on the specific industry, product, and production needs. Understanding these configurations and their performance measures is crucial for optimizing production processes and achieving business goals.

> [Imagen decorativa: primer plano de una cadena de transmisión industrial (Alamy); sello «Made with Gamma».]

### Página 12 — Shop Floor Control Strategies in Flowshop Systems

This presentation will explore shop floor control strategies in flowshop systems. We will delve into the definition and importance of flowshop systems, and then examine different control strategies.

> [Imagen decorativa: ilustración de una línea de producción con bandas transportadoras y cajas naranjas.]

### Página 13 — Introduction to Flowshop Systems

Flowshop systems are a type of manufacturing process where jobs move through a series of workstations in a fixed sequence. The order of workstations is determined by the manufacturing process. Each workstation performs a specific task on the job.

| Definition of Flowshop Systems | Importance in Manufacturing | Examples of Industries Using Flowshop Systems |
|---|---|---|
| A flowshop system is a type of manufacturing process where jobs move through a series of workstations in a fixed sequence. This sequence is determined by the manufacturing process and each workstation performs a specific task on the job. | Flowshop systems are crucial in manufacturing for improving efficiency and productivity. They optimize resource utilization and ensure a smooth flow of products through the production process. | Flowshop systems are used in a variety of industries, including automotive, electronics, food processing, and pharmaceuticals. They are particularly valuable in industries with high production volumes and standardized products. |

> [Imagen decorativa: banda superior con la ilustración de una máquina industrial naranja.]

### Página 14 — Overview of Shop Floor Control Strategies

Shop floor control strategies are a set of methods used to manage and optimize the flow of work on the factory floor. These strategies aim to ensure efficient production, minimize delays, and meet customer demands.

**Definition and Purpose** — Shop floor control strategies are a set of methods used to manage and optimize the flow of work on the factory floor. Their purpose is to ensure efficient production, minimize delays, and meet customer demands.

**Key Strategies**

1. Push
2. Pull
3. Kanban

### Página 15 — Push Strategy: How it Works

The push strategy relies on a predetermined production schedule or forecast. Work is pushed through the system regardless of actual demand.

- **Production Schedule** — A push system follows a predetermined production schedule, regardless of actual demand.
- **Work-in-Progress** — Work is pushed through the system, leading to higher levels of work-in-progress and potential waste.
- **Inventory Management** — Push systems often involve higher levels of inventory to meet anticipated demand.
- **Potential Bottlenecks** — Bottlenecks can occur if the production schedule is not aligned with actual demand.

> [Imagen decorativa: ilustración isométrica de una máquina con tuberías naranjas; íconos de reloj, fábrica, calendario y alerta junto a cada punto.]

### Página 16 — Pull Strategy: How it Works

The pull strategy operates on the principle of actual demand. Work is pulled through the system only when it is needed.

- **Kanban** — Kanban is a popular pull strategy that uses visual signals to manage the flow of work.
- **Lean Manufacturing** — Pull systems are often associated with lean manufacturing principles, which focus on eliminating waste and maximizing efficiency.

> [Imagen decorativa: dos fotos ilustrativas, un tablero Kanban con notas adhesivas de colores y una línea de producción con tarjetas naranjas.]

### Página 17 — Push vs. Pull Strategies

Push and pull are two contrasting shop floor control strategies that offer different approaches to managing the flow of work.

| Push | Pull |
|---|---|
| Work is pushed through the system based on a predetermined schedule or forecast. | Work is pulled through the system based on actual demand. |
| Can lead to excess inventory and waste. | Reduces waste and inventory levels. |
| Less responsive to changes in demand. | More responsive to changes in demand. |

> [Imagen decorativa: ilustración generada por IA de un diagrama de procesos con texto ilegible.]

### Página 18 — Understanding Kanban

Kanban is a popular shop floor control strategy that relies on visual signals to manage the flow of work. It uses cards, boards, and signals to communicate task status and control inventory levels.

1. **Definition of Kanban** — Kanban is a shop floor control strategy that relies on visual signals to manage the flow of work. It uses cards, boards, and signals to communicate task status and control inventory levels.
2. **Origins and Principles** — Kanban originated in Toyota's production system and is based on the principle of pulling work through the system based on actual demand.
3. **How Kanban Works in Flowshop Systems** — In a flowshop system, Kanban can be used to track the movement of jobs through workstations, ensuring that each workstation only pulls in work when it is ready for it.
4. **Benefits of Using Kanban** — Kanban can improve efficiency by reducing work-in-progress, identifying bottlenecks, and enabling faster response times.

> [Imagen decorativa: tablero Kanban con notas adhesivas de colores.]

### Página 19 — (sin título) Push, Kanban y ConWIP

> [Diagrama: tres líneas de producción idénticas, cada una con la secuencia **Workstation → Buffer → Workstation → Buffer → Workstation → Buffer →** (rectángulo = estación, triángulo = buffer). Lo que cambia es el flujo de información (flechas punteadas):
> - **Push:** una sola flecha punteada «Production order» entra a la primera estación. La orden de producción empuja el material por toda la línea, sin señal de regreso.
> - **Kanban:** tres flechas punteadas curvas rotuladas «Kanban Card». Cada una va del buffer de salida de una estación de vuelta a esa misma estación: cada estación produce solo cuando su buffer consume una tarjeta (control local, etapa por etapa).
> - **ConWIP:** una sola flecha punteada larga, «ConWIP Card», va del buffer final de la línea de vuelta a la primera estación: el trabajo en proceso total de la línea queda limitado por un número fijo de tarjetas (control global).
> Leyenda: rectángulo = **Workstation**; triángulo = **Buffer**; flecha continua = **Physical flow**; flecha punteada = **Information flow**.]

### Página 20 — Definition and Origins of Kanban

Kanban, meaning "signboard" or "card" in Japanese, originated in Toyota's production system in the 1940s. It evolved from a system used to manage production in the automotive industry.

1. **Early Stages** — In the early days of Toyota, production was often chaotic and inefficient. Kanban was developed as a way to improve the flow of work and reduce waste.
2. **Development of the Kanban System** — Kanban initially involved the use of physical cards to track the movement of parts and materials through the production line.
3. **Evolution of Kanban** — The Kanban system has evolved over time, with the introduction of digital tools and software to manage tasks and processes.

> [Imagen decorativa: notas adhesivas sobre una pared.]

### Página 21 — Principles and Benefits of Kanban in Flowshop Systems

Kanban's principles and benefits, when applied to flowshop systems, contribute to a more efficient and responsive production environment.

1. **Visual Signal** — Kanban uses visual signals to communicate the status of work, facilitating better visibility and coordination.
2. **Pull System** — Kanban operates on a pull system, where workstations pull in work only when they are ready, reducing unnecessary work-in-progress.
3. **Continuous Improvement** — Kanban promotes continuous improvement by encouraging teams to identify bottlenecks and optimize processes.

> [Imagen decorativa: ilustración isométrica de una oficina con un tablero Kanban; sello «Made with Gamma».]

### Página 22 — Conclusion: Choosing the Right Strategy

The choice between push, pull, and Kanban strategies depends on various factors, including production volume, product complexity, and customer demand.

1. **Push** — Suitable for high-volume production with standardized products and a stable demand.
2. **Pull** — More appropriate for products with variable demand and a focus on reducing waste.
3. **Kanban** — A versatile option that can be implemented in various settings, offering flexibility and adaptability.

> [Imagen decorativa: ilustración generada por IA con flechas y círculos y texto sin sentido («Peeslicn», «Pulsn», «Pedeng»).]

## Anexo: texto extraído automáticamente del PDF

> Texto plano tal como sale del PDF, sin fórmulas ni tablas que estén como imagen. La versión fiel y completa es la sección «Contenido completo» de arriba.

### Página 1

Debate Rules
Condensed from Competitive Debate: Rules and Techniques, by George McCoy Musgrave. New York: H.W. 
Wilson, 1957)
1. There are two teams.
2. Each team has two constructive speeches (1 minute), and one rebuttal speech (40 seconds). The affirmative 
gives the first constructive speech, and the rebuttals alternate: negative, affirmative, negative, affirmative. 
The affirmative has both the first and last speeches of the debate.
3. The affirmative must advocate everything required by the topic itself. No revision of position of a team is 
permitted during the debate.
4. He who asserts must prove. In order to establish an assertion, the team must support it with enough 
evidence and logic to convince an intelligent but previously uninformed person that it is more reasonable to 
believe the assertion than to disbelieve it. Facts must be accurate. Visual materials are not permissible, and if 
introduced, they become available for the opponents' use if desired.
5. The judge must base his decision entirely on the material presented, without regard for other material 
which he may happen to possess.

### Página 2 · 1 imagen(es)

• Cap 1, from the book:
J.. Hopp, & Mark L.. Spearman. 
(2001). Factory Physics: Foundations 
of Manufacturing Management. 
Irwin/McGraw-Hill.Ed. 2. 
Recommended Reading: term 1

### Página 3 · 3 imagen(es)

Introduction to 
Production 
Systems
Production systems refer to the processes and resources used 
to create goods or services. Different configurations exist, each 
with unique characteristics and applications. This presentation 
will explore flowshop, jobshop, and openshop configurations, 
along with key performance measures.

### Página 4

Flowshop Configuration
Characteristics
In a flowshop, products follow a 
fixed sequence of operations. 
This configuration is suitable for 
high-volume production of 
standardized products, such as 
automobiles or electronics.
Example
Imagine a car assembly line 
where each station performs a 
specific task in a predetermined 
order. This represents a 
flowshop system.
Advantages
Flowshops are known for their 
efficiency, due to streamlined 
operations and minimal process 
variability.
STATION 1
STATION 2
STATION 3

### Página 5 · 3 imagen(es)

Jobshop Configuration
preencoded.png
Product Reference
Production Route
Product ref 1,
Station A – station C
Product ref 2
Station B – station A – station C
Product ref 3
Station C – station A – station B
STATION A
STATION B
STATION C

### Página 6 · 2 imagen(es)

Jobshop Configuration
1
Flexibility
Jobshops are highly flexible, allowing for the production of customized products 
with varying production sequences.
2
Variety
This configuration handles a wide range of products and orders, making it ideal for 
small batch production or unique projects.
3
Examples
Examples include custom furniture manufacturing or specialized tool fabrication, 
where each product has a unique production route.
4
Scheduling Complexity
Jobshops present challenges in scheduling due to the variability in product orders 
and routes.

### Página 7 · 2 imagen(es)

Openshop Configuration
Machine Flexibility
In an openshop, machines can handle any type of operation, allowing for greater flexibility in 
production routes.
Unpredictable Routing
Product orders can be processed in any order, resulting in unpredictable production routes. 
This can lead to challenges in scheduling and resource allocation.
Example
Imagine a workshop where various machines can perform different operations on any 
product, allowing for a wide range of production possibilities.
High Variability
Openshops are characterized by high variability in product orders and production 
sequences, making them challenging to manage.
STATION 1
STATION 2
STATION 3
Product Reference
Production Route
Product ref 1
Not strict
Product ref 2
Not strict
Product ref 3
Not strict

### Página 8 · 2 imagen(es)

Performance Measures: WIP, Takt 
Time, and Throughput
1
Work-in-Progress (WIP)
Measures the average amount of work that is currently in progress 
within a production system.
2
Takt Time
Represents the rate at which a product needs to be completed to 
meet customer demand.
3
Throughput
Indicates the rate at which a production system produces finished 
goods or services over a given period.

### Página 9 · 3 imagen(es)

Other Performance 
Measures
Cycle Time
The total time it takes to 
complete a product from 
start to finish.
Lead Time
The time it takes to 
deliver a finished product 
to the customer.
Efficiency
Measures how well 
resources are utilized and 
how effectively products 
are produced.
preencoded.png

### Página 10 · 5 imagen(es)

Comparison of Production System 
Configurations
Flowshop
High volume, standardized 
products, efficient operations, 
low flexibility.
Jobshop
Customizable products, flexible 
operations, complex scheduling, 
lower volume.
Openshop
High variability, flexible 
machines, unpredictable routing, 
challenging to manage.
preencoded.png

### Página 11 · 3 imagen(es)

Conclusion and Key 
Takeaways
Production system configurations offer different advantages 
and challenges depending on the specific industry, product, 
and production needs. Understanding these configurations and 
their performance measures is crucial for optimizing 
production processes and achieving business goals.
preencoded.png

### Página 12 · 1 imagen(es)

Shop Floor 
Control Strategies 
in Flowshop 
Systems
This presentation will explore shop floor control strategies in 
flowshop systems. We will delve into the definition and 
importance of flowshop systems, and then examine different 
control strategies.

### Página 13 · 1 imagen(es)

Introduction to Flowshop Systems
Flowshop systems are a type of manufacturing process where jobs move through a series of workstations in a fixed 
sequence. The order of workstations is determined by the manufacturing process. Each workstation performs a 
specific task on the job.
Definition of Flowshop 
Systems
A flowshop system is a type of 
manufacturing process where 
jobs move through a series of 
workstations in a fixed 
sequence. This sequence is 
determined by the 
manufacturing process and 
each workstation performs a 
specific task on the job.
Importance in 
Manufacturing
Flowshop systems are crucial 
in manufacturing for improving 
efficiency and productivity. 
They optimize resource 
utilization and ensure a smooth 
flow of products through the 
production process.
Examples of Industries 
Using Flowshop Systems
Flowshop systems are used in 
a variety of industries, 
including automotive, 
electronics, food processing, 
and pharmaceuticals. They are 
particularly valuable in 
industries with high production 
volumes and standardized 
products.

### Página 14

Overview of Shop Floor Control Strategies
Shop floor control strategies are a set of methods used to manage and optimize the flow of work on the factory 
floor. These strategies aim to ensure efficient production, minimize delays, and meet customer demands.
Definition and Purpose
Shop floor control strategies are a set of methods 
used to manage and optimize the flow of work on 
the factory floor. Their purpose is to ensure efficient 
production, minimize delays, and meet customer 
demands.
Key Strategies
1.
Push
2. Pull
3. Kanban

### Página 15 · 5 imagen(es)

Push Strategy: How it Works
The push strategy relies on a predetermined production schedule or forecast. Work is pushed 
through the system regardless of actual demand.
Production Schedule
A push system follows a predetermined production schedule, regardless of actual demand.
Work-in-Progress
Work is pushed through the system, leading to higher levels of work-in-progress and potential 
waste.
Inventory Management
Push systems often involve higher levels of inventory to meet anticipated demand.
Potential Bottlenecks
Bottlenecks can occur if the production schedule is not aligned with actual demand.

### Página 16 · 2 imagen(es)

Pull Strategy: How it Works
The pull strategy operates on the principle of actual demand. Work is pulled through the system only when it is 
needed.
Kanban
Kanban is a popular pull strategy that uses visual 
signals to manage the flow of work.
Lean Manufacturing
Pull systems are often associated with lean 
manufacturing principles, which focus on eliminating 
waste and maximizing efficiency.

### Página 17 · 1 imagen(es)

Push vs. Pull Strategies
Push and pull are two contrasting shop floor control strategies 
that offer different approaches to managing the flow of work.
Push
Pull
Work is pushed through 
the system based on a 
predetermined schedule or 
forecast.
Work is pulled through the 
system based on actual 
demand.
Can lead to excess 
inventory and waste.
Reduces waste and 
inventory levels.
Less responsive to 
changes in demand.
More responsive to 
changes in demand.

### Página 18 · 1 imagen(es)

Understanding Kanban
Kanban is a popular shop floor control strategy that relies on visual signals to manage the flow of 
work. It uses cards, boards, and signals to communicate task status and control inventory levels.
1
Definition of Kanban
Kanban is a shop floor control strategy that relies on visual signals to manage the flow of 
work. It uses cards, boards, and signals to communicate task status and control inventory 
levels.
2
Origins and Principles
Kanban originated in Toyota's production system and is based on the principle of pulling 
work through the system based on actual demand.
3
How Kanban Works in Flowshop Systems
In a flowshop system, Kanban can be used to track the movement of jobs through 
workstations, ensuring that each workstation only pulls in work when it is ready for it.
4
Benefits of Using Kanban
Kanban can improve efficiency by reducing work-in-progress, identifying bottlenecks, 
and enabling faster response times.

### Página 19 · 1 imagen(es)

_(sin texto: página solo con imágenes)_

### Página 20 · 1 imagen(es)

Definition and Origins of Kanban
Kanban, meaning "signboard" or "card" in Japanese, originated in Toyota's production system in 
the 1940s. It evolved from a system used to manage production in the automotive industry.
1
Early Stages
In the early days of Toyota, production was often chaotic and inefficient. Kanban 
was developed as a way to improve the flow of work and reduce waste.
2
Development of the Kanban System
Kanban initially involved the use of physical cards to track the movement of parts 
and materials through the production line.
3
Evolution of Kanban
The Kanban system has evolved over time, with the introduction of digital tools 
and software to manage tasks and processes.

### Página 21 · 5 imagen(es)

Principles and Benefits of Kanban in 
Flowshop Systems
Kanban's principles and benefits, when applied to flowshop systems, contribute to a more 
efficient and responsive production environment.
Visual Signal
Kanban uses visual signals to communicate the status of work, facilitating better 
visibility and coordination.
Pull System
Kanban operates on a pull system, where workstations pull in work only when they 
are ready, reducing unnecessary work-in-progress.
Continuous Improvement
Kanban promotes continuous improvement by encouraging teams to identify 
bottlenecks and optimize processes.
preencoded.png

### Página 22 · 1 imagen(es)

Conclusion: Choosing the Right 
Strategy
The choice between push, pull, and Kanban strategies depends on various factors, including 
production volume, product complexity, and customer demand.
1
Push
Suitable for high-volume production with standardized products and a 
stable demand.
2
Pull
More appropriate for products with variable demand and a focus on 
reducing waste.
3
Kanban
A versatile option that can be implemented in various settings, offering 
flexibility and adaptability.

