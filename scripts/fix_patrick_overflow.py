content = open('index.html', 'r', encoding='utf-8').read()

# Aumentar seção para 650px
content = content.replace(
    '.d .sib-testimonials {height:550px;}',
    '.d .sib-testimonials {height:650px;}'
)

# Aumentar container do texto para 300px (acomoda Patrick)
for slide in ['view-1_1', 'view-1-1_1', 'view-1-2_1']:
    content = content.replace(
        f'.d .sie-testimonials_{slide} {{left:261px;top:177px;width:679px;height:240px;}}',
        f'.d .sie-testimonials_{slide} {{left:261px;top:177px;width:679px;height:300px;}}'
    )

# Nome: top:490px (177 + 300 + 13px gap)
for slide in ['view-1_0', 'view-1-1_0', 'view-1-2_0']:
    content = content.replace(
        f'.d .sie-testimonials_{slide} {{left:318px;top:430px;width:562px;height:40px;}}',
        f'.d .sie-testimonials_{slide} {{left:318px;top:490px;width:562px;height:40px;}}'
    )

# Setas: centradas na seção 650/2 = 325px
content = content.replace(
    '.d .sie-testimonials_2 {left:24px;top:252px;width:32px;height:32px;}',
    '.d .sie-testimonials_2 {left:24px;top:310px;width:32px;height:32px;}'
)
content = content.replace(
    '.d .sie-testimonials_3 {left:1144px;top:252px;width:32px;height:32px;}',
    '.d .sie-testimonials_3 {left:1144px;top:310px;width:32px;height:32px;}'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
