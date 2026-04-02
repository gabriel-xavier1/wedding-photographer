with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Layout plan (desktop, bloco 700px):
# Foto: left:24, top:0, width:440, height:700 (full height)
# Coluna direita: left:548, largura:600px
#
# Vertical rhythm com 24px de gap entre elementos:
# freebie_4 subheading:  top:80,  height:24
# freebie_3 heading:     top:120, height:70  (80+24+16 gap)
# freebie_2 paragraph:   top:210, height:300 (120+70+20 gap)
# freebie_1 button:      top:530, height:50  (210+300+20 gap)
# Total: 530+50 = 580 < 700 ✓

replacements = [
    # Altura do bloco
    ('.m .sib-freebie {height:460px;}',
     '.m .sib-freebie {height:520px;}'),
    ('.d .sib-freebie {height:640px;}',
     '.d .sib-freebie {height:700px;}'),

    # Foto: full height
    ('.d .sie-freebie_0 {left:24px;top:0px;width:440px;height:640px;}',
     '.d .sie-freebie_0 {left:24px;top:0px;width:440px;height:700px;}'),

    # freebie_4 subheading
    ('.d .sie-freebie_4 {left:548px;top:120px;width:490px;height:21px;transition-duration:0.5s;transition-property:opacity;}',
     '.d .sie-freebie_4 {left:548px;top:80px;width:600px;height:24px;transition-duration:0.5s;transition-property:opacity;}'),

    # freebie_3 heading
    ('.d .sie-freebie_3 {left:548px;top:155px;width:527px;height:60px;}',
     '.d .sie-freebie_3 {left:548px;top:120px;width:600px;height:70px;}'),

    # freebie_2 paragraph
    ('.d .sie-freebie_2 {left:548px;top:235px;width:490px;height:280px;}',
     '.d .sie-freebie_2 {left:548px;top:210px;width:600px;height:300px;}'),

    # freebie_1 button
    ('.d .sie-freebie_1 {left:548px;top:535px;width:172px;height:50px;}',
     '.d .sie-freebie_1 {left:548px;top:530px;width:200px;height:50px;}'),

    # Mobile: redistribuir também
    # freebie_4 subheading mobile
    ('.m .sie-freebie_4 {left:25px;top:43px;width:249px;height:30px;transition-duration:0.5s;transition-property:opacity;}',
     '.m .sie-freebie_4 {left:25px;top:32px;width:270px;height:24px;transition-duration:0.5s;transition-property:opacity;}'),

    # freebie_3 heading mobile
    ('.m .sie-freebie_3 {left:25px;top:84px;width:209px;height:67px;}',
     '.m .sie-freebie_3 {left:25px;top:64px;width:270px;height:60px;}'),

    # freebie_2 paragraph mobile
    ('.m .sie-freebie_2 {left:25px;top:168px;width:270px;height:137px;}',
     '.m .sie-freebie_2 {left:25px;top:140px;width:270px;height:300px;}'),

    # freebie_1 button mobile
    ('.m .sie-freebie_1 {left:25px;top:370px;width:165px;height:50px;}',
     '.m .sie-freebie_1 {left:25px;top:460px;width:165px;height:50px;}'),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new, 1)
        print(f'OK: {new[:60]}')
    else:
        print(f'NOT FOUND: {old[:60]}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
