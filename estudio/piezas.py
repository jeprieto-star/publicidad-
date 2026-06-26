# -*- coding: utf-8 -*-
"""
Piezas de la campaña — sistema "Tierra de Café".
Cada función devuelve (ancho, alto, contenido, fondo, seed).
"""
from . import marca as M
from . import svg as S


# ----------------------------------------------------------------------
# Cabecera reutilizable (banda espresso con topo + corporación + región)
# ----------------------------------------------------------------------
def _cabecera(W, h=148):
    s = [S.panel(0, 0, W, h, "url(#gEspresso)")]
    s.append(S.topo(0, 0, W, h, color=M.AMBAR, op=0.20, n=5, sw=2, seed=4))
    s.append(S.franja_granos(20, h-16, W-40, paso=42, r=6, color=M.AMBAR, op=0.20))
    s.append(S.texto(W/2, h*0.40, M.CORPORACION, h*0.165, fill=M.HUESO, font=M.COND,
                     weight="600", spacing=1.4, upper=True))
    s.append(S.texto(W/2, h*0.74, M.CONEXION, h*0.150,
                     fill=M.AMBAR_CL, font=M.COND, weight="500", spacing=1.6, upper=True))
    return "".join(s)


def _nombre(cx, y, cand, ancho=300):
    s = [S.texto(cx, y, cand["corto"], S.fit(cand["corto"], ancho, 40, 0.50),
                 fill=M.ESPRESSO, font=M.COND, weight="600")]
    s.append(S.cinta(cx, y+14, 168, 34, cand["rol"], fill="url(#gCereza)", size=17))
    return "".join(s)


# ======================================================================
# 1 · AFICHE PRINCIPAL
# ======================================================================
def afiche_principal():
    W, H = 1000, 1400
    s = [S.grano_textura(0, 0, W, H, 0.05)]
    s.append(_cabecera(W))
    # foto de cafetales (laderas) como banda superior
    s.append(S.foto(0, 148, W, 410, M.F_CAFETALES, velo="velAbajo"))
    s.append(S.texto(W/2, 206, "ELECCIONES CAFETERAS", 26, fill=M.HUESO, font=M.COND,
                     weight="500", spacing=4, upper=True, sombra=True))
    # retratos
    cy = 522
    S_left, S_right = 308, 692
    s.append(S.retrato_circular(S_left, cy, 138, M.CANDIDATOS[0]))
    s.append(S.retrato_circular(S_right, cy, 138, M.CANDIDATOS[1]))
    # grano-acento entre retratos
    s.append(S.grano(W/2, cy-6, 24, color=M.CEREZA, rot=18))
    s.append(S.grano(W/2-2, cy+30, 17, color=M.ESPRESSO, rot=-24))
    # nombres
    s.append(_nombre(S_left, 712, M.CANDIDATOS[0]))
    s.append(_nombre(S_right, 712, M.CANDIDATOS[1]))
    # LEMA
    s.append(S.texto(W/2, 884, M.LEMA_1, S.fit(M.LEMA_1, 940, 112, 0.50),
                     fill=M.CEREZA, font=M.DISPLAY, spacing=1))
    s.append(S.texto(W/2, 966, M.LEMA_2, S.fit(M.LEMA_2, 940, 92, 0.50),
                     fill=M.ESPRESSO, font=M.DISPLAY, spacing=1))
    s.append(S.texto(W/2, 1028, M.PROMESA, 38, fill=M.CEREZA_OSC, font=M.SERIF,
                     weight="500", italic=True))
    s.append(S.franja_granos(220, 1064, 560, paso=46, r=8, color=M.ESPRESSO, op=0.35))
    # CTA
    s.append(S.cta(W/2, 1104, 640, 150))
    # pie: conexión cafetera
    s.append(S.texto(W/2, 1344, M.CONEXION.upper(),
                     24, fill=M.ESPRESSO, font=M.COND, weight="600", spacing=2))
    return W, H, "".join(s), "url(#gCrema)", 7


