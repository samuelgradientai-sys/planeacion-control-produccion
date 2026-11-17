"""
Regla de despacho ATC (Apparent Tardiness Cost) para una maquina.
Ejemplo de la Lec 17 (diapositivas 43-45).

    I_j(t) = (w_j / p_j) * exp( -max(d_j - p_j - t, 0) / (K * p_barra) )

    K       : constante a determinar (en el ejemplo K = 1)
    p_barra : tiempo promedio de los trabajos no programados

En cada instante t se programa el trabajo con MAYOR indice I_j(t)
(secuenciacion I[k] >= I[k+1]); luego t avanza en p_j y se repite.

Uso:
    python atc_lec17.py              -> p_barra se recalcula con los trabajos pendientes
    python atc_lec17.py --pbar-fijo  -> p_barra fijo con todos los trabajos (asi salen
                                        exactamente los indices de la diapositiva 45)
    python atc_lec17.py --K 2        -> cambiar la constante K
"""

import argparse
import math

# Datos del ejemplo (diapositiva 43)
TRABAJOS = {
    1: {"p": 5, "d": 1, "w": 2},
    2: {"p": 7, "d": 9, "w": 3},
    3: {"p": 2, "d": 10, "w": 2},
    4: {"p": 8, "d": 6, "w": 1},
}

# Solucion ATC de la diapositiva 45, para verificar
ESPERADO = {
    "secuencia": [1, 3, 2, 4],
    "flujo_promedio": 12,
    "retardo_max": 16,
    "tardanza_ponderada": 39,
}


def indice_atc(trabajo, t, K, p_barra):
    """I_j(t) = (w_j/p_j) * exp(-max(d_j - p_j - t, 0) / (K * p_barra))"""
    holgura = max(trabajo["d"] - trabajo["p"] - t, 0)
    return (trabajo["w"] / trabajo["p"]) * math.exp(-holgura / (K * p_barra))


def programar_atc(trabajos, K=1.0, pbar_fijo=False):
    """Construye la secuencia ATC. Devuelve la secuencia y el detalle de cada iteracion."""
    pendientes = sorted(trabajos)
    p_barra_total = sum(trabajos[j]["p"] for j in pendientes) / len(pendientes)

    t = 0
    secuencia = []
    iteraciones = []

    while pendientes:
        if pbar_fijo:
            p_barra = p_barra_total
        else:
            p_barra = sum(trabajos[j]["p"] for j in pendientes) / len(pendientes)

        indices = {j: indice_atc(trabajos[j], t, K, p_barra) for j in pendientes}

        # Mayor indice; si hay empate, el trabajo de menor numero
        elegido = max(pendientes, key=lambda j: (indices[j], -j))

        iteraciones.append({"t": t, "p_barra": p_barra, "indices": indices, "elegido": elegido})
        secuencia.append(elegido)
        pendientes.remove(elegido)
        t += trabajos[elegido]["p"]

    return secuencia, iteraciones


def evaluar(secuencia, trabajos):
    """Calcula Cj, Lj, wjTj y las medidas de desempeno de una secuencia."""
    t = 0
    filas = []
    for j in secuencia:
        tr = trabajos[j]
        t += tr["p"]
        L = t - tr["d"]
        T = max(L, 0)
        filas.append({"j": j, "p": tr["p"], "C": t, "d": tr["d"], "L": L, "w": tr["w"], "wT": tr["w"] * T})

    n = len(filas)
    medidas = {
        "flujo_promedio": sum(f["C"] for f in filas) / n,
        "flujo_ponderado": sum(f["w"] * f["C"] for f in filas),
        "retardo_max": max(f["L"] for f in filas),
        "tardanza_ponderada": sum(f["wT"] for f in filas),
    }
    return filas, medidas


def imprimir_iteraciones(iteraciones, trabajos):
    ids = sorted(trabajos)
    print("Indices ATC en cada decision (* = trabajo elegido)")
    print(f"{'t':>4} {'p_barra':>8} | " + " ".join(f"{'I(' + str(j) + ')':>8}" for j in ids))
    print("-" * (16 + 9 * len(ids)))
    for it in iteraciones:
        celdas = []
        for j in ids:
            if j in it["indices"]:
                marca = "*" if j == it["elegido"] else " "
                celdas.append(f"{it['indices'][j]:7.4f}{marca}")
            else:
                celdas.append(f"{'-':>8}")
        print(f"{it['t']:>4} {it['p_barra']:>8.3f} | " + " ".join(celdas))
    print()


def imprimir_tabla(filas):
    print("Programa ATC")
    etiquetas = [("Secuencia", "j"), ("pj", "p"), ("Cj", "C"), ("dj", "d"),
                 ("Lj = Cj - dj", "L"), ("wj", "w"), ("wjTj", "wT")]
    for nombre, clave in etiquetas:
        print(f"{nombre:<13}" + "".join(f"{f[clave]:>6}" for f in filas))
    print()


def verificar(secuencia, medidas):
    print("Comparacion con la diapositiva 45")
    checks = [
        ("Secuencia", secuencia, ESPERADO["secuencia"]),
        ("Flujo promedio", medidas["flujo_promedio"], ESPERADO["flujo_promedio"]),
        ("Retardo max", medidas["retardo_max"], ESPERADO["retardo_max"]),
        ("Tardanza ponderada", medidas["tardanza_ponderada"], ESPERADO["tardanza_ponderada"]),
    ]
    todo_ok = True
    for nombre, obtenido, esperado in checks:
        ok = obtenido == esperado
        todo_ok &= ok
        print(f"  {nombre:<20} obtenido = {str(obtenido):<14} esperado = {str(esperado):<14} {'OK' if ok else 'DIFERENTE'}")
    print("  Resultado:", "coincide con la solucion de clase" if todo_ok else "NO coincide")


def main():
    parser = argparse.ArgumentParser(description="Regla ATC - ejemplo Lec 17")
    parser.add_argument("--K", type=float, default=1.0, help="constante K (por defecto 1)")
    parser.add_argument("--pbar-fijo", action="store_true",
                        help="usar p_barra de todos los trabajos en vez de solo los pendientes")
    args = parser.parse_args()

    modo = "fijo (todos los trabajos)" if args.pbar_fijo else "trabajos no programados"
    print(f"Regla ATC  |  K = {args.K}  |  p_barra = {modo}\n")

    secuencia, iteraciones = programar_atc(TRABAJOS, K=args.K, pbar_fijo=args.pbar_fijo)
    filas, medidas = evaluar(secuencia, TRABAJOS)

    imprimir_iteraciones(iteraciones, TRABAJOS)
    imprimir_tabla(filas)

    print("Secuencia ATC:", " -> ".join(map(str, secuencia)))
    print(f"Flujo promedio          = {medidas['flujo_promedio']:g}")
    print(f"Flujo ponderado (wjCj)  = {medidas['flujo_ponderado']:g}")
    print(f"Retardo maximo (Lmax)   = {medidas['retardo_max']:g}")
    print(f"Tardanza ponderada      = {medidas['tardanza_ponderada']:g}")
    print()

    verificar(secuencia, medidas)


if __name__ == "__main__":
    main()
