content = open('index.html', 'r', encoding='utf-8').read()

# freebie_0 = foto, freebie_2 = texto
for sid in ['freebie_0', 'freebie_2', 'freebie_3', 'freebie_4']:
    idx = content.find(f'.d .sie-{sid} ')
    if idx != -1:
        print(f'--- {sid} CSS ---')
        print(repr(content[idx:idx+200]))
        print()
