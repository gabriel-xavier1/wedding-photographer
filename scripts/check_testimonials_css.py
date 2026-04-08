content = open('index.html', 'r', encoding='utf-8').read()
import re
matches = re.findall(r'[^\n]*sie-testimonials[^\n]*\{[^\}]+\}', content)
for m in matches[:20]:
    print(m)
    print()
