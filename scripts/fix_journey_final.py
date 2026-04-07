content = open('index.html', 'r', encoding='utf-8').read()

old = '<a href="services.html" style="text-decoration:none;"><button type="button" aria-label="The Journey" class="se-button weddings-journey-btn" style="background-color:rgba(198,99,57,1);border:none;padding:13px 28px;cursor:pointer;transition:background-color 0.3s ease;"><span style="color:#fff;font-family:inherit;font-size:inherit;letter-spacing:0.2em;text-transform:uppercase;">The Journey</span></button></a><style>.weddings-journey-btn:hover{background-color:rgba(41,38,36,1) !important;}</style>'

new = '<a href="services.html" style="text-decoration:none;"><button type="button" aria-label="The Journey" class="se-button weddings-journey-btn" style="background-color:rgba(198,99,57,1);border:none;width:220px;height:47px;padding:13px 28px;cursor:pointer;transition:background-color 0.3s ease,color 0.3s ease;"><span class="journey-span" style="color:#fff;font-family:inherit;font-size:inherit;letter-spacing:0.2em;text-transform:uppercase;">The Journey</span></button></a><style>.weddings-journey-btn:hover{background-color:#fff !important;}.weddings-journey-btn:hover .journey-span{color:rgba(41,38,36,1) !important;}</style>'

if old in content:
    content = content.replace(old, new)
    print('OK')
else:
    print('NOT FOUND')

open('index.html', 'w', encoding='utf-8').write(content)
