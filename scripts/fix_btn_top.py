content = open('index.html', 'r', encoding='utf-8').read()

content = content.replace(
    '.d .sie-weddings_btn {position:absolute;left:58px;top:440px;width:500px;height:60px;}',
    '.d .sie-weddings_btn {position:absolute;left:58px;top:500px;width:500px;height:60px;}'
)

# Vídeo: 500+60+80 = 640px
content = content.replace(
    '.d .sie-weddings_video {position:absolute;left:58px;top:560px;width:900px;height:400px;}',
    '.d .sie-weddings_video {position:absolute;left:58px;top:640px;width:900px;height:400px;}'
)

# Seção: 640+400+80 = 1120px
content = content.replace(
    '.d .sib-weddings {height:1000px;}',
    '.d .sib-weddings {height:1120px;}'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
