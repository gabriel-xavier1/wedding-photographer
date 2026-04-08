content = open('index.html', 'r', encoding='utf-8').read()

# Foto 1 - Steph & Iain
old1 = 'class="se-img" style="width:100%;height:100%;background-image:url(\'https://i.postimg.cc/NjPzCHwP/steph_e_iain.png\');background-size:cover;background-position:center;"></div><noscript><img src="https://i.postimg.cc/NjPzCHwP/steph_e_iain.png" class="se-img" alt="Steph e Iain" title="Steph & Iain"/></noscript>'
new1 = 'style="width:100%;height:100%;background-image:url(\'https://i.postimg.cc/NjPzCHwP/steph_e_iain.png\');background-size:cover;background-position:center center;" data-img="manual-posts_0" class="se-img se-gr slzy"></div><noscript><img src="https://i.postimg.cc/NjPzCHwP/steph_e_iain.png" class="se-img" alt="Steph & Iain" title="Steph & Iain"/></noscript>'

# Foto 2 - Clara & Edgar
old2 = 'class="se-img" style="width:100%;height:100%;background-image:url(\'https://i.postimg.cc/ZKk9ZN6n/TS_11618.jpg\');background-size:cover;background-position:center;"></div><noscript><img src="https://i.postimg.cc/ZKk9ZN6n/TS_11618.jpg" class="se-img" alt="Clara e Edgar" title="Clara & Edgar"/></noscript>'
new2 = 'style="width:100%;height:100%;background-image:url(\'https://i.postimg.cc/ZKk9ZN6n/TS_11618.jpg\');background-size:cover;background-position:center center;" data-img="manual-posts_3" class="se-img se-gr slzy"></div><noscript><img src="https://i.postimg.cc/ZKk9ZN6n/TS_11618.jpg" class="se-img" alt="Clara & Edgar" title="Clara & Edgar"/></noscript>'

# Foto 3 - Ada & Joshua
old3 = 'class="se-img" style="width:100%;height:100%;background-image:url(\'https://i.postimg.cc/8zn0X6VX/ada_e_joshua.png\');background-size:cover;background-position:center;"></div><noscript><img src="https://i.postimg.cc/8zn0X6VX/ada_e_joshua.png" class="se-img" alt="Ada e Joshua" title="Ada & Joshua"/></noscript>'
new3 = 'style="width:100%;height:100%;background-image:url(\'https://i.postimg.cc/8zn0X6VX/ada_e_joshua.png\');background-size:cover;background-position:center center;" data-img="manual-posts_5" class="se-img se-gr slzy"></div><noscript><img src="https://i.postimg.cc/8zn0X6VX/ada_e_joshua.png" class="se-img" alt="Ada & Joshua" title="Ada & Joshua"/></noscript>'

for old, new in [(old1, new1), (old2, new2), (old3, new3)]:
    if old in content:
        content = content.replace(old, new)
        print('OK')
    else:
        print('NOT FOUND')

open('index.html', 'w', encoding='utf-8').write(content)
