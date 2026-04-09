content = open('services.html', 'r', encoding='utf-8').read()

imgs = [
    'https://i.postimg.cc/ZKk9ZN6n/TS_11618.jpg',
    'https://i.postimg.cc/nzgXXj56/B4020162_5A7B_41FD_9B4D_A29F4DC2823F_L0_001_22_03_2025_07_29_36.jpg',
    'https://i.postimg.cc/qqvhR7sh/Chloe_Loius_366_2048x1365.jpg',
    'https://i.postimg.cc/gJ0yCMq1/Mr_Mrs_Scobell.png',
    'https://i.postimg.cc/dQpjd8r5/Joe_Sarka.png',
    'https://i.postimg.cc/W37p5D82/Amber_Max_83.jpg',
]

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
      <img src="{imgs[0]}" style="width:100%;height:100%;object-fit:cover;display:block;" alt=""/>
    </div>
    <div style="position:absolute;left:33%;top:0;width:34%;height:300px;overflow:hidden;">
      <img src="{imgs[1]}" style="width:100%;height:100%;object-fit:cover;display:block;" alt=""/>
    </div>
    <div style="position:absolute;right:0;top:0;width:31%;height:260px;overflow:hidden;">
      <img src="{imgs[2]}" style="width:100%;height:100%;object-fit:cover;display:block;" alt=""/>
    </div>
    <!-- Bottom row -->
    <div style="position:absolute;left:0;top:240px;width:22%;height:240px;overflow:hidden;">
      <img src="{imgs[3]}" style="width:100%;height:100%;object-fit:cover;display:block;" alt=""/>
    </div>
    <div style="position:absolute;left:23%;top:270px;width:34%;height:210px;overflow:hidden;">
      <img src="{imgs[4]}" style="width:100%;height:100%;object-fit:cover;display:block;" alt=""/>
    </div>
    <div style="position:absolute;right:0;top:240px;width:40%;height:240px;overflow:hidden;">
      <img src="{imgs[5]}" style="width:100%;height:100%;object-fit:cover;display:block;" alt=""/>
    </div>
  </div>
</div>
'''

# Replace existing collage section
old_start = content.find('<div id="collage-intro"')
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
