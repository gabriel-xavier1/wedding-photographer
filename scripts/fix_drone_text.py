with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'margin-top:24px;text-transform:uppercase;letter-spacing:0.2em;font-size:13px;font-family:\'Overpass\';font-weight:500;">Drone available, weather and venue depending.',
    'margin-top:24px;text-transform:uppercase;letter-spacing:0.2em;font-size:10px;font-family:\'Overpass\';font-weight:500;">Drone available, weather and venue depending.'
)

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('done')
