content = open('index.html', 'r', encoding='utf-8').read()

# Aumentar container do texto para acomodar o texto mais longo
for slide in ['view-1_1', 'view-1-1_1', 'view-1-2_1']:
    content = content.replace(
        f'.d .sie-testimonials_{slide} {{left:261px;top:160px;width:679px;height:260px;}}',
        f'.d .sie-testimonials_{slide} {{left:261px;top:100px;width:679px;height:360px;}}'
    )

# Mover nome para top:480px (100 + 360 + 20 gap)
for slide in ['view-1_0', 'view-1-1_0', 'view-1-2_0']:
    content = content.replace(
        f'.d .sie-testimonials_{slide} {{left:318px;top:430px;width:562px;height:30px;}}',
        f'.d .sie-testimonials_{slide} {{left:318px;top:480px;width:562px;height:30px;}}'
    )

# Seção: 480 + 30 + 60 = 570px
content = content.replace(
    '.d .sib-testimonials {height:620px;}',
    '.d .sib-testimonials {height:570px;}'
)
content = content.replace(
    '"slug": "testimonials"', '"slug": "testimonials"'  # no-op, height is in CSS only
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
