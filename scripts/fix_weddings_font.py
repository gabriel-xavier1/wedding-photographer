content = open('index.html', 'r', encoding='utf-8').read()

content = content.replace(
    ".d .sie-weddings_title-text {color:#ffffff;font-size:72px;line-height:1;}",
    ".d .sie-weddings_title-text {color:#ffffff;font-size:72px;line-height:1;font-family:'Instrument Serif';}"
)
content = content.replace(
    ".d .sie-weddings_text-text {color:#d4cfc4;font-size:16px;line-height:1.8;text-align:left;}",
    ".d .sie-weddings_text-text {color:#d4cfc4;font-size:16px;line-height:1.8;text-align:left;font-family:'Instrument Sans';}"
)

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
