content = open('services.html', 'r', encoding='utf-8').read()

# Encontrar e substituir o texto atual
idx = content.find('sie-service-1_2 se"><p class="se-t sie-service-1_2-text st-m-paragraph st-d-paragraph se-rc">')
end = content.find('</p></div><div data-sid="service-1_3"', idx)
start_pos = idx + len('sie-service-1_2 se"><p class="se-t sie-service-1_2-text st-m-paragraph st-d-paragraph se-rc">')

new_text = ('Full day coverage<br>'
            'All happy tears and love captured.<br><br>'
            'Two Photographers<br>'
            'One photographer for up to 10 hours<br>'
            'Second photographer for up to 5 hours<br><br>'
            'Same Day Previews<br>'
            'Previews delivered during wedding breakfast<br><br>'
            'High Res &amp; Web Size Images<br>'
            'Between 400\u2013800 photos delivered<br><br>'
            'Memory Box<br>'
            '(10 6x4 photos printed in a wooden box)<br><br>'
            'USB Drive<br>'
            '(Includes entire gallery, mailed to you)<br><br>'
            'Online Gallery<br>'
            '(Includes 2 years of cloud storage)<br><br>'
            'Consultation Meetings<br>'
            '(Timeline &amp; creative planning meetings with me)<br><br>'
            'Drone available, weather and venue depending.<br>')

content = content[:start_pos] + new_text + content[end:]

# Ajustar CSS do texto para ter hierarquia visual
# Título de cada item em tamanho maior via CSS
css_add = '''
.d .sie-service-1_2-text br + br {display:block;margin-top:8px;}
'''

open('services.html', 'w', encoding='utf-8').write(content)
print('OK')
