with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

fixes = [
    # Reduzir altura do parágrafo para o real (texto ocupa ~220px)
    ('.d .sie-freebie_2 {left:460px;top:195px;width:560px;height:280px;}',
     '.d .sie-freebie_2 {left:460px;top:195px;width:560px;height:220px;}'),

    # Botão: 195+220+16 = 431
    ('.d .sie-freebie_1 {left:460px;top:475px;width:220px;height:50px;}',
     '.d .sie-freebie_1 {left:460px;top:431px;width:220px;height:50px;}'),

    # Reduzir altura do bloco: 431+50+30 = 511 → 520px
    ('.d .sib-freebie {height:590px;}',
     '.d .sib-freebie {height:520px;}'),

    # Foto acompanha
    ('.d .sie-freebie_0 {left:24px;top:0px;width:380px;height:590px;}',
     '.d .sie-freebie_0 {left:24px;top:0px;width:380px;height:520px;}'),
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
