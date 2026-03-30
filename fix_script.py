import json

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.strip().startswith('{"mobile":{'):
        data = json.loads(line)
        for block in data['blockData']:
            if block['slug'] == 'hero':
                block['d']['bgMediaType'] = 'none'
                if 'bgImage' in block['d']: del block['d']['bgImage']
                block['m']['bgMediaType'] = 'none'
                if 'bgImage' in block['m']: del block['m']['bgImage']
                
                for state in block.get('states', []):
                    # Also make sure to scrub states of bgImage so we don't 404
                    if 'd' in state:
                        state['d']['bgMediaType'] = 'none'
                        if 'bgImage' in state['d']: del state['d']['bgImage']
                    if 'm' in state:
                        state['m']['bgMediaType'] = 'none'
                        if 'bgImage' in state['m']: del state['m']['bgImage']
                    
        lines[i] = "      " + json.dumps(data) + "\n"
        break

for i, line in enumerate(lines):
    if '.m .sib-hero .ss-bg {' in line:
        lines[i] = ".m .sib-hero .ss-bg {background-color:rgba(41,38,36,1); background-image:url('https://i.postimg.cc/zDCSSh8V/TS-13166-(1).jpg') !important; background-size: cover !important; background-position: center !important; background-attachment: fixed !important;}\n"
    elif '.d .sib-hero .ss-bg {' in line:
        lines[i] = ".d .sib-hero .ss-bg {background-color:rgba(41,38,36,1); background-image:url('https://i.postimg.cc/zDCSSh8V/TS-13166-(1).jpg') !important; background-size: cover !important; background-position: center !important; background-attachment: fixed !important;}\n"

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print("Parallax fix applied successfully")
