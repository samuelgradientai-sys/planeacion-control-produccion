"""Genera la carpeta `claude-proyectos/`: paquetes de Markdown pensados para cargarse en un
Proyecto de claude.ai («Añadir contenido desde GitHub»), que tiene un límite de tamaño.

Paquetes:
  corte-1-completo/, corte-2-completo/, corte-3-completo/
      Todo el contenido de un corte: README de cada tema + resumen y contenido completo de cada
      clase + explicación de cada Excel + cuadernos, Word y código. Sin los anexos automáticos
      (repiten el contenido) ni los CSV/binarios, que siguen en el repositorio.
  curso-completo-resumido/
      Los tres cortes en un solo Proyecto: README de cortes y temas, resumen de cada clase,
      resúmenes de cuadernos/Word, catálogo y erratas.

Uso (desde la raíz del repositorio):  python -I herramientas/generar_paquetes_claude.py .
No editar a mano lo que hay en claude-proyectos/: se regenera con este script.
"""
import sys, re, pathlib, posixpath, urllib.parse, shutil
sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
OUT = ROOT / "claude-proyectos"
REPO_URL = "https://github.com/samuelgradientai-sys/planeacion-control-produccion"
CAPACIDAD_EST = 760_000  # caracteres ≈ 100 % de un Proyecto (estimado; el diálogo muestra el valor real)

CORTES = {
    "corte-1-pronosticos": "Corte 1: Pronósticos de demanda",
    "corte-2-planeacion-agregada-mrp": "Corte 2: Planeación agregada, tamaño de lote y MRP",
    "corte-3-programacion-scheduling": "Corte 3: Programación de la producción (scheduling)",
}
BINARIOS = {".pdf", ".xlsx", ".xls", ".docx", ".ipynb"}
TEXTO_CODIGO = {".py": "python", ".gms": "gams", ".json": "json", ".csv": "csv"}
# Archivos de código que no se incluyen (copias generadas o salidas largas ya explicadas en los README)
OMITIR = {
    "corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/gradescope/reto1_willy_wonka/reto_schedulling.py":
        "copia generada de `solucion/reto1.py` dentro de la plantilla (ver `construir_plantillas.py`)",
    "corte-3-programacion-scheduling/proyecto-competencia-scheduling/solucion/gradescope/reto2_monstruopolis/reto_schedulling.py":
        "copia generada de `solucion/reto2.py` dentro de la plantilla (ver `construir_plantillas.py`)",
}
# Cuadernos cuyo contenido está completo dentro de otro (solo se incluye su resumen)
SOLO_RESUMEN = {
    "corte-2-planeacion-agregada-mrp/proyecto-thyms-gemelo-digital/Gemelo_Digital_Thyms.md":
        "Las celdas 0–35 de este cuaderno son idénticas (código y salidas) a las de `Gemelo_Digital_Thyms_MEJORADO`, cuyo contenido completo sí está en este paquete.",
}

LINK = re.compile(r"(!?\[[^\]]*\])\(([^)\s]+)\)")

def absolutizar(texto, rel_md):
    """Reescribe los enlaces relativos de un .md (ubicado en rel_md) como rutas desde la raíz del
    repositorio (más cortas que la URL completa; la guía de cada paquete da la URL base)."""
    base = posixpath.dirname(rel_md)
    def rep(m):
        url = m.group(2)
        if re.match(r"^[a-z]+:|^#", url):
            return m.group(0)
        ruta, _, ancla = url.partition("#")
        destino = posixpath.normpath(posixpath.join(base, urllib.parse.unquote(ruta)))
        if ruta.endswith("/") or (ROOT / destino).is_dir():
            destino += "/"
        return f"{m.group(1)}(/{urllib.parse.quote(destino)}{'#' + ancla if ancla else ''})"
    # no tocar bloques de código
    partes = re.split(r"(```.*?```)", texto, flags=re.S)
    return "".join(p if p.startswith("```") else LINK.sub(rep, p) for p in partes)

def leer(rel):
    return (ROOT / rel).read_text("utf-8").replace("\r\n", "\n")

def corte_anexo(t):
    i = t.find("\n## Anexo")
    return t[:i].rstrip() + "\n" if i > 0 else t

def solo_resumen(t):
    for h in ("\n## Contenido completo", "\n## Contenido del cuaderno", "\n## Texto completo", "\n## Anexo"):
        i = t.find(h)
        if i > 0:
            t = t[:i]
    return t.rstrip() + "\n"

def es_gemelo(rel):
    p = ROOT / rel
    return any(p.with_suffix(e).exists() for e in BINARIOS)

def orden(p):
    n = p.name
    return (0 if n == "README.md" else 1 if re.match(r"L\d\d", n) else 2, str(p.relative_to(ROOT)).lower())

