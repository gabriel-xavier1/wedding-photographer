services = open('services.html', 'r', encoding='utf-8').read()

def remove_block(content, block_id):
    marker = f'<div id="{block_id}"'
    start = content.find(marker)
    if start < 0:
        print(f"  NOT FOUND: {block_id}")
        return content
    depth = 0
    i = start
    while i < len(content):
        if content[i:i+4] == '<div': depth += 1
        elif content[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                end = i + 6
                break
        i += 1
    content = content[:start] + content[end:]
    print(f"  Removed: {block_id}")
    return content

to_remove = ['service-3', 'packages', 'freebie-2', 'portfolio', 'testimonials', 'cta-contact']

for block_id in to_remove:
    services = remove_block(services, block_id)

open('services.html', 'w', encoding='utf-8').write(services)
print("Done!")