# ======================================================================
# 2 · AFICHE DE PROPUESTAS
# ======================================================================
def afiche_propuestas():
    W, H = 1000, 1400
    s = [S.grano_textura(0, 0, W, H, 0.05)]
    s.append(_cabecera(W))
    s.append(S.texto(W/2, 222, "NUESTRAS", 38, fill=M.CEREZA, font=M.COND, weight="600",
                     spacing=6, upper=True))
    s.append(S.texto(W/2, 326, "PROPUESTAS", 92, fill=M.ESPRESSO, font=M.DISPLAY, spacing=2))
    s.append(S.regla_amb(W/2-90, 352, 180, 7))
    # filas
    y0 = 396
    rh = 150
    for i, p in enumerate(M.PROPUESTAS):
        y = y0 + i*rh
        if i % 2 == 0:
            s.append(S.panel(46, y-8, W-92, rh-16, M.HUESO, rx=22, sombra=True))
        else:
            s.append(S.panel(46, y-8, W-92, rh-16, M.CREMA_OSC, rx=22))
        cyr = y + (rh-16)/2 - 8
        s.append(S.icono(p["icono"], 132, cyr, 52))
        # número grande tenue
        s.append(S.texto(232, cyr+34, str(i+1), 96, fill=M.CEREZA, font=M.DISPLAY,
                         op=0.16, anchor="middle"))
        s.append(S.texto(286, cyr-10, p["titulo"], 38, fill=M.ESPRESSO, font=M.COND,
                         weight="600", anchor="start"))
        for j, ln in enumerate(S.wrap(p["texto"], 46)):
            s.append(S.texto(286, cyr+26+j*30, ln, 25, fill=M.TINTA, font=M.SANS,
                             anchor="start"))
    # franja foto recoleccion + lema abajo
    yf = y0 + len(M.PROPUESTAS)*rh + 6
    s.append(S.foto(0, yf, W, H-yf, M.F_RECOLECCION, pos="xMidYMid", velo="velArriba"))
    s.append(S.panel(0, yf, W, H-yf, "url(#velCereza)", op=0.0))
    s.append(S.texto(W/2, H-92, M.LEMA, S.fit(M.LEMA, 940, 52, 0.50), fill=M.HUESO,
                     font=M.DISPLAY, spacing=1, sombra=True))
    s.append(S.cinta(W/2, H-66, 360, 46, "VOTA PLANCHA N.º " + M.PLANCHA,
                     fill="url(#gCereza)", size=22))
    return W, H, "".join(s), "url(#gCrema)", 11


# ======================================================================
# 3 · PASACALLE  (banner horizontal)
# ======================================================================
def pasacalle():
    W, H = 2000, 500
    s = [S.panel(0, 0, W, H, "url(#gEspresso)")]
    s.append(S.topo(0, 0, W, H, color=M.AMBAR, op=0.16, n=6, sw=2.4, seed=5))
    s.append(S.grano_textura(0, 0, W, H, 0.05))
    # sello izquierda
    s.append(S.sello(250, H/2, 150))
    # retratos derecha
    s.append(S.retrato_circular(1620, H/2, 120, M.CANDIDATOS[0]))
    s.append(S.retrato_circular(1830, H/2, 120, M.CANDIDATOS[1]))
    s.append(S.texto(1620, 470, M.CANDIDATOS[0]["rol"], 22, fill=M.AMBAR_CL, font=M.COND,
                     weight="600", spacing=2, upper=True))
    s.append(S.texto(1830, 470, M.CANDIDATOS[1]["rol"], 22, fill=M.AMBAR_CL, font=M.COND,
                     weight="600", spacing=2, upper=True))
    # centro: lema
    cx = 920
    s.append(S.texto(cx, 150, "COMITÉ DE CAFETEROS DEL TOLIMA", 26, fill=M.AMBAR_CL,
                     font=M.COND, weight="500", spacing=3, upper=True))
    s.append(S.texto(cx, 250, M.LEMA_1, 96, fill=M.HUESO, font=M.DISPLAY, spacing=1))
    s.append(S.texto(cx, 338, M.LEMA_2, 78, fill=M.CEREZA_CL, font=M.DISPLAY, spacing=1))
    s.append(S.texto(cx, 408, M.CONEXION, 28, fill=M.HUESO,
                     font=M.COND, weight="500", spacing=2, upper=True))
    return W, H, "".join(s), "url(#gEspresso)", 5


