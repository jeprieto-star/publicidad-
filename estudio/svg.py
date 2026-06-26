# -*- coding: utf-8 -*-
"""
Componentes gráficos del sistema "Tierra de Café".
Estilo: cartel cálido, fotografía real protagonista, tipografía de impacto,
sello con número, grano de café y líneas topográficas de la cordillera.
"""
import os
import base64
import math
import random
from . import marca as M

_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_UID = [0]


def _uid(p="id"):
    _UID[0] += 1
    return f"{p}{_UID[0]}"


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def data_uri(path):
    full = path if os.path.isabs(path) else os.path.join(_BASE, path)
    ext = os.path.splitext(full)[1].lower().lstrip(".")
    mime = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "webp": "webp"}.get(ext, "png")
    try:
        with open(full, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("ascii")
        return f"data:image/{mime};base64,{b64}"
    except FileNotFoundError:
        return ""


_SZ = {}
def img_size(path):
    full = path if os.path.isabs(path) else os.path.join(_BASE, path)
    if full in _SZ:
        return _SZ[full]
    try:
        from PIL import Image
        with Image.open(full) as im:
            wh = im.size
    except Exception:
        wh = (1000, 1000)
    _SZ[full] = wh
    return wh


def fit(texto, ancho_max, size_max, factor=0.52):
    n = max(1, len(str(texto)))
    return min(size_max, ancho_max / (n * factor))


# ----------------------------------------------------------------------
# TEXTO
# ----------------------------------------------------------------------
def texto(x, y, s, size, fill=M.TINTA, font=None, weight="400", anchor="middle",
          spacing=None, italic=False, upper=False, op=1.0, stroke=None, stroke_w=0,
          sombra=False):
    font = font or M.SANS
    if upper:
        s = str(s).upper()
    extra = ""
    if spacing is not None:
        extra += f' letter-spacing="{spacing}"'
    if italic:
        extra += ' font-style="italic"'
    if sombra:
        extra += ' filter="url(#sh_txt)"'
    paint = ""
    if stroke and stroke_w:
        paint = (f' paint-order="stroke" stroke="{stroke}" stroke-width="{stroke_w}"'
                 f' stroke-linejoin="round"')
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" '
            f'opacity="{op}"{extra}{paint}>{esc(s)}</text>')


def wrap(text, max_chars):
    out, cur = [], ""
    for w in text.split():
        if len(cur) + len(w) + 1 <= max_chars:
            cur = (cur + " " + w).strip()
        else:
            out.append(cur)
            cur = w
    if cur:
        out.append(cur)
    return out


# ----------------------------------------------------------------------
# DEFS
# ----------------------------------------------------------------------
def defs(seed=7):
    random.seed(seed)
    # textura de grano (puntitos) generada como feTurbulence
    return f"""
<defs>
  <linearGradient id="gCrema" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{M.HUESO}"/><stop offset="1" stop-color="{M.CREMA_OSC}"/>
  </linearGradient>
  <linearGradient id="gEspresso" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{M.ESPRESSO_2}"/><stop offset="1" stop-color="{M.ESPRESSO}"/>
  </linearGradient>
  <linearGradient id="gCereza" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{M.CEREZA_CL}"/><stop offset="1" stop-color="{M.CEREZA_OSC}"/>
  </linearGradient>
  <linearGradient id="gAmbar" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{M.AMBAR}"/><stop offset="1" stop-color="{M.AMBAR_CL}"/>
  </linearGradient>
  <!-- velos para apoyar texto sobre foto -->
  <linearGradient id="velAbajo" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{M.ESPRESSO}" stop-opacity="0"/>
    <stop offset="0.45" stop-color="{M.ESPRESSO}" stop-opacity="0.05"/>
    <stop offset="1" stop-color="{M.ESPRESSO}" stop-opacity="0.92"/>
  </linearGradient>
  <linearGradient id="velArriba" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{M.ESPRESSO}" stop-opacity="0.85"/>
    <stop offset="0.5" stop-color="{M.ESPRESSO}" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="velIzq" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{M.ESPRESSO}" stop-opacity="0.9"/>
    <stop offset="0.7" stop-color="{M.ESPRESSO}" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="velCereza" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{M.CEREZA_OSC}" stop-opacity="0"/>
    <stop offset="1" stop-color="{M.CEREZA_OSC}" stop-opacity="0.92"/>
  </linearGradient>

  <filter id="sh_card" x="-30%" y="-30%" width="160%" height="160%">
    <feDropShadow dx="0" dy="14" stdDeviation="26" flood-color="{M.NEGRO}" flood-opacity="0.34"/>
  </filter>
  <filter id="sh_soft" x="-40%" y="-40%" width="180%" height="180%">
    <feDropShadow dx="0" dy="6" stdDeviation="12" flood-color="{M.NEGRO}" flood-opacity="0.25"/>
  </filter>
  <filter id="sh_txt" x="-30%" y="-30%" width="160%" height="160%">
    <feDropShadow dx="0" dy="2" stdDeviation="6" flood-color="{M.NEGRO}" flood-opacity="0.55"/>
  </filter>
  <filter id="grano">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 0.6 0"/>
  </filter>
  <filter id="blurBg" x="-20%" y="-20%" width="140%" height="140%">
    <feGaussianBlur stdDeviation="6"/>
  </filter>
</defs>
"""


