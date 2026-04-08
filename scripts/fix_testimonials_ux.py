content = open('index.html', 'r', encoding='utf-8').read()

# Aumentar container do texto para os 3 slides
for slide in ['view-1_1', 'view-1-1_1', 'view-1-2_1']:
    content = content.replace(
        f'.d .sie-testimonials_{slide} {{left:261px;top:177px;width:679px;height:190px;}}',
        f'.d .sie-testimonials_{slide} {{left:261px;top:160px;width:679px;height:260px;}}'
    )

# Font-size do texto menor + line-height para respirar
for slide in ['view-1_1', 'view-1-1_1', 'view-1-2_1']:
    content = content.replace(
        f'.d .sie-testimonials_{slide}-text {{color:rgba(255,255,255,1);font-size:1.5rem;text-align:center;}}',
        f'.d .sie-testimonials_{slide}-text {{color:rgba(255,255,255,1);font-size:1.1rem;line-height:1.8;text-align:center;}}'
    )

# Nome menor: 32px -> 22px, subir um pouco
for slide in ['view-1_0', 'view-1-1_0', 'view-1-2_0']:
    content = content.replace(
        f'.d .sie-testimonials_{slide}-text {{color:rgba(255,255,255,1);font-size:32px;text-align:center;}}',
        f'.d .sie-testimonials_{slide}-text {{color:rgba(255,255,255,1);font-size:22px;letter-spacing:0.1em;text-align:center;}}'
    )
    content = content.replace(
        f'.d .sie-testimonials_{slide} {{left:318px;top:394px;width:562px;height:34px;}}',
        f'.d .sie-testimonials_{slide} {{left:318px;top:430px;width:562px;height:30px;}}'
    )

# Setas - ver tamanho atual
import re
arrows = re.findall(r'[^\n]*testimonials_[23][^\n]*\{[^\}]+\}', content)
for a in arrows:
    print(a)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
