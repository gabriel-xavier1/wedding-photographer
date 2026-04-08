content = open('index.html', 'r', encoding='utf-8').read()

content = content.replace(
    '.d .sie-testimonials_view-1-1_1-text {color:rgba(255,255,255,1);font-size:35px;text-align:center;}',
    '.d .sie-testimonials_view-1-1_1-text {color:rgba(255,255,255,1);font-size:20px;text-align:center;}'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
