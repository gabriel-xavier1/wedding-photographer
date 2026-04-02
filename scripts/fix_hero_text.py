with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # about_4 - esconder no mobile (estava aparecendo por cima)
    ('.m .sie-about_4 {left:205px;top:115px;width:115px;height:142px;}',
     '.m .sie-about_4 {left:205px;top:115px;width:115px;height:142px;display:none;}'),

    # about - aumentar altura do section para caber tudo
    ('.m .sib-about {height:701px;}',
     '.m .sib-about {height:760px;}'),

    # about_1 texto - dar mais altura para nao cortar
    ('.m .sie-about_1 {left:25px;top:345px;width:270px;height:249px;}',
     '.m .sie-about_1 {left:25px;top:345px;width:270px;height:280px;}'),

    # about_0 botao - descer junto
    ('.m .sie-about_0 {left:25px;top:619px;width:180px;height:45px;}',
     '.m .sie-about_0 {left:25px;top:660px;width:180px;height:45px;}'),

    # freebie - aumentar altura do section
    ('.m .sib-freebie {height:420px;}',
     '.m .sib-freebie {height:460px;}'),

    # freebie_2 texto - dar mais altura
    ('.m .sie-freebie_2 {left:25px;top:168px;width:270px;height:137px;}',
     '.m .sie-freebie_2 {left:25px;top:168px;width:270px;height:160px;}'),

    # freebie_1 botao - descer para nao sobrepor texto
    ('.m .sie-freebie_1 {left:25px;top:326px;width:165px;height:50px;}',
     '.m .sie-freebie_1 {left:25px;top:360px;width:165px;height:50px;}'),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        print('OK:', new[:70])
    else:
        print('NAO ENCONTRADO:', old[:70])

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('DONE')
