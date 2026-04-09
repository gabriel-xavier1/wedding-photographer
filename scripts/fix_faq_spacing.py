content = open('services.html', 'r', encoding='utf-8').read()

# Current: 860px desktop, bottom padding ~2x top padding
# faq_3 top = 74px (top padding)
# faq_16 bottom = 786px
# Target: container = 786 + 74 = 860... but visually still too much
# The screenshot shows ~40px top, ~80px bottom -> need to cut ~40px
# New target: 860 - 40 = 820px

content = content.replace('.d .sib-faq {height:860px;}', '.d .sib-faq {height:820px;}')
content = content.replace('.d .sib-faq.sb-nm-wH .sc {height:860px;}', '.d .sib-faq.sb-nm-wH .sc {height:820px;}')
content = content.replace('.d .sie-faq_0 {left:0px;top:0px;width:460px;height:860px;}',
                           '.d .sie-faq_0 {left:0px;top:0px;width:460px;height:820px;}')
content = content.replace(
    '"slug":"faq","visible":"a","states":[],"d":{"h":860,',
    '"slug":"faq","visible":"a","states":[],"d":{"h":820,'
)

# Mobile: also reduce proportionally
# faq_16 mobile bottom = 910+60 = 970px
# faq_3 mobile top = 214px -> too much, use ~40px equivalent
# Current 1000px, reduce to 970 + 40 = 1010... already 1000
# Keep mobile at 1000 but reduce to 980
content = content.replace('.m .sib-faq {height:1000px;}', '.m .sib-faq {height:980px;}')
content = content.replace('.m .sib-faq.sb-nm-wH .sc {height:1000px;}', '.m .sib-faq.sb-nm-wH .sc {height:980px;}')
content = content.replace('.m .sie-faq_0 {left:0px;top:0px;width:320px;height:1000px;}',
                           '.m .sie-faq_0 {left:0px;top:0px;width:320px;height:980px;}')
content = content.replace(
    '"bgMediaType":"none"},"m":{"h":1000,"w":320,"nature":"wH"',
    '"bgMediaType":"none"},"m":{"h":980,"w":320,"nature":"wH"'
)

open('services.html', 'w', encoding='utf-8').write(content)
print("Done!")
