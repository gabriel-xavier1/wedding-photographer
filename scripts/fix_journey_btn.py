content = open('index.html', 'r', encoding='utf-8').read()

idx_start = content.find('sie-weddings_btn se">')
idx_end = content.find('</div><div data-sid="weddings_photo"')

old = content[idx_start + len('sie-weddings_btn se">'):idx_end]
new = '<a href="services.html" style="text-decoration:none;"><button type="button" aria-label="The Journey" class="se-button st-primary"><span class="st-m-primary st-d-primary">The Journey</span></button></a>'

content = content[:idx_start + len('sie-weddings_btn se">')] + new + content[idx_end:]
open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
