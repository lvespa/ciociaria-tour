import sys
import re
from build_pages import tours_data

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

filter_html = '''
      <div class="filter-bar">
        <button class="filter-btn active" data-filter="all">
          <span data-lang="it">Tutti</span><span data-lang="en">All</span>
        </button>
        <button class="filter-btn" data-filter="culturali">
          <span data-lang="it">Culturali</span><span data-lang="en">Cultural</span>
        </button>
        <button class="filter-btn" data-filter="trekking">
          Trekking
        </button>
        <button class="filter-btn" data-filter="bici">
          <span data-lang="it">Bici</span><span data-lang="en">Bike</span>
        </button>
        <button class="filter-btn" data-filter="esperienze">
          <span data-lang="it">Esperienze</span><span data-lang="en">Experiences</span>
        </button>
        <button class="filter-btn" data-filter="cammini">
          <span data-lang="it">Cammini</span><span data-lang="en">Walks</span>
        </button>
      </div>
'''

cards_html = ""
for tour in tours_data:
    cards_html += f'''
        <a href="tour-{tour['id']}.html" class="tour-card" data-filter="{tour['category_class']}" style="text-decoration:none; display:block; color:inherit;">
          <img src="{tour['image']}" class="tour-card-img" alt="{tour['title_it']}" />
          <div class="tour-card-body">
            <h3 style="margin-top:10px; font-size:1.3rem;">
              <span data-lang="it">{tour['title_it']}</span>
              <span data-lang="en">{tour['title_en']}</span>
            </h3>
            <p style="margin-bottom:15px; font-size:0.9rem;">
              <span data-lang="it">{tour['desc_it'][:110]}...</span>
              <span data-lang="en">{tour['desc_en'][:110]}...</span>
            </p>
            <div class="tour-tag">
              <span data-lang="it">Scopri di più ➔</span>
              <span data-lang="en">Learn more ➔</span>
            </div>
          </div>
        </a>
'''

