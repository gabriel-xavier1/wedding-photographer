content = open('services.html', 'r', encoding='utf-8').read()

# Find the garbage between faq_10 closing and faq_11 opening
idx = content.find('<div data-sid="faq_11"the wilderness')
if idx >= 0:
    # Find where the real faq_11 starts
    real_faq11 = content.find('<div data-sid="faq_11" class="sie-faq_11', idx)
    print(f"Garbage found at {idx}, real faq_11 at {real_faq11}")
    print("Garbage:", repr(content[idx:real_faq11]))
    # Remove the garbage
    content = content[:idx] + content[real_faq11:]
    print("Fixed!")
else:
    # Try alternate search
    idx2 = content.find('the wilderness is my second home')
    if idx2 >= 0:
        print(f"Found garbage at {idx2}")
        print(repr(content[idx2-50:idx2+200]))
    else:
        print("No garbage found")

open('services.html', 'w', encoding='utf-8').write(content)
