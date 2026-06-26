# -*- coding: utf-8 -*-
"""
Helpers SVG y componentes gráficos reutilizables de la campaña.
"""
import os
import base64
from . import config as C

# Raíz del proyecto (carpeta que contiene 'campana/')
_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ----------------------------------------------------------------------
# HELPERS BÁSICOS
# ----------------------------------------------------------------------
def esc(s):
    """Escapa caracteres especiales para XML."""
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
        return ""  # se mostrará el fondo azul de respaldo


def ajustar_size(texto_str, ancho_max, size_max, factor=0.60):
    """Calcula un tamaño de fuente que haga caber el texto (mayúsculas, bold)."""
    n = max(1, len(texto_str))
    size_fit = ancho_max / (n * factor)
    return min(size_max, size_fit)


def texto(x, y, contenido, size, fill=C.NEGRO, weight="bold", anchor="middle",
          spacing=None, peso_extra=0.0, opacity=1.0, font=None, italic=False,
          stroke=None, stroke_w=0.0):
    """
    Texto con truco de 'engrosado': dado que solo hay una fuente variable,
    aplicamos un contorno del mismo color del relleno (paint-order=stroke)
    para simular pesos más fuertes y dar impacto tipográfico.

    peso_extra: 0.0 = normal, ~0.06 = bold real, ~0.12 = black/heavy.
    """
    font = font or C.FUENTE
    extra = ""
    if spacing is not None:
        extra += f' letter-spacing="{spacing}"'
    if italic:
        extra += ' font-style="italic"'
    paint = ""
    if peso_extra > 0:
        sw = size * peso_extra
        paint = (f' paint-order="stroke" stroke="{fill}" stroke-width="{sw:.2f}"'
                 f' stroke-linejoin="round" stroke-linecap="round"')
    if stroke is not None and stroke_w > 0:
        # contorno de color distinto (borde) además del relleno
        paint = (f' paint-order="stroke" stroke="{stroke}" stroke-width="{stroke_w:.2f}"'
                 f' stroke-linejoin="round" stroke-linecap="round"')
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" '
            f'font-weight="bold" fill="{fill}" text-anchor="{anchor}" '
            f'opacity="{opacity}"{extra}{paint}>{esc(contenido)}</text>')


def wrap(text, max_chars):
    """Parte un texto en líneas de ~max_chars respetando palabras."""
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
# DEFINICIONES (gradientes, sombras) — se inyectan en <defs>
# ----------------------------------------------------------------------
def defs():
    return f"""
  <defs>
    <linearGradient id="gCielo" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#FFE9A8"/>
      <stop offset="0.55" stop-color="{C.CREMA}"/>
      <stop offset="1" stop-color="{C.CREMA_OSC}"/>
    </linearGradient>
    <linearGradient id="gVerde" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{C.VERDE_CLARO}"/>
      <stop offset="1" stop-color="{C.VERDE_OSC}"/>
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
    <radialGradient id="gCereza" cx="0.35" cy="0.3" r="0.8">
      <stop offset="0" stop-color="#F0625A"/>
      <stop offset="0.5" stop-color="{C.ROJO}"/>
      <stop offset="1" stop-color="{C.ROJO_OSC}"/>
    </radialGradient>
    <radialGradient id="gSol" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#FFF3C4"/>
      <stop offset="0.6" stop-color="{C.AMARILLO_CL}"/>
      <stop offset="1" stop-color="{C.AMARILLO}"/>
    </radialGradient>
    <filter id="sombra" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="6" stdDeviation="10" flood-color="#000000" flood-opacity="0.28"/>
    </filter>
    <filter id="sombraSuave" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="#000000" flood-opacity="0.22"/>
    </filter>
  </defs>
"""


# ----------------------------------------------------------------------
# COMPONENTE: GRANO / CEREZA DE CAFÉ
# ----------------------------------------------------------------------
def cereza(cx, cy, r):
    return f"""
    <g>
      <circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#gCereza)"/>
      <ellipse cx="{cx - r*0.3:.1f}" cy="{cy - r*0.35:.1f}" rx="{r*0.32:.1f}" ry="{r*0.22:.1f}" fill="#FFFFFF" opacity="0.45"/>
      <circle cx="{cx}" cy="{cy + r*0.6:.1f}" r="{r*0.12:.1f}" fill="{C.CAFE_OSC}"/>
    </g>"""


