content = open('index.html', 'r', encoding='utf-8').read()

old = '''<p class="se-t sie-weddings_btn-text"><span style="display:inline-block;width:180px;border-bottom:1px solid #fff;vertical-align:middle;margin-right:10px;"></span><a href="services.html" style="color:#fff;text-decoration:none;font-family:inherit;">The Journey</a></p>'''

new = '''<a href="services.html" class="investment-btn" style="display:flex;align-items:center;gap:20px;text-decoration:none;color:#fff;cursor:pointer;transition:opacity 0.3s ease;width:100%;"><span class="line" style="flex:1;height:4px;background:#fff;position:relative;transition:transform 0.3s ease;transform-origin:right;"><span style="position:absolute;right:-2px;top:50%;width:14px;height:14px;border-top:4px solid #fff;border-right:4px solid #fff;transform:translateY(-50%) rotate(45deg);"></span></span><span style="font-family:\'Playfair Display\', serif;font-size:34px;white-space:nowrap;">the journey</span></a><style>.investment-btn:hover{opacity:0.7;}.investment-btn:hover .line{transform:scaleX(1.05);}</style>'''

if old in content:
    content = content.replace(old, new)
    print('OK')
else:
    print('NOT FOUND')

open('index.html', 'w', encoding='utf-8').write(content)
