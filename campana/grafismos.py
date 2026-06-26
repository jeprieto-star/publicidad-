# -*- coding: utf-8 -*-
"""
Sistema de diseño de la campaña: helpers SVG y componentes reutilizables.

Enfoque PROFESIONAL y FOTOGRÁFICO:
  - Fondos con fotografías reales de paisaje andino / café (assets/fondos/).
  - Retratos de los candidatos con el fondo recortado (PNG transparente).
  - Velos (scrims) y degradados para garantizar la legibilidad del texto.
  - Acentos de marca: franja tricolor, sello de plancha, tipografía de impacto.
"""
import os
import base64
from . import config as C

# Raíz del proyecto (carpeta que contiene 'campana/')
_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

_UID = [0]
def _uid(prefijo="id"):
    _UID[0] += 1
    return f"{prefijo}{_UID[0]}"


# ----------------------------------------------------------------------
# HELPERS BÁSICOS
# ----------------------------------------------------------------------
def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def data_uri(path):
    """Convierte una imagen del proyecto en data URI base64 (auto-contenida)."""
    full = path if os.path.isabs(path) else os.path.join(_BASE, path)
    ext = os.path.splitext(full)[1].lower().lstrip(".")
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp",
            "gif": "gif"}.get(ext, "png")
    try:
        with open(full, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("ascii")
        return f"data:image/{mime};base64,{b64}"
    except FileNotFoundError:
        return ""


_SIZE_CACHE = {}
def img_size(path):
    """Devuelve (ancho, alto) de una imagen usando Pillow (con caché)."""
    full = path if os.path.isabs(path) else os.path.join(_BASE, path)
    if full in _SIZE_CACHE:
        return _SIZE_CACHE[full]
    try:
        from PIL import Image
        with Image.open(full) as im:
            wh = im.size
    except Exception:
        wh = (1000, 1200)
    _SIZE_CACHE[full] = wh
    return wh


def ajustar_size(texto_str, ancho_max, size_max, factor=0.60):
    n = max(1, len(texto_str))
    return min(size_max, ancho_max / (n * factor))


def texto(x, y, contenido, size, fill=C.NEGRO, weight="bold", anchor="middle",
          spacing=None, peso_extra=0.0, opacity=1.0, font=None, italic=False,
          sombra=False):
    """Texto con engrosado simulado (stroke del mismo color) y sombra opcional."""
    font = font or C.FUENTE
    extra = ""
    if spacing is not None:
        extra += f' letter-spacing="{spacing}"'
    if italic:
        extra += ' font-style="italic"'
    if sombra:
        extra += ' filter="url(#txtShadow)"'
    paint = ""
    if peso_extra > 0:
        sw = size * peso_extra
        paint = (f' paint-order="stroke" stroke="{fill}" stroke-width="{sw:.2f}"'
                 f' stroke-linejoin="round" stroke-linecap="round"')
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" '
            f'font-weight="bold" fill="{fill}" text-anchor="{anchor}" '
            f'opacity="{opacity}"{extra}{paint}>{esc(contenido)}</text>')


def wrap(text, max_chars):
    palabras = text.split()
    lineas, actual = [], ""
    for p in palabras:
        if len(actual) + len(p) + 1 <= max_chars:
            actual = (actual + " " + p).strip()
        else:
            if actual:
                lineas.append(actual)
            actual = p
    if actual:
        lineas.append(actual)
    return lineas


