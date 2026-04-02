with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Adicionar background-image diretamente no CSS do elemento freebie_0
# para garantir que a imagem apareça independente do loader do Showit
old_css = '.d .sie-freebie_0 .se-img {background-repeat:no-repeat;background-size:cover;background-position:50% 50%;border-radius:inherit;}'
new_css = '.d .sie-freebie_0 .se-img {background-repeat:no-repeat;background-size:cover;background-position:50% 50%;border-radius:inherit;background-image:url(\'https://i.postimg.cc/qqvhR7sh/Chloe-Loius-366-2048x1365.jpg\') !important;}'

if old_css in content:
    content = content.replace(old_css, new_css, 1)
    print('freebie_0 CSS image OK')
else:
    print('NOT FOUND')
    idx = content.find('sie-freebie_0 .se-img')
    print(repr(content[idx:idx+120]) if idx != -1 else 'nothing')

# Mobile também - mas freebie_0 está display:none no mobile, então só desktop importa
# Remover o display:none do mobile para mostrar a imagem
old_m = '.m .sie-freebie_0 {left:62px;top:78px;width:196px;height:272px;display:none;}'
new_m = '.m .sie-freebie_0 {left:62px;top:78px;width:196px;height:272px;display:none;}'
# Manter display:none no mobile pois o layout original não mostra a imagem no mobile

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
