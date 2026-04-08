content = open('index.html', 'r', encoding='utf-8').read()

# Seção maior
content = content.replace(
    '.d .sib-testimonials {height:550px;}',
    '.d .sib-testimonials {height:620px;}'
)

# Título: top:50px
content = content.replace(
    '.d .sie-testimonials_0 {left:94px;top:40px;width:1012px;height:17px;}',
    '.d .sie-testimonials_0 {left:94px;top:50px;width:1012px;height:17px;}'
)

# Texto: top:100px, height:320px → termina em 420px
for slide in ['view-1_1', 'view-1-1_1', 'view-1-2_1']:
    content = content.replace(
        f'.d .sie-testimonials_{slide} {{left:261px;top:80px;width:679px;height:360px;}}',
        f'.d .sie-testimonials_{slide} {{left:261px;top:100px;width:679px;height:320px;}}'
    )

# Nome: top:450px, font-size:28px
for slide in ['view-1_0', 'view-1-1_0', 'view-1-2_0']:
    content = content.replace(
        f'.d .sie-testimonials_{slide} {{left:318px;top:460px;width:562px;height:30px;}}',
        f'.d .sie-testimonials_{slide} {{left:318px;top:450px;width:562px;height:40px;}}'
    )
    content = content.replace(
        f'.d .sie-testimonials_{slide}-text {{color:rgba(255,255,255,1);font-size:22px;letter-spacing:0.1em;text-align:center;}}',
        f'.d .sie-testimonials_{slide}-text {{color:rgba(255,255,255,1);font-size:28px;letter-spacing:0.1em;text-align:center;}}'
    )

# Setas: centradas verticalmente (620/2 = 310px)
content = content.replace(
    '.d .sie-testimonials_2 {left:24px;top:244px;width:32px;height:32px;}',
    '.d .sie-testimonials_2 {left:24px;top:294px;width:32px;height:32px;}'
)
content = content.replace(
    '.d .sie-testimonials_3 {left:1144px;top:244px;width:32px;height:32px;}',
    '.d .sie-testimonials_3 {left:1144px;top:294px;width:32px;height:32px;}'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
