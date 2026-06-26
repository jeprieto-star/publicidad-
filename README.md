# Campaña Plancha N.º 2 — *Comprometidos con los Cafeteros*

Kit de **publicidad completo** para la candidatura **Plancha N.º 2** al
**Comité Departamental de Cafeteros del Tolima**, con enfoque en los municipios del
**Norte del Tolima: Líbano, Villahermosa y Casabianca**.

> **Lema:** COMPROMETIDOS CON LOS CAFETEROS
> **Sublema:** Por unos cafeteros prósperos

Todas las piezas se generan por código (Python + [cairosvg](https://cairosvg.org/)) y se exportan en
**SVG** (vectorial/editable), **PNG** (alta resolución) y **PDF** (listo para imprenta).

---

## 📦 Piezas incluidas

| # | Pieza | Formato sugerido | Uso |
|---|-------|------------------|-----|
| 01 | Afiche principal | Vertical 50×70 cm | Cartel con candidatos + lema |
| 02 | Afiche de propuestas | Vertical 50×70 cm | Las 5 propuestas con iconos |
| 03 | Pasacalle | Banner horizontal (4:1) | Cruce de calle / vinilo |
| 04 | Valla / Vaya | Gran formato 8×3 m (8:3) | Lectura a distancia |
| 05 | Volante | Media carta vertical | Reparto mano a mano |
| 06 | Tarjeta de presentación | 9×5 cm | Contacto / entrega personal |
| 07 | Post redes | 1080×1080 px | Instagram / Facebook |
| 08 | Historia redes | 1080×1920 px | Historias / estados |

Los archivos finales quedan en `salida/png`, `salida/pdf` y `salida/svg`.
Abre **`index.html`** en el navegador para ver la galería y descargar cada pieza.

---

## 🎨 Las 5 propuestas

1. **Buenas vías** de comunicación para sacar la cosecha
2. **Buenos incentivos** por renovación de café
3. **Mejoramiento y construcción** de beneficiaderos
4. **Proyectos productivos** para las mujeres cafeteras
5. **La defensoría** de los cafeteros

---

## ⚙️ Cómo personalizar y regenerar

Todo lo editable vive en **`campana/config.py`**:

- **Nombres de los candidatos** → campo `nombre` en `CANDIDATOS`.
- **Fotos reales** → reemplaza los archivos `assets/candidato-1.png` y `assets/candidato-2.png`
  (puedes usar `.jpg`; actualiza la ruta en `config.py`). Recomendado: foto vertical, rostro centrado.
- **Propuestas, municipios, lema y colores** → variables en `config.py`.

Luego regenera **todas** las piezas:

```bash
# 1. Crear entorno e instalar dependencias (solo la primera vez)
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 2. Generar todo el kit
python generar_campana.py
```

> ℹ️ Las fotos se incrustan dentro del SVG (base64), por lo que cada archivo es autosuficiente.

---

## 🗂️ Estructura del proyecto

```
publicidad-/
├── generar_campana.py      # Punto de entrada: genera todas las piezas
├── index.html              # Galería visual para ver/descargar
├── requirements.txt
├── assets/                 # Fotos de los candidatos (reemplazables)
├── campana/
│   ├── config.py           # ← TODO lo editable (datos, textos, colores)
│   ├── grafismos.py        # Componentes gráficos (rama de café, sello, iconos…)
│   ├── piezas.py           # Definición de cada pieza
│   └── render.py           # Exportación a SVG / PNG / PDF
└── salida/
    ├── svg/  ├── png/  └── pdf/
```

---

## ✅ Estado de la campaña

- [x] **Fotos reales** de los dos candidatos integradas (`assets/recortes/`).
- [x] **Nombres reales** en `campana/config.py`:
  - **Principal:** Jhon Esneider Prieto Prieto
  - **Suplente:** Nelson Ferned Orozco Castaño
- [x] **Identidad regional** (Líbano · Casabianca · Villahermosa · Norte del Tolima) presente en todas las piezas.
- [x] Kit completo generado en **SVG / PNG / PDF** (carpeta `salida/`).
- [ ] Revisar los PDF y enviarlos a imprenta.


---

# ☕ PROPUESTA NUEVA (v2) — *Tierra de Café*

Rediseño **completo y desde cero**, con una dirección de arte totalmente
distinta a la versión anterior:

- **Estilo cálido y de impacto** (no el verde editorial sobrio anterior):
  paleta **cereza de café + espresso + crema + ámbar**.
- **Tipografía de cartel**: Anton (titulares), Oswald (rótulos),
  Fraunces (acentos), Noto Sans (cuerpo).
- **Fotografía real del café como protagonista**: los **cafetales**, la
  **recolección** y el **grano maduro** — incluso de fondo en los retratos,
  para conectar con quienes siembran café.
- **Mensaje amplio**: por las familias cafeteras, sin municipios ni zonas
  específicas de territorio.
- **Sistema de marca propio**: sello/insignia con el número **2**, grano de
  café estilizado y líneas topográficas de la cordillera.
- **Sitio web interactivo** para compartir por WhatsApp/redes.

## Piezas (carpeta `salida_v2/` — SVG · PNG · PDF)

| # | Pieza |
|---|-------|
| 01 | Afiche principal |
| 02 | Afiche de propuestas |
| 03 | Pasacalle |
| 04 | Valla |
| 05 | Volante |
| 06 | Tarjeta |
| 07 | Post para redes (1080×1080) |
| 08 | Historia / estado (1080×1920) |
| 09 | **Sello / logotipo** de campaña (suelto) |

➕ **Sitio web:** `sitio/index.html` (landing one-page lista para GitHub Pages).

## Cómo regenerar la propuesta v2

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
bash instalar_fuentes.sh      # instala Anton / Oswald / Fraunces (una vez)
python generar_v2.py          # genera todo en salida_v2/
```

> Todo lo editable (nombres, propuestas, colores, fotos) vive en
> `estudio/marca.py`. La lógica gráfica está en `estudio/svg.py` y el armado
> de cada pieza en `estudio/piezas.py`.

## Estructura de la propuesta v2

```
estudio/
├── marca.py     # ← datos, paleta y tipografía (TODO lo editable)
├── svg.py       # componentes: foto, sello, grano, topografía, iconos…
├── piezas.py    # definición de cada pieza
└── render.py    # exportación SVG / PNG / PDF
assets_v2/region/ # fotos reales de la región (Líbano, cafetales, nevado…)
generar_v2.py     # punto de entrada
sitio/index.html  # micrositio interactivo de campaña
salida_v2/        # svg/ · png/ · pdf/
```
