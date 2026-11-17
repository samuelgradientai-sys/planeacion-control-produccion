"""
Banco de pruebas local del RETO 01 (Willy Wonka). No se sube a Gradescope.

Uso (desde la carpeta PROYECTO ALGORITMO):
    python pruebas/probar_reto1.py               -> 30 instancias de la plantilla (semilla 42)
    python pruebas/probar_reto1.py --exacto      -> ademas calcula el optimo exacto de cada instancia
    python pruebas/probar_reto1.py --n 100 --semilla 7

Que revisa:
  * que la secuencia sea una permutacion de los 15 lotes y no tenga N -> R;
  * recalcula el Cmax con un evaluador independiente (sencillo y legible);
  * compara con la cota inferior (LB) y, opcional, con el optimo exacto;
  * muestra tambien lo que daria la funcion calcular_makespan_penalizado de la
    plantilla, que tiene un error en como busca el tipo anterior (ver README).
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

import reto1  # noqa: E402
from exacto_reto1 import optimo_exacto  # noqa: E402


# --------------------------------------------------------------- generador
def generar_instancia_plantilla():
    """Copia exacta de generar_instancia() de la plantilla (sin escribir archivos).
    Usa el random GLOBAL en el mismo orden, asi con random.seed(42) salen las
    mismas instancias que genera la plantilla."""
    tipos = ["S", "N", "R"]
    lotes = [f"L{i}" for i in range(1, 16)]
    rangos = {"M1": (25, 45), "M2": (20, 40), "M3": (10, 25)}
    lotes_dict = {}
    for lote in lotes:
        tipo = random.choice(tipos)
        lotes_dict[lote] = {
            "tipo": tipo,
            "M1": random.randint(*rangos["M1"]),
            "M2": random.randint(*rangos["M2"]),
            "M3": random.randint(*rangos["M3"]),
        }
    setup_dict = {}
    for maquina in ["M1", "M2", "M3"]:
        setup_dict[maquina] = {}
        for tipo_ant in tipos:
            for tipo_sig in tipos:
                if tipo_ant == tipo_sig:
                    tiempo_setup = 0
                elif maquina == "M1":
                    tiempo_setup = random.randint(10, 40)
                elif maquina == "M2":
                    tiempo_setup = random.randint(5, 30)
                else:
                    tiempo_setup = random.randint(3, 15)
                setup_dict[maquina][f"{tipo_ant}-{tipo_sig}"] = tiempo_setup
    return {"lotes": lotes_dict, "setup": setup_dict}


# --------------------------------------------------------------- evaluadores
def cmax_independiente(data, secuencia):
    """Evaluador simple: misma regla de tiempos, escrito sin optimizaciones."""
    lotes, setup = data["lotes"], data["setup"]
    fin = {"M1": 0, "M2": 0, "M3": 0}
    anterior = None
    for lote in secuencia:
        llegada = 0
        for m in ("M1", "M2", "M3"):
            s = 0 if anterior is None else setup[m][f"{lotes[anterior]['tipo']}-{lotes[lote]['tipo']}"]
            inicio = max(fin[m], llegada) + s
            fin[m] = inicio + lotes[lote][m]
            llegada = fin[m]
        anterior = lote
    return fin["M3"]


def violaciones(data, secuencia):
    t = [data["lotes"][x]["tipo"] for x in secuencia]
    return sum(1 for a, b in zip(t, t[1:]) if a == "N" and b == "R")


def cmax_plantilla(data, secuencia):
    """Copia textual de calcular_makespan_penalizado() de la plantilla."""
    lotes = data["lotes"]
    setup = data["setup"]
    maquinas = ["M1", "M2", "M3"]
    penalizado = False
    for i in range(1, len(secuencia)):
        if lotes[secuencia[i - 1]]["tipo"] == "N" and lotes[secuencia[i]]["tipo"] == "R":
            penalizado = True
            break
    fin_maquina = {m: 0 for m in maquinas}
    fin_lote = {l: 0 for l in secuencia}
    for lote in secuencia:
        tipo_actual = lotes[lote]["tipo"]
        for m_idx, m in enumerate(maquinas):
            prev_tipo = None
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
            fin = inicio + lotes[lote][m]
            fin_maquina[m] = fin
            fin_lote[lote] = fin
    makespan = max(fin_maquina.values())
    return float("inf") if penalizado else makespan


# --------------------------------------------------------------- chequeos
def chequear_insercion(n_pruebas=300):
    """Compara la insercion acelerada (Taillard) contra evaluar todas las posiciones."""
    rng = random.Random(1)
    estado = random.getstate()
    random.seed(99)
    for _ in range(n_pruebas):
        modelo = reto1.WillyWonka(generar_instancia_plantilla())
        seq = list(range(modelo.n))
        rng.shuffle(seq)
        j = seq.pop(rng.randrange(len(seq)))
        val, pos = modelo.mejor_insercion(seq, j)
        bruto = min(modelo.evaluar(seq[:i] + [j] + seq[i:]) for i in range(len(seq) + 1))
        assert val == bruto, (val, bruto)
    random.setstate(estado)
    print(f"[ok] insercion acelerada = fuerza bruta en {n_pruebas} casos")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=30, help="numero de instancias")
    ap.add_argument("--semilla", type=int, default=42, help="semilla del generador (plantilla = 42)")
    ap.add_argument("--exacto", action="store_true",
                    help="calcula el optimo con programacion dinamica (pruebas/exacto_reto1.py)")
    args = ap.parse_args()

    chequear_insercion()
    random.seed(args.semilla)
    instancias = [generar_instancia_plantilla() for _ in range(args.n)]

    filas = []
    print(f"\n{'inst':>4} {'LB':>5} {'inicial':>7} {'Cmax':>5} {'optimo':>6} {'gapLB%':>6} "
          f"{'iter':>4} {'ms':>6} {'plantilla':>9}  estado")
    for k, data in enumerate(instancias, 1):
        t0 = time.perf_counter()
        res = reto1.solve(data)
        ms = (time.perf_counter() - t0) * 1000

        seq = res["secuencia"]
        assert sorted(seq) == sorted(data["lotes"]), "la secuencia no es una permutacion"
        v = violaciones(data, seq)
        c_ind = cmax_independiente(data, seq)
        assert c_ind == res["Cmax"], f"Cmax reportado {res['Cmax']} != recalculado {c_ind}"

        _, _, info = reto1.WillyWonka(data).resolver()
        opt = None
        if args.exacto:
            opt = optimo_exacto(data, res["Cmax"])[0]
        gap = 100 * (res["Cmax"] - info["lb"]) / info["lb"]
        estado = "optimo demostrado" if info["optimo_probado"] else ""
        if opt is not None and not info["optimo_probado"]:
            estado = "optimo" if opt == res["Cmax"] else f"a {res['Cmax'] - opt} del optimo"
        if v:
            estado = f"INFACTIBLE ({v} N->R)"
        filas.append({"lb": info["lb"], "cmax": res["Cmax"], "ms": ms, "ini": info["inicial"],
                      "opt": opt, "lbopt": info["optimo_probado"], "gap": gap})
        print(f"{k:>4} {info['lb']:>5} {info['inicial']:>7} {res['Cmax']:>5} "
              f"{opt if opt is not None else '-':>6} {gap:>6.2f} {info['iteraciones']:>4} "
              f"{ms:>6.1f} {cmax_plantilla(data, seq):>9}  {estado}")

    print("\n==== RESUMEN RETO 1 ====")
    print(f"instancias:                  {len(filas)}")
    print(f"optimo demostrado:           {sum(f['lbopt'] for f in filas)}/{len(filas)}")
    if args.exacto:
        nopt = sum(f["cmax"] == f["opt"] for f in filas)
        brecha = statistics.mean(100 * (f["cmax"] - f["opt"]) / f["opt"] for f in filas)
        print(f"optimas (metodo exacto):     {nopt}/{len(filas)}   brecha promedio {brecha:.4f}%")
    print(f"Cmax promedio:               {statistics.mean(f['cmax'] for f in filas):.2f}")
    print(f"brecha promedio vs LB:       {statistics.mean(f['gap'] for f in filas):.3f}%")
    print(f"mejora vs mejor inicial:     "
          f"{statistics.mean(100 * (f['ini'] - f['cmax']) / f['ini'] for f in filas):.3f}%")
    print(f"tiempo promedio:             {statistics.mean(f['ms'] for f in filas):.2f} ms"
          f"  (max {max(f['ms'] for f in filas):.1f} ms)")


if __name__ == "__main__":
    main()
