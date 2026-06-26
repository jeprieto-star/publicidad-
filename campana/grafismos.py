# -*- coding: utf-8 -*-
"""
Sistema de diseño EDITORIAL de la campaña.

Principios:
  - Las FOTOGRAFÍAS respiran limpias, en sus propias zonas. NUNCA se lavan
    con un tinte de color encima. Si el texto necesita legibilidad sobre una
    foto, se usa un degradado MUY sutil en un solo borde, o se coloca el
    texto en un panel de color sólido adyacente (layout de zonas).
  - Paleta sobria: verde bosque + crema + oro apagado + terracota.
  - Jerarquía tipográfica clara, aire generoso, reglas finas como acento.
"""
import os
import base64
from . import config as C

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


def ajustar_size(texto_str, ancho_max, size_max, factor=0.58):
    n = max(1, len(texto_str))
    return min(size_max, ancho_max / (n * factor))


# ----------------------------------------------------------------------
# TEXTO
# ----------------------------------------------------------------------
def texto(x, y, contenido, size, fill=C.NEGRO, weight="bold", anchor="middle",
          spacing=None, peso_extra=0.0, opacity=1.0, font=None, italic=False,
          sombra=False, upper=False):
    font = font or C.FUENTE
    if upper:
        contenido = str(contenido).upper()
    extra = ""
    if spacing is not None:
        extra += f' letter-spacing="{spacing}"'
    if italic:
        extra += ' font-style="italic"'
    if sombra:
        extra += ' filter="url(#txtShadow)"'
    fw = "bold" if weight in ("bold", "black") else ("600" if weight == "semibold" else "normal")
    paint = ""
    if peso_extra > 0:
        sw = size * peso_extra
        paint = (f' paint-order="stroke" stroke="{fill}" stroke-width="{sw:.2f}"'
                 f' stroke-linejoin="round" stroke-linecap="round"')
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" '
            f'font-weight="{fw}" fill="{fill}" text-anchor="{anchor}" '
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


# ----------------------------------------------------------------------
# DEFINICIONES (<defs>)
# ----------------------------------------------------------------------
def defs():
    return f"""
  <defs>
    <linearGradient id="gCrema" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{C.HUESO}"/>
      <stop offset="1" stop-color="{C.CREMA}"/>
    </linearGradient>
    <linearGradient id="gVerde" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{C.VERDE}"/>
      <stop offset="1" stop-color="{C.VERDE_OSC}"/>
    </linearGradient>
    <linearGradient id="gVerdeH" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{C.VERDE_OSC}"/>
      <stop offset="1" stop-color="{C.VERDE}"/>
    </linearGradient>
    <linearGradient id="gOro" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{C.ORO}"/>
      <stop offset="1" stop-color="{C.ORO_CL}"/>
    </linearGradient>
    <linearGradient id="gTerra" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{C.TERRACOTA}"/>
      <stop offset="1" stop-color="{C.TERRA_OSC}"/>
    </linearGradient>

    <!-- Degradado de borde MUY sutil (solo para anclar texto en un borde
         de la foto, sin lavar la imagen). Verde profundo translúcido. -->
    <linearGradient id="fadeAbajo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0"    stop-color="{C.VERDE_OSC}" stop-opacity="0"/>
      <stop offset="0.6"  stop-color="{C.VERDE_OSC}" stop-opacity="0"/>
      <stop offset="1"    stop-color="{C.VERDE_OSC}" stop-opacity="0.82"/>
    </linearGradient>
    <linearGradient id="fadeArriba" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0"    stop-color="{C.VERDE_OSC}" stop-opacity="0.72"/>
      <stop offset="0.45" stop-color="{C.VERDE_OSC}" stop-opacity="0"/>
      <stop offset="1"    stop-color="{C.VERDE_OSC}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="fadeIzq" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0"    stop-color="{C.VERDE_OSC}" stop-opacity="0.85"/>
      <stop offset="0.55" stop-color="{C.VERDE_OSC}" stop-opacity="0"/>
      <stop offset="1"    stop-color="{C.VERDE_OSC}" stop-opacity="0"/>
    </linearGradient>

    <filter id="sombra" x="-40%" y="-40%" width="180%" height="180%">
      <feDropShadow dx="0" dy="10" stdDeviation="20" flood-color="{C.NEGRO}" flood-opacity="0.28"/>
    </filter>
    <filter id="sombraSuave" x="-40%" y="-40%" width="180%" height="180%">
      <feDropShadow dx="0" dy="4" stdDeviation="10" flood-color="{C.NEGRO}" flood-opacity="0.20"/>
    </filter>
    <filter id="txtShadow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="2" stdDeviation="5" flood-color="{C.NEGRO}" flood-opacity="0.45"/>
    </filter>
  </defs>
"""