# ----------------------------------------------------------------------
# FONDOS / TEXTURAS
# ----------------------------------------------------------------------
def grano_textura(x, y, w, h, op=0.06):
    """Capa de grano fina para dar cuerpo a fondos planos."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" filter="url(#grano)" '
            f'opacity="{op}"/>')


def topo(x, y, w, h, color=None, op=0.5, n=7, sw=2.2, seed=3):
    """Líneas topográficas (curvas de nivel) de la cordillera — motivo de marca."""
    color = color or M.AMBAR
    random.seed(seed)
    s = [f'<g fill="none" stroke="{color}" stroke-width="{sw}" opacity="{op}" '
         f'stroke-linecap="round">']
    for i in range(n):
        yy = y + h * (i + 0.5) / n
        amp = h * 0.06 * (1 + 0.3 * math.sin(i))
        seg = max(4, w // 90)
        pts = []
        for k in range(seg + 1):
            px = x + w * k / seg
            py = yy + amp * math.sin(k * 0.9 + i * 1.3) + random.uniform(-3, 3)
            pts.append(f"{px:.1f},{py:.1f}")
        s.append(f'<polyline points="{" ".join(pts)}"/>')
    s.append("</g>")
    return "".join(s)


def foto(x, y, w, h, ruta, pos="xMidYMid", rx=0, velo=None, borde=None, borde_w=0):
    """Fotografía real cubriendo el área (slice). 'velo' = id(s) de degradado."""
    cid = _uid("cl")
    s = [f'<g><clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"/></clipPath>']
    s.append(f'<g clip-path="url(#{cid})">')
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{M.ESPRESSO}"/>')
    s.append(f'<image href="{data_uri(ruta)}" x="{x}" y="{y}" width="{w}" height="{h}" '
             f'preserveAspectRatio="{pos} slice"/>')
    if velo:
        for v in (velo if isinstance(velo, (list, tuple)) else [velo]):
            s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#{v})"/>')
    s.append("</g></g>")
    if borde:
        s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="none" '
                 f'stroke="{borde}" stroke-width="{borde_w}"/>')
    return "".join(s)


def panel(x, y, w, h, fill, rx=0, sombra=False, stroke=None, stroke_w=0, op=1.0):
    filt = ' filter="url(#sh_card)"' if sombra else ''
    st = f' stroke="{stroke}" stroke-width="{stroke_w}"' if stroke else ''
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
            f'opacity="{op}"{st}{filt}/>')


# ----------------------------------------------------------------------
# GRANO DE CAFÉ  (motivo de marca, vectorial)
# ----------------------------------------------------------------------
def grano(cx, cy, r, color=None, rot=0):
    color = color or M.ESPRESSO
    return (f'<g transform="translate({cx},{cy}) rotate({rot})">'
            f'<ellipse cx="0" cy="0" rx="{r*0.66:.1f}" ry="{r:.1f}" fill="{color}"/>'
            f'<path d="M0,{-r*0.86:.1f} C {r*0.30:.1f},{-r*0.4:.1f} {-r*0.30:.1f},{r*0.4:.1f} '
            f'0,{r*0.86:.1f}" fill="none" stroke="{M.CREMA}" stroke-width="{r*0.14:.1f}" '
            f'stroke-linecap="round" opacity="0.85"/></g>')


def cereza(cx, cy, r, color=None):
    color = color or M.CEREZA
    return (f'<g><circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/>'
            f'<circle cx="{cx-r*0.3:.1f}" cy="{cy-r*0.32:.1f}" r="{r*0.26:.1f}" '
            f'fill="{M.CEREZA_CL}" opacity="0.8"/>'
            f'<path d="M{cx:.1f},{cy-r:.1f} q {r*0.2:.1f},{-r*0.5:.1f} {r*0.55:.1f},{-r*0.4:.1f}" '
            f'fill="none" stroke="{M.VERDE}" stroke-width="{r*0.18:.1f}" stroke-linecap="round"/></g>')


def franja_granos(x, y, w, paso=46, r=9, color=None, op=0.5):
    """Cinta horizontal de granos (separador decorativo)."""
    color = color or M.ESPRESSO
    s = []
    n = int(w // paso)
    for i in range(n + 1):
        s.append(grano(x + i * paso, y, r, color=color, rot=-22 if i % 2 else 22))
    return f'<g opacity="{op}">' + "".join(s) + "</g>"


# ----------------------------------------------------------------------
# SELLO DE PLANCHA (insignia circular con el número 2)
# ----------------------------------------------------------------------
def sello(cx, cy, r, numero=M.PLANCHA, fondo="url(#gCereza)", aro=None, texto_arc=True):
    aro = aro or M.AMBAR
    s = [f'<g filter="url(#sh_card)">']
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fondo}"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{r*0.9:.1f}" fill="none" stroke="{aro}" '
             f'stroke-width="{r*0.05:.1f}"/>')
    # granos decorativos arriba
    s.append(texto(cx, cy - r*0.40, "PLANCHA", r*0.185, fill=M.AMBAR_CL, font=M.COND,
                   weight="600", spacing=r*0.05, upper=True))
    s.append(texto(cx, cy + r*0.54, numero, r*0.95, fill=M.HUESO, font=M.DISPLAY))
    s.append("</g>")
    return "".join(s)


# ----------------------------------------------------------------------
# RETRATO  (foto recortada del candidato sobre disco/panel de marca)
# ----------------------------------------------------------------------
def retrato_circular(cx, cy, r, cand, borde=None, fondo="url(#gEspresso)", bw=None,
                     fondo_img=None, veil=0.42):
    """Retrato del candidato (recorte) sobre un fondo de CAFETALES —
    conecta con quienes siembran café. El fondo va desenfocado y con un
    velo espresso para que la figura resalte."""
    borde = borde or M.AMBAR
    bw = bw if bw is not None else r * 0.07
    cid = _uid("rc")
    ruta = cand["recorte"]
    w, h = img_size(ruta)
    ratio = w / h
    ih = r * 2.18
    iw = ih * ratio
    ix = cx - iw / 2
    iy = cy - r * 1.04
    bg = fondo_img if fondo_img is not None else M.F_CAFETALES
    bx, by, bd = cx - r, cy - r, 2 * r
    return f"""
