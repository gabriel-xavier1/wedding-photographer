content = open('index.html', 'r', encoding='utf-8').read()
import re
fonts = re.findall(r'font-family:[^;\"]{1,80}', content)
seen = set()
for f in fonts:
    if f not in seen:
        seen.add(f)
        print(f)
