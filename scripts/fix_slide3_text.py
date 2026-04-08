content = open('index.html', 'r', encoding='utf-8').read()

# Trocar nome
content = content.replace(
    'class="sie-testimonials_view-1-2_0 se"><p class="se-t sie-testimonials_view-1-2_0-text st-m-title st-d-title se-rc">Patrick &amp; Samantha<br></p>',
    'class="sie-testimonials_view-1-2_0 se"><p class="se-t sie-testimonials_view-1-2_0-text st-m-title st-d-title se-rc">Josie Stubbs<br></p>'
)

# Trocar texto
old = '"We couldn\'t have asked for a better photographer than Jacque. We aren\'t the kind of people who take loads of pictures normally but Jacque made us feel so comfortable and guided us so effortlessly on the day. Looking over the photos was amazing because Jacque was able to blend in so naturally around the venue which resulted in so many lovely, natural photos. She was professional from start to finish and we even got a lovely card from her before she left which was so thoughtful, we loved it. We would 100% recommend Jacque to anyone looking for a photographer!"'

new = '"This woman\'s work is just amazing! Me and my husband only really had a few basic ideas for our wedding photos but Jacque helped us get the best shots for our wedding and was very professional. Her photos are of good quality and she is affordable too. She also gets photos back in quick time (ours only took 4 weeks) and she is very organised. She was also very good with children at our wedding too."'

if old in content:
    content = content.replace(old, new)
    print('OK')
else:
    print('NOT FOUND')

open('index.html', 'w', encoding='utf-8').write(content)
