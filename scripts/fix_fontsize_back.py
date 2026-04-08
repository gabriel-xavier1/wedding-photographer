content = open('index.html', 'r', encoding='utf-8').read()

for slide in ['view-1_1', 'view-1-1_1', 'view-1-2_1']:
    content = content.replace(
        f'.d .sie-testimonials_{slide}-text {{color:rgba(255,255,255,1);font-size:1.1rem;line-height:1.8;text-align:center;}}',
        f'.d .sie-testimonials_{slide}-text {{color:rgba(255,255,255,1);font-size:1.5rem;line-height:1.8;text-align:center;}}'
    )

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
