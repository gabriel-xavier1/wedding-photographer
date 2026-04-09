content = open('services.html', 'r', encoding='utf-8').read()

# The Showit JS reads init_data JSON to know which elements exist and their positions
# faq_14, faq_15, faq_16 are not in the JSON - that's why they don't render
# We need to add them to the JSON

# Find the faq_13 entry in JSON to insert after it
# Pattern from faq_12 and faq_13:
# {"type":"text","visible":"a","id":"faq_12","blockId":"faq","m":{...},"d":{...}}
# {"type":"text","visible":"a","id":"faq_13","blockId":"faq","m":{...},"d":{...}}

# faq_12 desktop: left:492, top:511, w:665, h:40
# faq_13 desktop: left:492, top:558, w:665, h:90
# faq_14 (line): left:492, top:668, w:665, h:1
# faq_15 (title): left:492, top:698, w:665, h:23
# faq_16 (answer): left:492, top:726, w:665, h:60

# faq_12 mobile: left:17, top:664, w:284, h:50
# faq_13 mobile: left:17, top:724, w:286, h:80
# faq_14 (line): left:17, top:824, w:286, h:1
# faq_15 (title): left:17, top:850, w:284, h:50
# faq_16 (answer): left:17, top:910, w:286, h:60

new_json_entries = (
    ',{"type":"line","visible":"a","id":"faq_14","blockId":"faq",'
    '"m":{"x":17,"y":824,"w":286,"h":1,"a":0},'
    '"d":{"x":492,"y":668,"w":665,"h":1,"a":0}}'
    ',{"type":"text","visible":"a","id":"faq_15","blockId":"faq",'
    '"m":{"x":17,"y":850,"w":284,"h":50,"a":0,"trIn":{"cl":"fadeIn","d":"0.5","dl":"0"}},'
    '"d":{"x":492,"y":698,"w":665,"h":23,"a":0,"trIn":{"cl":"fadeIn","d":"0.5","dl":"0"}}}'
    ',{"type":"text","visible":"a","id":"faq_16","blockId":"faq",'
    '"m":{"x":17,"y":910,"w":286,"h":60,"a":0,"trIn":{"cl":"fadeIn","d":"0.5","dl":"0"}},'
    '"d":{"x":492,"y":726,"w":665,"h":60,"a":0,"trIn":{"cl":"fadeIn","d":"0.5","dl":"0"}}}'
)

# Find faq_13 JSON entry and insert after it
# Look for the closing of faq_13 entry
faq13_marker = '"id":"faq_13","blockId":"faq"'
idx = content.find(faq13_marker)
count = 0
while idx >= 0:
    # Find the closing } of this object
    end = content.find('}', idx)
    # Make sure we get the full object (nested braces)
    depth = 0
    start = content.rfind('{', 0, idx)
    for i in range(start, len(content)):
        if content[i] == '{':
            depth += 1
        elif content[i] == '}':
            depth -= 1
            if depth == 0:
                end = i
                break
    
    # Check if faq_14 already exists after this
    next_chunk = content[end:end+100]
    if '"faq_14"' not in content[end:end+200]:
        content = content[:end+1] + new_json_entries + content[end+1:]
        count += 1
        print(f"Inserted at position {end}")
    
    # Find next occurrence
    idx = content.find(faq13_marker, end + len(new_json_entries) + 100)

print(f"Total insertions: {count}")

# Verify
if '"faq_14"' in content:
    print("faq_14 found in JSON ✓")
if '"faq_15"' in content:
    print("faq_15 found in JSON ✓")
if '"faq_16"' in content:
    print("faq_16 found in JSON ✓")

open('services.html', 'w', encoding='utf-8').write(content)
print("Done!")
