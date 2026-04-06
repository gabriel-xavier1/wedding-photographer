content = open('index.html', 'r', encoding='utf-8').read()

old = ('I know\n how overwhelming wedding planning can feel.<br>There are so many decisions to make, so many things that feel important.<br><br>But when the day is over\u2026<br>when the music stops and everything is packed away\u2026<br>what remains are the memories.<br><br>Most couples only realise how important their photos are after the day is over.<br><br>Because of that, I take on a limited number of weddings each year to make<br>sure every story is captured with care and intention.<br>')

new = ('Wedding planning is overwhelming.<br>So many decisions. So many things that feel important.<br><br>But when the day is over,<br>what remains are the memories.<br><br>Most couples only realise how much their photos matter<br>after the day is gone.<br><br>That\u2019s why I take on a limited number of weddings each year,<br>so every story gets the care and intention it deserves.<br>')

if old in content:
    content = content.replace(old, new)
    print('OK')
else:
    print('NOT FOUND - trying alt')
    # try without newline
    old2 = old.replace('\n ', ' ')
    if old2 in content:
        content = content.replace(old2, new)
        print('OK alt')
    else:
        print('STILL NOT FOUND')

open('index.html', 'w', encoding='utf-8').write(content)
