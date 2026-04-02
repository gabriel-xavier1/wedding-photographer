with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

fixes = [
    # Reduzir largura do parágrafo para texto mais fluido
    ('.d .sie-freebie_2 {left:460px;top:195px;width:700px;height:260px;}',
     '.d .sie-freebie_2 {left:460px;top:195px;width:560px;height:280px;}'),

    # Subheading e heading também mais estreitos para consistência
    ('.d .sie-freebie_4 {left:460px;top:67px;width:700px;height:21px;transition-duration:0.5s;transition-property:opacity;}',
     '.d .sie-freebie_4 {left:460px;top:67px;width:560px;height:21px;transition-duration:0.5s;transition-property:opacity;}'),

    ('.d .sie-freebie_3 {left:460px;top:115px;width:700px;height:60px;}',
     '.d .sie-freebie_3 {left:460px;top:115px;width:560px;height:60px;}'),

    # Botão: abaixo do texto 195+280+24 = 499
    ('.d .sie-freebie_1 {left:460px;top:475px;width:200px;height:50px;}',
     '.d .sie-freebie_1 {left:460px;top:499px;width:200px;height:50px;}'),

    # Altura do bloco: 499+50+30 = 579 → 590px
    ('.d .sib-freebie {height:590px;}',
     '.d .sib-freebie {height:590px;}'),  # já está correto

    # Foto acompanha
    ('.d .sie-freebie_0 {left:24px;top:0px;width:380px;height:590px;}',
     '.d .sie-freebie_0 {left:24px;top:0px;width:380px;height:590px;}'),
]

for old, new in fixes:
    if old == new:
        print(f'SKIP (same): {old[:60]}')
        continue
    if old in content:
        content = content.replace(old, new, 1)
        print(f'OK: {new[:70]}')
    else:
        print(f'NOT FOUND: {old[:70]}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
