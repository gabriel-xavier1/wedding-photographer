with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Target layout (matching the reference image):
# Bloco: 860px
# Heading "MEET YOUR PHOTOGRAPHER,": top:80, height:104 → termina em 184
# Nome "Jacque.": top:240 (184+56 gap), height:70 → termina em 310
# Texto: top:350 (310+40 gap), height:380 → termina em 730
# Botão: top:754 (730+24 gap), height:47
# Bloco: 754+47+59 = 860 ✓
# Foto: top:0, height:860 (full bleed)

fixes = [
    # Heading - dar margem em cima
    ('.d .sie-about_2 {left:58px;top:80px;width:560px;height:104px;}',
     '.d .sie-about_2 {left:58px;top:80px;width:560px;height:104px;}'),  # já ok

    # Nome - mais espaço abaixo do heading
    ('.d .sie-about_5 {left:58px;top:208px;width:392px;height:50px;}',
     '.d .sie-about_5 {left:58px;top:240px;width:392px;height:70px;}'),

    # Texto - abaixo do nome
    ('.d .sie-about_1 {left:58px;top:282px;width:540px;height:420px !important;overflow:visible !important;}',
     '.d .sie-about_1 {left:58px;top:350px;width:540px;height:380px !important;overflow:visible !important;}'),

    # Botão - logo abaixo do texto
    ('.d .sie-about_0 {left:58px;top:726px;width:220px;height:47px;}',
     '.d .sie-about_0 {left:58px;top:754px;width:220px;height:47px;}'),

    # Foto - full bleed, sem margem
    ('.d .sie-about_3 {left:620px;top:80px;width:540px;height:700px;}',
     '.d .sie-about_3 {left:620px;top:0px;width:580px;height:860px;}'),
]

for old, new in fixes:
    if old == new:
        print(f'SKIP: {old[:60]}')
        continue
    if old in content:
        content = content.replace(old, new, 1)
        print(f'OK: {new[:70]}')
    else:
        print(f'NOT FOUND: {old[:70]}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
