content = open('index.html', 'r', encoding='utf-8').read()

# 1. Trocar texto about_2: MEET YOUR PHOTOGRAPHER -> HI I AM
content = content.replace(
    '>MEET YOUR<br>PHOTOGRAPHER,<br></p>',
    '>HI<br>I AM<br></p>'
)

# 2. CSS about_2 desktop: ajustar height e font-size
content = content.replace(
    '.d .sie-about_2 {left:58px;top:123px;width:560px;height:130px;}',
    '.d .sie-about_2 {left:58px;top:123px;width:560px;height:110px;}'
)
content = content.replace(
    '.d .sie-about_2-text {color:rgba(22,22,22,1);font-size:52px;}',
    '.d .sie-about_2-text {color:rgba(22,22,22,1);font-size:48px;}'
)

# 3. CSS about_5 desktop: subir Jacque. para ficar logo abaixo do I AM
content = content.replace(
    '.d .sie-about_5 {left:58px;top:230px;width:392px;height:80px;}',
    '.d .sie-about_5 {left:58px;top:220px;width:392px;height:80px;}'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
