content = open('services.html', 'r', encoding='utf-8').read()

line_svg = (
    '<div data-sid="faq_14" class="sie-faq_14 se">'
    '<svg class="se-line"><line '
    'data-d-strokelinecap="butt" data-d-linestyle="solid" data-d-thickness="1" '
    'data-d-rotatedwidth="665" data-d-rotatedheight="0" data-d-widthoffset="0" '
    'data-d-heightoffset="0" data-d-isround="false" data-d-rotation="0" '
    'data-d-roundedsolid="false" data-d-dotted="false" data-d-length="665" '
    'data-d-mirrorline="false" data-d-dashwidth="21" data-d-spacing="15" '
    'data-d-dasharrayvalue="none" '
    'data-m-strokelinecap="butt" data-m-linestyle="solid" data-m-thickness="1" '
    'data-m-rotatedwidth="286" data-m-rotatedheight="0" data-m-widthoffset="0" '
    'data-m-heightoffset="0" data-m-isround="false" data-m-rotation="0" '
    'data-m-roundedsolid="false" data-m-dotted="false" data-m-length="286" '
    'data-m-mirrorline="false" data-m-dashwidth="21" data-m-spacing="15" '
    'data-m-dasharrayvalue="none" '
    'x1="0" y1="0" x2="100%" y2="100%" /></svg></div>'
)

q5_block = (
    line_svg
    + '<div class="str-im str-id" data-tran="faq_15">'
    + '<div data-sid="faq_15" class="sie-faq_15 se">'
    + '<h3 class="se-t sie-faq_12-text st-m-subheading st-d-subheading se-rc">'
    + '<b>How soon will we receive our photos?<br></b><br></h3>'
    + '</div></div>'
    + '<div class="str-im str-id" data-tran="faq_16">'
    + '<div data-sid="faq_16" class="sie-faq_16 se">'
    + '<p class="se-t sie-faq_13-text st-m-paragraph st-d-paragraph se-rc">'
    + 'During busy periods it can take up to 4 weeks to receive your full online gallery.<br>'
    + '</p></div></div>'
)

# Find the garbage section and replace it
old_marker = 'how the day will be.<br></p></div></div></div></div></div><div id="cta-contact"'
new_marker = 'how the day will be.<br></p></div></div>' + q5_block + '</div></div></div><div id="cta-contact"'

if old_marker in content:
    # Find position and extract what's between the two cta-contact divs to remove garbage
    idx = content.find(old_marker)
    # Find the real cta-contact div
    real_cta = content.find('<div id="cta-contact" data-bid="cta-contact"', idx)
    garbage_end = real_cta
    content = content[:idx] + new_marker.replace('<div id="cta-contact"', '') + content[garbage_end:]
    print("Fixed!")
else:
    print("Pattern not found, searching...")
    idx = content.find('how the day will be')
    print(repr(content[idx:idx+400]))

open('services.html', 'w', encoding='utf-8').write(content)
