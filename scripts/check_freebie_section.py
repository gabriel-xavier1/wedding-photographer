content = open('index.html', 'r', encoding='utf-8').read()

import re
# altura total da section freebie
matches = re.findall(r'\.d \.sib-freebie[^}]+\}', content)
for m in matches:
    print(m)
    print()

# altura do sc container
idx = content.find('id="freebie"')
print(repr(content[idx:idx+300]))
