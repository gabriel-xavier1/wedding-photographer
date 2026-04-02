import json
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'<script id="init_data" type="application/json">([\s\S]*?)</script>', text)
if match:
    data = json.loads(match.group(1))
    
    about_data = None
    if isinstance(data['blockData'], list):
        for block in data['blockData']:
            if block.get('bid') == 'about':
                about_data = block
                break
    else:
        # If it's a dict
        for key, block in data['blockData'].items():
            if block.get('bid') == 'about':
                about_data = block
                break
        
    if about_data:
        for item in about_data['items']:
            sid = item.get('sid')
            item_type = item.get('type')
            item_d = item.get('d', {})
            print(f"ID: {sid}, Type: {item_type}, Desktop: x={item_d.get('x')}, w={item_d.get('w')}, y={item_d.get('y')}")
