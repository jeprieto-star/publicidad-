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
# PALETA — editorial, sobria y profesional
#   Verde bosque + crema cálido + oro apagado + terracota.
#   Baja saturación: nada de "carnaval". El color enmarca, no grita.
# ----------------------------------------------------------------------
VERDE_OSC   = "#15392A"   # verde bosque profundo (color base de marca)
VERDE       = "#1F6B47"   # verde medio
VERDE_CLARO = "#3E8E63"   # verde claro (acentos sutiles)
VERDE_SALVIA= "#8FA98E"   # verde salvia desaturado (líneas finas)
CAFE_OSC    = "#2A1B11"   # café casi negro (texto sobre claro)
CAFE        = "#6B4329"   # café medio
CAFE_CLARO  = "#A07852"   # café claro
TERRACOTA   = "#A8472E"   # terracota / ladrillo (sustituye al rojo chillón)
TERRA_OSC   = "#7E3220"   # terracota oscuro
ORO         = "#C3922E"   # oro apagado (acento principal)
ORO_CL      = "#DEB85C"   # oro claro
CREMA       = "#F6EEDD"   # crema cálido (fondo claro)
CREMA_OSC   = "#EBDDC2"   # crema más profundo
HUESO       = "#FCFAF3"   # blanco hueso (paneles claros)
BLANCO      = "#FFFFFF"
NEGRO       = "#211913"   # carbón cálido (texto)
TINTA       = "#2C2017"   # tinta marrón para cuerpos de texto
AZUL_FOTO   = "#1CA3EC"   # tono del fondo azul de las fotos de estudio (respaldo)

# Compatibilidad con nombres antiguos del sistema
ROJO        = TERRACOTA
ROJO_OSC    = TERRA_OSC
AMARILLO    = ORO
AMARILLO_CL = ORO_CL

# Acento tricolor (poncho/bandera) en tonos APAGADOS, usado solo como
# regla fina y corta — nunca como bloque dominante.
TRICOLOR = [ORO, "#2E5A7A", TERRACOTA]  # oro apagado, azul petróleo, terracota

# ----------------------------------------------------------------------
# TIPOGRAFÍA (única disponible en el entorno)
# ----------------------------------------------------------------------
FUENTE = "Noto Sans"
