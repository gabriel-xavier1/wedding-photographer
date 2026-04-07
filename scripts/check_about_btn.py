content = open('index.html', 'r', encoding='utf-8').read()
import re

# CSS do about_0 (get to know me)
matches = re.findall(r'[^\n]*sie-about_0[^\n]*', content)
for m in matches:
    if '{' in m:
        print(m)
