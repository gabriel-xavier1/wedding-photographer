with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Trocar heading "HI\nI AM" para "MEET YOUR\nPHOTOGRAPHER,"
content = content.replace(
    '<p class="se-t sie-about_2-text st-m-heading st-d-heading se-rc">HI<br>I AM<br></p>',
    '<p class="se-t sie-about_2-text st-m-heading st-d-heading se-rc">MEET YOUR<br>PHOTOGRAPHER,<br></p>'
)
print('about_2 heading updated')

# 2. Trocar nome "Willow." para "Jacque."
content = content.replace(
    '<p class="se-t sie-about_5-text st-m-title st-d-title se-rc">Willow.<br></p>',
    '<p class="se-t sie-about_5-text st-m-title st-d-title se-rc">Jacque.<br></p>'
)
print('about_5 name updated')

# 3. Trocar foto about_3 para a foto da Jacque
# Substituir o div da imagem about_3 com a URL da Jacque
old_img = 'data-sid="about_3" class="sie-about_3 se"><div style="width:100%;height:100%" data-img="about_3" class="se-img se-gr slzy"></div><noscript><img src="//static.showit.co/400/rrCs5PsGvZ-lALVbMzbPSA/135701/sandra-seitamaa-6a23hx3xkdo-unsplash.jpg" class="se-img" alt="" title="sandra-seitamaa-6a23hx3xkdo-unsplash"/></noscript>'
new_img = 'data-sid="about_3" class="sie-about_3 se"><div style="width:100%;height:100%;background-image:url(\'https://i.postimg.cc/V5P1f0DJ/Whats_App_Image_2026_02_06_at_17_55_03.jpg\');background-size:cover;background-position:center center;" data-img="about_3" class="se-img se-gr slzy"></div><noscript><img src="https://i.postimg.cc/V5P1f0DJ/Whats_App_Image_2026_02_06_at_17_55_03.jpg" class="se-img" alt="" title="Jacque"/></noscript>'

if old_img in content:
    content = content.replace(old_img, new_img, 1)
    print('about_3 photo updated')
else:
    # Try to find what's there
    idx = content.find('data-sid="about_3"')
    print('about_3 NOT FOUND, current:', repr(content[idx:idx+200]) if idx != -1 else 'nothing')

# 4. Also update CSS to force the image
old_css = '.d .sie-about_3 .se-img {background-repeat:no-repeat;background-size:cover;background-position:50% 50%;border-radius:inherit;}'
new_css = ".d .sie-about_3 .se-img {background-repeat:no-repeat;background-size:cover;background-position:center center;border-radius:inherit;background-image:url('https://i.postimg.cc/V5P1f0DJ/Whats_App_Image_2026_02_06_at_17_55_03.jpg') !important;}"
if old_css in content:
    content = content.replace(old_css, new_css, 1)
    print('about_3 CSS updated')

old_css_m = '.m .sie-about_3 .se-img {background-repeat:no-repeat;background-size:cover;background-position:50% 50%;border-radius:inherit;}'
new_css_m = ".m .sie-about_3 .se-img {background-repeat:no-repeat;background-size:cover;background-position:center center;border-radius:inherit;background-image:url('https://i.postimg.cc/V5P1f0DJ/Whats_App_Image_2026_02_06_at_17_55_03.jpg') !important;}"
if old_css_m in content:
    content = content.replace(old_css_m, new_css_m, 1)
    print('about_3 CSS mobile updated')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
