content = open('index.html', 'r', encoding='utf-8').read()

replacements = [
    # Seção altura
    ('.d .sib-weddings {height:1090px;}',
     '.d .sib-weddings {height:1000px;}'),

    # Título: esquerda, top:80px, font-size do investment (47px)
    ('.d .sie-weddings_title {position:absolute;left:484px;top:125px;width:560px;height:60px;}',
     '.d .sie-weddings_title {position:absolute;left:58px;top:80px;width:520px;height:70px;}'),

    ('.d .sie-weddings_title-text {color:#ffffff;font-size:47px;line-height:1;}',
     '.d .sie-weddings_title-text {color:#ffffff;font-size:72px;line-height:1;}'),

    # Texto: esquerda, top:200px (80+70+50 gap)
    ('.d .sie-weddings_text {position:absolute;left:484px;top:209px;width:560px;height:300px;}',
     '.d .sie-weddings_text {position:absolute;left:58px;top:200px;width:500px;height:220px;}'),

    # Botão: esquerda, top:440px (200+220+20 gap)
    ('.d .sie-weddings_btn {position:absolute;left:484px;top:530px;width:560px;height:60px;}',
     '.d .sie-weddings_btn {position:absolute;left:58px;top:440px;width:500px;height:60px;}'),

    # Foto: direita, top:80px (mesmo padding de cima)
    ('.d .sie-weddings_photo {position:absolute;left:24px;top:80px;width:380px;height:500px;}',
     '.d .sie-weddings_photo {position:absolute;right:0;top:0;width:500px;height:540px;}'),

    # Vídeo: esquerda, top:540px (440+60+40 gap), largura quase total
    ('.d .sie-weddings_video {position:absolute;left:484px;top:610px;width:560px;height:400px;}',
     '.d .sie-weddings_video {position:absolute;left:58px;top:560px;width:900px;height:400px;}'),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        print(f'OK')
    else:
        print(f'NOT FOUND: {old[:60]}')

open('index.html', 'w', encoding='utf-8').write(content)
