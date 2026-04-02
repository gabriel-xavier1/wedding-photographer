content = open('index.html', 'r', encoding='utf-8').read()

sections = ['intro_0', 'intro_1', 'intro_2', 'intro_3', 'offers_0', 'offers_3', 'offers_5', 'offers_7', 'offers_9', 'offers_11']

for sid in sections:
    idx = content.find(f'data-sid="{sid}"')
    if idx != -1:
        print(f'--- {sid} ---')
        print(repr(content[idx:idx+300]))
        print()
