content = open('index.html', 'r', encoding='utf-8').read()
idx = content.find('se-button')
print(content[idx-200:idx+500])
