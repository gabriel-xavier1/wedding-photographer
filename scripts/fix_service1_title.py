content = open('services.html', 'r', encoding='utf-8').read()

# Trocar titulo "couples" pelo novo titulo
content = content.replace(
    '>couples<br></h3>',
    '>Wedding Package 1<br></h3>'
)

# Adicionar "LOVER" e subtitulo no campo de texto acima do conteudo
# O service-1_1 tem font-size:77px - vamos usar para "LOVER"
# Precisamos adicionar um segundo elemento ou usar o campo existente

# Na verdade, o titulo e um campo unico. Vamos colocar tudo nele com spans
content = content.replace(
    '>Wedding Package 1<br></h3>',
    '><span style="font-size:0.35em;letter-spacing:0.1em;display:block;margin-bottom:4px;">Wedding Package 1</span>LOVER<span style="font-size:0.3em;font-weight:normal;display:block;margin-top:4px;">up to 10 hours coverage</span><br></h3>'
)

open('services.html', 'w', encoding='utf-8').write(content)
print('OK')
