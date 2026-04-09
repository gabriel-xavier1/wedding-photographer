import re

services = open('services.html', 'r', encoding='utf-8').read()

# Map: element index -> new URL
updates = {
    0: 'https://i.postimg.cc/mk9tCZWH/FBA073BF_9F8D_48C4_AC7D_9C9BB3FC1F19.jpg',  # left large
    2: 'https://i.postimg.cc/jdVWKfy5/Emma_Emma_403.jpg',   # right top
    4: 'https://i.postimg.cc/ZKk9ZN6n/TS_11618.jpg',        # right bottom
}

# Remove old CSS overrides for scrolling-images
services = re.sub(r'[^\n]*sie-scrolling-images_\d[^\n]*background-image[^\n]*\n', '', services)

# Build new CSS
css = ''
for i, url in updates.items():
    css += f".d .sie-scrolling-images_{i} .se-img {{background-image:url('{url}') !important;background-size:cover !important;background-position:center center !important;}}\n"
    css += f".m .sie-scrolling-images_{i} .se-img {{background-image:url('{url}') !important;background-size:cover !important;background-position:center center !important;}}\n"

style_close = services.find('</style>')
services = services[:style_close] + css + services[style_close:]

open('services.html', 'w', encoding='utf-8').write(services)
print("Done!")
