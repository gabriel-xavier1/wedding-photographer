with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

fixes = [
    # 1. Subir botão: texto termina em ~195+280=475, botão com 32px gap = top:507
    ('.d .sie-freebie_1 {left:460px;top:499px;width:200px;height:50px;}',
     '.d .sie-freebie_1 {left:460px;top:507px;width:220px;height:50px;}'),

    # 2. Aumentar largura do botão para "View Investments" caber sem cortar
    # CSS do botão - garantir que o texto não seja truncado
]

for old, new in fixes:
    if old in content:
        content = content.replace(old, new, 1)
        print(f'OK: {new[:70]}')
    else:
        print(f'NOT FOUND: {old[:70]}')

# 3. Corrigir o texto do botão - está a ser truncado pelo CSS do span
# Adicionar white-space:nowrap e width auto no botão
old_btn_css = '.d .sie-freebie_1 .se-button {}'
new_btn_css = '.d .sie-freebie_1 .se-button {white-space:nowrap;width:auto;min-width:220px;}'
if old_btn_css in content:
    content = content.replace(old_btn_css, new_btn_css, 1)
    print('button CSS fixed')
else:
    print('button CSS not found')

# 4. Reduzir altura do bloco para botão não ficar tão longe do fundo
old_h = '.d .sib-freebie {height:590px;}'
new_h = '.d .sib-freebie {height:590px;}'  # manter

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
