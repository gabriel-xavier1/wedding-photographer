import re

index = open('index.html', 'r', encoding='utf-8').read()
services = open('services.html', 'r', encoding='utf-8').read()

NEW_SLUG = 'intro-2'

# ── 1. Extract intro HTML from index.html exactly ────────────────────────────
intro_start = index.find('<div id="intro" data-bid="intro"')
depth = 0
i = intro_start
while i < len(index):
    if index[i:i+4] == '<div': depth += 1
    elif index[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            intro_end = i + 6
            break
    i += 1
intro_html = index[intro_start:intro_end]

# ── 2. Rename all ids/bids/sids/trans to use intro-2 ─────────────────────────
intro_html = intro_html.replace('id="intro"', f'id="{NEW_SLUG}"')
intro_html = intro_html.replace('data-bid="intro"', f'data-bid="{NEW_SLUG}"')
intro_html = re.sub(r'data-sid="intro_', f'data-sid="{NEW_SLUG}_', intro_html)
intro_html = re.sub(r'data-tran="intro_', f'data-tran="{NEW_SLUG}_', intro_html)
# Keep sie-intro_ CSS classes — they already exist in services.html

# ── 3. Extract the intro JSON entry from services.html init_data ──────────────
# Find "slug":"intro" in services init_data
script_end = services.find('</script>')
init_data = services[:script_end]

idx = init_data.find('"slug":"intro"')
# Walk back to find the opening { of this block entry
brace = idx
while brace > 0 and init_data[brace] != '{':
    brace -= 1

# Walk forward to find the closing }
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

intro_json = init_data[brace:json_end]

# ── 4. Create intro-2 JSON by string replacement ─────────────────────────────
intro2_json = intro_json.replace('"slug":"intro"', f'"slug":"{NEW_SLUG}"')
# Also rename element ids in JSON
intro2_json = re.sub(r'"id":"intro_(\w+)"', rf'"id":"{NEW_SLUG}_\1"', intro2_json)
intro2_json = re.sub(r'"blockId":"intro"', f'"blockId":"{NEW_SLUG}"', intro2_json)

# ── 5. Add CSS for intro-2 (copy intro CSS rules) ────────────────────────────
# Extract all CSS rules for sib-intro and sie-intro from services.html
style_end = services.find('</style>')
css_block = services[:style_end]

intro_css_rules = re.findall(r'[^\n]*(?:sib-intro|sie-intro_)[^\n]*\{[^}]+\}', css_block)
# Create intro-2 versions
intro2_css = ''
for rule in intro_css_rules:
    new_rule = rule.replace('sib-intro', f'sib-{NEW_SLUG}').replace('sie-intro_', f'sie-{NEW_SLUG}_')
    intro2_css += new_rule + '\n'

# ── 6. Insert JSON into init_data (before closing ]} of blockData array) ──────
# Find the end of blockData array — last }] before elementData
blockdata_end = services.find(',"elementData"')
services = services[:blockdata_end] + ',' + intro2_json + services[blockdata_end:]
print("Inserted intro-2 JSON block entry")

# ── 7. Insert elementData entries for intro-2 ────────────────────────────────
# Find intro element entries in services init_data and duplicate for intro-2
# Find all "blockId":"intro" element entries
elem_pattern = re.compile(r'\{[^{}]*"blockId":"intro"[^{}]*\}')
intro_elems = elem_pattern.findall(services[:services.find('</script>')])
intro2_elems = []
for elem in intro_elems:
    new_elem = re.sub(r'"id":"intro_(\w+)"', rf'"id":"{NEW_SLUG}_\1"', elem)
    new_elem = new_elem.replace('"blockId":"intro"', f'"blockId":"{NEW_SLUG}"')
    intro2_elems.append(new_elem)

if intro2_elems:
    # Insert before closing ]} of elementData
    elem_insert_pos = services.rfind(']}', 0, services.find('</script>'))
    services = services[:elem_insert_pos] + ',' + ','.join(intro2_elems) + services[elem_insert_pos:]
    print(f"Inserted {len(intro2_elems)} element entries for intro-2")

# ── 8. Add CSS before </style> ───────────────────────────────────────────────
style_close = services.find('</style>')
services = services[:style_close] + intro2_css + '\n' + services[style_close:]
print("Added CSS for intro-2")

# ── 9. Insert HTML after collage ─────────────────────────────────────────────
collage_start = services.find('<div id="collage-intro"')
depth = 0
i = collage_start
while i < len(services):
    if services[i:i+4] == '<div': depth += 1
    elif services[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            collage_end = i + 6
            break
    i += 1

services = services[:collage_end] + '\n' + intro_html + services[collage_end:]
print("Inserted intro-2 HTML after collage")

open('services.html', 'w', encoding='utf-8').write(services)
print("Done!")
