# -*- coding: utf-8 -*-
"""
Piezas publicitarias — sistema EDITORIAL de zonas.

Cada función devuelve (ancho, alto, contenido_svg, fondo).

Reglas de diseño:
  - Las fotografías van LIMPIAS, en su propia zona. No se lavan con color.
  - El texto vive en paneles de color sólido adyacentes, o sobre la foto con
    una sombra de texto (nunca con un tinte que cubra la imagen).
  - Paleta sobria (verde bosque, crema, oro apagado, terracota), aire y
    jerarquía tipográfica. Sin nombres de municipios (campaña de todo el Tolima).
"""
from . import config as C
from . import grafismos as G

LEMA1 = "COMPROMETIDOS"
LEMA2 = "CON LOS CAFETEROS"
TAGLINE = "Por el campo cafetero del Tolima"


# ----------------------------------------------------------------------
# Cabecera de marca (banda verde fina + corporación + acento tricolor)
# ----------------------------------------------------------------------
def _cabecera(s, W, h=94):
    s.append(G.panel(0, 0, W, h, "url(#gVerdeH)"))
    s.append(G.texto(W/2, h*0.46, C.CORPORACION, h*0.205, fill=C.HUESO,
                     peso_extra=0.015, spacing=1.5, upper=True))
    s.append(G.texto(W/2, h*0.80, f"PLANCHA N.º {C.PLANCHA}  ·  ELECCIONES CAFETERAS",
                     h*0.15, fill=C.ORO_CL, spacing=2, upper=True))
    s.append(G.regla_tricolor(W/2 - h*1.0, h - 7, h*2.0, h=5, gap=6))


def _pie(s, W, H, tono="verde"):
    s.append(G.regla_tricolor(0, H-8, W, h=8))


# ======================================================================
# 01 · AFICHE PRINCIPAL (1000 x 1400)
# ======================================================================
def afiche_principal():
    W, H = 1000, 1400
    s = []
    s.append(G.panel(0, 0, W, H, "url(#gCrema)"))
    _cabecera(s, W)

    # ---- foto de paisaje LIMPIA (hero) ----
    fy, fh = 94, 416
    s.append(G.foto(0, fy, W, fh, C.F_MONTANA, pos="xMidYMid"))
    s.append(G.regla_tricolor(0, fy + fh - 6, W, h=6))

    # ---- zona del lema (sobre crema, con aire) ----
    s.append(G.texto(W/2, 614, LEMA1, 90, fill=C.VERDE_OSC, peso_extra=0.02))
    s.append(G.texto(W/2, 688, LEMA2, 64, fill=C.TERRACOTA, peso_extra=0.02))
    s.append(G.filete(W/2-150, 716, W/2+150, 716, color=C.ORO, w=3))
    s.append(G.texto(W/2, 758, C.SUBLEMA, 31, fill=C.CAFE, italic=True))

    # ---- retratos enmarcados (fotos limpias) ----
    fw, fhr, ytop = 356, 300, 800
    cx1, cx2 = 288, 712
    s.append(G.marco_retrato(cx1 - fw/2, ytop, fw, fhr, C.CANDIDATOS[0]))
    s.append(G.marco_retrato(cx2 - fw/2, ytop, fw, fhr, C.CANDIDATOS[1]))
    s.append(G.nombre_bajo(cx1, ytop + fhr + 52, fw + 60, C.CANDIDATOS[0]["nombre"],
                           C.CANDIDATOS[0]["rol"], size=32))
    s.append(G.nombre_bajo(cx2, ytop + fhr + 52, fw + 60, C.CANDIDATOS[1]["nombre"],
                           C.CANDIDATOS[1]["rol"], size=32))

    # ---- llamado a votar ----
    s.append(G.cta(W/2, 1272, 720, 114, tono="terra", seal_r=72))
    _pie(s, W, H)
    return W, H, "".join(s), "url(#gCrema)"


