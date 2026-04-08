content = open('index.html', 'r', encoding='utf-8').read()

# Ajustar tamanho do video: left:58px, width:1142px, height:643px (16:9)
content = content.replace(
    '.d .sie-weddings_video {position:absolute;left:58px;top:640px;width:900px;height:400px;}',
    '.d .sie-weddings_video {position:absolute;left:58px;top:640px;width:1142px;height:643px;}'
)

# Ajustar altura da seção: 640 + 643 + 80 = 1363px
content = content.replace(
    '.d .sib-weddings {height:1120px;}',
    '.d .sib-weddings {height:1363px;}'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
