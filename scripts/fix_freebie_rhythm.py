with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Seguindo o ritmo da imagem de referência:
# subheading top:67, heading top:110 (gap:43), paragraph top:210 (gap:100), button top:490 (gap:80 após texto)
# Bloco: 590px original → com texto mais longo precisa de 620px

fixes = [
    # freebie_4 subheading: top:67 (como no original)
    ('.d .sie-freebie_4 {left:460px;top:80px;width:700px;height:21px;transition-duration:0.5s;transition-property:opacity;}',
     '.d .sie-freebie_4 {left:460px;top:67px;width:700px;height:21px;transition-duration:0.5s;transition-property:opacity;}'),

    # freebie_3 heading: top:110 (67+21+22 gap)
    ('.d .sie-freebie_3 {left:460px;top:115px;width:700px;height:60px;}',
     '.d .sie-freebie_3 {left:460px;top:110px;width:700px;height:60px;}'),

    # freebie_2 paragraph: top:210 (110+60+40 gap — respiro generoso como no original)
    ('.d .sie-freebie_2 {left:460px;top:195px;width:700px;height:260px;}',
     '.d .sie-freebie_2 {left:460px;top:210px;width:700px;height:260px;}'),

    # freebie_1 button: top:550 (210+260+80 gap — mesmo respiro da imagem de referência)
    ('.d .sie-freebie_1 {left:460px;top:475px;width:200px;height:50px;}',
     '.d .sie-freebie_1 {left:460px;top:550px;width:200px;height:50px;}'),

    # Bloco: 550+50+20 = 620px ✓ já está correto
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
