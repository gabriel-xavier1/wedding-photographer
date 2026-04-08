content = open('index.html', 'r', encoding='utf-8').read()

# Nome: top:417px (177 + 220 + 20px gap)
for slide in ['view-1_0', 'view-1-1_0', 'view-1-2_0']:
    content = content.replace(
        f'.d .sie-testimonials_{slide} {{left:318px;top:410px;width:562px;height:40px;}}',
        f'.d .sie-testimonials_{slide} {{left:318px;top:417px;width:562px;height:40px;}}'
    )

# Remover override de font-size do slide 3 (texto novo é menor)
content = content.replace(
    '\n.d .sie-testimonials_view-1-2_1-text {font-size:1.0rem !important;line-height:1.8 !important;}\n',
    '\n'
)

# Garantir font-size 1.4rem para todos os slides
for slide in ['view-1_1', 'view-1-1_1', 'view-1-2_1']:
    # Corrigir qualquer variação
    import re
    content = re.sub(
        rf'(\.d \.sie-testimonials_{slide}-text \{{color:rgba\(255,255,255,1\);font-size:)[^;]+(;)',
        r'\g<1>1.4rem\2',
        content
    )

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
