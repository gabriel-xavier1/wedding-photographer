content = open('index.html', 'r', encoding='utf-8').read()

# Replicar exatamente o padrão do investment na seção weddings
# Foto: left:24px, top:80px, width:380px (igual freebie_0)
# Texto começa em left:484px (24+380+80=484), top:80px para label
# Título: top:125px, font-size:47px
# Texto: top:209px
# Botão: top:530px
# Vídeo: top:610px (530+50+30 gap)
# Seção: height suficiente para vídeo 400px = 610+400+80 = 1090px

replacements = [
    ('.d .sib-weddings {height:980px;}',
     '.d .sib-weddings {height:1090px;}'),

    ('.d .sie-weddings_title {position:absolute;left:80px;top:80px;width:520px;height:100px;}',
     '.d .sie-weddings_title {position:absolute;left:484px;top:125px;width:560px;height:60px;}'),

    ('.d .sie-weddings_title-text {color:#ffffff;font-size:72px;line-height:1;}',
     '.d .sie-weddings_title-text {color:#ffffff;font-size:47px;line-height:1;}'),

    ('.d .sie-weddings_text {position:absolute;left:80px;top:210px;width:500px;height:200px;}',
     '.d .sie-weddings_text {position:absolute;left:484px;top:209px;width:560px;height:300px;}'),

    ('.d .sie-weddings_text-text {color:#d4cfc4;font-size:16px;line-height:1.8;text-align:left;}',
     '.d .sie-weddings_text-text {color:#d4cfc4;font-size:16px;line-height:1.8;text-align:left;}'),

    ('.d .sie-weddings_btn {position:absolute;left:80px;top:430px;width:500px;height:60px;}',
     '.d .sie-weddings_btn {position:absolute;left:484px;top:530px;width:560px;height:60px;}'),

    ('.d .sie-weddings_photo {position:absolute;right:80px;top:80px;width:460px;height:440px;}',
     '.d .sie-weddings_photo {position:absolute;left:24px;top:80px;width:380px;height:500px;}'),

    ('.d .sie-weddings_video {position:absolute;left:80px;top:530px;width:840px;height:400px;}',
     '.d .sie-weddings_video {position:absolute;left:484px;top:610px;width:560px;height:400px;}'),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        print(f'OK: {old[:50]}')
    else:
        print(f'NOT FOUND: {old[:50]}')

open('index.html', 'w', encoding='utf-8').write(content)