# ----------------------------------------------------------------------
# FOTOGRAFÍA LIMPIA  (sin tinte de cobertura)
# ----------------------------------------------------------------------
def foto(x, y, w, h, ruta, pos="xMidYMid", rx=0, fade=None, borde=None,
         borde_w=0):
    """
    Coloca una fotografía cubriendo (x,y,w,h) con 'slice', SIN lavarla.
    fade: id(s) de degradado de borde sutil (p.ej. 'fadeAbajo') solo si hace
          falta apoyar texto en un borde. Es translúcido y NO cubre el centro.
    borde: color de un filete fino opcional alrededor de la foto.
    """
    cid = _uid("clip")
    s = [f'<g>']
    s.append(f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"/></clipPath>')
    s.append(f'<g clip-path="url(#{cid})">')
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{C.VERDE_OSC}"/>')
    s.append(f'<image href="{data_uri(ruta)}" x="{x}" y="{y}" width="{w}" height="{h}" '
             f'preserveAspectRatio="{pos} slice"/>')
    if fade:
        fades = fade if isinstance(fade, (list, tuple)) else [fade]
        for fdef in fades:
            s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#{fdef})"/>')
    s.append('</g></g>')
    if borde:
        s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="none" '
                 f'stroke="{borde}" stroke-width="{borde_w}"/>')
    return "".join(s)


def panel(x, y, w, h, fill, rx=0, sombra=False, stroke=None, stroke_w=0):
    """Bloque de color sólido (zona de texto, separado de las fotos)."""
    filt = ' filter="url(#sombraSuave)"' if sombra else ''
    st = f' stroke="{stroke}" stroke-width="{stroke_w}"' if stroke else ''
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}"{st}{filt}/>')


# ----------------------------------------------------------------------
# REGLA TRICOLOR FINA  (acento corto, nunca dominante)
# ----------------------------------------------------------------------
def regla_tricolor(x, y, w, h=6, horizontal=True, gap=0):
    """Tres segmentos cortos en tonos apagados. Acento discreto."""
    s = []
    if horizontal:
        seg = (w - 2 * gap) / 3.0
        for i, col in enumerate(C.TRICOLOR):
            s.append(f'<rect x="{x + i*(seg+gap):.1f}" y="{y}" width="{seg:.1f}" height="{h}" rx="{h/2:.1f}" fill="{col}"/>')
    else:
        seg = (h - 2 * gap) / 3.0
        for i, col in enumerate(C.TRICOLOR):
            s.append(f'<rect x="{x}" y="{y + i*(seg+gap):.1f}" width="{w}" height="{seg:.1f}" rx="{w/2:.1f}" fill="{col}"/>')
    return "".join(s)


def filete(x1, y1, x2, y2, color=None, w=2, op=1.0):
    color = color or C.ORO
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}" opacity="{op}"/>'


