with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Padding igual: 60px em cima e em baixo
# Conteúdo: subheading top:60, botão termina em 433+50=483
# Bloco: 483+60 = 543px
# Foto: top:60, height = 543-60-60 = 423px

fixes = [
    # Bloco
    ('.d .sib-freebie {height:520px;}',
     '.d .sib-freebie {height:543px;}'),

    # Foto: top:60, height:423
    ('.d .sie-freebie_0 {left:24px;top:48px;width:380px;height:424px;}',
     '.d .sie-freebie_0 {left:24px;top:60px;width:380px;height:423px;}'),
]

for old, new in fixes:
    if old in content:
        content = content.replace(old, new, 1)
        print(f'OK: {new[:70]}')
    else:
        print(f'NOT FOUND: {old[:70]}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
