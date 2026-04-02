with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Trocar a imagem no JSON de dados (init_data) - é onde o Showit carrega a imagem
old_json_img = '"id": "freebie_0", "blockId": "freebie", "m": {"x": 62, "y": 78, "w": 196, "h": 272, "a": 0, "trIn": {"cl": "fadeIn", "d": 1, "dl": "0"}}, "d": {"x": 122, "y": 67, "w": 357, "h": 457, "a": 0, "gs": {"s": 50}, "trIn":'
idx = content.find(old_json_img)
if idx != -1:
    # Find the "c": {...} part after this element
    c_idx = content.find('"c": {', idx)
    c_end = content.find('}', c_idx) + 1
    old_c = content[c_idx:c_end]
    new_c = '"c": {"key": "https://i.postimg.cc/qqvhR7sh/Chloe-Loius-366-2048x1365.jpg", "aspect_ratio": 1.5, "title": "Chloe Louis Wedding", "type": "url"}'
    content = content.replace(old_c, new_c, 1)
    print('JSON image OK')
    print('old:', old_c)
    print('new:', new_c)
else:
    print('JSON freebie_0 NOT FOUND')

# 2. Corrigir o CSS do botão desktop - estava em top:380, texto freebie_2 em top:260+96=356
# Mover botão desktop para top:460 para ficar abaixo do texto
old_css_d = '.d .sie-freebie_1 {left:548px;top:380px;width:172px;height:50px;}'
new_css_d = '.d .sie-freebie_1 {left:548px;top:470px;width:172px;height:50px;}'
if old_css_d in content:
    content = content.replace(old_css_d, new_css_d, 1)
    print('freebie_1 desktop position OK')
else:
    print('freebie_1 desktop CSS NOT FOUND')
    idx2 = content.find('sie-freebie_1 {left:548')
    print(repr(content[idx2:idx2+80]) if idx2 != -1 else 'nothing')

# 3. Ajustar altura desktop do freebie para acomodar
old_h_d = '.d .sib-freebie {height:590px;}'
new_h_d = '.d .sib-freebie {height:640px;}'
if old_h_d in content:
    content = content.replace(old_h_d, new_h_d, 1)
    print('freebie desktop height OK')
else:
    print('freebie desktop height NOT FOUND')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
