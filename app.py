
from flask import Flask, render_template, request
import os
from mathjax_markdown import markdown_to_html
from flask import send_from_directory
from pathlib import Path

app = Flask(__name__)

MARKDOWN_FOLDER = 'markdown'

def list_markdown_files():
    md_files = []
    for path in Path(MARKDOWN_FOLDER).rglob('*.md'):
        relative_path = path.relative_to(MARKDOWN_FOLDER)
        # Wandle Pfadobjekt in Unix-Style-String (mit / statt \)
        md_files.append(str(relative_path.as_posix()))
    return sorted(md_files)

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_file = None
    html_content = None
    files = list_markdown_files()

    if request.method == 'POST':
        selected_file = request.form.get('markdown_file')
        if selected_file:
            safe_path = os.path.normpath(os.path.join(MARKDOWN_FOLDER, selected_file))
            if os.path.commonprefix([os.path.abspath(safe_path), os.path.abspath(MARKDOWN_FOLDER)]) == os.path.abspath(MARKDOWN_FOLDER):
                if os.path.exists(safe_path):
                    with open(safe_path, 'r', encoding='utf-8') as f:
                        md_text = f.read()
                    html_content = markdown_to_html(md_text)

    return render_template('index.html', files=files, selected_file=selected_file, html_content=html_content)

@app.route('/markdown/<path:filename>')
def serve_markdown_file(filename):
    return send_from_directory('markdown', filename)
if __name__ == '__main__':
    app.run(debug=True)