# ======================================================================
# 4 · VALLA  (gran formato, lectura a distancia)
# ======================================================================
def valla():
    W, H = 2400, 900
    s = []
    # izquierda: foto nevado/cafetales con velo
    pw = 1360
    s.append(S.foto(0, 0, pw, H, M.F_CAFETALES, velo=["velIzq"]))
    s.append(S.panel(0, 0, pw, H, "url(#velAbajo)", op=0.0))
    s.append(S.texto(70, 150, "COMITÉ DE CAFETEROS DEL TOLIMA", 34, fill=M.HUESO,
                     font=M.COND, weight="600", spacing=2, anchor="start", upper=True,
                     sombra=True))
    s.append(S.texto(70, 360, M.LEMA_1, 150, fill=M.HUESO, font=M.DISPLAY, anchor="start",
                     sombra=True))
    s.append(S.texto(70, 500, M.LEMA_2, 118, fill=M.AMBAR_CL, font=M.DISPLAY,
                     anchor="start", sombra=True))
    s.append(S.texto(74, 588, M.PROMESA, 46, fill=M.HUESO, font=M.SERIF, italic=True,
                     anchor="start", sombra=True))
    s.append(S.texto(74, 700, M.CONEXION.upper(), 34,
                     fill=M.AMBAR_CL, font=M.COND, weight="600", spacing=2, anchor="start",
                     sombra=True))
    # derecha: panel espresso con retratos + sello + CTA
    px = pw
    s.append(S.panel(px, 0, W-px, H, "url(#gEspresso)"))
    s.append(S.topo(px, 0, W-px, H, color=M.AMBAR, op=0.14, n=5, sw=2.4, seed=2))
    s.append(S.retrato_circular(px+270, 250, 168, M.CANDIDATOS[0]))
    s.append(S.retrato_circular(px+730, 250, 168, M.CANDIDATOS[1]))
    s.append(S.texto(px+270, 470, M.CANDIDATOS[0]["corto"], 40, fill=M.HUESO, font=M.COND,
                     weight="600"))
    s.append(S.texto(px+730, 470, M.CANDIDATOS[1]["corto"], 40, fill=M.HUESO, font=M.COND,
                     weight="600"))
    s.append(S.cinta(px+270, 492, 180, 40, M.CANDIDATOS[0]["rol"], size=19))
    s.append(S.cinta(px+730, 492, 180, 40, M.CANDIDATOS[1]["rol"], size=19))
    s.append(S.cta(px+(W-px)/2, 640, 720, 170))
    return W, H, "".join(s), "url(#gEspresso)", 9


# ======================================================================
# 5 · VOLANTE  (candidatos + propuestas en una pieza)
# ======================================================================
def volante():
    W, H = 1000, 1400
    s = [S.grano_textura(0, 0, W, H, 0.05)]
    s.append(_cabecera(W, 132))
    # banda retratos sobre foto café
    s.append(S.foto(0, 132, W, 300, M.F_CAFE, velo="velAbajo"))
    s.append(S.retrato_circular(300, 312, 112, M.CANDIDATOS[0]))
    s.append(S.retrato_circular(700, 312, 112, M.CANDIDATOS[1]))
    s.append(S.sello(W/2, 300, 76))
    s.append(_nombre(300, 480, M.CANDIDATOS[0], 280))
    s.append(_nombre(700, 480, M.CANDIDATOS[1], 280))
    s.append(S.texto(W/2, 606, M.LEMA_1, 64, fill=M.CEREZA, font=M.DISPLAY))
    s.append(S.texto(W/2, 664, M.LEMA_2, 52, fill=M.ESPRESSO, font=M.DISPLAY))
    s.append(S.texto(W/2, 706, M.PROMESA, 30, fill=M.CEREZA_OSC, font=M.SERIF, italic=True))
    # propuestas compactas (2 columnas)
    y0 = 752
    rh = 116
    for i, p in enumerate(M.PROPUESTAS):
        col = i % 2
        row = i // 2
        x = 60 + col*470
        y = y0 + row*rh
        s.append(S.panel(x, y, 440, rh-14, M.HUESO if (i % 2 == 0) else M.CREMA_OSC,
                         rx=18, sombra=(i % 2 == 0)))
        s.append(S.icono(p["icono"], x+58, y+(rh-14)/2, 40))
        s.append(S.texto(x+108, y+40, p["titulo"], 28, fill=M.ESPRESSO, font=M.COND,
                         weight="600", anchor="start"))
        for j, ln in enumerate(S.wrap(p["texto"], 30)):
            s.append(S.texto(x+108, y+68+j*24, ln, 19, fill=M.TINTA, font=M.SANS,
                             anchor="start"))
    s.append(S.cta(W/2, 1240, 600, 130))
    return W, H, "".join(s), "url(#gCrema)", 7


