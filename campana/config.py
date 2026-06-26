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
LEMA = "COMPROMETIDOS CON LOS CAFETEROS"
SUBLEMA = "Por unos cafeteros prósperos"
LLAMADO = "VOTA PLANCHA N.º 2"

# Región / municipios
REGION_TITULO = "Norte del Tolima"
MUNICIPIOS = ["Líbano", "Villahermosa", "Casabianca"]

# ----------------------------------------------------------------------
# CANDIDATOS
# Reemplaza "nombre" por el nombre real y coloca la foto en assets/.
# Las fotos de los candidatos deben llamarse exactamente como el campo "foto".
# ----------------------------------------------------------------------
CANDIDATOS = [
    {
        "nombre": "NOMBRE CANDIDATO PRINCIPAL",
        "rol": "PRINCIPAL",
        "foto": "assets/candidato-1.png",   # reemplazar por la foto real
    },
    {
        "nombre": "NOMBRE CANDIDATO SUPLENTE",
        "rol": "SUPLENTE",
        "foto": "assets/candidato-2.png",   # reemplazar por la foto real
    },
]

# ----------------------------------------------------------------------
# PROPUESTAS (con icono identificador)
# ----------------------------------------------------------------------
PROPUESTAS = [
    {"icono": "via",          "titulo": "Buenas vías",            "texto": "Buenas vías de comunicación para sacar la cosecha"},
    {"icono": "renovacion",   "titulo": "Renovación de café",     "texto": "Buenos incentivos por renovación de café"},
    {"icono": "beneficiadero","titulo": "Beneficiaderos",         "texto": "Mejoramiento y construcción de beneficiaderos"},
    {"icono": "mujer",        "titulo": "Mujer cafetera",         "texto": "Proyectos productivos para las mujeres cafeteras"},
    {"icono": "defensoria",   "titulo": "Defensoría",             "texto": "La defensoría de los cafeteros"},
]

# ----------------------------------------------------------------------
# PALETA CAFETERA
# ----------------------------------------------------------------------
VERDE_OSC   = "#0F4D26"
VERDE       = "#1E7A3D"
VERDE_CLARO = "#3FA34D"
CAFE_OSC    = "#3A2317"
CAFE        = "#6F4322"
CAFE_CLARO  = "#9C6B3F"
ROJO        = "#C1272D"
ROJO_OSC    = "#8E1B1F"
AMARILLO    = "#F2A900"
AMARILLO_CL = "#FCC419"
CREMA       = "#FBF4E2"
CREMA_OSC   = "#F0E2C0"
BLANCO      = "#FFFFFF"
NEGRO       = "#231308"
AZUL_FOTO   = "#1CA3EC"   # tono del fondo azul de las fotos de estudio

# Tira tricolor (referencia al poncho / bandera) usada como acento
TRICOLOR = [AMARILLO, "#0B5BA6", ROJO]  # amarillo, azul, rojo

# ----------------------------------------------------------------------
# TIPOGRAFÍA (única disponible en el entorno)
# ----------------------------------------------------------------------
FUENTE = "Noto Sans"
