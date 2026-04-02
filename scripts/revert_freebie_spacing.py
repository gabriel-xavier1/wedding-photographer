with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Reverter para os valores antes do fix_freebie_spacing.py
# (estado após fix_freebie_layout.py)
reverts = [
    # Altura do bloco
    ('.m .sib-freebie {height:680px;}',
     '.m .sib-freebie {height:520px;}'),
    ('.d .sib-freebie {height:700px;}',
     '.d .sib-freebie {height:640px;}'),

    # Foto
    ('.d .sie-freebie_0 {left:24px;top:0px;width:440px;height:700px;}',
     '.d .sie-freebie_0 {left:24px;top:0px;width:440px;height:640px;}'),

    # freebie_4 subheading
    ('.d .sie-freebie_4 {left:548px;top:80px;width:600px;height:24px;transition-duration:0.5s;transition-property:opacity;}',
     '.d .sie-freebie_4 {left:548px;top:120px;width:490px;height:21px;transition-duration:0.5s;transition-property:opacity;}'),

    # freebie_3 heading
    ('.d .sie-freebie_3 {left:548px;top:120px;width:600px;height:70px;}',
     '.d .sie-freebie_3 {left:548px;top:155px;width:527px;height:60px;}'),

    # freebie_2 paragraph
    ('.d .sie-freebie_2 {left:548px;top:210px;width:600px;height:300px;}',
     '.d .sie-freebie_2 {left:548px;top:235px;width:490px;height:280px;}'),

    # freebie_1 button
    ('.d .sie-freebie_1 {left:548px;top:530px;width:200px;height:50px;}',
     '.d .sie-freebie_1 {left:548px;top:470px;width:172px;height:50px;}'),

    # Mobile
    ('.m .sie-freebie_4 {left:25px;top:236px;width:270px;height:24px;transition-duration:0.5s;transition-property:opacity;}',
     '.m .sie-freebie_4 {left:25px;top:32px;width:270px;height:24px;transition-duration:0.5s;transition-property:opacity;}'),
    ('.m .sie-freebie_3 {left:25px;top:268px;width:270px;height:50px;}',
     '.m .sie-freebie_3 {left:25px;top:64px;width:270px;height:60px;}'),
    ('.m .sie-freebie_2 {left:25px;top:328px;width:270px;height:220px;}',
     '.m .sie-freebie_2 {left:25px;top:140px;width:270px;height:300px;}'),
    ('.m .sie-freebie_1 {left:25px;top:564px;width:165px;height:50px;}',
     '.m .sie-freebie_1 {left:25px;top:460px;width:165px;height:50px;}'),
    ('.m .sie-freebie_0 {left:12px;top:0px;width:296px;height:220px;}',
     '.m .sie-freebie_0 {left:12px;top:0px;width:296px;height:220px;}'),
]

for old, new in reverts:
    if old in content:
        content = content.replace(old, new, 1)
        print(f'OK: {new[:60]}')
    else:
        print(f'NOT FOUND: {old[:60]}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