# ----------------------------------------------------------------------
# DEFINICIONES (<defs>): gradientes de marca, velos y filtros
# ----------------------------------------------------------------------
def defs():
    return f"""
  <defs>
    <linearGradient id="gCielo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{C.CREMA}"/>
      <stop offset="1" stop-color="{C.CREMA_OSC}"/>
    </linearGradient>
    <linearGradient id="gVerde" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{C.VERDE}"/>
      <stop offset="1" stop-color="{C.VERDE_OSC}"/>
    </linearGradient>
    <linearGradient id="gVerdeH" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{C.VERDE_OSC}"/>
      <stop offset="1" stop-color="{C.VERDE}"/>
    </linearGradient>
    <linearGradient id="gCafe" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{C.CAFE}"/>
      <stop offset="1" stop-color="{C.CAFE_OSC}"/>
    </linearGradient>
    <linearGradient id="gRojo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{C.ROJO}"/>
      <stop offset="1" stop-color="{C.ROJO_OSC}"/>
    </linearGradient>
    <linearGradient id="gOro" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{C.AMARILLO_CL}"/>
      <stop offset="1" stop-color="{C.AMARILLO}"/>
    </linearGradient>

    <!-- VELOS (scrims) para legibilidad sobre fotografía -->
    <linearGradient id="scrimAbajo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0"    stop-color="{C.VERDE_OSC}" stop-opacity="0"/>
      <stop offset="0.45" stop-color="{C.VERDE_OSC}" stop-opacity="0.45"/>
      <stop offset="1"    stop-color="{C.VERDE_OSC}" stop-opacity="0.95"/>
    </linearGradient>
    <linearGradient id="scrimArriba" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0"   stop-color="{C.VERDE_OSC}" stop-opacity="0.92"/>
      <stop offset="0.5" stop-color="{C.VERDE_OSC}" stop-opacity="0.35"/>
      <stop offset="1"   stop-color="{C.VERDE_OSC}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="scrimIzq" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0"   stop-color="{C.VERDE_OSC}" stop-opacity="0.96"/>
      <stop offset="0.5" stop-color="{C.VERDE_OSC}" stop-opacity="0.55"/>
      <stop offset="1"   stop-color="{C.VERDE_OSC}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="scrimDer" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0"   stop-color="{C.VERDE_OSC}" stop-opacity="0"/>
      <stop offset="0.5" stop-color="{C.VERDE_OSC}" stop-opacity="0.55"/>
      <stop offset="1"   stop-color="{C.VERDE_OSC}" stop-opacity="0.96"/>
    </linearGradient>
    <radialGradient id="vineta" cx="0.5" cy="0.45" r="0.75">
      <stop offset="0"    stop-color="#000000" stop-opacity="0"/>
      <stop offset="0.7"  stop-color="#000000" stop-opacity="0"/>
      <stop offset="1"    stop-color="#000000" stop-opacity="0.45"/>
    </radialGradient>

    <filter id="sombra" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="8" stdDeviation="14" flood-color="#000000" flood-opacity="0.35"/>
    </filter>
    <filter id="sombraSuave" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="3" stdDeviation="6" flood-color="#000000" flood-opacity="0.28"/>
    </filter>
    <filter id="sombraRetrato" x="-40%" y="-20%" width="180%" height="160%">
      <feDropShadow dx="0" dy="10" stdDeviation="22" flood-color="{C.VERDE_OSC}" flood-opacity="0.55"/>
    </filter>
    <filter id="txtShadow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#000000" flood-opacity="0.55"/>
    </filter>
  </defs>
"""


