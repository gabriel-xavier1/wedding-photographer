content = open('services.html', 'r', encoding='utf-8').read()

# Reverter service-1_3 para "Starting at"
content = content.replace(
    '>Wedding Package 1 \u2013 Lover (Most Booked)<br>Up to 10 hours coverage<br></p>',
    '>Starting at<br></p>'
)

# Corrigir preco - mostrar apenas £950.00 com extra hour menor
content = content.replace(
    '>\u00a3950.00<br>*Extra hour \u00a3150.00</p>',
    '>\u00a3950.00</p>'
)

# Adicionar extra hour no campo service-1_3 (starting at)
content = content.replace(
    '>Starting at<br></p>',
    '>Drone available, weather and venue depending.<br></p>'
)

# Reduzir font-size do preco
content = content.replace(
    '.d .sie-service-1_4-text {font-size:46px;}',
    '.d .sie-service-1_4-text {font-size:36px;}'
)

# Adicionar CSS para extra hour abaixo do preco
css = '\n.d .sie-service-1_4-text::after {content:" *Extra hour \\00a3150.00";display:block;font-size:18px;font-style:italic;}\n'
content = content.replace('</style>', css + '</style>', 1)

open('services.html', 'w', encoding='utf-8').write(content)
print('OK')
