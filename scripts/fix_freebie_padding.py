with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Dois dedos = ~48px em cima e em baixo da foto
# Bloco: 520px
# Foto: top:48, height = 520 - 48 - 48 = 424px
# Texto e botão também sobem 8px (48-40=8)

fixes = [
    # Foto: top:48, height:424
    ('.d .sie-freebie_0 {left:24px;top:40px;width:380px;height:440px;}',
     '.d .sie-freebie_0 {left:24px;top:48px;width:380px;height:424px;}'),

    # Subheading: sobe 8px (60→52... mas manter alinhamento com texto)
    # Manter top:60 para o texto ficar centrado verticalmente
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
