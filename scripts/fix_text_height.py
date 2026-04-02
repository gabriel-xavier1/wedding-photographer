content = open('index.html', 'r', encoding='utf-8').read()

# Aumentar height do container de texto de 220px para 280px
content = content.replace(
    '.d .sie-freebie_2 {left:560px;top:209px;width:560px;height:220px;}',
    '.d .sie-freebie_2 {left:560px;top:209px;width:560px;height:280px;}'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
