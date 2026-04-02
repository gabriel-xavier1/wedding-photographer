content = open('index.html', 'r', encoding='utf-8').read()

# Separar o texto em múltiplos <p> mantendo o conteúdo exato
old = 'sie-freebie_2 se"><p class="se-t sie-freebie_2-text st-m-paragraph st-d-paragraph se-rc">I know how overwhelming wedding planning can feel. There are so many decisions to make, so many things that feel important.<br>But when the day is over…<br>when the music stops and everything is packed away…<br>what remains are the memories.<br>Most couples only realise how important their photos are after the day is over.<br>Because of that, I take on a limited number of weddings each year to make sure every story is captured with care and intention.<br></p>'

new = 'sie-freebie_2 se"><p class="se-t sie-freebie_2-text st-m-paragraph st-d-paragraph se-rc">I know how overwhelming wedding planning can feel. There are so many decisions to make, so many things that feel important.</p><p class="se-t sie-freebie_2-text st-m-paragraph st-d-paragraph se-rc">But when the day is over…<br>when the music stops and everything is packed away…<br>what remains are the memories.</p><p class="se-t sie-freebie_2-text st-m-paragraph st-d-paragraph se-rc">Most couples only realise how important their photos are after the day is over.</p><p class="se-t sie-freebie_2-text st-m-paragraph st-d-paragraph se-rc">Because of that, I take on a limited number of weddings each year to make sure every story is captured with care and intention.</p>'

if old in content:
    content = content.replace(old, new)
    print('OK')
else:
    print('NOT FOUND')

open('index.html', 'w', encoding='utf-8').write(content)
