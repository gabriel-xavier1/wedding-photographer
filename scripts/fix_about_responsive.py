with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The old about block inner content
old = '''<div id="about" data-bid="about" class="sb sib-about sb-ps"><div class="ss-s ss-bg"><div class="sc" style="width:1200px"><a href="about.html" target="_self" class="sie-about_0 se" data-sid="about_0" style="top:713px"><span type="button" aria-label="get to know me" class="se-button st-primary" data-link="{&quot;type&quot;:&quot;page&quot;,&quot;target&quot;:&quot;about&quot;}"><span class="st-m-primary st-d-primary">get to know me</span></span></a><div data-sid="about_1" class="sie-about_1 se"><p class="se-t sie-about_1-text st-m-paragraph st-d-paragraph se-rc">I\u2019m Jacque \u2014 documentary wedding photographer, professional vibe-reader, and unapologetic romantic.<br><br>I believe that after the wedding, what actually matters isn\u2019t the chair covers or the timeline running perfectly.<br><br>It\u2019s the feeling.<br>The way you looked at each other.<br>The way your mum cried.<br>The way your friends reacted during the speeches.<br>My job isn\u2019t to stage your love story.<br>It\u2019s to document it as it really happens \u2014 and make sure you never forget how it felt to be that in love.<br></p></div><div data-sid="about_2" class="sie-about_2 se"><p class="se-t sie-about_2-text st-m-heading st-d-heading se-rc">HI<br>I AM<br></p></div><div data-sid="about_3" class="sie-about_3 se"><div style="width:100%;height:100%;background-image:url(\'https://i.postimg.cc/V5P1f0DJ/Whats-App-Image-2026-02-06-at-17-55-03.jpg\');background-size:cover;background-position:center center;" data-img="about_3" class="se-img se-gr slzy"></div><noscript><img src="https://i.postimg.cc/V5P1f0DJ/Whats-App-Image-2026-02-06-at-17-55-03.jpg" class="se-img" alt="" title="Jacque"/></noscript></div><div data-sid="about_4" class="sie-about_4 se"><div style="width:100%;height:100%" data-img="about_4" class="se-img se-gr slzy"></div><noscript><img src="OuJ9EdyGER0-wwVCOSxA_A/135701/sandra-seitamaa-jxkefdlseg4-unsplash.jpg" class="se-img" alt="" title="sandra-seitamaa-JxKEFDLsEG4-unsplash"/></noscript></div><div data-sid="about_5" class="sie-about_5 se"><p class="se-t sie-about_5-text st-m-title st-d-title se-rc">Jacque.<br></p></div></div></div></div>'''

new = '''<div id="about" data-bid="about" class="sb sib-about sb-ps">
<style>
  .about-responsive-wrapper {
    display: flex;
    flex-direction: row;
    align-items: flex-start;
    justify-content: space-between;
    gap: clamp(32px, 5vw, 80px);
    padding: clamp(48px, 6vw, 96px) clamp(24px, 5vw, 80px);
    max-width: 1200px;
    margin: 0 auto;
    box-sizing: border-box;
  }
  .about-col-text {
    flex: 1 1 45%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 24px;
  }
  .about-col-photo {
    flex: 1 1 45%;
    max-width: 540px;
  }
  .about-col-photo img {
    width: 100%;
    height: auto;
    display: block;
    object-fit: cover;
    border-radius: 4px;
  }
  .about-title {
    font-size: clamp(1.5rem, 3vw, 2.5rem);
    line-height: 1.2;
    margin: 0;
  }
  .about-name {
    font-size: clamp(2.5rem, 6vw, 5rem);
    line-height: 1;
    margin: 0;
  }
  .about-body {
    font-size: clamp(0.875rem, 1.2vw, 1rem);
    line-height: 1.75;
    margin: 0;
  }
  .about-btn-wrap {
    margin-top: auto;
  }
  @media (max-width: 768px) {
    .about-responsive-wrapper {
      flex-direction: column-reverse;
    }
    .about-col-photo {
      max-width: 100%;
      width: 100%;
    }
    .about-col-text {
      flex: 1 1 100%;
    }
  }
</style>
<div class="about-responsive-wrapper">
  <div class="about-col-text">
    <div>
      <p class="about-title se-t st-m-heading st-d-heading">HI<br>I AM</p>
      <p class="about-name se-t st-m-title st-d-title">Jacque.</p>
    </div>
    <p class="about-body se-t st-m-paragraph st-d-paragraph">
      I\u2019m Jacque \u2014 documentary wedding photographer, professional vibe-reader, and unapologetic romantic.<br><br>
      I believe that after the wedding, what actually matters isn\u2019t the chair covers or the timeline running perfectly.<br><br>
      It\u2019s the feeling.<br>
      The way you looked at each other.<br>
      The way your mum cried.<br>
      The way your friends reacted during the speeches.<br>
      My job isn\u2019t to stage your love story.<br>
      It\u2019s to document it as it really happens \u2014 and make sure you never forget how it felt to be that in love.
    </p>
    <div class="about-btn-wrap">
      <a href="about.html" target="_self">
        <span type="button" aria-label="get to know me" class="se-button st-primary">
          <span class="st-m-primary st-d-primary">get to know me</span>
        </span>
      </a>
    </div>
  </div>
  <div class="about-col-photo">
    <img src="https://i.postimg.cc/V5P1f0DJ/Whats-App-Image-2026-02-06-at-17-55-03.jpg" alt="Jacque" title="Jacque" />
  </div>
</div>
</div>'''

if old in content:
    content = content.replace(old, new)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('DONE')
else:
    print('NOT FOUND - trying partial match')
    # Debug: find about block boundaries
    start = content.find('id="about"')
    end = content.find('id="trusted-by"')
    print(f'About block found: {start} to {end}')
    print(repr(content[start:start+100]))