# ======================================================================
# 02 · AFICHE DE PROPUESTAS (1000 x 1400)
# ======================================================================
def afiche_propuestas():
    W, H = 1000, 1400
    s = []
    s.append(G.panel(0, 0, W, H, "url(#gCrema)"))
    _cabecera(s, W)

    # título
    s.append(G.texto(W/2, 188, "NUESTRAS PROPUESTAS", 60, fill=C.VERDE_OSC, peso_extra=0.02))
    s.append(G.texto(W/2, 232, C.LEMA, 26, fill=C.CAFE, spacing=2, upper=True))

    # banda fotográfica limpia (granos de café) como acento temático
    by, bh = 262, 132
    s.append(G.foto(60, by, W-120, bh, C.F_GRANOS, pos="xMidYMid", rx=18,
                    borde=C.CREMA_OSC, borde_w=4))
    s.append(G.regla_tricolor(W/2 - 110, by + bh + 14, 220, h=5))

    # tarjetas de propuestas
    top0, alto, gap = by + bh + 44, 148, 14
    for i, p in enumerate(C.PROPUESTAS):
        top = top0 + i * (alto + gap)
        s.append(G.panel(60, top, W-120, alto, C.HUESO, rx=20, sombra=True))
        s.append(G.panel(60, top, 12, alto, "url(#gOro)", rx=6))
        cy = top + alto/2
        s.append(G.icono(p["icono"], 156, cy, 56))
        s.append(G.texto(250, top + 56, p["titulo"], 38, fill=C.VERDE_OSC,
                         peso_extra=0.02, anchor="start"))
        for j, ln in enumerate(G.wrap(p["texto"], 46)[:2]):
            s.append(G.texto(250, top + 98 + j*34, ln, 25, fill=C.TINTA,
                             anchor="start", weight="normal"))

    s.append(G.cta(W/2, top0 + 5*(alto+gap) + 8, 720, 108, tono="terra", seal_r=66))
    _pie(s, W, H)
    return W, H, "".join(s), "url(#gCrema)"


# ======================================================================
# 03 · PASACALLE (2000 x 500) horizontal
# ======================================================================
def pasacalle():
    W, H = 2000, 500
    s = []
    s.append(G.panel(0, 0, W, H, "url(#gCrema)"))

    # zona izquierda: panel verde con retratos circulares
    pw = 720
    s.append(G.panel(0, 0, pw, H, "url(#gVerdeH)"))
    s.append(G.regla_tricolor(0, 0, pw, h=10))
    s.append(G.regla_tricolor(0, H-10, pw, h=10))
    s.append(G.foto_circular(205, 250, 132, C.CANDIDATOS[0], borde=9))
    s.append(G.foto_circular(515, 250, 132, C.CANDIDATOS[1], borde=9))
    s.append(G.texto(205, 432, C.CANDIDATOS[0]["rol"], 26, fill=C.ORO_CL, peso_extra=0.03, spacing=2, upper=True))
    s.append(G.texto(515, 432, C.CANDIDATOS[1]["rol"], 26, fill=C.ORO_CL, peso_extra=0.03, spacing=2, upper=True))

    # zona central: lema
    cxm = (pw + 1660) / 2
    s.append(G.texto(cxm, 170, C.CORPORACION, 28, fill=C.CAFE, peso_extra=0.02, spacing=1.5, upper=True))
    s.append(G.texto(cxm, 270, LEMA1, 96, fill=C.VERDE_OSC, peso_extra=0.02))
    s.append(G.texto(cxm, 350, LEMA2, 70, fill=C.TERRACOTA, peso_extra=0.02))
    s.append(G.filete(cxm-180, 384, cxm+180, 384, color=C.ORO, w=3))
    s.append(G.texto(cxm, 428, C.SUBLEMA, 30, fill=C.CAFE, italic=True))

    # zona derecha: sello de plancha
    s.append(G.panel(1660, 0, W-1660, H, "url(#gVerde)"))
    s.append(G.regla_tricolor(1660, 0, W-1660, h=10))
    s.append(G.regla_tricolor(1660, H-10, W-1660, h=10))
    s.append(G.sello_plancha(1830, 250, 150, dominante=True, tono="terra"))
    return W, H, "".join(s), "url(#gCrema)"


