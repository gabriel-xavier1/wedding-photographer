with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Trocar a imagem do freebie
old_img = 'data-img="freebie_0" class="se-img se-gr slzy"></div><noscript><img src="//static.showit.co/400/KlQt6K4i1VVS2rUibaxQ7w/135701/iacob-hiticas-s6kasezsk5e-unsplash.jpg" class="se-img" alt="" title="iacob-hiticas-S6kAsEzsk5E-unsplash"/></noscript>'
new_img = 'data-img="freebie_0" class="se-img se-gr slzy" style="background-image:url(\'https://i.postimg.cc/qqvhR7sh/Chloe-Loius-366-2048x1365.jpg\');background-size:cover;background-position:center center;"></div><noscript><img src="https://i.postimg.cc/qqvhR7sh/Chloe-Loius-366-2048x1365.jpg" class="se-img" alt="" title="Chloe Louis Wedding"/></noscript>'

if old_img in content:
    content = content.replace(old_img, new_img, 1)
    print('freebie image OK')
else:
    print('freebie image NOT FOUND')
    idx = content.find('data-img="freebie_0"')
    print(repr(content[idx:idx+200]) if idx != -1 else 'nothing')

# 2. Ajustar posição do botão no CSS para não sobrepor o texto
# Desktop: mover botão para baixo do texto (freebie_2 termina em top:260+96=356, botão estava em top:380 - ok)
# O problema é no mobile: freebie_2 está em top:168+137=305, botão em top:326 - muito próximo
# Vamos dar mais espaço no mobile: top:326 -> top:360
old_css_m = '.m .sie-freebie_1 {left:25px;top:326px;width:165px;height:50px;}'
new_css_m = '.m .sie-freebie_1 {left:25px;top:370px;width:165px;height:50px;}'

if old_css_m in content:
    content = content.replace(old_css_m, new_css_m, 1)
    print('freebie_1 mobile position OK')
else:
    print('freebie_1 mobile CSS NOT FOUND')
    idx = content.find('sie-freebie_1 {left:25px')
    print(repr(content[idx:idx+100]) if idx != -1 else 'nothing')

# Ajustar altura do bloco freebie no mobile para acomodar
old_h_m = '.m .sib-freebie {height:420px;}'
new_h_m = '.m .sib-freebie {height:460px;}'

if old_h_m in content:
    content = content.replace(old_h_m, new_h_m, 1)
    print('freebie mobile height OK')
else:
    print('freebie mobile height NOT FOUND')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
