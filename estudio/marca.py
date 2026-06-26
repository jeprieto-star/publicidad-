# -*- coding: utf-8 -*-
"""
MARCA — Propuesta NUEVA "Tierra de Café"
========================================
Dirección de arte completamente distinta a la versión anterior:

  · Sistema cálido y potente (no el verde editorial sobrio anterior).
  · Paleta cereza de café + espresso + crema + ámbar.
  · Tipografía de cartel: Anton (titulares), Oswald (rótulos),
    Fraunces (acentos con carácter), Noto Sans (cuerpo).
  · La FOTOGRAFÍA REAL del café es protagonista: los cafetales, la
    recolección, el grano maduro y las manos campesinas.
  · Recurso gráfico de marca: sello con el número 2, grano de café
    estilizado y líneas topográficas de la cordillera.

Todo lo editable de la campaña vive aquí.
"""

# ----------------------------------------------------------------------
# DATOS
# ----------------------------------------------------------------------
PLANCHA = "2"
CORPORACION = "Comité Departamental de Cafeteros del Tolima"

# Mensaje de conexión con las familias que siembran café
# (sin municipios ni zonas específicas de territorio)
CONEXION = "Por las familias que siembran café"
CONEXION_CORTA = "Con quienes siembran el café"
TIERRA = "Tierra de café"

LEMA_1 = "COMPROMETIDOS"
LEMA_2 = "CON LOS CAFETEROS"
LEMA = "COMPROMETIDOS CON LOS CAFETEROS"
PROMESA = "Por unos cafeteros prósperos"          # acento serif
LLAMADO = "VOTA PLANCHA"

CANDIDATOS = [
    {
        "nombre": "Jhon Esneider Prieto Prieto",
        "corto": "Jhon E. Prieto",
        "rol": "PRINCIPAL",
        "recorte": "assets/recortes/jhon-esneider-prieto.png",
    },
    {
        "nombre": "Nelson Ferned Orozco Castaño",
        "corto": "Nelson F. Orozco",
        "rol": "SUPLENTE",
        "recorte": "assets/recortes/nelson-ferned-orozco.png",
    },
]

# Propuestas: icono + título corto + texto
PROPUESTAS = [
    {"icono": "via",          "titulo": "Vías para la cosecha",
     "texto": "Buenas vías de comunicación para sacar el café de la montaña."},
    {"icono": "grano",        "titulo": "Renovación de café",
     "texto": "Buenos incentivos por la renovación de los cafetales."},
    {"icono": "beneficiadero","titulo": "Beneficiaderos",
     "texto": "Mejoramiento y construcción de beneficiaderos."},
    {"icono": "mujer",        "titulo": "Mujer cafetera",
     "texto": "Proyectos productivos para las mujeres del campo."},
    {"icono": "escudo",       "titulo": "Defensoría cafetera",
     "texto": "Defensa de los derechos del caficultor de la región."},
]

# ----------------------------------------------------------------------
# FOTOGRAFÍA DEL CAFÉ (real) — protagonista de las piezas
# ----------------------------------------------------------------------
F_RECOLECCION= "assets_v2/region/recoleccion.jpg"      # manos cosechando cereza
F_CAFETALES  = "assets_v2/region/cafetales.jpg"        # laderas de cafetales
F_CAFE       = "assets_v2/region/cafe.jpg"             # rama con cereza roja

# ----------------------------------------------------------------------
# PALETA — cálida, de tierra cafetera
# ----------------------------------------------------------------------
ESPRESSO   = "#241310"   # casi negro café (base oscura)
ESPRESSO_2 = "#3A2017"
CEREZA     = "#C5341E"   # rojo cereza de café (acento de marca)
CEREZA_OSC = "#9C2614"
CEREZA_CL  = "#E0573C"
AMBAR      = "#E7A12B"   # oro/ámbar
AMBAR_CL   = "#F6C45A"
CREMA      = "#F7EFE0"   # crema cálido (fondo claro)
CREMA_OSC  = "#ECDCC1"
ARENA      = "#E3CBA0"
HUESO      = "#FCF9F2"
VERDE      = "#2F5233"   # verde hoja de café (soporte)
VERDE_CL   = "#5C8559"
TINTA      = "#2A1A12"   # texto sobre claro
BLANCO     = "#FFFFFF"
NEGRO      = "#1A0F0A"

# ----------------------------------------------------------------------
# TIPOGRAFÍA (instaladas vía Fontsource -> ~/.fonts)
# ----------------------------------------------------------------------
DISPLAY = "Anton"        # titulares enormes, condensada
COND    = "Oswald"       # rótulos, nombres, números
SERIF   = "Fraunces"     # acentos con carácter (cursiva editorial)
SANS    = "Noto Sans"    # cuerpo
