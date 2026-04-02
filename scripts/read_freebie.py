content = open('index.html', 'r', encoding='utf-8').read()

sections = ['freebie_2', 'freebie_3', 'freebie_4']

for sid in sections:
    idx = content.find(f'data-sid="{sid}"')
    if idx != -1:
        print(f'--- {sid} ---')
        print(repr(content[idx:idx+400]))
        print()
