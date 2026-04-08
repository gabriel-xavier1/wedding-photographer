content = open('index.html', 'r', encoding='utf-8').read()

# 1. Titulo "galleries" -> "Galleries"
content = content.replace('>galleries</h2>', '>Galleries</h2>')

# 2. Textos: mover top de 571px para 591px (20px gap)
content = content.replace(
    '.d .sie-manual-posts_1 {left:24px;top:571px;width:368px;height:89px;',
    '.d .sie-manual-posts_1 {left:24px;top:591px;width:368px;height:89px;'
)
content = content.replace(
    '.d .sie-manual-posts_4 {left:416px;top:571px;width:368px;height:89px;',
    '.d .sie-manual-posts_4 {left:416px;top:591px;width:368px;height:89px;'
)
content = content.replace(
    '.d .sie-manual-posts_6 {left:808px;top:571px;width:368px;height:89px;',
    '.d .sie-manual-posts_6 {left:808px;top:591px;width:368px;height:89px;'
)

# 3. Adicionar CSS override para forçar background-image via CSS (mais confiável)
css = '''
.d .sie-manual-posts_0 .se-img {background-image:url('https://i.postimg.cc/NjPzCHwP/steph_e_iain.png') !important;background-size:cover !important;background-position:center center !important;}
.d .sie-manual-posts_3 .se-img {background-image:url('https://i.postimg.cc/dQpjd8r5/Joe-Sarka.png') !important;background-size:cover !important;background-position:center center !important;}
.d .sie-manual-posts_5 .se-img {background-image:url('https://i.postimg.cc/gJ0yCMq1/Mr-Mrs-Scobell.png') !important;background-size:cover !important;background-position:center center !important;}
'''

# Remover overrides antigos se existirem
import re
content = re.sub(r'\n\.d \.sie-manual-posts_[035] \.se-img \{background-image:url\([^\}]+\}\n', '\n', content)

content = content.replace('</style>', css + '</style>', 1)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
