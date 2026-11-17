"""
Version LOCAL del modulo `generador` que importa la plantilla del Reto 2
(`from generador import GeneradorInstancias`). El real esta en Gradescope y no
lo tenemos: este lo imita segun el enunciado para poder probar. NO SE SUBE.

Instancia (mismas claves que usa la plantilla):
    {"jobs": ["J1", ...], "m": 3, "p": {j: pj}, "r": {j: rj}, "d": {j: dj},
     "w": {j: wj}, "preds": {j: [predecesores]}}
  * p_j entre 10 y 100, r_j entre 0 y 30, w_j entre 1 y 5
  * ~10 % de los trabajos con precedencia (unas 5 parejas i -> j con i < j: sin ciclos)
  * d_j = tiempo minimo teorico de finalizacion = max(r_j, d de sus predecesores) + p_j
    (con holgura > 0 se le suma un margen aleatorio, para probar fechas mas sueltas)
"""
import random
import time

import numpy as np


def generar(rng, n=50, m=3, n_prec=5, holgura=0.0):
    jobs = [f"J{i}" for i in range(1, n + 1)]
    p = {j: rng.randint(10, 100) for j in jobs}
    r = {j: rng.randint(0, 30) for j in jobs}
    w = {j: rng.randint(1, 5) for j in jobs}
    preds = {j: [] for j in jobs}
    parejas = set()
    while len(parejas) < n_prec:
        a, b = sorted(rng.sample(range(n), 2))
        parejas.add((a, b))
    for a, b in sorted(parejas):
        preds[jobs[b]].append(jobs[a])
    # tiempo minimo teorico de finalizacion (CPM hacia adelante; i < j, sin ciclos)
    emin = {}
    for j in jobs:
        emin[j] = max([r[j]] + [emin[i] for i in preds[j]]) + p[j]
    carga = sum(p.values()) / m
    d = {j: emin[j] + (int(rng.uniform(0, holgura) * carga) if holgura > 0 else 0) for j in jobs}
    return {"jobs": jobs, "m": m, "p": p, "r": r, "d": d, "w": w, "preds": preds}


class GeneradorInstancias:
    def __init__(self, n_instancias: int = 30, semilla: int = 42, timelimit: int = 30, holgura=0.0):
        self.n_instancias = n_instancias
        self.semilla = semilla
        self.timelimit = timelimit
        self.holgura = holgura
        random.seed(semilla)
        np.random.seed(semilla)
        self._rng = random.Random(semilla)
        self.resultados = {"instancia": [], "valor_objetivo": [], "tiempo_seg": []}

    def generar_instancia(self, indice):
        return generar(self._rng, holgura=self.holgura)

    def resolver_instancia(self, instancia):
        raise NotImplementedError

    def ejecutar_experimentos(self):
        import pandas as pd
        print(f"Ejecutando {self.n_instancias} instancias...\n")
        inicio = time.time()
        for i in range(1, self.n_instancias + 1):
            inst = self.generar_instancia(i)
            t0 = time.time()
            res = self.resolver_instancia(inst)
            t1 = time.time()
            self.resultados["instancia"].append(i)
            self.resultados["valor_objetivo"].append(res["valor_objetivo"])
            self.resultados["tiempo_seg"].append(round(t1 - t0, 4))
            print(f"Instancia {i}: sum wjTj = {res['valor_objetivo']}  ({round(t1 - t0, 4)} s)")
        df = pd.DataFrame(self.resultados)
        print("\nTiempo promedio:", round(df["tiempo_seg"].mean(), 4), "s",
              "| total:", round(time.time() - inicio, 2), "s")
        return df
