content = open('services.html', 'r', encoding='utf-8').read()

# Trocar "Starting at" pelo subtítulo do pacote
content = content.replace(
    '>Starting at<br></p>',
    '>Wedding Package 1 \u2013 Lover (Most Booked)<br>Up to 10 hours coverage<br></p>'
)

# Trocar preço
content = content.replace(
    '>$650</p>',
    '>\u00a3950.00<br>*Extra hour \u00a3150.00</p>'
)

open('services.html', 'w', encoding='utf-8').write(content)
print('OK')