# ======================================================================
# 04 · VALLA (2400 x 900) ~8:3
# ======================================================================
def valla():
    W, H = 2400, 900
    s = []
    s.append(G.panel(0, 0, W, H, "url(#gCrema)"))

    # ---- zona izquierda: panel verde con retratos enmarcados ----
    pw = 1020
    s.append(G.panel(0, 0, pw, H, "url(#gVerdeH)"))
    s.append(G.regla_tricolor(0, 0, pw, h=12))
    fw, fhr, ytop = 380, 500, 150
    cx1, cx2 = 300, 720
    s.append(G.marco_retrato(cx1 - fw/2, ytop, fw, fhr, C.CANDIDATOS[0]))
    s.append(G.marco_retrato(cx2 - fw/2, ytop, fw, fhr, C.CANDIDATOS[1]))
    s.append(G.nombre_bajo(cx1, ytop + fhr + 58, fw + 30, C.CANDIDATOS[0]["nombre"],
                           C.CANDIDATOS[0]["rol"], size=34, color=C.HUESO, color_rol=C.ORO_CL))
    s.append(G.nombre_bajo(cx2, ytop + fhr + 58, fw + 30, C.CANDIDATOS[1]["nombre"],
                           C.CANDIDATOS[1]["rol"], size=34, color=C.HUESO, color_rol=C.ORO_CL))

    # ---- zona derecha: foto de paisaje LIMPIA con lema (sombra de texto) ----
    rx0 = pw
    rw = W - pw
    s.append(G.foto(rx0, 0, rw, H, C.F_MONTANA, pos="xMidYMid", fade=("fadeArriba",)))
    s.append(G.regla_tricolor(rx0, 0, rw, h=12))
    lx = rx0 + 70
    lema_w = rw - 150
    s1 = G.ajustar_size(LEMA1, lema_w, 134, factor=0.64)
    s2 = G.ajustar_size(LEMA2, lema_w, 110, factor=0.64)
    s.append(G.texto(lx, 150, C.CORPORACION, 34, fill=C.HUESO, peso_extra=0.02,
                     anchor="start", spacing=1.5, sombra=True, upper=True))
    s.append(G.texto(lx, 312, LEMA1, s1, fill=C.HUESO, peso_extra=0.03, anchor="start", sombra=True))
    s.append(G.texto(lx, 312 + s1*0.94, LEMA2, s2, fill=C.ORO_CL, peso_extra=0.03, anchor="start", sombra=True))
    s.append(G.texto(lx + 4, 312 + s1*0.94 + s2*0.66, C.SUBLEMA, 46, fill=C.HUESO,
                     italic=True, anchor="start", sombra=True))

    # banda verde inferior: llamado a votar + sello grande (único sello)
    bandy = 700
    bh = H - bandy
    s.append(G.panel(rx0, bandy, rw, bh, "url(#gVerde)"))
    s.append(G.regla_tricolor(rx0, bandy, rw, h=8))
    sx = rx0 + rw - 160
    s.append(G.sello_plancha(sx, bandy + bh/2, 92, dominante=True, tono="terra"))
    vtx = (rx0 + 60 + (sx - 110)) / 2
    s.append(G.texto(vtx, bandy + bh*0.42, C.LLAMADO, 58, fill=C.ORO_CL, peso_extra=0.03, spacing=3, upper=True))
    s.append(G.texto(vtx, bandy + bh*0.80, "N.º " + C.PLANCHA, 80, fill=C.HUESO, peso_extra=0.03))
    return W, H, "".join(s), "url(#gCrema)"


