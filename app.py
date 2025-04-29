
from flask import Flask, render_template, request
import os
from mathjax_markdown import markdown_to_html

app = Flask(__name__)

MARKDOWN_FOLDER = 'markdown'

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_file = None
    html_content = None
    files = [f for f in os.listdir(MARKDOWN_FOLDER) if f.endswith('.md')]

    if request.method == 'POST':
        selected_file = request.form.get('markdown_file')
        if selected_file:
            file_path = os.path.join(MARKDOWN_FOLDER, selected_file)
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    md_text = f.read()
                html_content = markdown_to_html(md_text)

    return render_template('index.html', files=files, selected_file=selected_file, html_content=html_content)

if __name__ == '__main__':
    app.run(debug=True)
