content = open('services.html', 'r', encoding='utf-8').read()

for sid in ['faq_12', 'faq_13', 'faq_14', 'faq_15', 'faq_16']:
    marker = f'data-sid="{sid}"'
    idx = content.find(marker)
    if idx >= 0:
        print(f'\n=== {sid} ===')
        print(repr(content[idx:idx+250]))
    else:
        print(f'\n=== {sid} NOT FOUND ===')