# ======================================================================
# 6 · TARJETA  (9x5)
# ======================================================================
def tarjeta():
    W, H = 1050, 600
    s = [S.panel(0, 0, W, H, "url(#gEspresso)")]
    s.append(S.topo(0, 0, W, H, color=M.AMBAR, op=0.16, n=5, sw=2.2, seed=6))
    s.append(S.grano_textura(0, 0, W, H, 0.05))
    s.append(S.retrato_circular(180, 232, 120, M.CANDIDATOS[0]))
    s.append(S.retrato_circular(390, 232, 120, M.CANDIDATOS[1]))
    s.append(S.texto(180, 400, M.CANDIDATOS[0]["rol"], 22, fill=M.AMBAR_CL, font=M.COND,
                     weight="600", spacing=2, upper=True))
    s.append(S.texto(390, 400, M.CANDIDATOS[1]["rol"], 22, fill=M.AMBAR_CL, font=M.COND,
                     weight="600", spacing=2, upper=True))
    s.append(S.texto(180, 446, M.CANDIDATOS[0]["corto"], 26, fill=M.HUESO, font=M.COND,
                     weight="500"))
    s.append(S.texto(390, 446, M.CANDIDATOS[1]["corto"], 26, fill=M.HUESO, font=M.COND,
                     weight="500"))
    # derecha
    cxd = 760
    s.append(S.sello(cxd, 150, 96))
    s.append(S.texto(cxd, 300, M.LEMA_1, 52, fill=M.HUESO, font=M.DISPLAY))
    s.append(S.texto(cxd, 348, M.LEMA_2, 42, fill=M.CEREZA_CL, font=M.DISPLAY))
    s.append(S.texto(cxd, 392, M.PROMESA, 24, fill=M.AMBAR_CL, font=M.SERIF, italic=True))
    s.append(S.franja_granos(cxd-150, 430, 300, paso=40, r=7, color=M.AMBAR, op=0.5))
    s.append(S.texto(cxd, 486, M.CONEXION.upper(), 21, fill=M.HUESO, font=M.COND,
                     weight="600", spacing=1.2))
    s.append(S.texto(cxd, 520, M.TIERRA.upper(), 20, fill=M.AMBAR_CL, font=M.COND,
                     weight="500", spacing=4))
    return W, H, "".join(s), "url(#gEspresso)", 6


# ======================================================================
# 7 · POST REDES  (1080x1080)
# ======================================================================
def post_ig():
    W, H = 1080, 1080
    s = [S.foto(0, 0, W, H, M.F_CAFETALES, velo=["velArriba", "velAbajo"])]
    s.append(S.texto(W/2, 92, "COMITÉ DE CAFETEROS DEL TOLIMA", 24, fill=M.HUESO,
                     font=M.COND, weight="600", spacing=3, upper=True, sombra=True))
    s.append(S.texto(W/2, 132, M.CONEXION, 22, fill=M.AMBAR_CL,
                     font=M.COND, weight="500", spacing=2, upper=True, sombra=True))
    # retratos
    s.append(S.retrato_circular(370, 470, 158, M.CANDIDATOS[0]))
    s.append(S.retrato_circular(710, 470, 158, M.CANDIDATOS[1]))
    s.append(S.grano(W/2, 460, 26, color=M.CEREZA, rot=18))
    s.append(S.texto(370, 672, M.CANDIDATOS[0]["rol"], 24, fill=M.AMBAR_CL, font=M.COND,
                     weight="600", spacing=2, upper=True, sombra=True))
    s.append(S.texto(710, 672, M.CANDIDATOS[1]["rol"], 24, fill=M.AMBAR_CL, font=M.COND,
                     weight="600", spacing=2, upper=True, sombra=True))
    s.append(S.texto(W/2, 800, M.LEMA_1, 104, fill=M.HUESO, font=M.DISPLAY, sombra=True))
    s.append(S.texto(W/2, 884, M.LEMA_2, 80, fill=M.AMBAR_CL, font=M.DISPLAY, sombra=True))
    s.append(S.texto(W/2, 940, M.PROMESA, 34, fill=M.HUESO, font=M.SERIF, italic=True,
                     sombra=True))
    s.append(S.cinta(W/2, 982, 380, 60, "VOTA PLANCHA N.º " + M.PLANCHA,
                     fill="url(#gCereza)", size=28))
    return W, H, "".join(s), "url(#gEspresso)", 5


