import re

services = open('services.html', 'r', encoding='utf-8').read()

NEW_SLUG = 'intro-2'

script_end = services.find('</script>')
init_data = services[:script_end]

# Find all element entries with blockId intro using a broader pattern
# Elements look like: {"type":"...","visible":"...","id":"intro_X","blockId":"intro",...}
# Find by looking for "blockId":"intro" and extracting the surrounding object

intro_elems = []
search_from = 0
while True:
    idx = init_data.find('"blockId":"intro"', search_from)
    if idx < 0:
        break
    # Walk back to find opening {
    brace = idx
    while brace > 0 and init_data[brace] != '{':
        brace -= 1
    # Walk forward to find closing }
    depth = 0
    j = brace
    while j < len(init_data):
        if init_data[j] == '{': depth += 1
        elif init_data[j] == '}':
            depth -= 1
            if depth == 0:
                elem_end = j + 1
                break
        j += 1
    elem = init_data[brace:elem_end]
    intro_elems.append(elem)
    search_from = elem_end

print(f"Found {len(intro_elems)} intro elements")

# Create intro-2 versions
intro2_elems = []
for elem in intro_elems:
    new_elem = re.sub(r'"id":"intro_(\w+)"', rf'"id":"{NEW_SLUG}_\1"', elem)
    new_elem = new_elem.replace('"blockId":"intro"', f'"blockId":"{NEW_SLUG}"')
    intro2_elems.append(new_elem)

# Check if already inserted
if f'"blockId":"{NEW_SLUG}"' in init_data:
    print("intro-2 elements already exist, skipping")
else:
    # Insert before closing ]} of elementData
    elem_insert_pos = services.rfind(']}', 0, services.find('</script>'))
    services = services[:elem_insert_pos] + ',' + ','.join(intro2_elems) + services[elem_insert_pos:]
    print(f"Inserted {len(intro2_elems)} element entries")

open('services.html', 'w', encoding='utf-8').write(services)
print("Done!")
