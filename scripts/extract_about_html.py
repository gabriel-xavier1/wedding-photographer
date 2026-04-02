with open('original copy 2/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    orig = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    current = f.read()

# Extract about section HTML from original
start_marker = 'id="about"'
end_marker = 'id="trusted-by"'

start = orig.find(start_marker)
end = orig.find(end_marker)

if start == -1 or end == -1:
    print("Markers not found")
else:
    # Go back to find the opening div
    div_start = orig.rfind('<div ', 0, start)
    about_html = orig[div_start:end]
    print("Found about section, length:", len(about_html))
    print("Preview:", about_html[:200])

    # Now replace in current index.html
    curr_start = current.find(start_marker)
    curr_end = current.find(end_marker)
    curr_div_start = current.rfind('<div ', 0, curr_start)

    old_about = current[curr_div_start:curr_end]
    new_content = current.replace(old_about, about_html, 1)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Done - about section replaced")
