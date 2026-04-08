content = open('index.html', 'r', encoding='utf-8').read()
idx = content.find('sis-testimonials_view-1-1')
print(repr(content[idx:idx+600]))
