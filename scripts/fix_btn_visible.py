content = open('index.html', 'r', encoding='utf-8').read()

# Aumentar seção
content = content.replace(
    '.d .sib-freebie {height:700px;}',
    '.d .sib-freebie {height:720px;}'
)

# Subir botão para ficar dentro da seção com folga
content = content.replace(
    '.d .sie-freebie_1 {left:460px;top:620px;width:220px;height:50px;}',
    '.d .sie-freebie_1 {left:460px;top:600px;width:220px;height:50px;}'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
