"""
RETO 02 - Fabrica de juguetes de Monstruopolis
==============================================
P3 | r_j, prec | sum w_j T_j : 3 maquinas identicas en paralelo, fechas de
liberacion, precedencias (i -> j: j empieza cuando i termino), sin interrupciones.
Objetivo: minimizar la tardanza ponderada total.

Representacion
--------------
Una lista de prioridad: permutacion de los trabajos en la que cada predecesor
aparece antes que sus sucesores. El decodificador programa los trabajos en el
orden de la lista, cada uno lo antes posible:
    listo_j = max(r_j, fin de sus predecesores)
    maquina = la que permite empezar antes; si varias permiten empezar en
              listo_j se usa la que quedo libre mas tarde ("best fit"), asi las
              que quedaron libres antes siguen disponibles para otros trabajos.
Cualquier lista asi da un programa factible (respeta r_j, precedencias y no
hay solapes), por eso la busqueda nunca produce soluciones infactibles.

Algoritmo
---------
1. Reglas de despacho: WSPT (w/p), ATC con varios K, razon de cadenas (para que
   un predecesor "herede" la prioridad de su sucesor) y EDD. Se queda la mejor.
2. Recocido simulado sobre la lista con movimientos de insercion e intercambio
   en una ventana. Para que cada vecino sea barato de evaluar:
   - se re-decodifica solo desde la primera posicion que cambio (se guardan
     "fotos" del estado de las maquinas en cada posicion);
   - se corta apenas el costo supera el umbral de aceptacion (el numero
     aleatorio de Metropolis se sortea ANTES de evaluar);
   - si despues del tramo modificado las maquinas quedan igual que en la
     solucion base, el resto del programa es identico y no se recalcula.
"""
import heapq
import json
import math
import random
import re
import sys
import time
from bisect import bisect_right, insort

# === INICIO ALGORITMO ===
# ---------------------------------------------------------------- parametros
# Calibrados con 30 instancias contra corridas largas (3 x 500 000 iteraciones):
#   d_j ajustado (enunciado): 10 000 iter -> brecha ~0,05 % en ~0,09 s
#                             20 000 iter -> ~0,04 % en ~0,18 s
#                             0 iter (solo reglas de despacho) -> ~2,9 % en ~2 ms
#   d_j holgado (prueba de robustez): 10 000 iter -> ~1,8 %; 20 000 -> ~0,7 %
TIEMPO_MAX_R2 = 5.0       # tope de seguridad (segundos) por instancia
ITER_SA_R2 = 10000        # iteraciones del recocido simulado
VENTANA_R2 = 20           # distancia maxima de un movimiento en la lista
T_INI_R2 = 0.6            # temperatura inicial  (x peso medio x p medio)
T_FIN_R2 = 0.001          # temperatura final    (x peso medio x p medio)
SEMILLA_R2 = 2026         # semilla propia: no altera el random global


# ------------------------------------------------------- lectura de datos
_ALIAS = {
    "id": ("job", "trabajo", "id", "j", "nombre", "name"),
    "p": ("p_j", "p", "pj", "proc", "procesamiento", "tiempo_procesamiento"),
    "r": ("r_j", "r", "rj", "release", "liberacion"),
    "d": ("d_j", "d", "dj", "due", "entrega", "fecha_entrega"),
    "w": ("w_j", "w", "wj", "peso", "prioridad", "weight"),
    "pred": ("predecesores", "preds", "pred", "predecessors", "precedencias"),
}


def _campo(fila, clave):
    bajas = {str(k).strip().lower(): v for k, v in fila.items()}
    for alias in _ALIAS[clave]:
        if alias in bajas:
            return bajas[alias]
    return None


def _numero(x):
    if isinstance(x, (int, float)):
        return x
    v = float(str(x).strip())
    return int(v) if v.is_integer() else v


def _lista(x):
    """Predecesores como lista: acepta lista, None, '', '-', 'J1, J3', '[J1;J3]'."""
    if x is None or (isinstance(x, float) and x != x):
        return []
    if isinstance(x, (list, tuple, set)):
        return list(x)
    s = str(x).strip().strip("[]")
    if s.lower() in ("", "-", "none", "nan", "ninguno", "null"):
        return []
    return [t.strip().strip("'\"") for t in re.split(r"[,;\s]+", s) if t.strip().strip("'\"")]


