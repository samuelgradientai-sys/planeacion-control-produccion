"""
Plantilla base para GradeScope - RETO 01 Willy Wonka
-------------------------------------------------------
             INSTRUCCIONES IMPORTANTES
-------------------------------------------------------
1. NO cambiar el nombre de la clase ni las funciones principales.
   - Clase obligatoria: Schedulling
   - Metodos obligatorios: generar_instancia(), resolver_instancia(), ejecutar_experimentos()
2. SOLO deben modificar:
   - El contenido de generar_instancia() para crear sus propios datos.
   - El contenido de resolver_instancia() para construir su modelo de optimizacion.
3. NO modificar:
   - Los nombres de las funciones o variables internas del experimento.
   - El metodo ejecutar_experimentos() ni su estructura.
   - El nombre del archivo: debe llamarse EXACTAMENTE `reto_schedulling.py`
4. El metodo ejecutar_experimentos():
   - Ejecuta automaticamente 30 instancias.
   - Mide el tiempo de ejecucion por instancia.
   - Devuelve un consolidado con los tiempos individuales.
   - Reporta el tiempo promedio y el total al final.

ARCHIVO GENERADO por construir_plantillas.py a partir de reto1.py (no editar a mano).
Algoritmo: cota inferior por ordenes de tipo + heuristica (NEH, bloques por tipo,
busqueda local con aceleracion de Taillard) + programacion dinamica acotada que
encuentra y demuestra el optimo. Ver reto1.py e INFORME_TECNICO.md.
"""

# Agregar dependencias si es necesario, pero sin remover las que ya se encuentran abajo
import random
import numpy as np
import time
import pandas as pd
try:  # modulo del ejemplo del profesor; no se usa y puede no existir en Gradescope
    from optimizador import load_from_dict, run_ga  # noqa: F401
except ImportError:
    pass
import json
import itertools
import math

# === INICIO ALGORITMO ===
# ---------------------------------------------------------------- parametros
# Con 200 instancias del generador de la plantilla: optimo demostrado en 200/200,
# ~3,5 ms en promedio (mediana ~0,4 ms, peor caso ~60 ms).
TIEMPO_MAX_R1 = 2.0      # tope de seguridad (segundos) por instancia
MAX_ITER_R1 = 1500       # iteraciones maximas del Iterated Greedy
MAX_SIN_MEJORA_R1 = 5    # (respaldo) para si el mejor no cambia en estas iteraciones
D_DESTRUCCION_R1 = 4     # lotes que se retiran en cada destruccion
EXACTO_R1 = True         # demostrar/encontrar el optimo con el metodo exacto
MAX_ESTADOS_R1 = 400000  # tope de seguridad del exacto (si se pasa, queda la heuristica)
T_ACEPTACION_R1 = 0.4    # constante de temperatura de Ruiz y Stutzle
SEMILLA_R1 = 2026        # semilla propia: no altera el random global
PENAL_R1 = 10 ** 6       # penalidad interna por cada pareja N -> R

MAQUINAS_R1 = ("M1", "M2", "M3")


