content = open('index.html', 'r', encoding='utf-8').read()
idx = content.find('st-secondary.se-button {')
print(content[idx:idx+300])
