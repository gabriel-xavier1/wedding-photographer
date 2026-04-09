content = open('services.html', 'r', encoding='utf-8').read()

idx = content.find('id="service-1"')
print(repr(content[idx:idx+1500]))
