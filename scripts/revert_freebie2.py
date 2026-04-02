with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

reverts = [
    # Altura mobile - original era 420px
    ('.m .sib-freebie {height:560px;}',
     '.m .sib-freebie {height:420px;}'),

    # Foto mobile - original era display:none
    ('.m .sie-freebie_0 {left:12px;top:0px;width:296px;height:200px;}',
     '.m .sie-freebie_0 {left:62px;top:78px;width:196px;height:272px;display:none;}'),

    # freebie_4 mobile
    ('.m .sie-freebie_4 {left:25px;top:216px;width:270px;height:24px;transition-duration:0.5s;transition-property:opacity;}',
     '.m .sie-freebie_4 {left:25px;top:43px;width:249px;height:30px;transition-duration:0.5s;transition-property:opacity;}'),

    # freebie_3 mobile
    ('.m .sie-freebie_3 {left:25px;top:248px;width:270px;height:50px;}',
     '.m .sie-freebie_3 {left:25px;top:84px;width:209px;height:67px;}'),

    # freebie_2 mobile
    ('.m .sie-freebie_2 {left:25px;top:308px;width:270px;height:160px;}',
     '.m .sie-freebie_2 {left:25px;top:168px;width:270px;height:137px;}'),

    # freebie_1 button mobile
    ('.m .sie-freebie_1 {left:25px;top:484px;width:165px;height:50px;}',
     '.m .sie-freebie_1 {left:25px;top:326px;width:165px;height:50px;}'),
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
