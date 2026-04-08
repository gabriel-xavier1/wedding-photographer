content = open('index.html', 'r', encoding='utf-8').read()

# 1. Atualizar imagens no JSON do Showit
content = content.replace(
    '"id": "manual-posts_0", "blockId": "manual-posts", "m": {"x": 25, "y": 104, "w": 270, "h": 270, "a": 0}, "d": {"x": 24, "y": 179, "w": 368, "h": 366, "a": 0}, "c": {"key": "lrPZdC8eQyeEvSGzP-pMaA/135701/andres-molina--x2t5s6srfe-unsplash_1.jpg", "aspect_ratio": 1.4997}',
    '"id": "manual-posts_0", "blockId": "manual-posts", "m": {"x": 25, "y": 104, "w": 270, "h": 270, "a": 0}, "d": {"x": 24, "y": 179, "w": 368, "h": 366, "a": 0}, "c": {"key": "https://i.postimg.cc/NjPzCHwP/steph_e_iain.png", "aspect_ratio": 1.4997, "type": "asset"}'
)
content = content.replace(
    '"id": "manual-posts_3", "blockId": "manual-posts", "m": {"x": 25, "y": 478, "w": 270, "h": 270, "a": 0}, "d": {"x": 416, "y": 179, "w": 368, "h": 366, "a": 0}, "c": {"key": "SZbB5bYe-qaa6z_8X8nnNQ/135701/kaboompics_wedding-dress-shoes-bouquet-31914.jpg", "aspect_ratio": 0.66667}',
    '"id": "manual-posts_3", "blockId": "manual-posts", "m": {"x": 25, "y": 478, "w": 270, "h": 270, "a": 0}, "d": {"x": 416, "y": 179, "w": 368, "h": 366, "a": 0}, "c": {"key": "https://i.postimg.cc/ZKk9ZN6n/TS_11618.jpg", "aspect_ratio": 1.4997, "type": "asset"}'
)
content = content.replace(
    '"id": "manual-posts_5", "blockId": "manual-posts", "m": {"x": 25, "y": 855, "w": 270, "h": 270, "a": 0}, "d": {"x": 808, "y": 179, "w": 368, "h": 366, "a": 0}, "c": {"key": "BODbylQ_Yfp9oD8Up_NNXA/135701/andres-molina-d1qzc4vpybg-unsplash.jpg", "aspect_ratio": 1.5}',
    '"id": "manual-posts_5", "blockId": "manual-posts", "m": {"x": 25, "y": 855, "w": 270, "h": 270, "a": 0}, "d": {"x": 808, "y": 179, "w": 368, "h": 366, "a": 0}, "c": {"key": "https://i.postimg.cc/8zn0X6VX/ada_e_joshua.png", "aspect_ratio": 1.4997, "type": "asset"}'
)

# 2. Trocar nomes dos posts com nome centralizado + VIEW GALLERY
content = content.replace(
    '>Steph &amp; Iain<br></h3>',
    ' style="text-align:center;">Steph &amp; Iain<br><span style="font-size:12px;letter-spacing:2px;text-transform:uppercase;text-decoration:underline;">View Gallery →</span></h3>'
)
content = content.replace(
    '>Clara &amp; Edgar<br></h3>',
    ' style="text-align:center;">Clara &amp; Edgar<br><span style="font-size:12px;letter-spacing:2px;text-transform:uppercase;text-decoration:underline;">View Gallery →</span></h3>'
)
content = content.replace(
    '>Ada &amp; Joshua<br></h3>',
    ' style="text-align:center;">Ada &amp; Joshua<br><span style="font-size:12px;letter-spacing:2px;text-transform:uppercase;text-decoration:underline;">View Gallery →</span></h3>'
)

# 3. Centralizar texto dos nomes via CSS
css_add = '\n.d .sie-manual-posts_1-text, .d .sie-manual-posts_4-text, .d .sie-manual-posts_6-text {text-align:center !important;}\n'
content = content.replace('</style>', css_add + '</style>', 1)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
