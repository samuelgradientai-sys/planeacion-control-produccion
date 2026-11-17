# THYMS-presentacion-corte-2

> **Archivo:** [`THYMS-presentacion-corte-2.pdf`](./THYMS-presentacion-corte-2.pdf) · **Corte 2** · 9 páginas  
> **Nombre original:** `CORTE 2/THYMS Presentacion Corte 2.pdf`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Resumen

**Tema:** presentación del grupo con el entregable del Corte 2 sobre THYMS Colombia S.A.S. (6 de octubre de 2026): S&OP apoyado en un gemelo digital de la planta de tintes.

**Ideas clave:**
- **La capacidad no es el problema:** la llenadora (cuello de botella) trabaja al 29 % y la demanda podría crecer 3,37 veces (según el libro) antes de saturarla. Las restricciones reales son:
  - la bodega de producto terminado;
  - la bahía del producto C (punto de reorden + lote = 20.100 frente a 14.000);
  - la materia prima importada (13 días de cobertura frente a 55 requeridos).
- **El pronóstico del Corte 1 estaba sesgado;** corregido, el sesgo baja de 29.600 a 1.600 tubos/mes y el RMSE un 17 %.
- **Gemelo digital en SimPy:**
  - 6 estaciones;
  - demanda de facturas reales, fallas, alistamientos y OEE;
  - 16 sensores virtuales;
  - validado con balance de masa, ley de Little y horas de equipo (±0,7 %).
- **Escenarios:** bajar el lote de C a 7.800 elimina los días sobre la bahía; con un solo turno el servicio cae al 97,97 %; el servicio se mantiene ≥ 99,4 % hasta 2 veces la demanda.
- **Optimización** (Bowman = flujo en red, MILP de turnos): la persecución es óptima. Pero ejecutada a lazo abierto en el gemelo da 79,4 % de servicio frente al 99,99 % del modelo agregado; el plan debe fijar volúmenes y el punto de reorden liberar los lotes.

**Fórmulas y métodos** (los detalles están en los cuadernos):
- Suavización exponencial simple $F_{t+1} = \alpha y_t + (1-\alpha)F_t$, con $\alpha$ = 0,05 y nivel inicial = promedio de 3 meses ($y_t$ = venta del mes $t$, $F_t$ = pronóstico).
- Sesgo $\bar{e}$, señal de rastreo $\sum e_t / MAD$ y RMSE.
- Índices estacionales $s_m = y_m/\bar{y}$ con intervalo del 80 %.
- Ley de Little $WIP = TH \times$ tiempo de flujo; takt time = tiempo disponible / demanda.
- Modelo de transporte de Bowman y modelo de flujo en red para el plan agregado; MILP para los turnos.
- Simulación de eventos discretos con 30 réplicas, números aleatorios comunes e intervalo del 95 %.

**Resultados presentados:**

| Resultado | Valor | Página |
|---|---|---|
| Ocupación de la llenadora | 29 % (28,9 %) | 2, 5 |
| Factor de demanda antes de saturar | 3,37× | 2 |
| Tiempo de flujo por lote / takt / throughput / WIP | 16,9 h / 11,1 s/tubo / 352 frente a 325 tubos/h / 5.308 | 2 |
| Cobertura de materia prima | 13 frente a 55 días | 2 |
| Sesgo del pronóstico | 44,6 M → 2,4 M COP (29.600 → 1.600 tubos/mes) | 3, 7 |
| Señal de rastreo | 3,42 → 0,22 | 3 |
| RMSE | 76,8 M → 63,6 M COP (50.800 → 42.100 tubos/mes) | 3 |
| Prueba de estrés | ≥ 99,4 % hasta 2,0×; 93,9 % con 2,5×; 70,8 % con 3,0× | 5 |
| Lote de C de 7.800 | días sobre la bahía 32,3 % → 0 %; inventario −10,3 % | 5, 7 |
| Persecución frente a nivelado | inventario promedio 45.100 → 29.500 (−35 %); meses sobre la bodega 5 → 0 | 6, 7 |
| Servicio del plan a lazo abierto | 79,42 % (persecución) y 84,99 % (nivelado), frente a 99,99 % con punto de reorden | 6 |
| Un turno en enero, abril y agosto | −8.300 horas-hombre/año; −114,5 M COP/año | 6, 7 |
| Compras estacionales (+11.665 kg) | espera de materia prima 44,8 h → 9,3 h | 7 |
| Programa maestro | 156 lotes/año (−0,36 % frente al plan); alistamientos = 27,9 % del tiempo de la llenadora | 7 |

