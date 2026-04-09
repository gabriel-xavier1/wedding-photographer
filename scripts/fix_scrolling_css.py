services = open('services.html', 'r', encoding='utf-8').read()

new_imgs = [
    'https://i.postimg.cc/mk9tCZWH/FBA073BF_9F8D_48C4_AC7D_9C9BB3FC1F19.jpg',
    'https://i.postimg.cc/VkSqrvwP/Emma_Emma_403.jpg',
    'https://i.postimg.cc/ZKk9ZN6n/TS_11618.jpg',
    'https://i.postimg.cc/nzgXXj56/B4020162_5A7B_41FD_9B4D_A29F4DC2823F_L0_001_22_03_2025_07_29_36.jpg',
    'https://i.postimg.cc/mk9tCZWH/FBA073BF_9F8D_48C4_AC7D_9C9BB3FC1F19.jpg',
    'https://i.postimg.cc/VkSqrvwP/Emma_Emma_403.jpg',
]

# Build CSS override rules
css_rules = ''
for i, url in enumerate(new_imgs):
    css_rules += f".d .sie-scrolling-images_{i} .se-img {{background-image:url('{url}') !important;background-size:cover !important;background-position:center center !important;}}\n"
    css_rules += f".m .sie-scrolling-images_{i} .se-img {{background-image:url('{url}') !important;background-size:cover !important;background-position:center center !important;}}\n"

# Remove old scrolling-images CSS overrides if any
import re
services = re.sub(r'[^\n]*sie-scrolling-images_\d[^\n]*background-image[^\n]*\n', '', services)

# Insert before </style>
style_close = services.find('</style>')
services = services[:style_close] + css_rules + services[style_close:]

# Also fix the Learn More button - hide it via CSS too (belt and suspenders)
if '.sie-intro_4 {display:none' not in services:
    extra_css = '.sie-intro_4 {display:none !important;}\n'
    style_close = services.find('</style>')
    services = services[:style_close] + extra_css + services[style_close:]

open('services.html', 'w', encoding='utf-8').write(services)
print("Done!")
