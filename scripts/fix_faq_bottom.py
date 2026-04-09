content = open('services.html', 'r', encoding='utf-8').read()

# faq_16 bottom = 726+60 = 786px
# faq_3 (Q1 title) starts at top:74 -> same padding at bottom = 74px
# New desktop height = 786 + 74 = 860px

# faq_16 mobile bottom = 910+60 = 970px
# faq_3 mobile top:214 -> same padding at bottom = 214px... too much
# Use faq_3 mobile top:214 but that's the title start, not padding
# Actually look at faq_5 (divider after Q1): top:356, faq_4 bottom = 253+73=326, gap=30px
# So bottom padding should be ~30px: 970+30 = 1000px mobile

# Desktop: 900 -> 860
content = content.replace('.d .sib-faq {height:900px;}', '.d .sib-faq {height:860px;}')
content = content.replace('.d .sib-faq.sb-nm-wH .sc {height:900px;}', '.d .sib-faq.sb-nm-wH .sc {height:860px;}')
content = content.replace('.d .sie-faq_0 {left:0px;top:0px;width:460px;height:900px;}',
                           '.d .sie-faq_0 {left:0px;top:0px;width:460px;height:860px;}')
# Update JSON desktop height
content = content.replace(
    '"slug":"faq","visible":"a","states":[],"d":{"h":900,',
    '"slug":"faq","visible":"a","states":[],"d":{"h":860,'
)

# Mobile: 1100 -> 1000
content = content.replace('.m .sib-faq {height:1100px;}', '.m .sib-faq {height:1000px;}')
content = content.replace('.m .sib-faq.sb-nm-wH .sc {height:1100px;}', '.m .sib-faq.sb-nm-wH .sc {height:1000px;}')
content = content.replace('.m .sie-faq_0 {left:0px;top:0px;width:320px;height:1100px;}',
                           '.m .sie-faq_0 {left:0px;top:0px;width:320px;height:1000px;}')
content = content.replace(
    '"bgMediaType":"none"},"m":{"h":1100,"w":320,"nature":"wH"',
    '"bgMediaType":"none"},"m":{"h":1000,"w":320,"nature":"wH"'
)

open('services.html', 'w', encoding='utf-8').write(content)
print("Done!")
