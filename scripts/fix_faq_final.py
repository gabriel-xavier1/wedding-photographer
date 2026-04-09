content = open('services.html', 'r', encoding='utf-8').read()

# 1. Add desktop .sc height rule (missing!)
content = content.replace(
    '.m .sib-faq.sb-nm-wH .sc {height:1000px;}',
    '.m .sib-faq.sb-nm-wH .sc {height:1000px;}.d .sib-faq.sb-nm-wH .sc {height:826px;}'
)

# 2. Fix mobile faq_0 (left image/title column) height to match container
content = content.replace(
    '.m .sie-faq_0 {left:0px;top:0px;width:320px;height:220px;}',
    '.m .sie-faq_0 {left:0px;top:0px;width:320px;height:1000px;}'
)

# 3. Fix desktop faq_0 height to match container
content = content.replace(
    '.d .sie-faq_0 {left:0px;top:0px;width:460px;height:826px;}',
    '.d .sie-faq_0 {left:0px;top:0px;width:460px;height:826px;}'
)

# 4. On mobile, faq_1 (FAQ title text) and faq_2 (subtitle) are in the left column
# They need to stay at top. The questions (faq_3+) are full width on mobile (left:17px, width:286px)
# The issue on mobile is faq_12 appears on left side - check if it's because
# mobile faq_0 clips content. Actually on mobile all questions are left:17 which is fine.

# 5. The real issue: on desktop, faq_12 shows on LEFT side in screenshot
# This means the .sc container is not tall enough and elements overflow weirdly
# Let's also ensure the JSON init_data height matches
import re

# Update the JSON block height for faq section - desktop h and mobile h
# Find: "slug":"faq"...  "d":{"h":670  -> change to 826
# and "m":{"h":801 -> change to 1000
def replace_faq_json_height(content, old_d_h, new_d_h, old_m_h, new_m_h):
    # Find the faq slug section in JSON
    idx = content.find('"slug":"faq"')
    if idx < 0:
        print("faq slug not found")
        return content
    # Find the d height near this position
    chunk = content[idx:idx+500]
    print("JSON chunk:", repr(chunk[:300]))
    return content

content = replace_faq_json_height(content, 670, 826, 801, 1000)

open('services.html', 'w', encoding='utf-8').write(content)
print("Done!")
