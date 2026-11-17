# programacion-produccion-una-maquina

> **Archivo:** [`programacion-produccion-una-maquina.xlsx`](./programacion-produccion-una-maquina.xlsx) · **Corte 3** · Libro de Excel con 3 hoja(s): `Reglas de Despacho`, `Restricciones de Precedencia`, `Tardanza Máxima`  
> **Nombre original:** `CORTE 3/Programación de Producción.xlsx`  
> Este .md es una versión en texto del archivo para poder leerlo sin abrir el binario.

## Explicación de los ejemplos

### Qué es

Libro de trabajo de clase para el tema **programación de una máquina** ([L17](./L17-single-machine-scheduling.md)). Tiene tres hojas:

1. `Reglas de Despacho`: un ejemplo cotidiano con $r_j$ (el mismo de [ejemplo-1-programacion-produccion](./ejemplo-1-programacion-produccion.md)) y el "ejemplo clase 20/10": 6 trabajos secuenciados con orden natural, al azar, SPT, WSPT, EDD y holgura mínima (MS), con $\sum C_j/n$, $\sum w_jT_j$, número de tardíos y $\sum w_jC_j$.
2. `Restricciones de Precedencia`: cadenas que no se pueden romper (razón $\sum w/\sum p$), cadenas que sí (factor $\rho$) y el ejercicio de *preemption* de la p. 25 de L17, con un Gantt dibujado a mano.
3. `Tardanza Máxima`: 20 trabajos y una secuencia evaluada con `VLOOKUP`; parece preparada para optimizar con Solver, como en la p. 48 de L17 (deducido).

Se aprende a calcular $C_j$, $T_j$, $L_j$ y $U_j$ a partir de una secuencia, a comparar reglas de despacho y a aplicar las reglas de cadenas y de *preemption*.

No hay gráficos de Excel. La hoja 2 tiene una imagen (un Gantt a mano).

Notación de las fórmulas: $[k]$ es el trabajo en la posición $k$; $C_{[k]}=C_{[k-1]}+p_{[k]}$; $T_j=\max(C_j-d_j,0)$; $L_j=C_j-d_j$.

---

### Hoja `Reglas de Despacho`

#### Bloque A (filas 3-8): ejemplo cotidiano con liberaciones

**Objetivo (deducido):** programar cuatro actividades personales en un solo "recurso" (la persona), respetando la hora en que cada una está disponible ($r_j$), y medir el tiempo de flujo. Es idéntico a [ejemplo-1-programacion-produccion](./ejemplo-1-programacion-produccion.md); ahí está explicado en detalle.

| N (posición) | Trabajo | $r_j$ (h) | $d_j$ | $p_j$ | $w_j$ | $s_j$ | $c_j$ | $c_j-r_j$ | $w_jc_j$ |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Pago Factura | 50 | 19-oct (fecha) | 20 min | 3 | 30 min | 50.33 | 0.33 | 150.99 |
| 2 | Proyecto | 24 | "24 h + 30 días" | 10 h | 5 | 3 h | 60.33 | 36.33 | 301.65 |
| 3 | Entrevista de Trabajo | 100 | "100 h + 2 h" | 1 h | 4 | 0 h | 101 | 1 | 404 |
| 4 | Seminario | 0 | 19-oct (fecha) | 2 h | 2 | 0 h | 103 | 103 | 206 |

(En la hoja las filas aparecen en el orden 2, 4, 1, 3; la columna N da la posición en la secuencia.)

- Fórmulas: `I6 = 50+0.33` ($C=r+p$, con 20 min = 0.33 h); `I4 = I6+10`; `I7 = 100+1` (nota J7: "si r_j es > c_j del anterior, inicia en r_j"); `I5 = I7+2`; `K = I−D` ($C_j-r_j$); `L = G·I` ($w_jC_j$).
- Resultados: `K8 = AVERAGE(K4:K7)` = **35.165** h ("Tiempo de Flujo" promedio $\bar F=\frac1n\sum(C_j-r_j)$); `L8 = AVERAGE(L4:L7)` = **265.66** (promedio de $w_jC_j$; la suma sería 1062.64).

#### Bloque B (filas 10-18): "ejemplo clase 20/10", orden natural

**Datos de entrada** (los mismos en todos los bloques que siguen):

| Trabajo | $p_j$ | $d_j$ | $w_j$ | $w_j/p_j$ |
|---|---|---|---|---|
| 1 | 6 | 36 | 1 | 0.1667 |
| 2 | 4 | 21 | 1 | 0.25 |
| 3 | 7 | 18 | 1 | 0.1429 |
| 4 | 12 | 15 | 3 | 0.25 |
| 5 | 5 | 1 | 2 | 0.4 |
| 6 | 2 | 32 | 1 | 0.5 |

**Método:** `E13 = C13`, `E14 = E13+C14` → $C_{[k]}=C_{[k-1]}+p_{[k]}$; `F = IF(E<D,0,E−D)` → $T_j=\max(C_j-d_j,0)$; `G = IF(F>0,F,E−D)` → $L_j=C_j-d_j$; `J12 = AVERAGE(E13:E18)` → $\sum C_j/n$; `J13 = {SUM(H13:H18*F13:F18)}` (fórmula matricial) → $\sum w_jT_j$; `J14` = número de tardíos, escrito a mano.

Secuencia 1-2-3-4-5-6 (orden natural, FIFO):

| Trabajo | Inicio | $C_j$ | $d_j$ | $T_j$ | $L_j$ | $w_j$ |
|---|---|---|---|---|---|---|
| 1 | 0 | 6 | 36 | 0 | −30 | 1 |
| 2 | 6 | 10 | 21 | 0 | −11 | 1 |
| 3 | 10 | 17 | 18 | 0 | −1 | 1 |
| 4 | 17 | 29 | 15 | 14 | 14 | 3 |
| 5 | 29 | 34 | 1 | 33 | 33 | 2 |
| 6 | 34 | 36 | 32 | 4 | 4 | 1 |

