"""
Cota inferior fuerte para el RETO 02 (solo para medir que tan cerca del optimo
estamos; no se sube). Usa numpy.

Formulacion indexada en el tiempo: cada trabajo j escoge un inicio s >= e_j
(e_j = inicio mas temprano por r_j y precedencias) y paga w_j * max(0, s + p_j - d_j).
La restriccion "a lo sumo m trabajos a la vez" se relaja con multiplicadores
lambda_t >= 0 (relajacion lagrangiana):

    L(lambda) = sum_j min_s [ w_j T_j(s) + sum_{t=s}^{s+p_j-1} lambda_t ] - m * sum_t lambda_t

Para cualquier lambda >= 0, L(lambda) <= optimo. Se busca el mejor lambda con
subgradiente (paso de Polyak). Se ignoran las precedencias entre trabajos salvo
el inicio mas temprano, asi que es una cota valida.

    python pruebas/cota_reto2.py          -> brecha de reto2.py contra la cota en 30 instancias
"""
import os
import random
import sys

import numpy as np

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))
sys.path.insert(0, AQUI)


def cota_lagrangiana(inst, ub, iteraciones=800):
    jobs, m = inst["jobs"], inst["m"]
    p = np.array([inst["p"][j] for j in jobs])
    w = np.array([inst["w"][j] for j in jobs], dtype=float)
    d = np.array([inst["d"][j] for j in jobs])
    # inicio mas temprano por liberacion y precedencias (CPM)
    e = {}
    for j in jobs:                                   # los predecesores van antes en la lista
        e[j] = max([inst["r"][j]] + [e[i] + inst["p"][i] for i in inst["preds"][j]])
    pend = [j for j in jobs if any(i not in e for i in inst["preds"][j])]
    assert not pend
    e = np.array([e[j] for j in jobs])
    n = len(jobs)
    T = int(e.max() + p.sum())                       # horizonte seguro
    S = np.arange(T)
    fin = S[None, :] + p[:, None]                    # n x T
    valido = (S[None, :] >= e[:, None]) & (fin <= T)
    tard = w[:, None] * np.maximum(0, fin - d[:, None])
    fin_c = np.minimum(fin, T)
    lam = np.zeros(T)
    mejor = 0.0
    mu = 2.0
    sin_mejora = 0
    filas = np.arange(n)
    for _ in range(iteraciones):
        Lc = np.concatenate(([0.0], np.cumsum(lam)))   # Lc[t] = sum lam[0..t-1]
        costo = tard + Lc[fin_c] - Lc[S][None, :]
        costo[~valido] = np.inf
        s = costo.argmin(axis=1)
        valor = costo[filas, s].sum() - m * lam.sum()
        if valor > mejor + 1e-9:
            mejor, sin_mejora = valor, 0
        else:
            sin_mejora += 1
            if sin_mejora >= 25:
                mu, sin_mejora = mu / 2, 0
                if mu < 1e-4:
                    break
        uso = np.zeros(T + 1)
        np.add.at(uso, s, 1)
        np.add.at(uso, s + p, -1)
        g = np.cumsum(uso)[:T] - m
        norma = float((g * g).sum())
        if norma == 0:
            break
        lam = np.maximum(0.0, lam + mu * (ub - valor) / norma * g)
    return mejor


if __name__ == "__main__":
    import time
    import statistics
    import reto2
    from generador import generar
    holgura = float(sys.argv[1]) if len(sys.argv) > 1 else 0.0
    rng = random.Random(42)
    instancias = [generar(rng, holgura=holgura) for _ in range(30)]
    brechas = []
    for k, inst in enumerate(instancias, 1):
        ub = reto2.tardanza_ponderada(inst, reto2.solve(inst))
        t0 = time.perf_counter()
        lb = cota_lagrangiana(inst, ub)
        brechas.append(100 * (ub - lb) / ub)
        print(f"inst {k:>2}: nuestra {ub:>7}  cota {lb:9.1f}  brecha <= {brechas[-1]:.2f}%  ({time.perf_counter() - t0:.1f} s)")
    print(f"\nbrecha promedio contra la cota: {statistics.mean(brechas):.2f}%  (max {max(brechas):.2f}%)")
