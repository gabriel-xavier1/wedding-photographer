content = open('services.html', 'r', encoding='utf-8').read()

# 1. Increase container heights
content = content.replace('.m .sib-faq {height:801px;}', '.m .sib-faq {height:1050px;}')
content = content.replace('.d .sib-faq {height:670px;}', '.d .sib-faq {height:830px;}')
content = content.replace('.m .sib-faq.sb-nm-wH .sc {height:801px;}', '.m .sib-faq.sb-nm-wH .sc {height:1050px;}')

# 2. Also fix the faq_0 (left image column) height to match
content = content.replace('.d .sie-faq_0 {left:0px;top:0px;width:460px;height:670px;}', '.d .sie-faq_0 {left:0px;top:0px;width:460px;height:830px;}')
content = content.replace('.m .sie-faq_0 {left:0px;top:0px;width:320px;height:188px;}', '.m .sie-faq_0 {left:0px;top:0px;width:320px;height:220px;}')

# 3. Add CSS for faq_14 (divider line), faq_15 (question title), faq_16 (answer)
# Pattern from existing elements:
# faq_11 (divider): d top:478, m top:638
# faq_12 (title):   d top:511, m top:664
# faq_13 (answer):  d top:540, m top:684
# Spacing: divider->title = 33px (d), 26px (m); title->answer = 29px (d), 20px (m)
# answer height = 77px (d), 68px (m)
# Next divider = 540+77+30 = 647 (d), 684+68+20 = 772 (m)

new_css = """
.d .sie-faq_14 {left:492px;top:647px;width:665px;height:1px;}
.m .sie-faq_14 {left:17px;top:772px;width:286px;height:1px;}
.sie-faq_14 svg {vertical-align:top;overflow:visible;pointer-events:none;box-sizing:content-box;}
.m .sie-faq_14 svg {stroke:rgba(22,22,22,1);transform:scaleX(1);padding:0.5px;height:1px;width:286px;}
.d .sie-faq_14 svg {stroke:rgba(22,22,22,1);transform:scaleX(1);padding:0.5px;height:1px;width:665px;}
.m .sie-faq_14 line {stroke-linecap:butt;stroke-width:1;stroke-dasharray:none;pointer-events:all;}
.d .sie-faq_14 line {stroke-linecap:butt;stroke-width:1;stroke-dasharray:none;pointer-events:all;}
.d .sie-faq_15 {left:492px;top:680px;width:665px;height:23px;}
.m .sie-faq_15 {left:17px;top:798px;width:284px;height:15px;}
.d .sie-faq_15-text {font-size:15px;text-align:left;}
.m .sie-faq_15-text {font-size:12px;text-align:left;}
.d .sie-faq_16 {left:492px;top:709px;width:665px;height:77px;}
.m .sie-faq_16 {left:17px;top:818px;width:286px;height:68px;}
.d .sie-faq_16-text {color:rgba(22,22,22,1);font-size:16px;text-align:left;}
.m .sie-faq_16-text {color:rgba(22,22,22,1);font-size:12px;text-align:left;}
"""

# Insert before closing </style>
content = content.replace('.m .sib-cta-contact {height:333px;}', new_css + '.m .sib-cta-contact {height:333px;}')

open('services.html', 'w', encoding='utf-8').write(content)
print("Done!")
