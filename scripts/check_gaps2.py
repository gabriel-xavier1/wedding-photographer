content = open('index.html', 'r', encoding='utf-8').read()
import re

# About: texto about_1 termina em x+w, foto about_3 começa em x
about_txt = re.search(r'"id": "about_1".*?"d": \{"x": (\d+).*?"w": (\d+)', content)
about_img = re.search(r'"id": "about_3".*?"d": \{"x": (\d+)', content)

if about_txt and about_img:
    txt_right = int(about_txt.group(1)) + int(about_txt.group(2))
    img_left = int(about_img.group(1))
    print(f'About - texto termina em x:{txt_right}, foto começa em x:{img_left}, gap:{img_left - txt_right}px')

# Freebie: foto freebie_0 termina, texto freebie_2 começa
free_img = re.search(r'"id": "freebie_0".*?"d": \{"x": (\d+).*?"w": (\d+)', content)
free_txt = re.search(r'"id": "freebie_2".*?"d": \{"x": (\d+)', content)

if free_img and free_txt:
    img_right = int(free_img.group(1)) + int(free_img.group(2))
    txt_left = int(free_txt.group(1))
    print(f'Freebie - foto termina em x:{img_right}, texto começa em x:{txt_left}, gap:{txt_left - img_right}px')
