content = open('index.html', 'r', encoding='utf-8').read()

# Aumentar seção para acomodar tudo
content = content.replace(
    '.d .sib-freebie {height:720px;}',
    '.d .sib-freebie {height:800px;}'
)

# Foto acompanha
content = content.replace(
    '.d .sie-freebie_0 {left:24px;top:40px;width:380px;height:620px;}',
    '.d .sie-freebie_0 {left:24px;top:40px;width:380px;height:720px;}'
)

# Botão logo abaixo do texto com 24px de gap
content = content.replace(
    '.d .sie-freebie_1 {left:460px;top:600px;width:220px;height:50px;}',
    '.d .sie-freebie_1 {left:460px;top:640px;width:220px;height:50px;}'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
