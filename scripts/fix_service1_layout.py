content = open('services.html', 'r', encoding='utf-8').read()

# Texto termina em: 196 + 620 = 816px
# Botao: top:836px (816 + 20 gap)
content = content.replace(
    '.d .sie-service-1_5 {left:686px;top:688px;width:196px;height:54px;}',
    '.d .sie-service-1_5 {left:686px;top:836px;width:196px;height:54px;}'
)

# Starting at: top:910px (836 + 54 + 20)
content = content.replace(
    '.d .sie-service-1_3 {left:686px;top:840px;width:166px;height:16px;}',
    '.d .sie-service-1_3 {left:686px;top:910px;width:490px;height:16px;}'
)

# Preco: top:934px
content = content.replace(
    '.d .sie-service-1_4 {left:686px;top:864px;width:490px;height:48px;}',
    '.d .sie-service-1_4 {left:686px;top:934px;width:490px;height:60px;}'
)

# Seção: 934 + 60 + 60 = 1054px
content = content.replace(
    '"slug":"service-1","visible":"a","states":[],"d":{"h":960,',
    '"slug":"service-1","visible":"a","states":[],"d":{"h":1060,'
)
content = content.replace(
    '.d .sib-service-1 {height:960px;}',
    '.d .sib-service-1 {height:1060px;}'
)

# Foto acompanha
content = content.replace(
    '.d .sie-service-1_0 {left:0px;top:0px;width:600px;height:960px;',
    '.d .sie-service-1_0 {left:0px;top:0px;width:600px;height:1060px;'
)

open('services.html', 'w', encoding='utf-8').write(content)
print('OK')
