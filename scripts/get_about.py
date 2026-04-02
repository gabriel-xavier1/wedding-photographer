with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('id="about"')
end = content.find('id="trusted-by"')
block = content[start:end]
print(block)
