content = open('index.html', 'r', encoding='utf-8').read()

old = '<a href="services.html" style="text-decoration:none;"><button type="button" aria-label="The Journey" class="se-button st-primary"><span class="st-m-primary st-d-primary">The Journey</span></button></a>'

new = '<a href="services.html" style="text-decoration:none;"><button type="button" aria-label="The Journey" class="se-button st-primary" style="background-color:rgba(244,239,233,1);color:rgba(41,38,36,1);border-color:rgba(244,239,233,1);"><span class="st-m-primary st-d-primary" style="color:rgba(41,38,36,1);">The Journey</span></button></a>'

if old in content:
    content = content.replace(old, new)
    print('OK')
else:
    print('NOT FOUND')

open('index.html', 'w', encoding='utf-8').write(content)