$\sum C_j/n=22$; $\sum w_jT_j=112$; tardíos = 3.

#### Bloque C (filas 20-27): "Secuencia elegida al azar"

| Trabajo | Inicio | $C_j$ | $d_j$ | $T_j$ | $L_j$ | $w_j$ | $w_jC_j$ |
|---|---|---|---|---|---|---|---|
| 4 | 0 | 12 | 15 | 0 | −3 | 3 | 36 |
| 3 | 12 | 19 | 18 | 1 | 1 | 1 | 19 |
| 1 | 19 | 25 | 36 | 0 | −11 | 1 | 25 |
| 5 | 25 | 30 | 1 | 29 | 29 | 2 | 60 |
| 2 | 30 | 34 | 21 | 13 | 13 | 1 | 34 |
| 6 | 34 | 36 | 32 | 4 | 4 | 1 | 36 |

$\sum C_j/n$ = **28.8** en la hoja (ver Observaciones; el valor correcto es 26); $\sum w_jT_j=76$; tardíos = 4; `K27 = SUM` → $\sum w_jC_j=210$.

#### Bloque D (filas 28-35): "Secuencia organizada desde el más corto" (SPT)

| Trabajo | Inicio | $C_j$ | $d_j$ | $T_j$ | $L_j$ | $w_j$ | $w_j/p_j$ | Prioridad WSPT | $w_jC_j$ |
|---|---|---|---|---|---|---|---|---|---|
| 6 | 0 | 2 | 32 | 0 | −30 | 1 | 0.5 | 1 | 2 |
| 2 | 2 | 6 | 21 | 0 | −15 | 1 | 0.25 | 3 | 6 |
| 5 | 6 | 11 | 1 | 10 | 10 | 2 | 0.4 | 2 | 22 |
| 1 | 11 | 17 | 36 | 0 | −19 | 1 | 0.1667 | 5 | 17 |
| 3 | 17 | 24 | 18 | 6 | 6 | 1 | 0.1429 | 6 | 24 |
| 4 | 24 | 36 | 15 | 21 | 21 | 3 | 0.25 | 4 | 108 |

$\sum C_j/n=16$; $\sum w_jT_j=89$; tardíos = 3; $\sum w_jC_j=179$. Las columnas K (`=H/C`, $w_j/p_j$) y L (prioridad de mayor a menor, escrita a mano) preparan el bloque WSPT.

#### Bloque E (filas 36-43): "Secuencia por prioridad WSPT"

| Trabajo | Inicio | $C_j$ | $d_j$ | $T_j$ | $L_j$ | $w_j$ | $w_jC_j$ |
|---|---|---|---|---|---|---|---|
| 6 | 0 | 2 | 32 | 0 | −30 | 1 | 2 |
| 5 | 2 | 7 | 1 | 6 | 6 | 2 | 14 |
| 2 | 7 | 11 | 21 | 0 | −10 | 1 | 11 |
| 4 | 11 | 23 | 15 | 8 | 8 | 3 | 69 |
| 1 | 23 | 29 | 36 | 0 | −7 | 1 | 29 |
| 3 | 29 | 36 | 18 | 18 | 18 | 1 | 36 |

$\sum C_j/n=18$; $\sum w_jT_j=54$; tardíos = 3; **$\sum w_jC_j=161$**, el mínimo de todo el libro, como garantiza el teorema de WSPT. Los trabajos 2 y 4 empatan en $w/p=0.25$; cualquier orden entre ellos da 161.

#### Bloque F (filas 44-51): "Secuencia por tiempo de terminación EDD"

Secuencia 5-4-3-2-6-1. Valores que guardó la hoja:

| Trabajo | $C_j$ (hoja) | $C_j$ correcto | $d_j$ | $T_j$ | $L_j$ correcto | $w_j$ | $w_jC_j$ (hoja) |
|---|---|---|---|---|---|---|---|
| 5 | 5 | 5 | 1 | 4 | 4 | 2 | 10 |
| 4 | 17 | 17 | 15 | 2 | 2 | 3 | 51 |
| 3 | 24 | 24 | 18 | 6 | 6 | 1 | 24 |
| 2 | 28 | 28 | 21 | 7 | 7 | 1 | 28 |
| 6 | **2** | 30 | 32 | 0 | −2 | 1 | 2 |
| 1 | **8** | 36 | 36 | 0 | 0 | 1 | 8 |

Hoja: $\sum C_j/n=14$, $\sum w_jT_j=27$, tardíos = 4, $\sum w_jC_j=123$. Corregido (cálculo propio): $\sum C_j/n=23.33$, $\sum w_jT_j=27$ (no cambia), $\sum w_jC_j=179$, $L_{max}=7$ (el menor de todas las reglas, como garantiza EDD).

#### Bloque G (filas 52-68): "Secuencia por holgura mínima MS"

**Método:** holgura $s_j(t)=\max(d_j-p_j-t,0)$. Las fórmulas son `E53 = IF(D−C>0,D−C,0)` para $t=0$ y `F53 = IF(D−C−$E$59>0, D−C−$E$59, 0)` para los demás instantes. La fila 59 ("Menor Holgura") guarda el reloj $t$ después de cada trabajo elegido: `E59 = C57` (=5), `F59 = C56+E59` (=17), `G59 = C54+F59` (=21), `H59 = C55+G59` (=28). Las celdas de los trabajos ya programados quedan vacías.

| Trabajo | $p_j$ | $d_j$ | $s_j(0)$ | $s_j(5)$ | $s_j(17)$ | $s_j(21)$ | $s_j(28)$ |
|---|---|---|---|---|---|---|---|
| 1 | 6 | 36 | 30 | 25 | 13 | 9 | 2 |
| 2 | 4 | 21 | 17 | 12 | **0** | | |
| 3 | 7 | 18 | 11 | 6 | 0 | **0** | |
| 4 | 12 | 15 | 3 | **0** | | | |
| 5 | 5 | 1 | **0** | | | | |
| 6 | 2 | 32 | 30 | 25 | 13 | 9 | **2** |
| Elegido → nuevo $t$ | | | 5 → 5 | 4 → 17 | 2 → 21 | 3 → 28 | 6 → 30, luego 1 → 36 |

