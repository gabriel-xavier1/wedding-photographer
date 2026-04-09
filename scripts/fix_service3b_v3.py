import json
import re

with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the init_data JSON
match = re.search(r'<script id="init_data" type="application/json">\s*(.*?)\s*</script>', content, re.DOTALL)
if not match:
    print("ERROR: init_data not found")
    exit(1)

json_str = match.group(1)
data = json.loads(json_str)

# Check if service-3b already in blockData
slugs = [b['slug'] for b in data['blockData']]
print("Current slugs:", slugs)

# Add service-3b to blockData if not present
if 'service-3b' not in slugs:
    # Find service-1 block data
    s1 = next(b for b in data['blockData'] if b['slug'] == 'service-1')
    s3b = json.loads(json.dumps(s1))  # deep copy
    s3b['slug'] = 'service-3b'
    # Insert after service-2
    s2_idx = next(i for i, b in enumerate(data['blockData']) if b['slug'] == 'service-2')
    data['blockData'].insert(s2_idx + 1, s3b)
    print("Added service-3b to blockData")

# Clone elementData from service-1 to service-3b
s1_elements = [e for e in data['elementData'] if e.get('blockId') == 'service-1']
s3b_elements_existing = [e for e in data['elementData'] if e.get('blockId') == 'service-3b']

if not s3b_elements_existing:
    new_elements = []
    for e in s1_elements:
        ne = json.loads(json.dumps(e))
        ne['blockId'] = 'service-3b'
        ne['id'] = ne['id'].replace('service-1', 'service-3b')
        new_elements.append(ne)
    
    # Insert after last service-1 element
    last_s1_idx = max(i for i, e in enumerate(data['elementData']) if e.get('blockId') == 'service-1')
    for i, ne in enumerate(new_elements):
        data['elementData'].insert(last_s1_idx + 1 + i, ne)
    print(f"Added {len(new_elements)} elements for service-3b")

new_json = json.dumps(data, separators=(',', ':'))
new_script = f'<script id="init_data" type="application/json">\n      {new_json}\n    </script>'
old_script = match.group(0)
content = content.replace(old_script, new_script)

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('done')
