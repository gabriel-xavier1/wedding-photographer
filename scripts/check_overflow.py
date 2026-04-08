content = open('index.html', 'r', encoding='utf-8').read()
import re
matches = re.findall(r'[^\n]*view-1-2_1[^\n]*overflow[^\n]*', content)
for m in matches:
    print(m)

# Verificar se há duplicação no HTML
count = content.count("We couldn't have asked for a better photographer")
print(f'\nOccurrences: {count}')
