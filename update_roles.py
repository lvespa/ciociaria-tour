import glob
import os

def update_role_and_cooking():
    replacements = {
        # Cooking class HTML fixes
        "Assistenza in Fattoria — Laboratorio Locale": "Cooking Class — Pasta Fresca d'Uovo",
        "Farm Experience Assistance — Local Workshop": "Cooking Class — Fresh Egg Pasta",
        
        "Servizio di accompagnamento e interpretariato per le tue esperienze in fattoria. N.B: L'offerta copre esclusivamente il compenso per il servizio di guida.":
        "Esperienza in un autentico pastificio e ristorante locale: assisterai alla produzione e creerai tu stesso la pasta fresca all'uovo. Servizio di accompagnamento turistico.",
        
        "Guiding and interpreting services during your farm experiences. Note: The offer exclusively covers the tour leader service fee.":
        "Experience in an authentic pasta factory and local restaurant: watch the production and make fresh egg pasta yourself. Tour leader service included.",

        "Assistenza linguistica e logistica<": "Incontro al pastificio artigianale<",
        "Linguistic and logistical assistance<": "Meeting at the artisan pasta factory<",
        "Supporto per la traduzione del laboratorio<": "Creazione della pasta fresca all'uovo<",
        "Translation support during the workshop<": "Making fresh egg pasta<",
        
        # Guida -> Accompagnatrice replacements in general (careful with exact strings)
        "Servizio di guida e accompagnamento": "Servizio di accompagnamento",
        "Servizio esclusivo di visita guidata": "Servizio esclusivo di accompagnamento turistico",
        "Servizio di visita guidata privata": "Servizio di accompagnamento privato",
        "Private guided tour service": "Private tour leader service",
        "Exclusive tour guide service": "Exclusive tour leader service",
        "Certified tour guide service": "Certified tour leader service",
        "Servizio di guida": "Servizio di accompagnamento turistico",
        "Guided cycling service": "Cycling tour leader service",
        "guida cicloturistica": "accompagnatore turistico",
        "la nostra guida storica": "il nostro tour leader",
        "a historical guide": "a tour leader",
        "con guida storica WWII a piedi": "con accompagnatore turistico esperto WWII a piedi",
        "WWII historian guide on foot": "WWII expert tour leader on foot",
        "Tour Guide – Luisanna Vespa": "Tour Leader – Luisanna Vespa",
        "guida fotografica naturalistica": "accompagnatore naturalistico",
        "wildlife photography guide": "nature tour leader",
        "Conclusione del tour guidato": "Conclusione del servizio di accompagnamento",
        "End of guided tour": "End of tour leader service",
        "Visita guidata completa": "Visita completa",
        "Complete guided tour": "Complete visit",
        "Visita guidata breve": "Visita breve",
        "Short guided tour": "Short visit",
        "Trekking guidato": "Trekking in compagnia",
        "Guided hike": "Hike with tour leader",
        
    }

    files = glob.glob("tour-*.html") + ["index.html"]
    
    for fpath in files:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        for old, new in replacements.items():
            content = content.replace(old, new)
            
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print("Role and Cooking Class updates completed.")

if __name__ == '__main__':
    update_role_and_cooking()
