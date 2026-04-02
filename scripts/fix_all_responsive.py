with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

fixes = []

# ============================================================
# FREEBIE - corrigir mobile e tablet
# ============================================================

# 1. Mostrar foto no mobile (remover display:none)
fixes.append((
    '.m .sie-freebie_0 {left:62px;top:78px;width:196px;height:272px;display:none;}',
    '.m .sie-freebie_0 {left:12px;top:0px;width:296px;height:220px;}'
))

# 2. Aumentar altura do bloco mobile para acomodar foto + texto + botão
fixes.append((
    '.m .sib-freebie {height:520px;}',
    '.m .sib-freebie {height:680px;}'
))

# 3. Redistribuir elementos mobile com foto no topo
# freebie_4 subheading
fixes.append((
    '.m .sie-freebie_4 {left:25px;top:32px;width:270px;height:24px;transition-duration:0.5s;transition-property:opacity;}',
    '.m .sie-freebie_4 {left:25px;top:236px;width:270px;height:24px;transition-duration:0.5s;transition-property:opacity;}'
))

# freebie_3 heading
fixes.append((
    '.m .sie-freebie_3 {left:25px;top:64px;width:270px;height:60px;}',
    '.m .sie-freebie_3 {left:25px;top:268px;width:270px;height:50px;}'
))

# freebie_2 paragraph
fixes.append((
    '.m .sie-freebie_2 {left:25px;top:140px;width:270px;height:300px;}',
    '.m .sie-freebie_2 {left:25px;top:328px;width:270px;height:220px;}'
))

# freebie_1 button - abaixo do texto com margem
fixes.append((
    '.m .sie-freebie_1 {left:25px;top:460px;width:165px;height:50px;}',
    '.m .sie-freebie_1 {left:25px;top:564px;width:165px;height:50px;}'
))

# ============================================================
# ABOUT - corrigir mobile
# ============================================================

# Aumentar altura do bloco mobile
fixes.append((
    '.m .sib-about {height:740px;}',
    '.m .sib-about {height:780px;}'
))

# Foto mobile - maior e melhor posicionada
fixes.append((
    '.m .sie-about_3 {left:12px;top:63px;width:222px;height:143px;}',
    '.m .sie-about_3 {left:12px;top:40px;width:296px;height:190px;}'
))

# about_2 "HI I AM" - abaixo da foto
fixes.append((
    '.m .sie-about_2 {left:25px;top:239px;width:233px;height:67px;}',
    '.m .sie-about_2 {left:25px;top:248px;width:233px;height:50px;}'
))

# about_5 "Jacque." - nome
fixes.append((
    '.m .sie-about_5 {left:25px;top:301px;width:233px;height:29px;}',
    '.m .sie-about_5 {left:25px;top:306px;width:233px;height:36px;}'
))

# about_1 texto principal
fixes.append((
    '.m .sie-about_1 {left:25px;top:345px;width:270px;height:249px;}',
    '.m .sie-about_1 {left:25px;top:352px;width:270px;height:320px;}'
))

# about_0 botão - remover inline style e posicionar abaixo do texto
fixes.append((
    'class="sie-about_0 se" data-sid="about_0" style="top:713px"',
    'class="sie-about_0 se" data-sid="about_0"'
))

fixes.append((
    '.m .sie-about_0 {left:25px;top:580px;width:180px;height:45px;}',
    '.m .sie-about_0 {left:25px;top:690px;width:180px;height:45px;}'
))

# ============================================================
# Aplicar
# ============================================================
for old, new in fixes:
    if old in content:
        content = content.replace(old, new, 1)
        print(f'OK: {new[:65]}')
    else:
        print(f'NOT FOUND: {old[:65]}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('\nDone.')
