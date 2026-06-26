# -*- coding: utf-8 -*-
"""
Definición de cada pieza publicitaria de la campaña.
Cada función devuelve (ancho, alto, contenido_svg, fondo).

Sistema profesional y fotográfico:
  - Fondos con fotografías reales de paisaje andino y café.
  - Retratos de los candidatos con el fondo recortado.
  - Velos/degradados para legibilidad. Acentos de marca (tricolor, sello).
  - Sin nombres de municipios (campaña para todo el departamento del Tolima).
"""
from . import config as C
from . import grafismos as G

LEMA1 = "COMPROMETIDOS"
LEMA2 = "CON LOS CAFETEROS"
TAGLINE = "Por el campo cafetero del Tolima"


# ----------------------------------------------------------------------
# Helpers de composición comunes
# ----------------------------------------------------------------------
def _header(s, W, color=None, size=24, y=62, sombra=True, spacing=2):
    """Franja tricolor + nombre de la corporación."""
    color = color or C.BLANCO
    s.append(G.tira_tricolor(0, 0, W, 16, horizontal=True))
    s.append(G.texto(W/2, y, C.CORPORACION.upper(), size, fill=color,
                     peso_extra=0.04, spacing=spacing, sombra=sombra))
    s.append(f'<line x1="{W*0.30:.0f}" y1="{y+16}" x2="{W*0.70:.0f}" y2="{y+16}" '
             f'stroke="{C.AMARILLO}" stroke-width="3"/>')


def _lema_blanco(s, cx, y1, s1, s2, gap, color1=C.BLANCO, color2=C.AMARILLO_CL,
                 sub=True, sub_size=None):
    """Lema en dos líneas con sombra, sobre fotografía."""
    s.append(G.texto(cx, y1, LEMA1, s1, fill=color1, peso_extra=0.06, sombra=True))
    s.append(G.texto(cx, y1 + gap, LEMA2, s2, fill=color2, peso_extra=0.06, sombra=True))
    if sub:
        ss = sub_size or s2 * 0.42
        s.append(G.texto(cx, y1 + gap + ss * 1.4, C.SUBLEMA, ss, fill=C.CREMA,
                         italic=True, peso_extra=0.02, sombra=True))


def _cta(s, cx, y, w, h, seal_r=None, vota_size=None, plancha_size=None):
    """Banda roja de llamado a votar con sello de plancha."""
    x = cx - w / 2
    seal_r = seal_r or h * 0.62
    vota_size = vota_size or h * 0.30
    plancha_size = plancha_size or h * 0.46
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h*0.22:.0f}" '
             f'fill="url(#gRojo)" filter="url(#sombra)"/>')
    s.append(G.sello_plancha(x + h*0.78, y + h/2, seal_r))
    tx = x + h*1.5
    avail = (x + w) - tx
    s.append(G.texto(tx + avail/2, y + h*0.40, C.LLAMADO, vota_size,
                     fill=C.AMARILLO_CL, peso_extra=0.05, spacing=vota_size*0.06))
    s.append(G.texto(tx + avail/2, y + h*0.82, "N.º " + C.PLANCHA, plancha_size,
                     fill=C.BLANCO, peso_extra=0.05))


# ======================================================================
# 01 · AFICHE PRINCIPAL (50x70 cm -> 1000 x 1400)
# ======================================================================
def afiche_principal():
    W, H = 1000, 1400
    s = []
    # fondo fotográfico (montañas verdes con nevado)
    s.append(G.fondo_foto(0, 0, W, H, C.F_MONTANA,
                          scrim=("scrimArriba", "scrimAbajo"),
                          tinte=C.VERDE_OSC, tinte_op=0.16, vineta=True))
    _header(s, W)

    # lema sobre la fotografía
    _lema_blanco(s, W/2, 196, 86, 72, 78, sub=True, sub_size=34)

    # panel inferior (escenario verde donde "se paran" los retratos)
    py = 1066
    s.append(f'<rect x="0" y="{py}" width="{W}" height="{H-py}" fill="url(#gVerde)"/>')
    s.append(G.tira_tricolor(0, py-6, W, 6, horizontal=True))

    # retratos recortados de los candidatos
    base_y = py + 30
    s.append(G.piso_elipse(266, base_y-6, 180, 30, op=0.30))
    s.append(G.piso_elipse(734, base_y-6, 180, 30, op=0.30))
    s.append(G.retrato(266, base_y, 560, C.CANDIDATOS[0]))
    s.append(G.retrato(734, base_y, 560, C.CANDIDATOS[1]))

    # placas de nombre
    s.append(G.placa_nombre(266, py + 34, 462, C.CANDIDATOS[0]["nombre"],
                            C.CANDIDATOS[0]["rol"], alto=104, size_nombre=40))
    s.append(G.placa_nombre(734, py + 34, 462, C.CANDIDATOS[1]["nombre"],
                            C.CANDIDATOS[1]["rol"], alto=104, size_nombre=40))

    # CTA
    _cta(s, W/2, 1234, 760, 126, seal_r=78)
    s.append(G.tira_tricolor(0, H-12, W, 12, horizontal=True))
    return W, H, "".join(s), "url(#gVerde)"


