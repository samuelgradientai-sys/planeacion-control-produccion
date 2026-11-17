"""
Algoritmo de Wagner-Whitin (tamaño de lote dinámico).

Notación (igual que en el tablero):
    Z_j  : costo mínimo hasta el momento j (demanda de los periodos 0..j-1 cubierta)
    C_ij : costo de producir en el periodo i para cubrir la demanda de i..j-1
           = setup_i + c_var_i * (d_i + ... + d_{j-1}) + costo de mantener inventario

    Z_0 = 0
    Z_j = min_{i<j} { Z_i + C_ij }
"""

# ---------------- Datos del ejercicio ----------------
# ---------------- Datos del ejercicio (cuerpo) ----------------
demanda = [0, 0, 2380, 0, 2500, 0, 0, 0, 0, 0]   # netos de las semanas 1 a 10
setup   = [80]*10
c_var   = [0]*10
h       = [0.01]*10


def costo_lote(i, j):
    """C_ij: producir en el periodo i toda la demanda de los periodos i..j-1."""
    q = sum(demanda[i:j])
    costo = setup[i] + c_var[i] * q
    # La demanda del periodo k se guarda desde el periodo i hasta el k
    for k in range(i + 1, j):
        costo += demanda[k] * sum(h[i:k])
    return costo


def wagner_whitin():
    n = len(demanda)
    C = {(i, j): costo_lote(i, j) for i in range(n) for j in range(i + 1, n + 1)}

    Z = [0] * (n + 1)
    mejor_i = [None] * (n + 1)

    print("Z_0 = $0")
    for j in range(1, n + 1):
        opciones = {i: Z[i] + C[i, j] for i in range(j)}
        i_opt = min(opciones, key=opciones.get)
        Z[j] = opciones[i_opt]
        mejor_i[j] = i_opt

        print(f"\nZ_{j} = min {{")
        for i, valor in opciones.items():
            marca = "  <-- min" if i == i_opt else ""
            print(f"    Z_{i} + C_{i}{j} = {Z[i]} + {C[i, j]} = {valor}{marca}")
        print(f"}} => ${Z[j]}")

    # Reconstrucción del plan óptimo (hacia atrás)
    produccion = [0] * n
    j = n
    while j > 0:
        i = mejor_i[j]
        produccion[i] = sum(demanda[i:j])
        j = i

    return Z, produccion


def mostrar_plan(produccion):
    print("\nPlan óptimo de producción")
    print(f"{'Periodo':>7} {'Demanda':>8} {'Produc.':>8} {'Inv.final':>10} "
          f"{'Setup':>6} {'Variable':>9} {'Mantener':>9}")
    inventario = 0
    total = 0
    for t, d in enumerate(demanda):
        inventario += produccion[t] - d
        c_setup = setup[t] if produccion[t] > 0 else 0
        c_varia = c_var[t] * produccion[t]
        c_mant = h[t] * inventario
        total += c_setup + c_varia + c_mant
        print(f"{t:>7} {d:>8} {produccion[t]:>8} {inventario:>10} "
              f"{c_setup:>6} {c_varia:>9} {c_mant:>9}")
    print(f"\nCosto total = ${total}")


if __name__ == "__main__":
    Z, produccion = wagner_whitin()
    mostrar_plan(produccion)