# ======================================================================
# 8 · HISTORIA REDES  (1080x1920)
# ======================================================================
def historia_ig():
    W, H = 1080, 1920
    s = [S.foto(0, 0, W, H, M.F_RECOLECCION, velo=["velArriba", "velAbajo"])]
    s.append(S.texto(W/2, 150, "COMITÉ DE CAFETEROS DEL TOLIMA", 26, fill=M.HUESO,
                     font=M.COND, weight="600", spacing=3, upper=True, sombra=True))
    s.append(S.texto(W/2, 196, M.CONEXION, 24, fill=M.AMBAR_CL,
                     font=M.COND, weight="500", spacing=2, upper=True, sombra=True))
    s.append(S.sello(W/2, 470, 150))
    s.append(S.retrato_circular(330, 880, 168, M.CANDIDATOS[0]))
    s.append(S.retrato_circular(750, 880, 168, M.CANDIDATOS[1]))
    s.append(S.texto(330, 1098, M.CANDIDATOS[0]["corto"], 38, fill=M.HUESO, font=M.COND,
                     weight="600", sombra=True))
    s.append(S.texto(750, 1098, M.CANDIDATOS[1]["corto"], 38, fill=M.HUESO, font=M.COND,
                     weight="600", sombra=True))
    s.append(S.cinta(330, 1120, 200, 44, M.CANDIDATOS[0]["rol"], size=21))
    s.append(S.cinta(750, 1120, 200, 44, M.CANDIDATOS[1]["rol"], size=21))
    s.append(S.texto(W/2, 1340, M.LEMA_1, 132, fill=M.HUESO, font=M.DISPLAY, sombra=True))
    s.append(S.texto(W/2, 1452, M.LEMA_2, 104, fill=M.AMBAR_CL, font=M.DISPLAY, sombra=True))
    s.append(S.texto(W/2, 1524, M.PROMESA, 44, fill=M.HUESO, font=M.SERIF, italic=True,
                     sombra=True))
    s.append(S.cta(W/2, 1620, 720, 180))
    return W, H, "".join(s), "url(#gEspresso)", 8


# ======================================================================
# 9 · SELLO / LOGOTIPO  (insignia suelta, fondo transparente)
# ======================================================================
def sello_marca():
    W, H = 900, 900
    cx, cy, R = W/2, H/2, 360
    s = [f'<g filter="url(#sh_card)"><circle cx="{cx}" cy="{cy}" r="{R}" fill="url(#gCereza)"/></g>']
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{R*0.9:.0f}" fill="none" stroke="{M.AMBAR}" stroke-width="10"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{R*0.82:.0f}" fill="none" stroke="{M.AMBAR}" stroke-width="3" opacity="0.55"/>')
    rUp = R*0.72
    s.append(f'<defs><path id="arcUp" d="M{cx-rUp:.0f},{cy} A{rUp:.0f},{rUp:.0f} 0 0 1 {cx+rUp:.0f},{cy}"/>'
             f'<path id="arcDn" d="M{cx-rUp:.0f},{cy} A{rUp:.0f},{rUp:.0f} 0 0 0 {cx+rUp:.0f},{cy}"/></defs>')
    s.append(f'<text font-family="{M.COND}" font-weight="600" font-size="39" fill="{M.AMBAR_CL}" '
             f'letter-spacing="2.5"><textPath href="#arcUp" startOffset="50%" text-anchor="middle">'
             f'COMPROMETIDOS CON LOS CAFETEROS</textPath></text>')
    s.append(f'<text font-family="{M.COND}" font-weight="600" font-size="38" fill="{M.AMBAR_CL}" '
             f'letter-spacing="5"><textPath href="#arcDn" startOffset="50%" text-anchor="middle">'
             f'FAMILIAS CAFETERAS</textPath></text>')
    s.append(S.texto(cx, cy-150, "PLANCHA", 50, fill=M.HUESO, font=M.COND, weight="600",
                     spacing=10, upper=True))
    s.append(S.grano(cx-178, cy+34, 34, color=M.ESPRESSO, rot=20))
    s.append(S.grano(cx+178, cy+34, 34, color=M.ESPRESSO, rot=-20))
    s.append(S.texto(cx, cy+148, M.PLANCHA, 300, fill=M.HUESO, font=M.DISPLAY))
    return W, H, "".join(s), "none", 3