# ======================================================================
# 02 · AFICHE DE PROPUESTAS (1000 x 1400)
# ======================================================================
def afiche_propuestas():
    W, H = 1000, 1400
    s = []
    # cuerpo crema con textura verde aérea muy tenue
    s.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#gCielo)"/>')
    # franja-cabecera fotográfica
    hb = 300
    s.append(G.fondo_foto(0, 0, W, hb, C.F_VERDE_AER,
                          scrim=("scrimArriba", "scrimAbajo"),
                          tinte=C.VERDE_OSC, tinte_op=0.30))
    _header(s, W)
    s.append(G.texto(W/2, 168, "NUESTRAS PROPUESTAS", 64, fill=C.BLANCO,
                     peso_extra=0.06, sombra=True))
    s.append(G.texto(W/2, 224, C.LEMA, 30, fill=C.AMARILLO_CL, peso_extra=0.04, sombra=True))

    # tarjetas de propuestas
    top0, alto_card, gap = hb + 22, 168, 14
    for i, p in enumerate(C.PROPUESTAS):
        top = top0 + i * (alto_card + gap)
        s.append(f'<rect x="60" y="{top}" width="{W-120}" height="{alto_card}" rx="24" '
                 f'fill="{C.BLANCO}" filter="url(#sombraSuave)"/>')
        s.append(f'<rect x="60" y="{top}" width="14" height="{alto_card}" rx="7" fill="url(#gRojo)"/>')
        cy = top + alto_card / 2
        s.append(G.icono(p["icono"], 168, cy, 60))
        s.append(G.texto(266, top + 58, p["titulo"], 40, fill=C.VERDE_OSC,
                         peso_extra=0.05, anchor="start"))
        lineas = G.wrap(p["texto"], 42)
        for j, ln in enumerate(lineas[:2]):
            s.append(G.texto(266, top + 100 + j * 36, ln, 27, fill=C.CAFE_OSC,
                             anchor="start", weight="normal"))

    # CTA inferior
    _cta(s, W/2, top0 + 5*(alto_card+gap) + 6, 760, 116, seal_r=72)
    s.append(G.tira_tricolor(0, H-12, W, 12, horizontal=True))
    return W, H, "".join(s), "url(#gCielo)"


# ======================================================================
# 03 · PASACALLE (horizontal 2000 x 500)
# ======================================================================
def pasacalle():
    W, H = 2000, 500
    s = []
    s.append(G.fondo_foto(0, 0, W, H, C.F_MONT_AZUL,
                          scrim=("scrimIzq",), tinte=C.VERDE_OSC, tinte_op=0.42, vineta=True))
    s.append(G.tira_tricolor(0, 0, W, 12, horizontal=True))
    s.append(G.tira_tricolor(0, H-12, W, 12, horizontal=True))

    # retratos circulares
    s.append(G.foto_circular(150, 250, 120, C.CANDIDATOS[0], borde=8))
    s.append(G.foto_circular(415, 250, 120, C.CANDIDATOS[1], borde=8))

    # lema
    s.append(G.texto(575, 205, LEMA1, 92, fill=C.BLANCO, peso_extra=0.06, anchor="start", sombra=True))
    s.append(G.texto(575, 300, LEMA2, 82, fill=C.AMARILLO_CL, peso_extra=0.06, anchor="start", sombra=True))
    s.append(G.texto(577, 360, C.SUBLEMA, 32, fill=C.CREMA, italic=True, anchor="start", sombra=True))
    s.append(G.texto(577, 414, C.CORPORACION.upper(), 26, fill=C.CREMA_OSC, peso_extra=0.03,
                     anchor="start", spacing=1, sombra=True))

    # sello plancha grande a la derecha
    s.append(G.sello_plancha(1800, 250, 168, dominante=True))
    return W, H, "".join(s), "url(#gVerde)"


