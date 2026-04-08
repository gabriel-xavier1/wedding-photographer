content = open('index.html', 'r', encoding='utf-8').read()

# CSS
import re
matches = re.findall(r'[^\n]*manual-posts[^\n]*\{[^\}]+\}', content)
for m in matches[:15]:
    print(m)
    print()
