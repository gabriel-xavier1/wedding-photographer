content = open('index.html', 'r', encoding='utf-8').read()

# Seção: 580 (botão termina) + 80px (mesmo gap de cima) = 660px
content = content.replace(
    '"slug": "freebie", "visible": "a", "states": [], "d": {"h": 720,',
    '"slug": "freebie", "visible": "a", "states": [], "d": {"h": 660,'
)
content = content.replace(
    '.d .sib-freebie {height:720px;}',
    '.d .sib-freebie {height:660px;}'
)

# Foto acompanha
content = content.replace(
    '.d .sie-freebie_0 {left:24px;top:80px;width:380px;height:580px;}',
    '.d .sie-freebie_0 {left:24px;top:80px;width:380px;height:500px;}'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
