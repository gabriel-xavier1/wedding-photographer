content = open('services.html', 'r', encoding='utf-8').read()

# Trocar texto
old = 'For anniversaries, engagements, or simply a chapter of your story you want to remember.<br>We wander, explore, laugh, slow down, and let the landscape shape the mood.<br><br>Perfect for couples who want:<br>\u2022 Natural, emotion-driven photos<br>\u2022 A relaxed, organic experience<br>\u2022 To reconnect far from the noise<br><br>WHAT\'S INCLUDED:<br>\u2022 1\u20132 hour session<br>\u2022 Location scouting + planning<br>\u2022 Outfit guidance<br>\u2022 High-resolution gallery delivered online<br>'

new = '\U0001f4f8 Wedding Package 1 \u2013 Lover (Most Booked)<br>Up to 10 hours coverage<br><br>\U0001f4c5 Full Day Coverage<br>All happy tears and love captured.<br><br>\U0001f465 Two Photographers<br>One photographer for up to 10 hours<br>Second photographer for up to 5 hours<br><br>\u26a1 Same Day Previews<br>Previews delivered during wedding breakfast<br><br>\U0001f5bc\ufe0f High Resolution &amp; Web Size Images<br>Between 400\u2013800 photos delivered<br><br>\U0001f4e6 Memory Box<br>10 photos (6x4) printed in a wooden box<br><br>\U0001f4be USB Drive<br>Includes entire gallery (mailed to you)<br><br>\U0001f310 Online Gallery<br>Includes 2 years of cloud storage<br><br>\U0001f5d3\ufe0f Consultation Meetings<br>Timeline &amp; creative planning meetings<br><br>\U0001f681 Drone Coverage<br>Available depending on weather and venue<br>'

if old in content:
    content = content.replace(old, new)
    print('text OK')
else:
    print('NOT FOUND - trying index approach')
    idx = content.find('sie-service-1_2 se">')
    end = content.find('</p></div><div data-sid="service-1_3"', idx)
    old2 = content[idx + len('sie-service-1_2 se"><p class="se-t sie-service-1_2-text st-m-paragraph st-d-paragraph se-rc">'):end]
    content = content[:idx + len('sie-service-1_2 se"><p class="se-t sie-service-1_2-text st-m-paragraph st-d-paragraph se-rc">')] + new + content[end:]
    print('text OK via index')

# Ajustar altura container texto: 560px
content = content.replace(
    '.d .sie-service-1_2 {left:686px;top:196px;width:490px;height:360px;}',
    '.d .sie-service-1_2 {left:686px;top:196px;width:490px;height:620px;}'
)
content = content.replace(
    '.d .sie-service-1_2 {left:686px;top:196px;width:490px;height:560px;}',
    '.d .sie-service-1_2 {left:686px;top:196px;width:490px;height:620px;}'
)

# Ajustar posição "Starting at" e preço
content = content.replace(
    '.d .sie-service-1_3 {left:686px;top:589px;width:166px;height:16px;}',
    '.d .sie-service-1_3 {left:686px;top:840px;width:166px;height:16px;}'
)
content = content.replace(
    '.d .sie-service-1_3 {left:686px;top:780px;width:166px;height:16px;}',
    '.d .sie-service-1_3 {left:686px;top:840px;width:166px;height:16px;}'
)
content = content.replace(
    '.d .sie-service-1_4 {left:686px;top:613px;width:490px;height:48px;}',
    '.d .sie-service-1_4 {left:686px;top:864px;width:490px;height:48px;}'
)
content = content.replace(
    '.d .sie-service-1_4 {left:686px;top:804px;width:490px;height:48px;}',
    '.d .sie-service-1_4 {left:686px;top:864px;width:490px;height:48px;}'
)

# Aumentar seção
content = content.replace(
    '"slug":"service-1","visible":"a","states":[],"d":{"h":840,',
    '"slug":"service-1","visible":"a","states":[],"d":{"h":960,'
)
content = content.replace(
    '"slug":"service-1","visible":"a","states":[],"d":{"h":900,',
    '"slug":"service-1","visible":"a","states":[],"d":{"h":960,'
)
content = content.replace(
    '.d .sib-service-1 {height:840px;}',
    '.d .sib-service-1 {height:960px;}'
)
content = content.replace(
    '.d .sib-service-1 {height:900px;}',
    '.d .sib-service-1 {height:960px;}'
)

# Foto
content = content.replace(
    '.d .sie-service-1_0 {left:0px;top:0px;width:600px;height:840px;',
    '.d .sie-service-1_0 {left:0px;top:0px;width:600px;height:960px;'
)

open('services.html', 'w', encoding='utf-8').write(content)
print('Done')
