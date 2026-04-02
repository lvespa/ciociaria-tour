import os
import glob

replacements = {
    # Battaglia di Cassino
    "e le rovine di San Pietro Infine.</span": "e le rovine di San Pietro Infine. Servizio esclusivo di accompagnamento.</span",
    "the ruins of San Pietro Infine.</span": "the ruins of San Pietro Infine. Exclusive tour guide service.</span",
    "Pranzo in agriturismo locale<": "Conclusione del tour guidato<",
    "Pranzo in agriturismo incluso<": "Conclusione del tour guidato<",
    "Lunch in a local farmhouse included<": "End of guided tour<",
    "Lunch in local farmhouse<": "End of guided tour<",

    # Ciociaria Cinema
    "Include proiezione scene e aperitivo.</span": "Servizio di puro accompagnamento turistico professionale.</span",
    "Includes scene projection and aperitivo.</span": "Exclusive professional guiding service on the movie sets.</span",
    "Aperitivo con prodotti tipici<": "Considerazioni finali sui set<",
    "Aperitivo with local products<": "Final remarks on the sets<",

    # Picinisco Trekking
    "e una sosta irresistibile per formaggi DOP e vino locale.": "e per godere di meravigliosi panorami appenninici.",
    "and an irresistible stop for PDO cheeses and local wine.": "and wonderful views over the Apennine mountains.",
    "Degustazione Pecorino e Vino DOC<": "Arrivo al belvedere<",
    "Pecorino and DOC Wine tasting<": "Arrival at the viewpoint<",
    "Acquisto dal produttore<": "Rientro al punto di partenza<",
    "Direct purchase from producer<": "Return to starting point<",

    # Via Latina
    "Tappa enogastronomica ad Aquino inclusa.": "Servizio di esclusivo accompagnamento cicloturistico.",
    "Food & wine stop in Aquino included.": "Exclusive guided cycling service.",
    "Food &amp; wine stop in Aquino included.": "Exclusive guided cycling service.",
    "Sosta Enogastronomica ad Aquino<": "Pausa ristoro<",
    "Food & Wine stop in Aquino<": "Refreshment break<",
    "Food &amp; Wine stop in Aquino<": "Refreshment break<",

    # Cooking Class Card Updates
    "Cooking Class — Pasta Fresca alla Fattoria": "Assistenza in Fattoria — Laboratorio Locale",
    "Cooking Class — Fresh Pasta at the Farm": "Farm Experience Assistance — Local Workshop",
    "Laboratorio di cucina genuina alla Fattoria di Nonno Peppe. Si impara la pasta fresca locale e segue degustazione coi piatti preparati e vino del territorio.":
    "Servizio di accompagnamento e interpretariato per le tue esperienze in fattoria. N.B: L'offerta copre esclusivamente il compenso per il servizio di guida.",
    "Authentic cooking workshop at Nonno Peppe's Farm. Learn local fresh pasta making, followed by a tasting of your dishes with local wine.":
    "Guiding and interpreting services during your farm experiences. Note: The offer exclusively covers the tour leader service fee.",
    
    "Taglio delle fettuccine e maccaroni<": "Assistenza linguistica e logistica<",
    "Cutting fettuccine and maccaroni<": "Linguistic and logistical assistance<",
    "Cottura e preparazione dei sughi<": "Supporto per la traduzione del laboratorio<",
    "Cooking and sauce preparation<": "Translation support during the workshop<",
    "Pranzo conviviale in fattoria<": "Conclusione del servizio di accompagnamento<",
    "Convivial lunch at the farm<": "End of guiding service<",

    # Aperitivo Aquino Card Updates
    "Aperitivo nelle Aree Archeologiche di Aquino": "Visita Serale Archeologica — Aquinum",
    "Aperitivo in the Archaeological Areas of Aquino": "Evening Tour — Archaeological Areas of Aquino",
    "Aperitivo serale tra le rovine di Aquinum. Un longa bar tra le pietre antiche, musica live e guida storica. Il tramonto sulle rovine è magico.":
    "Vivi la magia delle rovine di Aquinum al tramonto. Servizio di visita guidata privata all'interno del fantastico sito archeologico romano.",
    "Evening aperitivo among the ruins of Aquinum. A long bar set among ancient stones, live music, and a historical guide. The sunset over the ruins is magical.":
    "Experience the magic of the Aquinum ruins at sunset. Private guided tour service directly within the ancient Roman archaeological site.",
    
    '">Food</span': '">Focus</span',
    '">Locale</span': '">Storia Antica</span',
    '">Local</span': '">Ancient Roman History</span',
    "Concerto di musica dal vivo<": "Esplorazione approfondita della via Latina<",
    "Live music concert<": "In-depth exploration of the Via Latina<",
    "Aperitivo con prodotti tipici locali<": "Passeggiata tra i resti antichi in notturna<",
    "Aperitivo with local typical products<": "Night walk among ancient remains<",
    "Food &amp; Wine Tour": "Wine Heritage Guided Tour",
    "Tour Enogastronomico": "Tour Enogastronomico (Solo Servizio Guida)",
}

def clean_pages():
    for fpath in glob.glob("tour-*.html"):
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            changes_made = False
            for old, new in replacements.items():
                if old in content:
                    content = content.replace(old, new)
                    changes_made = True
            
            if changes_made:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Scrubbed {fpath} successfully.")
        except Exception as e:
            print(f"Error on {fpath}: {e}")

if __name__ == '__main__':
    clean_pages()