def fuente(rel):
    return f"\n\n---\n\n<!-- fuente: {rel} -->\n"

def bloque_codigo(rel):
    ext = pathlib.Path(rel).suffix.lower()
    return (f"# Código: `{rel}`\n\n> Archivo completo: {REPO_URL}/blob/main/{urllib.parse.quote(rel)}\n\n"
            f"```{TEXTO_CODIGO[ext]}\n{leer(rel).rstrip()}\n```\n")

def paquete_tema(carpeta):
    """Todo el contenido de una carpeta de tema en un solo Markdown."""
    partes, omitidos = [], []
    for p in sorted((x for x in carpeta.rglob("*") if x.is_file()), key=orden):
        rel = p.relative_to(ROOT).as_posix()
        if "-datos/" in rel or p.suffix.lower() in BINARIOS:
            continue
        if rel in OMITIR:
            omitidos.append(f"- `{rel}`: {OMITIR[rel]}."); continue
        if p.suffix.lower() == ".md":
            t = leer(rel)
            if rel in SOLO_RESUMEN:
                t = solo_resumen(t) + f"\n> **Contenido completo omitido en este paquete:** {SOLO_RESUMEN[rel]}\n"
            elif es_gemelo(rel):
                t = corte_anexo(t)
            partes.append(fuente(rel) + absolutizar(t, rel))
        elif p.suffix.lower() in TEXTO_CODIGO and not (p.suffix.lower() == ".csv" and p.stat().st_size > 20_000):
            partes.append(fuente(rel) + bloque_codigo(rel))
        else:
            omitidos.append(f"- `{rel}` (ver en el repositorio: {REPO_URL}/blob/main/{urllib.parse.quote(rel)})")
    texto = "".join(partes).lstrip("\n-").lstrip()
    if omitidos:
        texto += "\n\n---\n\n**Archivos de esta carpeta que no se copiaron en el paquete** (están completos en el repositorio):\n\n" + "\n".join(omitidos) + "\n"
    return texto

def guia(nombre, descripcion, contenido_paquete):
    claude = leer("CLAUDE.md")
    claude = claude.split("\n", 1)[1]  # quitar el título
    return (f"# Guía del paquete «{nombre}»\n\n"
            f"{descripcion}\n\n"
            f"**Repositorio completo** (archivos originales PDF/Excel, anexos con todas las celdas y CSV de datos): {REPO_URL}\n\n"
            f"## Archivos de este paquete\n\n{contenido_paquete}\n\n"
            f"## Paquetes disponibles\n\n"
            f"- `claude-proyectos/corte-1-completo/`: Corte 1 con todo el detalle.\n"
            f"- `claude-proyectos/corte-2-completo/`: Corte 2 con todo el detalle.\n"
            f"- `claude-proyectos/corte-3-completo/`: Corte 3 con todo el detalle, código incluido.\n"
            f"- `claude-proyectos/curso-completo-resumido/`: los tres cortes en versión resumida.\n\n"
            f"En los paquetes, cada archivo original empieza con un comentario `<!-- fuente: ruta -->`. Los enlaces son rutas desde la raíz del repositorio: `/ruta/archivo.md` corresponde a `{REPO_URL}/blob/main/ruta/archivo.md`.\n\n"
            f"---\n\n# Guía general del repositorio (CLAUDE.md)\n"
            + absolutizar(claude, "CLAUDE.md"))

def escribir(ruta, texto):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(texto.rstrip() + "\n", "utf-8", newline="\n")
    return len(texto)

