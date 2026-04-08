content = open('index.html', 'r', encoding='utf-8').read()

# 1. Trocar titulo "on the blog" -> "galleries"
content = content.replace(
    '>on the blog</h2>',
    '>galleries</h2>'
)

# 2. Trocar links de blog.html -> gallery
content = content.replace(
    'href="blog.html" target="_self" class="sie-manual-posts_0 se"',
    'href="https://gallery.jacqueprates.co.uk/" target="_blank" class="sie-manual-posts_0 se"'
)
content = content.replace(
    'href="blog.html" target="_self" class="sie-manual-posts_1 se"',
    'href="https://gallery.jacqueprates.co.uk/" target="_blank" class="sie-manual-posts_1 se"'
)
content = content.replace(
    'href="blog.html" target="_self" class="sie-manual-posts_3 se"',
    'href="https://gallery.jacqueprates.co.uk/" target="_blank" class="sie-manual-posts_3 se"'
)
content = content.replace(
    'href="blog.html" target="_self" class="sie-manual-posts_4 se"',
    'href="https://gallery.jacqueprates.co.uk/" target="_blank" class="sie-manual-posts_4 se"'
)
content = content.replace(
    'href="blog.html" target="_self" class="sie-manual-posts_5 se"',
    'href="https://gallery.jacqueprates.co.uk/" target="_blank" class="sie-manual-posts_5 se"'
)
content = content.replace(
    'href="blog.html" target="_self" class="sie-manual-posts_6 se"',
    'href="https://gallery.jacqueprates.co.uk/" target="_blank" class="sie-manual-posts_6 se"'
)

# 3. Trocar nomes dos posts
content = content.replace(
    '>Carmen &amp; Rob: Whistler Forest Couple\'s Session<br></h3>',
    '>Steph &amp; Iain<br></h3>'
)
content = content.replace(
    '>Leah &amp; Josh: Banff Sunrise Elopement<br></h3>',
    '>Clara &amp; Edgar<br></h3>'
)
content = content.replace(
    '>Corey &amp; Miranda: Winter Mountain Wedding<br></h3>',
    '>Ada &amp; Joshua<br></h3>'
)

# 4. Trocar imagens das fotos
# Foto 1 (manual-posts_0)
content = content.replace(
    'data-img="manual-posts_0" class="se-img se-gr slzy"></div><noscript><img src="//static.showit.co/400/lrPZdC8eQyeEvSGzP-pMaA/135701/andres-molina--x2t5s6srfe-unsplash_1.jpg" class="se-img" alt="" title="andres-molina--X2t5s6SRfE-unsplash (1)"/></noscript>',
    'class="se-img" style="width:100%;height:100%;background-image:url(\'https://i.postimg.cc/NjPzCHwP/steph_e_iain.png\');background-size:cover;background-position:center;"></div><noscript><img src="https://i.postimg.cc/NjPzCHwP/steph_e_iain.png" class="se-img" alt="Steph e Iain" title="Steph & Iain"/></noscript>'
)

# Foto 2 (manual-posts_3)
content = content.replace(
    'data-img="manual-posts_3" class="se-img se-gr slzy"></div><noscript><img src="//static.showit.co/400/SZbB5bYe-qaa6z_8X8nnNQ/135701/kaboompics_wedding-dress-shoes-bouquet-31914.jpg" class="se-img" alt="" title="kaboompics_wedding-dress-shoes-bouquet-31914"/></noscript>',
    'class="se-img" style="width:100%;height:100%;background-image:url(\'https://i.postimg.cc/ZKk9ZN6n/TS_11618.jpg\');background-size:cover;background-position:center;"></div><noscript><img src="https://i.postimg.cc/ZKk9ZN6n/TS_11618.jpg" class="se-img" alt="Clara e Edgar" title="Clara & Edgar"/></noscript>'
)

# Foto 3 (manual-posts_5)
content = content.replace(
    'data-img="manual-posts_5" class="se-img se-gr slzy"></div><noscript><img src="//static.showit.co/400/BODbylQ_Yfp9oD8Up_NNXA/135701/andres-molina-d1qzc4vpybg-unsplash.jpg" class="se-img" alt="" title="andres-molina-D1QzC4vPybg-unsplash"/></noscript>',
    'class="se-img" style="width:100%;height:100%;background-image:url(\'https://i.postimg.cc/8zn0X6VX/ada_e_joshua.png\');background-size:cover;background-position:center;"></div><noscript><img src="https://i.postimg.cc/8zn0X6VX/ada_e_joshua.png" class="se-img" alt="Ada e Joshua" title="Ada & Joshua"/></noscript>'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
