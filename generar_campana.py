# -*- coding: utf-8 -*-
"""
Generador de la publicidad de la campaña "Plancha N.º 2 - Comprometidos con los Cafeteros".

Uso:
    python generar_campana.py

Genera todas las piezas en salida/ (SVG vectorial + PNG alta resolución + PDF de imprenta).
Edita los datos en campana/config.py (nombres, fotos, propuestas) y vuelve a ejecutar.
"""
import os
from campana import config as C
from campana import render as R
from campana import piezas as P

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "salida")
SVG = os.path.join(OUT, "svg")
PNG = os.path.join(OUT, "png")
PDF = os.path.join(OUT, "pdf")

# Piezas: (nombre_archivo, funcion, escala_png)
PIEZAS = [
    ("01-afiche-principal",  P.afiche_principal, 2.0),
    ("02-afiche-propuestas", P.afiche_propuestas, 2.0),
    ("03-pasacalle",         P.pasacalle,         1.5),
    ("04-valla",             P.valla,             1.4),
    ("05-volante",           P.volante,           2.0),
    ("06-tarjeta",           P.tarjeta,           2.0),
    ("07-post-redes",        P.post_ig,           1.5),
    ("08-historia-redes",    P.historia_ig,       1.0),
]


def main():
    # fotos placeholder (solo si no existen las reales)
    R.generar_placeholder_foto(os.path.join(BASE, "assets", "candidato-1.png"),
                               "FOTO CANDIDATO PRINCIPAL")
    R.generar_placeholder_foto(os.path.join(BASE, "assets", "candidato-2.png"),
                               "FOTO CANDIDATO SUPLENTE")

    print("Generando piezas de la campaña Plancha N.º", C.PLANCHA)
    for nombre, fn, escala in PIEZAS:
        ancho, alto, contenido, fondo = fn()
        svg = R.documento(ancho, alto, contenido, fondo)
        ruta = R.exportar(svg, nombre, SVG, PNG, PDF, escala=escala)
        print(f"  [ok] {nombre}  ->  {ancho}x{alto}px  ({ruta})")
    print("Listo. Revisa la carpeta salida/.")


if __name__ == "__main__":
    main()
