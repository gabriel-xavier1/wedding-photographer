content = open('services.html', 'r', encoding='utf-8').read()

# Desktop: container=820, faq_1 h=126 -> center top = (820-126)/2 = 347
# Also move faq_2 (subtitle) proportionally: currently at 375 (143px below faq_1 top 232)
# New faq_2 top = 347 + 126 + 10 = 483... but faq_2 is a subtitle, keep relative gap
# faq_1 was at 232, faq_2 at 375 -> gap = 143px
# New faq_1 top = 347, faq_2 top = 347 + 143 = 490

content = content.replace(
    '.d .sie-faq_1 {left:65px;top:232px;width:340px;height:126px;}',
    '.d .sie-faq_1 {left:65px;top:347px;width:340px;height:126px;}'
)
content = content.replace(
    '.d .sie-faq_2 {left:65px;top:375px;width:253px;height:36px;}',
    '.d .sie-faq_2 {left:65px;top:490px;width:253px;height:36px;}'
)

# Mobile: container=980, faq_1 h=69 -> center top = (980-69)/2 = 455
# faq_1 was at 39, faq_2 at 121 -> gap = 82px
# New faq_2 top = 455 + 82 = 537
content = content.replace(
    '.m .sie-faq_1 {left:25px;top:39px;width:270px;height:69px;}',
    '.m .sie-faq_1 {left:25px;top:455px;width:270px;height:69px;}'
)
content = content.replace(
    '.m .sie-faq_2 {left:25px;top:121px;width:266px;height:34px;}',
    '.m .sie-faq_2 {left:25px;top:537px;width:266px;height:34px;}'
)

# Update JSON positions too
import re

def update_json_pos(content, elem_id, new_m_y, new_d_y):
    # Find the JSON entry for this element and update y positions
    pattern = f'"id":"{elem_id}","blockId":"faq"'
    idx = content.find(pattern)
    if idx < 0:
        print(f"  {elem_id} not found in JSON")
        return content
    # Find the m y value
    chunk_start = content.rfind('{', 0, idx)
    chunk_end = content.find('}', idx) + 1
    chunk = content[chunk_start:chunk_end]
    # Update m.y
    new_chunk = re.sub(r'("m":\{"x":\d+,"y":)\d+', f'\\g<1>{new_m_y}', chunk)
    # Update d.y  
    new_chunk = re.sub(r'("d":\{"x":\d+,"y":)\d+', f'\\g<1>{new_d_y}', new_chunk)
    content = content[:chunk_start] + new_chunk + content[chunk_end:]
    print(f"  Updated {elem_id}: m.y={new_m_y}, d.y={new_d_y}")
    return content

content = update_json_pos(content, 'faq_1', 455, 347)
content = update_json_pos(content, 'faq_2', 537, 490)

open('services.html', 'w', encoding='utf-8').write(content)
print("Done!")