En $t=17$ empatan 2 y 3 (holgura 0) y en $t=28$ empatan 1 y 6 (holgura 2). La hoja elige 2 y 6, los de menor $p_j$; el desempate por SPT es deducido, la hoja no lo dice.

Resultado (filas 61-68):

| Trabajo | Inicio | $C_j$ | $d_j$ | $T_j$ |
|---|---|---|---|---|
| 5 | 0 | 5 | 1 | 4 |
| 4 | 5 | 17 | 15 | 2 |
| 2 | 17 | 21 | 21 | 0 |
| 3 | 21 | 28 | 18 | 10 |
| 6 | 28 | 30 | 32 | 0 |
| 1 | 30 | 36 | 36 | 0 |

`F68 = SUM(F62:F67)` → $\sum T_j=16$. Cálculo propio: $\sum w_jT_j=24$, $\sum C_j/n=22.83$, $\sum w_jC_j=176$, tardíos = 3.

#### Bloque H (filas 70-77): sin rótulo

Secuencia 5-4-2-6-3-1. La hoja no dice qué regla aplica. No coincide con MS ni con EDD, y tampoco con ATC ($K=1$) ni CR calculadas con estos datos (cálculo propio; deducido).

| Trabajo | $C_j$ (hoja) | $C_j$ correcto | $d_j$ | $T_j$ (hoja) | $T_j$ correcto | $w_j$ |
|---|---|---|---|---|---|---|
| 5 | 5 | 5 | 1 | 4 | 4 | 2 |
| 4 | 17 | 17 | 15 | 2 | 2 | 3 |
| 2 | 21 | 21 | 21 | 0 | 0 | 1 |
| 6 | **2** | 23 | 32 | 0 | 0 | 1 |
| 3 | **9** | 30 | 18 | 0 | **12** | 1 |
| 1 | **15** | 36 | 36 | 0 | 0 | 1 |

Hoja: $\sum C_j/n=11.5$, $\sum w_jT_j=14$, tardíos = 3, $\sum w_jC_j=108$. Corregido: $\sum C_j/n=22$, $\sum w_jT_j=26$, $\sum w_jC_j=171$, tardíos = 3.

#### Resumen comparativo del ejemplo 20/10

Valores corregidos donde la hoja tiene errores; $L_{max}$ y las celdas marcadas con \* son cálculo propio.

| Regla | Secuencia | $\sum C_j/n$ | $\sum w_jT_j$ | Tardíos | $\sum w_jC_j$ | $L_{max}$ |
|---|---|---|---|---|---|---|
| Orden natural | 1-2-3-4-5-6 | 22 | 112 | 3 | 224\* | 33 |
| Al azar | 4-3-1-5-2-6 | 26 (hoja: 28.8) | 76 | 4 | 210 | 29 |
| SPT | 6-2-5-1-3-4 | **16** | 89 | 3 | 179 | 21 |
| WSPT | 6-5-2-4-1-3 | 18 | 54 | 3 | **161** | 18 |
| EDD | 5-4-3-2-6-1 | 23.33 (hoja: 14) | 27 | 4 | 179 (hoja: 123) | **7** |
| MS | 5-4-2-3-6-1 | 22.83\* | **24\*** | 3 | 176\* | 10 |
| Sin rótulo | 5-4-2-6-3-1 | 22 (hoja: 11.5) | 26 (hoja: 14) | 3 | 171 (hoja: 108) | 12 |

**Conclusión:** SPT minimiza el flujo promedio, WSPT minimiza $\sum w_jC_j$ y EDD minimiza $L_{max}$, como dice la teoría de L17. Para la tardanza ponderada, las reglas orientadas a fechas (MS, EDD) son mucho mejores que FIFO o SPT.

---

### Hoja `Restricciones de Precedencia`

#### Bloque 1 (filas 1-13): "1|Prec|ΣCj — Si, NO se pueden romper las cadenas"

**Datos:**

| Job | $P_j$ | $W_j$ |
|---|---|---|
| A | 2 | 1 |
| B | 4 | 2 |
| C | 11 | 3 |
| D | 30 | 2 |
| E | 13 | 5 |
| F | 20 | 1 |

Cadenas (columna "Prec"): `C-A-B`, `E-F` y `D` (trabajo suelto).

**Método:** si una cadena debe terminarse una vez iniciada, se programa primero la de mayor $\sum W_j/\sum P_j$ (L17, p. 15).

| Cadena | Fórmula | $\sum W/\sum P$ |
|---|---|---|
| C-B-A | `=(C5+C4+C3)/(B5+B4+B3)` = 6/17 | 0.3529 |
| E-F | `=(C7+C8)/(B7+B8)` = 6/33 | 0.1818 |
| D | `=C6/B6` = 2/30 | 0.0667 |

"Se inicia con la cadena que tiene la mayor relación" → **Respuesta: C-B-A-E-F-D**.

#### Bloque 2 (filas 15-29): "Si SI se pueden romper las cadenas" (factor $\rho$)

| Cadena | Prefijo | Fórmula | Valor |
|---|---|---|---|
| C-B-A | hasta C | `=C19/B19` = 3/11 | 0.2727 |
| C-B-A | hasta B | `=(C19+C18)/(B19+B18)` = 5/15 | 0.3333 |
| C-B-A | hasta A | `=(C19+C18+C17)/(B19+B18+B17)` = 6/17 | **0.3529** → $l^*=A$, "ρ-factor = 0,35" |
| E-F | hasta E | `=C21/B21` = 5/13 | **0.3846** → $l^*=E$, "ρ-factor = 0,38" |
| E-F | hasta F (rotulado "l=E") | `=(C21+C22)/(B21+B22)` = 6/33 | 0.1818 |

