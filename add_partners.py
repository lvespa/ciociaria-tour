import sys
import re

partners_html = '''
  <!-- ══ PARTNERS ═══════════════════════════════════════ -->
  <section class="partners" id="partners" style="background:var(--cream); padding:90px 24px;">
    <div class="section-inner" style="text-align:center;">
      <p class="section-label">
        <span data-lang="it">I Miei Consigli</span>
        <span data-lang="en">My Recommendations</span>
      </p>
      <h2 class="section-title">
        <span data-lang="it">Partner Locali & Affiliazioni</span>
        <span data-lang="en">Local Partners & Affiliations</span>
      </h2>
      <p class="section-desc" style="margin: 0 auto 50px; max-width:700px;">
        <span data-lang="it">Una rete di professionisti e strutture fidate per rendere il tuo soggiorno in Ciociaria perfetto sotto ogni punto di vista.</span>
        <span data-lang="en">A network of trusted professionals and facilities to make your stay in Ciociaria perfect in every way.</span>
      </p>
      
      <div style="display:flex; flex-wrap:wrap; justify-content:center; gap:30px; margin-bottom:20px;">
         
         <!-- Partner 1 -->
         <div style="background:#fff; padding:40px 30px; border-radius:18px; width:300px; text-align:center; box-shadow:0 10px 30px rgba(0,0,0,0.05); transition:transform 0.3s;">
            <div style="font-size:3rem; margin-bottom:20px;">🚲</div>
            <strong style="margin:10px 0; display:block; font-size:1.25rem; font-family:'Cormorant Garamond', serif; color:var(--dark);">GoAout Pontecorvo</strong>
            <span style="font-size:0.9rem; color:var(--muted);"><span data-lang="it">Noleggio e-bike e mountain bike di alta qualità per le tue avventure.</span><span data-lang="en">High quality e-bike and mountain bike rental for your adventures.</span></span>
         </div>
         
         <!-- Partner 2 -->
         <div style="background:#fff; padding:40px 30px; border-radius:18px; width:300px; text-align:center; box-shadow:0 10px 30px rgba(0,0,0,0.05); transition:transform 0.3s;">
            <div style="font-size:3rem; margin-bottom:20px;">🏨</div>
            <strong style="margin:10px 0; display:block; font-size:1.25rem; font-family:'Cormorant Garamond', serif; color:var(--dark);">Hotel della Pace, Cassino</strong>
            <span style="font-size:0.9rem; color:var(--muted);"><span data-lang="it">Ospitalità e comfort nel cuore di Cassino, base perfetta per i tuoi tour.</span><span data-lang="en">Hospitality and comfort in the heart of Cassino, perfect base for your tours.</span></span>
         </div>
         
         <!-- Partner 3 -->
         <div style="background:#fff; padding:40px 30px; border-radius:18px; width:300px; text-align:center; box-shadow:0 10px 30px rgba(0,0,0,0.05); transition:transform 0.3s; border:2px solid var(--gold-lt);">
            <div style="font-size:3rem; margin-bottom:20px;">🏛️</div>
            <strong style="margin:10px 0; display:block; font-size:1.25rem; font-family:'Cormorant Garamond', serif; color:var(--dark);">
              <span data-lang="it">Guida Ufficiale</span><span data-lang="en">Official Guide</span>
            </strong>
            <span style="font-size:0.9rem; color:var(--muted);"><span data-lang="it">Hai bisogno di una guida ufficiale? Contatta la nostra guida ufficiale partner per riservare le tue esperienze guidate.</span><span data-lang="en">Need an official guide? Contact our official guide partner to book your guided experiences.</span></span>
         </div>
         
      </div>
    </div>
  </section>

  <!-- ══ CONTACT STRIP ══════════════════════════════════ -->
'''

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

if "<!-- ══ PARTNERS ═══════════════════════════════════════ -->" not in content:
    content = content.replace("<!-- ══ CONTACT STRIP ══════════════════════════════════ -->", partners_html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Partners section added to index.html")
else:
    print("Partners section already exists.")
