with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Sistema consistente 24px gap:
# about_2 heading: top:80, height:104 → termina em 184
# about_5 nome:    top:208 (184+24), height:50 → termina em 258
# about_1 texto:   top:282 (258+24), height:420 → termina em 702
# about_0 botão:   top:726 (702+24), height:47
# Bloco: 726+47+80 = 853 → usar 860px
# Foto: top:80, height:860-80-80=700px

fixes = [
    # Bloco
    ('.d .sib-about {height:920px;}',
     '.d .sib-about {height:860px;}'),

    # about_2 heading
    ('.d .sie-about_2 {left:58px;top:161px;width:392px;height:104px;}',
     '.d .sie-about_2 {left:58px;top:80px;width:560px;height:104px;}'),

    # about_5 nome
    ('.d .sie-about_5 {left:58px;top:220px;width:392px;height:50px;}',
     '.d .sie-about_5 {left:58px;top:208px;width:392px;height:50px;}'),

    # about_1 texto
    ('.d .sie-about_1 {left:58px;top:300px;width:500px;height:460px !important;overflow:visible !important;}',
     '.d .sie-about_1 {left:58px;top:282px;width:540px;height:420px !important;overflow:visible !important;}'),

    # about_0 botão
    ('.d .sie-about_0 {left:58px;top:760px;width:220px;height:47px;}',
     '.d .sie-about_0 {left:58px;top:726px;width:220px;height:47px;}'),

    # Foto: top:80, height:700
    ('.d .sie-about_3 {left:620px;top:80px;width:540px;height:680px;}',
     '.d .sie-about_3 {left:620px;top:80px;width:540px;height:700px;}'),
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
