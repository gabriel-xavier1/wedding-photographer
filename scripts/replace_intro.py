import re

index = open('index.html', 'r', encoding='utf-8').read()
services = open('services.html', 'r', encoding='utf-8').read()

# ── 1. Extract intro HTML from index.html ─────────────────────────────────────
intro_start_idx = index.find('<div id="intro" data-bid="intro"')
depth = 0
i = intro_start_idx
while i < len(index):
    if index[i:i+4] == '<div': depth += 1
    elif index[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            intro_end_idx = i + 6
            break
    i += 1
intro_html_new = index[intro_start_idx:intro_end_idx]
print(f"Extracted intro HTML from index ({len(intro_html_new)} chars)")

# ── 2. Extract intro JSON blockData entry from index.html ─────────────────────
script_end_idx = index.find('</script>')
idx = index.find('"slug": "intro"')
if idx < 0:
    idx = index.find('"slug":"intro"')
brace = idx
while brace > 0 and index[brace] != '{':
    brace -= 1
depth = 0
j = brace
while j < len(index):
    if index[j] == '{': depth += 1
    elif index[j] == '}':
        depth -= 1
        if depth == 0:
            json_block_end = j + 1
            break
    j += 1
intro_json_block = index[brace:json_block_end]
print(f"Extracted intro JSON block ({len(intro_json_block)} chars)")

# ── 3. Extract intro elementData entries from index.html ──────────────────────
intro_elems = []
search_from = 0
init_data_index = index[:script_end_idx]
while True:
    idx2 = init_data_index.find('"blockId": "intro"', search_from)
    if idx2 < 0:
        idx2 = init_data_index.find('"blockId":"intro"', search_from)
    if idx2 < 0:
        break
    brace2 = idx2
    while brace2 > 0 and init_data_index[brace2] != '{':
        brace2 -= 1
    depth = 0
    j2 = brace2
    while j2 < len(init_data_index):
        if init_data_index[j2] == '{': depth += 1
        elif init_data_index[j2] == '}':
            depth -= 1
            if depth == 0:
                elem_end2 = j2 + 1
                break
        j2 += 1
    intro_elems.append(init_data_index[brace2:elem_end2])
    search_from = elem_end2
print(f"Extracted {len(intro_elems)} intro element entries from index")

# ── 4. Extract intro CSS from index.html ──────────────────────────────────────
style_end_idx = index.find('</style>')
css_block_index = index[:style_end_idx]
intro_css_lines = [line for line in css_block_index.split('\n') 
                   if ('sib-intro' in line or 'sie-intro' in line) and line.strip()]
intro_css_new = '\n'.join(intro_css_lines)
print(f"Extracted {len(intro_css_lines)} CSS lines from index")

# ── 5. Replace intro HTML in services.html ────────────────────────────────────
intro_start_svc = services.find('<div id="intro" data-bid="intro"')
depth = 0
i = intro_start_svc
while i < len(services):
    if services[i:i+4] == '<div': depth += 1
    elif services[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            intro_end_svc = i + 6
            break
    i += 1
services = services[:intro_start_svc] + intro_html_new + services[intro_end_svc:]
print("Replaced intro HTML in services")

# ── 6. Replace intro JSON blockData in services.html ─────────────────────────
script_end_svc = services.find('</script>')
idx3 = services.find('"slug":"intro"')
brace3 = idx3
while brace3 > 0 and services[brace3] != '{':
    brace3 -= 1
depth = 0
j3 = brace3
while j3 < len(services):
    if services[j3] == '{': depth += 1
    elif services[j3] == '}':
        depth -= 1
        if depth == 0:
            json_block_end_svc = j3 + 1
            break
    j3 += 1
services = services[:brace3] + intro_json_block + services[json_block_end_svc:]
print("Replaced intro JSON block in services")

# ── 7. Replace intro elementData entries in services.html ─────────────────────
# Remove old intro elements
script_end_svc = services.find('</script>')
init_data_svc = services[:script_end_svc]

# Find and remove all old intro element entries
old_elems_positions = []
search_from = 0
while True:
    idx4 = init_data_svc.find('"blockId":"intro"', search_from)
    if idx4 < 0:
        break
    brace4 = idx4
    while brace4 > 0 and init_data_svc[brace4] != '{':
        brace4 -= 1
    depth = 0
    j4 = brace4
    while j4 < len(init_data_svc):
        if init_data_svc[j4] == '{': depth += 1
        elif init_data_svc[j4] == '}':
            depth -= 1
            if depth == 0:
                elem_end4 = j4 + 1
                break
        j4 += 1
    old_elems_positions.append((brace4, elem_end4))
    search_from = elem_end4

print(f"Found {len(old_elems_positions)} old intro elements to replace")

# Remove old elements (in reverse order to preserve positions)
for start, end in reversed(old_elems_positions):
    # Also remove the preceding comma if present
    prefix = services[start-1:start]
    if prefix == ',':
        services = services[:start-1] + services[end:]
    else:
        services = services[:start] + services[end:]

# Insert new elements before closing ]} of elementData
elem_insert_pos = services.rfind(']}', 0, services.find('</script>'))
services = services[:elem_insert_pos] + ',' + ','.join(intro_elems) + services[elem_insert_pos:]
print(f"Inserted {len(intro_elems)} new intro elements")

# ── 8. Replace intro CSS in services.html ─────────────────────────────────────
style_end_svc = services.find('</style>')
css_block_svc = services[:style_end_svc]

# Remove old intro CSS lines
lines = services[:style_end_svc].split('\n')
new_lines = [l for l in lines if 'sib-intro' not in l and 'sie-intro' not in l]
services = '\n'.join(new_lines) + '\n' + intro_css_new + '\n' + services[style_end_svc:]
print("Replaced intro CSS")

open('services.html', 'w', encoding='utf-8').write(services)
print("\nAll done!")