# ======================================================================
# 05 · VOLANTE (1000 x 1400)
# ======================================================================
def volante():
    W, H = 1000, 1400
    s = []
    s.append(G.panel(0, 0, W, H, "url(#gCrema)"))
    _cabecera(s, W)

    # lema
    s.append(G.texto(W/2, 188, LEMA1, 74, fill=C.VERDE_OSC, peso_extra=0.02))
    s.append(G.texto(W/2, 248, LEMA2, 50, fill=C.TERRACOTA, peso_extra=0.02))
    s.append(G.texto(W/2, 292, C.SUBLEMA, 27, fill=C.CAFE, italic=True))

    # retratos circulares + nombres
    s.append(G.foto_circular(310, 432, 128, C.CANDIDATOS[0]))
    s.append(G.foto_circular(690, 432, 128, C.CANDIDATOS[1]))
    s.append(G.nombre_bajo(310, 612, 360, C.CANDIDATOS[0]["nombre"], C.CANDIDATOS[0]["rol"], size=28))
    s.append(G.nombre_bajo(690, 612, 360, C.CANDIDATOS[1]["nombre"], C.CANDIDATOS[1]["rol"], size=28))

    # propuestas compactas
    s.append(G.texto(W/2, 752, "NUESTRAS PROPUESTAS", 36, fill=C.VERDE_OSC, peso_extra=0.02))
    s.append(G.regla_tricolor(W/2-90, 768, 180, h=5))
    top0 = 800
    for i, p in enumerate(C.PROPUESTAS):
        top = top0 + i * 94
        s.append(G.panel(90, top, W-180, 82, C.HUESO, rx=16, sombra=True))
        s.append(G.panel(90, top, 9, 82, "url(#gOro)", rx=4))
        s.append(G.icono(p["icono"], 150, top + 41, 36))
        s.append(G.texto(212, top + 36, p["titulo"], 29, fill=C.VERDE_OSC, peso_extra=0.02, anchor="start"))
        s.append(G.texto(212, top + 66, p["texto"], 20, fill=C.TINTA, anchor="start", weight="normal"))

    s.append(G.cta(W/2, top0 + 5*94 + 10, 720, 108, tono="terra", seal_r=66))
    _pie(s, W, H)
    return W, H, "".join(s), "url(#gCrema)"


# ======================================================================
# 06 · TARJETA (1050 x 600)
# ======================================================================
def tarjeta():
    W, H = 1050, 600
    s = []
    s.append(G.panel(0, 0, W, H, "url(#gCrema)"))

    # panel izquierdo verde con retratos circulares
    pw = 440
    s.append(G.panel(0, 0, pw, H, "url(#gVerdeH)"))
    s.append(G.regla_tricolor(0, 0, pw, h=8))
    s.append(G.regla_tricolor(0, H-8, pw, h=8))
    cx1, cx2, cy, r = 148, 318, 210, 88
    s.append(G.foto_circular(cx1, cy, r, C.CANDIDATOS[0], borde=8))
    s.append(G.foto_circular(cx2, cy, r, C.CANDIDATOS[1], borde=8))
    for cxn, cand in ((cx1, C.CANDIDATOS[0]), (cx2, C.CANDIDATOS[1])):
        lineas = G.nombre_lineas(cand["nombre"])
        sn = G.ajustar_size(max(lineas, key=len), 196, 20, factor=0.56)
        yb = cy + r + 36
        for j, ln in enumerate(lineas[:2]):
            s.append(G.texto(cxn, yb + j*(sn+3), ln, sn, fill=C.HUESO, peso_extra=0.02))
        s.append(G.texto(cxn, yb + 2*(sn+3) + 8, cand["rol"], 14, fill=C.ORO_CL,
                         peso_extra=0.02, spacing=1, upper=True))

    # zona derecha: lema + plancha
    cxd = 745
    s.append(G.texto(cxd, 78, C.CORPORACION, 16, fill=C.CAFE, peso_extra=0.02, spacing=1, upper=True))
    s.append(G.filete(cxd-150, 98, cxd+150, 98, color=C.ORO, w=2))
    s1 = G.ajustar_size(LEMA1, 540, 52, factor=0.58)
    s.append(G.texto(cxd, 172, LEMA1, s1, fill=C.VERDE_OSC, peso_extra=0.02))
    s.append(G.texto(cxd, 222, LEMA2, 40, fill=C.TERRACOTA, peso_extra=0.02))
    s.append(G.texto(cxd, 262, C.SUBLEMA, 23, fill=C.CAFE, italic=True))

    s.append(G.sello_plancha(622, 410, 74, tono="terra"))
    s.append(G.texto(726, 392, C.LLAMADO, 30, fill=C.TERRA_OSC, peso_extra=0.02, anchor="start", spacing=1))
    s.append(G.texto(726, 446, "N.º " + C.PLANCHA, 50, fill=C.VERDE_OSC, peso_extra=0.02, anchor="start"))
    s.append(G.texto(cxd, 548, TAGLINE, 21, fill=C.VERDE_OSC, peso_extra=0.02))
    return W, H, "".join(s), "url(#gCrema)"


