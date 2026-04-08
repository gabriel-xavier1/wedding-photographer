content = open('index.html', 'r', encoding='utf-8').read()

# Igualar setas: ambas 46x46 no desktop
content = content.replace(
    '.d .sie-testimonials_2 {left:1px;top:252px;width:46px;height:47px;}',
    '.d .sie-testimonials_2 {left:1px;top:252px;width:46px;height:46px;}'
)
content = content.replace(
    '.d .sie-testimonials_3 {left:1153px;top:252px;width:46px;height:47px;}',
    '.d .sie-testimonials_3 {left:1153px;top:252px;width:46px;height:46px;}'
)

# Adicionar line-height nos textos dos 3 slides via CSS inline override
content = content.replace(
    '.d .sie-testimonials_view-1_1-text {color:rgba(255,255,255,1);font-size:1.5rem;text-align:center;}',
    '.d .sie-testimonials_view-1_1-text {color:rgba(255,255,255,1);font-size:1.1rem;line-height:1.9;text-align:center;}'
)
content = content.replace(
    '.d .sie-testimonials_view-1-1_1-text {color:rgba(255,255,255,1);font-size:1.5rem;text-align:center;}',
    '.d .sie-testimonials_view-1-1_1-text {color:rgba(255,255,255,1);font-size:1.1rem;line-height:1.9;text-align:center;}'
)
content = content.replace(
    '.d .sie-testimonials_view-1-2_1-text {color:rgba(255,255,255,1);font-size:1.5rem;text-align:center;}',
    '.d .sie-testimonials_view-1-2_1-text {color:rgba(255,255,255,1);font-size:1.1rem;line-height:1.9;text-align:center;}'
)

# Aumentar container dos textos para acomodar line-height maior
for slide in ['view-1_1', 'view-1-1_1', 'view-1-2_1']:
    content = content.replace(
        f'.d .sie-testimonials_{slide} {{left:261px;top:177px;width:679px;height:190px;}}',
        f'.d .sie-testimonials_{slide} {{left:261px;top:140px;width:679px;height:280px;}}'
    )

# Seção testimonials: aumentar altura para acomodar
content = content.replace(
    '"slug": "testimonials", "visible": "a", "states": [{"d": {"bgFillType": "color", "bgColor": "#000000:0", "bgMediaType": "none"}, "m": {"bgFillType": "color", "bgColor": "#000000:0", "bgMediaType": "none"}, "slug": "view-1"}, {"d": {"bgFillType": "color", "bgColor": "#000000:0", "bgMediaType": "none"}, "m": {"bgFillType": "color", "bgColor": "#000000:0", "bgMediaType": "none"}, "slug": "view-1-1"}, {"d": {"bgFillType": "color", "bgColor": "#000000:0", "bgMediaType": "none"}, "m": {"bgFillType": "color", "bgColor": "#000000:0", "bgMediaType": "none"}, "slug": "view-1-2"}], "d": {"h": 550,',
    '"slug": "testimonials", "visible": "a", "states": [{"d": {"bgFillType": "color", "bgColor": "#000000:0", "bgMediaType": "none"}, "m": {"bgFillType": "color", "bgColor": "#000000:0", "bgMediaType": "none"}, "slug": "view-1"}, {"d": {"bgFillType": "color", "bgColor": "#000000:0", "bgMediaType": "none"}, "m": {"bgFillType": "color", "bgColor": "#000000:0", "bgMediaType": "none"}, "slug": "view-1-1"}, {"d": {"bgFillType": "color", "bgColor": "#000000:0", "bgMediaType": "none"}, "m": {"bgFillType": "color", "bgColor": "#000000:0", "bgMediaType": "none"}, "slug": "view-1-2"}], "d": {"h": 620,'
)
content = content.replace(
    '.d .sib-testimonials {height:550px;}',
    '.d .sib-testimonials {height:620px;}'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
