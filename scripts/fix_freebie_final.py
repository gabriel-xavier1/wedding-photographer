content = open('index.html', 'r', encoding='utf-8').read()

# Aumentar container do texto
content = content.replace(
    '.d .sie-freebie_2 {left:460px;top:209px;width:560px;height:320px;}',
    '.d .sie-freebie_2 {left:460px;top:209px;width:560px;height:380px;}'
)

# Mover botão para baixo do texto
content = content.replace(
    '.d .sie-freebie_1 {left:460px;top:453px;width:220px;height:50px;}',
    '.d .sie-freebie_1 {left:460px;top:610px;width:220px;height:50px;}'
)

# Aumentar foto para acompanhar
content = content.replace(
    '.d .sie-freebie_0 {left:24px;top:80px;width:380px;height:423px;}',
    '.d .sie-freebie_0 {left:24px;top:80px;width:380px;height:560px;}'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
