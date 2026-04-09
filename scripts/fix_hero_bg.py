services = open('services.html', 'r', encoding='utf-8').read()

new_url = 'https://i.postimg.cc/q7dCxz6g/home-invesment.jpg'

# The Showit JS reads bgImage from JSON and applies it as inline style on .ssp-d
# We need to update the bgImage key in the hero slug JSON entry
# Current: "bgImage":{"key":"_i_LgiyN3eoHHkkGV6XTDg/135701/andres-molina-fluledeatmy-unsplash.jpg",...}
# Replace with external URL format

old_key = '"key":"_i_LgiyN3eoHHkkGV6XTDg/135701/andres-molina-fluledeatmy-unsplash.jpg"'
new_key = f'"key":"{new_url}"'

if old_key in services:
    services = services.replace(old_key, new_key)
    print("Updated hero bgImage key in JSON")
else:
    # Try with spaces
    old_key2 = '"key": "_i_LgiyN3eoHHkkGV6XTDg/135701/andres-molina-fluledeatmy-unsplash.jpg"'
    new_key2 = f'"key": "{new_url}"'
    if old_key2 in services:
        services = services.replace(old_key2, new_key2)
        print("Updated hero bgImage key in JSON (with spaces)")
    else:
        print("Key not found, searching...")
        idx = services.find('fluledeatmy')
        print(f"Found at: {idx}")
        print(repr(services[idx-50:idx+100]))

open('services.html', 'w', encoding='utf-8').write(services)
print("Done!")
