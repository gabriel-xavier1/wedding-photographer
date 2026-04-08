import re
content = open('index.html', 'r', encoding='utf-8').read()

# Dados das fotos
photos = [
    ('manual-posts_0', 'https://i.postimg.cc/NjPzCHwP/steph_e_iain.png'),
    ('manual-posts_3', 'https://i.postimg.cc/ZKk9ZN6n/TS_11618.jpg'),
    ('manual-posts_5', 'https://i.postimg.cc/8zn0X6VX/ada_e_joshua.png'),
]

for img_id, url in photos:
    # 1. Corrigir o HTML - remover style duplicado
    # Padrão: <div style="width:100%;height:100%" style="...background-image...">
    pattern = rf'(<div )style="width:100%;height:100%" (style="width:100%;height:100%;background-image:url\(\'{re.escape(url)}\'\)[^"]*" data-img="{img_id}")'
    replacement = rf'\1\2'
    new_content = re.sub(pattern, replacement, content)
    if new_content != content:
        content = new_content
        print(f'Fixed double style: {img_id}')
    else:
        print(f'Double style not found for {img_id}, trying direct fix...')
        # Tentar substituição direta do HTML completo
        # Buscar o div com data-img e substituir
        idx = content.find(f'data-img="{img_id}"')
        if idx != -1:
            # Pegar o div anterior
            div_start = content.rfind('<div ', 0, idx)
            div_end = content.find('>', idx) + 1
            old_div = content[div_start:div_end]
            new_div = f'<div style="width:100%;height:100%;background-image:url(\'{url}\');background-size:cover;background-position:center center;" data-img="{img_id}" class="se-img se-gr slzy">'
            content = content[:div_start] + new_div + content[div_end:]
            print(f'  Direct fix applied: {img_id}')

    # 2. Adicionar CSS override para forçar background-image
    css_rule = f'.d .sie-{img_id} .se-img {{background-image:url(\'{url}\') !important;background-size:cover !important;background-position:center center !important;}}\n'
    if css_rule not in content:
        content = content.replace('</style>', css_rule + '</style>', 1)
        print(f'CSS override added: {img_id}')

open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
