content = open('services.html', 'r', encoding='utf-8').read()

img = 'https://i.postimg.cc/W37p5D82/Amber_Max_83.jpg'

new_section = f'''
<div id="collage-intro" style="background-color:#3d3d30;padding:60px 40px 60px;text-align:center;">
  <div style="max-width:820px;margin:0 auto 48px;">
    <p style="color:#ffffff;font-family:'Instrument Serif',serif;font-size:21px;line-height:1.8;margin-bottom:20px;">
      Imagine looking back on your images, feeling like you're instantly transported back to that moment on your wedding day.
    </p>
    <p style="color:#ffffff;font-family:'Instrument Serif',serif;font-size:21px;line-height:1.8;margin-bottom:20px;">
      Or you want images that truly reflect the uninhibited personality of your mates.
    </p>
    <p style="color:#ffffff;font-family:'Instrument Serif',serif;font-size:21px;line-height:1.8;">
      Those are the photos I'd want from my wedding day, that's for sure!
    </p>
  </div>
  <!-- Collage -->
  <div style="max-width:1100px;margin:0 auto;position:relative;height:480px;">
    <!-- Top row -->
    <div style="position:absolute;left:0;top:0;width:32%;height:260px;overflow:hidden;">
      <img src="{img}" style="width:100%;height:100%;object-fit:cover;display:block;" alt=""/>
    </div>
    <div style="position:absolute;left:33%;top:0;width:34%;height:300px;overflow:hidden;">
      <img src="{img}" style="width:100%;height:100%;object-fit:cover;display:block;" alt=""/>
    </div>
    <div style="position:absolute;right:0;top:0;width:31%;height:260px;overflow:hidden;">
      <img src="{img}" style="width:100%;height:100%;object-fit:cover;display:block;" alt=""/>
    </div>
    <!-- Bottom row -->
    <div style="position:absolute;left:0;top:240px;width:22%;height:240px;overflow:hidden;">
      <img src="{img}" style="width:100%;height:100%;object-fit:cover;display:block;" alt=""/>
    </div>
    <div style="position:absolute;left:23%;top:270px;width:34%;height:210px;overflow:hidden;">
      <img src="{img}" style="width:100%;height:100%;object-fit:cover;display:block;" alt=""/>
    </div>
    <div style="position:absolute;right:0;top:240px;width:40%;height:240px;overflow:hidden;">
      <img src="{img}" style="width:100%;height:100%;object-fit:cover;display:block;" alt=""/>
    </div>
  </div>
</div>
'''

# Replace existing collage section
old_start = content.find('<div id="collage-intro"')
old_end = content.find('</div>', content.find('</div>', old_start + 1))
# Find the closing of the whole section (multiple nested divs)
depth = 0
i = old_start
while i < len(content):
    if content[i:i+4] == '<div':
        depth += 1
    elif content[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            old_end = i + 6
            break
    i += 1

content = content[:old_start] + new_section + content[old_end:]

open('services.html', 'w', encoding='utf-8').write(content)
print("Done!")
