with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

fixes = [
    # Aumentar altura do texto para acomodar o conteúdo longo
    ('.d .sie-freebie_2 {left:548px;top:260px;width:490px;height:96px;}',
     '.d .sie-freebie_2 {left:548px;top:260px;width:490px;height:220px;}'),

    # Mover botão para abaixo do texto: 260+220+20 = 500
    ('.d .sie-freebie_1 {left:548px;top:380px;width:172px;height:50px;}',
     '.d .sie-freebie_1 {left:548px;top:500px;width:172px;height:50px;}'),

    # Aumentar altura do bloco desktop para acomodar
    ('.d .sib-freebie {height:590px;}',
     '.d .sib-freebie {height:620px;}'),

    # Foto desktop também cresce
    ('.d .sie-freebie_0 {left:122px;top:67px;width:357px;height:457px;}',
     '.d .sie-freebie_0 {left:122px;top:0px;width:440px;height:620px;}'),
]

for old, new in fixes:
    if old in content:
        content = content.replace(old, new, 1)
        print(f'OK: {new[:65]}')
    else:
        print(f'NOT FOUND: {old[:65]}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
