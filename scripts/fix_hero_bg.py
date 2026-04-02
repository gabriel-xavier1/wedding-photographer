with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# O Showit usa bgScroll:"p" para parallax - o engine JS aplica o background
# e pode conflitar com o CSS. Mudar para "x" (scroll normal) no bloco principal do hero
# O estado view-1 já tem "bgScroll":"x" mas o bloco principal tem "bgScroll":"p"

# Mudar bgScroll do bloco hero principal de "p" para "x"
old = '"slug": "hero"'
idx = content.find(old)
if idx != -1:
    # Find the main block d section bgScroll
    hero_section = content[idx:idx+2000]
    print("Hero section found, checking bgScroll...")
    print(repr(hero_section[200:600]))
else:
    print("Hero slug not found")

# Mais direto: substituir bgScroll no contexto do hero desktop
old_scroll = '"bgScroll": "p", "bgImage": {"key": "https://i.postimg.cc/zDCSSh8V/TS-13166-(1).jpg"'
new_scroll = '"bgScroll": "x", "bgImage": {"key": "https://i.postimg.cc/zDCSSh8V/TS-13166-(1).jpg"'

count = content.count(old_scroll)
print(f"Found {count} occurrences of bgScroll:p with hero image")

if count > 0:
    content = content.replace(old_scroll, new_scroll)
    print("bgScroll changed to x")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