def cargar_instancia(data):
    """Convierte la entrada (varios formatos posibles) a listas internas.

    Formatos aceptados:
      * plantilla Gradescope: {"jobs": [...], "m": 3, "p": {j: pj}, "r": {...},
        "d": {...}, "w": {...}, "preds": {j: [i, ...]}}
      * lista de filas: [{"Trabajo": "J1", "p_j": 45, "r_j": 3, "d_j": 60,
        "w_j": 2, "Predecesores": ["J3"]}, ...]  (o {"jobs"/"trabajos": [filas]})
    """
    m = 3
    filas = None
    if isinstance(data, list):
        filas = data
    else:
        if "m" in data:
            m = int(data["m"])
        for k in ("jobs", "trabajos", "Trabajos", "instancia", "data"):
            v = data.get(k)
            if isinstance(v, list) and v and isinstance(v[0], dict):
                filas = v
                break

    if filas is not None:
        ids = [_campo(f, "id") for f in filas]
        if any(i is None for i in ids):
            ids = [f"J{k + 1}" for k in range(len(filas))]
        p = [_numero(_campo(f, "p")) for f in filas]
        r = [_numero(_campo(f, "r") or 0) for f in filas]
        d = [_numero(_campo(f, "d")) for f in filas]
        w = [_numero(_campo(f, "w") if _campo(f, "w") is not None else 1) for f in filas]
        preds_raw = [_lista(_campo(f, "pred")) for f in filas]
    else:
        ids = list(data["jobs"]) if "jobs" in data else list(data["p"])

        def valor(campo, k, j, defecto=None):
            v = data.get(campo, defecto)
            if isinstance(v, dict):
                v = v.get(j, v.get(str(j), defecto))
            elif isinstance(v, list):
                v = v[k]
            return defecto if v is None else _numero(v)

        p = [valor("p", k, j) for k, j in enumerate(ids)]
        r = [valor("r", k, j, 0) for k, j in enumerate(ids)]
        d = [valor("d", k, j) for k, j in enumerate(ids)]
        w = [valor("w", k, j, 1) for k, j in enumerate(ids)]
        pr = data.get("preds", data.get("predecesores", {}))
        if isinstance(pr, dict):
            preds_raw = [_lista(pr.get(j, pr.get(str(j)))) for j in ids]
        elif isinstance(pr, list) and len(pr) == len(ids) and all(
                isinstance(x, (list, tuple)) or x is None for x in pr):
            preds_raw = [_lista(x) for x in pr]
        else:
            preds_raw = [[] for _ in ids]
        # precedencias como lista de parejas [i, j]
        for par in data.get("precedencias", data.get("prec", [])) or []:
            if isinstance(par, dict):
                par = (par.get("i", par.get("pred")), par.get("j", par.get("succ")))
            i_, j_ = par
            preds_raw[[str(x) for x in ids].index(str(j_))].append(i_)

    # nombres de predecesores -> indices (tolera "J3", 3 o "3")
    indice = {}
    for k, j in enumerate(ids):
        indice[str(j)] = k
        num = re.sub(r"\D", "", str(j))
        if num:
            indice.setdefault(num, k)
    preds = []
    for k, lst in enumerate(preds_raw):
        idx = []
        for x in lst:
            s = str(x).strip()
            pos = indice.get(s, indice.get(re.sub(r"\D", "", s)))
            if pos is not None and pos != k and pos not in idx:
                idx.append(pos)
        preds.append(tuple(idx))
    if d and any(v is None for v in d):
        raise ValueError("faltan fechas de entrega d_j")
    return ids, p, r, d, w, preds, m


