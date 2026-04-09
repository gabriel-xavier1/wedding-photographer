import re

index = open('index.html', 'r', encoding='utf-8').read()
services = open('services.html', 'r', encoding='utf-8').read()

# ── 1. Extract scrolling-images HTML from index ───────────────────────────────
si_start = index.find('<div id="scrolling-images"')
depth = 0
i = si_start
while i < len(index):
    if index[i:i+4] == '<div': depth += 1
    elif index[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            si_end = i + 6
            break
    i += 1
si_html = index[si_start:si_end]
print(f"Extracted scrolling-images HTML ({len(si_html)} chars)")

# ── 2. Extract scrolling-images JSON blockData from index ─────────────────────
script_end = index.find('</script>')
init_data = index[:script_end]
idx = init_data.find('"slug": "scrolling-images"')
if idx < 0:
    idx = init_data.find('"slug":"scrolling-images"')
brace = idx
while brace > 0 and init_data[brace] != '{':
    brace -= 1
depth = 0
j = brace
while j < len(init_data):
    if init_data[j] == '{': depth += 1
    elif init_data[j] == '}':
        depth -= 1
        if depth == 0:
            json_end = j + 1
            break
    j += 1
si_json_block = init_data[brace:json_end]
print(f"Extracted scrolling-images JSON block ({len(si_json_block)} chars)")
print(f"  Preview: {si_json_block[:150]}")

# ── 3. Extract scrolling-images elementData from index ────────────────────────
si_elems = []
search_from = 0
while True:
    idx2 = init_data.find('"blockId": "scrolling-images"', search_from)
    if idx2 < 0:
        idx2 = init_data.find('"blockId":"scrolling-images"', search_from)
    if idx2 < 0:
        break
    brace2 = idx2
    while brace2 > 0 and init_data[brace2] != '{':
        brace2 -= 1
    depth = 0
    j2 = brace2
    while j2 < len(init_data):
        if init_data[j2] == '{': depth += 1
        elif init_data[j2] == '}':
            depth -= 1
            if depth == 0:
                elem_end2 = j2 + 1
                break
        j2 += 1
    si_elems.append(init_data[brace2:elem_end2])
    search_from = elem_end2
print(f"Extracted {len(si_elems)} scrolling-images elements")

# ── 4. Extract scrolling-images CSS from index ────────────────────────────────
style_end = index.find('</style>')
css_block = index[:style_end]
si_css_lines = [line for line in css_block.split('\n')
                if ('sib-scrolling-images' in line or 'sie-scrolling-images' in line) and line.strip()]
si_css = '\n'.join(si_css_lines)
print(f"Extracted {len(si_css_lines)} CSS lines")

# ── 5. Check if scrolling-images already in services ─────────────────────────
if 'scrolling-images' in services:
    print("WARNING: scrolling-images already exists in services.html - skipping")
else:
    # ── 6. Insert JSON blockData after intro block entry ──────────────────────
    svc_script_end = services.find('</script>')
    svc_init = services[:svc_script_end]
    
    # Find intro block entry end in services
    idx3 = svc_init.find('"slug":"intro"')
    if idx3 < 0:
        idx3 = svc_init.find('"slug": "intro"')
    brace3 = idx3
    while brace3 > 0 and svc_init[brace3] != '{':
        brace3 -= 1
    depth = 0
    j3 = brace3
    while j3 < len(svc_init):
        if svc_init[j3] == '{': depth += 1
        elif svc_init[j3] == '}':
            depth -= 1
            if depth == 0:
                intro_json_end = j3 + 1
                break
        j3 += 1
    # Insert after intro block entry
    services = services[:intro_json_end] + ',' + si_json_block + services[intro_json_end:]
    print("Inserted scrolling-images JSON block")

    # ── 7. Insert elementData entries ─────────────────────────────────────────
    elem_insert_pos = services.rfind(']}', 0, services.find('</script>'))
    services = services[:elem_insert_pos] + ',' + ','.join(si_elems) + services[elem_insert_pos:]
    print(f"Inserted {len(si_elems)} element entries")

    # ── 8. Add CSS ────────────────────────────────────────────────────────────
    style_close = services.find('</style>')
    services = services[:style_close] + si_css + '\n' + services[style_close:]
    print("Added CSS")

    # ── 9. Insert HTML after intro block ──────────────────────────────────────
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
    services = services[:intro_end_svc] + '\n' + si_html + services[intro_end_svc:]
    print("Inserted scrolling-images HTML after intro")

open('services.html', 'w', encoding='utf-8').write(services)
print("\nAll done!")