class WillyWonka:
    """Datos de una instancia y los procedimientos del algoritmo."""

    def __init__(self, data):
        lotes = data["lotes"]
        setup = data["setup"]
        self.nombres = list(lotes)
        n = self.n = len(self.nombres)
        self.tipo = [str(lotes[x]["tipo"]).strip().upper() for x in self.nombres]
        self.P1 = [lotes[x]["M1"] for x in self.nombres]
        self.P2 = [lotes[x]["M2"] for x in self.nombres]
        self.P3 = [lotes[x]["M3"] for x in self.nombres]

        # alistamiento por maquina y pareja de tipos (anterior, siguiente)
        tipos = sorted(set(self.tipo))
        self.st = {}
        for m in MAQUINAS_R1:
            tabla = setup.get(m, {})
            for a in tipos:
                for b in tipos:
                    v = tabla.get(f"{a}-{b}")
                    if v is None and isinstance(tabla.get(a), dict):
                        v = tabla[a].get(b)
                    self.st[m, a, b] = v if v is not None else 0

        # matrices lote x lote; la fila n es el "inicio" (sin lote anterior)
        t = self.tipo
        self.S1, self.S2, self.S3 = (
            [[self.st[m, t[i], t[j]] for j in range(n)] for i in range(n)] + [[0] * n]
            for m in MAQUINAS_R1
        )
        self.PROH = [[1 if (t[i] == "N" and t[j] == "R") else 0 for j in range(n)]
                     for i in range(n)] + [[0] * n]
        self._preparar_tipos()

    # ------------------------------------------------------------ evaluacion
    def evaluar(self, seq):
        """Cmax de la secuencia + PENAL por cada pareja N -> R."""
        P1, P2, P3 = self.P1, self.P2, self.P3
        S1, S2, S3, PROH = self.S1, self.S2, self.S3, self.PROH
        c1 = c2 = c3 = 0
        viol = 0
        a = self.n
        for x in seq:
            c1 += S1[a][x] + P1[x]
            if c1 > c2:
                c2 = c1
            c2 += S2[a][x] + P2[x]
            if c2 > c3:
                c3 = c2
            c3 += S3[a][x] + P3[x]
            viol += PROH[a][x]
            a = x
        return c3 + PENAL_R1 * viol

    def mejor_insercion(self, pi, j):
        """Mejor posicion para insertar el lote j en la secuencia parcial pi.

        Aceleracion de Taillard adaptada a alistamientos:
          e[k]  = fin del lote pi[k-1] en cada maquina (cabezas)
          q[k]  = camino mas largo desde el lote pi[k] hasta el final (colas)
        Al insertar j entre a = pi[i-1] y b = pi[i] se recalculan solo j y b
        (b cambia de alistamiento porque ahora su anterior es j):
          Cmax = max_m ( fin de b en m + q[i+1][m] )
        Devuelve (valor penalizado, posicion).
        """
        P1, P2, P3 = self.P1, self.P2, self.P3
        S1, S2, S3, PROH = self.S1, self.S2, self.S3, self.PROH
        ini = self.n
        L = len(pi)

        # cabezas
        e1 = [0] * (L + 1)
        e2 = [0] * (L + 1)
        e3 = [0] * (L + 1)
        c1 = c2 = c3 = 0
        viol = 0
        a = ini
        for k in range(L):
            x = pi[k]
            c1 += S1[a][x] + P1[x]
            if c1 > c2:
                c2 = c1
            c2 += S2[a][x] + P2[x]
            if c2 > c3:
                c3 = c2
            c3 += S3[a][x] + P3[x]
            e1[k + 1] = c1
            e2[k + 1] = c2
            e3[k + 1] = c3
            viol += PROH[a][x]
            a = x

        # colas
        q1 = [0] * (L + 1)
        q2 = [0] * (L + 1)
        q3 = [0] * (L + 1)
        t1 = t2 = t3 = 0
        for k in range(L - 1, -1, -1):
            x = pi[k]
            a = pi[k - 1] if k else ini
            t3 = t3 + S3[a][x] + P3[x]
            t2 = (t2 if t2 > t3 else t3) + S2[a][x] + P2[x]
            t1 = (t1 if t1 > t2 else t2) + S1[a][x] + P1[x]
            q1[k] = t1
            q2[k] = t2
            q3[k] = t3

        # todas las posiciones de insercion
        p1j, p2j, p3j = P1[j], P2[j], P3[j]
        mejor = float("inf")
        mejor_pos = 0
        for i in range(L + 1):
            a = pi[i - 1] if i else ini
            f1 = e1[i] + S1[a][j] + p1j
            f2 = (e2[i] if e2[i] > f1 else f1) + S2[a][j] + p2j
            f3 = (e3[i] if e3[i] > f2 else f2) + S3[a][j] + p3j
            v = viol + PROH[a][j]
            if i < L:
                b = pi[i]
                v += PROH[j][b] - PROH[a][b]
                g1 = f1 + S1[j][b] + P1[b]
                g2 = (f2 if f2 > g1 else g1) + S2[j][b] + P2[b]
                g3 = (f3 if f3 > g2 else g2) + S3[j][b] + P3[b]
                c = g1 + q1[i + 1]
                t = g2 + q2[i + 1]
                if t > c:
                    c = t
                t = g3 + q3[i + 1]
                if t > c:
                    c = t
            else:
                c = f3
            val = c + PENAL_R1 * v
            if val < mejor:
                mejor = val
                mejor_pos = i
        return mejor, mejor_pos

    # ------------------------------------------------- cotas y metodo exacto
    def _preparar_tipos(self):
        """Tablas por TIPO de lote (no por lote), que usan la cota y el exacto."""
        tipos = sorted(set(self.tipo))
        k = self.k = len(tipos)
        self.ti = [tipos.index(t) for t in self.tipo]
        # fila k = inicio (sin lote anterior): alistamiento 0 y nada prohibido
        self.PT = [[tipos[a] == "N" and tipos[b] == "R" for b in range(k)] for a in range(k)] + [[False] * k]
        self.STT = [[[self.st[m, tipos[a], tipos[b]] if a < k else 0 for b in range(k)]
                     for a in range(k + 1)] for m in MAQUINAS_R1]
        self.lotes_tipo = [[j for j in range(self.n) if self.ti[j] == t] for t in range(k)]
        self._caminos = {}
        self._resto = {}

    def caminos(self, lt, S):
        """Ordenes de tipos posibles para lo que falta: recorridos que salen del
        tipo lt, pasan por todos los tipos del conjunto S (mascara de bits) y
        nunca van de N a R. Devuelve la lista de (alist. M1, alist. M2, alist. M3,
        primer tipo, ultimo tipo) no dominados. Se calcula una vez y se guarda."""
        clave0 = (lt, S)
        res = self._caminos.get(clave0)
        if res is not None:
            return res
        k, PT = self.k, self.PT
        A, B, C = self.STT
        est = {}
        cola = []

        def agregar(clave, v):
            lst = est.setdefault(clave, [])
            for u in lst:
                if u[0] <= v[0] and u[1] <= v[1] and u[2] <= v[2]:
                    return
            lst[:] = [u for u in lst if not (v[0] <= u[0] and v[1] <= u[1] and v[2] <= u[2])]
            lst.append(v)
            cola.append((clave, v))

        for t1 in range(k):
            if S >> t1 & 1 and not PT[lt][t1]:
                agregar((1 << t1, t1, t1), (A[lt][t1], B[lt][t1], C[lt][t1]))
        while cola:
            (cub, act, t1), v = cola.pop()
            if v not in est[(cub, act, t1)]:
                continue
            for b in range(k):
                if b != act and S >> b & 1 and not PT[act][b]:
                    agregar((cub | 1 << b, b, t1), (v[0] + A[act][b], v[1] + B[act][b], v[2] + C[act][b]))
        res = [(v[0], v[1], v[2], t1, act) for (cub, act, t1), lst in est.items() if cub == S for v in lst]
        self._caminos[clave0] = res
        return res

    def datos_resto(self, mask):
        """Datos de los lotes que faltan (los que no estan en mask): sumas de
        tiempos, tipos presentes y minimos por tipo. Se guardan por mascara."""
        d = self._resto.get(mask)
        if d is None:
            k, ti = self.k, self.ti
            P1, P2, P3 = self.P1, self.P2, self.P3
            INF = float("inf")
            sp1 = sp2 = sp3 = S = 0
            mp1 = [INF] * k
            mp2 = [INF] * k
            mp12 = [INF] * k
            mp3 = [INF] * k
            m23 = [INF] * k
            resto = []
            for j in range(self.n):
                if mask >> j & 1:
                    continue
                resto.append(j)
                t = ti[j]
                S |= 1 << t
                a, b, c = P1[j], P2[j], P3[j]
                sp1 += a
                sp2 += b
                sp3 += c
                if a < mp1[t]:
                    mp1[t] = a
                if b < mp2[t]:
                    mp2[t] = b
                if a + b < mp12[t]:
                    mp12[t] = a + b
                if c < mp3[t]:
                    mp3[t] = c
                if b + c < m23[t]:
                    m23[t] = b + c
            d = (resto, sp1, sp2, sp3, S, mp1, mp2, mp12, mp3, m23)
            self._resto[mask] = d
        return d

    def resto_sin(self, d, j, nmask):
        """datos_resto(nmask) a partir de los datos d del estado padre, donde
        nmask = padre + lote j: se resta j y solo se recalculan los minimos de
        su tipo (mucho mas barato que recorrer todos los lotes)."""
        r = self._resto.get(nmask)
        if r is not None:
            return r
        resto, sp1, sp2, sp3, S, mp1, mp2, mp12, mp3, m23 = d
        P1, P2, P3 = self.P1, self.P2, self.P3
        t = self.ti[j]
        mp1, mp2, mp12, mp3, m23 = mp1[:], mp2[:], mp12[:], mp3[:], m23[:]
        INF = float("inf")
        a1 = a2 = a12 = a3 = a23 = INF
        for x in self.lotes_tipo[t]:
            if nmask >> x & 1:
                continue
            a, b, c = P1[x], P2[x], P3[x]
            if a < a1:
                a1 = a
            if b < a2:
                a2 = b
            if a + b < a12:
                a12 = a + b
            if c < a3:
                a3 = c
            if b + c < a23:
                a23 = b + c
        mp1[t], mp2[t], mp12[t], mp3[t], m23[t] = a1, a2, a12, a3, a23
        if a1 == INF:                       # ya no quedan lotes de ese tipo
            S &= ~(1 << t)
        r = ([x for x in resto if x != j], sp1 - P1[j], sp2 - P2[j], sp3 - P3[j], S,
             mp1, mp2, mp12, mp3, m23)
        self._resto[nmask] = r
        return r

    def cota(self, c1, c2, c3, lt, d, tope=float("inf")):
        """Cota inferior del Cmax desde un estado parcial: maquinas libres en
        (c1, c2, c3), ultimo tipo lt y lotes restantes descritos por d.

        Para cada orden de tipos posible (ver caminos) con primer tipo t1 y
        ultimo tipo tk, y alistamientos w1, w2, w3 en cada maquina:
          B1 = c1 + sum p1 + w1 + min (p2+p3) de los lotes de tipo tk
          B2 = max(c2, c1 + s1 + min p1 de tipo t1) + sum p2 + w2 + min p3 de tipo tk
          B3 = max(c3, llegada a M3 del primer lote) + sum p3 + w3
        La cota es el minimo, entre los ordenes, de max(B1, B2, B3): las tres
        maquinas tienen que usar el MISMO orden de tipos."""
        _, sp1, sp2, sp3, S, mp1, mp2, mp12, mp3, m23 = d
        A, B, _ = self.STT
        mejor = tope
        a1 = c1 + sp1
        for w1, w2, w3, t1, tk in self.caminos(lt, S):
            b = a1 + w1 + m23[tk]
            if b >= mejor:
                continue
            s1f = A[lt][t1]
            x = c1 + s1f + mp1[t1]
            b2 = (c2 if c2 > x else x) + sp2 + w2 + mp3[tk]
            if b2 > b:
                b = b2
                if b >= mejor:
                    continue
            s2f = B[lt][t1]
            y = c2 + s2f + mp2[t1]
            z = c1 + s1f + s2f + mp12[t1]
            if z > y:
                y = z
            if c3 > y:
                y = c3
            b3 = y + sp3 + w3
            if b3 > b:
                b = b3
            if b < mejor:
                mejor = b
        return mejor

    def cota_inferior(self):
        """Cota inferior del Cmax de toda la instancia."""
        return self.cota(0, 0, 0, self.k, self.datos_resto(0))

    def exacto(self, ub, limite):
        """Programacion dinamica acotada (tipo ramificacion y acotamiento).

        Construye las secuencias lote a lote, por capas. Estado: (lotes ya
        programados, tipo del ultimo). De cada estado se guardan solo los
        vectores (fin M1, fin M2, fin M3) no dominados, y se descarta todo
        estado cuya cota ya no puede mejorar ub (la mejor solucion conocida).
        Devuelve (secuencia o None, valor, completo): si completo es True y la
        secuencia es None, ub era optimo; si hay secuencia, es la optima."""
        n, k = self.n, self.k
        P1, P2, P3, ti, PT = self.P1, self.P2, self.P3, self.ti, self.PT
        A, B, C = self.STT
        cota, resto_sin = self.cota, self.resto_sin
        lleno = (1 << n) - 1
        capa = {(0, k): [(0, 0, 0, None)]}
        estados = 0
        for _ in range(n):
            nueva = {}
            for (mask, lt), frente in capa.items():
                d = self.datos_resto(mask)
                for j in d[0]:
                    tj = ti[j]
                    if PT[lt][tj]:
                        continue
                    nmask = mask | (1 << j)
                    s1, s2, s3 = A[lt][tj], B[lt][tj], C[lt][tj]
                    p1, p2, p3 = P1[j], P2[j], P3[j]
                    ultimo = nmask == lleno
                    if not ultimo:
                        dn = resto_sin(d, j, nmask)
                    clave = (nmask, tj)
                    for ent in frente:
                        n1 = ent[0] + s1 + p1
                        n2 = (ent[1] if ent[1] > n1 else n1) + s2 + p2
                        n3 = (ent[2] if ent[2] > n2 else n2) + s3 + p3
                        if ultimo:
                            if n3 >= ub:
                                continue
                        elif cota(n1, n2, n3, tj, dn, ub) >= ub:
                            continue
                        lst = nueva.get(clave)
                        if lst is None:
                            nueva[clave] = [(n1, n2, n3, (j, ent))]
                            estados += 1
                            continue
                        dominado = False
                        for e in lst:
                            if e[0] <= n1 and e[1] <= n2 and e[2] <= n3:
                                dominado = True
                                break
                        if dominado:
                            continue
                        lst[:] = [e for e in lst if not (n1 <= e[0] and n2 <= e[1] and n3 <= e[2])]
                        lst.append((n1, n2, n3, (j, ent)))
                        estados += 1
                if estados > MAX_ESTADOS_R1 or time.perf_counter() > limite:
                    return None, ub, False
            capa = nueva
            if not capa:
                return None, ub, True
        fin = min((e for lst in capa.values() for e in lst), key=lambda e: e[2])
        seq = []
        e = fin
        while e[3] is not None:
            j, e = e[3]
            seq.append(j)
        return seq[::-1], fin[2], True

    # -------------------------------------------------------- constructivos
    def neh(self):
        """NEH: lotes por tiempo total decreciente, cada uno a su mejor posicion."""
        P1, P2, P3 = self.P1, self.P2, self.P3
        orden = sorted(range(self.n), key=lambda j: -(P1[j] + P2[j] + P3[j]))
        seq = [orden[0]]
        for j in orden[1:]:
            _, i = self.mejor_insercion(seq, j)
            seq.insert(i, j)
        return seq

    def por_bloques(self):
        """Una secuencia por cada orden de bloques de tipo que no ponga N antes de R.
        Dentro del bloque: regla de Johnson con A = p1+p2 y B = p2+p3."""
        P1, P2, P3 = self.P1, self.P2, self.P3
        presentes = list(dict.fromkeys(self.tipo))
        salida = []
        for orden in itertools.permutations(presentes):
            if any(orden[k] == "N" and orden[k + 1] == "R" for k in range(len(orden) - 1)):
                continue
            seq = []
            for t in orden:
                grupo = [j for j in range(self.n) if self.tipo[j] == t]
                g1 = sorted((j for j in grupo if P1[j] + P2[j] < P2[j] + P3[j]),
                            key=lambda j: P1[j] + P2[j])
                g2 = sorted((j for j in grupo if P1[j] + P2[j] >= P2[j] + P3[j]),
                            key=lambda j: -(P2[j] + P3[j]))
                seq += g1 + g2
            salida.append(seq)
        return salida

    # --------------------------------------------------------- mejora
    def busqueda_local(self, seq, val, rng):
        """Insercion: saca cada lote y lo pone en su mejor posicion, hasta que nada mejore."""
        mejora = True
        while mejora:
            mejora = False
            orden = seq[:]
            rng.shuffle(orden)
            for j in orden:
                k = seq.index(j)
                pi = seq[:k] + seq[k + 1:]
                v, i = self.mejor_insercion(pi, j)
                if v < val:
                    pi.insert(i, j)
                    seq, val = pi, v
                    mejora = True
        return seq, val

    def resolver(self, tiempo_max=TIEMPO_MAX_R1, semilla=SEMILLA_R1,
                 max_iter=MAX_ITER_R1, max_sin_mejora=MAX_SIN_MEJORA_R1, exacto=EXACTO_R1):
        """Devuelve (secuencia de indices, Cmax, info)."""
        t0 = time.perf_counter()
        limite = t0 + tiempo_max
        n = self.n
        if n == 0:
            return [], 0, {"lb": 0, "iteraciones": 0, "optimo_probado": True}
        rng = random.Random(semilla)
        lb = self.cota_inferior()

        # 1) soluciones iniciales (NEH + bloques) y busqueda local, empezando por
        #    la mejor. Con el exacto activo basta con la mejor (el exacto hace el
        #    resto); sin el, se aplica a todas. Se para si alguna llega a la cota.
        candidatos = [self.neh()] + self.por_bloques()
        valores = [self.evaluar(s) for s in candidatos]
        orden = sorted(range(len(candidatos)), key=valores.__getitem__)
        mejor, mejor_val = candidatos[orden[0]], valores[orden[0]]
        inicial = mejor_val
        for k in (orden[:1] if exacto else orden):
            if mejor_val <= lb:
                break
            s, v = self.busqueda_local(candidatos[k], valores[k], rng)
            if v < mejor_val:
                mejor, mejor_val = s, v
        heuristica = mejor_val
        probado = mejor_val <= lb

        # 2) metodo exacto: encuentra una secuencia mejor o demuestra que no existe
        if not probado and exacto and mejor_val < PENAL_R1:
            seq, val, completo = self.exacto(mejor_val, limite)
            if seq is not None:
                mejor, mejor_val = seq, val
            probado = completo

        # 3) Iterated Greedy: solo si no se demostro el optimo (exacto apagado o
        #    se llego a su tope de seguridad)
        actual, actual_val = mejor[:], mejor_val
        temp = T_ACEPTACION_R1 * (sum(self.P1) + sum(self.P2) + sum(self.P3)) / (n * 3 * 10)
        d = min(D_DESTRUCCION_R1, n - 1)
        it = sin_mejora = 0
        while (not probado and mejor_val > lb and it < max_iter and sin_mejora < max_sin_mejora
               and time.perf_counter() < limite):
            it += 1
            pi = actual[:]
            quitados = [pi.pop(rng.randrange(len(pi))) for _ in range(d)]
            val = None
            for j in quitados:
                val, i = self.mejor_insercion(pi, j)
                pi.insert(i, j)
            pi, val = self.busqueda_local(pi, val, rng)
            if val < actual_val:
                actual, actual_val = pi, val
                if val < mejor_val:
                    mejor, mejor_val = pi[:], val
                    sin_mejora = 0
                    continue
            elif rng.random() < math.exp(-(val - actual_val) / temp):
                actual, actual_val = pi, val
            sin_mejora += 1

        cmax = mejor_val % PENAL_R1 if mejor_val >= PENAL_R1 else mejor_val
        info = {"lb": lb, "inicial": inicial, "heuristica": heuristica, "iteraciones": it,
                "factible": mejor_val < PENAL_R1, "optimo_probado": probado or mejor_val <= lb}
        return mejor, cmax, info