def grano_cafe(cx, cy, r, color=None):
    """Grano de café (forma ovalada con surco central)."""
    color = color or C.CAFE
    return f"""
    <g transform="translate({cx},{cy})">
      <ellipse cx="0" cy="0" rx="{r}" ry="{r*1.35:.1f}" fill="{color}"/>
      <path d="M0,{-r*1.2:.1f} C {r*0.5:.1f},{-r*0.4:.1f} {-r*0.5:.1f},{r*0.4:.1f} 0,{r*1.2:.1f}"
            fill="none" stroke="{C.CAFE_OSC}" stroke-width="{r*0.18:.1f}" stroke-linecap="round"/>
    </g>"""


# ----------------------------------------------------------------------
# COMPONENTE: HOJA Y RAMA DE CAFÉ
# ----------------------------------------------------------------------
def hoja(fill="url(#gVerde)", largo=110):
    """Hoja apuntando hacia arriba, base en (0,0). Devuelve un <g> sin transform."""
    a = largo
    return f"""
    <g>
      <path d="M0,0 C {a*0.28:.1f},{-a*0.18:.1f} {a*0.30:.1f},{-a*0.72:.1f} 0,{-a:.1f}
               C {-a*0.30:.1f},{-a*0.72:.1f} {-a*0.28:.1f},{-a*0.18:.1f} 0,0 Z"
            fill="{fill}"/>
      <path d="M0,{-a*0.05:.1f} L0,{-a*0.92:.1f}" stroke="{C.VERDE_OSC}" stroke-width="{a*0.025:.1f}" stroke-linecap="round" opacity="0.6"/>
    </g>"""


def rama_cafe(x, y, escala=1.0, rot=0, espejo=False):
    """
    Rama de café con pares de hojas y racimos de cerezas a lo largo del tallo.
    Tallo apuntando hacia arriba desde (x,y).
    """
    sx = -1 if espejo else 1
    partes = [f'<g transform="translate({x},{y}) rotate({rot}) scale({escala*sx},{escala})">']
    # tallo curvo
    partes.append(f'<path d="M0,0 C 10,-120 -10,-260 0,-420" fill="none" '
                  f'stroke="{C.CAFE}" stroke-width="14" stroke-linecap="round"/>')
    # pares de hojas + cerezas a distintas alturas
    niveles = [
        (-70, 32, 0.9), (-150, 40, 1.05), (-235, 36, 0.95),
        (-320, 30, 0.85), (-390, 22, 0.7),
    ]
    for (ty, ang, esc) in niveles:
        tx = 6  # leve curvatura
        partes.append(f'<g transform="translate({tx},{ty})">')
        # hoja derecha
        partes.append(f'<g transform="rotate({90 - ang}) scale({esc})">{hoja()}</g>')
        # hoja izquierda
        partes.append(f'<g transform="rotate({-(90 - ang)}) scale({esc})">{hoja()}</g>')
        # racimo de cerezas en la axila
        partes.append(cereza(-10 * esc, 6, 11 * esc))
        partes.append(cereza(12 * esc, 4, 12 * esc))
        partes.append(cereza(2 * esc, 16, 10 * esc))
        partes.append("</g>")
    partes.append("</g>")
    return "".join(partes)


