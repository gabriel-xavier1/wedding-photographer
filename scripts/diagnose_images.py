content = open('index.html', 'r', encoding='utf-8').read()

# Comparar: imagem que FUNCIONA (about_3 - postimg) vs imagem que NAO FUNCIONA (manual-posts_0)
print('=== ABOUT_3 (FUNCIONA) ===')
idx = content.find('sie-about_3 se">')
print(repr(content[idx:idx+350]))

print()
print('=== FREEBIE_0 (FUNCIONA) ===')
idx2 = content.find('sie-freebie_0 se">')
print(repr(content[idx2:idx2+350]))

print()
print('=== MANUAL-POSTS_0 (NAO FUNCIONA) ===')
# Buscar pelo href do link que envolve a foto
idx3 = content.find('gallery.jacqueprates.co.uk/" target="_blank" class="sie-manual-posts_0')
print(repr(content[idx3:idx3+500]))

print()
print('=== CSS manual-posts_0 ===')
import re
css = re.findall(r'\.d \.sie-manual-posts_0[^\n]+', content)
for c in css[:5]:
    print(c)
