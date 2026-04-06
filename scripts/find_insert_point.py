content = open('index.html', 'r', encoding='utf-8').read()
idx = content.find('id="testimonials"')
print(repr(content[idx-30:idx+30]))
print('Position:', idx)
