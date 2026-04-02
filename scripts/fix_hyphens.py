content = open('index.html', 'r', encoding='utf-8').read()

content = content.replace("I'm Jacque \u2014 documentary", "I'm Jacque, documentary")
content = content.replace("vibe-reader", "vibe reader")
content = content.replace("it really happens \u2014 and make sure", "it really happens, and make sure")

open('index.html', 'w', encoding='utf-8').write(content)
print('OK')
