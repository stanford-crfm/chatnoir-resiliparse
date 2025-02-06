with open("sample.html", "r") as f:
    html = f.read()

from resiliparse_dom import parse_html

dom = parse_html(html)

print(dom.to_text())
