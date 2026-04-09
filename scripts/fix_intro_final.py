import re

services = open('services.html', 'r', encoding='utf-8').read()

# ── Step 1: Remove the duplicate intro block inserted after collage ───────────
# The duplicate is the second occurrence of id="intro"
first = services.find('<div id="intro"')
second = services.find('<div id="intro"', first + 1)

if second >= 0:
    depth = 0
    i = second
    while i < len(services):
        if services[i:i+4] == '<div': depth += 1
        elif services[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                dup_end = i + 6
                break
        i += 1
    services = services[:second] + services[dup_end:]
    print("Removed duplicate intro block")
else:
    print("No duplicate found")

# ── Step 2: Update texts in the ORIGINAL intro block ─────────────────────────
# intro_0: "The experience" -> "Raw, soulful, storytelling"
services = services.replace(
    '>The experience<br></p>',
    '>Raw, soulful, storytelling<br></p>'
)

# intro_1: "Your story deserves..." -> new heading
old_h3 = 'Your story deserves to be documented with <i>intention, presence, and heart.</i><br><br>'
new_h3 = 'Where the wind tangles your hair, your footsteps echo in soft sand, and the mountains stand witness to your vows \u2014 that\u2019s where your story unfolds.<br>'
services = services.replace(old_h3, new_h3)

# intro_2: paragraph -> clear it
services = re.sub(
    r'(data-sid="intro_2"[^>]*>.*?se-rc">).*?(<br></p>)',
    r'\1<br>\2',
    services, flags=re.DOTALL
)

# ── Step 3: Move intro block to after collage ─────────────────────────────────
# Extract intro block from current position
intro_start = services.find('<div id="intro"')
depth = 0
i = intro_start
while i < len(services):
    if services[i:i+4] == '<div': depth += 1
    elif services[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            intro_end = i + 6
            break
    i += 1
intro_html = services[intro_start:intro_end]

# Remove from current position
services = services[:intro_start] + services[intro_end:]

# Find collage end
collage_start = services.find('<div id="collage-intro"')
depth = 0
i = collage_start
while i < len(services):
    if services[i:i+4] == '<div': depth += 1
    elif services[i:i+6] == '</div>':
        depth -= 1
        if depth == 0:
            collage_end = i + 6
            break
    i += 1

# Insert intro after collage
services = services[:collage_end] + '\n' + intro_html + services[collage_end:]
print("Moved intro block after collage")

open('services.html', 'w', encoding='utf-8').write(services)
print("Done!")
