with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

btn = '<br><br><a href="contact.html" style="display:inline-block;margin-top:8px;padding:14px 36px;background-color:#c0522a;color:#fff;text-decoration:none;letter-spacing:0.15em;font-size:13px;font-family:\'Overpass\',sans-serif;font-weight:500;text-transform:uppercase;">INQUIRE</a>'

content = content.replace(btn, '')

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('done')
