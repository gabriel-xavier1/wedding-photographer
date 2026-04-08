content = open('index.html', 'r', encoding='utf-8').read()

# Seta esquerda (testimonials_2): reduzir e reposicionar dentro da seção
content = content.replace(
    '.d .sie-testimonials_2 {left:1px;top:252px;width:46px;height:46px;}',
    '.d .sie-testimonials_2 {left:24px;top:260px;width:32px;height:32px;}'
)
# Seta direita (testimonials_3): reduzir e reposicionar dentro da seção
content = content.replace(
    '.d .sie-testimonials_3 {left:1153px;top:252px;width:46px;height:46px;}',
    '.d .sie-testimonials_3 {left:1144px;top:260px;width:32px;height:32px;}'
)

# Ícones das setas: reduzir tamanho
content = content.replace(
    '.d .sie-testimonials_r-y19MSMR_1 {left:12px;top:14px;width:23px;height:20px;}',
    '.d .sie-testimonials_r-y19MSMR_1 {left:6px;top:6px;width:20px;height:20px;}'
)
content = content.replace(
    '.d .sie-testimonials_cLzxFj5fr_1 {left:12px;top:14px;width:23px;height:20px;}',
    '.d .sie-testimonials_cLzxFj5fr_1 {left:6px;top:6px;width:20px;height:20px;}'
)

# Voltar font-size para 1.5rem
for slide in ['view-1_1', 'view-1-1_1', 'view-1-2_1']:
    content = content.replace(
        f'.d .sie-testimonials_{slide}-text {{color:rgba(255,255,255,1);font-size:1.1rem;line-height:1.9;text-align:center;}}',
        f'.d .sie-testimonials_{slide}-text {{color:rgba(255,255,255,1);font-size:1.5rem;line-height:1.9;text-align:center;}}'
    )

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
