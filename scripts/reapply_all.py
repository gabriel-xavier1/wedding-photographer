content = open('index.html', 'r', encoding='utf-8').read()

# 1. Trocar video tag por iframe com parallax
old_video = '<div data-sid="weddings_video" class="sie-weddings_video se"><video controls style="width:100%;height:100%;object-fit:cover;border-radius:6px;" poster=""><source src="" type="video/mp4"/></video></div>'
new_video = '<div data-sid="weddings_video" class="sie-weddings_video se video-reveal"><iframe width="100%" height="100%" src="https://www.youtube.com/embed/Qxn61VjTaZ4?si=TCKzufLCysVfLOVy" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="border-radius:6px;display:block;"></iframe></div><style>.video-reveal{opacity:0;transform:translateY(40px);transition:opacity 0.9s ease,transform 0.9s ease;}.video-reveal.visible{opacity:1;transform:translateY(0);}</style><script>(function(){var el=document.querySelector(\'.video-reveal\');if(!el)return;var obs=new IntersectionObserver(function(entries){entries.forEach(function(e){if(e.isIntersecting){el.classList.add(\'visible\');obs.disconnect();}});},{threshold:0.15});obs.observe(el);})();</script>'

if old_video in content:
    content = content.replace(old_video, new_video)
    print('video OK')
else:
    print('video NOT FOUND')

# 2. Tamanho do video
content = content.replace(
    '.d .sie-weddings_video {position:absolute;left:58px;top:640px;width:900px;height:400px;}',
    '.d .sie-weddings_video {position:absolute;left:58px;top:640px;width:1142px;height:643px;}'
)

# 3. Altura da seção
content = content.replace(
    '.d .sib-weddings {height:1120px;}',
    '.d .sib-weddings {height:1363px;}'
)

# 4. Testimonial Herni & Graham
content = content.replace(
    '>Leah &amp; Ryan<br></p>',
    '>Herni &amp; Graham<br></p>'
)
content = content.replace(
    '"Choosing Willow was the easiest part of our elopement. She made the whole experience feel <i>effortless and deeply meaningful</i>. Our photos feel like us \u2014 the quiet moments, the wild ones, the ones we didn\u2019t even know she saw. <i>We\u2019ll treasure them forever.</i>"<br>',
    '"I\'m from South East Asia and my Husband is from Scotland descendants. On our wedding we were wearing two different outfits for ceremony in the morning and evening party. Our Photographer Jacque Prates was great, she was professional, she guided us how to pose for the pictures \u2014 also candid pictures \u2014 and the results were absolutely amazing. Everyone was amazed with the results. Thank you Jacque Prates!"<br>'
)

# 5. Testimonial Martha & Matt
content = content.replace(
    '>Maya &amp; Tom<br></p>',
    '>Martha &amp; Matt<br></p>'
)
content = content.replace(
    '"Willow captured our day with such tenderness and intention. She didn\u2019t just take photos \u2014 <i>she held space for every emotion, every breath, every little spark between us</i>. Looking at our gallery feels like stepping back into the exact magic of that day."<br><br>',
    '"Where do I even start\u2026 Jacque was perfect from start to finish! We had 3 calls prior to the wedding which made us feel so at ease. Throughout the day Jacque was organised and made sure all the photos we had asked for were taken. So many of our guests commented on how lovely Jacque was and she really made our day special! We got our pictures back quickly and love them all! We cannot recommend Jacque enough! Thank you! \u2764\ufe0f"<br><br>'
)

# 6. Font size Martha & Matt
content = content.replace(
    '.d .sie-testimonials_view-1-1_1-text {color:rgba(255,255,255,1);font-size:35px;text-align:center;}',
    '.d .sie-testimonials_view-1-1_1-text {color:rgba(255,255,255,1);font-size:20px;text-align:center;}'
)

open('index.html', 'w', encoding='utf-8').write(content)
print('All done')
