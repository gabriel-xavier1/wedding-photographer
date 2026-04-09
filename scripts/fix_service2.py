with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace image
content = content.replace(
    'style="width:100%;height:100%" data-img="service-2_0" class="se-img se-gr slzy"></div><noscript><img src="//static.showit.co/800/lrPZdC8eQyeEvSGzP-pMaA/135701/andres-molina--x2t5s6srfe-unsplash_1.jpg" class="se-img" alt="" title="andres-molina--X2t5s6SRfE-unsplash (1)"/></noscript>',
    'style="width:100%;height:100%;background-image:url(https://i.postimg.cc/d3fQLGZL/Vivien_Jordon_463.jpg);background-size:cover;background-position:center center;" data-img="service-2_0" class="se-img se-gr slzy"></div>'
)

# Replace title
content = content.replace(
    '<h3 class="se-t sie-service-2_1-text st-m-heading st-d-heading se-rc">elopements<br></h3>',
    '<h3 class="se-t sie-service-2_1-text st-m-heading st-d-heading se-rc"><span style="font-size:0.35em;letter-spacing:0.1em;display:block;margin-bottom:4px;">Wedding Package 2</span>MINE<span style="font-size:0.3em;font-weight:normal;display:block;margin-top:4px;">up to 5 hours coverage</span><br></h3>'
)

# Replace body text
old_body = 'Elopements are not \u201cless\u201d \u2014 they are more intentional, more connected, and more reflective of who you are.<br>Whether your vows happen on a cliff at sunrise or in a quiet clearing deep in the woods, I\u2019m here to document the whole, beautiful story.<br><br>Perfect for couples who want:<br>\u2022 A meaningful day without pressure<br>\u2022 A celebration rooted in presence<br>\u2022 Space to breathe, explore, and be themselves<br><br>WHAT\u2019S INCLUDED:<br>\u2022 Tailored timeline support<br>\u2022 Location scouting + permits guidance<br>\u2022 2\u20134 hours of coverage<br>\u2022 Online gallery with unlimited downloads<br>\u2022 Optional film add-ons<br>'

new_body = '<strong style="font-size:1.1em;">Up to 5 hours coverage</strong><br>All happy tears and love captured.<br><br><strong style="font-size:1.1em;">One Photographer</strong><br>One photographer throughout the coverage<br><br><strong style="font-size:1.1em;">Same Day Previews</strong><br>Previews delivered before midnight<br><br><strong style="font-size:1.1em;">High Res &amp; Web Size Images</strong><br>Between 300\u2013500 photos delivered<br><br><strong style="font-size:1.1em;">Online Gallery</strong><br>(Includes 2 years of cloud storage)<br><br><strong style="font-size:1.1em;">Consultation Meetings</strong><br>(Timeline &amp; creative planning meetings with me)<br><br><span style="display:block;margin-top:24px;text-transform:uppercase;letter-spacing:0.2em;font-size:13px;font-family:\'Overpass\';font-weight:500;">Drone available, weather and venue depending.</span><span style="display:block;margin-top:8px;font-size:42px;font-family:\'Instrument Serif\';line-height:1.1;">\u00a3550.00</span><span style="display:block;margin-top:4px;font-size:18px;font-style:italic;font-family:\'Instrument Serif\';">*Extra hour \u00a3150.00</span><br><br><a href="contact.html" style="display:inline-block;margin-top:8px;padding:14px 36px;background-color:#c0522a;color:#fff;text-decoration:none;letter-spacing:0.15em;font-size:13px;font-family:\'Overpass\',sans-serif;font-weight:500;text-transform:uppercase;">INQUIRE</a>'

content = content.replace(old_body, new_body)

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('done')
