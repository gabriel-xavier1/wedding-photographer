content = open('index.html', 'r', encoding='utf-8').read()

for img_id, url in [
    ('manual-posts_0', 'https://i.postimg.cc/NjPzCHwP/steph_e_iain.png'),
    ('manual-posts_3', 'https://i.postimg.cc/ZKk9ZN6n/TS_11618.jpg'),
    ('manual-posts_5', 'https://i.postimg.cc/8zn0X6VX/ada_e_joshua.png'),
]:
    old = f'<div style="width:100%;height:100%" style="width:100%;height:100%;background-image:url(\'{url}\');background-size:cover;background-position:center center;" data-img="{img_id}" class="se-img se-gr slzy">'
    new = f'<div style="width:100%;height:100%;background-image:url(\'{url}\');background-size:cover;background-position:center center;" data-img="{img_id}" class="se-img se-gr slzy">'
    if old in content:
        content = content.replace(old, new)
        print(f'OK: {img_id}')
    else:
        print(f'NOT FOUND: {img_id}')

open('index.html', 'w', encoding='utf-8').write(content)