# ----------------------------------------------------------------------
# RETRATOS  (la foto del candidato recortada — busto)
# ----------------------------------------------------------------------
def marco_retrato(x, y, w, h, candidato, rx=18, fondo="url(#gVerde)",
                  borde=None, borde_w=6, etiqueta=None):
    """
    Retrato dentro de un marco rectangular limpio. La foto recortada se apoya
    en la base del marco (busto), sobre un fondo de color de marca. Filete fino.
    """
    borde = borde or C.HUESO
    cid = _uid("mr")
    ruta = candidato.get("recorte") or candidato["foto"]
    iw, ih = img_size(ruta)
    ratio = iw / ih
    # el busto llena el ancho del marco y se ancla abajo
    draw_w = w * 1.04
    draw_h = draw_w / ratio
    if draw_h < h * 1.02:
        draw_h = h * 1.02
        draw_w = draw_h * ratio
    dx = x + (w - draw_w) / 2
    dy = y + h - draw_h
    s = [f'<g filter="url(#sombra)">']
    s.append(f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"/></clipPath>')
    s.append(f'<g clip-path="url(#{cid})">')
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fondo}"/>')
    s.append(f'<image href="{data_uri(ruta)}" x="{dx:.1f}" y="{dy:.1f}" '
             f'width="{draw_w:.1f}" height="{draw_h:.1f}" preserveAspectRatio="xMidYMid meet"/>')
    s.append('</g>')
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="none" '
             f'stroke="{borde}" stroke-width="{borde_w}"/>')
    s.append('</g>')
    return "".join(s)


def foto_circular(cx, cy, r, candidato, color_borde=None, borde=10,
                  fondo_circulo="url(#gVerde)"):
    color_borde = color_borde or C.ORO
    cid = _uid("cc")
    ruta = candidato.get("recorte") or candidato["foto"]
    w, h = img_size(ruta)
    ratio = w / h
    ih = r * 2.15
    iw = ih * ratio
    ix = cx - iw / 2
    iy = cy - r * 1.02
    return f"""
    <g filter="url(#sombra)">
      <circle cx="{cx}" cy="{cy}" r="{r+borde}" fill="{C.HUESO}"/>
      <clipPath id="{cid}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>
      <g clip-path="url(#{cid})">
        <circle cx="{cx}" cy="{cy}" r="{r}" fill="{fondo_circulo}"/>
        <image href="{data_uri(ruta)}" x="{ix:.1f}" y="{iy:.1f}" width="{iw:.1f}" height="{ih:.1f}"
               preserveAspectRatio="xMidYMid meet"/>
      </g>
      <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color_borde}" stroke-width="{borde*0.7:.0f}"/>
      <circle cx="{cx}" cy="{cy}" r="{r+borde}" fill="none" stroke="{C.VERDE_OSC}" stroke-width="1.5" opacity="0.25"/>
    </g>"""


# ----------------------------------------------------------------------
# NOMBRE DEL CANDIDATO  (tipografía limpia, sin caja pesada)
# ----------------------------------------------------------------------
def nombre_bajo(cx, y, ancho, nombre, rol, color=None, color_rol=None,
                size=40, anchor="middle", regla=True):
    """Nombre (1-2 líneas) + rol en versalitas, con una regla de oro fina.
    Estilo editorial: sin caja de color, deja respirar el diseño."""
    color = color or C.VERDE_OSC
    color_rol = color_rol or C.CAFE
    lineas = nombre_lineas(nombre)
    ref = max(lineas, key=len)
    sn = ajustar_size(ref, ancho, size, factor=0.56)
    s = []
    yy = y
    for ln in lineas[:2]:
        s.append(texto(cx, yy, ln, sn, fill=color, peso_extra=0.02, anchor=anchor))
        yy += sn * 1.04
    if regla:
        rw = ancho * 0.30
        s.append(regla_tricolor(cx - rw/2, yy - sn*0.45, rw, h=5))
    s.append(texto(cx, yy + sn*0.42, rol, sn*0.40, fill=color_rol, peso_extra=0.02,
                   spacing=sn*0.09, anchor=anchor, upper=True))
    return "".join(s)


def etiqueta_rol(cx, y, texto_str, fill="url(#gOro)", color=None, w=200, h=40):
    """Píldora pequeña para el rol (PRINCIPAL / SUPLENTE)."""
    color = color or C.VERDE_OSC
    x = cx - w/2
    return (panel(x, y, w, h, fill, rx=h/2)
            + texto(cx, y + h*0.68, texto_str, h*0.42, fill=color,
                    peso_extra=0.03, spacing=h*0.06, upper=True))


