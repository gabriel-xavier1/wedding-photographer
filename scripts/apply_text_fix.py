with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the about_1 paragraph and fix double <br><br> between the feeling sentences
old = (
    "It\u2019s the feeling.<br><br>"
    "The way you looked at each other.<br><br>"
    "The way your mum cried.<br><br>"
    "The way your friends reacted during the speeches.<br><br>"
    "My job isn\u2019t to stage your love story.<br><br>"
    "It\u2019s to document"
)
new = (
    "It\u2019s the feeling.<br>"
    "The way you looked at each other.<br>"
    "The way your mum cried.<br>"
    "The way your friends reacted during the speeches.<br>"
    "My job isn\u2019t to stage your love story.<br>"
    "It\u2019s to document"
)

if old in content:
    content = content.replace(old, new)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('DONE - text fixed')
else:
    # Check what's there
    idx = content.find("It\u2019s the feeling")
    if idx > -1:
        print('Found at:', idx)
        print(repr(content[idx:idx+300]))
    else:
        print('NOT FOUND')