La hoja no escribe la secuencia final. Continuación propia con la regla de L17 (p. 17): primero E ($\rho=0.385$); luego C-B-A completa ($\rho=0.353$ frente a F $=1/20=0.05$ y D $=0.067$); luego D ($0.067>0.05$) y al final F. Secuencia deducida: **E-C-B-A-D-F**.

#### Bloque 3 (filas 31-54): "1|Prec|ΣCj/ΣWj*Cj", preemption con liberaciones

Es el ejercicio de L17, p. 25 ($1|r_j,prmp|\sum w_jC_j$), con **$W_j=1$** para todos (celda `J32`). Entonces la regla "mayor $w_j$ / tiempo restante" equivale a escoger el menor tiempo restante.

| Trabajo | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| $P_j$ | 6 | 18 | 12 | 10 | 10 | 17 | 16 |
| $R_j$ | 0 | 0 | 0 | 14 | 25 | 25 | 50 |
| $W_j/P_j$ (`L33:L39 = J32/P`) | 0.1667 | 0.0556 | 0.0833 | 0.1 | 0.1 | 0.0588 | 0.0625 |

Decisiones por evento (columna B = `MAX` de las razones de los disponibles; C = elegido):

| $t$ | Disponibles | Máx. $W/P$ | Elegido | Nota de la hoja |
|---|---|---|---|---|
| 0 | 1, 2, 3 | 0.1667 | 1 | "se mueve el reloj t"; termina en t=6 |
| 6 | 2, 3 | 0.0833 | 3 | "el 3 no se termina (interrumpido por la llegada del 4)"; "3\*=12-8=2" |
| 14 | 2, 3\*, 4 | 0.5 | 3\* | termina en t=18; próxima llegada t=25 |
| 18 | 2, 4 | 0.1 | 4 | "el 4 no se termina (interrumpido por la llegada del 5 y 6)"; "4\*=10-7=3" |
| 25 | 2, 4\*, 5, 6 | 0.3333 | 4\* | (texto: "Terminación del trabajo (t=18)") |
| 28 | 2, 5, 6 | 0.1 | 5 | termina en t=38 |
| 38 | 2, 6 | 0.0588 | 6 | "el 6 no se termina (interrumpido por la llegada del 7)"; "6\*=17-12" |
| 50 (la hoja dice "t=38") | 2, 6\*, 7 | 0.2 | 6\* | |
| 55 | 2, 7 | 0.0625 | 7 | |
| (71) | 2 | — | 2 | celda `C54` = 2 |

**Imagen (Gantt a mano, anclado cerca de G40:S50):** una barra horizontal con eje 0 a 71, más una segunda fila para el trabajo 2. Notas: "si o si tiene que iniciar actividad 4" en t=14, "actividad 5,6" en t=25 y "actividad 7" en t=50. Unas llaves marcan que el trabajo 3 avanza 8 unidades (6→14) y el 4 avanza 7 (18→25).

| Trabajo | Inicio | Fin |
|---|---|---|
| 1 | 0 | 6 |
| 3 | 6 | 14 |
| 3\* (resto) | 14 | 18 |
| 4 | 18 | 25 |
| 4\* (resto) | 25 | 28 |
| 5 | 28 | 38 |
| 6 | 38 | 50 |
| 6\* (resto) | 50 | 55 |
| 7 | 55 | 71 |
| 2 | 71 | 89 (dibujado en otra fila, sin escala) |

**Resultados (cálculo propio, la hoja no los totaliza):** $C_1=6$, $C_3=18$, $C_4=28$, $C_5=38$, $C_6=55$, $C_7=71$, $C_2=89$. $\sum C_j=\sum w_jC_j=305$; tiempo de flujo total $\sum(C_j-r_j)=191$; $C_{max}=89$.

**Conclusión:** el trabajo más largo (2, con $p=18$ y $r=0$) queda de último porque siempre aparece otro con menor tiempo restante. En las tres llegadas ($t=14$, 25 y 50) se revisa la prioridad, pero el trabajo en proceso sigue: le queda poco y su razón es la mayor. Por eso, en este caso, la *preemption* no llega a cambiar de trabajo.

---

### Hoja `Tardanza Máxima`

**Objetivo (deducido):** evaluar una permutación de 20 trabajos para optimizarla después con Solver Evolutionary y la restricción "todos diferentes", como en la p. 48 de L17. El nombre de la hoja dice "Tardanza Máxima", pero no hay fechas de entrega: lo que se calcula es un "Tiempo de Flujo Ponderado".

**Datos** (columnas A-C). $P_j$ y $W_j$ de los trabajos 17-20 son `=RANDBETWEEN(10,50)`: cambian en cada recálculo; los valores de abajo son los que guardó Excel. Los trabajos 1-16 son valores fijos.

| Trabajo | $P_j$ | $W_j$ | | Trabajo | $P_j$ | $W_j$ |
|---|---|---|---|---|---|---|
| 1 | 10 | 12 | | 11 | 15 | 33 |
| 2 | 36 | 22 | | 12 | 41 | 44 |
| 3 | 36 | 23 | | 13 | 21 | 17 |
| 4 | 26 | 11 | | 14 | 24 | 36 |
| 5 | 48 | 40 | | 15 | 24 | 31 |
| 6 | 11 | 46 | | 16 | 14 | 22 |
| 7 | 23 | 37 | | 17 | 42 | 45 |
| 8 | 49 | 48 | | 18 | 46 | 36 |
| 9 | 21 | 24 | | 19 | 38 | 24 |
| 10 | 47 | 16 | | 20 | 48 | 47 |

**Secuencia** (F2:F21): 18, 19, 7, 2, 14, 17, 16, 5, 11, 6, 4, 8, 15, 20, 1, 13, 9, 3, 12, 10.

