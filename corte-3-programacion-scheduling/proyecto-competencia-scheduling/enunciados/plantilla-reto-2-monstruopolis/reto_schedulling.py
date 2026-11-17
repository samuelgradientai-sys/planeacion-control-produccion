

# Plantilla base para GradeScope
# este archivo debe llamarse reto_schedulling.py 
# Agregar dependencias si es necesario, pero sin remover las que ya se encuentran abajo
import random
import numpy as np
import time
import pandas as pd
import json

# === Dependencias para el modelo===
from itertools import product, combinations
from generador import GeneradorInstancias

class Schedulling(GeneradorInstancias):
    def __init__(self, n_instancias: int = 30, semilla: int = 42, timelimit: int = 30):
        # reutilizamos el __init__ del generador
        super().__init__(n_instancias=n_instancias, semilla=semilla, timelimit=timelimit)
        self.timelimit = timelimit  # por claridad

    def resolver_instancia(self, instancia: dict):
        """
        Heurística mejorada para:
            P3 | r_j, prec | Σ w_j T_j
        - Usa un simulador que respeta:
            * fechas de liberación r_j
            * precedencias preds[j]
            * m máquinas paralelas sin solape
        """
        import math
        import time
        import random

        # ===================== 1. Sets y parámetros =====================
        J = instancia["jobs"]
        m = instancia["m"]
        Mset = [f"M{i+1}" for i in range(m)]

        p = instancia["p"]      # p_j tiempos de proceso
        r = instancia["r"]      # r_j tiempos de liberación
        d = instancia["d"]      # d_j due dates
        w = instancia["w"]      # w_j indices de prioridad
        preds = instancia["preds"]  # lista de predecesores por j

        # Construir lista de sucesores (para actualizar precedencias rápido)
        succs = {j: [] for j in J}
        for j in J:
            for u in preds[j]:
                succs[u].append(j)

        # --------------------- constructor de calendario ---------------------
        def build_schedule():
            """
            Construye una programación completa
            """
            secuencia_local = []
            for j in J:
                sj = start_times.get(j, 0.0)
                cj = end_times.get(j, sj + p[j])
                mm = machine_of.get(j, Mset[0])
                secuencia_local.append({
                    "job": j,
                    "machine": mm,
                    "start": round(float(sj), 6),
                    "end": round(float(cj), 6),
                    "Cj": round(float(cj), 6)
                })


		# INSERTA AQUI TU CODIGO PARA OPTIMIZAR best_val y best_seq




        best_val = float("inf")
        best_seq = None

        max_time = self.timelimit - 1.0 if self.timelimit else 29.0

        while (time.perf_counter() - start_global) < max_time:

            sec, val = build_schedule()

            if val < best_val:
                best_val = val
                best_seq = secuencia_local


        return {
            "secuencia": best_seq,
            "valor_objetivo": round(float(best_val), 4)
        }