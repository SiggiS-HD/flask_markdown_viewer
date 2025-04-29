
# 📘 Flask Markdown Viewer

Ein schlanker, serverseitiger Markdown-Viewer auf Basis von **Flask**, der Markdown-Dokumente aus einem Verzeichnis anzeigt – mit Unterstützung für:

- serverseitiges Markdown-Rendering (via `markdown2`)
- mathematische Formeln (`\(...\)` und `\[...\]`) via **MathJax**
- Codeblöcke mit Syntax-Hervorhebung
- Tabellen im Markdown-Format
- Zitate/Blockquotes (Markdown `>`-Blöcke)
- optimiertes CSS für Anzeige und Druck
- PDF-Erzeugung via **Strg+P** (Browser) mit `@media print` Styling
- kein JavaScript notwendig – außer dem MathJax-CDN

---

## 🔧 Installation

### Voraussetzungen

- Python 3.10 oder neuer
- pip
- Virtuelle Umgebung empfohlen

### Abhängigkeiten

```bash
pip install flask markdown2
```

---

## 📁 Projektstruktur

```text
flask_markdown_viewer/
├── app.py
├── mathjax_markdown.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── markdown/
│   └── (hier liegen Deine .md-Dateien)
```

---

## 🚀 Start der App

### 🐧 Linux/macOS mit Gunicorn

```bash
pip install gunicorn
gunicorn -w 1 -b 127.0.0.1:5000 app:app
```

- Die App ist erreichbar unter: [http://127.0.0.1:5000](http://127.0.0.1:5000)

### 🪟 Windows mit Waitress

```bash
pip install waitress
python -m waitress --host=127.0.0.1 --port=5000 app:app
```

---

## 📄 Verwendung

1. Lege Markdown-Dateien in den Ordner `markdown/`
2. Starte die App
3. Rufe im Browser auf: [http://127.0.0.1:5000](http://127.0.0.1:5000)
4. Wähle ein Dokument aus dem Dropdown und klicke auf „Anzeigen“
5. Zur PDF-Erzeugung einfach:
   - `Strg + P` (Windows) oder `Cmd + P` (Mac)
   - Ziel: „Als PDF speichern“
   - „Hintergrundgrafiken drucken“ aktivieren (wichtig für Farben bei Code & Tabellen)

---

## 🖌️ Features & Darstellung

- **MathJax** zur Darstellung mathematischer Formeln
- **Codeblöcke** mit farblichem Hintergrund
- **Tabellen** mit Rahmen und Hintergrund
- **Blockquotes** (Markdown `> Zitat`) optisch hervorgehoben
- **@media print**-Optimierung:
  - Nur der gerenderte Inhalt wird gedruckt
  - Kopfzeile, Formular, Buttons werden automatisch ausgeblendet
  - Seitenumbrüche bei Tabellen, Code und Überschriften werden vermieden

---

## 📷 Beispiel-Markdown (Vorschlag für `example_math.md`)

```markdown
# Beispiel: Mathematische Formel

Die Formel für Energie lautet:

\[
E = mc^2
\]

## Beispiel: Tabelle

| Sprache | Jahr | Typ     |
|---------|------|----------|
| Python  | 1991 | Dynamisch |
| C       | 1972 | Statisch  |

## Beispiel: Codeblock

\`\`\`bash
echo "Hallo Welt"
\`\`\`

## Beispiel: Zitat

> Dieser Bereich ist ein Markdown-Zitat (Blockquote).
```

---

## 📝 Lizenz

MIT – frei für private und kommerzielle Nutzung.

---

## 🙏 Dank

Dieses Projekt wurde mit Unterstützung einer interaktiven ChatGPT-Beratung erstellt – inklusive Planung, Stil und PDF-Druckunterstützung.
