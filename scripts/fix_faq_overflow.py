content = open('services.html', 'r', encoding='utf-8').read()

# The real issue: Showit's .sc has overflow:hidden by default
# faq_15 and faq_16 are being clipped. 
# Solution: add overflow:visible to the faq block's sc, and increase heights significantly

# 1. Add overflow visible rule for faq sc
overflow_rule = '\n.sib-faq .sc {overflow:visible !important;}\n.sib-faq .ss-bg {overflow:visible !important;}\n'
content = content.replace(
    '.sib-faq {z-index:5;}',
    '.sib-faq {z-index:5;}' + overflow_rule
)

# 2. Bump container heights to be very generous
content = content.replace('.m .sib-faq {height:1000px;}', '.m .sib-faq {height:1100px;}')
content = content.replace('.d .sib-faq {height:826px;}', '.d .sib-faq {height:900px;}')
content = content.replace('.m .sib-faq.sb-nm-wH .sc {height:1000px;}', '.m .sib-faq.sb-nm-wH .sc {height:1100px;}')
content = content.replace('.d .sib-faq.sb-nm-wH .sc {height:826px;}', '.d .sib-faq.sb-nm-wH .sc {height:900px;}')
content = content.replace('.d .sie-faq_0 {left:0px;top:0px;width:460px;height:826px;}',
                           '.d .sie-faq_0 {left:0px;top:0px;width:460px;height:900px;}')
content = content.replace('.m .sie-faq_0 {left:0px;top:0px;width:320px;height:1000px;}',
                           '.m .sie-faq_0 {left:0px;top:0px;width:320px;height:1100px;}')

# 3. Update JSON heights too
content = content.replace(
    '"slug":"faq","visible":"a","states":[],"d":{"h":826,',
    '"slug":"faq","visible":"a","states":[],"d":{"h":900,'
)
content = content.replace(
    '"bgMediaType":"none"},"m":{"h":1000,"w":320,"nature":"wH"',
    '"bgMediaType":"none"},"m":{"h":1100,"w":320,"nature":"wH"'
)

open('services.html', 'w', encoding='utf-8').write(content)
print("Done!")
