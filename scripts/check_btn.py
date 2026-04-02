content = open('index.html', 'r', encoding='utf-8').read()

import re

# CSS do botao
matches = re.findall(r'\.d \.sie-freebie_1[^}]+\}', content)
for m in matches:
    print('CSS:', m)

# HTML do botao
idx = content.find('data-sid="freebie_1"')
print('\nHTML:', repr(content[idx:idx+300]))