<g filter="url(#sh_card)">
  <circle cx="{cx}" cy="{cy}" r="{r+bw}" fill="{M.HUESO}"/>
  <clipPath id="{cid}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>
  <g clip-path="url(#{cid})">
    <circle cx="{cx}" cy="{cy}" r="{r}" fill="{fondo}"/>
    <g filter="url(#blurBg)"><image href="{data_uri(bg)}" x="{bx:.1f}" y="{by:.1f}"
         width="{bd:.1f}" height="{bd:.1f}" preserveAspectRatio="xMidYMid slice"/></g>
    <circle cx="{cx}" cy="{cy}" r="{r}" fill="{M.ESPRESSO}" opacity="{veil}"/>
    <rect x="{bx:.1f}" y="{cy:.1f}" width="{bd:.1f}" height="{r:.1f}" fill="url(#velAbajo)" opacity="0.5"/>
    <image href="{data_uri(ruta)}" x="{ix:.1f}" y="{iy:.1f}" width="{iw:.1f}" height="{ih:.1f}"
           preserveAspectRatio="xMidYMid meet"/>
  </g>
  <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{borde}" stroke-width="{bw:.1f}"/>
</g>"""


def retrato_arco(x, y, w, h, cand, fondo="url(#gEspresso)", borde=None, bw=8):
    """Retrato en marco con tope en arco (forma de portal/iglesia)."""
    borde = borde or M.AMBAR
    cid = _uid("ra")
    ruta = cand["recorte"]
    iw0, ih0 = img_size(ruta)
    ratio = iw0 / ih0
    dw = w * 1.06
    dh = dw / ratio
    if dh < h * 1.02:
        dh = h * 1.02
        dw = dh * ratio
    dx = x + (w - dw) / 2
    dy = y + h - dh
    rad = w / 2
    d = (f'M{x},{y+h} L{x},{y+rad:.1f} A{rad:.1f},{rad:.1f} 0 0 1 {x+w},{y+rad:.1f} '
         f'L{x+w},{y+h} Z')
    s = [f'<g filter="url(#sh_card)">']
    s.append(f'<clipPath id="{cid}"><path d="{d}"/></clipPath>')
    s.append(f'<g clip-path="url(#{cid})">')
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fondo}"/>')
    s.append(f'<image href="{data_uri(ruta)}" x="{dx:.1f}" y="{dy:.1f}" width="{dw:.1f}" '
             f'height="{dh:.1f}" preserveAspectRatio="xMidYMid meet"/>')
    s.append("</g>")
    s.append(f'<path d="{d}" fill="none" stroke="{borde}" stroke-width="{bw}"/>')
    s.append("</g>")
    return "".join(s)


# ----------------------------------------------------------------------
# CINTA / ETIQUETA
# ----------------------------------------------------------------------
def cinta(cx, y, w, h, s_txt, fill="url(#gCereza)", color=None, size=None, rx=None):
    color = color or M.HUESO
    rx = rx if rx is not None else h/2
    size = size or h*0.46
    x = cx - w/2
    return (panel(x, y, w, h, fill, rx=rx)
            + texto(cx, y + h*0.70, s_txt, size, fill=color, font=M.COND,
                    weight="600", spacing=size*0.10, upper=True))


def regla_amb(x, y, w, h=6):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2:.1f}" fill="{M.AMBAR}"/>'


# ----------------------------------------------------------------------
# CTA  (llamado a votar con sello)
# ----------------------------------------------------------------------
def cta(cx, y, w, h):
    x = cx - w/2
    seal = h*0.62
    s = [panel(x, y, w, h, "url(#gEspresso)", rx=h*0.16, sombra=True)]
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h*0.16:.0f}" fill="none" '
             f'stroke="{M.AMBAR}" stroke-width="2" opacity="0.5"/>')
    s.append(sello(x + h*0.78, y + h/2, seal))
    tx = x + h*1.5
    av = (x + w) - tx
    s.append(texto(tx + av/2, y + h*0.44, M.LLAMADO, h*0.24, fill=M.AMBAR_CL, font=M.COND,
                   weight="600", spacing=h*0.05, upper=True))
    s.append(texto(tx + av/2, y + h*0.84, "N.º " + M.PLANCHA, h*0.42, fill=M.HUESO,
                   font=M.DISPLAY))
    return "".join(s)


# ----------------------------------------------------------------------
# ICONOS de propuestas (línea, sobre disco crema con aro cereza)
# ----------------------------------------------------------------------
def icono(nombre, cx, cy, r, disco=True):
    u = r / 50.0
    sw = 5.2 * u
    g = []
    if disco:
        g.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{M.CREMA}"/>')
        g.append(f'<circle cx="{cx}" cy="{cy}" r="{r-1.4*u:.1f}" fill="none" '
                 f'stroke="{M.CEREZA}" stroke-opacity="0.5" stroke-width="{1.7*u:.1f}"/>')
    col = M.ESPRESSO
    g.append(f'<g fill="none" stroke="{col}" stroke-width="{sw:.1f}" '
             f'stroke-linecap="round" stroke-linejoin="round">')
    if nombre == "via":
        g.append(f'<path d="M{cx-22*u:.1f},{cy+30*u:.1f} L{cx-8*u:.1f},{cy-30*u:.1f}"/>')
        g.append(f'<path d="M{cx+22*u:.1f},{cy+30*u:.1f} L{cx+8*u:.1f},{cy-30*u:.1f}"/>')
        g.append(f'<path d="M{cx:.1f},{cy+26*u:.1f} L{cx:.1f},{cy+14*u:.1f} '
                 f'M{cx:.1f},{cy+2*u:.1f} L{cx:.1f},{cy-10*u:.1f} '
                 f'M{cx:.1f},{cy-20*u:.1f} L{cx:.1f},{cy-28*u:.1f}" stroke="{M.CEREZA}"/>')
    elif nombre == "grano":
        g.append(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{20*u:.1f}" ry="{28*u:.1f}"/>')
        g.append(f'<path d="M{cx:.1f},{cy-26*u:.1f} C {cx+9*u:.1f},{cy-12*u:.1f} '
                 f'{cx-9*u:.1f},{cy+12*u:.1f} {cx:.1f},{cy+26*u:.1f}" stroke="{M.CEREZA}"/>')
    elif nombre == "beneficiadero":
        g.append(f'<path d="M{cx-26*u:.1f},{cy-2*u:.1f} L{cx:.1f},{cy-26*u:.1f} '
                 f'L{cx+26*u:.1f},{cy-2*u:.1f}"/>')
        g.append(f'<path d="M{cx-20*u:.1f},{cy-2*u:.1f} L{cx-20*u:.1f},{cy+26*u:.1f} '
                 f'L{cx+20*u:.1f},{cy+26*u:.1f} L{cx+20*u:.1f},{cy-2*u:.1f}"/>')
        g.append(f'<path d="M{cx-5*u:.1f},{cy+26*u:.1f} L{cx-5*u:.1f},{cy+8*u:.1f} '
                 f'L{cx+9*u:.1f},{cy+8*u:.1f} L{cx+9*u:.1f},{cy+26*u:.1f}" stroke="{M.CEREZA}"/>')
    elif nombre == "mujer":
        g.append(f'<circle cx="{cx:.1f}" cy="{cy-17*u:.1f}" r="{8*u:.1f}"/>')
        g.append(f'<path d="M{cx-18*u:.1f},{cy+28*u:.1f} L{cx:.1f},{cy-3*u:.1f} '
                 f'L{cx+18*u:.1f},{cy+28*u:.1f} Z"/>')
        g.append(f'<path d="M{cx-10*u:.1f},{cy+12*u:.1f} L{cx+10*u:.1f},{cy+12*u:.1f}" '
                 f'stroke="{M.CEREZA}"/>')
    elif nombre == "escudo":
        g.append(f'<path d="M{cx:.1f},{cy-30*u:.1f} L{cx+24*u:.1f},{cy-20*u:.1f} '
                 f'L{cx+24*u:.1f},{cy+2*u:.1f} C {cx+24*u:.1f},{cy+22*u:.1f} '
                 f'{cx+12*u:.1f},{cy+30*u:.1f} {cx:.1f},{cy+33*u:.1f} '
                 f'C {cx-12*u:.1f},{cy+30*u:.1f} {cx-24*u:.1f},{cy+22*u:.1f} '
                 f'{cx-24*u:.1f},{cy+2*u:.1f} L {cx-24*u:.1f},{cy-20*u:.1f} Z"/>')
        g.append(f'<path d="M{cx-11*u:.1f},{cy+2*u:.1f} L{cx-2*u:.1f},{cy+12*u:.1f} '
                 f'L{cx+13*u:.1f},{cy-10*u:.1f}" stroke="{M.CEREZA}"/>')
    g.append("</g>")
    return "".join(g)
