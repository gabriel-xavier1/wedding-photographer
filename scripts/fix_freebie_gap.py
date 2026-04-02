content = open('index.html', 'r', encoding='utf-8').read()

# Mover texto, Investments, How much e botão de 460 para 436 (gap 32px como about)
for old, new in [
    ('"id": "freebie_2", "blockId": "freebie", "m": {"x": 25, "y": 570, "w": 270, "h": 300, "a": 0}, "d": {"x": 460,',
     '"id": "freebie_2", "blockId": "freebie", "m": {"x": 25, "y": 570, "w": 270, "h": 300, "a": 0}, "d": {"x": 436,'),
    ('"id": "freebie_3", "blockId": "freebie", "m": {"x": 25, "y": 84, "w": 209, "h": 67, "a": 0}, "d": {"x": 460,',
     '"id": "freebie_3", "blockId": "freebie", "m": {"x": 25, "y": 84, "w": 209, "h": 67, "a": 0}, "d": {"x": 436,'),
    ('"id": "freebie_4", "blockId": "freebie", "m": {"x": 25, "y": 43, "w": 249, "h": 30, "a": 0, "trIn": {"cl": "fadeIn", "d": 1, "dl": "0"}}, "d": {"x": 460,',
     '"id": "freebie_4", "blockId": "freebie", "m": {"x": 25, "y": 43, "w": 249, "h": 30, "a": 0, "trIn": {"cl": "fadeIn", "d": 1, "dl": "0"}}, "d": {"x": 436,'),
    ('"id": "freebie_1", "blockId": "freebie", "m": {"x": 25, "y": 900, "w": 220, "h": 50, "a": 0}, "d": {"x": 460,',
     '"id": "freebie_1", "blockId": "freebie", "m": {"x": 25, "y": 900, "w": 220, "h": 50, "a": 0}, "d": {"x": 436,'),
    # CSS
    ('.d .sie-freebie_2 {left:460px;', '.d .sie-freebie_2 {left:436px;'),
    ('.d .sie-freebie_3 {left:460px;', '.d .sie-freebie_3 {left:436px;'),
    ('.d .sie-freebie_4 {left:460px;', '.d .sie-freebie_4 {left:436px;'),
    ('.d .sie-freebie_1 {left:460px;', '.d .sie-freebie_1 {left:436px;'),
]:
    if old in content:
        content = content.replace(old, new)
        print(f'OK: {old[:50]}...')
    else:
        print(f'NOT FOUND: {old[:50]}...')

open('index.html', 'w', encoding='utf-8').write(content)
