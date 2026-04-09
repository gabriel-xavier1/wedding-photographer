content = open('services.html', 'r', encoding='utf-8').read()

# Ver todos os elementos do service-1
import re
matches = re.findall(r'[^\n]*sie-service-1[^\n]*', content)
for m in matches[:20]:
    if '{' in m or 'se">' in m:
        print(m[:200])
        print()
