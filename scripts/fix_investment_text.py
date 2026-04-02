content = open('index.html', 'r', encoding='utf-8').read()

# freebie_4: trocar heading
content = content.replace(
    '>How much will it cost?<br><br></h3>',
    '>Wedding Photography Investment<br></h3>'
)

# freebie_2: melhorar fluxo do parágrafo
old = 'I know how overwhelming wedding planning can feel. There are so many decisions to make, so many things that feel important.<br>But when the day is over\u2026<br>when the music stops and everything is packed away\u2026<br>what remains are the memories.<br>Most couples only realise how important their photos are after the day is over.<br>Because of that, I take on a limited number of weddings each year to make sure every story is captured with care and intention.<br>'

new = 'I know how overwhelming wedding planning can feel.<br>There are so many decisions, so many things that seem important.<br><br>But when the day is over,<br>when the music stops and everything is packed away,<br>what remains are the memories.<br><br>Most couples only realise how much their photos matter after the day is gone.<br><br>That\u2019s why I take on a limited number of weddings each year,<br>so every story gets the care and intention it deserves.<br>'

if old in content:
    content = content.replace(old, new)
    print('freebie_2 OK')
else:
    print('freebie_2 NOT FOUND')

open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
