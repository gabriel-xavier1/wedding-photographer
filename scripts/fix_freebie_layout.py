with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Foto: preencher altura total do bloco (640px), começar do topo, largura maior
    ('.d .sie-freebie_0 {left:122px;top:67px;width:357px;height:457px;}',
     '.d .sie-freebie_0 {left:24px;top:0px;width:440px;height:640px;}'),

    # freebie_4 subheading "HOW MUCH WILL IT COST?" - descer um pouco
    ('.d .sie-freebie_4 {left:548px;top:161px;width:490px;height:21px;transition-duration:0.5s;transition-property:opacity;}',
     '.d .sie-freebie_4 {left:548px;top:120px;width:490px;height:21px;transition-duration:0.5s;transition-property:opacity;}'),

    # freebie_3 heading "Investments"
    ('.d .sie-freebie_3 {left:548px;top:192px;width:527px;height:43px;}',
     '.d .sie-freebie_3 {left:548px;top:155px;width:527px;height:60px;}'),

    # freebie_2 paragraph - mais espaço e altura maior para o texto longo
    ('.d .sie-freebie_2 {left:548px;top:260px;width:490px;height:96px;}',
     '.d .sie-freebie_2 {left:548px;top:235px;width:490px;height:280px;}'),

    # freebie_1 botão - logo abaixo do texto (235+280+20=535)
    ('.d .sie-freebie_1 {left:548px;top:470px;width:172px;height:50px;}',
     '.d .sie-freebie_1 {left:548px;top:535px;width:172px;height:50px;}'),

    # Altura do bloco desktop para acomodar tudo
    ('.d .sib-freebie {height:640px;}',
     '.d .sib-freebie {height:640px;}'),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new, 1)
        print(f'OK: {old[:50]}...')
    else:
        print(f'NOT FOUND: {old[:50]}...')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
