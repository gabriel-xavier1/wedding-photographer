content = open('index.html', 'r', encoding='utf-8').read()

old = ('I\'m Jacque, documentary wedding photographer, professional vibe reader, and unapologetic romantic.<br><br>'
       'I believe that after the wedding, what actually matters isn\'t the chair covers or the timeline running perfectly.<br><br>'
       'It\'s the feeling.<br>'
       'The way you looked at each other.<br>'
       'The way your mum cried.<br>'
       'The way your friends reacted during the speeches.<br><br>'
       'My job isn\'t to stage your love story.<br>'
       'It\'s to document it as it really happens, and make sure you never forget how it felt to be that in love.<br>')

new = ('Documentary wedding photographer, vibe reader, unapologetic romantic.<br><br>'
       'After the wedding, what matters isn\'t the chair covers or the perfect timeline.<br>'
       'It\'s the feeling.<br><br>'
       'The way you looked at each other.<br>'
       'The way your mum cried.<br>'
       'The way your friends reacted during the speeches.<br><br>'
       'My job isn\'t to stage your love story.<br>'
       'It\'s to document it as it really happens.<br>')

if old in content:
    content = content.replace(old, new)
    print('OK')
else:
    print('NOT FOUND')

open('index.html', 'w', encoding='utf-8').write(content)
