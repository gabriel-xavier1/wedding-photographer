content = open('index.html', 'r', encoding='utf-8').read()

# Slide 1 (Herni & Graham) - achar e substituir pelo indice
idx1 = content.find('sie-testimonials_view-1_1 se">')
end1 = content.find('</p></div></div></div><div id="testimonials_view-1-1"', idx1)
old1 = content[idx1:end1 + len('</p>')]
new1 = 'sie-testimonials_view-1_1 se"><p class="se-t sie-testimonials_view-1_1-text st-m-heading st-d-heading se-rc">"I\'m from South East Asia and my Husband is from Scotland descendants. On our wedding we were wearing two different outfits for ceremony in the morning and evening party. Our Photographer Jacque Prates was great, she was professional, she guided us how to pose for the pictures \u2014 also candid pictures \u2014 and the results were absolutely amazing. Everyone was amazed with the results. Thank you Jacque Prates!"</p>'
content = content.replace(old1, new1)
print('Slide 1 OK')

# Slide 2 (Martha & Matt) - achar e substituir pelo indice
idx2 = content.find('sie-testimonials_view-1-1_1 se">')
end2 = content.find('</p></div></div></div><div id="testimonials_view-1-2"', idx2)
old2 = content[idx2:end2 + len('</p>')]
new2 = 'sie-testimonials_view-1-1_1 se"><p class="se-t sie-testimonials_view-1-1_1-text st-m-heading st-d-heading se-rc">"Where do I even start\u2026 Jacque was perfect from start to finish! We had 3 calls prior to the wedding which made us feel so at ease. Throughout the day Jacque was organised and made sure all the photos we had asked for were taken. So many of our guests commented on how lovely Jacque was and she really made our day special! We got our pictures back quickly and love them all! We cannot recommend Jacque enough! Thank you! \u2764\ufe0f"</p>'
content = content.replace(old2, new2)
print('Slide 2 OK')

open('index.html', 'w', encoding='utf-8').write(content)
