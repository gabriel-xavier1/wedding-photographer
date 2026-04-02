with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Corrigir o div da imagem - tinha style duplicado, limpar e usar só o correto
old_div = '<div style="width:100%;height:100%" data-img="freebie_0" class="se-img se-gr slzy" style="background-image:url(\'https://i.postimg.cc/qqvhR7sh/Chloe-Loius-366-2048x1365.jpg\');background-size:cover;background-position:center center;"></div>'
new_div = '<div style="width:100%;height:100%" data-img="freebie_0" class="se-img se-gr slzy"></div>'

if old_div in content:
    content = content.replace(old_div, new_div, 1)
    print('duplicate style removed OK')
else:
    # Check what's there
    idx = content.find('data-img="freebie_0"')
    print('Current freebie_0 div:', repr(content[idx:idx+200]) if idx != -1 else 'nothing')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