# ======================================================================
# 04 · VALLA / VAYA (gran formato 2400 x 900, ~8:3)
# ======================================================================
def valla():
    W, H = 2400, 900
    s = []
    s.append(G.fondo_foto(0, 0, W, H, C.F_NEVADO,
                          scrim=("scrimAbajo",), tinte=C.VERDE_OSC, tinte_op=0.20, vineta=True))
    s.append(G.tira_tricolor(0, 0, W, 16, horizontal=True))

    # panel verde inferior (escenario)
    py = 760
    s.append(f'<rect x="0" y="{py}" width="{W}" height="{H-py}" fill="url(#gVerde)"/>')
    s.append(G.tira_tricolor(0, py-6, W, 6, horizontal=True))

    # retratos recortados a la izquierda
    base_y = py + 24
    s.append(G.piso_elipse(330, base_y-6, 210, 30, op=0.28))
    s.append(G.piso_elipse(830, base_y-6, 210, 30, op=0.28))
    s.append(G.retrato(330, base_y, 660, C.CANDIDATOS[0]))
    s.append(G.retrato(830, base_y, 660, C.CANDIDATOS[1]))
    s.append(G.placa_nombre(330, py + 32, 470, C.CANDIDATOS[0]["nombre"],
                            C.CANDIDATOS[0]["rol"], alto=100, size_nombre=38))
    s.append(G.placa_nombre(830, py + 32, 470, C.CANDIDATOS[1]["nombre"],
                            C.CANDIDATOS[1]["rol"], alto=100, size_nombre=38))

    # lema a la derecha (autoajustado para no chocar con el sello)
    lx = 1180
    lema_w = 900
    s1 = G.ajustar_size(LEMA1, lema_w, 108, factor=0.70)
    s2 = G.ajustar_size(LEMA2, lema_w, 84, factor=0.70)
    s.append(G.texto(lx, 240, C.CORPORACION.upper(), 28, fill=C.CREMA, peso_extra=0.03,
                     anchor="start", spacing=2, sombra=True))
    s.append(G.texto(lx, 240 + 128, LEMA1, s1, fill=C.BLANCO, peso_extra=0.06, anchor="start", sombra=True))
    s.append(G.texto(lx, 240 + 128 + s1*0.94, LEMA2, s2, fill=C.AMARILLO_CL, peso_extra=0.06, anchor="start", sombra=True))
    s.append(G.texto(lx + 4, 240 + 128 + s1*0.94 + s2*0.78, C.SUBLEMA, 46, fill=C.CREMA,
                     italic=True, anchor="start", sombra=True))

    # CTA + sello a la derecha (sobre el panel verde)
    _cta(s, 1640, 800, 760, 96, seal_r=60)
    s.append(G.sello_plancha(2250, 330, 130, dominante=True))
    return W, H, "".join(s), "url(#gVerde)"