# ----------------------------------------------------------------------
# FONDO FOTOGRÁFICO
# ----------------------------------------------------------------------
def fondo_foto(x, y, w, h, ruta, scrim=None, tinte=None, tinte_op=0.0,
               vineta=False, pos="xMidYMid", clip_rx=0):
    """
    Coloca una fotografía cubriendo el rectángulo (x,y,w,h) con 'slice'.
    scrim: id de gradiente de velo a superponer (p.ej. 'scrimAbajo').
    tinte: color de marca a superponer (unifica las fotos) con opacidad tinte_op.
    """
    cid = _uid("clip")
    s = [f'<g>']
    s.append(f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{clip_rx}"/></clipPath>')
    s.append(f'<g clip-path="url(#{cid})">')
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{C.VERDE_OSC}"/>')
    s.append(f'<image href="{data_uri(ruta)}" x="{x}" y="{y}" width="{w}" height="{h}" '
             f'preserveAspectRatio="{pos} slice"/>')
    if tinte and tinte_op > 0:
        s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{tinte}" opacity="{tinte_op}"/>')
    if vineta:
        s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#vineta)"/>')
    if scrim:
        if isinstance(scrim, (list, tuple)):
            for sc in scrim:
                s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#{sc})"/>')
        else:
            s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#{scrim})"/>')
    s.append('</g></g>')
    return "".join(s)


# ----------------------------------------------------------------------
# RETRATO DEL CANDIDATO (foto con fondo recortado)
# ----------------------------------------------------------------------
def retrato(cx, base_y, alto, candidato, sombra=True, recorte_key="recorte"):
    """
    Dibuja el retrato recortado del candidato escalado a 'alto' px,
    con su base (hombros) apoyada en base_y y centrado horizontalmente en cx.
    """
    ruta = candidato.get(recorte_key) or candidato["foto"]
    w, h = img_size(ruta)
    ratio = w / h
    aw = alto * ratio
    x = cx - aw / 2
    y = base_y - alto
    filt = ' filter="url(#sombraRetrato)"' if sombra else ''
    return (f'<image href="{data_uri(ruta)}" x="{x:.1f}" y="{y:.1f}" '
            f'width="{aw:.1f}" height="{alto:.1f}" preserveAspectRatio="xMidYMid meet"{filt}/>')


def piso_elipse(cx, cy, rx, ry, color=None, op=0.35):
    """Sombra/base elíptica bajo un retrato para 'anclarlo' a la composición."""
    color = color or C.VERDE_OSC
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{color}" opacity="{op}"/>'


# ----------------------------------------------------------------------
# SELLO DE PLANCHA (badge circular con el número)
# ----------------------------------------------------------------------
def sello_plancha(cx, cy, r, numero=C.PLANCHA, dominante=False):
    aro = r * 0.88
    s = [f'<g filter="url(#sombra)">']
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#gRojo)"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{C.BLANCO}" stroke-width="{r*0.05:.1f}"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{aro:.1f}" fill="none" stroke="{C.AMARILLO}" stroke-width="{r*0.035:.1f}"/>')
    if dominante:
        s.append(texto(cx, cy - r*0.46, "PLANCHA", r*0.20, fill=C.AMARILLO_CL, peso_extra=0.05, spacing=r*0.04))
        s.append(texto(cx, cy + r*0.50, numero, r*1.22, fill=C.BLANCO, peso_extra=0.04))
    else:
        s.append(texto(cx, cy - r*0.40, "PLANCHA", r*0.21, fill=C.AMARILLO_CL, peso_extra=0.05, spacing=r*0.03))
        s.append(texto(cx, cy + r*0.52, numero, r*1.02, fill=C.BLANCO, peso_extra=0.04))
    s.append('</g>')
    return "".join(s)


# Compatibilidad
def sello_plancha_grande(cx, cy, r, numero=C.PLANCHA):
    return sello_plancha(cx, cy, r, numero, dominante=True)


# ----------------------------------------------------------------------
# FRANJA TRICOLOR (acento poncho/bandera)
# ----------------------------------------------------------------------
def tira_tricolor(x, y, w, h, horizontal=True):
    s = []
    if horizontal:
        bw = w / 3.0
        for i, col in enumerate(C.TRICOLOR):
            s.append(f'<rect x="{x + i*bw:.1f}" y="{y}" width="{bw+1:.1f}" height="{h}" fill="{col}"/>')
    else:
        bh = h / 3.0
        for i, col in enumerate(C.TRICOLOR):
            s.append(f'<rect x="{x}" y="{y + i*bh:.1f}" width="{w}" height="{bh+1:.1f}" fill="{col}"/>')
    return "".join(s)


# ----------------------------------------------------------------------
# ICONOS DE PROPUESTAS (pictogramas de línea limpios sobre disco)
# ----------------------------------------------------------------------
def icono(nombre, cx, cy, r, color_disco="url(#gVerde)", color=None, sombra=True):
    color = color or C.BLANCO
    u = r / 50.0
    sw = 6.5 * u
    filt = ' filter="url(#sombraSuave)"' if sombra else ''
    g = [f'<g{filt}><circle cx="{cx}" cy="{cy}" r="{r}" fill="{color_disco}"/>'
         f'<circle cx="{cx}" cy="{cy}" r="{r-2*u:.1f}" fill="none" stroke="#FFFFFF" stroke-opacity="0.30" stroke-width="{1.6*u:.1f}"/></g>']
    g.append(f'<g fill="none" stroke="{color}" stroke-width="{sw:.1f}" '
             f'stroke-linecap="round" stroke-linejoin="round">')
    if nombre == "via":
        g.append(f'<path d="M{cx-20*u:.1f},{cy+30*u:.1f} C {cx-30*u:.1f},{cy+2*u:.1f} {cx+28*u:.1f},{cy:.1f} {cx+18*u:.1f},{cy-30*u:.1f}"/>')
        g.append(f'<path d="M{cx-4*u:.1f},{cy+18*u:.1f} L{cx+2*u:.1f},{cy+2*u:.1f} M{cx+6*u:.1f},{cy-10*u:.1f} L{cx+10*u:.1f},{cy-24*u:.1f}" '
                 f'stroke="{C.AMARILLO_CL}" stroke-width="{4*u:.1f}"/>')
    elif nombre == "renovacion":
        # brote de café (tallo con dos hojas) = renovación / nueva siembra
        g.append(f'<path d="M{cx:.1f},{cy+32*u:.1f} L{cx:.1f},{cy-6*u:.1f}"/>')
        g.append(f'<path d="M{cx:.1f},{cy+4*u:.1f} C {cx+8*u:.1f},{cy-12*u:.1f} {cx+22*u:.1f},{cy-16*u:.1f} {cx+30*u:.1f},{cy-14*u:.1f} '
                 f'C {cx+28*u:.1f},{cy-2*u:.1f} {cx+16*u:.1f},{cy+8*u:.1f} {cx:.1f},{cy+4*u:.1f} Z" '
                 f'fill="{color}" stroke="none"/>')
        g.append(f'<path d="M{cx:.1f},{cy-10*u:.1f} C {cx-8*u:.1f},{cy-26*u:.1f} {cx-20*u:.1f},{cy-30*u:.1f} {cx-28*u:.1f},{cy-28*u:.1f} '
                 f'C {cx-26*u:.1f},{cy-16*u:.1f} {cx-14*u:.1f},{cy-6*u:.1f} {cx:.1f},{cy-10*u:.1f} Z" '
                 f'fill="{color}" stroke="none"/>')
    elif nombre == "beneficiadero":
        g.append(f'<path d="M{cx-26*u:.1f},{cy-2*u:.1f} L{cx:.1f},{cy-26*u:.1f} L{cx+26*u:.1f},{cy-2*u:.1f}"/>')
        g.append(f'<path d="M{cx-20*u:.1f},{cy-2*u:.1f} L{cx-20*u:.1f},{cy+26*u:.1f} L{cx+20*u:.1f},{cy+26*u:.1f} L{cx+20*u:.1f},{cy-2*u:.1f}"/>')
        g.append(f'<path d="M{cx-4*u:.1f},{cy+26*u:.1f} L{cx-4*u:.1f},{cy+10*u:.1f} L{cx+8*u:.1f},{cy+10*u:.1f} L{cx+8*u:.1f},{cy+26*u:.1f}"/>')
    elif nombre == "mujer":
        g.append(f'<circle cx="{cx:.1f}" cy="{cy-16*u:.1f}" r="{9*u:.1f}"/>')
        g.append(f'<path d="M{cx-18*u:.1f},{cy+28*u:.1f} L{cx:.1f},{cy-4*u:.1f} L{cx+18*u:.1f},{cy+28*u:.1f} Z"/>')
        g.append(f'<path d="M{cx-10*u:.1f},{cy+14*u:.1f} L{cx+10*u:.1f},{cy+14*u:.1f}"/>')
    elif nombre == "defensoria":
        g.append(f'<path d="M{cx:.1f},{cy-30*u:.1f} L{cx+24*u:.1f},{cy-20*u:.1f} L{cx+24*u:.1f},{cy+2*u:.1f} '
                 f'C {cx+24*u:.1f},{cy+22*u:.1f} {cx+12*u:.1f},{cy+30*u:.1f} {cx:.1f},{cy+32*u:.1f} '
                 f'C {cx-12*u:.1f},{cy+30*u:.1f} {cx-24*u:.1f},{cy+22*u:.1f} {cx-24*u:.1f},{cy+2*u:.1f} '
                 f'L {cx-24*u:.1f},{cy-20*u:.1f} Z"/>')
        g.append(f'<path d="M{cx-11*u:.1f},{cy+2*u:.1f} L{cx-2*u:.1f},{cy+12*u:.1f} L{cx+13*u:.1f},{cy-10*u:.1f}" '
                 f'stroke="{C.AMARILLO_CL}"/>')
    g.append('</g>')
    return "".join(g)


# ----------------------------------------------------------------------
# UTILIDADES DE TEXTO PARA NOMBRES
# ----------------------------------------------------------------------
def nombre_lineas(nombre):
    palabras = nombre.split()
    if len(palabras) <= 1 or len(nombre) <= 15:
        return [nombre]
    mejor_i, mejor_dif = 1, 10**9
    for i in range(1, len(palabras)):
        a = len(" ".join(palabras[:i]))
        b = len(" ".join(palabras[i:]))
        if abs(a - b) < mejor_dif:
            mejor_dif, mejor_i = abs(a - b), i
    return [" ".join(palabras[:mejor_i]), " ".join(palabras[mejor_i:])]


def placa_nombre(cx, y, ancho, nombre, rol, alto=120, size_nombre=48,
                 fondo="url(#gVerde)", color_rol=None):
    """Placa con el nombre (1-2 líneas, autoajustado) y el rol debajo."""
    color_rol = color_rol or C.AMARILLO_CL
    x = cx - ancho / 2
    lineas = nombre_lineas(nombre)
    s = [f'<g filter="url(#sombraSuave)">']
    s.append(f'<rect x="{x}" y="{y}" width="{ancho}" height="{alto}" rx="{alto*0.14:.0f}" fill="{fondo}"/>')
    s.append(f'<rect x="{x}" y="{y}" width="{ancho}" height="{alto}" rx="{alto*0.14:.0f}" fill="none" stroke="{C.AMARILLO}" stroke-width="2" opacity="0.6"/>')
    if len(lineas) == 1:
        sn = ajustar_size(lineas[0], ancho * 0.88, min(size_nombre, alto * 0.44), factor=0.58)
        s.append(texto(cx, y + alto * 0.46, lineas[0], sn, fill=C.BLANCO, peso_extra=0.045))
        s.append(texto(cx, y + alto * 0.80, rol, alto * 0.17, fill=color_rol, peso_extra=0.04, spacing=alto * 0.05))
    else:
        ancho_ref = max(lineas, key=len)
        sn = ajustar_size(ancho_ref, ancho * 0.88, min(size_nombre, alto * 0.30), factor=0.58)
        s.append(texto(cx, y + alto * 0.32, lineas[0], sn, fill=C.BLANCO, peso_extra=0.045))
        s.append(texto(cx, y + alto * 0.57, lineas[1], sn, fill=C.BLANCO, peso_extra=0.045))
        s.append(texto(cx, y + alto * 0.85, rol, alto * 0.145, fill=color_rol, peso_extra=0.04, spacing=alto * 0.045))
    s.append('</g>')
    return "".join(s)


def cinta(cx, y, w, h, texto_str, fondo="url(#gRojo)", color=C.BLANCO, size=None):
    """Cinta/etiqueta con texto centrado (para lemas y llamados)."""
    x = cx - w / 2
    size = size or h * 0.42
    s = [f'<g filter="url(#sombraSuave)">']
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h*0.12:.0f}" fill="{fondo}"/>')
    s.append(texto(cx, y + h*0.68, texto_str, size, fill=color, peso_extra=0.04, spacing=size*0.02))
    s.append('</g>')
    return "".join(s)


