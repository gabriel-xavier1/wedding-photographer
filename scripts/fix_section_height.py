content = open('index.html', 'r', encoding='utf-8').read()

# Aumentar altura da seção
content = content.replace(
    '.d .sib-freebie {height:583px;}',
    '.d .sib-freebie {height:700px;}'
)

# Ajustar botão para ficar logo abaixo do texto (texto termina em ~589px, gap de 20px)
content = content.replace(
    '.d .sie-freebie_1 {left:460px;top:610px;width:220px;height:50px;}',
    '.d .sie-freebie_1 {left:460px;top:620px;width:220px;height:50px;}'
)

# Foto acompanha a seção
content = content.replace(
    '.d .sie-freebie_0 {left:24px;top:80px;width:380px;height:560px;}',
    '.d .sie-freebie_0 {left:24px;top:40px;width:380px;height:620px;}'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
