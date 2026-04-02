content = open('index.html', 'r', encoding='utf-8').read()

for sid in ['about_2', 'about_5']:
    idx = content.find(f'.d .sie-{sid} ')
    print(f'--- {sid} CSS ---')
    print(repr(content[idx:idx+250]))
    print()

for sid in ['about_2', 'about_5']:
    idx = content.find(f'data-sid="{sid}"')
    print(f'--- {sid} HTML ---')
    print(repr(content[idx:idx+200]))
    print()
