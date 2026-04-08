content = open('index.html', 'r', encoding='utf-8').read()
print('weddings section found:', 'id="weddings"' in content)
idx = content.find('sib-weddings')
print('sib-weddings found:', idx != -1)
