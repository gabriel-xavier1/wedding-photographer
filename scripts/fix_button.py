with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = 'class="sie-about_0 se" data-sid="about_0"'
new = 'class="sie-about_0 se" data-sid="about_0" style="top:713px"'

if old in content:
    content = content.replace(old, new)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('DONE')
else:
    print('NOT FOUND')
