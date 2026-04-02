with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

fixes = [
    # Block heights - already correct from last restore
    # about_1 text
    ('.d .sie-about_1 {left:686px;top:518px;width:490px;height:187px;}',
     '.d .sie-about_1 {left:686px;top:518px;width:490px;height:187px;}'),

    # about_2 heading - restore original font size and position
    ('.d .sie-about_2 {left:58px;top:161px;width:392px;height:104px;}',
     '.d .sie-about_2 {left:58px;top:161px;width:392px;height:104px;}'),

    # about_3 photo - restore original (no custom image override)
    (".d .sie-about_3 .se-img {background-repeat:no-repeat;background-size:cover;background-position:center center;border-radius:inherit;background-image:url('https://i.postimg.cc/V5P1f0DJ/Whats-App-Image-2026-02-06-at-17-55-03.jpg') !important;}",
     ".d .sie-about_3 .se-img {background-repeat:no-repeat;background-size:cover;background-position:50% 50%;border-radius:inherit;}"),

    (".m .sie-about_3 .se-img {background-repeat:no-repeat;background-size:cover;background-position:center center;border-radius:inherit;background-image:url('https://i.postimg.cc/V5P1f0DJ/Whats-App-Image-2026-02-06-at-17-55-03.jpg') !important;}",
     ".m .sie-about_3 .se-img {background-repeat:no-repeat;background-size:cover;background-position:50% 50%;border-radius:inherit;}"),

    # about_4 - restore (was hidden, now show original)
    ('.d .sie-about_4 {display:none !important;}',
     '.d .sie-about_4 {left:686px;top:105px;width:267px;height:343px;}'),
    ('.m .sie-about_4 {display:none !important;}',
     '.m .sie-about_4 {left:205px;top:115px;width:115px;height:142px;}'),
    ('.d .sie-about_4 .se-img {display:none !important;}',
     '.d .sie-about_4 .se-img {background-repeat:no-repeat;background-size:cover;background-position:50% 50%;border-radius:inherit;}'),
    ('.m .sie-about_4 .se-img {display:none !important;}',
     '.m .sie-about_4 .se-img {background-repeat:no-repeat;background-size:cover;background-position:50% 50%;border-radius:inherit;}'),
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
    '<p class="se-t sie-about_2-text st-m-heading st-d-heading se-rc">HI<br>I AM<br></p>',
    '<p class="se-t sie-about_2-text st-m-heading st-d-heading se-rc">HI<br>I AM<br></p>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done.')
