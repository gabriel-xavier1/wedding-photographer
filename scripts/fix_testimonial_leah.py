content = open('index.html', 'r', encoding='utf-8').read()

# Nome
content = content.replace(
    'class="sie-testimonials_view-1_0 se"><p class="se-t sie-testimonials_view-1_0-text st-m-title st-d-title se-rc">Leah &amp; Ryan<br></p>',
    'class="sie-testimonials_view-1_0 se"><p class="se-t sie-testimonials_view-1_0-text st-m-title st-d-title se-rc">Herni &amp; Graham<br></p>'
)

# Texto
idx = content.find('"Choosing Willow was the easiest part of our elopement.')
end = content.find('<br></p></div></div></div><div id="testimonials_view-1-1"', idx)
old_text = content[idx:end + len('<br>')]

new_text = '"I\'m from South East Asia and my Husband is from Scotland descendants. On our wedding we were wearing two different outfits for ceremony in the morning and evening party. Our Photographer Jacque Prates was great, she was professional, she guided us how to pose for the pictures — also candid pictures — and the results were absolutely amazing. Everyone was amazed with the results. Thank you Jacque Prates!"<br>'

content = content.replace(old_text, new_text)
print('OK')

open('index.html', 'w', encoding='utf-8').write(content)
