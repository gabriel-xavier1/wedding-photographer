with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Sistema de espaçamento consistente: gap de 24px entre todos os elementos
# freebie_4 subheading: top:60, height:21 → termina em 81
# freebie_3 heading:    top:105 (81+24), height:60 → termina em 165
# freebie_2 paragraph:  top:189 (165+24), height:220 → termina em 409
# freebie_1 button:     top:433 (409+24), height:50
# bloco: 433+50+37 = 520 ✓

fixes = [
    ('.d .sie-freebie_4 {left:460px;top:67px;width:560px;height:21px;transition-duration:0.5s;transition-property:opacity;}',
     '.d .sie-freebie_4 {left:460px;top:60px;width:560px;height:21px;transition-duration:0.5s;transition-property:opacity;}'),

    ('.d .sie-freebie_3 {left:460px;top:115px;width:560px;height:60px;}',
     '.d .sie-freebie_3 {left:460px;top:105px;width:560px;height:60px;}'),

    ('.d .sie-freebie_2 {left:460px;top:195px;width:560px;height:220px;}',
     '.d .sie-freebie_2 {left:460px;top:189px;width:560px;height:220px;}'),

    ('.d .sie-freebie_1 {left:460px;top:431px;width:220px;height:50px;}',
     '.d .sie-freebie_1 {left:460px;top:433px;width:220px;height:50px;}'),
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