# ----------------------------------------------------------------------
# SELLO DE PLANCHA  (sobrio: aro de oro sobre verde, número grande)
# ----------------------------------------------------------------------
def sello_plancha(cx, cy, r, numero=C.PLANCHA, dominante=False, tono="verde"):
    if tono == "terra":
        fondo = "url(#gTerra)"
    else:
        fondo = "url(#gVerde)"
    aro = r * 0.86
    s = [f'<g filter="url(#sombra)">']
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fondo}"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{aro:.1f}" fill="none" stroke="{C.ORO}" stroke-width="{r*0.045:.1f}"/>')
    if dominante:
        s.append(texto(cx, cy - r*0.44, "PLANCHA", r*0.22, fill=C.ORO_CL, peso_extra=0.03, spacing=r*0.05, upper=True))
        s.append(texto(cx, cy + r*0.52, numero, r*1.20, fill=C.HUESO, peso_extra=0.02))
    else:
        s.append(texto(cx, cy - r*0.40, "PLANCHA", r*0.22, fill=C.ORO_CL, peso_extra=0.03, spacing=r*0.04, upper=True))
        s.append(texto(cx, cy + r*0.50, numero, r*1.04, fill=C.HUESO, peso_extra=0.02))
    s.append('</g>')
    return "".join(s)


def sello_plancha_grande(cx, cy, r, numero=C.PLANCHA):
    return sello_plancha(cx, cy, r, numero, dominante=True)


# ----------------------------------------------------------------------
# LLAMADO A VOTAR  (banda sobria con sello)
# ----------------------------------------------------------------------
def cta(cx, y, w, h, tono="terra", seal_r=None):
    x = cx - w/2
    seal_r = seal_r or h*0.60
    fondo = "url(#gTerra)" if tono == "terra" else "url(#gVerde)"
    s = [panel(x, y, w, h, fondo, rx=h*0.18, sombra=True)]
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h*0.18:.0f}" fill="none" stroke="{C.ORO}" stroke-width="2" opacity="0.55"/>')
    s.append(sello_plancha(x + h*0.74, y + h/2, seal_r, tono="verde" if tono == "terra" else "terra"))
    tx = x + h*1.42
    avail = (x + w) - tx
    s.append(texto(tx + avail/2, y + h*0.42, C.LLAMADO, h*0.26, fill=C.ORO_CL,
                   peso_extra=0.03, spacing=h*0.05, upper=True))
    s.append(texto(tx + avail/2, y + h*0.82, "N.º " + C.PLANCHA, h*0.40,
                   fill=C.HUESO, peso_extra=0.03))
    return "".join(s)


