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

## ✅ Pendiente para finalizar

- [ ] Subir las **fotos reales** de los dos candidatos a `assets/`.
- [ ] Escribir los **nombres reales** en `campana/config.py`.
- [ ] Confirmar quién es **principal** y quién **suplente**.
- [ ] Ejecutar `python generar_campana.py` y enviar a imprenta los PDF.
