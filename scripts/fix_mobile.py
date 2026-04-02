import re

with open('W:/.clone/original copy 2/index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    curr = f.read()

# Pegar todos os valores .m do about e freebie do original
mobile_patterns = [
    r'\.m \.sib-about \{[^}]+\}',
    r'\.m \.sib-about \.ss-bg \{[^}]+\}',
    r'\.m \.sie-about_0 \{[^}]+\}',
    r'\.m \.sie-about_0\.se \{[^}]+\}',
    r'\.m \.sie-about_0 \.se-button \{[^}]+\}',
    r'\.m \.sie-about_0 \.se-button span \{[^}]+\}',
    r'\.m \.sie-about_1 \{[^}]+\}',
    r'\.m \.sie-about_1-text \{[^}]+\}',
    r'\.m \.sie-about_2 \{[^}]+\}',
    r'\.m \.sie-about_2-text \{[^}]+\}',
    r'\.m \.sie-about_3 \{[^}]+\}',
    r'\.m \.sie-about_4 \{[^}]+\}',
    r'\.m \.sie-about_5 \{[^}]+\}',
    r'\.m \.sie-about_5-text \{[^}]+\}',
    r'\.m \.sib-freebie \{[^}]+\}',
    r'\.m \.sib-freebie \.ss-bg \{[^}]+\}',
    r'\.m \.sie-freebie_0 \{[^}]+\}',
    r'\.m \.sie-freebie_1 \{[^}]+\}',
    r'\.m \.sie-freebie_1\.se \{[^}]+\}',
    r'\.m \.sie-freebie_1 \.se-button \{[^}]+\}',
    r'\.m \.sie-freebie_1 \.se-button span \{[^}]+\}',
    r'\.m \.sie-freebie_2 \{[^}]+\}',
    r'\.m \.sie-freebie_3 \{[^}]+\}',
    r'\.m \.sie-freebie_3-text \{[^}]+\}',
    r'\.m \.sie-freebie_4 \{[^}]+\}',
]

for p in mobile_patterns:
    orig_m = re.search(p, orig)
    curr_m = re.search(p, curr)
    if orig_m and curr_m:
        if orig_m.group() != curr_m.group():
            curr = curr.replace(curr_m.group(), orig_m.group())
            print(f'RESTORED: {orig_m.group()[:80]}')
    elif orig_m and not curr_m:
        print(f'MISSING in curr: {orig_m.group()[:80]}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(curr)
print('DONE')
