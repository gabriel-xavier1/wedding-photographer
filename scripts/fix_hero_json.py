with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Restaurar bgScroll "p" no bloco principal do hero (desktop e mobile)
# O commit original tinha "bgScroll": "p" no bloco d e m do hero
# Eu mudei para "x" - isso quebrou o carregamento

# Desktop hero block
old_d = '"bgPos": "cb", "bgScroll": "x", "bgImage": {"key": "https://i.postimg.cc/zDCSSh8V/TS-13166-(1).jpg", "aspect_ratio": 1.5, "title": "TS-13166", "type": "asset"}}, "m": {"h": 480'
new_d = '"bgPos": "cb", "bgScroll": "p", "bgImage": {"key": "https://i.postimg.cc/zDCSSh8V/TS-13166-(1).jpg", "aspect_ratio": 1.5, "title": "TS-13166", "type": "asset"}}, "m": {"h": 480'

if old_d in content:
    content = content.replace(old_d, new_d, 1)
    print('hero desktop bgScroll restored to p')
else:
    print('NOT FOUND desktop')

# Mobile hero block  
old_m = '"bgPos": "cb", "bgScroll": "x", "bgImage": {"key": "https://i.postimg.cc/zDCSSh8V/TS-13166-(1).jpg", "aspect_ratio": 1.5, "title": "TS-13166", "type": "asset"}}, "stateTrans"'
new_m = '"bgPos": "cb", "bgScroll": "p", "bgImage": {"key": "https://i.postimg.cc/zDCSSh8V/TS-13166-(1).jpg", "aspect_ratio": 1.5, "title": "TS-13166", "type": "asset"}}, "stateTrans"'

if old_m in content:
    content = content.replace(old_m, new_m, 1)
    print('hero mobile bgScroll restored to p')
else:
    print('NOT FOUND mobile')
    # Debug - find what's there
    idx = content.find('"bgScroll"')
    while idx != -1 and 'TS-13166' not in content[idx:idx+200]:
        idx = content.find('"bgScroll"', idx+1)
    if idx != -1:
        print('Found:', repr(content[idx:idx+300]))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
