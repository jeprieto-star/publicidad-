# -*- coding: utf-8 -*-
"""
Definición de cada pieza publicitaria.
Cada función devuelve (ancho, alto, contenido_svg, fondo).
"""
from . import config as C
from . import grafismos as G


def _municipios_linea():
    return "  •  ".join(C.MUNICIPIOS) + "  —  " + C.REGION_TITULO


# ======================================================================
# AFICHE PRINCIPAL (vertical 50x70 cm  -> 1000 x 1400)
# ======================================================================
def afiche_principal():
    W, H = 1000, 1400
    s = []

    # --- decoración de fondo ---
    s.append(G.sol(140, 165, 60))
    s.append(G.montanas(W, H, alto=210))
    s.append(G.rama_cafe(95, H + 10, escala=0.62, rot=-10))
    s.append(G.rama_cafe(W - 95, H + 10, escala=0.62, rot=10, espejo=True))

    # --- franja superior tricolor + corporación ---
    s.append(G.tira_tricolor(0, 0, W, 16, horizontal=True))
    s.append(G.texto(W/2, 70, C.CORPORACION.upper(), 26, fill=C.CAFE, peso_extra=0.05, spacing=2))
    s.append(f'<line x1="{W*0.22}" y1="86" x2="{W*0.78}" y2="86" stroke="{C.AMARILLO}" stroke-width="3"/>')

    # --- lema principal ---
    s.append(G.texto(W/2, 178, "COMPROMETIDOS", 84, fill=C.VERDE_OSC, peso_extra=0.06))
    s.append(G.texto(W/2, 262, "CON LOS CAFETEROS", 70, fill=C.CAFE_OSC, peso_extra=0.06))
    s.append(G.texto(W/2, 320, C.SUBLEMA, 36, fill=C.ROJO, peso_extra=0.04, italic=True))

    # --- fotos de candidatos ---
    fy, fh, fw = 372, 462, 380
    s.append(G.foto_candidato(80, fy, fw, fh, C.CANDIDATOS[0]))
    s.append(G.foto_candidato(540, fy, fw, fh, C.CANDIDATOS[1]))
    s.append(G.placa_nombre(80 + fw/2, fy + fh + 18, fw, C.CANDIDATOS[0]["nombre"], "CANDIDATO " + C.CANDIDATOS[0]["rol"]))
    s.append(G.placa_nombre(540 + fw/2, fy + fh + 18, fw, C.CANDIDATOS[1]["nombre"], "CANDIDATO " + C.CANDIDATOS[1]["rol"]))

    # --- banner de llamado a votar ---
    by = 1010
    s.append(f'<rect x="120" y="{by}" width="{W-240}" height="150" rx="30" fill="url(#gRojo)" filter="url(#sombra)"/>')
    s.append(G.sello_plancha(212, by + 75, 90))
    s.append(G.texto(575, by + 64, "VOTA", 46, fill=C.AMARILLO_CL, peso_extra=0.05, anchor="middle"))
    s.append(G.texto(575, by + 122, "PLANCHA N.º " + C.PLANCHA, 60, fill=C.BLANCO, peso_extra=0.06, anchor="middle"))

    # --- municipios ---
    s.append(f'<rect x="220" y="1200" width="{W-440}" height="58" rx="29" fill="{C.BLANCO}" opacity="0.92" filter="url(#sombraSuave)"/>')
    s.append(G.texto(W/2, 1238, _municipios_linea(), 28, fill=C.VERDE_OSC, peso_extra=0.05))

    return W, H, "".join(s), "url(#gCielo)"



def _encabezado(s, W, titulo, color_titulo=None):
    """Franja superior tricolor + corporación + título de sección."""
    color_titulo = color_titulo or C.VERDE_OSC
    s.append(G.tira_tricolor(0, 0, W, 16, horizontal=True))
    s.append(G.texto(W/2, 64, C.CORPORACION.upper(), 24, fill=C.CAFE, peso_extra=0.05, spacing=2))
    s.append(f'<line x1="{W*0.24}" y1="80" x2="{W*0.76}" y2="80" stroke="{C.AMARILLO}" stroke-width="3"/>')
    s.append(G.texto(W/2, 150, titulo, 72, fill=color_titulo, peso_extra=0.06))