# ----------------------------------------------------------------------
# COMPONENTE: MONTAÑAS (Cordillera / paisaje cafetero del Norte del Tolima)
# ----------------------------------------------------------------------
def montanas(ancho, base_y, alto=240):
    """Capas de montañas con un nevado al fondo (referencia al paisaje del Líbano)."""
    w, by, h = ancho, base_y, alto
    return f"""
    <g>
      <!-- capa lejana (azulada) -->
      <path d="M0,{by} L0,{by-h*0.75:.0f} L{w*0.22:.0f},{by-h:.0f} L{w*0.40:.0f},{by-h*0.7:.0f}
               L{w*0.62:.0f},{by-h*0.95:.0f} L{w*0.82:.0f},{by-h*0.62:.0f} L{w},{by-h*0.8:.0f} L{w},{by} Z"
            fill="#9FB8A6" opacity="0.55"/>
      <!-- nevado -->
      <path d="M{w*0.55:.0f},{by-h*0.95:.0f} l {h*0.10:.0f},{h*0.18:.0f} l {-h*0.05:.0f},{-h*0.02:.0f}
               l {h*0.05:.0f},{h*0.06:.0f} l {-h*0.07:.0f},0 l {-h*0.05:.0f},{-h*0.05:.0f} Z"
            fill="#FFFFFF" opacity="0.85"/>
      <!-- capa media (verde) -->
      <path d="M0,{by} L0,{by-h*0.45:.0f} L{w*0.30:.0f},{by-h*0.72:.0f} L{w*0.55:.0f},{by-h*0.4:.0f}
               L{w*0.78:.0f},{by-h*0.68:.0f} L{w},{by-h*0.42:.0f} L{w},{by} Z"
            fill="{C.VERDE}" opacity="0.85"/>
      <!-- capa cercana (verde oscuro con textura de cultivo) -->
      <path d="M0,{by} L0,{by-h*0.25:.0f} L{w*0.4:.0f},{by-h*0.42:.0f} L{w*0.7:.0f},{by-h*0.2:.0f}
               L{w},{by-h*0.34:.0f} L{w},{by} Z"
            fill="{C.VERDE_OSC}"/>
    </g>"""


def sol(cx, cy, r):
    """Sol con rayos (sol del Tolima / optimismo)."""
    import math
    rayos = []
    for i in range(16):
        ang = math.radians(i * (360 / 16))
        x1 = cx + math.cos(ang) * r * 1.18
        y1 = cy + math.sin(ang) * r * 1.18
        x2 = cx + math.cos(ang) * r * 1.55
        y2 = cy + math.sin(ang) * r * 1.55
        rayos.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                     f'stroke="{C.AMARILLO}" stroke-width="{r*0.10:.1f}" stroke-linecap="round"/>')
    return f'<g opacity="0.95">{"".join(rayos)}<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#gSol)"/></g>'


# ----------------------------------------------------------------------
# COMPONENTE: SELLO DE PLANCHA (badge circular con el número)
# ----------------------------------------------------------------------
def sello_plancha(cx, cy, r, numero=C.PLANCHA):
    return f"""
    <g filter="url(#sombra)">
      <circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#gRojo)" stroke="{C.BLANCO}" stroke-width="{r*0.06:.1f}"/>
      <circle cx="{cx}" cy="{cy}" r="{r*0.86:.1f}" fill="none" stroke="{C.AMARILLO}" stroke-width="{r*0.04:.1f}" stroke-dasharray="{r*0.10:.1f} {r*0.07:.1f}"/>
      {texto(cx, cy - r*0.40, "PLANCHA", r*0.21, fill=C.AMARILLO_CL, peso_extra=0.06, spacing=r*0.03)}
      {texto(cx, cy + r*0.52, numero, r*1.02, fill=C.BLANCO, peso_extra=0.05)}
    </g>"""


def sello_plancha_grande(cx, cy, r, numero=C.PLANCHA):
    """Variante con el número dominante para vallas/redes."""
    return f"""
    <g filter="url(#sombra)">
      <circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#gRojo)" stroke="{C.BLANCO}" stroke-width="{r*0.05:.1f}"/>
      <circle cx="{cx}" cy="{cy}" r="{r*0.88:.1f}" fill="none" stroke="{C.AMARILLO}" stroke-width="{r*0.035:.1f}"/>
      {texto(cx, cy - r*0.5, "PLANCHA", r*0.19, fill=C.AMARILLO_CL, peso_extra=0.06, spacing=r*0.03)}
      {texto(cx, cy + r*0.46, numero, r*1.18, fill=C.BLANCO, peso_extra=0.05)}
    </g>"""


# ----------------------------------------------------------------------
# COMPONENTE: MARCO DE FOTO DE CANDIDATO
# ----------------------------------------------------------------------
def foto_candidato(x, y, w, h, candidato, mostrar_rol=True, r_borde=18):
    """Foto enmarcada con placa de nombre debajo."""
    nombre = candidato["nombre"]
    rol = candidato["rol"]
    foto = candidato["foto"]
    placa_h = h * 0.0  # nombre va fuera, en las piezas
    s = []
    s.append(f'<g filter="url(#sombra)">')
    # marco
    s.append(f'<rect x="{x-10}" y="{y-10}" width="{w+20}" height="{h+20}" rx="{r_borde}" fill="{C.BLANCO}"/>')
    # recorte de la foto
    cid = f"clip_{abs(hash((x,y,w,h)))%100000}"
    s.append(f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r_borde*0.7:.0f}"/></clipPath>')
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r_borde*0.7:.0f}" fill="{C.AZUL_FOTO}"/>')
    s.append(f'<image href="{data_uri(foto)}" x="{x}" y="{y}" width="{w}" height="{h}" '
             f'preserveAspectRatio="xMidYMid slice" clip-path="url(#{cid})"/>')
    # borde de acento
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r_borde*0.7:.0f}" fill="none" '
             f'stroke="{C.AMARILLO}" stroke-width="6"/>')
    s.append('</g>')
    return "".join(s)


