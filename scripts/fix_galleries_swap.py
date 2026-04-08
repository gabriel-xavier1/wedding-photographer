content = open('index.html', 'r', encoding='utf-8').read()

# Foto 2: Clara & Edgar -> Joe & Sarka
content = content.replace(
    "url('https://i.postimg.cc/ZKk9ZN6n/TS_11618.jpg')",
    "url('https://i.postimg.cc/dQpjd8r5/Joe-Sarka.png')"
)
content = content.replace(
    'background-image:url(\'https://i.postimg.cc/ZKk9ZN6n/TS_11618.jpg\')',
    'background-image:url(\'https://i.postimg.cc/dQpjd8r5/Joe-Sarka.png\')'
)
content = content.replace('>Clara &amp; Edgar<br>', '>Joe &amp; Sarka<br>')
content = content.replace('"https://i.postimg.cc/ZKk9ZN6n/TS_11618.jpg"', '"https://i.postimg.cc/dQpjd8r5/Joe-Sarka.png"')

# Foto 3: Ada & Joshua -> Mr & Mrs Scobell
content = content.replace(
    "url('https://i.postimg.cc/8zn0X6VX/ada_e_joshua.png')",
    "url('https://i.postimg.cc/gJ0yCMq1/Mr-Mrs-Scobell.png')"
)
content = content.replace(
    'background-image:url(\'https://i.postimg.cc/8zn0X6VX/ada_e_joshua.png\')',
    'background-image:url(\'https://i.postimg.cc/gJ0yCMq1/Mr-Mrs-Scobell.png\')'
)
content = content.replace('>Ada &amp; Joshua<br>', '>Mr &amp; Mrs Scobell<br>')
content = content.replace('"https://i.postimg.cc/8zn0X6VX/ada_e_joshua.png"', '"https://i.postimg.cc/gJ0yCMq1/Mr-Mrs-Scobell.png"')

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
