content = open('services.html', 'r', encoding='utf-8').read()

# Encontrar seção couples
idx = content.find('service-1')
if idx != -1:
    print('Found service-1 at:', idx)
    print(repr(content[idx:idx+500]))
else:
    print('service-1 not found')
    # Tentar encontrar couples
    idx2 = content.find('couples')
    print('couples at:', idx2)
    print(repr(content[idx2:idx2+300]))
