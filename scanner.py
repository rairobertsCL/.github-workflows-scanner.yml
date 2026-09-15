import feedparser
import xml.etree.ElementTree as ET

# Matriz de palabras clave de interés legislativo
keywords = ['artificial intelligence', 'quantum', 'regulation', 'platform', 'policy', 'governance']

def parse_opml(file_path):
    tree = ET.parse(file_path)
    return [outline.attrib['xmlUrl'] for outline in tree.findall('.//outline') if 'xmlUrl' in outline.attrib]

urls = parse_opml('fuentes.opml')
reporte = []

for url in urls:
    feed = feedparser.parse(url)
    for entry in feed.entries:
        if any(kw in entry.title.lower() or kw in entry.summary.lower() for kw in keywords):
            reporte.append(f"- {entry.title}\n  Enlace: {entry.link}\n")

with open('reporte_legislativo.txt', 'w', encoding='utf-8') as f:
    f.write("Hallazgos de Horizon Scanning:\n\n" + "\n".join(reporte))