import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('id="about"')
end = content.find('id="trusted-by"')
block = content[start:end]

# Find full tags with sie-about_
matches = re.findall(r'<[^>]*(sie-about_\d+)[^>]*>', block)
for full_tag in re.finditer(r'<[^>]*(sie-about_\d+)[^>]*>', block):
    print(full_tag.group(0)[:400])
    print('---')
