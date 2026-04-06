content = open('index.html', 'r', encoding='utf-8').read()

# Cor de fundo: trocar #2c2e1e pelo marrom da seção offers
content = content.replace(
    '.d .sib-weddings {height:980px;background-color:#2c2e1e;}',
    '.d .sib-weddings {height:980px;}'
)
content = content.replace(
    '.m .sib-weddings {height:1200px;background-color:#2c2e1e;}',
    '.m .sib-weddings {height:1200px;}'
)

# Adicionar bg color no ss-bg como o offers faz
content = content.replace(
    '.d .sie-weddings_title {position:absolute;left:58px;top:60px;width:520px;height:120px;}',
    '.d .sib-weddings .ss-bg {background-color:rgba(41,38,36,1);}\n.m .sib-weddings .ss-bg {background-color:rgba(41,38,36,1);}\n.d .sie-weddings_title {position:absolute;left:80px;top:80px;width:520px;height:100px;}'
)

# Ajustar espaçamentos
content = content.replace(
    '.d .sie-weddings_title-text {color:#ffffff;font-size:80px;line-height:1;}',
    '.d .sie-weddings_title-text {color:#ffffff;font-size:72px;line-height:1;}'
)
content = content.replace(
    '.d .sie-weddings_text {position:absolute;left:58px;top:200px;width:500px;height:200px;}',
    '.d .sie-weddings_text {position:absolute;left:80px;top:210px;width:500px;height:200px;}'
)
content = content.replace(
    '.d .sie-weddings_btn {position:absolute;left:58px;top:430px;width:320px;height:30px;}',
    '.d .sie-weddings_btn {position:absolute;left:80px;top:430px;width:500px;height:60px;}'
)
content = content.replace(
    '.d .sie-weddings_photo {position:absolute;right:0;top:0;width:500px;height:480px;}',
    '.d .sie-weddings_photo {position:absolute;right:80px;top:80px;width:460px;height:440px;}'
)
content = content.replace(
    '.d .sie-weddings_video {position:absolute;left:58px;top:510px;width:900px;height:420px;}',
    '.d .sie-weddings_video {position:absolute;left:80px;top:530px;width:840px;height:400px;}'
)
content = content.replace(
    '.m .sie-weddings_title {position:absolute;left:25px;top:50px;width:270px;height:80px;}',
    '.m .sie-weddings_title {position:absolute;left:25px;top:60px;width:270px;height:80px;}'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