# ======================================================================
# AFICHE DE PROPUESTAS (vertical 1000 x 1400)
# ======================================================================
def afiche_propuestas():
    W, H = 1000, 1400
    s = []
    s.append(G.montanas(W, H, alto=170))
    s.append(G.rama_cafe(70, H + 20, escala=0.5, rot=-8))
    s.append(G.rama_cafe(W - 70, H + 20, escala=0.5, rot=8, espejo=True))

    _encabezado(s, W, "NUESTRAS PROPUESTAS")
    s.append(G.texto(W/2, 196, C.LEMA, 34, fill=C.ROJO, peso_extra=0.05))

    # filas de propuestas
    top0, alto_card, gap = 236, 176, 12
    for i, p in enumerate(C.PROPUESTAS):
        top = top0 + i * (alto_card + gap)
        fill_card = C.BLANCO if i % 2 == 0 else "#FFFDF6"
        s.append(f'<rect x="64" y="{top}" width="{W-128}" height="{alto_card}" rx="26" '
                 f'fill="{fill_card}" filter="url(#sombraSuave)"/>')
        s.append(f'<rect x="64" y="{top}" width="14" height="{alto_card}" rx="7" fill="url(#gRojo)"/>')
        cy = top + alto_card / 2
        s.append(G.icono(p["icono"], 168, cy, 66))
        s.append(G.texto(270, top + 60, p["titulo"], 40, fill=C.VERDE_OSC, peso_extra=0.05, anchor="start"))
        lineas = G.wrap(p["texto"], 40)
        for j, ln in enumerate(lineas[:2]):
            s.append(G.texto(270, top + 104 + j * 38, ln, 29, fill=C.CAFE_OSC, peso_extra=0.02, anchor="start", weight="normal"))

    # pie con sello + municipios
    s.append(f'<rect x="250" y="1252" width="{W-290}" height="120" rx="26" fill="{C.BLANCO}" opacity="0.94" filter="url(#sombra)"/>')
    s.append(G.sello_plancha(150, 1312, 80))
    s.append(G.texto(600, 1302, C.LLAMADO, 50, fill=C.ROJO_OSC, peso_extra=0.06))
    s.append(G.texto(600, 1352, _municipios_linea(), 25, fill=C.VERDE_OSC, peso_extra=0.04))
    return W, H, "".join(s), "url(#gCielo)"


# ======================================================================
# PASACALLE (horizontal 2000 x 500)
# ======================================================================
def pasacalle():
    W, H = 2000, 500
    s = []
    s.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#gVerde)"/>')
    # textura de granos sutil
    s.append(G.tira_tricolor(0, 0, W, 14, horizontal=True))
    s.append(G.tira_tricolor(0, H - 14, W, 14, horizontal=True))
    s.append(G.rama_cafe(40, H + 30, escala=0.5, rot=-90))

    # fotos de candidatos (circulares) a la izquierda
    s.append(G.foto_circular(195, 235, 135, C.CANDIDATOS[0]))
    s.append(G.foto_circular(485, 235, 135, C.CANDIDATOS[1]))

    # lema central
    s.append(G.texto(660, 200, "COMPROMETIDOS", 94, fill=C.BLANCO, peso_extra=0.06, anchor="start"))
    s.append(G.texto(660, 298, "CON LOS CAFETEROS", 84, fill=C.AMARILLO_CL, peso_extra=0.06, anchor="start"))
    s.append(G.texto(662, 360, C.SUBLEMA, 32, fill=C.CREMA, peso_extra=0.03, anchor="start", italic=True))
    s.append(G.texto(662, 410, _municipios_linea(), 30, fill=C.AMARILLO_CL, peso_extra=0.03, anchor="start"))

    # sello plancha grande a la derecha
    s.append(G.sello_plancha_grande(1800, 250, 162))
    return W, H, "".join(s), "url(#gVerde)"


