"""
Plantilla base para GradeScope
-------------------------------------------------------
             INSTRUCCIONES IMPORTANTES
-------------------------------------------------------
1. NO cambiar el nombre de la clase ni las funciones principales.
   - Clase obligatoria: Schedulling
   - Métodos obligatorios: generar_instancia(), resolver_instancia(), ejecutar_experimentos()
2. SOLO deben modificar:
   - El contenido de generar_instancia() para crear sus propios datos.
   - El contenido de resolver_instancia() para construir su modelo de optimización.
3. NO modificar:
   - Los nombres de las funciones o variables internas del experimento.
   - El método ejecutar_experimentos() ni su estructura.
   - El nombre del archivo: debe llamarse EXACTAMENTE `reto_schedulling.py`
4. El método ejecutar_experimentos():
   - Ejecuta automáticamente 30 instancias.
   - Mide el tiempo de ejecución por instancia.
   - Devuelve un consolidado con los tiempos individuales.
   - Reporta el tiempo promedio y el total al final.

Cualquier cambio fuera de lo permitido puede causar errores de evaluación automática.
"""

# Agregar dependencias si es necesario, pero sin remover las que ya se encuentran abajo
import random
import numpy as np
import time
import pandas as pd
from optimizador import load_from_dict, run_ga
import json

class Schedulling:
    def __init__(self, n_instancias: int = 30, semilla: int = 42):
        """
        Inicializa la clase con número de instancias y semilla.
        No modificar esta función.
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

        # Rangos de tiempos de procesamiento por máquina
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
        data, jobs, setups = load_from_dict(instancia)
        best_seq, best_ms = run_ga(jobs, setups)
        return {
            "secuencia": [jobs[i]["id"] for i in best_seq], # pueden agregar, eliminar o agregar salidas del modelo
        }

    def ejecutar_experimentos(self):
        """
        Genera y resuelve las instancias, mide tiempos de ejecución
        y consolida los resultados.
        NO modificar esta función.
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