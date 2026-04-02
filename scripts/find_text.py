import json
import re

def find_text_in_json(obj, target, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            find_text_in_json(v, target, path + "['" + str(k) + "']")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            find_text_in_json(v, target, path + "[" + str(i) + "]")
    elif isinstance(obj, str):
        if target in obj:
            print(f"Found '{target}' at {path}")

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

match = re.search(r'<script id="init_data" type="application/json">([\s\S]*?)</script>', text)
if match:
    data = json.loads(match.group(1))
    find_text_in_json(data, "MEET YOUR PHOTOGRAPHER")
    find_text_in_json(data, "Willow")
