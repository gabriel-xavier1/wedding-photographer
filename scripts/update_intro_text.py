services = open('services.html', 'r', encoding='utf-8').read()

# intro_0: title (script font) - "earth-rooted" -> "Your wedding day happens so quickly"
services = services.replace(
    '>earth-rooted<br></div>',
    '>Your wedding day happens so quickly<br></div>'
)

# intro_1: "Raw, soulful," -> clear
services = services.replace(
    '>Raw, soulful,<br></div>',
    '><br></div>'
)

# intro_2: "storytelling" -> clear
services = services.replace(
    '>storytelling<br></div>',
    '><br></div>'
)

# intro_3: paragraph text
old_p = '>Where the wind tangles your hair, your footsteps echo in soft sand, and the mountains stand witness to your vows \u2014 that\u2019s where your story unfolds.<'
new_p = ">Time flies. Before you know it, the day is gone. But I'm there to capture it all. The mini moments between the I-do's and First kiss. A sweet moment with grandma or your guests barefoot on the dance floor \u2013 I live for that stuff. It's the memories not on your shot list, and the ones you didn't know you really wanted.<"

if old_p in services:
    services = services.replace(old_p, new_p)
    print("Replaced intro_3 text (with em dash)")
else:
    # Try without special chars
    import re
    services = re.sub(
        r'(data-sid="intro_3"[^>]*>.*?se-rc">).*?(<)',
        r"\1Time flies. Before you know it, the day is gone. But I'm there to capture it all. The mini moments between the I-do's and First kiss. A sweet moment with grandma or your guests barefoot on the dance floor \u2013 I live for that stuff. It's the memories not on your shot list, and the ones you didn't know you really wanted.\2",
        services, flags=re.DOTALL, count=1
    )
    print("Replaced intro_3 text (regex)")

open('services.html', 'w', encoding='utf-8').write(services)
print("Done!")