**Páginas clave:**
- p. 2: estudio preliminar;
- p. 3: pronóstico;
- p. 4: diseño y validación del gemelo;
- p. 5: escenarios;
- p. 6: optimización y comparación plan frente a gemelo (gráficos);
- p. 7: tabla de mejoras;
- p. 8: conclusiones.

**Relación con otros archivos del repo:**
- Estudio preliminar y plan agregado: [`Datos Thyms Completo.md`](./Datos%20Thyms%20Completo.md).
- Pronóstico, gemelo, escenarios y estrés: [`Gemelo_Digital_Thyms.md`](./Gemelo_Digital_Thyms.md).
- Gemelo guiado por el plan (79,42 %, 84,99 %, 99,99 %): [`Gemelo_Digital_Thyms_MEJORADO.md`](./Gemelo_Digital_Thyms_MEJORADO.md).
- Resumen completo del trabajo: [`CONTEXTO_GEMELO_THYMS.md`](./CONTEXTO_GEMELO_THYMS.md).
- Pronóstico del Corte 1 que se corrige: [proyecto-thyms-pronostico](../../corte-1-pronosticos/proyecto-thyms-pronostico/).
- Teoría del modelo de Bowman y del flujo en red: [01-planeacion-agregada-modelo-bowman](../01-planeacion-agregada-modelo-bowman/).
- Siguiente paso propuesto (Wagner–Whitin / Silver–Meal): [03-wagner-whitin-y-silver-meal](../03-wagner-whitin-y-silver-meal/).

**Advertencias:**
- Los resultados de **Bowman, flujo en red, MILP de turnos y programa maestro** (página 6 y parte de la 7) **no están en los archivos de esta carpeta**: no hay un libro ni un cuaderno de THYMS con esos modelos. Los archivos de [01-planeacion-agregada-modelo-bowman](../01-planeacion-agregada-modelo-bowman/) son ejemplos de clase con otros datos.
- Tampoco salen de estos archivos:
  - el «26 % de uso de mano de obra en el mes pico» (p. 2);
  - las horas de espera de materia prima 44,8 h → 9,3 h y el «×5» (pp. 5 y 7): el cuaderno solo reporta réplicas con faltante, 3 frente a 6;
  - los −114,5 M COP de mano de obra.
- Los «61 g/tubo» (p. 2) equivalen a 6.106 kg de materia prima por 100.000 tubos (hoja `Restricciones`).
- La página 7 no explica qué significa «(sin cambio)»; podría referirse a que el servicio no cambia [interpretación no confirmada]. «(por validar)» se entiende porque el plan + punto de reorden todavía no se había simulado: es el «siguiente paso» de la página 8.

## Contenido completo (página por página)

### Página 1 — S&OP con Gemelo Digital (portada)

