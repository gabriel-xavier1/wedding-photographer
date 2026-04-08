content = open('index.html', 'r', encoding='utf-8').read()
idx = content.find('sie-testimonials_view-1-2_1 se">')
print(repr(content[idx:idx+1000]))