class Monstruopolis:
    """Datos de una instancia y los procedimientos del algoritmo."""

    def __init__(self, ids, p, r, d, w, preds, m=3):
        self.ids, self.p, self.r, self.d, self.w = ids, p, r, d, w
        self.preds = preds
        self.m = m
        n = self.n = len(ids)
        succs = [[] for _ in range(n)]
        for j in range(n):
            for i in preds[j]:
                succs[i].append(j)
        self.succs = [tuple(s) for s in succs]
        self.con_suc = [bool(s) for s in succs]
        # datos de cada trabajo en una tupla: se leen de una vez en el decodificador
        self.datos = [(r[j], p[j], d[j], w[j], preds[j], self.con_suc[j]) for j in range(n)]

    # ------------------------------------------------------------ decodificador
    def decodificar(self, L):
        """Programa completo de la lista L. Devuelve (costo, C, f_av, f_costo):
        f_av[k] = tiempos en que quedan libres las maquinas (ordenados) y
        f_costo[k] = costo acumulado, ANTES de programar L[k] ("fotos")."""
        n = self.n
        f_av = [None] * (n + 1)
        f_costo = [0] * (n + 1)
        f_av[0] = (0,) * self.m
        costo, C, _ = self.evaluar_desde(L, 0, n, float("inf"), [0] * n, f_av, f_costo, f_av, f_costo)
        return costo, C, f_av, f_costo

    def evaluar_desde(self, L, lo, hi, umbral, C_base, f_av, f_costo, tmp_av, tmp_costo):
        """Re-decodifica L desde la posicion lo partiendo de las fotos del
        programa base (f_av[lo], f_costo[lo]); L solo cambio entre lo y hi.

        - Si el costo supera el umbral corta y devuelve None (vecino rechazado).
        - Convergencia: pasada la posicion hi, si las maquinas quedan igual que
          en el programa base, el resto del programa es identico y su costo se
          toma de f_costo sin recalcularlo.
        Devuelve (costo, C, k) con k = posicion hasta la que se recalculo."""
        if self.m != 3:
            return self._evaluar_general(L, lo, hi, umbral, C_base, f_av, f_costo, tmp_av, tmp_costo)
        datos = self.datos
        n = self.n
        a0, a1, a2 = f_av[lo]          # maquinas libres en a0 <= a1 <= a2
        costo = f_costo[lo]
        C = C_base[:]
        sucio = False                  # algun predecesor termino distinto que en la base
        k1 = lo                        # k1 = posicion del trabajo + 1
        for j in L[lo:]:
            k1 += 1
            t, pj, dj, wj, pr, cs = datos[j]
            for i in pr:
                if C[i] > t:
                    t = C[i]
            # best fit: la maquina libre mas tarde que no haga esperar a j
            if t >= a2:
                c = t + pj
                a2 = c
            elif t >= a1:
                c = t + pj
                if c <= a2:
                    a1 = c
                else:
                    a1, a2 = a2, c
            else:
                if t < a0:
                    t = a0
                c = t + pj
                if c <= a1:
                    a0 = c
                elif c <= a2:
                    a0, a1 = a1, c
                else:
                    a0, a1, a2 = a1, a2, c
            if cs and c != C_base[j]:
                sucio = True
            C[j] = c
            if c > dj:
                costo += wj * (c - dj)
                if costo > umbral:
                    return None
            est = (a0, a1, a2)
            tmp_av[k1] = est
            tmp_costo[k1] = costo
            if k1 > hi and not sucio and est == f_av[k1]:
                costo += f_costo[n] - f_costo[k1]
                return (costo, C, k1) if costo <= umbral else None
        return costo, C, n

    def _evaluar_general(self, L, lo, hi, umbral, C_base, f_av, f_costo, tmp_av, tmp_costo):
        """Igual que evaluar_desde pero para cualquier numero de maquinas."""
        p, r, d, w, preds, con_suc = self.p, self.r, self.d, self.w, self.preds, self.con_suc
        n = self.n
        av = list(f_av[lo])
        costo = f_costo[lo]
        C = C_base[:]
        sucio = False
        for k in range(lo, n):
            j = L[k]
            t = r[j]
            for i in preds[j]:
                if C[i] > t:
                    t = C[i]
            idx = bisect_right(av, t) - 1
            if idx < 0:
                idx = 0
                t = av[0]
            c = t + p[j]
            del av[idx]
            insort(av, c)
            if con_suc[j] and c != C_base[j]:
                sucio = True
            C[j] = c
            c -= d[j]
            if c > 0:
                costo += w[j] * c
                if costo > umbral:
                    return None
            est = tuple(av)
            tmp_av[k + 1] = est
            tmp_costo[k + 1] = costo
            if k >= hi and not sucio and est == f_av[k + 1]:
                costo += f_costo[n] - f_costo[k + 1]
                return (costo, C, k + 1) if costo <= umbral else None
        return costo, C, n

    def aceptar(self, f_av, f_costo, tmp_av, tmp_costo, lo, kc):
        """Actualiza las fotos del programa base con las del vecino aceptado."""
        if kc < self.n:
            delta = tmp_costo[kc] - f_costo[kc]
            if delta:
                for q in range(kc + 1, self.n + 1):
                    f_costo[q] += delta
        f_av[lo + 1:kc + 1] = tmp_av[lo + 1:kc + 1]
        f_costo[lo + 1:kc + 1] = tmp_costo[lo + 1:kc + 1]

    def programa(self, L):
        """Programa con nombre de maquina: lista de (j, maquina, inicio, fin)."""
        p, r, preds = self.p, self.r, self.preds
        libre = [0] * self.m
        C = [0] * self.n
        salida = []
        for j in L:
            t = r[j]
            for i in preds[j]:
                if C[i] > t:
                    t = C[i]
            aptas = [k for k in range(self.m) if libre[k] <= t]
            if aptas:   # best fit: la que quedo libre mas tarde sin pasarse de t
                k = max(aptas, key=lambda q: (libre[q], -q))
            else:
                k = min(range(self.m), key=lambda q: (libre[q], q))
                t = libre[k]
            C[j] = t + p[j]
            libre[k] = C[j]
            salida.append((j, k, t, C[j]))
        return salida

    # --------------------------------------------------------- reglas iniciales
    def lista_topologica(self, clave):
        """Ordena por clave (menor primero) respetando precedencias (Kahn)."""
        n = self.n
        faltan = [len(self.preds[j]) for j in range(n)]
        heap = [(clave[j], j) for j in range(n) if faltan[j] == 0]
        heapq.heapify(heap)
        L = []
        while heap:
            _, j = heapq.heappop(heap)
            L.append(j)
            for s in self.succs[j]:
                faltan[s] -= 1
                if faltan[s] == 0:
                    heapq.heappush(heap, (clave[s], s))
        if len(L) < n:   # ciclo en precedencias (no deberia pasar)
            vistos = set(L)
            L += [j for j in sorted(range(n), key=clave.__getitem__) if j not in vistos]
        return L

    def razon_cadena(self):
        """rho_j = max(w/p) de las cadenas que salen de j (estilo Sidney):
        un predecesor de un trabajo urgente sube su prioridad."""
        n, p, w = self.n, self.p, self.w
        orden = self.lista_topologica(list(range(n)))
        mejor = [(w[j], p[j]) for j in range(n)]
        for j in reversed(orden):
            for s in self.succs[j]:
                ws, ps = mejor[s]
                cand = (w[j] + ws, p[j] + ps)
                if cand[0] * mejor[j][1] > mejor[j][0] * cand[1]:
                    mejor[j] = cand
        return [a / b for a, b in mejor]

    def despacho(self, indice):
        """Despacho dinamico: cuando se libera una maquina elige, entre los
        trabajos listos, el de mayor indice(j, t, p_medio)."""
        n, m = self.n, self.m
        p, r, preds = self.p, self.r, self.preds
        faltan = [len(preds[j]) for j in range(n)]
        listo = list(r)
        disponibles = {j for j in range(n) if faltan[j] == 0}
        av = [0] * m
        resto_p = sum(p)
        L = []
        while disponibles:
            t = av[0]
            cand = [j for j in disponibles if listo[j] <= t]
            if not cand:
                t = min(listo[j] for j in disponibles)
                cand = [j for j in disponibles if listo[j] <= t]
            pm = resto_p / (n - len(L))
            j = max(cand, key=lambda q: (indice(q, t, pm), -q))
            s = listo[j]
            idx = bisect_right(av, s) - 1
            if idx < 0:
                idx = 0
                s = av[0]
            c = s + p[j]
            del av[idx]
            insort(av, c)
            L.append(j)
            disponibles.discard(j)
            resto_p -= p[j]
            for q in self.succs[j]:
                if c > listo[q]:
                    listo[q] = c
                faltan[q] -= 1
                if faltan[q] == 0:
                    disponibles.add(q)
        return L

    def listas_iniciales(self):
        p, d, w = self.p, self.d, self.w
        listas = [
            self.lista_topologica([-w[j] / p[j] for j in range(self.n)]),     # WSPT
            self.lista_topologica([-x for x in self.razon_cadena()]),        # cadenas
            self.lista_topologica([d[j] for j in range(self.n)]),            # EDD
            self.despacho(lambda j, t, pm: w[j] / p[j]),                      # WSPT dinamico
        ]
        for K in (0.5, 1.0, 2.0, 4.0):                                       # ATC
            listas.append(self.despacho(
                lambda j, t, pm, K=K: w[j] / p[j] * math.exp(-max(d[j] - p[j] - t, 0) / (K * pm))))
        return listas

    # ------------------------------------------------------------- busqueda
    def recocido(self, L, rng, iteraciones, limite):
        """Recocido simulado sobre la lista. Devuelve (mejor lista, mejor costo)."""
        n = self.n
        preds, succs = self.preds, self.succs
        pos = [0] * n
        for k, j in enumerate(L):
            pos[j] = k
        costo, C, f_av, f_costo = self.decodificar(L)
        mejor, mejor_costo = L[:], costo
        if costo == 0 or iteraciones <= 0 or n < 2:
            return mejor, mejor_costo
        tmp_av = f_av[:]
        tmp_costo = f_costo[:]
        escala = (sum(self.w) / n) * (sum(self.p) / n)
        T = T_INI_R2 * escala
        factor = (T_FIN_R2 / T_INI_R2) ** (1.0 / iteraciones)
        W = VENTANA_R2
        ancho = 2 * W + 1
        log = math.log
        azar = rng.random            # random() es mucho mas rapido que randint()
        for it in range(iteraciones):
            if (it & 511) == 0 and time.perf_counter() > limite:
                break
            T *= factor
            a = int(azar() * n)
            b = a + int(azar() * ancho) - W
            if b < 0 or b >= n or b == a:
                continue
            x = L[a]
            if azar() < 0.5:
                # insercion: x pasa de la posicion a a la b
                if b < a:
                    if preds[x] and any(pos[i] >= b for i in preds[x]):
                        continue
                    lo, hi = b, a
                else:
                    if succs[x] and any(pos[s] <= b for s in succs[x]):
                        continue
                    lo, hi = a, b
                nueva = L[:]
                del nueva[a]
                nueva.insert(b, x)
            else:
                # intercambio de las posiciones lo y hi
                lo, hi = (a, b) if a < b else (b, a)
                y1, y2 = L[lo], L[hi]
                if ((succs[y1] and any(pos[s] <= hi for s in succs[y1]))
                        or (preds[y2] and any(pos[i] >= lo for i in preds[y2]))):
                    continue
                nueva = L[:]
                nueva[lo], nueva[hi] = y2, y1
            u = azar()
            umbral = costo - T * log(u) if u > 0.0 else float("inf")
            res = self.evaluar_desde(nueva, lo, hi, umbral, C, f_av, f_costo, tmp_av, tmp_costo)
            if res is None:
                continue
            costo, C, kc = res
            L = nueva
            self.aceptar(f_av, f_costo, tmp_av, tmp_costo, lo, kc)
            for k in range(lo, hi + 1):
                pos[L[k]] = k
            if costo < mejor_costo:
                mejor, mejor_costo = L[:], costo
                if costo == 0:
                    break
        return mejor, mejor_costo

    def resolver(self, tiempo_max=TIEMPO_MAX_R2, semilla=SEMILLA_R2, iteraciones=ITER_SA_R2):
        """Devuelve (lista, costo, info)."""
        t0 = time.perf_counter()
        limite = t0 + tiempo_max
        rng = random.Random(semilla)
        listas = self.listas_iniciales()
        costos = [self.decodificar(L)[0] for L in listas]
        k = min(range(len(listas)), key=costos.__getitem__)
        L, costo = listas[k], costos[k]
        info = {"inicial": costo, "regla": k}
        L, costo = self.recocido(L, rng, iteraciones, limite)
        info["tiempo"] = time.perf_counter() - t0
        return L, costo, info
