content = open('index.html', 'r', encoding='utf-8').read()

# Igualar font-size do The Journey ao título (72px) e mesma font-family
content = content.replace(
    "font-family:'Playfair Display', serif;font-size:34px;white-space:nowrap;",
    "font-family:'Instrument Serif';font-size:72px;white-space:nowrap;"
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
