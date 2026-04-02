with open('original/index.html', 'r', encoding='utf-8') as f:
    original = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    current = f.read()

# Extract original about block
start_orig = original.find('id="about"')
end_orig = original.find('id="trusted-by"')
orig_block = original[start_orig:end_orig]

# Find current about block boundaries
start_curr = current.find('id="about"')
end_curr = current.find('id="trusted-by"')

if start_curr == -1 or end_curr == -1:
    print('ERROR: could not find about block in current file')
else:
    restored = current[:start_curr] + orig_block + current[end_curr:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(restored)
    print('DONE')
