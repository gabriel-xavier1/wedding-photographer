content = open('index.html', 'r', encoding='utf-8').read()

# Ver como about_3 (foto da Jacque) está implementada - funciona com postimg
idx = content.find('about_3" class="sie-about_3 se">')
print('about_3:', repr(content[idx:idx+300]))
print()

# Ver como freebie_0 está implementada - funciona com postimg
idx2 = content.find('freebie_0" class="sie-freebie_0 se">')
print('freebie_0:', repr(content[idx2:idx2+300]))
print()

# Ver como manual-posts_0 está atualmente
idx3 = content.find('manual-posts_0" class="sie-manual-posts_0 se">')
print('manual-posts_0:', repr(content[idx3:idx3+400]))