tours_section = f'''
  <!-- ══ TOURS ══════════════════════════════════════════ -->
  <section class="tours" id="tours">
    <div class="section-inner">
      <div class="tours-header">
        <p class="section-label">
          <span data-lang="it">Le Mie Esperienze</span>
          <span data-lang="en">My Experiences</span>
        </p>
        <h2 class="section-title">
          <span data-lang="it">Scopri il territorio passo dopo passo</span>
          <span data-lang="en">Discover the region step by step</span>
        </h2>
        <p class="section-desc">
          <span data-lang="it">Seleziona la categoria per esplorare i tour.</span>
          <span data-lang="en">Select a category to explore the tours.</span>
        </p>
      </div>
      {filter_html}
      <div class="tours-grid" id="tours-grid-container">
        {cards_html}
      </div>
    </div>
  </section>

  <!-- ══ TRAVEL DESIGN ══════════════════════════════════ -->
  <section class="travel-design" id="travel-design" style="background:#fff; padding:90px 24px;">
    <div class="section-inner" style="text-align:center;">
      <p class="section-label">
        <span data-lang="it">Travel Design</span>
        <span data-lang="en">Travel Design</span>
      </p>
      <h2 class="section-title">
        <span data-lang="it">Crea il Tuo Tour su Misura</span>
        <span data-lang="en">Create Your Tailored Tour</span>
      </h2>
      <p class="section-desc" style="margin: 0 auto 40px; max-width:700px;">
        <span data-lang="it">Raccontami di te, dei tuoi interessi e dei tuoi compagni di viaggio. Progetterò un itinerario unico, studiato appositamente per le tue esigenze, senza alcun impegno.</span>
        <span data-lang="en">Tell me about yourself, your interests, and your travel companions. I will design a unique itinerary, specifically tailored to your needs, with no obligation.</span>
      </p>
      <img src="06_travel-design/travel-design-itinerario-su-misura.jpg" alt="Travel Design" style="width:100%; max-width:900px; border-radius:18px; margin-bottom:50px; object-fit:cover; height:400px; box-shadow:0 20px 50px rgba(0,0,0,0.15);" />
      
      <div style="display:flex; flex-wrap:wrap; justify-content:center; gap:24px; margin-bottom:50px;">
         <div style="background:var(--cream); padding:30px; border-radius:16px; width:240px; text-align:left; box-shadow:0 4px 15px rgba(0,0,0,0.03);">
            <b style="color:var(--gold); font-size:1.5rem; font-family:'Cormorant Garamond', serif;">01</b><br>
            <strong style="margin:10px 0; display:block; font-size:1.1rem; color:var(--dark);"><span data-lang="it">Raccontami di te</span><span data-lang="en">Tell me about you</span></strong>
            <span style="font-size:0.85rem; color:var(--muted);"><span data-lang="it">Scrivi via email: chi sei, cosa ti interessa e quanto tempo hai.</span><span data-lang="en">Write via email: who you are, interests and time available.</span></span>
         </div>
         <div style="background:var(--cream); padding:30px; border-radius:16px; width:240px; text-align:left; box-shadow:0 4px 15px rgba(0,0,0,0.03);">
            <b style="color:var(--gold); font-size:1.5rem; font-family:'Cormorant Garamond', serif;">02</b><br>
            <strong style="margin:10px 0; display:block; font-size:1.1rem; color:var(--dark);"><span data-lang="it">Progetto il tour</span><span data-lang="en">I design the tour</span></strong>
            <span style="font-size:0.85rem; color:var(--muted);"><span data-lang="it">Ricevi una proposta personalizzata con tappe ed esperienze.</span><span data-lang="en">Receive a custom proposal with spots and experiences.</span></span>
         </div>
         <div style="background:var(--cream); padding:30px; border-radius:16px; width:240px; text-align:left; box-shadow:0 4px 15px rgba(0,0,0,0.03);">
            <b style="color:var(--gold); font-size:1.5rem; font-family:'Cormorant Garamond', serif;">03</b><br>
            <strong style="margin:10px 0; display:block; font-size:1.1rem; color:var(--dark);"><span data-lang="it">Raffiniamo insieme</span><span data-lang="en">We refine together</span></strong>
            <span style="font-size:0.85rem; color:var(--muted);"><span data-lang="it">Ci confrontiamo e aggiustiamo i dettagli finché non è perfetto.</span><span data-lang="en">We talk and adjust details until it's perfect.</span></span>
         </div>
         <div style="background:var(--cream); padding:30px; border-radius:16px; width:240px; text-align:left; box-shadow:0 4px 15px rgba(0,0,0,0.03);">
            <b style="color:var(--gold); font-size:1.5rem; font-family:'Cormorant Garamond', serif;">04</b><br>
            <strong style="margin:10px 0; display:block; font-size:1.1rem; color:var(--dark);"><span data-lang="it">Parti e vivi</span><span data-lang="en">Go and experience</span></strong>
            <span style="font-size:0.85rem; color:var(--muted);"><span data-lang="it">Il giorno del tour Luisanna è con te, passo dopo passo.</span><span data-lang="en">On tour day, Luisanna is with you, step by step.</span></span>
         </div>
      </div>
      
      <a href="https://wa.me/393489128901" style="display:inline-flex; align-items:center; gap:10px; background:#25D366; color:#fff; padding:18px 40px; border-radius:50px; text-decoration:none; font-weight:700; font-size:0.95rem; text-transform:uppercase; letter-spacing:0.05em; transition:0.3s; box-shadow:0 8px 24px rgba(37,211,102,0.3);">
         <span data-lang="it">Contattami su WhatsApp</span><span data-lang="en">Contact me on WhatsApp</span>
      </a>
    </div>
  </section>
'''

pattern = re.compile(r'<!-- ══ TOURS ══════════════════════════════════════════ -->(.*?)<!-- ══ HIGHLIGHTS ═════════════════════════════════════ -->', re.DOTALL)
html = pattern.sub(tours_section + '\\n  <!-- ══ HIGHLIGHTS ═════════════════════════════════════ -->', html)

css_inject = '''
    /* ─── FILTER BAR ────────────────────────────────── */
    .filter-bar {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 12px;
      margin-bottom: 50px;
    }
    .filter-btn {
      background: transparent;
      border: 1px solid rgba(201, 168, 76, 0.4);
      color: var(--muted);
      padding: 10px 24px;
      border-radius: 30px;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.3s ease;
      outline: none;
      font-family: 'Inter', sans-serif;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }
    .filter-btn.active, .filter-btn:hover {
      background: var(--gold);
      color: var(--dark);
      border-color: var(--gold);
    }
    .tour-card {
      transition: opacity 0.4s ease, transform 0.4s ease, box-shadow 0.4s ease;
    }
'''
if "/* ─── FILTER BAR" not in html:
    html = html.replace('</style>', css_inject + '\\n  </style>')

js_inject = '''
    // Filter logic
    document.querySelectorAll('.filter-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const filter = btn.getAttribute('data-filter');
        document.querySelectorAll('.tour-card').forEach(card => {
          if (filter === 'all' || card.getAttribute('data-filter') === filter) {
             card.style.display = 'block';
             setTimeout(() => { card.style.opacity = '1'; card.style.transform = 'translateY(0)'; }, 50);
          } else {
             card.style.opacity = '0';
             card.style.transform = 'translateY(10px)';
             setTimeout(() => card.style.display = 'none', 400);
          }
        });
      });
    });
'''
if "// Filter logic" not in html:
    html = html.replace('</script>', js_inject + '\\n  </script>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("index.html updated successfully!")
