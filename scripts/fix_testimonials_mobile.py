content = open('index.html', 'r', encoding='utf-8').read()

# 1. Reduzir font-size mobile para caber melhor
for slide in ['view-1_1', 'view-1-1_1', 'view-1-2_1']:
    content = content.replace(
        f'.m .sie-testimonials_{slide}-text {{color:rgba(255,255,255,1);font-size:23px;text-align:center;}}',
        f'.m .sie-testimonials_{slide}-text {{color:rgba(255,255,255,1);font-size:16px;line-height:1.7;text-align:center;}}'
    )

# 2. Aumentar container do texto mobile: height 194px -> 320px
for slide in ['view-1_1', 'view-1-1_1', 'view-1-2_1']:
    content = content.replace(
        f'.m .sie-testimonials_{slide} {{left:23px;top:97px;width:270px;height:194px;}}',
        f'.m .sie-testimonials_{slide} {{left:23px;top:97px;width:270px;height:320px;}}'
    )

# view-1-2_1 tem left:21px
content = content.replace(
    '.m .sie-testimonials_view-1-2_1 {left:21px;top:97px;width:278px;height:194px;}',
    '.m .sie-testimonials_view-1-2_1 {left:21px;top:97px;width:278px;height:320px;}'
)

# 3. Mover nome para top:430px (97+320+13)
for slide in ['view-1_0', 'view-1-1_0', 'view-1-2_0']:
    content = content.replace(
        f'.m .sie-testimonials_{slide} {{left:45px;top:312px;width:230px;height:25px;}}',
        f'.m .sie-testimonials_{slide} {{left:45px;top:430px;width:230px;height:25px;}}'
    )

# 4. Aumentar seção mobile
content = content.replace(
    '"slug": "testimonials"', '"slug": "testimonials"'  # placeholder
)
# Atualizar height mobile da seção via CSS
content = content.replace(
    '.m .sib-testimonials {height:445px;}',
    '.m .sib-testimonials {height:520px;}'
)

# 5. Reduzir font-size do nome no mobile
for slide in ['view-1_0', 'view-1-1_0', 'view-1-2_0']:
    content = content.replace(
        f'.m .sie-testimonials_{slide}-text {{color:rgba(255,255,255,1);font-size:26px;text-align:center;}}',
        f'.m .sie-testimonials_{slide}-text {{color:rgba(255,255,255,1);font-size:20px;text-align:center;}}'
    )

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
