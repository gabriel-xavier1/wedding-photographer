with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

fixes = []

# 1. Remover texto hero_1 (subheading "wedding photography in british columbia...")
fixes.append((
    '>wedding photography in british columbia, and beyond</h1>',
    '></h1>'
))

# 2. Remover texto hero_3 (italic "(aka couples who feel most at home in the wild)")
fixes.append((
    '><i>(aka couples who feel most at home in the wild)</i><br></p>',
    '></p>'
))

# 3. Esconder hero_1 e hero_3 via CSS (display:none) para não ocupar espaço
fixes.append((
    '.d .sie-hero_1 {left:84px;top:249px;width:1032px;height:16px;}',
    '.d .sie-hero_1 {left:84px;top:249px;width:1032px;height:16px;display:none;}'
))
fixes.append((
    '.m .sie-hero_1 {left:21px;top:136px;width:278px;height:33px;}',
    '.m .sie-hero_1 {left:21px;top:136px;width:278px;height:33px;display:none;}'
))
fixes.append((
    '.d .sie-hero_3 {left:84px;top:475px;width:1032px;height:36px;}',
    '.d .sie-hero_3 {left:84px;top:475px;width:1032px;height:36px;display:none;}'
))
fixes.append((
    '.m .sie-hero_3 {left:62px;top:259px;width:195px;height:42px;}',
    '.m .sie-hero_3 {left:62px;top:259px;width:195px;height:42px;display:none;}'
))

# 4. Reposicionar hero_2 (título "for the real memories") - centrado verticalmente
# Desktop: bloco 800px, título height:165 → top = (800-165-48-43)/2 = 272 → ~280
fixes.append((
    '.d .sie-hero_2 {left:208px;top:290px;width:785px;height:165px;}',
    '.d .sie-hero_2 {left:208px;top:280px;width:785px;height:165px;}'
))

# 5. Botão desktop: top = 280+165+48 = 493
fixes.append((
    '.d .sie-hero_4 {left:490px;top:546px;width:220px;height:43px;}',
    '.d .sie-hero_4 {left:490px;top:493px;width:220px;height:43px;}'
))

# 6. Mobile: título centrado, bloco 480px
# hero_2 mobile: top = (480-64-40-43)/2 = 166 → ~170
fixes.append((
    '.m .sie-hero_2 {left:12px;top:186px;width:296px;height:64px;}',
    '.m .sie-hero_2 {left:12px;top:170px;width:296px;height:64px;}'
))

# 7. Botão mobile: top = 170+64+40 = 274
fixes.append((
    '.m .sie-hero_4 {left:60px;top:322px;width:200px;height:43px;}',
    '.m .sie-hero_4 {left:60px;top:274px;width:200px;height:43px;}'
))

for old, new in fixes:
    if old in content:
        content = content.replace(old, new, 1)
        print(f'OK: {new[:70]}')
    else:
        print(f'NOT FOUND: {old[:70]}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('\nDone.')
