import re

new_desc_it = "Un'avventura al tramonto per esplorare e scoprire la magia delle rovine di Aquinum. L'esperienza base include l'accompagnamento nell'area. Su richiesta, è possibile arricchire la serata prenotando separatamente una visita con la nostra Guida Storica partner (costo extra) o un'esclusiva esperienza con musica dal vivo."
new_desc_en = "A sunset adventure to explore and discover the magic of the Aquinum ruins. The base experience includes tour leader assistance. Upon request, you can enhance the evening by separately booking a tour with our Official Guide partner (extra cost) or an exclusive live music experience."

def fix_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Scrub out the short description in index.html and the tour page.
    content = re.sub(r'Vivi la magia delle rovine di Aquinum al tramonto\.[^<]+', new_desc_it, content)
    content = re.sub(r'Experience the magic of the Aquinum ruins at sunset\.[^<]+', new_desc_en, content)

    if 'program-list' in content:
        prog_it = """<ul class="program-list">
        <li>Arrivo al tramonto alle rovine</li>
        <li>Passeggiata esplorativa e scoperta del sito</li>
        <li>Esperienza musicale (opzionale su prenotazione)</li>
        <li>Visita con Guida Ufficiale (opzionale su prenotazione, costo extra)</li>
        <li>Conclusione del servizio di accompagnamento</li>
      </ul>"""
      
        prog_en = """<ul class="program-list" data-lang="en" style="display:none;">
        <li>Arrival at the ruins at sunset</li>
        <li>Exploratory walk and discovery of the site</li>
        <li>Musical experience (optional upon reservation)</li>
        <li>Tour with Official Guide (optional upon reservation, extra cost)</li>
        <li>End of tour leader service</li>
      </ul>"""
        
        # Replace the single ul block for Italian
        content = re.sub(r'<ul class="program-list">.*?</ul>', prog_it, content, count=1, flags=re.DOTALL)
        # Replace the single ul block for English
        content = re.sub(r'<ul class="program-list" data-lang="en"[^>]*>.*?</ul>', prog_en, content, count=1, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def fix_tours_md():
    with open('tours.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the paragraph in tours.md
    content = re.sub(r'Vivi la magia delle rovine di Aquinum al tramonto\.[^\n]+', new_desc_it, content)
    
    # Also fix the program items in tours.md since it has the old items
    content = content.replace("Esplorazione approfondita della via Latina", "Passeggiata esplorativa e scoperta del sito")
    content = content.replace("Passeggiata tra i resti antichi in notturna", "Esperienza musicale / Visita con Guida Ufficiale (su prenotazione)")
    
    with open('tours.md', 'w', encoding='utf-8') as f:
        f.write(content)

fix_html('index.html')
fix_html('tour-aperitivo-aquino.html')
fix_tours_md()

print("Aquino Evening Tour texts updated successfully.")
