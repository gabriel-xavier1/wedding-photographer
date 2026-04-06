content = open('index.html', 'r', encoding='utf-8').read()

weddings_section = '''<div id="weddings" data-bid="weddings" class="sb sib-weddings"><style>
.sib-weddings { background-color: #2c2e1e; }
.d .sie-weddings-title { position:absolute; left:58px; top:60px; width:500px; }
.sie-weddings-title-text { color:#fff; font-size:80px; font-family:inherit; line-height:1; }
.d .sie-weddings-text { position:absolute; left:58px; top:180px; width:500px; }
.sie-weddings-text-text { color:#d4cfc4; font-size:16px; line-height:1.7; }
.d .sie-weddings-btn { position:absolute; left:58px; top:430px; width:300px; }
.sie-weddings-btn-text { color:#fff; font-size:18px; }
.d .sie-weddings-photo { position:absolute; right:0; top:0; width:480px; height:500px; }
.d .sie-weddings-video { position:absolute; left:58px; top:540px; width:900px; height:420px; }
.sib-weddings .sc { position:relative; height:1000px; }
</style><div class="ss-s ss-bg"><div class="sc" style="width:1200px">
<div class="sie-weddings-title"><h2 class="sie-weddings-title-text">Weddings</h2></div>
<div class="sie-weddings-text"><p class="sie-weddings-text-text">Every wedding is unique.<br>Every couple brings their own story, history, and energy. That\'s what makes each wedding day truly unforgettable.<br>It\'s in the laughter.<br>The happy tears.<br>The quiet, calm moments before everything begins.<br>This isn\'t just a collection of pretty photos.<br>It\'s a journey from start to finish.</p></div>
<div class="sie-weddings-btn"><p class="sie-weddings-btn-text"><span style="display:inline-block;width:200px;border-bottom:1px solid #fff;vertical-align:middle;margin-right:12px;"></span><a href="services.html" style="color:#fff;text-decoration:none;">The Journey</a></p></div>
<div class="sie-weddings-photo"><img src="https://images.unsplash.com/photo-1519741497674-611481863552?w=960" style="width:100%;height:100%;object-fit:cover;" alt="Wedding photography"/></div>
<div class="sie-weddings-video"><video controls poster="" style="width:100%;height:100%;object-fit:cover;border-radius:8px;"><source src="" type="video/mp4"/></video><p style="color:#888;font-size:12px;margin-top:8px;text-align:center;">[ Video placeholder — substitua pela URL do vídeo ]</p></div>
</div></div></div>'''

insert_before = '<div id="testimonials"'

if insert_before in content:
    content = content.replace(insert_before, weddings_section + insert_before)
    print('OK')
else:
    print('NOT FOUND')

open('index.html', 'w', encoding='utf-8').write(content)