> [Imagen decorativa: fondo negro con una foto de cabello castaño ondulado, de espaldas.]
> [Imagen decorativa: logo dorado «THYM'S ACADEMIC» arriba al centro.]

- **S&OP con Gemelo Digital**
- **Thyms Colombia S.A.S**
- Proyecto C2 · Planeación, Programación y Control de la Producción · Universidad de La Sabana
- Prof. William J. Guerrero · 6 de octubre de 2026

### Página 2 — 1. Estudio preliminar: la capacidad no es el problema

> [Imagen decorativa: logo «THYM'S ACADEMIC» arriba a la izquierda; aparece igual en las páginas 2 a 8.]

Cuatro indicadores destacados en círculos:

| Valor | Indicador |
|---|---|
| 29% | Ocupación de la llenadora |
| 3,37× | Demanda antes de saturar la llenadora |
| 16,9 h | Tiempo de flujo por lote (gemelo) |
| 13 vs 55 | Cobertura de materia prima (días) |

- Takt 11,1 s/tubo · throughput 352 vs 325 tubos/h requeridos · WIP 5.308 (Ley de Little verificada)
- Restricciones críticas: almacenamiento de PT (plan nivelado = 1,66× la bodega), bahía del producto C (20.100 vs 14.000), materia prima importada
- Agregación en tres unidades: tubos · kg (61 g/tubo) · horas-hombre (26% de uso de mano de obra en el mes pico)

### Página 3 — 2. Pronóstico: mejor que el Corte 1

> [Gráfico: líneas; eje Y «Tubos / mes» de 0 a 200k; eje X de ene-26 a ago-27.
> - «Ventas reales (escala planta)» (gris), de ene-26 a ago-26: ≈ 63k, 102k, 133k, 35k, 131k, 104k, 153k, 79k.
> - «Pronóstico SES estacional» (marrón), de sep-26 a ago-27: ≈ 100k en sep, oct, nov y dic, luego 63k, 102k, 133k, 35k, 131k, 104k, 153k, 79k.
> - «Intervalo de predicción 80%» (banda rosada): de ≈ 46k a 154k en sep–dic, hasta ≈ 235k en jul-27.
> - «Nivel SES (100.038 tubos/mes)» (línea discontinua horizontal en ≈ 100k).]

- Sesgo del Corte 1: 44,6M → 2,4 M COP
  - 29.600 → 1.600 tubos/mes
- Señal de rastreo: 3,42 → 0,22
- RMSE −17% (63,6M vs 76,8M)
  - 50.800 → 42.100 tubos/mes
- El pronóstico se actualiza dentro del gemelo cada mes
- El MAPE del Corte 1 es menor solo porque premia pronósticos bajos: para planear importa más el sesgo
- Índices estacionales (julio 1,53; abril 0,35) + intervalo del 80%

### Página 4 — 3. Gemelo digital: diseño y validación

Lista numerada:
1. Modelo de eventos discretos en SimPy · 6 estaciones · parámetros leídos del libro de 14 hojas
2. Demanda estocástica (facturas reales), fallas (MTBF/MTTR), alistamientos dependientes de la secuencia, OEE, plazo de la materia prima, festivos colombianos
3. 16 sensores virtuales por hora · consultas en vivo paso a paso (gancho para tablero)
4. Validación: balance de masa exacto · Ley de Little · horas de equipo dentro de ±0,7%
5. 30 réplicas, números aleatorios comunes, IC del 95%

### Página 5 — 4. Escenarios what-if: cuellos de botella

Lista numerada:
1. Llenadora 28,9% vs reactores 10,5%, encartonadora 16,0%, empaque 15,4%
2. Prueba de estrés: servicio ≥ 99,4% hasta 2,0× la demanda; 93,9% con 2,5×; 70,8% con 3,0×
3. Lote de C 15.600 → 7.800: días sobre la bahía 32,3% → 0%, inventario −10,3%
4. Compras sin estacionalidad: espera de materia prima ×5, servicio 99,85%
5. Un solo turno: servicio 97,97%, llenadora 57,5%

### Página 6 — 5. Optimización: Bowman, flujo y MILP

- Mismo problema de dos formas: transporte de Bowman = flujo en red → persecución, con inventario promedio de 29.500 tubos (nivelado: 45.100)
- Recursos en orden: inventario → horas extra → maquila → ventas perdidas (≥ 3,4× la demanda)
- Turnos con MILP: un turno basta en meses bajos (ene, abr, ago): −8.300 horas-hombre/año

> [Gráfico (a): «Inventario de PT a fin de mes, promedio de 30 réplicas»; eje Y «Inventario PT (tubos)» de 0 a 80k+; eje X de Ene a Dic. Valores aproximados leídos del gráfico:
>
> | Serie | Ene | Feb | Mar | Abr | May | Jun | Jul | Ago | Sep | Oct | Nov | Dic |
> |---|---|---|---|---|---|---|---|---|---|---|---|---|
> | Gemelo – punto de reorden (actual) | 32k | 38k | 36k | 35k | 36k | 35k | 36k | 38k | 32k | 36k | 33k | 36k |
> | Gemelo – plan de persecución | 12k | 15,5k | 13k | 16,5k | 14k | 17k | 16,5k | 9,5k | 15k | 16k | 15,5k | 14k |
> | Gemelo – plan nivelado | 50k | 46k | 13k | 78k | 52k | 48k | 1k | 9,5k | 15k | 16k | 15k | 14k |
> | Agregado – persecución (punteado) | 29k | 27,5k | 28k | 28k | 25,5k | 25k | 24k | 25k | 25k | 26k | 26k | 25,5k |
> | Agregado – nivelado (punteado) | 66k | 62k | 29k | 95k | 61k | 57k | 7k | 27,5k | 27,5k | 29k | 29k | 28k |
>
> Línea roja discontinua: «Capacidad de bodega (58k)». El gemelo nivelado y el agregado nivelado pasan la bodega en abril (y el agregado también en enero y febrero).]

> [Gráfico (b): barras «Inventario promedio y servicio», eje Y «Inventario promedio de fin de mes (tubos)» de 0 a 40.000, con barras de error:
> - Punto de reorden ≈ 35.300 (NS 99,99%);
> - Plan de persecución ≈ 14.600 (NS 79,42%), con barra de error de ≈ 11.800 a 17.400;
> - Plan nivelado ≈ 29.900 (NS 84,99%), con barra de error de ≈ 27.300 a 32.400.]

Recuadro inferior: **Mismo plan: 99,99% de servicio en el modelo agregado, 79,4% ejecutado a lazo abierto en el gemelo**

### Página 7 — 6. Mejoras e impacto en los KPI

| Mejora | KPI | Antes → Después |
|---|---|---|
| Corrección del pronóstico | Sesgo (tubos/mes) | 29.600 → 1.600 |
| Persecución en lugar de nivelado | Inventario promedio (tubos) / meses sobre bodega | 45.100 → 29.500 (−35 %) / 5 → 0 |
| Lote de C 15.600 → 7.800 | Días de C sobre la bahía · Inventario PT | 32,3 % → 0 % · −10,3 % *(sin cambio)* |
| Compras estacionales + 11.665 kg | Espera de materia prima | 44,8 h → 9,3 h *(sin cambio)* |
| El plan fija volúmenes, el ROP libera | Servicio | 79,4 % → 99,99 % (por validar) |
| Un turno en ene/abr/ago | Costo de mano de obra | −114,5 M COP/año (≈ −8.300 h-h) |

Nota al pie: *Programa maestro: 156 lotes/año, −0,36% vs plan · alistamientos = 27,9% del tiempo de la llenadora*

### Página 8 — 7. Conclusiones

- La capacidad es abundante: el foco está en almacenamiento, cobertura de materia prima y reglas de ejecución
- Persecución es óptima (Bowman = flujo), pero debe ejecutarse a lazo cerrado para mantener el servicio ≈ 100%
- Limitaciones: una zona de ventas, 8 meses de datos y algunos supuestos de costos
- Siguiente paso: simular plan + punto de reorden juntos; Wagner–Whitin / Silver–Meal sobre el programa maestro

### Página 9 — ¡Gracias!

«¡Gracias!» sobre fondo negro, con el logo «THYM'S ACADEMIC» (imagen decorativa).

## Anexo: texto extraído automáticamente del PDF

> Texto plano tal como sale del PDF, sin fórmulas ni tablas que estén como imagen. La versión fiel y completa es la sección «Contenido completo» de arriba.

### Página 1 · 2 imagen(es)

S&OP con Gemelo Digital
Thyms Colombia S.A.S
Proyecto C2 · Planeación, Programación y Control de la Producción · Universidad de La Sabana
Prof. William J. Guerrero · 6 de octubre de 2026

### Página 2 · 1 imagen(es)

1. Estudio preliminar: la capacidad no es el problema
29%
Ocupación de la llenadora
3,37×
Demanda antes de saturar la 
llenadora
16,9 h
Tiempo de flujo por lote 
(gemelo)
13 vs 55
Cobertura de materia prima 
(días)
• Takt 11,1 s/tubo · throughput 352 vs 325 tubos/h requeridos · WIP 5.308 (Ley de Little verificada)
• Restricciones críticas: almacenamiento de PT (plan nivelado = 1,66× la bodega), bahía del producto C (20.100 vs 14.000), 
materia prima importada
• Agregación en tres unidades: tubos · kg (61 g/tubo) · horas-hombre (26% de uso de mano de obra en el mes pico)

### Página 3 · 2 imagen(es)

2. Pronóstico: mejor que el Corte 1
• Sesgo del Corte 1: 44,6M → 2,4 M COP
o
29.600 → 1.600 tubos/mes
• Señal de rastreo: 3,42 → 0,22
• RMSE −17% (63,6M vs 76,8M)
o
50.800 → 42.100 tubos/mes 
• El pronóstico se actualiza dentro del 
gemelo cada mes
• El MAPE del Corte 1 es menor solo porque premia pronósticos bajos: para planear importa más el sesgo
• Índices estacionales (julio 1,53; abril 0,35) + intervalo del 80%

### Página 4 · 1 imagen(es)

3. Gemelo digital: diseño y validación
1
Modelo de eventos discretos en SimPy · 6 estaciones · parámetros leídos del libro de 14 hojas
2
Demanda estocástica (facturas reales), fallas (MTBF/MTTR), alistamientos dependientes de la 
secuencia, OEE, plazo de la materia prima, festivos colombianos
3
16 sensores virtuales por hora · consultas en vivo paso a paso (gancho para tablero)
4
Validación: balance de masa exacto · Ley de Little · horas de equipo dentro de ±0,7%
5
30 réplicas, números aleatorios comunes, IC del 95%

### Página 5 · 1 imagen(es)

4. Escenarios what-if: cuellos de botella
1
Llenadora 28,9% vs reactores 10,5%, encartonadora 16,0%, empaque 15,4%
2
Prueba de estrés: servicio ≥ 99,4% hasta 2,0× la demanda; 93,9% con 2,5×; 70,8% con 3,0×
3
Lote de C 15.600 → 7.800: días sobre la bahía 32,3% → 0%, inventario −10,3%
4
Compras sin estacionalidad: espera de materia prima ×5, servicio 99,85%
5
Un solo turno: servicio 97,97%, llenadora 57,5%

### Página 6 · 3 imagen(es)

5. Optimización: Bowman, flujo y MILP
• Mismo problema de dos formas: transporte de 
Bowman = flujo en red → persecución, con 
inventario promedio de 29.500 tubos (nivelado: 
45.100)
• Recursos en orden: inventario → horas extra → 
maquila → ventas perdidas (≥ 3,4× la demanda)
• Turnos con MILP: un turno basta en meses bajos 
(ene, abr, ago): −8.300 horas-hombre/año
Mismo plan: 99,99% de servicio en el modelo agregado, 79,4% ejecutado a lazo abierto en el gemelo

### Página 7 · 1 imagen(es)

6. Mejoras e impacto en los KPI
Mejora
KPI
Antes → Después
Corrección del pronóstico
Sesgo (tubos/mes)
29.600 → 1.600
Persecución en lugar de nivelado
Inventario promedio (tubos) / meses sobre 
bodega
45.100 → 29.500 (−35 %) / 5 → 0
Lote de C 15.600 → 7.800
Días de C sobre la bahía · Inventario PT
32,3 % → 0 % · −10,3 % (sin cambio)
Compras estacionales + 11.665 kg
Espera de materia prima
44,8 h → 9,3 h (sin cambio)
El plan fija volúmenes, el ROP libera
Servicio
79,4 % → 99,99 % (por validar)
Un turno en ene/abr/ago
Costo de mano de obra
−114,5 M COP/año (≈ −8.300 h-h)
Programa maestro: 156 lotes/año, −0,36% vs plan · alistamientos = 27,9% del tiempo de la llenadora

### Página 8 · 1 imagen(es)

7. Conclusiones
La capacidad es abundante: el foco está en almacenamiento, cobertura de materia prima y reglas 
de ejecución
Persecución es óptima (Bowman = flujo), pero debe ejecutarse a lazo cerrado para mantener el 
servicio ≈ 100%
Limitaciones: una zona de ventas, 8 meses de datos y algunos supuestos de costos
Siguiente paso: simular plan + punto de reorden juntos; Wagner–Whitin / Silver–Meal sobre el 
programa maestro

### Página 9 · 1 imagen(es)

¡Gracias!

