import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('id="about"')
end = content.find('id="trusted-by"')
block = content[start:end]

# Find all elements with sie-about_ in class
matches = re.findall(r'<[^>]*(sie-about_\d+)[^>]*>', block)
for m in matches:
    print(m[:300])
    print('---')