# ======================================================================
# VALLA / VAYA (gran formato horizontal 2400 x 900, ratio 8:3)
# ======================================================================
def valla():
    W, H = 2400, 900
    s = []
    s.append(G.sol(180, 180, 90))
    s.append(G.montanas(W, H, alto=300))
    s.append(G.rama_cafe(90, H + 20, escala=0.7, rot=-8))
    s.append(G.rama_cafe(W - 90, H + 20, escala=0.7, rot=8, espejo=True))
    s.append(G.tira_tricolor(0, 0, W, 18, horizontal=True))
    s.append(G.texto(W/2, 78, C.CORPORACION.upper(), 30, fill=C.CAFE, peso_extra=0.05, spacing=3))

    # fotos
    fy, fh, fw = 150, 470, 360
    s.append(G.foto_candidato(120, fy, fw, fh, C.CANDIDATOS[0]))
    s.append(G.foto_candidato(120 + fw + 40, fy, fw, fh, C.CANDIDATOS[1]))
    s.append(G.placa_nombre(120 + fw/2, fy + fh + 16, fw, C.CANDIDATOS[0]["nombre"], "PRINCIPAL", alto=106, size_nombre=40))
    s.append(G.placa_nombre(120 + fw + 40 + fw/2, fy + fh + 16, fw, C.CANDIDATOS[1]["nombre"], "SUPLENTE", alto=106, size_nombre=40))

    # lema (autoajustado al espacio entre fotos y sello)
    lx = 955
    lema_w = 950
    s1 = G.ajustar_size("COMPROMETIDOS", lema_w, 124, factor=0.70)
    s2 = G.ajustar_size("CON LOS CAFETEROS", lema_w, 104, factor=0.70)
    s.append(G.texto(lx, 250, "COMPROMETIDOS", s1, fill=C.VERDE_OSC, peso_extra=0.06, anchor="start"))
    s.append(G.texto(lx, 366, "CON LOS CAFETEROS", s2, fill=C.CAFE_OSC, peso_extra=0.06, anchor="start"))
    s.append(G.texto(lx + 4, 440, C.SUBLEMA, 52, fill=C.ROJO, peso_extra=0.04, anchor="start", italic=True))

    # sello plancha grande
    s.append(G.sello_plancha_grande(2155, 295, 182))

    # banda inferior: municipios + llamado
    s.append(f'<rect x="{lx-4}" y="528" width="940" height="92" rx="46" fill="url(#gRojo)" filter="url(#sombra)"/>')
    s.append(G.texto(lx + 466, 588, C.LLAMADO, 58, fill=C.BLANCO, peso_extra=0.06))
    s.append(G.texto(lx + 466, 688, _municipios_linea(), 38, fill=C.VERDE_OSC, peso_extra=0.05, anchor="middle"))
    return W, H, "".join(s), "url(#gCielo)"


# ======================================================================
# VOLANTE (vertical 1000 x 1400) - foto + propuestas compactas + CTA
# ======================================================================
def volante():
    W, H = 1000, 1400
    s = []
    s.append(G.montanas(W, H, alto=150))
    s.append(G.tira_tricolor(0, 0, W, 16, horizontal=True))
    s.append(G.texto(W/2, 60, C.CORPORACION.upper(), 22, fill=C.CAFE, peso_extra=0.05, spacing=2))
    s.append(G.texto(W/2, 138, "COMPROMETIDOS", 70, fill=C.VERDE_OSC, peso_extra=0.06))
    s.append(G.texto(W/2, 206, "CON LOS CAFETEROS", 58, fill=C.CAFE_OSC, peso_extra=0.06))

    # fotos circulares
    s.append(G.foto_circular(330, 380, 130, C.CANDIDATOS[0]))
    s.append(G.foto_circular(670, 380, 130, C.CANDIDATOS[1]))
    s.append(G.texto(330, 545, C.CANDIDATOS[0]["rol"], 30, fill=C.ROJO_OSC, peso_extra=0.05))
    s.append(G.texto(670, 545, C.CANDIDATOS[1]["rol"], 30, fill=C.ROJO_OSC, peso_extra=0.05))

    # propuestas (lista compacta con iconos pequeños)
    s.append(G.texto(W/2, 630, "NUESTRAS PROPUESTAS", 40, fill=C.VERDE_OSC, peso_extra=0.05))
    top0 = 668
    for i, p in enumerate(C.PROPUESTAS):
        top = top0 + i * 96
        s.append(f'<rect x="90" y="{top}" width="{W-180}" height="84" rx="18" fill="{C.BLANCO}" filter="url(#sombraSuave)"/>')
        s.append(G.icono(p["icono"], 150, top + 42, 38))
        s.append(G.texto(214, top + 38, p["titulo"], 30, fill=C.VERDE_OSC, peso_extra=0.05, anchor="start"))
        s.append(G.texto(214, top + 70, p["texto"], 22, fill=C.CAFE_OSC, anchor="start", weight="normal"))

    # CTA
    by = top0 + 5 * 96 + 6
    s.append(f'<rect x="120" y="{by}" width="{W-240}" height="120" rx="26" fill="url(#gRojo)" filter="url(#sombra)"/>')
    s.append(G.sello_plancha(210, by + 60, 74))
    s.append(G.texto(590, by + 50, C.LLAMADO, 46, fill=C.BLANCO, peso_extra=0.06))
    s.append(G.texto(590, by + 95, _municipios_linea(), 20, fill=C.AMARILLO_CL, peso_extra=0.03))
    return W, H, "".join(s), "url(#gCielo)"


