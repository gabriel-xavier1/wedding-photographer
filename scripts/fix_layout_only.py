content = open('index.html', 'r', encoding='utf-8').read()

# Aumentar foto de 380px para 480px
content = content.replace(
    '.d .sie-freebie_0 {left:24px;top:80px;width:380px;height:423px;}',
    '.d .sie-freebie_0 {left:24px;top:80px;width:480px;height:534px;}'
)

# Ajustar posição do texto para manter gap (~56px)
content = content.replace(
    '.d .sie-freebie_2 {left:460px;top:209px;width:560px;height:220px;}',
    '.d .sie-freebie_2 {left:560px;top:209px;width:560px;height:220px;}'
)

content = content.replace(
    '.d .sie-freebie_3 {left:460px;top:125px;width:560px;height:60px;}',
    '.d .sie-freebie_3 {left:560px;top:125px;width:560px;height:60px;}'
)

content = content.replace(
    '.d .sie-freebie_4 {left:460px;top:80px;width:560px;height:21px;',
    '.d .sie-freebie_4 {left:560px;top:80px;width:560px;height:21px;'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK - Layout ajustado, texto preservado')
