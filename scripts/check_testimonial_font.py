content = open('index.html', 'r', encoding='utf-8').read()
import re
matches = re.findall(r'[^\n]*testimonials_view-1-1_1[^\n]*font[^\n]*', content)
for m in matches:
    print(m)
