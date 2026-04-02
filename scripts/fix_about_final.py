with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix photo - correct URL
old_img = 'data-sid="about_3" class="sie-about_3 se"><div style="width:100%;height:100%" data-img="about_3" class="se-img se-gr slzy"></div><noscript><img src="//static.showit.co/800/rrCs5PsGvZ-lALVbMzbPSA/135701'
idx = content.find(old_img)
if idx != -1:
    end = content.find('</noscript>', idx) + len('</noscript>')
    old_full = content[idx:end]
    new_full = 'data-sid="about_3" class="sie-about_3 se"><div style="width:100%;height:100%;background-image:url(\'https://i.postimg.cc/V5P1f0DJ/Whats-App-Image-2026-02-06-at-17-55-03.jpg\');background-size:cover;background-position:center center;" data-img="about_3" class="se-img se-gr slzy"></div><noscript><img src="https://i.postimg.cc/V5P1f0DJ/Whats-App-Image-2026-02-06-at-17-55-03.jpg" class="se-img" alt="" title="Jacque"/></noscript>'
    content = content.replace(old_full, new_full, 1)
    print('about_3 photo fixed')
else:
    print('about_3 NOT FOUND')

# Update about_1 text with proper formatting
old_text = 'sie-about_1-text st-m-paragraph st-d-paragraph se-rc">'
idx2 = content.find(old_text)
if idx2 != -1:
    end2 = content.find('</p>', idx2)
    old_para = content[idx2:end2+4]
    new_para = 'sie-about_1-text st-m-paragraph st-d-paragraph se-rc">I\'m Jacque \u2014 documentary wedding photographer, professional vibe-reader, and unapologetic romantic.<br><br>I believe that after the wedding, what actually matters isn\'t the chair covers or the timeline running perfectly.<br><br>It\'s the feeling.<br>The way you looked at each other.<br>The way your mum cried.<br>The way your friends reacted during the speeches.<br><br>My job isn\'t to stage your love story.<br>It\'s to document it as it really happens \u2014 and make sure you never forget how it felt to be that in love.<br></p>'
    content = content.replace(old_para, new_para, 1)
    print('about_1 text updated')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