# ======================================================================
# TARJETA DE PRESENTACIÓN (9x5 cm -> 1050 x 600)
# ======================================================================
def tarjeta():
    W, H = 1050, 600
    s = []
    s.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#gCielo)"/>')
    s.append(G.rama_cafe(58, H + 30, escala=0.40, rot=-10))
    s.append(G.tira_tricolor(0, 0, W, 12, horizontal=True))
    s.append(G.tira_tricolor(0, H - 12, W, 12, horizontal=True))
    s.append(G.texto(W/2, 50, C.CORPORACION.upper(), 19, fill=C.CAFE, peso_extra=0.04, spacing=1))

    # zona izquierda: fotos + nombres
    cx1, cx2, cy, r = 170, 398, 280, 84
    s.append(G.foto_circular(cx1, cy, r, C.CANDIDATOS[0]))
    s.append(G.foto_circular(cx2, cy, r, C.CANDIDATOS[1]))
    for cxn, cand in ((cx1, C.CANDIDATOS[0]), (cx2, C.CANDIDATOS[1])):
        lineas = G.nombre_lineas(cand["nombre"])
        sn = G.ajustar_size(max(lineas, key=len), 220, 21, factor=0.60)
        yb = cy + r + 36
        for j, ln in enumerate(lineas[:2]):
            s.append(G.texto(cxn, yb + j * (sn + 4), ln, sn, fill=C.NEGRO, peso_extra=0.04))
        s.append(G.texto(cxn, yb + len(lineas[:2]) * (sn + 4) + 12, cand["rol"], 15, fill=C.ROJO_OSC, peso_extra=0.03, spacing=1))

    # zona derecha: lema + plancha + región
    cxd = 770
    s1 = G.ajustar_size("COMPROMETIDOS", 470, 48, factor=0.62)
    s2 = G.ajustar_size("CON LOS CAFETEROS", 470, 40, factor=0.62)
    s.append(G.texto(cxd, 168, "COMPROMETIDOS", s1, fill=C.VERDE_OSC, peso_extra=0.06))
    s.append(G.texto(cxd, 214, "CON LOS CAFETEROS", s2, fill=C.CAFE_OSC, peso_extra=0.06))
    s.append(G.texto(cxd, 258, C.SUBLEMA, 24, fill=C.ROJO, italic=True, peso_extra=0.03))

    s.append(G.sello_plancha(605, 410, 70))
    s.append(G.texto(700, 392, "VOTA", 26, fill=C.ROJO_OSC, peso_extra=0.05, anchor="start"))
    s.append(G.texto(700, 440, "PLANCHA N.º " + C.PLANCHA, 38, fill=C.ROJO_OSC, peso_extra=0.05, anchor="start"))
    s.append(G.texto(cxd, 520, "  •  ".join(C.MUNICIPIOS), 22, fill=C.VERDE_OSC, peso_extra=0.04))
    s.append(G.texto(cxd, 550, C.REGION_TITULO + ", Colombia", 18, fill=C.CAFE, peso_extra=0.03))
    return W, H, "".join(s), "url(#gCielo)"


