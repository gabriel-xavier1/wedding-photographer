content = open('index.html', 'r', encoding='utf-8').read()
import re
matches = re.findall(r'[^\n]*manual-posts_[012][^\n]*\{[^\}]+\}', content)
for m in matches[:10]:
    print(m)
    print()