# ----------------------------------------------------------------------
# FOTO CIRCULAR (retrato recortado dentro de un círculo de color)
# ----------------------------------------------------------------------
def foto_circular(cx, cy, r, candidato, color_borde=None, borde=10,
                  fondo_circulo="url(#gVerde)"):
    """Retrato recortado encajado en un círculo de marca con borde de acento."""
    color_borde = color_borde or C.AMARILLO
    cid = _uid("cc")
    ruta = candidato.get("recorte") or candidato["foto"]
    w, h = img_size(ruta)
    ratio = w / h
    # encuadrar el retrato: el alto del recorte llena ~1.9r, centrado arriba
    ih = r * 2.15
    iw = ih * ratio
    ix = cx - iw / 2
    iy = cy - r * 1.05
    return f"""
    <g filter="url(#sombra)">
      <circle cx="{cx}" cy="{cy}" r="{r+borde}" fill="{C.BLANCO}"/>
      <clipPath id="{cid}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>
      <g clip-path="url(#{cid})">
        <circle cx="{cx}" cy="{cy}" r="{r}" fill="{fondo_circulo}"/>
        <image href="{data_uri(ruta)}" x="{ix:.1f}" y="{iy:.1f}" width="{iw:.1f}" height="{ih:.1f}"
               preserveAspectRatio="xMidYMid meet"/>
      </g>
      <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color_borde}" stroke-width="{borde*0.8:.0f}"/>
    </g>"""
