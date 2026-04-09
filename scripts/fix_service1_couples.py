content = open('services.html', 'r', encoding='utf-8').read()

# 1. Trocar foto
old_img = 'data-img="service-1_0" class="se-img se-gr slzy"></div><noscript><img src="//static.showit.co/800/GVepQJFMWjrlKuqaoi32wQ/135701/andres-molina-hqcr9ntrrny-unsplash.jpg" class="se-img" alt="" title="andres-molina-hqCr9nTrRnY-unsplash"/></noscript>'
new_img = 'style="width:100%;height:100%;background-image:url(\'https://i.postimg.cc/Y9Yk2NH3/Billie-Arran-289.jpg\');background-size:cover;background-position:center center;" data-img="service-1_0" class="se-img se-gr slzy"></div><noscript><img src="https://i.postimg.cc/Y9Yk2NH3/Billie-Arran-289.jpg" class="se-img" alt="Couples Session" title="Couples Session"/></noscript>'

content = content.replace(old_img, new_img)

# 2. Trocar texto do conteúdo
old_text = 'For anniversaries, engagements, or simply a chapter of your story you want to remember.<br>We wander, explore, laugh, slow down, and let the landscape shape the mood.<br><br>Perfect for couples who want:<br>• Natural, emotion-driven photos<br>• A relaxed, organic experience<br>• To reconnect far from the noise<br><br>WHAT\'S INCLUDED:<br>• 1–2 hour session<br>• Location scouting + planning<br>• Outfit guidance<br>• High-resolution gallery delivered online<br>'

new_text = 'Wedding Package 1<br><br><strong>Full day coverage</strong><br>All happy tears and love captured.<br><br><strong>Two Photographers</strong><br>One photographer for up to 10 hours<br>Second photographer for up to 5 hours<br><br><strong>Same Day Previews</strong><br>Previews delivered during wedding breakfast<br><br><strong>High Res &amp; Web Size Images</strong><br>Between 400–800 photos delivered<br><br><strong>Memory Box</strong><br>(10 6x4 photos printed in a wooden box)<br><br><strong>USB Drive</strong><br>(Includes entire gallery, mailed to you!)<br><br><strong>Online Gallery</strong><br>(Included 2 year of cloud storage)<br><br><strong>Consultation Meetings</strong><br>(Timeline &amp; creative planning meetings with me)<br><br>Drone available, weather and venue depending.<br>'

content = content.replace(old_text, new_text)

# 3. Ajustar altura do container de texto para caber o conteúdo
content = content.replace(
    '.d .sie-service-1_2 {left:686px;top:196px;width:490px;height:360px;}',
    '.d .sie-service-1_2 {left:686px;top:196px;width:490px;height:560px;}'
)

# 4. Ajustar posição do "Starting at" e preço
content = content.replace(
    '.d .sie-service-1_3 {left:686px;top:589px;width:166px;height:16px;}',
    '.d .sie-service-1_3 {left:686px;top:780px;width:166px;height:16px;}'
)
content = content.replace(
    '.d .sie-service-1_4 {left:686px;top:613px;width:490px;height:48px;}',
    '.d .sie-service-1_4 {left:686px;top:804px;width:490px;height:48px;}'
)

# 5. Aumentar altura da seção
content = content.replace(
    '"slug":"service-1","visible":"a","states":[],"d":{"h":840,',
    '"slug":"service-1","visible":"a","states":[],"d":{"h":900,'
)
content = content.replace(
    '.d .sib-service-1 {height:840px;}',
    '.d .sib-service-1 {height:900px;}'
)

# 6. Adicionar CSS para imagem
css = "\n.d .sie-service-1_0 .se-img {background-image:url('https://i.postimg.cc/Y9Yk2NH3/Billie-Arran-289.jpg') !important;background-size:cover !important;background-position:center center !important;}\n"
content = content.replace('</style>', css + '</style>', 1)

open('services.html', 'w', encoding='utf-8').write(content)
print('OK')
