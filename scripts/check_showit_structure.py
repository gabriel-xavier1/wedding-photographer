content = open('index.html', 'r', encoding='utf-8').read()

# Ver estrutura completa de uma seção simples como intro
idx = content.find('id="intro"')
print(repr(content[idx:idx+800]))
