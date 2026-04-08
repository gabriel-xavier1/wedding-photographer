content = open('index.html', 'r', encoding='utf-8').read()
idx = content.find('manual-posts_0')
print(repr(content[idx:idx+500]))
