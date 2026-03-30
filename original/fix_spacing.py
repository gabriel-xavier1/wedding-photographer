import urllib.request
import os

urls = {
    'index.html': 'https://aspen-willow.showit.site/',
    'about.html': 'https://aspen-willow.showit.site/about',
    'services.html': 'https://aspen-willow.showit.site/services',
    'portfolio.html': 'https://aspen-willow.showit.site/portfolio-demo-delete',
    'blog.html': 'https://aspen-willow.showit.site/blog-demo-delete',
    'contact.html': 'https://aspen-willow.showit.site/contact'
}

replacements = {
    'href=\"/\"': 'href=\"index.html\"',
    'href=\"/about\"': 'href=\"about.html\"',
    'href=\"/services\"': 'href=\"services.html\"',
    'href=\"/portfolio-demo-delete\"': 'href=\"portfolio.html\"',
    'href=\"/blog-demo-delete\"': 'href=\"blog.html\"',
    'href=\"/contact\"': 'href=\"contact.html\"',
    'href=\"/featured-project-demo-delete\"': 'href=\"portfolio.html\"',
    'href=\"/services#service-1\"': 'href=\"services.html#service-1\"',
    'href=\"/services#service-2\"': 'href=\"services.html#service-2\"',
    'href=\"/services#service-3\"': 'href=\"services.html#service-3\"',
    'href=\"/legal-notices\"': 'href=\"#\"',
    'href=\"/single-post-demo-delete\"': 'href=\"blog.html\"',
    'href=\"/category/\"': 'href=\"blog.html\"'
}

for fname, url in urls.items():
    print(f"Downloading {fname}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
        for old, new in replacements.items():
            content = content.replace(old, new)
        with open('w:/.clone/' + fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {fname}")
    except Exception as e:
        print(f"Error {fname}: {e}")