# === FIN ALGORITMO ===


def solve(data):
    """
    Parametro: data - diccionario (o lista) cargado desde data.json
    Retorna: lista con un diccionario por trabajo
             [{"job": "J1", "machine": "M1", "start": 0, "end": 45}, ...]
    """
    ids, p, r, d, w, preds, m = cargar_instancia(data)
    modelo = Monstruopolis(ids, p, r, d, w, preds, m)
    L, _, _ = modelo.resolver()
    filas = {j: (k, s, c) for j, k, s, c in modelo.programa(L)}
    return [{"job": ids[j], "machine": f"M{filas[j][0] + 1}",
             "start": filas[j][1], "end": filas[j][2]} for j in range(len(ids))]


def tardanza_ponderada(data, salida):
    """sum w_j * max(0, C_j - d_j) de una salida de solve()."""
    ids, p, r, d, w, preds, m = cargar_instancia(data)
    fin = {str(f["job"]): f["end"] for f in salida}
    return sum(w[k] * max(0, fin[str(j)] - d[k]) for k, j in enumerate(ids))


if __name__ == "__main__":
    ruta = sys.argv[1] if len(sys.argv) > 1 else "data.json"
    with open(ruta, encoding="utf-8") as f:
        data = json.load(f)
    t0 = time.time()
    salida = solve(data)
    print(json.dumps(salida, indent=2))
    print(f"// sum wjTj = {tardanza_ponderada(data, salida)}  |  "
          f"tiempo = {int((time.time() - t0) * 1000)} ms", file=sys.stderr)
