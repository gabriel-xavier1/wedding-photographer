import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find about block
start = content.find('id="about"')
end = content.find('id="trusted-by"')
block = content[start:end]

# Find all sie-about_ elements with style
matches = re.findall(r'class="(sie-about_\d+)[^"]*"[^>]*style="([^"]*)"', block)
for cls, style in matches:
    print(f'{cls}: {style}')
    print('---')
