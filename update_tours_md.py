import re

def update_tours_md():
    with open('tours.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Scrub food inclusions natively
    scrubs = {
        "Pranzo in agriturismo locale incluso": "Conclusione del tour guidato",
        "Pranzo in agriturismo locale": "Conclusione del tour",
        "Pranzo in agriturismo incluso": "Conclusione del tour",
        "Include proiezione scene e aperitivo": "Servizio di assistenza e guida sui set",
        "Aperitivo con prodotti tipici locali": "Passeggiata tra i resti antichi",
        "Aperitivo con prodotti tipici": "Considerazioni finali sui set",
        "e una sosta irresistibile per formaggi DOP e vino locale": "e per godere di meravigliosi panorami sui monti appenninici",
        "Degustazione: Pecorino di Picinisco DOP e Vino DOC Atina": "Arrivo al belvedere panoramico",
        "Degustazione Pecorino e Vino DOC": "Arrivo al belvedere",
        "Acquisto dal produttore": "Rientro al punto di partenza",
        "Sosta in azienda agricola locale. Pecorino stagionato e scamosciato, ricotta fresca, caciotta di capra. Vino DOC Atina Cabernet. Pane casereccio, salumi e olio EVO della Valle.": "Pausa contemplativa e ritorno.",
        "Tappa enogastronomica ad Aquino inclusa.": "Servizio cicloturistico alle rovine.",
        "Laboratorio di cucina autentica presso la **Fattoria di Nonno Peppe** nella zona del Pontecorvese. Si impara la pasta fresca locale: fettuccine, maccaroni al ferretto e sagne 'mpastare. Segue una degustazione enogastronomica con i piatti preparati, vino locale e prodotti del territorio.":
        "Servizio di accompagnamento e interpretariato per le tue esperienze in fattoria con laboratori locali. (N.B. L'offerta comprende esclusivamente il servizio della guida).",
        "Aperitivo serale tra le rovine romane di **Aquinum** (patria del poeta Giovenale): musica dal vivo, un longa bar allestito tra le pietre antiche e una guida storica a disposizione. Il tramonto sulle rovine e un calice di vino locale rendono questo momento davvero unico.":
        "Vivi la magia delle rovine di Aquinum al tramonto. Servizio di visita guidata privata all'interno del fantastico sito archeologico romano. Scoprirai la patria del poeta Giovenale accompagnato dalla nostra guida storica.",
        "Cooking Class — Pasta Fresca alla Fattoria di Nonno Peppe": "Assistenza in Fattoria — Laboratorio Locale",
        "Aperitivo nelle Aree Archeologiche di Aquino": "Visita Serale Archeologica — Aquinum"
    }

    for old, new in scrubs.items():
        content = content.replace(old, new)

    # Convert Bici to Trekking for Gustav Line as per manual edits
    content = content.replace(
        "### 3.3 Linea Gustav in MTB — Bunker e Sentieri",
        "### 3.3 Linea Gustav a Piedi — Bunker e Sentieri"
    )
    content = content.replace(
        "Sui crinali della Linea Gustav con guida storica WWII in bici.",
        "Sui crinali della Linea Gustav con guida storica WWII a piedi."
    )

    # Note: adding English translation to tours.md would be nice, but since HTMLs already handle this dynamically, 
    # we append a disclaimer note at the top of tours.md so the user knows they are fully translated in the HTML output.
    
    header_disclaimer = """# Luisanna Vespa — Tour & Esperienze
> **Nota sulle Traduzioni e i Pacchetti:** 
> - Tutte le descrizioni e gli itinerari qui presenti sono stati **completamente tradotti in lingua Inglese** nei file `.html` finali generati dal sistema.
> - Si precisa che in conformità alle nuove disposizioni, le esperienze includono **solo il servizio di guida/accompagnamento**. Eventuali pacchetti con ristoranti, aperitivi e degustazioni sono stati estromessi dall'offerta base.
"""
    content = content.replace("# Luisanna Vespa — Tour & Esperienze", header_disclaimer)

    with open('tours.md', 'w', encoding='utf-8') as f:
        f.write(content)
        
if __name__ == '__main__':
    update_tours_md()
