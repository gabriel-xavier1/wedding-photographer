content = open('services.html', 'r', encoding='utf-8').read()

# ============================================================
# DESKTOP layout recalculation
# Starting point: faq_3 (Q1 title) at top:74
# Pattern: title(23h) -> answer -> divider(1h) -> title -> answer -> divider...
# Gap between answer bottom and divider: ~30px
# Gap between divider and next title: ~35px
# Gap between title and answer: ~27px
# ============================================================

# Q1: faq_3 title top:74, faq_4 answer top:100 (h:44) -> bottom:144
# divider faq_5: top:175 (gap 31) -> bottom:176
# Q2: faq_6 title top:213 (gap 37), faq_7 answer top:241 (h:48) -> bottom:289
# divider faq_8: top:313 (gap 24) -> bottom:314
# Q3: faq_9 title top:346 (gap 32), faq_10 answer top:375 (h:77) -> bottom:452
# divider faq_11: top:478 (gap 26) -> bottom:479
# Q4: faq_12 title top:511 (gap 32), faq_13 answer top:540 (h:77) -> bottom:617
# BUT "CAN WE MEET..." title is 2 lines, needs more height!
# Let's give faq_12 height:40 and faq_13 top:551, height:90
# divider faq_14: top:651, faq_15 title top:686, faq_16 answer top:715

# Fix faq_12 height (title is 2 lines on desktop)
content = content.replace(
    '.d .sie-faq_12 {left:492px;top:511px;width:665px;height:23px;}',
    '.d .sie-faq_12 {left:492px;top:511px;width:665px;height:40px;}'
)
# Fix faq_13 top and height (answer needs more room)
content = content.replace(
    '.d .sie-faq_13 {left:492px;top:540px;width:665px;height:77px;}',
    '.d .sie-faq_13 {left:492px;top:558px;width:665px;height:90px;}'
)
# Fix faq_14 divider (after faq_13 bottom: 558+90=648, gap 20)
content = content.replace(
    '.d .sie-faq_14 {left:492px;top:647px;width:665px;height:1px;}',
    '.d .sie-faq_14 {left:492px;top:668px;width:665px;height:1px;}'
)
# Fix faq_15 title (after divider, gap 30)
content = content.replace(
    '.d .sie-faq_15 {left:492px;top:680px;width:665px;height:23px;}',
    '.d .sie-faq_15 {left:492px;top:698px;width:665px;height:23px;}'
)
# Fix faq_16 answer (after title, gap 27)
content = content.replace(
    '.d .sie-faq_16 {left:492px;top:709px;width:665px;height:77px;}',
    '.d .sie-faq_16 {left:492px;top:726px;width:665px;height:60px;}'
)

# Desktop container: faq_16 bottom = 726+60=786, add 40px padding = 826
content = content.replace('.d .sib-faq {height:830px;}', '.d .sib-faq {height:826px;}')
content = content.replace('.d .sie-faq_0 {left:0px;top:0px;width:460px;height:830px;}',
                           '.d .sie-faq_0 {left:0px;top:0px;width:460px;height:826px;}')

# ============================================================
# MOBILE layout recalculation
# Q4 title "CAN WE MEET..." is very long, needs more height
# faq_12 top:664, height:15 -> needs height:50 for 2 lines
# faq_13 top:684 -> push to 664+50+10=724, height:80
# faq_14 divider: 724+80+20=824
# faq_15 title: 824+20=844, height:15
# faq_16 answer: 844+20=864, height:60
# container: 864+60+30=954
# ============================================================

content = content.replace(
    '.m .sie-faq_12 {left:17px;top:664px;width:284px;height:15px;}',
    '.m .sie-faq_12 {left:17px;top:664px;width:284px;height:50px;}'
)
content = content.replace(
    '.m .sie-faq_13 {left:17px;top:684px;width:286px;height:68px;}',
    '.m .sie-faq_13 {left:17px;top:724px;width:286px;height:80px;}'
)
content = content.replace(
    '.m .sie-faq_14 {left:17px;top:772px;width:286px;height:1px;}',
    '.m .sie-faq_14 {left:17px;top:824px;width:286px;height:1px;}'
)
content = content.replace(
    '.m .sie-faq_15 {left:17px;top:798px;width:284px;height:15px;}',
    '.m .sie-faq_15 {left:17px;top:850px;width:284px;height:50px;}'
)
content = content.replace(
    '.m .sie-faq_16 {left:17px;top:818px;width:286px;height:68px;}',
    '.m .sie-faq_16 {left:17px;top:910px;width:286px;height:60px;}'
)

# Mobile container: 910+60+30=1000
content = content.replace('.m .sib-faq {height:1050px;}', '.m .sib-faq {height:1000px;}')
content = content.replace('.m .sib-faq.sb-nm-wH .sc {height:1050px;}', '.m .sib-faq.sb-nm-wH .sc {height:1000px;}')

open('services.html', 'w', encoding='utf-8').write(content)
print("Done!")
