import os

dir_path = r'w:\.clone'

links_to_replace = {
    'href="/"': 'href="index.html"',
    'href="/about"': 'href="about.html"',
    'href="/services"': 'href="services.html"',
    'href="/portfolio-demo-delete"': 'href="portfolio.html"',
    'href="/blog-demo-delete"': 'href="blog.html"',
    'href="/contact"': 'href="contact.html"',
    'href="/featured-project-demo-delete"': 'href="portfolio.html"',
}

html_files = [f for f in os.listdir(dir_path) if f.endswith('.html')]

for file_name in html_files:
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    for old_link, new_link in links_to_replace.items():
        content = content.replace(old_link, new_link)
        
    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_name}")
    else:
        print(f"No changes in {file_name}")
