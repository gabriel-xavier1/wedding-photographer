import subprocess
import re

# Get the old commit's index.html
result = subprocess.run(
    ['git', 'show', '335dde71ba374190025727bcd369211f5ace5d0d:index.html'],
    capture_output=True, text=True, encoding='utf-8'
)
old_content = result.stdout

# Get current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    current_content = f.read()

# Extract about CSS from old commit (lines with sib-about or sie-about)
# CSS section
old_css_lines = []
for line in old_content.split('\n'):
    if 'sib-about' in line or 'sie-about' in line:
        old_css_lines.append(line)

print("Old about CSS lines:")
for l in old_css_lines:
    print(repr(l))

# Extract about CSS from current
current_css_lines = []
for line in current_content.split('\n'):
    if 'sib-about' in line or 'sie-about' in line:
        current_css_lines.append(line)

print("\nCurrent about CSS lines:")
for l in current_css_lines:
    print(repr(l))
