content = open('services.html', 'r', encoding='utf-8').read()

# Titulo: aumentar height para 140px (tem 3 linhas agora)
content = content.replace(
    '.d .sie-service-1_1 {left:686px;top:98px;width:490px;height:75px;}',
    '.d .sie-service-1_1 {left:686px;top:80px;width:490px;height:140px;}'
)

# Texto: comecar em top:240px (80+140+20)
content = content.replace(
    '.d .sie-service-1_2 {left:686px;top:196px;width:490px;height:620px;}',
    '.d .sie-service-1_2 {left:686px;top:240px;width:490px;height:680px;}'
)

# Botao: top:940px (240+680+20)
content = content.replace(
    '.d .sie-service-1_5 {left:686px;top:836px;width:196px;height:54px;}',
    '.d .sie-service-1_5 {left:686px;top:940px;width:196px;height:54px;}'
)

# Starting at: top:1014px
content = content.replace(
    '.d .sie-service-1_3 {left:686px;top:910px;width:490px;height:16px;}',
    '.d .sie-service-1_3 {left:686px;top:1014px;width:490px;height:16px;}'
)

# Preco: top:1038px
content = content.replace(
    '.d .sie-service-1_4 {left:686px;top:934px;width:490px;height:60px;}',
    '.d .sie-service-1_4 {left:686px;top:1038px;width:490px;height:60px;}'
)

# Secao: 1038+60+60 = 1158px
content = content.replace(
    '"slug":"service-1","visible":"a","states":[],"d":{"h":1060,',
    '"slug":"service-1","visible":"a","states":[],"d":{"h":1160,'
)
content = content.replace(
    '.d .sib-service-1 {height:1060px;}',
    '.d .sib-service-1 {height:1160px;}'
)
content = content.replace(
    '.d .sie-service-1_0 {left:0px;top:0px;width:600px;height:1060px;',
    '.d .sie-service-1_0 {left:0px;top:0px;width:600px;height:1160px;'
)

open('services.html', 'w', encoding='utf-8').write(content)
print('OK')
