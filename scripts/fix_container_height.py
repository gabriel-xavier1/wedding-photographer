content = open('index.html', 'r', encoding='utf-8').read()

content = content.replace(
    '.d .sie-freebie_2 {left:460px;top:209px;width:560px;height:220px;}',
    '.d .sie-freebie_2 {left:460px;top:209px;width:560px;height:320px;}'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
