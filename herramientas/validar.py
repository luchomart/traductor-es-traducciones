#!/usr/bin/env python3
"""
Revisa que el repo esté bien formado. Lo corre GitHub en cada pull request.

    python3 herramientas/validar.py            revisa los archivos de traducciones
    python3 herramientas/validar.py --indice   además rehace index.json

Revisa: carpetas de variantes válidas, nombres de archivo, formato {"revisadas": {...}, "ia": {...}} y
que los marcadores (%s, %d, %1$s...) del inglés estén en el español.
index.json no hace falta tocarlo: GitHub lo rehace solo cada vez que algo entra a main.
"""
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

FORMATO = 1
VARIANTES = {"es_es", "es_mx", "es_ar", "es_cl", "es_uy", "es_ve", "es_ec"}
NOMBRE = re.compile(r"^@?[a-z0-9_.-]+(__[a-z0-9_.-]+)*\.json$")
MARCADOR = re.compile(r"%(?:\d+\$)?[sdf%]")
RAIZ = Path(__file__).resolve().parent.parent


def marcadores(texto: str) -> Counter:
    return Counter(m for m in MARCADOR.findall(texto) if m != "%%")


def revisar_archivo(f: Path, errores: list):
    rel = f.relative_to(RAIZ)
    if not NOMBRE.match(f.name):
        errores.append(f"{rel}: nombre inválido (minúsculas, números, _ . - y @ al principio)")
    try:
        datos = json.loads(f.read_text(encoding="utf-8"))
    except Exception as e:
        errores.append(f"{rel}: no es JSON válido ({e})")
        return
    if not isinstance(datos, dict) or set(datos) - {"revisadas", "ia"}:
        errores.append(f'{rel}: tiene que ser {{"revisadas": {{...}}, "ia": {{...}}}}')
        return
    vistos = set()
    for seccion in ("revisadas", "ia"):
        tabla = datos.get(seccion, {})
        if not isinstance(tabla, dict):
            errores.append(f"{rel}: \"{seccion}\" tiene que ser un objeto")
            continue
        for ingles, espanol in tabla.items():
            donde = f"{rel} [{seccion}] {ingles[:50]!r}"
            if not isinstance(espanol, str) or not espanol.strip() or not ingles.strip():
                errores.append(f"{donde}: texto vacío")
                continue
            if ingles in vistos:
                errores.append(f"{donde}: está en las dos secciones")
            vistos.add(ingles)
            if marcadores(ingles) != marcadores(espanol):
                errores.append(f"{donde}: los marcadores no coinciden ({' '.join(sorted(marcadores(ingles).elements())) or 'ninguno'} → "
                               f"{' '.join(sorted(marcadores(espanol).elements())) or 'ninguno'})")


def indice() -> dict:
    archivos = {}
    for f in sorted(RAIZ.glob("es_*/*.json")):
        datos = json.loads(f.read_text(encoding="utf-8"))
        archivos[f"{f.parent.name}/{f.name}"] = {
            "hash": hashlib.sha256(f.read_bytes()).hexdigest()[:16],
            "revisadas": len(datos.get("revisadas") or {}),
            "ia": len(datos.get("ia") or {}),
        }
    return {"formato": FORMATO, "archivos": archivos}


def main():
    errores = []
    for d in sorted(p for p in RAIZ.iterdir() if p.is_dir() and p.name.startswith("es")):
        if d.name not in VARIANTES:
            errores.append(f"{d.name}/: variante desconocida (válidas: {', '.join(sorted(VARIANTES))})")
            continue
        for f in sorted(d.iterdir()):
            if f.suffix != ".json":
                errores.append(f"{f.relative_to(RAIZ)}: solo van archivos .json")
            else:
                revisar_archivo(f, errores)

    if not errores:
        nuevo = json.dumps(indice(), ensure_ascii=False, indent=1) + "\n"
        f = RAIZ / "index.json"
        if "--indice" in sys.argv:
            f.write_text(nuevo, encoding="utf-8")
            print("index.json rehecho")

    for e in errores:
        print("✗", e)
    print(f"{len(errores)} problema(s)" if errores else "✓ todo bien")
    sys.exit(1 if errores else 0)


if __name__ == "__main__":
    main()
