content = open('index.html', 'r', encoding='utf-8').read()

# 1. Herni & Graham (view-1 = primeiro slide)
content = content.replace(
    '>Leah &amp; Ryan<br></p>',
    '>Herni &amp; Graham<br></p>'
)
content = content.replace(
    '"Choosing Willow was the easiest part of our elopement. She made the whole experience feel <i>effortless and deeply meaningful</i>. Our photos feel like us \u2014 the quiet moments, the wild ones, the ones we didn\u2019t even know she saw. <i>We\u2019ll treasure them forever.</i>"<br>',
    '"I\'m from South East Asia and my Husband is from Scotland descendants. On our wedding we were wearing two different outfits for ceremony in the morning and evening party. Our Photographer Jacque Prates was great, she was professional, she guided us how to pose for the pictures \u2014 also candid pictures \u2014 and the results were absolutely amazing. Everyone was amazed with the results. Thank you Jacque Prates!"<br>'
)

# 2. Martha & Matt (view-1-1 = segundo slide)
content = content.replace(
    '>Maya &amp; Tom<br></p>',
    '>Martha &amp; Matt<br></p>'
)
content = content.replace(
    '"Willow captured our day with such tenderness and intention. She didn\u2019t just take photos \u2014 <i>she held space for every emotion, every breath, every little spark between us</i>. Looking at our gallery feels like stepping back into the exact magic of that day."<br><br>',
    '"Where do I even start\u2026 Jacque was perfect from start to finish! We had 3 calls prior to the wedding which made us feel so at ease. Throughout the day Jacque was organised and made sure all the photos we had asked for were taken. So many of our guests commented on how lovely Jacque was and she really made our day special! We got our pictures back quickly and love them all! We cannot recommend Jacque enough! Thank you! \u2764\ufe0f"<br><br>'
)

# 3. Font size do segundo slide
content = content.replace(
    '.d .sie-testimonials_view-1-1_1-text {color:rgba(255,255,255,1);font-size:35px;text-align:center;}',
    '.d .sie-testimonials_view-1-1_1-text {color:rgba(255,255,255,1);font-size:20px;text-align:center;}'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
