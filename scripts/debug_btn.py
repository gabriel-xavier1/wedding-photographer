content = open('index.html', 'r', encoding='utf-8').read()

import re

# Todos os CSS do freebie_1
matches = re.findall(r'[^\n]*freebie_1[^\n]*', content)
for m in matches:
    print(m)
    print()
