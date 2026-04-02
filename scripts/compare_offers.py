with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = "se-rc\">Every couple brings their own story, history, and energy. That\u2019s what makes each wedding day truly unforgettable.<br>It\u2019s in the laughter.<br>The happy tears.<br>The quiet, calm moments before everything begins.<br>This isn\u2019t just a collection of pretty photos.<br>It\u2019s a journey from start to finish.<br></p>"
new = "se-rc\">Whether you\u2019re exchanging vows in a quiet pine forest, climbing dunes at sunrise, or holding each other close beneath a sky full of desert stars, your day deserves to be remembered with intention.<br></p>"

if old in content:
    content = content.replace(old, new)
    print('OK offers_0')
else:
    # try ascii apostrophe
    old2 = "se-rc\">Every couple brings their own story, history, and energy. That's what makes each wedding day truly unforgettable.<br>It's in the laughter.<br>The happy tears.<br>The quiet, calm moments before everything begins.<br>This isn't just a collection of pretty photos.<br>It's a journey from start to finish.<br></p>"
    new2 = "se-rc\">Whether you're exchanging vows in a quiet pine forest, climbing dunes at sunrise, or holding each other close beneath a sky full of desert stars, your day deserves to be remembered with intention.<br></p>"
    if old2 in content:
        content = content.replace(old2, new2)
        print('OK offers_0 (ascii)')
    else:
        print('NAO ENCONTRADO offers_0')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
