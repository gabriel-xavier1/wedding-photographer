with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

fixes = [
    # Block height
    ('.d .sib-about {height:828px;}',
     '.d .sib-about {height:920px;}'),

    # about_0 button - esquerda, alinhado abaixo do texto
    ('.d .sie-about_0 {left:686px;top:742px;width:220px;height:47px;}',
     '.d .sie-about_0 {left:58px;top:760px;width:220px;height:47px;}'),

    # about_1 texto - esquerda
    ('.d .sie-about_1 {left:686px;top:518px;width:490px;height:187px;}',
     '.d .sie-about_1 {left:58px;top:300px;width:500px;height:460px !important;overflow:visible !important;}'),

    # about_2 heading - esquerda (já está)
    # about_3 foto - direita, grande
    ('.d .sie-about_3 {left:26px;top:367px;width:585px;height:422px;}',
     '.d .sie-about_3 {left:620px;top:80px;width:540px;height:680px;}'),

    # about_4 - esconder (foto pequena de cima)
    ('.d .sie-about_4 {left:686px;top:105px;width:267px;height:343px;}',
     '.d .sie-about_4 {display:none !important;}'),
    ('.d .sie-about_4 .se-img {background-repeat:no-repeat;background-size:cover;background-position:50% 50%;border-radius:inherit;}',
     '.d .sie-about_4 .se-img {display:none !important;}'),

    # about_5 nome - esquerda
    ('.d .sie-about_5 {left:58px;top:278px;width:392px;height:50px;}',
     '.d .sie-about_5 {left:58px;top:220px;width:392px;height:50px;}'),
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
