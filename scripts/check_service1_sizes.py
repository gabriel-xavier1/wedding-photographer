content = open('services.html', 'r', encoding='utf-8').read()
import re
matches = re.findall(r'\.d \.sie-service-1[^\n]+\{[^\}]+\}', content)
for m in matches[:15]:
    print(m)
    print()
