content = open('index.html', 'r', encoding='utf-8').read()

# Texto atual (quebrado errado)
old = ('I know how overwhelming wedding planning can feel. There are so many<br>'
       'decisions to make, so many things that feel important.<br><br>'
       'But when the day is over\u2026<br>when the music stops and everything is packed away\u2026<br>what remains are the memories.<br><br>'
       'Most couples only realise how important their photos are after the day is<br>over.<br><br>'
       'Because of that, I take on a limited number of weddings each year')

# Texto corrigido com ~74 chars por linha
new = ('I know how overwhelming wedding planning can feel.<br>'
       'There are so many decisions to make, so many things that feel important.<br><br>'
       'But when the day is over\u2026<br>'
       'when the music stops and everything is packed away\u2026<br>'
       'what remains are the memories.<br><br>'
       'Most couples only realise how important their photos are after the day is over.<br><br>'
       'Because of that, I take on a limited number of weddings each year')

if old in content:
    content = content.replace(old, new)
    print('OK')
else:
    print('NOT FOUND')

open('index.html', 'w', encoding='utf-8').write(content)
