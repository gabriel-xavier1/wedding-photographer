index = open('index.html', 'r', encoding='utf-8').read()

# Extract full intro HTML
intro_start = index.find('<div id="intro" data-bid="intro"')
depth = 0
i = intro_start
while i < len(index):
    if index[i:i+4] == '<div': depth += 1
    elif index[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            intro_end = i + 6
            break
    i += 1
intro_html = index[intro_start:intro_end]

with open('scripts/intro_html_dump.txt', 'w', encoding='utf-8') as f:
    f.write(intro_html)

print(f"Intro HTML length: {len(intro_html)}")
print("First 2000 chars:")
print(intro_html[:2000])
