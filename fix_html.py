import json

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# find first string starting with <!DOCTYPE html> to slice off any corrupted lines at the top
for i, line in enumerate(lines):
    if line.strip().startswith('<!DOCTYPE html>'):
        lines = lines[i:]
        break

# find the init_data JSON line
for i, line in enumerate(lines):
    if line.strip().startswith('{"mobile":{'):
        data = json.loads(line)
        for block in data['blockData']:
            if block['slug'] == 'hero':
                # Apply the image in the 'd' and 'm' dictionaries explicitly
                block['d']['bgMediaType'] = 'image'
                block['d']['bgImage'] = {
                    "key": "https://i.postimg.cc/zDCSSh8V/TS-13166-(1).jpg",
                    "aspect_ratio": 1.5,
                    "title": "TS-13166",
                    "type": "asset"
                }
                block['d']['bgOpacity'] = '90'
                block['d']['bgPos'] = 'cb'
                block['d']['bgScroll'] = 'p' # Added parallax scrolling for nice effect
                
                block['m']['bgMediaType'] = 'image'
                block['m']['bgImage'] = {
                    "key": "https://i.postimg.cc/zDCSSh8V/TS-13166-(1).jpg",
                    "aspect_ratio": 1.5,
                    "title": "TS-13166",
                    "type": "asset"
                }
                block['m']['bgOpacity'] = '60'
                block['m']['bgPos'] = 'cb'
                block['m']['bgScroll'] = 'p'
        lines[i] = "      " + json.dumps(data) + "\n"
        break

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print("File fixed!")
