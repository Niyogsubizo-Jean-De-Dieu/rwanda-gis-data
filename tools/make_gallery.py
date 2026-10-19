"""Extract the example figures for the README from a generated Area Profile report.

Usage (from the repository root):
    python tools/make_gallery.py Area_Profile_Gicumbi.docx

It reads the report made by the notebook, finds each figure by its caption and saves a
resized copy in docs/images/. Needs: pip install python-docx pillow
"""
import io
import os
import sys

from docx import Document
from PIL import Image

KEYS = {
    'Elevation map': 'elevation_map.png',
    'Slope classes': 'slope_classes.png',
    'Climate diagram': 'climate_diagram.png',
    'Land cover of': 'land_cover.png',
    'Population density by': 'population_density.png',
    'Built-up surface in': 'builtup_2020.png',
    'Annual tree-cover loss': 'tree_cover_loss.png',
    'Cropland and cropland on slopes': 'erosion_hotspots.png',
}
MAX_WIDTH = 900

report = sys.argv[1]
doc = Document(report)
rels = {r.rId: r for r in doc.part.rels.values() if 'image' in r.reltype}
os.makedirs('docs/images', exist_ok=True)

pending = None
saved = set()
for p in doc.paragraphs:
    blips = p._p.xpath('.//a:blip/@r:embed')
    if blips:
        pending = rels[blips[0]].target_part.blob
        continue
    if p.style.name == 'Caption' and p.text.startswith('Figure') and pending is not None:
        for key, name in KEYS.items():
            if key in p.text and name not in saved:
                im = Image.open(io.BytesIO(pending)).convert('RGB')
                if im.width > MAX_WIDTH:
                    im = im.resize((MAX_WIDTH, round(im.height * MAX_WIDTH / im.width)), Image.LANCZOS)
                im.save(f'docs/images/{name}', optimize=True)
                saved.add(name)
                print('saved', name)
        pending = None

missing = sorted(set(KEYS.values()) - saved)
if missing:
    print('not found in this report:', ', '.join(missing))