def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    resumen_tamanos = []
    erratas = absolutizar(leer("ERRATAS.md"), "ERRATAS.md")

    # ---------- paquetes completos por corte
    for corte, titulo in CORTES.items():
        n = corte.split("-")[1]
        dest = OUT / f"corte-{n}-completo"
        total, lista = 0, []
        total += escribir(dest / "00-README-del-corte.md", absolutizar(leer(f"{corte}/README.md"), f"{corte}/README.md"))
        lista.append("- `00-README-del-corte.md`: temas del corte en orden de clase.")
        for carpeta in sorted(x for x in (ROOT / corte).iterdir() if x.is_dir()):
            nombre = f"{carpeta.name}.md"
            total += escribir(dest / nombre, paquete_tema(carpeta))
            lista.append(f"- `{nombre}`: todo el contenido de la carpeta `{corte}/{carpeta.name}/`.")
        total += escribir(dest / "ERRATAS.md", erratas)
        lista.append("- `ERRATAS.md`: errores detectados en todo el material, con su corrección.")
        total += escribir(dest / "00-GUIA.md", guia(f"corte-{n}-completo",
            f"Este paquete contiene **todo el material del {titulo}**: el README de cada tema; el resumen y el contenido completo, página por página, de cada presentación; la explicación de cada Excel; los cuadernos, documentos Word y código. Solo se omitieron los anexos automáticos (repiten el contenido) y los CSV de datos largos, que están en el repositorio.",
            "\n".join(lista)))
        resumen_tamanos.append((dest.name, total))

    # ---------- paquete resumido de todo el curso
    dest = OUT / "curso-completo-resumido"
    total, lista = 0, []
    for corte, titulo in CORTES.items():
        n = corte.split("-")[1]
        partes = [absolutizar(leer(f"{corte}/README.md"), f"{corte}/README.md")]
        for carpeta in sorted(x for x in (ROOT / corte).iterdir() if x.is_dir()):
            for p in sorted((x for x in carpeta.rglob("*.md") if "-datos" not in x.parent.name), key=orden):
                rel = p.relative_to(ROOT).as_posix()
                if p.name == "README.md" and p.parent == carpeta:
                    partes.append(fuente(rel) + absolutizar(leer(rel), rel))
                elif es_gemelo(rel) and (p.with_suffix(".pdf").exists() or p.with_suffix(".ipynb").exists() or p.with_suffix(".docx").exists()):
                    partes.append(fuente(rel) + absolutizar(solo_resumen(leer(rel)), rel))
        nombre = f"corte-{n}.md"
        total += escribir(dest / nombre, "".join(partes))
        lista.append(f"- `{nombre}`: {titulo}. Incluye el README del corte, el README de cada tema (archivos, fórmulas clave y ejercicios resueltos con sus resultados) y el resumen de cada presentación, cuaderno y documento.")
    # el catálogo sin enlaces (las rutas ya aparecen como texto en cada fila)
    catalogo = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", leer("CATALOGO.md"))
    total += escribir(dest / "catalogo.md", catalogo)
    lista.append("- `catalogo.md`: todos los archivos del repositorio, con su nombre original y una descripción.")
    total += escribir(dest / "erratas.md", erratas)
    lista.append("- `erratas.md`: errores detectados en el material, con su corrección.")
    total += escribir(dest / "00-GUIA.md", guia("curso-completo-resumido",
        "Este paquete contiene **los tres cortes del curso en versión resumida**: el README de cada corte y de cada tema, el resumen de cada presentación (tema, ideas clave, todas las fórmulas, ejemplos resueltos y páginas clave), los resúmenes de cuadernos y documentos, el catálogo y las erratas. La transcripción página por página y la explicación detallada de cada Excel están en los paquetes `corte-N-completo` y en el repositorio.",
        "\n".join(lista)))
    resumen_tamanos.append((dest.name, total))

    # ---------- README de la carpeta
    filas = "\n".join(f"| `{n}/` | {t/1000:.0f} mil | ≈ {100*t/CAPACIDAD_EST:.0f} % |" for n, t in resumen_tamanos)
    escribir(OUT / "README.md", f"""# Paquetes para Proyectos de claude.ai

Un Proyecto de claude.ai tiene un límite de tamaño (≈ su ventana de contexto). El repositorio completo ocupa unas 5 veces ese límite: sus PDF, Excel, CSV y anexos repiten mucho contenido. Estas carpetas se **generan automáticamente** con [`herramientas/generar_paquetes_claude.py`]({REPO_URL}/blob/main/herramientas/generar_paquetes_claude.py) y caben en un Proyecto.

| Carpeta | Tamaño (caracteres) | Uso estimado de un Proyecto |
|---|---|---|
{filas}

El porcentaje es una estimación; el diálogo «Añadir contenido desde GitHub» muestra el valor real.

## Cómo usarlos

En el Proyecto: **Añadir contenido desde GitHub** → repositorio `planeacion-control-produccion` → desmarca todo → marca **solo una** de estas carpetas.

- **Opción A, un Proyecto por corte, con todo el detalle:** crea tres Proyectos (Corte 1, Corte 2, Corte 3) y carga en cada uno su carpeta `corte-N-completo/`.
- **Opción B, un solo Proyecto con todo el curso resumido:** carga `curso-completo-resumido/`.

Los tres paquetes completos juntos no caben en un solo Proyecto. Puedes combinar `curso-completo-resumido/` con el paquete completo de **un** corte si el diálogo lo permite (ver el porcentaje).

No edites estos archivos a mano. Si cambia el material, vuelve a correr `python -I herramientas/generar_paquetes_claude.py .` desde la raíz del repositorio.
""")
    for n, t in resumen_tamanos:
        print(f"{n:28s} {t/1000:7.0f} mil caracteres  ≈ {100*t/CAPACIDAD_EST:.0f} %")

if __name__ == "__main__":
    main()
