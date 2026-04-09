import re

index = open('index.html', 'r', encoding='utf-8').read()
services = open('services.html', 'r', encoding='utf-8').read()

script_end = index.find('</script>')
init_data = index[:script_end]

# Find all intro elements
print("=== INDEX intro elements ===")
search_from = 0
while True:
    idx = init_data.find('"blockId": "intro"', search_from)
    if idx < 0:
        break
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
                elem_end = j + 1
                break
        j += 1
    elem = init_data[brace:elem_end]
    print(f"\n  {elem[:300]}")
    search_from = elem_end

# Also check intro block JSON
print("\n=== INDEX intro blockData ===")
idx2 = init_data.find('"slug": "intro"')
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
            block_end = j2 + 1
            break
    j2 += 1
print(init_data[brace2:block_end])

# Check services intro elements
print("\n=== SERVICES intro elements ===")
svc_script_end = services.find('</script>')
svc_init = services[:svc_script_end]
search_from = 0
while True:
    idx3 = svc_init.find('"blockId":"intro"', search_from)
    if idx3 < 0:
        idx3 = svc_init.find('"blockId": "intro"', search_from)
    if idx3 < 0:
        break
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
                elem_end3 = j3 + 1
                break
        j3 += 1
    elem3 = svc_init[brace3:elem_end3]
    print(f"\n  {elem3[:300]}")
    search_from = elem_end3
