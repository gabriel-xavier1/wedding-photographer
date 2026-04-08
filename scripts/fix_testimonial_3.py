content = open('index.html', 'r', encoding='utf-8').read()

# Nome
content = content.replace(
    'class="sie-testimonials_view-1-2_0 se"><p class="se-t sie-testimonials_view-1-2_0-text st-m-title st-d-title se-rc">Harper &amp; Eli<br></p>',
    'class="sie-testimonials_view-1-2_0 se"><p class="se-t sie-testimonials_view-1-2_0-text st-m-title st-d-title se-rc">Patrick &amp; Samantha<br></p>'
)

# Texto - substituir pelo índice
idx = content.find('sie-testimonials_view-1-2_1 se">')
end = content.find('</p></div></div></div><div class="ss-s ss-fg">', idx)
old = content[idx:end + len('</p>')]
new = 'sie-testimonials_view-1-2_1 se"><p class="se-t sie-testimonials_view-1-2_1-text st-m-heading st-d-heading se-rc">"We couldn\'t have asked for a better photographer than Jacque. We aren\'t the kind of people who take loads of pictures normally but Jacque made us feel so comfortable and guided us so effortlessly on the day. Looking over the photos was amazing because Jacque was able to blend in so naturally around the venue which resulted in so many lovely, natural photos. She was professional from start to finish and we even got a lovely card from her before she left which was so thoughtful, we loved it. We would 100% recommend Jacque to anyone looking for a photographer!"</p>'

content = content.replace(old, new)
print('OK')

open('index.html', 'w', encoding='utf-8').write(content)
