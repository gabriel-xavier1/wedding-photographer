with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: text - remove double <br><br> between the feeling sentences
old_text = (
    "It\u2019s the feeling.<br>"
    "The way you looked at each other.<br>"
    "The way your mum cried.<br>"
    "The way your friends reacted during the speeches.<br>"
    "My job isn\u2019t to stage your love story.<br>"
)
# Check if already single br or still double
if "It\u2019s the feeling.<br><br>" in content:
    content = content.replace(
        "It\u2019s the feeling.<br><br>The way you looked at each other.<br><br>The way your mum cried.<br><br>The way your friends reacted during the speeches.<br><br>My job isn\u2019t to stage your love story.<br><br>",
        "It\u2019s the feeling.<br>The way you looked at each other.<br>The way your mum cried.<br>The way your friends reacted during the speeches.<br>My job isn\u2019t to stage your love story.<br>"
    )
    print('Text fixed')
elif old_text in content:
    print('Text already correct')
else:
    print('Text pattern not found')

# Fix 2: photo - replace about_3 image
old_photo = (
    'data-sid="about_3" class="sie-about_3 se"><div style="width:100%;height:100%" '
    'data-img="about_3" class="se-img se-gr slzy"></div>'
    '<noscript><img src="//static.showit.co/800/rrCs5PsGvZ-lALVbMzbPSA/135701/sandra-seitamaa-6a23hx3xkdo-unsplash.jpg" '
    'class="se-img" alt="" title="sandra-seitamaa-6a23HX3Xkdo-unsplash"/></noscript>'
)
new_photo = (
    'data-sid="about_3" class="sie-about_3 se">'
    '<div style="width:100%;height:100%;background-image:url(\'https://i.postimg.cc/V5P1f0DJ/Whats-App-Image-2026-02-06-at-17-55-03.jpg\');background-size:cover;background-position:center center;" '
    'data-img="about_3" class="se-img se-gr slzy"></div>'
    '<noscript><img src="https://i.postimg.cc/V5P1f0DJ/Whats-App-Image-2026-02-06-at-17-55-03.jpg" '
    'class="se-img" alt="" title="Jacque"/></noscript>'
)

if old_photo in content:
    content = content.replace(old_photo, new_photo)
    print('Photo fixed')
else:
    print('Photo pattern not found - checking...')
    idx = content.find('sie-about_3 se')
    if idx != -1:
        print(repr(content[idx:idx+250]))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
