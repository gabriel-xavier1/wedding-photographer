content = open('index.html', 'r', encoding='utf-8').read()
import re
btns = re.findall(r'\.st-(?:primary|secondary)[^}]+\}', content[:8000])
for b in btns:
    print(b)
    print()