**Método:** `G = VLOOKUP(ROUND(F,0), A:B, 2)` trae el $P_j$ del trabajo en esa posición; la columna se rotula "Cj", pero no es un tiempo de terminación. `H = VLOOKUP(ROUND(F,0), A:C, 3)` trae $W_j$. `J3 = SUMPRODUCT(G2:G21, H2:H21)` = **20197**, rotulado "Tiempo de Flujo Ponderado". El `ROUND` sugiere que la secuencia la escriben variables continuas de Solver (deducido).

**Resultado y corrección (cálculo propio):**

- $20197=\sum_j p_jw_j$ es una constante: no depende de la secuencia, así que Solver no puede mejorarla.
- El $\sum w_jC_j$ real de la secuencia guardada, con $C_{[k]}=\sum_{i\le k}p_{[i]}$, es **192388** ($C_{max}=620$).
- El óptimo para $1||\sum w_jC_j$ (WSPT) es **151038**, con el orden 6, 11, 7, 16, 14, 15, 1, 9, 12, 17, 8, 20, 5, 13, 18, 3, 19, 2, 4, 10.

---

### Observaciones

- **`Reglas de Despacho`, J21:** `=AVERAGE(E22:E27)` omite la fila 21 e incluye la 27, que está vacía. Da 28.8; el promedio correcto de $C_j$ es 26.
- **`Reglas de Despacho`, E49 y E74:** `=C49` y `=C74` reinician el reloj en el trabajo 6. Probablemente se copió la fila de un bloque donde el 6 iba primero (SPT/WSPT; deducido). Esto altera $C_j$, $\sum C_j/n$, $\sum w_jC_j$ y, en el bloque H, la tardanza del trabajo 3. Ver las tablas corregidas arriba.
- **Número de tardíos** (J14, J23, J31, J39, J47, J73): escrito a mano, no calculado. Los valores coinciden con los programas correctos.
- **Bloque A:** los setups $s_j$ (3 h y 30 min) no se usan en los $C_j$. Las fechas de entrega están en texto o como fecha (19-oct), así que no se calcula tardanza. La máquina queda ociosa de 0 a 50 aunque Seminario ($r=0$) y Proyecto ($r=24$) estaban disponibles: no es un programa sin retrasos. El "Tiempo de Flujo" de la columna L es un promedio de $w_jC_j$, no una suma.
- **`Restricciones de Precedencia`:** la cadena se escribe `C-A-B` en los datos y `C-B-A` en los cálculos y la respuesta. La razón de la cadena completa no cambia, pero el orden interno sí. F26 se rotula "l=E" cuando es el prefijo hasta F. El título "1|Prec|ΣCj" usa pesos, así que en realidad es $\sum w_jC_j$. El bloque 3 se titula "1|Prec|…" pero es $1|r_j,prmp|\sum w_jC_j$.
- **Bloque 3, errores de texto:** "3\*=12-8=2" debería ser 4 (y `B40` usa $1/2=0.5$ en vez de $1/4$; la decisión no cambia). "Terminación del trabajo (t=18)" en E45 debería ser t=28. "en t=38" en D50 debería ser t=50, y E51 debería decir t=55.
- **`Tardanza Máxima`:** el nombre no corresponde al cálculo. La fórmula objetivo es invariante a la secuencia. `RANDBETWEEN` hace que los trabajos 17-20 cambien al recalcular.
- No hay hojas vacías ni gráficos de Excel.

## Anexo: volcado de celdas por hoja

> Valores calculados (los que Excel guardó). Hojas largas se recortan; las fórmulas se listan aparte. Abra el .xlsx para ver formato y gráficos.

### Hoja `Reglas de Despacho` — 77 filas × 13 columnas

