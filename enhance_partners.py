import sys
import re

css_inject = '''
    /* ─── PARTNERS ──────────────────────────────────── */
    .partners-section {
      background: var(--cream);
      padding: 90px 24px;
    }
    .partners-grid {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 30px;
      margin-bottom: 30px;
    }
    .partner-card {
      background: #fff;
      padding: 40px 30px;
      border-radius: 18px;
      width: 300px;
      text-align: center;
      box-shadow: 0 10px 30px rgba(0,0,0,0.05);
      transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      cursor: default;
      position: relative;
      overflow: hidden;
    }
    .partner-card::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 4px;
      background: var(--gold);
      transform: scaleX(0);
      transition: transform 0.4s ease;
      transform-origin: left;
    }
    .partner-card:hover {
      transform: translateY(-12px);
      box-shadow: 0 20px 40px rgba(0,0,0,0.12);
    }
    .partner-card:hover::before {
      transform: scaleX(1);
    }
    .partner-icon {
      font-size: 3.5rem;
      margin-bottom: 20px;
      display: inline-block;
      transition: transform 0.4s ease;
    }
    .partner-card:hover .partner-icon {
      transform: scale(1.15) rotate(5deg);
    }
    .partner-title {
      margin: 10px 0;
      display: block;
      font-size: 1.35rem;
      font-family: 'Cormorant Garamond', serif;
      color: var(--dark);
      font-weight: 700;
    }
    .partner-desc {
      font-size: 0.95rem;
      color: var(--muted);
      line-height: 1.6;
    }
    .partner-special {
      border: 1px solid rgba(201, 168, 76, 0.4);
      background: linear-gradient(to bottom, #fff, #faf6ef);
    }
'''

new_partners_html = '''  <!-- ══ PARTNERS ═══════════════════════════════════════ -->
  <section class="partners-section" id="partners">
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
      
      <div class="partners-grid">
         
         <!-- Partner 1 -->
         <div class="partner-card">
            <div class="partner-icon">🚲</div>
            <span class="partner-title">GoAout Pontecorvo</span>
            <span class="partner-desc">
              <span data-lang="it">Noleggio e-bike e mountain bike di alta qualità per le tue avventure.</span>
              <span data-lang="en">High quality e-bike and mountain bike rental for your adventures.</span>
            </span>
         </div>
         
         <!-- Partner 2 -->
         <div class="partner-card">
            <div class="partner-icon">🏨</div>
            <span class="partner-title">Hotel della Pace, Cassino</span>
            <span class="partner-desc">
              <span data-lang="it">Ospitalità e comfort nel cuore di Cassino, base perfetta per i tuoi tour.</span>
              <span data-lang="en">Hospitality and comfort in the heart of Cassino, perfect base for your tours.</span>
            </span>
         </div>
         
         <!-- Partner 3 -->
         <div class="partner-card partner-special">
            <div class="partner-icon">🏛️</div>
            <span class="partner-title">
              <span data-lang="it">Guida Ufficiale</span><span data-lang="en">Official Guide</span>
            </span>
            <span class="partner-desc">
              <span data-lang="it">Hai bisogno di una guida ufficiale? Contatta la nostra guida partner per riservare le tue esperienze guidate.</span>
              <span data-lang="en">Need an official guide? Contact our official guide partner to book your guided experiences.</span>
            </span>
         </div>

         <!-- Partner 4: Assicurazione -->
         <div class="partner-card partner-special">
            <div class="partner-icon">🛡️</div>
            <span class="partner-title">
              <span data-lang="it">Assicurazione Infortuni</span><span data-lang="en">Accident Insurance</span>
            </span>
            <span class="partner-desc">
              <span data-lang="it">Viaggia in totale serenità. Con una piccola quota extra puoi richiedere l'attivazione di una polizza infortuni dedicata per ogni partecipante.</span>
              <span data-lang="en">Travel with total peace of mind. For a small extra fee, you can request an accident insurance policy for each participant.</span>
            </span>
         </div>
         
      </div>
    </div>
  </section>'''

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the existing Partners section using regex
pattern = re.compile(r'<!-- ══ PARTNERS ═══════════════════════════════════════ -->.*?</section>', re.DOTALL)
if pattern.search(content):
    content = pattern.sub(new_partners_html, content)
else:
    print("Could not find the old partners section. Exiting.")
    sys.exit(1)

# Inject CSS
if "/* ─── PARTNERS" not in content:
    content = content.replace('</style>', css_inject + '\\n  </style>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Enhanced partners section injected successfully.")
