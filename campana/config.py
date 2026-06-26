# -*- coding: utf-8 -*-
"""
Configuración central de la campaña.
================================================================
TODO lo editable de la campaña vive aquí. Cambia un nombre, una
propuesta o una foto en este archivo y vuelve a ejecutar
`python generar_campana.py` para regenerar TODAS las piezas.
================================================================
"""

# ----------------------------------------------------------------------
# DATOS DE LA CAMPAÑA
# ----------------------------------------------------------------------
PLANCHA = "2"
CORPORACION = "Comité Departamental de Cafeteros del Tolima"
CORPORACION_CORTA = "Comité Departamental de Cafeteros"
DEPARTAMENTO = "Tolima"
LEMA = "COMPROMETIDOS CON LOS CAFETEROS"
SUBLEMA = "Por unos cafeteros prósperos"
LLAMADO = "VOTA PLANCHA"

# ----------------------------------------------------------------------
# CANDIDATOS
#   foto     -> foto original (con fondo azul de estudio)
#   recorte  -> foto con el fondo removido (PNG transparente)
# ----------------------------------------------------------------------
CANDIDATOS = [
    {
        "nombre": "Jhon Esneider Prieto Prieto",
        "rol": "PRINCIPAL",
        "foto": "assets/jhon-esneider-prieto.jpg",
        "recorte": "assets/recortes/jhon-esneider-prieto.png",
    },
    {
        "nombre": "Nelson Ferned Orozco Castaño",
        "rol": "SUPLENTE",
        "foto": "assets/nelson-ferned-orozco.jpg",
        "recorte": "assets/recortes/nelson-ferned-orozco.png",
    },
]

# ----------------------------------------------------------------------
# PROPUESTAS (con icono identificador)
# ----------------------------------------------------------------------
PROPUESTAS = [
    {"icono": "via",          "titulo": "Buenas vías",        "texto": "Vías de comunicación para sacar la cosecha"},
    {"icono": "renovacion",   "titulo": "Renovación de café", "texto": "Buenos incentivos por renovación de café"},
    {"icono": "beneficiadero","titulo": "Beneficiaderos",     "texto": "Mejoramiento y construcción de beneficiaderos"},
    {"icono": "mujer",        "titulo": "Mujer cafetera",     "texto": "Proyectos productivos para las mujeres cafeteras"},
    {"icono": "defensoria",   "titulo": "Defensoría",         "texto": "Defensoría de los derechos de los cafeteros"},
]

# ----------------------------------------------------------------------
# FONDOS FOTOGRÁFICOS (paisaje andino / café — assets/fondos/)
# ----------------------------------------------------------------------
F_MONTANA   = "assets/fondos/montana-verde.jpg"
F_NEVADO    = "assets/fondos/nevado.jpg"
F_VALLE     = "assets/fondos/valle-amanecer.jpg"
F_VIA       = "assets/fondos/via-montana.jpg"
F_BOSQUE    = "assets/fondos/bosque-verde.jpg"
F_VERDE_AER = "assets/fondos/verde-aereo.jpg"
F_MONT_AZUL = "assets/fondos/montana-azul.jpg"
F_LAGO      = "assets/fondos/lago-andino.jpg"
F_GRANOS    = "assets/fondos/granos-cafe.png"
F_TAZA      = "assets/fondos/taza-cafe.jpg"

# ----------------------------------------------------------------------
# PALETA CAFETERA
# ----------------------------------------------------------------------
VERDE_OSC   = "#0E431F"
VERDE       = "#1E7A3D"
VERDE_CLARO = "#3FA34D"
CAFE_OSC    = "#2C1A0F"
CAFE        = "#6F4322"
CAFE_CLARO  = "#9C6B3F"
ROJO        = "#C1272D"
ROJO_OSC    = "#8E1B1F"
AMARILLO    = "#F2A900"
AMARILLO_CL = "#FFC42E"
CREMA       = "#FBF4E2"
CREMA_OSC   = "#F0E2C0"
BLANCO      = "#FFFFFF"
NEGRO       = "#1A1208"
AZUL_FOTO   = "#1CA3EC"   # tono del fondo azul de las fotos de estudio (respaldo)

# Tira tricolor (referencia al poncho / bandera) usada como acento
TRICOLOR = [AMARILLO, "#0B5BA6", ROJO]  # amarillo, azul, rojo

# ----------------------------------------------------------------------
# TIPOGRAFÍA (única disponible en el entorno)
# ----------------------------------------------------------------------
FUENTE = "Noto Sans"
