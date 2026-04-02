content = open('index.html', 'r', encoding='utf-8').read()
import re

# About: foto about_3 e texto about_1
about_img = re.search(r'"id": "about_3".*?"d": \{"x": (\d+).*?"w": (\d+)', content)
about_txt = re.search(r'"id": "about_1".*?"d": \{"x": (\d+)', content)

if about_img and about_txt:
    img_right = int(about_img.group(1)) + int(about_img.group(2))
    txt_left = int(about_txt.group(1))
    print(f'About - foto termina em x:{img_right}, texto começa em x:{txt_left}, gap:{txt_left - img_right}px')

# Freebie: foto freebie_0 e texto freebie_2
free_img = re.search(r'"id": "freebie_0".*?"d": \{"x": (\d+).*?"w": (\d+)', content)
free_txt = re.search(r'"id": "freebie_2".*?"d": \{"x": (\d+)', content)

if free_img and free_txt:
    img_right = int(free_img.group(1)) + int(free_img.group(2))
    txt_left = int(free_txt.group(1))
    print(f'Freebie - foto termina em x:{img_right}, texto começa em x:{txt_left}, gap:{txt_left - img_right}px')
