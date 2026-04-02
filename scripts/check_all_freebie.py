content = open('index.html', 'r', encoding='utf-8').read()

import re
matches = re.findall(r'\.d \.sie-freebie_\w+ \{[^}]+\}', content)
for m in matches:
    print(m)
    print()
