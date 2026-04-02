with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Analisando a imagem:
# - Foto começa em top:60 mas visualmente parece colada ao topo
# - Botão termina em 433+50=483, bloco tem 543px → espaço em baixo = 60px
# - Mas a foto parece colada ao topo visualmente
# 
# O problema: o bloco anterior (manual-posts) pode ter margin/padding
# A solução é aumentar o top da foto e de todos os elementos
# 
# Novo plano com 80px de padding em cima e em baixo:
# - Foto: top:80, height = bloco - 80 - 80
# - Subheading: top:80
# - Heading: top:80+21+24=125
# - Paragraph: top:125+60+24=209
# - Button: top:209+220+24=453
# - Bloco: 453+50+80 = 583px
# - Foto height: 583-80-80 = 423px

fixes = [
    # Bloco
    ('.d .sib-freebie {height:543px;}',
     '.d .sib-freebie {height:583px;}'),

    # Foto
    ('.d .sie-freebie_0 {left:24px;top:60px;width:380px;height:423px;}',
     '.d .sie-freebie_0 {left:24px;top:80px;width:380px;height:423px;}'),

    # Subheading
    ('.d .sie-freebie_4 {left:460px;top:60px;width:560px;height:21px;transition-duration:0.5s;transition-property:opacity;}',
     '.d .sie-freebie_4 {left:460px;top:80px;width:560px;height:21px;transition-duration:0.5s;transition-property:opacity;}'),

    # Heading: 80+21+24=125
    ('.d .sie-freebie_3 {left:460px;top:105px;width:560px;height:60px;}',
     '.d .sie-freebie_3 {left:460px;top:125px;width:560px;height:60px;}'),

    # Paragraph: 125+60+24=209
    ('.d .sie-freebie_2 {left:460px;top:189px;width:560px;height:220px;}',
     '.d .sie-freebie_2 {left:460px;top:209px;width:560px;height:220px;}'),

    # Button: 209+220+24=453
    ('.d .sie-freebie_1 {left:460px;top:433px;width:220px;height:50px;}',
     '.d .sie-freebie_1 {left:460px;top:453px;width:220px;height:50px;}'),
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
