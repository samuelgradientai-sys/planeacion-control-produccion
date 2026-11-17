"""
Banco de pruebas local del RETO 02 (Monstruopolis). No se sube a Gradescope.

Uso (desde la carpeta PROYECTO ALGORITMO):
    python pruebas/probar_reto2.py                 -> 30 instancias (semilla 42)
    python pruebas/probar_reto2.py --referencia    -> ademas una corrida larga para medir la brecha
    python pruebas/probar_reto2.py --holgura 0.5   -> fechas de entrega mas sueltas

Que revisa (con un validador independiente del algoritmo):
  * una entrada por trabajo, maquina valida, end = start + p_j;
  * start >= r_j, predecesores terminados antes de empezar, sin solapes por maquina;
  * recalcula sum w_j T_j.
"""
import argparse
import os
import random
import statistics
import sys
import time

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(AQUI))
sys.path.insert(0, AQUI)

import reto2  # noqa: E402
from generador import generar  # noqa: E402


def validar(inst, salida):
    """Devuelve (sum wjTj, lista de violaciones)."""
    errores = []
    jobs = inst["jobs"]
    maquinas = {f"M{k + 1}" for k in range(inst["m"])}
    por_job = {}
    for f in salida:
        if f["job"] in por_job:
            errores.append(f"{f['job']} repetido")
        por_job[f["job"]] = f
    for j in jobs:
        if j not in por_job:
            errores.append(f"{j} falta")
            continue
        f = por_job[j]
        if f["machine"] not in maquinas:
            errores.append(f"{j} maquina {f['machine']}")
        if f["end"] - f["start"] != inst["p"][j]:
            errores.append(f"{j} duracion")
        if f["start"] < inst["r"][j]:
            errores.append(f"{j} empieza antes de r_j")
        for i in inst["preds"][j]:
            if por_job[i]["end"] > f["start"]:
                errores.append(f"{i}->{j} precedencia")
    for mq in maquinas:
        tareas = sorted((f["start"], f["end"], f["job"]) for f in salida if f["machine"] == mq)
        for (s1, e1, j1), (s2, e2, j2) in zip(tareas, tareas[1:]):
            if s2 < e1:
                errores.append(f"solape {j1}/{j2} en {mq}")
    total = sum(inst["w"][j] * max(0, por_job[j]["end"] - inst["d"][j]) for j in jobs if j in por_job)
    return total, errores


def cota_inferior(inst):
    """sum wT >= sum wC - sum wd, con sum wC acotado por Eastman-Even-Isaacs
    (sin liberaciones ni precedencias) y por sum w_j (r_j + p_j)."""
    jobs, m = inst["jobs"], inst["m"]
    p, w, d, r = inst["p"], inst["w"], inst["d"], inst["r"]
    orden = sorted(jobs, key=lambda j: -w[j] / p[j])
    acum, eei = 0, 0
    for j in orden:
        acum += p[j]
        eei += w[j] * acum / m
    eei += (m - 1) / (2 * m) * sum(w[j] * p[j] for j in jobs)
    lb_wc = max(eei, sum(w[j] * (r[j] + p[j]) for j in jobs))
    return max(0.0, lb_wc - sum(w[j] * d[j] for j in jobs))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=30)
    ap.add_argument("--semilla", type=int, default=42)
    ap.add_argument("--holgura", type=float, default=0.0)
    ap.add_argument("--referencia", action="store_true")
    args = ap.parse_args()

    rng = random.Random(args.semilla)
    instancias = [generar(rng, holgura=args.holgura) for _ in range(args.n)]

    filas = []
    print(f"{'inst':>4} {'LB':>7} {'regla':>7} {'final':>7} {'ref':>7} "
          f"{'gap%':>6} {'ms':>7}  estado")
    for k, inst in enumerate(instancias, 1):
        t0 = time.perf_counter()
        salida = reto2.solve(inst)
        ms = (time.perf_counter() - t0) * 1000
        total, errores = validar(inst, salida)

        modelo = reto2.Monstruopolis(*reto2.cargar_instancia(inst))
        _, costo, info = modelo.resolver()
        assert costo == total, (costo, total)
        ref = None
        if args.referencia:
            ref = min([total] + [modelo.resolver(tiempo_max=60, semilla=s, iteraciones=400000)[1]
                                 for s in (11, 22)])
        lb = cota_inferior(inst)
        gap = 100 * (total - ref) / ref if ref else 0.0
        estado = "OK" if not errores else "ERRORES: " + "; ".join(errores[:3])
        filas.append({"tot": total, "ref": ref, "ms": ms, "ini": info["inicial"], "gap": gap})
        print(f"{k:>4} {lb:>7.0f} {info['inicial']:>7} {total:>7} "
              f"{ref if ref is not None else '-':>7} {gap:>6.2f} {ms:>7.1f}  {estado}")

    print("\n==== RESUMEN RETO 2 ====")
    print(f"instancias:              {len(filas)}")
    print(f"sum wjTj promedio:       {statistics.mean(f['tot'] for f in filas):.1f}")
    print(f"mejora vs mejor regla:   "
          f"{statistics.mean(100 * (f['ini'] - f['tot']) / f['ini'] for f in filas if f['ini']):.2f}%")
    if args.referencia:
        print(f"brecha vs corrida larga: {statistics.mean(f['gap'] for f in filas):.3f}%  "
              f"(iguales: {sum(f['tot'] == f['ref'] for f in filas)})")
    print(f"tiempo promedio:         {statistics.mean(f['ms'] for f in filas):.1f} ms"
          f"  (max {max(f['ms'] for f in filas):.1f} ms)")


if __name__ == "__main__":
    main()
