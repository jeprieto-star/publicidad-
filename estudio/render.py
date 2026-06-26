# -*- coding: utf-8 -*-
"""Arma el documento SVG y exporta a SVG / PNG / PDF."""
import os
import cairosvg
from . import svg as S


def documento(w, h, contenido, fondo="url(#gCrema)", seed=7):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     width="{w}" height="{h}" viewBox="0 0 {w} {h}">
{S.defs(seed)}
  <rect x="0" y="0" width="{w}" height="{h}" fill="{fondo}"/>
{contenido}
</svg>"""


def exportar(svg_str, nombre, c_svg, c_png, c_pdf, escala=2.0):
    for d in (c_svg, c_png, c_pdf):
        os.makedirs(d, exist_ok=True)
    with open(os.path.join(c_svg, nombre + ".svg"), "w", encoding="utf-8") as f:
        f.write(svg_str)
    png = os.path.join(c_png, nombre + ".png")
    cairosvg.svg2png(bytestring=svg_str.encode("utf-8"), write_to=png, scale=escala,
                     background_color="white")
    cairosvg.svg2pdf(bytestring=svg_str.encode("utf-8"),
                     write_to=os.path.join(c_pdf, nombre + ".pdf"))
    return png