# ======================================================================
# 05 · VOLANTE (vertical 1000 x 1400)
# ======================================================================
def volante():
    W, H = 1000, 1400
    s = []
    s.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#gCielo)"/>')
    hb = 250
    s.append(G.fondo_foto(0, 0, W, hb, C.F_BOSQUE,
                          scrim=("scrimArriba", "scrimAbajo"),
                          tinte=C.VERDE_OSC, tinte_op=0.32))
    _header(s, W, size=22)
    s.append(G.texto(W/2, 150, LEMA1, 70, fill=C.BLANCO, peso_extra=0.06, sombra=True))
    s.append(G.texto(W/2, 216, LEMA2, 56, fill=C.AMARILLO_CL, peso_extra=0.06, sombra=True))

    # retratos circulares
    s.append(G.foto_circular(320, 400, 132, C.CANDIDATOS[0]))
    s.append(G.foto_circular(680, 400, 132, C.CANDIDATOS[1]))
    for cxn, cand in ((320, C.CANDIDATOS[0]), (680, C.CANDIDATOS[1])):
        s.append(G.placa_nombre(cxn, 552, 350, cand["nombre"], cand["rol"],
                                alto=92, size_nombre=30))

    # propuestas compactas
    s.append(G.texto(W/2, 712, "NUESTRAS PROPUESTAS", 40, fill=C.VERDE_OSC, peso_extra=0.05))
    top0 = 742
    for i, p in enumerate(C.PROPUESTAS):
        top = top0 + i * 96
        s.append(f'<rect x="90" y="{top}" width="{W-180}" height="84" rx="18" '
                 f'fill="{C.BLANCO}" filter="url(#sombraSuave)"/>')
        s.append(G.icono(p["icono"], 150, top + 42, 38))
        s.append(G.texto(214, top + 38, p["titulo"], 30, fill=C.VERDE_OSC,
                         peso_extra=0.05, anchor="start"))
        s.append(G.texto(214, top + 70, p["texto"], 21, fill=C.CAFE_OSC,
                         anchor="start", weight="normal"))

    _cta(s, W/2, top0 + 5*96 + 8, 760, 116, seal_r=72)
    s.append(G.tira_tricolor(0, H-12, W, 12, horizontal=True))
    return W, H, "".join(s), "url(#gCielo)"


# ======================================================================
# 06 · TARJETA DE PRESENTACIÓN (9x5 cm -> 1050 x 600)
# ======================================================================
def tarjeta():
    W, H = 1050, 600
    s = []
    s.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#gCielo)"/>')
    # panel izquierdo de café (granos)
    pw = 430
    s.append(G.fondo_foto(0, 0, pw, H, C.F_GRANOS,
                          scrim=("scrimIzq",), tinte=C.CAFE_OSC, tinte_op=0.45, vineta=True))
    s.append(G.tira_tricolor(0, 0, W, 10, horizontal=True))
    s.append(G.tira_tricolor(0, H-10, W, 10, horizontal=True))

    # retratos circulares sobre el panel de café
    cx1, cx2, cy, r = 144, 332, 230, 86
    s.append(G.foto_circular(cx1, cy, r, C.CANDIDATOS[0], borde=8))
    s.append(G.foto_circular(cx2, cy, r, C.CANDIDATOS[1], borde=8))
    for cxn, cand in ((cx1, C.CANDIDATOS[0]), (cx2, C.CANDIDATOS[1])):
        lineas = G.nombre_lineas(cand["nombre"])
        sn = G.ajustar_size(max(lineas, key=len), 210, 21, factor=0.58)
        yb = cy + r + 40
        for j, ln in enumerate(lineas[:2]):
            s.append(G.texto(cxn, yb + j * (sn + 4), ln, sn, fill=C.BLANCO, peso_extra=0.04, sombra=True))
        s.append(G.texto(cxn, yb + 2 * (sn + 4) + 10, cand["rol"], 15, fill=C.AMARILLO_CL,
                         peso_extra=0.03, spacing=1, sombra=True))

    # zona derecha: lema + plancha
    cxd = 740
    s.append(G.texto(cxd, 70, C.CORPORACION.upper(), 17, fill=C.CAFE, peso_extra=0.04, spacing=1))
    s1 = G.ajustar_size(LEMA1, 540, 50, factor=0.60)
    s2 = G.ajustar_size(LEMA2, 540, 42, factor=0.60)
    s.append(G.texto(cxd, 170, LEMA1, s1, fill=C.VERDE_OSC, peso_extra=0.06))
    s.append(G.texto(cxd, 218, LEMA2, s2, fill=C.CAFE_OSC, peso_extra=0.06))
    s.append(G.texto(cxd, 260, C.SUBLEMA, 24, fill=C.ROJO, italic=True, peso_extra=0.03))

    s.append(G.sello_plancha(610, 410, 72))
    s.append(G.texto(712, 392, C.LLAMADO, 30, fill=C.ROJO_OSC, peso_extra=0.05, anchor="start"))
    s.append(G.texto(712, 444, "N.º " + C.PLANCHA, 48, fill=C.ROJO_OSC, peso_extra=0.05, anchor="start"))
    s.append(G.texto(cxd, 540, TAGLINE, 22, fill=C.VERDE_OSC, peso_extra=0.03))
    return W, H, "".join(s), "url(#gCielo)"


