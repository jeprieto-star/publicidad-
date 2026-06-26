# -*- coding: utf-8 -*-
"""
Render: arma el documento SVG completo y lo exporta a SVG, PNG y PDF.
"""
import os
import cairosvg
from . import config as C
from . import grafismos as G


def documento(ancho, alto, contenido, fondo="url(#gCielo)"):
    """Envuelve el contenido en un documento SVG completo con <defs> y fondo."""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     width="{ancho}" height="{alto}" viewBox="0 0 {ancho} {alto}">
{G.defs()}
  <rect x="0" y="0" width="{ancho}" height="{alto}" fill="{fondo}"/>
{contenido}
</svg>"""


def exportar(svg_str, nombre, carpeta_svg, carpeta_png, carpeta_pdf, escala=2.0):
    """Guarda el SVG y lo exporta a PNG (alta resolución) y PDF."""
    os.makedirs(carpeta_svg, exist_ok=True)
    os.makedirs(carpeta_png, exist_ok=True)
    os.makedirs(carpeta_pdf, exist_ok=True)

    ruta_svg = os.path.join(carpeta_svg, nombre + ".svg")
    with open(ruta_svg, "w", encoding="utf-8") as f:
        f.write(svg_str)

    ruta_png = os.path.join(carpeta_png, nombre + ".png")
    cairosvg.svg2png(bytestring=svg_str.encode("utf-8"), write_to=ruta_png,
                     scale=escala, background_color="white")

    ruta_pdf = os.path.join(carpeta_pdf, nombre + ".pdf")
    cairosvg.svg2pdf(bytestring=svg_str.encode("utf-8"), write_to=ruta_pdf)

    return ruta_png


def generar_placeholder_foto(ruta, etiqueta):
    """Crea una foto placeholder (silueta sobre fondo azul de estudio) si no existe."""
    if os.path.exists(ruta):
        return
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    w, h = 1080, 1320
    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <rect width="{w}" height="{h}" fill="{C.AZUL_FOTO}"/>
  <g fill="#FFFFFF" opacity="0.85">
    <circle cx="{w/2}" cy="{h*0.40}" r="220"/>
    <path d="M{w/2-360},{h} C {w/2-360},{h*0.66} {w/2-200},{h*0.60} {w/2},{h*0.60}
             C {w/2+200},{h*0.60} {w/2+360},{h*0.66} {w/2+360},{h} Z"/>
  </g>
  <text x="{w/2}" y="{h*0.93}" font-family="{C.FUENTE}" font-size="48" font-weight="bold"
        fill="#FFFFFF" text-anchor="middle">{G.esc(etiqueta)}</text>
  <text x="{w/2}" y="{h*0.97}" font-family="{C.FUENTE}" font-size="30"
        fill="#E6F4FF" text-anchor="middle">(reemplazar por la foto real)</text>
</svg>"""
    cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=ruta, scale=1.0)
