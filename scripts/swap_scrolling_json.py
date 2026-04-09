import re

services = open('services.html', 'r', encoding='utf-8').read()

# The Showit JS reads "c": {"key": "..."} from JSON to load images
# We need to swap the "key" values for _0 (top-left) and _5 (bottom-left)

# Current state based on CSS:
# _5 is at top:34px (top-left) with FBA073BF
# _0 is at top:-745px (bottom-left scroll) with B4020162
# User wants to swap: FBA073BF goes to bottom, B4020162 goes to top

# Find and swap the "c" key values in JSON for scrolling-images_0 and scrolling-images_5
# Also swap the noscript src in HTML

# Step 1: Find JSON element for scrolling-images_0 and get its "c" key
script_end = services.find('</script>')
init_data = services[:script_end]

def get_elem_c_key(content, elem_id):
    marker = f'"id": "{elem_id}"'
    idx = content.find(marker)
    if idx < 0:
        marker = f'"id":"{elem_id}"'
        idx = content.find(marker)
    if idx < 0:
        return None, -1, -1
    # Find "c": {"key": "..."} after this position
    c_idx = content.find('"c": {', idx)
    if c_idx < 0:
        c_idx = content.find('"c":{', idx)
    if c_idx < 0:
        return None, -1, -1
    key_idx = content.find('"key":', c_idx)
    if key_idx < 0:
        return None, -1, -1
    # Find the value
    val_start = content.find('"', key_idx + 6) + 1
    val_end = content.find('"', val_start)
    return content[val_start:val_end], val_start, val_end

key0, s0, e0 = get_elem_c_key(init_data, 'scrolling-images_0')
key5, s5, e5 = get_elem_c_key(init_data, 'scrolling-images_5')

print(f"_0 key: {key0}")
print(f"_5 key: {key5}")

if key0 and key5:
    # Swap: put key5 in _0 position and key0 in _5 position
    # Do in reverse order to preserve positions
    if s5 > s0:
        services = services[:s5] + key0 + services[e5:]
        services = services[:s0] + key5 + services[e0:]
    else:
        services = services[:s0] + key5 + services[e0:]
        services = services[:s5] + key0 + services[e5:]
    print("Swapped JSON keys!")

# Step 2: Also swap noscript src in HTML
# Find noscript for scrolling-images_0 and _5
def get_noscript_src(content, sid):
    marker = f'data-sid="{sid}"'
    idx = content.find(marker)
    if idx < 0:
        return None, -1, -1
    ns_idx = content.find('<noscript>', idx)
    src_idx = content.find('src="', ns_idx) + 5
    src_end = content.find('"', src_idx)
    return content[src_idx:src_end], src_idx, src_end

src0, ns0, ne0 = get_noscript_src(services, 'scrolling-images_0')
src5, ns5, ne5 = get_noscript_src(services, 'scrolling-images_5')

print(f"_0 noscript src: {src0}")
print(f"_5 noscript src: {src5}")

if src0 and src5:
    if ne5 > ns0:
        services = services[:ns5] + src0 + services[ne5:]
        services = services[:ns0] + src5 + services[ne0:]
    else:
        services = services[:ns0] + src5 + services[ne0:]
        services = services[:ns5] + src0 + services[ne5:]
    print("Swapped noscript srcs!")

open('services.html', 'w', encoding='utf-8').write(services)
print("Done!")
