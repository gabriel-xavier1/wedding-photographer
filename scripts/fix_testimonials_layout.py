content = open('index.html', 'r', encoding='utf-8').read()

# Título "WHAT THE MOST AMAZING PEOPLE SAY..."
content = content.replace(
    '.d .sie-testimonials_0 {left:94px;top:122px;width:1012px;height:17px;}',
    '.d .sie-testimonials_0 {left:94px;top:40px;width:1012px;height:17px;}'
)

# Texto: começa em top:80px, height:360px → termina em 440px
for slide in ['view-1_1', 'view-1-1_1', 'view-1-2_1']:
    content = content.replace(
        f'.d .sie-testimonials_{slide} {{left:261px;top:100px;width:679px;height:360px;}}',
        f'.d .sie-testimonials_{slide} {{left:261px;top:80px;width:679px;height:360px;}}'
    )

# Nome: top:460px (440 + 20px gap)
for slide in ['view-1_0', 'view-1-1_0', 'view-1-2_0']:
    content = content.replace(
        f'.d .sie-testimonials_{slide} {{left:318px;top:480px;width:562px;height:30px;}}',
        f'.d .sie-testimonials_{slide} {{left:318px;top:460px;width:562px;height:30px;}}'
    )

# Setas: centradas verticalmente (80 + 360/2 = 260px)
content = content.replace(
    '.d .sie-testimonials_2 {left:24px;top:260px;width:32px;height:32px;}',
    '.d .sie-testimonials_2 {left:24px;top:244px;width:32px;height:32px;}'
)
content = content.replace(
    '.d .sie-testimonials_3 {left:1144px;top:260px;width:32px;height:32px;}',
    '.d .sie-testimonials_3 {left:1144px;top:244px;width:32px;height:32px;}'
)

# Seção: 460 + 30 + 60 = 550px
content = content.replace(
    '.d .sib-testimonials {height:570px;}',
    '.d .sib-testimonials {height:550px;}'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