| Fila | A | B | C | D | E | F | G | H | I | J | K | L | M |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3 |  | N | Trabajo | r_j | d_j | p_j | w_j | s_j | c_j |  | c_j - r_j | w_j * c_j |  |
| 4 |  | 2 | Proyecto | 24 | 24 h + 30 días | 10 h | 5 | 3 h | 60.33 |  | 36.33 | 301.65 |  |
| 5 |  | 4 | Seminario | 0 | 2026-10-19 | 2 h | 2 | 0 h | 103 |  | 103 | 206 |  |
| 6 |  | 1 | Pago Factura | 50 | 2026-10-19 | 20 min | 3 | 30 min | 50.33 | 20 min = 0,33 h | 0.33 | 150.99 |  |
| 7 |  | 3 | Entrevista de Trabajo | 100 | 100 h + 2 h | 1 h | 4 | 0 h | 101 | si r_j es > c_j del anterior, inicia en r_j | 1 | 404 |  |
| 8 |  |  |  |  |  |  |  |  |  | Tiempo de Flujo | 35.165 | 265.66 |  |
| 10 |  | ejemplo clase 20/10 |  |  |  |  |  |  |  |  |  |  |  |
| 12 |  | N | p_j | d_j | c_j | t_j | l_j | w_j | ΣC_j/n | 22 |  |  |  |
| 13 |  | 1 | 6 | 36 | 6 | 0 | -30 | 1 | Tardanza Ponderada (Σw_j*t_j) | 112 |  |  |  |
| 14 |  | 2 | 4 | 21 | 10 | 0 | -11 | 1 | # Trabajos Tardíos (Σu_j) | 3 |  |  |  |
| 15 |  | 3 | 7 | 18 | 17 | 0 | -1 | 1 |  |  |  |  |  |
| 16 |  | 4 | 12 | 15 | 29 | 14 | 14 | 3 |  |  |  |  |  |
| 17 |  | 5 | 5 | 1 | 34 | 33 | 33 | 2 |  |  |  |  |  |
| 18 |  | 6 | 2 | 32 | 36 | 4 | 4 | 1 |  |  |  |  |  |
| 20 |  | N | p_j | d_j | c_j | t_j | l_j | w_j |  |  | w_j*c_j |  |  |
| 21 | Secuencia elegida al azar | 4 | 12 | 15 | 12 | 0 | -3 | 3 | ΣC_j/n | 28.8 | 36 |  |  |
| 22 |  | 3 | 7 | 18 | 19 | 1 | 1 | 1 | Tardanza Ponderada (Σw_j*t_j) | 76 | 19 |  |  |
| 23 |  | 1 | 6 | 36 | 25 | 0 | -11 | 1 | # Trabajos Tardíos (Σu_j) | 4 | 25 |  |  |
| 24 |  | 5 | 5 | 1 | 30 | 29 | 29 | 2 |  |  | 60 |  |  |
| 25 |  | 2 | 4 | 21 | 34 | 13 | 13 | 1 |  |  | 34 |  |  |
| 26 |  | 6 | 2 | 32 | 36 | 4 | 4 | 1 |  |  | 36 |  |  |
| 27 |  |  |  |  |  |  |  |  |  |  | 210 |  |  |
| 28 |  | N | p_j | d_j | c_j | t_j | l_j | w_j |  |  | w_j/p_j | Prioridad (mayor a menor) | w_j*c_j |
| 29 | Secuencia organizada desde el más corto | 6 | 2 | 32 | 2 | 0 | -30 | 1 | ΣC_j/n | 16 | 0.5 | 1 | 2 |
| 30 |  | 2 | 4 | 21 | 6 | 0 | -15 | 1 | Tardanza Ponderada (Σw_j*t_j) | 89 | 0.25 | 3 | 6 |
| 31 |  | 5 | 5 | 1 | 11 | 10 | 10 | 2 | # Trabajos Tardíos (Σu_j) | 3 | 0.4 | 2 | 22 |
| 32 |  | 1 | 6 | 36 | 17 | 0 | -19 | 1 |  |  | 0.166667 | 5 | 17 |
| 33 |  | 3 | 7 | 18 | 24 | 6 | 6 | 1 |  |  | 0.142857 | 6 | 24 |
| 34 |  | 4 | 12 | 15 | 36 | 21 | 21 | 3 |  |  | 0.25 | 4 | 108 |
| 35 |  |  |  |  |  |  |  |  |  |  |  |  | 179 |
| 36 |  | N | p_j | d_j | c_j | t_j | l_j | w_j |  |  | w_j*c_j |  |  |
| 37 | Secuencia por prioridad WSPT | 6 | 2 | 32 | 2 | 0 | -30 | 1 | ΣC_j/n | 18 | 2 |  |  |
| 38 |  | 5 | 5 | 1 | 7 | 6 | 6 | 2 | Tardanza Ponderada (Σw_j*t_j) | 54 | 14 |  |  |
| 39 |  | 2 | 4 | 21 | 11 | 0 | -10 | 1 | # Trabajos Tardíos (Σu_j) | 3 | 11 |  |  |
| 40 |  | 4 | 12 | 15 | 23 | 8 | 8 | 3 |  |  | 69 |  |  |
| 41 |  | 1 | 6 | 36 | 29 | 0 | -7 | 1 |  |  | 29 |  |  |
| 42 |  | 3 | 7 | 18 | 36 | 18 | 18 | 1 |  |  | 36 |  |  |
| 43 |  |  |  |  |  |  |  |  |  |  | 161 |  |  |
| 44 |  | N | p_j | d_j | c_j | t_j | l_j | w_j |  |  | w_j*c_j |  |  |
| 45 | Secuencia por tiempo de terminación EDD | 5 | 5 | 1 | 5 | 4 | 4 | 2 | ΣC_j/n | 14 | 10 |  |  |
| 46 |  | 4 | 12 | 15 | 17 | 2 | 2 | 3 | Tardanza Ponderada (Σw_j*t_j) | 27 | 51 |  |  |
| 47 |  | 3 | 7 | 18 | 24 | 6 | 6 | 1 | # Trabajos Tardíos (Σu_j) | 4 | 24 |  |  |
| 48 |  | 2 | 4 | 21 | 28 | 7 | 7 | 1 |  |  | 28 |  |  |
| 49 |  | 6 | 2 | 32 | 2 | 0 | -30 | 1 |  |  | 2 |  |  |
| 50 |  | 1 | 6 | 36 | 8 | 0 | -28 | 1 |  |  | 8 |  |  |
| 51 |  |  |  |  |  |  |  |  |  |  | 123 |  |  |
| 52 |  | N | p_j | d_j | s_j (t=0) | s_j (t=5) | s_j (t=17) | s_j (t=21) | s_j (t=28) |  |  |  |  |
| 53 | Secuencia por holgura mínima MS | 1 | 6 | 36 | 30 | 25 | 13 | 9 | 2 |  |  |  |  |
| 54 |  | 2 | 4 | 21 | 17 | 12 | 0 |  |  |  |  |  |  |
| 55 |  | 3 | 7 | 18 | 11 | 6 | 0 | 0 |  |  |  |  |  |
| 56 |  | 4 | 12 | 15 | 3 | 0 |  |  |  |  |  |  |  |
| 57 |  | 5 | 5 | 1 | 0 |  |  |  |  |  |  |  |  |
| 58 |  | 6 | 2 | 32 | 30 | 25 | 13 | 9 | 2 |  |  |  |  |
| 59 |  |  |  | Menor Holgura | 5 | 17 | 21 | 28 |  |  |  |  |  |
| 61 |  | N | p_j | d_j | c_j | t_j |  |  |  |  |  |  |  |
| 62 | Secuencia por holgura mínima MS | 5 | 5 | 1 | 5 | 4 |  |  |  |  |  |  |  |
| 63 |  | 4 | 12 | 15 | 17 | 2 |  |  |  |  |  |  |  |
| 64 |  | 2 | 4 | 21 | 21 | 0 |  |  |  |  |  |  |  |
| 65 |  | 3 | 7 | 18 | 28 | 10 |  |  |  |  |  |  |  |
| 66 |  | 6 | 2 | 32 | 30 | 0 |  |  |  |  |  |  |  |

