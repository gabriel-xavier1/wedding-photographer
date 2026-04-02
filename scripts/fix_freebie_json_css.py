content = open('index.html', 'r', encoding='utf-8').read()

# 1. Atualizar JSON do Showit - posição do botão freebie_1
content = content.replace(
    '"id": "freebie_1", "blockId": "freebie", "m": {"x": 25, "y": 900, "w": 220, "h": 50, "a": 0}, "d": {"x": 460, "y": 380, "w": 172, "h": 50',
    '"id": "freebie_1", "blockId": "freebie", "m": {"x": 25, "y": 900, "w": 220, "h": 50, "a": 0}, "d": {"x": 460, "y": 530, "w": 172, "h": 50'
)

# 2. Atualizar JSON - altura da seção freebie
content = content.replace(
    '"slug": "freebie", "visible": "a", "states": [], "d": {"h": 590,',
    '"slug": "freebie", "visible": "a", "states": [], "d": {"h": 720,'
)

# 3. Atualizar JSON - texto freebie_2 altura
content = content.replace(
    '"id": "freebie_2", "blockId": "freebie", "m": {"x": 25, "y": 570, "w": 270, "h": 300, "a": 0}, "d": {"x": 460, "y": 260, "w": 490, "h": 96',
    '"id": "freebie_2", "blockId": "freebie", "m": {"x": 25, "y": 570, "w": 270, "h": 300, "a": 0}, "d": {"x": 460, "y": 209, "w": 490, "h": 300'
)

# 4. CSS - seção
content = content.replace(
    '.d .sib-freebie {height:800px;}',
    '.d .sib-freebie {height:720px;}'
)

# 5. CSS - texto container
content = content.replace(
    '.d .sie-freebie_2 {left:460px;top:209px;width:560px;height:320px;}',
    '.d .sie-freebie_2 {left:460px;top:209px;width:490px;height:300px;}'
)

# 6. CSS - botão
content = content.replace(
    '.d .sie-freebie_1 {left:460px;top:640px;width:220px;height:50px;}',
    '.d .sie-freebie_1 {left:460px;top:530px;width:172px;height:50px;}'
)

# 7. CSS - foto
content = content.replace(
    '.d .sie-freebie_0 {left:24px;top:40px;width:380px;height:720px;}',
    '.d .sie-freebie_0 {left:24px;top:80px;width:380px;height:580px;}'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
