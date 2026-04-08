content = open('index.html', 'r', encoding='utf-8').read()

# Reverter seção e nome para valores menores
content = content.replace(
    '.d .sib-testimonials {height:650px;}',
    '.d .sib-testimonials {height:550px;}'
)

for slide in ['view-1_1', 'view-1-1_1', 'view-1-2_1']:
    content = content.replace(
        f'.d .sie-testimonials_{slide} {{left:261px;top:177px;width:679px;height:300px;}}',
        f'.d .sie-testimonials_{slide} {{left:261px;top:177px;width:679px;height:220px;}}'
    )

for slide in ['view-1_0', 'view-1-1_0', 'view-1-2_0']:
    content = content.replace(
        f'.d .sie-testimonials_{slide} {{left:318px;top:490px;width:562px;height:40px;}}',
        f'.d .sie-testimonials_{slide} {{left:318px;top:410px;width:562px;height:40px;}}'
    )

content = content.replace(
    '.d .sie-testimonials_2 {left:24px;top:310px;width:32px;height:32px;}',
    '.d .sie-testimonials_2 {left:24px;top:252px;width:32px;height:32px;}'
)
content = content.replace(
    '.d .sie-testimonials_3 {left:1144px;top:310px;width:32px;height:32px;}',
    '.d .sie-testimonials_3 {left:1144px;top:252px;width:32px;height:32px;}'
)

# Font-size menor só para o slide 3 (Patrick & Samantha) via CSS override
css_override = '\n.d .sie-testimonials_view-1-2_1-text {font-size:1.0rem !important;line-height:1.8 !important;}\n'
content = content.replace('</style>', css_override + '</style>', 1)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
