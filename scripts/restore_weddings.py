backup = open('index_backup.html', 'r', encoding='utf-8').read()
current = open('index.html', 'r', encoding='utf-8').read()

# Extrair seção weddings do backup
start_tag = '<div id="weddings"'
end_tag = '<div id="testimonials"'

idx_start = backup.find(start_tag)
idx_end = backup.find(end_tag)
weddings_section = backup[idx_start:idx_end]
print('Weddings section length:', len(weddings_section))

# Inserir na posição correta no arquivo atual
if end_tag in current:
    current = current.replace(end_tag, weddings_section + end_tag, 1)
    open('index.html', 'w', encoding='utf-8').write(current)
    print('OK - section restored')
else:
    print('NOT FOUND - testimonials section missing')
