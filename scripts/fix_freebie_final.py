with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

fixes = [
    # Foto: largura máxima 380px para não invadir coluna de texto (que começa em 548)
    ('.d .sie-freebie_0 {left:122px;top:0px;width:440px;height:620px;}',
     '.d .sie-freebie_0 {left:24px;top:0px;width:380px;height:620px;}'),

    # Coluna de texto: mover para left:460 para dar mais espaço
    # freebie_4 subheading
    ('.d .sie-freebie_4 {left:548px;top:161px;width:490px;height:21px;transition-duration:0.5s;transition-property:opacity;}',
     '.d .sie-freebie_4 {left:460px;top:80px;width:700px;height:21px;transition-duration:0.5s;transition-property:opacity;}'),

    # freebie_3 heading
    ('.d .sie-freebie_3 {left:548px;top:192px;width:527px;height:43px;}',
     '.d .sie-freebie_3 {left:460px;top:115px;width:700px;height:60px;}'),

    # freebie_2 paragraph
    ('.d .sie-freebie_2 {left:548px;top:260px;width:490px;height:220px;}',
     '.d .sie-freebie_2 {left:460px;top:195px;width:700px;height:260px;}'),

    # freebie_1 button: abaixo do texto 195+260+24=479
    ('.d .sie-freebie_1 {left:548px;top:500px;width:172px;height:50px;}',
     '.d .sie-freebie_1 {left:460px;top:475px;width:200px;height:50px;}'),
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
