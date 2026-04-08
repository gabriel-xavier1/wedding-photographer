content = open('index.html', 'r', encoding='utf-8').read()

# Restaurar posicionamento original
# Título: top:122px (original)
content = content.replace(
    '.d .sie-testimonials_0 {left:94px;top:50px;width:1012px;height:17px;}',
    '.d .sie-testimonials_0 {left:94px;top:122px;width:1012px;height:17px;}'
)

# Texto: top:177px, height:190px (original)
for slide in ['view-1_1', 'view-1-1_1', 'view-1-2_1']:
    content = content.replace(
        f'.d .sie-testimonials_{slide} {{left:261px;top:100px;width:679px;height:320px;}}',
        f'.d .sie-testimonials_{slide} {{left:261px;top:177px;width:679px;height:240px;}}'
    )

# Nome: top:394px (original era 394px)
for slide in ['view-1_0', 'view-1-1_0', 'view-1-2_0']:
    content = content.replace(
        f'.d .sie-testimonials_{slide} {{left:318px;top:450px;width:562px;height:40px;}}',
        f'.d .sie-testimonials_{slide} {{left:318px;top:430px;width:562px;height:40px;}}'
    )

# Setas: top:252px (original)
content = content.replace(
    '.d .sie-testimonials_2 {left:24px;top:294px;width:32px;height:32px;}',
    '.d .sie-testimonials_2 {left:24px;top:252px;width:32px;height:32px;}'
)
content = content.replace(
    '.d .sie-testimonials_3 {left:1144px;top:294px;width:32px;height:32px;}',
    '.d .sie-testimonials_3 {left:1144px;top:252px;width:32px;height:32px;}'
)

# Seção: 550px
content = content.replace(
    '.d .sib-testimonials {height:620px;}',
    '.d .sib-testimonials {height:550px;}'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
