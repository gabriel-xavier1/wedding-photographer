with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add service-3b to blockData JSON
old_blockdata = '{"slug":"service-2","visible":"a","states":[],"d":{"h":840,"w":1200'
new_blockdata = '{"slug":"service-3b","visible":"a","states":[],"d":{"h":1160,"w":1200,"locking":{},"nature":"wH","bgFillType":"color","bgColor":"colors-4","bgMediaType":"none"},"m":{"h":790,"w":320,"bgFillType":"color","bgColor":"colors-4","bgMediaType":"none"}},{"slug":"service-2","visible":"a","states":[],"d":{"h":840,"w":1200'

content = content.replace(old_blockdata, new_blockdata, 1)

# 2. Replace the service-3b block with proper Showit structure
old_block_start = '<div id="service-3b" data-bid="service-1" class="sb sib-service-1 sb-nd-wH"'
end_marker = '<div id="service-3"'
start = content.find(old_block_start)
end = content.find(end_marker, start)

if start == -1 or end == -1:
    print(f"ERROR: start={start}, end={end}")
    exit(1)

new_block = '<div id="service-3b" data-bid="service-3b" class="sb sib-service-3b sb-nd-wH"><div class="ss-s ss-bg"><div class="sc" style="width:1200px"><div class="str-im str-id" data-tran="service-3b_0"><div data-sid="service-3b_0" class="sie-service-3b_0 se"><div style="width:100%;height:100%;background-image:url(\'https://i.postimg.cc/5t5Ry1Qv/Taylor_Paul_368.jpg\');background-size:cover;background-position:center center;" data-img="service-3b_0" class="se-img se-gr slzy"></div></div></div><div class="str-im str-id" data-tran="service-3b_1"><div data-sid="service-3b_1" class="sie-service-3b_1 se"><h3 class="se-t sie-service-3b_1-text st-m-heading st-d-heading se-rc"><span style="font-size:0.35em;letter-spacing:0.1em;display:block;margin-bottom:4px;">Wedding Package 3</span>Ours<span style="font-size:0.3em;font-weight:normal;display:block;margin-top:4px;">Hourly Package</span><br></h3></div></div><div data-sid="service-3b_2" class="sie-service-3b_2 se"><p class="se-t sie-service-3b_2-text st-m-paragraph st-d-paragraph se-rc"><strong style="font-size:1.1em;">For the amount of hours hired.</strong><br>All happy tears and love captured.<br><br><strong style="font-size:1.1em;">One Photographer</strong><br>One photographer throughout the coverage<br><br><strong style="font-size:1.1em;">Same Day Previews</strong><br>Previews delivered before midnight.<br><br><strong style="font-size:1.1em;">High Res &amp; Web Size Images</strong><br>Between 30\u201360 photos delivered per hour hired<br><br><strong style="font-size:1.1em;">Online Gallery</strong><br>(Included 2 years of cloud storage)<br><br><strong style="font-size:1.1em;">Consultation Meetings</strong><br>(Timeline &amp; creative planning meetings with me)<br><br><span style="display:block;margin-top:8px;font-size:42px;font-family:\'Instrument Serif\';line-height:1.1;">\u00a3160.00/hour</span></p></div></div></div></div>'

content = content[:start] + new_block + content[end:]

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('done')
