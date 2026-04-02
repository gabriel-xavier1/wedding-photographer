with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

fixes = [
    # Subir botão: 210+260+24 = 494 → top:494
    ('.d .sie-freebie_1 {left:460px;top:550px;width:200px;height:50px;}',
     '.d .sie-freebie_1 {left:460px;top:494px;width:200px;height:50px;}'),

    # Ajustar altura do bloco: 494+50+30 = 574 → usar 580px
    ('.d .sib-freebie {height:620px;}',
     '.d .sib-freebie {height:580px;}'),

    # Foto acompanha altura do bloco
    ('.d .sie-freebie_0 {left:24px;top:0px;width:380px;height:620px;}',
     '.d .sie-freebie_0 {left:24px;top:0px;width:380px;height:580px;}'),

    # Adicionar overflow:hidden no bloco para cortar qualquer overflow
]

for old, new in fixes:
    if old in content:
        content = content.replace(old, new, 1)
        print(f'OK: {new[:70]}')
    else:
        print(f'NOT FOUND: {old[:70]}')

# Adicionar overflow:hidden na regra do bloco freebie
old_bg = '.d .sib-freebie .ss-bg {background-color:rgba(244,239,233,1);}'
new_bg = '.d .sib-freebie .ss-bg {background-color:rgba(244,239,233,1);overflow:hidden;}'
if old_bg in content:
    content = content.replace(old_bg, new_bg, 1)
    print('overflow:hidden added')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
