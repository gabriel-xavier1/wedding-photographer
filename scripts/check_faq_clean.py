content = open('services.html', 'r', encoding='utf-8').read()
start = content.find('<div id="faq"')
end = content.find('<div id="cta-contact"', start)
chunk = content[start:end]

import re
sids = re.findall(r'data-sid="(faq_[^"]+)"', chunk)
print('FAQ elements found:', sids)

if 'wilderness' in chunk:
    print('WARNING: wilderness garbage still present')
elif 'dreaming' in chunk:
    print('WARNING: dreaming garbage still present')
else:
    print('Clean - no garbage!')

print('Total FAQ block size:', len(chunk), 'chars')
