with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the service-3b HTML pure block with Showit-style block
old = '<div id="service-3b" style="width:100%;background-color:rgba(238,232,223,1);position:relative;">'

# Find the end of the service-3b block
start = content.find(old)
if start == -1:
    print("ERROR: service-3b not found")
    exit(1)

# Find the closing div of service-3b - it ends before service-3
end_marker = '<div id="service-3"'
end = content.find(end_marker, start)
if end == -1:
    print("ERROR: end marker not found")
    exit(1)

old_block = content[start:end]

new_block = '<div id="service-3b" data-bid="service-1" class="sb sib-service-1 sb-nd-wH" style="background-color:rgba(238,232,223,1) !important;"><div class="ss-s ss-bg"><div class="sc" style="width:1200px"><div class="str-im str-id" data-tran="service-3b_0"><div data-sid="service-3b_0" class="sie-service-1_0 se" style="left:40px;top:40px;width:520px;height:calc(100% - 80px);min-height:1020px;background:#fff;box-shadow:0 8px 32px rgba(0,0,0,0.18);"><div style="width:100%;height:100%;background-image:url(\'https://i.postimg.cc/5t5Ry1Qv/Taylor_Paul_368.jpg\');background-size:cover;background-position:center center;position:absolute;top:18px;left:18px;right:18px;bottom:60px;width:auto;height:auto;" class="se-img se-gr slzy"></div></div></div><div class="str-im str-id" data-tran="service-3b_1"><div data-sid="service-3b_1" class="sie-service-1_1 se"><h3 class="se-t sie-service-1_1-text st-m-heading st-d-heading se-rc"><span style="font-size:0.35em;letter-spacing:0.1em;display:block;margin-bottom:4px;">Wedding Package 3</span>Ours<span style="font-size:0.3em;font-weight:normal;display:block;margin-top:4px;">Hourly Package</span><br></h3></div></div><div data-sid="service-3b_2" class="sie-service-1_2 se"><p class="se-t sie-service-1_2-text st-m-paragraph st-d-paragraph se-rc"><strong style="font-size:1.1em;">For the amount of hours hired.</strong><br>All happy tears and love captured.<br><br><strong style="font-size:1.1em;">One Photographer</strong><br>One photographer throughout the coverage<br><br><strong style="font-size:1.1em;">Same Day Previews</strong><br>Previews delivered before midnight.<br><br><strong style="font-size:1.1em;">High Res &amp; Web Size Images</strong><br>Between 30\u201360 photos delivered per hour hired<br><br><strong style="font-size:1.1em;">Online Gallery</strong><br>(Included 2 years of cloud storage)<br><br><strong style="font-size:1.1em;">Consultation Meetings</strong><br>(Timeline &amp; creative planning meetings with me)<br><br><span style="display:block;margin-top:8px;font-size:42px;font-family:\'Instrument Serif\';line-height:1.1;">\u00a3160.00/hour</span></p></div></div></div></div>'

content = content[:start] + new_block + content[end:]

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('done')
