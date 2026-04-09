services = open('services.html', 'r', encoding='utf-8').read()

def extract_block(content, block_id):
    """Extract a full HTML block by id"""
    marker = f'<div id="{block_id}"'
    start = content.find(marker)
    if start < 0:
        # try data-bid version
        marker = f'id="{block_id}" data-bid'
        start = content.find(marker)
        if start < 0:
            print(f"  Block {block_id} not found!")
            return None, content
        # walk back to <div
        while start > 0 and content[start:start+4] != '<div':
            start -= 1
    depth = 0
    i = start
    while i < len(content):
        if content[i:i+4] == '<div': depth += 1
        elif content[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                end = i + 6
                break
        i += 1
    return content[start:end], content[:start] + content[end:]

# Extract blocks in current order, removing them from content
print("Extracting blocks...")
collage_html, services = extract_block(services, 'collage-intro')
print(f"  collage-intro: {len(collage_html) if collage_html else 0} chars")

intro_html, services = extract_block(services, 'intro')
print(f"  intro: {len(intro_html) if intro_html else 0} chars")

si_html, services = extract_block(services, 'scrolling-images')
print(f"  scrolling-images: {len(si_html) if si_html else 0} chars")

# Find insertion point: after hero, before navigation-services
hero_marker = '<div id="hero"'
hero_start = services.find(hero_marker)
depth = 0
i = hero_start
while i < len(services):
    if services[i:i+4] == '<div': depth += 1
    elif services[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            hero_end = i + 6
            break
    i += 1

# Insert in correct order: collage → intro → scrolling-images
insert = '\n' + collage_html + '\n' + intro_html + '\n' + si_html + '\n'
services = services[:hero_end] + insert + services[hero_end:]
print("Reordered: hero → collage → intro → scrolling-images → navigation-services")

# Now fix JSON blockData order too
# Find the blockData array and reorder intro + scrolling-images entries
# The JSON order determines Showit's render order
script_end = services.find('</script>')
init_data = services[:script_end]

def extract_json_block(content, slug):
    """Extract a JSON block entry by slug"""
    idx = content.find(f'"slug": "{slug}"')
    if idx < 0:
        idx = content.find(f'"slug":"{slug}"')
    if idx < 0:
        print(f"  JSON block {slug} not found!")
        return None, content
    brace = idx
    while brace > 0 and content[brace] != '{':
        brace -= 1
    # check for preceding comma
    pre_comma = brace - 1
    has_comma = content[pre_comma] == ','
    depth = 0
    j = brace
    while j < len(content):
        if content[j] == '{': depth += 1
        elif content[j] == '}':
            depth -= 1
            if depth == 0:
                end = j + 1
                break
        j += 1
    if has_comma:
        block = content[brace:end]
        new_content = content[:pre_comma] + content[end:]
    else:
        block = content[brace:end]
        new_content = content[:brace] + content[end:]
    return block, new_content

# Extract JSON blocks
print("\nReordering JSON blockData...")
intro_json, services = extract_json_block(services, 'intro')
si_json, services = extract_json_block(services, 'scrolling-images')
print(f"  intro JSON: {len(intro_json) if intro_json else 0} chars")
print(f"  scrolling-images JSON: {len(si_json) if si_json else 0} chars")

# Find hero JSON block end and insert after it
hero_json_idx = services.find('"slug": "hero"')
if hero_json_idx < 0:
    hero_json_idx = services.find('"slug":"hero"')
brace_h = hero_json_idx
while brace_h > 0 and services[brace_h] != '{':
    brace_h -= 1
depth = 0
j = brace_h
while j < len(services):
    if services[j] == '{': depth += 1
    elif services[j] == '}':
        depth -= 1
        if depth == 0:
            hero_json_end = j + 1
            break
    j += 1

# Insert: hero → intro → scrolling-images → navigation-services...
services = services[:hero_json_end] + ',' + intro_json + ',' + si_json + services[hero_json_end:]
print("JSON reordered: hero → intro → scrolling-images → navigation-services")

open('services.html', 'w', encoding='utf-8').write(services)
print("\nDone!")