# === FIN ALGORITMO ===


class Schedulling:
    def __init__(self, n_instancias: int = 30, semilla: int = 42):
        """
        Inicializa la clase con numero de instancias y semilla.
        No modificar esta funcion.
        """
        self.n_instancias = n_instancias
        self.semilla = semilla
        random.seed(semilla)
        np.random.seed(semilla)
        self.resultados = {"instancia": [], "valor_objetivo": [], "tiempo_seg": []}
        self.consolidado = None

    def generar_instancia(self, indice):
        """
        Genera una instancia aleatoria del problema de lotes y setups.
        Retorna un diccionario con los tiempos de procesamiento y tiempos de setup.
        """
        tipos = ["S", "N", "R"]
        lotes = [f"L{i}" for i in range(1, 16)]

        # Rangos de tiempos de procesamiento por maquina
        rangos = {
            "M1": (25, 45),
            "M2": (20, 40),
            "M3": (10, 25)
        }

        # --------------------------
        # Generar datos de los lotes
        # --------------------------
        lotes_dict = {}
        for lote in lotes:
            tipo = random.choice(tipos)
            lotes_dict[lote] = {
                "tipo": tipo,
                "M1": random.randint(*rangos["M1"]),
                "M2": random.randint(*rangos["M2"]),
                "M3": random.randint(*rangos["M3"])
            }

        # --------------------------
        # Generar tiempos de setup
        # --------------------------
        setup_dict = {}
        for maquina in ["M1", "M2", "M3"]:
            setup_dict[maquina] = {}
            for tipo_ant in tipos:
                for tipo_sig in tipos:
                    if tipo_ant == tipo_sig:
                        tiempo_setup = 0
                    else:
                        if maquina == "M1":
                            tiempo_setup = random.randint(10, 40)
                        elif maquina == "M2":
                            tiempo_setup = random.randint(5, 30)
                        else:  # M3
                            tiempo_setup = random.randint(3, 15)
                    setup_dict[maquina][f"{tipo_ant}-{tipo_sig}"] = tiempo_setup

        # --------------------------
        # Consolidar instancia
        # --------------------------
        instancia = {
            "lotes": lotes_dict,
            "setup": setup_dict
        }
        with open(f'instancia_{indice}.json', "w", encoding="utf-8") as f:
            json.dump(instancia, f, indent=4, ensure_ascii=False)

        return instancia

    def resolver_instancia(self, instancia: dict):
        inicio = time.time()
        modelo = WillyWonka(instancia)
        seq, cmax, _ = modelo.resolver()
        secuencia = [modelo.nombres[j] for j in seq]
        return {
            "secuencia": secuencia,
            "valor_objetivo": int(cmax),
            "Cmax": int(cmax),
            "tiempo": int((time.time() - inicio) * 1000),
        }

    def ejecutar_experimentos(self):
        """
        Genera y resuelve las instancias, mide tiempos de ejecucion
        y consolida los resultados.
        NO modificar esta funcion.
        """
        print(f"Ejecutando {self.n_instancias} instancias...\n")

        # Reinicia resultados
        self.resultados = {"instancia": [], "valor_objetivo": [], "tiempo_seg": []}

        inicio_total = time.time()

        for i in range(1, self.n_instancias + 1):
            instancia = self.generar_instancia(i)
            t0 = time.time()
            resultado = self.resolver_instancia(instancia)
            t1 = time.time()

            # Guarda resultados
            self.resultados["instancia"].append(i)
            self.resultados["valor_objetivo"].append(resultado["valor_objetivo"])
            self.resultados["tiempo_seg"].append(round(t1 - t0, 4))

            print(f"Instancia {i} optimizada en {round(t1 - t0, 4)} seg")

        # Tiempo total
        tiempo_total = time.time() - inicio_total

        # Crear DataFrame consolidado
        self.consolidado = pd.DataFrame(self.resultados)

        # Calcular promedios solo de tiempo
        promedio_tiempo = self.consolidado["tiempo_seg"].mean()

        print("\n==== REPORTE DE RENDIMIENTO ====")
        print("Tiempo promedio por instancia:", round(promedio_tiempo, 4), "seg")
        print("Tiempo total de ejecución:", round(tiempo_total, 2), "seg")

        return self.consolidado

    def calcular_makespan_penalizado(self , data={}, secuencia=[f'L{i}' for i in range(1,16)]):
        lotes = data["lotes"]
        setup = data["setup"]
        maquinas = ["M1", "M2", "M3"]

        # Validación: N no puede ir inmediatamente antes de R
        penalizado = False
        for i in range(1, len(secuencia)):
            tipo_anterior = lotes[secuencia[i-1]]["tipo"]
            tipo_actual = lotes[secuencia[i]]["tipo"]
            if tipo_anterior == "N" and tipo_actual == "R":
                penalizado = True
                break

        fin_maquina = {m: 0 for m in maquinas}
        fin_lote = {l: 0 for l in secuencia}

        for lote in secuencia:
            tipo_actual = lotes[lote]["tipo"]
            for m_idx, m in enumerate(maquinas):
                prev_tipo = None
                # Buscar el último tipo procesado en esta máquina
                if fin_maquina[m] > 0:
                    for l in secuencia:
                        if fin_lote[l] <= fin_maquina[m] and l != lote:
                            prev_tipo = lotes[l]["tipo"]

                t_setup = 0
                if prev_tipo is not None and prev_tipo != tipo_actual:
                    t_setup = setup[m][f"{prev_tipo}-{tipo_actual}"]

                if m_idx == 0:
                    inicio = fin_maquina[m] + t_setup
                else:
                    inicio = max(fin_maquina[m], fin_lote[lote]) + t_setup

                duracion = lotes[lote][m]
                fin = inicio + duracion

                fin_maquina[m] = fin
                fin_lote[lote] = fin

        makespan = max(fin_maquina.values())

        # Penalización si se violó la regla N → R
        if penalizado:
            makespan = float('inf')

        return makespan
# ----------------------------------------------------------
# Ejecución directa (GradeScope)
# ----------------------------------------------------------
if __name__ == "__main__":
    sch = Schedulling(30)
    df_resultados = sch.ejecutar_experimentos()
    print("\nConsolidado final:")
    print(df_resultados)