# ======================================================================
# POST REDES SOCIALES (cuadrado 1080 x 1080)
# ======================================================================
def post_ig():
    W, H = 1080, 1080
    s = []
    s.append(G.sol(120, 130, 64))
    s.append(G.montanas(W, H, alto=150))
    s.append(G.rama_cafe(60, H + 20, escala=0.5, rot=-8))
    s.append(G.rama_cafe(W - 60, H + 20, escala=0.5, rot=8, espejo=True))
    s.append(G.tira_tricolor(0, 0, W, 14, horizontal=True))
    s.append(G.texto(W/2, 70, C.CORPORACION.upper(), 24, fill=C.CAFE, peso_extra=0.05, spacing=2))
    s.append(G.texto(W/2, 168, "COMPROMETIDOS", 84, fill=C.VERDE_OSC, peso_extra=0.06))
    s.append(G.texto(W/2, 246, "CON LOS CAFETEROS", 70, fill=C.CAFE_OSC, peso_extra=0.06))
    s.append(G.texto(W/2, 300, C.SUBLEMA, 34, fill=C.ROJO, italic=True, peso_extra=0.04))

    s.append(G.foto_circular(340, 540, 170, C.CANDIDATOS[0]))
    s.append(G.foto_circular(740, 540, 170, C.CANDIDATOS[1]))
    s.append(G.texto(340, 745, C.CANDIDATOS[0]["rol"], 30, fill=C.ROJO_OSC, peso_extra=0.05))
    s.append(G.texto(740, 745, C.CANDIDATOS[1]["rol"], 30, fill=C.ROJO_OSC, peso_extra=0.05))

    by = 820
    s.append(f'<rect x="150" y="{by}" width="{W-300}" height="130" rx="28" fill="url(#gRojo)" filter="url(#sombra)"/>')
    s.append(G.sello_plancha(245, by + 65, 78))
    s.append(G.texto(635, by + 56, C.LLAMADO, 48, fill=C.BLANCO, peso_extra=0.06))
    s.append(G.texto(635, by + 102, _municipios_linea(), 21, fill=C.AMARILLO_CL, peso_extra=0.03))
    return W, H, "".join(s), "url(#gCielo)"


# ======================================================================
# HISTORIA REDES SOCIALES (vertical 1080 x 1920)
# ======================================================================
def historia_ig():
    W, H = 1080, 1920
    s = []
    s.append(G.sol(150, 220, 80))
    s.append(G.montanas(W, H, alto=240))
    s.append(G.rama_cafe(80, H + 20, escala=0.7, rot=-8))
    s.append(G.rama_cafe(W - 80, H + 20, escala=0.7, rot=8, espejo=True))
    s.append(G.tira_tricolor(0, 0, W, 18, horizontal=True))
    s.append(G.texto(W/2, 130, C.CORPORACION.upper(), 28, fill=C.CAFE, peso_extra=0.05, spacing=2))

    s.append(G.texto(W/2, 280, "COMPROMETIDOS", 96, fill=C.VERDE_OSC, peso_extra=0.06))
    s.append(G.texto(W/2, 372, "CON LOS CAFETEROS", 80, fill=C.CAFE_OSC, peso_extra=0.06))
    s.append(G.texto(W/2, 436, C.SUBLEMA, 40, fill=C.ROJO, italic=True, peso_extra=0.04))

    s.append(G.foto_circular(330, 700, 190, C.CANDIDATOS[0]))
    s.append(G.foto_circular(750, 700, 190, C.CANDIDATOS[1]))
    s.append(G.placa_nombre(330, 905, 380, C.CANDIDATOS[0]["nombre"], "PRINCIPAL", alto=104, size_nombre=38))
    s.append(G.placa_nombre(750, 905, 380, C.CANDIDATOS[1]["nombre"], "SUPLENTE", alto=104, size_nombre=38))

    # propuestas
    top0 = 1060
    for i, p in enumerate(C.PROPUESTAS):
        top = top0 + i * 104
        s.append(f'<rect x="110" y="{top}" width="{W-220}" height="92" rx="20" fill="{C.BLANCO}" filter="url(#sombraSuave)"/>')
        s.append(G.icono(p["icono"], 178, top + 46, 42))
        s.append(G.texto(246, top + 42, p["titulo"], 32, fill=C.VERDE_OSC, peso_extra=0.05, anchor="start"))
        s.append(G.texto(246, top + 76, p["texto"], 23, fill=C.CAFE_OSC, anchor="start", weight="normal"))

    by = top0 + 5 * 104 + 16
    s.append(f'<rect x="150" y="{by}" width="{W-300}" height="150" rx="30" fill="url(#gRojo)" filter="url(#sombra)"/>')
    s.append(G.sello_plancha(255, by + 75, 88))
    s.append(G.texto(655, by + 64, C.LLAMADO, 54, fill=C.BLANCO, peso_extra=0.06))
    s.append(G.texto(655, by + 116, _municipios_linea(), 22, fill=C.AMARILLO_CL, peso_extra=0.03))
    return W, H, "".join(s), "url(#gCielo)"
