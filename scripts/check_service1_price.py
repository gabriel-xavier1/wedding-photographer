content = open('services.html', 'r', encoding='utf-8').read()
for sid in ['service-1_1', 'service-1_3', 'service-1_4']:
    idx = content.find(f'data-sid="{sid}"')
    print(f'--- {sid} ---')
    print(repr(content[idx:idx+200]))
    print()
