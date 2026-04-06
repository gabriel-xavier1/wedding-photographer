content = open('index.html', 'r', encoding='utf-8').read()

# Remover seção anterior mal inserida
old_section_start = '<div id="weddings" data-bid="weddings" class="sb sib-weddings">'
old_section_end = '</div><div id="testimonials"'

if old_section_start in content:
    start = content.find(old_section_start)
    end = content.find('</div><div id="testimonials"') + len('</div>')
    content = content[:start] + '<div id="testimonials"' + content[end+len('<div id="testimonials"'):]
    print('Removed old section')

# CSS da nova seção no bloco de estilos existente
css_insert = '''.d .sib-weddings {height:980px;background-color:#2c2e1e;}
.m .sib-weddings {height:1200px;background-color:#2c2e1e;}
.d .sie-weddings_title {position:absolute;left:58px;top:60px;width:520px;height:120px;}
.d .sie-weddings_title-text {color:#ffffff;font-size:80px;line-height:1;}
.m .sie-weddings_title {position:absolute;left:25px;top:50px;width:270px;height:80px;}
.m .sie-weddings_title-text {color:#ffffff;font-size:48px;}
.d .sie-weddings_text {position:absolute;left:58px;top:200px;width:500px;height:200px;}
.d .sie-weddings_text-text {color:#d4cfc4;font-size:16px;line-height:1.8;text-align:left;}
.m .sie-weddings_text {position:absolute;left:25px;top:150px;width:270px;height:250px;}
.m .sie-weddings_text-text {color:#d4cfc4;font-size:15px;line-height:1.8;}
.d .sie-weddings_btn {position:absolute;left:58px;top:430px;width:320px;height:30px;}
.d .sie-weddings_btn-text {color:#ffffff;font-size:18px;}
.m .sie-weddings_btn {position:absolute;left:25px;top:420px;width:270px;height:30px;}
.m .sie-weddings_btn-text {color:#ffffff;font-size:16px;}
.d .sie-weddings_photo {position:absolute;right:0;top:0;width:500px;height:480px;}
.m .sie-weddings_photo {position:absolute;left:0;top:490px;width:320px;height:220px;}
.d .sie-weddings_video {position:absolute;left:58px;top:510px;width:900px;height:420px;}
.m .sie-weddings_video {position:absolute;left:10px;top:730px;width:300px;height:220px;}
.sie-weddings_video video {width:100%;height:100%;object-fit:cover;border-radius:6px;}
'''

# Inserir CSS antes do fechamento do bloco de estilos
css_end = '</style>'
first_style_end = content.find(css_end)
content = content[:first_style_end] + css_insert + content[first_style_end:]

# HTML da seção no padrão Showit
weddings_html = '''<div id="weddings" data-bid="weddings" class="sb sib-weddings"><div class="ss-s ss-bg"><div class="sc" style="width:1200px"><div data-sid="weddings_title" class="sie-weddings_title se"><h2 class="se-t sie-weddings_title-text">Weddings</h2></div><div data-sid="weddings_text" class="sie-weddings_text se"><p class="se-t sie-weddings_text-text">Every wedding is unique.<br>Every couple brings their own story, history, and energy.<br>That\'s what makes each wedding day truly unforgettable.<br>It\'s in the laughter.<br>The happy tears.<br>The quiet, calm moments before everything begins.<br>This isn\'t just a collection of pretty photos.<br>It\'s a journey from start to finish.</p></div><div data-sid="weddings_btn" class="sie-weddings_btn se"><p class="se-t sie-weddings_btn-text"><span style="display:inline-block;width:180px;border-bottom:1px solid #fff;vertical-align:middle;margin-right:10px;"></span><a href="services.html" style="color:#fff;text-decoration:none;font-family:inherit;">The Journey</a></p></div><div data-sid="weddings_photo" class="sie-weddings_photo se"><img src="https://images.unsplash.com/photo-1519741497674-611481863552?w=960" style="width:100%;height:100%;object-fit:cover;" alt="Wedding photography"/></div><div data-sid="weddings_video" class="sie-weddings_video se"><video controls style="width:100%;height:100%;object-fit:cover;border-radius:6px;" poster=""><source src="" type="video/mp4"/></video></div></div></div></div>'''

# Inserir antes do testimonials
insert_before = '<div id="testimonials"'
if insert_before in content:
    content = content.replace(insert_before, weddings_html + insert_before, 1)
    print('OK - section inserted')
else:
    print('NOT FOUND')

open('index.html', 'w', encoding='utf-8').write(content)
