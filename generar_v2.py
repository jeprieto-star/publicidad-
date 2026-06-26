# -*- coding: utf-8 -*-
"""
Generador de la PROPUESTA NUEVA — "Tierra de Café · Norte del Tolima".
Salida en salida_v2/ (SVG + PNG + PDF).
    python generar_v2.py
"""
import os
from estudio import render as R
from estudio import piezas as P

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "salida_v2")
SVG, PNG, PDF = (os.path.join(OUT, x) for x in ("svg", "png", "pdf"))

PIEZAS = [
    ("01-afiche-principal",  P.afiche_principal,  2.0),
    ("02-afiche-propuestas", P.afiche_propuestas, 2.0),
    ("03-pasacalle",         P.pasacalle,         1.5),
    ("04-valla",             P.valla,             1.4),
    ("05-volante",           P.volante,           2.0),
    ("06-tarjeta",           P.tarjeta,           2.0),
    ("07-post-redes",        P.post_ig,           1.5),
    ("08-historia-redes",    P.historia_ig,       1.0),
    ("09-sello-marca",       P.sello_marca,       2.0),
]


def main():
    print("Generando propuesta NUEVA · Tierra de Café")
    for nombre, fn, esc in PIEZAS:
        w, h, cont, fondo, seed = fn()
        svg = R.documento(w, h, cont, fondo, seed)
        R.exportar(svg, nombre, SVG, PNG, PDF, escala=esc)
        print(f"  [ok] {nombre}  {w}x{h}")
    print("Listo -> salida_v2/")


if __name__ == "__main__":
    main()