def placa_nombre(cx, y, ancho, nombre, rol, alto=92, size_nombre=44):
    """Placa con el nombre del candidato y su rol (el nombre se autoajusta)."""
    x = cx - ancho / 2
    size_n = ajustar_size(nombre, ancho * 0.88, size_nombre, factor=0.62)
    s = [f'<g filter="url(#sombraSuave)">']
    s.append(f'<rect x="{x}" y="{y}" width="{ancho}" height="{alto}" rx="{alto*0.18:.0f}" fill="url(#gVerde)"/>')
    s.append(f'<rect x="{x}" y="{y}" width="{ancho}" height="{alto*0.30:.0f}" rx="{alto*0.18:.0f}" fill="#FFFFFF" opacity="0.12"/>')
    s.append(texto(cx, y + alto*0.50, nombre, size_n, fill=C.BLANCO, peso_extra=0.05))
    s.append(texto(cx, y + alto*0.85, rol, size_nombre*0.42, fill=C.AMARILLO_CL, peso_extra=0.04, spacing=size_nombre*0.06))
    s.append('</g>')
    return "".join(s)


# ----------------------------------------------------------------------
# TIRA TRICOLOR (acento poncho/bandera)
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
# ICONOS DE PROPUESTAS (dibujados, monocromos sobre disco)
# ----------------------------------------------------------------------
def _disco(cx, cy, r, fill="url(#gOro)"):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" filter="url(#sombraSuave)"/>'


def icono(nombre, cx, cy, r, color_disco="url(#gOro)", color=None):
    """Devuelve un icono centrado en (cx,cy) dentro de un disco de radio r."""
    color = color or C.CAFE_OSC
    g = [_disco(cx, cy, r, color_disco)]
    u = r / 50.0  # unidad relativa
    sw = 6 * u
    if nombre == "via":
        # carretera serpenteante
        g.append(f'<path d="M{cx-22*u:.1f},{cy+28*u:.1f} C {cx-30*u:.1f},{cy:.1f} {cx+30*u:.1f},{cy:.1f} {cx+20*u:.1f},{cy-30*u:.1f}" '
                 f'fill="none" stroke="{color}" stroke-width="{14*u:.1f}" stroke-linecap="round"/>')
        g.append(f'<path d="M{cx-22*u:.1f},{cy+28*u:.1f} C {cx-30*u:.1f},{cy:.1f} {cx+30*u:.1f},{cy:.1f} {cx+20*u:.1f},{cy-30*u:.1f}" '
                 f'fill="none" stroke="{C.AMARILLO_CL}" stroke-width="{3*u:.1f}" stroke-dasharray="{8*u:.1f} {8*u:.1f}"/>')
    elif nombre == "renovacion":
        # planta brotando / flechas circulares
        g.append(f'<path d="M{cx:.1f},{cy+30*u:.1f} L{cx:.1f},{cy-2*u:.1f}" stroke="{color}" stroke-width="{sw:.1f}" stroke-linecap="round"/>')
        g.append(f'<path d="M{cx:.1f},{cy+6*u:.1f} C {cx+26*u:.1f},{cy+4*u:.1f} {cx+24*u:.1f},{cy-26*u:.1f} {cx+2*u:.1f},{cy-24*u:.1f} '
                 f'C {cx+6*u:.1f},{cy-6*u:.1f} {cx+18*u:.1f},{cy-4*u:.1f} {cx:.1f},{cy:.1f} Z" fill="{C.VERDE}"/>')
        g.append(f'<path d="M{cx:.1f},{cy+2*u:.1f} C {cx-26*u:.1f},{cy:.1f} {cx-24*u:.1f},{cy-30*u:.1f} {cx-2*u:.1f},{cy-28*u:.1f} '
                 f'C {cx-6*u:.1f},{cy-10*u:.1f} {cx-18*u:.1f},{cy-8*u:.1f} {cx:.1f},{cy-4*u:.1f} Z" fill="{C.VERDE_CLARO}"/>')
    elif nombre == "beneficiadero":
        # casa/tanque de beneficio
        g.append(f'<path d="M{cx-30*u:.1f},{cy-2*u:.1f} L{cx:.1f},{cy-28*u:.1f} L{cx+30*u:.1f},{cy-2*u:.1f} Z" fill="{color}"/>')
        g.append(f'<rect x="{cx-24*u:.1f}" y="{cy-2*u:.1f}" width="{48*u:.1f}" height="{30*u:.1f}" rx="{4*u:.1f}" fill="{color}"/>')
        g.append(f'<rect x="{cx-6*u:.1f}" y="{cy+8*u:.1f}" width="{12*u:.1f}" height="{20*u:.1f}" fill="{C.AMARILLO_CL}"/>')
        # gota de agua (lavado del café)
        g.append(f'<path d="M{cx+22*u:.1f},{cy+14*u:.1f} q {6*u:.1f},{10*u:.1f} 0,{16*u:.1f} q {-6*u:.1f},{-6*u:.1f} 0,{-16*u:.1f} Z" fill="{C.AZUL_FOTO}"/>')
    elif nombre == "mujer":
        # silueta femenina simple
        g.append(f'<circle cx="{cx:.1f}" cy="{cy-18*u:.1f}" r="{10*u:.1f}" fill="{color}"/>')
        g.append(f'<path d="M{cx:.1f},{cy-6*u:.1f} L{cx-18*u:.1f},{cy+28*u:.1f} L{cx+18*u:.1f},{cy+28*u:.1f} Z" fill="{color}"/>')
        g.append(f'<path d="M{cx:.1f},{cy-6*u:.1f} L{cx-10*u:.1f},{cy+10*u:.1f} L{cx+10*u:.1f},{cy+10*u:.1f} Z" fill="{C.ROJO}"/>')
    elif nombre == "defensoria":
        # escudo
        g.append(f'<path d="M{cx:.1f},{cy-30*u:.1f} L{cx+26*u:.1f},{cy-20*u:.1f} L{cx+26*u:.1f},{cy+4*u:.1f} '
                 f'C {cx+26*u:.1f},{cy+24*u:.1f} {cx+12*u:.1f},{cy+32*u:.1f} {cx:.1f},{cy+34*u:.1f} '
                 f'C {cx-12*u:.1f},{cy+32*u:.1f} {cx-26*u:.1f},{cy+24*u:.1f} {cx-26*u:.1f},{cy+4*u:.1f} '
                 f'L{cx-26*u:.1f},{cy-20*u:.1f} Z" fill="{color}"/>')
        g.append(f'<path d="M{cx-12*u:.1f},{cy+2*u:.1f} L{cx-3*u:.1f},{cy+12*u:.1f} L{cx+14*u:.1f},{cy-12*u:.1f}" '
                 f'fill="none" stroke="{C.AMARILLO_CL}" stroke-width="{6*u:.1f}" stroke-linecap="round" stroke-linejoin="round"/>')
    return f'<g>{"".join(g)}</g>'



# ----------------------------------------------------------------------
# COMPONENTE: FOTO CIRCULAR DE CANDIDATO
# ----------------------------------------------------------------------
def foto_circular(cx, cy, r, candidato, color_borde=None, borde=10):
    """Foto recortada en círculo con borde de acento."""
    color_borde = color_borde or C.AMARILLO
    cid = f"cc_{abs(hash((cx, cy, r)))%100000}"
    return f"""
    <g filter="url(#sombra)">
      <circle cx="{cx}" cy="{cy}" r="{r+borde}" fill="{C.BLANCO}"/>
      <clipPath id="{cid}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>
      <circle cx="{cx}" cy="{cy}" r="{r}" fill="{C.AZUL_FOTO}"/>
      <image href="{data_uri(candidato['foto'])}" x="{cx-r}" y="{cy-r}" width="{2*r}" height="{2*r}"
             preserveAspectRatio="xMidYMid slice" clip-path="url(#{cid})"/>
      <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color_borde}" stroke-width="{borde*0.8:.0f}"/>
    </g>"""
