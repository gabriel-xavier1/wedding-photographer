import re

services = open('services.html', 'r', encoding='utf-8').read()

new_imgs = [
    'https://i.postimg.cc/mk9tCZWH/FBA073BF_9F8D_48C4_AC7D_9C9BB3FC1F19.jpg',
    'https://i.postimg.cc/VkSqrvwP/Emma_Emma_403.jpg',
    'https://i.postimg.cc/ZKk9ZN6n/TS_11618.jpg',
    'https://i.postimg.cc/nzgXXj56/B4020162_5A7B_41FD_9B4D_A29F4DC2823F_L0_001_22_03_2025_07_29_36.jpg',
    'https://i.postimg.cc/mk9tCZWH/FBA073BF_9F8D_48C4_AC7D_9C9BB3FC1F19.jpg',  # repeat
    'https://i.postimg.cc/VkSqrvwP/Emma_Emma_403.jpg',  # repeat
]

# Find each scrolling-images_X element and replace the img src
for i in range(6):
    sid = f'scrolling-images_{i}'
    # Find the data-img attribute and replace the background image URL
    # Pattern: data-img="scrolling-images_X" ... src="OLD_URL"
    pattern = rf'(data-sid="{sid}"[^>]*>.*?<noscript><img src=")[^"]+(")'
    replacement = rf'\g<1>{new_imgs[i]}\g<2>'
    new_services = re.sub(pattern, replacement, services, flags=re.DOTALL, count=1)
    if new_services != services:
        services = new_services
        print(f"  Updated {sid}")
    else:
        print(f"  {sid} not found or unchanged")

open('services.html', 'w', encoding='utf-8').write(services)
print("Done!")