> **Hoja larga:** arriba se muestran 60 de 70 filas con datos. **Todos los valores de la hoja están en [`programacion-produccion-una-maquina-datos/Reglas_de_Despacho.csv`](./programacion-produccion-una-maquina-datos/Reglas_de_Despacho.csv)** (CSV, UTF-8).

**Fórmulas (26 patrones distintos):**

- `I4`: `=I6+10`
- `K4`: `=I4-D4`
- `L4`: `=G4*I4`
- `I6`: `=50+0.33`
- `I7`: `=100+1`
- `K8`: `=AVERAGE(K4:K7)`
- `L8`: `=AVERAGE(L4:L7)`
- `J12`: `=AVERAGE(E13:E18)`
- `E13`: `=C13`
- `F13`: `=IF(E13<D13,0,E13-D13)`
- `G13`: `=IF(F13>0,F13,E13-D13)`
- `E14`: `=E13+C14`
- `K21`: `=E21*H21`
- `K27`: `=SUM(K21:K26)`
- `K29`: `=H29/C29`
- `M35`: `=SUM(M29:M34)`
- `K37`: `=H37*E37`
- `E53`: `=IF(D53-C53>0,D53-C53,0)`
- `F53`: `=IF(D53-C53-$E$59>0,D53-C53-$E$59,0)`
- `G53`: `=IF(D53-C53-$F$59>0,D53-C53-$F$59,0)`
- `H53`: `=IF(D53-C53-$G$59>0,D53-C53-$G$59,0)`
- `I53`: `=IF(D53-C53-$H$59>0,D53-C53-$H$59,0)`
- `F59`: `=C56+E59`
- `G59`: `=C54+F59`
- `H59`: `=C55+G59`
- `F68`: `=SUM(F62:F67)`

### Hoja `Restricciones de Precedencia` — 54 filas × 12 columnas · 1 imagen(es)

| Fila | A | B | C | D | E | F | G | H | I | J | K | L |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1\|Prec\|𝚺Cj | Si, NO se pueden romper las cadenas |  |  |  |  |  |  |  |  |  |  |
| 2 | Job | Pj | Wj | Prec |  |  |  |  |  |  |  |  |
| 3 | A | 2 | 1 | C-A-B |  |  |  |  |  |  |  |  |
| 4 | B | 4 | 2 | E-F |  |  |  |  |  |  |  |  |
| 5 | C | 11 | 3 | D |  |  |  |  |  |  |  |  |
| 6 | D | 30 | 2 |  |  |  |  |  |  |  |  |  |
| 7 | E | 13 | 5 |  |  |  |  |  |  |  |  |  |
| 8 | F | 20 | 1 |  |  |  |  |  |  |  |  |  |
| 10 | Cadena C-B-A |  |  | Cadena E-F |  |  | Cadena D |  |  |  |  |  |
| 11 | 𝚺Wj/𝚺Pj | 0.352941 |  | 𝚺Wj/𝚺Pj | 0.181818 |  | 𝚺Wj/𝚺Pj | 0.0666667 |  |  |  |  |
| 12 |  | Se inicia con la cadena que tiene la mayor relación |  |  |  |  |  |  |  |  |  |  |
| 13 | Respuesta | C-B-A-E-F-D |  |  |  |  |  |  |  |  |  |  |
| 15 | 1\|Prec\|𝚺Cj | Si SI se pueden romper las cadenas |  |  |  |  |  |  |  |  |  |  |
| 16 | Job | Pj | Wj | Prec |  |  |  |  |  |  |  |  |
| 17 | A | 2 | 1 | C-A-B |  |  |  |  |  |  |  |  |
| 18 | B | 4 | 2 | E-F |  |  |  |  |  |  |  |  |
| 19 | C | 11 | 3 | D |  |  |  |  |  |  |  |  |
| 20 | D | 30 | 2 |  |  |  |  |  |  |  |  |  |
| 21 | E | 13 | 5 |  |  |  |  |  |  |  |  |  |
| 22 | F | 20 | 1 |  |  |  |  |  |  |  |  |  |
| 24 | Cadena C-B-A |  |  |  | Cadena E-F |  |  |  |  |  |  |  |
| 25 | 𝚺Wj/𝚺Pj (l=C) | 0.272727 |  |  | 𝚺Wj/𝚺Pj (l=E) | 0.384615 |  |  |  |  |  |  |
| 26 | 𝚺Wj/𝚺Pj (l=B) | 0.333333 |  |  | 𝚺Wj/𝚺Pj (l=E) | 0.181818 |  |  |  |  |  |  |
| 27 | 𝚺Wj/𝚺Pj (l=A) | 0.352941 |  |  |  | l*= E |  |  |  |  |  |  |
| 28 |  | l* =A | se busca el mayor |  |  | ρ-factor = 0,38 |  |  |  |  |  |  |
| 29 |  | ρ-factor = 0,35 |  |  |  |  |  |  |  |  |  |  |
| 31 | 1\|Prec\|𝚺Cj/𝚺Wj*Cj |  |  |  |  |  |  |  |  |  |  |  |
| 32 | Trabajo | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Wj = | 1 |  | Wj/Pj |
| 33 | Pj | 6 | 18 | 12 | 10 | 10 | 17 | 16 |  |  | 1 | 0.166667 |
| 34 | Rj | 0 | 0 | 0 | 14 | 25 | 25 | 50 |  |  | 2 | 0.0555556 |
| 35 |  |  |  |  |  |  |  |  |  |  | 3 | 0.0833333 |
| 36 | Max (Wj/Pj) | 0.166667 | 1 | en t=0, trabajos disponibles: 1, 2, 3 | se mueve el reloj t | Llegada del proximo trabajo (t=14) |  |  |  |  | 4 | 0.1 |
| 37 |  |  |  |  |  | Terminación del trabajo (t=6) |  |  |  |  | 5 | 0.1 |
| 38 | Max (Wj/Pj) | 0.0833333 | 3 | en t=6, trabajos disponibles:  2, 3 | el 3 no se termina (interrumpido por la llegada del 4) | 3*=12-8=2 |  |  |  |  | 6 | 0.0588235 |
| 39 |  |  |  |  |  |  |  |  |  |  | 7 | 0.0625 |
| 40 | Max (Wj/Pj) | 0.5 | 3* | en t=14, trabajos disponibles:  2, 3*,4 | Llegada del proximo trabajo (t=25) |  |  |  |  |  |  |  |
| 41 |  |  |  |  | Terminación del trabajo (t=18) |  |  |  |  |  |  |  |
| 42 | Max (Wj/Pj) | 0.1 | 4 | en t=18, trabajos disponibles:  2, 4 | el 4 no se termina (interrumpido por la llegada del 5 y 6) | 4*=10-7=3 |  |  |  |  |  |  |
| 44 | Max (Wj/Pj) | 0.333333 | 4* | en t=25, trabajos disponibles:  2, 4*, 5, 6 | Llegada del proximo trabajo (t=50) |  |  |  |  |  |  |  |
| 45 |  |  |  |  | Terminación del trabajo (t=18) |  |  |  |  |  |  |  |
| 46 | Max (Wj/Pj) | 0.1 | 5 | en t=28, trabajos disponibles: 2, 5, 6 | Llegada del proximo trabajo (t=50) |  |  |  |  |  |  |  |
| 47 |  |  |  |  | Terminación del trabajo (t=38) |  |  |  |  |  |  |  |
| 48 | Max (Wj/Pj) | 0.0588235 | 6 | en t=38, trabajos disponibles: 2, 6 | el 6 no se termina (interrumpido por la llegada del 7) | 6*=17-12 |  |  |  |  |  |  |
| 50 | Max (Wj/Pj) | 0.2 | 6* | en t=38, trabajos disponibles: 2, 6*, 7 | Llegada del proximo trabajo (t=50) |  |  |  |  |  |  |  |
| 51 |  |  |  |  | Terminación del trabajo (t=38) |  |  |  |  |  |  |  |
| 52 | Max (Wj/Pj) | 0.0625 | 7 | en t=55, trabajos disponibles: 2, 7 |  |  |  |  |  |  |  |  |
| 54 |  |  | 2 |  |  |  |  |  |  |  |  |  |

