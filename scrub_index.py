import os
import re
import glob

# Step 1. Define the replacement mappings for index.html
replacements = {
    # Battaglia di Cassino
    "Il tour più completo sulla Seconda Guerra Mondiale in Italia. Dall'Historiale di Cassino all'Abbazia di Montecassino, passando per i cimiteri militari (polacco, Commonwealth, americano), Hill 593 e le rovine di San Pietro Infine...":
    "Il tour più completo sulla Seconda Guerra Mondiale in Italia. Dall'Historiale all'Abbazia, passando per i cimiteri militari... (Servizio esclusivo di accompagnamento)",
    
    "The most comprehensive WWII tour in Italy. From the Cassino Historiale to the Montecassino Abbey, through the military cemeteries (Polish, Commonwealth, American), Hill 593, and the ruins of San Pietro Infine...":
    "The most comprehensive WWII tour in Italy. From the Cassino Historiale to the Montecassino Abbey, through the military cemeteries... (Exclusive tour guide service)",

    # Ciociaria Cinema
    "Case natali di Nino Manfredi e Marcello Mastroianni, i paesaggi del film 'La Ciociara' di Vittorio De Sica con Sophia Loren. Include proiezione scene e aperitivo...":
    "Case natali di Nino Manfredi e Marcello Mastroianni, i paesaggi del film 'La Ciociara'. Servizio di assistenza e guida accreditata sui set...",
    
    "Birthplaces of Nino Manfredi and Marcello Mastroianni, the landscapes of Vittorio De Sica's film 'Two Women' starring Sophia Loren. Includes scene projection and aperitivo...":
    "Birthplaces of Nino Manfredi and Marcello Mastroianni, the landscapes of Vittorio De Sica's film 'Two Women'. Certified tour guide service...",

    # Picinisco Trekking
    "Un percorso a piedi tra natura selvaggia, il borgo medievale di Picinisco e una sosta irresistibile per formaggi DOP e vino locale. Adatto a famiglie...":
    "Un percorso a piedi in compagnia della vostra guida tra natura selvaggia e il borgo medievale di Picinisco. Adatto a famiglie...",
    
    "A walking route through wild nature, the medieval village of Picinisco, and an irresistible stop for PDO cheeses and local wine. Family friendly...":
    "A guided walking route through wild nature and the medieval village of Picinisco. Family friendly experience...",

    # Via Latina
    "Via Latina romana tra Aquinum, Casinum e l'anfiteatro romano. Pianeggiante, adatto a famiglie. Tappa enogastronomica ad Aquino inclusa...":
    "Via Latina romana tra Aquinum, Casinum e l'anfiteatro romano. Pianeggiante, adatto a famiglie. Servizio di guida...",
    
    "Roman Via Latina between Aquinum, Casinum, and the Roman amphitheatre. Flat, family-friendly. Food & wine stop in Aquino included...":
    "Roman Via Latina between Aquinum, Casinum, and the Roman amphitheatre. Flat, family-friendly. Guided cycling service...",

    # Cooking Class Card Updates
    "Cooking Class — Pasta Fresca alla Fattoria": "Assistenza in Fattoria — Laboratorio Locale",
    "Cooking Class — Fresh Pasta at the Farm": "Farm Experience Assistance — Local Workshop",
    "Laboratorio di cucina genuina alla Fattoria di Nonno Peppe. Si impara la pasta fresca locale e segue degustazione coi piatti preparati e vino del territorio...":
    "Servizio di accompagnamento e interpretariato per le tue esperienze in fattoria. N.B: L'offerta copre esclusivamente il compenso per il servizio di guida...",
    "Authentic cooking workshop at Nonno Peppe's Farm. Learn local fresh pasta making, followed by a tasting of your dishes with local wine...":
    "Guiding and interpreting services during your authentic farm experiences. Note: The offer exclusively covers the tour leader service fee...",

    # Aperitivo Aquino Card Updates
    "Aperitivo nelle Aree Archeologiche di Aquino": "Visita Serale Archeologica — Aquinum",
    "Aperitivo in the Archaeological Areas of Aquino": "Evening Tour — Archaeological Areas of Aquino",
    "Aperitivo serale tra le rovine di Aquinum. Un longa bar tra le pietre antiche, musica live e guida storica. Il tramonto sulle rovine è magico...":
    "Vivi la magia delle rovine di Aquinum al tramonto. Servizio di visita guidata privata all'interno del fantastico sito archeologico romano...",
    "Evening aperitivo among the ruins of Aquinum. A long bar set among ancient stones, live music, and a historical guide. The sunset over the ruins is magical...":
    "Experience the magic of the Aquinum ruins at sunset. Private guided tour service directly within the ancient Roman archaeological site..."
}

def clean_index_html():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        for old, new in replacements.items():
            if old in content:
                content = content.replace(old, new)
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Scrubbed index.html successfully.")
    except Exception as e:
        print(f"Error on index.html: {e}")

# Call the clean function
clean_index_html()