# ======================================================================
# 07 · POST REDES SOCIALES (cuadrado 1080 x 1080)
# ======================================================================
def post_ig():
    W, H = 1080, 1080
    s = []
    s.append(G.fondo_foto(0, 0, W, H, C.F_MONTANA,
                          scrim=("scrimArriba", "scrimAbajo"),
                          tinte=C.VERDE_OSC, tinte_op=0.18, vineta=True))
    _header(s, W)
    s.append(G.texto(W/2, 188, LEMA1, 88, fill=C.BLANCO, peso_extra=0.06, sombra=True))
    s.append(G.texto(W/2, 268, LEMA2, 72, fill=C.AMARILLO_CL, peso_extra=0.06, sombra=True))
    s.append(G.texto(W/2, 322, C.SUBLEMA, 34, fill=C.CREMA, italic=True, peso_extra=0.02, sombra=True))

    s.append(G.foto_circular(340, 560, 165, C.CANDIDATOS[0]))
    s.append(G.foto_circular(740, 560, 165, C.CANDIDATOS[1]))
    s.append(G.placa_nombre(340, 748, 360, C.CANDIDATOS[0]["nombre"], C.CANDIDATOS[0]["rol"],
                            alto=92, size_nombre=30))
    s.append(G.placa_nombre(740, 748, 360, C.CANDIDATOS[1]["nombre"], C.CANDIDATOS[1]["rol"],
                            alto=92, size_nombre=30))

    _cta(s, W/2, 900, 780, 128, seal_r=80)
    s.append(G.tira_tricolor(0, H-12, W, 12, horizontal=True))
    return W, H, "".join(s), "url(#gVerde)"


# ======================================================================
# 08 · HISTORIA REDES SOCIALES (vertical 1080 x 1920)
# ======================================================================
def historia_ig():
    W, H = 1080, 1920
    s = []
    s.append(G.fondo_foto(0, 0, W, H, C.F_VALLE,
                          scrim=("scrimArriba", "scrimAbajo"),
                          tinte=C.VERDE_OSC, tinte_op=0.20, vineta=True))
    _header(s, W, size=28, y=120)
    s.append(G.texto(W/2, 290, LEMA1, 100, fill=C.BLANCO, peso_extra=0.06, sombra=True))
    s.append(G.texto(W/2, 384, LEMA2, 80, fill=C.AMARILLO_CL, peso_extra=0.06, sombra=True))
    s.append(G.texto(W/2, 446, C.SUBLEMA, 40, fill=C.CREMA, italic=True, peso_extra=0.02, sombra=True))

    s.append(G.foto_circular(330, 700, 185, C.CANDIDATOS[0]))
    s.append(G.foto_circular(750, 700, 185, C.CANDIDATOS[1]))
    s.append(G.placa_nombre(330, 902, 384, C.CANDIDATOS[0]["nombre"], C.CANDIDATOS[0]["rol"],
                            alto=100, size_nombre=34))
    s.append(G.placa_nombre(750, 902, 384, C.CANDIDATOS[1]["nombre"], C.CANDIDATOS[1]["rol"],
                            alto=100, size_nombre=34))

    # propuestas
    top0 = 1070
    for i, p in enumerate(C.PROPUESTAS):
        top = top0 + i * 104
        s.append(f'<rect x="110" y="{top}" width="{W-220}" height="92" rx="20" '
                 f'fill="{C.BLANCO}" opacity="0.96" filter="url(#sombraSuave)"/>')
        s.append(G.icono(p["icono"], 178, top + 46, 42))
        s.append(G.texto(246, top + 42, p["titulo"], 32, fill=C.VERDE_OSC,
                         peso_extra=0.05, anchor="start"))
        s.append(G.texto(246, top + 76, p["texto"], 22, fill=C.CAFE_OSC,
                         anchor="start", weight="normal"))

    _cta(s, W/2, top0 + 5*104 + 18, 780, 150, seal_r=90)
    s.append(G.tira_tricolor(0, H-14, W, 14, horizontal=True))
    return W, H, "".join(s), "url(#gVerde)"
