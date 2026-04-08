content = open('index.html', 'r', encoding='utf-8').read()

# Nome
content = content.replace(
    'class="sie-testimonials_view-1-1_0 se"><p class="se-t sie-testimonials_view-1-1_0-text st-m-title st-d-title se-rc">Maya &amp; Tom<br></p>',
    'class="sie-testimonials_view-1-1_0 se"><p class="se-t sie-testimonials_view-1-1_0-text st-m-title st-d-title se-rc">Martha &amp; Matt<br></p>'
)

# Encontrar e substituir o texto exato
idx = content.find('Willow captured our day')
end = content.find('<br><br></p></div></div></div><div id="tes', idx)
old_text = content[idx:end + len('<br><br>')]
new_text = 'Where do I even start\u2026 Jacque was perfect from start to finish! We had 3 calls prior to the wedding which made us feel so at ease. Throughout the day Jacque was organised and made sure all the photos we had asked for were taken. So many of our guests commented on how lovely Jacque was and she really made our day special! We got our pictures back quickly and love them all! We cannot recommend Jacque enough! Thank you! \u2764\ufe0f"<br><br>'

content = content.replace(old_text, new_text)
print('OK')

open('index.html', 'w', encoding='utf-8').write(content)
