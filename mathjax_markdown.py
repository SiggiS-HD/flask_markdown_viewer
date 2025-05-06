
import re
import markdown2

def extract_math(text):
    math_expressions = []

    def replace_block(match):
        math_expressions.append(match.group(0))
        return f"@@BLOCK{len(math_expressions)-1}@@"
    text = re.sub(r'\\\[.*?\\\]', replace_block, text, flags=re.DOTALL)

    def replace_inline(match):
        math_expressions.append(match.group(0))
        return f"@@INLINE{len(math_expressions)-1}@@"
    text = re.sub(r'\\\(.*?\\\)', replace_inline, text, flags=re.DOTALL)

    return text, math_expressions

def restore_math(html, math_expressions):
    for i, expr in enumerate(math_expressions):
        html = html.replace(f"@@BLOCK{i}@@", expr)
        html = html.replace(f"@@INLINE{i}@@", expr)
    return html

def fix_image_paths(html):
    return re.sub(r'src="(?!http)([^"]+)"', r'src="/markdown/\1"', html)

def wrap_images(html):
    def replacer(match):
        return f'<div class="print-image">{match.group(0)}</div>'
    return re.sub(r'<img[^>]+>', replacer, html)

def markdown_to_html(md_text):
    protected_text, math_expressions = extract_math(md_text)
    html = markdown2.markdown(
        protected_text,
        extras=["fenced-code-blocks", "tables", "code-friendly", "toc"]
    )

    html = restore_math(html, math_expressions)
    html = fix_image_paths(html)
    html = wrap_images(html)
    return html
