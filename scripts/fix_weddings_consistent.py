content = open('index.html', 'r', encoding='utf-8').read()

# Botão: top:470px (texto termina 420 + gap 50px = 470)
content = content.replace(
    '.d .sie-weddings_btn {position:absolute;left:58px;top:440px;width:500px;height:60px;}',
    '.d .sie-weddings_btn {position:absolute;left:58px;top:470px;width:500px;height:60px;}'
)

# Vídeo: top:580px (botão termina 470+60=530 + gap 50px = 580)
content = content.replace(
    '.d .sie-weddings_video {position:absolute;left:58px;top:560px;width:900px;height:400px;}',
    '.d .sie-weddings_video {position:absolute;left:58px;top:580px;width:900px;height:400px;}'
)

# Seção: 580+400+80 = 1060px
content = content.replace(
    '.d .sib-weddings {height:1000px;}',
    '.d .sib-weddings {height:1060px;}'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
