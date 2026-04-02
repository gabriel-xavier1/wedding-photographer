with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Restore about CSS to commit 335dde71 values
# Old commit values:
# .m .sib-about {height:701px;}  (original from 335dde71)
# .d .sib-about {height:828px;}
# .d .sie-about_0 {left:686px;top:742px;width:220px;height:47px;}
# .m .sie-about_0 {left:25px;top:619px;width:180px;height:45px;}
# .d .sie-about_1 {left:686px;top:518px;width:490px;height:187px;}
# .m .sie-about_1 {left:25px;top:345px;width:270px;height:249px;}
# .d .sie-about_2 {left:58px;top:161px;width:392px;height:104px;}
# .m .sie-about_2 {left:25px;top:239px;width:233px;height:67px;}
# .d .sie-about_3 {left:26px;top:367px;width:585px;height:422px;}
# .m .sie-about_3 {left:12px;top:63px;width:222px;height:143px;}
# .d .sie-about_5 {left:58px;top:278px;width:392px;height:50px;}
# .m .sie-about_5 {left:25px;top:301px;width:233px;height:29px;}
# Also restore inline style on about_0 button and about_2 text

fixes = [
    # Block heights
    ('.m .sib-about {height:660px;}', '.m .sib-about {height:701px;}'),
    ('.d .sib-about {height:920px;}', '.d .sib-about {height:828px;}'),

    # about_0 button
    ('.d .sie-about_0 {left:58px;top:745px;width:220px;height:47px;}',
     '.d .sie-about_0 {left:686px;top:742px;width:220px;height:47px;}'),
    ('.m .sie-about_0 {left:25px;top:602px;width:180px;height:45px;}',
     '.m .sie-about_0 {left:25px;top:619px;width:180px;height:45px;}'),

    # about_1 text
    ('.d .sie-about_1 {left:58px;top:240px;width:500px;height:480px !important;overflow:visible !important;}',
     '.d .sie-about_1 {left:686px;top:518px;width:490px;height:187px;}'),
    ('.m .sie-about_1 {left:25px;top:326px;width:270px;height:260px;}',
     '.m .sie-about_1 {left:25px;top:345px;width:270px;height:249px;}'),

    # about_2 heading
    ('.d .sie-about_2 {left:58px;top:100px;width:560px;height:50px;}',
     '.d .sie-about_2 {left:58px;top:161px;width:392px;height:104px;}'),
    ('.m .sie-about_2 {left:25px;top:220px;width:270px;height:50px;}',
     '.m .sie-about_2 {left:25px;top:239px;width:233px;height:67px;}'),

    # about_3 photo
    ('.d .sie-about_3 {left:620px;top:80px;width:540px;height:680px;}',
     '.d .sie-about_3 {left:26px;top:367px;width:585px;height:422px;}'),
    ('.m .sie-about_3 {left:12px;top:63px;width:222px;height:143px;}',
     '.m .sie-about_3 {left:12px;top:63px;width:222px;height:143px;}'),

    # about_5 name
    ('.d .sie-about_5 {left:58px;top:165px;width:392px;height:50px;}',
     '.d .sie-about_5 {left:58px;top:278px;width:392px;height:50px;}'),
    ('.m .sie-about_5 {left:25px;top:278px;width:270px;height:36px;}',
     '.m .sie-about_5 {left:25px;top:301px;width:233px;height:29px;}'),
]

for old, new in fixes:
    if old == new:
        print(f'SKIP: {old[:60]}')
        continue
    if old in content:
        content = content.replace(old, new, 1)
        print(f'OK: {new[:70]}')
    else:
        print(f'NOT FOUND: {old[:70]}')

# Restore about_2 text to original "HI\nI AM"
content = content.replace(
    '<p class="se-t sie-about_2-text st-m-heading st-d-heading se-rc">MEET YOUR PHOTOGRAPHER,<br>Jaque<br></p>',
    '<p class="se-t sie-about_2-text st-m-heading st-d-heading se-rc">HI<br>I AM<br></p>'
)
print('about_2 text restored')

# Restore about_0 button - remove inline style that was added
content = content.replace(
    'class="sie-about_0 se" data-sid="about_0"',
    'class="sie-about_0 se" data-sid="about_0" style="top:713px"'
)
print('about_0 inline style restored')

# Restore about_3 CSS - remove the custom image override, use original
content = content.replace(
    ".d .sie-about_3 .se-img {background-repeat:no-repeat;background-size:cover;background-position:center center;border-radius:inherit;background-image:url('https://i.postimg.cc/V5P1f0DJ/Whats-App-Image-2026-02-06-at-17-55-03.jpg') !important;}",
    ".d .sie-about_3 .se-img {background-repeat:no-repeat;background-size:cover;background-position:center center;border-radius:inherit;background-image:url('https://i.postimg.cc/V5P1f0DJ/Whats-App-Image-2026-02-06-at-17-55-03.jpg') !important;}"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
