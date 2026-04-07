content = open('index.html', 'r', encoding='utf-8').read()

old = '<a href="services.html" style="text-decoration:none;"><button type="button" aria-label="The Journey" class="se-button st-primary" style="background-color:rgba(244,239,233,1);color:rgba(41,38,36,1);border-color:rgba(244,239,233,1);"><span class="st-m-primary st-d-primary" style="color:rgba(41,38,36,1);">The Journey</span></button></a>'

new = '''<a href="services.html" style="text-decoration:none;"><button type="button" aria-label="The Journey" class="se-button weddings-journey-btn" style="background-color:rgba(198,99,57,1);border:none;padding:13px 28px;cursor:pointer;transition:background-color 0.3s ease;"><span style="color:#fff;font-family:inherit;font-size:inherit;letter-spacing:0.2em;text-transform:uppercase;">The Journey</span></button></a><style>.weddings-journey-btn:hover{background-color:#fff !important;}.weddings-journey-btn:hover span{color:rgba(41,38,36,1) !important;}</style>'''

if old in content:
    content = content.replace(old, new)
    print('OK')
else:
    print('NOT FOUND')

open('index.html', 'w', encoding='utf-8').write(content)
