"""
Metodo exacto para verificar el RETO 01: programacion dinamica por capas con
frentes de Pareto y poda por cota. Solo para pruebas (no se sube).

Estado: (lotes ya programados, tipo del ultimo lote). Para cada estado se
guardan los vectores (fin M1, fin M2, fin M3) no dominados. Un estado se poda
si su cota inferior ya no puede mejorar la mejor solucion conocida (UB).
Si nada sobrevive, la UB es optima.
"""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))

import reto1  # noqa: E402


def optimo_exacto(data, ub, limite_estados=3_000_000):
    """Devuelve (Cmax optimo, estados explorados). Busca algo estrictamente menor que ub."""
    m = reto1.WillyWonka(data)
    n = m.n
    tipos = sorted(set(m.tipo))
    k = len(tipos)
    ti = [tipos.index(t) for t in m.tipo]
    ini = k                                   # tipo virtual "sin anterior"
    prohibido = [[tipos[a] == "N" and tipos[b] == "R" for b in range(k)] for a in range(k)] + [[False] * k]
    ST = []
    for maq in reto1.MAQUINAS_R1:
        ST.append([[m.st[maq, tipos[a], tipos[b]] for b in range(k)] for a in range(k)] + [[0] * k])
    P1, P2, P3 = m.P1, m.P2, m.P3
    INF = float("inf")

    # W[maq][inicio][conjunto de tipos] = recorrido minimo que cubre el conjunto
    def recorridos(s):
        W = [[INF] * (1 << k) for _ in range(k + 1)]
        for a in range(k + 1):
            dist = {}
            base = 0 if a == ini else (1 << a)
            dist[(base, a)] = 0
            cambio = True
            while cambio:
                cambio = False
                for (mask, u), du in list(dist.items()):
                    for b in range(k):
                        if b == u or prohibido[u][b]:
                            continue
                        clave = (mask | (1 << b), b)
                        nd = du + s[u][b]
                        if nd < dist.get(clave, INF):
                            dist[clave] = nd
                            cambio = True
            for (mask, u), du in dist.items():
                for sub in range(1 << k):
                    if sub & ~mask == 0 and du < W[a][sub]:
                        W[a][sub] = du
        return W

    W1, W2, W3 = (recorridos(s) for s in ST)

    cache = {}

    def datos_resto(mask):
        r = cache.get(mask)
        if r is None:
            resto = [j for j in range(n) if not mask >> j & 1]
            tmask = 0
            for j in resto:
                tmask |= 1 << ti[j]
            r = (resto, tmask, sum(P1[j] for j in resto), sum(P2[j] for j in resto),
                 sum(P3[j] for j in resto), min(P2[j] + P3[j] for j in resto),
                 min(P1[j] for j in resto), min(P3[j] for j in resto),
                 min(P1[j] + P2[j] for j in resto), min(P2[j] for j in resto))
            cache[mask] = r
        return r

    capa = {(0, ini): [(0, 0, 0)]}
    explorados = 0
    for _ in range(n):
        nueva = {}
        for (mask, lt), frente in capa.items():
            resto = datos_resto(mask)[0]
            for j in resto:
                tj = ti[j]
                if lt != ini and prohibido[lt][tj]:
                    continue
                nmask = mask | (1 << j)
                s1, s2, s3 = ST[0][lt][tj], ST[1][lt][tj], ST[2][lt][tj]
                ultimo = nmask == (1 << n) - 1
                if not ultimo:
                    _, tm, sp1, sp2, sp3, m23, mp1, mp3, m12, mp2 = datos_resto(nmask)
                for c1, c2, c3 in frente:
                    n1 = c1 + s1 + P1[j]
                    n2 = (c2 if c2 > n1 else n1) + s2 + P2[j]
                    n3 = (c3 if c3 > n2 else n2) + s3 + P3[j]
                    if ultimo:
                        cota = n3
                    else:
                        cota = max(n1 + sp1 + W1[tj][tm] + m23,
                                   max(n2, n1 + mp1) + sp2 + W2[tj][tm] + mp3,
                                   max(n3, n2 + mp2, n1 + m12) + sp3 + W3[tj][tm])
                    if cota >= ub:
                        continue
                    explorados += 1
                    clave = (nmask, tj)
                    lst = nueva.get(clave)
                    if lst is None:
                        nueva[clave] = [(n1, n2, n3)]
                        continue
                    dominado = False
                    for e in lst:
                        if e[0] <= n1 and e[1] <= n2 and e[2] <= n3:
                            dominado = True
                            break
                    if not dominado:
                        lst[:] = [e for e in lst if not (n1 <= e[0] and n2 <= e[1] and n3 <= e[2])]
                        lst.append((n1, n2, n3))
            if explorados > limite_estados:
                return None, explorados
        capa = nueva
        if not capa:
            return ub, explorados            # nada mejora la UB: es optima
    mejor = min(f[2] for frente in capa.values() for f in frente)
    return mejor, explorados


if __name__ == "__main__":
    import random
    import time
    from probar_reto1 import generar_instancia_plantilla

    random.seed(42)
    instancias = [generar_instancia_plantilla() for _ in range(30)]
    tot = 0
    for i, data in enumerate(instancias, 1):
        res = reto1.solve(data)
        t0 = time.perf_counter()
        opt, est = optimo_exacto(data, res["Cmax"])
        dt = time.perf_counter() - t0
        marca = "" if opt == res["Cmax"] else f"  <-- optimo {opt}, heuristica {res['Cmax']}"
        tot += opt == res["Cmax"]
        print(f"inst {i:>2}: heuristica {res['Cmax']:>4}  exacto {opt}  estados {est:>8}  {dt*1000:8.1f} ms{marca}")
    print(f"\nheuristica optima en {tot}/30 instancias")
