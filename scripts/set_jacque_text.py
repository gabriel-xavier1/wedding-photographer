with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = 'Based wherever the next trail leads, I specialize in intimate, atmospheric storytelling for couples who choose adventure over expectation.<br><br>From windswept cliffs to moss-covered forests, from the vast calm of the desert to alpine lakes at dawn \u2014 every location becomes part of your story.<br>I\u2019ll help you feel grounded, present, and fully yourselves, so your photos breathe with the truth of who you are.<br>'

new = 'I\u2019m Jacque \u2014 documentary wedding photographer, professional vibe-reader, and unapologetic romantic.<br><br>I believe that after the wedding, what actually matters isn\u2019t the chair covers or the timeline running perfectly.<br><br>It\u2019s the feeling.<br>The way you looked at each other.<br>The way your mum cried.<br>The way your friends reacted during the speeches.<br>My job isn\u2019t to stage your love story.<br>It\u2019s to document it as it really happens \u2014 and make sure you never forget how it felt to be that in love.<br>'

if old in content:
    content = content.replace(old, new)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('DONE')
else:
    print('NOT FOUND')
