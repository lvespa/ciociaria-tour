import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

insurance_html = '''
         <!-- Partner 4: Assicurazione -->
         <div style="background:#fff; padding:40px 30px; border-radius:18px; width:300px; text-align:center; box-shadow:0 10px 30px rgba(0,0,0,0.05); transition:transform 0.3s; border:2px solid rgba(201, 168, 76, 0.4);">
            <div style="font-size:3rem; margin-bottom:20px;">🛡️</div>
            <strong style="margin:10px 0; display:block; font-size:1.25rem; font-family:'Cormorant Garamond', serif; color:var(--dark);">
              <span data-lang="it">Assicurazione Infortuni</span><span data-lang="en">Accident Insurance</span>
            </strong>
            <span style="font-size:0.9rem; color:var(--muted);"><span data-lang="it">Viaggia in totale serenità. Con una piccola quota extra puoi richiedere l'attivazione di una polizza infortuni dedicata per ogni partecipante.</span><span data-lang="en">Travel with total peace of mind. For a small extra fee, you can request an accident insurance policy for each participant.</span></span>
         </div>'''

target = """         <!-- Partner 3 -->
         <div style="background:#fff; padding:40px 30px; border-radius:18px; width:300px; text-align:center; box-shadow:0 10px 30px rgba(0,0,0,0.05); transition:transform 0.3s; border:2px solid var(--gold-lt);">
            <div style="font-size:3rem; margin-bottom:20px;">🏛️</div>
            <strong style="margin:10px 0; display:block; font-size:1.25rem; font-family:'Cormorant Garamond', serif; color:var(--dark);">
              <span data-lang="it">Guida Ufficiale</span><span data-lang="en">Official Guide</span>
            </strong>
            <span style="font-size:0.9rem; color:var(--muted);"><span data-lang="it">Hai bisogno di una guida ufficiale? Contatta la nostra guida ufficiale partner per riservare le tue esperienze guidate.</span><span data-lang="en">Need an official guide? Contact our official guide partner to book your guided experiences.</span></span>
         </div>"""

if target in content and "Assicurazione Infortuni" not in content:
    content = content.replace(target, target + "\\n" + insurance_html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Insurance section added successfully.")
else:
    print("Could not find Target or Insurance section already exists.")