**Fórmulas (14 patrones distintos):**

- `B11`: `=(C5+C4+C3)/(B5+B4+B3)`
- `E11`: `=(C7+C8)/(B7+B8)`
- `H11`: `=C6/B6`
- `L33`: `=$J$32/B33`
- `L34`: `=J32/C33`
- `L35`: `=J32/D33`
- `B36`: `=MAX(L33,L34,L35)`
- `L36`: `=J32/E33`
- `L37`: `=J32/F33`
- `B38`: `=MAX(L34,L35)`
- `L38`: `=J32/G33`
- `L39`: `=J32/H33`
- `B40`: `=MAX(L34,J32/2,L36)`
- `B44`: `=MAX(L34,J32/3,L37,L38)`

### Hoja `Tardanza Máxima` — 21 filas × 10 columnas

| Fila | A | B | C | D | E | F | G | H | I | J |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Trabajo | Pj | Wj |  |  | Secuencia | Cj | Wj |  |  |
| 2 | 1 | 10 | 12 |  |  | 18 | 46 | 36 |  | Tiempo de Flujo Ponderado |
| 3 | 2 | 36 | 22 |  |  | 19 | 38 | 24 |  | 20197 |
| 4 | 3 | 36 | 23 |  |  | 7 | 23 | 37 |  |  |
| 5 | 4 | 26 | 11 |  |  | 2 | 36 | 22 |  |  |
| 6 | 5 | 48 | 40 |  |  | 14 | 24 | 36 |  |  |
| 7 | 6 | 11 | 46 |  |  | 17 | 42 | 45 |  |  |
| 8 | 7 | 23 | 37 |  |  | 16 | 14 | 22 |  |  |
| 9 | 8 | 49 | 48 |  |  | 5 | 48 | 40 |  |  |
| 10 | 9 | 21 | 24 |  |  | 11 | 15 | 33 |  |  |
| 11 | 10 | 47 | 16 |  |  | 6 | 11 | 46 |  |  |
| 12 | 11 | 15 | 33 |  |  | 4 | 26 | 11 |  |  |
| 13 | 12 | 41 | 44 |  |  | 8 | 49 | 48 |  |  |
| 14 | 13 | 21 | 17 |  |  | 15 | 24 | 31 |  |  |
| 15 | 14 | 24 | 36 |  |  | 20 | 48 | 47 |  |  |
| 16 | 15 | 24 | 31 |  |  | 1 | 10 | 12 |  |  |
| 17 | 16 | 14 | 22 |  |  | 13 | 21 | 17 |  |  |
| 18 | 17 | 42 | 45 |  |  | 9 | 21 | 24 |  |  |
| 19 | 18 | 46 | 36 |  |  | 3 | 36 | 23 |  |  |
| 20 | 19 | 38 | 24 |  |  | 12 | 41 | 44 |  |  |
| 21 | 20 | 48 | 47 |  |  | 10 | 47 | 16 |  |  |

**Fórmulas (4 patrones distintos):**

- `G2`: `=VLOOKUP(ROUND(F2,0),$A$2:$B$21,2,FALSE)`
- `H2`: `=VLOOKUP(ROUND(F2,0),$A$2:$C$21,3,FALSE)`
- `J3`: `=SUMPRODUCT(G2:G21,H2:H21)`
- `B18`: `=RANDBETWEEN(10,50)`

