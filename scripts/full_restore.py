
# Step 1: Write the full original HTML from the user's paste
import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Restore the about_1 text with <br> (single line breaks, no double)
# The original Showit text in about_1
old_text = (
    "I\u2019m Jacque \u2014 documentary wedding photographer, professional vibe-reader, and unapologetic romantic.<br><br>"
    "I believe that after the wedding, what actually matters isn\u2019t the chair covers or the timeline running perfectly.<br><br>"
    "It\u2019s the feeling.<br><br>"
    "The way you looked at each other.<br><br>"
    "The way your mum cried.<br><br>"
    "The way your friends reacted during the speeches.<br><br>"
    "My job isn\u2019t to stage your love story.<br><br>"
    "It\u2019s to document it as it really happens \u2014 and make sure you never forget how it felt to be that in love.<br>"
)

new_text = (
    "I\u2019m Jacque \u2014 documentary wedding photographer, professional vibe-reader, and unapologetic romantic.<br><br>"
    "I believe that after the wedding, what actually matters isn\u2019t the chair covers or the timeline running perfectly.<br><br>"
    "It\u2019s the feeling.<br>"
    "The way you looked at each other.<br>"
    "The way your mum cried.<br>"
    "The way your friends reacted during the speeches.<br>"
    "My job isn\u2019t to stage your love story.<br>"
    "It\u2019s to document it as it really happens \u2014 and make sure you never forget how it felt to be that in love.<br>"
)

# Fix 2: Restore Jacque's photo in about_3
old_img = 'data-src="//static.showit.co/1200/rrCs5PsGvZ-lALVbMzbPSA/135701/sandra-seitamaa-6a23hx3xkdo-unsplash.jpg"'
new_img = 'data-src="//static.showit.co/1200/rrCs5PsGvZ-lALVbMzbPSA/135701/sandra-seitamaa-6a23hx3xkdo-unsplash.jpg" style="background-image:url(\'https://i.postimg.cc/V5P1f0DJ/Whats-App-Image-2026-02-06-at-17-55-03.jpg\')"'

changes = 0

if old_text in content:
    content = content.replace(old_text, new_text)
    changes += 1
    print('Text fix applied')
else:
    print('Text: not found, checking current state...')
    if 'It\u2019s the feeling.<br>' in content:
        print('Text already has single <br> - OK')
        changes += 1

# Apply photo fix via CSS override in about_3
old_about3_img = (
    '<div style="width: 100%; height: 100%; position: absolute; top: 0px; left: 0px;" '
    'data-img="about_3" class="se-img se-gr slzy" '
    'data-src="//static.showit.co/1200/rrCs5PsGvZ-lALVbMzbPSA/135701/sandra-seitamaa-6a23hx3xkdo-unsplash.jpg">'
)
new_about3_img = (
    '<div style="width: 100%; height: 100%; position: absolute; top: 0px; left: 0px; '
    'background-image:url(\'https://i.postimg.cc/V5P1f0DJ/Whats-App-Image-2026-02-06-at-17-55-03.jpg\');'
    'background-size:cover;background-position:center center;" '
    'data-img="about_3" class="se-img se-gr slzy" '
    'data-src="//static.showit.co/1200/rrCs5PsGvZ-lALVbMzbPSA/135701/sandra-seitamaa-6a23hx3xkdo-unsplash.jpg">'
)

if old_about3_img in content:
    content = content.replace(old_about3_img, new_about3_img)
    changes += 1
    print('Photo fix applied')
elif 'postimg.cc' in content:
    print('Photo already set - OK')
    changes += 1

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Done. {changes} fixes applied.')
