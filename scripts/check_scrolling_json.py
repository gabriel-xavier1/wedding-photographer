services = open('services.html', 'r', encoding='utf-8').read()

script_end = services.find('</script>')
init_data = services[:script_end]

# Find scrolling-images_0 element
for i in range(6):
    sid = f'"id": "scrolling-images_{i}"'
    idx = init_data.find(sid)
    if idx < 0:
        sid = f'"id":"scrolling-images_{i}"'
        idx = init_data.find(sid)
    if idx < 0:
        print(f"scrolling-images_{i} not found")
        continue
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
                end = j + 1
                break
        j += 1
    elem = init_data[brace:end]
    print(f"\nscrolling-images_{i}:")
    print(elem[:400])
