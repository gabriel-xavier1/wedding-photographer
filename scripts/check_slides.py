content = open('index.html', 'r', encoding='utf-8').read()

for slide in ['view-1_0', 'view-1_1', 'view-1-1_0', 'view-1-1_1']:
    idx = content.find(f'sie-testimonials_{slide} se')
    print(f'--- {slide} ---')
    print(repr(content[idx:idx+200]))
    print()
