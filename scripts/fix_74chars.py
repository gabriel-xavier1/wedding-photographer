import textwrap

content = open('index.html', 'r', encoding='utf-8').read()

def wrap74(text):
    lines = textwrap.wrap(text, width=74, break_long_words=False, break_on_hyphens=False)
    return '<br>'.join(lines)

old = ('I know how overwhelming wedding planning can feel. There are so many decisions to make, so many things that feel important.<br><br>'
       'But when the day is over\u2026<br>when the music stops and everything is packed away\u2026<br>what remains are the memories.<br><br>'
       'Most couples only realise how important their photos are after the day is over.<br><br>'
       'Because of that, I take on a limited number of weddings each year to make sure every story is captured with care and intention.<br>')

p1 = wrap74('I know how overwhelming wedding planning can feel. There are so many decisions to make, so many things that feel important.')
p2 = 'But when the day is over\u2026<br>when the music stops and everything is packed away\u2026<br>what remains are the memories.'
p3 = wrap74('Most couples only realise how important their photos are after the day is over.')
p4 = wrap74('Because of that, I take on a limited number of weddings each year to make sure every story is captured with care and intention.')

new = f'{p1}<br><br>{p2}<br><br>{p3}<br><br>{p4}<br>'

if old in content:
    content = content.replace(old, new)
    print('OK')
    # Mostrar resultado
    for i, p in enumerate([p1, p2, p3, p4], 1):
        for line in p.split('<br>'):
            print(f'P{i} ({len(line)} chars): {line}')
        print()
else:
    print('NOT FOUND')

open('index.html', 'w', encoding='utf-8').write(content)
