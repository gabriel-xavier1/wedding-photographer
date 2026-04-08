content = open('index.html', 'r', encoding='utf-8').read()

old = '<div data-sid="weddings_video" class="sie-weddings_video se"><video controls style="width:100%;height:100%;object-fit:cover;border-radius:6px;" poster=""><source src="" type="video/mp4"/></video></div>'

new = '''<div data-sid="weddings_video" class="sie-weddings_video se video-reveal"><video controls style="width:100%;height:100%;object-fit:cover;border-radius:6px;" poster=""><source src="" type="video/mp4"/></video></div><style>.video-reveal{opacity:0;transform:translateY(40px);transition:opacity 0.9s ease,transform 0.9s ease;}.video-reveal.visible{opacity:1;transform:translateY(0);}</style><script>(function(){var el=document.querySelector('.video-reveal');if(!el)return;var obs=new IntersectionObserver(function(entries){entries.forEach(function(e){if(e.isIntersecting){el.classList.add('visible');obs.disconnect();}});},{threshold:0.15});obs.observe(el);})();</script>'''

if old in content:
    content = content.replace(old, new)
    print('OK')
else:
    print('NOT FOUND')

open('index.html', 'w', encoding='utf-8').write(content)
