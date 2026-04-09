content = open('services.html', 'r', encoding='utf-8').read()

img_url = 'https://i.postimg.cc/W37p5D82/Amber_Max_83.jpg'

new_section = f'''
<div id="collage-intro" style="background-color:#3a3a32;padding:60px 40px 50px;text-align:center;">
  <div style="max-width:800px;margin:0 auto;">
    <p style="color:#ffffff;font-family:'Instrument Serif',serif;font-size:22px;line-height:1.7;margin-bottom:24px;">
      Imagine looking back on your images, feeling like you're instantly transported back to that moment on your wedding day.
    </p>
    <p style="color:#ffffff;font-family:'Instrument Serif',serif;font-size:22px;line-height:1.7;margin-bottom:24px;">
      Or you want images that truly reflect the uninhibited personality of your mates.
    </p>
    <p style="color:#ffffff;font-family:'Instrument Serif',serif;font-size:22px;line-height:1.7;margin-bottom:40px;">
      Those are the photos I'd want from my wedding day, that's for sure!
    </p>
  </div>
  <div style="max-width:1100px;margin:0 auto;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(2,220px);gap:8px;">
    <div style="overflow:hidden;"><img src="{img_url}" style="width:100%;height:100%;object-fit:cover;display:block;" alt="wedding photo"/></div>
    <div style="overflow:hidden;"><img src="{img_url}" style="width:100%;height:100%;object-fit:cover;display:block;" alt="wedding photo"/></div>
    <div style="overflow:hidden;"><img src="{img_url}" style="width:100%;height:100%;object-fit:cover;display:block;" alt="wedding photo"/></div>
    <div style="overflow:hidden;"><img src="{img_url}" style="width:100%;height:100%;object-fit:cover;display:block;" alt="wedding photo"/></div>
    <div style="overflow:hidden;"><img src="{img_url}" style="width:100%;height:100%;object-fit:cover;display:block;" alt="wedding photo"/></div>
    <div style="overflow:hidden;"><img src="{img_url}" style="width:100%;height:100%;object-fit:cover;display:block;" alt="wedding photo"/></div>
  </div>
</div>
'''

# Insert before navigation-services block
marker = '<div id="navigation-services"'
content = content.replace(marker, new_section + marker)

open('services.html', 'w', encoding='utf-8').write(content)
print("Done!")