# ----------------------------------------------------------------------
# ICONOS DE PROPUESTAS  (línea fina, refinados, sobre disco tenue)
# ----------------------------------------------------------------------
def icono(nombre, cx, cy, r, color_disco=None, color=None, sombra=False):
    """Pictograma de línea fina dentro de un disco crema con aro de oro."""
    color_disco = color_disco or C.CREMA
    color = color or C.VERDE_OSC
    u = r / 50.0
    sw = 5.0 * u
    filt = ' filter="url(#sombraSuave)"' if sombra else ''
    g = [f'<g{filt}><circle cx="{cx}" cy="{cy}" r="{r}" fill="{color_disco}"/>'
         f'<circle cx="{cx}" cy="{cy}" r="{r-1.5*u:.1f}" fill="none" stroke="{C.ORO}" stroke-opacity="0.55" stroke-width="{1.6*u:.1f}"/></g>']
    g.append(f'<g fill="none" stroke="{color}" stroke-width="{sw:.1f}" '
             f'stroke-linecap="round" stroke-linejoin="round">')
    if nombre == "via":
        # carretera en perspectiva con línea discontinua
        g.append(f'<path d="M{cx-22*u:.1f},{cy+30*u:.1f} L{cx-8*u:.1f},{cy-30*u:.1f}"/>')
        g.append(f'<path d="M{cx+22*u:.1f},{cy+30*u:.1f} L{cx+8*u:.1f},{cy-30*u:.1f}"/>')
        g.append(f'<path d="M{cx:.1f},{cy+26*u:.1f} L{cx:.1f},{cy+14*u:.1f} M{cx:.1f},{cy+2*u:.1f} L{cx:.1f},{cy-10*u:.1f} M{cx:.1f},{cy-20*u:.1f} L{cx:.1f},{cy-28*u:.1f}" stroke="{C.ORO}"/>')
    elif nombre == "renovacion":
        # brote de café: tallo + dos hojas
        g.append(f'<path d="M{cx:.1f},{cy+32*u:.1f} L{cx:.1f},{cy-8*u:.1f}"/>')
        g.append(f'<path d="M{cx:.1f},{cy+6*u:.1f} C {cx+10*u:.1f},{cy-10*u:.1f} {cx+24*u:.1f},{cy-12*u:.1f} {cx+30*u:.1f},{cy-10*u:.1f} '
                 f'C {cx+27*u:.1f},{cy+2*u:.1f} {cx+15*u:.1f},{cy+10*u:.1f} {cx:.1f},{cy+6*u:.1f} Z" fill="{C.VERDE_CLARO}" stroke="{color}"/>')
        g.append(f'<path d="M{cx:.1f},{cy-8*u:.1f} C {cx-10*u:.1f},{cy-24*u:.1f} {cx-22*u:.1f},{cy-26*u:.1f} {cx-28*u:.1f},{cy-24*u:.1f} '
                 f'C {cx-25*u:.1f},{cy-12*u:.1f} {cx-13*u:.1f},{cy-4*u:.1f} {cx:.1f},{cy-8*u:.1f} Z" fill="{C.VERDE_CLARO}" stroke="{color}"/>')
    elif nombre == "beneficiadero":
        # casa/planta de beneficio con techo
        g.append(f'<path d="M{cx-28*u:.1f},{cy-4*u:.1f} L{cx:.1f},{cy-26*u:.1f} L{cx+28*u:.1f},{cy-4*u:.1f}"/>')
        g.append(f'<path d="M{cx-22*u:.1f},{cy-4*u:.1f} L{cx-22*u:.1f},{cy+26*u:.1f} L{cx+22*u:.1f},{cy+26*u:.1f} L{cx+22*u:.1f},{cy-4*u:.1f}"/>')
        g.append(f'<path d="M{cx-6*u:.1f},{cy+26*u:.1f} L{cx-6*u:.1f},{cy+8*u:.1f} L{cx+8*u:.1f},{cy+8*u:.1f} L{cx+8*u:.1f},{cy+26*u:.1f}"/>')
    elif nombre == "mujer":
        # figura femenina simplificada
        g.append(f'<circle cx="{cx:.1f}" cy="{cy-18*u:.1f}" r="{8*u:.1f}"/>')
        g.append(f'<path d="M{cx-18*u:.1f},{cy+28*u:.1f} L{cx:.1f},{cy-4*u:.1f} L{cx+18*u:.1f},{cy+28*u:.1f} Z"/>')
    elif nombre == "defensoria":
        # escudo con visto bueno
        g.append(f'<path d="M{cx:.1f},{cy-30*u:.1f} L{cx+24*u:.1f},{cy-20*u:.1f} L{cx+24*u:.1f},{cy+2*u:.1f} '
                 f'C {cx+24*u:.1f},{cy+22*u:.1f} {cx+12*u:.1f},{cy+30*u:.1f} {cx:.1f},{cy+33*u:.1f} '
                 f'C {cx-12*u:.1f},{cy+30*u:.1f} {cx-24*u:.1f},{cy+22*u:.1f} {cx-24*u:.1f},{cy+2*u:.1f} '
                 f'L {cx-24*u:.1f},{cy-20*u:.1f} Z"/>')
        g.append(f'<path d="M{cx-11*u:.1f},{cy+2*u:.1f} L{cx-2*u:.1f},{cy+12*u:.1f} L{cx+13*u:.1f},{cy-10*u:.1f}" stroke="{C.ORO}"/>')
    g.append('</g>')
    return "".join(g)