# ======================================================================
# 07 · POST REDES (1080 x 1080)
# ======================================================================
def post_ig():
    W, H = 1080, 1080
    s = []
    s.append(G.panel(0, 0, W, H, "url(#gCrema)"))

    # foto de paisaje LIMPIA en la mitad superior
    fh = 470
    s.append(G.foto(0, 0, W, fh, C.F_MONTANA, pos="xMidYMid", fade=("fadeArriba",)))
    s.append(G.texto(W/2, 70, C.CORPORACION, 24, fill=C.HUESO, peso_extra=0.02,
                     spacing=1.5, sombra=True, upper=True))
    s.append(G.texto(W/2, 196, LEMA1, 94, fill=C.HUESO, peso_extra=0.03, sombra=True))
    s.append(G.texto(W/2, 278, LEMA2, 66, fill=C.ORO_CL, peso_extra=0.03, sombra=True))
    s.append(G.regla_tricolor(0, fh-6, W, h=6))

    # retratos circulares montados sobre la costura
    s.append(G.foto_circular(346, fh, 162, C.CANDIDATOS[0]))
    s.append(G.foto_circular(734, fh, 162, C.CANDIDATOS[1]))
    s.append(G.nombre_bajo(346, fh + 220, 380, C.CANDIDATOS[0]["nombre"], C.CANDIDATOS[0]["rol"], size=30))
    s.append(G.nombre_bajo(734, fh + 220, 380, C.CANDIDATOS[1]["nombre"], C.CANDIDATOS[1]["rol"], size=30))

    s.append(G.cta(W/2, 902, 760, 122, tono="terra", seal_r=76))
    _pie(s, W, H)
    return W, H, "".join(s), "url(#gCrema)"


# ======================================================================
# 08 · HISTORIA REDES (1080 x 1920)
# ======================================================================
def historia_ig():
    W, H = 1080, 1920
    s = []
    s.append(G.panel(0, 0, W, H, "url(#gCrema)"))

    # foto de paisaje LIMPIA arriba
    fh = 600
    s.append(G.foto(0, 0, W, fh, C.F_VALLE, pos="xMidYMid", fade=("fadeArriba",)))
    s.append(G.texto(W/2, 120, C.CORPORACION, 26, fill=C.HUESO, peso_extra=0.02,
                     spacing=2, sombra=True, upper=True))
    s.append(G.texto(W/2, 290, LEMA1, 104, fill=C.HUESO, peso_extra=0.03, sombra=True))
    s.append(G.texto(W/2, 380, LEMA2, 74, fill=C.ORO_CL, peso_extra=0.03, sombra=True))
    s.append(G.texto(W/2, 444, C.SUBLEMA, 38, fill=C.HUESO, italic=True, sombra=True))
    s.append(G.regla_tricolor(0, fh-6, W, h=6))

    # retratos circulares montados sobre la costura
    ccy = 690
    s.append(G.foto_circular(338, ccy, 175, C.CANDIDATOS[0]))
    s.append(G.foto_circular(742, ccy, 175, C.CANDIDATOS[1]))
    s.append(G.nombre_bajo(338, ccy + 237, 400, C.CANDIDATOS[0]["nombre"], C.CANDIDATOS[0]["rol"], size=32))
    s.append(G.nombre_bajo(742, ccy + 237, 400, C.CANDIDATOS[1]["nombre"], C.CANDIDATOS[1]["rol"], size=32))

    # propuestas
    s.append(G.texto(W/2, 1078, "NUESTRAS PROPUESTAS", 38, fill=C.VERDE_OSC, peso_extra=0.02))
    s.append(G.regla_tricolor(W/2-95, 1094, 190, h=5))
    top0 = 1128
    for i, p in enumerate(C.PROPUESTAS):
        top = top0 + i * 104
        s.append(G.panel(110, top, W-220, 92, C.HUESO, rx=18, sombra=True))
        s.append(G.panel(110, top, 9, 92, "url(#gOro)", rx=4))
        s.append(G.icono(p["icono"], 176, top + 46, 40))
        s.append(G.texto(244, top + 42, p["titulo"], 31, fill=C.VERDE_OSC, peso_extra=0.02, anchor="start"))
        s.append(G.texto(244, top + 74, p["texto"], 21, fill=C.TINTA, anchor="start", weight="normal"))

    s.append(G.cta(W/2, top0 + 5*104 + 16, 780, 140, tono="terra", seal_r=86))
    _pie(s, W, H)
    return W, H, "".join(s), "url(#gCrema)"
