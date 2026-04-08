content = open('index.html', 'r', encoding='utf-8').read()

old = '<video controls style="width:100%;height:100%;object-fit:cover;border-radius:6px;" poster=""><source src="" type="video/mp4"/></video>'

new = '<iframe width="100%" height="100%" src="https://www.youtube.com/embed/Qxn61VjTaZ4?si=TCKzufLCysVfLOVy" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="border-radius:6px;display:block;"></iframe>'

if old in content:
    content = content.replace(old, new)
    print('OK')
else:
    print('NOT FOUND')

open('index.html', 'w', encoding='utf-8').write(content)
