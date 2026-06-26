#!/usr/bin/env bash
# Instala las fuentes de cartel usadas por la propuesta v2 (Anton, Oswald,
# Fraunces) en ~/.fonts, convirtiendo los woff2 de Fontsource a TTF.
# Requiere: node/npm, python con fonttools+brotli.
set -e
DIR="$(cd "$(dirname "$0")" && pwd)/_fonts"
mkdir -p "$DIR" && cd "$DIR"

echo "› Descargando paquetes de fuentes (Fontsource)…"
for p in anton oswald fraunces; do
  NODE_OPTIONS= npm pack "@fontsource/$p" >/dev/null 2>&1 || true
done
for f in *.tgz; do tar xzf "$f"; done

echo "› Convirtiendo woff2 → ttf e instalando en ~/.fonts…"
pip install --quiet fonttools brotli 2>/dev/null || true
python - <<'PY'
import os, glob
from fontTools.ttLib import TTFont
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)) if "__file__" in dir() else ".", "package", "files")
SRC = os.path.join(os.getcwd(), "package", "files")
DST = os.path.expanduser("~/.fonts"); os.makedirs(DST, exist_ok=True)
WANT = {"anton":[400], "oswald":[400,600,700], "fraunces":[400,600,700,900]}
for fam, pesos in WANT.items():
    for w in pesos:
        for ext in ("woff2","woff"):
            src=f"{SRC}/{fam}-latin-{w}-normal.{ext}"
            if os.path.exists(src):
                f=TTFont(src); f.flavor=None
                f.save(f"{DST}/{fam}-{w}.ttf"); break
print("Fuentes instaladas en", DST)
PY
fc-cache -f ~/.fonts >/dev/null 2>&1 || true
echo "✓ Listo. Verifica con:  fc-list : family | sort -u"
