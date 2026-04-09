content = open('services.html', 'r', encoding='utf-8').read()

# 1. Update JSON heights for faq block (Showit uses these for rendering)
# There are multiple occurrences (repeated in script tags), replace all
content = content.replace(
    '"slug":"faq","visible":"a","states":[],"d":{"h":670,',
    '"slug":"faq","visible":"a","states":[],"d":{"h":826,'
)
content = content.replace(
    '"bgMediaType":"none"},"m":{"h":801,"w":320,"nature":"wH"',
    '"bgMediaType":"none"},"m":{"h":1000,"w":320,"nature":"wH"'
)

# 2. Fix desktop .sc height (was missing)
content = content.replace(
    '.m .sib-faq.sb-nm-wH .sc {height:1000px;}.d .sib-faq.sb-nm-wH .sc {height:826px;}',
    '.m .sib-faq.sb-nm-wH .sc {height:1000px;}'
)
# Add desktop sc height properly after mobile one
content = content.replace(
    '.m .sib-faq.sb-nm-wH .sc {height:1000px;}',
    '.m .sib-faq.sb-nm-wH .sc {height:1000px;}\n.d .sib-faq.sb-nm-wH .sc {height:826px;}'
)

# 3. Fix mobile faq_0 height to cover full container
content = content.replace(
    '.m .sie-faq_0 {left:0px;top:0px;width:320px;height:1000px;}',
    '.m .sie-faq_0 {left:0px;top:0px;width:320px;height:1000px;}'
)

# Verify
import re
print("=== JSON heights ===")
for m in re.finditer(r'"slug":"faq"[^}]*"d":\{"h":(\d+)', content):
    print(f"  desktop h: {m.group(1)}")
for m in re.finditer(r'"slug":"faq".*?"m":\{"h":(\d+)', content):
    print(f"  mobile h: {m.group(1)}")

print("\n=== CSS heights ===")
for line in content.split('\n'):
    if 'sib-faq' in line and ('height' in line or 'sc' in line):
        print(' ', line.strip())

open('services.html', 'w', encoding='utf-8').write(content)
print("\nDone!")
