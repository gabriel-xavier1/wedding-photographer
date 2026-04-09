import re

services = open('services.html', 'r', encoding='utf-8').read()

# Map: data-sid -> URL
photo_map = {
    'scrolling-images_0': 'https://i.postimg.cc/nzgXXj56/B4020162_5A7B_41FD_9B4D_A29F4DC2823F_L0_001_22_03_2025_07_29_36.jpg',
    'scrolling-images_2': 'https://i.postimg.cc/jdVWKfy5/Emma_Emma_403.jpg',
    'scrolling-images_3': 'https://i.postimg.cc/ZKk9ZN6n/TS_11618.jpg',
    'scrolling-images_5': 'https://i.postimg.cc/mk9tCZWH/FBA073BF_9F8D_48C4_AC7D_9C9BB3FC1F19.jpg',
}

for sid, url in photo_map.items():
    # Find the inner div with data-img="sid" and add/replace inline style
    # Pattern: <div style="width:100%;height:100%" data-img="scrolling-images_X" class="se-img ...">
    old = f'<div style="width:100%;height:100%" data-img="{sid}"'
    new = f'<div style="width:100%;height:100%;background-image:url(\'{url}\');background-size:cover;background-position:center center;" data-img="{sid}"'
    
    if old in services:
        services = services.replace(old, new)
        print(f"  Updated inline style for {sid}")
    else:
        # Try without the style attribute
        old2 = f'data-img="{sid}" class="se-img'
        if old2 in services:
            services = services.replace(
                old2,
                f'style="width:100%;height:100%;background-image:url(\'{url}\');background-size:cover;background-position:center center;" data-img="{sid}" class="se-img'
            )
            print(f"  Updated (alt) inline style for {sid}")
        else:
            print(f"  WARNING: {sid} not found!")

open('services.html', 'w', encoding='utf-8').write(services)
print("Done!")
